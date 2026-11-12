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
| 1 · Fact database | 🟡 **南山經 complete** — 73 records (南次一經 · 南次二經 · 南次三經 · 卷總) |
| 2 · Validation | ⬜ Not started |
| 3 · `mapping_worthy` annotation | ⬜ Not started |
| 4 · The map | ⬜ Not started |

## Contents

| Path | What |
|---|---|
| [`docs/rules.md`](docs/rules.md) | The extraction rules — inclusion test, bracket convention |
| [`docs/schema.md`](docs/schema.md) | The record schema |
| [`docs/roadmap.md`](docs/roadmap.md) | The plan, stage by stage |
| [`data/shanhaijing_locations.jsonl`](data/shanhaijing_locations.jsonl) | The fact database (source of truth) |
| [`tools/render.py`](tools/render.py) | Renders the database into the Markdown lists in `output/` |
| [`output/`](output/) | Generated human-readable bullet lists |
| [`docs/audit/`](docs/audit/) | Per-entry "excluded text" reports |

## Source

- Primary transcription: **zh.wikisource** — [`山海經/南山經`](https://zh.wikisource.org/wiki/山海經/南山經)
- A second independent source is still needed for cross-checking (see roadmap).

## Licence

- **Code and data: CC0 1.0 Universal** — see [`LICENSE`](LICENSE).
- The 山海經 text itself is public domain (ancient). Individual *transcriptions* may carry their own licence — the wikisource transcription is CC BY-SA, so quoted clauses are attributed to it in the data.
