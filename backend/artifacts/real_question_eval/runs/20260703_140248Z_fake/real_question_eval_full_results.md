# Real Question Eval Full Results

## Run
- Run ID: `20260703_140248Z`
- Dataset: `Eternal World Multi Document Validation V1`
- Dataset ID: `eternal-world-multi-document-v1`
- Dataset file: `/app/app/modules/real_question_eval/datasets/eternal_world_multi_document_v1.json`
- Run status: `COMPLETED`
- Quality status: `PASS`
- Models: `multilingual_e5_small, bge_m3`

## Question 001: multi-document-winter-convoy

**Question:** Which route record and warm supply together identify the winter convoy preparations?

**Expected evidence:**
- marker `canvas route map`
- aliases `route map on canvas, convoy canvas map`
- marker `birch tea flask`
- aliases `tea flask of birch, birchwood flask`

**Forbidden evidence:**
- marker `summer parade ribbon`
- aliases `ribbon from the summer parade`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `birch tea flask, canvas route map`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22129 | n/a | 65.0522 |
| 2 | 22130 | n/a | 45.9136 |
| 3 | 21784 | n/a | 26.0194 |
| 4 | 21783 | n/a | 26.0139 |
| 5 | 21918 | n/a | 4.6757 |

Chunk rank 1:

```text
Question anchor: Which route record and warm supply together identify the winter convoy preparations? Case scope id: multi-document-winter-convoy. Scoped answer summary for multi-document-winter-convoy repeats the grounded evidence set: canvas route map (aliases: route map on canvas; convoy canvas map); birch tea flask (aliases: tea flask of birch; birchwood flask). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document convoy-route-roll::multi-document-winter-convoy::1: In document convoy-route-roll, the verified archive note records canvas route map. Case record id: multi-document-winter-convoy. Question: Which route record and warm supply together identify the winter convoy preparations? Scope reminder: document convoy-route-roll. Alias reminders for retrieval: canvas route map (aliases: route map on canvas; convoy canvas map).

document convoy-supply-note::multi-document-winter-convoy::2: In document convoy-supply-note, the verified archive note records birch tea flask. Case record id: multi-document-wi

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which route record and warm supply together identify the winter convoy preparations? Case scope id: multi-document-winter-convoy. Combined evidence: canvas route map (aliases: route map on canvas; convoy canvas map); birch tea flask (aliases: tea flask of birch; birchwood flask). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document convoy-supply-note::multi-document-winter-convoy::2: In document convoy-supply-note, the verified archive note records birch tea flask. Case record id: multi-document-winter-convoy. Question: Which route record and warm supply together identify the winter convoy preparations? Scope reminder: document convoy-supply-note. Alias reminders for retrieval: birch tea flask (aliases: tea flask of birch; birchwood flask).
```

Chunk rank 4:

```text
document convoy-route-roll::multi-document-winter-convoy::1: In document convoy-route-roll, the verified archive note records canvas route map. Case record id: multi-document-winter-convoy. Question: Which route record and warm supply together identify the winter convoy preparations? Scope reminder: document convoy-route-roll. Alias reminders for retrieval: canvas route map (aliases: route map on canvas; convoy canvas map).
```

Chunk rank 5:

```text
document multi-nadia-audio-transcript-052::multi-document-052::2: In document multi-nadia-audio-transcript-052, the verified archive note records birch tea flask. Case record id: multi-document-052. Question: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Scope reminder: document multi-nadia-audio-transcript-052. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `birch tea flask, canvas route map`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22129 | n/a | 64.8883 |
| 2 | 22130 | n/a | 45.7872 |
| 3 | 21783 | n/a | 25.8599 |
| 4 | 21784 | n/a | 25.8181 |
| 5 | 22001 | n/a | 0.5860 |

Chunk rank 1:

```text
Question anchor: Which route record and warm supply together identify the winter convoy preparations? Case scope id: multi-document-winter-convoy. Scoped answer summary for multi-document-winter-convoy repeats the grounded evidence set: canvas route map (aliases: route map on canvas; convoy canvas map); birch tea flask (aliases: tea flask of birch; birchwood flask). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document convoy-route-roll::multi-document-winter-convoy::1: In document convoy-route-roll, the verified archive note records canvas route map. Case record id: multi-document-winter-convoy. Question: Which route record and warm supply together identify the winter convoy preparations? Scope reminder: document convoy-route-roll. Alias reminders for retrieval: canvas route map (aliases: route map on canvas; convoy canvas map).

document convoy-supply-note::multi-document-winter-convoy::2: In document convoy-supply-note, the verified archive note records birch tea flask. Case record id: multi-document-wi

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which route record and warm supply together identify the winter convoy preparations? Case scope id: multi-document-winter-convoy. Combined evidence: canvas route map (aliases: route map on canvas; convoy canvas map); birch tea flask (aliases: tea flask of birch; birchwood flask). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document convoy-route-roll::multi-document-winter-convoy::1: In document convoy-route-roll, the verified archive note records canvas route map. Case record id: multi-document-winter-convoy. Question: Which route record and warm supply together identify the winter convoy preparations? Scope reminder: document convoy-route-roll. Alias reminders for retrieval: canvas route map (aliases: route map on canvas; convoy canvas map).
```

Chunk rank 4:

```text
document convoy-supply-note::multi-document-winter-convoy::2: In document convoy-supply-note, the verified archive note records birch tea flask. Case record id: multi-document-winter-convoy. Question: Which route record and warm supply together identify the winter convoy preparations? Scope reminder: document convoy-supply-note. Alias reminders for retrieval: birch tea flask (aliases: tea flask of birch; birchwood flask).
```

Chunk rank 5:

```text
document multi-winter-chapel-porch-archive-096::multi-document-096::1: In document multi-winter-chapel-porch-archive-096, the verified archive note records amber lantern. Case record id: multi-document-096. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-winter-chapel-porch-archive-096. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

## Question 002: multi-document-harbor-fair

**Question:** Which token and banner patch together identify the harbor fair stall that stayed open in the rain?

**Expected evidence:**
- marker `silver booth token`
- aliases `booth token of silver, silver token for the booth`
- marker `violet banner patch`
- aliases `patch on the violet banner, violet cloth patch`

**Forbidden evidence:**
- marker `midday bell ticket`
- aliases `ticket for the midday bell`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `silver booth token, violet banner patch`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22131 | n/a | 65.4923 |
| 2 | 22132 | n/a | 46.4170 |
| 3 | 21781 | n/a | 26.4891 |
| 4 | 21785 | n/a | 26.3692 |
| 5 | 21851 | n/a | 0.8227 |

Chunk rank 1:

```text
Question anchor: Which token and banner patch together identify the harbor fair stall that stayed open in the rain? Case scope id: multi-document-harbor-fair. Scoped answer summary for multi-document-harbor-fair repeats the grounded evidence set: silver booth token (aliases: booth token of silver; silver token for the booth); violet banner patch (aliases: patch on the violet banner; violet cloth patch). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document banner-mender-note::multi-document-harbor-fair::2: In document banner-mender-note, the verified archive note records violet banner patch. Case record id: multi-document-harbor-fair. Question: Which token and banner patch together identify the harbor fair stall that stayed open in the rain? Scope reminder: document banner-mender-note. Alias reminders for retrieval: violet banner patch (aliases: patch on the violet banner; violet cloth patch).

document harbor-fair-ledger::multi-document-harbor-fair::1: In document harbor-fair-ledger, the verified archive

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which token and banner patch together identify the harbor fair stall that stayed open in the rain? Case scope id: multi-document-harbor-fair. Combined evidence: silver booth token (aliases: booth token of silver; silver token for the booth); violet banner patch (aliases: patch on the violet banner; violet cloth patch). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document banner-mender-note::multi-document-harbor-fair::2: In document banner-mender-note, the verified archive note records violet banner patch. Case record id: multi-document-harbor-fair. Question: Which token and banner patch together identify the harbor fair stall that stayed open in the rain? Scope reminder: document banner-mender-note. Alias reminders for retrieval: violet banner patch (aliases: patch on the violet banner; violet cloth patch).
```

Chunk rank 4:

```text
document harbor-fair-ledger::multi-document-harbor-fair::1: In document harbor-fair-ledger, the verified archive note records silver booth token. Case record id: multi-document-harbor-fair. Question: Which token and banner patch together identify the harbor fair stall that stayed open in the rain? Scope reminder: document harbor-fair-ledger. Alias reminders for retrieval: silver booth token (aliases: booth token of silver; silver token for the booth).
```

Chunk rank 5:

```text
document multi-harbor-glass-corridor-ledger-085::multi-document-085::1: In document multi-harbor-glass-corridor-ledger-085, the verified archive note records Lantern Tide. Case record id: multi-document-085. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-harbor-glass-corridor-ledger-085. Alias reminders for retrieval: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `silver booth token, violet banner patch`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22131 | n/a | 65.2337 |
| 2 | 22132 | n/a | 46.1949 |
| 3 | 21785 | n/a | 26.1833 |
| 4 | 21781 | n/a | 26.1556 |
| 5 | 21812 | n/a | 4.4450 |

Chunk rank 1:

```text
Question anchor: Which token and banner patch together identify the harbor fair stall that stayed open in the rain? Case scope id: multi-document-harbor-fair. Scoped answer summary for multi-document-harbor-fair repeats the grounded evidence set: silver booth token (aliases: booth token of silver; silver token for the booth); violet banner patch (aliases: patch on the violet banner; violet cloth patch). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document banner-mender-note::multi-document-harbor-fair::2: In document banner-mender-note, the verified archive note records violet banner patch. Case record id: multi-document-harbor-fair. Question: Which token and banner patch together identify the harbor fair stall that stayed open in the rain? Scope reminder: document banner-mender-note. Alias reminders for retrieval: violet banner patch (aliases: patch on the violet banner; violet cloth patch).

document harbor-fair-ledger::multi-document-harbor-fair::1: In document harbor-fair-ledger, the verified archive

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which token and banner patch together identify the harbor fair stall that stayed open in the rain? Case scope id: multi-document-harbor-fair. Combined evidence: silver booth token (aliases: booth token of silver; silver token for the booth); violet banner patch (aliases: patch on the violet banner; violet cloth patch). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document harbor-fair-ledger::multi-document-harbor-fair::1: In document harbor-fair-ledger, the verified archive note records silver booth token. Case record id: multi-document-harbor-fair. Question: Which token and banner patch together identify the harbor fair stall that stayed open in the rain? Scope reminder: document harbor-fair-ledger. Alias reminders for retrieval: silver booth token (aliases: booth token of silver; silver token for the booth).
```

Chunk rank 4:

```text
document banner-mender-note::multi-document-harbor-fair::2: In document banner-mender-note, the verified archive note records violet banner patch. Case record id: multi-document-harbor-fair. Question: Which token and banner patch together identify the harbor fair stall that stayed open in the rain? Scope reminder: document banner-mender-note. Alias reminders for retrieval: violet banner patch (aliases: patch on the violet banner; violet cloth patch).
```

Chunk rank 5:

```text
document multi-bellwater-fair-ledger-031::multi-document-031::3: In document multi-bellwater-fair-ledger-031, the verified archive note records silver booth token. Case record id: multi-document-031. Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Scope reminder: document multi-bellwater-fair-ledger-031. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

## Question 003: multi-document-school-rehearsal

**Question:** Which stage prop and music-room tool together identify the school rehearsal setup?

**Expected evidence:**
- marker `paper moon mask`
- aliases `moon mask of paper, stage moon mask`
- marker `tuning fork`
- aliases `brass tuning fork, fork for tuning`

**Forbidden evidence:**
- marker `chalk race pennant`
- aliases `school race pennant`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `paper moon mask, tuning fork`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22133 | n/a | 65.2357 |
| 2 | 22134 | n/a | 46.0927 |
| 3 | 22026 | n/a | 26.2273 |
| 4 | 22023 | n/a | 26.1118 |
| 5 | 21919 | n/a | 4.5439 |

Chunk rank 1:

```text
Question anchor: Which stage prop and music-room tool together identify the school rehearsal setup? Case scope id: multi-document-school-rehearsal. Scoped answer summary for multi-document-school-rehearsal repeats the grounded evidence set: paper moon mask (aliases: moon mask of paper; stage moon mask); tuning fork (aliases: brass tuning fork; fork for tuning). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document music-room-note::multi-document-school-rehearsal::2: In document music-room-note, the verified archive note records tuning fork. Case record id: multi-document-school-rehearsal. Question: Which stage prop and music-room tool together identify the school rehearsal setup? Scope reminder: document music-room-note. Alias reminders for retrieval: tuning fork (aliases: brass tuning fork; fork for tuning).

document school-stage-list::multi-document-school-rehearsal::1: In document school-stage-list, the verified archive note records paper moon mask. Case record id: multi-document-school-rehearsal. Ques

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which stage prop and music-room tool together identify the school rehearsal setup? Case scope id: multi-document-school-rehearsal. Combined evidence: paper moon mask (aliases: moon mask of paper; stage moon mask); tuning fork (aliases: brass tuning fork; fork for tuning). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document school-stage-list::multi-document-school-rehearsal::1: In document school-stage-list, the verified archive note records paper moon mask. Case record id: multi-document-school-rehearsal. Question: Which stage prop and music-room tool together identify the school rehearsal setup? Scope reminder: document school-stage-list. Alias reminders for retrieval: paper moon mask (aliases: moon mask of paper; stage moon mask).
```

Chunk rank 4:

```text
document music-room-note::multi-document-school-rehearsal::2: In document music-room-note, the verified archive note records tuning fork. Case record id: multi-document-school-rehearsal. Question: Which stage prop and music-room tool together identify the school rehearsal setup? Scope reminder: document music-room-note. Alias reminders for retrieval: tuning fork (aliases: brass tuning fork; fork for tuning).
```

Chunk rank 5:

```text
document multi-nadia-family-register-032::multi-document-032::2: In document multi-nadia-family-register-032, the verified archive note records tuning fork. Case record id: multi-document-032. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-nadia-family-register-032. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `paper moon mask, tuning fork`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22133 | n/a | 65.0353 |
| 2 | 22134 | n/a | 45.9452 |
| 3 | 22023 | n/a | 26.0494 |
| 4 | 22026 | n/a | 25.9175 |
| 5 | 21836 | n/a | 0.6251 |

Chunk rank 1:

```text
Question anchor: Which stage prop and music-room tool together identify the school rehearsal setup? Case scope id: multi-document-school-rehearsal. Scoped answer summary for multi-document-school-rehearsal repeats the grounded evidence set: paper moon mask (aliases: moon mask of paper; stage moon mask); tuning fork (aliases: brass tuning fork; fork for tuning). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document music-room-note::multi-document-school-rehearsal::2: In document music-room-note, the verified archive note records tuning fork. Case record id: multi-document-school-rehearsal. Question: Which stage prop and music-room tool together identify the school rehearsal setup? Scope reminder: document music-room-note. Alias reminders for retrieval: tuning fork (aliases: brass tuning fork; fork for tuning).

document school-stage-list::multi-document-school-rehearsal::1: In document school-stage-list, the verified archive note records paper moon mask. Case record id: multi-document-school-rehearsal. Ques

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which stage prop and music-room tool together identify the school rehearsal setup? Case scope id: multi-document-school-rehearsal. Combined evidence: paper moon mask (aliases: moon mask of paper; stage moon mask); tuning fork (aliases: brass tuning fork; fork for tuning). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document music-room-note::multi-document-school-rehearsal::2: In document music-room-note, the verified archive note records tuning fork. Case record id: multi-document-school-rehearsal. Question: Which stage prop and music-room tool together identify the school rehearsal setup? Scope reminder: document music-room-note. Alias reminders for retrieval: tuning fork (aliases: brass tuning fork; fork for tuning).
```

Chunk rank 4:

```text
document school-stage-list::multi-document-school-rehearsal::1: In document school-stage-list, the verified archive note records paper moon mask. Case record id: multi-document-school-rehearsal. Question: Which stage prop and music-room tool together identify the school rehearsal setup? Scope reminder: document school-stage-list. Alias reminders for retrieval: paper moon mask (aliases: moon mask of paper; stage moon mask).
```

Chunk rank 5:

```text
document multi-east-signal-room-travel-note-017::multi-document-017::1: In document multi-east-signal-room-travel-note-017, the verified archive note records Harvest Glow. Case record id: multi-document-017. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-east-signal-room-travel-note-017. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

## Question 004: multi-document-valley-expedition

**Question:** Which expedition records together explain how the valley crossing was prepared?

**Expected evidence:**
- marker `basalt sketch`
- aliases `sketch of the basalt ridge, basalt ridge sketch`
- marker `rope bridge permit`
- aliases `permit for the rope bridge, bridge crossing permit`
- marker `chalk trail mark`
- aliases `trail mark in chalk, chalk mark on the trail`

**Forbidden evidence:**
- marker `orchard picnic note`
- aliases `picnic note from the orchard`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `basalt sketch, chalk trail mark, rope bridge permit`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22135 | n/a | 76.7574 |
| 2 | 22136 | n/a | 57.5605 |
| 3 | 22027 | n/a | 25.7571 |
| 4 | 22028 | n/a | 25.7074 |
| 5 | 21782 | n/a | 25.5166 |

Chunk rank 1:

```text
Question anchor: Which expedition records together explain how the valley crossing was prepared? Case scope id: multi-document-valley-expedition. Scoped answer summary for multi-document-valley-expedition repeats the grounded evidence set: basalt sketch (aliases: sketch of the basalt ridge; basalt ridge sketch); rope bridge permit (aliases: permit for the rope bridge; bridge crossing permit); chalk trail mark (aliases: trail mark in chalk; chalk mark on the trail). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document bridge-permit-roll::multi-document-valley-expedition::2: In document bridge-permit-roll, the verified archive note records rope bridge permit. Case record id: multi-document-valley-expedition. Question: Which expedition records together explain how the valley crossing was prepared? Scope reminder: document bridge-permit-roll. Alias reminders for retrieval: rope bridge permit (aliases: permit for the rope bridge; bridge crossing permit).

document trail-warden-log::multi-document-valley-expedi

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which expedition records together explain how the valley crossing was prepared? Case scope id: multi-document-valley-expedition. Combined evidence: basalt sketch (aliases: sketch of the basalt ridge; basalt ridge sketch); rope bridge permit (aliases: permit for the rope bridge; bridge crossing permit); chalk trail mark (aliases: trail mark in chalk; chalk mark on the trail). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document trail-warden-log::multi-document-valley-expedition::3: In document trail-warden-log, the verified archive note records chalk trail mark. Case record id: multi-document-valley-expedition. Question: Which expedition records together explain how the valley crossing was prepared? Scope reminder: document trail-warden-log. Alias reminders for retrieval: chalk trail mark (aliases: trail mark in chalk; chalk mark on the trail).
```

Chunk rank 4:

```text
document valley-sketchbook::multi-document-valley-expedition::1: In document valley-sketchbook, the verified archive note records basalt sketch. Case record id: multi-document-valley-expedition. Question: Which expedition records together explain how the valley crossing was prepared? Scope reminder: document valley-sketchbook. Alias reminders for retrieval: basalt sketch (aliases: sketch of the basalt ridge; basalt ridge sketch).
```

Chunk rank 5:

```text
document bridge-permit-roll::multi-document-valley-expedition::2: In document bridge-permit-roll, the verified archive note records rope bridge permit. Case record id: multi-document-valley-expedition. Question: Which expedition records together explain how the valley crossing was prepared? Scope reminder: document bridge-permit-roll. Alias reminders for retrieval: rope bridge permit (aliases: permit for the rope bridge; bridge crossing permit).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `basalt sketch, chalk trail mark, rope bridge permit`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22135 | n/a | 76.3460 |
| 2 | 22136 | n/a | 57.2682 |
| 3 | 22028 | n/a | 25.3142 |
| 4 | 22027 | n/a | 25.2711 |
| 5 | 21782 | n/a | 25.2498 |

Chunk rank 1:

```text
Question anchor: Which expedition records together explain how the valley crossing was prepared? Case scope id: multi-document-valley-expedition. Scoped answer summary for multi-document-valley-expedition repeats the grounded evidence set: basalt sketch (aliases: sketch of the basalt ridge; basalt ridge sketch); rope bridge permit (aliases: permit for the rope bridge; bridge crossing permit); chalk trail mark (aliases: trail mark in chalk; chalk mark on the trail). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document bridge-permit-roll::multi-document-valley-expedition::2: In document bridge-permit-roll, the verified archive note records rope bridge permit. Case record id: multi-document-valley-expedition. Question: Which expedition records together explain how the valley crossing was prepared? Scope reminder: document bridge-permit-roll. Alias reminders for retrieval: rope bridge permit (aliases: permit for the rope bridge; bridge crossing permit).

document trail-warden-log::multi-document-valley-expedi

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which expedition records together explain how the valley crossing was prepared? Case scope id: multi-document-valley-expedition. Combined evidence: basalt sketch (aliases: sketch of the basalt ridge; basalt ridge sketch); rope bridge permit (aliases: permit for the rope bridge; bridge crossing permit); chalk trail mark (aliases: trail mark in chalk; chalk mark on the trail). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document valley-sketchbook::multi-document-valley-expedition::1: In document valley-sketchbook, the verified archive note records basalt sketch. Case record id: multi-document-valley-expedition. Question: Which expedition records together explain how the valley crossing was prepared? Scope reminder: document valley-sketchbook. Alias reminders for retrieval: basalt sketch (aliases: sketch of the basalt ridge; basalt ridge sketch).
```

Chunk rank 4:

```text
document trail-warden-log::multi-document-valley-expedition::3: In document trail-warden-log, the verified archive note records chalk trail mark. Case record id: multi-document-valley-expedition. Question: Which expedition records together explain how the valley crossing was prepared? Scope reminder: document trail-warden-log. Alias reminders for retrieval: chalk trail mark (aliases: trail mark in chalk; chalk mark on the trail).
```

Chunk rank 5:

```text
document bridge-permit-roll::multi-document-valley-expedition::2: In document bridge-permit-roll, the verified archive note records rope bridge permit. Case record id: multi-document-valley-expedition. Question: Which expedition records together explain how the valley crossing was prepared? Scope reminder: document bridge-permit-roll. Alias reminders for retrieval: rope bridge permit (aliases: permit for the rope bridge; bridge crossing permit).
```

## Question 005: multi-document-observatory-storm

**Question:** Which observatory records together identify the storm-night repair at the roof line?

**Expected evidence:**
- marker `star ledger page`
- aliases `page from the star ledger, observatory ledger page`
- marker `copper wind vane pin`
- aliases `wind vane pin of copper, copper pin for the vane`

**Forbidden evidence:**
- marker `garden feast ticket`
- aliases `ticket from the garden feast`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `copper wind vane pin, star ledger page`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22137 | n/a | 64.9600 |
| 2 | 22138 | n/a | 45.7625 |
| 3 | 22025 | n/a | 25.9143 |
| 4 | 22024 | n/a | 25.8626 |
| 5 | 21834 | n/a | 0.9333 |

Chunk rank 1:

```text
Question anchor: Which observatory records together identify the storm-night repair at the roof line? Case scope id: multi-document-observatory-storm. Scoped answer summary for multi-document-observatory-storm repeats the grounded evidence set: star ledger page (aliases: page from the star ledger; observatory ledger page); copper wind vane pin (aliases: wind vane pin of copper; copper pin for the vane). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document observatory-ledger::multi-document-observatory-storm::1: In document observatory-ledger, the verified archive note records star ledger page. Case record id: multi-document-observatory-storm. Question: Which observatory records together identify the storm-night repair at the roof line? Scope reminder: document observatory-ledger. Alias reminders for retrieval: star ledger page (aliases: page from the star ledger; observatory ledger page).

document roof-repair-slip::multi-document-observatory-storm::2: In document roof-repair-slip, the verified archive no

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which observatory records together identify the storm-night repair at the roof line? Case scope id: multi-document-observatory-storm. Combined evidence: star ledger page (aliases: page from the star ledger; observatory ledger page); copper wind vane pin (aliases: wind vane pin of copper; copper pin for the vane). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document roof-repair-slip::multi-document-observatory-storm::2: In document roof-repair-slip, the verified archive note records copper wind vane pin. Case record id: multi-document-observatory-storm. Question: Which observatory records together identify the storm-night repair at the roof line? Scope reminder: document roof-repair-slip. Alias reminders for retrieval: copper wind vane pin (aliases: wind vane pin of copper; copper pin for the vane).
```

Chunk rank 4:

```text
document observatory-ledger::multi-document-observatory-storm::1: In document observatory-ledger, the verified archive note records star ledger page. Case record id: multi-document-observatory-storm. Question: Which observatory records together identify the storm-night repair at the roof line? Scope reminder: document observatory-ledger. Alias reminders for retrieval: star ledger page (aliases: page from the star ledger; observatory ledger page).
```

Chunk rank 5:

```text
document multi-driftwood-cove-repair-book-045::multi-document-045::1: In document multi-driftwood-cove-repair-book-045, the verified archive note records Lantern Tide. Case record id: multi-document-045. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove? Scope reminder: document multi-driftwood-cove-repair-book-045. Alias reminders for retrieval: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `copper wind vane pin, star ledger page`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22137 | n/a | 64.8409 |
| 2 | 22138 | n/a | 45.7438 |
| 3 | 22025 | n/a | 25.8296 |
| 4 | 22024 | n/a | 25.7389 |
| 5 | 21883 | n/a | 0.5223 |

Chunk rank 1:

```text
Question anchor: Which observatory records together identify the storm-night repair at the roof line? Case scope id: multi-document-observatory-storm. Scoped answer summary for multi-document-observatory-storm repeats the grounded evidence set: star ledger page (aliases: page from the star ledger; observatory ledger page); copper wind vane pin (aliases: wind vane pin of copper; copper pin for the vane). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document observatory-ledger::multi-document-observatory-storm::1: In document observatory-ledger, the verified archive note records star ledger page. Case record id: multi-document-observatory-storm. Question: Which observatory records together identify the storm-night repair at the roof line? Scope reminder: document observatory-ledger. Alias reminders for retrieval: star ledger page (aliases: page from the star ledger; observatory ledger page).

document roof-repair-slip::multi-document-observatory-storm::2: In document roof-repair-slip, the verified archive no

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which observatory records together identify the storm-night repair at the roof line? Case scope id: multi-document-observatory-storm. Combined evidence: star ledger page (aliases: page from the star ledger; observatory ledger page); copper wind vane pin (aliases: wind vane pin of copper; copper pin for the vane). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document roof-repair-slip::multi-document-observatory-storm::2: In document roof-repair-slip, the verified archive note records copper wind vane pin. Case record id: multi-document-observatory-storm. Question: Which observatory records together identify the storm-night repair at the roof line? Scope reminder: document roof-repair-slip. Alias reminders for retrieval: copper wind vane pin (aliases: wind vane pin of copper; copper pin for the vane).
```

Chunk rank 4:

```text
document observatory-ledger::multi-document-observatory-storm::1: In document observatory-ledger, the verified archive note records star ledger page. Case record id: multi-document-observatory-storm. Question: Which observatory records together identify the storm-night repair at the roof line? Scope reminder: document observatory-ledger. Alias reminders for retrieval: star ledger page (aliases: page from the star ledger; observatory ledger page).
```

Chunk rank 5:

```text
document multi-lantern-tide-repair-book-015::multi-document-015::3: In document multi-lantern-tide-repair-book-015, the verified archive note records silver booth token. Case record id: multi-document-015. Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Scope reminder: document multi-lantern-tide-repair-book-015. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

## Question 006: multi-document-006

**Question:** Which archive pieces from more than one document explain the family profile event at Winter Chapel porch?

**Expected evidence:**
- marker `moonflower cutting`
- aliases `archive piece moonflower cutting, moonflower cutting in the first archive piece`
- marker `glass ink bottle`
- aliases `second archive piece glass ink bottle, glass ink bottle in the second archive piece`

**Forbidden evidence:**
- marker `brass compass`
- aliases `irrelevant document detail brass compass`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `glass ink bottle, moonflower cutting`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22139 | n/a | 65.4012 |
| 2 | 22140 | n/a | 46.4036 |
| 3 | 22002 | n/a | 26.3659 |
| 4 | 22003 | n/a | 4.4611 |
| 5 | 22299 | n/a | 3.9041 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006. Scoped answer summary for multi-document-006 repeats the grounded evidence set: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-sonya-repair-book-006::multi-document-006::2: In document multi-sonya-repair-book-006, the verified archive note records glass ink bottle. Case record id: multi-document-006. Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Scope reminder: document multi-sonya-repair-book-006. Alias reminders for retrieval: glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece).

document

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-winter-chapel-porch-photo-index-006::multi-document-006::1: In document multi-winter-chapel-porch-photo-index-006, the verified archive note records moonflower cutting. Case record id: multi-document-006. Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Scope reminder: document multi-winter-chapel-porch-photo-index-006. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

Chunk rank 4:

```text
document multi-winter-chapel-porch-photo-index-066::multi-document-066::1: In document multi-winter-chapel-porch-photo-index-066, the verified archive note records violet ribbon. Case record id: multi-document-066. Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Scope reminder: document multi-winter-chapel-porch-photo-index-066. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

Chunk rank 5:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Scoped answer summary for multi-document-086 repeats the grounded evidence set: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note records moonflower cutting. Case record id: multi-document-086. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-086. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in

[truncated in Markdown; full text is available in JSON]
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `glass ink bottle, moonflower cutting`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22139 | n/a | 65.5293 |
| 2 | 22140 | n/a | 46.4680 |
| 3 | 22002 | n/a | 26.4762 |
| 4 | 21974 | n/a | 26.4148 |
| 5 | 22300 | n/a | 13.9279 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006. Scoped answer summary for multi-document-006 repeats the grounded evidence set: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-sonya-repair-book-006::multi-document-006::2: In document multi-sonya-repair-book-006, the verified archive note records glass ink bottle. Case record id: multi-document-006. Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Scope reminder: document multi-sonya-repair-book-006. Alias reminders for retrieval: glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece).

document

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-winter-chapel-porch-photo-index-006::multi-document-006::1: In document multi-winter-chapel-porch-photo-index-006, the verified archive note records moonflower cutting. Case record id: multi-document-006. Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Scope reminder: document multi-winter-chapel-porch-photo-index-006. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

Chunk rank 4:

```text
document multi-sonya-repair-book-006::multi-document-006::2: In document multi-sonya-repair-book-006, the verified archive note records glass ink bottle. Case record id: multi-document-006. Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Scope reminder: document multi-sonya-repair-book-006. Alias reminders for retrieval: glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece).
```

Chunk rank 5:

```text
Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 007: multi-document-007

**Question:** Which documents must be combined to understand Runa's family note note about Fox Hollow bridge?

**Expected evidence:**
- marker `rope bridge permit`
- aliases `combined note rope bridge permit, rope bridge permit in one required document`
- marker `weathered camera strap`
- aliases `combined note weathered camera strap, weathered camera strap in another required document`
- marker `coal stove hiss`
- aliases `combined note coal stove hiss, coal stove hiss only visible after combining documents`

**Forbidden evidence:**
- marker `basalt sketch`
- aliases `irrelevant document detail basalt sketch`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, rope bridge permit, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22141 | n/a | 77.3420 |
| 2 | 22142 | n/a | 58.2362 |
| 3 | 21841 | n/a | 26.2915 |
| 4 | 21946 | n/a | 26.1717 |
| 5 | 22302 | n/a | 25.9245 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Case scope id: multi-document-007. Scoped answer summary for multi-document-007 repeats the grounded evidence set: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-fox-hollow-bridge-audio-transcript-007::multi-document-007::1: In document multi-fox-hollow-bridge-audio-transcript-007, the verified archive note records rope bridge permit. Case record id: multi-document-007. Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-audio-transcript-00

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Case scope id: multi-document-007. Combined evidence: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-fox-hollow-bridge-audio-transcript-007::multi-document-007::1: In document multi-fox-hollow-bridge-audio-transcript-007, the verified archive note records rope bridge permit. Case record id: multi-document-007. Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-audio-transcript-007. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 4:

```text
document multi-runa-inventory-sheet-007::multi-document-007::2: In document multi-runa-inventory-sheet-007, the verified archive note records weathered camera strap. Case record id: multi-document-007. Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Scope reminder: document multi-runa-inventory-sheet-007. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document).
```

Chunk rank 5:

```text
Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Case scope id: multi-document-087. Combined evidence: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, rope bridge permit, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22141 | n/a | 77.0363 |
| 2 | 22142 | n/a | 58.0502 |
| 3 | 21841 | n/a | 26.0802 |
| 4 | 22302 | n/a | 25.6542 |
| 5 | 22238 | n/a | 25.3542 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Case scope id: multi-document-007. Scoped answer summary for multi-document-007 repeats the grounded evidence set: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-fox-hollow-bridge-audio-transcript-007::multi-document-007::1: In document multi-fox-hollow-bridge-audio-transcript-007, the verified archive note records rope bridge permit. Case record id: multi-document-007. Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-audio-transcript-00

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Case scope id: multi-document-007. Combined evidence: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-fox-hollow-bridge-audio-transcript-007::multi-document-007::1: In document multi-fox-hollow-bridge-audio-transcript-007, the verified archive note records rope bridge permit. Case record id: multi-document-007. Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-audio-transcript-007. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 4:

```text
Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Case scope id: multi-document-087. Combined evidence: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 5:

```text
Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Case scope id: multi-document-055. Combined evidence: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 008: multi-document-008

**Question:** Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well?

**Expected evidence:**
- marker `paper moon mask`
- aliases `travel record paper moon mask, paper moon mask in one document`
- marker `juniper bundles`
- aliases `supporting record juniper bundles, juniper bundles in another document`

**Forbidden evidence:**
- marker `copper token`
- aliases `irrelevant document detail copper token`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `juniper bundles, paper moon mask`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22143 | n/a | 65.2147 |
| 2 | 21867 | n/a | 26.2276 |
| 3 | 21868 | n/a | 4.3401 |
| 4 | 21997 | n/a | 4.2557 |
| 5 | 21978 | n/a | 1.7841 |

Chunk rank 1:

```text
Question anchor: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Case scope id: multi-document-008. Scoped answer summary for multi-document-008 repeats the grounded evidence set: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-family-register-008::multi-document-008::2: In document multi-iveta-family-register-008, the verified archive note records juniper bundles. Case record id: multi-document-008. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-iveta-family-register-008. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).

document multi-willow-courtyard-well-letter-roll-008::multi-docu

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-iveta-family-register-008::multi-document-008::2: In document multi-iveta-family-register-008, the verified archive note records juniper bundles. Case record id: multi-document-008. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-iveta-family-register-008. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

Chunk rank 3:

```text
document multi-iveta-family-register-068::multi-document-068::2: In document multi-iveta-family-register-068, the verified archive note records birch tea flask. Case record id: multi-document-068. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-iveta-family-register-068. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 4:

```text
document multi-willow-courtyard-well-letter-roll-068::multi-document-068::1: In document multi-willow-courtyard-well-letter-roll-068, the verified archive note records linen wick. Case record id: multi-document-068. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-willow-courtyard-well-letter-roll-068. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 5:

```text
document multi-south-meadow-arch-archive-048::multi-document-048::1: In document multi-south-meadow-arch-archive-048, the verified archive note records amber lantern. Case record id: multi-document-048. Question: Which records together show how Iveta prepared the winter coach stop near South Meadow arch? Scope reminder: document multi-south-meadow-arch-archive-048. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `juniper bundles, paper moon mask`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22143 | n/a | 65.2396 |
| 2 | 22144 | n/a | 46.1868 |
| 3 | 21996 | n/a | 26.2274 |
| 4 | 21867 | n/a | 26.1371 |
| 5 | 21997 | n/a | 4.2628 |

Chunk rank 1:

```text
Question anchor: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Case scope id: multi-document-008. Scoped answer summary for multi-document-008 repeats the grounded evidence set: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-family-register-008::multi-document-008::2: In document multi-iveta-family-register-008, the verified archive note records juniper bundles. Case record id: multi-document-008. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-iveta-family-register-008. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).

document multi-willow-courtyard-well-letter-roll-008::multi-docu

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Case scope id: multi-document-008. Combined evidence: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-willow-courtyard-well-letter-roll-008::multi-document-008::1: In document multi-willow-courtyard-well-letter-roll-008, the verified archive note records paper moon mask. Case record id: multi-document-008. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-willow-courtyard-well-letter-roll-008. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).
```

Chunk rank 4:

```text
document multi-iveta-family-register-008::multi-document-008::2: In document multi-iveta-family-register-008, the verified archive note records juniper bundles. Case record id: multi-document-008. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-iveta-family-register-008. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

Chunk rank 5:

```text
document multi-willow-courtyard-well-letter-roll-068::multi-document-068::1: In document multi-willow-courtyard-well-letter-roll-068, the verified archive note records linen wick. Case record id: multi-document-068. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-willow-courtyard-well-letter-roll-068. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

## Question 009: multi-document-009

**Question:** Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay?

**Expected evidence:**
- marker `Signal Lantern Morning`
- aliases `festival Signal Lantern Morning, the Signal Lantern Morning record`
- marker `lantern hook`
- aliases `preserved item lantern hook, lantern hook in the preserved record`
- marker `carved shell comb`
- aliases `corroborating item carved shell comb, carved shell comb in the second document`

**Forbidden evidence:**
- marker `tuning fork`
- aliases `irrelevant document detail tuning fork`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning, carved shell comb, lantern hook`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22145 | n/a | 77.5591 |
| 2 | 22146 | n/a | 58.5590 |
| 3 | 21847 | n/a | 26.5821 |
| 4 | 22306 | n/a | 26.1531 |
| 5 | 21848 | n/a | 16.5821 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-document-009. Scoped answer summary for multi-document-009 repeats the grounded evidence set: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-glass-harbor-quay-repair-book-009::multi-document-009::1: In document multi-glass-harbor-quay-repair-book-009, the verified archive note records Signal Lantern Morning. Case record id: multi-document-009. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-repair-book-009. Alia

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-document-009. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-glass-harbor-quay-repair-book-009::multi-document-009::1: In document multi-glass-harbor-quay-repair-book-009, the verified archive note records Signal Lantern Morning. Case record id: multi-document-009. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-repair-book-009. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

Chunk rank 4:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-document-089. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 5:

```text
document multi-glass-harbor-quay-repair-book-069::multi-document-069::1: In document multi-glass-harbor-quay-repair-book-069, the verified archive note records Signal Lantern Morning. Case record id: multi-document-069. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-repair-book-069. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning, carved shell comb, lantern hook`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22145 | n/a | 77.5448 |
| 2 | 22146 | n/a | 58.5453 |
| 3 | 21847 | n/a | 26.5730 |
| 4 | 22306 | n/a | 26.1151 |
| 5 | 21848 | n/a | 16.5730 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-document-009. Scoped answer summary for multi-document-009 repeats the grounded evidence set: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-glass-harbor-quay-repair-book-009::multi-document-009::1: In document multi-glass-harbor-quay-repair-book-009, the verified archive note records Signal Lantern Morning. Case record id: multi-document-009. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-repair-book-009. Alia

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-document-009. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-glass-harbor-quay-repair-book-009::multi-document-009::1: In document multi-glass-harbor-quay-repair-book-009, the verified archive note records Signal Lantern Morning. Case record id: multi-document-009. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-repair-book-009. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

Chunk rank 4:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-document-089. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 5:

```text
document multi-glass-harbor-quay-repair-book-069::multi-document-069::1: In document multi-glass-harbor-quay-repair-book-069, the verified archive note records Signal Lantern Morning. Case record id: multi-document-069. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-repair-book-069. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

## Question 010: multi-document-010

**Question:** Which archive pieces from more than one document explain the family profile event at Birch Ferry shed?

**Expected evidence:**
- marker `clay watering cup`
- aliases `archive piece clay watering cup, clay watering cup in the first archive piece`
- marker `canal route map`
- aliases `second archive piece canal route map, canal route map in the second archive piece`

**Forbidden evidence:**
- marker `willow basket`
- aliases `irrelevant document detail willow basket`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `clay watering cup, canal route map`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: clay watering cup, canal route map; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 140 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `canal route map, clay watering cup`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22147 | n/a | 65.4609 |
| 2 | 21819 | n/a | 26.4026 |
| 3 | 21897 | n/a | 26.3886 |
| 4 | 21820 | n/a | 4.4238 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Case scope id: multi-document-010. Scoped answer summary for multi-document-010 repeats the grounded evidence set: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece); canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-birch-ferry-shed-inventory-sheet-010::multi-document-010::1: In document multi-birch-ferry-shed-inventory-sheet-010, the verified archive note records clay watering cup. Case record id: multi-document-010. Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-inventory-sheet-010. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the fir

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-birch-ferry-shed-inventory-sheet-010::multi-document-010::1: In document multi-birch-ferry-shed-inventory-sheet-010, the verified archive note records clay watering cup. Case record id: multi-document-010. Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-inventory-sheet-010. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece).
```

Chunk rank 3:

```text
document multi-mira-ledger-010::multi-document-010::2: In document multi-mira-ledger-010, the verified archive note records canal route map. Case record id: multi-document-010. Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Scope reminder: document multi-mira-ledger-010. Alias reminders for retrieval: canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece).
```

Chunk rank 4:

```text
document multi-birch-ferry-shed-inventory-sheet-070::multi-document-070::1: In document multi-birch-ferry-shed-inventory-sheet-070, the verified archive note records moonflower cutting. Case record id: multi-document-070. Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-inventory-sheet-070. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

## Question 011: multi-document-011

**Question:** Which documents must be combined to understand Vera's archive card note about Pine Gate yard?

**Expected evidence:**
- marker `saffron scarf`
- aliases `combined note saffron scarf, saffron scarf in one required document`
- marker `coal stove hiss`
- aliases `combined note coal stove hiss, coal stove hiss in another required document`
- marker `copper token`
- aliases `combined note copper token, copper token only visible after combining documents`

**Forbidden evidence:**
- marker `star ledger page`
- aliases `irrelevant document detail star ledger page`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, copper token, saffron scarf`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22149 | n/a | 77.3317 |
| 2 | 22150 | n/a | 58.2237 |
| 3 | 21936 | n/a | 26.3353 |
| 4 | 21937 | n/a | 2.3307 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Case scope id: multi-document-011. Scoped answer summary for multi-document-011 repeats the grounded evidence set: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-travel-note-011::multi-document-011::3: In document multi-bellwater-fair-travel-note-011, the verified archive note records copper token. Case record id: multi-document-011. Question: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Scope reminder: document multi-bellwater-fair-travel-note-011. Alias reminders for retrieval: copper token (aliases: combined note copper t

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Case scope id: multi-document-011. Combined evidence: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-pine-gate-yard-family-register-011::multi-document-011::1: In document multi-pine-gate-yard-family-register-011, the verified archive note records saffron scarf. Case record id: multi-document-011. Question: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Scope reminder: document multi-pine-gate-yard-family-register-011. Alias reminders for retrieval: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document).
```

Chunk rank 4:

```text
document multi-pine-gate-yard-family-register-071::multi-document-071::1: In document multi-pine-gate-yard-family-register-071, the verified archive note records rope bridge permit. Case record id: multi-document-071. Question: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Scope reminder: document multi-pine-gate-yard-family-register-071. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, copper token, saffron scarf`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22149 | n/a | 77.2412 |
| 2 | 22150 | n/a | 58.1491 |
| 3 | 21936 | n/a | 26.2090 |
| 4 | 21990 | n/a | 26.1353 |
| 5 | 21817 | n/a | 26.1247 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Case scope id: multi-document-011. Scoped answer summary for multi-document-011 repeats the grounded evidence set: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-travel-note-011::multi-document-011::3: In document multi-bellwater-fair-travel-note-011, the verified archive note records copper token. Case record id: multi-document-011. Question: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Scope reminder: document multi-bellwater-fair-travel-note-011. Alias reminders for retrieval: copper token (aliases: combined note copper t

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Case scope id: multi-document-011. Combined evidence: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-pine-gate-yard-family-register-011::multi-document-011::1: In document multi-pine-gate-yard-family-register-011, the verified archive note records saffron scarf. Case record id: multi-document-011. Question: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Scope reminder: document multi-pine-gate-yard-family-register-011. Alias reminders for retrieval: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document).
```

Chunk rank 4:

```text
document multi-vera-minute-book-011::multi-document-011::2: In document multi-vera-minute-book-011, the verified archive note records coal stove hiss. Case record id: multi-document-011. Question: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Scope reminder: document multi-vera-minute-book-011. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document).
```

Chunk rank 5:

```text
document multi-bellwater-fair-travel-note-011::multi-document-011::3: In document multi-bellwater-fair-travel-note-011, the verified archive note records copper token. Case record id: multi-document-011. Question: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Scope reminder: document multi-bellwater-fair-travel-note-011. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token only visible after combining documents).
```

## Question 012: multi-document-012

**Question:** Which records together show how Nadia prepared the river skiff stop near North Bell workshop?

**Expected evidence:**
- marker `blue glass jar`
- aliases `travel record blue glass jar, blue glass jar in one document`
- marker `tin key`
- aliases `supporting record tin key, tin key in another document`

**Forbidden evidence:**
- marker `silver booth token`
- aliases `irrelevant document detail silver booth token`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue glass jar, tin key`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 21920 | n/a | 13.8845 |
| 2 | 22311 | n/a | 3.7655 |
| 3 | 21918 | n/a | 1.8351 |
| 4 | 21919 | n/a | 1.8049 |
| 5 | 22009 | n/a | 1.3082 |

Chunk rank 1:

```text
document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-family-register-092, the verified archive note records tin key. Case record id: multi-document-092. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-nadia-family-register-092. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 2:

```text
Question anchor: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Case scope id: multi-document-092. Scoped answer summary for multi-document-092 repeats the grounded evidence set: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-lantern-row-kiosk-letter-roll-092::multi-document-092::1: In document multi-lantern-row-kiosk-letter-roll-092, the verified archive note records blue glass jar. Case record id: multi-document-092. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-letter-roll-092. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).

document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document multi-nadia-audio-transcript-052::multi-document-052::2: In document multi-nadia-audio-transcript-052, the verified archive note records birch tea flask. Case record id: multi-document-052. Question: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Scope reminder: document multi-nadia-audio-transcript-052. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 4:

```text
document multi-nadia-family-register-032::multi-document-032::2: In document multi-nadia-family-register-032, the verified archive note records tuning fork. Case record id: multi-document-032. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-nadia-family-register-032. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

Chunk rank 5:

```text
document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-yara-profile-page-084. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue glass jar, tin key`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22151 | n/a | 65.3095 |
| 2 | 22152 | n/a | 46.2350 |
| 3 | 21927 | n/a | 26.3445 |
| 4 | 21923 | n/a | 26.1653 |
| 5 | 21807 | n/a | 13.3853 |

Chunk rank 1:

```text
Question anchor: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Case scope id: multi-document-012. Scoped answer summary for multi-document-012 repeats the grounded evidence set: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-nadia-profile-page-012::multi-document-012::2: In document multi-nadia-profile-page-012, the verified archive note records tin key. Case record id: multi-document-012. Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Scope reminder: document multi-nadia-profile-page-012. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).

document multi-north-bell-workshop-archive-012::multi-document-012::1: In document multi-north-bell-workshop-archive-012, the verified arc

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Case scope id: multi-document-012. Combined evidence: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-north-bell-workshop-archive-012::multi-document-012::1: In document multi-north-bell-workshop-archive-012, the verified archive note records blue glass jar. Case record id: multi-document-012. Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Scope reminder: document multi-north-bell-workshop-archive-012. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

Chunk rank 4:

```text
document multi-nadia-profile-page-012::multi-document-012::2: In document multi-nadia-profile-page-012, the verified archive note records tin key. Case record id: multi-document-012. Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Scope reminder: document multi-nadia-profile-page-012. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 5:

```text
document multi-bell-bridge-square-archive-060::multi-document-060::1: In document multi-bell-bridge-square-archive-060, the verified archive note records blue glass jar. Case record id: multi-document-060. Question: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Scope reminder: document multi-bell-bridge-square-archive-060. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

## Question 013: multi-document-013

**Question:** Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier?

**Expected evidence:**
- marker `Moon Orchard Rest`
- aliases `festival Moon Orchard Rest, the Moon Orchard Rest record`
- marker `copper wind vane pin`
- aliases `preserved item copper wind vane pin, copper wind vane pin in the preserved record`
- marker `brass compass`
- aliases `corroborating item brass compass, brass compass in the second document`

**Forbidden evidence:**
- marker `birch tea flask`
- aliases `irrelevant document detail birch tea flask`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Orchard Rest, brass compass, copper wind vane pin`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22153 | n/a | 77.6707 |
| 2 | 21839 | n/a | 26.7322 |
| 3 | 21840 | n/a | 16.6362 |
| 4 | 21935 | n/a | 14.2136 |
| 5 | 21908 | n/a | 6.2929 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-document-013. Scoped answer summary for multi-document-013 repeats the grounded evidence set: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-memory-log-013::multi-document-013::2: In document multi-anya-memory-log-013, the verified archive note records copper wind vane pin. Case record id: multi-document-013. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-anya-memory-log-013. Alias reminders for retrieval: copper wind vane pin (aliases: pre

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-fog-island-pier-ledger-013::multi-document-013::1: In document multi-fog-island-pier-ledger-013, the verified archive note records Moon Orchard Rest. Case record id: multi-document-013. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-fog-island-pier-ledger-013. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 3:

```text
document multi-fog-island-pier-ledger-073::multi-document-073::1: In document multi-fog-island-pier-ledger-073, the verified archive note records Moon Orchard Rest. Case record id: multi-document-073. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-fog-island-pier-ledger-073. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 4:

```text
document multi-old-quarry-path-travel-note-053::multi-document-053::1: In document multi-old-quarry-path-travel-note-053, the verified archive note records Moon Orchard Rest. Case record id: multi-document-053. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Scope reminder: document multi-old-quarry-path-travel-note-053. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 5:

```text
document multi-moon-orchard-rest-family-register-053::multi-document-053::3: In document multi-moon-orchard-rest-family-register-053, the verified archive note records oak barrel hoops. Case record id: multi-document-053. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Scope reminder: document multi-moon-orchard-rest-family-register-053. Alias reminders for retrieval: oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Orchard Rest, brass compass, copper wind vane pin`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22153 | n/a | 77.6506 |
| 2 | 22154 | n/a | 58.5826 |
| 3 | 21906 | n/a | 30.5148 |
| 4 | 21839 | n/a | 26.6741 |
| 5 | 21840 | n/a | 16.6359 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-document-013. Scoped answer summary for multi-document-013 repeats the grounded evidence set: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-memory-log-013::multi-document-013::2: In document multi-anya-memory-log-013, the verified archive note records copper wind vane pin. Case record id: multi-document-013. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-anya-memory-log-013. Alias reminders for retrieval: copper wind vane pin (aliases: pre

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-document-013. Combined evidence: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-moon-orchard-rest-audio-transcript-013::multi-document-013::3: In document multi-moon-orchard-rest-audio-transcript-013, the verified archive note records brass compass. Case record id: multi-document-013. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-moon-orchard-rest-audio-transcript-013. Alias reminders for retrieval: brass compass (aliases: corroborating item brass compass; brass compass in the second document).
```

Chunk rank 4:

```text
document multi-fog-island-pier-ledger-013::multi-document-013::1: In document multi-fog-island-pier-ledger-013, the verified archive note records Moon Orchard Rest. Case record id: multi-document-013. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-fog-island-pier-ledger-013. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 5:

```text
document multi-fog-island-pier-ledger-073::multi-document-073::1: In document multi-fog-island-pier-ledger-073, the verified archive note records Moon Orchard Rest. Case record id: multi-document-073. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-fog-island-pier-ledger-073. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

## Question 014: multi-document-014

**Question:** Which archive pieces from more than one document explain the family profile event at Moon Mill yard?

**Expected evidence:**
- marker `wax thread`
- aliases `archive piece wax thread, wax thread in the first archive piece`
- marker `basalt sketch`
- aliases `second archive piece basalt sketch, basalt sketch in the second archive piece`

**Forbidden evidence:**
- marker `oak barrel hoops`
- aliases `irrelevant document detail oak barrel hoops`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `basalt sketch, wax thread`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22155 | n/a | 65.5274 |
| 2 | 22156 | n/a | 46.4102 |
| 3 | 21904 | n/a | 26.4611 |
| 4 | 22011 | n/a | 26.3392 |
| 5 | 22316 | n/a | 13.8892 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-014. Scoped answer summary for multi-document-014 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-moon-mill-yard-minute-book-014::multi-document-014::1: In document multi-moon-mill-yard-minute-book-014, the verified archive note records wax thread. Case record id: multi-document-014. Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Scope reminder: document multi-moon-mill-yard-minute-book-014. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).

document multi-yara-travel-note-014::multi-document-014::

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-014. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-moon-mill-yard-minute-book-014::multi-document-014::1: In document multi-moon-mill-yard-minute-book-014, the verified archive note records wax thread. Case record id: multi-document-014. Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Scope reminder: document multi-moon-mill-yard-minute-book-014. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

Chunk rank 4:

```text
document multi-yara-travel-note-014::multi-document-014::2: In document multi-yara-travel-note-014, the verified archive note records basalt sketch. Case record id: multi-document-014. Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Scope reminder: document multi-yara-travel-note-014. Alias reminders for retrieval: basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece).
```

Chunk rank 5:

```text
Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `basalt sketch, wax thread`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22155 | n/a | 65.4891 |
| 2 | 22156 | n/a | 46.4563 |
| 3 | 21904 | n/a | 26.5130 |
| 4 | 21905 | n/a | 4.4640 |
| 5 | 22012 | n/a | 4.4087 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-014. Scoped answer summary for multi-document-014 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-moon-mill-yard-minute-book-014::multi-document-014::1: In document multi-moon-mill-yard-minute-book-014, the verified archive note records wax thread. Case record id: multi-document-014. Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Scope reminder: document multi-moon-mill-yard-minute-book-014. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).

document multi-yara-travel-note-014::multi-document-014::

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-014. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-moon-mill-yard-minute-book-014::multi-document-014::1: In document multi-moon-mill-yard-minute-book-014, the verified archive note records wax thread. Case record id: multi-document-014. Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Scope reminder: document multi-moon-mill-yard-minute-book-014. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

Chunk rank 4:

```text
document multi-moon-mill-yard-minute-book-074::multi-document-074::1: In document multi-moon-mill-yard-minute-book-074, the verified archive note records clay watering cup. Case record id: multi-document-074. Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Scope reminder: document multi-moon-mill-yard-minute-book-074. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece).
```

Chunk rank 5:

```text
document multi-yara-travel-note-074::multi-document-074::2: In document multi-yara-travel-note-074, the verified archive note records canal route map. Case record id: multi-document-074. Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Scope reminder: document multi-yara-travel-note-074. Alias reminders for retrieval: canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece).
```

## Question 015: multi-document-015

**Question:** Which documents must be combined to understand Ada's holiday card note about Driftwood cove?

**Expected evidence:**
- marker `smoke vent chain`
- aliases `combined note smoke vent chain, smoke vent chain in one required document`
- marker `copper token`
- aliases `combined note copper token, copper token in another required document`
- marker `silver booth token`
- aliases `combined note silver booth token, silver booth token only visible after combining documents`

**Forbidden evidence:**
- marker `glass ink bottle`
- aliases `irrelevant document detail glass ink bottle`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `copper token, silver booth token, smoke vent chain`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22157 | n/a | 77.2997 |
| 2 | 22158 | n/a | 58.1596 |
| 3 | 21883 | n/a | 26.2355 |
| 4 | 21793 | n/a | 26.2029 |
| 5 | 21832 | n/a | 26.1087 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Case scope id: multi-document-015. Scoped answer summary for multi-document-015 repeats the grounded evidence set: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-photo-index-015::multi-document-015::2: In document multi-ada-photo-index-015, the verified archive note records copper token. Case record id: multi-document-015. Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Scope reminder: document multi-ada-photo-index-015. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper toke

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Case scope id: multi-document-015. Combined evidence: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-lantern-tide-repair-book-015::multi-document-015::3: In document multi-lantern-tide-repair-book-015, the verified archive note records silver booth token. Case record id: multi-document-015. Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Scope reminder: document multi-lantern-tide-repair-book-015. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

Chunk rank 4:

```text
document multi-ada-photo-index-015::multi-document-015::2: In document multi-ada-photo-index-015, the verified archive note records copper token. Case record id: multi-document-015. Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Scope reminder: document multi-ada-photo-index-015. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token in another required document).
```

Chunk rank 5:

```text
document multi-driftwood-cove-profile-page-015::multi-document-015::1: In document multi-driftwood-cove-profile-page-015, the verified archive note records smoke vent chain. Case record id: multi-document-015. Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Scope reminder: document multi-driftwood-cove-profile-page-015. Alias reminders for retrieval: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `copper token, silver booth token, smoke vent chain`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22157 | n/a | 77.0531 |
| 2 | 22158 | n/a | 58.0039 |
| 3 | 21832 | n/a | 26.0433 |
| 4 | 21793 | n/a | 26.0248 |
| 5 | 21792 | n/a | 13.5145 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Case scope id: multi-document-015. Scoped answer summary for multi-document-015 repeats the grounded evidence set: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-photo-index-015::multi-document-015::2: In document multi-ada-photo-index-015, the verified archive note records copper token. Case record id: multi-document-015. Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Scope reminder: document multi-ada-photo-index-015. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper toke

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Case scope id: multi-document-015. Combined evidence: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-driftwood-cove-profile-page-015::multi-document-015::1: In document multi-driftwood-cove-profile-page-015, the verified archive note records smoke vent chain. Case record id: multi-document-015. Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Scope reminder: document multi-driftwood-cove-profile-page-015. Alias reminders for retrieval: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document).
```

Chunk rank 4:

```text
document multi-ada-photo-index-015::multi-document-015::2: In document multi-ada-photo-index-015, the verified archive note records copper token. Case record id: multi-document-015. Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Scope reminder: document multi-ada-photo-index-015. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token in another required document).
```

Chunk rank 5:

```text
document multi-ada-minute-book-095::multi-document-095::2: In document multi-ada-minute-book-095, the verified archive note records copper token. Case record id: multi-document-095. Question: Which documents must be combined to understand Ada's archive card note about River Lantern inn? Scope reminder: document multi-ada-minute-book-095. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token in another required document).
```

## Question 016: multi-document-016

**Question:** Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft?

**Expected evidence:**
- marker `amber lantern`
- aliases `travel record amber lantern, amber lantern in one document`
- marker `tuning fork`
- aliases `supporting record tuning fork, tuning fork in another document`

**Forbidden evidence:**
- marker `weathered camera strap`
- aliases `irrelevant document detail weathered camera strap`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `amber lantern, tuning fork`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22159 | n/a | 65.3625 |
| 2 | 22160 | n/a | 46.2472 |
| 3 | 21940 | n/a | 26.4233 |
| 4 | 21968 | n/a | 26.1969 |
| 5 | 21941 | n/a | 4.3757 |

Chunk rank 1:

```text
Question anchor: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-016. Scoped answer summary for multi-document-016 repeats the grounded evidence set: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ridge-post-loft-memory-log-016::multi-document-016::1: In document multi-ridge-post-loft-memory-log-016, the verified archive note records amber lantern. Case record id: multi-document-016. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-ridge-post-loft-memory-log-016. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).

document multi-sonya-audio-transcript-016::multi-document-016::2: In document multi-sonya-audio-t

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-016. Combined evidence: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ridge-post-loft-memory-log-016::multi-document-016::1: In document multi-ridge-post-loft-memory-log-016, the verified archive note records amber lantern. Case record id: multi-document-016. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-ridge-post-loft-memory-log-016. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 4:

```text
document multi-sonya-audio-transcript-016::multi-document-016::2: In document multi-sonya-audio-transcript-016, the verified archive note records tuning fork. Case record id: multi-document-016. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-sonya-audio-transcript-016. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

Chunk rank 5:

```text
document multi-ridge-post-loft-memory-log-076::multi-document-076::1: In document multi-ridge-post-loft-memory-log-076, the verified archive note records blue glass jar. Case record id: multi-document-076. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-ridge-post-loft-memory-log-076. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `amber lantern, tuning fork`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22159 | n/a | 65.2485 |
| 2 | 22160 | n/a | 46.2175 |
| 3 | 21940 | n/a | 26.2496 |
| 4 | 21968 | n/a | 26.1269 |
| 5 | 22320 | n/a | 13.6796 |

Chunk rank 1:

```text
Question anchor: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-016. Scoped answer summary for multi-document-016 repeats the grounded evidence set: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ridge-post-loft-memory-log-016::multi-document-016::1: In document multi-ridge-post-loft-memory-log-016, the verified archive note records amber lantern. Case record id: multi-document-016. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-ridge-post-loft-memory-log-016. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).

document multi-sonya-audio-transcript-016::multi-document-016::2: In document multi-sonya-audio-t

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-016. Combined evidence: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ridge-post-loft-memory-log-016::multi-document-016::1: In document multi-ridge-post-loft-memory-log-016, the verified archive note records amber lantern. Case record id: multi-document-016. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-ridge-post-loft-memory-log-016. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 4:

```text
document multi-sonya-audio-transcript-016::multi-document-016::2: In document multi-sonya-audio-transcript-016, the verified archive note records tuning fork. Case record id: multi-document-016. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-sonya-audio-transcript-016. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

Chunk rank 5:

```text
Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-096. Combined evidence: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 017: multi-document-017

**Question:** Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room?

**Expected evidence:**
- marker `Harvest Glow`
- aliases `festival Harvest Glow, the Harvest Glow record`
- marker `cedar shovel`
- aliases `preserved item cedar shovel, cedar shovel in the preserved record`
- marker `willow basket`
- aliases `corroborating item willow basket, willow basket in the second document`

**Forbidden evidence:**
- marker `juniper bundles`
- aliases `irrelevant document detail juniper bundles`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Harvest Glow, cedar shovel, willow basket`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22161 | n/a | 77.6708 |
| 2 | 22162 | n/a | 58.5113 |
| 3 | 21854 | n/a | 30.6848 |
| 4 | 21836 | n/a | 26.6860 |
| 5 | 21837 | n/a | 16.6860 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-017. Scoped answer summary for multi-document-017 repeats the grounded evidence set: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-east-signal-room-travel-note-017::multi-document-017::1: In document multi-east-signal-room-travel-note-017, the verified archive note records Harvest Glow. Case record id: multi-document-017. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-east-signal-room-travel-note-017. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-017. Combined evidence: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-harvest-glow-family-register-017::multi-document-017::3: In document multi-harvest-glow-family-register-017, the verified archive note records willow basket. Case record id: multi-document-017. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-harvest-glow-family-register-017. Alias reminders for retrieval: willow basket (aliases: corroborating item willow basket; willow basket in the second document).
```

Chunk rank 4:

```text
document multi-east-signal-room-travel-note-017::multi-document-017::1: In document multi-east-signal-room-travel-note-017, the verified archive note records Harvest Glow. Case record id: multi-document-017. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-east-signal-room-travel-note-017. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

Chunk rank 5:

```text
document multi-east-signal-room-travel-note-077::multi-document-077::1: In document multi-east-signal-room-travel-note-077, the verified archive note records Harvest Glow. Case record id: multi-document-077. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-east-signal-room-travel-note-077. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Harvest Glow, cedar shovel, willow basket`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22161 | n/a | 77.5770 |
| 2 | 22162 | n/a | 58.5390 |
| 3 | 21854 | n/a | 30.4296 |
| 4 | 21836 | n/a | 26.6218 |
| 5 | 22322 | n/a | 25.9914 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-017. Scoped answer summary for multi-document-017 repeats the grounded evidence set: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-east-signal-room-travel-note-017::multi-document-017::1: In document multi-east-signal-room-travel-note-017, the verified archive note records Harvest Glow. Case record id: multi-document-017. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-east-signal-room-travel-note-017. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-017. Combined evidence: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-harvest-glow-family-register-017::multi-document-017::3: In document multi-harvest-glow-family-register-017, the verified archive note records willow basket. Case record id: multi-document-017. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-harvest-glow-family-register-017. Alias reminders for retrieval: willow basket (aliases: corroborating item willow basket; willow basket in the second document).
```

Chunk rank 4:

```text
document multi-east-signal-room-travel-note-017::multi-document-017::1: In document multi-east-signal-room-travel-note-017, the verified archive note records Harvest Glow. Case record id: multi-document-017. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-east-signal-room-travel-note-017. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

Chunk rank 5:

```text
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-097. Combined evidence: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 018: multi-document-018

**Question:** Which archive pieces from more than one document explain the family profile event at South Meadow arch?

**Expected evidence:**
- marker `violet ribbon`
- aliases `archive piece violet ribbon, violet ribbon in the first archive piece`
- marker `star ledger page`
- aliases `second archive piece star ledger page, star ledger page in the second archive piece`

**Forbidden evidence:**
- marker `carved shell comb`
- aliases `irrelevant document detail carved shell comb`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `star ledger page, violet ribbon`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22163 | n/a | 65.5103 |
| 2 | 22164 | n/a | 46.4006 |
| 3 | 21979 | n/a | 26.5518 |
| 4 | 21980 | n/a | 4.5518 |
| 5 | 21872 | n/a | 4.3864 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-018. Scoped answer summary for multi-document-018 repeats the grounded evidence set: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-repair-book-018::multi-document-018::2: In document multi-iveta-repair-book-018, the verified archive note records star ledger page. Case record id: multi-document-018. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-iveta-repair-book-018. Alias reminders for retrieval: star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece).

document multi-south-meadow-

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-018. Combined evidence: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-south-meadow-arch-photo-index-018::multi-document-018::1: In document multi-south-meadow-arch-photo-index-018, the verified archive note records violet ribbon. Case record id: multi-document-018. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-south-meadow-arch-photo-index-018. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

Chunk rank 4:

```text
document multi-south-meadow-arch-photo-index-078::multi-document-078::1: In document multi-south-meadow-arch-photo-index-078, the verified archive note records wax thread. Case record id: multi-document-078. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-south-meadow-arch-photo-index-078. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

Chunk rank 5:

```text
document multi-iveta-repair-book-078::multi-document-078::2: In document multi-iveta-repair-book-078, the verified archive note records basalt sketch. Case record id: multi-document-078. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-iveta-repair-book-078. Alias reminders for retrieval: basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `star ledger page, violet ribbon`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22163 | n/a | 65.4483 |
| 2 | 22164 | n/a | 46.4007 |
| 3 | 21979 | n/a | 26.4987 |
| 4 | 21980 | n/a | 4.5173 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-018. Scoped answer summary for multi-document-018 repeats the grounded evidence set: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-repair-book-018::multi-document-018::2: In document multi-iveta-repair-book-018, the verified archive note records star ledger page. Case record id: multi-document-018. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-iveta-repair-book-018. Alias reminders for retrieval: star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece).

document multi-south-meadow-

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-018. Combined evidence: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-south-meadow-arch-photo-index-018::multi-document-018::1: In document multi-south-meadow-arch-photo-index-018, the verified archive note records violet ribbon. Case record id: multi-document-018. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-south-meadow-arch-photo-index-018. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

Chunk rank 4:

```text
document multi-south-meadow-arch-photo-index-078::multi-document-078::1: In document multi-south-meadow-arch-photo-index-078, the verified archive note records wax thread. Case record id: multi-document-078. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-south-meadow-arch-photo-index-078. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

## Question 019: multi-document-019

**Question:** Which documents must be combined to understand Zora's boat manifest note about Maple Court attic?

**Expected evidence:**
- marker `blue oar`
- aliases `combined note blue oar, blue oar in one required document`
- marker `silver booth token`
- aliases `combined note silver booth token, silver booth token in another required document`
- marker `weathered camera strap`
- aliases `combined note weathered camera strap, weathered camera strap only visible after combining documents`

**Forbidden evidence:**
- marker `canal route map`
- aliases `irrelevant document detail canal route map`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `blue oar, silver booth token, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 2 < 3.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22166 | n/a | 58.3303 |
| 2 | 21887 | n/a | 26.2932 |
| 3 | 21888 | n/a | 2.0222 |

Chunk rank 1:

```text
Question: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic? Case scope id: multi-document-019. Combined evidence: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 2:

```text
document multi-maple-court-attic-audio-transcript-019::multi-document-019::1: In document multi-maple-court-attic-audio-transcript-019, the verified archive note records blue oar. Case record id: multi-document-019. Question: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic? Scope reminder: document multi-maple-court-attic-audio-transcript-019. Alias reminders for retrieval: blue oar (aliases: combined note blue oar; blue oar in one required document).
```

Chunk rank 3:

```text
document multi-maple-court-attic-audio-transcript-079::multi-document-079::1: In document multi-maple-court-attic-audio-transcript-079, the verified archive note records smoke vent chain. Case record id: multi-document-079. Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Scope reminder: document multi-maple-court-attic-audio-transcript-079. Alias reminders for retrieval: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue oar, silver booth token, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22165 | n/a | 77.3638 |
| 2 | 22166 | n/a | 58.2551 |
| 3 | 21887 | n/a | 26.3817 |
| 4 | 22015 | n/a | 26.2574 |
| 5 | 21958 | n/a | 26.1813 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic? Case scope id: multi-document-019. Scoped answer summary for multi-document-019 repeats the grounded evidence set: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-maple-court-attic-audio-transcript-019::multi-document-019::1: In document multi-maple-court-attic-audio-transcript-019, the verified archive note records blue oar. Case record id: multi-document-019. Question: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic? Scope reminder: document multi-maple-court-attic-audio-transcript-019. Alias reminders for retr

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic? Case scope id: multi-document-019. Combined evidence: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-maple-court-attic-audio-transcript-019::multi-document-019::1: In document multi-maple-court-attic-audio-transcript-019, the verified archive note records blue oar. Case record id: multi-document-019. Question: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic? Scope reminder: document multi-maple-court-attic-audio-transcript-019. Alias reminders for retrieval: blue oar (aliases: combined note blue oar; blue oar in one required document).
```

Chunk rank 4:

```text
document multi-zora-inventory-sheet-019::multi-document-019::2: In document multi-zora-inventory-sheet-019, the verified archive note records silver booth token. Case record id: multi-document-019. Question: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic? Scope reminder: document multi-zora-inventory-sheet-019. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token in another required document).
```

Chunk rank 5:

```text
document multi-signal-lantern-morning-ledger-019::multi-document-019::3: In document multi-signal-lantern-morning-ledger-019, the verified archive note records weathered camera strap. Case record id: multi-document-019. Question: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic? Scope reminder: document multi-signal-lantern-morning-ledger-019. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents).
```

## Question 020: multi-document-020

**Question:** Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery?

**Expected evidence:**
- marker `linen wick`
- aliases `travel record linen wick, linen wick in one document`
- marker `birch tea flask`
- aliases `supporting record birch tea flask, birch tea flask in another document`

**Forbidden evidence:**
- marker `coal stove hiss`
- aliases `irrelevant document detail coal stove hiss`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `birch tea flask, linen wick`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22167 | n/a | 65.4880 |
| 2 | 22168 | n/a | 46.3603 |
| 3 | 21895 | n/a | 26.5360 |
| 4 | 21981 | n/a | 26.3620 |
| 5 | 21894 | n/a | 13.9825 |

Chunk rank 1:

```text
Question anchor: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Case scope id: multi-document-020. Scoped answer summary for multi-document-020 repeats the grounded evidence set: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-mira-family-register-020::multi-document-020::2: In document multi-mira-family-register-020, the verified archive note records birch tea flask. Case record id: multi-document-020. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-mira-family-register-020. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).

document multi-star-basin-gallery-letter-roll-020::multi-document-020::1: In documen

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Case scope id: multi-document-020. Combined evidence: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-mira-family-register-020::multi-document-020::2: In document multi-mira-family-register-020, the verified archive note records birch tea flask. Case record id: multi-document-020. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-mira-family-register-020. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 4:

```text
document multi-star-basin-gallery-letter-roll-020::multi-document-020::1: In document multi-star-basin-gallery-letter-roll-020, the verified archive note records linen wick. Case record id: multi-document-020. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-star-basin-gallery-letter-roll-020. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 5:

```text
document multi-mira-audio-transcript-100::multi-document-100::2: In document multi-mira-audio-transcript-100, the verified archive note records birch tea flask. Case record id: multi-document-100. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-mira-audio-transcript-100. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `birch tea flask, linen wick`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22167 | n/a | 65.2465 |
| 2 | 22168 | n/a | 46.1780 |
| 3 | 21981 | n/a | 26.2638 |
| 4 | 21982 | n/a | 4.2960 |
| 5 | 21896 | n/a | 4.1829 |

Chunk rank 1:

```text
Question anchor: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Case scope id: multi-document-020. Scoped answer summary for multi-document-020 repeats the grounded evidence set: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-mira-family-register-020::multi-document-020::2: In document multi-mira-family-register-020, the verified archive note records birch tea flask. Case record id: multi-document-020. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-mira-family-register-020. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).

document multi-star-basin-gallery-letter-roll-020::multi-document-020::1: In documen

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Case scope id: multi-document-020. Combined evidence: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-star-basin-gallery-letter-roll-020::multi-document-020::1: In document multi-star-basin-gallery-letter-roll-020, the verified archive note records linen wick. Case record id: multi-document-020. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-star-basin-gallery-letter-roll-020. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 4:

```text
document multi-star-basin-gallery-letter-roll-080::multi-document-080::1: In document multi-star-basin-gallery-letter-roll-080, the verified archive note records amber lantern. Case record id: multi-document-080. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-star-basin-gallery-letter-roll-080. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 5:

```text
document multi-mira-family-register-080::multi-document-080::2: In document multi-mira-family-register-080, the verified archive note records tuning fork. Case record id: multi-document-080. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-mira-family-register-080. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

## Question 021: multi-document-021

**Question:** Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse?

**Expected evidence:**
- marker `Bellwater Fair`
- aliases `festival Bellwater Fair, the Bellwater Fair record`
- marker `green apron`
- aliases `preserved item green apron, green apron in the preserved record`
- marker `oak barrel hoops`
- aliases `corroborating item oak barrel hoops, oak barrel hoops in the second document`

**Forbidden evidence:**
- marker `tin key`
- aliases `irrelevant document detail tin key`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Bellwater Fair, green apron, oak barrel hoops`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22169 | n/a | 77.6195 |
| 2 | 22170 | n/a | 58.6182 |
| 3 | 21966 | n/a | 26.6571 |
| 4 | 21967 | n/a | 16.6571 |
| 5 | 21938 | n/a | 14.0636 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-document-021. Scoped answer summary for multi-document-021 repeats the grounded evidence set: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-profile-page-021::multi-document-021::3: In document multi-bellwater-fair-profile-page-021, the verified archive note records oak barrel hoops. Case record id: multi-document-021. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-bellwater-fair-profile-page-021. Alias reminders for retrieval: oak barrel hoops (a

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-document-021. Combined evidence: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-snow-orchard-storehouse-repair-book-021::multi-document-021::1: In document multi-snow-orchard-storehouse-repair-book-021, the verified archive note records Bellwater Fair. Case record id: multi-document-021. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-snow-orchard-storehouse-repair-book-021. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

Chunk rank 4:

```text
document multi-snow-orchard-storehouse-repair-book-081::multi-document-081::1: In document multi-snow-orchard-storehouse-repair-book-081, the verified archive note records Bellwater Fair. Case record id: multi-document-081. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-snow-orchard-storehouse-repair-book-081. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

Chunk rank 5:

```text
document multi-pine-gate-yard-travel-note-041::multi-document-041::1: In document multi-pine-gate-yard-travel-note-041, the verified archive note records Bellwater Fair. Case record id: multi-document-041. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Scope reminder: document multi-pine-gate-yard-travel-note-041. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Bellwater Fair, green apron, oak barrel hoops`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22169 | n/a | 77.5255 |
| 2 | 22170 | n/a | 58.4872 |
| 3 | 21984 | n/a | 30.4393 |
| 4 | 21966 | n/a | 26.5173 |
| 5 | 21967 | n/a | 16.4800 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-document-021. Scoped answer summary for multi-document-021 repeats the grounded evidence set: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-profile-page-021::multi-document-021::3: In document multi-bellwater-fair-profile-page-021, the verified archive note records oak barrel hoops. Case record id: multi-document-021. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-bellwater-fair-profile-page-021. Alias reminders for retrieval: oak barrel hoops (a

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-document-021. Combined evidence: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-vera-archive-021::multi-document-021::2: In document multi-vera-archive-021, the verified archive note records green apron. Case record id: multi-document-021. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-vera-archive-021. Alias reminders for retrieval: green apron (aliases: preserved item green apron; green apron in the preserved record).
```

Chunk rank 4:

```text
document multi-snow-orchard-storehouse-repair-book-021::multi-document-021::1: In document multi-snow-orchard-storehouse-repair-book-021, the verified archive note records Bellwater Fair. Case record id: multi-document-021. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-snow-orchard-storehouse-repair-book-021. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

Chunk rank 5:

```text
document multi-snow-orchard-storehouse-repair-book-081::multi-document-081::1: In document multi-snow-orchard-storehouse-repair-book-081, the verified archive note records Bellwater Fair. Case record id: multi-document-081. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-snow-orchard-storehouse-repair-book-081. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

## Question 022: multi-document-022

**Question:** Which archive pieces from more than one document explain the family profile event at Cedar Hill station?

**Expected evidence:**
- marker `moonflower cutting`
- aliases `archive piece moonflower cutting, moonflower cutting in the first archive piece`
- marker `glass ink bottle`
- aliases `second archive piece glass ink bottle, glass ink bottle in the second archive piece`

**Forbidden evidence:**
- marker `brass compass`
- aliases `irrelevant document detail brass compass`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `glass ink bottle, moonflower cutting`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22171 | n/a | 65.3961 |
| 2 | 22172 | n/a | 46.4036 |
| 3 | 21826 | n/a | 26.3427 |
| 4 | 21827 | n/a | 4.3427 |
| 5 | 22299 | n/a | 3.9041 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Case scope id: multi-document-022. Scoped answer summary for multi-document-022 repeats the grounded evidence set: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-cedar-hill-station-inventory-sheet-022::multi-document-022::1: In document multi-cedar-hill-station-inventory-sheet-022, the verified archive note records moonflower cutting. Case record id: multi-document-022. Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Scope reminder: document multi-cedar-hill-station-inventory-sheet-022. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflowe

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Case scope id: multi-document-022. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-cedar-hill-station-inventory-sheet-022::multi-document-022::1: In document multi-cedar-hill-station-inventory-sheet-022, the verified archive note records moonflower cutting. Case record id: multi-document-022. Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Scope reminder: document multi-cedar-hill-station-inventory-sheet-022. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

Chunk rank 4:

```text
document multi-cedar-hill-station-inventory-sheet-082::multi-document-082::1: In document multi-cedar-hill-station-inventory-sheet-082, the verified archive note records violet ribbon. Case record id: multi-document-082. Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Scope reminder: document multi-cedar-hill-station-inventory-sheet-082. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

Chunk rank 5:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Scoped answer summary for multi-document-086 repeats the grounded evidence set: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note records moonflower cutting. Case record id: multi-document-086. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-086. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in

[truncated in Markdown; full text is available in JSON]
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `glass ink bottle, moonflower cutting`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22171 | n/a | 65.4408 |
| 2 | 22172 | n/a | 46.4702 |
| 3 | 22140 | n/a | 13.9791 |
| 4 | 22300 | n/a | 13.9749 |
| 5 | 22268 | n/a | 13.9749 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Case scope id: multi-document-022. Scoped answer summary for multi-document-022 repeats the grounded evidence set: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-cedar-hill-station-inventory-sheet-022::multi-document-022::1: In document multi-cedar-hill-station-inventory-sheet-022, the verified archive note records moonflower cutting. Case record id: multi-document-022. Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Scope reminder: document multi-cedar-hill-station-inventory-sheet-022. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflowe

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Case scope id: multi-document-022. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 4:

```text
Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 5:

```text
Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Case scope id: multi-document-070. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 023: multi-document-023

**Question:** Which documents must be combined to understand Anya's travel ledger note about Old Quarry path?

**Expected evidence:**
- marker `rope bridge permit`
- aliases `combined note rope bridge permit, rope bridge permit in one required document`
- marker `weathered camera strap`
- aliases `combined note weathered camera strap, weathered camera strap in another required document`
- marker `coal stove hiss`
- aliases `combined note coal stove hiss, coal stove hiss only visible after combining documents`

**Forbidden evidence:**
- marker `basalt sketch`
- aliases `irrelevant document detail basalt sketch`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, rope bridge permit, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22173 | n/a | 77.3223 |
| 2 | 21933 | n/a | 26.3394 |
| 3 | 21804 | n/a | 26.2557 |
| 4 | 21934 | n/a | 2.1516 |
| 5 | 21805 | n/a | 2.0963 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Case scope id: multi-document-023. Scoped answer summary for multi-document-023 repeats the grounded evidence set: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-minute-book-023::multi-document-023::2: In document multi-anya-minute-book-023, the verified archive note records weathered camera strap. Case record id: multi-document-023. Question: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Scope reminder: document multi-anya-minute-book-023. Alias reminders for retrieval: weathered camera

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-old-quarry-path-family-register-023::multi-document-023::1: In document multi-old-quarry-path-family-register-023, the verified archive note records rope bridge permit. Case record id: multi-document-023. Question: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Scope reminder: document multi-old-quarry-path-family-register-023. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 3:

```text
document multi-anya-minute-book-023::multi-document-023::2: In document multi-anya-minute-book-023, the verified archive note records weathered camera strap. Case record id: multi-document-023. Question: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Scope reminder: document multi-anya-minute-book-023. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document).
```

Chunk rank 4:

```text
document multi-old-quarry-path-family-register-083::multi-document-083::1: In document multi-old-quarry-path-family-register-083, the verified archive note records blue oar. Case record id: multi-document-083. Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Scope reminder: document multi-old-quarry-path-family-register-083. Alias reminders for retrieval: blue oar (aliases: combined note blue oar; blue oar in one required document).
```

Chunk rank 5:

```text
document multi-anya-minute-book-083::multi-document-083::2: In document multi-anya-minute-book-083, the verified archive note records silver booth token. Case record id: multi-document-083. Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Scope reminder: document multi-anya-minute-book-083. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token in another required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, rope bridge permit, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22173 | n/a | 77.2210 |
| 2 | 22174 | n/a | 58.1545 |
| 3 | 21933 | n/a | 26.2010 |
| 4 | 21804 | n/a | 26.1340 |
| 5 | 21913 | n/a | 26.0907 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Case scope id: multi-document-023. Scoped answer summary for multi-document-023 repeats the grounded evidence set: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-minute-book-023::multi-document-023::2: In document multi-anya-minute-book-023, the verified archive note records weathered camera strap. Case record id: multi-document-023. Question: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Scope reminder: document multi-anya-minute-book-023. Alias reminders for retrieval: weathered camera

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Case scope id: multi-document-023. Combined evidence: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-old-quarry-path-family-register-023::multi-document-023::1: In document multi-old-quarry-path-family-register-023, the verified archive note records rope bridge permit. Case record id: multi-document-023. Question: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Scope reminder: document multi-old-quarry-path-family-register-023. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 4:

```text
document multi-anya-minute-book-023::multi-document-023::2: In document multi-anya-minute-book-023, the verified archive note records weathered camera strap. Case record id: multi-document-023. Question: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Scope reminder: document multi-anya-minute-book-023. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document).
```

Chunk rank 5:

```text
document multi-moon-orchard-rest-travel-note-023::multi-document-023::3: In document multi-moon-orchard-rest-travel-note-023, the verified archive note records coal stove hiss. Case record id: multi-document-023. Question: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Scope reminder: document multi-moon-orchard-rest-travel-note-023. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents).
```

## Question 024: multi-document-024

**Question:** Which records together show how Yara prepared the canal barge stop near Cloud Wharf office?

**Expected evidence:**
- marker `paper moon mask`
- aliases `travel record paper moon mask, paper moon mask in one document`
- marker `juniper bundles`
- aliases `supporting record juniper bundles, juniper bundles in another document`

**Forbidden evidence:**
- marker `copper token`
- aliases `irrelevant document detail copper token`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `juniper bundles, paper moon mask`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22175 | n/a | 65.4130 |
| 2 | 21829 | n/a | 26.4375 |
| 3 | 22008 | n/a | 26.2762 |
| 4 | 21830 | n/a | 4.5603 |
| 5 | 22009 | n/a | 4.3727 |

Chunk rank 1:

```text
Question anchor: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-024. Scoped answer summary for multi-document-024 repeats the grounded evidence set: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-cloud-wharf-office-archive-024::multi-document-024::1: In document multi-cloud-wharf-office-archive-024, the verified archive note records paper moon mask. Case record id: multi-document-024. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-024. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).

document multi-yara-profile-page-024::multi-document-024::2: In doc

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-cloud-wharf-office-archive-024::multi-document-024::1: In document multi-cloud-wharf-office-archive-024, the verified archive note records paper moon mask. Case record id: multi-document-024. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-024. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).
```

Chunk rank 3:

```text
document multi-yara-profile-page-024::multi-document-024::2: In document multi-yara-profile-page-024, the verified archive note records juniper bundles. Case record id: multi-document-024. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-yara-profile-page-024. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

Chunk rank 4:

```text
document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records linen wick. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-084. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 5:

```text
document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-yara-profile-page-084. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `juniper bundles, paper moon mask`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22175 | n/a | 65.2801 |
| 2 | 22176 | n/a | 46.1718 |
| 3 | 21829 | n/a | 26.2608 |
| 4 | 22008 | n/a | 26.2042 |
| 5 | 21830 | n/a | 4.2986 |

Chunk rank 1:

```text
Question anchor: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-024. Scoped answer summary for multi-document-024 repeats the grounded evidence set: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-cloud-wharf-office-archive-024::multi-document-024::1: In document multi-cloud-wharf-office-archive-024, the verified archive note records paper moon mask. Case record id: multi-document-024. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-024. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).

document multi-yara-profile-page-024::multi-document-024::2: In doc

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-024. Combined evidence: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-cloud-wharf-office-archive-024::multi-document-024::1: In document multi-cloud-wharf-office-archive-024, the verified archive note records paper moon mask. Case record id: multi-document-024. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-024. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).
```

Chunk rank 4:

```text
document multi-yara-profile-page-024::multi-document-024::2: In document multi-yara-profile-page-024, the verified archive note records juniper bundles. Case record id: multi-document-024. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-yara-profile-page-024. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

Chunk rank 5:

```text
document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records linen wick. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-084. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

## Question 025: multi-document-025

**Question:** Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor?

**Expected evidence:**
- marker `Lantern Tide`
- aliases `festival Lantern Tide, the Lantern Tide record`
- marker `lantern hook`
- aliases `preserved item lantern hook, lantern hook in the preserved record`
- marker `carved shell comb`
- aliases `corroborating item carved shell comb, carved shell comb in the second document`

**Forbidden evidence:**
- marker `tuning fork`
- aliases `irrelevant document detail tuning fork`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Tide, carved shell comb, lantern hook`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22177 | n/a | 77.4607 |
| 2 | 22178 | n/a | 58.4510 |
| 3 | 21789 | n/a | 30.4884 |
| 4 | 21850 | n/a | 26.4081 |
| 5 | 21851 | n/a | 16.5463 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-document-025. Scoped answer summary for multi-document-025 repeats the grounded evidence set: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-memory-log-025::multi-document-025::2: In document multi-ada-memory-log-025, the verified archive note records lantern hook. Case record id: multi-document-025. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-ada-memory-log-025. Alias reminders for retrieval: lantern hook (aliases: preserved item lantern hook; lantern hook in the

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-document-025. Combined evidence: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ada-memory-log-025::multi-document-025::2: In document multi-ada-memory-log-025, the verified archive note records lantern hook. Case record id: multi-document-025. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-ada-memory-log-025. Alias reminders for retrieval: lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record).
```

Chunk rank 4:

```text
document multi-harbor-glass-corridor-ledger-025::multi-document-025::1: In document multi-harbor-glass-corridor-ledger-025, the verified archive note records Lantern Tide. Case record id: multi-document-025. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-harbor-glass-corridor-ledger-025. Alias reminders for retrieval: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record).
```

Chunk rank 5:

```text
document multi-harbor-glass-corridor-ledger-085::multi-document-085::1: In document multi-harbor-glass-corridor-ledger-085, the verified archive note records Lantern Tide. Case record id: multi-document-085. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-harbor-glass-corridor-ledger-085. Alias reminders for retrieval: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Tide, carved shell comb, lantern hook`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22177 | n/a | 77.5063 |
| 2 | 22178 | n/a | 58.4420 |
| 3 | 21789 | n/a | 30.3920 |
| 4 | 21878 | n/a | 30.3414 |
| 5 | 21850 | n/a | 26.5099 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-document-025. Scoped answer summary for multi-document-025 repeats the grounded evidence set: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-memory-log-025::multi-document-025::2: In document multi-ada-memory-log-025, the verified archive note records lantern hook. Case record id: multi-document-025. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-ada-memory-log-025. Alias reminders for retrieval: lantern hook (aliases: preserved item lantern hook; lantern hook in the

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-document-025. Combined evidence: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ada-memory-log-025::multi-document-025::2: In document multi-ada-memory-log-025, the verified archive note records lantern hook. Case record id: multi-document-025. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-ada-memory-log-025. Alias reminders for retrieval: lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record).
```

Chunk rank 4:

```text
document multi-lantern-tide-audio-transcript-025::multi-document-025::3: In document multi-lantern-tide-audio-transcript-025, the verified archive note records carved shell comb. Case record id: multi-document-025. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-lantern-tide-audio-transcript-025. Alias reminders for retrieval: carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document).
```

Chunk rank 5:

```text
document multi-harbor-glass-corridor-ledger-025::multi-document-025::1: In document multi-harbor-glass-corridor-ledger-025, the verified archive note records Lantern Tide. Case record id: multi-document-025. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-harbor-glass-corridor-ledger-025. Alias reminders for retrieval: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record).
```

## Question 026: multi-document-026

**Question:** Which archive pieces from more than one document explain the family profile event at North Orchard lane?

**Expected evidence:**
- marker `clay watering cup`
- aliases `archive piece clay watering cup, clay watering cup in the first archive piece`
- marker `canal route map`
- aliases `second archive piece canal route map, canal route map in the second archive piece`

**Forbidden evidence:**
- marker `willow basket`
- aliases `irrelevant document detail willow basket`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `canal route map, clay watering cup`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22179 | n/a | 65.4047 |
| 2 | 21931 | n/a | 26.3938 |
| 3 | 21932 | n/a | 4.4611 |
| 4 | 21977 | n/a | 4.3392 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-026. Scoped answer summary for multi-document-026 repeats the grounded evidence set: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece); canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-north-orchard-lane-minute-book-026::multi-document-026::1: In document multi-north-orchard-lane-minute-book-026, the verified archive note records clay watering cup. Case record id: multi-document-026. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-026. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-north-orchard-lane-minute-book-026::multi-document-026::1: In document multi-north-orchard-lane-minute-book-026, the verified archive note records clay watering cup. Case record id: multi-document-026. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-026. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece).
```

Chunk rank 3:

```text
document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note records moonflower cutting. Case record id: multi-document-086. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-086. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

Chunk rank 4:

```text
document multi-sonya-travel-note-086::multi-document-086::2: In document multi-sonya-travel-note-086, the verified archive note records glass ink bottle. Case record id: multi-document-086. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-sonya-travel-note-086. Alias reminders for retrieval: glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `canal route map, clay watering cup`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22179 | n/a | 65.5032 |
| 2 | 22180 | n/a | 46.3852 |
| 3 | 21931 | n/a | 26.4697 |
| 4 | 21976 | n/a | 26.4534 |
| 5 | 21932 | n/a | 4.5332 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-026. Scoped answer summary for multi-document-026 repeats the grounded evidence set: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece); canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-north-orchard-lane-minute-book-026::multi-document-026::1: In document multi-north-orchard-lane-minute-book-026, the verified archive note records clay watering cup. Case record id: multi-document-026. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-026. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-026. Combined evidence: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece); canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-north-orchard-lane-minute-book-026::multi-document-026::1: In document multi-north-orchard-lane-minute-book-026, the verified archive note records clay watering cup. Case record id: multi-document-026. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-026. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece).
```

Chunk rank 4:

```text
document multi-sonya-travel-note-026::multi-document-026::2: In document multi-sonya-travel-note-026, the verified archive note records canal route map. Case record id: multi-document-026. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-sonya-travel-note-026. Alias reminders for retrieval: canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece).
```

Chunk rank 5:

```text
document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note records moonflower cutting. Case record id: multi-document-086. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-086. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

## Question 027: multi-document-027

**Question:** Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade?

**Expected evidence:**
- marker `saffron scarf`
- aliases `combined note saffron scarf, saffron scarf in one required document`
- marker `coal stove hiss`
- aliases `combined note coal stove hiss, coal stove hiss in another required document`
- marker `copper token`
- aliases `combined note copper token, copper token only visible after combining documents`

**Forbidden evidence:**
- marker `star ledger page`
- aliases `irrelevant document detail star ledger page`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, copper token, saffron scarf`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22181 | n/a | 77.4541 |
| 2 | 21862 | n/a | 26.4485 |
| 3 | 21953 | n/a | 26.2845 |
| 4 | 21863 | n/a | 2.1498 |
| 5 | 21841 | n/a | 1.6969 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade? Case scope id: multi-document-027. Scoped answer summary for multi-document-027 repeats the grounded evidence set: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-harvest-glow-repair-book-027::multi-document-027::3: In document multi-harvest-glow-repair-book-027, the verified archive note records copper token. Case record id: multi-document-027. Question: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade? Scope reminder: document multi-harvest-glow-repair-book-027. Alias reminders for retrieval: copper token (aliases: combin

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-hollow-market-arcade-profile-page-027::multi-document-027::1: In document multi-hollow-market-arcade-profile-page-027, the verified archive note records saffron scarf. Case record id: multi-document-027. Question: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade? Scope reminder: document multi-hollow-market-arcade-profile-page-027. Alias reminders for retrieval: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document).
```

Chunk rank 3:

```text
document multi-runa-photo-index-027::multi-document-027::2: In document multi-runa-photo-index-027, the verified archive note records coal stove hiss. Case record id: multi-document-027. Question: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade? Scope reminder: document multi-runa-photo-index-027. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document).
```

Chunk rank 4:

```text
document multi-hollow-market-arcade-profile-page-087::multi-document-087::1: In document multi-hollow-market-arcade-profile-page-087, the verified archive note records rope bridge permit. Case record id: multi-document-087. Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Scope reminder: document multi-hollow-market-arcade-profile-page-087. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 5:

```text
document multi-fox-hollow-bridge-audio-transcript-007::multi-document-007::1: In document multi-fox-hollow-bridge-audio-transcript-007, the verified archive note records rope bridge permit. Case record id: multi-document-007. Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-audio-transcript-007. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, copper token, saffron scarf`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22181 | n/a | 77.1321 |
| 2 | 22182 | n/a | 58.1420 |
| 3 | 21862 | n/a | 26.0789 |
| 4 | 21859 | n/a | 26.0625 |
| 5 | 21953 | n/a | 26.0445 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade? Case scope id: multi-document-027. Scoped answer summary for multi-document-027 repeats the grounded evidence set: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-harvest-glow-repair-book-027::multi-document-027::3: In document multi-harvest-glow-repair-book-027, the verified archive note records copper token. Case record id: multi-document-027. Question: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade? Scope reminder: document multi-harvest-glow-repair-book-027. Alias reminders for retrieval: copper token (aliases: combin

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade? Case scope id: multi-document-027. Combined evidence: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-hollow-market-arcade-profile-page-027::multi-document-027::1: In document multi-hollow-market-arcade-profile-page-027, the verified archive note records saffron scarf. Case record id: multi-document-027. Question: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade? Scope reminder: document multi-hollow-market-arcade-profile-page-027. Alias reminders for retrieval: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document).
```

Chunk rank 4:

```text
document multi-harvest-glow-repair-book-027::multi-document-027::3: In document multi-harvest-glow-repair-book-027, the verified archive note records copper token. Case record id: multi-document-027. Question: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade? Scope reminder: document multi-harvest-glow-repair-book-027. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token only visible after combining documents).
```

Chunk rank 5:

```text
document multi-runa-photo-index-027::multi-document-027::2: In document multi-runa-photo-index-027, the verified archive note records coal stove hiss. Case record id: multi-document-027. Question: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade? Scope reminder: document multi-runa-photo-index-027. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document).
```

## Question 028: multi-document-028

**Question:** Which records together show how Iveta prepared the winter coach stop near Marble stair hall?

**Expected evidence:**
- marker `blue glass jar`
- aliases `travel record blue glass jar, blue glass jar in one document`
- marker `tin key`
- aliases `supporting record tin key, tin key in another document`

**Forbidden evidence:**
- marker `silver booth token`
- aliases `irrelevant document detail silver booth token`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue glass jar, tin key`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22183 | n/a | 65.2381 |
| 2 | 21891 | n/a | 26.2041 |
| 3 | 21865 | n/a | 26.2015 |
| 4 | 21866 | n/a | 4.2015 |
| 5 | 21868 | n/a | 1.8129 |

Chunk rank 1:

```text
Question anchor: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Case scope id: multi-document-028. Scoped answer summary for multi-document-028 repeats the grounded evidence set: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-audio-transcript-028::multi-document-028::2: In document multi-iveta-audio-transcript-028, the verified archive note records tin key. Case record id: multi-document-028. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-iveta-audio-transcript-028. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).

document multi-marble-stair-hall-memory-log-028::multi-document-028::1: In document multi-marble-stair-hall-memory-log-028, the

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-marble-stair-hall-memory-log-028::multi-document-028::1: In document multi-marble-stair-hall-memory-log-028, the verified archive note records blue glass jar. Case record id: multi-document-028. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-marble-stair-hall-memory-log-028. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

Chunk rank 3:

```text
document multi-iveta-audio-transcript-028::multi-document-028::2: In document multi-iveta-audio-transcript-028, the verified archive note records tin key. Case record id: multi-document-028. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-iveta-audio-transcript-028. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 4:

```text
document multi-iveta-audio-transcript-088::multi-document-088::2: In document multi-iveta-audio-transcript-088, the verified archive note records juniper bundles. Case record id: multi-document-088. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-iveta-audio-transcript-088. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

Chunk rank 5:

```text
document multi-iveta-family-register-068::multi-document-068::2: In document multi-iveta-family-register-068, the verified archive note records birch tea flask. Case record id: multi-document-068. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-iveta-family-register-068. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue glass jar, tin key`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22183 | n/a | 65.2331 |
| 2 | 22184 | n/a | 46.2182 |
| 3 | 21891 | n/a | 26.2125 |
| 4 | 21865 | n/a | 26.1228 |
| 5 | 21892 | n/a | 4.2023 |

Chunk rank 1:

```text
Question anchor: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Case scope id: multi-document-028. Scoped answer summary for multi-document-028 repeats the grounded evidence set: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-audio-transcript-028::multi-document-028::2: In document multi-iveta-audio-transcript-028, the verified archive note records tin key. Case record id: multi-document-028. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-iveta-audio-transcript-028. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).

document multi-marble-stair-hall-memory-log-028::multi-document-028::1: In document multi-marble-stair-hall-memory-log-028, the

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Case scope id: multi-document-028. Combined evidence: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-marble-stair-hall-memory-log-028::multi-document-028::1: In document multi-marble-stair-hall-memory-log-028, the verified archive note records blue glass jar. Case record id: multi-document-028. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-marble-stair-hall-memory-log-028. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

Chunk rank 4:

```text
document multi-iveta-audio-transcript-028::multi-document-028::2: In document multi-iveta-audio-transcript-028, the verified archive note records tin key. Case record id: multi-document-028. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-iveta-audio-transcript-028. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 5:

```text
document multi-marble-stair-hall-memory-log-088::multi-document-088::1: In document multi-marble-stair-hall-memory-log-088, the verified archive note records paper moon mask. Case record id: multi-document-088. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-marble-stair-hall-memory-log-088. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).
```

## Question 029: multi-document-029

**Question:** Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock?

**Expected evidence:**
- marker `Signal Lantern Morning`
- aliases `festival Signal Lantern Morning, the Signal Lantern Morning record`
- marker `copper wind vane pin`
- aliases `preserved item copper wind vane pin, copper wind vane pin in the preserved record`
- marker `brass compass`
- aliases `corroborating item brass compass, brass compass in the second document`

**Forbidden evidence:**
- marker `birch tea flask`
- aliases `irrelevant document detail birch tea flask`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning, brass compass, copper wind vane pin`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22185 | n/a | 77.6482 |
| 2 | 22186 | n/a | 58.4708 |
| 3 | 21956 | n/a | 30.4867 |
| 4 | 21796 | n/a | 26.7980 |
| 5 | 21797 | n/a | 16.7980 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-document-029. Scoped answer summary for multi-document-029 repeats the grounded evidence set: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-amber-canal-lock-travel-note-029::multi-document-029::1: In document multi-amber-canal-lock-travel-note-029, the verified archive note records Signal Lantern Morning. Case record id: multi-document-029. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-amber-canal-lock-travel-note-02

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-document-029. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-signal-lantern-morning-family-register-029::multi-document-029::3: In document multi-signal-lantern-morning-family-register-029, the verified archive note records brass compass. Case record id: multi-document-029. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-signal-lantern-morning-family-register-029. Alias reminders for retrieval: brass compass (aliases: corroborating item brass compass; brass compass in the second document).
```

Chunk rank 4:

```text
document multi-amber-canal-lock-travel-note-029::multi-document-029::1: In document multi-amber-canal-lock-travel-note-029, the verified archive note records Signal Lantern Morning. Case record id: multi-document-029. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-amber-canal-lock-travel-note-029. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

Chunk rank 5:

```text
document multi-amber-canal-lock-travel-note-089::multi-document-089::1: In document multi-amber-canal-lock-travel-note-089, the verified archive note records Signal Lantern Morning. Case record id: multi-document-089. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-amber-canal-lock-travel-note-089. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning, brass compass, copper wind vane pin`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22185 | n/a | 77.5438 |
| 2 | 22186 | n/a | 58.5097 |
| 3 | 21796 | n/a | 26.5765 |
| 4 | 21797 | n/a | 16.5765 |
| 5 | 21957 | n/a | 8.4417 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-document-029. Scoped answer summary for multi-document-029 repeats the grounded evidence set: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-amber-canal-lock-travel-note-029::multi-document-029::1: In document multi-amber-canal-lock-travel-note-029, the verified archive note records Signal Lantern Morning. Case record id: multi-document-029. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-amber-canal-lock-travel-note-02

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-document-029. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-amber-canal-lock-travel-note-029::multi-document-029::1: In document multi-amber-canal-lock-travel-note-029, the verified archive note records Signal Lantern Morning. Case record id: multi-document-029. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-amber-canal-lock-travel-note-029. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

Chunk rank 4:

```text
document multi-amber-canal-lock-travel-note-089::multi-document-089::1: In document multi-amber-canal-lock-travel-note-089, the verified archive note records Signal Lantern Morning. Case record id: multi-document-089. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-amber-canal-lock-travel-note-089. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

Chunk rank 5:

```text
document multi-signal-lantern-morning-family-register-089::multi-document-089::3: In document multi-signal-lantern-morning-family-register-089, the verified archive note records carved shell comb. Case record id: multi-document-089. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-signal-lantern-morning-family-register-089. Alias reminders for retrieval: carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document).
```

## Question 030: multi-document-030

**Question:** Which archive pieces from more than one document explain the family profile event at Bell Bridge square?

**Expected evidence:**
- marker `wax thread`
- aliases `archive piece wax thread, wax thread in the first archive piece`
- marker `basalt sketch`
- aliases `second archive piece basalt sketch, basalt sketch in the second archive piece`

**Forbidden evidence:**
- marker `oak barrel hoops`
- aliases `irrelevant document detail oak barrel hoops`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `basalt sketch, wax thread`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22187 | n/a | 65.5168 |
| 2 | 22188 | n/a | 46.4102 |
| 3 | 21808 | n/a | 26.4611 |
| 4 | 22316 | n/a | 14.0392 |
| 5 | 22156 | n/a | 14.0335 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-030. Scoped answer summary for multi-document-030 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bell-bridge-square-photo-index-030::multi-document-030::1: In document multi-bell-bridge-square-photo-index-030, the verified archive note records wax thread. Case record id: multi-document-030. Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Scope reminder: document multi-bell-bridge-square-photo-index-030. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).

document multi-mira-repair-book-030::

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-030. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-bell-bridge-square-photo-index-030::multi-document-030::1: In document multi-bell-bridge-square-photo-index-030, the verified archive note records wax thread. Case record id: multi-document-030. Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Scope reminder: document multi-bell-bridge-square-photo-index-030. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

Chunk rank 4:

```text
Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 5:

```text
Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-014. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `basalt sketch, wax thread`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22187 | n/a | 65.5104 |
| 2 | 22188 | n/a | 46.4803 |
| 3 | 21808 | n/a | 26.5221 |
| 4 | 22251 | n/a | 3.9605 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-030. Scoped answer summary for multi-document-030 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bell-bridge-square-photo-index-030::multi-document-030::1: In document multi-bell-bridge-square-photo-index-030, the verified archive note records wax thread. Case record id: multi-document-030. Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Scope reminder: document multi-bell-bridge-square-photo-index-030. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).

document multi-mira-repair-book-030::

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-030. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-bell-bridge-square-photo-index-030::multi-document-030::1: In document multi-bell-bridge-square-photo-index-030, the verified archive note records wax thread. Case record id: multi-document-030. Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Scope reminder: document multi-bell-bridge-square-photo-index-030. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

Chunk rank 4:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Case scope id: multi-document-062. Scoped answer summary for multi-document-062 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-lantern-row-kiosk-minute-book-062::multi-document-062::1: In document multi-lantern-row-kiosk-minute-book-062, the verified archive note records wax thread. Case record id: multi-document-062. Question: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-minute-book-062. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).

document multi-nadia-travel-note-062::mult

[truncated in Markdown; full text is available in JSON]
```

## Question 031: multi-document-031

**Question:** Which documents must be combined to understand Vera's photo album page note about Watchtower landing?

**Expected evidence:**
- marker `smoke vent chain`
- aliases `combined note smoke vent chain, smoke vent chain in one required document`
- marker `copper token`
- aliases `combined note copper token, copper token in another required document`
- marker `silver booth token`
- aliases `combined note silver booth token, silver booth token only visible after combining documents`

**Forbidden evidence:**
- marker `glass ink bottle`
- aliases `irrelevant document detail glass ink bottle`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `copper token, silver booth token, smoke vent chain`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22189 | n/a | 77.3722 |
| 2 | 22190 | n/a | 58.2730 |
| 3 | 21993 | n/a | 26.2975 |
| 4 | 21812 | n/a | 26.1797 |
| 5 | 21915 | n/a | 13.4258 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Case scope id: multi-document-031. Scoped answer summary for multi-document-031 repeats the grounded evidence set: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-ledger-031::multi-document-031::3: In document multi-bellwater-fair-ledger-031, the verified archive note records silver booth token. Case record id: multi-document-031. Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Scope reminder: document multi-bellwater-fair-ledger-031. Alias reminders for retrieval: silver booth token (

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Case scope id: multi-document-031. Combined evidence: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-watchtower-landing-audio-transcript-031::multi-document-031::1: In document multi-watchtower-landing-audio-transcript-031, the verified archive note records smoke vent chain. Case record id: multi-document-031. Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Scope reminder: document multi-watchtower-landing-audio-transcript-031. Alias reminders for retrieval: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document).
```

Chunk rank 4:

```text
document multi-bellwater-fair-ledger-031::multi-document-031::3: In document multi-bellwater-fair-ledger-031, the verified archive note records silver booth token. Case record id: multi-document-031. Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Scope reminder: document multi-bellwater-fair-ledger-031. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

Chunk rank 5:

```text
document multi-moss-archive-room-profile-page-063::multi-document-063::1: In document multi-moss-archive-room-profile-page-063, the verified archive note records smoke vent chain. Case record id: multi-document-063. Question: Which documents must be combined to understand Anya's family note note about Moss Archive room? Scope reminder: document multi-moss-archive-room-profile-page-063. Alias reminders for retrieval: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `copper token, silver booth token, smoke vent chain`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22189 | n/a | 77.1609 |
| 2 | 22190 | n/a | 58.1539 |
| 3 | 21993 | n/a | 26.1201 |
| 4 | 21986 | n/a | 26.1102 |
| 5 | 21812 | n/a | 26.0595 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Case scope id: multi-document-031. Scoped answer summary for multi-document-031 repeats the grounded evidence set: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-ledger-031::multi-document-031::3: In document multi-bellwater-fair-ledger-031, the verified archive note records silver booth token. Case record id: multi-document-031. Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Scope reminder: document multi-bellwater-fair-ledger-031. Alias reminders for retrieval: silver booth token (

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Case scope id: multi-document-031. Combined evidence: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-watchtower-landing-audio-transcript-031::multi-document-031::1: In document multi-watchtower-landing-audio-transcript-031, the verified archive note records smoke vent chain. Case record id: multi-document-031. Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Scope reminder: document multi-watchtower-landing-audio-transcript-031. Alias reminders for retrieval: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document).
```

Chunk rank 4:

```text
document multi-vera-inventory-sheet-031::multi-document-031::2: In document multi-vera-inventory-sheet-031, the verified archive note records copper token. Case record id: multi-document-031. Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Scope reminder: document multi-vera-inventory-sheet-031. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token in another required document).
```

Chunk rank 5:

```text
document multi-bellwater-fair-ledger-031::multi-document-031::3: In document multi-bellwater-fair-ledger-031, the verified archive note records silver booth token. Case record id: multi-document-031. Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Scope reminder: document multi-bellwater-fair-ledger-031. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

## Question 032: multi-document-032

**Question:** Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk?

**Expected evidence:**
- marker `amber lantern`
- aliases `travel record amber lantern, amber lantern in one document`
- marker `tuning fork`
- aliases `supporting record tuning fork, tuning fork in another document`

**Forbidden evidence:**
- marker `weathered camera strap`
- aliases `irrelevant document detail weathered camera strap`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `amber lantern, tuning fork`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22191 | n/a | 65.3398 |
| 2 | 21875 | n/a | 26.3337 |
| 3 | 21919 | n/a | 26.2596 |
| 4 | 21920 | n/a | 4.3401 |
| 5 | 21876 | n/a | 4.2557 |

Chunk rank 1:

```text
Question anchor: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Case scope id: multi-document-032. Scoped answer summary for multi-document-032 repeats the grounded evidence set: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-lantern-row-kiosk-letter-roll-032::multi-document-032::1: In document multi-lantern-row-kiosk-letter-roll-032, the verified archive note records amber lantern. Case record id: multi-document-032. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-letter-roll-032. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).

document multi-nadia-family-register-032::multi-document-032::2: In document multi-n

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-lantern-row-kiosk-letter-roll-032::multi-document-032::1: In document multi-lantern-row-kiosk-letter-roll-032, the verified archive note records amber lantern. Case record id: multi-document-032. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-letter-roll-032. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 3:

```text
document multi-nadia-family-register-032::multi-document-032::2: In document multi-nadia-family-register-032, the verified archive note records tuning fork. Case record id: multi-document-032. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-nadia-family-register-032. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

Chunk rank 4:

```text
document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-family-register-092, the verified archive note records tin key. Case record id: multi-document-092. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-nadia-family-register-092. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 5:

```text
document multi-lantern-row-kiosk-letter-roll-092::multi-document-092::1: In document multi-lantern-row-kiosk-letter-roll-092, the verified archive note records blue glass jar. Case record id: multi-document-092. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-letter-roll-092. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `amber lantern, tuning fork`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22191 | n/a | 65.1722 |
| 2 | 22192 | n/a | 46.1957 |
| 3 | 21875 | n/a | 26.1187 |
| 4 | 21876 | n/a | 4.1478 |
| 5 | 21920 | n/a | 4.1141 |

Chunk rank 1:

```text
Question anchor: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Case scope id: multi-document-032. Scoped answer summary for multi-document-032 repeats the grounded evidence set: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-lantern-row-kiosk-letter-roll-032::multi-document-032::1: In document multi-lantern-row-kiosk-letter-roll-032, the verified archive note records amber lantern. Case record id: multi-document-032. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-letter-roll-032. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).

document multi-nadia-family-register-032::multi-document-032::2: In document multi-n

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Case scope id: multi-document-032. Combined evidence: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-lantern-row-kiosk-letter-roll-032::multi-document-032::1: In document multi-lantern-row-kiosk-letter-roll-032, the verified archive note records amber lantern. Case record id: multi-document-032. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-letter-roll-032. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 4:

```text
document multi-lantern-row-kiosk-letter-roll-092::multi-document-092::1: In document multi-lantern-row-kiosk-letter-roll-092, the verified archive note records blue glass jar. Case record id: multi-document-092. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-letter-roll-092. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

Chunk rank 5:

```text
document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-family-register-092, the verified archive note records tin key. Case record id: multi-document-092. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-nadia-family-register-092. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

## Question 033: multi-document-033

**Question:** Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room?

**Expected evidence:**
- marker `Moon Orchard Rest`
- aliases `festival Moon Orchard Rest, the Moon Orchard Rest record`
- marker `cedar shovel`
- aliases `preserved item cedar shovel, cedar shovel in the preserved record`
- marker `willow basket`
- aliases `corroborating item willow basket, willow basket in the second document`

**Forbidden evidence:**
- marker `juniper bundles`
- aliases `irrelevant document detail juniper bundles`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Orchard Rest, cedar shovel, willow basket`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22193 | n/a | 77.6830 |
| 2 | 21916 | n/a | 26.6000 |
| 3 | 21917 | n/a | 16.6000 |
| 4 | 21935 | n/a | 14.4669 |
| 5 | 21908 | n/a | 6.5606 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-document-033. Scoped answer summary for multi-document-033 repeats the grounded evidence set: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-archive-033::multi-document-033::2: In document multi-anya-archive-033, the verified archive note records cedar shovel. Case record id: multi-document-033. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Scope reminder: document multi-anya-archive-033. Alias reminders for retrieval: cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-moss-archive-room-repair-book-033::multi-document-033::1: In document multi-moss-archive-room-repair-book-033, the verified archive note records Moon Orchard Rest. Case record id: multi-document-033. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Scope reminder: document multi-moss-archive-room-repair-book-033. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 3:

```text
document multi-moss-archive-room-repair-book-093::multi-document-093::1: In document multi-moss-archive-room-repair-book-093, the verified archive note records Moon Orchard Rest. Case record id: multi-document-093. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Scope reminder: document multi-moss-archive-room-repair-book-093. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 4:

```text
document multi-old-quarry-path-travel-note-053::multi-document-053::1: In document multi-old-quarry-path-travel-note-053, the verified archive note records Moon Orchard Rest. Case record id: multi-document-053. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Scope reminder: document multi-old-quarry-path-travel-note-053. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 5:

```text
document multi-moon-orchard-rest-family-register-053::multi-document-053::3: In document multi-moon-orchard-rest-family-register-053, the verified archive note records oak barrel hoops. Case record id: multi-document-053. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Scope reminder: document multi-moon-orchard-rest-family-register-053. Alias reminders for retrieval: oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Orchard Rest, cedar shovel, willow basket`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22193 | n/a | 77.6066 |
| 2 | 22194 | n/a | 58.6167 |
| 3 | 21916 | n/a | 26.6105 |
| 4 | 21917 | n/a | 16.6105 |
| 5 | 22314 | n/a | 4.5797 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-document-033. Scoped answer summary for multi-document-033 repeats the grounded evidence set: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-archive-033::multi-document-033::2: In document multi-anya-archive-033, the verified archive note records cedar shovel. Case record id: multi-document-033. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Scope reminder: document multi-anya-archive-033. Alias reminders for retrieval: cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-document-033. Combined evidence: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-moss-archive-room-repair-book-033::multi-document-033::1: In document multi-moss-archive-room-repair-book-033, the verified archive note records Moon Orchard Rest. Case record id: multi-document-033. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Scope reminder: document multi-moss-archive-room-repair-book-033. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 4:

```text
document multi-moss-archive-room-repair-book-093::multi-document-093::1: In document multi-moss-archive-room-repair-book-093, the verified archive note records Moon Orchard Rest. Case record id: multi-document-093. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Scope reminder: document multi-moss-archive-room-repair-book-093. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 5:

```text
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-document-093. Combined evidence: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 034: multi-document-034

**Question:** Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin?

**Expected evidence:**
- marker `violet ribbon`
- aliases `archive piece violet ribbon, violet ribbon in the first archive piece`
- marker `star ledger page`
- aliases `second archive piece star ledger page, star ledger page in the second archive piece`

**Forbidden evidence:**
- marker `carved shell comb`
- aliases `irrelevant document detail carved shell comb`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `violet ribbon, star ledger page`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: violet ribbon, star ledger page; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 140 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `violet ribbon`
- Missing: `star ledger page`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 1 < 2.; Missing expected markers: star ledger page; Evidence coverage below requirement: 0.500 < 1.000.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 21823 | n/a | 26.4187 |
| 2 | 21824 | n/a | 4.4372 |

Chunk rank 1:

```text
document multi-blue-trunk-cabin-inventory-sheet-034::multi-document-034::1: In document multi-blue-trunk-cabin-inventory-sheet-034, the verified archive note records violet ribbon. Case record id: multi-document-034. Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Scope reminder: document multi-blue-trunk-cabin-inventory-sheet-034. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

Chunk rank 2:

```text
document multi-blue-trunk-cabin-inventory-sheet-094::multi-document-094::1: In document multi-blue-trunk-cabin-inventory-sheet-094, the verified archive note records wax thread. Case record id: multi-document-094. Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Scope reminder: document multi-blue-trunk-cabin-inventory-sheet-094. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

## Question 035: multi-document-035

**Question:** Which documents must be combined to understand Ada's family note note about River Lantern inn?

**Expected evidence:**
- marker `blue oar`
- aliases `combined note blue oar, blue oar in one required document`
- marker `silver booth token`
- aliases `combined note silver booth token, silver booth token in another required document`
- marker `weathered camera strap`
- aliases `combined note weathered camera strap, weathered camera strap only visible after combining documents`

**Forbidden evidence:**
- marker `canal route map`
- aliases `irrelevant document detail canal route map`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue oar, silver booth token, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22197 | n/a | 77.3274 |
| 2 | 22198 | n/a | 58.2639 |
| 3 | 21791 | n/a | 26.3776 |
| 4 | 22166 | n/a | 25.4303 |
| 5 | 21787 | n/a | 9.5977 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Ada's family note note about River Lantern inn? Case scope id: multi-document-035. Scoped answer summary for multi-document-035 repeats the grounded evidence set: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-minute-book-035::multi-document-035::2: In document multi-ada-minute-book-035, the verified archive note records silver booth token. Case record id: multi-document-035. Question: Which documents must be combined to understand Ada's family note note about River Lantern inn? Scope reminder: document multi-ada-minute-book-035. Alias reminders for retrieval: silver booth token (aliases: combined note sil

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Ada's family note note about River Lantern inn? Case scope id: multi-document-035. Combined evidence: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ada-minute-book-035::multi-document-035::2: In document multi-ada-minute-book-035, the verified archive note records silver booth token. Case record id: multi-document-035. Question: Which documents must be combined to understand Ada's family note note about River Lantern inn? Scope reminder: document multi-ada-minute-book-035. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token in another required document).
```

Chunk rank 4:

```text
Question: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic? Case scope id: multi-document-019. Combined evidence: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 5:

```text
document multi-ada-inventory-sheet-055::multi-document-055::2: In document multi-ada-inventory-sheet-055, the verified archive note records weathered camera strap. Case record id: multi-document-055. Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Scope reminder: document multi-ada-inventory-sheet-055. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue oar, silver booth token, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22197 | n/a | 77.0878 |
| 2 | 22198 | n/a | 58.0254 |
| 3 | 21942 | n/a | 26.0999 |
| 4 | 21791 | n/a | 25.9677 |
| 5 | 21885 | n/a | 25.9643 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Ada's family note note about River Lantern inn? Case scope id: multi-document-035. Scoped answer summary for multi-document-035 repeats the grounded evidence set: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-minute-book-035::multi-document-035::2: In document multi-ada-minute-book-035, the verified archive note records silver booth token. Case record id: multi-document-035. Question: Which documents must be combined to understand Ada's family note note about River Lantern inn? Scope reminder: document multi-ada-minute-book-035. Alias reminders for retrieval: silver booth token (aliases: combined note sil

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Ada's family note note about River Lantern inn? Case scope id: multi-document-035. Combined evidence: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-river-lantern-inn-family-register-035::multi-document-035::1: In document multi-river-lantern-inn-family-register-035, the verified archive note records blue oar. Case record id: multi-document-035. Question: Which documents must be combined to understand Ada's family note note about River Lantern inn? Scope reminder: document multi-river-lantern-inn-family-register-035. Alias reminders for retrieval: blue oar (aliases: combined note blue oar; blue oar in one required document).
```

Chunk rank 4:

```text
document multi-ada-minute-book-035::multi-document-035::2: In document multi-ada-minute-book-035, the verified archive note records silver booth token. Case record id: multi-document-035. Question: Which documents must be combined to understand Ada's family note note about River Lantern inn? Scope reminder: document multi-ada-minute-book-035. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token in another required document).
```

Chunk rank 5:

```text
document multi-lantern-tide-travel-note-035::multi-document-035::3: In document multi-lantern-tide-travel-note-035, the verified archive note records weathered camera strap. Case record id: multi-document-035. Question: Which documents must be combined to understand Ada's family note note about River Lantern inn? Scope reminder: document multi-lantern-tide-travel-note-035. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents).
```

## Question 036: multi-document-036

**Question:** Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch?

**Expected evidence:**
- marker `linen wick`
- aliases `travel record linen wick, linen wick in one document`
- marker `birch tea flask`
- aliases `supporting record birch tea flask, birch tea flask in another document`

**Forbidden evidence:**
- marker `coal stove hiss`
- aliases `irrelevant document detail coal stove hiss`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `birch tea flask, linen wick`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22199 | n/a | 65.2639 |
| 2 | 22200 | n/a | 46.1974 |
| 3 | 22000 | n/a | 26.2456 |
| 4 | 21972 | n/a | 26.1939 |
| 5 | 21830 | n/a | 13.3301 |

Chunk rank 1:

```text
Question anchor: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-036. Scoped answer summary for multi-document-036 repeats the grounded evidence set: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-sonya-profile-page-036::multi-document-036::2: In document multi-sonya-profile-page-036, the verified archive note records birch tea flask. Case record id: multi-document-036. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-sonya-profile-page-036. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).

document multi-winter-chapel-porch-archive-036::multi-document-036::1: In document multi-winte

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-036. Combined evidence: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-winter-chapel-porch-archive-036::multi-document-036::1: In document multi-winter-chapel-porch-archive-036, the verified archive note records linen wick. Case record id: multi-document-036. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-winter-chapel-porch-archive-036. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 4:

```text
document multi-sonya-profile-page-036::multi-document-036::2: In document multi-sonya-profile-page-036, the verified archive note records birch tea flask. Case record id: multi-document-036. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-sonya-profile-page-036. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 5:

```text
document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records linen wick. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-084. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `birch tea flask, linen wick`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22199 | n/a | 65.2175 |
| 2 | 22200 | n/a | 46.1620 |
| 3 | 22000 | n/a | 26.2729 |
| 4 | 22001 | n/a | 4.2729 |
| 5 | 21973 | n/a | 4.1129 |

Chunk rank 1:

```text
Question anchor: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-036. Scoped answer summary for multi-document-036 repeats the grounded evidence set: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-sonya-profile-page-036::multi-document-036::2: In document multi-sonya-profile-page-036, the verified archive note records birch tea flask. Case record id: multi-document-036. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-sonya-profile-page-036. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).

document multi-winter-chapel-porch-archive-036::multi-document-036::1: In document multi-winte

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-036. Combined evidence: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-winter-chapel-porch-archive-036::multi-document-036::1: In document multi-winter-chapel-porch-archive-036, the verified archive note records linen wick. Case record id: multi-document-036. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-winter-chapel-porch-archive-036. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 4:

```text
document multi-winter-chapel-porch-archive-096::multi-document-096::1: In document multi-winter-chapel-porch-archive-096, the verified archive note records amber lantern. Case record id: multi-document-096. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-winter-chapel-porch-archive-096. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 5:

```text
document multi-sonya-profile-page-096::multi-document-096::2: In document multi-sonya-profile-page-096, the verified archive note records tuning fork. Case record id: multi-document-096. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-sonya-profile-page-096. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

## Question 037: multi-document-037

**Question:** Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge?

**Expected evidence:**
- marker `Harvest Glow`
- aliases `festival Harvest Glow, the Harvest Glow record`
- marker `green apron`
- aliases `preserved item green apron, green apron in the preserved record`
- marker `oak barrel hoops`
- aliases `corroborating item oak barrel hoops, oak barrel hoops in the second document`

**Forbidden evidence:**
- marker `tin key`
- aliases `irrelevant document detail tin key`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Harvest Glow, green apron, oak barrel hoops`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22201 | n/a | 77.6952 |
| 2 | 22202 | n/a | 58.5555 |
| 3 | 21852 | n/a | 30.5801 |
| 4 | 21950 | n/a | 30.5250 |
| 5 | 21843 | n/a | 26.6295 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-037. Scoped answer summary for multi-document-037 repeats the grounded evidence set: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-fox-hollow-bridge-ledger-037::multi-document-037::1: In document multi-fox-hollow-bridge-ledger-037, the verified archive note records Harvest Glow. Case record id: multi-document-037. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-ledger-037. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harv

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-037. Combined evidence: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-harvest-glow-audio-transcript-037::multi-document-037::3: In document multi-harvest-glow-audio-transcript-037, the verified archive note records oak barrel hoops. Case record id: multi-document-037. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-harvest-glow-audio-transcript-037. Alias reminders for retrieval: oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document).
```

Chunk rank 4:

```text
document multi-runa-memory-log-037::multi-document-037::2: In document multi-runa-memory-log-037, the verified archive note records green apron. Case record id: multi-document-037. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-runa-memory-log-037. Alias reminders for retrieval: green apron (aliases: preserved item green apron; green apron in the preserved record).
```

Chunk rank 5:

```text
document multi-fox-hollow-bridge-ledger-037::multi-document-037::1: In document multi-fox-hollow-bridge-ledger-037, the verified archive note records Harvest Glow. Case record id: multi-document-037. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-ledger-037. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Harvest Glow, green apron, oak barrel hoops`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22201 | n/a | 77.5270 |
| 2 | 22202 | n/a | 58.5050 |
| 3 | 21843 | n/a | 26.5074 |
| 4 | 21844 | n/a | 16.4772 |
| 5 | 21864 | n/a | 14.1133 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-037. Scoped answer summary for multi-document-037 repeats the grounded evidence set: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-fox-hollow-bridge-ledger-037::multi-document-037::1: In document multi-fox-hollow-bridge-ledger-037, the verified archive note records Harvest Glow. Case record id: multi-document-037. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-ledger-037. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harv

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-037. Combined evidence: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-fox-hollow-bridge-ledger-037::multi-document-037::1: In document multi-fox-hollow-bridge-ledger-037, the verified archive note records Harvest Glow. Case record id: multi-document-037. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-ledger-037. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

Chunk rank 4:

```text
document multi-fox-hollow-bridge-ledger-097::multi-document-097::1: In document multi-fox-hollow-bridge-ledger-097, the verified archive note records Harvest Glow. Case record id: multi-document-097. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-ledger-097. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

Chunk rank 5:

```text
document multi-hollow-market-arcade-repair-book-057::multi-document-057::1: In document multi-hollow-market-arcade-repair-book-057, the verified archive note records Harvest Glow. Case record id: multi-document-057. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Scope reminder: document multi-hollow-market-arcade-repair-book-057. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

## Question 038: multi-document-038

**Question:** Which archive pieces from more than one document explain the family profile event at Willow Courtyard well?

**Expected evidence:**
- marker `moonflower cutting`
- aliases `archive piece moonflower cutting, moonflower cutting in the first archive piece`
- marker `glass ink bottle`
- aliases `second archive piece glass ink bottle, glass ink bottle in the second archive piece`

**Forbidden evidence:**
- marker `brass compass`
- aliases `irrelevant document detail brass compass`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `glass ink bottle, moonflower cutting`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22203 | n/a | 65.4064 |
| 2 | 22204 | n/a | 46.4036 |
| 3 | 21998 | n/a | 26.3659 |
| 4 | 21999 | n/a | 4.3659 |
| 5 | 22299 | n/a | 3.9041 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Case scope id: multi-document-038. Scoped answer summary for multi-document-038 repeats the grounded evidence set: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-travel-note-038::multi-document-038::2: In document multi-iveta-travel-note-038, the verified archive note records glass ink bottle. Case record id: multi-document-038. Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Scope reminder: document multi-iveta-travel-note-038. Alias reminders for retrieval: glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece).

docum

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Case scope id: multi-document-038. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-willow-courtyard-well-minute-book-038::multi-document-038::1: In document multi-willow-courtyard-well-minute-book-038, the verified archive note records moonflower cutting. Case record id: multi-document-038. Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Scope reminder: document multi-willow-courtyard-well-minute-book-038. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

Chunk rank 4:

```text
document multi-willow-courtyard-well-minute-book-098::multi-document-098::1: In document multi-willow-courtyard-well-minute-book-098, the verified archive note records violet ribbon. Case record id: multi-document-098. Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Scope reminder: document multi-willow-courtyard-well-minute-book-098. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

Chunk rank 5:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Scoped answer summary for multi-document-086 repeats the grounded evidence set: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note records moonflower cutting. Case record id: multi-document-086. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-086. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in

[truncated in Markdown; full text is available in JSON]
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `glass ink bottle, moonflower cutting`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22203 | n/a | 65.5008 |
| 2 | 22204 | n/a | 46.4745 |
| 3 | 21998 | n/a | 26.4876 |
| 4 | 21873 | n/a | 26.3735 |
| 5 | 22236 | n/a | 13.9273 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Case scope id: multi-document-038. Scoped answer summary for multi-document-038 repeats the grounded evidence set: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-travel-note-038::multi-document-038::2: In document multi-iveta-travel-note-038, the verified archive note records glass ink bottle. Case record id: multi-document-038. Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Scope reminder: document multi-iveta-travel-note-038. Alias reminders for retrieval: glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece).

docum

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Case scope id: multi-document-038. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-willow-courtyard-well-minute-book-038::multi-document-038::1: In document multi-willow-courtyard-well-minute-book-038, the verified archive note records moonflower cutting. Case record id: multi-document-038. Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Scope reminder: document multi-willow-courtyard-well-minute-book-038. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

Chunk rank 4:

```text
document multi-iveta-travel-note-038::multi-document-038::2: In document multi-iveta-travel-note-038, the verified archive note records glass ink bottle. Case record id: multi-document-038. Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Scope reminder: document multi-iveta-travel-note-038. Alias reminders for retrieval: glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece).
```

Chunk rank 5:

```text
Question: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office? Case scope id: multi-document-054. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 039: multi-document-039

**Question:** Which documents must be combined to understand Zora's archive card note about Glass Harbor quay?

**Expected evidence:**
- marker `rope bridge permit`
- aliases `combined note rope bridge permit, rope bridge permit in one required document`
- marker `weathered camera strap`
- aliases `combined note weathered camera strap, weathered camera strap in another required document`
- marker `coal stove hiss`
- aliases `combined note coal stove hiss, coal stove hiss only visible after combining documents`

**Forbidden evidence:**
- marker `basalt sketch`
- aliases `irrelevant document detail basalt sketch`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, rope bridge permit, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22205 | n/a | 77.2201 |
| 2 | 22206 | n/a | 58.2214 |
| 3 | 21845 | n/a | 26.2041 |
| 4 | 22237 | n/a | 15.7590 |
| 5 | 21849 | n/a | 13.7764 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay? Case scope id: multi-document-039. Scoped answer summary for multi-document-039 repeats the grounded evidence set: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-glass-harbor-quay-profile-page-039::multi-document-039::1: In document multi-glass-harbor-quay-profile-page-039, the verified archive note records rope bridge permit. Case record id: multi-document-039. Question: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-profile-page-039. Alias r

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay? Case scope id: multi-document-039. Combined evidence: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-glass-harbor-quay-profile-page-039::multi-document-039::1: In document multi-glass-harbor-quay-profile-page-039, the verified archive note records rope bridge permit. Case record id: multi-document-039. Question: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-profile-page-039. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 4:

```text
Question anchor: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Case scope id: multi-document-055. Scoped answer summary for multi-document-055 repeats the grounded evidence set: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-inventory-sheet-055::multi-document-055::2: In document multi-ada-inventory-sheet-055, the verified archive note records weathered camera strap. Case record id: multi-document-055. Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Scope reminder: document multi-ada-inventory-sheet-055. Alias reminders for

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
document multi-harbor-glass-corridor-audio-transcript-055::multi-document-055::1: In document multi-harbor-glass-corridor-audio-transcript-055, the verified archive note records rope bridge permit. Case record id: multi-document-055. Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Scope reminder: document multi-harbor-glass-corridor-audio-transcript-055. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, rope bridge permit, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22205 | n/a | 77.2234 |
| 2 | 22206 | n/a | 58.1358 |
| 3 | 21845 | n/a | 26.2601 |
| 4 | 22021 | n/a | 26.1114 |
| 5 | 21846 | n/a | 2.2699 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay? Case scope id: multi-document-039. Scoped answer summary for multi-document-039 repeats the grounded evidence set: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-glass-harbor-quay-profile-page-039::multi-document-039::1: In document multi-glass-harbor-quay-profile-page-039, the verified archive note records rope bridge permit. Case record id: multi-document-039. Question: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-profile-page-039. Alias r

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay? Case scope id: multi-document-039. Combined evidence: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-glass-harbor-quay-profile-page-039::multi-document-039::1: In document multi-glass-harbor-quay-profile-page-039, the verified archive note records rope bridge permit. Case record id: multi-document-039. Question: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-profile-page-039. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 4:

```text
document multi-zora-photo-index-039::multi-document-039::2: In document multi-zora-photo-index-039, the verified archive note records weathered camera strap. Case record id: multi-document-039. Question: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay? Scope reminder: document multi-zora-photo-index-039. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document).
```

Chunk rank 5:

```text
document multi-glass-harbor-quay-profile-page-099::multi-document-099::1: In document multi-glass-harbor-quay-profile-page-099, the verified archive note records blue oar. Case record id: multi-document-099. Question: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-profile-page-099. Alias reminders for retrieval: blue oar (aliases: combined note blue oar; blue oar in one required document).
```

## Question 040: multi-document-040

**Question:** Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed?

**Expected evidence:**
- marker `paper moon mask`
- aliases `travel record paper moon mask, paper moon mask in one document`
- marker `juniper bundles`
- aliases `supporting record juniper bundles, juniper bundles in another document`

**Forbidden evidence:**
- marker `copper token`
- aliases `irrelevant document detail copper token`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `paper moon mask, juniper bundles`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: paper moon mask, juniper bundles; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 140 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 21894 | n/a | 4.3428 |
| 2 | 21822 | n/a | 4.1510 |
| 3 | 21895 | n/a | 2.2442 |
| 4 | 22009 | n/a | 1.5469 |

Chunk rank 1:

```text
document multi-mira-audio-transcript-100::multi-document-100::2: In document multi-mira-audio-transcript-100, the verified archive note records birch tea flask. Case record id: multi-document-100. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-mira-audio-transcript-100. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 2:

```text
document multi-birch-ferry-shed-memory-log-100::multi-document-100::1: In document multi-birch-ferry-shed-memory-log-100, the verified archive note records linen wick. Case record id: multi-document-100. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-memory-log-100. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 3:

```text
document multi-mira-family-register-020::multi-document-020::2: In document multi-mira-family-register-020, the verified archive note records birch tea flask. Case record id: multi-document-020. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-mira-family-register-020. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 4:

```text
document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-yara-profile-page-084. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `juniper bundles, paper moon mask`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22207 | n/a | 65.1710 |
| 2 | 22208 | n/a | 46.1041 |
| 3 | 21821 | n/a | 26.1295 |
| 4 | 21893 | n/a | 26.0649 |
| 5 | 21822 | n/a | 4.1340 |

Chunk rank 1:

```text
Question anchor: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Case scope id: multi-document-040. Scoped answer summary for multi-document-040 repeats the grounded evidence set: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-birch-ferry-shed-memory-log-040::multi-document-040::1: In document multi-birch-ferry-shed-memory-log-040, the verified archive note records paper moon mask. Case record id: multi-document-040. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-memory-log-040. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).

document multi-mira-audio-transcript-040::multi-document-040

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Case scope id: multi-document-040. Combined evidence: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-birch-ferry-shed-memory-log-040::multi-document-040::1: In document multi-birch-ferry-shed-memory-log-040, the verified archive note records paper moon mask. Case record id: multi-document-040. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-memory-log-040. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).
```

Chunk rank 4:

```text
document multi-mira-audio-transcript-040::multi-document-040::2: In document multi-mira-audio-transcript-040, the verified archive note records juniper bundles. Case record id: multi-document-040. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-mira-audio-transcript-040. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

Chunk rank 5:

```text
document multi-birch-ferry-shed-memory-log-100::multi-document-100::1: In document multi-birch-ferry-shed-memory-log-100, the verified archive note records linen wick. Case record id: multi-document-100. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-memory-log-100. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

## Question 041: multi-document-041

**Question:** Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard?

**Expected evidence:**
- marker `Bellwater Fair`
- aliases `festival Bellwater Fair, the Bellwater Fair record`
- marker `lantern hook`
- aliases `preserved item lantern hook, lantern hook in the preserved record`
- marker `carved shell comb`
- aliases `corroborating item carved shell comb, carved shell comb in the second document`

**Forbidden evidence:**
- marker `tuning fork`
- aliases `irrelevant document detail tuning fork`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Bellwater Fair, carved shell comb, lantern hook`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22209 | n/a | 77.7013 |
| 2 | 22210 | n/a | 58.5930 |
| 3 | 21811 | n/a | 30.5274 |
| 4 | 21938 | n/a | 26.7461 |
| 5 | 21995 | n/a | 14.0756 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Case scope id: multi-document-041. Scoped answer summary for multi-document-041 repeats the grounded evidence set: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-family-register-041::multi-document-041::3: In document multi-bellwater-fair-family-register-041, the verified archive note records carved shell comb. Case record id: multi-document-041. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Scope reminder: document multi-bellwater-fair-family-register-041. Alias reminders for retrieval: carved shell comb (al

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Case scope id: multi-document-041. Combined evidence: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-bellwater-fair-family-register-041::multi-document-041::3: In document multi-bellwater-fair-family-register-041, the verified archive note records carved shell comb. Case record id: multi-document-041. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Scope reminder: document multi-bellwater-fair-family-register-041. Alias reminders for retrieval: carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document).
```

Chunk rank 4:

```text
document multi-pine-gate-yard-travel-note-041::multi-document-041::1: In document multi-pine-gate-yard-travel-note-041, the verified archive note records Bellwater Fair. Case record id: multi-document-041. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Scope reminder: document multi-pine-gate-yard-travel-note-041. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

Chunk rank 5:

```text
document multi-watchtower-landing-ledger-061::multi-document-061::1: In document multi-watchtower-landing-ledger-061, the verified archive note records Bellwater Fair. Case record id: multi-document-061. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing? Scope reminder: document multi-watchtower-landing-ledger-061. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Bellwater Fair, carved shell comb, lantern hook`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22209 | n/a | 77.5062 |
| 2 | 22210 | n/a | 58.4936 |
| 3 | 21811 | n/a | 30.3990 |
| 4 | 21938 | n/a | 26.5020 |
| 5 | 22170 | n/a | 1.9700 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Case scope id: multi-document-041. Scoped answer summary for multi-document-041 repeats the grounded evidence set: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-family-register-041::multi-document-041::3: In document multi-bellwater-fair-family-register-041, the verified archive note records carved shell comb. Case record id: multi-document-041. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Scope reminder: document multi-bellwater-fair-family-register-041. Alias reminders for retrieval: carved shell comb (al

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Case scope id: multi-document-041. Combined evidence: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-bellwater-fair-family-register-041::multi-document-041::3: In document multi-bellwater-fair-family-register-041, the verified archive note records carved shell comb. Case record id: multi-document-041. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Scope reminder: document multi-bellwater-fair-family-register-041. Alias reminders for retrieval: carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document).
```

Chunk rank 4:

```text
document multi-pine-gate-yard-travel-note-041::multi-document-041::1: In document multi-pine-gate-yard-travel-note-041, the verified archive note records Bellwater Fair. Case record id: multi-document-041. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Scope reminder: document multi-pine-gate-yard-travel-note-041. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

Chunk rank 5:

```text
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-document-021. Combined evidence: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 042: multi-document-042

**Question:** Which archive pieces from more than one document explain the family profile event at North Bell workshop?

**Expected evidence:**
- marker `clay watering cup`
- aliases `archive piece clay watering cup, clay watering cup in the first archive piece`
- marker `canal route map`
- aliases `second archive piece canal route map, canal route map in the second archive piece`

**Forbidden evidence:**
- marker `willow basket`
- aliases `irrelevant document detail willow basket`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `clay watering cup, canal route map`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: clay watering cup, canal route map; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 60 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `canal route map, clay watering cup`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22211 | n/a | 65.5343 |
| 2 | 22212 | n/a | 46.3987 |
| 3 | 21929 | n/a | 26.5176 |
| 4 | 21925 | n/a | 26.4461 |
| 5 | 21808 | n/a | 2.1105 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at North Bell workshop? Case scope id: multi-document-042. Scoped answer summary for multi-document-042 repeats the grounded evidence set: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece); canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-nadia-repair-book-042::multi-document-042::2: In document multi-nadia-repair-book-042, the verified archive note records canal route map. Case record id: multi-document-042. Question: Which archive pieces from more than one document explain the family profile event at North Bell workshop? Scope reminder: document multi-nadia-repair-book-042. Alias reminders for retrieval: canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece).

document multi-nort

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at North Bell workshop? Case scope id: multi-document-042. Combined evidence: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece); canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-north-bell-workshop-photo-index-042::multi-document-042::1: In document multi-north-bell-workshop-photo-index-042, the verified archive note records clay watering cup. Case record id: multi-document-042. Question: Which archive pieces from more than one document explain the family profile event at North Bell workshop? Scope reminder: document multi-north-bell-workshop-photo-index-042. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece).
```

Chunk rank 4:

```text
document multi-nadia-repair-book-042::multi-document-042::2: In document multi-nadia-repair-book-042, the verified archive note records canal route map. Case record id: multi-document-042. Question: Which archive pieces from more than one document explain the family profile event at North Bell workshop? Scope reminder: document multi-nadia-repair-book-042. Alias reminders for retrieval: canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece).
```

Chunk rank 5:

```text
document multi-bell-bridge-square-photo-index-030::multi-document-030::1: In document multi-bell-bridge-square-photo-index-030, the verified archive note records wax thread. Case record id: multi-document-030. Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Scope reminder: document multi-bell-bridge-square-photo-index-030. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

## Question 043: multi-document-043

**Question:** Which documents must be combined to understand Anya's holiday card note about Fog Island pier?

**Expected evidence:**
- marker `saffron scarf`
- aliases `combined note saffron scarf, saffron scarf in one required document`
- marker `coal stove hiss`
- aliases `combined note coal stove hiss, coal stove hiss in another required document`
- marker `copper token`
- aliases `combined note copper token, copper token only visible after combining documents`

**Forbidden evidence:**
- marker `star ledger page`
- aliases `irrelevant document detail star ledger page`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, copper token, saffron scarf`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22213 | n/a | 77.4235 |
| 2 | 22214 | n/a | 58.2211 |
| 3 | 21838 | n/a | 26.3791 |
| 4 | 21800 | n/a | 26.2593 |
| 5 | 21909 | n/a | 26.2168 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Case scope id: multi-document-043. Scoped answer summary for multi-document-043 repeats the grounded evidence set: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-inventory-sheet-043::multi-document-043::2: In document multi-anya-inventory-sheet-043, the verified archive note records coal stove hiss. Case record id: multi-document-043. Question: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Scope reminder: document multi-anya-inventory-sheet-043. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; c

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Case scope id: multi-document-043. Combined evidence: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-fog-island-pier-audio-transcript-043::multi-document-043::1: In document multi-fog-island-pier-audio-transcript-043, the verified archive note records saffron scarf. Case record id: multi-document-043. Question: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Scope reminder: document multi-fog-island-pier-audio-transcript-043. Alias reminders for retrieval: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document).
```

Chunk rank 4:

```text
document multi-anya-inventory-sheet-043::multi-document-043::2: In document multi-anya-inventory-sheet-043, the verified archive note records coal stove hiss. Case record id: multi-document-043. Question: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Scope reminder: document multi-anya-inventory-sheet-043. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document).
```

Chunk rank 5:

```text
document multi-moon-orchard-rest-ledger-043::multi-document-043::3: In document multi-moon-orchard-rest-ledger-043, the verified archive note records copper token. Case record id: multi-document-043. Question: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Scope reminder: document multi-moon-orchard-rest-ledger-043. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token only visible after combining documents).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, copper token, saffron scarf`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22213 | n/a | 77.2137 |
| 2 | 22214 | n/a | 58.1575 |
| 3 | 21838 | n/a | 26.2590 |
| 4 | 21800 | n/a | 26.0907 |
| 5 | 21909 | n/a | 26.0669 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Case scope id: multi-document-043. Scoped answer summary for multi-document-043 repeats the grounded evidence set: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-inventory-sheet-043::multi-document-043::2: In document multi-anya-inventory-sheet-043, the verified archive note records coal stove hiss. Case record id: multi-document-043. Question: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Scope reminder: document multi-anya-inventory-sheet-043. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; c

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Case scope id: multi-document-043. Combined evidence: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-fog-island-pier-audio-transcript-043::multi-document-043::1: In document multi-fog-island-pier-audio-transcript-043, the verified archive note records saffron scarf. Case record id: multi-document-043. Question: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Scope reminder: document multi-fog-island-pier-audio-transcript-043. Alias reminders for retrieval: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document).
```

Chunk rank 4:

```text
document multi-anya-inventory-sheet-043::multi-document-043::2: In document multi-anya-inventory-sheet-043, the verified archive note records coal stove hiss. Case record id: multi-document-043. Question: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Scope reminder: document multi-anya-inventory-sheet-043. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document).
```

Chunk rank 5:

```text
document multi-moon-orchard-rest-ledger-043::multi-document-043::3: In document multi-moon-orchard-rest-ledger-043, the verified archive note records copper token. Case record id: multi-document-043. Question: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Scope reminder: document multi-moon-orchard-rest-ledger-043. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token only visible after combining documents).
```

## Question 044: multi-document-044

**Question:** Which records together show how Yara prepared the canal barge stop near Moon Mill yard?

**Expected evidence:**
- marker `blue glass jar`
- aliases `travel record blue glass jar, blue glass jar in one document`
- marker `tin key`
- aliases `supporting record tin key, tin key in another document`

**Forbidden evidence:**
- marker `silver booth token`
- aliases `irrelevant document detail silver booth token`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue glass jar, tin key`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22215 | n/a | 65.3544 |
| 2 | 22005 | n/a | 26.3456 |
| 3 | 21903 | n/a | 26.2619 |
| 4 | 22009 | n/a | 1.8921 |
| 5 | 21825 | n/a | 1.7604 |

Chunk rank 1:

```text
Question anchor: Which records together show how Yara prepared the canal barge stop near Moon Mill yard? Case scope id: multi-document-044. Scoped answer summary for multi-document-044 repeats the grounded evidence set: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-moon-mill-yard-letter-roll-044::multi-document-044::1: In document multi-moon-mill-yard-letter-roll-044, the verified archive note records blue glass jar. Case record id: multi-document-044. Question: Which records together show how Yara prepared the canal barge stop near Moon Mill yard? Scope reminder: document multi-moon-mill-yard-letter-roll-044. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).

document multi-yara-family-register-044::multi-document-044::2: In document multi-yara-family-register-044

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-yara-family-register-044::multi-document-044::2: In document multi-yara-family-register-044, the verified archive note records tin key. Case record id: multi-document-044. Question: Which records together show how Yara prepared the canal barge stop near Moon Mill yard? Scope reminder: document multi-yara-family-register-044. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 3:

```text
document multi-moon-mill-yard-letter-roll-044::multi-document-044::1: In document multi-moon-mill-yard-letter-roll-044, the verified archive note records blue glass jar. Case record id: multi-document-044. Question: Which records together show how Yara prepared the canal barge stop near Moon Mill yard? Scope reminder: document multi-moon-mill-yard-letter-roll-044. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

Chunk rank 4:

```text
document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-yara-profile-page-084. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 5:

```text
document multi-blue-trunk-cabin-memory-log-064::multi-document-064::1: In document multi-blue-trunk-cabin-memory-log-064, the verified archive note records amber lantern. Case record id: multi-document-064. Question: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin? Scope reminder: document multi-blue-trunk-cabin-memory-log-064. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue glass jar, tin key`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22215 | n/a | 65.2697 |
| 2 | 22216 | n/a | 46.2175 |
| 3 | 21903 | n/a | 26.2698 |
| 4 | 22005 | n/a | 26.1547 |
| 5 | 22008 | n/a | 1.6712 |

Chunk rank 1:

```text
Question anchor: Which records together show how Yara prepared the canal barge stop near Moon Mill yard? Case scope id: multi-document-044. Scoped answer summary for multi-document-044 repeats the grounded evidence set: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-moon-mill-yard-letter-roll-044::multi-document-044::1: In document multi-moon-mill-yard-letter-roll-044, the verified archive note records blue glass jar. Case record id: multi-document-044. Question: Which records together show how Yara prepared the canal barge stop near Moon Mill yard? Scope reminder: document multi-moon-mill-yard-letter-roll-044. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).

document multi-yara-family-register-044::multi-document-044::2: In document multi-yara-family-register-044

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Yara prepared the canal barge stop near Moon Mill yard? Case scope id: multi-document-044. Combined evidence: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-moon-mill-yard-letter-roll-044::multi-document-044::1: In document multi-moon-mill-yard-letter-roll-044, the verified archive note records blue glass jar. Case record id: multi-document-044. Question: Which records together show how Yara prepared the canal barge stop near Moon Mill yard? Scope reminder: document multi-moon-mill-yard-letter-roll-044. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

Chunk rank 4:

```text
document multi-yara-family-register-044::multi-document-044::2: In document multi-yara-family-register-044, the verified archive note records tin key. Case record id: multi-document-044. Question: Which records together show how Yara prepared the canal barge stop near Moon Mill yard? Scope reminder: document multi-yara-family-register-044. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 5:

```text
document multi-yara-profile-page-024::multi-document-024::2: In document multi-yara-profile-page-024, the verified archive note records juniper bundles. Case record id: multi-document-024. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-yara-profile-page-024. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

## Question 045: multi-document-045

**Question:** Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove?

**Expected evidence:**
- marker `Lantern Tide`
- aliases `festival Lantern Tide, the Lantern Tide record`
- marker `copper wind vane pin`
- aliases `preserved item copper wind vane pin, copper wind vane pin in the preserved record`
- marker `brass compass`
- aliases `corroborating item brass compass, brass compass in the second document`

**Forbidden evidence:**
- marker `birch tea flask`
- aliases `irrelevant document detail birch tea flask`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Tide, brass compass, copper wind vane pin`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22217 | n/a | 77.3655 |
| 2 | 21786 | n/a | 30.2909 |
| 3 | 21834 | n/a | 26.3963 |
| 4 | 21790 | n/a | 6.0196 |
| 5 | 21789 | n/a | 5.9845 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove? Case scope id: multi-document-045. Scoped answer summary for multi-document-045 repeats the grounded evidence set: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-archive-045::multi-document-045::2: In document multi-ada-archive-045, the verified archive note records copper wind vane pin. Case record id: multi-document-045. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove? Scope reminder: document multi-ada-archive-045. Alias reminders for retrieval: copper wind vane pin (aliases: preserved item copper wind vane pin; copper

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-ada-archive-045::multi-document-045::2: In document multi-ada-archive-045, the verified archive note records copper wind vane pin. Case record id: multi-document-045. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove? Scope reminder: document multi-ada-archive-045. Alias reminders for retrieval: copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record).
```

Chunk rank 3:

```text
document multi-driftwood-cove-repair-book-045::multi-document-045::1: In document multi-driftwood-cove-repair-book-045, the verified archive note records Lantern Tide. Case record id: multi-document-045. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove? Scope reminder: document multi-driftwood-cove-repair-book-045. Alias reminders for retrieval: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record).
```

Chunk rank 4:

```text
document multi-ada-memory-log-085::multi-document-085::2: In document multi-ada-memory-log-085, the verified archive note records green apron. Case record id: multi-document-085. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-ada-memory-log-085. Alias reminders for retrieval: green apron (aliases: preserved item green apron; green apron in the preserved record).
```

Chunk rank 5:

```text
document multi-ada-memory-log-025::multi-document-025::2: In document multi-ada-memory-log-025, the verified archive note records lantern hook. Case record id: multi-document-025. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-ada-memory-log-025. Alias reminders for retrieval: lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Tide, brass compass, copper wind vane pin`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22217 | n/a | 77.2891 |
| 2 | 22218 | n/a | 58.2261 |
| 3 | 21786 | n/a | 30.1923 |
| 4 | 21834 | n/a | 26.3030 |
| 5 | 21790 | n/a | 5.8879 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove? Case scope id: multi-document-045. Scoped answer summary for multi-document-045 repeats the grounded evidence set: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-archive-045::multi-document-045::2: In document multi-ada-archive-045, the verified archive note records copper wind vane pin. Case record id: multi-document-045. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove? Scope reminder: document multi-ada-archive-045. Alias reminders for retrieval: copper wind vane pin (aliases: preserved item copper wind vane pin; copper

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove? Case scope id: multi-document-045. Combined evidence: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ada-archive-045::multi-document-045::2: In document multi-ada-archive-045, the verified archive note records copper wind vane pin. Case record id: multi-document-045. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove? Scope reminder: document multi-ada-archive-045. Alias reminders for retrieval: copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record).
```

Chunk rank 4:

```text
document multi-driftwood-cove-repair-book-045::multi-document-045::1: In document multi-driftwood-cove-repair-book-045, the verified archive note records Lantern Tide. Case record id: multi-document-045. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove? Scope reminder: document multi-driftwood-cove-repair-book-045. Alias reminders for retrieval: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record).
```

Chunk rank 5:

```text
document multi-ada-memory-log-085::multi-document-085::2: In document multi-ada-memory-log-085, the verified archive note records green apron. Case record id: multi-document-085. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-ada-memory-log-085. Alias reminders for retrieval: green apron (aliases: preserved item green apron; green apron in the preserved record).
```

## Question 046: multi-document-046

**Question:** Which archive pieces from more than one document explain the family profile event at Ridge Post loft?

**Expected evidence:**
- marker `wax thread`
- aliases `archive piece wax thread, wax thread in the first archive piece`
- marker `basalt sketch`
- aliases `second archive piece basalt sketch, basalt sketch in the second archive piece`

**Forbidden evidence:**
- marker `oak barrel hoops`
- aliases `irrelevant document detail oak barrel hoops`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `basalt sketch, wax thread`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22219 | n/a | 65.6158 |
| 2 | 22220 | n/a | 46.4540 |
| 3 | 21939 | n/a | 26.5875 |
| 4 | 21971 | n/a | 26.3489 |
| 5 | 22315 | n/a | 3.8551 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Ridge Post loft? Case scope id: multi-document-046. Scoped answer summary for multi-document-046 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ridge-post-loft-inventory-sheet-046::multi-document-046::1: In document multi-ridge-post-loft-inventory-sheet-046, the verified archive note records wax thread. Case record id: multi-document-046. Question: Which archive pieces from more than one document explain the family profile event at Ridge Post loft? Scope reminder: document multi-ridge-post-loft-inventory-sheet-046. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).

document multi-sonya-ledger-046::multi-d

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Ridge Post loft? Case scope id: multi-document-046. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ridge-post-loft-inventory-sheet-046::multi-document-046::1: In document multi-ridge-post-loft-inventory-sheet-046, the verified archive note records wax thread. Case record id: multi-document-046. Question: Which archive pieces from more than one document explain the family profile event at Ridge Post loft? Scope reminder: document multi-ridge-post-loft-inventory-sheet-046. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

Chunk rank 4:

```text
document multi-sonya-ledger-046::multi-document-046::2: In document multi-sonya-ledger-046, the verified archive note records basalt sketch. Case record id: multi-document-046. Question: Which archive pieces from more than one document explain the family profile event at Ridge Post loft? Scope reminder: document multi-sonya-ledger-046. Alias reminders for retrieval: basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece).
```

Chunk rank 5:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Scoped answer summary for multi-document-094 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-blue-trunk-cabin-inventory-sheet-094::multi-document-094::1: In document multi-blue-trunk-cabin-inventory-sheet-094, the verified archive note records wax thread. Case record id: multi-document-094. Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Scope reminder: document multi-blue-trunk-cabin-inventory-sheet-094. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).

document multi-yara-ledger-094::mul

[truncated in Markdown; full text is available in JSON]
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `basalt sketch, wax thread`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22219 | n/a | 65.5410 |
| 2 | 22220 | n/a | 46.4711 |
| 3 | 21939 | n/a | 26.5428 |
| 4 | 21971 | n/a | 26.3809 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Ridge Post loft? Case scope id: multi-document-046. Scoped answer summary for multi-document-046 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ridge-post-loft-inventory-sheet-046::multi-document-046::1: In document multi-ridge-post-loft-inventory-sheet-046, the verified archive note records wax thread. Case record id: multi-document-046. Question: Which archive pieces from more than one document explain the family profile event at Ridge Post loft? Scope reminder: document multi-ridge-post-loft-inventory-sheet-046. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).

document multi-sonya-ledger-046::multi-d

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Ridge Post loft? Case scope id: multi-document-046. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ridge-post-loft-inventory-sheet-046::multi-document-046::1: In document multi-ridge-post-loft-inventory-sheet-046, the verified archive note records wax thread. Case record id: multi-document-046. Question: Which archive pieces from more than one document explain the family profile event at Ridge Post loft? Scope reminder: document multi-ridge-post-loft-inventory-sheet-046. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

Chunk rank 4:

```text
document multi-sonya-ledger-046::multi-document-046::2: In document multi-sonya-ledger-046, the verified archive note records basalt sketch. Case record id: multi-document-046. Question: Which archive pieces from more than one document explain the family profile event at Ridge Post loft? Scope reminder: document multi-sonya-ledger-046. Alias reminders for retrieval: basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece).
```

## Question 047: multi-document-047

**Question:** Which documents must be combined to understand Runa's boat manifest note about East Signal room?

**Expected evidence:**
- marker `smoke vent chain`
- aliases `combined note smoke vent chain, smoke vent chain in one required document`
- marker `copper token`
- aliases `combined note copper token, copper token in another required document`
- marker `silver booth token`
- aliases `combined note silver booth token, silver booth token only visible after combining documents`

**Forbidden evidence:**
- marker `glass ink bottle`
- aliases `irrelevant document detail glass ink bottle`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `copper token, silver booth token, smoke vent chain`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22221 | n/a | 77.4561 |
| 2 | 22222 | n/a | 58.2730 |
| 3 | 21952 | n/a | 26.3659 |
| 4 | 21835 | n/a | 26.3353 |
| 5 | 21861 | n/a | 26.3298 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Case scope id: multi-document-047. Scoped answer summary for multi-document-047 repeats the grounded evidence set: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-east-signal-room-family-register-047::multi-document-047::1: In document multi-east-signal-room-family-register-047, the verified archive note records smoke vent chain. Case record id: multi-document-047. Question: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Scope reminder: document multi-east-signal-room-family-register-047. Alias reminders for retrieval:

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Case scope id: multi-document-047. Combined evidence: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-runa-minute-book-047::multi-document-047::2: In document multi-runa-minute-book-047, the verified archive note records copper token. Case record id: multi-document-047. Question: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Scope reminder: document multi-runa-minute-book-047. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token in another required document).
```

Chunk rank 4:

```text
document multi-east-signal-room-family-register-047::multi-document-047::1: In document multi-east-signal-room-family-register-047, the verified archive note records smoke vent chain. Case record id: multi-document-047. Question: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Scope reminder: document multi-east-signal-room-family-register-047. Alias reminders for retrieval: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document).
```

Chunk rank 5:

```text
document multi-harvest-glow-travel-note-047::multi-document-047::3: In document multi-harvest-glow-travel-note-047, the verified archive note records silver booth token. Case record id: multi-document-047. Question: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Scope reminder: document multi-harvest-glow-travel-note-047. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `copper token, silver booth token, smoke vent chain`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22221 | n/a | 77.3056 |
| 2 | 22222 | n/a | 58.2328 |
| 3 | 21835 | n/a | 26.3215 |
| 4 | 21861 | n/a | 26.2207 |
| 5 | 21952 | n/a | 26.1340 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Case scope id: multi-document-047. Scoped answer summary for multi-document-047 repeats the grounded evidence set: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-east-signal-room-family-register-047::multi-document-047::1: In document multi-east-signal-room-family-register-047, the verified archive note records smoke vent chain. Case record id: multi-document-047. Question: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Scope reminder: document multi-east-signal-room-family-register-047. Alias reminders for retrieval:

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Case scope id: multi-document-047. Combined evidence: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-east-signal-room-family-register-047::multi-document-047::1: In document multi-east-signal-room-family-register-047, the verified archive note records smoke vent chain. Case record id: multi-document-047. Question: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Scope reminder: document multi-east-signal-room-family-register-047. Alias reminders for retrieval: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document).
```

Chunk rank 4:

```text
document multi-harvest-glow-travel-note-047::multi-document-047::3: In document multi-harvest-glow-travel-note-047, the verified archive note records silver booth token. Case record id: multi-document-047. Question: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Scope reminder: document multi-harvest-glow-travel-note-047. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

Chunk rank 5:

```text
document multi-runa-minute-book-047::multi-document-047::2: In document multi-runa-minute-book-047, the verified archive note records copper token. Case record id: multi-document-047. Question: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Scope reminder: document multi-runa-minute-book-047. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token in another required document).
```

## Question 048: multi-document-048

**Question:** Which records together show how Iveta prepared the winter coach stop near South Meadow arch?

**Expected evidence:**
- marker `amber lantern`
- aliases `travel record amber lantern, amber lantern in one document`
- marker `tuning fork`
- aliases `supporting record tuning fork, tuning fork in another document`

**Forbidden evidence:**
- marker `weathered camera strap`
- aliases `irrelevant document detail weathered camera strap`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `amber lantern, tuning fork`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22223 | n/a | 65.5178 |
| 2 | 21978 | n/a | 26.6771 |
| 3 | 21870 | n/a | 26.3337 |
| 4 | 21868 | n/a | 1.8955 |
| 5 | 21980 | n/a | 1.1629 |

Chunk rank 1:

```text
Question anchor: Which records together show how Iveta prepared the winter coach stop near South Meadow arch? Case scope id: multi-document-048. Scoped answer summary for multi-document-048 repeats the grounded evidence set: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-profile-page-048::multi-document-048::2: In document multi-iveta-profile-page-048, the verified archive note records tuning fork. Case record id: multi-document-048. Question: Which records together show how Iveta prepared the winter coach stop near South Meadow arch? Scope reminder: document multi-iveta-profile-page-048. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).

document multi-south-meadow-arch-archive-048::multi-document-048::1: In document multi-south-meadow-arch-archive-04

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-south-meadow-arch-archive-048::multi-document-048::1: In document multi-south-meadow-arch-archive-048, the verified archive note records amber lantern. Case record id: multi-document-048. Question: Which records together show how Iveta prepared the winter coach stop near South Meadow arch? Scope reminder: document multi-south-meadow-arch-archive-048. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 3:

```text
document multi-iveta-profile-page-048::multi-document-048::2: In document multi-iveta-profile-page-048, the verified archive note records tuning fork. Case record id: multi-document-048. Question: Which records together show how Iveta prepared the winter coach stop near South Meadow arch? Scope reminder: document multi-iveta-profile-page-048. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

Chunk rank 4:

```text
document multi-iveta-family-register-068::multi-document-068::2: In document multi-iveta-family-register-068, the verified archive note records birch tea flask. Case record id: multi-document-068. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-iveta-family-register-068. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 5:

```text
document multi-south-meadow-arch-photo-index-078::multi-document-078::1: In document multi-south-meadow-arch-photo-index-078, the verified archive note records wax thread. Case record id: multi-document-078. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-south-meadow-arch-photo-index-078. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `amber lantern, tuning fork`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22223 | n/a | 65.3177 |
| 2 | 22224 | n/a | 46.2395 |
| 3 | 21978 | n/a | 26.3329 |
| 4 | 21870 | n/a | 26.1722 |
| 5 | 21866 | n/a | 1.6383 |

Chunk rank 1:

```text
Question anchor: Which records together show how Iveta prepared the winter coach stop near South Meadow arch? Case scope id: multi-document-048. Scoped answer summary for multi-document-048 repeats the grounded evidence set: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-profile-page-048::multi-document-048::2: In document multi-iveta-profile-page-048, the verified archive note records tuning fork. Case record id: multi-document-048. Question: Which records together show how Iveta prepared the winter coach stop near South Meadow arch? Scope reminder: document multi-iveta-profile-page-048. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).

document multi-south-meadow-arch-archive-048::multi-document-048::1: In document multi-south-meadow-arch-archive-04

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Iveta prepared the winter coach stop near South Meadow arch? Case scope id: multi-document-048. Combined evidence: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-south-meadow-arch-archive-048::multi-document-048::1: In document multi-south-meadow-arch-archive-048, the verified archive note records amber lantern. Case record id: multi-document-048. Question: Which records together show how Iveta prepared the winter coach stop near South Meadow arch? Scope reminder: document multi-south-meadow-arch-archive-048. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 4:

```text
document multi-iveta-profile-page-048::multi-document-048::2: In document multi-iveta-profile-page-048, the verified archive note records tuning fork. Case record id: multi-document-048. Question: Which records together show how Iveta prepared the winter coach stop near South Meadow arch? Scope reminder: document multi-iveta-profile-page-048. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

Chunk rank 5:

```text
document multi-iveta-audio-transcript-088::multi-document-088::2: In document multi-iveta-audio-transcript-088, the verified archive note records juniper bundles. Case record id: multi-document-088. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-iveta-audio-transcript-088. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

## Question 049: multi-document-049

**Question:** Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic?

**Expected evidence:**
- marker `Signal Lantern Morning`
- aliases `festival Signal Lantern Morning, the Signal Lantern Morning record`
- marker `cedar shovel`
- aliases `preserved item cedar shovel, cedar shovel in the preserved record`
- marker `willow basket`
- aliases `corroborating item willow basket, willow basket in the second document`

**Forbidden evidence:**
- marker `juniper bundles`
- aliases `irrelevant document detail juniper bundles`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning, cedar shovel, willow basket`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22225 | n/a | 77.5610 |
| 2 | 22226 | n/a | 58.5590 |
| 3 | 21955 | n/a | 30.4698 |
| 4 | 21889 | n/a | 26.5821 |
| 5 | 22266 | n/a | 2.1927 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic? Case scope id: multi-document-049. Scoped answer summary for multi-document-049 repeats the grounded evidence set: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-maple-court-attic-ledger-049::multi-document-049::1: In document multi-maple-court-attic-ledger-049, the verified archive note records Signal Lantern Morning. Case record id: multi-document-049. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic? Scope reminder: document multi-maple-court-attic-ledger-049. Alias reminders for retrieval:

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic? Case scope id: multi-document-049. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-signal-lantern-morning-audio-transcript-049::multi-document-049::3: In document multi-signal-lantern-morning-audio-transcript-049, the verified archive note records willow basket. Case record id: multi-document-049. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic? Scope reminder: document multi-signal-lantern-morning-audio-transcript-049. Alias reminders for retrieval: willow basket (aliases: corroborating item willow basket; willow basket in the second document).
```

Chunk rank 4:

```text
document multi-maple-court-attic-ledger-049::multi-document-049::1: In document multi-maple-court-attic-ledger-049, the verified archive note records Signal Lantern Morning. Case record id: multi-document-049. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic? Scope reminder: document multi-maple-court-attic-ledger-049. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

Chunk rank 5:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-document-069. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning, cedar shovel, willow basket`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22225 | n/a | 77.5694 |
| 2 | 22226 | n/a | 58.5359 |
| 3 | 22019 | n/a | 30.4429 |
| 4 | 21889 | n/a | 26.5828 |
| 5 | 22306 | n/a | 2.1151 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic? Case scope id: multi-document-049. Scoped answer summary for multi-document-049 repeats the grounded evidence set: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-maple-court-attic-ledger-049::multi-document-049::1: In document multi-maple-court-attic-ledger-049, the verified archive note records Signal Lantern Morning. Case record id: multi-document-049. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic? Scope reminder: document multi-maple-court-attic-ledger-049. Alias reminders for retrieval:

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic? Case scope id: multi-document-049. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-zora-memory-log-049::multi-document-049::2: In document multi-zora-memory-log-049, the verified archive note records cedar shovel. Case record id: multi-document-049. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic? Scope reminder: document multi-zora-memory-log-049. Alias reminders for retrieval: cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record).
```

Chunk rank 4:

```text
document multi-maple-court-attic-ledger-049::multi-document-049::1: In document multi-maple-court-attic-ledger-049, the verified archive note records Signal Lantern Morning. Case record id: multi-document-049. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic? Scope reminder: document multi-maple-court-attic-ledger-049. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

Chunk rank 5:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-document-089. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 050: multi-document-050

**Question:** Which archive pieces from more than one document explain the family profile event at Star Basin gallery?

**Expected evidence:**
- marker `violet ribbon`
- aliases `archive piece violet ribbon, violet ribbon in the first archive piece`
- marker `star ledger page`
- aliases `second archive piece star ledger page, star ledger page in the second archive piece`

**Forbidden evidence:**
- marker `carved shell comb`
- aliases `irrelevant document detail carved shell comb`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `star ledger page, violet ribbon`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22227 | n/a | 65.4991 |
| 2 | 22228 | n/a | 46.4770 |
| 3 | 21983 | n/a | 26.4664 |
| 4 | 22196 | n/a | 14.1073 |
| 5 | 22260 | n/a | 14.1029 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Star Basin gallery? Case scope id: multi-document-050. Scoped answer summary for multi-document-050 repeats the grounded evidence set: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-mira-travel-note-050::multi-document-050::2: In document multi-mira-travel-note-050, the verified archive note records star ledger page. Case record id: multi-document-050. Question: Which archive pieces from more than one document explain the family profile event at Star Basin gallery? Scope reminder: document multi-mira-travel-note-050. Alias reminders for retrieval: star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece).

document multi-star-basin-gal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Star Basin gallery? Case scope id: multi-document-050. Combined evidence: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-star-basin-gallery-minute-book-050::multi-document-050::1: In document multi-star-basin-gallery-minute-book-050, the verified archive note records violet ribbon. Case record id: multi-document-050. Question: Which archive pieces from more than one document explain the family profile event at Star Basin gallery? Scope reminder: document multi-star-basin-gallery-minute-book-050. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

Chunk rank 4:

```text
Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-034. Combined evidence: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 5:

```text
Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-066. Combined evidence: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `star ledger page, violet ribbon`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22227 | n/a | 65.4785 |
| 2 | 22228 | n/a | 46.4312 |
| 3 | 21983 | n/a | 26.4987 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Star Basin gallery? Case scope id: multi-document-050. Scoped answer summary for multi-document-050 repeats the grounded evidence set: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-mira-travel-note-050::multi-document-050::2: In document multi-mira-travel-note-050, the verified archive note records star ledger page. Case record id: multi-document-050. Question: Which archive pieces from more than one document explain the family profile event at Star Basin gallery? Scope reminder: document multi-mira-travel-note-050. Alias reminders for retrieval: star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece).

document multi-star-basin-gal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Star Basin gallery? Case scope id: multi-document-050. Combined evidence: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-star-basin-gallery-minute-book-050::multi-document-050::1: In document multi-star-basin-gallery-minute-book-050, the verified archive note records violet ribbon. Case record id: multi-document-050. Question: Which archive pieces from more than one document explain the family profile event at Star Basin gallery? Scope reminder: document multi-star-basin-gallery-minute-book-050. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

## Question 051: multi-document-051

**Question:** Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse?

**Expected evidence:**
- marker `blue oar`
- aliases `combined note blue oar, blue oar in one required document`
- marker `silver booth token`
- aliases `combined note silver booth token, silver booth token in another required document`
- marker `weathered camera strap`
- aliases `combined note weathered camera strap, weathered camera strap only visible after combining documents`

**Forbidden evidence:**
- marker `canal route map`
- aliases `irrelevant document detail canal route map`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue oar, silver booth token, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22229 | n/a | 77.3133 |
| 2 | 22230 | n/a | 58.2924 |
| 3 | 21965 | n/a | 26.3500 |
| 4 | 21959 | n/a | 9.7145 |
| 5 | 21812 | n/a | 9.6110 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse? Case scope id: multi-document-051. Scoped answer summary for multi-document-051 repeats the grounded evidence set: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-repair-book-051::multi-document-051::3: In document multi-bellwater-fair-repair-book-051, the verified archive note records weathered camera strap. Case record id: multi-document-051. Question: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse? Scope reminder: document multi-bellwater-fair-repair-book-051. Alias reminders for re

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse? Case scope id: multi-document-051. Combined evidence: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-snow-orchard-storehouse-profile-page-051::multi-document-051::1: In document multi-snow-orchard-storehouse-profile-page-051, the verified archive note records blue oar. Case record id: multi-document-051. Question: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse? Scope reminder: document multi-snow-orchard-storehouse-profile-page-051. Alias reminders for retrieval: blue oar (aliases: combined note blue oar; blue oar in one required document).
```

Chunk rank 4:

```text
document multi-signal-lantern-morning-ledger-079::multi-document-079::3: In document multi-signal-lantern-morning-ledger-079, the verified archive note records silver booth token. Case record id: multi-document-079. Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Scope reminder: document multi-signal-lantern-morning-ledger-079. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

Chunk rank 5:

```text
document multi-bellwater-fair-ledger-031::multi-document-031::3: In document multi-bellwater-fair-ledger-031, the verified archive note records silver booth token. Case record id: multi-document-031. Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Scope reminder: document multi-bellwater-fair-ledger-031. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue oar, silver booth token, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22229 | n/a | 77.1980 |
| 2 | 22230 | n/a | 58.1754 |
| 3 | 21965 | n/a | 26.2043 |
| 4 | 21992 | n/a | 26.1177 |
| 5 | 21816 | n/a | 26.0757 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse? Case scope id: multi-document-051. Scoped answer summary for multi-document-051 repeats the grounded evidence set: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-repair-book-051::multi-document-051::3: In document multi-bellwater-fair-repair-book-051, the verified archive note records weathered camera strap. Case record id: multi-document-051. Question: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse? Scope reminder: document multi-bellwater-fair-repair-book-051. Alias reminders for re

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse? Case scope id: multi-document-051. Combined evidence: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-snow-orchard-storehouse-profile-page-051::multi-document-051::1: In document multi-snow-orchard-storehouse-profile-page-051, the verified archive note records blue oar. Case record id: multi-document-051. Question: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse? Scope reminder: document multi-snow-orchard-storehouse-profile-page-051. Alias reminders for retrieval: blue oar (aliases: combined note blue oar; blue oar in one required document).
```

Chunk rank 4:

```text
document multi-vera-photo-index-051::multi-document-051::2: In document multi-vera-photo-index-051, the verified archive note records silver booth token. Case record id: multi-document-051. Question: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse? Scope reminder: document multi-vera-photo-index-051. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token in another required document).
```

Chunk rank 5:

```text
document multi-bellwater-fair-repair-book-051::multi-document-051::3: In document multi-bellwater-fair-repair-book-051, the verified archive note records weathered camera strap. Case record id: multi-document-051. Question: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse? Scope reminder: document multi-bellwater-fair-repair-book-051. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents).
```

## Question 052: multi-document-052

**Question:** Which records together show how Nadia prepared the river skiff stop near Cedar Hill station?

**Expected evidence:**
- marker `linen wick`
- aliases `travel record linen wick, linen wick in one document`
- marker `birch tea flask`
- aliases `supporting record birch tea flask, birch tea flask in another document`

**Forbidden evidence:**
- marker `coal stove hiss`
- aliases `irrelevant document detail coal stove hiss`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `birch tea flask, linen wick`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22231 | n/a | 65.3398 |
| 2 | 21828 | n/a | 26.2950 |
| 3 | 21918 | n/a | 26.2901 |
| 4 | 22295 | n/a | 3.2734 |
| 5 | 21920 | n/a | 1.8129 |

Chunk rank 1:

```text
Question anchor: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Case scope id: multi-document-052. Scoped answer summary for multi-document-052 repeats the grounded evidence set: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-cedar-hill-station-memory-log-052::multi-document-052::1: In document multi-cedar-hill-station-memory-log-052, the verified archive note records linen wick. Case record id: multi-document-052. Question: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Scope reminder: document multi-cedar-hill-station-memory-log-052. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).

document multi-nadia-audio-transcript-052::multi-document-052::2: In document multi-nadia-a

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-cedar-hill-station-memory-log-052::multi-document-052::1: In document multi-cedar-hill-station-memory-log-052, the verified archive note records linen wick. Case record id: multi-document-052. Question: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Scope reminder: document multi-cedar-hill-station-memory-log-052. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 3:

```text
document multi-nadia-audio-transcript-052::multi-document-052::2: In document multi-nadia-audio-transcript-052, the verified archive note records birch tea flask. Case record id: multi-document-052. Question: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Scope reminder: document multi-nadia-audio-transcript-052. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 4:

```text
Question anchor: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-084. Scoped answer summary for multi-document-084 repeats the grounded evidence set: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records linen wick. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-084. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).

document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084,

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-family-register-092, the verified archive note records tin key. Case record id: multi-document-092. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-nadia-family-register-092. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `birch tea flask, linen wick`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22231 | n/a | 65.1967 |
| 2 | 22232 | n/a | 46.1620 |
| 3 | 21828 | n/a | 26.1671 |
| 4 | 21918 | n/a | 26.1318 |

Chunk rank 1:

```text
Question anchor: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Case scope id: multi-document-052. Scoped answer summary for multi-document-052 repeats the grounded evidence set: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-cedar-hill-station-memory-log-052::multi-document-052::1: In document multi-cedar-hill-station-memory-log-052, the verified archive note records linen wick. Case record id: multi-document-052. Question: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Scope reminder: document multi-cedar-hill-station-memory-log-052. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).

document multi-nadia-audio-transcript-052::multi-document-052::2: In document multi-nadia-a

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Case scope id: multi-document-052. Combined evidence: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-cedar-hill-station-memory-log-052::multi-document-052::1: In document multi-cedar-hill-station-memory-log-052, the verified archive note records linen wick. Case record id: multi-document-052. Question: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Scope reminder: document multi-cedar-hill-station-memory-log-052. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 4:

```text
document multi-nadia-audio-transcript-052::multi-document-052::2: In document multi-nadia-audio-transcript-052, the verified archive note records birch tea flask. Case record id: multi-document-052. Question: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Scope reminder: document multi-nadia-audio-transcript-052. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

## Question 053: multi-document-053

**Question:** Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path?

**Expected evidence:**
- marker `Moon Orchard Rest`
- aliases `festival Moon Orchard Rest, the Moon Orchard Rest record`
- marker `green apron`
- aliases `preserved item green apron, green apron in the preserved record`
- marker `oak barrel hoops`
- aliases `corroborating item oak barrel hoops, oak barrel hoops in the second document`

**Forbidden evidence:**
- marker `tin key`
- aliases `irrelevant document detail tin key`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Orchard Rest, green apron, oak barrel hoops`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22233 | n/a | 77.7943 |
| 2 | 22234 | n/a | 58.6128 |
| 3 | 21908 | n/a | 30.7559 |
| 4 | 21801 | n/a | 30.5462 |
| 5 | 21935 | n/a | 26.8412 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Case scope id: multi-document-053. Scoped answer summary for multi-document-053 repeats the grounded evidence set: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-letter-roll-053::multi-document-053::2: In document multi-anya-letter-roll-053, the verified archive note records green apron. Case record id: multi-document-053. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Scope reminder: document multi-anya-letter-roll-053. Alias reminders for retrieval: green apron (aliases: preserved item green apron; green ap

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Case scope id: multi-document-053. Combined evidence: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-moon-orchard-rest-family-register-053::multi-document-053::3: In document multi-moon-orchard-rest-family-register-053, the verified archive note records oak barrel hoops. Case record id: multi-document-053. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Scope reminder: document multi-moon-orchard-rest-family-register-053. Alias reminders for retrieval: oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document).
```

Chunk rank 4:

```text
document multi-anya-letter-roll-053::multi-document-053::2: In document multi-anya-letter-roll-053, the verified archive note records green apron. Case record id: multi-document-053. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Scope reminder: document multi-anya-letter-roll-053. Alias reminders for retrieval: green apron (aliases: preserved item green apron; green apron in the preserved record).
```

Chunk rank 5:

```text
document multi-old-quarry-path-travel-note-053::multi-document-053::1: In document multi-old-quarry-path-travel-note-053, the verified archive note records Moon Orchard Rest. Case record id: multi-document-053. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Scope reminder: document multi-old-quarry-path-travel-note-053. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Orchard Rest, green apron, oak barrel hoops`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22233 | n/a | 77.6133 |
| 2 | 22234 | n/a | 58.6196 |
| 3 | 21935 | n/a | 26.6263 |
| 4 | 22274 | n/a | 2.2338 |
| 5 | 22194 | n/a | 2.2119 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Case scope id: multi-document-053. Scoped answer summary for multi-document-053 repeats the grounded evidence set: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-letter-roll-053::multi-document-053::2: In document multi-anya-letter-roll-053, the verified archive note records green apron. Case record id: multi-document-053. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Scope reminder: document multi-anya-letter-roll-053. Alias reminders for retrieval: green apron (aliases: preserved item green apron; green ap

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Case scope id: multi-document-053. Combined evidence: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-old-quarry-path-travel-note-053::multi-document-053::1: In document multi-old-quarry-path-travel-note-053, the verified archive note records Moon Orchard Rest. Case record id: multi-document-053. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Scope reminder: document multi-old-quarry-path-travel-note-053. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 4:

```text
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-document-073. Combined evidence: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 5:

```text
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-document-033. Combined evidence: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 054: multi-document-054

**Question:** Which archive pieces from more than one document explain the family profile event at Cloud Wharf office?

**Expected evidence:**
- marker `moonflower cutting`
- aliases `archive piece moonflower cutting, moonflower cutting in the first archive piece`
- marker `glass ink bottle`
- aliases `second archive piece glass ink bottle, glass ink bottle in the second archive piece`

**Forbidden evidence:**
- marker `brass compass`
- aliases `irrelevant document detail brass compass`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `glass ink bottle, moonflower cutting`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22235 | n/a | 65.5109 |
| 2 | 22236 | n/a | 46.4471 |
| 3 | 21831 | n/a | 26.5374 |
| 4 | 21829 | n/a | 1.3781 |
| 5 | 21830 | n/a | 1.3344 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office? Case scope id: multi-document-054. Scoped answer summary for multi-document-054 repeats the grounded evidence set: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-cloud-wharf-office-photo-index-054::multi-document-054::1: In document multi-cloud-wharf-office-photo-index-054, the verified archive note records moonflower cutting. Case record id: multi-document-054. Question: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-photo-index-054. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office? Case scope id: multi-document-054. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-cloud-wharf-office-photo-index-054::multi-document-054::1: In document multi-cloud-wharf-office-photo-index-054, the verified archive note records moonflower cutting. Case record id: multi-document-054. Question: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-photo-index-054. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

Chunk rank 4:

```text
document multi-cloud-wharf-office-archive-024::multi-document-024::1: In document multi-cloud-wharf-office-archive-024, the verified archive note records paper moon mask. Case record id: multi-document-024. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-024. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).
```

Chunk rank 5:

```text
document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records linen wick. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-084. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `glass ink bottle, moonflower cutting`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22235 | n/a | 65.4771 |
| 2 | 22236 | n/a | 46.4634 |
| 3 | 21831 | n/a | 26.4337 |
| 4 | 22140 | n/a | 13.9316 |
| 5 | 22300 | n/a | 13.9279 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office? Case scope id: multi-document-054. Scoped answer summary for multi-document-054 repeats the grounded evidence set: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-cloud-wharf-office-photo-index-054::multi-document-054::1: In document multi-cloud-wharf-office-photo-index-054, the verified archive note records moonflower cutting. Case record id: multi-document-054. Question: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-photo-index-054. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office? Case scope id: multi-document-054. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-cloud-wharf-office-photo-index-054::multi-document-054::1: In document multi-cloud-wharf-office-photo-index-054, the verified archive note records moonflower cutting. Case record id: multi-document-054. Question: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-photo-index-054. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

Chunk rank 4:

```text
Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 5:

```text
Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 055: multi-document-055

**Question:** Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor?

**Expected evidence:**
- marker `rope bridge permit`
- aliases `combined note rope bridge permit, rope bridge permit in one required document`
- marker `weathered camera strap`
- aliases `combined note weathered camera strap, weathered camera strap in another required document`
- marker `coal stove hiss`
- aliases `combined note coal stove hiss, coal stove hiss only visible after combining documents`

**Forbidden evidence:**
- marker `basalt sketch`
- aliases `irrelevant document detail basalt sketch`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, rope bridge permit, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22237 | n/a | 77.4014 |
| 2 | 22238 | n/a | 58.2789 |
| 3 | 21787 | n/a | 26.3217 |
| 4 | 21849 | n/a | 26.2975 |
| 5 | 21791 | n/a | 1.6441 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Case scope id: multi-document-055. Scoped answer summary for multi-document-055 repeats the grounded evidence set: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-inventory-sheet-055::multi-document-055::2: In document multi-ada-inventory-sheet-055, the verified archive note records weathered camera strap. Case record id: multi-document-055. Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Scope reminder: document multi-ada-inventory-sheet-055. Alias reminders for

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Case scope id: multi-document-055. Combined evidence: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ada-inventory-sheet-055::multi-document-055::2: In document multi-ada-inventory-sheet-055, the verified archive note records weathered camera strap. Case record id: multi-document-055. Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Scope reminder: document multi-ada-inventory-sheet-055. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document).
```

Chunk rank 4:

```text
document multi-harbor-glass-corridor-audio-transcript-055::multi-document-055::1: In document multi-harbor-glass-corridor-audio-transcript-055, the verified archive note records rope bridge permit. Case record id: multi-document-055. Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Scope reminder: document multi-harbor-glass-corridor-audio-transcript-055. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 5:

```text
document multi-ada-minute-book-035::multi-document-035::2: In document multi-ada-minute-book-035, the verified archive note records silver booth token. Case record id: multi-document-035. Question: Which documents must be combined to understand Ada's family note note about River Lantern inn? Scope reminder: document multi-ada-minute-book-035. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token in another required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, rope bridge permit, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22237 | n/a | 77.2669 |
| 2 | 22238 | n/a | 58.1589 |
| 3 | 21849 | n/a | 26.2844 |
| 4 | 21881 | n/a | 26.1371 |
| 5 | 21787 | n/a | 26.1366 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Case scope id: multi-document-055. Scoped answer summary for multi-document-055 repeats the grounded evidence set: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-inventory-sheet-055::multi-document-055::2: In document multi-ada-inventory-sheet-055, the verified archive note records weathered camera strap. Case record id: multi-document-055. Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Scope reminder: document multi-ada-inventory-sheet-055. Alias reminders for

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Case scope id: multi-document-055. Combined evidence: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-harbor-glass-corridor-audio-transcript-055::multi-document-055::1: In document multi-harbor-glass-corridor-audio-transcript-055, the verified archive note records rope bridge permit. Case record id: multi-document-055. Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Scope reminder: document multi-harbor-glass-corridor-audio-transcript-055. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 4:

```text
document multi-lantern-tide-ledger-055::multi-document-055::3: In document multi-lantern-tide-ledger-055, the verified archive note records coal stove hiss. Case record id: multi-document-055. Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Scope reminder: document multi-lantern-tide-ledger-055. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents).
```

Chunk rank 5:

```text
document multi-ada-inventory-sheet-055::multi-document-055::2: In document multi-ada-inventory-sheet-055, the verified archive note records weathered camera strap. Case record id: multi-document-055. Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Scope reminder: document multi-ada-inventory-sheet-055. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document).
```

## Question 056: multi-document-056

**Question:** Which records together show how Sonya prepared the quarry lift stop near North Orchard lane?

**Expected evidence:**
- marker `paper moon mask`
- aliases `travel record paper moon mask, paper moon mask in one document`
- marker `juniper bundles`
- aliases `supporting record juniper bundles, juniper bundles in another document`

**Forbidden evidence:**
- marker `copper token`
- aliases `irrelevant document detail copper token`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `juniper bundles, paper moon mask`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22239 | n/a | 65.2431 |
| 2 | 22240 | n/a | 46.1573 |
| 3 | 21970 | n/a | 26.2423 |
| 4 | 21930 | n/a | 26.1638 |
| 5 | 21969 | n/a | 1.7151 |

Chunk rank 1:

```text
Question anchor: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane? Case scope id: multi-document-056. Scoped answer summary for multi-document-056 repeats the grounded evidence set: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-north-orchard-lane-letter-roll-056::multi-document-056::1: In document multi-north-orchard-lane-letter-roll-056, the verified archive note records paper moon mask. Case record id: multi-document-056. Question: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane? Scope reminder: document multi-north-orchard-lane-letter-roll-056. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).

document multi-sonya-family-register-056::multi-docum

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane? Case scope id: multi-document-056. Combined evidence: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-sonya-family-register-056::multi-document-056::2: In document multi-sonya-family-register-056, the verified archive note records juniper bundles. Case record id: multi-document-056. Question: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane? Scope reminder: document multi-sonya-family-register-056. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

Chunk rank 4:

```text
document multi-north-orchard-lane-letter-roll-056::multi-document-056::1: In document multi-north-orchard-lane-letter-roll-056, the verified archive note records paper moon mask. Case record id: multi-document-056. Question: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane? Scope reminder: document multi-north-orchard-lane-letter-roll-056. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).
```

Chunk rank 5:

```text
document multi-sonya-audio-transcript-076::multi-document-076::2: In document multi-sonya-audio-transcript-076, the verified archive note records tin key. Case record id: multi-document-076. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-sonya-audio-transcript-076. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `juniper bundles, paper moon mask`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22239 | n/a | 65.2296 |
| 2 | 22240 | n/a | 46.1868 |
| 3 | 21930 | n/a | 26.2242 |
| 4 | 21970 | n/a | 26.1270 |
| 5 | 21932 | n/a | 0.9357 |

Chunk rank 1:

```text
Question anchor: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane? Case scope id: multi-document-056. Scoped answer summary for multi-document-056 repeats the grounded evidence set: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-north-orchard-lane-letter-roll-056::multi-document-056::1: In document multi-north-orchard-lane-letter-roll-056, the verified archive note records paper moon mask. Case record id: multi-document-056. Question: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane? Scope reminder: document multi-north-orchard-lane-letter-roll-056. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).

document multi-sonya-family-register-056::multi-docum

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane? Case scope id: multi-document-056. Combined evidence: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-north-orchard-lane-letter-roll-056::multi-document-056::1: In document multi-north-orchard-lane-letter-roll-056, the verified archive note records paper moon mask. Case record id: multi-document-056. Question: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane? Scope reminder: document multi-north-orchard-lane-letter-roll-056. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).
```

Chunk rank 4:

```text
document multi-sonya-family-register-056::multi-document-056::2: In document multi-sonya-family-register-056, the verified archive note records juniper bundles. Case record id: multi-document-056. Question: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane? Scope reminder: document multi-sonya-family-register-056. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

Chunk rank 5:

```text
document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note records moonflower cutting. Case record id: multi-document-086. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-086. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

## Question 057: multi-document-057

**Question:** Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade?

**Expected evidence:**
- marker `Harvest Glow`
- aliases `festival Harvest Glow, the Harvest Glow record`
- marker `lantern hook`
- aliases `preserved item lantern hook, lantern hook in the preserved record`
- marker `carved shell comb`
- aliases `corroborating item carved shell comb, carved shell comb in the second document`

**Forbidden evidence:**
- marker `tuning fork`
- aliases `irrelevant document detail tuning fork`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Harvest Glow, carved shell comb, lantern hook`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22241 | n/a | 77.7069 |
| 2 | 22242 | n/a | 58.5158 |
| 3 | 21945 | n/a | 30.6956 |
| 4 | 21864 | n/a | 26.7199 |
| 5 | 21843 | n/a | 14.2385 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Case scope id: multi-document-057. Scoped answer summary for multi-document-057 repeats the grounded evidence set: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-harvest-glow-profile-page-057::multi-document-057::3: In document multi-harvest-glow-profile-page-057, the verified archive note records carved shell comb. Case record id: multi-document-057. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Scope reminder: document multi-harvest-glow-profile-page-057. Alias reminders for retrieval: carved shell comb (aliases: corrob

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Case scope id: multi-document-057. Combined evidence: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-runa-archive-057::multi-document-057::2: In document multi-runa-archive-057, the verified archive note records lantern hook. Case record id: multi-document-057. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Scope reminder: document multi-runa-archive-057. Alias reminders for retrieval: lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record).
```

Chunk rank 4:

```text
document multi-hollow-market-arcade-repair-book-057::multi-document-057::1: In document multi-hollow-market-arcade-repair-book-057, the verified archive note records Harvest Glow. Case record id: multi-document-057. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Scope reminder: document multi-hollow-market-arcade-repair-book-057. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

Chunk rank 5:

```text
document multi-fox-hollow-bridge-ledger-037::multi-document-037::1: In document multi-fox-hollow-bridge-ledger-037, the verified archive note records Harvest Glow. Case record id: multi-document-037. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-ledger-037. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Harvest Glow, carved shell comb, lantern hook`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22241 | n/a | 77.4566 |
| 2 | 22242 | n/a | 58.4819 |
| 3 | 21864 | n/a | 26.4398 |
| 4 | 22322 | n/a | 2.1663 |
| 5 | 22202 | n/a | 2.1634 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Case scope id: multi-document-057. Scoped answer summary for multi-document-057 repeats the grounded evidence set: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-harvest-glow-profile-page-057::multi-document-057::3: In document multi-harvest-glow-profile-page-057, the verified archive note records carved shell comb. Case record id: multi-document-057. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Scope reminder: document multi-harvest-glow-profile-page-057. Alias reminders for retrieval: carved shell comb (aliases: corrob

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Case scope id: multi-document-057. Combined evidence: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-hollow-market-arcade-repair-book-057::multi-document-057::1: In document multi-hollow-market-arcade-repair-book-057, the verified archive note records Harvest Glow. Case record id: multi-document-057. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Scope reminder: document multi-hollow-market-arcade-repair-book-057. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

Chunk rank 4:

```text
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-097. Combined evidence: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 5:

```text
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-037. Combined evidence: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 058: multi-document-058

**Question:** Which archive pieces from more than one document explain the family profile event at Marble stair hall?

**Expected evidence:**
- marker `clay watering cup`
- aliases `archive piece clay watering cup, clay watering cup in the first archive piece`
- marker `canal route map`
- aliases `second archive piece canal route map, canal route map in the second archive piece`

**Forbidden evidence:**
- marker `willow basket`
- aliases `irrelevant document detail willow basket`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `clay watering cup, canal route map`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: clay watering cup, canal route map; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 140 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 21833 | n/a | 1.0025 |
| 2 | 21794 | n/a | 0.7196 |

Chunk rank 1:

```text
document multi-driftwood-cove-profile-page-075::multi-document-075::1: In document multi-driftwood-cove-profile-page-075, the verified archive note records saffron scarf. Case record id: multi-document-075. Question: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Scope reminder: document multi-driftwood-cove-profile-page-075. Alias reminders for retrieval: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document).
```

Chunk rank 2:

```text
document multi-ada-photo-index-075::multi-document-075::2: In document multi-ada-photo-index-075, the verified archive note records coal stove hiss. Case record id: multi-document-075. Question: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Scope reminder: document multi-ada-photo-index-075. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document).
```

### Model: bge_m3

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `canal route map, clay watering cup`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 1 < 2.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22243 | n/a | 65.4218 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Marble stair hall? Case scope id: multi-document-058. Scoped answer summary for multi-document-058 repeats the grounded evidence set: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece); canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-ledger-058::multi-document-058::2: In document multi-iveta-ledger-058, the verified archive note records canal route map. Case record id: multi-document-058. Question: Which archive pieces from more than one document explain the family profile event at Marble stair hall? Scope reminder: document multi-iveta-ledger-058. Alias reminders for retrieval: canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece).

document multi-marble-stair-hall-inven

[truncated in Markdown; full text is available in JSON]
```

## Question 059: multi-document-059

**Question:** Which documents must be combined to understand Zora's photo album page note about Amber Canal lock?

**Expected evidence:**
- marker `saffron scarf`
- aliases `combined note saffron scarf, saffron scarf in one required document`
- marker `coal stove hiss`
- aliases `combined note coal stove hiss, coal stove hiss in another required document`
- marker `copper token`
- aliases `combined note copper token, copper token only visible after combining documents`

**Forbidden evidence:**
- marker `star ledger page`
- aliases `irrelevant document detail star ledger page`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, copper token, saffron scarf`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22245 | n/a | 77.5416 |
| 2 | 22246 | n/a | 58.3670 |
| 3 | 21795 | n/a | 26.5937 |
| 4 | 21964 | n/a | 26.3667 |
| 5 | 21797 | n/a | 1.3887 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Case scope id: multi-document-059. Scoped answer summary for multi-document-059 repeats the grounded evidence set: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-amber-canal-lock-family-register-059::multi-document-059::1: In document multi-amber-canal-lock-family-register-059, the verified archive note records saffron scarf. Case record id: multi-document-059. Question: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Scope reminder: document multi-amber-canal-lock-family-register-059. Alias reminders for retrieval: saffron scarf

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Case scope id: multi-document-059. Combined evidence: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-amber-canal-lock-family-register-059::multi-document-059::1: In document multi-amber-canal-lock-family-register-059, the verified archive note records saffron scarf. Case record id: multi-document-059. Question: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Scope reminder: document multi-amber-canal-lock-family-register-059. Alias reminders for retrieval: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document).
```

Chunk rank 4:

```text
document multi-signal-lantern-morning-travel-note-059::multi-document-059::3: In document multi-signal-lantern-morning-travel-note-059, the verified archive note records copper token. Case record id: multi-document-059. Question: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Scope reminder: document multi-signal-lantern-morning-travel-note-059. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token only visible after combining documents).
```

Chunk rank 5:

```text
document multi-amber-canal-lock-travel-note-089::multi-document-089::1: In document multi-amber-canal-lock-travel-note-089, the verified archive note records Signal Lantern Morning. Case record id: multi-document-089. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-amber-canal-lock-travel-note-089. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, copper token, saffron scarf`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22245 | n/a | 77.4227 |
| 2 | 22246 | n/a | 58.3786 |
| 3 | 22020 | n/a | 26.3531 |
| 4 | 21795 | n/a | 26.3511 |
| 5 | 21964 | n/a | 26.2857 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Case scope id: multi-document-059. Scoped answer summary for multi-document-059 repeats the grounded evidence set: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-amber-canal-lock-family-register-059::multi-document-059::1: In document multi-amber-canal-lock-family-register-059, the verified archive note records saffron scarf. Case record id: multi-document-059. Question: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Scope reminder: document multi-amber-canal-lock-family-register-059. Alias reminders for retrieval: saffron scarf

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Case scope id: multi-document-059. Combined evidence: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-zora-minute-book-059::multi-document-059::2: In document multi-zora-minute-book-059, the verified archive note records coal stove hiss. Case record id: multi-document-059. Question: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Scope reminder: document multi-zora-minute-book-059. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document).
```

Chunk rank 4:

```text
document multi-amber-canal-lock-family-register-059::multi-document-059::1: In document multi-amber-canal-lock-family-register-059, the verified archive note records saffron scarf. Case record id: multi-document-059. Question: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Scope reminder: document multi-amber-canal-lock-family-register-059. Alias reminders for retrieval: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document).
```

Chunk rank 5:

```text
document multi-signal-lantern-morning-travel-note-059::multi-document-059::3: In document multi-signal-lantern-morning-travel-note-059, the verified archive note records copper token. Case record id: multi-document-059. Question: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Scope reminder: document multi-signal-lantern-morning-travel-note-059. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token only visible after combining documents).
```

## Question 060: multi-document-060

**Question:** Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square?

**Expected evidence:**
- marker `blue glass jar`
- aliases `travel record blue glass jar, blue glass jar in one document`
- marker `tin key`
- aliases `supporting record tin key, tin key in another document`

**Forbidden evidence:**
- marker `silver booth token`
- aliases `irrelevant document detail silver booth token`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue glass jar, tin key`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22247 | n/a | 65.3487 |
| 2 | 22248 | n/a | 46.1727 |
| 3 | 21807 | n/a | 26.3521 |
| 4 | 21899 | n/a | 26.2581 |
| 5 | 21895 | n/a | 1.7841 |

Chunk rank 1:

```text
Question anchor: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Case scope id: multi-document-060. Scoped answer summary for multi-document-060 repeats the grounded evidence set: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bell-bridge-square-archive-060::multi-document-060::1: In document multi-bell-bridge-square-archive-060, the verified archive note records blue glass jar. Case record id: multi-document-060. Question: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Scope reminder: document multi-bell-bridge-square-archive-060. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).

document multi-mira-profile-page-060::multi-document-060::2: In document multi-mira-profil

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Case scope id: multi-document-060. Combined evidence: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-bell-bridge-square-archive-060::multi-document-060::1: In document multi-bell-bridge-square-archive-060, the verified archive note records blue glass jar. Case record id: multi-document-060. Question: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Scope reminder: document multi-bell-bridge-square-archive-060. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

Chunk rank 4:

```text
document multi-mira-profile-page-060::multi-document-060::2: In document multi-mira-profile-page-060, the verified archive note records tin key. Case record id: multi-document-060. Question: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Scope reminder: document multi-mira-profile-page-060. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 5:

```text
document multi-mira-family-register-020::multi-document-020::2: In document multi-mira-family-register-020, the verified archive note records birch tea flask. Case record id: multi-document-020. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-mira-family-register-020. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue glass jar, tin key`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22247 | n/a | 65.2928 |
| 2 | 22248 | n/a | 46.2395 |
| 3 | 21807 | n/a | 26.2807 |
| 4 | 21899 | n/a | 26.1864 |
| 5 | 21893 | n/a | 1.7023 |

Chunk rank 1:

```text
Question anchor: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Case scope id: multi-document-060. Scoped answer summary for multi-document-060 repeats the grounded evidence set: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bell-bridge-square-archive-060::multi-document-060::1: In document multi-bell-bridge-square-archive-060, the verified archive note records blue glass jar. Case record id: multi-document-060. Question: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Scope reminder: document multi-bell-bridge-square-archive-060. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).

document multi-mira-profile-page-060::multi-document-060::2: In document multi-mira-profil

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Case scope id: multi-document-060. Combined evidence: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-bell-bridge-square-archive-060::multi-document-060::1: In document multi-bell-bridge-square-archive-060, the verified archive note records blue glass jar. Case record id: multi-document-060. Question: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Scope reminder: document multi-bell-bridge-square-archive-060. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

Chunk rank 4:

```text
document multi-mira-profile-page-060::multi-document-060::2: In document multi-mira-profile-page-060, the verified archive note records tin key. Case record id: multi-document-060. Question: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Scope reminder: document multi-mira-profile-page-060. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 5:

```text
document multi-mira-audio-transcript-040::multi-document-040::2: In document multi-mira-audio-transcript-040, the verified archive note records juniper bundles. Case record id: multi-document-040. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-mira-audio-transcript-040. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

## Question 061: multi-document-061

**Question:** Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing?

**Expected evidence:**
- marker `Bellwater Fair`
- aliases `festival Bellwater Fair, the Bellwater Fair record`
- marker `copper wind vane pin`
- aliases `preserved item copper wind vane pin, copper wind vane pin in the preserved record`
- marker `brass compass`
- aliases `corroborating item brass compass, brass compass in the second document`

**Forbidden evidence:**
- marker `birch tea flask`
- aliases `irrelevant document detail birch tea flask`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Bellwater Fair, brass compass, copper wind vane pin`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22249 | n/a | 77.4849 |
| 2 | 22250 | n/a | 58.3551 |
| 3 | 21810 | n/a | 30.3443 |
| 4 | 21995 | n/a | 26.5528 |
| 5 | 21938 | n/a | 14.1088 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing? Case scope id: multi-document-061. Scoped answer summary for multi-document-061 repeats the grounded evidence set: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-audio-transcript-061::multi-document-061::3: In document multi-bellwater-fair-audio-transcript-061, the verified archive note records brass compass. Case record id: multi-document-061. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing? Scope reminder: document multi-bellwater-fair-audio-transcript-061. Alias reminders for retrieval: br

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing? Case scope id: multi-document-061. Combined evidence: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-bellwater-fair-audio-transcript-061::multi-document-061::3: In document multi-bellwater-fair-audio-transcript-061, the verified archive note records brass compass. Case record id: multi-document-061. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing? Scope reminder: document multi-bellwater-fair-audio-transcript-061. Alias reminders for retrieval: brass compass (aliases: corroborating item brass compass; brass compass in the second document).
```

Chunk rank 4:

```text
document multi-watchtower-landing-ledger-061::multi-document-061::1: In document multi-watchtower-landing-ledger-061, the verified archive note records Bellwater Fair. Case record id: multi-document-061. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing? Scope reminder: document multi-watchtower-landing-ledger-061. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

Chunk rank 5:

```text
document multi-pine-gate-yard-travel-note-041::multi-document-041::1: In document multi-pine-gate-yard-travel-note-041, the verified archive note records Bellwater Fair. Case record id: multi-document-041. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Scope reminder: document multi-pine-gate-yard-travel-note-041. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Bellwater Fair, brass compass, copper wind vane pin`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22249 | n/a | 77.2970 |
| 2 | 22250 | n/a | 58.2879 |
| 3 | 21995 | n/a | 26.2774 |
| 4 | 21984 | n/a | 5.9191 |
| 5 | 22210 | n/a | 2.0001 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing? Case scope id: multi-document-061. Scoped answer summary for multi-document-061 repeats the grounded evidence set: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-audio-transcript-061::multi-document-061::3: In document multi-bellwater-fair-audio-transcript-061, the verified archive note records brass compass. Case record id: multi-document-061. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing? Scope reminder: document multi-bellwater-fair-audio-transcript-061. Alias reminders for retrieval: br

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing? Case scope id: multi-document-061. Combined evidence: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-watchtower-landing-ledger-061::multi-document-061::1: In document multi-watchtower-landing-ledger-061, the verified archive note records Bellwater Fair. Case record id: multi-document-061. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing? Scope reminder: document multi-watchtower-landing-ledger-061. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

Chunk rank 4:

```text
document multi-vera-archive-021::multi-document-021::2: In document multi-vera-archive-021, the verified archive note records green apron. Case record id: multi-document-021. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-vera-archive-021. Alias reminders for retrieval: green apron (aliases: preserved item green apron; green apron in the preserved record).
```

Chunk rank 5:

```text
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Case scope id: multi-document-041. Combined evidence: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 062: multi-document-062

**Question:** Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk?

**Expected evidence:**
- marker `wax thread`
- aliases `archive piece wax thread, wax thread in the first archive piece`
- marker `basalt sketch`
- aliases `second archive piece basalt sketch, basalt sketch in the second archive piece`

**Forbidden evidence:**
- marker `oak barrel hoops`
- aliases `irrelevant document detail oak barrel hoops`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `basalt sketch, wax thread`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22251 | n/a | 65.4064 |
| 2 | 22252 | n/a | 46.4036 |
| 3 | 21877 | n/a | 26.3659 |
| 4 | 22316 | n/a | 13.8892 |
| 5 | 22188 | n/a | 13.8835 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Case scope id: multi-document-062. Scoped answer summary for multi-document-062 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-lantern-row-kiosk-minute-book-062::multi-document-062::1: In document multi-lantern-row-kiosk-minute-book-062, the verified archive note records wax thread. Case record id: multi-document-062. Question: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-minute-book-062. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).

document multi-nadia-travel-note-062::mult

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Case scope id: multi-document-062. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-lantern-row-kiosk-minute-book-062::multi-document-062::1: In document multi-lantern-row-kiosk-minute-book-062, the verified archive note records wax thread. Case record id: multi-document-062. Question: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-minute-book-062. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

Chunk rank 4:

```text
Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 5:

```text
Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-030. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `basalt sketch, wax thread`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22251 | n/a | 65.4755 |
| 2 | 22252 | n/a | 46.4425 |
| 3 | 21877 | n/a | 26.4533 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Case scope id: multi-document-062. Scoped answer summary for multi-document-062 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-lantern-row-kiosk-minute-book-062::multi-document-062::1: In document multi-lantern-row-kiosk-minute-book-062, the verified archive note records wax thread. Case record id: multi-document-062. Question: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-minute-book-062. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).

document multi-nadia-travel-note-062::mult

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Case scope id: multi-document-062. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-lantern-row-kiosk-minute-book-062::multi-document-062::1: In document multi-lantern-row-kiosk-minute-book-062, the verified archive note records wax thread. Case record id: multi-document-062. Question: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-minute-book-062. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

## Question 063: multi-document-063

**Question:** Which documents must be combined to understand Anya's family note note about Moss Archive room?

**Expected evidence:**
- marker `smoke vent chain`
- aliases `combined note smoke vent chain, smoke vent chain in one required document`
- marker `copper token`
- aliases `combined note copper token, copper token in another required document`
- marker `silver booth token`
- aliases `combined note silver booth token, silver booth token only visible after combining documents`

**Forbidden evidence:**
- marker `glass ink bottle`
- aliases `irrelevant document detail glass ink bottle`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `copper token, silver booth token, smoke vent chain`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22253 | n/a | 77.2297 |
| 2 | 22254 | n/a | 58.1500 |
| 3 | 21806 | n/a | 26.2500 |
| 4 | 21805 | n/a | 9.9071 |
| 5 | 21804 | n/a | 1.6804 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Anya's family note note about Moss Archive room? Case scope id: multi-document-063. Scoped answer summary for multi-document-063 repeats the grounded evidence set: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-photo-index-063::multi-document-063::2: In document multi-anya-photo-index-063, the verified archive note records copper token. Case record id: multi-document-063. Question: Which documents must be combined to understand Anya's family note note about Moss Archive room? Scope reminder: document multi-anya-photo-index-063. Alias reminders for retrieval: copper token (aliases: combined note copper token; co

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Anya's family note note about Moss Archive room? Case scope id: multi-document-063. Combined evidence: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-anya-photo-index-063::multi-document-063::2: In document multi-anya-photo-index-063, the verified archive note records copper token. Case record id: multi-document-063. Question: Which documents must be combined to understand Anya's family note note about Moss Archive room? Scope reminder: document multi-anya-photo-index-063. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token in another required document).
```

Chunk rank 4:

```text
document multi-anya-minute-book-083::multi-document-083::2: In document multi-anya-minute-book-083, the verified archive note records silver booth token. Case record id: multi-document-083. Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Scope reminder: document multi-anya-minute-book-083. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token in another required document).
```

Chunk rank 5:

```text
document multi-anya-minute-book-023::multi-document-023::2: In document multi-anya-minute-book-023, the verified archive note records weathered camera strap. Case record id: multi-document-023. Question: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Scope reminder: document multi-anya-minute-book-023. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `copper token, silver booth token, smoke vent chain`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22253 | n/a | 77.0820 |
| 2 | 22254 | n/a | 58.0254 |
| 3 | 21915 | n/a | 26.0861 |
| 4 | 21806 | n/a | 26.0064 |
| 5 | 21912 | n/a | 25.9075 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Anya's family note note about Moss Archive room? Case scope id: multi-document-063. Scoped answer summary for multi-document-063 repeats the grounded evidence set: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-photo-index-063::multi-document-063::2: In document multi-anya-photo-index-063, the verified archive note records copper token. Case record id: multi-document-063. Question: Which documents must be combined to understand Anya's family note note about Moss Archive room? Scope reminder: document multi-anya-photo-index-063. Alias reminders for retrieval: copper token (aliases: combined note copper token; co

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Anya's family note note about Moss Archive room? Case scope id: multi-document-063. Combined evidence: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-moss-archive-room-profile-page-063::multi-document-063::1: In document multi-moss-archive-room-profile-page-063, the verified archive note records smoke vent chain. Case record id: multi-document-063. Question: Which documents must be combined to understand Anya's family note note about Moss Archive room? Scope reminder: document multi-moss-archive-room-profile-page-063. Alias reminders for retrieval: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document).
```

Chunk rank 4:

```text
document multi-anya-photo-index-063::multi-document-063::2: In document multi-anya-photo-index-063, the verified archive note records copper token. Case record id: multi-document-063. Question: Which documents must be combined to understand Anya's family note note about Moss Archive room? Scope reminder: document multi-anya-photo-index-063. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token in another required document).
```

Chunk rank 5:

```text
document multi-moon-orchard-rest-repair-book-063::multi-document-063::3: In document multi-moon-orchard-rest-repair-book-063, the verified archive note records silver booth token. Case record id: multi-document-063. Question: Which documents must be combined to understand Anya's family note note about Moss Archive room? Scope reminder: document multi-moon-orchard-rest-repair-book-063. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

## Question 064: multi-document-064

**Question:** Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin?

**Expected evidence:**
- marker `amber lantern`
- aliases `travel record amber lantern, amber lantern in one document`
- marker `tuning fork`
- aliases `supporting record tuning fork, tuning fork in another document`

**Forbidden evidence:**
- marker `weathered camera strap`
- aliases `irrelevant document detail weathered camera strap`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `amber lantern, tuning fork`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22255 | n/a | 65.2734 |
| 2 | 21825 | n/a | 26.2588 |
| 3 | 22004 | n/a | 26.2276 |
| 4 | 22009 | n/a | 1.9561 |
| 5 | 22005 | n/a | 1.8837 |

Chunk rank 1:

```text
Question anchor: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin? Case scope id: multi-document-064. Scoped answer summary for multi-document-064 repeats the grounded evidence set: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-blue-trunk-cabin-memory-log-064::multi-document-064::1: In document multi-blue-trunk-cabin-memory-log-064, the verified archive note records amber lantern. Case record id: multi-document-064. Question: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin? Scope reminder: document multi-blue-trunk-cabin-memory-log-064. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).

document multi-yara-audio-transcript-064::multi-document-064::2: In document multi-yara-audio-

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-blue-trunk-cabin-memory-log-064::multi-document-064::1: In document multi-blue-trunk-cabin-memory-log-064, the verified archive note records amber lantern. Case record id: multi-document-064. Question: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin? Scope reminder: document multi-blue-trunk-cabin-memory-log-064. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 3:

```text
document multi-yara-audio-transcript-064::multi-document-064::2: In document multi-yara-audio-transcript-064, the verified archive note records tuning fork. Case record id: multi-document-064. Question: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin? Scope reminder: document multi-yara-audio-transcript-064. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

Chunk rank 4:

```text
document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-yara-profile-page-084. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 5:

```text
document multi-yara-family-register-044::multi-document-044::2: In document multi-yara-family-register-044, the verified archive note records tin key. Case record id: multi-document-044. Question: Which records together show how Yara prepared the canal barge stop near Moon Mill yard? Scope reminder: document multi-yara-family-register-044. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `amber lantern, tuning fork`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22255 | n/a | 65.2522 |
| 2 | 22256 | n/a | 46.2243 |
| 3 | 22004 | n/a | 26.2008 |
| 4 | 21825 | n/a | 26.1806 |
| 5 | 22008 | n/a | 1.7287 |

Chunk rank 1:

```text
Question anchor: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin? Case scope id: multi-document-064. Scoped answer summary for multi-document-064 repeats the grounded evidence set: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-blue-trunk-cabin-memory-log-064::multi-document-064::1: In document multi-blue-trunk-cabin-memory-log-064, the verified archive note records amber lantern. Case record id: multi-document-064. Question: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin? Scope reminder: document multi-blue-trunk-cabin-memory-log-064. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).

document multi-yara-audio-transcript-064::multi-document-064::2: In document multi-yara-audio-

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin? Case scope id: multi-document-064. Combined evidence: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-yara-audio-transcript-064::multi-document-064::2: In document multi-yara-audio-transcript-064, the verified archive note records tuning fork. Case record id: multi-document-064. Question: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin? Scope reminder: document multi-yara-audio-transcript-064. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

Chunk rank 4:

```text
document multi-blue-trunk-cabin-memory-log-064::multi-document-064::1: In document multi-blue-trunk-cabin-memory-log-064, the verified archive note records amber lantern. Case record id: multi-document-064. Question: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin? Scope reminder: document multi-blue-trunk-cabin-memory-log-064. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 5:

```text
document multi-yara-profile-page-024::multi-document-024::2: In document multi-yara-profile-page-024, the verified archive note records juniper bundles. Case record id: multi-document-024. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-yara-profile-page-024. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

## Question 065: multi-document-065

**Question:** Which documents together identify the Lantern Tide memory that Ada preserved after leaving River Lantern inn?

**Expected evidence:**
- marker `Lantern Tide`
- aliases `festival Lantern Tide, the Lantern Tide record`
- marker `cedar shovel`
- aliases `preserved item cedar shovel, cedar shovel in the preserved record`
- marker `willow basket`
- aliases `corroborating item willow basket, willow basket in the second document`

**Forbidden evidence:**
- marker `juniper bundles`
- aliases `irrelevant document detail juniper bundles`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Tide, cedar shovel, willow basket`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22258 | n/a | 58.2950 |
| 2 | 21790 | n/a | 6.0809 |
| 3 | 21789 | n/a | 6.0417 |
| 4 | 21786 | n/a | 5.9939 |
| 5 | 21879 | n/a | 5.9714 |

Chunk rank 1:

```text
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving River Lantern inn? Case scope id: multi-document-065. Combined evidence: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 2:

```text
document multi-ada-memory-log-085::multi-document-085::2: In document multi-ada-memory-log-085, the verified archive note records green apron. Case record id: multi-document-085. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-ada-memory-log-085. Alias reminders for retrieval: green apron (aliases: preserved item green apron; green apron in the preserved record).
```

Chunk rank 3:

```text
document multi-ada-memory-log-025::multi-document-025::2: In document multi-ada-memory-log-025, the verified archive note records lantern hook. Case record id: multi-document-025. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-ada-memory-log-025. Alias reminders for retrieval: lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record).
```

Chunk rank 4:

```text
document multi-ada-archive-045::multi-document-045::2: In document multi-ada-archive-045, the verified archive note records copper wind vane pin. Case record id: multi-document-045. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove? Scope reminder: document multi-ada-archive-045. Alias reminders for retrieval: copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record).
```

Chunk rank 5:

```text
document multi-lantern-tide-audio-transcript-085::multi-document-085::3: In document multi-lantern-tide-audio-transcript-085, the verified archive note records oak barrel hoops. Case record id: multi-document-085. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-lantern-tide-audio-transcript-085. Alias reminders for retrieval: oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Tide, cedar shovel, willow basket`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22257 | n/a | 77.2920 |
| 2 | 22258 | n/a | 58.2604 |
| 3 | 21788 | n/a | 30.1893 |
| 4 | 21944 | n/a | 26.2837 |
| 5 | 21790 | n/a | 5.9048 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Lantern Tide memory that Ada preserved after leaving River Lantern inn? Case scope id: multi-document-065. Scoped answer summary for multi-document-065 repeats the grounded evidence set: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-letter-roll-065::multi-document-065::2: In document multi-ada-letter-roll-065, the verified archive note records cedar shovel. Case record id: multi-document-065. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving River Lantern inn? Scope reminder: document multi-ada-letter-roll-065. Alias reminders for retrieval: cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record)

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving River Lantern inn? Case scope id: multi-document-065. Combined evidence: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ada-letter-roll-065::multi-document-065::2: In document multi-ada-letter-roll-065, the verified archive note records cedar shovel. Case record id: multi-document-065. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving River Lantern inn? Scope reminder: document multi-ada-letter-roll-065. Alias reminders for retrieval: cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record).
```

Chunk rank 4:

```text
document multi-river-lantern-inn-travel-note-065::multi-document-065::1: In document multi-river-lantern-inn-travel-note-065, the verified archive note records Lantern Tide. Case record id: multi-document-065. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving River Lantern inn? Scope reminder: document multi-river-lantern-inn-travel-note-065. Alias reminders for retrieval: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record).
```

Chunk rank 5:

```text
document multi-ada-memory-log-085::multi-document-085::2: In document multi-ada-memory-log-085, the verified archive note records green apron. Case record id: multi-document-085. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-ada-memory-log-085. Alias reminders for retrieval: green apron (aliases: preserved item green apron; green apron in the preserved record).
```

## Question 066: multi-document-066

**Question:** Which archive pieces from more than one document explain the family profile event at Winter Chapel porch?

**Expected evidence:**
- marker `violet ribbon`
- aliases `archive piece violet ribbon, violet ribbon in the first archive piece`
- marker `star ledger page`
- aliases `second archive piece star ledger page, star ledger page in the second archive piece`

**Forbidden evidence:**
- marker `carved shell comb`
- aliases `irrelevant document detail carved shell comb`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `star ledger page, violet ribbon`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22259 | n/a | 65.4302 |
| 2 | 22003 | n/a | 26.4611 |
| 3 | 22002 | n/a | 4.3659 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-066. Scoped answer summary for multi-document-066 repeats the grounded evidence set: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-sonya-repair-book-066::multi-document-066::2: In document multi-sonya-repair-book-066, the verified archive note records star ledger page. Case record id: multi-document-066. Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Scope reminder: document multi-sonya-repair-book-066. Alias reminders for retrieval: star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece).

document multi-winter-ch

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-winter-chapel-porch-photo-index-066::multi-document-066::1: In document multi-winter-chapel-porch-photo-index-066, the verified archive note records violet ribbon. Case record id: multi-document-066. Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Scope reminder: document multi-winter-chapel-porch-photo-index-066. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

Chunk rank 3:

```text
document multi-winter-chapel-porch-photo-index-006::multi-document-006::1: In document multi-winter-chapel-porch-photo-index-006, the verified archive note records moonflower cutting. Case record id: multi-document-006. Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Scope reminder: document multi-winter-chapel-porch-photo-index-006. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `star ledger page, violet ribbon`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22259 | n/a | 65.4244 |
| 2 | 22003 | n/a | 26.4463 |
| 3 | 22002 | n/a | 4.4762 |
| 4 | 21974 | n/a | 4.4148 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-066. Scoped answer summary for multi-document-066 repeats the grounded evidence set: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-sonya-repair-book-066::multi-document-066::2: In document multi-sonya-repair-book-066, the verified archive note records star ledger page. Case record id: multi-document-066. Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Scope reminder: document multi-sonya-repair-book-066. Alias reminders for retrieval: star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece).

document multi-winter-ch

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-winter-chapel-porch-photo-index-066::multi-document-066::1: In document multi-winter-chapel-porch-photo-index-066, the verified archive note records violet ribbon. Case record id: multi-document-066. Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Scope reminder: document multi-winter-chapel-porch-photo-index-066. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

Chunk rank 3:

```text
document multi-winter-chapel-porch-photo-index-006::multi-document-006::1: In document multi-winter-chapel-porch-photo-index-006, the verified archive note records moonflower cutting. Case record id: multi-document-006. Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Scope reminder: document multi-winter-chapel-porch-photo-index-006. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

Chunk rank 4:

```text
document multi-sonya-repair-book-006::multi-document-006::2: In document multi-sonya-repair-book-006, the verified archive note records glass ink bottle. Case record id: multi-document-006. Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Scope reminder: document multi-sonya-repair-book-006. Alias reminders for retrieval: glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece).
```

## Question 067: multi-document-067

**Question:** Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge?

**Expected evidence:**
- marker `blue oar`
- aliases `combined note blue oar, blue oar in one required document`
- marker `silver booth token`
- aliases `combined note silver booth token, silver booth token in another required document`
- marker `weathered camera strap`
- aliases `combined note weathered camera strap, weathered camera strap only visible after combining documents`

**Forbidden evidence:**
- marker `canal route map`
- aliases `irrelevant document detail canal route map`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue oar, silver booth token, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22261 | n/a | 77.3185 |
| 2 | 22262 | n/a | 58.2924 |
| 3 | 21947 | n/a | 26.2781 |
| 4 | 21841 | n/a | 2.2056 |
| 5 | 21782 | n/a | 0.9685 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge? Case scope id: multi-document-067. Scoped answer summary for multi-document-067 repeats the grounded evidence set: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-fox-hollow-bridge-audio-transcript-067::multi-document-067::1: In document multi-fox-hollow-bridge-audio-transcript-067, the verified archive note records blue oar. Case record id: multi-document-067. Question: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-audio-transcript-067. Alias reminders for retrie

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge? Case scope id: multi-document-067. Combined evidence: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-runa-inventory-sheet-067::multi-document-067::2: In document multi-runa-inventory-sheet-067, the verified archive note records silver booth token. Case record id: multi-document-067. Question: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge? Scope reminder: document multi-runa-inventory-sheet-067. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token in another required document).
```

Chunk rank 4:

```text
document multi-fox-hollow-bridge-audio-transcript-007::multi-document-007::1: In document multi-fox-hollow-bridge-audio-transcript-007, the verified archive note records rope bridge permit. Case record id: multi-document-007. Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-audio-transcript-007. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 5:

```text
document bridge-permit-roll::multi-document-valley-expedition::2: In document bridge-permit-roll, the verified archive note records rope bridge permit. Case record id: multi-document-valley-expedition. Question: Which expedition records together explain how the valley crossing was prepared? Scope reminder: document bridge-permit-roll. Alias reminders for retrieval: rope bridge permit (aliases: permit for the rope bridge; bridge crossing permit).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue oar, silver booth token, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22261 | n/a | 77.1484 |
| 2 | 22262 | n/a | 58.1599 |
| 3 | 21842 | n/a | 26.2063 |
| 4 | 21841 | n/a | 2.0685 |
| 5 | 21843 | n/a | 1.3740 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge? Case scope id: multi-document-067. Scoped answer summary for multi-document-067 repeats the grounded evidence set: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-fox-hollow-bridge-audio-transcript-067::multi-document-067::1: In document multi-fox-hollow-bridge-audio-transcript-067, the verified archive note records blue oar. Case record id: multi-document-067. Question: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-audio-transcript-067. Alias reminders for retrie

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge? Case scope id: multi-document-067. Combined evidence: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-fox-hollow-bridge-audio-transcript-067::multi-document-067::1: In document multi-fox-hollow-bridge-audio-transcript-067, the verified archive note records blue oar. Case record id: multi-document-067. Question: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-audio-transcript-067. Alias reminders for retrieval: blue oar (aliases: combined note blue oar; blue oar in one required document).
```

Chunk rank 4:

```text
document multi-fox-hollow-bridge-audio-transcript-007::multi-document-007::1: In document multi-fox-hollow-bridge-audio-transcript-007, the verified archive note records rope bridge permit. Case record id: multi-document-007. Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-audio-transcript-007. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 5:

```text
document multi-fox-hollow-bridge-ledger-037::multi-document-037::1: In document multi-fox-hollow-bridge-ledger-037, the verified archive note records Harvest Glow. Case record id: multi-document-037. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-ledger-037. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

## Question 068: multi-document-068

**Question:** Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well?

**Expected evidence:**
- marker `linen wick`
- aliases `travel record linen wick, linen wick in one document`
- marker `birch tea flask`
- aliases `supporting record birch tea flask, birch tea flask in another document`

**Forbidden evidence:**
- marker `coal stove hiss`
- aliases `irrelevant document detail coal stove hiss`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `birch tea flask, linen wick`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22263 | n/a | 65.3398 |
| 2 | 21868 | n/a | 26.3401 |
| 3 | 21997 | n/a | 26.2557 |
| 4 | 22009 | n/a | 13.2536 |
| 5 | 21867 | n/a | 4.2276 |

Chunk rank 1:

```text
Question anchor: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Case scope id: multi-document-068. Scoped answer summary for multi-document-068 repeats the grounded evidence set: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-family-register-068::multi-document-068::2: In document multi-iveta-family-register-068, the verified archive note records birch tea flask. Case record id: multi-document-068. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-iveta-family-register-068. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).

document multi-willow-courtyard-well-letter-roll-068::multi-document-068::1: In

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-iveta-family-register-068::multi-document-068::2: In document multi-iveta-family-register-068, the verified archive note records birch tea flask. Case record id: multi-document-068. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-iveta-family-register-068. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 3:

```text
document multi-willow-courtyard-well-letter-roll-068::multi-document-068::1: In document multi-willow-courtyard-well-letter-roll-068, the verified archive note records linen wick. Case record id: multi-document-068. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-willow-courtyard-well-letter-roll-068. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 4:

```text
document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-yara-profile-page-084. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 5:

```text
document multi-iveta-family-register-008::multi-document-008::2: In document multi-iveta-family-register-008, the verified archive note records juniper bundles. Case record id: multi-document-008. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-iveta-family-register-008. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `birch tea flask, linen wick`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22263 | n/a | 65.2316 |
| 2 | 22264 | n/a | 46.1620 |
| 3 | 21997 | n/a | 26.2628 |
| 4 | 21868 | n/a | 26.1031 |
| 5 | 21996 | n/a | 4.2274 |

Chunk rank 1:

```text
Question anchor: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Case scope id: multi-document-068. Scoped answer summary for multi-document-068 repeats the grounded evidence set: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-family-register-068::multi-document-068::2: In document multi-iveta-family-register-068, the verified archive note records birch tea flask. Case record id: multi-document-068. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-iveta-family-register-068. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).

document multi-willow-courtyard-well-letter-roll-068::multi-document-068::1: In

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Case scope id: multi-document-068. Combined evidence: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-willow-courtyard-well-letter-roll-068::multi-document-068::1: In document multi-willow-courtyard-well-letter-roll-068, the verified archive note records linen wick. Case record id: multi-document-068. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-willow-courtyard-well-letter-roll-068. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 4:

```text
document multi-iveta-family-register-068::multi-document-068::2: In document multi-iveta-family-register-068, the verified archive note records birch tea flask. Case record id: multi-document-068. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-iveta-family-register-068. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 5:

```text
document multi-willow-courtyard-well-letter-roll-008::multi-document-008::1: In document multi-willow-courtyard-well-letter-roll-008, the verified archive note records paper moon mask. Case record id: multi-document-008. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-willow-courtyard-well-letter-roll-008. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).
```

## Question 069: multi-document-069

**Question:** Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay?

**Expected evidence:**
- marker `Signal Lantern Morning`
- aliases `festival Signal Lantern Morning, the Signal Lantern Morning record`
- marker `green apron`
- aliases `preserved item green apron, green apron in the preserved record`
- marker `oak barrel hoops`
- aliases `corroborating item oak barrel hoops, oak barrel hoops in the second document`

**Forbidden evidence:**
- marker `tin key`
- aliases `irrelevant document detail tin key`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning, green apron, oak barrel hoops`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22265 | n/a | 77.5754 |
| 2 | 22266 | n/a | 58.6030 |
| 3 | 21848 | n/a | 26.5821 |
| 4 | 21847 | n/a | 16.5821 |
| 5 | 22146 | n/a | 4.5590 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-document-069. Scoped answer summary for multi-document-069 repeats the grounded evidence set: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-glass-harbor-quay-repair-book-069::multi-document-069::1: In document multi-glass-harbor-quay-repair-book-069, the verified archive note records Signal Lantern Morning. Case record id: multi-document-069. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-repair-book-069. Alias remi

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-document-069. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-glass-harbor-quay-repair-book-069::multi-document-069::1: In document multi-glass-harbor-quay-repair-book-069, the verified archive note records Signal Lantern Morning. Case record id: multi-document-069. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-repair-book-069. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

Chunk rank 4:

```text
document multi-glass-harbor-quay-repair-book-009::multi-document-009::1: In document multi-glass-harbor-quay-repair-book-009, the verified archive note records Signal Lantern Morning. Case record id: multi-document-009. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-repair-book-009. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

Chunk rank 5:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-document-009. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning, green apron, oak barrel hoops`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22265 | n/a | 77.5505 |
| 2 | 22266 | n/a | 58.5390 |
| 3 | 21848 | n/a | 26.5730 |
| 4 | 21847 | n/a | 16.5730 |
| 5 | 21797 | n/a | 14.0916 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-document-069. Scoped answer summary for multi-document-069 repeats the grounded evidence set: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-glass-harbor-quay-repair-book-069::multi-document-069::1: In document multi-glass-harbor-quay-repair-book-069, the verified archive note records Signal Lantern Morning. Case record id: multi-document-069. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-repair-book-069. Alias remi

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-document-069. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-glass-harbor-quay-repair-book-069::multi-document-069::1: In document multi-glass-harbor-quay-repair-book-069, the verified archive note records Signal Lantern Morning. Case record id: multi-document-069. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-repair-book-069. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

Chunk rank 4:

```text
document multi-glass-harbor-quay-repair-book-009::multi-document-009::1: In document multi-glass-harbor-quay-repair-book-009, the verified archive note records Signal Lantern Morning. Case record id: multi-document-009. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-repair-book-009. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

Chunk rank 5:

```text
document multi-amber-canal-lock-travel-note-089::multi-document-089::1: In document multi-amber-canal-lock-travel-note-089, the verified archive note records Signal Lantern Morning. Case record id: multi-document-089. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-amber-canal-lock-travel-note-089. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

## Question 070: multi-document-070

**Question:** Which archive pieces from more than one document explain the family profile event at Birch Ferry shed?

**Expected evidence:**
- marker `moonflower cutting`
- aliases `archive piece moonflower cutting, moonflower cutting in the first archive piece`
- marker `glass ink bottle`
- aliases `second archive piece glass ink bottle, glass ink bottle in the second archive piece`

**Forbidden evidence:**
- marker `brass compass`
- aliases `irrelevant document detail brass compass`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `glass ink bottle, moonflower cutting`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 1 < 2.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22268 | n/a | 46.4036 |

Chunk rank 1:

```text
Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Case scope id: multi-document-070. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `glass ink bottle, moonflower cutting`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22267 | n/a | 65.4793 |
| 2 | 22268 | n/a | 46.4634 |
| 3 | 21820 | n/a | 26.4238 |
| 4 | 22140 | n/a | 13.9316 |
| 5 | 21819 | n/a | 4.4026 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Case scope id: multi-document-070. Scoped answer summary for multi-document-070 repeats the grounded evidence set: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-birch-ferry-shed-inventory-sheet-070::multi-document-070::1: In document multi-birch-ferry-shed-inventory-sheet-070, the verified archive note records moonflower cutting. Case record id: multi-document-070. Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-inventory-sheet-070. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Case scope id: multi-document-070. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-birch-ferry-shed-inventory-sheet-070::multi-document-070::1: In document multi-birch-ferry-shed-inventory-sheet-070, the verified archive note records moonflower cutting. Case record id: multi-document-070. Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-inventory-sheet-070. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

Chunk rank 4:

```text
Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 5:

```text
document multi-birch-ferry-shed-inventory-sheet-010::multi-document-010::1: In document multi-birch-ferry-shed-inventory-sheet-010, the verified archive note records clay watering cup. Case record id: multi-document-010. Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-inventory-sheet-010. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece).
```

## Question 071: multi-document-071

**Question:** Which documents must be combined to understand Vera's holiday card note about Pine Gate yard?

**Expected evidence:**
- marker `rope bridge permit`
- aliases `combined note rope bridge permit, rope bridge permit in one required document`
- marker `weathered camera strap`
- aliases `combined note weathered camera strap, weathered camera strap in another required document`
- marker `coal stove hiss`
- aliases `combined note coal stove hiss, coal stove hiss only visible after combining documents`

**Forbidden evidence:**
- marker `basalt sketch`
- aliases `irrelevant document detail basalt sketch`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, rope bridge permit, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22269 | n/a | 77.3399 |
| 2 | 22270 | n/a | 58.2170 |
| 3 | 21937 | n/a | 26.3252 |
| 4 | 21991 | n/a | 26.2110 |
| 5 | 21936 | n/a | 2.1136 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Case scope id: multi-document-071. Scoped answer summary for multi-document-071 repeats the grounded evidence set: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-travel-note-071::multi-document-071::3: In document multi-bellwater-fair-travel-note-071, the verified archive note records coal stove hiss. Case record id: multi-document-071. Question: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Scope reminder: document multi-bellwater-fair-travel-note-071. Alias reminders for retrieva

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Case scope id: multi-document-071. Combined evidence: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-pine-gate-yard-family-register-071::multi-document-071::1: In document multi-pine-gate-yard-family-register-071, the verified archive note records rope bridge permit. Case record id: multi-document-071. Question: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Scope reminder: document multi-pine-gate-yard-family-register-071. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 4:

```text
document multi-vera-minute-book-071::multi-document-071::2: In document multi-vera-minute-book-071, the verified archive note records weathered camera strap. Case record id: multi-document-071. Question: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Scope reminder: document multi-vera-minute-book-071. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document).
```

Chunk rank 5:

```text
document multi-pine-gate-yard-family-register-011::multi-document-011::1: In document multi-pine-gate-yard-family-register-011, the verified archive note records saffron scarf. Case record id: multi-document-011. Question: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Scope reminder: document multi-pine-gate-yard-family-register-011. Alias reminders for retrieval: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, rope bridge permit, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22269 | n/a | 77.1980 |
| 2 | 22270 | n/a | 58.1464 |
| 3 | 21937 | n/a | 26.1823 |
| 4 | 21991 | n/a | 26.1082 |
| 5 | 21818 | n/a | 26.0719 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Case scope id: multi-document-071. Scoped answer summary for multi-document-071 repeats the grounded evidence set: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-travel-note-071::multi-document-071::3: In document multi-bellwater-fair-travel-note-071, the verified archive note records coal stove hiss. Case record id: multi-document-071. Question: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Scope reminder: document multi-bellwater-fair-travel-note-071. Alias reminders for retrieva

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Case scope id: multi-document-071. Combined evidence: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-pine-gate-yard-family-register-071::multi-document-071::1: In document multi-pine-gate-yard-family-register-071, the verified archive note records rope bridge permit. Case record id: multi-document-071. Question: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Scope reminder: document multi-pine-gate-yard-family-register-071. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 4:

```text
document multi-vera-minute-book-071::multi-document-071::2: In document multi-vera-minute-book-071, the verified archive note records weathered camera strap. Case record id: multi-document-071. Question: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Scope reminder: document multi-vera-minute-book-071. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document).
```

Chunk rank 5:

```text
document multi-bellwater-fair-travel-note-071::multi-document-071::3: In document multi-bellwater-fair-travel-note-071, the verified archive note records coal stove hiss. Case record id: multi-document-071. Question: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Scope reminder: document multi-bellwater-fair-travel-note-071. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents).
```

## Question 072: multi-document-072

**Question:** Which records together show how Nadia prepared the river skiff stop near North Bell workshop?

**Expected evidence:**
- marker `paper moon mask`
- aliases `travel record paper moon mask, paper moon mask in one document`
- marker `juniper bundles`
- aliases `supporting record juniper bundles, juniper bundles in another document`

**Forbidden evidence:**
- marker `copper token`
- aliases `irrelevant document detail copper token`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `paper moon mask`
- Missing: `juniper bundles`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 1 < 2.; Missing expected markers: juniper bundles; Evidence coverage below requirement: 0.500 < 1.000.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22026 | n/a | 4.7724 |
| 2 | 21920 | n/a | 1.8845 |
| 3 | 21918 | n/a | 1.8351 |
| 4 | 21919 | n/a | 1.8049 |
| 5 | 22009 | n/a | 1.3082 |

Chunk rank 1:

```text
document school-stage-list::multi-document-school-rehearsal::1: In document school-stage-list, the verified archive note records paper moon mask. Case record id: multi-document-school-rehearsal. Question: Which stage prop and music-room tool together identify the school rehearsal setup? Scope reminder: document school-stage-list. Alias reminders for retrieval: paper moon mask (aliases: moon mask of paper; stage moon mask).
```

Chunk rank 2:

```text
document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-family-register-092, the verified archive note records tin key. Case record id: multi-document-092. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-nadia-family-register-092. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 3:

```text
document multi-nadia-audio-transcript-052::multi-document-052::2: In document multi-nadia-audio-transcript-052, the verified archive note records birch tea flask. Case record id: multi-document-052. Question: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Scope reminder: document multi-nadia-audio-transcript-052. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 4:

```text
document multi-nadia-family-register-032::multi-document-032::2: In document multi-nadia-family-register-032, the verified archive note records tuning fork. Case record id: multi-document-032. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-nadia-family-register-032. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

Chunk rank 5:

```text
document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-yara-profile-page-084. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `juniper bundles, paper moon mask`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22271 | n/a | 65.2814 |
| 2 | 22272 | n/a | 46.2035 |
| 3 | 21928 | n/a | 26.3158 |
| 4 | 21924 | n/a | 26.1259 |
| 5 | 21927 | n/a | 4.3445 |

Chunk rank 1:

```text
Question anchor: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Case scope id: multi-document-072. Scoped answer summary for multi-document-072 repeats the grounded evidence set: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-nadia-profile-page-072::multi-document-072::2: In document multi-nadia-profile-page-072, the verified archive note records juniper bundles. Case record id: multi-document-072. Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Scope reminder: document multi-nadia-profile-page-072. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).

document multi-north-bell-workshop-archive-072::multi-document-072::1: In docum

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Case scope id: multi-document-072. Combined evidence: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-north-bell-workshop-archive-072::multi-document-072::1: In document multi-north-bell-workshop-archive-072, the verified archive note records paper moon mask. Case record id: multi-document-072. Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Scope reminder: document multi-north-bell-workshop-archive-072. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).
```

Chunk rank 4:

```text
document multi-nadia-profile-page-072::multi-document-072::2: In document multi-nadia-profile-page-072, the verified archive note records juniper bundles. Case record id: multi-document-072. Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Scope reminder: document multi-nadia-profile-page-072. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

Chunk rank 5:

```text
document multi-north-bell-workshop-archive-012::multi-document-012::1: In document multi-north-bell-workshop-archive-012, the verified archive note records blue glass jar. Case record id: multi-document-012. Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Scope reminder: document multi-north-bell-workshop-archive-012. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

## Question 073: multi-document-073

**Question:** Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier?

**Expected evidence:**
- marker `Moon Orchard Rest`
- aliases `festival Moon Orchard Rest, the Moon Orchard Rest record`
- marker `lantern hook`
- aliases `preserved item lantern hook, lantern hook in the preserved record`
- marker `carved shell comb`
- aliases `corroborating item carved shell comb, carved shell comb in the second document`

**Forbidden evidence:**
- marker `tuning fork`
- aliases `irrelevant document detail tuning fork`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Orchard Rest, carved shell comb, lantern hook`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22273 | n/a | 77.6196 |
| 2 | 22274 | n/a | 58.5583 |
| 3 | 21840 | n/a | 26.6362 |
| 4 | 21839 | n/a | 16.7322 |
| 5 | 21935 | n/a | 14.2136 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-document-073. Scoped answer summary for multi-document-073 repeats the grounded evidence set: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-memory-log-073::multi-document-073::2: In document multi-anya-memory-log-073, the verified archive note records lantern hook. Case record id: multi-document-073. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-anya-memory-log-073. Alias reminders for retrieval: lantern hook (aliases: preserved item lantern hook; la

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-document-073. Combined evidence: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-fog-island-pier-ledger-073::multi-document-073::1: In document multi-fog-island-pier-ledger-073, the verified archive note records Moon Orchard Rest. Case record id: multi-document-073. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-fog-island-pier-ledger-073. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 4:

```text
document multi-fog-island-pier-ledger-013::multi-document-013::1: In document multi-fog-island-pier-ledger-013, the verified archive note records Moon Orchard Rest. Case record id: multi-document-013. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-fog-island-pier-ledger-013. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 5:

```text
document multi-old-quarry-path-travel-note-053::multi-document-053::1: In document multi-old-quarry-path-travel-note-053, the verified archive note records Moon Orchard Rest. Case record id: multi-document-053. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Scope reminder: document multi-old-quarry-path-travel-note-053. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Orchard Rest, carved shell comb, lantern hook`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22273 | n/a | 77.6315 |
| 2 | 22274 | n/a | 58.6287 |
| 3 | 21840 | n/a | 26.6359 |
| 4 | 21839 | n/a | 16.6741 |
| 5 | 21906 | n/a | 8.5148 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-document-073. Scoped answer summary for multi-document-073 repeats the grounded evidence set: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-memory-log-073::multi-document-073::2: In document multi-anya-memory-log-073, the verified archive note records lantern hook. Case record id: multi-document-073. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-anya-memory-log-073. Alias reminders for retrieval: lantern hook (aliases: preserved item lantern hook; la

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-document-073. Combined evidence: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-fog-island-pier-ledger-073::multi-document-073::1: In document multi-fog-island-pier-ledger-073, the verified archive note records Moon Orchard Rest. Case record id: multi-document-073. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-fog-island-pier-ledger-073. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 4:

```text
document multi-fog-island-pier-ledger-013::multi-document-013::1: In document multi-fog-island-pier-ledger-013, the verified archive note records Moon Orchard Rest. Case record id: multi-document-013. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-fog-island-pier-ledger-013. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 5:

```text
document multi-moon-orchard-rest-audio-transcript-013::multi-document-013::3: In document multi-moon-orchard-rest-audio-transcript-013, the verified archive note records brass compass. Case record id: multi-document-013. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-moon-orchard-rest-audio-transcript-013. Alias reminders for retrieval: brass compass (aliases: corroborating item brass compass; brass compass in the second document).
```

## Question 074: multi-document-074

**Question:** Which archive pieces from more than one document explain the family profile event at Moon Mill yard?

**Expected evidence:**
- marker `clay watering cup`
- aliases `archive piece clay watering cup, clay watering cup in the first archive piece`
- marker `canal route map`
- aliases `second archive piece canal route map, canal route map in the second archive piece`

**Forbidden evidence:**
- marker `willow basket`
- aliases `irrelevant document detail willow basket`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `canal route map, clay watering cup`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 1 < 2.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22275 | n/a | 65.3381 |
| 2 | 21904 | n/a | 4.4611 |
| 3 | 22011 | n/a | 4.3392 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-074. Scoped answer summary for multi-document-074 repeats the grounded evidence set: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece); canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-moon-mill-yard-minute-book-074::multi-document-074::1: In document multi-moon-mill-yard-minute-book-074, the verified archive note records clay watering cup. Case record id: multi-document-074. Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Scope reminder: document multi-moon-mill-yard-minute-book-074. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece).

do

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-moon-mill-yard-minute-book-014::multi-document-014::1: In document multi-moon-mill-yard-minute-book-014, the verified archive note records wax thread. Case record id: multi-document-014. Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Scope reminder: document multi-moon-mill-yard-minute-book-014. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

Chunk rank 3:

```text
document multi-yara-travel-note-014::multi-document-014::2: In document multi-yara-travel-note-014, the verified archive note records basalt sketch. Case record id: multi-document-014. Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Scope reminder: document multi-yara-travel-note-014. Alias reminders for retrieval: basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `canal route map, clay watering cup`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22275 | n/a | 65.4924 |
| 2 | 22276 | n/a | 46.3852 |
| 3 | 21905 | n/a | 26.4640 |
| 4 | 22012 | n/a | 26.4087 |
| 5 | 21904 | n/a | 4.5130 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-074. Scoped answer summary for multi-document-074 repeats the grounded evidence set: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece); canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-moon-mill-yard-minute-book-074::multi-document-074::1: In document multi-moon-mill-yard-minute-book-074, the verified archive note records clay watering cup. Case record id: multi-document-074. Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Scope reminder: document multi-moon-mill-yard-minute-book-074. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece).

do

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-074. Combined evidence: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece); canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-moon-mill-yard-minute-book-074::multi-document-074::1: In document multi-moon-mill-yard-minute-book-074, the verified archive note records clay watering cup. Case record id: multi-document-074. Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Scope reminder: document multi-moon-mill-yard-minute-book-074. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece).
```

Chunk rank 4:

```text
document multi-yara-travel-note-074::multi-document-074::2: In document multi-yara-travel-note-074, the verified archive note records canal route map. Case record id: multi-document-074. Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Scope reminder: document multi-yara-travel-note-074. Alias reminders for retrieval: canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece).
```

Chunk rank 5:

```text
document multi-moon-mill-yard-minute-book-014::multi-document-014::1: In document multi-moon-mill-yard-minute-book-014, the verified archive note records wax thread. Case record id: multi-document-014. Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Scope reminder: document multi-moon-mill-yard-minute-book-014. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

## Question 075: multi-document-075

**Question:** Which documents must be combined to understand Ada's boat manifest note about Driftwood cove?

**Expected evidence:**
- marker `saffron scarf`
- aliases `combined note saffron scarf, saffron scarf in one required document`
- marker `coal stove hiss`
- aliases `combined note coal stove hiss, coal stove hiss in another required document`
- marker `copper token`
- aliases `combined note copper token, copper token only visible after combining documents`

**Forbidden evidence:**
- marker `star ledger page`
- aliases `irrelevant document detail star ledger page`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, copper token, saffron scarf`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22277 | n/a | 77.1391 |
| 2 | 22278 | n/a | 58.1264 |
| 3 | 21793 | n/a | 9.9051 |
| 4 | 21883 | n/a | 1.8540 |
| 5 | 21791 | n/a | 1.6441 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Case scope id: multi-document-075. Scoped answer summary for multi-document-075 repeats the grounded evidence set: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-photo-index-075::multi-document-075::2: In document multi-ada-photo-index-075, the verified archive note records coal stove hiss. Case record id: multi-document-075. Question: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Scope reminder: document multi-ada-photo-index-075. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Case scope id: multi-document-075. Combined evidence: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ada-photo-index-015::multi-document-015::2: In document multi-ada-photo-index-015, the verified archive note records copper token. Case record id: multi-document-015. Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Scope reminder: document multi-ada-photo-index-015. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token in another required document).
```

Chunk rank 4:

```text
document multi-lantern-tide-repair-book-015::multi-document-015::3: In document multi-lantern-tide-repair-book-015, the verified archive note records silver booth token. Case record id: multi-document-015. Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Scope reminder: document multi-lantern-tide-repair-book-015. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

Chunk rank 5:

```text
document multi-ada-minute-book-035::multi-document-035::2: In document multi-ada-minute-book-035, the verified archive note records silver booth token. Case record id: multi-document-035. Question: Which documents must be combined to understand Ada's family note note about River Lantern inn? Scope reminder: document multi-ada-minute-book-035. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token in another required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, copper token, saffron scarf`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22277 | n/a | 77.0879 |
| 2 | 22278 | n/a | 58.0198 |
| 3 | 21833 | n/a | 26.0511 |
| 4 | 21794 | n/a | 25.9893 |
| 5 | 21884 | n/a | 25.9857 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Case scope id: multi-document-075. Scoped answer summary for multi-document-075 repeats the grounded evidence set: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-photo-index-075::multi-document-075::2: In document multi-ada-photo-index-075, the verified archive note records coal stove hiss. Case record id: multi-document-075. Question: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Scope reminder: document multi-ada-photo-index-075. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Case scope id: multi-document-075. Combined evidence: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-driftwood-cove-profile-page-075::multi-document-075::1: In document multi-driftwood-cove-profile-page-075, the verified archive note records saffron scarf. Case record id: multi-document-075. Question: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Scope reminder: document multi-driftwood-cove-profile-page-075. Alias reminders for retrieval: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document).
```

Chunk rank 4:

```text
document multi-ada-photo-index-075::multi-document-075::2: In document multi-ada-photo-index-075, the verified archive note records coal stove hiss. Case record id: multi-document-075. Question: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Scope reminder: document multi-ada-photo-index-075. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document).
```

Chunk rank 5:

```text
document multi-lantern-tide-repair-book-075::multi-document-075::3: In document multi-lantern-tide-repair-book-075, the verified archive note records copper token. Case record id: multi-document-075. Question: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Scope reminder: document multi-lantern-tide-repair-book-075. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token only visible after combining documents).
```

## Question 076: multi-document-076

**Question:** Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft?

**Expected evidence:**
- marker `blue glass jar`
- aliases `travel record blue glass jar, blue glass jar in one document`
- marker `tin key`
- aliases `supporting record tin key, tin key in another document`

**Forbidden evidence:**
- marker `silver booth token`
- aliases `irrelevant document detail silver booth token`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue glass jar, tin key`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22279 | n/a | 65.3625 |
| 2 | 22280 | n/a | 46.2472 |
| 3 | 21941 | n/a | 26.3757 |
| 4 | 21969 | n/a | 26.2348 |
| 5 | 21940 | n/a | 4.4233 |

Chunk rank 1:

```text
Question anchor: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-076. Scoped answer summary for multi-document-076 repeats the grounded evidence set: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ridge-post-loft-memory-log-076::multi-document-076::1: In document multi-ridge-post-loft-memory-log-076, the verified archive note records blue glass jar. Case record id: multi-document-076. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-ridge-post-loft-memory-log-076. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).

document multi-sonya-audio-transcript-076::multi-document-076::2: In document multi-sonya-audio-transc

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-076. Combined evidence: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ridge-post-loft-memory-log-076::multi-document-076::1: In document multi-ridge-post-loft-memory-log-076, the verified archive note records blue glass jar. Case record id: multi-document-076. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-ridge-post-loft-memory-log-076. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

Chunk rank 4:

```text
document multi-sonya-audio-transcript-076::multi-document-076::2: In document multi-sonya-audio-transcript-076, the verified archive note records tin key. Case record id: multi-document-076. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-sonya-audio-transcript-076. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 5:

```text
document multi-ridge-post-loft-memory-log-016::multi-document-016::1: In document multi-ridge-post-loft-memory-log-016, the verified archive note records amber lantern. Case record id: multi-document-016. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-ridge-post-loft-memory-log-016. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue glass jar, tin key`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22279 | n/a | 65.2603 |
| 2 | 22280 | n/a | 46.2175 |
| 3 | 21941 | n/a | 26.2698 |
| 4 | 21969 | n/a | 26.1415 |
| 5 | 21940 | n/a | 4.2496 |

Chunk rank 1:

```text
Question anchor: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-076. Scoped answer summary for multi-document-076 repeats the grounded evidence set: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ridge-post-loft-memory-log-076::multi-document-076::1: In document multi-ridge-post-loft-memory-log-076, the verified archive note records blue glass jar. Case record id: multi-document-076. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-ridge-post-loft-memory-log-076. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).

document multi-sonya-audio-transcript-076::multi-document-076::2: In document multi-sonya-audio-transc

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-076. Combined evidence: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ridge-post-loft-memory-log-076::multi-document-076::1: In document multi-ridge-post-loft-memory-log-076, the verified archive note records blue glass jar. Case record id: multi-document-076. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-ridge-post-loft-memory-log-076. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

Chunk rank 4:

```text
document multi-sonya-audio-transcript-076::multi-document-076::2: In document multi-sonya-audio-transcript-076, the verified archive note records tin key. Case record id: multi-document-076. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-sonya-audio-transcript-076. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 5:

```text
document multi-ridge-post-loft-memory-log-016::multi-document-016::1: In document multi-ridge-post-loft-memory-log-016, the verified archive note records amber lantern. Case record id: multi-document-016. Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Scope reminder: document multi-ridge-post-loft-memory-log-016. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

## Question 077: multi-document-077

**Question:** Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room?

**Expected evidence:**
- marker `Harvest Glow`
- aliases `festival Harvest Glow, the Harvest Glow record`
- marker `copper wind vane pin`
- aliases `preserved item copper wind vane pin, copper wind vane pin in the preserved record`
- marker `brass compass`
- aliases `corroborating item brass compass, brass compass in the second document`

**Forbidden evidence:**
- marker `birch tea flask`
- aliases `irrelevant document detail birch tea flask`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Harvest Glow, brass compass, copper wind vane pin`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22281 | n/a | 77.5982 |
| 2 | 21837 | n/a | 26.6860 |
| 3 | 21836 | n/a | 16.6860 |
| 4 | 21854 | n/a | 8.6848 |
| 5 | 21945 | n/a | 6.1623 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-077. Scoped answer summary for multi-document-077 repeats the grounded evidence set: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-east-signal-room-travel-note-077::multi-document-077::1: In document multi-east-signal-room-travel-note-077, the verified archive note records Harvest Glow. Case record id: multi-document-077. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-east-signal-room-travel-note-077. Alias reminders for retrieval: Harvest Glow (aliases: fes

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-east-signal-room-travel-note-077::multi-document-077::1: In document multi-east-signal-room-travel-note-077, the verified archive note records Harvest Glow. Case record id: multi-document-077. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-east-signal-room-travel-note-077. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

Chunk rank 3:

```text
document multi-east-signal-room-travel-note-017::multi-document-017::1: In document multi-east-signal-room-travel-note-017, the verified archive note records Harvest Glow. Case record id: multi-document-017. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-east-signal-room-travel-note-017. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

Chunk rank 4:

```text
document multi-harvest-glow-family-register-017::multi-document-017::3: In document multi-harvest-glow-family-register-017, the verified archive note records willow basket. Case record id: multi-document-017. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-harvest-glow-family-register-017. Alias reminders for retrieval: willow basket (aliases: corroborating item willow basket; willow basket in the second document).
```

Chunk rank 5:

```text
document multi-runa-archive-057::multi-document-057::2: In document multi-runa-archive-057, the verified archive note records lantern hook. Case record id: multi-document-057. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Scope reminder: document multi-runa-archive-057. Alias reminders for retrieval: lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Harvest Glow, brass compass, copper wind vane pin`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22281 | n/a | 77.5168 |
| 2 | 22282 | n/a | 58.4837 |
| 3 | 21837 | n/a | 26.5844 |
| 4 | 21836 | n/a | 16.6218 |
| 5 | 21854 | n/a | 8.4296 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-077. Scoped answer summary for multi-document-077 repeats the grounded evidence set: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-east-signal-room-travel-note-077::multi-document-077::1: In document multi-east-signal-room-travel-note-077, the verified archive note records Harvest Glow. Case record id: multi-document-077. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-east-signal-room-travel-note-077. Alias reminders for retrieval: Harvest Glow (aliases: fes

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-077. Combined evidence: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-east-signal-room-travel-note-077::multi-document-077::1: In document multi-east-signal-room-travel-note-077, the verified archive note records Harvest Glow. Case record id: multi-document-077. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-east-signal-room-travel-note-077. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

Chunk rank 4:

```text
document multi-east-signal-room-travel-note-017::multi-document-017::1: In document multi-east-signal-room-travel-note-017, the verified archive note records Harvest Glow. Case record id: multi-document-017. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-east-signal-room-travel-note-017. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

Chunk rank 5:

```text
document multi-harvest-glow-family-register-017::multi-document-017::3: In document multi-harvest-glow-family-register-017, the verified archive note records willow basket. Case record id: multi-document-017. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-harvest-glow-family-register-017. Alias reminders for retrieval: willow basket (aliases: corroborating item willow basket; willow basket in the second document).
```

## Question 078: multi-document-078

**Question:** Which archive pieces from more than one document explain the family profile event at South Meadow arch?

**Expected evidence:**
- marker `wax thread`
- aliases `archive piece wax thread, wax thread in the first archive piece`
- marker `basalt sketch`
- aliases `second archive piece basalt sketch, basalt sketch in the second archive piece`

**Forbidden evidence:**
- marker `oak barrel hoops`
- aliases `irrelevant document detail oak barrel hoops`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `basalt sketch, wax thread`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22283 | n/a | 65.5603 |
| 2 | 22284 | n/a | 46.4947 |
| 3 | 21980 | n/a | 26.5518 |
| 4 | 21872 | n/a | 26.3864 |
| 5 | 21979 | n/a | 4.5518 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-078. Scoped answer summary for multi-document-078 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-repair-book-078::multi-document-078::2: In document multi-iveta-repair-book-078, the verified archive note records basalt sketch. Case record id: multi-document-078. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-iveta-repair-book-078. Alias reminders for retrieval: basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece).

document multi-south-meadow-arch-photo-index-078::multi-do

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-078. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-south-meadow-arch-photo-index-078::multi-document-078::1: In document multi-south-meadow-arch-photo-index-078, the verified archive note records wax thread. Case record id: multi-document-078. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-south-meadow-arch-photo-index-078. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

Chunk rank 4:

```text
document multi-iveta-repair-book-078::multi-document-078::2: In document multi-iveta-repair-book-078, the verified archive note records basalt sketch. Case record id: multi-document-078. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-iveta-repair-book-078. Alias reminders for retrieval: basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece).
```

Chunk rank 5:

```text
document multi-south-meadow-arch-photo-index-018::multi-document-018::1: In document multi-south-meadow-arch-photo-index-018, the verified archive note records violet ribbon. Case record id: multi-document-018. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-south-meadow-arch-photo-index-018. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `basalt sketch, wax thread`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22283 | n/a | 65.4930 |
| 2 | 22284 | n/a | 46.4875 |
| 3 | 21980 | n/a | 26.5173 |
| 4 | 21979 | n/a | 4.4987 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-078. Scoped answer summary for multi-document-078 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-repair-book-078::multi-document-078::2: In document multi-iveta-repair-book-078, the verified archive note records basalt sketch. Case record id: multi-document-078. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-iveta-repair-book-078. Alias reminders for retrieval: basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece).

document multi-south-meadow-arch-photo-index-078::multi-do

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-078. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-south-meadow-arch-photo-index-078::multi-document-078::1: In document multi-south-meadow-arch-photo-index-078, the verified archive note records wax thread. Case record id: multi-document-078. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-south-meadow-arch-photo-index-078. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

Chunk rank 4:

```text
document multi-south-meadow-arch-photo-index-018::multi-document-018::1: In document multi-south-meadow-arch-photo-index-018, the verified archive note records violet ribbon. Case record id: multi-document-018. Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Scope reminder: document multi-south-meadow-arch-photo-index-018. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

## Question 079: multi-document-079

**Question:** Which documents must be combined to understand Zora's travel ledger note about Maple Court attic?

**Expected evidence:**
- marker `smoke vent chain`
- aliases `combined note smoke vent chain, smoke vent chain in one required document`
- marker `copper token`
- aliases `combined note copper token, copper token in another required document`
- marker `silver booth token`
- aliases `combined note silver booth token, silver booth token only visible after combining documents`

**Forbidden evidence:**
- marker `glass ink bottle`
- aliases `irrelevant document detail glass ink bottle`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `copper token, silver booth token, smoke vent chain`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22285 | n/a | 77.4433 |
| 2 | 22286 | n/a | 58.2730 |
| 3 | 21959 | n/a | 26.4931 |
| 4 | 21888 | n/a | 26.2975 |
| 5 | 21812 | n/a | 13.5246 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Case scope id: multi-document-079. Scoped answer summary for multi-document-079 repeats the grounded evidence set: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-maple-court-attic-audio-transcript-079::multi-document-079::1: In document multi-maple-court-attic-audio-transcript-079, the verified archive note records smoke vent chain. Case record id: multi-document-079. Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Scope reminder: document multi-maple-court-attic-audio-transcript-079. Alias reminders for re

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Case scope id: multi-document-079. Combined evidence: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-signal-lantern-morning-ledger-079::multi-document-079::3: In document multi-signal-lantern-morning-ledger-079, the verified archive note records silver booth token. Case record id: multi-document-079. Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Scope reminder: document multi-signal-lantern-morning-ledger-079. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

Chunk rank 4:

```text
document multi-maple-court-attic-audio-transcript-079::multi-document-079::1: In document multi-maple-court-attic-audio-transcript-079, the verified archive note records smoke vent chain. Case record id: multi-document-079. Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Scope reminder: document multi-maple-court-attic-audio-transcript-079. Alias reminders for retrieval: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document).
```

Chunk rank 5:

```text
document multi-bellwater-fair-ledger-031::multi-document-031::3: In document multi-bellwater-fair-ledger-031, the verified archive note records silver booth token. Case record id: multi-document-031. Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Scope reminder: document multi-bellwater-fair-ledger-031. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `copper token, silver booth token, smoke vent chain`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22285 | n/a | 77.2827 |
| 2 | 22286 | n/a | 58.1782 |
| 3 | 21888 | n/a | 26.3156 |
| 4 | 22016 | n/a | 26.1575 |
| 5 | 21959 | n/a | 26.1526 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Case scope id: multi-document-079. Scoped answer summary for multi-document-079 repeats the grounded evidence set: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-maple-court-attic-audio-transcript-079::multi-document-079::1: In document multi-maple-court-attic-audio-transcript-079, the verified archive note records smoke vent chain. Case record id: multi-document-079. Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Scope reminder: document multi-maple-court-attic-audio-transcript-079. Alias reminders for re

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Case scope id: multi-document-079. Combined evidence: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-maple-court-attic-audio-transcript-079::multi-document-079::1: In document multi-maple-court-attic-audio-transcript-079, the verified archive note records smoke vent chain. Case record id: multi-document-079. Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Scope reminder: document multi-maple-court-attic-audio-transcript-079. Alias reminders for retrieval: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document).
```

Chunk rank 4:

```text
document multi-zora-inventory-sheet-079::multi-document-079::2: In document multi-zora-inventory-sheet-079, the verified archive note records copper token. Case record id: multi-document-079. Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Scope reminder: document multi-zora-inventory-sheet-079. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token in another required document).
```

Chunk rank 5:

```text
document multi-signal-lantern-morning-ledger-079::multi-document-079::3: In document multi-signal-lantern-morning-ledger-079, the verified archive note records silver booth token. Case record id: multi-document-079. Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Scope reminder: document multi-signal-lantern-morning-ledger-079. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

## Question 080: multi-document-080

**Question:** Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery?

**Expected evidence:**
- marker `amber lantern`
- aliases `travel record amber lantern, amber lantern in one document`
- marker `tuning fork`
- aliases `supporting record tuning fork, tuning fork in another document`

**Forbidden evidence:**
- marker `weathered camera strap`
- aliases `irrelevant document detail weathered camera strap`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `amber lantern, tuning fork`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22287 | n/a | 65.3101 |
| 2 | 21982 | n/a | 26.3314 |
| 3 | 21895 | n/a | 4.5360 |
| 4 | 21981 | n/a | 4.3620 |
| 5 | 21894 | n/a | 1.9825 |

Chunk rank 1:

```text
Question anchor: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Case scope id: multi-document-080. Scoped answer summary for multi-document-080 repeats the grounded evidence set: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-mira-family-register-080::multi-document-080::2: In document multi-mira-family-register-080, the verified archive note records tuning fork. Case record id: multi-document-080. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-mira-family-register-080. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).

document multi-star-basin-gallery-letter-roll-080::multi-document-080::1: In document multi-star-basin-

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-star-basin-gallery-letter-roll-080::multi-document-080::1: In document multi-star-basin-gallery-letter-roll-080, the verified archive note records amber lantern. Case record id: multi-document-080. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-star-basin-gallery-letter-roll-080. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 3:

```text
document multi-mira-family-register-020::multi-document-020::2: In document multi-mira-family-register-020, the verified archive note records birch tea flask. Case record id: multi-document-020. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-mira-family-register-020. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 4:

```text
document multi-star-basin-gallery-letter-roll-020::multi-document-020::1: In document multi-star-basin-gallery-letter-roll-020, the verified archive note records linen wick. Case record id: multi-document-020. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-star-basin-gallery-letter-roll-020. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 5:

```text
document multi-mira-audio-transcript-100::multi-document-100::2: In document multi-mira-audio-transcript-100, the verified archive note records birch tea flask. Case record id: multi-document-100. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-mira-audio-transcript-100. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `amber lantern, tuning fork`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22287 | n/a | 65.3102 |
| 2 | 22288 | n/a | 46.2389 |
| 3 | 21982 | n/a | 26.2960 |
| 4 | 21896 | n/a | 26.1829 |
| 5 | 21981 | n/a | 4.2638 |

Chunk rank 1:

```text
Question anchor: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Case scope id: multi-document-080. Scoped answer summary for multi-document-080 repeats the grounded evidence set: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-mira-family-register-080::multi-document-080::2: In document multi-mira-family-register-080, the verified archive note records tuning fork. Case record id: multi-document-080. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-mira-family-register-080. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).

document multi-star-basin-gallery-letter-roll-080::multi-document-080::1: In document multi-star-basin-

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Case scope id: multi-document-080. Combined evidence: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-star-basin-gallery-letter-roll-080::multi-document-080::1: In document multi-star-basin-gallery-letter-roll-080, the verified archive note records amber lantern. Case record id: multi-document-080. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-star-basin-gallery-letter-roll-080. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 4:

```text
document multi-mira-family-register-080::multi-document-080::2: In document multi-mira-family-register-080, the verified archive note records tuning fork. Case record id: multi-document-080. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-mira-family-register-080. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

Chunk rank 5:

```text
document multi-star-basin-gallery-letter-roll-020::multi-document-020::1: In document multi-star-basin-gallery-letter-roll-020, the verified archive note records linen wick. Case record id: multi-document-020. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-star-basin-gallery-letter-roll-020. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

## Question 081: multi-document-081

**Question:** Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse?

**Expected evidence:**
- marker `Bellwater Fair`
- aliases `festival Bellwater Fair, the Bellwater Fair record`
- marker `cedar shovel`
- aliases `preserved item cedar shovel, cedar shovel in the preserved record`
- marker `willow basket`
- aliases `corroborating item willow basket, willow basket in the second document`

**Forbidden evidence:**
- marker `juniper bundles`
- aliases `irrelevant document detail juniper bundles`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Bellwater Fair, cedar shovel, willow basket`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22289 | n/a | 77.6048 |
| 2 | 22290 | n/a | 58.5799 |
| 3 | 21967 | n/a | 26.6571 |
| 4 | 21966 | n/a | 16.6571 |
| 5 | 21938 | n/a | 14.0636 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-document-081. Scoped answer summary for multi-document-081 repeats the grounded evidence set: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-profile-page-081::multi-document-081::3: In document multi-bellwater-fair-profile-page-081, the verified archive note records willow basket. Case record id: multi-document-081. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-bellwater-fair-profile-page-081. Alias reminders for retrieval: willow basket (aliases: corr

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-document-081. Combined evidence: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-snow-orchard-storehouse-repair-book-081::multi-document-081::1: In document multi-snow-orchard-storehouse-repair-book-081, the verified archive note records Bellwater Fair. Case record id: multi-document-081. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-snow-orchard-storehouse-repair-book-081. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

Chunk rank 4:

```text
document multi-snow-orchard-storehouse-repair-book-021::multi-document-021::1: In document multi-snow-orchard-storehouse-repair-book-021, the verified archive note records Bellwater Fair. Case record id: multi-document-021. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-snow-orchard-storehouse-repair-book-021. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

Chunk rank 5:

```text
document multi-pine-gate-yard-travel-note-041::multi-document-041::1: In document multi-pine-gate-yard-travel-note-041, the verified archive note records Bellwater Fair. Case record id: multi-document-041. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Scope reminder: document multi-pine-gate-yard-travel-note-041. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Bellwater Fair, cedar shovel, willow basket`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22289 | n/a | 77.4824 |
| 2 | 22290 | n/a | 58.4809 |
| 3 | 21985 | n/a | 30.3855 |
| 4 | 21967 | n/a | 26.4800 |
| 5 | 21966 | n/a | 16.5173 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-document-081. Scoped answer summary for multi-document-081 repeats the grounded evidence set: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-profile-page-081::multi-document-081::3: In document multi-bellwater-fair-profile-page-081, the verified archive note records willow basket. Case record id: multi-document-081. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-bellwater-fair-profile-page-081. Alias reminders for retrieval: willow basket (aliases: corr

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-document-081. Combined evidence: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-vera-archive-081::multi-document-081::2: In document multi-vera-archive-081, the verified archive note records cedar shovel. Case record id: multi-document-081. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-vera-archive-081. Alias reminders for retrieval: cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record).
```

Chunk rank 4:

```text
document multi-snow-orchard-storehouse-repair-book-081::multi-document-081::1: In document multi-snow-orchard-storehouse-repair-book-081, the verified archive note records Bellwater Fair. Case record id: multi-document-081. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-snow-orchard-storehouse-repair-book-081. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

Chunk rank 5:

```text
document multi-snow-orchard-storehouse-repair-book-021::multi-document-021::1: In document multi-snow-orchard-storehouse-repair-book-021, the verified archive note records Bellwater Fair. Case record id: multi-document-021. Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Scope reminder: document multi-snow-orchard-storehouse-repair-book-021. Alias reminders for retrieval: Bellwater Fair (aliases: festival Bellwater Fair; the Bellwater Fair record).
```

## Question 082: multi-document-082

**Question:** Which archive pieces from more than one document explain the family profile event at Cedar Hill station?

**Expected evidence:**
- marker `violet ribbon`
- aliases `archive piece violet ribbon, violet ribbon in the first archive piece`
- marker `star ledger page`
- aliases `second archive piece star ledger page, star ledger page in the second archive piece`

**Forbidden evidence:**
- marker `carved shell comb`
- aliases `irrelevant document detail carved shell comb`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `star ledger page, violet ribbon`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22291 | n/a | 65.3342 |
| 2 | 21827 | n/a | 26.3427 |
| 3 | 21826 | n/a | 4.3427 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Case scope id: multi-document-082. Scoped answer summary for multi-document-082 repeats the grounded evidence set: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-cedar-hill-station-inventory-sheet-082::multi-document-082::1: In document multi-cedar-hill-station-inventory-sheet-082, the verified archive note records violet ribbon. Case record id: multi-document-082. Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Scope reminder: document multi-cedar-hill-station-inventory-sheet-082. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piec

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-cedar-hill-station-inventory-sheet-082::multi-document-082::1: In document multi-cedar-hill-station-inventory-sheet-082, the verified archive note records violet ribbon. Case record id: multi-document-082. Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Scope reminder: document multi-cedar-hill-station-inventory-sheet-082. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

Chunk rank 3:

```text
document multi-cedar-hill-station-inventory-sheet-022::multi-document-022::1: In document multi-cedar-hill-station-inventory-sheet-022, the verified archive note records moonflower cutting. Case record id: multi-document-022. Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Scope reminder: document multi-cedar-hill-station-inventory-sheet-022. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

### Model: bge_m3

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `violet ribbon, star ledger page`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: violet ribbon, star ledger page; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 140 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

## Question 083: multi-document-083

**Question:** Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path?

**Expected evidence:**
- marker `blue oar`
- aliases `combined note blue oar, blue oar in one required document`
- marker `silver booth token`
- aliases `combined note silver booth token, silver booth token in another required document`
- marker `weathered camera strap`
- aliases `combined note weathered camera strap, weathered camera strap only visible after combining documents`

**Forbidden evidence:**
- marker `canal route map`
- aliases `irrelevant document detail canal route map`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue oar, silver booth token, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22293 | n/a | 77.5339 |
| 2 | 22294 | n/a | 58.2961 |
| 3 | 21934 | n/a | 26.5285 |
| 4 | 21805 | n/a | 26.4667 |
| 5 | 21804 | n/a | 9.9529 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Case scope id: multi-document-083. Scoped answer summary for multi-document-083 repeats the grounded evidence set: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-minute-book-083::multi-document-083::2: In document multi-anya-minute-book-083, the verified archive note records silver booth token. Case record id: multi-document-083. Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Scope reminder: document multi-anya-minute-book-083. Alias reminders for retrieval: silver booth token (aliases: comb

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Case scope id: multi-document-083. Combined evidence: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-old-quarry-path-family-register-083::multi-document-083::1: In document multi-old-quarry-path-family-register-083, the verified archive note records blue oar. Case record id: multi-document-083. Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Scope reminder: document multi-old-quarry-path-family-register-083. Alias reminders for retrieval: blue oar (aliases: combined note blue oar; blue oar in one required document).
```

Chunk rank 4:

```text
document multi-anya-minute-book-083::multi-document-083::2: In document multi-anya-minute-book-083, the verified archive note records silver booth token. Case record id: multi-document-083. Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Scope reminder: document multi-anya-minute-book-083. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token in another required document).
```

Chunk rank 5:

```text
document multi-anya-minute-book-023::multi-document-023::2: In document multi-anya-minute-book-023, the verified archive note records weathered camera strap. Case record id: multi-document-023. Question: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Scope reminder: document multi-anya-minute-book-023. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue oar, silver booth token, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22293 | n/a | 77.2131 |
| 2 | 22294 | n/a | 58.1679 |
| 3 | 21934 | n/a | 26.2392 |
| 4 | 21805 | n/a | 26.1121 |
| 5 | 21914 | n/a | 26.0727 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Case scope id: multi-document-083. Scoped answer summary for multi-document-083 repeats the grounded evidence set: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-minute-book-083::multi-document-083::2: In document multi-anya-minute-book-083, the verified archive note records silver booth token. Case record id: multi-document-083. Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Scope reminder: document multi-anya-minute-book-083. Alias reminders for retrieval: silver booth token (aliases: comb

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Case scope id: multi-document-083. Combined evidence: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-old-quarry-path-family-register-083::multi-document-083::1: In document multi-old-quarry-path-family-register-083, the verified archive note records blue oar. Case record id: multi-document-083. Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Scope reminder: document multi-old-quarry-path-family-register-083. Alias reminders for retrieval: blue oar (aliases: combined note blue oar; blue oar in one required document).
```

Chunk rank 4:

```text
document multi-anya-minute-book-083::multi-document-083::2: In document multi-anya-minute-book-083, the verified archive note records silver booth token. Case record id: multi-document-083. Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Scope reminder: document multi-anya-minute-book-083. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token in another required document).
```

Chunk rank 5:

```text
document multi-moon-orchard-rest-travel-note-083::multi-document-083::3: In document multi-moon-orchard-rest-travel-note-083, the verified archive note records weathered camera strap. Case record id: multi-document-083. Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Scope reminder: document multi-moon-orchard-rest-travel-note-083. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents).
```

## Question 084: multi-document-084

**Question:** Which records together show how Yara prepared the canal barge stop near Cloud Wharf office?

**Expected evidence:**
- marker `linen wick`
- aliases `travel record linen wick, linen wick in one document`
- marker `birch tea flask`
- aliases `supporting record birch tea flask, birch tea flask in another document`

**Forbidden evidence:**
- marker `coal stove hiss`
- aliases `irrelevant document detail coal stove hiss`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `birch tea flask, linen wick`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22295 | n/a | 65.5056 |
| 2 | 22296 | n/a | 46.2722 |
| 3 | 21830 | n/a | 26.5603 |
| 4 | 22009 | n/a | 26.3727 |
| 5 | 21829 | n/a | 4.4375 |

Chunk rank 1:

```text
Question anchor: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-084. Scoped answer summary for multi-document-084 repeats the grounded evidence set: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records linen wick. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-084. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).

document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084,

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-084. Combined evidence: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records linen wick. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-084. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 4:

```text
document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-yara-profile-page-084. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 5:

```text
document multi-cloud-wharf-office-archive-024::multi-document-024::1: In document multi-cloud-wharf-office-archive-024, the verified archive note records paper moon mask. Case record id: multi-document-024. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-024. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `birch tea flask, linen wick`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22295 | n/a | 65.2626 |
| 2 | 22296 | n/a | 46.1448 |
| 3 | 21830 | n/a | 26.2986 |
| 4 | 22009 | n/a | 26.1567 |
| 5 | 21829 | n/a | 4.2608 |

Chunk rank 1:

```text
Question anchor: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-084. Scoped answer summary for multi-document-084 repeats the grounded evidence set: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records linen wick. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-084. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).

document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084,

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-084. Combined evidence: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records linen wick. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-084. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 4:

```text
document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case record id: multi-document-084. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-yara-profile-page-084. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 5:

```text
document multi-cloud-wharf-office-archive-024::multi-document-024::1: In document multi-cloud-wharf-office-archive-024, the verified archive note records paper moon mask. Case record id: multi-document-024. Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Scope reminder: document multi-cloud-wharf-office-archive-024. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).
```

## Question 085: multi-document-085

**Question:** Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor?

**Expected evidence:**
- marker `Lantern Tide`
- aliases `festival Lantern Tide, the Lantern Tide record`
- marker `green apron`
- aliases `preserved item green apron, green apron in the preserved record`
- marker `oak barrel hoops`
- aliases `corroborating item oak barrel hoops, oak barrel hoops in the second document`

**Forbidden evidence:**
- marker `tin key`
- aliases `irrelevant document detail tin key`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Tide, green apron, oak barrel hoops`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22297 | n/a | 77.6440 |
| 2 | 22298 | n/a | 58.5087 |
| 3 | 21790 | n/a | 30.5274 |
| 4 | 21879 | n/a | 30.4770 |
| 5 | 21851 | n/a | 26.5463 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-document-085. Scoped answer summary for multi-document-085 repeats the grounded evidence set: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-memory-log-085::multi-document-085::2: In document multi-ada-memory-log-085, the verified archive note records green apron. Case record id: multi-document-085. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-ada-memory-log-085. Alias reminders for retrieval: green apron (aliases: preserved item green apron; green apron in the preserved

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-document-085. Combined evidence: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ada-memory-log-085::multi-document-085::2: In document multi-ada-memory-log-085, the verified archive note records green apron. Case record id: multi-document-085. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-ada-memory-log-085. Alias reminders for retrieval: green apron (aliases: preserved item green apron; green apron in the preserved record).
```

Chunk rank 4:

```text
document multi-lantern-tide-audio-transcript-085::multi-document-085::3: In document multi-lantern-tide-audio-transcript-085, the verified archive note records oak barrel hoops. Case record id: multi-document-085. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-lantern-tide-audio-transcript-085. Alias reminders for retrieval: oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document).
```

Chunk rank 5:

```text
document multi-harbor-glass-corridor-ledger-085::multi-document-085::1: In document multi-harbor-glass-corridor-ledger-085, the verified archive note records Lantern Tide. Case record id: multi-document-085. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-harbor-glass-corridor-ledger-085. Alias reminders for retrieval: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Tide, green apron, oak barrel hoops`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22297 | n/a | 77.5028 |
| 2 | 22298 | n/a | 58.4312 |
| 3 | 21790 | n/a | 30.4153 |
| 4 | 21851 | n/a | 26.5099 |
| 5 | 21850 | n/a | 16.5099 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-document-085. Scoped answer summary for multi-document-085 repeats the grounded evidence set: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-memory-log-085::multi-document-085::2: In document multi-ada-memory-log-085, the verified archive note records green apron. Case record id: multi-document-085. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-ada-memory-log-085. Alias reminders for retrieval: green apron (aliases: preserved item green apron; green apron in the preserved

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-document-085. Combined evidence: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record); green apron (aliases: preserved item green apron; green apron in the preserved record); oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-ada-memory-log-085::multi-document-085::2: In document multi-ada-memory-log-085, the verified archive note records green apron. Case record id: multi-document-085. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-ada-memory-log-085. Alias reminders for retrieval: green apron (aliases: preserved item green apron; green apron in the preserved record).
```

Chunk rank 4:

```text
document multi-harbor-glass-corridor-ledger-085::multi-document-085::1: In document multi-harbor-glass-corridor-ledger-085, the verified archive note records Lantern Tide. Case record id: multi-document-085. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-harbor-glass-corridor-ledger-085. Alias reminders for retrieval: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record).
```

Chunk rank 5:

```text
document multi-harbor-glass-corridor-ledger-025::multi-document-025::1: In document multi-harbor-glass-corridor-ledger-025, the verified archive note records Lantern Tide. Case record id: multi-document-025. Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Scope reminder: document multi-harbor-glass-corridor-ledger-025. Alias reminders for retrieval: Lantern Tide (aliases: festival Lantern Tide; the Lantern Tide record).
```

## Question 086: multi-document-086

**Question:** Which archive pieces from more than one document explain the family profile event at North Orchard lane?

**Expected evidence:**
- marker `moonflower cutting`
- aliases `archive piece moonflower cutting, moonflower cutting in the first archive piece`
- marker `glass ink bottle`
- aliases `second archive piece glass ink bottle, glass ink bottle in the second archive piece`

**Forbidden evidence:**
- marker `brass compass`
- aliases `irrelevant document detail brass compass`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `glass ink bottle, moonflower cutting`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22299 | n/a | 65.5274 |
| 2 | 22300 | n/a | 46.4102 |
| 3 | 21932 | n/a | 26.4611 |
| 4 | 21977 | n/a | 26.3392 |
| 5 | 21931 | n/a | 4.3938 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Scoped answer summary for multi-document-086 repeats the grounded evidence set: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note records moonflower cutting. Case record id: multi-document-086. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-086. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note records moonflower cutting. Case record id: multi-document-086. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-086. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

Chunk rank 4:

```text
document multi-sonya-travel-note-086::multi-document-086::2: In document multi-sonya-travel-note-086, the verified archive note records glass ink bottle. Case record id: multi-document-086. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-sonya-travel-note-086. Alias reminders for retrieval: glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece).
```

Chunk rank 5:

```text
document multi-north-orchard-lane-minute-book-026::multi-document-026::1: In document multi-north-orchard-lane-minute-book-026, the verified archive note records clay watering cup. Case record id: multi-document-026. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-026. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `glass ink bottle, moonflower cutting`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22299 | n/a | 65.5665 |
| 2 | 22300 | n/a | 46.4791 |
| 3 | 21932 | n/a | 26.5332 |
| 4 | 21977 | n/a | 26.4719 |
| 5 | 22140 | n/a | 13.9106 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Scoped answer summary for multi-document-086 repeats the grounded evidence set: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note records moonflower cutting. Case record id: multi-document-086. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-086. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note records moonflower cutting. Case record id: multi-document-086. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-north-orchard-lane-minute-book-086. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

Chunk rank 4:

```text
document multi-sonya-travel-note-086::multi-document-086::2: In document multi-sonya-travel-note-086, the verified archive note records glass ink bottle. Case record id: multi-document-086. Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Scope reminder: document multi-sonya-travel-note-086. Alias reminders for retrieval: glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece).
```

Chunk rank 5:

```text
Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006. Combined evidence: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece); glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 087: multi-document-087

**Question:** Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade?

**Expected evidence:**
- marker `rope bridge permit`
- aliases `combined note rope bridge permit, rope bridge permit in one required document`
- marker `weathered camera strap`
- aliases `combined note weathered camera strap, weathered camera strap in another required document`
- marker `coal stove hiss`
- aliases `combined note coal stove hiss, coal stove hiss only visible after combining documents`

**Forbidden evidence:**
- marker `basalt sketch`
- aliases `irrelevant document detail basalt sketch`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, rope bridge permit, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22301 | n/a | 77.5895 |
| 2 | 22302 | n/a | 58.4781 |
| 3 | 21863 | n/a | 26.6680 |
| 4 | 22141 | n/a | 15.6893 |
| 5 | 21862 | n/a | 2.3604 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Case scope id: multi-document-087. Scoped answer summary for multi-document-087 repeats the grounded evidence set: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-harvest-glow-repair-book-087::multi-document-087::3: In document multi-harvest-glow-repair-book-087, the verified archive note records coal stove hiss. Case record id: multi-document-087. Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Scope reminder: document multi-harvest-glow-repair-book-087. Alias reminder

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Case scope id: multi-document-087. Combined evidence: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-hollow-market-arcade-profile-page-087::multi-document-087::1: In document multi-hollow-market-arcade-profile-page-087, the verified archive note records rope bridge permit. Case record id: multi-document-087. Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Scope reminder: document multi-hollow-market-arcade-profile-page-087. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 4:

```text
Question anchor: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Case scope id: multi-document-007. Scoped answer summary for multi-document-007 repeats the grounded evidence set: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-fox-hollow-bridge-audio-transcript-007::multi-document-007::1: In document multi-fox-hollow-bridge-audio-transcript-007, the verified archive note records rope bridge permit. Case record id: multi-document-007. Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-audio-transcript-00

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
document multi-hollow-market-arcade-profile-page-027::multi-document-027::1: In document multi-hollow-market-arcade-profile-page-027, the verified archive note records saffron scarf. Case record id: multi-document-027. Question: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade? Scope reminder: document multi-hollow-market-arcade-profile-page-027. Alias reminders for retrieval: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, rope bridge permit, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22301 | n/a | 77.3214 |
| 2 | 22302 | n/a | 58.2745 |
| 3 | 21863 | n/a | 26.3071 |
| 4 | 21954 | n/a | 26.2175 |
| 5 | 21860 | n/a | 26.2161 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Case scope id: multi-document-087. Scoped answer summary for multi-document-087 repeats the grounded evidence set: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-harvest-glow-repair-book-087::multi-document-087::3: In document multi-harvest-glow-repair-book-087, the verified archive note records coal stove hiss. Case record id: multi-document-087. Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Scope reminder: document multi-harvest-glow-repair-book-087. Alias reminder

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Case scope id: multi-document-087. Combined evidence: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-hollow-market-arcade-profile-page-087::multi-document-087::1: In document multi-hollow-market-arcade-profile-page-087, the verified archive note records rope bridge permit. Case record id: multi-document-087. Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Scope reminder: document multi-hollow-market-arcade-profile-page-087. Alias reminders for retrieval: rope bridge permit (aliases: combined note rope bridge permit; rope bridge permit in one required document).
```

Chunk rank 4:

```text
document multi-runa-photo-index-087::multi-document-087::2: In document multi-runa-photo-index-087, the verified archive note records weathered camera strap. Case record id: multi-document-087. Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Scope reminder: document multi-runa-photo-index-087. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document).
```

Chunk rank 5:

```text
document multi-harvest-glow-repair-book-087::multi-document-087::3: In document multi-harvest-glow-repair-book-087, the verified archive note records coal stove hiss. Case record id: multi-document-087. Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Scope reminder: document multi-harvest-glow-repair-book-087. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss only visible after combining documents).
```

## Question 088: multi-document-088

**Question:** Which records together show how Iveta prepared the winter coach stop near Marble stair hall?

**Expected evidence:**
- marker `paper moon mask`
- aliases `travel record paper moon mask, paper moon mask in one document`
- marker `juniper bundles`
- aliases `supporting record juniper bundles, juniper bundles in another document`

**Forbidden evidence:**
- marker `copper token`
- aliases `irrelevant document detail copper token`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `juniper bundles, paper moon mask`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22303 | n/a | 65.2147 |
| 2 | 21866 | n/a | 26.2015 |
| 3 | 21891 | n/a | 4.2041 |
| 4 | 21865 | n/a | 4.2015 |
| 5 | 21868 | n/a | 1.8129 |

Chunk rank 1:

```text
Question anchor: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Case scope id: multi-document-088. Scoped answer summary for multi-document-088 repeats the grounded evidence set: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-audio-transcript-088::multi-document-088::2: In document multi-iveta-audio-transcript-088, the verified archive note records juniper bundles. Case record id: multi-document-088. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-iveta-audio-transcript-088. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).

document multi-marble-stair-hall-memory-log-088::multi-document-088::

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-iveta-audio-transcript-088::multi-document-088::2: In document multi-iveta-audio-transcript-088, the verified archive note records juniper bundles. Case record id: multi-document-088. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-iveta-audio-transcript-088. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

Chunk rank 3:

```text
document multi-marble-stair-hall-memory-log-028::multi-document-028::1: In document multi-marble-stair-hall-memory-log-028, the verified archive note records blue glass jar. Case record id: multi-document-028. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-marble-stair-hall-memory-log-028. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

Chunk rank 4:

```text
document multi-iveta-audio-transcript-028::multi-document-028::2: In document multi-iveta-audio-transcript-028, the verified archive note records tin key. Case record id: multi-document-028. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-iveta-audio-transcript-028. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 5:

```text
document multi-iveta-family-register-068::multi-document-068::2: In document multi-iveta-family-register-068, the verified archive note records birch tea flask. Case record id: multi-document-068. Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Scope reminder: document multi-iveta-family-register-068. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `juniper bundles, paper moon mask`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22303 | n/a | 65.2650 |
| 2 | 22304 | n/a | 46.1905 |
| 3 | 21892 | n/a | 26.2023 |
| 4 | 21866 | n/a | 26.1944 |
| 5 | 21891 | n/a | 4.2125 |

Chunk rank 1:

```text
Question anchor: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Case scope id: multi-document-088. Scoped answer summary for multi-document-088 repeats the grounded evidence set: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-audio-transcript-088::multi-document-088::2: In document multi-iveta-audio-transcript-088, the verified archive note records juniper bundles. Case record id: multi-document-088. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-iveta-audio-transcript-088. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).

document multi-marble-stair-hall-memory-log-088::multi-document-088::

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Case scope id: multi-document-088. Combined evidence: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document); juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-marble-stair-hall-memory-log-088::multi-document-088::1: In document multi-marble-stair-hall-memory-log-088, the verified archive note records paper moon mask. Case record id: multi-document-088. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-marble-stair-hall-memory-log-088. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).
```

Chunk rank 4:

```text
document multi-iveta-audio-transcript-088::multi-document-088::2: In document multi-iveta-audio-transcript-088, the verified archive note records juniper bundles. Case record id: multi-document-088. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-iveta-audio-transcript-088. Alias reminders for retrieval: juniper bundles (aliases: supporting record juniper bundles; juniper bundles in another document).
```

Chunk rank 5:

```text
document multi-marble-stair-hall-memory-log-028::multi-document-028::1: In document multi-marble-stair-hall-memory-log-028, the verified archive note records blue glass jar. Case record id: multi-document-028. Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Scope reminder: document multi-marble-stair-hall-memory-log-028. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

## Question 089: multi-document-089

**Question:** Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock?

**Expected evidence:**
- marker `Signal Lantern Morning`
- aliases `festival Signal Lantern Morning, the Signal Lantern Morning record`
- marker `lantern hook`
- aliases `preserved item lantern hook, lantern hook in the preserved record`
- marker `carved shell comb`
- aliases `corroborating item carved shell comb, carved shell comb in the second document`

**Forbidden evidence:**
- marker `tuning fork`
- aliases `irrelevant document detail tuning fork`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning, carved shell comb, lantern hook`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22305 | n/a | 77.7208 |
| 2 | 22306 | n/a | 58.5613 |
| 3 | 22018 | n/a | 30.5230 |
| 4 | 21957 | n/a | 30.4867 |
| 5 | 21797 | n/a | 26.7980 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-document-089. Scoped answer summary for multi-document-089 repeats the grounded evidence set: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-amber-canal-lock-travel-note-089::multi-document-089::1: In document multi-amber-canal-lock-travel-note-089, the verified archive note records Signal Lantern Morning. Case record id: multi-document-089. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-amber-canal-lock-travel-note-089. Alias rem

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-document-089. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-zora-letter-roll-089::multi-document-089::2: In document multi-zora-letter-roll-089, the verified archive note records lantern hook. Case record id: multi-document-089. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-zora-letter-roll-089. Alias reminders for retrieval: lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record).
```

Chunk rank 4:

```text
document multi-signal-lantern-morning-family-register-089::multi-document-089::3: In document multi-signal-lantern-morning-family-register-089, the verified archive note records carved shell comb. Case record id: multi-document-089. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-signal-lantern-morning-family-register-089. Alias reminders for retrieval: carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document).
```

Chunk rank 5:

```text
document multi-amber-canal-lock-travel-note-089::multi-document-089::1: In document multi-amber-canal-lock-travel-note-089, the verified archive note records Signal Lantern Morning. Case record id: multi-document-089. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-amber-canal-lock-travel-note-089. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning, carved shell comb, lantern hook`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22305 | n/a | 77.5587 |
| 2 | 22306 | n/a | 58.5614 |
| 3 | 21957 | n/a | 30.4417 |
| 4 | 21797 | n/a | 26.5765 |
| 5 | 22146 | n/a | 26.1151 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-document-089. Scoped answer summary for multi-document-089 repeats the grounded evidence set: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-amber-canal-lock-travel-note-089::multi-document-089::1: In document multi-amber-canal-lock-travel-note-089, the verified archive note records Signal Lantern Morning. Case record id: multi-document-089. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-amber-canal-lock-travel-note-089. Alias rem

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-document-089. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-signal-lantern-morning-family-register-089::multi-document-089::3: In document multi-signal-lantern-morning-family-register-089, the verified archive note records carved shell comb. Case record id: multi-document-089. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-signal-lantern-morning-family-register-089. Alias reminders for retrieval: carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document).
```

Chunk rank 4:

```text
document multi-amber-canal-lock-travel-note-089::multi-document-089::1: In document multi-amber-canal-lock-travel-note-089, the verified archive note records Signal Lantern Morning. Case record id: multi-document-089. Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Scope reminder: document multi-amber-canal-lock-travel-note-089. Alias reminders for retrieval: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record).
```

Chunk rank 5:

```text
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-document-009. Combined evidence: Signal Lantern Morning (aliases: festival Signal Lantern Morning; the Signal Lantern Morning record); lantern hook (aliases: preserved item lantern hook; lantern hook in the preserved record); carved shell comb (aliases: corroborating item carved shell comb; carved shell comb in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 090: multi-document-090

**Question:** Which archive pieces from more than one document explain the family profile event at Bell Bridge square?

**Expected evidence:**
- marker `clay watering cup`
- aliases `archive piece clay watering cup, clay watering cup in the first archive piece`
- marker `canal route map`
- aliases `second archive piece canal route map, canal route map in the second archive piece`

**Forbidden evidence:**
- marker `willow basket`
- aliases `irrelevant document detail willow basket`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `canal route map, clay watering cup`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22307 | n/a | 65.3995 |
| 2 | 21809 | n/a | 26.3938 |
| 3 | 21808 | n/a | 4.4611 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-090. Scoped answer summary for multi-document-090 repeats the grounded evidence set: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece); canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bell-bridge-square-photo-index-090::multi-document-090::1: In document multi-bell-bridge-square-photo-index-090, the verified archive note records clay watering cup. Case record id: multi-document-090. Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Scope reminder: document multi-bell-bridge-square-photo-index-090. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-bell-bridge-square-photo-index-090::multi-document-090::1: In document multi-bell-bridge-square-photo-index-090, the verified archive note records clay watering cup. Case record id: multi-document-090. Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Scope reminder: document multi-bell-bridge-square-photo-index-090. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece).
```

Chunk rank 3:

```text
document multi-bell-bridge-square-photo-index-030::multi-document-030::1: In document multi-bell-bridge-square-photo-index-030, the verified archive note records wax thread. Case record id: multi-document-030. Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Scope reminder: document multi-bell-bridge-square-photo-index-030. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

### Model: bge_m3

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `canal route map, clay watering cup`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 1 < 2.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22307 | n/a | 65.4085 |
| 2 | 21808 | n/a | 4.5221 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-090. Scoped answer summary for multi-document-090 repeats the grounded evidence set: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first archive piece); canal route map (aliases: second archive piece canal route map; canal route map in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bell-bridge-square-photo-index-090::multi-document-090::1: In document multi-bell-bridge-square-photo-index-090, the verified archive note records clay watering cup. Case record id: multi-document-090. Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Scope reminder: document multi-bell-bridge-square-photo-index-090. Alias reminders for retrieval: clay watering cup (aliases: archive piece clay watering cup; clay watering cup in the first

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-bell-bridge-square-photo-index-030::multi-document-030::1: In document multi-bell-bridge-square-photo-index-030, the verified archive note records wax thread. Case record id: multi-document-030. Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Scope reminder: document multi-bell-bridge-square-photo-index-030. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

## Question 091: multi-document-091

**Question:** Which documents must be combined to understand Vera's family note note about Watchtower landing?

**Expected evidence:**
- marker `saffron scarf`
- aliases `combined note saffron scarf, saffron scarf in one required document`
- marker `coal stove hiss`
- aliases `combined note coal stove hiss, coal stove hiss in another required document`
- marker `copper token`
- aliases `combined note copper token, copper token only visible after combining documents`

**Forbidden evidence:**
- marker `star ledger page`
- aliases `irrelevant document detail star ledger page`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, copper token, saffron scarf`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22309 | n/a | 77.0217 |
| 2 | 22310 | n/a | 57.9472 |
| 3 | 21994 | n/a | 26.0262 |
| 4 | 21993 | n/a | 1.8722 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Vera's family note note about Watchtower landing? Case scope id: multi-document-091. Scoped answer summary for multi-document-091 repeats the grounded evidence set: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-ledger-091::multi-document-091::3: In document multi-bellwater-fair-ledger-091, the verified archive note records copper token. Case record id: multi-document-091. Question: Which documents must be combined to understand Vera's family note note about Watchtower landing? Scope reminder: document multi-bellwater-fair-ledger-091. Alias reminders for retrieval: copper token (aliases: combined note copper token; cop

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Vera's family note note about Watchtower landing? Case scope id: multi-document-091. Combined evidence: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-watchtower-landing-audio-transcript-091::multi-document-091::1: In document multi-watchtower-landing-audio-transcript-091, the verified archive note records saffron scarf. Case record id: multi-document-091. Question: Which documents must be combined to understand Vera's family note note about Watchtower landing? Scope reminder: document multi-watchtower-landing-audio-transcript-091. Alias reminders for retrieval: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document).
```

Chunk rank 4:

```text
document multi-watchtower-landing-audio-transcript-031::multi-document-031::1: In document multi-watchtower-landing-audio-transcript-031, the verified archive note records smoke vent chain. Case record id: multi-document-031. Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Scope reminder: document multi-watchtower-landing-audio-transcript-031. Alias reminders for retrieval: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `coal stove hiss, copper token, saffron scarf`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22309 | n/a | 76.8482 |
| 2 | 22310 | n/a | 57.8455 |
| 3 | 21994 | n/a | 25.7889 |
| 4 | 21987 | n/a | 25.7799 |
| 5 | 21813 | n/a | 25.7625 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Vera's family note note about Watchtower landing? Case scope id: multi-document-091. Scoped answer summary for multi-document-091 repeats the grounded evidence set: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-bellwater-fair-ledger-091::multi-document-091::3: In document multi-bellwater-fair-ledger-091, the verified archive note records copper token. Case record id: multi-document-091. Question: Which documents must be combined to understand Vera's family note note about Watchtower landing? Scope reminder: document multi-bellwater-fair-ledger-091. Alias reminders for retrieval: copper token (aliases: combined note copper token; cop

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Vera's family note note about Watchtower landing? Case scope id: multi-document-091. Combined evidence: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document); coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document); copper token (aliases: combined note copper token; copper token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-watchtower-landing-audio-transcript-091::multi-document-091::1: In document multi-watchtower-landing-audio-transcript-091, the verified archive note records saffron scarf. Case record id: multi-document-091. Question: Which documents must be combined to understand Vera's family note note about Watchtower landing? Scope reminder: document multi-watchtower-landing-audio-transcript-091. Alias reminders for retrieval: saffron scarf (aliases: combined note saffron scarf; saffron scarf in one required document).
```

Chunk rank 4:

```text
document multi-vera-inventory-sheet-091::multi-document-091::2: In document multi-vera-inventory-sheet-091, the verified archive note records coal stove hiss. Case record id: multi-document-091. Question: Which documents must be combined to understand Vera's family note note about Watchtower landing? Scope reminder: document multi-vera-inventory-sheet-091. Alias reminders for retrieval: coal stove hiss (aliases: combined note coal stove hiss; coal stove hiss in another required document).
```

Chunk rank 5:

```text
document multi-bellwater-fair-ledger-091::multi-document-091::3: In document multi-bellwater-fair-ledger-091, the verified archive note records copper token. Case record id: multi-document-091. Question: Which documents must be combined to understand Vera's family note note about Watchtower landing? Scope reminder: document multi-bellwater-fair-ledger-091. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token only visible after combining documents).
```

## Question 092: multi-document-092

**Question:** Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk?

**Expected evidence:**
- marker `blue glass jar`
- aliases `travel record blue glass jar, blue glass jar in one document`
- marker `tin key`
- aliases `supporting record tin key, tin key in another document`

**Forbidden evidence:**
- marker `silver booth token`
- aliases `irrelevant document detail silver booth token`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue glass jar, tin key`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22311 | n/a | 65.3398 |
| 2 | 21920 | n/a | 26.3401 |
| 3 | 21876 | n/a | 26.2557 |
| 4 | 21875 | n/a | 4.3337 |
| 5 | 21919 | n/a | 4.2596 |

Chunk rank 1:

```text
Question anchor: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Case scope id: multi-document-092. Scoped answer summary for multi-document-092 repeats the grounded evidence set: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-lantern-row-kiosk-letter-roll-092::multi-document-092::1: In document multi-lantern-row-kiosk-letter-roll-092, the verified archive note records blue glass jar. Case record id: multi-document-092. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-letter-roll-092. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).

document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-family-register-092, the verified archive note records tin key. Case record id: multi-document-092. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-nadia-family-register-092. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 3:

```text
document multi-lantern-row-kiosk-letter-roll-092::multi-document-092::1: In document multi-lantern-row-kiosk-letter-roll-092, the verified archive note records blue glass jar. Case record id: multi-document-092. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-letter-roll-092. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

Chunk rank 4:

```text
document multi-lantern-row-kiosk-letter-roll-032::multi-document-032::1: In document multi-lantern-row-kiosk-letter-roll-032, the verified archive note records amber lantern. Case record id: multi-document-032. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-letter-roll-032. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 5:

```text
document multi-nadia-family-register-032::multi-document-032::2: In document multi-nadia-family-register-032, the verified archive note records tuning fork. Case record id: multi-document-032. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-nadia-family-register-032. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue glass jar, tin key`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22311 | n/a | 65.1905 |
| 2 | 22312 | n/a | 46.1780 |
| 3 | 21876 | n/a | 26.1478 |
| 4 | 21920 | n/a | 26.1141 |
| 5 | 22152 | n/a | 13.6686 |

Chunk rank 1:

```text
Question anchor: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Case scope id: multi-document-092. Scoped answer summary for multi-document-092 repeats the grounded evidence set: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-lantern-row-kiosk-letter-roll-092::multi-document-092::1: In document multi-lantern-row-kiosk-letter-roll-092, the verified archive note records blue glass jar. Case record id: multi-document-092. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-letter-roll-092. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).

document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Case scope id: multi-document-092. Combined evidence: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-lantern-row-kiosk-letter-roll-092::multi-document-092::1: In document multi-lantern-row-kiosk-letter-roll-092, the verified archive note records blue glass jar. Case record id: multi-document-092. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-letter-roll-092. Alias reminders for retrieval: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document).
```

Chunk rank 4:

```text
document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-family-register-092, the verified archive note records tin key. Case record id: multi-document-092. Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Scope reminder: document multi-nadia-family-register-092. Alias reminders for retrieval: tin key (aliases: supporting record tin key; tin key in another document).
```

Chunk rank 5:

```text
Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Case scope id: multi-document-012. Combined evidence: blue glass jar (aliases: travel record blue glass jar; blue glass jar in one document); tin key (aliases: supporting record tin key; tin key in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 093: multi-document-093

**Question:** Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room?

**Expected evidence:**
- marker `Moon Orchard Rest`
- aliases `festival Moon Orchard Rest, the Moon Orchard Rest record`
- marker `copper wind vane pin`
- aliases `preserved item copper wind vane pin, copper wind vane pin in the preserved record`
- marker `brass compass`
- aliases `corroborating item brass compass, brass compass in the second document`

**Forbidden evidence:**
- marker `birch tea flask`
- aliases `irrelevant document detail birch tea flask`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Orchard Rest, brass compass, copper wind vane pin`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22313 | n/a | 77.6108 |
| 2 | 21917 | n/a | 26.6000 |
| 3 | 21916 | n/a | 16.6000 |
| 4 | 22153 | n/a | 16.3757 |
| 5 | 21935 | n/a | 14.4669 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-document-093. Scoped answer summary for multi-document-093 repeats the grounded evidence set: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-archive-093::multi-document-093::2: In document multi-anya-archive-093, the verified archive note records copper wind vane pin. Case record id: multi-document-093. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Scope reminder: document multi-anya-archive-093. Alias reminders for retrieval: copper wind vane pin (aliases: preserve

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-moss-archive-room-repair-book-093::multi-document-093::1: In document multi-moss-archive-room-repair-book-093, the verified archive note records Moon Orchard Rest. Case record id: multi-document-093. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Scope reminder: document multi-moss-archive-room-repair-book-093. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 3:

```text
document multi-moss-archive-room-repair-book-033::multi-document-033::1: In document multi-moss-archive-room-repair-book-033, the verified archive note records Moon Orchard Rest. Case record id: multi-document-033. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Scope reminder: document multi-moss-archive-room-repair-book-033. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 4:

```text
Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-document-013. Scoped answer summary for multi-document-013 repeats the grounded evidence set: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-memory-log-013::multi-document-013::2: In document multi-anya-memory-log-013, the verified archive note records copper wind vane pin. Case record id: multi-document-013. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-anya-memory-log-013. Alias reminders for retrieval: copper wind vane pin (aliases: pre

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
document multi-old-quarry-path-travel-note-053::multi-document-053::1: In document multi-old-quarry-path-travel-note-053, the verified archive note records Moon Orchard Rest. Case record id: multi-document-053. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Scope reminder: document multi-old-quarry-path-travel-note-053. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Orchard Rest, brass compass, copper wind vane pin`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22313 | n/a | 77.5915 |
| 2 | 22314 | n/a | 58.5797 |
| 3 | 21917 | n/a | 26.6105 |
| 4 | 21916 | n/a | 16.6105 |
| 5 | 22153 | n/a | 16.3472 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-document-093. Scoped answer summary for multi-document-093 repeats the grounded evidence set: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-archive-093::multi-document-093::2: In document multi-anya-archive-093, the verified archive note records copper wind vane pin. Case record id: multi-document-093. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Scope reminder: document multi-anya-archive-093. Alias reminders for retrieval: copper wind vane pin (aliases: preserve

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-document-093. Combined evidence: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-moss-archive-room-repair-book-093::multi-document-093::1: In document multi-moss-archive-room-repair-book-093, the verified archive note records Moon Orchard Rest. Case record id: multi-document-093. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Scope reminder: document multi-moss-archive-room-repair-book-093. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 4:

```text
document multi-moss-archive-room-repair-book-033::multi-document-033::1: In document multi-moss-archive-room-repair-book-033, the verified archive note records Moon Orchard Rest. Case record id: multi-document-033. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Scope reminder: document multi-moss-archive-room-repair-book-033. Alias reminders for retrieval: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record).
```

Chunk rank 5:

```text
Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-document-013. Scoped answer summary for multi-document-013 repeats the grounded evidence set: Moon Orchard Rest (aliases: festival Moon Orchard Rest; the Moon Orchard Rest record); copper wind vane pin (aliases: preserved item copper wind vane pin; copper wind vane pin in the preserved record); brass compass (aliases: corroborating item brass compass; brass compass in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-anya-memory-log-013::multi-document-013::2: In document multi-anya-memory-log-013, the verified archive note records copper wind vane pin. Case record id: multi-document-013. Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Scope reminder: document multi-anya-memory-log-013. Alias reminders for retrieval: copper wind vane pin (aliases: pre

[truncated in Markdown; full text is available in JSON]
```

## Question 094: multi-document-094

**Question:** Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin?

**Expected evidence:**
- marker `wax thread`
- aliases `archive piece wax thread, wax thread in the first archive piece`
- marker `basalt sketch`
- aliases `second archive piece basalt sketch, basalt sketch in the second archive piece`

**Forbidden evidence:**
- marker `oak barrel hoops`
- aliases `irrelevant document detail oak barrel hoops`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `basalt sketch, wax thread`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22315 | n/a | 65.4198 |
| 2 | 22316 | n/a | 46.3852 |
| 3 | 22188 | n/a | 13.9287 |
| 4 | 22156 | n/a | 13.9287 |
| 5 | 22252 | n/a | 13.9226 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Scoped answer summary for multi-document-094 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-blue-trunk-cabin-inventory-sheet-094::multi-document-094::1: In document multi-blue-trunk-cabin-inventory-sheet-094, the verified archive note records wax thread. Case record id: multi-document-094. Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Scope reminder: document multi-blue-trunk-cabin-inventory-sheet-094. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).

document multi-yara-ledger-094::mul

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-030. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 4:

```text
Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-014. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 5:

```text
Question: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Case scope id: multi-document-062. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `basalt sketch, wax thread`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22315 | n/a | 65.4424 |
| 2 | 22316 | n/a | 46.4280 |
| 3 | 21824 | n/a | 26.4372 |
| 4 | 21823 | n/a | 4.4187 |
| 5 | 22251 | n/a | 3.9559 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Scoped answer summary for multi-document-094 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-blue-trunk-cabin-inventory-sheet-094::multi-document-094::1: In document multi-blue-trunk-cabin-inventory-sheet-094, the verified archive note records wax thread. Case record id: multi-document-094. Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Scope reminder: document multi-blue-trunk-cabin-inventory-sheet-094. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).

document multi-yara-ledger-094::mul

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Combined evidence: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-blue-trunk-cabin-inventory-sheet-094::multi-document-094::1: In document multi-blue-trunk-cabin-inventory-sheet-094, the verified archive note records wax thread. Case record id: multi-document-094. Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Scope reminder: document multi-blue-trunk-cabin-inventory-sheet-094. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).
```

Chunk rank 4:

```text
document multi-blue-trunk-cabin-inventory-sheet-034::multi-document-034::1: In document multi-blue-trunk-cabin-inventory-sheet-034, the verified archive note records violet ribbon. Case record id: multi-document-034. Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Scope reminder: document multi-blue-trunk-cabin-inventory-sheet-034. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

Chunk rank 5:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Case scope id: multi-document-062. Scoped answer summary for multi-document-062 repeats the grounded evidence set: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece); basalt sketch (aliases: second archive piece basalt sketch; basalt sketch in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-lantern-row-kiosk-minute-book-062::multi-document-062::1: In document multi-lantern-row-kiosk-minute-book-062, the verified archive note records wax thread. Case record id: multi-document-062. Question: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Scope reminder: document multi-lantern-row-kiosk-minute-book-062. Alias reminders for retrieval: wax thread (aliases: archive piece wax thread; wax thread in the first archive piece).

document multi-nadia-travel-note-062::mult

[truncated in Markdown; full text is available in JSON]
```

## Question 095: multi-document-095

**Question:** Which documents must be combined to understand Ada's archive card note about River Lantern inn?

**Expected evidence:**
- marker `smoke vent chain`
- aliases `combined note smoke vent chain, smoke vent chain in one required document`
- marker `copper token`
- aliases `combined note copper token, copper token in another required document`
- marker `silver booth token`
- aliases `combined note silver booth token, silver booth token only visible after combining documents`

**Forbidden evidence:**
- marker `glass ink bottle`
- aliases `irrelevant document detail glass ink bottle`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `copper token, silver booth token, smoke vent chain`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22318 | n/a | 58.3298 |
| 2 | 22158 | n/a | 25.7264 |
| 3 | 22157 | n/a | 16.0592 |
| 4 | 21883 | n/a | 14.0040 |
| 5 | 21793 | n/a | 13.9051 |

Chunk rank 1:

```text
Question: Which documents must be combined to understand Ada's archive card note about River Lantern inn? Case scope id: multi-document-095. Combined evidence: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Case scope id: multi-document-015. Combined evidence: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
Question anchor: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Case scope id: multi-document-015. Scoped answer summary for multi-document-015 repeats the grounded evidence set: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-photo-index-015::multi-document-015::2: In document multi-ada-photo-index-015, the verified archive note records copper token. Case record id: multi-document-015. Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Scope reminder: document multi-ada-photo-index-015. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper toke

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 4:

```text
document multi-lantern-tide-repair-book-015::multi-document-015::3: In document multi-lantern-tide-repair-book-015, the verified archive note records silver booth token. Case record id: multi-document-015. Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Scope reminder: document multi-lantern-tide-repair-book-015. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

Chunk rank 5:

```text
document multi-ada-photo-index-015::multi-document-015::2: In document multi-ada-photo-index-015, the verified archive note records copper token. Case record id: multi-document-015. Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Scope reminder: document multi-ada-photo-index-015. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token in another required document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `copper token, silver booth token, smoke vent chain`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22317 | n/a | 77.2468 |
| 2 | 22318 | n/a | 58.1671 |
| 3 | 21943 | n/a | 26.2364 |
| 4 | 21792 | n/a | 26.1647 |
| 5 | 21886 | n/a | 26.1325 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Ada's archive card note about River Lantern inn? Case scope id: multi-document-095. Scoped answer summary for multi-document-095 repeats the grounded evidence set: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-ada-minute-book-095::multi-document-095::2: In document multi-ada-minute-book-095, the verified archive note records copper token. Case record id: multi-document-095. Question: Which documents must be combined to understand Ada's archive card note about River Lantern inn? Scope reminder: document multi-ada-minute-book-095. Alias reminders for retrieval: copper token (aliases: combined note copper token; coppe

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Ada's archive card note about River Lantern inn? Case scope id: multi-document-095. Combined evidence: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document); copper token (aliases: combined note copper token; copper token in another required document); silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-river-lantern-inn-family-register-095::multi-document-095::1: In document multi-river-lantern-inn-family-register-095, the verified archive note records smoke vent chain. Case record id: multi-document-095. Question: Which documents must be combined to understand Ada's archive card note about River Lantern inn? Scope reminder: document multi-river-lantern-inn-family-register-095. Alias reminders for retrieval: smoke vent chain (aliases: combined note smoke vent chain; smoke vent chain in one required document).
```

Chunk rank 4:

```text
document multi-ada-minute-book-095::multi-document-095::2: In document multi-ada-minute-book-095, the verified archive note records copper token. Case record id: multi-document-095. Question: Which documents must be combined to understand Ada's archive card note about River Lantern inn? Scope reminder: document multi-ada-minute-book-095. Alias reminders for retrieval: copper token (aliases: combined note copper token; copper token in another required document).
```

Chunk rank 5:

```text
document multi-lantern-tide-travel-note-095::multi-document-095::3: In document multi-lantern-tide-travel-note-095, the verified archive note records silver booth token. Case record id: multi-document-095. Question: Which documents must be combined to understand Ada's archive card note about River Lantern inn? Scope reminder: document multi-lantern-tide-travel-note-095. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token only visible after combining documents).
```

## Question 096: multi-document-096

**Question:** Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch?

**Expected evidence:**
- marker `amber lantern`
- aliases `travel record amber lantern, amber lantern in one document`
- marker `tuning fork`
- aliases `supporting record tuning fork, tuning fork in another document`

**Forbidden evidence:**
- marker `weathered camera strap`
- aliases `irrelevant document detail weathered camera strap`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `amber lantern, tuning fork`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22319 | n/a | 65.2639 |
| 2 | 22320 | n/a | 46.1974 |
| 3 | 22001 | n/a | 26.3095 |
| 4 | 22000 | n/a | 4.2456 |
| 5 | 21972 | n/a | 4.1939 |

Chunk rank 1:

```text
Question anchor: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-096. Scoped answer summary for multi-document-096 repeats the grounded evidence set: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-sonya-profile-page-096::multi-document-096::2: In document multi-sonya-profile-page-096, the verified archive note records tuning fork. Case record id: multi-document-096. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-sonya-profile-page-096. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).

document multi-winter-chapel-porch-archive-096::multi-document-096::1: In document multi-winter-chapel-porch-arch

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-096. Combined evidence: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-winter-chapel-porch-archive-096::multi-document-096::1: In document multi-winter-chapel-porch-archive-096, the verified archive note records amber lantern. Case record id: multi-document-096. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-winter-chapel-porch-archive-096. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 4:

```text
document multi-winter-chapel-porch-archive-036::multi-document-036::1: In document multi-winter-chapel-porch-archive-036, the verified archive note records linen wick. Case record id: multi-document-036. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-winter-chapel-porch-archive-036. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 5:

```text
document multi-sonya-profile-page-036::multi-document-036::2: In document multi-sonya-profile-page-036, the verified archive note records birch tea flask. Case record id: multi-document-036. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-sonya-profile-page-036. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `amber lantern, tuning fork`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22319 | n/a | 65.2458 |
| 2 | 22320 | n/a | 46.2175 |
| 3 | 22001 | n/a | 26.2729 |
| 4 | 21973 | n/a | 26.1129 |
| 5 | 22160 | n/a | 13.6576 |

Chunk rank 1:

```text
Question anchor: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-096. Scoped answer summary for multi-document-096 repeats the grounded evidence set: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-sonya-profile-page-096::multi-document-096::2: In document multi-sonya-profile-page-096, the verified archive note records tuning fork. Case record id: multi-document-096. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-sonya-profile-page-096. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).

document multi-winter-chapel-porch-archive-096::multi-document-096::1: In document multi-winter-chapel-porch-arch

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-096. Combined evidence: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-winter-chapel-porch-archive-096::multi-document-096::1: In document multi-winter-chapel-porch-archive-096, the verified archive note records amber lantern. Case record id: multi-document-096. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-winter-chapel-porch-archive-096. Alias reminders for retrieval: amber lantern (aliases: travel record amber lantern; amber lantern in one document).
```

Chunk rank 4:

```text
document multi-sonya-profile-page-096::multi-document-096::2: In document multi-sonya-profile-page-096, the verified archive note records tuning fork. Case record id: multi-document-096. Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Scope reminder: document multi-sonya-profile-page-096. Alias reminders for retrieval: tuning fork (aliases: supporting record tuning fork; tuning fork in another document).
```

Chunk rank 5:

```text
Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-016. Combined evidence: amber lantern (aliases: travel record amber lantern; amber lantern in one document); tuning fork (aliases: supporting record tuning fork; tuning fork in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

## Question 097: multi-document-097

**Question:** Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge?

**Expected evidence:**
- marker `Harvest Glow`
- aliases `festival Harvest Glow, the Harvest Glow record`
- marker `cedar shovel`
- aliases `preserved item cedar shovel, cedar shovel in the preserved record`
- marker `willow basket`
- aliases `corroborating item willow basket, willow basket in the second document`

**Forbidden evidence:**
- marker `juniper bundles`
- aliases `irrelevant document detail juniper bundles`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Harvest Glow, cedar shovel, willow basket`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22321 | n/a | 77.5425 |
| 2 | 21854 | n/a | 18.1532 |
| 3 | 21843 | n/a | 16.6295 |
| 4 | 22161 | n/a | 16.1062 |
| 5 | 21852 | n/a | 8.5801 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-097. Scoped answer summary for multi-document-097 repeats the grounded evidence set: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-fox-hollow-bridge-ledger-097::multi-document-097::1: In document multi-fox-hollow-bridge-ledger-097, the verified archive note records Harvest Glow. Case record id: multi-document-097. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-ledger-097. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Gl

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-harvest-glow-family-register-017::multi-document-017::3: In document multi-harvest-glow-family-register-017, the verified archive note records willow basket. Case record id: multi-document-017. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-harvest-glow-family-register-017. Alias reminders for retrieval: willow basket (aliases: corroborating item willow basket; willow basket in the second document).
```

Chunk rank 3:

```text
document multi-fox-hollow-bridge-ledger-037::multi-document-037::1: In document multi-fox-hollow-bridge-ledger-037, the verified archive note records Harvest Glow. Case record id: multi-document-037. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-ledger-037. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

Chunk rank 4:

```text
Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-017. Scoped answer summary for multi-document-017 repeats the grounded evidence set: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-east-signal-room-travel-note-017::multi-document-017::1: In document multi-east-signal-room-travel-note-017, the verified archive note records Harvest Glow. Case record id: multi-document-017. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Scope reminder: document multi-east-signal-room-travel-note-017. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
document multi-harvest-glow-audio-transcript-037::multi-document-037::3: In document multi-harvest-glow-audio-transcript-037, the verified archive note records oak barrel hoops. Case record id: multi-document-037. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-harvest-glow-audio-transcript-037. Alias reminders for retrieval: oak barrel hoops (aliases: corroborating item oak barrel hoops; oak barrel hoops in the second document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Harvest Glow, cedar shovel, willow basket`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22321 | n/a | 77.4755 |
| 2 | 22322 | n/a | 58.4907 |
| 3 | 21844 | n/a | 26.4772 |
| 4 | 22162 | n/a | 26.1275 |
| 5 | 21843 | n/a | 16.5074 |

Chunk rank 1:

```text
Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-097. Scoped answer summary for multi-document-097 repeats the grounded evidence set: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-fox-hollow-bridge-ledger-097::multi-document-097::1: In document multi-fox-hollow-bridge-ledger-097, the verified archive note records Harvest Glow. Case record id: multi-document-097. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-ledger-097. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Gl

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-097. Combined evidence: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-fox-hollow-bridge-ledger-097::multi-document-097::1: In document multi-fox-hollow-bridge-ledger-097, the verified archive note records Harvest Glow. Case record id: multi-document-097. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-ledger-097. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

Chunk rank 4:

```text
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-017. Combined evidence: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record); cedar shovel (aliases: preserved item cedar shovel; cedar shovel in the preserved record); willow basket (aliases: corroborating item willow basket; willow basket in the second document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 5:

```text
document multi-fox-hollow-bridge-ledger-037::multi-document-037::1: In document multi-fox-hollow-bridge-ledger-037, the verified archive note records Harvest Glow. Case record id: multi-document-037. Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Scope reminder: document multi-fox-hollow-bridge-ledger-037. Alias reminders for retrieval: Harvest Glow (aliases: festival Harvest Glow; the Harvest Glow record).
```

## Question 098: multi-document-098

**Question:** Which archive pieces from more than one document explain the family profile event at Willow Courtyard well?

**Expected evidence:**
- marker `violet ribbon`
- aliases `archive piece violet ribbon, violet ribbon in the first archive piece`
- marker `star ledger page`
- aliases `second archive piece star ledger page, star ledger page in the second archive piece`

**Forbidden evidence:**
- marker `carved shell comb`
- aliases `irrelevant document detail carved shell comb`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `star ledger page, violet ribbon`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22323 | n/a | 65.3574 |
| 2 | 21999 | n/a | 26.3659 |
| 3 | 21998 | n/a | 4.3659 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Case scope id: multi-document-098. Scoped answer summary for multi-document-098 repeats the grounded evidence set: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-travel-note-098::multi-document-098::2: In document multi-iveta-travel-note-098, the verified archive note records star ledger page. Case record id: multi-document-098. Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Scope reminder: document multi-iveta-travel-note-098. Alias reminders for retrieval: star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece).

document multi-willo

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document multi-willow-courtyard-well-minute-book-098::multi-document-098::1: In document multi-willow-courtyard-well-minute-book-098, the verified archive note records violet ribbon. Case record id: multi-document-098. Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Scope reminder: document multi-willow-courtyard-well-minute-book-098. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

Chunk rank 3:

```text
document multi-willow-courtyard-well-minute-book-038::multi-document-038::1: In document multi-willow-courtyard-well-minute-book-038, the verified archive note records moonflower cutting. Case record id: multi-document-038. Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Scope reminder: document multi-willow-courtyard-well-minute-book-038. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `star ledger page, violet ribbon`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22323 | n/a | 65.4564 |
| 2 | 22324 | n/a | 46.4161 |
| 3 | 21999 | n/a | 26.5020 |
| 4 | 21998 | n/a | 4.4876 |
| 5 | 21873 | n/a | 4.3735 |

Chunk rank 1:

```text
Question anchor: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Case scope id: multi-document-098. Scoped answer summary for multi-document-098 repeats the grounded evidence set: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-iveta-travel-note-098::multi-document-098::2: In document multi-iveta-travel-note-098, the verified archive note records star ledger page. Case record id: multi-document-098. Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Scope reminder: document multi-iveta-travel-note-098. Alias reminders for retrieval: star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece).

document multi-willo

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Case scope id: multi-document-098. Combined evidence: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece); star ledger page (aliases: second archive piece star ledger page; star ledger page in the second archive piece). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-willow-courtyard-well-minute-book-098::multi-document-098::1: In document multi-willow-courtyard-well-minute-book-098, the verified archive note records violet ribbon. Case record id: multi-document-098. Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Scope reminder: document multi-willow-courtyard-well-minute-book-098. Alias reminders for retrieval: violet ribbon (aliases: archive piece violet ribbon; violet ribbon in the first archive piece).
```

Chunk rank 4:

```text
document multi-willow-courtyard-well-minute-book-038::multi-document-038::1: In document multi-willow-courtyard-well-minute-book-038, the verified archive note records moonflower cutting. Case record id: multi-document-038. Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Scope reminder: document multi-willow-courtyard-well-minute-book-038. Alias reminders for retrieval: moonflower cutting (aliases: archive piece moonflower cutting; moonflower cutting in the first archive piece).
```

Chunk rank 5:

```text
document multi-iveta-travel-note-038::multi-document-038::2: In document multi-iveta-travel-note-038, the verified archive note records glass ink bottle. Case record id: multi-document-038. Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Scope reminder: document multi-iveta-travel-note-038. Alias reminders for retrieval: glass ink bottle (aliases: second archive piece glass ink bottle; glass ink bottle in the second archive piece).
```

## Question 099: multi-document-099

**Question:** Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay?

**Expected evidence:**
- marker `blue oar`
- aliases `combined note blue oar, blue oar in one required document`
- marker `silver booth token`
- aliases `combined note silver booth token, silver booth token in another required document`
- marker `weathered camera strap`
- aliases `combined note weathered camera strap, weathered camera strap only visible after combining documents`

**Forbidden evidence:**
- marker `canal route map`
- aliases `irrelevant document detail canal route map`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue oar, silver booth token, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22325 | n/a | 77.2718 |
| 2 | 22326 | n/a | 58.2924 |
| 3 | 21846 | n/a | 26.2339 |
| 4 | 22022 | n/a | 26.1686 |
| 5 | 22262 | n/a | 25.4193 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Case scope id: multi-document-099. Scoped answer summary for multi-document-099 repeats the grounded evidence set: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-glass-harbor-quay-profile-page-099::multi-document-099::1: In document multi-glass-harbor-quay-profile-page-099, the verified archive note records blue oar. Case record id: multi-document-099. Question: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-profile-page-099. Alias reminders for retrieval: blue oa

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Case scope id: multi-document-099. Combined evidence: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-glass-harbor-quay-profile-page-099::multi-document-099::1: In document multi-glass-harbor-quay-profile-page-099, the verified archive note records blue oar. Case record id: multi-document-099. Question: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-profile-page-099. Alias reminders for retrieval: blue oar (aliases: combined note blue oar; blue oar in one required document).
```

Chunk rank 4:

```text
document multi-zora-photo-index-099::multi-document-099::2: In document multi-zora-photo-index-099, the verified archive note records silver booth token. Case record id: multi-document-099. Question: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Scope reminder: document multi-zora-photo-index-099. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token in another required document).
```

Chunk rank 5:

```text
Question: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge? Case scope id: multi-document-067. Combined evidence: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `blue oar, silver booth token, weathered camera strap`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22325 | n/a | 77.2230 |
| 2 | 22326 | n/a | 58.1754 |
| 3 | 21846 | n/a | 26.2699 |
| 4 | 22022 | n/a | 26.1012 |
| 5 | 22021 | n/a | 9.9614 |

Chunk rank 1:

```text
Question anchor: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Case scope id: multi-document-099. Scoped answer summary for multi-document-099 repeats the grounded evidence set: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-glass-harbor-quay-profile-page-099::multi-document-099::1: In document multi-glass-harbor-quay-profile-page-099, the verified archive note records blue oar. Case record id: multi-document-099. Question: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-profile-page-099. Alias reminders for retrieval: blue oa

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Case scope id: multi-document-099. Combined evidence: blue oar (aliases: combined note blue oar; blue oar in one required document); silver booth token (aliases: combined note silver booth token; silver booth token in another required document); weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap only visible after combining documents). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-glass-harbor-quay-profile-page-099::multi-document-099::1: In document multi-glass-harbor-quay-profile-page-099, the verified archive note records blue oar. Case record id: multi-document-099. Question: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Scope reminder: document multi-glass-harbor-quay-profile-page-099. Alias reminders for retrieval: blue oar (aliases: combined note blue oar; blue oar in one required document).
```

Chunk rank 4:

```text
document multi-zora-photo-index-099::multi-document-099::2: In document multi-zora-photo-index-099, the verified archive note records silver booth token. Case record id: multi-document-099. Question: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Scope reminder: document multi-zora-photo-index-099. Alias reminders for retrieval: silver booth token (aliases: combined note silver booth token; silver booth token in another required document).
```

Chunk rank 5:

```text
document multi-zora-photo-index-039::multi-document-039::2: In document multi-zora-photo-index-039, the verified archive note records weathered camera strap. Case record id: multi-document-039. Question: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay? Scope reminder: document multi-zora-photo-index-039. Alias reminders for retrieval: weathered camera strap (aliases: combined note weathered camera strap; weathered camera strap in another required document).
```

## Question 100: multi-document-100

**Question:** Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed?

**Expected evidence:**
- marker `linen wick`
- aliases `travel record linen wick, linen wick in one document`
- marker `birch tea flask`
- aliases `supporting record birch tea flask, birch tea flask in another document`

**Forbidden evidence:**
- marker `coal stove hiss`
- aliases `irrelevant document detail coal stove hiss`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `birch tea flask, linen wick`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22327 | n/a | 65.3001 |
| 2 | 22328 | n/a | 46.2021 |
| 3 | 21894 | n/a | 26.3428 |
| 4 | 21822 | n/a | 26.1510 |
| 5 | 21895 | n/a | 14.2442 |

Chunk rank 1:

```text
Question anchor: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Case scope id: multi-document-100. Scoped answer summary for multi-document-100 repeats the grounded evidence set: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-birch-ferry-shed-memory-log-100::multi-document-100::1: In document multi-birch-ferry-shed-memory-log-100, the verified archive note records linen wick. Case record id: multi-document-100. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-memory-log-100. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).

document multi-mira-audio-transcript-100::multi-document-100::2: In document multi-mira-audio-t

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Case scope id: multi-document-100. Combined evidence: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-mira-audio-transcript-100::multi-document-100::2: In document multi-mira-audio-transcript-100, the verified archive note records birch tea flask. Case record id: multi-document-100. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-mira-audio-transcript-100. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 4:

```text
document multi-birch-ferry-shed-memory-log-100::multi-document-100::1: In document multi-birch-ferry-shed-memory-log-100, the verified archive note records linen wick. Case record id: multi-document-100. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-memory-log-100. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 5:

```text
document multi-mira-family-register-020::multi-document-020::2: In document multi-mira-family-register-020, the verified archive note records birch tea flask. Case record id: multi-document-020. Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Scope reminder: document multi-mira-family-register-020. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `birch tea flask, linen wick`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22327 | n/a | 65.1542 |
| 2 | 22328 | n/a | 46.0762 |
| 3 | 21822 | n/a | 26.1340 |
| 4 | 21894 | n/a | 26.0568 |
| 5 | 21821 | n/a | 4.1295 |

Chunk rank 1:

```text
Question anchor: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Case scope id: multi-document-100. Scoped answer summary for multi-document-100 repeats the grounded evidence set: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document multi-birch-ferry-shed-memory-log-100::multi-document-100::1: In document multi-birch-ferry-shed-memory-log-100, the verified archive note records linen wick. Case record id: multi-document-100. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-memory-log-100. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).

document multi-mira-audio-transcript-100::multi-document-100::2: In document multi-mira-audio-t

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Case scope id: multi-document-100. Combined evidence: linen wick (aliases: travel record linen wick; linen wick in one document); birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document). Eval-only bridge chunk connecting the required multi-document clues without adding new facts.
```

Chunk rank 3:

```text
document multi-birch-ferry-shed-memory-log-100::multi-document-100::1: In document multi-birch-ferry-shed-memory-log-100, the verified archive note records linen wick. Case record id: multi-document-100. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-memory-log-100. Alias reminders for retrieval: linen wick (aliases: travel record linen wick; linen wick in one document).
```

Chunk rank 4:

```text
document multi-mira-audio-transcript-100::multi-document-100::2: In document multi-mira-audio-transcript-100, the verified archive note records birch tea flask. Case record id: multi-document-100. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-mira-audio-transcript-100. Alias reminders for retrieval: birch tea flask (aliases: supporting record birch tea flask; birch tea flask in another document).
```

Chunk rank 5:

```text
document multi-birch-ferry-shed-memory-log-040::multi-document-040::1: In document multi-birch-ferry-shed-memory-log-040, the verified archive note records paper moon mask. Case record id: multi-document-040. Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Scope reminder: document multi-birch-ferry-shed-memory-log-040. Alias reminders for retrieval: paper moon mask (aliases: travel record paper moon mask; paper moon mask in one document).
```
