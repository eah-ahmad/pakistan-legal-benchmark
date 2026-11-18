# Legal Pathway — Project Implementation Status Audit

**Project:** Legal Pathway — Comparative Legal QA System for Pakistani Law  
**Domain:** Pakistani Constitutional Law, Pakistan Penal Code (PPC), Prevention of Electronic Crimes Act (PECA 2016)  
**Audit Date:** November 17, 2026  
**Auditor Mode:** Read-Only Workspace Inspection  

---

## 1. Executive Summary

An audit of the Legal Pathway codebase was conducted to determine the current implementation status of the planned research comparing Retrieval-Augmented Generation (RAG), Fine-Tuning (LoRA / QLoRA), and Hybrid RAG + Fine-Tuning.

**Key Finding:**  
The repository contains a functional, well-structured data extraction, chunking, and RAG evaluation prototype designed to execute in Google Colab with local preprocessing. However, **fine-tuning, LoRA/QLoRA training scripts, and hybrid RAG + fine-tuning pipelines are completely unbuilt**. There are no training scripts, no adapter configurations, and no fine-tuning data preparation pipelines present in the workspace.

---

## 2. Component Implementation Status Table

| Component | Status | Evidence | Remaining Work |
|---|---|---|---|
| **Dataset** | Completed and verified | Raw statutes present (`Pakistan_Constitution.pdf`, `Penal_code.pdf`, `PECA.pdf`, extracted to `raw/*.txt`). Structured parent chunks (`chunks.json`: 1,013 sections) and subchunks (`embed_units.json`: 1,198 units) exist. Benchmark tests (`retrieval_test.json`: 30 items, `mcq_final.json`: 40 items, `mcq_dev.json`: 20 items, `out_of_scope.json`: 18 items) are generated and checked. | Human auditing/expansion of question sets if larger sample size is needed for academic publication. |
| **Preprocessing** | Completed and verified | `extractFromPdf.py` (PyMuPDF-based text extraction) and `chunk.py` (forward TOC-guided parsing, footnote/amendment stripping, section boundary detection, subchunking >2000 chars) are implemented and generated verified outputs (`omitted.json`, `chunk_diagnostics.txt`). | Preprocessing for fine-tuning formats (e.g., supervised instruction-tuning pairs / Alpaca / ShareGPT format) is not yet implemented. |
| **RAG** | Completed and verified | `rag_pipeline.py` implements end-to-end RAG: dual query/document prefix handling for embedding candidates (`Qwen3-Embedding-0.6B`, `embeddinggemma-300m`, `bge-small-en-v1.5`), ChromaDB vector indexing (cosine space), candidate pool expansion, parent-chunk resolution, cross-encoder reranking (`BAAI/bge-reranker-v2-m3`), grounded prompt construction, and greedy generation. | Execution runs on Colab; persistent ChromaDB vector store is generated on the fly during Colab runs rather than pre-committed. |
| **Fine-tuning** | Not implemented | Zero fine-tuning or training scripts found in workspace (`grep` for `peft`, `lora`, `qlora`, `train`, `Trainer`, `SFTTrainer` yielded only evaluation print statements and pre-trained inference loading). | Build dataset formatting pipeline (instruction/response pairs), training scripts (Hugging Face `transformers.Trainer` or TRL `SFTTrainer`), loss tracking, and validation logging. |
| **LoRA/QLoRA** | Not implemented | No PEFT/LoRA/QLoRA configuration, quantization configs (`BitsAndBytesConfig` for training), or adapter weight saves present. | Configure PEFT LoRA target modules (e.g. `q_proj`, `v_proj`, `k_proj`, `o_proj`), 4-bit/8-bit QLoRA configs, and hyperparameter tuning regimes. |
| **Hybrid RAG + FT** | Not implemented | Neither fine-tuned weights nor integration between fine-tuned adapter checkpoints and the retrieval pipeline exist. | Merge or load fine-tuned adapter into `rag_pipeline.py` / `evaluate.py` to run retrieval context against the fine-tuned LLM. |
| **Evaluation** | Partially implemented | `evaluate.py` evaluates baseline (no retrieval), RAG, and RAG+rerank across MCQ accuracy, regex-based legal citation accuracy (law + article/section number within gap limits), refusal rate on out-of-scope questions, and context hit@5. `check_tests.py` verifies test quality. `test_parsers.py` contains regression tests for answer/citation parsing. Results have been prototyped, but full evaluation execution results (`results.csv`, `eval_details.json`) are not committed. | 1. Implement evaluation harness for the Fine-Tuned (FT) and Hybrid (FT + RAG) models.<br>2. Add hallucination evaluation scripts (currently relies on manual review of `free_text_review.csv`).<br>3. Commit and log formal comparative benchmark runs across all 4 experimental arms. |

---

## 3. Detailed Workspace Audit

### 3.1 Project Directory Structure
```
all_programming/files/
├── .venv/                         # Local Python 3.13 virtual environment (PyMuPDF only)
├── .vscode/settings.json          # Editor settings
├── raw/                           # Extracted raw text corpora
│   ├── constitution.txt           # Constitution of Pakistan (467 KB)
│   ├── peca.txt                   # PECA 2016 Act (105 KB)
│   ├── ppc.txt                    # Pakistan Penal Code (522 KB)
│   └── verify.py                  # Raw text line/content verifier
├── review/                        # CSVs for question authoring & review
│   ├── mcq_draft.csv
│   ├── oos_draft.csv
│   └── retrieval_draft.csv
├── tests/                         # Evaluator test sets
│   ├── check_report.txt           # Leakage and quality audit report
│   ├── dev_ids.txt                # Dev set identifiers
│   ├── mcq_dev.json               # 20 MCQ questions for prompt engineering/tuning
│   ├── mcq_final.json             # 40 held-out MCQ questions for evaluation
│   ├── mcq_test.json              # 60 total combined MCQ questions
│   ├── out_of_scope.json          # 18 out-of-scope queries (must trigger refusal)
│   ├── out_of_scope_v2.json       # Revised 18 out-of-scope queries
│   └── retrieval_test.json        # 30 retrieval validation queries
├── build_tests.py                 # Assembles verified CSV drafts into tests/*.json
├── check_tests.py                 # Lexical leakage & heading overlap validation
├── chunk.py                       # Core parsing and legal hierarchical chunker
├── chunks.json                    # 1,013 parent legal section records
├── chunk_diagnostics.txt          # Chunker diagnostics, longest/shortest chunks
├── demo_grading.csv               # 20 graded sample queries
├── demo_questions.txt             # Demo prompt texts
├── embed_test.ipynb               # Colab notebook: Recall@k & MRR for embedding selection
├── embed_units.json               # 1,198 embedding units (clauses/subsections)
├── evaluate.py                    # Evaluation runner for Baseline, RAG, RAG+Rerank
├── extractFromPdf.py              # PyMuPDF extractor from PDFs to raw/*.txt
├── fix_oos.py                     # Out-of-scope question sanitization
├── inspect_text.py                # CLI helper to locate section text in raw files
├── make_grading_sheet.py          # Generates manual grading sheets
├── make_questions.py              # Template/LLM-assisted question generator
├── omitted.json                   # 43 skipped/repealed sections (e.g. Schedule listings)
├── Pakistan_Constitution.pdf      # Source legal document
├── PECA.pdf                       # Source legal document
├── Penal_code.pdf                 # Source legal document
├── rag_pipeline.py                # Core RAG implementation (ChromaDB + Cross-Encoder + LLM)
├── README.md                      # Operational guide & workflow documentation
├── review_report.md               # Prior audit & refactor report
├── run_rag.ipynb                  # Colab runner for index build and evaluation execution
├── split_mcq.py                   # Splits MCQ pool into dev (20) and final (40)
└── test_parsers.py                # Parser test suite for evaluate.py
```

### 3.2 Technologies & Base Models
- **Environment Execution Strategy:** Split workflow: Python 3.13 standard library + PyMuPDF locally for text processing; PyTorch, Hugging Face Transformers, SentenceTransformers, and ChromaDB run in Google Colab (GPU).
- **Generation LLM:** Configured for `Qwen/Qwen2.5-3B-Instruct` (with optional switch to `meta-llama/Llama-3.2-3B-Instruct` or Qwen3 variants).
- **Embedding Models Supported:**
  - `Qwen/Qwen3-Embedding-0.6B` (with task instruction prefix).
  - `google/embeddinggemma-300m` (with query/title prefix).
  - `BAAI/bge-small-en-v1.5` (with retrieval instruction prefix).
- **Reranker:** `BAAI/bge-reranker-v2-m3` (CrossEncoder).
- **Vector Database:** `chromadb` using cosine similarity (`hnsw:space: cosine`).

### 3.3 Status of Experimental Approaches
1. **Approach 0: Control / Base Model:** Implemented in `evaluate.py` (`baseline` setup: `use_rag=False, use_rerank=False`). Evaluates zero-shot generation without retrieved context.
2. **Approach 1: Retrieval-Augmented Generation (RAG):** Implemented in `rag_pipeline.py` and `evaluate.py` (both plain RAG and RAG with `bge-reranker-v2-m3`).
3. **Approach 2: Fine-Tuning (LoRA / QLoRA):** **NOT IMPLEMENTED.** No training data, PEFT configs, or training loops exist.
4. **Approach 3: Fine-Tuning combined with RAG:** **NOT IMPLEMENTED.** Requires both adapter training and pipeline integration.

### 3.4 Evaluation Scripts & Benchmark Setup
- **Evaluation Script (`evaluate.py`):**
  - Iterates over setups: `baseline`, `RAG`, and `RAG+rerank`.
  - Computes **MCQ Accuracy** (letter parsing with strict multi-choice collision handling).
  - Computes **Citation Accuracy** (validates presence of cited law and section within a 40-character window).
  - Computes **Refusal Rate** on unanswerable/out-of-scope prompts (`tests/out_of_scope.json`).
  - Computes **Context Hit@5** (checks if ground-truth parent section appears in retrieved context).
  - Flags **Contamination / Prior Knowledge** via baseline MCQ accuracy (scoring significantly above 25% random guess indicates base model memorization).
- **Test Set Hygiene:**
  - Strict separation: All evaluation samples reside exclusively in `tests/` marked with `"split": "test"`. Chunks for retrieval indexing are derived strictly from statutes (`chunks.json` / `embed_units.json`).

---

## 4. Current Technical Problems & Discrepancies

1. **Missing Supervised Fine-Tuning Dataset:**  
   The project has formulated retrieval and MCQ evaluation sets, but has zero question-answer pairs formatted for instruction fine-tuning. Training LoRA/QLoRA requires a dedicated training corpus separate from `tests/` to prevent contamination.
2. **Evaluation Results Not Persisted:**  
   While `evaluate.py` is written and runnable, benchmark execution artifacts (`results.csv`, `eval_details.json`) from full runs are not stored in the repository.
3. **Retrieval Leakage in Test Queries:**  
   According to `tests/check_report.txt`, all 30 retrieval questions in `tests/retrieval_test.json` verbatim mirror section headings (e.g. `What does Pakistani law provide regarding: [Exact Heading]?`), which inflates retrieval recall and does not accurately test semantic search under realistic user phrasing.
4. **Context Truncation Edge Cases:**  
   `rag_pipeline.py` caps context generation text (`MAX_CTX_CHARS=4000`), whereas 45 legal sections in `chunks.json` exceed 2,500–4,000 characters (max 11,581 characters), which can clip long penal provisions or constitutional schedules during prompt assembly.

---

## 5. Current Project Status

The Legal Pathway project is currently **midway through the RAG implementation and benchmark design phase**. The foundation (text extraction, structural section parsing, vector retrieval, cross-encoder reranking, and automated evaluation metrics for RAG vs. baseline) is completed and verified in code. However, **the project has not yet started the fine-tuning (LoRA/QLoRA) or hybrid (FT + RAG) adaptation phases**.

---

## 6. Three Most Important Unfinished Tasks

1. **Curate and Format a Dedicated Fine-Tuning Dataset:**  
   Construct a high-quality instruction-tuning dataset (legal question-answer pairs with statutory reasoning) strictly segregated from `tests/*.json` to avoid benchmark contamination.
2. **Develop LoRA/QLoRA Training Scripts:**  
   Create the training pipeline (e.g., using Hugging Face `peft`, `bitsandbytes`, and TRL `SFTTrainer` on Colab/GPU) targeting the chosen base model (e.g., `Qwen2.5-3B-Instruct`), fine-tune the adapters, and save adapter checkpoints.
3. **Implement and Execute the 4-Arm Comparative Evaluation:**  
   Integrate the trained LoRA/QLoRA adapter into `evaluate.py` to test:  
   *(1) Base Model Control*, *(2) RAG*, *(3) Fine-Tuning Alone*, and *(4) Fine-Tuning + RAG*, logging comparative metrics for MCQ accuracy, citation faithfulness, out-of-scope refusal, and hallucination.

---

## 7. Major Technical Blockers

1. **Compute and Quota Limits for Fine-Tuning:**  
   Local environment is CPU-only (Python 3.13 without PyTorch/CUDA). All training must be executed on Google Colab or external GPU clusters. Unstable free-tier Colab sessions risk timeouts during QLoRA training.
2. **Absence of Grounded Training Data for Legal Domain:**  
   While raw legal texts exist, LoRA adaptation cannot begin without structured instruction-tuning examples (input query, legal reasoning chain, and correct statutory citation).
3. **Hallucination Detection Metric Automation:**  
   `evaluate.py` currently tests refusal and citation accuracy automatically, but qualitative hallucination detection currently defaults to manual inspection of `free_text_review.csv`. An automated faithfulness metric (e.g., LLM-as-a-judge or NLI entailment scoring) is needed for rigorous academic comparison across the three approaches.
