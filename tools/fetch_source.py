#!/usr/bin/env python3
"""Fetch a 山海經 volume from zh.wikisource and strip it to plain text.

Removes 郭璞注 (the `{{*|…}}` commentary templates), wiki links, bold and HTML,
leaving only the classic text with its `==section==` headings.

Usage:  python3 tools/fetch_source.py 西山經 > /tmp/xishan.txt
"""
import re
import sys
import urllib.parse
import urllib.request

API = "https://zh.wikisource.org/w/index.php?title={}&action=raw"


def strip_templates(s):
    """Drop every {{…}} template, including nested ones."""
    out, depth, i = [], 0, 0
    while i < len(s):
        if s.startswith("{{", i):
            depth += 1
            i += 2
            continue
        if s.startswith("}}", i):
            depth = max(0, depth - 1)
            i += 2
            continue
        if depth == 0:
            out.append(s[i])
        i += 1
    return "".join(out)


def strip_links(s):
    s = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", s)
    s = re.sub(r"\[\[([^\]]*)\]\]", r"\1", s)
    return s


def resolve_variants(s):
    """{{另|main|variant}} and {{另2|main|note}} render as `main` — keep the main text."""
    return re.sub(r"\{\{另2?\|([^|{}]*)\|[^{}]*\}\}", r"\1", s)


def clean(raw):
    raw = resolve_variants(raw)
    raw = strip_templates(raw)
    raw = strip_links(raw)
    raw = re.sub(r"'''?", "", raw)
    raw = re.sub(r"<[^>]+>", "", raw)
    return raw


def main():
    title = sys.argv[1] if len(sys.argv) > 1 else "西山經"
    url = API.format(urllib.parse.quote("山海經/" + title))
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "shanhaijing-geo/0.1 (https://github.com/xiaoproton/shanhaijing-geo)"},
    )
    raw = urllib.request.urlopen(req).read().decode("utf-8")
    sys.stdout.write(clean(raw))


if __name__ == "__main__":
    main()
