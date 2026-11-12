#!/usr/bin/env python3
"""Draft-extract locating clauses from a cleaned 山海經 volume.

This is a TYPING AID, not an authority. It emits a draft JSONL that must be
reviewed by hand before commit — the extractor cannot tell a locating clause
from a description, and it never guesses a referent it cannot see.

Usage:  python3 tools/extract.py 西山經 < /tmp/shj_xishan_clean.txt
"""
import json
import re
import sys

DIRS = "東南|東北|西南|西北|東|西|南|北"
NUM = "[一二三四五六七八九十百千兩]+"
LI = "[里裏]"

DIST = rf"{NUM}{LI}(?:{NUM}{LI})?"

RE_HEAD = re.compile(r"^(.*?)(?:之首[，,]?曰|之首曰)([^，。；]+)")
RE_CHAIN = re.compile(rf"^(?:又)?(?:{DIRS})?(?:水行)?{DIST}[，,]?(?:曰|至[於于]?)?[^，。；]+")
RE_CHAIN_NAME = re.compile(rf"^(?:又)?(?:{DIRS})?(?:水行)?{DIST}[，,]?(?:曰|至[於于]?)?(.+)$")
RE_WATER = re.compile(r"^[^，。；]*水(?:出焉|出于)[^，。；]*(?:，[^，。；]*(?:流|注|潛)[^，。；]*)?")
RE_WANG = re.compile(rf"^(?:{DIRS})望[^，。；]+")
RE_ADJ = re.compile(r"^(?:在[^，。；]+之[東南西北]|臨[^，。；]+|其[東南西北]有[^，。；]*(?:，曰[^，。；]*)?)")
RE_SHORE = re.compile(r"^(?:處于|是錞于)[^，。；]+")
RE_SUM = re.compile(r"^(?:凡|右)[^。]*")
RE_SUBSUM = re.compile(rf"自[^，。；]+至[於于][^，。；]+，[^，。；]*{LI}")

OTHER = [
    ("水系", RE_WATER),
    ("望", RE_WANG),
    ("相对方位", RE_ADJ),
    ("水岸", RE_SHORE),
]

PREFIX = {
    "南山經之首": "N1", "南次二經": "N2", "南次三經": "N3",
    "西山經之首": "X1", "西次二經": "X2", "西次三經": "X3", "西次四經": "X4",
    "北山經之首": "B1", "北次二經": "B2", "北次三經": "B3",
    "東山經之首": "D1", "東次二經": "D2", "東次三經": "D3", "東次四經": "D4",
    "中山經之首": "Z1", "中次二經": "Z2", "中次三經": "Z3", "中次四經": "Z4",
    "中次五經": "Z5", "中次六經": "Z6", "中次七經": "Z7", "中次八經": "Z8",
    "中次九經": "Z9", "中次十經": "Z10", "中次十一經": "Z11", "中次十二經": "Z12",
}


def extract(body, chain, prefix, volume):
    paras = [p.strip() for p in body.split("\n") if p.strip()]
    recs = []
    prev = None
    for p in paras:
        m = RE_SUM.match(p)
        if m:
            recs.append(("小结", m.group(0), None))
            continue
        rest = p
        m = RE_HEAD.match(rest)
        if m:
            recs.append(("首山", m.group(0), None))
            prev = m.group(2).strip()
            rest = rest[m.end():]
        while True:
            rest = rest.lstrip("，。；")
            m = RE_CHAIN.match(rest)
            if not m:
                break
            clause = m.group(0)
            nm = RE_CHAIN_NAME.match(clause)
            recs.append(("链式方位距离", clause, prev))
            if nm:
                prev = nm.group(1).strip()
            rest = rest[m.end():]
        while rest:
            rest = rest.lstrip("，。；")
            if not rest:
                break
            hit = False
            for typ, pat in OTHER:
                m = pat.match(rest)
                if m:
                    recs.append((typ, m.group(0), prev))
                    rest = rest[m.end():]
                    hit = True
                    break
            if not hit:
                m = re.search(r"[，。；]", rest)
                if not m:
                    break
                rest = rest[m.end():]
        m = RE_SUBSUM.search(p)
        if m:
            recs.append(("小结", m.group(0), None))
    out = []
    for i, (typ, text, ref) in enumerate(recs, 1):
        if ref and typ not in ("首山", "小结"):
            text = f"({ref}){text}"
        out.append({
            "id": f"{prefix}-{i:02d}",
            "卷": volume,
            "次经": chain,
            "次序": i,
            "原文": text,
            "类型": typ,
            "mapping_worthy": "",
            "备注": "",
        })
    return out


def main():
    title = sys.argv[1]
    volume = sys.argv[2] if len(sys.argv) > 2 else title
    text = sys.stdin.read()
    parts = re.split(r"^==([^=]+)==\s*$", text, flags=re.M)
    sections = {}
    for i in range(1, len(parts), 2):
        sections[parts[i].strip()] = parts[i + 1]
    for chain, body in sections.items():
        prefix = PREFIX.get(chain)
        if prefix is None:
            print(f"# no prefix for {chain!r}", file=sys.stderr)
            continue
        for r in extract(body, chain, prefix, volume):
            print(json.dumps(r, ensure_ascii=False))


if __name__ == "__main__":
    main()
