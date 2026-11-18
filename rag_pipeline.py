# Muhammad Ahmad, CMS 542432, BSCS-15-D
"""
rag_pipeline.py  (runs on COLAB / Kaggle GPU)       RESEARCH PROTOTYPE - NOT LEGAL ADVICE
Needs in the working folder: chunks.json, embed_units.json (from chunk.py).

    import rag_pipeline as rp
    rp.CFG["EMBED_KEY"] = "qwen3-0.6b"      # winner of embed_test.ipynb
    rp.build_index()                         # once: embeds every unit and fills ChromaDB
    rp.ask("What is the punishment for hate speech?")             # RAG + rerank
    rp.ask("...", use_rerank=False)                               # plain RAG
    rp.ask("...", use_rag=False)                                  # baseline, no retrieval
    rp.demo()                                                     # interactive loop

Pipeline: question -> embed (with the model's query prefix) -> ChromaDB top 20 units -> collapse to parent
sections -> (optional) cross-encoder rerank -> top 5 -> grounded prompt -> small LLM -> answer + cited sources.
"""
import json, re
from pathlib import Path

CFG = dict(
    EMBED_KEY="qwen3-0.6b",                  # qwen3-0.6b | embeddinggemma-300m | bge-small-en-v1.5
    LLM_ID="Qwen/Qwen2.5-3B-Instruct",       # or "meta-llama/Llama-3.2-3B-Instruct" (gated, needs HF login)
    USE_4BIT=False,                          # True -> 4-bit via bitsandbytes (saves GPU memory)
    RERANK_ID="BAAI/bge-reranker-v2-m3",
    TOP_RETRIEVE=20, TOP_FINAL=5,
    MAX_CTX_CHARS=4000,
    TEMPERATURE=0.0,                         # 0 = greedy decoding (deterministic)
    USE_QUERY_EXPANSION=False,               # stretch flag: LLM rewrites the question into a search query
    USE_RELEVANCE_CHECK=False,               # stretch flag: LLM checks the context before answering
    CHUNKS="chunks.json", UNITS="embed_units.json", DB_DIR="chroma_db",
)

REFUSAL = "I don't know - this is not in the provided text."
QWEN_TASK = "Given a Pakistani legal question, retrieve the article or section of law that answers it"
EMBED_MODELS = {   # query/doc prefixes: verify against each model card
    "qwen3-0.6b": dict(id="Qwen/Qwen3-Embedding-0.6B",
                       q=lambda s: f"Instruct: {QWEN_TASK}\nQuery:{s}", d=lambda s: s),
    "embeddinggemma-300m": dict(id="google/embeddinggemma-300m",
                                q=lambda s: f"task: search result | query: {s}", d=lambda s: f"title: none | text: {s}"),
    "bge-small-en-v1.5": dict(id="BAAI/bge-small-en-v1.5",
                              q=lambda s: "Represent this sentence for searching relevant passages: " + s, d=lambda s: s),
}

SYSTEM_TEMPLATE = ("You are a research-prototype assistant for Pakistani law (Constitution of Pakistan, Pakistan Penal "
                   "Code, PECA 2016). {grounding} Cite the law and the article/section number for every claim, like "
                   "[PPC Section 302], [Constitution Article 19], [PECA Section 11].{refusal_rule} "
                   "This is not legal advice.")
SYSTEM_RAG = SYSTEM_TEMPLATE.format(
    grounding="Answer ONLY from the CONTEXT.",
    refusal_rule=f" If the CONTEXT does not contain the answer, reply exactly: \"{REFUSAL}\" "
                 "Never use outside knowledge.",
)
SYSTEM_BASE = SYSTEM_TEMPLATE.format(
    grounding="Answer from your own knowledge; if unsure, say I don't know.",
    refusal_rule="",
)

_S = {}   # lazily loaded models / data


# ---------------------------------------------------------------- data + models
def _data():
    if "parents" not in _S:
        _S["parents"] = {c["id"]: c for c in json.loads(Path(CFG["CHUNKS"]).read_text(encoding="utf-8"))}
        _S["units"] = json.loads(Path(CFG["UNITS"]).read_text(encoding="utf-8"))
    return _S["parents"], _S["units"]


def _embedder():
    key = CFG["EMBED_KEY"]
    if _S.get("emb_key") != key:
        import torch
        from sentence_transformers import SentenceTransformer
        m = SentenceTransformer(EMBED_MODELS[key]["id"], device="cuda" if torch.cuda.is_available() else "cpu")
        m.max_seq_length = 512
        _S["emb"], _S["emb_key"] = m, key
    return _S["emb"]


def embed_docs(texts):
    f = EMBED_MODELS[CFG["EMBED_KEY"]]["d"]
    return _embedder().encode([f(t) for t in texts], batch_size=32, normalize_embeddings=True, show_progress_bar=True)


def embed_query(q):
    return _embedder().encode([EMBED_MODELS[CFG["EMBED_KEY"]]["q"](q)], normalize_embeddings=True)[0]


def _llm():
    if "llm" not in _S:
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
        tok = AutoTokenizer.from_pretrained(CFG["LLM_ID"])
        kw = dict(device_map="auto")
        if CFG["USE_4BIT"]:
            kw["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                                                           bnb_4bit_compute_dtype=torch.float16)
        else:
            kw["torch_dtype"] = torch.float16
        _S["llm"] = (tok, AutoModelForCausalLM.from_pretrained(CFG["LLM_ID"], **kw))
    return _S["llm"]


def chat(system, user, max_new_tokens=300):
    tok, model = _llm()
    msgs = [{"role": "system", "content": system}, {"role": "user", "content": user}]
    try:
        ids = tok.apply_chat_template(msgs, add_generation_prompt=True, return_tensors="pt",
                                      return_dict=True, enable_thinking=False)
    except TypeError:
        ids = tok.apply_chat_template(msgs, add_generation_prompt=True, return_tensors="pt", return_dict=True)
    ids = ids.to(model.device)
    t = CFG["TEMPERATURE"]
    kw = dict(do_sample=True, temperature=t) if t > 0 else dict(do_sample=False)
    out = model.generate(**ids, max_new_tokens=max_new_tokens, pad_token_id=tok.eos_token_id, **kw)
    answer = tok.decode(out[0][ids["input_ids"].shape[1]:], skip_special_tokens=True)
    return re.sub(r"<think>.*?</think>\s*", "", answer, flags=re.S).strip()


# ---------------------------------------------------------------- index
def _col():
    import chromadb
    client = chromadb.PersistentClient(path=CFG["DB_DIR"])
    return client, f"legal_{CFG['EMBED_KEY'].replace('.', '_').replace('-', '_')}"


def build_index(rebuild=True):
    """Embed every unit with the chosen model and store in ChromaDB (cosine space)."""
    _, units = _data()
    client, name = _col()
    if rebuild:
        try:
            client.delete_collection(name)
        except Exception:
            pass
    col = client.get_or_create_collection(name, metadata={"hnsw:space": "cosine"})
    embs = embed_docs([u["embed_text"] for u in units])
    for i in range(0, len(units), 500):
        part = units[i:i + 500]
        col.add(ids=[u["unit_id"] for u in part], embeddings=embs[i:i + 500].tolist(),
                documents=[u["text"] for u in part],
                metadatas=[dict(parent_id=u["parent_id"], law=u["law"], number=u["number"]) for u in part])
    print(f"indexed {col.count()} units into '{name}'")


# ---------------------------------------------------------------- retrieval
def retrieve(query, k=None, include_units=False):
    k = k or CFG["TOP_RETRIEVE"]
    parents, _ = _data()
    client, name = _col()
    col = client.get_collection(name)
    collection_size = col.count()
    if collection_size == 0 or k <= 0:
        return ([], {}) if include_units else []
    fetch_count = min(k * 4, collection_size)
    out, seen = [], set()
    units_by_parent = {}
    seen_units = set()
    query_embedding = [embed_query(query).tolist()]
    while True:
        includes = ["metadatas", "documents"] if include_units else ["metadatas"]
        res = col.query(query_embeddings=query_embedding, n_results=fetch_count, include=includes)
        if include_units:
            rows = zip(res["ids"][0], res["documents"][0], res["metadatas"][0])
        else:
            rows = ((None, None, md) for md in res["metadatas"][0])
        for unit_id, document, md in rows:
            pid = md["parent_id"]
            if pid not in seen:
                seen.add(pid)
                out.append(parents[pid])
            if include_units and unit_id not in seen_units:
                seen_units.add(unit_id)
                units_by_parent.setdefault(pid, []).append({"unit_id": unit_id, "text": document or ""})
        if len(out) >= k or fetch_count >= collection_size:
            break
        fetch_count = min(fetch_count * 2, collection_size)
    out = out[:k]
    if include_units:
        selected = {parent["id"] for parent in out}
        return out, {pid: units for pid, units in units_by_parent.items() if pid in selected}
    return out


def rerank(query, cands, top=None):
    top = top or CFG["TOP_FINAL"]
    if "rr" not in _S:
        import torch
        from sentence_transformers import CrossEncoder
        _S["rr"] = CrossEncoder(CFG["RERANK_ID"], max_length=1024, device="cuda" if torch.cuda.is_available() else "cpu")
    scores = _S["rr"].predict([(query, f"{c['cite']} ({c['heading']}): {c['text'][:2000]}") for c in cands],
                              batch_size=8)
    return [c for _, c in sorted(zip(scores, cands), key=lambda x: -x[0])][:top]


# ---------------------------------------------------------------- generation
def _section_excerpt(section, matched_units):
    text = section["text"]
    limit = CFG["MAX_CTX_CHARS"]
    if len(text) <= limit:
        return text

    intervals = [(0, min(400, len(text)))]

    def rendered_length(spans):
        return sum(end - start for start, end in spans) + max(0, len(spans) - 1) * 6

    for unit in matched_units:
        unit_text = unit["text"]
        start = text.find(unit_text) if unit_text else -1
        if start < 0:
            continue
        end = start + len(unit_text)
        start = max(start, intervals[0][1])
        if start >= end:
            continue
        cost = rendered_length(intervals)
        available = limit - cost - 12
        if available <= 0:
            break
        truncated = end > start + available
        end = min(end, start + available)
        intervals.append((start, end))
        intervals.sort()
        merged = []
        for span_start, span_end in intervals:
            if merged and span_start <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], span_end))
            else:
                merged.append((span_start, span_end))
        intervals = merged
        if truncated:
            break

    pieces = []
    previous_end = 0
    for start, end in intervals:
        if start > previous_end:
            pieces.append("[...]")
        pieces.append(text[start:end])
        previous_end = end
    if previous_end < len(text):
        pieces.append("[...]")
    return "\n".join(pieces)


def _context(ctx, matched_units=None):
    matched_units = matched_units or {}
    return "\n\n".join(
        f"[{c['cite']} - {c['heading']}]\n{_section_excerpt(c, matched_units.get(c['id'], []))}"
        for c in ctx
    )


def ask(question, use_rerank=True, use_rag=True, mode="free", retrieval_query=None, max_new_tokens=300):
    """mode='free' -> free-text answer; mode='mcq' -> letter + citation (question must contain the options)."""
    tail = "Answer with the single letter (A, B, C or D) of the correct option, then on a new line cite the law and article/section number."
    if mode == "mcq":
        tail += (f" If the CONTEXT does not contain the answer, reply exactly: \"{REFUSAL}\""
                 if use_rag else ' If unsure, reply exactly: "I don\'t know".')
    else:
        tail = "Answer concisely and cite your sources."
    if not use_rag:
        return dict(answer=chat(SYSTEM_BASE, f"{question}\n\n{tail}", max_new_tokens), sources=[], contexts=[])
    rq = retrieval_query or question
    if CFG["USE_QUERY_EXPANSION"]:            # stretch: LLM turns the question into a keyword-rich search query
        rq = rq + " " + chat("Rewrite the question as a short legal search query with likely key terms. "
                             "Output only the query.", rq, 40)
    cands, matched_units = retrieve(rq, include_units=True)
    ctx = rerank(rq, cands) if use_rerank else cands[:CFG["TOP_FINAL"]]
    if CFG["USE_RELEVANCE_CHECK"]:            # stretch: refuse early if the context does not help
        v = chat("Reply YES or NO only.", f"CONTEXT:\n{_context(ctx, matched_units)}\n\nDoes the CONTEXT contain the information "
                 f"needed to answer this question?\n{rq}", 3)
        if v.upper().startswith("NO"):
            return dict(answer=REFUSAL, sources=[_src(c) for c in ctx], contexts=ctx)
    user = f"CONTEXT:\n{_context(ctx, matched_units)}\n\nQUESTION:\n{question}\n\n{tail}"
    return dict(answer=chat(SYSTEM_RAG, user, max_new_tokens), sources=[_src(c) for c in ctx], contexts=ctx)


def _src(c):
    return dict(id=c["id"], cite=c["cite"], heading=c["heading"], page=c.get("page"))


def demo():
    print("Research prototype - NOT legal advice. Empty line to quit.")
    while True:
        q = input("\nQuestion: ").strip()
        if not q:
            break
        r = ask(q)
        print("\nAnswer:", r["answer"], "\n\nSources retrieved:")
        for s in r["sources"]:
            print(f"  - {s['cite']} ({s['heading']}), pdf page {s['page']}")
