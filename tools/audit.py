#!/usr/bin/env python3
"""Generate the per-次經 audit: what was kept, what was excluded, and why.

The audit is the safety net — it shows every character that was dropped, so a
reviewer can challenge the rule rather than having to trust the extractor.

Usage:  python3 tools/audit.py 西山經 < /tmp/shj_xishan_clean.txt
"""
import re
import sys

from extract import (
    OTHER,
    RE_CHAIN,
    RE_CHAIN_NAME,
    RE_HEAD,
    RE_SUBSUM,
    RE_SUM,
    PREFIX,
)

TAGS = [
    (r"祠|瘞|糈|珪|璧|太牢|少牢|犧|齋|酒|席", "ritual"),
    (r"食之|佩之|可以|不饑|不聾|不妬|不蠱|已[癭痔瘧]|無[腫臥]疾", "medicine"),
    (r"草|木|華|葉|實|竹|菅|蕙", "flora"),
    (r"獸|鳥|魚|蛇|龜|蟲|狐|虎|豹|馬|牛|羊|犬|豕|猿|鼠|犀|兕|鹿", "fauna"),
    (r"金|玉|石|丹|銀|鐵|銅|沙|礫|雘|碧", "minerals"),
]


def tag(text):
    hits = [name for pat, name in TAGS if re.search(pat, text)]
    return " · ".join(hits) if hits else "description"


def split_kept(p):
    """Return (kept_clauses, excluded_text) for one paragraph."""
    kept = []
    rest = p
    m = RE_HEAD.match(rest)
    if m:
        kept.append(m.group(0))
        rest = rest[m.end():]
    while True:
        rest = rest.lstrip("，。；")
        m = RE_CHAIN.match(rest)
        if not m:
            break
        kept.append(m.group(0))
        rest = rest[m.end():]
    while rest:
        rest = rest.lstrip("，。；")
        if not rest:
            break
        hit = False
        for _typ, pat in OTHER:
            m = pat.match(rest)
            if m:
                kept.append(m.group(0))
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
        kept.append(m.group(0))
    excluded = p
    for k in kept:
        excluded = excluded.replace(k, "", 1)
    return kept, excluded


def entry_name(p):
    m = RE_HEAD.match(p)
    if m:
        return m.group(2).strip()
    m = RE_CHAIN.match(p)
    if m:
        nm = RE_CHAIN_NAME.match(m.group(0))
        if nm:
            return nm.group(1).strip()
    return p[:12]


def main():
    title = sys.argv[1]
    text = sys.stdin.read()
    parts = re.split(r"^==([^=]+)==\s*$", text, flags=re.M)
    sections = {}
    for i in range(1, len(parts), 2):
        sections[parts[i].strip()] = parts[i + 1]
    for chain, body in sections.items():
        if chain not in PREFIX:
            continue
        print(f"# Audit — {chain}\n")
        print("Per-entry record of **what was excluded** and why. This is the safety net: it lets anyone see every character dropped, and challenge the rule.\n")
        print("Rule applied: *include a clause if it asserts a spatial relation between two named places.* Everything below asserts no spatial relation.\n")
        print(f"Source: zh.wikisource, `山海經/{title}` (郭璞注 removed).\n")
        print("---\n")
        paras = [p.strip() for p in body.split("\n") if p.strip()]
        n = 0
        for p in paras:
            if RE_SUM.match(p):
                print("### 小結\n")
                print(f"**Kept:** `{RE_SUM.match(p).group(0)}`\n")
                tail = p[RE_SUM.match(p).end():].strip("。；，")
                if tail:
                    print("**Excluded:**")
                    print(f"> {tail}\n")
                    print(f"*{tag(tail)}*\n")
                continue
            n += 1
            kept, excluded = split_kept(p)
            print(f"### Entry {n} — {entry_name(p)}\n")
            print("**Kept:** " + " · ".join(f"`{k}`" for k in kept) + "\n")
            if excluded.strip("，。；"):
                print("**Excluded:**")
                print(f"> {excluded.strip('，。；')}\n")
                print(f"*{tag(excluded)}*\n")


if __name__ == "__main__":
    main()
