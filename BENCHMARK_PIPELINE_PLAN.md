# Benchmark Pipeline Transition Plan: Scaling to 320 Items

**Document:** `BENCHMARK_PIPELINE_PLAN.md`  
**Date:** November 17, 2026  
**Focus:** Minimal-footprint pipeline adaptation for the approved 320-question benchmark design, maximizing code reuse from `build_tests.py`, `split_mcq.py`, and `check_tests.py`.

---

## 1. Component Reuse Analysis

The existing codebase already implements solid data validation, chunk referencing, stratified splitting, and lexical overlap checking. We can reuse substantial parts without reinvention.

| Component / Function | Status | Reusable Code / Logic | Reason for Reuse |
|---|:---:|---|---|
| **`build_tests.py`** | **Partial Reuse (70%)** | `read()` CSV loader with `"status" == "ok"` gating, chunk ID existence verification against `chunks.json`, JSON serialization to `tests/`. | Core ingestion logic and status gating are robust; only schema parsing needs expansion. |
| **`split_mcq.py`** | **High Reuse (85%)** | `alloc_dev_counts()` proportional bucket allocation algorithm, `random.Random(seed)` deterministic shuffling, `dev_ids.txt` logging. | Exact multi-group stratified splitting logic works seamlessly for larger allocations (e.g. dev/final or train/dev/test splits). |
| **`check_tests.py`** | **High Reuse (80%)** | `content_words()` stopword tokenizer, `heading_overlap_ratio()`, option uniqueness validation, `top_chunk_matches()` overlap search for OOS. | Core lexical and overlap validation routines are already written and verified. |
| **`tests/check_report.txt` generation** | **Full Reuse (100%)** | Formatted report output logging leaks, generic headings, and out-of-scope match scores. | Reusable as the automated quality assurance sign-off artifact. |
| **`review/*.csv` workflow** | **Full Reuse (100%)** | Human review loop (draft question generation $\rightarrow$ manual verification $\rightarrow$ mark `status="ok"` $\rightarrow$ compilation). | Essential for ensuring legal expert review of scenarios and multi-hop queries. |

---

## 2. Components Requiring Modification

### 2.1 `build_tests.py` (Modifications Required)
1. **Support Extended Schema:**
   - Currently, `build_tests.py` only extracts `id`, `type`, `law`, `question`, `options`, `answer`, `source_id`, and `split`.
   - **Update Needed:** Ingest `category` (`statutory_rule`, `factual_scenario`, `multi_hop`, `out_of_scope`), `expected_citations` (list of dicts supporting multi-section citations), `is_answerable`, `refusal_required`, `required_reasoning_points`, and `expert_verified`.
2. **Support Free-Text & Multi-Hop Categories:**
   - Add handling for questions without options (where `options` is `None` or empty dict) for Categories 2 (free-text variant), 3 (multi-hop), and 5 (retrieval queries).
3. **Draft Sources:**
   - Ingest from updated review CSVs: `review/mcq_draft.csv`, `review/scenarios_draft.csv`, `review/multihop_draft.csv`, `review/retrieval_draft.csv`, and `review/oos_draft.csv`.

### 2.2 `split_mcq.py` (Modifications Required)
1. **Dynamic Split Configuration:**
   - Currently hardcoded for 20 dev and 40 final items (`total_dev=20`, checks `len == 20` and `40`).
   - **Update Needed:** Generalize to split the 180 answerable MCQs/scenarios into:
     - **Dev Benchmark:** 60 items (stratified across category and law).
     - **Final Test Benchmark:** 120 items (strictly held-out).
2. **Stratification Across Categories:**
   - Stratify not only by `(item["law"], item["type"])`, but by `(item["law"], item["category"])` to ensure scenarios, rules, and penal provisions are evenly balanced across splits.

### 2.3 `check_tests.py` (Modifications Required)
1. **Stricter Heading Leakage Threshold:**
   - Currently flags `heading_overlap >= 0.60`.
   - **Update Needed:** Lower threshold to `0.35` and check for substring phrase matches $>3$ tokens to completely eliminate the heading leaks seen in `retrieval_test.json`.
2. **Schema and Multi-Citation Verification:**
   - Validate that every citation listed in `expected_citations` exists in `chunks.json`.
   - Verify that all questions flagged as `refusal_required == True` have `is_answerable == False` and empty `options`/designated refusal target.
3. **Lexical Leakage Screening on Question Bodies:**
   - Flag questions that contain literal statutory references (e.g. `"Section 302"`, `"Article 19"`) unless explicitly categorized as statutory interpretation queries.

---

## 3. New Files and Scripts Genuinely Necessary

Only **two new small files** are needed; all other operations can be accommodated by modifying existing files.

1. **`review/scenarios_draft.csv` (New Data Input File):**
   - Holds draft factual scenario questions and multi-hop questions for expert verification before building.
2. **`check_contamination.py` (New Validation Script, ~60 LOC):**
   - Validates that test benchmark IDs and raw test questions have **zero overlap** with any training dataset prepared for fine-tuning.
   - Computes n-gram containment ($n=8$) and cosine similarity between any training corpus and `tests/benchmark_test.json`.

---

## 4. Question Schema and Train/Dev/Test Separation

### 4.1 Schema Implementation
All questions compiled by `build_tests.py` will produce a unified format saved to `tests/`:
- `tests/benchmark_test.json` (The complete 320-item final test benchmark).
- `tests/benchmark_dev.json` (The 80-item dev set for prompt tuning and threshold calibration).

```json
{
  "id": "scenario_ppc_042",
  "category": "factual_scenario",
  "law": "ppc",
  "question": "A person knowingly publishes an altered photograph...",
  "options": {"A": "...", "B": "...", "C": "...", "D": "..."},
  "answer": "B",
  "expected_citations": [
    {"law": "peca", "number": "21", "chunk_id": "peca-21"}
  ],
  "is_answerable": true,
  "refusal_required": false,
  "required_reasoning_points": ["Cites PECA Section 21", "Maximum 5 years"],
  "split": "test",
  "expert_verified": true
}
```

### 4.2 Separation Protocol
- **Dev Set (80 items):** Used exclusively for system prompt tuning, retrieval hyperparameter selection ($k$, rerank threshold), and parser calibration.
- **Test Set (320 items):** Strictly quarantined. Run only once during final multi-arm evaluation.
- **Fine-Tuning Training Set:** Must be generated strictly from designated training section chunks (e.g., 800 of 1,013 sections in `chunks.json`), while test scenario questions are linked to the 213 held-out sections, guaranteeing zero data leakage.

---

## 5. Automated Validation Rules for `check_tests.py`

| Check | Target File(s) | Rule / Threshold | Automated Action |
|---|---|---|---|
| **Heading Leakage** | All questions | Content-word overlap with target chunk heading $< 0.35$; no verbatim $>3$-word title spans. | Flag as `LEAK_HEADING` and fail validation. |
| **Duplicates** | All test sets | MD5 hash of lowercase, punctuation-stripped question text must be unique. | Flag as `DUPLICATE_QUESTION` and reject build. |
| **Citation Traceability** | `expected_citations` | Every `chunk_id` must exist in `chunks.json`. | Flag as `ORPHAN_CITATION` and reject build. |
| **Answer Key Integrity** | All MCQs | `answer` in `["A", "B", "C", "D"]`, exactly 4 unique non-empty options. | Flag as `INVALID_MCQ_OPTIONS`. |
| **Refusal Consistency** | Out-of-scope | `is_answerable == false` and `refusal_required == true`. | Flag as `INVALID_REFUSAL_METADATA`. |
| **Contamination Guard** | Train vs. Test | Max 8-gram lexical overlap between train and test questions $= 0$. | Flag as `DATASET_CONTAMINATION`. |

---

## 6. Recommended Implementation Order

To ensure uninterrupted progress and zero regressions:

```
Step 1: Update Verification Core (check_tests.py)
   ├── Add stricter heading-overlap threshold (0.35)
   ├── Add MD5 question deduplication check
   └── Add multi-citation chunk existence check

Step 2: Update Compiler (build_tests.py)
   ├── Extend parser to support the expanded JSON schema
   ├── Ingest new scenario and multi-hop review CSVs
   └── Enforce "status == ok" and "expert_verified == True" checks

Step 3: Prepare Review CSVs in review/
   ├── Populate review/scenarios_draft.csv (60 scenarios)
   ├── Populate review/multihop_draft.csv (30 multi-hop)
   ├── Expand review/mcq_draft.csv (120 rules) and oos_draft.csv (50 OOS)
   └── Perform legal verification and mark verified rows as "ok"

Step 4: Update Splitter (split_mcq.py)
   ├── Configure stratified split (80 Dev / 320 Final Test)
   └── Generate tests/benchmark_dev.json and tests/benchmark_test.json

Step 5: Run Automated Benchmark Audit
   ├── Execute python check_tests.py
   └── Inspect tests/check_report.txt to confirm 0 leaks and 0 invalid items
```
