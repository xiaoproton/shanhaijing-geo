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

### 北山經

| chain | 小結 states | chain actually lists | distance stated | distance summed |
|---|---|---|---|---|
| 北次一經 | 25 山 | 25 山 ✓ | 5490 里 | 5680 里 |
| 北次二經 | 17 山 | 16 山 | 5690 里 | 5240 里 |
| 北次三經 | 46 山 | 46 山 ✓ | 12350 里 | 11440 里 |
| 北山經（總） | 87 山 | 87 山 ✓ | 23230 里 | 22360 里 |

The three 小結 sum to **25+17+46 = 88 山** and **5490+5690+12350 = 23530 里** — the 卷-level total says 87 山 / 23230 里. Note the 卷-level *count* (87) matches the chain listing (25+16+46), so the 北次二經 小結's "十七山" is the odd one out.

### 東山經

| chain | 小結 states | chain actually lists | distance stated | distance summed |
|---|---|---|---|---|
| 東次一經 | 12 山 | 12 山 ✓ | 3600 里 | 3500 里 |
| 東次二經 | 17 山 | 17 山 ✓ | 6640 里 | 6640 里 ✓ |
| 東次三經 | 9 山 | 9 山 ✓ | 6900 里 | 6600 里 |
| 東次四經 | 8 山 | 8 山 ✓ | 1720 里 | 1720 里 ✓ |
| 東山經（總） | 46 山 | 46 山 ✓ | 18860 里 | 18860 里 ✓ |

The four 小結 sum to **12+17+9+8 = 46 山** and **3600+6640+6900+1720 = 18860 里** — both match the 卷-level total exactly. This is the first volume whose 卷-level checksum is internally consistent.

### 中山經

| chain | 小結 states | chain actually lists | distance stated | distance summed |
|---|---|---|---|---|
| 中山經 | 15 山 | 15 山 ✓ | 6670 里 | 937 里 |
| 中次二經 | 9 山 | 9 山 ✓ | 1670 里 | 1690 里 |
| 中次三經 | 5 山 | 5 山 ✓ | 440 里 | 80 里 |
| 中次四經 | 9 山 | 9 山 ✓ | 1670 里 | 1670 里 ✓ |
| 中次五經 | 16 山 | 15 山 | 2982 里 | 2990 里 |
| 中次六經 | 14 山 | 14 山 ✓ | 790 里 | 802 里 |
| 中次七經 | 19 山 | 19 山 ✓ | 1184 里 | 1056 里 |
| 中次八經 | 23 山 | 23 山 ✓ | 2890 里 | 3080 里 |
| 中次九經 | 16 山 | 16 山 ✓ | 3500 里 | 3650 里 |
| 中次十經 | 9 山 | 9 山 ✓ | 267 里 | 310 里 |
| 中次十一經 | 48 山 | 48 山 ✓ | 3732 里 | 4225 里 |
| 中次十二經 | 15 山 (小結作「十萬山」) | 15 山 | 2800 里 | 1849 里 |
| 中山經（總） | 197 山 | 197 山 ✓ | 21371 里 | 22339 里 |

The twelve 小結 sum to **197 山** (matching the 卷-level count) and **28595 里** — against the 卷-level 21371 里. The 中山經 chain's own 小結 (6670 里) is wildly out of scale with its fourteen hops (937 里); the 中次三經 小結 (440 里) is likewise far above its four hops (80 里).

### 五臧山經 (whole-work summary)

| states | value |
|---|---|
| 名山 | 5370 山 |
| 里 | 64056 里 |
| 天地東西 | 28000 里 |
| 天地南北 | 26000 里 |
| 出水之山 | 8000 里 |
| 受水之山 | 8000 里 |
| 出銅之山 | 467 |
| 出鐵之山 | 3690 |

Recorded as WZ-01/WZ-02. The 五藏山經's own 197 山 / 21371 里 (中山經 卷總) is a different figure from the 5370 山 / 64056 里 here — the latter counts the whole world, not the 五藏山經.

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
| B1-23 | `在而南流注于杠水` — 在而 likely a dittography |
| B1-29 | `北二百八十里` — lacks 又 |
| B2-26 | `又北水行五百里，流沙三百里，至于洹山` — two distances in one clause |
| B3-40 | `東三百里` — lacks 又 |
| B3-86 | `北百二十里` — lacks 又 |
| B3-100 | 小結 says `無逢之山`, the chain says `錞于毋逢之山` |
| D1-02 | `食水出焉。而東北流注于海` — sentence break where the rest of the volume uses a comma |
| D1-06 | `掛水出焉。而北流注于湖水` — same |
| D3-01 | `又《東次三經》之首` — carries a leading 又 |
| D3-08 | `其上有水出焉，名曰碧陽` — the water is named in a following clause |
| D3-10 | `行五百里，有山焉，曰跂踵之山` — not the usual `又…里` form |
| D4-01 | `又《東次四經》之首` — carries a leading 又 |
| Z1-20 | 小結 `白甘棗之山` — 白 for 自 |
| Z3-06 | `又東十里曰騩山` — no comma before 曰 |
| Z4-03 | `西五十里` — lacks 又 |
| Z5-02 | `東三百里` — lacks 又 |
| Z5-05 | `東北五百里` — lacks 又 |
| Z5-22 | 小結 `自苟林之山`, 首山 `苟牀之山` |
| Z6-04 | `西十里` — lacks 又 |
| Z7-07 | `明水出焉。南流注于伊水` — sentence break |
| Z7-24 | `而東南注于役水` — lacks 流 |
| Z7-25 | `而東北流注于役` — lacks 水 |
| Z7-27 | `北流注于役` — lacks 水 |
| Z8-03 | `東北百里` — lacks 又 |
| Z9-02 | `東注于江` — lacks 流 |
| Z10-10 | 小結 `自首山`, 首山 `首陽之山` |
| Z12-11 | `又東南一百五十九里，有堯山` — 有 instead of 曰 |
| Z12-17 | 小結 `凡十萬山` — likely 十五山 |

## Boundary cases

- **望 statements** — included, typed `望`, as direction information (confirmed 2026-11-12). 南山經: 5 (N2-03, N2-04, N2-12, N2-13, N2-33). 西山經: 11 (X3-03…06, X3-10, X3-12, X3-21…24, X3-48). 北山經: 4 (B3-18, B3-19, B3-98, B3-99). 東山經: 7 (D2-03…05, D2-28, D3-02, D3-13, D3-14). 中山經: 4 (Z3-02, Z3-04, Z6-02, Z6-03).
- **`西望日之所入` (X3-48)** — the referent is a description, not a place name. Included anyway, flagged.
- **Vague locators with no distance** — `臨於西海之上` (N1-03) · `其尾踆於東海` (N1-15) · `西臨流黃` (N2-02) · `處于東海` (N2-32) · `其南有谷，曰育遺` (N3-09) · `其南有谷焉，曰中谷` (N3-16) · `在河之南` (X3-02) · `臨彼嶽崇之山` (X3-11) · `是錞于西海` (X1-36) · `其東有林焉` (B3-38) · `是錞于北海` (B2-29) · `北臨乾昧` (D1-02) · `北臨食水` (D2-02) · `南臨䃌水` (D2-27) · `東臨扶木` (D4-02).
- **Sub-chain distance** — `自峚山至于鍾山，四百六十裏` (X3-15) — a distance between two named places inside an entry, not a 小結. Typed `小结`.
- **首山 clause carrying extra locators** — 北次二經's opening is `《北次二經》之首，在河之東，其首枕汾，其名曰管涔之山` (B2-01): the naming clause, a 相对方位 and a 首-pivot all in one sentence, recorded as one verbatim record.
- **`其首曰X` (peak-naming)** — `其首曰招搖之山` (N1-02) and `其首曰歸山` (B3-02) name the first *peak* of the chain's opening mountain. Recorded as their own records. **The chain referent is taken from the 小結, not from this clause**: 南山經's 小結 runs `自招搖之山`, so its chain referent is 招搖之山; 北次三經's runs `自太行之山`, so its referent stays 太行之山. The two chains resolve differently and each follows its own 小結.
- **Chain node that is not a mountain** — `泰澤` (B3-95 → B3-96) and `流沙` (D3-09 → D3-10) are a marsh and a desert, not 山, but they are chain nodes and are recorded as such.

## Cross-source check

- The 南次三經 count discrepancy (13 listed vs 14 stated) was **independently confirmed** against a second online transcription — it is a feature of the text, not a transcription defect.
