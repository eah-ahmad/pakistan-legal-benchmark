# Muhammad Ahmad, CMS 542432, BSCS-15-D
"""
split_mcq.py - Partition benchmark datasets into development and final-test sets.
Supports:
- Generalization across all benchmark categories (MCQs, factual scenarios, multi-hop, OOS).
- Stratification across both (law, category).
- Configurable target splits (default: 80 dev, 320 final-test; falls back proportionally if pool is smaller).
- Deterministic seeding (seed=7) for strict reproducibility.
- Zero item / ID overlap between splits.
- Preserves all question metadata, options, citations, and reasoning points.
"""
import copy
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TESTS = ROOT / "tests"
DEFAULT_SRC = TESTS / "mcq_test.json"
DEFAULT_DEV_OUT = TESTS / "mcq_dev.json"
DEFAULT_FINAL_OUT = TESTS / "mcq_final.json"
DEFAULT_DEV_IDS = TESTS / "dev_ids.txt"


def alloc_dev_counts(group_sizes, total_dev):
    """
    Allocates development items across groups proportionally to group size
    using the largest-remainder method.
    """
    total = sum(group_sizes.values())
    if total == 0:
        return {k: 0 for k in group_sizes}

    # If requested dev size exceeds total items, cap at total
    effective_dev = min(total_dev, total)

    raw = {key: (count * effective_dev) / total for key, count in group_sizes.items()}
    allocated = {key: int(value) for key, value in raw.items()}
    remaining = effective_dev - sum(allocated.values())

    order = sorted(group_sizes.keys(), key=lambda key: (raw[key] - allocated[key], group_sizes[key]), reverse=True)
    for key in order[:remaining]:
        # Do not allocate more than available in the group
        if allocated[key] < group_sizes[key]:
            allocated[key] += 1

    return allocated


def split_items(items, target_dev=80, target_final=320, seed=7):
    """
    Splits items into (dev_items, final_items) stratified by (law, category).
    Preserves all original fields and attaches 'split': 'dev' and 'split': 'final'.
    """
    if not items:
        return [], []

    # Check for duplicate IDs in input
    seen_ids = set()
    for it in items:
        qid = it.get("id")
        if qid in seen_ids:
            raise ValueError(f"Duplicate item ID detected in split input: '{qid}'")
        seen_ids.add(qid)

    # Group by (law, category)
    groups = defaultdict(list)
    for it in items:
        law = it.get("law", "unspecified").lower()
        category = it.get("category", it.get("type", "general"))
        groups[(law, category)].append(copy.deepcopy(it))

    # Deterministic shuffle within each group
    rng = random.Random(seed)
    for group in groups.values():
        rng.shuffle(group)

    total_pool = len(items)
    group_sizes = {key: len(val) for key, val in groups.items()}

    # Calculate target dev count
    if total_pool < (target_dev + target_final):
        # Scale target_dev proportionally based on target ratio if pool is smaller
        ratio = target_dev / (target_dev + target_final)
        actual_target_dev = round(total_pool * ratio)
        print(f"NOTICE: Total available pool ({total_pool}) is smaller than target ({target_dev} dev + {target_final} final).")
        print(f"        Scaling dev target proportionally to {actual_target_dev} (ratio {ratio:.2f}).")
    else:
        actual_target_dev = target_dev

    dev_alloc = alloc_dev_counts(group_sizes, total_dev=actual_target_dev)

    dev_items = []
    final_items = []

    for key in sorted(groups.keys()):
        items_in_group = groups[key]
        take_n = dev_alloc.get(key, 0)
        group_dev = items_in_group[:take_n]
        group_final = items_in_group[take_n:]

        # If pool >= target_dev + target_final, slice final to target_final proportionally
        dev_items.extend(group_dev)
        final_items.extend(group_final)

    # Cap final items at target_final if more are available
    if len(final_items) > target_final:
        # If final pool exceeds target_final, sample deterministically
        rng.shuffle(final_items)
        final_items = final_items[:target_final]

    # Assign split labels
    for it in dev_items:
        it["split"] = "dev"
    for it in final_items:
        it["split"] = "final"

    # Enforce zero overlap check
    dev_id_set = {it["id"] for it in dev_items}
    final_id_set = {it["id"] for it in final_items}
    overlap = dev_id_set & final_id_set
    if overlap:
        raise RuntimeError(f"Critical error: ID overlap detected between dev and final splits: {overlap}")

    return dev_items, final_items


def summarize_split(label, items):
    law_counts = Counter(it.get("law", "unspecified") for it in items)
    cat_counts = Counter(it.get("category", it.get("type", "general")) for it in items)
    print(f"\n{label} ({len(items)} items):")
    print(f"  By Law:      {dict(sorted(law_counts.items()))}")
    print(f"  By Category: {dict(sorted(cat_counts.items()))}")


def main(src_path=None, dev_out_path=None, final_out_path=None, dev_ids_path=None,
         target_dev=80, target_final=320, seed=7):
    src = Path(src_path or DEFAULT_SRC)
    dev_out = Path(dev_out_path or DEFAULT_DEV_OUT)
    final_out = Path(final_out_path or DEFAULT_FINAL_OUT)
    dev_ids_file = Path(dev_ids_path or DEFAULT_DEV_IDS)

    if not src.exists():
        print(f"Source file does not exist: {src}")
        return

    items = json.loads(src.read_text(encoding="utf-8"))
    print(f"Loaded {len(items)} items from {src}")

    # For legacy 60-item mcq_test.json compatibility, preserve 20/40 legacy defaults
    if len(items) == 60 and target_dev == 80 and target_final == 320:
        eff_dev, eff_final = 20, 40
    else:
        eff_dev, eff_final = target_dev, target_final

    dev_items, final_items = split_items(items, target_dev=eff_dev, target_final=eff_final, seed=seed)

    summarize_split("DEVELOPMENT SET", dev_items)
    summarize_split("FINAL TEST SET", final_items)

    # Save outputs
    dev_ids = [it["id"] for it in dev_items]
    dev_ids_file.write_text("\n".join(dev_ids) + "\n", encoding="utf-8")
    dev_out.write_text(json.dumps(dev_items, ensure_ascii=False, indent=1), encoding="utf-8")
    final_out.write_text(json.dumps(final_items, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"\nWrote Dev set:   {dev_out} ({len(dev_items)} items)")
    print(f"Wrote Final set: {final_out} ({len(final_items)} items)")
    print(f"Wrote Dev IDs:   {dev_ids_file}")


if __name__ == "__main__":
    main()
