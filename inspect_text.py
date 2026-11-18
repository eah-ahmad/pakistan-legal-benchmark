# Muhammad Ahmad, CMS 542432, BSCS-15-D
"""
inspect_text.py  (LOCAL) - show the RAW text around a search string, so you can paste it back.

Usage:
    python inspect_text.py ppc "Adulteration of drugs"
    python inspect_text.py constitution "Acting Chief Justice" --context 500 --max 3

Line breaks are shown as " | ". Whitespace in the search string matches any line break.
"""
import re, sys, argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW_DIR = ROOT / "raw"
LAWS = {"constitution": "constitution.txt", "ppc": "ppc.txt", "peca": "peca.txt"}


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")   # avoid Windows console encoding errors
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("law", choices=LAWS.keys())
    ap.add_argument("search")
    ap.add_argument("--context", type=int, default=300, help="characters on each side (default 300)")
    ap.add_argument("--max", type=int, default=6, help="max occurrences to print (default 6)")
    ap.add_argument("--regex", action="store_true", help="treat search as a regex")
    a = ap.parse_args()

    raw = (RAW_DIR / LAWS[a.law]).read_text(encoding="utf-8")
    if a.regex:
        pat = re.compile(a.search, re.I)
    else:
        words = a.search.split()
        pat = re.compile(r"\s+".join(re.escape(w) for w in words), re.I)
    hits = list(pat.finditer(raw))
    print(f"{len(hits)} occurrence(s) of {a.search!r} in {a.law}")
    for n, m in enumerate(hits[: a.max], start=1):
        page = re.findall(r"=== PAGE (\d+) ===", raw[: m.start()])
        pg = page[-1] if page else "?"
        s, e = max(0, m.start() - a.context), min(len(raw), m.end() + a.context)
        snippet = raw[s:e].replace("\n", " | ")
        print(f"\n--- hit {n}/{len(hits)}  (page {pg}, char {m.start()}) ---")
        print(snippet)
    if len(hits) > a.max:
        print(f"\n... {len(hits) - a.max} more (use --max N)")


if __name__ == "__main__":
    main()
