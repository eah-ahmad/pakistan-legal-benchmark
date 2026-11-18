# Muhammad Ahmad, CMS 542432, BSCS-15-D
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TESTS = ROOT / "tests"
CHUNKS = json.loads((ROOT / "chunks.json").read_text(encoding="utf-8"))
CHUNK_BY_ID = {chunk["id"]: chunk for chunk in CHUNKS}
STOPWORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are",
    "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but",
    "by", "can", "cannot", "could", "did", "do", "does", "doing", "down", "during", "each",
    "few", "for", "from", "further", "had", "has", "have", "having", "he", "her", "here",
    "hers", "herself", "him", "himself", "his", "how", "i", "if", "in", "into", "is", "it",
    "its", "itself", "just", "me", "more", "most", "my", "myself", "no", "nor", "not", "of",
    "off", "on", "once", "only", "or", "other", "our", "ours", "ourselves", "out", "over",
    "own", "same", "she", "should", "so", "some", "such", "than", "that", "the", "their",
    "theirs", "them", "themselves", "then", "there", "these", "they", "this", "those",
    "through", "to", "too", "under", "until", "up", "very", "was", "we", "were", "what",
    "when", "where", "which", "while", "who", "whom", "why", "with", "you", "your", "yours",
    "yourself", "yourselves"
}


def content_words(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return [word for word in text.split() if word and word not in STOPWORDS]


def normalize_question_text(text):
    """Normalized text for exact and near-exact duplicate detection."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return " ".join(text.split())


def question_hash(text):
    return hashlib.md5(normalize_question_text(text).encode("utf-8")).hexdigest()


def heading_overlap_ratio(question, heading):
    q_words = set(content_words(question))
    h_words = [w for w in content_words(heading) if w]
    if not h_words:
        return 0.0
    matched = sum(1 for w in h_words if w in q_words)
    return matched / len(h_words)


def load_json(path):
    p = Path(path)
    if not p.exists():
        return []
    return json.loads(p.read_text(encoding="utf-8"))


def find_chunk_by_source_id(source_id):
    return CHUNK_BY_ID.get(source_id)


def print_section(title):
    print(f"\n=== {title} ===")


def extract_expected_citations(item):
    """
    Extracts citation references supporting both legacy schema ('source_id')
    and expanded benchmark schema ('expected_citations': [{'chunk_id', ...}] or list of IDs).
    Returns a list of chunk_id strings.
    """
    citations = []
    if "expected_citations" in item and item["expected_citations"]:
        for c in item["expected_citations"]:
            if isinstance(c, dict):
                cid = c.get("chunk_id") or c.get("source_id") or c.get("id")
                if cid:
                    citations.append(cid)
            elif isinstance(c, str):
                citations.append(c)
    elif "source_id" in item and item["source_id"]:
        citations.append(item["source_id"])
    return citations


def check_duplicates(dataset_map):
    """
    Checks for normalized question text duplicates within and across files.
    dataset_map is a dict of {filename: list_of_items}.
    """
    print_section("Duplicate question screening")
    seen_hashes = {}
    duplicates = []
    for fname, items in dataset_map.items():
        for item in items:
            q = item.get("question", "")
            if not q:
                continue
            h = question_hash(q)
            norm_q = normalize_question_text(q)
            qid = item.get("id", "UNKNOWN")
            if h in seen_hashes:
                prev_file, prev_id, prev_text = seen_hashes[h]
                duplicates.append({
                    "file": fname,
                    "id": qid,
                    "duplicate_of_file": prev_file,
                    "duplicate_of_id": prev_id,
                    "text": q
                })
                print(f"- DUPLICATE: {fname} [{qid}] matches {prev_file} [{prev_id}]")
            else:
                seen_hashes[h] = (fname, qid, norm_q)
    print(f"Total duplicates flagged: {len(duplicates)}")
    return duplicates


def check_retrieval_leaks(filename="retrieval_test.json"):
    path = TESTS / filename
    retrieval = load_json(path)
    flagged = []
    print_section(f"Retrieval leak check ({filename})")
    for item in retrieval:
        cids = extract_expected_citations(item)
        if not cids:
            continue
        question = item.get("question", "")
        q_text = question.lower()
        reasons = []

        for cid in cids:
            chunk = find_chunk_by_source_id(cid)
            if not chunk:
                reasons.append(f"citation {cid} not in chunks.json")
                continue
            heading = chunk.get("heading", "")
            number = chunk.get("number", "")
            heading_text = heading.lower()

            if heading and heading_text in q_text:
                reasons.append(f"heading appears in question ({cid})")
            if number:
                m = re.search(rf"\b(?:Section|Article)\s*{re.escape(str(number))}\b", question, flags=re.IGNORECASE)
                if m:
                    reasons.append(f"number match: {number} ({cid})")
            ratio = heading_overlap_ratio(question, heading)
            if ratio >= 0.35:
                # 0.35 is treated as a warning threshold for potential leakage
                reasons.append(f"heading overlap {ratio:.2f} (warning >= 0.35) ({cid})")

        if reasons:
            flagged.append((filename, item["id"], question, reasons))
            print(f"- {filename} [{item['id']}] | reasons: {', '.join(reasons)}")
    print(f"Flagged retrieval questions in {filename}: {len(flagged)} / {len(retrieval)}")
    return flagged


def check_question_item(item, filename):
    """
    Validates a question item supporting both MCQ and free-text,
    legacy and expanded schema, citation traceability, and refusal metadata.
    """
    qid = item.get("id", "UNKNOWN")
    flags = []
    category = item.get("category", item.get("type", "unknown"))
    law = item.get("law", "unspecified")

    # 1. Validate citations against chunks.json
    cids = extract_expected_citations(item)
    is_answerable = item.get("is_answerable", True)
    refusal_required = item.get("refusal_required", False)

    if refusal_required or not is_answerable:
        # For explicitly unanswerable/refusal questions, having no valid citation is expected
        if cids:
            for cid in cids:
                if not find_chunk_by_source_id(cid):
                    flags.append(f"refusal question lists unknown citation: {cid}")
    else:
        if not cids:
            flags.append("missing citation (no source_id or expected_citations)")
        else:
            for cid in cids:
                if not find_chunk_by_source_id(cid):
                    flags.append(f"citation '{cid}' missing from chunks.json")

    # 2. MCQ vs Free-Text validation
    options = item.get("options")
    answer = item.get("answer")

    if options is not None:
        # MCQ format validation
        if not isinstance(options, dict):
            flags.append("options field must be a dictionary")
        else:
            if len(options) != 4:
                flags.append(f"options count is {len(options)}, expected 4")
            if len(set(options.values())) != len(options.values()):
                flags.append("options not all unique (duplicate option values)")
            if answer:
                if str(answer).strip().upper() not in options:
                    flags.append(f"answer key '{answer}' not in options {list(options.keys())}")
            else:
                if is_answerable and not refusal_required:
                    flags.append("missing answer key for answerable MCQ")
    else:
        # Free-text question format validation
        # Options are not required for free text or out-of-scope questions
        if is_answerable and not refusal_required and not answer and not item.get("required_reasoning_points"):
            flags.append("free-text question lacks ground-truth answer or required_reasoning_points")

    # 3. Heading overlap & leakage warning (threshold >= 0.35)
    question = item.get("question", "")
    for cid in cids:
        chunk = find_chunk_by_source_id(cid)
        if chunk:
            heading = chunk.get("heading", "")
            ratio = heading_overlap_ratio(question, heading)
            if ratio >= 0.35:
                flags.append(f"heading overlap {ratio:.2f} with {cid} (warning >= 0.35)")
            
            # Check for generic headings if lookup/define type
            if category in {"define", "lookup"}:
                words = [w for w in re.split(r"\s+", heading.strip()) if w]
                heading_norm = heading.lower()
                generic_prefix = (heading_norm.startswith("punishment") or 
                                  heading_norm.startswith("definition") or 
                                  heading_norm.startswith("interpretation"))
                if len(words) < 3 or generic_prefix:
                    flags.append(f"generic heading '{heading}' in {cid}")

    # 4. Refusal and answerability consistency
    if refusal_required and is_answerable:
        flags.append("conflicting metadata: refusal_required=True but is_answerable=True")
    if not is_answerable and not refusal_required:
        flags.append("ambiguous metadata: is_answerable=False but refusal_required=False")

    return flags


def check_dataset_file(filename):
    path = TESTS / filename
    items = load_json(path)
    if not items:
        return []
    print_section(f"Dataset integrity check: {filename}")
    law_counts = Counter(item.get("law", "unspecified") for item in items)
    type_counts = Counter(item.get("category", item.get("type", "unspecified")) for item in items)
    print(f"Total items: {len(items)}")
    print("Counts by law:", dict(sorted(law_counts.items())))
    print("Counts by category/type:", dict(sorted(type_counts.items())))

    flagged = []
    for item in items:
        qid = item.get("id", "UNKNOWN")
        flags = check_question_item(item, filename)
        if flags:
            cat = item.get("category", item.get("type", "unknown"))
            law = item.get("law", "unspecified")
            flagged.append((filename, qid, cat, law, flags))
            print(f"- [{filename}] {qid} [{cat}/{law}] | {'; '.join(flags)}")
    print(f"Flagged issues in {filename}: {len(flagged)}")
    return flagged


def top_chunk_matches(question, limit=3):
    q_words = set(content_words(question))
    if not q_words:
        return []
    matches = []
    for chunk in CHUNKS:
        heading_text = f"{chunk.get('heading', '')} {chunk.get('text', '')}"
        c_words = set(content_words(heading_text))
        overlap = len(q_words & c_words)
        if overlap == 0:
            continue
        score = overlap / len(q_words)
        matches.append((score, chunk["id"], chunk.get("law"), chunk.get("heading")))
    matches.sort(key=lambda x: (-x[0], x[1]))
    return matches[:limit]


def check_out_of_scope(filename="out_of_scope.json"):
    path = TESTS / filename
    oos_items = load_json(path)
    print_section(f"Out-of-scope check ({filename})")
    flagged = []
    special_ids = {"oos006", "oos013"}
    for item in oos_items:
        question = item.get("question", "")
        matches = top_chunk_matches(question, limit=3)
        qid = item.get("id", "UNKNOWN")
        if matches:
            print(f"- [{filename}] {qid} | Best match: {matches[0][1]} (score={matches[0][0]:.2f})")
            for score, chunk_id, law, heading in matches:
                print(f"    {chunk_id} [{law}] score={score:.2f} heading={heading}")
        is_special = qid in special_ids
        best_score = matches[0][0] if matches else 0.0
        if is_special or best_score >= 0.25:
            flagged.append((filename, qid, question, best_score, matches[:3]))
            print(f"  FLAGGED STRONG MATCH: {qid}")
    print(f"Strong out-of-scope matches flagged in {filename}: {len(flagged)}")
    return flagged


def main():
    test_files = [
        "retrieval_test.json",
        "mcq_test.json",
        "mcq_final.json",
        "mcq_dev.json",
        "out_of_scope.json",
    ]

    # Map files for duplicate detection
    dataset_map = {}
    for tf in test_files:
        p = TESTS / tf
        if p.exists():
            dataset_map[tf] = load_json(p)

    duplicates = check_duplicates(dataset_map)
    retrieval_flags = check_retrieval_leaks("retrieval_test.json")

    file_issues = []
    for tf in ["mcq_test.json", "mcq_final.json", "mcq_dev.json"]:
        if (TESTS / tf).exists():
            file_issues.extend(check_dataset_file(tf))

    oos_flags = check_out_of_scope("out_of_scope.json")

    # Generate comprehensive report
    report_lines = [
        "PAKISTANI LEGAL QA TEST CHECK REPORT (EXTENDED SCHEMA & AUDIT)",
        "=" * 65,
        "",
        "SUMMARY OF CHECKS:",
        f"- Duplicate question flags: {len(duplicates)}",
        f"- Retrieval leakage & warning flags (retrieval_test.json): {len(retrieval_flags)} / 30",
        f"- MCQ and Free-Text validation issues: {len(file_issues)}",
        f"- Out-of-scope high retrieval overlap flags: {len(oos_flags)} / {len(dataset_map.get('out_of_scope.json', []))}",
        "",
        "DUPLICATE QUESTIONS:",
    ]
    if duplicates:
        for d in duplicates:
            report_lines.append(f"- [{d['file']}] {d['id']} DUPLICATES [{d['duplicate_of_file']}] {d['duplicate_of_id']}: {d['text']}")
    else:
        report_lines.append("- None")

    report_lines.extend(["", "RETRIEVAL LEAK & WARNING FLAGS (threshold >= 0.35):"])
    if retrieval_flags:
        for fname, item_id, question, reasons in retrieval_flags:
            report_lines.append(f"- [{fname}] {item_id}: {question}")
            report_lines.append(f"  reasons={'; '.join(reasons)}")
    else:
        report_lines.append("- None")

    report_lines.extend(["", "DATASET INTEGRITY & VALIDATION ISSUES:"])
    if file_issues:
        for fname, item_id, item_type, law, flags in file_issues:
            report_lines.append(f"- [{fname}] {item_id} [{item_type}/{law}] | {'; '.join(flags)}")
    else:
        report_lines.append("- None")

    report_lines.extend(["", "STRONG OUT-OF-SCOPE OVERLAP MATCHES:"])
    if oos_flags:
        for fname, item_id, question, best_score, matches in oos_flags:
            report_lines.append(f"- [{fname}] {item_id} | best_score={best_score:.2f} | question={question}")
            for score, chunk_id, law, heading in matches:
                report_lines.append(f"    {chunk_id} [{law}] score={score:.2f}: {heading}")
    else:
        report_lines.append("- None")

    OUT = TESTS / "check_report.txt"
    OUT.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"\nWrote comprehensive report: {OUT}")


if __name__ == "__main__":
    main()
