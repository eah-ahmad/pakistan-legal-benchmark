# Legal Pathway — Benchmark Design Proposal

**Document:** `BENCHMARK_DESIGN_PROPOSAL.md`  
**Date:** November 17, 2026  
**Focus:** Research validity, rigorous comparative benchmarking, dataset hygiene, and cost/latency tracking across Pakistani Constitutional and Criminal Law.

---

## 1. Question Categories and Recommended Sample Sizes

To achieve statistical validity while keeping computational costs manageable on standard GPU runtimes, the benchmark prioritizes depth, diversity, and ecological validity over uncurated volume.

### Overview of Categories & Recommended Allocations

| Category | Description / Research Purpose | Prototype (Current) | Recommended (Essential) | Scaled (Optional / Future) |
|---|---|:---:|:---:|:---:|
| **1. Statutory Rule & Penalty (MCQ)** | Tests direct legal knowledge of specific penalties, elements of offences, or constitutional powers without quoting headings. | 40 | **120** (40 Constitution, 50 PPC, 30 PECA) | 240 |
| **2. Factual Legal Scenarios (MCQ & Free-Text)** | Multi-sentence practical scenarios (e.g. cyber harassment, property trespass, police detention) testing application and citation faithfulness. | 0 | **60** (20 Constitution, 25 PPC, 15 PECA) | 120 |
| **3. Complex / Multi-Hop Inquiries (Free-Text)** | Cross-provision interaction (e.g., PECA Section 28 invoking PPC; constitutional fundamental rights restricting penal enactments). | 0 | **30** (10 per statute area) | 60 |
| **4. Negative & Unanswerable / Out-of-Scope** | Tests evidence-based refusal across: (a) non-existent sections, (b) foreign jurisdictions, (c) civil/corporate laws, (d) non-legal queries. | 18 | **50** (15 fake sections, 15 foreign, 10 other domestic law, 10 general) | 100 |
| **5. Realistic Retrieval Benchmark** | Natural user queries without section numbers or headings to test dense semantic search and cross-encoder reranking. | 30 (100% leaked) | **60** (20 Constitution, 25 PPC, 15 PECA) | 120 |
| **Total Test Benchmark** | | **88** | **320** | **640** |

- **Essential Requirement:** A test set of **~250–320 items** (with ~180 answerable MCQs/scenarios and 50 refusals) provides sufficient sample size to compute 95% bootstrap confidence intervals and McNemar's tests ($\Delta \ge 5\%$ statistically detectable at $p < 0.05$).
- **Optional Improvement:** Expanding to 600+ items across subordinate legislation and procedural codes (CrPC).

---

## 2. Required Fields for Each Question

To guarantee automated evaluation, traceability, and metric repeatability, each benchmark item must adhere to a standardized JSON schema.

### Standardized Schema Fields

```json
{
  "id": "scenario_ppc_042",
  "category": "factual_scenario",
  "law": "ppc",
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
      "law": "peca",
      "provision_type": "Section",
      "number": "21",
      "chunk_id": "peca-21"
    }
  ],
  "is_answerable": true,
  "refusal_required": false,
  "required_reasoning_points": [
    "Identifies PECA 2016 as governing cyber modesty violations",
    "Cites Section 21",
    "Identifies 5-year maximum imprisonment"
  ],
  "distractor_types": {
    "A": "wrong_statute_defamation",
    "C": "wrong_section_same_act",
    "D": "irrelevant_ppc_provision"
  },
  "split": "test",
  "expert_verified": true
}
```

---

## 3. Prevention of Heading Leakage, Duplicates, and Contamination

### 3.1 Eliminating Heading and Lexical Leakage (Essential)
1. **Rule of Paraphrasing:** The question text must **never** contain the verbatim section heading or statutory title.
2. **Automated Lexical Guardrails:** Run an automated verification script (extending `check_tests.py`) that enforces:
   - `heading_overlap_ratio < 0.35` (maximum allowable content-word overlap).
   - Strict ban on statutory numbers within the question body unless assessing interpretation of that section.
   - Rejection of generic template stems like `"What is the subject of Section X?"`.

### 3.2 Duplicate and Variant Elimination (Essential)
- Hash-based deduplication on normalized question tokens: $H(Q_{\text{norm}})$.
- Cross-statute definition collision prevention: Distinct labels for identical generic headings (e.g. `PPC Sec 40: Definitions` vs `PECA Sec 2: Definitions`).

### 3.3 Strict Train / Test Contamination Prevention (Essential)
- **Zero-Overlap Partitioning:** Benchmark test IDs (`tests/*.json`) must be cryptographically hashed and quarantined.
- **Corpus vs. Fine-Tuning Split:**  
  - If LoRA/QLoRA is trained on statutory Q&A pairs, training pairs must be generated **only** from a designated training subset of sections (e.g., 80% of `chunks.json`), while test benchmark questions are sourced **strictly** from the 20% held-out sections.
  - Or, if fine-tuning is done on all sections (continual pre-training style), evaluation must rely heavily on *unseen scenario applications* and *held-out counterfactual queries* to measure generalization rather than statutory verbatim recall.

---

## 4. Evaluation Metrics for Each Category

| Question Category | Primary Metric | Secondary Metric | Evaluation Method |
|---|---|---|---|
| **MCQs (Statutory & Scenario)** | MCQ Accuracy (%) | Citation Faithfulness (%) | Deterministic option parsing + strict statutory regex matching. |
| **Citations** | Exact Citation Precision & Recall | Grounded Citation Distance | Verify that cited law and section match `expected_citations` within ground truth. |
| **Negative / Out-of-Scope** | Refusal Rate (%) | Spurious Citation Rate (%) | Exact match or verified refusal regex (`is_refusal()`). Penalty if any section citation is generated. |
| **Free-Text & Multi-Hop** | Faithfulness / Hallucination Rate | Answer Relevance | NLI / LLM-as-a-judge against retrieved statutory excerpts. |
| **Retrieval Corpus** | Recall@5, MRR | Context Hit@5 (%) | Parent section overlap in retrieved top-5 passages. |

- **Essential Requirement:** Automated scoring of MCQ Accuracy, Citation Faithfulness, and Out-of-Scope Refusal Rate.
- **Optional Improvement:** LLM-as-a-judge / NLI entailment scoring for multi-hop free-text responses to automate hallucination measurement.

---

## 5. Protocol for Fair Comparison Across All Four Arms

To eliminate experimental bias across:
- **Arm 1:** Base Model (Control)
- **Arm 2:** Base Model + RAG
- **Arm 3:** Fine-Tuned Model (LoRA/QLoRA)
- **Arm 4:** Fine-Tuned Model + RAG

### Controlled Experimental Invariants:
1. **Identical Test Set:** All 4 arms run against the exact same test files.
2. **Symmetric System Prompt:** All 4 arms receive the unified prompt template established in `PROMPT_ALIGNMENT_AUDIT.md`.
3. **Identical Generation Hyperparameters:**
   - Decoding: Greedy decoding (`temperature = 0.0`, `do_sample = False`).
   - Token Budget: Max 80 new tokens for MCQs; max 300 new tokens for free text.
   - Output Cleaning: Identical stop-words, EOS handling, and `<think>` tag stripping.
4. **Isolating Adaptation Gains:**
   - Baseline performance serves as the empirical measure of pre-training memorization / contamination.
   - RAG gains quantify retrieval impact.
   - Fine-tuning gains quantify parameter-adapted statutory knowledge and citation format compliance.
   - Hybrid gains quantify complementary interaction between retrieved evidence and fine-tuned legal comprehension.

---

## 6. Token Usage, Latency, and Computational Cost Measurements

To evaluate real-world deployability alongside academic accuracy, each query run must log runtime and computational resource metrics.

### Required Telemetry Logged Per Query:
1. **Prompt Tokens:** Total input tokens (system + context + question).
2. **Completion Tokens:** Generated output tokens.
3. **Retrieval Latency (ms):** ChromaDB vector search + CrossEncoder rerank time (Arms 2 & 4 only).
4. **Generation Latency (ms):** Time-to-first-token (TTFT) and end-to-end LLM inference time.
5. **Total Wall-Clock Time (ms):** Cumulative query response latency.
6. **Hardware Footprint:** Peak VRAM consumption (GB) logged per arm.

### Summary Reporting Table (Required in Final Results):
```
| Arm | MCQ Acc (%) | Cite Acc (%) | Refusal (%) | TTFT (ms) | Total Latency (s) | Prompt Toks | Output Toks |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Base Model | | | | | | | |
| Base + RAG | | | | | | | |
| Fine-Tuned | | | | | | | |
| FT + RAG | | | | | | | |
```

---

## 7. Expert Verification Requirements

To ensure research integrity while maximizing development efficiency, human verification must be targeted where automation fails.

### A. Mandatory Legal Expert Verification (Essential)
1. **Factual Legal Scenarios (Category 2):** A licensed Pakistani lawyer or legal scholar must verify that the scenario elements strictly meet the statutory threshold under the PPC/PECA.
2. **Multi-Hop Inquiries (Category 3):** Verification that cross-statute interactions are legally sound and reflect current judicial interpretation.
3. **MCQ Distractor Validity:** Reviewing options to ensure distractors are plausible but demonstrably incorrect under Pakistani law, avoiding ambiguous "all of the above" or non-exclusive statutory overlaps.
4. **Out-of-Scope Negative Queries:** Verification that "fake section numbers" are truly non-existent in the relevant act's historical amendments.

### B. Automatable Without Expert Review (Non-Essential)
1. **Direct Statutory Penalties (Category 1):** Traceable programmatically to section text (e.g., verifying penalty text via regex matching against `chunks.json`).
2. **Syntax and Format Validation:** Automated options validation (4 unique options, single correct key A–D).
3. **Lexical Leakage Screening:** Automated word overlap and n-gram filtering against section headings.

---

## 8. Summary: Essential vs. Optional Improvements

| Dimension | Essential Requirements (Must Implement) | Optional Improvements (Post-V1) |
|---|---|---|
| **Benchmark Size** | Expand MCQs to 120, Scenarios to 60, OOS to 50 (Total ~320). | Scale to 600+ questions including CrPC and civil codes. |
| **Leakage Elimination** | Remove 100% heading overlap from retrieval and MCQ questions. | Paraphrase with multi-dialect query expressions (Urdu-English code-switching). |
| **Evaluation Metrics** | Automated MCQ accuracy, citation accuracy, and refusal rate. | Automated LLM-as-a-judge / NLI faithfulness metrics for open generation. |
| **Telemetry** | Record prompt/output tokens, retrieval latency, and generation latency. | Track energy consumption / carbon footprint per inference. |
| **Verification** | Legal review of all 60 scenarios and 30 multi-hop queries. | Dual-blind legal review with inter-annotator agreement ($\kappa$). |
