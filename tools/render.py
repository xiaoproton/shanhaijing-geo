#!/usr/bin/env python3
"""Render the fact database into human-readable Markdown bullet lists.

Usage:  python3 tools/render.py
Writes one file per 次經 into output/<group>/.
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
    "中山經": "zhong-ci-yi-jing",
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
    "五臧山經（總）": "wu-zang-shan-jing-total",
    "海外南經": "hai-wai-nan-jing",
    "海外西經": "hai-wai-xi-jing",
    "海外北經": "hai-wai-bei-jing",
    "海外東經": "hai-wai-dong-jing",
    "海內南經": "hai-nei-nan-jing",
    "海內西經": "hai-nei-xi-jing",
    "海內北經": "hai-nei-bei-jing",
    "海內東經": "hai-nei-dong-jing",
    "大荒東經": "da-huang-dong-jing",
    "大荒南經": "da-huang-nan-jing",
    "大荒西經": "da-huang-xi-jing",
    "大荒北經": "da-huang-bei-jing",
    "海內經": "hai-nei-jing",
}

# Origin-volume groups. Each 次經 is filed under the volume group it belongs to.
GROUP = {
    "南山經": "wuzang-shanjing",
    "西山經": "wuzang-shanjing",
    "北山經": "wuzang-shanjing",
    "東山經": "wuzang-shanjing",
    "中山經": "wuzang-shanjing",
    "五臧山經": "wuzang-shanjing",
    "海外南經": "haiwai-sijing",
    "海外西經": "haiwai-sijing",
    "海外北經": "haiwai-sijing",
    "海外東經": "haiwai-sijing",
    "海內南經": "hainei-sijing",
    "海內西經": "hainei-sijing",
    "海內北經": "hainei-sijing",
    "海內東經": "hainei-sijing",
    "大荒東經": "dahuang-sijing",
    "大荒南經": "dahuang-sijing",
    "大荒西經": "dahuang-sijing",
    "大荒北經": "dahuang-sijing",
    "海內經": "haineijing",
}

SOURCE = {
    "南山經": "zh.wikisource, `山海經/南山經`",
    "西山經": "zh.wikisource, `山海經/西山經`",
    "北山經": "zh.wikisource, `山海經/北山經`",
    "東山經": "zh.wikisource, `山海經/東山經`",
    "中山經": "zh.wikisource, `山海經/中山經`",
    "海經": "zh.wikisource, `山海經/海外四經` · `海內四經` · `大荒四經` · `海內經`",
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
        group = GROUP.get(chain) or GROUP.get(volume)
        if group is None:
            raise SystemExit(f"no origin-volume group for {volume} / {chain}")
        folder = OUT / group
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"{slug}.md"
        path.write_text(render(volume, chain, items), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}  ({len(items)} records)")


if __name__ == "__main__":
    main()
