# Roadmap

## Stage 1 — Fact database

Extract every locating clause from all 18 卷, verbatim, with no interpretation.

- ✅ **Complete 2026-11-12 — 1031 records**
  - 五藏山經 (749): 南山經 73 · 西山經 153 · 北山經 177 · 東山經 86 · 中山經 303 · 五臧山經 總 2
  - 海經 (237): 海外四經 · 海內四經 · 大荒四經 · 海內經
- 45 rendered lists in `output/` (filed by origin volume), 39 audit reports in `docs/audit/`

## Stage 2 — Validation

- ⬜ Checksum each chain against its own 小結 (山數 + 總里數)
- ⬜ Flag every mismatch — never correct silently
- 🟡 **Lead — the 山經 ↔ 海經 seam**: the join is in 海內四經, not 海外/大荒. 海內東經 holds a river-source gazetteer (10 of its 27 rivers are also named in 山經) and 海內西經 restates the 崑崙 water cluster. The Han-era administrative names in 海內東經 suggest that block is a much later layer. Detail: [`output/connections/shan-hai-seams.md`](../output/connections/shan-hai-seams.md).

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
- **Output layout** — `output/` is filed by origin volume group (`wuzang-shanjing`, `haiwai-sijing`, `hainei-sijing`, `dahuang-sijing`, `haineijing`), plus `connections/`. *(Sam, 2026-11-12)*

## Honest limits

- The reconstruction is **dead reckoning** — error accumulates, and there is no loop closure to correct it. The result is *topological*, not geographic.
- The 里 is of uncertain length — deliberately irrelevant, since we never convert.
- Some scholars (e.g. 劉宗迪《失落的天书》) argue the 山經 is a **calendar/astronomical** system, not geography. This project maps *what the data implies*, not *what China looks like*.
