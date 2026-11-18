# Pakistani Legal QA - RAG research prototype (NOT legal advice)
Muhammad Ahmad, CMS 542432, BSCS-15-D

## Folder layout
```
project/
  pdfs/            Pakistan_Constitution.pdf  Penal_code.pdf  PECA.pdf
  extractFromPdf.py  chunk.py  inspect_text.py  make_questions.py  build_tests.py     (LOCAL)
  rag_pipeline.py  evaluate.py  embed_test.ipynb  run_rag.ipynb                       (COLAB)
  raw/ review/ tests/ chunks.json embed_units.json     (generated)
```

## Run order
| # | Step | Where | Command | Output |
|---|------|-------|---------|--------|
| 0 | install | local | `python -m venv .venv && source .venv/Scripts/activate && pip install pymupdf` | |
| 1 | extract text | local | `python extractFromPdf.py` | raw/constitution.txt, ppc.txt, peca.txt |
| 2 | chunk | local | `python chunk.py` | chunks.json, embed_units.json, omitted.json, chunk_diagnostics.txt |
| 2b | debug | local | `python inspect_text.py ppc "Adulteration of drugs"` | raw text around a string |
| 3 | draft questions | local (templates) or Colab `--llm` | `python make_questions.py` | review/*.csv |
| 4 | human review | you | edit CSVs, set `status` to `ok` | |
| 5 | build tests | local | `python build_tests.py` | tests/*.json |
| 6 | pick embedder | Colab | `embed_test.ipynb` | recall@1/3/5, MRR table |
| 7 | index + demo + eval | Colab | `run_rag.ipynb` | results.csv, free_text_review.csv, eval_details.json |

Python 3.13: steps 1-5 use only the standard library plus PyMuPDF (1.25+ ships 3.13 wheels; if `pip install pymupdf` fails, run extraction on Colab). Everything with torch/transformers/chromadb runs on Colab only.
Colab installs: `pip install -U sentence-transformers transformers chromadb accelerate bitsandbytes`. Qwen3-Embedding needs transformers>=4.51 and sentence-transformers>=2.7 (per its model card; verify). EmbeddingGemma and Llama-3.2 are gated on Hugging Face: accept the licence and `login()`.
For `make_questions.py --llm` on Colab: upload chunks.json + the script, `!python make_questions.py --llm`, download review/.

## Test-set hygiene
Test questions live only in `tests/` (each item has `"split": "test"`). The index is built only from chunks.json / embed_units.json, so test text is never retrieval corpus. Keep any future fine-tuning data in a separate folder and exclude tests/ from it.

## What to say in the viva
- **Extraction**: PyMuPDF reads the selectable text page by page; I keep page markers so each chunk can cite its PDF page.
- **Cleaning + chunking**: I remove page headers, bottom-of-page footnotes and amendment markers (`1[...]`, `* * *`). The table of contents is the authoritative list of sections; I find each number in the body searching only forward, so numbers cannot go backwards and schedule lists cannot collide. One chunk = one article/section with metadata (law, kind, number, heading, text), because legal answers are cited by section. Sections over 2,000 chars stay whole as the parent and are also split by clause for embedding ("search small, return whole"). The validation report checks missing numbers, shortest/longest chunks and samples.
- **Test sets**: drafts from templates (or an LLM), then manual review; three kinds: retrieval (known source), MCQ (answer key + source), out-of-scope (must be refused).
- **Embedding choice**: three candidates compared on my own questions by recall@k (is the right section in the top k) and MRR (average of 1/rank of the right section). Query prefixes are model-specific, so each model gets its own.
- **Retrieval**: ChromaDB cosine search returns the top 20, a cross-encoder (bge-reranker-v2-m3) reads question and passage together and re-scores them, keep the top 5. Compared with plain RAG.
- **Generation**: one small instruct LLM, greedy decoding, prompt = "answer only from context, cite law and number, otherwise say I don't know".
- **Evaluation**: baseline vs RAG vs RAG+rerank. MCQ accuracy = correct/total x 100; citation accuracy = answer cites the right law and number (regex); refusal rate on out-of-scope questions. The baseline MCQ score doubles as a simple contamination check (above 25% chance means the model already knows answers without retrieval). To the best of our knowledge this domain/metric combination is new; it is a small prototype and results depend on my own test sets.
- **Limits**: not legal advice; test sets are small and self-made; template questions can be easier than real ones; amendment version of PECA should be stated in the report.
