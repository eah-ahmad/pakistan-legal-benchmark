# Muhammad Ahmad, CMS 542432, BSCS-15-D
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TESTS = ROOT / "tests"
SRC = TESTS / "out_of_scope.json"
OUT = TESTS / "out_of_scope_v2.json"
CHECK = TESTS / "check_report.txt"

SPECIAL_REPLACEMENTS = {
    "oos006": {
        "question": "What are the penalties for tax evasion under the Income Tax Ordinance, 2001?",
        "category": "other_pk_law",
    },
    "oos013": {
        "question": "What are the eligibility requirements for a US H-1B visa?",
        "category": "other_country",
    },
}
GENERIC_REPLACEMENTS = {
    "fake_number": "What are the penalties for tax evasion under the Income Tax Ordinance, 2001?",
    "other_country": "What are the eligibility requirements for a US H-1B visa?",
    "other_pk_law": "What are the procedural requirements for filing an appeal under the Code of Civil Procedure, 1908?",
}


def read_report_flagged_ids():
    flagged_ids = set()
    if CHECK.exists():
        text = CHECK.read_text(encoding="utf-8")
        start = text.lower().find("strong out-of-scope flags:")
        if start >= 0:
            block = text[start:]
            for match in re.finditer(r"^\s*-\s*(oos\d+)\s*\|", block, flags=re.MULTILINE):
                flagged_ids.add(match.group(1))
    return flagged_ids


def main():
    items = json.loads(SRC.read_text(encoding="utf-8"))
    flagged_ids = read_report_flagged_ids() | set(SPECIAL_REPLACEMENTS)
    new_items = []
    replacements = []
    for item in items:
        new_item = dict(item)
        if item["id"] in flagged_ids:
            replacement = SPECIAL_REPLACEMENTS.get(item["id"], {
                "question": GENERIC_REPLACEMENTS.get(item.get("category", "other_country"), "What are the eligibility requirements for a US H-1B visa?"),
                "category": item.get("category", "other_country"),
            })
            old_question = item["question"]
            new_question = replacement["question"]
            new_item["question"] = new_question
            new_item["category"] = replacement["category"]
            replacements.append((item["id"], old_question, new_question, new_item["category"]))
        new_items.append(new_item)

    OUT.write_text(json.dumps(new_items, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Wrote {OUT} with {len(new_items)} items")
    for item_id, old_question, new_question, category in replacements:
        print(f"- {item_id} [{category}]")
        print(f"  old: {old_question}")
        print(f"  new: {new_question}")


if __name__ == "__main__":
    main()
