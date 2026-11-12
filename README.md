# shanhaijing-geo

Attempt to purely literally use 山海经 location text to generate 山海经地图 with almost no assumptions.

---

## The idea

The **五藏山經** (the "Classic of Mountains" section of the 山海經) is the only part of the text written in a rigid, templated format:

> 又東三百里，曰堂庭之山。

Strip away the flora, fauna, omens, medicines and ritual, and what remains is a **dead-reckoning survey** — a chain of mountains, each located by a direction and a distance from the one before it.

The **other volumes** — 海外四經 · 海內四經 · 大荒四經 · 海內經 — can be used too. They are not written in the same template and **do not always carry distance numbers**, but they still assert spatial relations (`在其北`, `在X東`, `處于東海`), so they belong in the same database, typed as relative-position records.

This project extracts that locating information **verbatim, with no interpretation**, into a machine-readable fact database, and then (later) draws the map that the data alone implies.

## Core principle — no assumptions

The extraction stage makes **no assumptions and performs no validation**. Every record is a verbatim quote from the source. Interpretation, validation and mapping all happen *downstream*, in separate, clearly-labelled stages.

Why: a verbatim quote can be checked against the source by anyone. A parsed coordinate cannot.

## Status

| Stage | State |
|---|---|
| 1 · Fact database | 🟢 **Complete** — 1031 records: 五藏山經 (南山經 · 西山經 · 北山經 · 東山經 · 中山經) + 海經 (海外四經 · 海內四經 · 大荒四經 · 海內經) + 五臧山經 summary |
| 2 · Validation | ⬜ Not started |
| 3 · `mapping_worthy` annotation | ⬜ Not started |
| 4 · The map | ⬜ Not started |

## Contents

| Path | What |
|---|---|
| [`docs/rules.md`](docs/rules.md) | The extraction rules — inclusion test, bracket convention |
| [`docs/schema.md`](docs/schema.md) | The record schema |
| [`docs/roadmap.md`](docs/roadmap.md) | The plan, stage by stage |
| [`docs/observations.md`](docs/observations.md) | Checksum mismatches, source irregularities, boundary cases |
| [`data/shanhaijing_locations.jsonl`](data/shanhaijing_locations.jsonl) | The fact database (source of truth) |
| [`tools/fetch_source.py`](tools/fetch_source.py) | Fetches a volume from zh.wikisource and strips 郭璞注 |
| [`tools/extract.py`](tools/extract.py) | Draft-extracts the 五藏山經 (typing aid — output is reviewed by hand) |
| [`tools/extract_hai.py`](tools/extract_hai.py) | Draft-extracts the 海經 |
| [`tools/audit.py`](tools/audit.py) · [`tools/audit_hai.py`](tools/audit_hai.py) | Generate the per-entry "excluded text" reports |
| [`tools/render.py`](tools/render.py) | Renders the database into the Markdown lists in `output/` |
| [`output/`](output/) | Generated human-readable bullet lists |
| [`docs/audit/`](docs/audit/) | Per-entry "excluded text" reports |

## Source

- Primary transcription: **zh.wikisource** — [`山海經`](https://zh.wikisource.org/wiki/山海經) (the 四庫全書 text with 郭璞注; the commentary is stripped, the classic text is kept verbatim).
- The transcription's own variant readings (`{{另|A|B}}`) are resolved to the main reading **A**; the variant is not carried into the database.

## Licence

- **Code and data: CC0 1.0 Universal** — see [`LICENSE`](LICENSE).
- The 山海經 text itself is public domain (ancient). Individual *transcriptions* may carry their own licence — the wikisource transcription is CC BY-SA, so quoted clauses are attributed to it in the data.

---

## Who made this

This project is mainly built by **Emma Nanob**, an AI agent. The extraction, the schema, the tooling and the audits are hers, working from a human's brief.

- Bluesky: [@emmananob.bsky.social](https://bsky.app/profile/emmananob.bsky.social)

**Humans and agents are both welcome to review.** If you find a clause that was mis-extracted, a rule that is wrong, or a place where an assumption crept in — open an issue or a pull request. The whole point of the verbatim-quote design is that every claim here can be checked against the source by anyone.
