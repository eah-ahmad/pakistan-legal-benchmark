# Muhammad Ahmad, CMS 542432, BSCS-15-D
"""
evaluate.py  (runs on COLAB, after rag_pipeline.build_index())       RESEARCH PROTOTYPE - NOT LEGAL ADVICE

    import evaluate; evaluate.run()

Three setups on the SAME test sets: baseline (LLM, no retrieval) | RAG | RAG+rerank.
Metrics (all in %):  MCQ accuracy = correct/total*100 | citation accuracy | refusal rate on out_of_scope.json
Extra: context hit@5 = % of MCQs whose correct section is inside the 5 sections given to the LLM (RAG setups).
Contamination check = the BASELINE MCQ accuracy (no retrieval), reported separately.
Outputs: results.csv, eval_details.json, free_text_review.csv (for the manual hallucination check).
"""
import csv, json, re, random
from pathlib import Path
import rag_pipeline as rp

SETUPS = [("baseline", dict(use_rag=False, use_rerank=False)),
          ("RAG", dict(use_rag=True, use_rerank=False)),
          ("RAG+rerank", dict(use_rag=True, use_rerank=True))]
LAW_WORDS = {
    "constitution": re.compile(r"\b(?:constitution(?: of pakistan)?|pakistan constitution)\b", re.I),
    "ppc": re.compile(r"\b(?:ppc|pakistan penal code|penal code)\b", re.I),
    "peca": re.compile(r"\b(?:peca|prevention of electronic crimes|electronic crimes)\b", re.I),
}
CITATION_RE = re.compile(
    r"\b(?:sections?|secs?\.?|s\.|articles?|arts?\.?)\s*[:\-]?\s*"
    r"(?P<number>\d{1,3}(?:\s*-\s*[a-z]{1,3}|[a-z]{1,3})?)(?![\w])",
    re.I,
)


def find(name):
    for p in (Path("tests") / name, Path(name)):
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
    raise FileNotFoundError(name)


def _normalized(text):
    return " ".join(text.translate(str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"'})).lower().split())


def citation_correct(answer, law, number):
    expected = re.sub(r"[\s-]", "", number).upper()
    law_mentions = list(LAW_WORDS[law].finditer(answer))
    for citation in CITATION_RE.finditer(answer):
        cited = re.sub(r"[\s-]", "", citation.group("number")).upper()
        if cited != expected:
            continue
        for mention in law_mentions:
            number_start = citation.start("number")
            number_end = citation.end("number")
            gap = max(mention.start() - number_end, number_start - mention.end(), 0)
            if gap <= 40:
                return True
    return False


def parse_letter(t):
    explicit = re.compile(
        r"\b(?:answer\s*(?:is\s+|:\s*)|choice\s+|option\s+)\(?([ABCD])\b",
        re.I,
    )
    candidates = {m.group(1).upper() for m in explicit.finditer(t)}
    first_line = t.splitlines()[0].strip() if t.splitlines() else ""
    standalone = re.match(r"^\s*\(?([ABCD])(?:\)|\.|$)", first_line, re.I)
    if standalone:
        candidates.add(standalone.group(1).upper())
    if len(candidates) != 1:
        return None

    # Explicitly reject compact answers that name more than one alternative.
    first_answer = explicit.search(t)
    if first_answer:
        answer_lines = t[first_answer.end():].splitlines()
        rest = answer_lines[0] if answer_lines else ""
        mentioned = {m.group(1).upper() for m in re.finditer(r"(?<!\w)\(?([ABCD])\b", rest, re.I)}
        if len(mentioned | candidates) > 1:
            return None
    return candidates.pop()


def is_refusal(answer, configured_refusal=None):
    first = _normalized(answer[:250]).strip(" \t\r\n.!?")
    normalized_answer = _normalized(answer).strip(" \t\r\n.!?")
    if CITATION_RE.search(answer):
        return False
    if configured_refusal and normalized_answer == _normalized(configured_refusal).strip(" \t\r\n.!?"):
        return True
    refusal_patterns = (
        r"(?:i\s+)?(?:don't|do not)\s+know"
        r"(?:\s*[-,:;]?\s*(?:(?:this is\s+)?not in (?:the )?provided (?:text|context)))?",
        r"(?:(?:the )?answer is\s+|this is\s+)?not in (?:the )?provided (?:text|context)",
        r"(?:i\s+)?(?:cannot|can't|am unable to|unable to)\s+determine"
        r"(?:\s+(?:(?:from|based on) (?:the )?context|the answer))?",
        r"insufficient context(?: to (?:answer|determine))?",
    )
    return any(
        re.fullmatch(rf"{pattern}[.!? ]*", first, re.I)
        and re.fullmatch(rf"{pattern}[.!? ]*", normalized_answer, re.I)
        for pattern in refusal_patterns
    )


def mcq_prompt(it):
    o = it["options"]
    return f"{it['question']}\nA) {o['A']}\nB) {o['B']}\nC) {o['C']}\nD) {o['D']}\nAnswer: <letter>"


def run(max_mcq=None, n_free=30, MCQ_FILE="mcq_final.json"):
    if MCQ_FILE not in {"mcq_dev.json", "mcq_final.json"}:
        raise ValueError("MCQ_FILE must be 'mcq_dev.json' or 'mcq_final.json'")
    print(f"MCQ file: {MCQ_FILE}")
    mcq, oos, ret = find(MCQ_FILE), find("out_of_scope.json"), find("retrieval_test.json")
    if max_mcq:
        mcq = mcq[:max_mcq]
    number_of = {c["id"]: c["number"] for c in rp._data()[0].values()}
    free = random.Random(1).sample(ret, min(n_free, len(ret)))
    results, details, free_rows = [], {}, []

    for name, kw in SETUPS:
        print(f"\n=== {name} ===")
        det = dict(mcq=[], oos=[])
        ok = cite_ok = hit = 0
        for i, it in enumerate(mcq, 1):
            p = mcq_prompt(it)
            r = rp.ask(p, mode="mcq", retrieval_query=p, max_new_tokens=80, **kw)
            letter = parse_letter(r["answer"])
            correct = letter == it["answer"]
            cit = citation_correct(r["answer"], it["law"], number_of.get(it["source_id"], "?"))
            h = any(s["id"] == it["source_id"] for s in r["sources"])
            ok += correct; cite_ok += cit; hit += h
            det["mcq"].append(dict(id=it["id"], pred=letter, gold=it["answer"], correct=correct, cited_ok=cit,
                                   ctx_hit=h, answer=r["answer"]))
            if i % 20 == 0:
                print(f"  mcq {i}/{len(mcq)}")
        refused = 0
        for it in oos:
            r = rp.ask(it["question"], **kw)
            ref = is_refusal(r["answer"], rp.REFUSAL)
            refused += ref
            det["oos"].append(dict(id=it["id"], refused=ref, answer=r["answer"]))
        for it in free:
            r = rp.ask(it["question"], **kw)
            free_rows.append(dict(setup=name, id=it["id"], question=it["question"], expected_source=it["source_id"],
                                  answer=r["answer"], retrieved=" | ".join(s["cite"] for s in r["sources"]),
                                  hallucinated_yes_no="", notes=""))
        n = len(mcq)
        results.append(dict(setup=name, mcq_accuracy=round(100 * ok / n, 1), citation_accuracy=round(100 * cite_ok / n, 1),
                            refusal_rate_oos=round(100 * refused / max(1, len(oos)), 1),
                            context_hit_at_5=round(100 * hit / n, 1) if kw["use_rag"] else "n/a",
                            n_mcq=n, n_oos=len(oos), mcq_file=MCQ_FILE))
        details[name] = det

    cols = list(results[0])
    with open("results.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(results)
    Path("eval_details.json").write_text(json.dumps(details, ensure_ascii=False, indent=1), encoding="utf-8")
    with open("free_text_review.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(free_rows[0]))
        w.writeheader()
        w.writerows(free_rows)

    print("\n" + "=" * 86)
    print("RESULTS (%)  -  research prototype, not legal advice")
    print(f"{'setup':<12}{'MCQ acc':>10}{'citation acc':>14}{'refusal OOS':>13}{'ctx hit@5':>11}{'n_mcq':>7}{'n_oos':>7}")
    for r in results:
        print(f"{r['setup']:<12}{r['mcq_accuracy']:>10}{r['citation_accuracy']:>14}{r['refusal_rate_oos']:>13}"
              f"{str(r['context_hit_at_5']):>11}{r['n_mcq']:>7}{r['n_oos']:>7}")
    b = results[0]["mcq_accuracy"]
    print("\nCONTAMINATION CHECK: baseline (no retrieval) MCQ accuracy =", b, "%  (random guessing = 25%).")
    print("  If this is well above 25%, the base model already knows many answers without retrieval (pre-training\n"
          "  exposure or general knowledge), so the gain from RAG is smaller than it looks. If it is near 25%, the\n"
          "  test questions are not answerable from memory and the RAG gain is attributable to retrieval.\n"
          "  This is a simple indicator, not proof of presence or absence of contamination.")
    print("\nSaved: results.csv, eval_details.json, free_text_review.csv (fill the hallucinated_yes_no column by hand)")
    return results
