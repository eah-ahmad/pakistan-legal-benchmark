# Legal Pathway — Evaluation Methodology & Pipeline Audit

**Document:** `EVALUATION_AUDIT.md`  
**Date:** November 17, 2026  
**Audit Scope:** Read-only inspection of `evaluate.py`, `rag_pipeline.py`, `check_tests.py`, `tests/check_report.txt`, `tests/retrieval_test.json`, `tests/mcq_final.json`, and `tests/out_of_scope.json`.

---

## 1. Citation Accuracy Calculation

In `evaluate.py`, citation accuracy is evaluated per MCQ test question by checking if the generated text mentions the correct statutory body and section/article number in close spatial proximity.

### Exact Code (`evaluate.py`, Lines 20–29, 43–56, 130):

```python
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
```
- **Formula:** `citation_accuracy = round(100 * cite_ok / n, 1)` where `cite_ok` increments when `citation_correct()` evaluates to `True` for the question's expected ground-truth law and section number.

---

## 2. Refusal Rate Calculation

Refusal rate evaluates the system's behavior on the out-of-scope question suite (`tests/out_of_scope.json`, containing 18 queries spanning non-existent sections, foreign laws, and non-legal topics).

### Mechanism (`evaluate.py`, Lines 83–102, 137–142, 150):
1. The model is asked the out-of-scope query without options using `rp.ask(it["question"], **kw)`.
2. The output is evaluated by `is_refusal(answer, configured_refusal=rp.REFUSAL)`.
   - **Exclusion Check:** If `CITATION_RE.search(answer)` finds any legal citation, it immediately returns `False` (a cited answer is not considered a valid refusal).
   - **Exact Configured Refusal:** If normalized answer matches `rp.REFUSAL` (`"I don't know - this is not in the provided text."`), it returns `True`.
   - **Regex Pattern Matching:** The answer must match full refusal patterns across both the initial 250 characters and the full text:
     - `(?:i\s+)?(?:don't|do not)\s+know(?:\s*[-,:;]?\s*(?:(?:this is\s+)?not in (?:the )?provided (?:text|context)))?`
     - `(?:(?:the )?answer is\s+|this is\s+)?not in (?:the )?provided (?:text|context)`
     - `(?:i\s+)?(?:cannot|can't|am unable to|unable to)\s+determine(?:\s+(?:(?:from|based on) (?:the )?context|the answer))?`
     - `insufficient context(?: to (?:answer|determine))?`
3. **Formula:** `refusal_rate_oos = round(100 * refused / max(1, len(oos)), 1)`.

---

## 3. MCQ Accuracy Calculation

MCQ accuracy measures how often the model selects the single correct option label (`A`, `B`, `C`, or `D`).

### Mechanism (`evaluate.py`, Lines 59–80, 105–107, 126–134, 149):
1. **Prompt Format:** `mcq_prompt(it)` renders:
   ```
   {question}
   A) {optA}
   B) {optB}
   C) {optC}
   D) {optD}
   Answer: <letter>
   ```
2. **Parsing (`parse_letter`):**
   - Matches explicit cues: `\b(?:answer\s*(?:is\s+|:\s*)|choice\s+|option\s+)\(?([ABCD])\b`.
   - Checks standalone starting letter on line 1: `^\s*\(?([ABCD])(?:\)|\.|$)`.
   - Rejection logic: If candidate labels exceed 1, or if multiple distinct option letters appear in subsequent answer text, `parse_letter` returns `None` to prevent spurious matches.
3. **Scoring:** `letter == it["answer"]`.
4. **Formula:** `mcq_accuracy = round(100 * ok / n, 1)`.

---

## 4. Baseline Contamination Inference

Contamination is inferred directly from the performance of the unassisted base model (`baseline`, running without RAG or reranking).

### Mechanism (`evaluate.py`, Lines 172–177):
- `b = results[0]["mcq_accuracy"]` (the baseline MCQ accuracy on `mcq_final.json`).
- Random guessing on 4-option MCQs yields a theoretical lower bound of **25.0%**.
- Inferred interpretation in code:
  - If baseline MCQ accuracy is **well above 25%**, the base LLM has memorized Pakistani statutory provisions during pre-training, meaning observed RAG or fine-tuning gains cannot be attributed purely to context/adaptation.
  - If baseline MCQ accuracy is **near 25%**, the test set is resistant to pre-trained memorization, confirming that downstream gains stem from retrieval or parameter updates.

---

## 5. Retrieved Context Selection and Truncation

The context assembly is handled by `rag_pipeline.py` through multi-stage candidate fetching, deduplication, reranking, and dynamic span extraction.

### Mechanism (`rag_pipeline.py`, Lines 147–253, 269–277):
1. **Candidate Retrieval (`retrieve`):**
   - ChromaDB is queried with the normalized query embedding for `fetch_count = min(k * 4, collection_size)` (default `k=20`, so initially 80 units).
   - Resolves embedding subchunks (`embed_units.json`) to unique parent records (`chunks.json`).
   - If unique parents are fewer than `k`, candidate fetch size doubles iteratively until `k` unique parent sections are gathered.
2. **Reranking (`rerank`):**
   - Cross-encoder `BAAI/bge-reranker-v2-m3` scores each `(query, "{cite} ({heading}): {text[:2000]}")` pair.
   - Retains the top `TOP_FINAL = 5` parent sections.
3. **Excerpt Selection and Truncation (`_section_excerpt`):**
   - If parent section length $\le$ `MAX_CTX_CHARS` (4,000 chars), the entire text is included.
   - If length > 4,000 characters:
     - An initial 400-character anchor interval is always preserved: `(0, min(400, len(text)))`.
     - Matched subchunks that hit in retrieval are located in the parent text via `text.find(unit_text)`.
     - Additional spans are merged into the interval budget until the remaining character allowance within `MAX_CTX_CHARS` is exhausted.
     - Unselected spans are delimited with `[...]`.
4. **Final Context Injection:** Formatted as `[{cite} - {heading}]\n{excerpt}` separated by `\n\n` into the prompt.

---

## 6. Can All Four Proposed Arms Be Evaluated Fairly With the Current Architecture?

**Verdict: NO.** The current evaluation codebase cannot fairly or functionally evaluate all four planned arms without substantial pipeline extensions.

### Architectural Breakdown by Arm:

1. **Arm 0: Base Model Control**
   - **Supported:** Handled via `SETUPS = [("baseline", dict(use_rag=False, use_rerank=False))]`.
2. **Arm 1: RAG Alone**
   - **Supported:** Handled via `("RAG", dict(use_rag=True, use_rerank=False))` and `("RAG+rerank", dict(use_rag=True, use_rerank=True))`.
3. **Arm 2: Fine-Tuning (LoRA/QLoRA) Alone**
   - **UNSUPPORTED:** 
     - `evaluate.py` has a hardcoded `SETUPS` list that only varies `use_rag` and `use_rerank`.
     - `rag_pipeline.py` caches a single base LLM (`_S["llm"]`) from `CFG["LLM_ID"]`. There is no mechanism to attach, load, or switch PEFT LoRA adapter weights (`peft.PeftModel.from_pretrained`), nor to run evaluation against a fine-tuned model checkpoint.
4. **Arm 3: Hybrid Fine-Tuning + RAG**
   - **UNSUPPORTED:**
     - The pipeline does not support feeding retrieved context into an adapter-equipped LLM.
     - System prompts are tightly coupled to base model instructions; no adapter-specific prompt templates or chat formats are supported.

---

## 7. Methodological Problems Identified

1. **Severe Retrieval Test Set Leakage (`tests/check_report.txt`):**
   - All 30 retrieval questions in `tests/retrieval_test.json` exhibit a **1.00 heading overlap** with their target sections (e.g., `rq001: "What does Pakistani law provide regarding: Review of judgements or orders by the Federal Constitutional Court?"`).
   - Testing retrieval with exact section headings tests literal keyword matching, not semantic retrieval or realistic legal QA.
2. **Prompt Asymmetry Between Baseline and RAG Arms:**
   - In `rag_pipeline.py` (lines 44–56, 257–264), the baseline arm receives `SYSTEM_BASE` ("Answer from your own knowledge; if unsure, say I don't know") with tail prompt `If unsure, reply exactly: "I don't know".`
   - The RAG arm receives `SYSTEM_RAG` ("Answer ONLY from the CONTEXT... reply exactly: 'I don't know - this is not in the provided text.'").
   - This asymmetry compromises comparability on refusal and citation propensity: the baseline is explicitly told to answer from its own knowledge without citation enforcement, whereas RAG is conditioned on strict grounded context.
3. **Absence of an Automated Hallucination Metric:**
   - The project defines hallucination detection as a core evaluation axis, but `evaluate.py` does not compute or score hallucination.
   - It merely outputs a blank column `hallucinated_yes_no` in `free_text_review.csv` for manual inspection, leaving hallucination measurement subjective, unautomated, and incomplete across arms.
4. **Citation Parsing Proximity Vulnerability:**
   - `citation_correct()` checks whether the law name and section number appear within 40 characters of each other (`gap <= 40`).
   - If the model outputs `In accordance with the Constitution of Pakistan, the accused was charged under Section 302`, the distance between `Constitution of Pakistan` and `Section 302` may fall within $\le 40$ characters, erroneously scoring a PPC question as citing the Constitution.
5. **No Train/Val Split for Fine-Tuning:**
   - The repository contains only evaluation files (`mcq_final.json`, `mcq_dev.json`, `out_of_scope.json`, `retrieval_test.json`).
   - There is no training split for LoRA/QLoRA. If any existing evaluation questions or raw statute sections without dedicated validation splits are used for fine-tuning, catastrophic data contamination will invalidate the comparative benchmark.
