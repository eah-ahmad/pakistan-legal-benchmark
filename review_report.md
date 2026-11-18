# Read-only review: Pakistani legal RAG project

Review date: 2026-10-11

Scope: `rag_pipeline.py`, `evaluate.py`, `run_rag.ipynb`, and `embed_test.ipynb`. The review did not run models, download model weights, or modify source, notebook, test, or raw-data files. The corpus JSON files were read only to verify parent-section sizes and subchunk counts.

## Findings by severity

### BLOCKER

None identified by static inspection.

### SHOULD FIX

1. **Parent text is not always passed in full to generation.** Retrieval resolves subchunks to the complete parent record and its citation, but `_context` slices each parent text to `MAX_CTX_CHARS=2500`. A read-only count of [chunks.json](./chunks.json) found 45 of 1,013 parent records longer than 2,500 characters (maximum: 11,581). Those records therefore lose text before the prompt is built, even though citations still refer to the parent. See [`rag_pipeline.py`](./rag_pipeline.py), lines 26, 141–147, 163–164, 187, and 191–192.

2. **The top-20 distinct-parent retrieval target is not guaranteed.** `retrieve` asks Chroma for up to `k * 4` embedding units (80 with the default `k=20`) and then removes duplicate `parent_id` values. It stops after 20 unique parents, but an 80-unit candidate pool can contain fewer than 20 parents when subchunks repeat. The corpus has parents with as many as 11 units, so this is possible. The reranker correctly reorders the candidate parent passages and keeps five, but it can only rerank the distinct parents returned. See [`rag_pipeline.py`](./rag_pipeline.py), lines 25, 134–149, and 151–160; [embed_units.json](./embed_units.json) was read only for the subchunk count.

3. **Qwen3 generation is not explicitly put into non-thinking mode.** The configured default is Qwen2.5, for which the current chat-template call is appropriate. But `LLM_ID` is selectable; if changed to Qwen3, `apply_chat_template` is called without `enable_thinking=False`. Qwen3’s model card says thinking is enabled by default and documents `enable_thinking=False` for non-thinking output. This matters for short, greedy MCQ generation. See [`rag_pipeline.py`](./rag_pipeline.py), lines 22, 97–103; the [Qwen3 model card](https://huggingface.co/Qwen/Qwen3-8B), “Switching Between Thinking and Non-Thinking Mode.”

4. **Evaluation answer parsing can mis-score results.**
   - `parse_letter` accepts the first standalone A–D at the very start, whether or not it is an answer label. For example, prose beginning “A provision…” is parsed as answer A even if it later states another option. It also does not recognize some natural labels such as “Choice C.” See [`evaluate.py`](./evaluate.py), lines 47–48.
   - Citation scoring tests the requested law and the requested number independently: a matching law name anywhere plus the expected number after any citation cue within the next 60 characters counts as correct. Those pieces need not form one citation, which can produce false positives; unusual number formats can produce false negatives. See [`evaluate.py`](./evaluate.py), lines 20, 24–44.
   - Refusal scoring is a substring search. It misses variants such as curly-apostrophe “don’t know,” “unable to determine,” and “insufficient context”; conversely, any response containing a refusal phrase counts as a refusal even if it then gives an answer or citation. See [`evaluate.py`](./evaluate.py), lines 21–22 and 84.

5. **Dev/final MCQ selection is not exposed.** The evaluation loads only `mcq_test.json`; `run(max_mcq=...)` can truncate that list but cannot select `mcq_dev.json` or `mcq_final.json`. The run notebook’s upload list likewise names only `mcq_test.json`. See [`evaluate.py`](./evaluate.py), lines 57–59, and [`run_rag.ipynb`](./run_rag.ipynb), JSON lines 28–32 and 79–80.

### MINOR

1. **A failed embedding model can silently disappear from the comparison table.** The notebook catches every exception around each model evaluation, prints a message, and continues; the final table contains only successful models. This makes it easy to overlook that one model has no result. See [`embed_test.ipynb`](./embed_test.ipynb), JSON lines 84–93.

## Requested checks

### a) Embedding query/document prefixes

- **Qwen3-Embedding:** correct format. The query uses `Instruct: {task}\nQuery:{query}` with a legal-retrieval task, while documents remain unprefixed. This matches the [Qwen3-Embedding model card](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B), which shows that query format and raw document text. See [`rag_pipeline.py`](./rag_pipeline.py), lines 34–42, and [`embed_test.ipynb`](./embed_test.ipynb), JSON lines 58–64.
- **EmbeddingGemma:** correct default prompts. Queries use `task: search result | query: ...` and documents use `title: none | text: ...`, matching the [EmbeddingGemma model card](https://huggingface.co/google/embeddinggemma), which identifies “search result” as its default task description and `none` as the default document title. See [`rag_pipeline.py`](./rag_pipeline.py), lines 35–42, and [`embed_test.ipynb`](./embed_test.ipynb), JSON lines 58–64.
- **bge-small-en-v1.5:** correct. The query uses the recommended retrieval instruction, and documents have no added instruction; the [BGE v1.5 model card](https://huggingface.co/BAAI/bge-small-en-v1.5) recommends no instruction on passages and allows query instructions for short-query-to-passage retrieval. See [`rag_pipeline.py`](./rag_pipeline.py), lines 35–42, and [`embed_test.ipynb`](./embed_test.ipynb), JSON lines 58–64.

### b) Normalization and Chroma metric

Both query and document embeddings use `normalize_embeddings=True`. Chroma’s collection is created with `hnsw:space` set to `cosine`. The embedding comparison notebook also normalizes both sides before computing `Q @ D.T`. See [`rag_pipeline.py`](./rag_pipeline.py), lines 73–80 and 123, and [`embed_test.ipynb`](./embed_test.ipynb), JSON lines 70–81.

### c) Reranking

The implementation uses `CrossEncoder.predict` on `(query, passage)` pairs and sorts candidates by the returned scores, which is the correct cross-encoder pattern described by the [bge-reranker-v2-m3 model card](https://huggingface.co/BAAI/bge-reranker-v2-m3). Configuration targets 20 retrieval parents and five final parents. The caveat is SHOULD FIX #2 above: because it fetches at most 80 subchunks before parent de-duplication, fewer than 20 parents may reach reranking. See [`rag_pipeline.py`](./rag_pipeline.py), lines 25, 134–160, and 181.

### d) Generation and model configuration

`TEMPERATURE=0.0` selects `do_sample=False`, i.e. greedy decoding, and MCQ evaluation sets `max_new_tokens=80`. `LLM_ID` is a configuration value and is set in the run notebook. The current default is Qwen2.5-3B-Instruct, not Qwen3. The Qwen3 thinking-mode limitation is SHOULD FIX #3 above. See [`rag_pipeline.py`](./rag_pipeline.py), lines 22, 27, and 97–103; [`evaluate.py`](./evaluate.py), line 71; [`run_rag.ipynb`](./run_rag.ipynb), JSON lines 44–47.

### e) Grounding, citation, and refusal prompt

The RAG system prompt instructs the model to answer only from `CONTEXT`, cite the law and article/section number for every claim, and return the exact configured “I don't know” refusal if context lacks the answer. MCQ mode repeats the single-letter, citation, and refusal requirements. The baseline intentionally uses a different prompt because it runs without retrieval. See [`rag_pipeline.py`](./rag_pipeline.py), lines 33–49 and 169–171.

### f) Parent sections and citations

Each retrieved embedding unit’s `parent_id` indexes the parent record loaded from `chunks.json`; returned sources cite that parent record. Thus retrieval/citation identity is parent-based. However, parent text longer than 2,500 characters is truncated for the prompt, as quantified in SHOULD FIX #1. See [`rag_pipeline.py`](./rag_pipeline.py), lines 37–42, 141–147, 163–164, and 191–192.

### g) Evaluation parsing edge cases

See SHOULD FIX #4. In summary, letter extraction can mistake leading prose for a choice and only returns one match; citation scoring does not require the law and number to belong to the same citation; refusal matching both misses common variants and treats a refusal phrase anywhere in a substantive answer as a refusal. These rules can respectively create false MCQ positives, citation positives/negatives, and refusal positives/negatives.

### h) Transformers 5.x and sentence-transformers 6.x API compatibility

Static inspection did not reveal a definite removed/renamed API in the calls used here: the files use the top-level `SentenceTransformer`/`CrossEncoder` imports, `SentenceTransformer.encode`, `CrossEncoder.predict`, `AutoTokenizer.from_pretrained`, `AutoModelForCausalLM.from_pretrained`, `apply_chat_template`, and `generate`. Sentence-transformers’ [v6.0 release notes](https://github.com/UKPLab/sentence-transformers/releases/tag/v6.0.0) introduce `MultiVectorEncoder` and do not identify these dense-embedding and cross-encoder calls as removed. Transformers’ [v5 release notes](https://github.com/huggingface/transformers/releases/tag/v5.0.0) describe major changes, including tokenizer backend refactoring, but document `AutoTokenizer.from_pretrained` continuing to select the backend transparently. No model-loading or runtime test was performed, per the no-download/no-GPU constraint, so model-specific compatibility is not established. Qwen3’s `enable_thinking=False` requirement is covered separately in SHOULD FIX #3.

### i) Evaluation settings and question-file selection

Baseline, RAG, and RAG+rerank are iterated over the same `mcq`, out-of-scope, and free-question lists, with the same model configuration and MCQ generation limit. They differ in retrieval/reranking flags as intended. The free-question sample is repeatable because it uses `random.Random(1)`. The MCQ file itself is fixed to `mcq_test.json`; there is no dev/final selector (SHOULD FIX #5). See [`evaluate.py`](./evaluate.py), lines 17–18 and 57–71.

## Follow-up implementation

After approval, the requested parser/selector fixes were made in `evaluate.py`, with standard-library coverage in `test_parsers.py`. `rag_pipeline.py` now expands the Chroma candidate count when parent de-duplication yields fewer than 20 sections, builds bounded parent-based context excerpts, supports Qwen3 non-thinking templates, and aligns baseline/RAG instructions. `run_rag.ipynb` now selects dev or final MCQs; `embed_test.ipynb` checkpoints each model's unchanged metrics to Drive and reports failures. The optional standard-library grading-sheet generator is `make_grading_sheet.py`.
