# Record schema

One JSON object per line (JSONL), UTF-8, no trailing commas.

| field | type | description |
|---|---|---|
| `id` | string | `N1-05` = 卷-次經-序號 (ASCII, stable) |
| `卷` | string | 南山經 … 海內經 (18 卷) |
| `次经` | string | 南次一經 … 中次十二經 (山經 only) |
| `次序` | int | position in the source's own sequence |
| `原文` | string | **verbatim** locating clause, original characters, with bracket context |
| `类型` | string | see below |
| `mapping_worthy` | string | **reserved, empty** — filled in stage 3 |
| `备注` | string | optional notes (never corrections) |

## `类型` values

| value | meaning |
|---|---|
| `首山` | chain head / first mountain |
| `链式方位距离` | chained direction + distance |
| `水系` | water source + flow direction + destination |
| `水岸` | borders a sea / lake (usually no distance) |
| `小结` | chain summary (the text's own checksum) |
| `相对方位` | relative position (海經 layer) |
| `无距离方位` | direction without distance |
| `无方位距离` | distance without direction |
| `全局尺度` | global extent statements |

## `mapping_worthy` (reserved)

Filled in stage 3. Planned values: `vague` · `verified-with:<source>` · `non-accurate` · `ok`.
