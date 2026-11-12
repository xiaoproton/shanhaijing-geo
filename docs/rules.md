# Extraction rules

## 1. The inclusion test

> **Include a clause if it asserts a spatial relation between two named places** — position, direction, distance, adjacency, containment, or flow-to.

**Included**

| Example | Relation |
|---|---|
| `又東三百里，曰堂庭之山` | direction + distance |
| `南山經之首曰䧿山` | chain head |
| `臨於西海之上` | adjacency (no distance) |
| `麗𪊨之水出焉，而西流注於海` | flow-to |
| `凡䧿山之首，自招搖之山，以至箕尾之山，凡十山，二千九百五十里` | chain summary |

**Excluded**

| Example | Why |
|---|---|
| `多桂` · `多金玉` | flora / minerals |
| `有獸焉，其狀如馬而白首…` | fauna |
| `佩之無瘕疾` · `食之已疥` | medicine |
| `其神狀皆鳥身而龍首` · `其祠之禮…` | ritual |
| `見則其邑大水` | omen |

## 2. The bracket convention

The original text leaves many referents implicit. A bracket supplies the referent, so each record is self-contained.

| Original | With bracket |
|---|---|
| `又東三百里，曰堂庭之山` | `(招搖之山)又東三百里，曰堂庭之山` |
| `麗𪊨之水出焉` | `(招搖之山)麗𪊨之水出焉` |
| `其首曰招搖之山` | `(䧿山)其首曰招搖之山` |

The bracket is **added text, not source text** — it is always parenthesised so it can be stripped mechanically.

## 3. Clause-level, not entry-level

One entry can carry more than one locating clause:

> 又東三百里，曰X之山，**Y水出焉，而南流注於Z**。

→ two records, sharing an entry.

## 4. Source order is preserved

Records are never reordered. Reordering would itself be a structural claim.

## 5. No validation during extraction

Checksums, cross-source diffs and consistency checks belong to **stage 2**. During extraction a mismatch is recorded verbatim and flagged in `备注` — never corrected.

## 6. Boundary cases

- **望 statements** (`東望X`) — line-of-sight; arguably locating. *Not yet decided.*
- **郭璞注** — commentary, not the classic text. Kept out of the main database.
