# Muhammad Ahmad, CMS 542432, BSCS-15-D
"""
build_tests.py - turns your REVIEWED csv files into the final test JSON files.
Supports both legacy schema and expanded benchmark schema:
- MCQs (options A-D, single answer key)
- Free-text questions (scenarios, multi-hop, without options)
- Multiple expected citations (chunk IDs)
- Answerability, refusal, and expert verification metadata
Only rows whose status is "ok" are kept.   Run:  python build_tests.py
Output: tests/retrieval_test.json, tests/mcq_test.json, tests/out_of_scope.json, tests/scenarios_test.json (optional)
"""
import csv, json, re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REVIEW, TESTS = ROOT / "review", ROOT / "tests"


def read_csv_rows(name):
    p = REVIEW / name
    if not p.exists():
        return []
    with open(p, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = []
        for line_num, r in enumerate(reader, start=2):
            st = r.get("status", "").strip().lower()
            if st == "ok":
                rows.append((line_num, r))
        return rows


def parse_bool(val, default=True):
    if val is None or str(val).strip() == "":
        return default
    s = str(val).strip().lower()
    if s in {"true", "1", "yes", "y"}:
        return True
    if s in {"false", "0", "no", "n"}:
        return False
    return default


def parse_citations(row, valid_ids):
    """
    Parses citations from 'expected_citations' or 'source_id' / 'chunk_id'.
    Supports:
      - Pipe or comma delimited string: "ppc-302 | constitution-19"
      - JSON string: '[{"chunk_id": "ppc-302", "law": "ppc"}]'
      - Single ID in source_id or chunk_id
    Returns: (list_of_citation_dicts, list_of_errors)
    """
    citations = []
    errors = []
    raw = row.get("expected_citations", "").strip() or row.get("source_id", "").strip() or row.get("chunk_id", "").strip()

    if not raw:
        return citations, errors

    if raw.startswith("[") and raw.endswith("]"):
        try:
            parsed = json.loads(raw)
            for item in parsed:
                if isinstance(item, dict):
                    cid = item.get("chunk_id") or item.get("source_id") or item.get("id")
                    if not cid:
                        errors.append("citation object missing 'chunk_id'")
                        continue
                    if cid not in valid_ids:
                        errors.append(f"citation '{cid}' not found in chunks.json")
                    citations.append(item)
                elif isinstance(item, str):
                    if item not in valid_ids:
                        errors.append(f"citation '{item}' not found in chunks.json")
                    citations.append({"chunk_id": item})
        except json.JSONDecodeError:
            errors.append(f"malformed JSON in expected_citations: '{raw}'")
    else:
        parts = [p.strip() for p in re.split(r"[,|;]", raw) if p.strip()]
        for cid in parts:
            if cid not in valid_ids:
                errors.append(f"citation '{cid}' not found in chunks.json")
            citations.append({"chunk_id": cid})

    return citations, errors


def parse_reasoning_points(row):
    raw = row.get("required_reasoning_points", "").strip()
    if not raw:
        return []
    if raw.startswith("[") and raw.endswith("]"):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            pass
    return [p.strip() for p in re.split(r"[|;\n]", raw) if p.strip()]


def build_record(row, valid_ids, default_category=None):
    """
    Constructs a validated question record supporting both MCQ and free-text,
    refusal metadata, multiple citations, and backward compatibility.
    Returns: (record_dict, list_of_error_strings)
    """
    errors = []
    qid = row.get("id", "").strip()
    if not qid:
        errors.append("missing required 'id'")

    question = row.get("question", "").strip()
    if not question:
        errors.append("missing required 'question' text")

    category = row.get("category", "").strip() or row.get("type", "").strip() or (default_category or "general")
    law = row.get("law", "").strip().lower() or "general"

    is_answerable = parse_bool(row.get("is_answerable"), default=True)
    refusal_required = parse_bool(row.get("refusal_required"), default=False)
    expert_verified = parse_bool(row.get("expert_verified"), default=True)

    if refusal_required and is_answerable:
        errors.append("conflicting metadata: refusal_required=True but is_answerable=True")

    citations, cite_errors = parse_citations(row, valid_ids)
    if is_answerable and not refusal_required:
        if not citations:
            errors.append("answerable question requires at least one valid citation in chunks.json")
        errors.extend(cite_errors)
    else:
        # Refusal questions may have no citation, but if provided, must be valid
        errors.extend(cite_errors)

    # Detect if MCQ (options A-D present) or Free-text
    opts = {k: row.get(k, "").strip() for k in "ABCD" if row.get(k) is not None}
    has_opts = any(opts.values())

    answer = row.get("answer", "").strip().upper()
    options_dict = None

    if has_opts:
        missing_opts = [k for k in "ABCD" if not opts.get(k)]
        if missing_opts:
            errors.append(f"MCQ missing option keys: {missing_opts}")
        else:
            if len(set(opts.values())) != 4:
                errors.append("MCQ options are not all unique")
            if is_answerable and not refusal_required:
                if answer not in "ABCD":
                    errors.append(f"MCQ answer key '{answer}' must be one of A, B, C, D")
            options_dict = opts
    else:
        # Free-text: answer may be descriptive text or empty for refusal
        raw_ans = row.get("answer", "").strip()
        answer = raw_ans if raw_ans else None
        if is_answerable and not refusal_required and not answer and not row.get("required_reasoning_points"):
            errors.append("free-text answerable question must provide 'answer' or 'required_reasoning_points'")

    if errors:
        return None, errors

    # Assemble validated record
    rec = {
        "id": qid,
        "category": category,
        "type": category,  # backward compatibility with legacy scripts
        "law": law,
        "question": question,
        "split": row.get("split", "test").strip() or "test",
        "is_answerable": is_answerable,
        "refusal_required": refusal_required,
        "expert_verified": expert_verified,
    }

    if options_dict:
        rec["options"] = options_dict
    if answer is not None:
        rec["answer"] = answer

    if citations:
        rec["expected_citations"] = citations
        # Maintain backward compatibility for single-citation legacy code
        rec["source_id"] = citations[0]["chunk_id"]

    pts = parse_reasoning_points(row)
    if pts:
        rec["required_reasoning_points"] = pts

    return rec, []


def process_dataset(csv_name, valid_ids, default_category, out_json_name=None):
    rows = read_csv_rows(csv_name)
    if not rows:
        return []
    records = []
    rejected = 0
    for line_num, r in rows:
        rec, errs = build_record(r, valid_ids, default_category=default_category)
        if errs:
            rejected += 1
            print(f"REJECTED [{csv_name}:line {line_num}] id={r.get('id', '?')}: {'; '.join(errs)}")
        else:
            records.append(rec)
    print(f"{csv_name}: {len(records)} valid records built, {rejected} rejected (from {len(rows)} approved rows)")
    if out_json_name and records:
        out_path = TESTS / out_json_name
        out_path.write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  -> Wrote {out_path} ({len(records)} items)")
    return records


def main():
    TESTS.mkdir(exist_ok=True)
    chunks_path = ROOT / "chunks.json"
    if not chunks_path.exists():
        raise FileNotFoundError(f"Missing {chunks_path}")

    ids = {c["id"] for c in json.loads(chunks_path.read_text(encoding="utf-8"))}

    # 1. Retrieval benchmark questions
    retrieval_records = process_dataset("retrieval_draft.csv", ids, default_category="retrieval", out_json_name="retrieval_test.json")

    # 2. MCQ benchmark questions
    mcq_records = process_dataset("mcq_draft.csv", ids, default_category="lookup", out_json_name="mcq_test.json")

    # 3. Out-of-scope benchmark questions
    oos_rows = read_csv_rows("oos_draft.csv")
    oos_records = []
    oos_rejected = 0
    for line_num, r in oos_rows:
        r.setdefault("is_answerable", "false")
        r.setdefault("refusal_required", "true")
        r.setdefault("category", r.get("category", "out_of_scope"))
        rec, errs = build_record(r, ids, default_category="out_of_scope")
        if errs:
            oos_rejected += 1
            print(f"REJECTED [oos_draft.csv:line {line_num}] id={r.get('id', '?')}: {'; '.join(errs)}")
        else:
            oos_records.append(rec)
    print(f"oos_draft.csv: {len(oos_records)} valid records built, {oos_rejected} rejected")
    if oos_records:
        out_path = TESTS / "out_of_scope.json"
        out_path.write_text(json.dumps(oos_records, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  -> Wrote {out_path} ({len(oos_records)} items)")

    # 4. Scenarios & Multi-hop (if review file exists)
    if (REVIEW / "scenarios_draft.csv").exists():
        process_dataset("scenarios_draft.csv", ids, default_category="scenario", out_json_name="scenarios_test.json")

    print("\nSummary of built datasets:")
    if mcq_records:
        print("MCQ by law:", dict(Counter(m["law"] for m in mcq_records)), "| by category:", dict(Counter(m["category"] for m in mcq_records)))
    if retrieval_records:
        print("Retrieval by law:", dict(Counter(r["law"] for r in retrieval_records)))
    if oos_records:
        print("OOS by category:", dict(Counter(o["category"] for o in oos_records)))


if __name__ == "__main__":
    main()
