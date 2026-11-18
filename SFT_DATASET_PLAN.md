# Supervised Fine-Tuning (SFT) Dataset Architecture and Design Plan

**Document:** `SFT_DATASET_PLAN.md`  
**Revision:** 2.1 (Post-Audit Statutory Verification & Readiness Correction)  
**Date:** November 17, 2026  
**Project:** Legal Pathway — Comparative Legal QA for Pakistani Law  
**Status:** Architecture and Design Specification  

---

## 1. Executive Summary and Conceptual Framework

This document specifies the dataset architecture, schema, contamination safeguards, training distribution, and uncertainty policies for the Supervised Fine-Tuning (SFT) phase of the Legal Pathway project. The research compares four experimental arms on Pakistani Constitutional and Criminal Law:
1. **Base Model Control** (`Qwen2.5-3B-Instruct`)
2. **Base Model + RAG**
3. **Fine-Tuned Model (LoRA/QLoRA)**
4. **Fine-Tuned Model + RAG**

The primary purpose of fine-tuning is domain adaptation: teaching the model structured legal reasoning, bracketed statutory citation syntax (e.g., `[PPC Section 302]`), and calibrated refusal behavior, while ensuring seamless operation both standalone (Arm 3) and when conditioned on retrieved evidence (Arm 4).

### Key Methodological Decisions Adopted:
- **No Statutory Chunk Withholding:** The RAG retrieval index will index 100% of the verified statutory corpus (`chunks.json`, 1,013 parent sections). Withholding statutory chunks would artificially cripple retrieval recall and confound comparative metrics.
- **Strict Question-Level Quarantine:** Test-set integrity is maintained by quarantining benchmark questions, options, scenario facts, and annotations—not the underlying statutory corpus.
- **Dual-Mode SFT Conditioning (60/40 Split):** A provisional distribution of 60% Standalone QA and 40% Context-Grounded QA is established as an experimental starting point to balance parametric legal recall with open-book evidence faithfulness.
- **Assistant-Only Loss Masking:** Backpropagation loss will be computed strictly on assistant completion tokens (`output`), masking system, instruction, and context tokens.
- **Granular Refusal Policy:** Nuanced handling of distinct uncertainty modes rather than forcing an identical one-size-fits-all refusal string.

---

## 2. Statutory Source Baseline Registry: Verified Files vs. Law in Force

To prevent legal anachronisms and ensure alignment between the RAG index and fine-tuning targets, the project strictly distinguishes:
1. **The Frozen Experimental Source Baseline:** The exact text extracted in `raw/*.txt` and indexed in `chunks.json`.
2. **The Law in Force as of the Cutoff Date (November 2026):** Actual historical enactments and amendments.
3. **Provisions Intentionally Excluded from the Experiment:** Legislation or post-baseline enactments absent from the repository.

### 2.1 Statutory Baseline Registry (Direct File Inspection)

| Statutory Instrument | Source File in Repo | Verified Text Content & Amendments Present in Repo | Law in Force as of Cutoff Date (Nov 2026) | Status in Experiment & Excluded Provisions |
|---|---|---|---|---|
| **Constitution of the Islamic Republic of Pakistan, 1973** | `raw/constitution.txt` (extracted from `Pakistan_Constitution.pdf`, 467 KB; 191 chunks in `chunks.json`) | Contains both the **26th Amendment Act, 2024 (Act XXVI of 2024)** (Constitutional Benches under Art. 191A & 202A) **AND** the **27th Amendment Act, 2025 (Act XXXII of 2025)** (establishing Chapter 1A: The Federal Constitutional Court under Art. 175B–175L and amended Art. 175A). | The 26th Amendment (2024) and 27th Amendment (2025) are both enacted constitutional law. | **Included:** Articles 1 through 280 as captured in `raw/constitution.txt`, including Chapter 1A (Federal Constitutional Court).<br>**Excluded:** Subsequent subordinate court procedural rules or post-2025 constitutional proposals. |
| **Pakistan Penal Code (Act XLV of 1860)** | `raw/ppc.txt` (extracted from `Penal_code.pdf`, 522 KB; 766 chunks in `chunks.json`) | Codified text up to **Dated: 30-11-2025**. Explicitly reflects omissions by the **Criminal Laws (Amendment) Act, 2025 (Act XXVII of 2025)** (e.g. at lines 6747 and 7431). | Codified penal law reflecting the Criminal Laws (Amendment) Act, 2025. | **Included:** Sections 1 through 511 as present in `raw/ppc.txt`.<br>**Excluded:** Provincial criminal law amendments (e.g. Punjab/Sindh specific enactments); federal codified text is the sole authority. |
| **Prevention of Electronic Crimes Act, 2016 (PECA)** | `raw/peca.txt` (extracted from `PECA.pdf`, 105 KB; 56 chunks in `chunks.json`) | Enacted **Act No. XL of 2016** (Sections 1 through 56). Does **NOT** contain the subsequent **PECA (Amendment) Act, 2025**. | In the real world, PECA has been subject to the PECA (Amendment) Act, 2025 and contentious judicial challenges. | **Frozen Baseline Rule:** The project corpus contains **only** the original enacted 2016 text. The PECA Amendment Act, 2025 is **intentionally excluded** from positive training targets and must be treated as out-of-corpus. |

> [!IMPORTANT]
> **Corpus Alignment Rule:** Ground-truth legal correctness is strictly anchored to the text inside `raw/*.txt` and `chunks.json`. SFT generation must not generate answers or citations based on external amendments (e.g., PECA Amendment Act 2025) that do not exist in the project's retrieval index.

---

## 3. SFT Dataset Schema

Training examples will be stored in standard JSON Lines (`.jsonl`) format. Each line is an independent, validated training record.

### 3.1 Standard Record Schema

```json
{
  "id": "sft_train_ppc_0142",
  "category": "factual_scenario",
  "law": "ppc",
  "prompt_mode": "standalone",
  "instruction": "Analyze the legal scenario under Pakistani law. Identify the specific offence, cite the governing statutory provision, and specify the maximum penalty.",
  "input": "A person knowingly fabricates a false document intending that it will cause an innocent individual to be convicted of an offence punishable with death. What offence has been committed under the Pakistan Penal Code, under which section, and what is the punishment?",
  "output": "Under Pakistani criminal law, this act constitutes the offence of fabricating false evidence to procure a capital conviction.\n\nGoverning Provision:\n[PPC Section 194 - Giving or fabricating false evidence with intent to procure conviction of capital offence]\n\nAnalysis & Punishment:\nSection 194 of the Pakistan Penal Code provides that whoever gives or fabricates false evidence intending to cause any person to be convicted of an offence punishable with death shall be punished with imprisonment for life, or with rigorous imprisonment for a term which may extend to ten years, and shall also be liable to fine. If an innocent person is executed as a consequence, the offender may be punished with death or the imprisonment specified above.",
  "expected_citations": [
    {
      "chunk_id": "ppc-194",
      "law": "ppc",
      "law_name": "Pakistan Penal Code",
      "provision_type": "Section",
      "number": "194",
      "title": "Giving or fabricating false evidence with intent to procure conviction of capital offence"
    }
  ],
  "source_document": {
    "act_name": "Pakistan Penal Code (Act XLV of 1860)",
    "file_reference": "raw/ppc.txt",
    "verified_baseline": "Codified text as extracted (reflecting Criminal Laws Amdt Act 2025)"
  },
  "is_answerable": true,
  "refusal_type": "none",
  "context_grounded": false,
  "verification_status": {
    "verified_by_legal_expert": true,
    "reviewer_initials": "LE_MA",
    "verification_date": "2026-11-20"
  },
  "metadata": {
    "source_chunk_ids": ["ppc-194"],
    "requires_reasoning_points": [
      "Identifies offence under Section 194",
      "Recognizes capital intent element",
      "States penalty: life imprisonment or rigorous up to 10 years and fine"
    ],
    "intended_arms": ["ft_only", "hybrid_rag_ft"],
    "split": "train"
  }
}
```

### 3.2 Representation of Context-Grounded Records (`prompt_mode: "grounded"`)
When `context_grounded: true`, the `input` field contains the retrieved context block matching the exact format assembled by `rag_pipeline.py`:

```json
{
  "id": "sft_train_grounded_peca_0089",
  "category": "grounded_qa",
  "law": "peca",
  "prompt_mode": "grounded",
  "instruction": "Answer the question based strictly on the provided legal context. Cite your sources.",
  "input": "CONTEXT:\n[PECA Section 11 - Hate speech]\nWhoever prepares or disseminates information, through any information system or device, that advances or is likely to advance interfaith, sectarian or racial hatred, shall be punished with imprisonment for a term which may extend to seven years or with fine or with both.\n\nQUESTION:\nWhat is the maximum penalty for hate speech under PECA?",
  "output": "Based on the provided context, the offence of hate speech under the Prevention of Electronic Crimes Act is punishable with imprisonment for a term which may extend to seven years, or with fine, or with both.\n\nGoverning Provision:\n[PECA Section 11 - Hate speech]",
  "expected_citations": [
    {
      "chunk_id": "peca-11",
      "law": "peca",
      "number": "11",
      "title": "Hate speech"
    }
  ],
  "is_answerable": true,
  "refusal_type": "none",
  "context_grounded": true
}
```

### 3.3 Representation of Multiple Statutory Citations
For complex inquiries involving statutory interaction (e.g. PECA Section 28 incorporating the PPC, or Constitutional rights limiting penal procedures), `expected_citations` is an ordered list:
```json
"expected_citations": [
  {"chunk_id": "peca-28", "law": "peca", "number": "28", "title": "Pakistan Penal Code, 1860 (Act XLV of 1860) to apply"},
  {"chunk_id": "ppc-415", "law": "ppc", "number": "415", "title": "Cheating"}
]
```
The text in `output` must reflect all cited sections in bracketed format: `[PECA Section 28]`, `[PPC Section 415]`.

---

## 4. Training Data Categories and Uncertainty Typology

### 4.1 Granular Refusal and Uncertainty Categories

Rather than forcing an identical refusal sentence for every failure mode, the SFT dataset distinguishes four distinct uncertainty categories:

```
                                  UNCERTAINTY TYPOLOGY
                                           |
    +------------------+-------------------+-------------------+--------------------+
    |                  |                   |                   |                    |
    v                  v                   v                   v                    v
[ Unsupported     [ Out-of-Corpus     [ Missing-Context   [ Genuinely          [ Substantive
  Fake Section ]    Domestic Law ]      (RAG Failure) ]     Ambiguous Law ]      Answerable ]
    |                  |                   |                   |                    |
    v                  v                   v                   v                    v
"Section 999 does  "The CrPC is not   "The provided       "Pakistani law       Provides answer
 not exist under    part of the        context does not    exhibits split       with bracketed
 the PPC."          covered corpus."   contain this."      judicial rulings."   statutory cite
```

1. **Unsupported / Non-Existent Legal Questions (`refusal_type: "unsupported_provision"`):**  
   - Inquiries about fake statutory sections (e.g. PPC Section 999 or Constitution Article 500).  
   - *Target Behavior:* Explicitly state that the cited section does not exist under the referenced statute.  
   - *Example Output:* `"Under Pakistani law, the Pakistan Penal Code, 1860 does not contain a Section 999. The Code concludes at Section 511."`
2. **Out-of-Corpus Domestic Legal Questions (`refusal_type: "out_of_corpus_law"`):**  
   - Inquiries about Pakistani laws outside the three project statutes (e.g., Code of Criminal Procedure 1898, Qanun-e-Shahadat Order 1984, Companies Act 2017) or amendments not in the corpus (e.g. PECA Amendment Act 2025).  
   - *Target Behavior:* Clarify that the question concerns a statute or amendment outside the project scope and refuse substantive analysis. These examples do **not** teach substantive CrPC/QSO law; they teach jurisdictional scope awareness.  
   - *Example Output:* `"This question concerns the Code of Criminal Procedure (CrPC), 1898. The system's statutory authority is limited to the Constitution of Pakistan, the Pakistan Penal Code, and PECA 2016. Because this matter is governed by external procedural law, it cannot be answered from the available statutory corpus."`
3. **Missing-Context Questions (`refusal_type: "missing_context"`):**  
   - Applicable to grounded prompts where the supplied `CONTEXT:\n[...]` lacks the answer.  
   - *Target Behavior:* Output the canonical refusal string: `"I don't know - this is not in the provided text."`
4. **Genuinely Unanswerable / Ambiguous Questions (`refusal_type: "inherent_ambiguity"`):**  
   - Questions where statutory text is silent, contradictory, or subject to unresolved judicial conflict without statutory codification.  
   - *Target Behavior:* Note statutory silence or competing judicial interpretations without taking an unsubstantiated stance.

---

## 5. Dual-Mode Conditioning: Balancing Standalone vs. Grounded SFT

### 5.1 Balancing Mechanism

| Mode | Share | Prompt Configuration | Training Objective |
|---|:---:|---|---|
| **Standalone QA** | **60%** (Provisional) | No `CONTEXT` block. Prompt contains instruction + question. | **Teaches Parametric Legal Competence:** The model learns to recall Pakistani statutory penalties, legal definitions, and bracketed citations directly from its weights without suffering from "empty context paralysis." |
| **Context-Grounded QA** | **40%** (Provisional) | Preceded by `CONTEXT:\n[...]`. Prompt contains instruction + context + question. | **Teaches Evidence Faithfulness:** The model learns to prioritize provided text, adhere strictly to excerpted clauses, cite only from the supplied context, and refuse when the context is insufficient. |

> [!NOTE]
> **Provisional Ratio Notice:** The 60/40 ratio is an **experimental starting point**, not a mathematically proven optimum. It balances the need for the model to generate robust answers in Arm 3 without requiring retrieved text, while providing sufficient open-book training signal (340 examples) so Arm 4 reliably conditions on ChromaDB retrieved passages.

### 5.2 Preventing Cross-Mode Failure
- **Standalone SFT:** Standalone examples instruct the model to answer from established Pakistani statutory law. Uncertainty is trained via explicit non-existent sections and out-of-corpus laws, not by teaching the model to refuse merely because context is absent.
- **Context-Grounded SFT:** The presence of `CONTEXT:\n` acts as a clear conditional trigger. When the trigger is present, the model operates in open-book extraction mode. When absent, it operates in parametric legal recall mode.

---

## 6. Dataset Size, Category, and Law Distribution

We specify a curated, high-quality initial dataset of **850 examples**.

### 6.1 Distribution Across Categories (850 Examples Total)

```
SFT Dataset Allocation (850 Examples)
├── Statutory Rules & Penalties (Standalone):     200 (23.5%)  [Legal Review: Spot-check]
├── Factual Legal Scenarios (Standalone):         180 (21.2%)  [Legal Review: MANDATORY]
├── Complex Multi-Hop Inquiries (Standalone):      80 (9.4%)   [Legal Review: MANDATORY]
├── Out-of-Corpus / Unsupported (Standalone):      50 (5.9%)   [Legal Review: Spot-check]
├── Grounded Context QA (Answerable):             260 (30.6%)  [Legal Review: Spot-check]
└── Grounded Context Refusal (Missing Context):    80 (9.4%)   [Legal Review: Spot-check]
```

### 6.2 Distribution Across Statutes
- **Pakistan Penal Code (PPC):** 400 examples (47.1%) — reflects the vast substantive breadth of offences, elements, and penalties across 511 sections in `raw/ppc.txt`.
- **Constitution of Pakistan:** 300 examples (35.3%) — covers fundamental rights, institutional powers, legislative procedures, and the 26th and 27th Amendment structures in `raw/constitution.txt`.
- **PECA 2016:** 150 examples (17.6%) — specialized cyber offences, investigative powers, and cross-statute interaction with the PPC under the enacted 2016 Act in `raw/peca.txt`.

### 6.3 Areas of Critical Legal Expert Verification
Expert review is particularly vital in the following high-risk sub-domains:
1. **Factual Legal Scenarios (180 items):** Ensuring that described fact patterns satisfy the precise statutory definitions under Pakistani criminal law (e.g., distinguishing criminal breach of trust under Section 405 from cheating under Section 415).
2. **Multi-Hop Legal Inquiries (80 items):** Ensuring that cross-provision reasoning (e.g., how PECA Section 28 incorporates PPC offences) correctly reflects established legal procedure and judicial interpretation.
3. **PECA Cyber Harassment & Modesty Offences:** Navigating nuanced differences between PECA Section 21 (modesty of natural person) and Section 24 (cyberstalking).
4. **27th Amendment Distinctions:** Ensuring that questions citing the Federal Constitutional Court reflect Chapter 1A provisions rather than conflating them with pre-27th Amendment Supreme Court exclusive jurisdictions.

---

## 7. Data Quality, Verification Safeguards, and Contamination Protocols

### 7.1 Automated Quality Filters
1. **Citation Validation:** Every citation in `output` is checked against `chunks.json`. Missing, misspelled, or hallucinated chunk IDs immediately reject the record.
2. **Format Enforcement:** Validates bracketed citation syntax (`[Law Section]`) and structured paragraph output.
3. **Assistant-Only Loss Masking:** The training loader must format examples so that labels for user prompts, system prompts, and context blocks are replaced with `-100`, computing cross-entropy loss exclusively on assistant response tokens.

### 7.2 Benchmark Quarantine and Contamination Guardrails
To protect the integrity of the evaluation benchmark, SFT data must pass a four-tier contamination screening pipeline:

```
+-------------------------------------------------------------------------+
| Tier 1: Exact Text Match (Case-sensitive Q_train == Q_test)             |
|   -> Automatic Rejection if matched                                     |
+-------------------------------------------------------------------------+
                                    | Passes
                                    v
+-------------------------------------------------------------------------+
| Tier 2: Normalized Hash Match (MD5 of lowercase, stripped tokens)       |
|   -> Automatic Rejection if matched                                     |
+-------------------------------------------------------------------------+
                                    | Passes
                                    v
+-------------------------------------------------------------------------+
| Tier 3: 8-Gram Containment (Jaccard word overlap >= 0.20)               |
|   -> Quarantined for Human Legal Review                                 |
+-------------------------------------------------------------------------+
                                    | Flagged
                                    v
+-------------------------------------------------------------------------+
| Tier 4: Dense Semantic Cosine Similarity (Score >= 0.82)                |
|   -> Quarantined for Human Legal Review                                 |
+-------------------------------------------------------------------------+
```

### 7.3 Why Semantic Similarity Requires Human Review Rather Than Automatic Deletion
- **Statutory Formulaic Phrasing:** Statutory language inherently repeats boilerplate phrases (e.g., *"Whoever commits the offence of... shall be punished with imprisonment..."*).
- **Automated Removal Risk:** Blindly deleting questions with high semantic similarity would systematically strip core statutory legal terms from training, biasing the training data away from essential penal definitions.
- **Review Protocol:** Tier 3 and 4 flags are reviewed by a human annotator. If the question tests the identical scenario, facts, and statutory target as an evaluation benchmark item, it is deleted. If it merely shares standard statutory terminology while asking a distinct legal question, it is retained.

---

## 8. Experimental Fairness Across All Four Arms

The training and evaluation workflow guarantees absolute comparability across the four experimental arms:

```
                            HELD-OUT EVALUATION BENCHMARK
           (Current: 60 MCQs / 18 OOS -> Planned Target: 80 Dev + 320 Final)
                                           |
         +---------------------------------+---------------------------------+
         |                                 |                                 |
         v                                 v                                 v
   [ Arm 1: Base ]                  [ Arm 2: RAG ]                   [ Arm 3: FT ]
    Raw Qwen-2.5                     Raw Qwen-2.5                     LoRA Fine-Tuned
    Zero Retrieval                   ChromaDB Context                 Zero Retrieval
         |                                 |                                 |
         +---------------------------------+---------------------------------+
                                           |
                                           v
                                    [ Arm 4: FT + RAG ]
                                     LoRA Fine-Tuned
                                     ChromaDB Context
```

### Fairness Guarantees:
1. **Identical Test Set:** All four arms are evaluated on the exact same held-out benchmark items.
2. **Unified Evaluation Prompt:** All arms use the common prompt grammar defined in `PROMPT_ALIGNMENT_AUDIT.md`, using an empty `{context_block}` for Arms 1 & 3, and the ChromaDB retrieved excerpt for Arms 2 & 4.
3. **Greedy Deterministic Decoding:** All evaluations run at `temperature = 0.0` with identical token constraints (80 tokens for MCQs, 300 tokens for free-text).
4. **Isolated Comparative Signals:**
   - Arm 1 measures pre-training memorization/contamination.
   - Arm 2 measures the isolated impact of vector retrieval and cross-encoder reranking.
   - Arm 3 measures the isolated impact of parameter fine-tuning on legal reasoning and citation style.
   - Arm 4 measures the interaction and complementarity of retrieved evidence combined with fine-tuned domain adaptation.

---

## 9. Current Project State, Unresolved Decisions, and Readiness Assessment

### 9.1 Actual Existing Benchmark Status (Clarification of Facts)
- **Currently Implemented and Validated:**
  - `tests/mcq_dev.json` contains **20 items**.
  - `tests/mcq_final.json` contains **40 items**.
  - `tests/out_of_scope.json` contains **18 items**.
  - `tests/retrieval_test.json` contains **30 items**.
- **Planned Target (Pending Implementation):** The expanded 400-question benchmark (80 dev and 320 final) is an approved design target in `BENCHMARK_DESIGN_PROPOSAL.md`, but the questions have **not yet been drafted, compiled, or populated into the JSON files**.
- **Readiness Claim Correction:** The plan is ready in terms of design specification, but dataset generation tooling cannot run against the 400-question benchmark until the questions are drafted and built into `tests/`.

### 9.2 Decisions to Finalize During Dataset Generation Tooling
1. **Benchmark Expansion Execution:** Decide whether to generate the 850 SFT training examples first against the existing 60-question MCQ benchmark, or to draft the 400-question benchmark first to enable the full 4-tier contamination check.
2. **Implementation of `check_contamination.py`:** Build the automated screening tool to enforce Tier 1 and Tier 2 string/hash rejections and route Tier 3/4 flags to reviewer queues.
3. **Fine-Tuning Token Constraints:** Finalize whether training sequence length should be capped at 2,048 or 4,096 tokens on Colab GPUs.
