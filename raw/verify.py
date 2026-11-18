import json
chunks = json.load(open("chunks.json", encoding="utf-8"))
print("longest 8:", [(c["id"], c["n_chars"]) for c in sorted(chunks, key=lambda c: -c["n_chars"])[:8]])

units = json.load(open("embed_units.json", encoding="utf-8"))
print("embed units:", len(units), "| keys:", list(units[0].keys()) if isinstance(units, list) else list(units)[:5])
if isinstance(units, list):
    lens = sorted(len(u.get("text", "")) for u in units)
    print("unit length min/median/max:", lens[0], lens[len(lens)//2], lens[-1])