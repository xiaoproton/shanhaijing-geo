# Roadmap

## Stage 1 — Fact database

Extract every locating clause from all 18 卷, verbatim, with no interpretation.

- 🟡 Pilot: 南次一經 (17 records)
- ✅ 南次二經 (34 records) · 南次三經 (21 records) · 卷總 (1 record) — **南山經 complete, 73 records**
- ⬜ 西山經 (4 chains) · 北山經 (3) · 東山經 (4) · 中山經 (12)
- ⬜ 海外四經 · 海內四經 · 大荒四經 · 海內經 (qualitative layer)

## Stage 2 — Validation

- ⬜ Checksum each chain against its own 小結 (山數 + 總里數)
- ⬜ Cross-check against a second independent transcription
- ⬜ Flag every mismatch — never correct silently

## Stage 3 — `mapping_worthy` annotation

- ⬜ Mark each record: `vague` / `verified-with:<source>` / `non-accurate` / `ok`

## Stage 4 — The map

Draw the map the data implies. Three conventions, rendered side by side:

- **A · Independent strips** — each chain drawn alone. *Zero cross-chain assumptions.*
- **B · Common-origin fan** — all 首 mountains at one point, chains radiating. *One labelled assumption.*
- **C · Network only** — nodes and labelled edges, no geometry.

Fixed parameters (explicit, never hidden): 8-compass → 45° bearings · 1 里 = 1 unit (arbitrary scale, **no km conversion**) · overlaps allowed.

## Decisions (settled)

- **Bracket scope** — every implicit referent gets one: `又`, `焉` and `其` alike. *(Sam, 2026-11-12)*
- **Second source** — none. zh.wikisource is the single source; no cross-checking against 漢典古籍 / 國學大師 / 袁珂《山海經校注》. *(Sam, 2026-11-12)*
- **望 statements** — included, typed `望` (direction info).
- **郭璞注** — excluded entirely; the source text is stripped of the commentary.

## Honest limits

- The reconstruction is **dead reckoning** — error accumulates, and there is no loop closure to correct it. The result is *topological*, not geographic.
- The 里 is of uncertain length — deliberately irrelevant, since we never convert.
- Some scholars (e.g. 劉宗迪《失落的天书》) argue the 山經 is a **calendar/astronomical** system, not geography. This project maps *what the data implies*, not *what China looks like*.
