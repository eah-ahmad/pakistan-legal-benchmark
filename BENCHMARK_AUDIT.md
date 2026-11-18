# Legal Pathway — Benchmark Quality & Dataset Hygiene Audit

**Document:** `BENCHMARK_AUDIT.md`  
**Date:** November 17, 2026  
**Audit Scope:** Read-only benchmark inspection of `tests/retrieval_test.json`, `tests/mcq_final.json`, `tests/mcq_dev.json`, `tests/out_of_scope.json`, `tests/check_report.txt`, `build_tests.py`, and `check_tests.py`.

---

## 1. Realistic Representation of Pakistani Legal Queries

**Finding: Low ecological validity.**  
The current benchmark questions do not realistically represent natural legal queries posed by citizens, practicing advocates, or legal researchers in Pakistan.

- **Synthetic, Templated Formulation:**  
  Across both `tests/retrieval_test.json` and the MCQ suites (`tests/mcq_final.json`, `tests/mcq_dev.json`), questions are generated from rigid mechanical templates:
  - Retrieval questions follow a single fixed template: `What does Pakistani law provide regarding: <Heading>?` (e.g., `tests/retrieval_test.json`, `rq001`–`rq030`).
  - MCQ questions strictly alternate between two reverse lookup templates:
    1. `lookup`: *"What is the subject (heading) of [Section/Article X] of the [Law]?"* (e.g., `mq001`–`mq010`, `mq021`–`mq030`, `mq041`–`mq050`).
    2. `define`: *"Which [section/article] of the [Law] deals with \"[Exact Heading]\"?"* (e.g., `mq011`–`mq020`, `mq031`–`mq040`, `mq051`–`mq060`).
- **Absence of Real-World Legal Scenarios:**  
  Real users rarely query statutory section numbers or recite exact legislative table-of-contents headings. Realistic legal inquiries involve:
  - Factual scenarios (e.g., *"A person posted edited photos of someone on social media without consent. What offence is committed and what is the punishment?"*).
  - Procedural inquiries (bail eligibility, compounding offences, jurisdiction, cognizable vs non-cognizable categorization).
  - Legal elements (mens rea, exceptions under Chapter IV of PPC).  
  Instead, the benchmark exclusively tests rote memorization of statutory heading-to-number mappings.

---

## 2. Correctness and Statutory Traceability of Answers and Citations

**Finding: Technically traceable, but shallow.**

- **Traceability to `chunks.json`:**  
  All ground-truth answers in `tests/mcq_final.json`, `tests/mcq_dev.json`, and `tests/retrieval_test.json` map directly to verified chunk IDs in `chunks.json` via `source_id` (e.g., `constitution-194`, `ppc-302`, `peca-11`).
- **Citation Precision:**  
  The citations are 1:1 reflections of official section headings from the Constitution of Pakistan (1973), Pakistan Penal Code (Act XLV of 1860), and PECA 2016.
- **Limitation:**  
  Because all questions ask for the heading or the section number matching that heading, correctness is purely lexical rather than substantive. None of the benchmark items require interpreting statutory text, analyzing exceptions, or tracing cross-statute interactions (e.g., PECA Section 28 incorporating the PPC, or CrPC procedures).

---

## 3. Distinction Between Answerable and Unanswerable Questions

**Finding: Well-categorized structurally, but vulnerable to embedding overlap.**

- **Appropriate Categorization in `tests/out_of_scope.json`:**  
  The 18 unanswerable questions are cleanly split into three defined failure archetypes:
  1. `fake_number`: Non-existent statutory sections (e.g., `oos001`: *"What does Section 999 of the Pakistan Penal Code say?"*, `oos003`: *"Explain Article 400 of the Constitution of Pakistan"*).
  2. `other_country`: Foreign legal frameworks (e.g., `oos006`: Indian Penal Code, `oos007`: US First Amendment, `oos008`: English common law, `oos009`: EU GDPR, `oos010`: Canadian Charter).
  3. `general_knowledge` / non-law topics (e.g., `oos011`: Companies Act 2017, `oos014`: capital of France, `oos018`: diabetes treatment).
- **Vulnerability to False Positive Retrieval Matches:**  
  As reported in `tests/check_report.txt` (lines 81–141), semantic embedding models retrieve high-scoring lexical overlaps for several out-of-scope queries (e.g., `oos006` matching `ppc-111` with score 0.86; `oos004` matching `constitution-260` with score 0.80). This tests whether the generation component can refuse despite top-k retrieval delivering misleading distractor passages.

---

## 4. Benchmark Flaws: Duplicates, Heading Leakage, Ambiguity, and Answer-Key Issues

### A. Total Heading Leakage (Exact File & IDs)
- **`tests/retrieval_test.json` (All 30 Items: `rq001` through `rq030`):**  
  Every single question contains the literal heading of the target chunk verbatim (`check_report.txt`, lines 4–64).  
  *Example (`rq001`):* `"What does Pakistani law provide regarding: Review of judgements or orders by the Federal Constitutional Court?"` $\rightarrow$ Target heading is verbatim `"Review of judgements or orders by the Federal Constitutional Court"`.  
  *Impact:* Measures trivial token-overlap string matching instead of semantic dense retrieval.

### B. Generic / Ambiguous Headings in MCQ Distractors
In `tests/check_report.txt` (lines 66–79), 12 MCQ questions were flagged for generic headings that create ambiguity or artificial difficulty:
- **`tests/mcq_test.json` (and sub-splits):**
  - `mq003` (`tests/mcq_dev.json`): Constitution Article 132 heading `"Provincial Ministers"` (generic).
  - `mq009` (`tests/mcq_final.json`): Constitution Article 91 heading `"The Cabinet"` (generic).
  - `mq019` (`tests/mcq_dev.json`): Constitution Article 51 heading `"National Assembly"` (generic).
  - `mq024` (`tests/mcq_final.json`): PPC Section 28 heading.
  - `mq029` (`tests/mcq_final.json`): PPC Section 40 heading.
  - `mq037` (`tests/mcq_dev.json`): PPC Section 19 heading.
  - `mq043` (`tests/mcq_dev.json`): PECA Section 3 heading.
  - `mq046` (`tests/mcq_final.json`): PECA Section 2 heading `"Definitions"`.
  - `mq049` (`tests/mcq_final.json`): PECA Section 26 heading.
  - `mq054` (`tests/mcq_dev.json`): PECA Section 2 heading.
  - `mq055` (`tests/mcq_dev.json`): PECA Section 29 heading.
  - `mq060` (`tests/mcq_final.json`): PECA Section 35 heading.

### C. Overlapping Definitions Across Acts
- **`tests/mcq_final.json` (`mq046`) & `tests/mcq_dev.json` (`mq054`):**  
  Both questions target Section 2 of PECA ("Definitions"). In multiple statutes (PPC Section 40, PECA Section 2, Constitution Article 260), the heading is simply `"Definitions"`. Asking *"What is the subject of Section 2?"* creates severe distractor ambiguity if options contain identical generic headers.

### D. Duplicate Question Ingestion across Versions
- **`tests/out_of_scope.json` vs `tests/out_of_scope_v2.json`:**  
  Two separate out-of-scope files exist in `tests/`. `out_of_scope_v2.json` contains revisions that are not loaded by `evaluate.py` (which hardcodes `out_of_scope.json` on line 114).

---

## 5. Sample Size Adequacy and Publication Limitations

### Current Sample Sizes:
- **Retrieval Test:** 30 queries (`tests/retrieval_test.json`).
- **Dev MCQ Test:** 20 questions (`tests/mcq_dev.json`).
- **Final Evaluation MCQ Test:** 40 questions (`tests/mcq_final.json`).
- **Out-of-Scope Test:** 18 questions (`tests/out_of_scope.json`).
- **Total Final Benchmark Items:** 58 items (40 MCQs + 18 OOS).

### Adequacy for Preliminary Prototyping:
- **Adequate for Quick Smoke Testing:** The small size allows rapid zero-cost iterations on CPU/Colab free tier (evaluating 40 MCQs with 80 tokens takes ~2–3 minutes). It confirms whether code pipelines run end-to-end without crashing.

### Limitations for Peer-Reviewed Academic Publication:
1. **Statistical Power & Significance:**  
   With $N = 40$ in `mcq_final.json`, each individual question represents **2.5 percentage points** of accuracy. A difference of 2 questions alters accuracy by 5.0%, making it impossible to establish statistical significance (e.g., McNemar's test or bootstrap confidence intervals) between RAG, LoRA, and Hybrid arms.
2. **Out-of-Scope Coarseness:**  
   With $N = 18$ in `out_of_scope.json`, each question accounts for **5.56 percentage points**. A difference of 1 question swings refusal rate substantially.
3. **Narrow Statutory Coverage:**  
   The corpus contains 1,013 parent statutory sections. An evaluation set of 40 MCQs covers only ~3.9% of the legal corpus, leaving 96% of statutory provisions completely unassessed.
4. **Publication Rejection Risk:**  
   Reviewers at NLP/AI venues (e.g., ACL, EMNLP, ICAIL, COLING) will reject benchmarks that rely on 40 template-generated lookup questions with 100% heading leakage. Standard legal QA benchmarks require hundreds to thousands of expert-curated or crowd-sourced scenario questions (e.g., LegalBench, LawBench, CJPE).

---

## 6. Separation Between Dev and Final Test Sets

**Finding: Properly stratified and split, but derived from the same synthetic distribution.**

- **Splitting Script (`split_mcq.py`):**  
  - Controlled pseudo-random seed (`random.Random(7)`).
  - Stratified allocation across both `law` (Constitution, PPC, PECA) and question `type` (`define`, `lookup`) ensures proportional representation.
  - Exactly 20 items assigned to `tests/mcq_dev.json` (`split: "dev"`) and 40 items assigned to `tests/mcq_final.json` (`split: "final"`).
  - Dev IDs are logged in `tests/dev_ids.txt`.
- **Zero Item Overlap:**  
  Set intersection between `mcq_dev.json` and `mcq_final.json` IDs is strictly empty ($\emptyset$).
- **Methodological Limitation:**  
  While the split is clean, both dev and final sets were drawn from the identical synthetic template pool (`review/mcq_draft.csv` via `tests/mcq_test.json`). Tuning prompts or hyperparameters on `mcq_dev.json` optimizes for template syntactic patterns rather than generalizable legal understanding.
