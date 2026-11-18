# Prompt and Generation Alignment Audit

**Document:** `PROMPT_ALIGNMENT_AUDIT.md`  
**Date:** November 17, 2026  
**Scope:** Strictly read-only audit of prompts, generation configurations, and evaluation parameters in `evaluate.py` and `rag_pipeline.py` across Baseline, RAG, and RAG + reranking.

---

## 1. Current Prompt and Generation Differences

The current pipeline implements distinct instruction branches depending on whether `use_rag` is `True` or `False`. Between RAG and RAG + reranking, the prompt and generation configurations are identical; the divergence occurs between Baseline and the RAG-enabled setups.

### Comparison Matrix

| Parameter / Dimension | Baseline (`use_rag=False, use_rerank=False`) | RAG (`use_rag=True, use_rerank=False`) | RAG + Reranking (`use_rag=True, use_rerank=True`) |
|---|---|---|---|
| **System Instruction** | `SYSTEM_BASE`: *"You are a research-prototype assistant for Pakistani law (Constitution of Pakistan, Pakistan Penal Code, PECA 2016). Answer from your own knowledge; if unsure, say I don't know. Cite the law and the article/section number for every claim, like [PPC Section 302], [Constitution Article 19], [PECA Section 11]. This is not legal advice."* | `SYSTEM_RAG`: *"You are a research-prototype assistant for Pakistani law (Constitution of Pakistan, Pakistan Penal Code, PECA 2016). Answer ONLY from the CONTEXT. Cite the law and the article/section number for every claim, like [PPC Section 302], [Constitution Article 19], [PECA Section 11]. If the CONTEXT does not contain the answer, reply exactly: 'I don't know - this is not in the provided text.' Never use outside knowledge. This is not legal advice."* | Identical to RAG (`SYSTEM_RAG`). |
| **Grounding Directive** | *"Answer from your own knowledge; if unsure, say I don't know."* | *"Answer ONLY from the CONTEXT."* and *"Never use outside knowledge."* | Identical to RAG. |
| **Refusal Rule in System Prompt** | No explicit refusal requirement or canonical refusal phrase specified. | Enforces exact canonical refusal phrase: `"I don't know - this is not in the provided text."` | Identical to RAG. |
| **User Prompt Structure (MCQ)** | `{question}\nA) ...\nB) ...\nC) ...\nD) ...\nAnswer: <letter>\n\nAnswer with the single letter (A, B, C or D) of the correct option, then on a new line cite the law and article/section number. If unsure, reply exactly: "I don't know".` | `CONTEXT:\n{_context(ctx)}\n\nQUESTION:\n{question}\nA) ...\nB) ...\nC) ...\nD) ...\nAnswer: <letter>\n\nAnswer with the single letter (A, B, C or D) of the correct option, then on a new line cite the law and article/section number. If the CONTEXT does not contain the answer, reply exactly: "I don't know - this is not in the provided text."` | Identical to RAG. |
| **User Prompt Structure (OOS)** | `{question}\n\nAnswer concisely and cite your sources.` | `CONTEXT:\n{_context(ctx)}\n\nQUESTION:\n{question}\n\nAnswer concisely and cite your sources.` | Identical to RAG. |
| **Refusal Trigger Formulation** | In MCQ tail: `If unsure, reply exactly: "I don't know".` | In MCQ tail: `If the CONTEXT does not contain the answer, reply exactly: "I don't know - this is not in the provided text."` | Identical to RAG. |
| **Citation Requirement** | Mentioned in `SYSTEM_BASE` and MCQ tail, but without grounding context from which to verify. | Mentioned in `SYSTEM_RAG` and MCQ tail, strictly anchored in retrieved `CONTEXT`. | Identical to RAG. |
| **Temperature** | `CFG["TEMPERATURE"] = 0.0` (Greedy decoding: `do_sample=False`). | `0.0` (Greedy decoding). | `0.0` (Greedy decoding). |
| **Max New Tokens** | - MCQ: 80 tokens (`evaluate.py:127`).<br>- Free text / OOS: 300 tokens (`rag_pipeline.py:255`). | - MCQ: 80 tokens.<br>- Free text / OOS: 300 tokens. | - MCQ: 80 tokens.<br>- Free text / OOS: 300 tokens. |
| **Generation Settings** | `enable_thinking=False` (when supported), `pad_token_id=tok.eos_token_id`, `skip_special_tokens=True`, `<think>` tags stripped via regex. | Identical. | Identical. |

---

## 2. Standardized Prompt Template for All Four Experimental Arms

To ensure fair, controlled comparison across:
1. **Base model (Control)**
2. **Base model + RAG**
3. **Fine-tuned model (LoRA/QLoRA)**
4. **Fine-tuned model + RAG**

The prompt structure must be symmetric in its persona, citation rules, and canonical refusal trigger, using a single conditional slot (`{context_block}`) that is empty when retrieval is omitted and populated when retrieval is active.

### 2.1 Proposed Common System Prompt

```text
You are a legal question-answering assistant specializing in Pakistani law (Constitution of Pakistan, Pakistan Penal Code, and Prevention of Electronic Crimes Act 2016).

Rules:
1. Grounding & Evidence: Base your answer strictly on the provided context if context is present; otherwise base your answer on established Pakistani statutory law. Do not speculate or extrapolate beyond statutory authority.
2. Citation: For every legal rule, offence, punishment, or right mentioned, you must explicitly cite the governing law and section/article number in brackets, for example: [PPC Section 302], [Constitution Article 19], or [PECA Section 11].
3. Refusal: If the available evidence or context is insufficient to answer the question, or if the provision does not exist under Pakistani law, you must reply exactly:
"I don't know - this is not in the provided text."
Never fabricate statutory sections or provisions.
4. Disclaimer: This system is a research prototype, not formal legal advice.
```

### 2.2 Proposed Common User Prompt Formats

#### For Multiple-Choice Questions (MCQ):
```text
{context_block}QUESTION:
{question}
A) {option_A}
B) {option_B}
C) {option_C}
D) {option_D}

INSTRUCTIONS:
1. State the single letter (A, B, C, or D) corresponding to the correct option.
2. On a new line, provide the statutory citation supporting your selection (e.g., [PPC Section 302]).
3. If the correct answer cannot be determined from the available legal authority, reply exactly:
"I don't know - this is not in the provided text."
```

#### For Free-Text & Out-of-Scope (OOS) Questions:
```text
{context_block}QUESTION:
{question}

INSTRUCTIONS:
1. Provide a concise, direct answer based strictly on verified Pakistani law.
2. Cite the exact law and section/article number for each claim.
3. If the provision does not exist or the evidence is insufficient, reply exactly:
"I don't know - this is not in the provided text."
```

Where `{context_block}` is defined uniformly as:
- **For Non-RAG Arms (Arm 1 & Arm 3):** `""` (Empty string).
- **For RAG-Enabled Arms (Arm 2 & Arm 4):**
  ```text
  CONTEXT:
  [PPC Section 302 - Punishment of qatl-i-amd]
  {excerpt_text}

  [Constitution Article 19 - Freedom of speech, etc.]
  {excerpt_text}

  ```

---

## 3. Unavoidable Configuration Differences Due to Retrieval

While prompts, temperature, stopping criteria, and token limits can and should be standardized, the following configuration and operational differences are inherent to the presence or absence of retrieval:

1. **Context Window Length & Input Token Count:**  
   - *Non-RAG Arms (1 & 3):* Input sequences consist strictly of system instructions and question text (~150–250 tokens).
   - *RAG Arms (2 & 4):* Input sequences include up to 5 top-ranked statutory excerpts (`MAX_CTX_CHARS=4000`), consuming ~1,000–1,500 prompt tokens. Attention patterns and prompt processing latency differ unavoidably.
2. **Context Hit @ 5 Metric Availability:**  
   - `context_hit_at_5` (measuring whether the ground-truth legal section was delivered inside the top-5 retrieved passages) is mathematically only defined for RAG-enabled arms. In unassisted arms, this metric is necessarily `n/a`.
3. **Retrieval Latency and Overhead:**  
   - Arms 2 and 4 incur embedding generation, ChromaDB vector querying, candidate deduplication, and cross-encoder reranking latency (`bge-reranker-v2-m3`), which non-RAG arms bypass completely.
4. **Failure Modes:**  
   - Non-RAG arms fail primarily via parametric hallucination, confabulated citations, or pre-training memorization gaps.
   - RAG arms introduce retrieval failures (distractor context retrieval, truncation of long statutory schedules, cross-encoder misranking) in addition to generation failure modes.
