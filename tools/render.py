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
    "西次一經": "xi-ci-yi-jing",
    "西次二經": "xi-ci-er-jing",
    "西次三經": "xi-ci-san-jing",
    "西次四經": "xi-ci-si-jing",
    "西山經（總）": "xi-shan-jing-total",
    "北次一經": "bei-ci-yi-jing",
    "北次二經": "bei-ci-er-jing",
    "北次三經": "bei-ci-san-jing",
    "北山經（總）": "bei-shan-jing-total",
    "東次一經": "dong-ci-yi-jing",
    "東次二經": "dong-ci-er-jing",
    "東次三經": "dong-ci-san-jing",
    "東次四經": "dong-ci-si-jing",
    "東山經（總）": "dong-shan-jing-total",
    "中次一經": "zhong-ci-yi-jing",
    "中次二經": "zhong-ci-er-jing",
    "中次三經": "zhong-ci-san-jing",
    "中次四經": "zhong-ci-si-jing",
    "中次五經": "zhong-ci-wu-jing",
    "中次六經": "zhong-ci-liu-jing",
    "中次七經": "zhong-ci-qi-jing",
    "中次八經": "zhong-ci-ba-jing",
    "中次九經": "zhong-ci-jiu-jing",
    "中次十經": "zhong-ci-shi-jing",
    "中次十一經": "zhong-ci-shi-yi-jing",
    "中次十二經": "zhong-ci-shi-er-jing",
    "中山經（總）": "zhong-shan-jing-total",
}

SOURCE = {
    "南山經": "zh.wikisource, `山海經/南山經`",
    "西山經": "zh.wikisource, `山海經/西山經`",
    "北山經": "zh.wikisource, `山海經/北山經`",
    "東山經": "zh.wikisource, `山海經/東山經`",
    "中山經": "zh.wikisource, `山海經/中山經`",
}


def load():
    recs = []
    for line in DATA.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            recs.append(json.loads(line))
    return recs


def render(volume, chain, recs):
    out = [
        f"# {volume} · {chain} — locating clauses",
        "",
        f"Source: {SOURCE.get(volume, 'zh.wikisource')}",
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
        groups.setdefault((r["卷"], r["次经"]), []).append(r)

    OUT.mkdir(exist_ok=True)
    for (volume, chain), items in groups.items():
        slug = SLUG.get(chain, chain)
        path = OUT / f"{slug}.md"
        path.write_text(render(volume, chain, items), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}  ({len(items)} records)")


if __name__ == "__main__":
    main()
