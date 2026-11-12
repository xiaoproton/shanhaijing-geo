#!/usr/bin/env python3
"""Generate the per-volume audit for a 海經 volume.

Shows every character that was dropped, so a reviewer can challenge the rule
rather than having to trust the extractor.

Usage:  python3 tools/audit_hai.py 海外南經 < /tmp/shj_海外南經.txt
"""
import re
import sys

from extract_hai import PATTERNS, RE_REGION

TAGS = [
    (r"祠|葬|珥|踐|操|戴|乘|使四鳥|黍食", "ritual"),
    (r"食之|可以|不死|壽|百歲", "medicine"),
    (r"草|木|華|葉|實|竹|樹|禾", "flora"),
    (r"獸|鳥|魚|蛇|龜|蟲|狐|虎|豹|馬|牛|羊|犬|豕|猿|鼠|龍|鳳", "fauna"),
    (r"金|玉|石|丹|銀|鐵|銅|沙|礫", "minerals"),
]


def tag(text):
    hits = [name for pat, name in TAGS if re.search(pat, text)]
    return " · ".join(hits) if hits else "description"


def split_kept(p):
    kept = []
    for s in [x.strip() for x in p.split("。") if x.strip()]:
        if RE_REGION.match(s):
            kept.append(s)
            continue
        for c in re.split(r"[，。；]", s):
            c = c.strip()
            if not c:
                continue
            for _typ, pat in PATTERNS:
                if pat.match(c):
                    kept.append(c)
                    break
    excluded = p
    for k in kept:
        excluded = excluded.replace(k, "", 1)
    excluded = re.sub(r"[，。；]{2,}", "。", excluded)
    return kept, excluded


def main():
    title = sys.argv[1]
    text = sys.stdin.read()
    parts = re.split(r"^==([^=]+)==\s*$", text, flags=re.M)
    sections = {}
    for i in range(1, len(parts), 2):
        sections[parts[i].strip()] = parts[i + 1]
    for chain, body in sections.items():
        if chain == "註釋":
            continue
        print(f"# Audit — {chain}\n")
        print("Per-entry record of **what was excluded** and why. This is the safety net: it lets anyone see every character dropped, and challenge the rule.\n")
        print("Rule applied: *include a clause if it asserts a spatial relation between two named places.* Everything below asserts no spatial relation.\n")
        print(f"Source: zh.wikisource, `山海經/{title}` (郭璞注 removed).\n")
        print("---\n")
        paras = [p.strip() for p in body.split("\n") if p.strip()]
        for n, p in enumerate(paras, 1):
            kept, excluded = split_kept(p)
            print(f"### Entry {n}\n")
            if kept:
                print("**Kept:** " + " · ".join(f"`{k}`" for k in kept) + "\n")
            if excluded.strip("，。；"):
                print("**Excluded:**")
                print(f"> {excluded.strip('，。；')}\n")
                print(f"*{tag(excluded)}*\n")


if __name__ == "__main__":
    main()
