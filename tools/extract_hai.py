#!/usr/bin/env python3
"""Draft-extract locating clauses from a cleaned 海經 volume.

The 海經 is a gazetteer of places with relative positions, not a chain of
mountains with distances, so it needs its own patterns. Like extract.py this
is a TYPING AID — every record must be reviewed by hand before commit.

Usage:  python3 tools/extract_hai.py 海外南經 < /tmp/shj_海外南經.txt
"""
import json
import re
import sys

DIR = "[東南西北中]"
RE_POS = re.compile(rf"^[^，。；]{{1,24}}在[^，。；]{{0,24}}{DIR}(?:北|南|東|西|隅)?$")
RE_WATER = re.compile(r"^[^，。；]{1,14}(?:水|河|江|沙|山|淵|澤|谷)出[^，。；]{1,14}$")
RE_BURY = re.compile(r"^[^，。；]{1,10}葬于[陰陽]$")

REGION = "(?:大荒|東海|西海|南海|北海|海內|海外|流沙|黑水|赤水|華山青水|西南黑水|甘水)"
SUFFIX = "(?:之外|之内|之中|之隅|之閒|之[東南西北]|[東南西北]隅|[東南西北]|中|隅)"
RE_REGION = re.compile(rf"^{REGION}[^，。；]{{0,6}}{SUFFIX}[，,]?[^。]*$")

PATTERNS = [
    ("相对方位", RE_POS),
    ("水系", RE_WATER),
    ("相对方位", RE_BURY),
]

PREFIX = {
    "海外南經": "HN", "海外西經": "HX", "海外北經": "HB", "海外東經": "HD",
    "海內南經": "NN", "海內西經": "NX", "海內北經": "NB", "海內東經": "ND",
    "大荒東經": "KD", "大荒南經": "KN", "大荒西經": "KX", "大荒北經": "KB",
    "海內經": "HJ",
}


def extract(body, chain, prefix, volume):
    paras = [p.strip() for p in body.split("\n") if p.strip()]
    recs = []
    for p in paras:
        sentences = [s.strip() for s in p.split("。") if s.strip()]
        for s in sentences:
            if RE_REGION.match(s):
                recs.append(("相对方位", s))
                continue
            for c in re.split(r"[，。；]", s):
                c = c.strip()
                if not c:
                    continue
                for typ, pat in PATTERNS:
                    if pat.match(c):
                        recs.append((typ, c))
                        break
    out = []
    for i, (typ, text) in enumerate(recs, 1):
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
