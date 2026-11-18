# Muhammad Ahmad, CMS 542432, BSCS-15-D
"""
make_questions.py - builds DRAFT test sets for you to review by hand. Every row is "needs human review".

  python make_questions.py                  (LOCAL, templates only, no model needed)
  python make_questions.py --llm            (COLAB GPU: an LLM writes natural retrieval questions + scenario text)
  options: --n-mcq 60  --n-retrieval 30  --seed 7  --model Qwen/Qwen2.5-3B-Instruct

Needs chunks.json (from chunk.py).  Writes review/retrieval_draft.csv, review/mcq_draft.csv, review/oos_draft.csv
Review step: open the CSVs in Excel/VS Code, fix wording, set the 'status' column to ok (or drop), then run
             python build_tests.py   -> tests/retrieval_test.json, tests/mcq_test.json, tests/out_of_scope.json

RULES: test files are NEVER indexed as corpus text (the index is built only from chunks.json / embed_units.json)
       and are kept in tests/ with "split": "test" so they can never leak into future fine-tuning data.
"""
import argparse, csv, json, random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REVIEW = ROOT / "review"
NEEDS = "needs human review"
LAW_NAME = {"constitution": "Constitution of Pakistan", "ppc": "Pakistan Penal Code", "peca": "PECA 2016"}
LABEL = {"constitution": "Article", "ppc": "Section", "peca": "Section"}

# ---------------------------------------------------------------- optional LLM (Colab)
_llm = {}


def load_llm(model_id):
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM
    _llm["tok"] = AutoTokenizer.from_pretrained(model_id)
    _llm["model"] = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")


def llm(prompt, max_new_tokens=90):
    tok, model = _llm["tok"], _llm["model"]
    ids = tok.apply_chat_template([{"role": "user", "content": prompt}], add_generation_prompt=True,
                                  return_tensors="pt", return_dict=True).to(model.device)
    out = model.generate(**ids, max_new_tokens=max_new_tokens, do_sample=False)
    return tok.decode(out[0][ids["input_ids"].shape[1]:], skip_special_tokens=True).strip().strip('"')


def llm_question(c):
    return llm("Below is a provision of Pakistani law. Write ONE plain-English question an ordinary person might ask "
               "that this provision answers. Do NOT mention the section/article number or its exact title. "
               "Output only the question.\n\n" + c["text"][:1500])


def llm_scenario(c):
    return llm("Below is a provision of Pakistani law. Write a 1-2 sentence everyday scenario in which a person does "
               "something that falls under this provision. Do NOT mention the law, section number or its title. "
               "Output only the scenario.\n\n" + c["text"][:1500], 100)


# ---------------------------------------------------------------- helpers
def write_csv(path, rows, cols):
    REVIEW.mkdir(exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {path} ({len(rows)} rows)")


def short(s, n=90):
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def opt_label(c):
    return f"{LABEL[c['law']]} {c['number']}"


def mcq_row(i, typ, c, q, correct, distractors, rng):
    opts = [correct] + distractors[:3]
    rng.shuffle(opts)
    letters = "ABCD"
    return dict(id=f"mq{i:03d}", type=typ, law=c["law"], question=q, A=opts[0], B=opts[1], C=opts[2], D=opts[3],
                answer=letters[opts.index(correct)], source_id=c["id"], status=NEEDS, notes="")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--llm", action="store_true")
    ap.add_argument("--model", default="Qwen/Qwen2.5-3B-Instruct")
    ap.add_argument("--n-mcq", type=int, default=60)
    ap.add_argument("--n-retrieval", type=int, default=30)
    ap.add_argument("--seed", type=int, default=7)
    a = ap.parse_args()
    rng = random.Random(a.seed)
    if a.llm:
        load_llm(a.model)

    chunks = json.loads((ROOT / "chunks.json").read_text(encoding="utf-8"))
    usable = {l: [c for c in chunks if c["law"] == l and c["kind"] != "schedule" and len(c["text"]) >= 120
                  and len(c["heading"]) >= 8] for l in LAW_NAME}
    used = set()

    def take(law, n):
        pool = [c for c in usable[law] if c["id"] not in used]
        rng.shuffle(pool)
        got = pool[:n]
        used.update(c["id"] for c in got)
        return got

    # ---------------- retrieval questions (balanced over laws)
    rows, k = [], 1
    per = a.n_retrieval // 3
    for law in LAW_NAME:
        for c in take(law, per):
            q = llm_question(c) if a.llm else f"What does Pakistani law provide regarding: {c['heading']}?"
            rows.append(dict(id=f"rq{k:03d}", question=q, source_id=c["id"], law=law, heading=c["heading"],
                             text_preview=c["text"][:300], method="llm" if a.llm else "template",
                             status=NEEDS, notes=""))
            k += 1
    write_csv(REVIEW / "retrieval_draft.csv", rows,
              ["id", "question", "source_id", "law", "heading", "text_preview", "method", "status", "notes"])

    # ---------------- MCQs (balanced over laws; lookup / define / scenario)
    per_law = a.n_mcq // 3
    n_sc = round(per_law * 0.25) if a.llm else 0
    n_lk = round((per_law - n_sc) * 0.45)
    n_df = per_law - n_sc - n_lk
    if not a.llm:
        print("note: no --llm, so no scenario MCQs (run with --llm on Colab to add ~25%).")
    rows, k = [], 1
    for law in LAW_NAME:
        allc = usable[law]
        for typ, n in (("lookup", n_lk), ("define", n_df), ("scenario", n_sc)):
            for c in take(law, n):
                others = [o for o in allc if o["id"] != c["id"]]
                if typ == "lookup":      # given the number, pick the heading
                    q = f"What is the subject (heading) of {opt_label(c)} of the {LAW_NAME[law]}?"
                    pool = [o for o in others if o["heading"] != c["heading"]]
                    d = [short(o["heading"]) for o in rng.sample(pool, 3)]
                    rows.append(mcq_row(k, typ, c, q, short(c["heading"]), d, rng))
                else:                    # given the subject / scenario, pick the number
                    i0 = allc.index(c)
                    near = [o for o in allc[max(0, i0 - 8): i0 + 9] if o["id"] != c["id"]]
                    far = rng.sample(others, 3)
                    pick = (rng.sample(near, min(3, len(near))) + far)[:3]
                    if typ == "define":
                        q = f"Which {LABEL[law].lower()} of the {LAW_NAME[law]} deals with \"{short(c['heading'], 120)}\"?"
                    else:
                        q = f"{llm_scenario(c)} Which provision of the {LAW_NAME[law]} applies most directly?"
                    rows.append(mcq_row(k, typ, c, q, opt_label(c), [opt_label(o) for o in pick], rng))
                k += 1
    write_csv(REVIEW / "mcq_draft.csv", rows,
              ["id", "type", "law", "question", "A", "B", "C", "D", "answer", "source_id", "status", "notes"])

    # ---------------- out-of-scope (must be refused)
    mx = {l: max([int("".join(ch for ch in c["number"] if ch.isdigit()) or 0) for c in chunks if c["law"] == l] or [0])
          for l in LAW_NAME}
    oos = [
        ("fake_number", f"What does Section 999 of the Pakistan Penal Code say?"),
        ("fake_number", f"What is the punishment under Section {mx['ppc'] + 140} of the Pakistan Penal Code?"),
        ("fake_number", f"Explain Article {mx['constitution'] + 120} of the Constitution of Pakistan."),
        ("fake_number", f"What does Article {mx['constitution'] + 300} of the Constitution of Pakistan guarantee?"),
        ("fake_number", f"What does Section {mx['peca'] + 40} of PECA 2016 provide?"),
        ("other_country", "What is the punishment for theft under Section 379 of the Indian Penal Code?"),
        ("other_country", "What does the First Amendment of the US Constitution protect?"),
        ("other_country", "What is the mandatory minimum sentence for murder under English law?"),
        ("other_country", "Explain the right to erasure under Article 17 of the GDPR."),
        ("other_country", "What does Section 7 of the Canadian Charter of Rights and Freedoms guarantee?"),
        ("other_pk_law", "What is the procedure for incorporating a company under the Companies Act, 2017?"),
        ("other_pk_law", "What are the income tax slabs for salaried individuals in Pakistan?"),
        ("other_pk_law", "What does the Code of Criminal Procedure say about the time limit for filing an appeal?"),
        ("unrelated", "What is the capital of France?"),
        ("unrelated", "Write a Python function that reverses a string."),
        ("unrelated", "How do I cook chicken biryani?"),
        ("unrelated", "Who won the 2022 FIFA World Cup?"),
        ("unrelated", "What is the recommended treatment for type 2 diabetes?"),
    ]
    rows = [dict(id=f"oos{i:03d}", question=q, category=cat, status=NEEDS, notes="")
            for i, (cat, q) in enumerate(oos, 1)]
    write_csv(REVIEW / "oos_draft.csv", rows, ["id", "question", "category", "status", "notes"])
    print("\nNEXT: edit review/*.csv (status -> ok / drop), then run: python build_tests.py")


if __name__ == "__main__":
    main()
