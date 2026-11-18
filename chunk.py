# Muhammad Ahmad, CMS 542432, BSCS-15-D
"""
chunk.py  (runs LOCALLY)   raw/*.txt  ->  chunks.json + embed_units.json (+ omitted.json, chunk_diagnostics.txt)

IDEA (easy to explain in the viva):
  1. Clean the raw text: drop "=== PAGE n ===" and "Page n of M" lines, drop footnotes at the bottom of
     each page, strip amendment markers like 1[ ... ] and "* * *" (deleted text).
  2. Read the TABLE OF CONTENTS (ToC) -> authoritative list of (number, title).
  3. Find where the BODY starts (the second "1." whose title matches the ToC's first title).
  4. Walk the ToC IN ORDER and find each number in the body, always searching FORWARD from the previous hit.
     (This is why numbers can never go backwards and why schedule-list numbers cannot collide.)
  5. Chunk i = body lines from its start up to the start of chunk i+1. One chunk per article/section.
  6. Sections longer than LONG_LIMIT chars: keep the whole section as the PARENT (for citation / prompt)
     and split into sub-chunks (embed units) by clause/illustration/exception. Search small, return whole.
  7. Print a validation report; log every ToC entry whose body is missing / too short with raw context.

Run:   python chunk.py                    rebuild ALL laws in LAWS  (overwrites chunks.json / embed_units.json)
       python chunk.py ppc peca           rebuild only these laws       (overwrites the output files!)
       python chunk.py newlaw --append    process only `newlaw` and MERGE it into the existing output files;
                                          the other laws are kept untouched (re-running a law replaces just that law)

ADD A NEW LAW = add ONE entry to LAWS below (see the template above it). Put its PDF in pdfs/ (or data/ or next to
this script); if raw/<file> does not exist yet it is extracted from the PDF automatically (needs: pip install pymupdf).
"""
import argparse, json, os, re, sys, random, bisect
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW_DIR = ROOT / "raw"
OUT_CHUNKS = ROOT / "chunks.json"          # parents: one record per article/section (full text)
OUT_UNITS = ROOT / "embed_units.json"      # what we embed (parent itself if short, sub-chunks if long)
OUT_OMITTED = ROOT / "omitted.json"
OUT_DIAG = ROOT / "chunk_diagnostics.txt"  # paste this file's content back to me if something is wrong
PDF_DIRS = [ROOT / "pdfs", ROOT / "data", ROOT]   # where to look for a law's PDF when raw/<file> is missing

# ------------------------------------------------------------------ settings
LONG_LIMIT = 2000        # parent longer than this -> also split into sub-chunks
SUB_TARGET = 1200        # approx size of a sub-chunk
MIN_BODY = 40            # ToC entries whose text is shorter than this get logged
CHUNK_SCHEDULES = False  # True -> also chunk the Constitution schedules as kind="schedule"
STRIP_FOOTNOTES = True   # drop footnote lines at the bottom of each page
SEED = 42
BIG_JUMP_LINES = 400     # warn if the next body match is this many lines past the previous one

# ---- ONE ENTRY PER LAW.  To add a law, copy the template, fill it in, then run:  python chunk.py <key> --append
#   key        short id used everywhere (ids look like "<key>-<number>", e.g. "ppc-302")
#   pdf        PDF file name (searched in pdfs/, data/, project folder) - only used if raw/<file> is missing
#   file       text file in raw/ (written automatically from the PDF if it does not exist yet)
#   name       full law name (stored in every chunk)
#   short      prefix used in citations: "PPC Section 302"            (default: key in upper case)
#   kind       "article" or "section"                                  (what the law's units are called)
#   label      word used in citations                                  (default: "Article" / "Section")
#   numbering  how numbers appear in the BODY text:
#                "plain" -> "12." "12A." "[12A."  (also glued footnote digits "112." and "*12." are handled)
#                "paren" -> as plain, plus lettered inserts written as "(2E) Title"  (PECA 2025 amendments)
#   has_schedules  True if the law has "FIRST SCHEDULE ..." after the articles (body ends there)
#   expected_max   optional: highest number you expect, only used for the sanity line in the report
#   key_fix    optional: {wrong_ToC_number: right_number} for typos in the table of contents
#
# NEW_LAW_TEMPLATE = dict(pdf="Companies_Act.pdf", file="companies.txt", name="Companies Act, 2017",
#                         short="Companies Act", kind="section", numbering="plain", has_schedules=False)
LAWS = {
    "constitution": dict(pdf="Pakistan_Constitution.pdf", file="constitution.txt", name="Constitution of Pakistan, 1973",
                         short="Constitution", kind="article", label="Article", numbering="plain",
                         has_schedules=True, expected_max=280),
    "ppc": dict(pdf="Penal_code.pdf", file="ppc.txt", name="Pakistan Penal Code, 1860", short="PPC",
                kind="section", label="Section", numbering="plain", has_schedules=False, expected_max=511,
                key_fix={"362N": "462N"}),                      # typo in the PPC table of contents
    "peca": dict(pdf="PECA.pdf", file="peca.txt", name="Prevention of Electronic Crimes Act, 2016", short="PECA",
                 kind="section", label="Section", numbering="paren", has_schedules=False, expected_max=55),
}
NUMBERING_STYLES = ("plain", "paren")


def check_config():
    """fill defaults and fail early with a clear message if an entry is incomplete"""
    for key, cfg in LAWS.items():
        for need in ("file", "name", "kind"):
            if not cfg.get(need):
                sys.exit(f"LAWS['{key}'] is missing '{need}'")
        if not re.fullmatch(r"[a-z0-9_]+", key):
            sys.exit(f"LAWS key '{key}' must be lower-case letters/digits/underscore (it is used inside ids)")
        if cfg["kind"] not in ("article", "section"):
            sys.exit(f"LAWS['{key}']: kind must be 'article' or 'section', not {cfg['kind']!r}")
        cfg.setdefault("short", key.upper())
        cfg.setdefault("label", "Article" if cfg["kind"] == "article" else "Section")
        cfg.setdefault("numbering", "plain")
        cfg.setdefault("has_schedules", False)
        cfg.setdefault("key_fix", {})
        cfg.setdefault("expected_max", None)
        if cfg["numbering"] not in NUMBERING_STYLES:
            sys.exit(f"LAWS['{key}']: numbering must be one of {NUMBERING_STYLES}, not {cfg['numbering']!r}")


def ensure_raw(cfg):
    """make sure raw/<file> exists; if not, extract it from the PDF in the same format extractFromPdf.py writes"""
    path = RAW_DIR / cfg["file"]
    if path.exists():
        return path
    pdf = next((d / cfg["pdf"] for d in PDF_DIRS if cfg.get("pdf") and (d / cfg["pdf"]).exists()), None)
    if pdf is None:
        log(f"   MISSING {path} and no PDF {cfg.get('pdf')!r} found in {[str(d) for d in PDF_DIRS]}")
        return None
    try:
        import pymupdf
    except ImportError:
        log(f"   {path.name} missing and PyMuPDF is not installed: pip install pymupdf  (or run extractFromPdf.py)")
        return None
    RAW_DIR.mkdir(exist_ok=True)
    doc = pymupdf.open(pdf)
    parts = [f"=== PAGE {i} ===\n{page.get_text().rstrip()}\n" for i, page in enumerate(doc, start=1)]
    path.write_text("\n".join(parts), encoding="utf-8")
    log(f"   extracted {pdf.name}: {len(doc)} pages -> {path}")
    doc.close()
    return path


# ------------------------------------------------------------------ regexes
PAGE_RE = re.compile(r"^=== PAGE (\d+) ===\s*$")
HDR_RE = re.compile(r"^\s*Page\s+\d+\s+of\s+\d+\s*$", re.I)
# a line that STARTS a numbered entry:  "180. Acting ..."  "225."  "375A. Gang rape"  "[2A. ..."
CAND_RE = re.compile(r"^\[?(\d{1,3}[A-Z]{0,3})\s*\.(?=\s|$|_|[A-Z\"\u201c])")
# footnote digit glued in front of the number:  "11. The Republic" (= footnote 1 + article 1), "1500. Punishment"
GLUE_RE = re.compile(r"^\[?(\d{2,5})([A-Z]{0,3})\s*\.(?=\s|$|_|[A-Z\"\u201c])")


def glue_keys(line):
    """'1500. Punishment' -> ['500', '00'?]: every key obtainable by removing a 1- or 2-digit footnote number"""
    g = GLUE_RE.match(line)
    if not g:
        return []
    d, letters = g.group(1), g.group(2)
    return [d[p:] + letters for p in (1, 2) if 1 <= len(d) - p <= 3]
# footnote line: small number followed by a typical footnote word ("1 Subs. by ...", "2 Ins. by ...")
FN_START = re.compile(
    r"^\s*\d{1,3}\s*[.)]?\s*(?:Subs\b|Substituted\b|Ins\b|Inserted\b|Re-?numbered\b|Rep\b|"
    r"(?:Omitted|Repealed|Deleted|Added|Inserted|Substituted) by\b|Added\b|"
    r"The (?:words?|figures?|commas?|full stop|semi-?colon|colon|brackets?|letters?|marginal|item|entry)\b|"
    r"Clauses?\b|Sub-?clauses?\b|Provisos?\b|Paragraphs?\b|Para\b|See\b|Cf\b|Vide\b|Marginal\b)", re.I)
FN_SEP = re.compile(r"^[_\-\u2013\u2014=]{8,}$")
# chapter / part headings that sit between sections (they would otherwise stick to the previous section's tail)
HEAD_CUT = re.compile(r"^(?:PART|Part|CHAPTER|Chapter)[\s\-\u2013.]*[IVXLCDM\d]+[A-Z]?\b|^Of\s+[A-Z][^.;:]{2,60}$|"
                      r"^[A-Z][A-Z\s,\-\u2013.&']{6,}$|^ANNEX\b|^_{3,}$")
SCHED_RE = re.compile(r"^\s*(?:FIRST|SECOND|THIRD|FOURTH|FIFTH|SIXTH|SEVENTH|EIGHTH|NINTH|TENTH)\s+SCHEDULE\b")
MARK_TOK = re.compile(r"(?<![\w])(\d{1,3})\[|\[|\]")
LOG = []


def log(msg=""):
    print(msg)
    LOG.append(str(msg))


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


# ------------------------------------------------------------------ step 1: read + clean
def read_pages(path):
    pages, cur = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = PAGE_RE.match(line.strip())
        if m:
            cur = [int(m.group(1)), []]
            pages.append(cur)
        elif cur is not None:
            cur[1].append(line.replace("\xa0", " "))
    return pages


def strip_markers(text):
    """Remove amendment markers: '1[the Supreme Court]' -> 'the Supreme Court'; real '[Omitted]' is kept."""
    stack = []

    def rep(m):
        s = m.group(0)
        if s == "[":
            stack.append(False)
            return s
        if s == "]":
            if not stack:
                return ""
            return "" if stack.pop() else s
        stack.append(True)       # footnote-number + '['
        return ""

    text = MARK_TOK.sub(rep, text)
    # footnote numbers glued to a word: "make 2rules as" -> "make rules as"  (not 2A, 1st, 2nd ...)
    text = re.sub(r"(?<=[\s(\"\u201c])\d{1,3}(?!(?:st|nd|rd|th)\b)(?=[a-z]{2,})", "", text)
    text = re.sub(r"(?:\*[ \t]*){3,}", " ", text)          # '* * * * *' = deleted text
    return text


def norm_head(l, cfg):
    """bring odd numbering styles to the canonical 'NUM. Title' form"""
    l = re.sub(r"^\{\s*(?=\d)", "", l)                                           # '{187. ...'
    l = re.sub(r"^\d{0,2}\*+\s*\[?\s*(?=\d)", "", l)                       # '*273. ...'  '4*[294B. ...'
    l = re.sub(r"^(\d{1,3})\s([A-Z])\s*\.(?=\s|$|_)", r"\1\2.", l)             # '462 I. ...' -> '462I.'
    l = re.sub(r"^(\d{1,3}[A-Z]{0,3})\s*,\s+(?=[A-Z])", r"\1. ", l)             # '26A, Punishment' -> '26A. Punishment'
    if cfg.get("numbering") == "paren":
        l = re.sub(r"^\((\d{1,3}[A-Z]{1,3})\)\s*(?=[A-Z])", r"\1. ", l)          # '(2E) Removal' -> '2E. Removal'
    return l


def clean_law(pages, cfg):
    """returns list of (page_no, line) and stats"""
    kept, dropped_fn, hdr = [], [], 0
    for pno, lines in pages:
        n0 = len(lines)
        lines = [l for l in lines if not HDR_RE.match(l)]
        hdr += n0 - len(lines)
        cut = len(lines)
        if STRIP_FOOTNOTES:
            for i, l in enumerate(lines):
                if i >= 0.25 * len(lines) and (FN_START.match(l) or FN_SEP.match(l.strip())):
                    cut = i
                    break
        dropped_fn += lines[cut:]
        kept += [(pno, l) for l in lines[:cut]]
    joined = "\n".join(l for _, l in kept)
    cleaned = strip_markers(joined).split("\n")
    assert len(cleaned) == len(kept)
    out = []
    for (p, _), l in zip(kept, cleaned):
        l = norm_head(re.sub(r"[ \t]+", " ", l).strip(), cfg)
        if l:
            out.append((p, l))
    return out, dropped_fn, hdr


# ------------------------------------------------------------------ step 2/3: ToC + body start
def build_cands(lines):
    """cands[key] = line indexes where an entry numbered `key` may start.
    Glued variants ('11. The Republic' = footnote 1 + article 1) are added too; they are only accepted when the
    title also matches (see locate), so they cannot cause false hits."""
    cands, glued = {}, set()
    for i, (_, t) in enumerate(lines):
        m = CAND_RE.match(t)
        if m:
            cands.setdefault(m.group(1), []).append(i)
        for k in glue_keys(t):
            cands.setdefault(k, []).append(i)
            glued.add((k, i))
    for k in cands:
        cands[k] = sorted(set(cands[k]))
    return cands, glued


def strip_num(line, key=None):
    """remove the leading number (normal or glued) from a line"""
    m = CAND_RE.match(line)
    if m and (key is None or m.group(1) == key):
        return CAND_RE.sub("", line, count=1).strip()
    g = GLUE_RE.match(line)
    if g:
        for k in glue_keys(line):
            if key is None or k == key:
                return line[g.end():].strip()
    return CAND_RE.sub("", line, count=1).strip()


def text_after_number(lines, i, n=3):
    first = strip_num(lines[i][1])
    parts = [first]
    for j in range(i + 1, min(len(lines), i + 1 + n)):
        if CAND_RE.match(lines[j][1]):          # stop at the next numbered entry
            break
        parts.append(lines[j][1])
    return " ".join(p for p in parts if p)


def find_body_start(lines, cands, glued=frozenset()):
    ones = cands.get("1", [])
    if len(ones) < 2:
        return None, None, "fewer than two lines starting with '1.' - cannot separate ToC from body"
    toc_start = ones[0]
    want = norm(text_after_number(lines, toc_start))[:20]
    for i in ones[1:]:
        if norm(text_after_number(lines, i)).startswith(want):
            return toc_start, i, "body start = next '1.' with the same title as the ToC's first entry"
    return toc_start, ones[1], "WARNING body start = second '1.' (title did not match the ToC's first title)"


def parse_toc(lines, a, b):
    idxs = [i for i in range(a, b) if CAND_RE.match(lines[i][1])]
    entries, seen = [], set()
    for n, i in enumerate(idxs):
        end = idxs[n + 1] if n + 1 < len(idxs) else b
        key = CAND_RE.match(lines[i][1]).group(1)
        parts = [CAND_RE.sub("", lines[i][1], count=1).strip()]
        for j in range(i + 1, end):
            if HEAD_CUT.match(lines[j][1]):
                break
            parts.append(lines[j][1])
        title = re.sub(r"\s+", " ", " ".join(p for p in parts if p)).strip()
        if key in seen:
            log(f"   ToC duplicate key ignored: {key} {title[:60]!r}")
            continue
        seen.add(key)
        entries.append((key, title))
    return entries


# ------------------------------------------------------------------ step 4: locate each ToC entry in the body
def title_ok(lines, i, title):
    want = norm(title)[:30]
    if not want:
        return True
    win = norm(" ".join(t for _, t in lines[max(0, i - 2): i + 4]))
    return want in win


def locate(lines, entries, cands, body_start, body_end, glued=frozenset(), fix=None):
    found, notes, ptr = {}, [], body_start
    fix = fix or {}
    for key, title in entries:
        key = fix.get(key, key)
        idxs = cands.get(key, [])
        pos = bisect.bisect_left(idxs, ptr)
        hit, mode = None, ""
        for i in idxs[pos:]:
            if i >= body_end:
                break
            if title_ok(lines, i, title):
                hit, mode = i, "A"
                break
        if hit is None:                                   # fallback: number matches, title does not
            for i in idxs[pos:]:
                if i >= body_end or i > ptr + 200:
                    break
                if (key, i) in glued and not CAND_RE.match(lines[i][1]):
                    continue                     # glued lines are only trusted when the title matches
                hit, mode = i, "B"
                break
        if hit is None:
            continue
        if mode == "B":
            notes.append(f"   number-only match (title differs) for {key} {title[:50]!r} at line {hit}")
        if hit - ptr > BIG_JUMP_LINES and ptr != body_start:
            notes.append(f"   big jump ({hit - ptr} lines) before {key} {title[:50]!r} - check previous entries")
        found[key] = hit
        ptr = hit + 1
    return found, notes


# ------------------------------------------------------------------ step 5: build chunk text
def trim_trailing_headings(seg):
    n = len(seg)
    for k in range(max(1, n - 8), n):
        if HEAD_CUT.match(seg[k]) and len(seg[k]) < 90:
            return seg[:k], n - k
    return seg, 0


def assemble(seg):
    s = "\n".join(seg)
    s = re.sub(r"(?m)^(\([A-Za-z0-9]{1,5}\))[ \t]*\n", r"\1 ", s)       # "(a)\ntext" -> "(a) text"
    s = re.sub(r"_{2,}", " ", s)                                          # '__' separator
    s = re.sub(r"\n(?!\([A-Za-z0-9]{1,5}\)|Explanation|Illustration|Exception|Provided|Proviso)", " ", s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r" ?\n ?", "\n", s)
    return s.strip()


def is_omitted(text):
    if re.fullmatch(r"[\*\s]*", text):                      # only '* * *' = deleted
        return True
    if len(text) < 200 and re.search(r"\[\s*(Omitted|Repealed|Deleted|Declared void[^\]]*)\s*\]", text, re.I):
        return True
    return bool(re.match(r"[\[\s]*(Omitted|Repealed|Deleted)\b", text, re.I)) and len(text) < 200


# ------------------------------------------------------------------ step 6: split long sections
def hard_split(p):
    if len(p) <= LONG_LIMIT:
        return [p]
    pieces, cur = [], ""
    for s in re.split(r"(?<=[.;:])\s+", p):
        if cur and len(cur) + len(s) + 1 > SUB_TARGET:
            pieces.append(cur)
            cur = s
        else:
            cur = f"{cur} {s}" if cur else s
    if cur:
        pieces.append(cur)
    return pieces


def split_parent(text):
    if len(text) <= LONG_LIMIT:
        return [text]
    subs, cur = [], ""
    for para in text.split("\n"):                 # paragraphs start at (a) (1) Explanation Illustration ...
        for piece in hard_split(para):
            if cur and len(cur) + len(piece) + 1 > SUB_TARGET:
                subs.append(cur)
                cur = piece
            else:
                cur = f"{cur}\n{piece}" if cur else piece
    if cur:
        subs.append(cur)
    if len(subs) > 1 and len(subs[-1]) < 150:     # merge a tiny tail into the previous piece
        tail = subs.pop()                              # pop FIRST, then append (old one-liner crashed)
        subs[-1] += "\n" + tail
    return subs


# ------------------------------------------------------------------ diagnostics helper
def raw_context(raw, title, width=150):
    """300 chars of RAW text around the LAST occurrence of the title (line breaks shown as ' | ')."""
    words = title.split()
    for n in (len(words), 6, 3):
        if n == 0 or n > len(words):
            continue
        pat = re.compile(r"\s+".join(re.escape(w) for w in words[:n]), re.I)
        ms = list(pat.finditer(raw))
        if ms:
            m = ms[-1]
            s, e = max(0, m.start() - width), min(len(raw), m.end() + width)
            return f"(match on first {n} words, occurrence {len(ms)} of {len(ms)}) " + raw[s:e].replace("\n", " | ")
    return "(title not found in raw text at all)"


# ------------------------------------------------------------------ main per-law routine
def process_law(law, cfg):
    log("=" * 78)
    log(f"LAW: {law}  ({cfg['name']})")
    path = ensure_raw(cfg)
    if path is None:
        return [], [], {}
    raw = path.read_text(encoding="utf-8")
    pages = read_pages(path)
    lines, dropped_fn, hdr = clean_law(pages, cfg)
    log(f"   pages={len(pages)}  clean lines={len(lines)}  page-header lines removed={hdr}  footnote lines dropped={len(dropped_fn)}")
    for l in [x for x in dropped_fn if x.strip()][:5]:
        log(f"      dropped example: {l[:100]!r}")

    cands, glued = build_cands(lines)
    toc_start, body_start, why = find_body_start(lines, cands, glued)
    log(f"   {why}")
    if body_start is None:
        log("   STOP: use inspect_text.py to look at how '1.' appears and paste the result back")
        return [], [], {}
    entries = parse_toc(lines, toc_start, body_start)
    fix = cfg.get("key_fix", {})
    entries = [(fix.get(k, k), t) for k, t in entries]
    log(f"   ToC: lines {toc_start}..{body_start}  entries={len(entries)}  first={entries[:2]}  last={entries[-2:]}")

    body_end = len(lines)
    if cfg["has_schedules"]:
        for i in range(body_start, len(lines)):
            if SCHED_RE.match(lines[i][1]):
                body_end = i
                break
        log(f"   articles end / schedules start at line {body_end} of {len(lines)}"
            + ("" if body_end < len(lines) else "  WARNING: 'FIRST SCHEDULE' line not found"))

    found, notes = locate(lines, entries, cands, body_start, body_end, glued)
    for n in notes:
        log(n)
    order = [(k, found[k]) for k, _ in entries if k in found]
    title_of = dict(entries)

    parents, omitted, problems = [], [], []
    for n, (key, start) in enumerate(order):
        end = order[n + 1][1] if n + 1 < len(order) else body_end
        seg = [t for _, t in lines[start:end]]
        seg[0] = strip_num(seg[0], key)
        seg, trimmed = trim_trailing_headings(seg)
        text = assemble(seg)
        title = title_of[key].strip(" .\u2014-")
        rec = dict(id=f"{law}-{key}", law=law, law_name=cfg["name"], kind=cfg["kind"], number=key,
                   heading=title, cite=f"{cfg['short']} {cfg['label']} {key}", page=lines[start][0],
                   text=text, n_chars=len(text))
        if is_omitted(text) or is_omitted(title):
            omitted.append(rec)
        else:
            parents.append(rec)
            if len(text) < MIN_BODY or len(text) < len(title) + 15:
                problems.append((key, title, "body too short"))
    for key, title in entries:
        if key not in found:
            if is_omitted(title):
                omitted.append(dict(id=f"{law}-{key}", law=law, number=key, heading=title, text="", note="not in body"))
            else:
                problems.append((key, title, "NOT FOUND in body"))

    # optional: schedules
    if cfg["has_schedules"] and CHUNK_SCHEDULES and body_end < len(lines):
        sidx = [i for i in range(body_end, len(lines)) if SCHED_RE.match(lines[i][1])] + [len(lines)]
        for a, b in zip(sidx, sidx[1:]):
            name = lines[a][1].split("_")[0].strip().title()
            txt = assemble([t for _, t in lines[a:b]])
            parents.append(dict(id=f"{law}-{norm(name)}", law=law, law_name=cfg["name"], kind="schedule",
                                number=name, heading=name, cite=f"{cfg['short']} {name}", page=lines[a][0],
                                text=txt, n_chars=len(txt)))

    # ---- report for this law
    nums = [int(re.match(r"\d+", k).group()) for k in found]
    log(f"   ToC entries={len(entries)}  matched={len(found)}  chunks kept={len(parents)}  omitted/repealed={len(omitted)}"
        f"  highest number matched={max(nums) if nums else None} (expected ~{cfg['expected_max'] or '?'})")
    if problems:
        log(f"   --- {len(problems)} ToC entries with NO body or body < {MIN_BODY} chars ---")
        for key, title, why in problems:
            log(f"   [{law} {key}] {title!r}: {why}")
            log(f"      raw: {raw_context(raw, title)}")
    return parents, omitted, dict(problems=len(problems))


# ------------------------------------------------------------------ units for embedding
def make_units(parents):
    units = []
    for p in parents:
        subs = split_parent(p["text"])
        prefix = f"{p['cite']} ({p['heading']}): "
        for k, s in enumerate(subs):
            units.append(dict(unit_id=p["id"] if len(subs) == 1 else f"{p['id']}#{k}", parent_id=p["id"],
                              law=p["law"], kind=p["kind"], number=p["number"], heading=p["heading"],
                              sub_index=k, n_subs=len(subs), text=s, embed_text=prefix + s))
    return units


def final_report(all_parents):
    log("=" * 78)
    log("VALIDATION REPORT")
    for law in LAWS:
        ps = [p for p in all_parents if p["law"] == law]
        if not ps:
            continue
        long_ = [p["id"] for p in ps if p["n_chars"] > LONG_LIMIT]
        log(f"{law}: {len(ps)} chunks; {len(long_)} longer than {LONG_LIMIT} chars (split into sub-chunks)")
        huge = [p for p in ps if p["n_chars"] > 6000]
        for p in huge:
            log(f"   CHECK possible swallowed tail: {p['id']} {p['n_chars']} chars; ends: ...{p['text'][-200:]!r}")
    srt = sorted(all_parents, key=lambda p: p["n_chars"])
    log("--- 10 shortest ---")
    for p in srt[:10]:
        log(f"   {p['id']:<20} {p['n_chars']:>6}  {p['heading'][:50]!r}  text={p['text'][:80]!r}")
    log("--- 10 longest ---")
    for p in srt[-10:][::-1]:
        log(f"   {p['id']:<20} {p['n_chars']:>6}  {p['heading'][:50]!r}")
    log("--- 5 random samples (start ... end) ---")
    rnd = random.Random(SEED)
    for p in rnd.sample(all_parents, min(5, len(all_parents))):
        log(f"   {p['id']} p.{p['page']} [{p['heading']}]\n      START: {p['text'][:300]!r}\n      END:   {p['text'][-150:]!r}")


# ------------------------------------------------------------------ append / merge support
def read_json(path):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else []


def write_json(path, data):
    tmp = path.with_suffix(path.suffix + ".tmp")          # write-then-rename: a crash never leaves a half file
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, path)


def merge(existing, new, laws_done, id_field):
    """keep every existing record of laws NOT in laws_done, replace the ones that are, in LAWS order"""
    kept = [r for r in existing if r.get("law") not in laws_done]
    order = {k: i for i, k in enumerate(LAWS)}
    merged = sorted(kept + new, key=lambda r: order.get(r.get("law"), len(order)))   # stable: keeps order inside a law
    ids = [r[id_field] for r in merged]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        sys.exit(f"duplicate {id_field} after merge: {sorted(dup)[:5]} - check the LAWS keys")
    return merged, len(kept)


def main():
    check_config()
    ap = argparse.ArgumentParser(description="chunk laws from raw/*.txt into chunks.json + embed_units.json")
    ap.add_argument("laws", nargs="*", help=f"law keys to process (default: all of {list(LAWS)})")
    ap.add_argument("--append", action="store_true",
                    help="merge the processed laws into the existing output files instead of overwriting them")
    a = ap.parse_args()
    bad = [x for x in a.laws if x not in LAWS]
    if bad:
        sys.exit(f"unknown law(s) {bad}; add an entry to LAWS first. Known: {list(LAWS)}")
    wanted = a.laws or list(LAWS)
    if a.append and not a.laws:
        log("note: --append without law names re-processes every law and replaces each one in the files.")
    if not a.append and a.laws and set(a.laws) != set(LAWS) and OUT_CHUNKS.exists():
        log(f"WARNING: you named only {a.laws} without --append, so chunks.json will contain ONLY these laws. "
            f"Use --append to keep the others.")

    new_parents, new_omitted = [], []
    for law in wanted:
        p, o, _ = process_law(law, LAWS[law])
        new_parents += p
        new_omitted += o
    if not new_parents:
        log("No chunks produced - output files NOT touched.")
    else:
        final_report(new_parents)
        new_units = make_units(new_parents)
        done = set(wanted)
        if a.append:
            parents, k1 = merge(read_json(OUT_CHUNKS), new_parents, done, "id")
            units, k2 = merge(read_json(OUT_UNITS), new_units, done, "unit_id")
            omitted, _ = merge(read_json(OUT_OMITTED), new_omitted, done, "id")
            log(f"\nAPPEND: kept {k1} existing chunks / {k2} existing units from other laws; "
                f"added or replaced {sorted(done)}")
        else:
            parents, units, omitted = new_parents, new_units, new_omitted
        write_json(OUT_CHUNKS, parents)
        write_json(OUT_UNITS, units)
        write_json(OUT_OMITTED, omitted)
        per = {}
        for p in parents:
            per[p["law"]] = per.get(p["law"], 0) + 1
        log(f"Wrote {len(parents)} chunks -> {OUT_CHUNKS.name}, {len(units)} embed units -> {OUT_UNITS.name}, "
            f"{len(omitted)} omitted -> {OUT_OMITTED.name}")
        log(f"chunks per law now in {OUT_CHUNKS.name}: {per}")
    with open(OUT_DIAG, "a" if a.append else "w", encoding="utf-8") as f:     # append mode keeps older laws' logs
        f.write(("\n\n##### run: " + " ".join(wanted) + " (append) #####\n" if a.append else "") + "\n".join(LOG))
    print(f"\n(all of the above is also saved in {OUT_DIAG.name})")


if __name__ == "__main__":
    main()