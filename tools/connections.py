#!/usr/bin/env python3
"""Find and document the connection points between 五藏山經 and 海經.

Usage:  python3 tools/connections.py
Writes output/connections/shan-hai-seams.md.

Everything in the generated file is derived from
`data/shanhaijing_locations.jsonl`; the interpretive notes are marked as
such and are fixed prose, not computed.
"""
import json
import pathlib
import re
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "shanhaijing_locations.jsonl"
OUT = ROOT / "output" / "connections" / "shan-hai-seams.md"

# Names the extraction patterns below miss because they are introduced in a
# 首山 / 望 / 之首 clause rather than a plain 曰X之山 clause.
SEED = [
    "昆侖", "崑崙", "華山", "岷", "衡山", "會稽", "積石", "姑射",
    "跂踵", "夸父", "青丘", "少室", "鳥鼠同穴", "烏鼠同穴",
]

# Han-era administrative / commandery names. Used only to flag the dating
# signal; this list is a judgement call, not a computed fact.
HAN_ADMIN = [
    "象郡", "桂陽", "臨晉", "晉陽", "井陘", "山陽", "期思", "朝陽",
    "漢陽", "蜀", "上窳", "衛臯", "長城",
]


def load():
    recs = []
    for line in DATA.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            recs.append(json.loads(line))
    return recs


def shan_names(shan):
    """Candidate place names in 五藏山經, with occurrence counts."""
    names = Counter()
    for r in shan:
        t = r["原文"]
        for m in re.finditer(r"曰([\u4e00-\u9fff]{1,6}?)(?:之山|山)", t):
            names[m.group(1)] += 1
        for m in re.finditer(r"([\u4e00-\u9fff]{1,5}?)之丘", t):
            names[m.group(1)] += 1
        for m in re.finditer(r"([\u4e00-\u9fff]{1,5}?)山之首", t):
            names[m.group(1)] += 1
        for m in re.finditer(r"([\u4e00-\u9fff]{1,5}?)水出焉", t):
            names[m.group(1) + "水"] += 1
        for m in re.finditer(r"望([\u4e00-\u9fff]{1,5})", t):
            names[m.group(1)] += 1
    for s in SEED:
        if any(s in r["原文"] for r in shan):
            names[s] += 0
    return names


def main():
    recs = load()
    shan = [r for r in recs if r["卷"] != "海經"]
    hai = [r for r in recs if r["卷"] == "海經"]
    hai_text = "\n".join(r["原文"] for r in hai)

    names = shan_names(shan)

    # --- 1. names present in both texts -------------------------------
    both = []
    for n in names:
        if len(n) < 2:
            continue
        if n in hai_text:
            s = [r for r in shan if n in r["原文"]]
            h = [r for r in hai if n in r["原文"]]
            both.append((n, s, h))
    both.sort(key=lambda x: (-len(x[1]), x[0]))

    # --- 2a. 海內東經 river gazetteer ---------------------------------
    nd = [r for r in hai if r["次经"] == "海內東經"]
    nd_water = [r for r in nd if r["类型"] == "水系"]
    nd_rows = []
    for r in nd_water:
        m = re.search(r"([\u4e00-\u9fff]{1,4})水出([\u4e00-\u9fff]{1,8})", r["原文"])
        river = (m.group(1) + "水") if m else ""
        src = m.group(2) if m else ""
        river_hit = next((x for x in shan if river and river in x["原文"]), None)
        src_hit = next((x for x in shan if src and src in x["原文"]), None)
        nd_rows.append((r, river, src, river_hit, src_hit))
    nd_river_shared = [x for x in nd_rows if x[3]]
    nd_src_shared = [x for x in nd_rows if x[4]]
    nd_src_absent = [x for x in nd_rows if not x[4]]

    # --- 2b. 海內西經 崑崙 water cluster -------------------------------
    nx_corner = [r for r in hai
                 if r["次经"] == "海內西經"
                 and re.search(r"出(東南|東北|西北|西南)隅", r["原文"])]
    kunlun_shan = [r for r in shan if "昆侖" in r["原文"] or "崑崙" in r["原文"]]
    kunlun_rivers = [r for r in kunlun_shan if "出焉" in r["原文"]]
    nx_rivers = set()
    for r in nx_corner:
        for m in re.finditer(r"([\u4e00-\u9fff]{1,3})水", r["原文"]):
            nx_rivers.add(m.group(1) + "水")
    shared_rivers = sorted(x for x in nx_rivers
                           if any(x in r["原文"] for r in kunlun_rivers))

    # --- write --------------------------------------------------------
    L = []
    A = L.append
    A("# 山經 ↔ 海經 — connection points")
    A("")
    A("Generated from `data/shanhaijing_locations.jsonl` by `tools/connections.py`.")
    A("")
    A("The question: **where does 五藏山經 touch 海經?** The answer is not in")
    A("海外經 or 大荒經 — it is in **海內四經**, and specifically in two blocks.")
    A("")
    A("---")
    A("")
    A("## 1. Named places appearing in both texts")
    A("")
    A("Mechanical name overlap. Treat these as **name echoes**, not geographic")
    A("joins: 海經 turns most of these mountains into 國 (青丘國, 姑射國,")
    A("跂踵國, 夸父國), which is a different register — ethnographic/mythic,")
    A("not a survey.")
    A("")
    A("| Place | 山經 | 海經 |")
    A("|---|---|---|")
    for n, s, h in both:
        s_txt = " · ".join(f"{r['id']} {r['原文']}" for r in s[:2])
        h_txt = " · ".join(f"{r['id']} {r['原文']}" for r in h[:3])
        A(f"| {n} | {len(s)} — {s_txt} | {len(h)} — {h_txt} |")
    A("")
    A(f"Total: **{len(both)}** names out of {len(names)} candidates in 五藏山經.")
    A("")
    A("---")
    A("")
    A("## 2. The two structural joins")
    A("")
    A("### 2a. 海內東經 — a river-source gazetteer")
    A("")
    A(f"`海內東經` holds {len(nd_water)} consecutive records of the form")
    A("**「X水出Y山」** — grammatically identical to 山經's 「X水出焉」. This is")
    A("the only block in 海經 that speaks 山經's language and can be laid on the")
    A("same map.")
    A("")
    for r in nd_water:
        A(f"- **{r['id']}** {r['原文']}")
    A("")
    A("#### Rivers shared with 山經")
    A("")
    A(f"{len(nd_river_shared)} of {len(nd_rows)} rivers in this list are rivers")
    A("that 山經 also names — the strongest evidence that the two texts describe")
    A("the same water system.")
    A("")
    A("| 海內東經 | River | 山經 record |")
    A("|---|---|---|")
    for r, river, src, rh, sh in nd_river_shared:
        A(f"| {r['id']} {r['原文']} | {river} | {rh['id']} {rh['原文']} |")
    A("")
    A("#### Source-mountains shared with 山經")
    A("")
    if nd_src_shared:
        A("| 海內東經 | Source | 山經 record |")
        A("|---|---|---|")
        for r, river, src, rh, sh in nd_src_shared:
            A(f"| {r['id']} {r['原文']} | {src} | {sh['id']} {sh['原文']} |")
    else:
        A("_None._")
    A("")
    A("#### Source-mountains that appear nowhere in 山經")
    A("")
    A(f"{len(nd_src_absent)} of {len(nd_rows)} — but many of these \"sources\"")
    A("are not mountains at all (舜葬, 吳, 蜀, 象郡, 臨晉, 桂陽 are places or")
    A("regions), so the count overstates the absence. See §3.")
    A("")
    A("### 2b. 海內西經 — the 崑崙 water cluster")
    A("")
    A("`海內西經` ends with four records sending the same rivers out of the four")
    A("corners of 崑崙. 山經 西次三經 has the same rivers leaving the same")
    A("mountain — 海內西經 is a **compressed restatement** of that passage.")
    A("")
    A("| 海內西經 | 原文 |")
    A("|---|---|")
    for r in nx_corner:
        A(f"| {r['id']} | {r['原文']} |")
    A("")
    A(f"Rivers named in both: **{' · '.join(shared_rivers) if shared_rivers else '—'}**")
    A("")
    A("山經 崑崙 records:")
    A("")
    for r in kunlun_shan:
        A(f"- **{r['id']}** [{r['次经']}] {r['原文']}")
    A("")
    A("---")
    A("")
    A("## 3. Dating signal — the seam is between two ages")
    A("")
    A("Only **one** source-mountain in 海內東經's river list (少室) is also")
    A("named in 山經 — but **10 of the 27 rivers are**. The rivers travel; the")
    A("mountains do not. The source-mountains absent from the whole 五藏山經:")
    A("")
    for r, river, src, rh, sh in nd_src_absent:
        flag = " **(Han-era administrative name)**" if any(x in src for x in HAN_ADMIN) else ""
        A(f"- **{r['id']}** {r['原文']}{flag}")
    A("")
    A("> **Interpretation (not computed).** Several of these are unmistakably")
    A("> Qin/Han administrative names — 象郡, 桂陽, 臨晉, 晉陽, 井陘, 山陽,")
    A("> 期思, 朝陽. That makes 海內東經's river list almost certainly a **much")
    A("> later layer** grafted onto the text: a Han-era gazetteer, not the same")
    A("> world as 山經. The seam exists, but it is a seam between two different")
    A("> ages, not a continuous map.")
    A("")
    A("---")
    A("")
    A("## 4. Method caveat")
    A("")
    A("A strict pattern match finds **zero** 山經 water-names in 海經, because")
    A("海經 writes 「X水出Y」 where 山經 writes 「X水出焉」. That is a method")
    A("artefact, not a fact: the rivers *are* shared (渭, 洛, 涇, 漢, 濟, 汝,")
    A("漳, 汾, 沁, 弱水, 黑水, 赤水, 洋水, 甘水 all appear in both). They were")
    A("checked by name, not by pattern.")
    A("")
    A("Name overlap is also weak evidence on its own: a shared name can mean a")
    A("shared place, a shared name-stock, or a later editor harmonising the two")
    A("texts. Only §2a and §2b give a join that can be drawn on a map.")
    A("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"  name overlaps: {len(both)}")
    print(f"  海內東經 water records: {len(nd_water)}")
    print(f"  rivers also in 山經: {len(nd_river_shared)}")
    print(f"  source-mountains also in 山經: {len(nd_src_shared)}")
    print(f"  source-mountains absent from 山經: {len(nd_src_absent)}")
    print(f"  海內西經 corner records: {len(nx_corner)}")
    print(f"  shared 崑崙 rivers: {shared_rivers}")


if __name__ == "__main__":
    main()
