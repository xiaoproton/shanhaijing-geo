#!/usr/bin/env python3
"""Render the fact database into human-readable Markdown bullet lists.

Usage:  python3 tools/render.py
Writes one file per 次經 into output/.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "shanhaijing_locations.jsonl"
OUT = ROOT / "output"

SLUG = {
    "南次一經": "nan-ci-yi-jing",
    "南次二經": "nan-ci-er-jing",
    "南次三經": "nan-ci-san-jing",
    "南山經（總）": "nan-shan-jing-total",
}

SOURCE = "zh.wikisource, `山海經/南山經`"


def load():
    recs = []
    for line in DATA.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            recs.append(json.loads(line))
    return recs


def render(chain, recs):
    out = [
        f"# 南山經 · {chain} — locating clauses",
        "",
        f"Source: {SOURCE}",
        f"Records: {len(recs)}",
        "Generated from: `data/shanhaijing_locations.jsonl`",
        "",
        "---",
        "",
    ]
    for r in recs:
        out.append(f"**{r['id']}** · {r['类型']}")
        out.append(f"> {r['原文']}")
        if r.get("备注"):
            out.append(f"*{r['备注']}*")
        out.append("")
    return "\n".join(out)


def main():
    recs = load()
    groups = {}
    for r in recs:
        groups.setdefault(r["次经"], []).append(r)

    OUT.mkdir(exist_ok=True)
    for chain, items in groups.items():
        slug = SLUG.get(chain, chain)
        path = OUT / f"{slug}.md"
        path.write_text(render(chain, items), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}  ({len(items)} records)")


if __name__ == "__main__":
    main()
