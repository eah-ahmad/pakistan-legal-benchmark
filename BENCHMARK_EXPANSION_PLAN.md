# Legal Pathway — Benchmark Expansion Plan (400 Questions: 80 Dev + 320 Final)

**Document:** `BENCHMARK_EXPANSION_PLAN.md`  
**Date:** November 17, 2026  
**Project:** Legal Pathway — Comparative Legal QA for Pakistani Law  
**Status:** Architectural Plan & Protocol Specification  

---

## 1. Inspection and Audit of Existing Benchmark Items

Before designing the 400-question benchmark expansion, a comprehensive audit of the existing 108 prototype items across `tests/` was conducted to establish reusability, structural flaws, and exclusion criteria.

### 1.1 Existing Item Audit Summary

| Existing File | Current Count | Quality & Diagnostic Findings | Reusability Verdict |
|---|:---:|---|---|
| `tests/retrieval_test.json` | 30 | **100% Heading Leakage:** As established in `tests/check_report.txt`, all 30 queries (`rq001`–`rq030`) verbatim copy the target chunk heading (e.g. `rq001: "What does Pakistani law provide regarding: Review of judgements or orders by the Federal Constitutional Court?"`). | **UNSUITABLE for Final Benchmark.** Must be discarded or completely rewritten into natural legal search queries without verbatim headings or numbers. |
| `tests/mcq_dev.json` & `tests/mcq_final.json` | 60 (20 dev / 40 final) | **Mechanical Reverse-Lookups:** 100% of questions are generated from two synthetic templates: `lookup` (*"What is the heading of Section X?"*) and `define` (*"Which section deals with [Heading]?"*). As logged in `check_report.txt`, 12 items suffer from ambiguous generic headings (*"Provincial Ministers"*, *"The Cabinet"*, *"Definitions"*). | **Severely Limited Reusability.** Only a small subset (~15–20 items) can be salvaged by converting them into substantive penalty/element MCQs. The pure heading-lookup items must be excluded from the final benchmark. |
| `tests/out_of_scope.json` | 18 | **Clean Structural Refusal Categories:** Effectively categorizes fake sections (PPC 999, Constitution Art 580), foreign jurisdictions (US 1st Amdt, Indian Penal Code 379), and non-legal queries. | **HIGHLY REUSABLE (100%).** All 18 items are retained as verified negative/refusal cases to seed the 50-item final refusal pool. |

---

## 2. Evaluation of Category Distribution and Dev/Final Allocation

### 2.1 Critical Assessment of the Proposed Final Set (320 Items)
The proposed 320-item distribution was evaluated against the project's core research objectives:
1. **Statutory Rules, Elements, and Penalties (MCQs: 120 items):**  
   *Assessment:* **Methodologically sound.** 120 MCQs provide sufficient statistical power to compute McNemar's tests and confidence intervals across all four experimental arms. However, questions must test *substantive rules* (e.g. elements of an offence, terms of imprisonment, monetary fines, constitutional quorums) rather than verbatim heading-to-number lookups.
2. **Factual Legal Scenarios (60 items: 40 MCQs + 20 Free-Text):**  
   *Assessment:* **Essential for practical validity.** Real-world legal queries do not ask for statutory sections in isolation; they present factual situations (e.g., electronic harassment, unlawful confinement, joint liability).
3. **Complex Multi-Hop Legal Questions (30 items: Free-Text):**  
   *Assessment:* **Crucial for testing advanced synthesis.** Tests cross-provision interaction (e.g. PECA Section 28 incorporating the PPC, or Constitutional fundamental rights under Art. 199 restricting executive penal powers).
4. **Negative, Unanswerable, and Out-of-Corpus Questions (50 items):**  
   *Assessment:* **Core metric requirement.** Directly evaluates the project's primary research objective of *evidence-based refusal and hallucination mitigation*. Distinguishes between fake sections, out-of-corpus laws, missing context, and ambiguous provisions.
5. **Natural-Language Statutory Retrieval Questions (60 items):**  
   *Assessment:* **Vital for RAG retrieval evaluation.** Tests dense vector search and cross-encoder reranking under realistic natural-language phrasing without heading leakage.

### 2.2 Recommended Category Distribution Across Both Splits (Total: 400 Items)
To ensure the Development Set (80 items) is an exact proportional miniature of the Final Set (320 items) while containing zero overlapping questions, scenarios, or facts, the 1:4 ratio is maintained strictly across all categories:

| Question Category | Dev Split (80 Items) | Final Test Split (320 Items) | Total Combined Pool | Target Evaluation Modality |
|---|:---:|:---:|:---:|---|
| **1. Statutory Rules, Elements & Penalties** | 30 | 120 | 150 | MCQ (Single Answer A–D) |
| **2. Factual Legal Scenarios** | 15 | 60 | 75 | Mixed (10 MCQ / 5 Free-Text in Dev; 40 MCQ / 20 Free-Text in Final) |
| **3. Complex Multi-Hop Inquiries** | 8 | 30 | 38 | Free-Text Synthesis |
| **4. Negative, Unanswerable & Out-of-Corpus** | 12 | 50 | 62 | Refusal / Certainty Evaluation |
| **5. Natural-Language Retrieval Benchmark** | 15 | 60 | 75 | Information Retrieval (Recall@k, MRR) |
| **Total Questions** | **80** | **320** | **400** | |

### 2.3 Statutory Allocation Across Laws
To prevent skew toward any single statute, the 400 questions are balanced proportionally according to the substantive breadth of the codified text:
- **Pakistan Penal Code (PPC):** ~190 questions (47.5%) — reflects the large breadth of offences, elements, exceptions, and punishments across 511 sections.
- **Constitution of Pakistan:** ~140 questions (35.0%) — fundamental rights, executive powers, 26th and 27th Amendments.
- **PECA 2016:** ~70 questions (17.5%) — specialized cybercrime offences, investigative powers, and cross-statute links.

---

## 3. Standardized Benchmark Question Schema

Every question in the expanded benchmark will be serialized in JSON using a comprehensive, auditable schema.

```json
{
  "id": "scenario_final_ppc_042",
  "category": "factual_scenario",
  "law": "ppc",
  "split": "final",
  "difficulty": "medium",
  "question": "A person knowingly publishes an altered photograph of a woman online to cause her harm. Which specific provision of Pakistani law applies, what is the offence, and what is the maximum term of imprisonment?",
  "options": {
    "A": "PPC Section 500, Defamation, 2 years",
    "B": "PECA Section 21, Offences against modesty of a natural person, 5 years",
    "C": "PECA Section 14, Unauthorized use of identity information, 3 years",
    "D": "PPC Section 292, Sale of obscene books, 3 months"
  },
  "answer": "B",
  "expected_citations": [
    {
      "chunk_id": "peca-21",
      "law": "peca",
      "provision_type": "Section",
      "number": "21",
      "title": "Offences against modesty of a natural person and minor"
    }
  ],
  "is_answerable": true,
  "refusal_required": false,
  "refusal_type": "none",
  "required_reasoning_points": [
    "Identifies PECA 2016 as governing electronic modesty violations",
    "Identifies Section 21 as the specific applicable section",
    "Identifies maximum imprisonment term of 5 years"
  ],
  "source_references": [
    {
      "file": "raw/peca.txt",
      "chunk_id": "peca-21",
      "statute_edition": "Act XL of 2016"
    }
  ],
  "distractor_explanations": {
    "A": "PPC Section 500 governs general defamation, not specific cyber modesty offences under special law",
    "C": "PECA Section 14 governs unauthorized identity information use, not modesty violations",
    "D": "PPC Section 292 applies to physical obscene literature"
  },
  "verification_status": {
    "verified_against_corpus": true,
    "legal_expert_verified": true,
    "reviewer_initials": "LE_MA",
    "adjudication_status": "uncontested",
    "verification_date": "2026-11-20"
  }
}
```

---

## 4. Gold-Answer and Citation Verification Procedure

A matching section number does **not** prove an answer is legally correct. Every question must undergo an evidence-grounded verification procedure against the frozen repository text.

```
                     ANSWER VERIFICATION PIPELINE
                                   |
+---------------------------------------------------------------------+
| 1. Statutory Grounding Check                                        |
|   Locate chunk in chunks.json. Read full text.                      |
|   Confirm every rule, penalty, and phrase is supported by the text. |
+---------------------------------------------------------------------+
                                   | Verified
                                   v
+---------------------------------------------------------------------+
| 2. Citation Existence & Syntax Audit                                |
|   Check chunk_id exists in chunks.json.                             |
|   Verify law name and section format matches [Law Section N].       |
+---------------------------------------------------------------------+
                                   | Verified
                                   v
+---------------------------------------------------------------------+
| 3. Substantive Legal Review (Scenarios & Multi-Hop)                 |
|   Licensed legal expert verifies fact pattern meets legal threshold.|
|   Confirm distractors are plausible but demonstrably incorrect.    |
+---------------------------------------------------------------------+
                                   | Disputed / Ambiguous
                                   v
+---------------------------------------------------------------------+
| 4. Second-Review Adjudication                                       |
|   If two reviewers disagree on interpretation, resolve or discard.  |
|   If law is split/silent, move to Category 4 (Uncertainty).         |
+---------------------------------------------------------------------+
```

### 4.1 Verification Criteria by Question Category
1. **Category 1 (Rules & Penalties):** Programmatic verification against `chunks.json`. Cross-check exact penalty numbers (years, fines) against statutory text.
2. **Category 2 (Scenarios):** Mandatory legal expert review. Ensure that described mens rea and acts satisfy legal elements under Pakistani case law and statutes.
3. **Category 3 (Multi-Hop):** Mandatory dual review. Confirm cross-statute interaction is legally sound (e.g. confirming CrPC applicability via PECA Sec 43 vs PPC Sec 4/5).
4. **Category 4 (Negative & Refusal):**
   - *Fake sections:* Programmatic verification that section number $> \max(\text{sections})$ or is not in `chunks.json`.
   - *Out-of-corpus laws:* Verify question concerns external laws (CrPC 1898, QSO 1984, Companies Act 2017, PECA Amendment Act 2025).
5. **Adjudication Procedure:** When a question involves conflicting statutory readings or unsettled High Court interpretations, it must **not** be forced into a single right answer. It must either be rewritten to remove ambiguity or reclassified into Category 4 (`refusal_type: "inherent_ambiguity"`).

---

## 5. Contamination Controls and Quarantine Architecture

The benchmark must be protected against contamination from any future Supervised Fine-Tuning (SFT) dataset.

```
+---------------------------------------------------------------------------+
|                          FROZEN STATUTORY SOURCE                          |
|         Constitution (1973) | Penal Code (1860) | PECA (2016)             |
+---------------------------------------------------------------------------+
                     |                                         |
                     v                                         v
+---------------------------------------+   +-------------------------------------+
|       RAG RETRIEVAL CORPUS            |   |     BENCHMARK QUESTION QUARANTINE   |
|   100% of chunks.json indexed         |   | 400 Questions: 80 Dev + 320 Final   |
|   in ChromaDB (cosine space)          |   | (Quarantined in tests/*.json)       |
+---------------------------------------+   +-------------------------------------+
                     |                                         |
                     |                                         v
                     |                      +-------------------------------------+
                     |                      | 4-Tier Contamination Screening      |
                     |                      | Tier 1: Exact Text Match            |
                     |                      | Tier 2: Normalized MD5 Hash         |
                     |                      | Tier 3: 8-Gram Containment (>= 0.20)|
                     |                      | Tier 4: Cosine Similarity (>= 0.82) |
                     |                      +-------------------------------------+
                     |                                         |
                     v                                         v
+---------------------------------------+   +-------------------------------------+
|       FOUR-ARM EVALUATION RUNNER      |   |        SFT TRAINING DATASET         |
|   Evaluates Arms 1, 2, 3, 4           |<--|  Cleaned and Verified               |
|   against the Quarantined Benchmark   |   |  (data/train_sft.jsonl)             |
+---------------------------------------+   +-------------------------------------+
```

### 5.1 Distinguishing Legitimate Statutory Overlap from Leakage
- **Legitimate Overlap:** SFT training examples and benchmark test questions will legitimately quote the same underlying statutory clauses (e.g., both citing `"punished with imprisonment which may extend to seven years"` under PECA Section 11). This is **not** contamination; it is domain knowledge.
- **Question-Level Contamination (Illegal Leakage):** SFT training examples must not share the same fact patterns, question phrasing, distractor options, or specific scenario formulations as benchmark items.
- **Screening Rule:** Any SFT pair triggering Tier 3 (8-gram overlap) or Tier 4 (dense similarity) against a benchmark question must be audited by a human reviewer. If it tests the identical scenario or prompt stem, it is permanently excised from the training set.

---

## 6. Strict Legal Source Boundaries and Exclusions

The benchmark must evaluate models exclusively on the verified statutory documents in the repository:

1. **Constitution of Pakistan, 1973 (`raw/constitution.txt`):**  
   - Reflects codified amendments up to and including the **26th Amendment Act, 2024** (Constitutional Benches under Art. 191A & 202A) **and** the **27th Amendment Act, 2025** (Chapter 1A: Federal Constitutional Court under Art. 175B–175L and amended Art. 175A).  
   - Benchmark questions on constitutional benches or the FCC are **valid and answerable** because the statutory provisions exist in `chunks.json`.
2. **Pakistan Penal Code, 1860 (`raw/ppc.txt`):**  
   - Codified federal text up to **Dated: 30-11-2025**, including omissions under the **Criminal Laws (Amendment) Act, 2025**.  
   - Benchmark questions on codified PPC sections are **valid and answerable**.
3. **PECA 2016 (`raw/peca.txt`):**  
   - Contains **only** the original enacted text of **Act No. XL of 2016**.  
   - **Mandatory Exclusion:** The **PECA (Amendment) Act, 2025 is absent** from the repository. Questions asking about provisions introduced by the 2025 PECA amendment must be categorized as **Category 4 (Out-of-Corpus Refusal)** and must require refusal. They must **never** be included as answerable benchmark items.

---

## 7. Acceptance Criteria Before Benchmark Freeze

Before the 400-question benchmark is declared frozen and ready for model evaluation, it must satisfy all of the following gates:

1. **Gate 1 — Total Volume & Allocation Check:**  
   Exactly 80 items in `tests/benchmark_dev.json` and exactly 320 items in `tests/benchmark_test.json`.
2. **Gate 2 — Zero Item/ID Overlap:**  
   $\text{dev\_ids} \cap \text{final\_ids} = \emptyset$. Zero duplicate questions across splits via normalized MD5 hashing.
3. **Gate 3 — Zero Heading Leakage:**  
   Every question in Category 5 (Retrieval) and Category 1 (Rules) must have `heading_overlap_ratio < 0.35` against its target chunk in `chunks.json`. Zero questions containing literal target headings.
4. **Gate 4 — 100% Citation Traceability:**  
   Every `chunk_id` referenced in `expected_citations` must exist in `chunks.json`. Zero orphaned citations.
5. **Gate 5 — Option and Answer Key Integrity:**  
   Every MCQ must have exactly 4 unique options, and `answer` must match one of `A`, `B`, `C`, or `D`.
6. **Gate 6 — Mandatory Legal Review Logged:**  
   100% of scenarios (75 items) and multi-hop questions (38 items) must have `legal_expert_verified: true` with reviewer initials recorded.
7. **Gate 7 — Validation Suite Clean Pass:**  
   `python check_tests.py` must run and produce zero errors or unresolved critical flags in `tests/check_report.txt`.

---

## 8. Remaining Methodological Decisions & Readiness Assessment

### 8.1 Remaining Decisions Before Generation Tooling
1. **Review CSV File Organization:** Confirm whether draft questions will be staged in separate review CSV files:
   - `review/mcq_rules_draft.csv` (150 rules/penalties)
   - `review/scenarios_draft.csv` (75 scenarios)
   - `review/multihop_draft.csv` (38 multi-hop)
   - `review/refusal_draft.csv` (62 unanswerable/out-of-corpus)
   - `review/retrieval_draft.csv` (75 natural retrieval queries)
2. **Free-Text Scoring Metric Formulation:** Finalize whether free-text scenarios and multi-hop questions in `evaluate.py` will be scored via automated token-level F1 / citation precision or via an LLM-as-a-judge prompt against `required_reasoning_points`.

---

### Final Recommendation

**The Benchmark Expansion Plan is COMPLETE, METHODOLOGICALLY SOUND, and READY for question drafting tooling.**

All statutory boundaries (including the 26th/27th Constitutional Amendments and the exclusion of the PECA 2025 Amendment), verification workflows, category distributions, and contamination safeguards are established. Once the draft CSV files are authored and verified by legal reviewers, the upgraded `build_tests.py` and `split_mcq.py` pipelines will compile the final 400-question benchmark.
