# Muhammad Ahmad, CMS 542432, BSCS-15-D
import csv
import json
import re
from pathlib import Path


STOPWORDS = {
    "about", "after", "against", "among", "and", "are", "can", "does", "for", "from",
    "how", "into", "its", "law", "may", "not", "our", "that", "the", "their", "these",
    "this", "those", "under", "was", "what", "when", "where", "which", "who", "why", "with",
}
TOKEN_RE = re.compile(r"\d+[a-z]*(?:-[a-z]+)?|[a-z]{3,}", re.I)
OUTPUT_COLUMNS = [
    "no", "question", "expected_chunk_ids", "expected_heading", "expected_text_preview",
    "model_answer", "grade", "notes",
]


def keywords(text):
    return {
        token.lower()
        for token in TOKEN_RE.findall(text)
        if token.lower() not in STOPWORDS
    }


def rank_chunks(question, chunks):
    terms = keywords(question)
    if not terms:
        return []

    scored = []
    for position, chunk in enumerate(chunks):
        heading_terms = keywords(chunk.get("heading", ""))
        text_terms = keywords(chunk.get("text", ""))
        heading_hits = terms & heading_terms
        text_hits = terms & text_terms
        matched = heading_hits | text_hits
        scored.append((
            2 * len(heading_hits) + len(text_hits),
            len(matched) / len(terms),
            -position,
            chunk,
            len(matched),
        ))
    return sorted(scored, reverse=True, key=lambda item: item[:3])


def main():
    questions = Path("demo_questions.txt").read_text(encoding="utf-8").splitlines()
    chunks = json.loads(Path("chunks.json").read_text(encoding="utf-8"))
    rows = []
    weak = []

    questions = [line.strip() for line in questions if line.strip()]
    for number, question in enumerate(questions, 1):
        ranked = rank_chunks(question, chunks)
        best = ranked[0] if ranked else None
        good_match = best is not None and best[0] >= 2 and best[1] >= 0.25
        if good_match:
            candidates = ranked[:2]
            ids = " | ".join(item[3]["id"] for item in candidates)
            heading = best[3].get("heading", "")
            preview = best[3].get("text", "")[:300]
        else:
            ids = "expect refusal"
            heading = "expect refusal"
            preview = ""
            weak.append((question, best))

        rows.append({
            "no": number,
            "question": question,
            "expected_chunk_ids": ids,
            "expected_heading": heading,
            "expected_text_preview": preview,
            "model_answer": "",
            "grade": "",
            "notes": "",
        })

    with Path("demo_grading.csv").open("w", newline="", encoding="utf-8-sig") as output:
        writer = csv.DictWriter(output, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote demo_grading.csv ({len(rows)} questions).")
    if weak:
        print("Questions with weak/no good matches (marked expect refusal):")
        for question, best in weak:
            if best and best[4] > 0:
                print(f"- {question} [candidate: {best[3]['id']}, score={best[0]}, coverage={best[1]:.0%}]")
            else:
                print(f"- {question} [no keyword match]")


if __name__ == "__main__":
    main()
