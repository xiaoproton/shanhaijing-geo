# Observations

Findings recorded during extraction. **Nothing here is corrected** — these are flags for stage 2 (validation).

## Checksum mismatches

### 南山經

| chain | 小結 states | chain actually lists | distance stated | distance summed |
|---|---|---|---|---|
| 南次一經 | 10 山 | 9 山 | 2950 里 | 2700 里 |
| 南次二經 | 17 山 | 17 山 ✓ | 7200 里 | 7210 里 |
| 南次三經 | 14 山 | 13 山 | 6530 里 | 5730 里 |
| 南山經（總） | 40 山 | 39 山 | 16380 里 | 15640 里 |

The three 小結 sum to **10+17+14 = 41 山** and **2950+7200+6530 = 16680 里** — neither matches the 卷-level total of 40 山 / 16380 里.

### 西山經

| chain | 小結 states | chain actually lists | distance stated | distance summed |
|---|---|---|---|---|
| 西次一經 | 19 山 | 19 山 ✓ | 2957 里 | 3045 里 |
| 西次二經 | 17 山 | 17 山 ✓ | 4140 里 | 4570 里 |
| 西次三經 | 23 山 | 23 山 ✓ | 6744 里 | 6640 里 |
| 西次四經 | 19 山 | 19 山 ✓ | 3680 里 | 3385 里 \* |
| 西山經（總） | 77 山 | 78 山 | 17517 里 | 17540 里 |

\* 西次四經 contains `北百二百里` (X4-09), which is malformed — the parser reads it as 300; 120 and 220 are the plausible readings. None of the three makes the chain sum to the stated 3680.

The four 小結 sum to **19+17+23+19 = 78 山** and **2957+4140+6744+3680 = 17521 里** — the 卷-level total says 77 山 / 17517 里.

## Source irregularities (preserved verbatim)

| id | irregularity |
|---|---|
| N1-09 | `又東三百里柢山` — lacks 曰 |
| N2-06 | `東南四百五十里曰長右之山` — lacks 又 |
| N2-31 | `東五百里，曰漆吳之山` — lacks 又 |
| N3-02 | `東五百里，曰禱過之山` — lacks 又 |
| N3-08 | `至於旄山之尾` — 至於 instead of 曰 |
| N3-10 | `至于非山之首` — 至于 instead of 曰 |
| N3-14 | `黑水山焉` — likely 出焉 |
| X1-22 | `又西四百八里` — likely 又西四百八十里 |
| X1-29 | `塗途之山` — 通行本作 臯塗之山 |
| X1-37 | `西流于於海` — 于於 likely a dittography |
| X2-23 | `又西三百裏五十里` — 裏 for 里 |
| X4-08 | `而江流注于河` — 江流 likely 東流 |
| X4-09 | `北百二百里` — malformed |

## Boundary cases

- **望 statements** — included, typed `望`, as direction information (confirmed 2026-11-12). 南山經: 5 records. 西山經: 11 records (X3-03…06, X3-10, X3-12, X3-20…23, X3-47).
- **`西望日之所入` (X3-47)** — the referent is a description, not a place name. Included anyway, flagged.
- **Vague locators with no distance** — `臨於西海之上` (N1-03) · `其尾踆於東海` (N1-15) · `西臨流黃` (N2-02) · `處于東海` (N2-32) · `其南有谷，曰育遺` (N3-09) · `其南有谷焉，曰中谷` (N3-16) · `在河之南` (X3-02) · `臨彼嶽崇之山` (X3-11) · `是錞于西海` (X1-36).
- **Sub-chain distance** — `自峚山至于鍾山，四百六十裏` (X3-15) — a distance between two named places inside an entry, not a 小結. Typed `小结`.

## Cross-source check

- The 南次三經 count discrepancy (13 listed vs 14 stated) was **independently confirmed** against a second online transcription — it is a feature of the text, not a transcription defect.
