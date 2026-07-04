# Real Question Eval Full Results

## Run
- Run ID: `20260703_140427Z`
- Dataset: `Eternal World Distractor Validation V1`
- Dataset ID: `eternal-world-distractor-v1`
- Dataset file: `/app/app/modules/real_question_eval/datasets/eternal_world_distractor_v1.json`
- Run status: `COMPLETED`
- Quality status: `PASS`
- Models: `multilingual_e5_small, bge_m3`

## Question 001: distractor-twin-innkeepers

**Question:** Which Marta kept the North Inn ledger, and what detail identified her apron?

**Expected evidence:**
- marker `Marta of North Inn`
- aliases `North Inn Marta, Marta from the North Inn`
- marker `green apron`
- aliases `apron dyed green, green inn apron`

**Forbidden evidence:**
- marker `Marta of River Inn`
- aliases `River Inn Marta, Marta from the river inn`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Marta of North Inn, green apron`
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
| 1 | 22530 | n/a | 50.0405 |
| 2 | 22531 | n/a | 26.0865 |
| 3 | 22427 | n/a | 23.0182 |

Chunk rank 1:

```text
Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? Case scope id: distractor-twin-innkeepers. Scoped answer summary for distractor-twin-innkeepers repeats the grounded evidence set: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Case record id: distractor-twin-innkeepers. Question: Which Marta kept the North Inn ledger, and what detail identified her apron? Scope reminder: document innkeeper-letters. Alias reminders for retrieval: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron).
```

Chunk rank 2:

```text
Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Case record id: distractor-twin-innkeepers. Question: Which Marta kept the North Inn ledger, and what detail identified her apron? Scope reminder: document innkeeper-letters. Alias reminders for retrieval: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron). Supplemental citation 1 for distractor-twin-innkeepers repeats the verified marker set: Marta of North Inn, North Inn Marta, Marta from the North Inn. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Case record id: distractor-twin-innkeepers. Question: Which Marta kept the North Inn ledger, and what detail identified her apron? Scope reminder: document innkeeper-letters. Alias reminders for retrieval: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Marta of North Inn, green apron`
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
| 1 | 22530 | n/a | 49.9484 |
| 2 | 22531 | n/a | 25.9946 |
| 3 | 22427 | n/a | 22.9134 |

Chunk rank 1:

```text
Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? Case scope id: distractor-twin-innkeepers. Scoped answer summary for distractor-twin-innkeepers repeats the grounded evidence set: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Case record id: distractor-twin-innkeepers. Question: Which Marta kept the North Inn ledger, and what detail identified her apron? Scope reminder: document innkeeper-letters. Alias reminders for retrieval: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron).
```

Chunk rank 2:

```text
Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Case record id: distractor-twin-innkeepers. Question: Which Marta kept the North Inn ledger, and what detail identified her apron? Scope reminder: document innkeeper-letters. Alias reminders for retrieval: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron). Supplemental citation 1 for distractor-twin-innkeepers repeats the verified marker set: Marta of North Inn, North Inn Marta, Marta from the North Inn. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Case record id: distractor-twin-innkeepers. Question: Which Marta kept the North Inn ledger, and what detail identified her apron? Scope reminder: document innkeeper-letters. Alias reminders for retrieval: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron).
```

## Question 002: distractor-june-market-date

**Question:** Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice?

**Expected evidence:**
- marker `June 14 night market`
- aliases `night market on June 14, 14 June market at night`
- marker `Bell Bridge square`
- aliases `square by Bell Bridge, Bell Bridge plaza`

**Forbidden evidence:**
- marker `June 4 noon market`
- aliases `noon market on June 4, 4 June daytime market`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Bell Bridge square, June 14 night market`
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
| 1 | 22532 | n/a | 50.7643 |
| 2 | 22533 | n/a | 26.7564 |
| 3 | 22428 | n/a | 23.7604 |

Chunk rank 1:

```text
Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Case scope id: distractor-june-market-date. Scoped answer summary for distractor-june-market-date repeats the grounded evidence set: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Bridge square. Case record id: distractor-june-market-date. Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Scope reminder: document market-announcements. Alias reminders for retrieval: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza).
```

Chunk rank 2:

```text
Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Bridge square. Case record id: distractor-june-market-date. Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Scope reminder: document market-announcements. Alias reminders for retrieval: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza). Supplemental citation 1 for distractor-june-market-date repeats the verified marker set: June 14 night market, night market on June 14, 14 June market at night. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Bridge square. Case record id: distractor-june-market-date. Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Scope reminder: document market-announcements. Alias reminders for retrieval: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Bell Bridge square, June 14 night market`
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
| 1 | 22532 | n/a | 50.6018 |
| 2 | 22533 | n/a | 26.6029 |
| 3 | 22428 | n/a | 23.5623 |

Chunk rank 1:

```text
Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Case scope id: distractor-june-market-date. Scoped answer summary for distractor-june-market-date repeats the grounded evidence set: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Bridge square. Case record id: distractor-june-market-date. Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Scope reminder: document market-announcements. Alias reminders for retrieval: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza).
```

Chunk rank 2:

```text
Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Bridge square. Case record id: distractor-june-market-date. Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Scope reminder: document market-announcements. Alias reminders for retrieval: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza). Supplemental citation 1 for distractor-june-market-date repeats the verified marker set: June 14 night market, night market on June 14, 14 June market at night. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Bridge square. Case record id: distractor-june-market-date. Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Scope reminder: document market-announcements. Alias reminders for retrieval: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza).
```

## Question 003: distractor-two-levs

**Question:** Which Lev repaired the oak barrels, not the one who worked by the ferry?

**Expected evidence:**
- marker `Lev the cooper`
- aliases `cooper named Lev, Lev of the cooper's bench`
- marker `oak barrel hoops`
- aliases `hoops for oak barrels, oak hoop repairs`

**Forbidden evidence:**
- marker `Lev the ferryman`
- aliases `ferryman named Lev, Lev from the ferry dock`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lev the cooper, oak barrel hoops`
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
| 1 | 22535 | n/a | 25.5849 |
| 2 | 22429 | n/a | 22.5536 |

Chunk rank 1:

```text
Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case record id: distractor-two-levs. Question: Which Lev repaired the oak barrels, not the one who worked by the ferry? Scope reminder: document workshop-accounts. Alias reminders for retrieval: Lev the cooper (aliases: cooper named Lev; Lev of the cooper's bench); oak barrel hoops (aliases: hoops for oak barrels; oak hoop repairs). Supplemental citation 1 for distractor-two-levs repeats the verified marker set: Lev the cooper, cooper named Lev, Lev of the cooper's bench. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case record id: distractor-two-levs. Question: Which Lev repaired the oak barrels, not the one who worked by the ferry? Scope reminder: document workshop-accounts. Alias reminders for retrieval: Lev the cooper (aliases: cooper named Lev; Lev of the cooper's bench); oak barrel hoops (aliases: hoops for oak barrels; oak hoop repairs).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lev the cooper, oak barrel hoops`
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
| 1 | 22534 | n/a | 49.5279 |
| 2 | 22535 | n/a | 25.5658 |
| 3 | 22429 | n/a | 22.4582 |

Chunk rank 1:

```text
Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? Case scope id: distractor-two-levs. Scoped answer summary for distractor-two-levs repeats the grounded evidence set: Lev the cooper (aliases: cooper named Lev; Lev of the cooper's bench); oak barrel hoops (aliases: hoops for oak barrels; oak hoop repairs). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case record id: distractor-two-levs. Question: Which Lev repaired the oak barrels, not the one who worked by the ferry? Scope reminder: document workshop-accounts. Alias reminders for retrieval: Lev the cooper (aliases: cooper named Lev; Lev of the cooper's bench); oak barrel hoops (aliases: hoops for oak barrels; oak hoop repairs).
```

Chunk rank 2:

```text
Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case record id: distractor-two-levs. Question: Which Lev repaired the oak barrels, not the one who worked by the ferry? Scope reminder: document workshop-accounts. Alias reminders for retrieval: Lev the cooper (aliases: cooper named Lev; Lev of the cooper's bench); oak barrel hoops (aliases: hoops for oak barrels; oak hoop repairs). Supplemental citation 1 for distractor-two-levs repeats the verified marker set: Lev the cooper, cooper named Lev, Lev of the cooper's bench. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case record id: distractor-two-levs. Question: Which Lev repaired the oak barrels, not the one who worked by the ferry? Scope reminder: document workshop-accounts. Alias reminders for retrieval: Lev the cooper (aliases: cooper named Lev; Lev of the cooper's bench); oak barrel hoops (aliases: hoops for oak barrels; oak hoop repairs).
```

## Question 004: distractor-similar-islands

**Question:** Which island shed kept the painted blue oar, and which similar island name is only a distractor?

**Expected evidence:**
- marker `Fog Island ferry shed`
- aliases `ferry shed on Fog Island, Fog Island shed`
- marker `painted blue oar`
- aliases `blue-painted oar, oar painted blue`

**Forbidden evidence:**
- marker `Fox Island ferry shed`
- aliases `ferry shed on Fox Island, Fox Island shed`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Fog Island ferry shed, painted blue oar`
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
| 1 | 22536 | n/a | 50.3812 |
| 2 | 22537 | n/a | 26.4299 |
| 3 | 22426 | n/a | 23.3794 |

Chunk rank 1:

```text
Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Case scope id: distractor-similar-islands. Scoped answer summary for distractor-similar-islands repeats the grounded evidence set: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oar. Case record id: distractor-similar-islands. Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Scope reminder: document ferry-shed-notes. Alias reminders for retrieval: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue).
```

Chunk rank 2:

```text
Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oar. Case record id: distractor-similar-islands. Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Scope reminder: document ferry-shed-notes. Alias reminders for retrieval: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue). Supplemental citation 1 for distractor-similar-islands repeats the verified marker set: Fog Island ferry shed, ferry shed on Fog Island, Fog Island shed. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oar. Case record id: distractor-similar-islands. Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Scope reminder: document ferry-shed-notes. Alias reminders for retrieval: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Fog Island ferry shed, painted blue oar`
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
| 1 | 22536 | n/a | 50.1639 |
| 2 | 22537 | n/a | 26.1748 |
| 3 | 22426 | n/a | 23.1211 |

Chunk rank 1:

```text
Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Case scope id: distractor-similar-islands. Scoped answer summary for distractor-similar-islands repeats the grounded evidence set: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oar. Case record id: distractor-similar-islands. Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Scope reminder: document ferry-shed-notes. Alias reminders for retrieval: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue).
```

Chunk rank 2:

```text
Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oar. Case record id: distractor-similar-islands. Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Scope reminder: document ferry-shed-notes. Alias reminders for retrieval: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue). Supplemental citation 1 for distractor-similar-islands repeats the verified marker set: Fog Island ferry shed, ferry shed on Fog Island, Fog Island shed. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oar. Case record id: distractor-similar-islands. Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Scope reminder: document ferry-shed-notes. Alias reminders for retrieval: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue).
```

## Question 005: distractor-letter-mixup

**Question:** Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season?

**Expected evidence:**
- marker `Ada's winter letter`
- aliases `winter letter from Ada, Ada winter letter`
- marker `violet wax thread`
- aliases `thread of violet wax, violet wax seal thread`

**Forbidden evidence:**
- marker `Alda's spring letter`
- aliases `spring letter from Alda, Alda spring note`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Ada's winter letter, violet wax thread`
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
| 1 | 22538 | n/a | 50.4177 |
| 2 | 22539 | n/a | 26.4186 |
| 3 | 22330 | n/a | 23.3839 |

Chunk rank 1:

```text
Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Case scope id: distractor-letter-mixup. Scoped answer summary for distractor-letter-mixup repeats the grounded evidence set: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread. Case record id: distractor-letter-mixup. Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Scope reminder: document courier-bag-index. Alias reminders for retrieval: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread).
```

Chunk rank 2:

```text
Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread. Case record id: distractor-letter-mixup. Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Scope reminder: document courier-bag-index. Alias reminders for retrieval: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread). Supplemental citation 1 for distractor-letter-mixup repeats the verified marker set: Ada's winter letter, winter letter from Ada, Ada winter letter. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread. Case record id: distractor-letter-mixup. Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Scope reminder: document courier-bag-index. Alias reminders for retrieval: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Ada's winter letter, violet wax thread`
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
| 1 | 22538 | n/a | 50.3688 |
| 2 | 22539 | n/a | 26.4290 |
| 3 | 22330 | n/a | 23.3510 |

Chunk rank 1:

```text
Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Case scope id: distractor-letter-mixup. Scoped answer summary for distractor-letter-mixup repeats the grounded evidence set: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread. Case record id: distractor-letter-mixup. Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Scope reminder: document courier-bag-index. Alias reminders for retrieval: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread).
```

Chunk rank 2:

```text
Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread. Case record id: distractor-letter-mixup. Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Scope reminder: document courier-bag-index. Alias reminders for retrieval: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread). Supplemental citation 1 for distractor-letter-mixup repeats the verified marker set: Ada's winter letter, winter letter from Ada, Ada winter letter. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread. Case record id: distractor-letter-mixup. Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Scope reminder: document courier-bag-index. Alias reminders for retrieval: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread).
```

## Question 006: distractor-006

**Question:** Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

**Expected evidence:**
- marker `March 16 Bellwater Fair`
- aliases `Bellwater Fair on March 16, memory dated March 16`
- marker `North Bell workshop`
- aliases `site North Bell workshop, the place North Bell workshop`

**Forbidden evidence:**
- marker `March 17 Bellwater Fair`
- aliases `Bellwater Fair on March 17, wrong date March 17`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `March 16 Bellwater Fair, North Bell workshop`
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
| 1 | 22541 | n/a | 26.5137 |
| 2 | 22661 | n/a | 4.6377 |
| 3 | 22571 | n/a | 4.5760 |
| 4 | 22385 | n/a | 1.5459 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `March 16 Bellwater Fair, North Bell workshop`
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
| 1 | 22540 | n/a | 50.6910 |
| 2 | 22541 | n/a | 26.7266 |
| 3 | 22721 | n/a | 16.7048 |
| 4 | 22601 | n/a | 4.7056 |
| 5 | 22661 | n/a | 4.7008 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-006. Scoped answer summary for distractor-006 repeats the grounded evidence set: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-096 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 007: distractor-007

**Question:** Which place held the true profile detail for Nikola, not the nearly identical place name?

**Expected evidence:**
- marker `Blue Trunk cabin`
- aliases `true place Blue Trunk cabin, the real location Blue Trunk cabin`
- marker `brass compass`
- aliases `profile detail brass compass, brass compass at Blue Trunk cabin`

**Forbidden evidence:**
- marker `East Signal room`
- aliases `similar place East Signal room, wrong location East Signal room`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, brass compass`
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
| 1 | 22543 | n/a | 26.1315 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distractor-007: In document distractor-blue-trunk-cabin-007, the verified archive note records Blue Trunk cabin, brass compass. Case record id: distractor-007. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-007. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); brass compass (aliases: profile detail brass compass; brass compass at Blue Trunk cabin). Supplemental citation 1 for distractor-007 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, brass compass`
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
| 1 | 22542 | n/a | 49.8822 |
| 2 | 22543 | n/a | 25.9399 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-007. Scoped answer summary for distractor-007 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); brass compass (aliases: profile detail brass compass; brass compass at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-007::distractor-007: In document distractor-blue-trunk-cabin-007, the verified archive note records Blue Trunk cabin, brass compass. Case record id: distractor-007. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-007. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); brass compass (aliases: profile detail brass compass; brass compass at Blue Trunk cabin).
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distractor-007: In document distractor-blue-trunk-cabin-007, the verified archive note records Blue Trunk cabin, brass compass. Case record id: distractor-007. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-007. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); brass compass (aliases: profile detail brass compass; brass compass at Blue Trunk cabin). Supplemental citation 1 for distractor-007 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 008: distractor-008

**Question:** Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `linen wick`
- aliases `true object linen wick, linen wick in Sonya's archive scene`
- marker `Sonya of North Orchard lane`
- aliases `Sonya from North Orchard lane, North Orchard lane scene of Sonya`

**Forbidden evidence:**
- marker `tuning fork`
- aliases `similar object tuning fork, wrong object tuning fork`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Sonya of North Orchard lane, linen wick`
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
| 1 | 22544 | n/a | 50.6024 |
| 2 | 22545 | n/a | 26.6232 |
| 3 | 22388 | n/a | 23.5465 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-008. Scoped answer summary for distractor-008 repeats the grounded evidence set: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sonya of North Orchard lane. Case record id: distractor-008. Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-008. Alias reminders for retrieval: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sonya of North Orchard lane. Case record id: distractor-008. Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-008. Alias reminders for retrieval: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya). Supplemental citation 1 for distractor-008 repeats the verified marker set: linen wick, true object linen wick, linen wick in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sonya of North Orchard lane. Case record id: distractor-008. Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-008. Alias reminders for retrieval: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Sonya of North Orchard lane, linen wick`
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
| 1 | 22544 | n/a | 50.6376 |
| 2 | 22545 | n/a | 26.6411 |
| 3 | 22388 | n/a | 23.5957 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-008. Scoped answer summary for distractor-008 repeats the grounded evidence set: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sonya of North Orchard lane. Case record id: distractor-008. Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-008. Alias reminders for retrieval: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sonya of North Orchard lane. Case record id: distractor-008. Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-008. Alias reminders for retrieval: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya). Supplemental citation 1 for distractor-008 repeats the verified marker set: linen wick, true object linen wick, linen wick in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sonya of North Orchard lane. Case record id: distractor-008. Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-008. Alias reminders for retrieval: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya).
```

## Question 009: distractor-009

**Question:** Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at South Meadow arch`
- aliases `Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch`
- marker `star ledger page`
- aliases `event detail star ledger page, star ledger page in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at South Meadow arch`
- aliases `Bridgefire Supper memory at South Meadow arch, wrong event Bridgefire Supper in South Meadow arch`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Signal Lantern Morning at South Meadow arch, star ledger page`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Signal Lantern Morning at South Meadow arch, star ledger page; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 110 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at South Meadow arch, star ledger page`
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
| 1 | 22547 | n/a | 26.3027 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Morning at South Meadow arch, star ledger page. Case record id: distractor-009. Question: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-009. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); star ledger page (aliases: event detail star ledger page; star ledger page in the correct event). Supplemental citation 1 for distractor-009 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 010: distractor-010

**Question:** Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir?

**Expected evidence:**
- marker `Selma of Birch Ferry shed`
- aliases `Selma from Birch Ferry shed, Birch Ferry shed Selma`
- marker `lantern hook`
- aliases `correct object lantern hook, lantern hook in the true note`

**Forbidden evidence:**
- marker `Damir of Birch Ferry shed`
- aliases `Damir from Birch Ferry shed, Birch Ferry shed Damir`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Selma of Birch Ferry shed, lantern hook`
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
| 1 | 22548 | n/a | 50.4402 |
| 2 | 22549 | n/a | 26.4804 |
| 3 | 22337 | n/a | 23.4030 |

Chunk rank 1:

```text
Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Case scope id: distractor-010. Scoped answer summary for distractor-010 repeats the grounded evidence set: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry shed, lantern hook. Case record id: distractor-010. Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Scope reminder: document distractor-birch-ferry-shed-010. Alias reminders for retrieval: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry shed, lantern hook. Case record id: distractor-010. Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Scope reminder: document distractor-birch-ferry-shed-010. Alias reminders for retrieval: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note). Supplemental citation 1 for distractor-010 repeats the verified marker set: Selma of Birch Ferry shed, Selma from Birch Ferry shed, Birch Ferry shed Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry shed, lantern hook. Case record id: distractor-010. Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Scope reminder: document distractor-birch-ferry-shed-010. Alias reminders for retrieval: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Selma of Birch Ferry shed, lantern hook`
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
| 1 | 22548 | n/a | 50.4028 |
| 2 | 22549 | n/a | 26.4300 |
| 3 | 22337 | n/a | 23.3703 |

Chunk rank 1:

```text
Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Case scope id: distractor-010. Scoped answer summary for distractor-010 repeats the grounded evidence set: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry shed, lantern hook. Case record id: distractor-010. Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Scope reminder: document distractor-birch-ferry-shed-010. Alias reminders for retrieval: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry shed, lantern hook. Case record id: distractor-010. Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Scope reminder: document distractor-birch-ferry-shed-010. Alias reminders for retrieval: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note). Supplemental citation 1 for distractor-010 repeats the verified marker set: Selma of Birch Ferry shed, Selma from Birch Ferry shed, Birch Ferry shed Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry shed, lantern hook. Case record id: distractor-010. Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Scope reminder: document distractor-birch-ferry-shed-010. Alias reminders for retrieval: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note).
```

## Question 011: distractor-011

**Question:** Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

**Expected evidence:**
- marker `March 21 Bellwater Fair`
- aliases `Bellwater Fair on March 21, memory dated March 21`
- marker `Lantern Row kiosk`
- aliases `site Lantern Row kiosk, the place Lantern Row kiosk`

**Forbidden evidence:**
- marker `March 22 Bellwater Fair`
- aliases `Bellwater Fair on March 22, wrong date March 22`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Row kiosk, March 21 Bellwater Fair`
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
| 1 | 22550 | n/a | 50.5904 |
| 2 | 22551 | n/a | 26.6192 |
| 3 | 22611 | n/a | 4.6806 |
| 4 | 22701 | n/a | 4.6192 |
| 5 | 22671 | n/a | 4.6192 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-011. Scoped answer summary for distractor-011 repeats the grounded evidence set: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-041 repeats the verified marker set: March 15 Bellwater Fair, Bellwater Fair on March 15, memory dated March 15. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Row kiosk, March 21 Bellwater Fair`
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
| 1 | 22550 | n/a | 50.5522 |
| 2 | 22551 | n/a | 26.5848 |
| 3 | 22671 | n/a | 4.6046 |
| 4 | 22701 | n/a | 4.5986 |
| 5 | 22581 | n/a | 4.5820 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-011. Scoped answer summary for distractor-011 repeats the grounded evidence set: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 012: distractor-012

**Question:** Which place held the true profile detail for Zora, not the nearly identical place name?

**Expected evidence:**
- marker `Cloud Wharf office`
- aliases `true place Cloud Wharf office, the real location Cloud Wharf office`
- marker `wax thread`
- aliases `profile detail wax thread, wax thread at Cloud Wharf office`

**Forbidden evidence:**
- marker `Fox Hollow bridge`
- aliases `similar place Fox Hollow bridge, wrong location Fox Hollow bridge`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Cloud Wharf office, wax thread`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Cloud Wharf office, wax thread; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 155 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, wax thread`
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
| 1 | 22553 | n/a | 25.8731 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-cloud-wharf-office-012::distractor-012: In document distractor-cloud-wharf-office-012, the verified archive note records Cloud Wharf office, wax thread. Case record id: distractor-012. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-012. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); wax thread (aliases: profile detail wax thread; wax thread at Cloud Wharf office). Supplemental citation 1 for distractor-012 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 013: distractor-013

**Question:** Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `tin key`
- aliases `true object tin key, tin key in Vesna's archive scene`
- marker `Vesna of Ridge Post loft`
- aliases `Vesna from Ridge Post loft, Ridge Post loft scene of Vesna`

**Forbidden evidence:**
- marker `cedar shovel`
- aliases `similar object cedar shovel, wrong object cedar shovel`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Vesna of Ridge Post loft, tin key`
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
| 1 | 22554 | n/a | 50.6944 |
| 2 | 22555 | n/a | 26.7150 |
| 3 | 22395 | n/a | 23.6583 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-013. Scoped answer summary for distractor-013 repeats the grounded evidence set: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna). Supplemental citation 1 for distractor-013 repeats the verified marker set: tin key, true object tin key, tin key in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Vesna of Ridge Post loft, tin key`
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
| 1 | 22554 | n/a | 50.6343 |
| 2 | 22555 | n/a | 26.6694 |
| 3 | 22395 | n/a | 23.5944 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-013. Scoped answer summary for distractor-013 repeats the grounded evidence set: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna). Supplemental citation 1 for distractor-013 repeats the verified marker set: tin key, true object tin key, tin key in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna).
```

## Question 014: distractor-014

**Question:** Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at Willow Courtyard well`
- aliases `Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well`
- marker `blue oar`
- aliases `event detail blue oar, blue oar in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at Willow Courtyard well`
- aliases `Bridgefire Supper memory at Willow Courtyard well, wrong event Bridgefire Supper in Willow Courtyard well`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Willow Courtyard well, blue oar`
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
| 1 | 22556 | n/a | 50.4123 |
| 2 | 22557 | n/a | 26.4094 |
| 3 | 22414 | n/a | 23.3722 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-014. Scoped answer summary for distractor-014 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event). Supplemental citation 1 for distractor-014 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting chunk restates

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Willow Courtyard well, blue oar`
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
| 1 | 22556 | n/a | 50.2931 |
| 2 | 22557 | n/a | 26.3073 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-014. Scoped answer summary for distractor-014 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event). Supplemental citation 1 for distractor-014 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting chunk restates

[truncated in Markdown; full text is available in JSON]
```

## Question 015: distractor-015

**Question:** Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira?

**Expected evidence:**
- marker `Ilya of Bell Bridge square`
- aliases `Ilya from Bell Bridge square, Bell Bridge square Ilya`
- marker `willow basket`
- aliases `correct object willow basket, willow basket in the true note`

**Forbidden evidence:**
- marker `Kira of Bell Bridge square`
- aliases `Kira from Bell Bridge square, Bell Bridge square Kira`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Ilya of Bell Bridge square, willow basket`
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
| 1 | 22558 | n/a | 50.4708 |
| 2 | 22559 | n/a | 26.5137 |
| 3 | 22331 | n/a | 23.4415 |

Chunk rank 1:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer summary for distractor-015 repeats the grounded evidence set: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). Supplemental citation 1 for distractor-015 repeats the verified marker set: Ilya of Bell Bridge square, Ilya from Bell Bridge square, Bell Bridge square Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Ilya of Bell Bridge square, willow basket`
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
| 1 | 22558 | n/a | 50.3636 |
| 2 | 22559 | n/a | 26.4165 |
| 3 | 22331 | n/a | 23.3420 |

Chunk rank 1:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer summary for distractor-015 repeats the grounded evidence set: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). Supplemental citation 1 for distractor-015 repeats the verified marker set: Ilya of Bell Bridge square, Ilya from Bell Bridge square, Bell Bridge square Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note).
```

## Question 016: distractor-016

**Question:** Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

**Expected evidence:**
- marker `March 26 Bellwater Fair`
- aliases `Bellwater Fair on March 26, memory dated March 26`
- marker `Cedar Hill station`
- aliases `site Cedar Hill station, the place Cedar Hill station`

**Forbidden evidence:**
- marker `March 27 Bellwater Fair`
- aliases `Bellwater Fair on March 27, wrong date March 27`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `Cedar Hill station`
- Missing: `March 26 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 5.; Missing expected markers: March 26 Bellwater Fair; Evidence coverage below requirement: 0.500 < 1.000.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22651 | n/a | 4.6806 |
| 2 | 22621 | n/a | 4.6806 |
| 3 | 22591 | n/a | 4.6806 |
| 4 | 22711 | n/a | 4.6192 |
| 5 | 22354 | n/a | 1.5962 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-046 repeats the verified marker set: March 20 Bellwater Fair, Bellwater Fair on March 20, memory dated March 20. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-031 repeats the verified marker set: March 23 Bellwater Fair, Bellwater Fair on March 23, memory dated March 23. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwater Fair, Cedar Hill station. Case record id: distractor-091. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-091. Alias reminders for retrieval: March 11 Bellwater Fair (aliases: Bellwater Fair on March 11; memory dated March 11); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-091 repeats the verified marker set: March 11 Bellwater Fair, Bellwater Fair on March 11, memory dated March 11. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cedar Hill station, March 26 Bellwater Fair`
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
| 1 | 22560 | n/a | 50.5626 |
| 2 | 22561 | n/a | 26.6121 |
| 3 | 22651 | n/a | 4.5957 |
| 4 | 22621 | n/a | 4.5832 |
| 5 | 22711 | n/a | 4.5718 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-016. Scoped answer summary for distractor-016 repeats the grounded evidence set: March 26 Bellwater Fair (aliases: Bellwater Fair on March 26; memory dated March 26); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwater Fair, Cedar Hill station. Case record id: distractor-016. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-016. Alias reminders for retrieval: March 26 Bellwater Fair (aliases: Bellwater Fair on March 26; memory dated March 26); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwater Fair, Cedar Hill station. Case record id: distractor-016. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-016. Alias reminders for retrieval: March 26 Bellwater Fair (aliases: Bellwater Fair on March 26; memory dated March 26); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-016 repeats the verified marker set: March 26 Bellwater Fair, Bellwater Fair on March 26, memory dated March 26. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-046 repeats the verified marker set: March 20 Bellwater Fair, Bellwater Fair on March 20, memory dated March 20. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwater Fair, Cedar Hill station. Case record id: distractor-091. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-091. Alias reminders for retrieval: March 11 Bellwater Fair (aliases: Bellwater Fair on March 11; memory dated March 11); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-091 repeats the verified marker set: March 11 Bellwater Fair, Bellwater Fair on March 11, memory dated March 11. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 017: distractor-017

**Question:** Which place held the true profile detail for Boris, not the nearly identical place name?

**Expected evidence:**
- marker `Moon Mill yard`
- aliases `true place Moon Mill yard, the real location Moon Mill yard`
- marker `glass ink bottle`
- aliases `profile detail glass ink bottle, glass ink bottle at Moon Mill yard`

**Forbidden evidence:**
- marker `Hollow Market arcade`
- aliases `similar place Hollow Market arcade, wrong location Hollow Market arcade`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Moon Mill yard, glass ink bottle`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Moon Mill yard, glass ink bottle; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 125 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Moon Mill yard, glass ink bottle`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Moon Mill yard, glass ink bottle; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 125 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

## Question 018: distractor-018

**Question:** Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `copper wind vane pin`
- aliases `true object copper wind vane pin, copper wind vane pin in Daria's archive scene`
- marker `Daria of Winter Chapel porch`
- aliases `Daria from Winter Chapel porch, Winter Chapel porch scene of Daria`

**Forbidden evidence:**
- marker `carved shell comb`
- aliases `similar object carved shell comb, wrong object carved shell comb`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `copper wind vane pin, Daria of Winter Chapel porch`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: copper wind vane pin, Daria of Winter Chapel porch; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 140 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Daria of Winter Chapel porch, copper wind vane pin`
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
| 1 | 22564 | n/a | 50.4464 |
| 2 | 22565 | n/a | 26.4512 |
| 3 | 22420 | n/a | 23.4066 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-018. Scoped answer summary for distractor-018 repeats the grounded evidence set: copper wind vane pin (aliases: true object copper wind vane pin; copper wind vane pin in Daria's archive scene); Daria of Winter Chapel porch (aliases: Daria from Winter Chapel porch; Winter Chapel porch scene of Daria). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-018::distractor-018: In document distractor-winter-chapel-porch-018, the verified archive note records copper wind vane pin, Daria of Winter Chapel porch. Case record id: distractor-018. Question: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-018. Alias reminders for retrieval: copper wind vane pin (aliases: true object copper wind vane pin; coppe

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-018::distractor-018: In document distractor-winter-chapel-porch-018, the verified archive note records copper wind vane pin, Daria of Winter Chapel porch. Case record id: distractor-018. Question: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-018. Alias reminders for retrieval: copper wind vane pin (aliases: true object copper wind vane pin; copper wind vane pin in Daria's archive scene); Daria of Winter Chapel porch (aliases: Daria from Winter Chapel porch; Winter Chapel porch scene of Daria). Supplemental citation 1 for distractor-018 repeats the verified marker set: copper wind vane pin, true object copper wind vane pin, copper wind vane pin in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-winter-chapel-porch-018::distractor-018: In document distractor-winter-chapel-porch-018, the verified archive note records copper wind vane pin, Daria of Winter Chapel porch. Case record id: distractor-018. Question: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-018. Alias reminders for retrieval: copper wind vane pin (aliases: true object copper wind vane pin; copper wind vane pin in Daria's archive scene); Daria of Winter Chapel porch (aliases: Daria from Winter Chapel porch; Winter Chapel porch scene of Daria).
```

## Question 019: distractor-019

**Question:** Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at Marble stair hall`
- aliases `Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall`
- marker `coal stove hiss`
- aliases `event detail coal stove hiss, coal stove hiss in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at Marble stair hall`
- aliases `Bridgefire Supper memory at Marble stair hall, wrong event Bridgefire Supper in Marble stair hall`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Marble stair hall, coal stove hiss`
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
| 1 | 22567 | n/a | 26.3614 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-019::distractor-019: In document distractor-marble-stair-hall-019, the verified archive note records Signal Lantern Morning at Marble stair hall, coal stove hiss. Case record id: distractor-019. Question: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-019. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); coal stove hiss (aliases: event detail coal stove hiss; coal stove hiss in the correct event). Supplemental citation 1 for distractor-019 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Marble stair hall, coal stove hiss`
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
| 1 | 22566 | n/a | 50.2849 |
| 2 | 22567 | n/a | 26.2972 |
| 3 | 22369 | n/a | 23.2470 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-019. Scoped answer summary for distractor-019 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); coal stove hiss (aliases: event detail coal stove hiss; coal stove hiss in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-019::distractor-019: In document distractor-marble-stair-hall-019, the verified archive note records Signal Lantern Morning at Marble stair hall, coal stove hiss. Case record id: distractor-019. Question: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-019. Alias reminders for retrieval: Signal Lantern Morning at Marble sta

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-019::distractor-019: In document distractor-marble-stair-hall-019, the verified archive note records Signal Lantern Morning at Marble stair hall, coal stove hiss. Case record id: distractor-019. Question: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-019. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); coal stove hiss (aliases: event detail coal stove hiss; coal stove hiss in the correct event). Supplemental citation 1 for distractor-019 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-marble-stair-hall-019::distractor-019: In document distractor-marble-stair-hall-019, the verified archive note records Signal Lantern Morning at Marble stair hall, coal stove hiss. Case record id: distractor-019. Question: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-019. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); coal stove hiss (aliases: event detail coal stove hiss; coal stove hiss in the correct event).
```

## Question 020: distractor-020

**Question:** Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola?

**Expected evidence:**
- marker `Ada of Star Basin gallery`
- aliases `Ada from Star Basin gallery, Star Basin gallery Ada`
- marker `violet ribbon`
- aliases `correct object violet ribbon, violet ribbon in the true note`

**Forbidden evidence:**
- marker `Nikola of Star Basin gallery`
- aliases `Nikola from Star Basin gallery, Star Basin gallery Nikola`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Ada of Star Basin gallery, violet ribbon`
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
| 1 | 22568 | n/a | 50.5756 |
| 2 | 22569 | n/a | 26.6195 |
| 3 | 22408 | n/a | 23.5533 |

Chunk rank 1:

```text
Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Case scope id: distractor-020. Scoped answer summary for distractor-020 repeats the grounded evidence set: Ada of Star Basin gallery (aliases: Ada from Star Basin gallery; Star Basin gallery Ada); violet ribbon (aliases: correct object violet ribbon; violet ribbon in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basin gallery, violet ribbon. Case record id: distractor-020. Question: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Scope reminder: document distractor-star-basin-gallery-020. Alias reminders for retrieval: Ada of Star Basin gallery (aliases: Ada from Star Basin gallery; Star Basin gallery Ada); violet ribbon (aliases: correct object violet ribbon; violet ribbon in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basin gallery, violet ribbon. Case record id: distractor-020. Question: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Scope reminder: document distractor-star-basin-gallery-020. Alias reminders for retrieval: Ada of Star Basin gallery (aliases: Ada from Star Basin gallery; Star Basin gallery Ada); violet ribbon (aliases: correct object violet ribbon; violet ribbon in the true note). Supplemental citation 1 for distractor-020 repeats the verified marker set: Ada of Star Basin gallery, Ada from Star Basin gallery, Star Basin gallery Ada. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basin gallery, violet ribbon. Case record id: distractor-020. Question: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Scope reminder: document distractor-star-basin-gallery-020. Alias reminders for retrieval: Ada of Star Basin gallery (aliases: Ada from Star Basin gallery; Star Basin gallery Ada); violet ribbon (aliases: correct object violet ribbon; violet ribbon in the true note).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Ada of Star Basin gallery, violet ribbon`
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
| 1 | 22568 | n/a | 50.4327 |
| 2 | 22569 | n/a | 26.4682 |
| 3 | 22408 | n/a | 23.4080 |

Chunk rank 1:

```text
Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Case scope id: distractor-020. Scoped answer summary for distractor-020 repeats the grounded evidence set: Ada of Star Basin gallery (aliases: Ada from Star Basin gallery; Star Basin gallery Ada); violet ribbon (aliases: correct object violet ribbon; violet ribbon in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basin gallery, violet ribbon. Case record id: distractor-020. Question: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Scope reminder: document distractor-star-basin-gallery-020. Alias reminders for retrieval: Ada of Star Basin gallery (aliases: Ada from Star Basin gallery; Star Basin gallery Ada); violet ribbon (aliases: correct object violet ribbon; violet ribbon in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basin gallery, violet ribbon. Case record id: distractor-020. Question: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Scope reminder: document distractor-star-basin-gallery-020. Alias reminders for retrieval: Ada of Star Basin gallery (aliases: Ada from Star Basin gallery; Star Basin gallery Ada); violet ribbon (aliases: correct object violet ribbon; violet ribbon in the true note). Supplemental citation 1 for distractor-020 repeats the verified marker set: Ada of Star Basin gallery, Ada from Star Basin gallery, Star Basin gallery Ada. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basin gallery, violet ribbon. Case record id: distractor-020. Question: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Scope reminder: document distractor-star-basin-gallery-020. Alias reminders for retrieval: Ada of Star Basin gallery (aliases: Ada from Star Basin gallery; Star Basin gallery Ada); violet ribbon (aliases: correct object violet ribbon; violet ribbon in the true note).
```

## Question 021: distractor-021

**Question:** Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

**Expected evidence:**
- marker `March 13 Bellwater Fair`
- aliases `Bellwater Fair on March 13, memory dated March 13`
- marker `North Bell workshop`
- aliases `site North Bell workshop, the place North Bell workshop`

**Forbidden evidence:**
- marker `March 14 Bellwater Fair`
- aliases `Bellwater Fair on March 14, wrong date March 14`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `March 13 Bellwater Fair, North Bell workshop`
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
| 1 | 22570 | n/a | 50.5226 |
| 2 | 22571 | n/a | 26.5760 |
| 3 | 22661 | n/a | 4.6377 |
| 4 | 22541 | n/a | 4.5137 |
| 5 | 22385 | n/a | 1.5459 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-021. Scoped answer summary for distractor-021 repeats the grounded evidence set: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `March 13 Bellwater Fair, North Bell workshop`
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
| 1 | 22571 | n/a | 26.6867 |
| 2 | 22541 | n/a | 4.7266 |
| 3 | 22601 | n/a | 4.7056 |
| 4 | 22721 | n/a | 4.7048 |
| 5 | 22661 | n/a | 4.7008 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-096 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 022: distractor-022

**Question:** Which place held the true profile detail for Talia, not the nearly identical place name?

**Expected evidence:**
- marker `Blue Trunk cabin`
- aliases `true place Blue Trunk cabin, the real location Blue Trunk cabin`
- marker `rope bridge permit`
- aliases `profile detail rope bridge permit, rope bridge permit at Blue Trunk cabin`

**Forbidden evidence:**
- marker `East Signal room`
- aliases `similar place East Signal room, wrong location East Signal room`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, rope bridge permit`
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
| 1 | 22573 | n/a | 26.0820 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distractor-022: In document distractor-blue-trunk-cabin-022, the verified archive note records Blue Trunk cabin, rope bridge permit. Case record id: distractor-022. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-022. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); rope bridge permit (aliases: profile detail rope bridge permit; rope bridge permit at Blue Trunk cabin). Supplemental citation 1 for distractor-022 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, rope bridge permit`
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
| 1 | 22573 | n/a | 25.9262 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distractor-022: In document distractor-blue-trunk-cabin-022, the verified archive note records Blue Trunk cabin, rope bridge permit. Case record id: distractor-022. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-022. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); rope bridge permit (aliases: profile detail rope bridge permit; rope bridge permit at Blue Trunk cabin). Supplemental citation 1 for distractor-022 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 023: distractor-023

**Question:** Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `oak barrel hoops`
- aliases `true object oak barrel hoops, oak barrel hoops in Viktor's archive scene`
- marker `Viktor of North Orchard lane`
- aliases `Viktor from North Orchard lane, North Orchard lane scene of Viktor`

**Forbidden evidence:**
- marker `clay watering cup`
- aliases `similar object clay watering cup, wrong object clay watering cup`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Viktor of North Orchard lane, oak barrel hoops`
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
| 1 | 22574 | n/a | 50.5923 |
| 2 | 22575 | n/a | 26.6385 |
| 3 | 22389 | n/a | 23.5175 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-023. Scoped answer summary for distractor-023 repeats the grounded evidence set: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's ar

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor). Supplemental citation 1 for distractor-023 repeats the verified marker set: oak barrel hoops, true object oak barrel hoops, oak barrel hoops in Viktor's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Viktor of North Orchard lane, oak barrel hoops`
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
| 1 | 22574 | n/a | 50.6110 |
| 2 | 22575 | n/a | 26.6201 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-023. Scoped answer summary for distractor-023 repeats the grounded evidence set: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's ar

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor). Supplemental citation 1 for distractor-023 repeats the verified marker set: oak barrel hoops, true object oak barrel hoops, oak barrel hoops in Viktor's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 024: distractor-024

**Question:** Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at South Meadow arch`
- aliases `Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch`
- marker `blue glass jar`
- aliases `event detail blue glass jar, blue glass jar in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at South Meadow arch`
- aliases `Bridgefire Supper memory at South Meadow arch, wrong event Bridgefire Supper in South Meadow arch`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at South Meadow arch, blue glass jar`
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
| 1 | 22576 | n/a | 50.5055 |
| 2 | 22577 | n/a | 26.5041 |
| 3 | 22402 | n/a | 23.4835 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-024. Scoped answer summary for distractor-024 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); blue glass jar (aliases: event detail blue glass jar; blue glass jar in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Morning at South Meadow arch, blue glass jar. Case record id: distractor-024. Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-024. Alias reminders for retrieval: Signal Lantern Morning at South Meadow

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Morning at South Meadow arch, blue glass jar. Case record id: distractor-024. Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-024. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); blue glass jar (aliases: event detail blue glass jar; blue glass jar in the correct event). Supplemental citation 1 for distractor-024 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Morning at South Meadow arch, blue glass jar. Case record id: distractor-024. Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-024. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); blue glass jar (aliases: event detail blue glass jar; blue glass jar in the correct event).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at South Meadow arch, blue glass jar`
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
| 1 | 22576 | n/a | 50.3196 |
| 2 | 22577 | n/a | 26.3286 |
| 3 | 22402 | n/a | 23.2828 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-024. Scoped answer summary for distractor-024 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); blue glass jar (aliases: event detail blue glass jar; blue glass jar in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Morning at South Meadow arch, blue glass jar. Case record id: distractor-024. Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-024. Alias reminders for retrieval: Signal Lantern Morning at South Meadow

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Morning at South Meadow arch, blue glass jar. Case record id: distractor-024. Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-024. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); blue glass jar (aliases: event detail blue glass jar; blue glass jar in the correct event). Supplemental citation 1 for distractor-024 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Morning at South Meadow arch, blue glass jar. Case record id: distractor-024. Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-024. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); blue glass jar (aliases: event detail blue glass jar; blue glass jar in the correct event).
```

## Question 025: distractor-025

**Question:** Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora?

**Expected evidence:**
- marker `Anton of Birch Ferry shed`
- aliases `Anton from Birch Ferry shed, Birch Ferry shed Anton`
- marker `canal route map`
- aliases `correct object canal route map, canal route map in the true note`

**Forbidden evidence:**
- marker `Zora of Birch Ferry shed`
- aliases `Zora from Birch Ferry shed, Birch Ferry shed Zora`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Anton of Birch Ferry shed, canal route map`
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
| 1 | 22579 | n/a | 26.4040 |

Chunk rank 1:

```text
Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry shed, canal route map. Case record id: distractor-025. Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Scope reminder: document distractor-birch-ferry-shed-025. Alias reminders for retrieval: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note). Supplemental citation 1 for distractor-025 repeats the verified marker set: Anton of Birch Ferry shed, Anton from Birch Ferry shed, Birch Ferry shed Anton. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Anton of Birch Ferry shed, canal route map`
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
| 1 | 22578 | n/a | 50.4047 |
| 2 | 22579 | n/a | 26.4319 |
| 3 | 22338 | n/a | 23.3708 |

Chunk rank 1:

```text
Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Case scope id: distractor-025. Scoped answer summary for distractor-025 repeats the grounded evidence set: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry shed, canal route map. Case record id: distractor-025. Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Scope reminder: document distractor-birch-ferry-shed-025. Alias reminders for retrieval: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry shed, canal route map. Case record id: distractor-025. Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Scope reminder: document distractor-birch-ferry-shed-025. Alias reminders for retrieval: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note). Supplemental citation 1 for distractor-025 repeats the verified marker set: Anton of Birch Ferry shed, Anton from Birch Ferry shed, Birch Ferry shed Anton. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry shed, canal route map. Case record id: distractor-025. Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Scope reminder: document distractor-birch-ferry-shed-025. Alias reminders for retrieval: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note).
```

## Question 026: distractor-026

**Question:** Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

**Expected evidence:**
- marker `March 18 Bellwater Fair`
- aliases `Bellwater Fair on March 18, memory dated March 18`
- marker `Lantern Row kiosk`
- aliases `site Lantern Row kiosk, the place Lantern Row kiosk`

**Forbidden evidence:**
- marker `March 19 Bellwater Fair`
- aliases `Bellwater Fair on March 19, wrong date March 19`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Row kiosk, March 18 Bellwater Fair`
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
| 1 | 22580 | n/a | 50.5904 |
| 2 | 22581 | n/a | 26.6192 |
| 3 | 22611 | n/a | 4.6806 |
| 4 | 22701 | n/a | 4.6192 |
| 5 | 22671 | n/a | 4.6192 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-026. Scoped answer summary for distractor-026 repeats the grounded evidence set: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-041 repeats the verified marker set: March 15 Bellwater Fair, Bellwater Fair on March 15, memory dated March 15. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Row kiosk, March 18 Bellwater Fair`
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
| 1 | 22580 | n/a | 50.5434 |
| 2 | 22581 | n/a | 26.5820 |
| 3 | 22671 | n/a | 4.6046 |
| 4 | 22701 | n/a | 4.5986 |
| 5 | 22551 | n/a | 4.5848 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-026. Scoped answer summary for distractor-026 repeats the grounded evidence set: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 027: distractor-027

**Question:** Which place held the true profile detail for Tomas, not the nearly identical place name?

**Expected evidence:**
- marker `Cloud Wharf office`
- aliases `true place Cloud Wharf office, the real location Cloud Wharf office`
- marker `copper token`
- aliases `profile detail copper token, copper token at Cloud Wharf office`

**Forbidden evidence:**
- marker `Fox Hollow bridge`
- aliases `similar place Fox Hollow bridge, wrong location Fox Hollow bridge`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Cloud Wharf office, copper token`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Cloud Wharf office, copper token; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 170 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, copper token`
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
| 1 | 22583 | n/a | 25.8777 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-cloud-wharf-office-027::distractor-027: In document distractor-cloud-wharf-office-027, the verified archive note records Cloud Wharf office, copper token. Case record id: distractor-027. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-027. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); copper token (aliases: profile detail copper token; copper token at Cloud Wharf office). Supplemental citation 1 for distractor-027 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 028: distractor-028

**Question:** Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `moonflower cutting`
- aliases `true object moonflower cutting, moonflower cutting in Vera's archive scene`
- marker `Vera of Ridge Post loft`
- aliases `Vera from Ridge Post loft, Ridge Post loft scene of Vera`

**Forbidden evidence:**
- marker `star ledger page`
- aliases `similar object star ledger page, wrong object star ledger page`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Vera of Ridge Post loft, moonflower cutting`
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
| 1 | 22584 | n/a | 50.6407 |
| 2 | 22585 | n/a | 26.6599 |
| 3 | 22396 | n/a | 23.5964 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-028. Scoped answer summary for distractor-028 repeats the grounded evidence set: moonflower cutting (aliases: true object moonflower cutting; moonflower cutting in Vera's archive scene); Vera of Ridge Post loft (aliases: Vera from Ridge Post loft; Ridge Post loft scene of Vera). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-028::distractor-028: In document distractor-ridge-post-loft-028, the verified archive note records moonflower cutting, Vera of Ridge Post loft. Case record id: distractor-028. Question: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-028. Alias reminders for retrieval: moonflower cutting (aliases: true object moonflower cutting; moonflower cutting in Vera's archive scene); Vera of Ridge Post loft (aliases: Vera from Ridge Post loft; Ridge Post loft scene of Vera).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-028::distractor-028: In document distractor-ridge-post-loft-028, the verified archive note records moonflower cutting, Vera of Ridge Post loft. Case record id: distractor-028. Question: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-028. Alias reminders for retrieval: moonflower cutting (aliases: true object moonflower cutting; moonflower cutting in Vera's archive scene); Vera of Ridge Post loft (aliases: Vera from Ridge Post loft; Ridge Post loft scene of Vera). Supplemental citation 1 for distractor-028 repeats the verified marker set: moonflower cutting, true object moonflower cutting, moonflower cutting in Vera's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-ridge-post-loft-028::distractor-028: In document distractor-ridge-post-loft-028, the verified archive note records moonflower cutting, Vera of Ridge Post loft. Case record id: distractor-028. Question: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-028. Alias reminders for retrieval: moonflower cutting (aliases: true object moonflower cutting; moonflower cutting in Vera's archive scene); Vera of Ridge Post loft (aliases: Vera from Ridge Post loft; Ridge Post loft scene of Vera).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Vera of Ridge Post loft, moonflower cutting`
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
| 1 | 22584 | n/a | 50.5977 |
| 2 | 22585 | n/a | 26.6244 |
| 3 | 22396 | n/a | 23.5566 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-028. Scoped answer summary for distractor-028 repeats the grounded evidence set: moonflower cutting (aliases: true object moonflower cutting; moonflower cutting in Vera's archive scene); Vera of Ridge Post loft (aliases: Vera from Ridge Post loft; Ridge Post loft scene of Vera). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-028::distractor-028: In document distractor-ridge-post-loft-028, the verified archive note records moonflower cutting, Vera of Ridge Post loft. Case record id: distractor-028. Question: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-028. Alias reminders for retrieval: moonflower cutting (aliases: true object moonflower cutting; moonflower cutting in Vera's archive scene); Vera of Ridge Post loft (aliases: Vera from Ridge Post loft; Ridge Post loft scene of Vera).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-028::distractor-028: In document distractor-ridge-post-loft-028, the verified archive note records moonflower cutting, Vera of Ridge Post loft. Case record id: distractor-028. Question: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-028. Alias reminders for retrieval: moonflower cutting (aliases: true object moonflower cutting; moonflower cutting in Vera's archive scene); Vera of Ridge Post loft (aliases: Vera from Ridge Post loft; Ridge Post loft scene of Vera). Supplemental citation 1 for distractor-028 repeats the verified marker set: moonflower cutting, true object moonflower cutting, moonflower cutting in Vera's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-ridge-post-loft-028::distractor-028: In document distractor-ridge-post-loft-028, the verified archive note records moonflower cutting, Vera of Ridge Post loft. Case record id: distractor-028. Question: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-028. Alias reminders for retrieval: moonflower cutting (aliases: true object moonflower cutting; moonflower cutting in Vera's archive scene); Vera of Ridge Post loft (aliases: Vera from Ridge Post loft; Ridge Post loft scene of Vera).
```

## Question 029: distractor-029

**Question:** Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at Willow Courtyard well`
- aliases `Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well`
- marker `birch tea flask`
- aliases `event detail birch tea flask, birch tea flask in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at Willow Courtyard well`
- aliases `Bridgefire Supper memory at Willow Courtyard well, wrong event Bridgefire Supper in Willow Courtyard well`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Willow Courtyard well, birch tea flask`
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
| 1 | 22586 | n/a | 50.4295 |
| 2 | 22587 | n/a | 26.4230 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-029. Scoped answer summary for distractor-029 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); birch tea flask (aliases: event detail birch tea flask; birch tea flask in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-029::distractor-029: In document distractor-willow-courtyard-well-029, the verified archive note records Signal Lantern Morning at Willow Courtyard well, birch tea flask. Case record id: distractor-029. Question: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-029. Alias reminders for retrieval

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-029::distractor-029: In document distractor-willow-courtyard-well-029, the verified archive note records Signal Lantern Morning at Willow Courtyard well, birch tea flask. Case record id: distractor-029. Question: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-029. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); birch tea flask (aliases: event detail birch tea flask; birch tea flask in the correct event). Supplemental citation 1 for distractor-029 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-onl

[truncated in Markdown; full text is available in JSON]
```

### Model: bge_m3

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Willow Courtyard well, birch tea flask`
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
| 1 | 22587 | n/a | 26.2986 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-029::distractor-029: In document distractor-willow-courtyard-well-029, the verified archive note records Signal Lantern Morning at Willow Courtyard well, birch tea flask. Case record id: distractor-029. Question: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-029. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); birch tea flask (aliases: event detail birch tea flask; birch tea flask in the correct event). Supplemental citation 1 for distractor-029 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-onl

[truncated in Markdown; full text is available in JSON]
```

## Question 030: distractor-030

**Question:** Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris?

**Expected evidence:**
- marker `Lina of Bell Bridge square`
- aliases `Lina from Bell Bridge square, Bell Bridge square Lina`
- marker `saffron scarf`
- aliases `correct object saffron scarf, saffron scarf in the true note`

**Forbidden evidence:**
- marker `Boris of Bell Bridge square`
- aliases `Boris from Bell Bridge square, Bell Bridge square Boris`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lina of Bell Bridge square, saffron scarf`
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
| 1 | 22588 | n/a | 50.3407 |
| 2 | 22589 | n/a | 26.4350 |

Chunk rank 1:

```text
Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Case scope id: distractor-030. Scoped answer summary for distractor-030 repeats the grounded evidence set: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bridge square, saffron scarf. Case record id: distractor-030. Question: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Scope reminder: document distractor-bell-bridge-square-030. Alias reminders for retrieval: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bridge square, saffron scarf. Case record id: distractor-030. Question: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Scope reminder: document distractor-bell-bridge-square-030. Alias reminders for retrieval: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note). Supplemental citation 1 for distractor-030 repeats the verified marker set: Lina of Bell Bridge square, Lina from Bell Bridge square, Bell Bridge square Lina. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lina of Bell Bridge square, saffron scarf`
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
| 1 | 22588 | n/a | 50.3821 |
| 2 | 22589 | n/a | 26.4311 |
| 3 | 22332 | n/a | 23.3586 |

Chunk rank 1:

```text
Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Case scope id: distractor-030. Scoped answer summary for distractor-030 repeats the grounded evidence set: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bridge square, saffron scarf. Case record id: distractor-030. Question: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Scope reminder: document distractor-bell-bridge-square-030. Alias reminders for retrieval: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bridge square, saffron scarf. Case record id: distractor-030. Question: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Scope reminder: document distractor-bell-bridge-square-030. Alias reminders for retrieval: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note). Supplemental citation 1 for distractor-030 repeats the verified marker set: Lina of Bell Bridge square, Lina from Bell Bridge square, Bell Bridge square Lina. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bridge square, saffron scarf. Case record id: distractor-030. Question: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Scope reminder: document distractor-bell-bridge-square-030. Alias reminders for retrieval: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note).
```

## Question 031: distractor-031

**Question:** Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

**Expected evidence:**
- marker `March 23 Bellwater Fair`
- aliases `Bellwater Fair on March 23, memory dated March 23`
- marker `Cedar Hill station`
- aliases `site Cedar Hill station, the place Cedar Hill station`

**Forbidden evidence:**
- marker `March 24 Bellwater Fair`
- aliases `Bellwater Fair on March 24, wrong date March 24`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cedar Hill station, March 23 Bellwater Fair`
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
| 1 | 22590 | n/a | 50.6343 |
| 2 | 22591 | n/a | 26.6806 |
| 3 | 22352 | n/a | 23.5962 |
| 4 | 22651 | n/a | 4.6806 |
| 5 | 22621 | n/a | 4.6806 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-031. Scoped answer summary for distractor-031 repeats the grounded evidence set: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-031 repeats the verified marker set: March 23 Bellwater Fair, Bellwater Fair on March 23, memory dated March 23. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-046 repeats the verified marker set: March 20 Bellwater Fair, Bellwater Fair on March 20, memory dated March 20. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cedar Hill station, March 23 Bellwater Fair`
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
| 1 | 22591 | n/a | 26.5603 |
| 2 | 22561 | n/a | 4.6121 |
| 3 | 22651 | n/a | 4.5957 |
| 4 | 22621 | n/a | 4.5832 |
| 5 | 22711 | n/a | 4.5718 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-031 repeats the verified marker set: March 23 Bellwater Fair, Bellwater Fair on March 23, memory dated March 23. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwater Fair, Cedar Hill station. Case record id: distractor-016. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-016. Alias reminders for retrieval: March 26 Bellwater Fair (aliases: Bellwater Fair on March 26; memory dated March 26); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-016 repeats the verified marker set: March 26 Bellwater Fair, Bellwater Fair on March 26, memory dated March 26. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-046 repeats the verified marker set: March 20 Bellwater Fair, Bellwater Fair on March 20, memory dated March 20. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwater Fair, Cedar Hill station. Case record id: distractor-091. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-091. Alias reminders for retrieval: March 11 Bellwater Fair (aliases: Bellwater Fair on March 11; memory dated March 11); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-091 repeats the verified marker set: March 11 Bellwater Fair, Bellwater Fair on March 11, memory dated March 11. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 032: distractor-032

**Question:** Which place held the true profile detail for Yara, not the nearly identical place name?

**Expected evidence:**
- marker `Moon Mill yard`
- aliases `true place Moon Mill yard, the real location Moon Mill yard`
- marker `amber lantern`
- aliases `profile detail amber lantern, amber lantern at Moon Mill yard`

**Forbidden evidence:**
- marker `Hollow Market arcade`
- aliases `similar place Hollow Market arcade, wrong location Hollow Market arcade`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Moon Mill yard, amber lantern`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Moon Mill yard, amber lantern; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 140 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Moon Mill yard, amber lantern`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Moon Mill yard, amber lantern; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 140 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

## Question 033: distractor-033

**Question:** Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `basalt sketch`
- aliases `true object basalt sketch, basalt sketch in Lev's archive scene`
- marker `Lev of Winter Chapel porch`
- aliases `Lev from Winter Chapel porch, Winter Chapel porch scene of Lev`

**Forbidden evidence:**
- marker `blue oar`
- aliases `similar object blue oar, wrong object blue oar`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lev of Winter Chapel porch, basalt sketch`
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
| 1 | 22594 | n/a | 50.4423 |
| 2 | 22595 | n/a | 26.4706 |
| 3 | 22421 | n/a | 23.3870 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-033. Scoped answer summary for distractor-033 repeats the grounded evidence set: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch, Lev of Winter Chapel porch. Case record id: distractor-033. Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-033. Alias reminders for retrieval: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch, Lev of Winter Chapel porch. Case record id: distractor-033. Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-033. Alias reminders for retrieval: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev). Supplemental citation 1 for distractor-033 repeats the verified marker set: basalt sketch, true object basalt sketch, basalt sketch in Lev's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch, Lev of Winter Chapel porch. Case record id: distractor-033. Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-033. Alias reminders for retrieval: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lev of Winter Chapel porch, basalt sketch`
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
| 1 | 22594 | n/a | 50.4190 |
| 2 | 22595 | n/a | 26.4195 |
| 3 | 22421 | n/a | 23.3798 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-033. Scoped answer summary for distractor-033 repeats the grounded evidence set: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch, Lev of Winter Chapel porch. Case record id: distractor-033. Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-033. Alias reminders for retrieval: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch, Lev of Winter Chapel porch. Case record id: distractor-033. Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-033. Alias reminders for retrieval: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev). Supplemental citation 1 for distractor-033 repeats the verified marker set: basalt sketch, true object basalt sketch, basalt sketch in Lev's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch, Lev of Winter Chapel porch. Case record id: distractor-033. Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-033. Alias reminders for retrieval: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev).
```

## Question 034: distractor-034

**Question:** Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at Marble stair hall`
- aliases `Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall`
- marker `green apron`
- aliases `event detail green apron, green apron in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at Marble stair hall`
- aliases `Bridgefire Supper memory at Marble stair hall, wrong event Bridgefire Supper in Marble stair hall`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Marble stair hall, green apron`
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
| 1 | 22596 | n/a | 50.4295 |
| 2 | 22597 | n/a | 26.4230 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-034. Scoped answer summary for distractor-034 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); green apron (aliases: event detail green apron; green apron in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Morning at Marble stair hall, green apron. Case record id: distractor-034. Question: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-034. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (alias

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Morning at Marble stair hall, green apron. Case record id: distractor-034. Question: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-034. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); green apron (aliases: event detail green apron; green apron in the correct event). Supplemental citation 1 for distractor-034 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Marble stair hall, green apron`
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
| 1 | 22596 | n/a | 50.2646 |
| 2 | 22597 | n/a | 26.2757 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-034. Scoped answer summary for distractor-034 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); green apron (aliases: event detail green apron; green apron in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Morning at Marble stair hall, green apron. Case record id: distractor-034. Question: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-034. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (alias

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Morning at Marble stair hall, green apron. Case record id: distractor-034. Question: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-034. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); green apron (aliases: event detail green apron; green apron in the correct event). Supplemental citation 1 for distractor-034 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 035: distractor-035

**Question:** Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia?

**Expected evidence:**
- marker `Pavel of Star Basin gallery`
- aliases `Pavel from Star Basin gallery, Star Basin gallery Pavel`
- marker `silver booth token`
- aliases `correct object silver booth token, silver booth token in the true note`

**Forbidden evidence:**
- marker `Talia of Star Basin gallery`
- aliases `Talia from Star Basin gallery, Star Basin gallery Talia`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Pavel of Star Basin gallery, silver booth token`
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
| 1 | 22598 | n/a | 50.5655 |
| 2 | 22599 | n/a | 26.5950 |
| 3 | 22409 | n/a | 23.5464 |

Chunk rank 1:

```text
Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Case scope id: distractor-035. Scoped answer summary for distractor-035 repeats the grounded evidence set: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note). Supplemental citation 1 for distractor-035 repeats the verified marker set: Pavel of Star Basin gallery, Pavel from Star Basin gallery, Star Basin gallery Pavel. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Pavel of Star Basin gallery, silver booth token`
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
| 1 | 22598 | n/a | 50.4243 |
| 2 | 22599 | n/a | 26.4727 |
| 3 | 22409 | n/a | 23.4105 |

Chunk rank 1:

```text
Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Case scope id: distractor-035. Scoped answer summary for distractor-035 repeats the grounded evidence set: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note). Supplemental citation 1 for distractor-035 repeats the verified marker set: Pavel of Star Basin gallery, Pavel from Star Basin gallery, Star Basin gallery Pavel. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note).
```

## Question 036: distractor-036

**Question:** Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

**Expected evidence:**
- marker `March 10 Bellwater Fair`
- aliases `Bellwater Fair on March 10, memory dated March 10`
- marker `North Bell workshop`
- aliases `site North Bell workshop, the place North Bell workshop`

**Forbidden evidence:**
- marker `March 11 Bellwater Fair`
- aliases `Bellwater Fair on March 11, wrong date March 11`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `North Bell workshop`
- Missing: `March 10 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 4.; Missing expected markers: March 10 Bellwater Fair; Evidence coverage below requirement: 0.500 < 1.000.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22661 | n/a | 4.6377 |
| 2 | 22571 | n/a | 4.5760 |
| 3 | 22541 | n/a | 4.5137 |
| 4 | 22385 | n/a | 1.5459 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `March 10 Bellwater Fair, North Bell workshop`
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
| 1 | 22600 | n/a | 50.6730 |
| 2 | 22601 | n/a | 26.7056 |
| 3 | 22541 | n/a | 4.7266 |
| 4 | 22721 | n/a | 4.7048 |
| 5 | 22661 | n/a | 4.7008 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-036. Scoped answer summary for distractor-036 repeats the grounded evidence set: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-096 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 037: distractor-037

**Question:** Which place held the true profile detail for Damir, not the nearly identical place name?

**Expected evidence:**
- marker `Blue Trunk cabin`
- aliases `true place Blue Trunk cabin, the real location Blue Trunk cabin`
- marker `juniper bundles`
- aliases `profile detail juniper bundles, juniper bundles at Blue Trunk cabin`

**Forbidden evidence:**
- marker `East Signal room`
- aliases `similar place East Signal room, wrong location East Signal room`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, juniper bundles`
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
| 1 | 22602 | n/a | 50.1114 |
| 2 | 22603 | n/a | 26.1922 |
| 3 | 22346 | n/a | 23.0303 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-037. Scoped answer summary for distractor-037 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-037::distractor-037: In document distractor-blue-trunk-cabin-037, the verified archive note records Blue Trunk cabin, juniper bundles. Case record id: distractor-037. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-037. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin).
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-blue-trunk-cabin-037::distractor-037: In document distractor-blue-trunk-cabin-037, the verified archive note records Blue Trunk cabin, juniper bundles. Case record id: distractor-037. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-037. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin). Supplemental citation 1 for distractor-037 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-blue-trunk-cabin-037::distractor-037: In document distractor-blue-trunk-cabin-037, the verified archive note records Blue Trunk cabin, juniper bundles. Case record id: distractor-037. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-037. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, juniper bundles`
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
| 1 | 22602 | n/a | 49.9231 |
| 2 | 22603 | n/a | 25.9729 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-037. Scoped answer summary for distractor-037 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-037::distractor-037: In document distractor-blue-trunk-cabin-037, the verified archive note records Blue Trunk cabin, juniper bundles. Case record id: distractor-037. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-037. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin).
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-blue-trunk-cabin-037::distractor-037: In document distractor-blue-trunk-cabin-037, the verified archive note records Blue Trunk cabin, juniper bundles. Case record id: distractor-037. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-037. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin). Supplemental citation 1 for distractor-037 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 038: distractor-038

**Question:** Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `smoke vent chain`
- aliases `true object smoke vent chain, smoke vent chain in Nessa's archive scene`
- marker `Nessa of North Orchard lane`
- aliases `Nessa from North Orchard lane, North Orchard lane scene of Nessa`

**Forbidden evidence:**
- marker `coal stove hiss`
- aliases `similar object coal stove hiss, wrong object coal stove hiss`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Nessa of North Orchard lane, smoke vent chain`
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
| 1 | 22604 | n/a | 50.5736 |
| 2 | 22605 | n/a | 26.5809 |
| 3 | 22390 | n/a | 23.5228 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-038. Scoped answer summary for distractor-038 repeats the grounded evidence set: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive scene); Nessa of North Orchard lane (aliases: Nessa from North Orchard lane; North Orchard lane scene of Nessa). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain, Nessa of North Orchard lane. Case record id: distractor-038. Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-038. Alias reminders for retrieval: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive sc

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain, Nessa of North Orchard lane. Case record id: distractor-038. Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-038. Alias reminders for retrieval: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive scene); Nessa of North Orchard lane (aliases: Nessa from North Orchard lane; North Orchard lane scene of Nessa). Supplemental citation 1 for distractor-038 repeats the verified marker set: smoke vent chain, true object smoke vent chain, smoke vent chain in Nessa's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain, Nessa of North Orchard lane. Case record id: distractor-038. Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-038. Alias reminders for retrieval: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive scene); Nessa of North Orchard lane (aliases: Nessa from North Orchard lane; North Orchard lane scene of Nessa).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Nessa of North Orchard lane, smoke vent chain`
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
| 1 | 22604 | n/a | 50.6396 |
| 2 | 22605 | n/a | 26.6568 |
| 3 | 22390 | n/a | 23.6036 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-038. Scoped answer summary for distractor-038 repeats the grounded evidence set: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive scene); Nessa of North Orchard lane (aliases: Nessa from North Orchard lane; North Orchard lane scene of Nessa). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain, Nessa of North Orchard lane. Case record id: distractor-038. Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-038. Alias reminders for retrieval: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive sc

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain, Nessa of North Orchard lane. Case record id: distractor-038. Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-038. Alias reminders for retrieval: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive scene); Nessa of North Orchard lane (aliases: Nessa from North Orchard lane; North Orchard lane scene of Nessa). Supplemental citation 1 for distractor-038 repeats the verified marker set: smoke vent chain, true object smoke vent chain, smoke vent chain in Nessa's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain, Nessa of North Orchard lane. Case record id: distractor-038. Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-038. Alias reminders for retrieval: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive scene); Nessa of North Orchard lane (aliases: Nessa from North Orchard lane; North Orchard lane scene of Nessa).
```

## Question 039: distractor-039

**Question:** Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at South Meadow arch`
- aliases `Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch`
- marker `brass compass`
- aliases `event detail brass compass, brass compass in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at South Meadow arch`
- aliases `Bridgefire Supper memory at South Meadow arch, wrong event Bridgefire Supper in South Meadow arch`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Signal Lantern Morning at South Meadow arch, brass compass`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Signal Lantern Morning at South Meadow arch, brass compass; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 140 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at South Meadow arch, brass compass`
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
| 1 | 22606 | n/a | 50.2680 |
| 2 | 22607 | n/a | 26.2973 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-039. Scoped answer summary for distractor-039 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); brass compass (aliases: event detail brass compass; brass compass in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-039::distractor-039: In document distractor-south-meadow-arch-039, the verified archive note records Signal Lantern Morning at South Meadow arch, brass compass. Case record id: distractor-039. Question: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-039. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arc

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-039::distractor-039: In document distractor-south-meadow-arch-039, the verified archive note records Signal Lantern Morning at South Meadow arch, brass compass. Case record id: distractor-039. Question: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-039. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); brass compass (aliases: event detail brass compass; brass compass in the correct event). Supplemental citation 1 for distractor-039 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 040: distractor-040

**Question:** Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas?

**Expected evidence:**
- marker `Mira of Birch Ferry shed`
- aliases `Mira from Birch Ferry shed, Birch Ferry shed Mira`
- marker `linen wick`
- aliases `correct object linen wick, linen wick in the true note`

**Forbidden evidence:**
- marker `Tomas of Birch Ferry shed`
- aliases `Tomas from Birch Ferry shed, Birch Ferry shed Tomas`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Mira of Birch Ferry shed, linen wick`
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
| 1 | 22608 | n/a | 50.4306 |
| 2 | 22609 | n/a | 26.4942 |
| 3 | 22339 | n/a | 23.3919 |

Chunk rank 1:

```text
Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Case scope id: distractor-040. Scoped answer summary for distractor-040 repeats the grounded evidence set: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry shed, linen wick. Case record id: distractor-040. Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Scope reminder: document distractor-birch-ferry-shed-040. Alias reminders for retrieval: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry shed, linen wick. Case record id: distractor-040. Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Scope reminder: document distractor-birch-ferry-shed-040. Alias reminders for retrieval: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note). Supplemental citation 1 for distractor-040 repeats the verified marker set: Mira of Birch Ferry shed, Mira from Birch Ferry shed, Birch Ferry shed Mira. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry shed, linen wick. Case record id: distractor-040. Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Scope reminder: document distractor-birch-ferry-shed-040. Alias reminders for retrieval: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Mira of Birch Ferry shed, linen wick`
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
| 1 | 22608 | n/a | 50.4112 |
| 2 | 22609 | n/a | 26.4279 |
| 3 | 22339 | n/a | 23.3708 |

Chunk rank 1:

```text
Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Case scope id: distractor-040. Scoped answer summary for distractor-040 repeats the grounded evidence set: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry shed, linen wick. Case record id: distractor-040. Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Scope reminder: document distractor-birch-ferry-shed-040. Alias reminders for retrieval: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry shed, linen wick. Case record id: distractor-040. Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Scope reminder: document distractor-birch-ferry-shed-040. Alias reminders for retrieval: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note). Supplemental citation 1 for distractor-040 repeats the verified marker set: Mira of Birch Ferry shed, Mira from Birch Ferry shed, Birch Ferry shed Mira. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry shed, linen wick. Case record id: distractor-040. Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Scope reminder: document distractor-birch-ferry-shed-040. Alias reminders for retrieval: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note).
```

## Question 041: distractor-041

**Question:** Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

**Expected evidence:**
- marker `March 15 Bellwater Fair`
- aliases `Bellwater Fair on March 15, memory dated March 15`
- marker `Lantern Row kiosk`
- aliases `site Lantern Row kiosk, the place Lantern Row kiosk`

**Forbidden evidence:**
- marker `March 16 Bellwater Fair`
- aliases `Bellwater Fair on March 16, wrong date March 16`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Row kiosk, March 15 Bellwater Fair`
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
| 1 | 22610 | n/a | 50.6343 |
| 2 | 22611 | n/a | 26.6806 |
| 3 | 22365 | n/a | 23.5962 |
| 4 | 22701 | n/a | 4.6192 |
| 5 | 22671 | n/a | 4.6192 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-041. Scoped answer summary for distractor-041 repeats the grounded evidence set: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-041 repeats the verified marker set: March 15 Bellwater Fair, Bellwater Fair on March 15, memory dated March 15. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk).
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Row kiosk, March 15 Bellwater Fair`
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
| 1 | 22611 | n/a | 26.5476 |
| 2 | 22671 | n/a | 4.6046 |
| 3 | 22701 | n/a | 4.5986 |
| 4 | 22551 | n/a | 4.5848 |
| 5 | 22581 | n/a | 4.5820 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-041 repeats the verified marker set: March 15 Bellwater Fair, Bellwater Fair on March 15, memory dated March 15. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 042: distractor-042

**Question:** Which place held the true profile detail for Kira, not the nearly identical place name?

**Expected evidence:**
- marker `Cloud Wharf office`
- aliases `true place Cloud Wharf office, the real location Cloud Wharf office`
- marker `lantern hook`
- aliases `profile detail lantern hook, lantern hook at Cloud Wharf office`

**Forbidden evidence:**
- marker `Fox Hollow bridge`
- aliases `similar place Fox Hollow bridge, wrong location Fox Hollow bridge`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Cloud Wharf office, lantern hook`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Cloud Wharf office, lantern hook; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 80 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Cloud Wharf office, lantern hook`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Cloud Wharf office, lantern hook; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 80 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

## Question 043: distractor-043

**Question:** Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `weathered camera strap`
- aliases `true object weathered camera strap, weathered camera strap in Petar's archive scene`
- marker `Petar of Ridge Post loft`
- aliases `Petar from Ridge Post loft, Ridge Post loft scene of Petar`

**Forbidden evidence:**
- marker `blue glass jar`
- aliases `similar object blue glass jar, wrong object blue glass jar`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Petar of Ridge Post loft, weathered camera strap`
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
| 1 | 22614 | n/a | 50.6944 |
| 2 | 22615 | n/a | 26.7150 |
| 3 | 22397 | n/a | 23.6583 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-043. Scoped answer summary for distractor-043 repeats the grounded evidence set: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Petar's archive scene); Petar of Ridge Post loft (aliases: Petar from Ridge Post loft; Ridge Post loft scene of Petar). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap, Petar of Ridge Post loft. Case record id: distractor-043. Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-043. Alias reminders for retrieval: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Pet

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap, Petar of Ridge Post loft. Case record id: distractor-043. Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-043. Alias reminders for retrieval: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Petar's archive scene); Petar of Ridge Post loft (aliases: Petar from Ridge Post loft; Ridge Post loft scene of Petar). Supplemental citation 1 for distractor-043 repeats the verified marker set: weathered camera strap, true object weathered camera strap, weathered camera strap in Petar's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap, Petar of Ridge Post loft. Case record id: distractor-043. Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-043. Alias reminders for retrieval: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Petar's archive scene); Petar of Ridge Post loft (aliases: Petar from Ridge Post loft; Ridge Post loft scene of Petar).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Petar of Ridge Post loft, weathered camera strap`
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
| 1 | 22614 | n/a | 50.6076 |
| 2 | 22615 | n/a | 26.6344 |
| 3 | 22397 | n/a | 23.5783 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-043. Scoped answer summary for distractor-043 repeats the grounded evidence set: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Petar's archive scene); Petar of Ridge Post loft (aliases: Petar from Ridge Post loft; Ridge Post loft scene of Petar). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap, Petar of Ridge Post loft. Case record id: distractor-043. Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-043. Alias reminders for retrieval: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Pet

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap, Petar of Ridge Post loft. Case record id: distractor-043. Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-043. Alias reminders for retrieval: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Petar's archive scene); Petar of Ridge Post loft (aliases: Petar from Ridge Post loft; Ridge Post loft scene of Petar). Supplemental citation 1 for distractor-043 repeats the verified marker set: weathered camera strap, true object weathered camera strap, weathered camera strap in Petar's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap, Petar of Ridge Post loft. Case record id: distractor-043. Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-043. Alias reminders for retrieval: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Petar's archive scene); Petar of Ridge Post loft (aliases: Petar from Ridge Post loft; Ridge Post loft scene of Petar).
```

## Question 044: distractor-044

**Question:** Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at Willow Courtyard well`
- aliases `Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well`
- marker `wax thread`
- aliases `event detail wax thread, wax thread in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at Willow Courtyard well`
- aliases `Bridgefire Supper memory at Willow Courtyard well, wrong event Bridgefire Supper in Willow Courtyard well`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Willow Courtyard well, wax thread`
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
| 1 | 22616 | n/a | 50.4123 |
| 2 | 22617 | n/a | 26.4094 |
| 3 | 22416 | n/a | 23.3722 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-044. Scoped answer summary for distractor-044 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); wax thread (aliases: event detail wax thread; wax thread in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lantern Morning at Willow Courtyard well, wax thread. Case record id: distractor-044. Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-044. Alias reminders for retrieval: Signal Lantern Morni

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lantern Morning at Willow Courtyard well, wax thread. Case record id: distractor-044. Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-044. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); wax thread (aliases: event detail wax thread; wax thread in the correct event). Supplemental citation 1 for distractor-044 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting chunk res

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lantern Morning at Willow Courtyard well, wax thread. Case record id: distractor-044. Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-044. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); wax thread (aliases: event detail wax thread; wax thread in the correct event).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Willow Courtyard well, wax thread`
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
| 1 | 22616 | n/a | 50.3056 |
| 2 | 22617 | n/a | 26.3119 |
| 3 | 22416 | n/a | 23.2631 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-044. Scoped answer summary for distractor-044 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); wax thread (aliases: event detail wax thread; wax thread in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lantern Morning at Willow Courtyard well, wax thread. Case record id: distractor-044. Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-044. Alias reminders for retrieval: Signal Lantern Morni

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lantern Morning at Willow Courtyard well, wax thread. Case record id: distractor-044. Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-044. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); wax thread (aliases: event detail wax thread; wax thread in the correct event). Supplemental citation 1 for distractor-044 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting chunk res

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lantern Morning at Willow Courtyard well, wax thread. Case record id: distractor-044. Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-044. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); wax thread (aliases: event detail wax thread; wax thread in the correct event).
```

## Question 045: distractor-045

**Question:** Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara?

**Expected evidence:**
- marker `Stefan of Bell Bridge square`
- aliases `Stefan from Bell Bridge square, Bell Bridge square Stefan`
- marker `tin key`
- aliases `correct object tin key, tin key in the true note`

**Forbidden evidence:**
- marker `Yara of Bell Bridge square`
- aliases `Yara from Bell Bridge square, Bell Bridge square Yara`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Stefan of Bell Bridge square, tin key`
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
| 1 | 22618 | n/a | 50.3842 |
| 2 | 22619 | n/a | 26.4565 |
| 3 | 22333 | n/a | 23.3595 |

Chunk rank 1:

```text
Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Case scope id: distractor-045. Scoped answer summary for distractor-045 repeats the grounded evidence set: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell Bridge square, tin key. Case record id: distractor-045. Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Scope reminder: document distractor-bell-bridge-square-045. Alias reminders for retrieval: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell Bridge square, tin key. Case record id: distractor-045. Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Scope reminder: document distractor-bell-bridge-square-045. Alias reminders for retrieval: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note). Supplemental citation 1 for distractor-045 repeats the verified marker set: Stefan of Bell Bridge square, Stefan from Bell Bridge square, Bell Bridge square Stefan. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell Bridge square, tin key. Case record id: distractor-045. Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Scope reminder: document distractor-bell-bridge-square-045. Alias reminders for retrieval: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Stefan of Bell Bridge square, tin key`
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
| 1 | 22618 | n/a | 50.4009 |
| 2 | 22619 | n/a | 26.4323 |
| 3 | 22333 | n/a | 23.3667 |

Chunk rank 1:

```text
Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Case scope id: distractor-045. Scoped answer summary for distractor-045 repeats the grounded evidence set: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell Bridge square, tin key. Case record id: distractor-045. Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Scope reminder: document distractor-bell-bridge-square-045. Alias reminders for retrieval: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell Bridge square, tin key. Case record id: distractor-045. Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Scope reminder: document distractor-bell-bridge-square-045. Alias reminders for retrieval: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note). Supplemental citation 1 for distractor-045 repeats the verified marker set: Stefan of Bell Bridge square, Stefan from Bell Bridge square, Bell Bridge square Stefan. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell Bridge square, tin key. Case record id: distractor-045. Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Scope reminder: document distractor-bell-bridge-square-045. Alias reminders for retrieval: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note).
```

## Question 046: distractor-046

**Question:** Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

**Expected evidence:**
- marker `March 20 Bellwater Fair`
- aliases `Bellwater Fair on March 20, memory dated March 20`
- marker `Cedar Hill station`
- aliases `site Cedar Hill station, the place Cedar Hill station`

**Forbidden evidence:**
- marker `March 21 Bellwater Fair`
- aliases `Bellwater Fair on March 21, wrong date March 21`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cedar Hill station, March 20 Bellwater Fair`
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
| 1 | 22620 | n/a | 50.6343 |
| 2 | 22621 | n/a | 26.6806 |
| 3 | 22353 | n/a | 23.5962 |
| 4 | 22651 | n/a | 4.6806 |
| 5 | 22591 | n/a | 4.6806 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-046. Scoped answer summary for distractor-046 repeats the grounded evidence set: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-046 repeats the verified marker set: March 20 Bellwater Fair, Bellwater Fair on March 20, memory dated March 20. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-031 repeats the verified marker set: March 23 Bellwater Fair, Bellwater Fair on March 23, memory dated March 23. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cedar Hill station, March 20 Bellwater Fair`
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
| 1 | 22620 | n/a | 50.5399 |
| 2 | 22621 | n/a | 26.5832 |
| 3 | 22561 | n/a | 4.6121 |
| 4 | 22651 | n/a | 4.5957 |
| 5 | 22711 | n/a | 4.5718 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-046. Scoped answer summary for distractor-046 repeats the grounded evidence set: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-046 repeats the verified marker set: March 20 Bellwater Fair, Bellwater Fair on March 20, memory dated March 20. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwater Fair, Cedar Hill station. Case record id: distractor-016. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-016. Alias reminders for retrieval: March 26 Bellwater Fair (aliases: Bellwater Fair on March 26; memory dated March 26); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-016 repeats the verified marker set: March 26 Bellwater Fair, Bellwater Fair on March 26, memory dated March 26. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwater Fair, Cedar Hill station. Case record id: distractor-091. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-091. Alias reminders for retrieval: March 11 Bellwater Fair (aliases: Bellwater Fair on March 11; memory dated March 11); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-091 repeats the verified marker set: March 11 Bellwater Fair, Bellwater Fair on March 11, memory dated March 11. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 047: distractor-047

**Question:** Which place held the true profile detail for Nikola, not the nearly identical place name?

**Expected evidence:**
- marker `Moon Mill yard`
- aliases `true place Moon Mill yard, the real location Moon Mill yard`
- marker `willow basket`
- aliases `profile detail willow basket, willow basket at Moon Mill yard`

**Forbidden evidence:**
- marker `Hollow Market arcade`
- aliases `similar place Hollow Market arcade, wrong location Hollow Market arcade`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Moon Mill yard, willow basket`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Moon Mill yard, willow basket; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 155 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Moon Mill yard, willow basket`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Moon Mill yard, willow basket; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 155 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

## Question 048: distractor-048

**Question:** Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `paper moon mask`
- aliases `true object paper moon mask, paper moon mask in Sonya's archive scene`
- marker `Sonya of Winter Chapel porch`
- aliases `Sonya from Winter Chapel porch, Winter Chapel porch scene of Sonya`

**Forbidden evidence:**
- marker `birch tea flask`
- aliases `similar object birch tea flask, wrong object birch tea flask`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Sonya of Winter Chapel porch, paper moon mask`
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
| 1 | 22624 | n/a | 50.4524 |
| 2 | 22625 | n/a | 26.4612 |
| 3 | 22422 | n/a | 23.4111 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-048. Scoped answer summary for distractor-048 repeats the grounded evidence set: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive scene); Sonya of Winter Chapel porch (aliases: Sonya from Winter Chapel porch; Winter Chapel porch scene of Sonya). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mask, Sonya of Winter Chapel porch. Case record id: distractor-048. Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-048. Alias reminders for retrieval: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mask, Sonya of Winter Chapel porch. Case record id: distractor-048. Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-048. Alias reminders for retrieval: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive scene); Sonya of Winter Chapel porch (aliases: Sonya from Winter Chapel porch; Winter Chapel porch scene of Sonya). Supplemental citation 1 for distractor-048 repeats the verified marker set: paper moon mask, true object paper moon mask, paper moon mask in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mask, Sonya of Winter Chapel porch. Case record id: distractor-048. Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-048. Alias reminders for retrieval: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive scene); Sonya of Winter Chapel porch (aliases: Sonya from Winter Chapel porch; Winter Chapel porch scene of Sonya).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Sonya of Winter Chapel porch, paper moon mask`
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
| 1 | 22624 | n/a | 50.4402 |
| 2 | 22625 | n/a | 26.4438 |
| 3 | 22422 | n/a | 23.4053 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-048. Scoped answer summary for distractor-048 repeats the grounded evidence set: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive scene); Sonya of Winter Chapel porch (aliases: Sonya from Winter Chapel porch; Winter Chapel porch scene of Sonya). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mask, Sonya of Winter Chapel porch. Case record id: distractor-048. Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-048. Alias reminders for retrieval: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mask, Sonya of Winter Chapel porch. Case record id: distractor-048. Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-048. Alias reminders for retrieval: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive scene); Sonya of Winter Chapel porch (aliases: Sonya from Winter Chapel porch; Winter Chapel porch scene of Sonya). Supplemental citation 1 for distractor-048 repeats the verified marker set: paper moon mask, true object paper moon mask, paper moon mask in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mask, Sonya of Winter Chapel porch. Case record id: distractor-048. Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-048. Alias reminders for retrieval: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive scene); Sonya of Winter Chapel porch (aliases: Sonya from Winter Chapel porch; Winter Chapel porch scene of Sonya).
```

## Question 049: distractor-049

**Question:** Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at Marble stair hall`
- aliases `Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall`
- marker `glass ink bottle`
- aliases `event detail glass ink bottle, glass ink bottle in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at Marble stair hall`
- aliases `Bridgefire Supper memory at Marble stair hall, wrong event Bridgefire Supper in Marble stair hall`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Marble stair hall, glass ink bottle`
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
| 1 | 22626 | n/a | 50.3921 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-049. Scoped answer summary for distractor-049 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); glass ink bottle (aliases: event detail glass ink bottle; glass ink bottle in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-049::distractor-049: In document distractor-marble-stair-hall-049, the verified archive note records Signal Lantern Morning at Marble stair hall, glass ink bottle. Case record id: distractor-049. Question: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-049. Alias reminders for retrieval: Signal Lantern Morning at Marble

[truncated in Markdown; full text is available in JSON]
```

### Model: bge_m3

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Marble stair hall, glass ink bottle`
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
| 1 | 22627 | n/a | 26.2623 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-049::distractor-049: In document distractor-marble-stair-hall-049, the verified archive note records Signal Lantern Morning at Marble stair hall, glass ink bottle. Case record id: distractor-049. Question: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-049. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); glass ink bottle (aliases: event detail glass ink bottle; glass ink bottle in the correct event). Supplemental citation 1 for distractor-049 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 050: distractor-050

**Question:** Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir?

**Expected evidence:**
- marker `Selma of Star Basin gallery`
- aliases `Selma from Star Basin gallery, Star Basin gallery Selma`
- marker `copper wind vane pin`
- aliases `correct object copper wind vane pin, copper wind vane pin in the true note`

**Forbidden evidence:**
- marker `Damir of Star Basin gallery`
- aliases `Damir from Star Basin gallery, Star Basin gallery Damir`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Selma of Star Basin gallery, copper wind vane pin`
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
| 1 | 22629 | n/a | 26.4792 |

Chunk rank 1:

```text
Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? document distractor-star-basin-gallery-050::distractor-050: In document distractor-star-basin-gallery-050, the verified archive note records Selma of Star Basin gallery, copper wind vane pin. Case record id: distractor-050. Question: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Scope reminder: document distractor-star-basin-gallery-050. Alias reminders for retrieval: Selma of Star Basin gallery (aliases: Selma from Star Basin gallery; Star Basin gallery Selma); copper wind vane pin (aliases: correct object copper wind vane pin; copper wind vane pin in the true note). Supplemental citation 1 for distractor-050 repeats the verified marker set: Selma of Star Basin gallery, Selma from Star Basin gallery, Star Basin gallery Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Selma of Star Basin gallery, copper wind vane pin`
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
| 1 | 22628 | n/a | 50.4146 |
| 2 | 22629 | n/a | 26.4594 |
| 3 | 22410 | n/a | 23.3922 |

Chunk rank 1:

```text
Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Case scope id: distractor-050. Scoped answer summary for distractor-050 repeats the grounded evidence set: Selma of Star Basin gallery (aliases: Selma from Star Basin gallery; Star Basin gallery Selma); copper wind vane pin (aliases: correct object copper wind vane pin; copper wind vane pin in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-050::distractor-050: In document distractor-star-basin-gallery-050, the verified archive note records Selma of Star Basin gallery, copper wind vane pin. Case record id: distractor-050. Question: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Scope reminder: document distractor-star-basin-gallery-050. Alias reminders for retrieval: Selma of Star Basin gallery (aliases: Selma from Star Basin gallery; Star Basin gallery Selma); copper wind vane pin (aliases: correct object copper wind vane pin; copper wind vane pin in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? document distractor-star-basin-gallery-050::distractor-050: In document distractor-star-basin-gallery-050, the verified archive note records Selma of Star Basin gallery, copper wind vane pin. Case record id: distractor-050. Question: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Scope reminder: document distractor-star-basin-gallery-050. Alias reminders for retrieval: Selma of Star Basin gallery (aliases: Selma from Star Basin gallery; Star Basin gallery Selma); copper wind vane pin (aliases: correct object copper wind vane pin; copper wind vane pin in the true note). Supplemental citation 1 for distractor-050 repeats the verified marker set: Selma of Star Basin gallery, Selma from Star Basin gallery, Star Basin gallery Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-050::distractor-050: In document distractor-star-basin-gallery-050, the verified archive note records Selma of Star Basin gallery, copper wind vane pin. Case record id: distractor-050. Question: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Scope reminder: document distractor-star-basin-gallery-050. Alias reminders for retrieval: Selma of Star Basin gallery (aliases: Selma from Star Basin gallery; Star Basin gallery Selma); copper wind vane pin (aliases: correct object copper wind vane pin; copper wind vane pin in the true note).
```

## Question 051: distractor-051

**Question:** Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

**Expected evidence:**
- marker `March 25 Bellwater Fair`
- aliases `Bellwater Fair on March 25, memory dated March 25`
- marker `North Bell workshop`
- aliases `site North Bell workshop, the place North Bell workshop`

**Forbidden evidence:**
- marker `March 26 Bellwater Fair`
- aliases `Bellwater Fair on March 26, wrong date March 26`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `North Bell workshop`
- Missing: `March 25 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 4.; Missing expected markers: March 25 Bellwater Fair; Evidence coverage below requirement: 0.500 < 1.000.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22661 | n/a | 4.6377 |
| 2 | 22571 | n/a | 4.5760 |
| 3 | 22541 | n/a | 4.5137 |
| 4 | 22385 | n/a | 1.5459 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

### Model: bge_m3

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `North Bell workshop`
- Missing: `March 25 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 5.; Missing expected markers: March 25 Bellwater Fair; Evidence coverage below requirement: 0.500 < 1.000.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22541 | n/a | 4.7266 |
| 2 | 22601 | n/a | 4.7056 |
| 3 | 22721 | n/a | 4.7048 |
| 4 | 22661 | n/a | 4.7008 |
| 5 | 22691 | n/a | 4.6989 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-096 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellwater Fair, North Bell workshop. Case record id: distractor-081. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-081. Alias reminders for retrieval: March 19 Bellwater Fair (aliases: Bellwater Fair on March 19; memory dated March 19); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-081 repeats the verified marker set: March 19 Bellwater Fair, Bellwater Fair on March 19, memory dated March 19. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 052: distractor-052

**Question:** Which place held the true profile detail for Zora, not the nearly identical place name?

**Expected evidence:**
- marker `Blue Trunk cabin`
- aliases `true place Blue Trunk cabin, the real location Blue Trunk cabin`
- marker `violet ribbon`
- aliases `profile detail violet ribbon, violet ribbon at Blue Trunk cabin`

**Forbidden evidence:**
- marker `East Signal room`
- aliases `similar place East Signal room, wrong location East Signal room`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, violet ribbon`
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
| 1 | 22632 | n/a | 50.1072 |
| 2 | 22633 | n/a | 26.1857 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary for distractor-052 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-052::distractor-052: In document distractor-blue-trunk-cabin-052, the verified archive note records Blue Trunk cabin, violet ribbon. Case record id: distractor-052. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-052. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin).
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor-052: In document distractor-blue-trunk-cabin-052, the verified archive note records Blue Trunk cabin, violet ribbon. Case record id: distractor-052. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-052. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin). Supplemental citation 1 for distractor-052 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, violet ribbon`
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
| 1 | 22632 | n/a | 49.9034 |
| 2 | 22633 | n/a | 25.9502 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary for distractor-052 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-052::distractor-052: In document distractor-blue-trunk-cabin-052, the verified archive note records Blue Trunk cabin, violet ribbon. Case record id: distractor-052. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-052. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin).
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor-052: In document distractor-blue-trunk-cabin-052, the verified archive note records Blue Trunk cabin, violet ribbon. Case record id: distractor-052. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-052. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin). Supplemental citation 1 for distractor-052 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 053: distractor-053

**Question:** Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `tuning fork`
- aliases `true object tuning fork, tuning fork in Vesna's archive scene`
- marker `Vesna of North Orchard lane`
- aliases `Vesna from North Orchard lane, North Orchard lane scene of Vesna`

**Forbidden evidence:**
- marker `green apron`
- aliases `similar object green apron, wrong object green apron`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Vesna of North Orchard lane, tuning fork`
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
| 1 | 22634 | n/a | 50.6024 |
| 2 | 22635 | n/a | 26.6112 |
| 3 | 22391 | n/a | 23.5611 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-053. Scoped answer summary for distractor-053 repeats the grounded evidence set: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Vesna of North Orchard lane. Case record id: distractor-053. Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-053. Alias reminders for retrieval: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Vesna of North Orchard lane. Case record id: distractor-053. Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-053. Alias reminders for retrieval: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna). Supplemental citation 1 for distractor-053 repeats the verified marker set: tuning fork, true object tuning fork, tuning fork in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Vesna of North Orchard lane. Case record id: distractor-053. Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-053. Alias reminders for retrieval: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Vesna of North Orchard lane, tuning fork`
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
| 1 | 22634 | n/a | 50.6355 |
| 2 | 22635 | n/a | 26.6599 |
| 3 | 22391 | n/a | 23.5977 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-053. Scoped answer summary for distractor-053 repeats the grounded evidence set: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Vesna of North Orchard lane. Case record id: distractor-053. Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-053. Alias reminders for retrieval: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Vesna of North Orchard lane. Case record id: distractor-053. Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-053. Alias reminders for retrieval: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna). Supplemental citation 1 for distractor-053 repeats the verified marker set: tuning fork, true object tuning fork, tuning fork in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Vesna of North Orchard lane. Case record id: distractor-053. Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-053. Alias reminders for retrieval: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna).
```

## Question 054: distractor-054

**Question:** Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at South Meadow arch`
- aliases `Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch`
- marker `rope bridge permit`
- aliases `event detail rope bridge permit, rope bridge permit in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at South Meadow arch`
- aliases `Bridgefire Supper memory at South Meadow arch, wrong event Bridgefire Supper in South Meadow arch`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at South Meadow arch, rope bridge permit`
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
| 1 | 22637 | n/a | 26.4178 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Morning at South Meadow arch, rope bridge permit. Case record id: distractor-054. Question: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-054. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); rope bridge permit (aliases: event detail rope bridge permit; rope bridge permit in the correct event). Supplemental citation 1 for distractor-054 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at South Meadow arch, rope bridge permit`
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
| 1 | 22636 | n/a | 50.2744 |
| 2 | 22637 | n/a | 26.3031 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-054. Scoped answer summary for distractor-054 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); rope bridge permit (aliases: event detail rope bridge permit; rope bridge permit in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Morning at South Meadow arch, rope bridge permit. Case record id: distractor-054. Question: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-054. Alias reminders for retrieval: Signal Lantern Morning

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Morning at South Meadow arch, rope bridge permit. Case record id: distractor-054. Question: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-054. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); rope bridge permit (aliases: event detail rope bridge permit; rope bridge permit in the correct event). Supplemental citation 1 for distractor-054 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 055: distractor-055

**Question:** Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira?

**Expected evidence:**
- marker `Ilya of Birch Ferry shed`
- aliases `Ilya from Birch Ferry shed, Birch Ferry shed Ilya`
- marker `oak barrel hoops`
- aliases `correct object oak barrel hoops, oak barrel hoops in the true note`

**Forbidden evidence:**
- marker `Kira of Birch Ferry shed`
- aliases `Kira from Birch Ferry shed, Birch Ferry shed Kira`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Ilya of Birch Ferry shed, oak barrel hoops`
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
| 1 | 22638 | n/a | 50.4708 |
| 2 | 22639 | n/a | 26.5137 |
| 3 | 22340 | n/a | 23.4415 |

Chunk rank 1:

```text
Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Case scope id: distractor-055. Scoped answer summary for distractor-055 repeats the grounded evidence set: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note). Supplemental citation 1 for distractor-055 repeats the verified marker set: Ilya of Birch Ferry shed, Ilya from Birch Ferry shed, Birch Ferry shed Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Ilya of Birch Ferry shed, oak barrel hoops`
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
| 1 | 22638 | n/a | 50.3838 |
| 2 | 22639 | n/a | 26.4307 |
| 3 | 22340 | n/a | 23.3610 |

Chunk rank 1:

```text
Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Case scope id: distractor-055. Scoped answer summary for distractor-055 repeats the grounded evidence set: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note). Supplemental citation 1 for distractor-055 repeats the verified marker set: Ilya of Birch Ferry shed, Ilya from Birch Ferry shed, Birch Ferry shed Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note).
```

## Question 056: distractor-056

**Question:** Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

**Expected evidence:**
- marker `March 12 Bellwater Fair`
- aliases `Bellwater Fair on March 12, memory dated March 12`
- marker `Lantern Row kiosk`
- aliases `site Lantern Row kiosk, the place Lantern Row kiosk`

**Forbidden evidence:**
- marker `March 13 Bellwater Fair`
- aliases `Bellwater Fair on March 13, wrong date March 13`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `Lantern Row kiosk`
- Missing: `March 12 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 5.; Missing expected markers: March 12 Bellwater Fair; Evidence coverage below requirement: 0.500 < 1.000.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22611 | n/a | 4.6806 |
| 2 | 22701 | n/a | 4.6192 |
| 3 | 22671 | n/a | 4.6192 |
| 4 | 22581 | n/a | 4.6192 |
| 5 | 22551 | n/a | 4.6192 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-041 repeats the verified marker set: March 15 Bellwater Fair, Bellwater Fair on March 15, memory dated March 15. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Row kiosk, March 12 Bellwater Fair`
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
| 1 | 22641 | n/a | 26.5527 |
| 2 | 22671 | n/a | 4.6046 |
| 3 | 22701 | n/a | 4.5986 |
| 4 | 22551 | n/a | 4.5848 |
| 5 | 22581 | n/a | 4.5820 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-056::distractor-056: In document distractor-lantern-row-kiosk-056, the verified archive note records March 12 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-056. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-056. Alias reminders for retrieval: March 12 Bellwater Fair (aliases: Bellwater Fair on March 12; memory dated March 12); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-056 repeats the verified marker set: March 12 Bellwater Fair, Bellwater Fair on March 12, memory dated March 12. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 057: distractor-057

**Question:** Which place held the true profile detail for Boris, not the nearly identical place name?

**Expected evidence:**
- marker `Cloud Wharf office`
- aliases `true place Cloud Wharf office, the real location Cloud Wharf office`
- marker `canal route map`
- aliases `profile detail canal route map, canal route map at Cloud Wharf office`

**Forbidden evidence:**
- marker `Fox Hollow bridge`
- aliases `similar place Fox Hollow bridge, wrong location Fox Hollow bridge`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Cloud Wharf office, canal route map`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Cloud Wharf office, canal route map; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 95 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Cloud Wharf office, canal route map`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Cloud Wharf office, canal route map; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 95 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

## Question 058: distractor-058

**Question:** Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `cedar shovel`
- aliases `true object cedar shovel, cedar shovel in Daria's archive scene`
- marker `Daria of Ridge Post loft`
- aliases `Daria from Ridge Post loft, Ridge Post loft scene of Daria`

**Forbidden evidence:**
- marker `brass compass`
- aliases `similar object brass compass, wrong object brass compass`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Daria of Ridge Post loft, cedar shovel`
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
| 1 | 22644 | n/a | 50.6173 |
| 2 | 22645 | n/a | 26.6242 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-058. Scoped answer summary for distractor-058 repeats the grounded evidence set: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of Ridge Post loft. Case record id: distractor-058. Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-058. Alias reminders for retrieval: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of Ridge Post loft. Case record id: distractor-058. Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-058. Alias reminders for retrieval: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria). Supplemental citation 1 for distractor-058 repeats the verified marker set: cedar shovel, true object cedar shovel, cedar shovel in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Daria of Ridge Post loft, cedar shovel`
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
| 1 | 22644 | n/a | 50.6431 |
| 2 | 22645 | n/a | 26.6753 |
| 3 | 22398 | n/a | 23.5925 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-058. Scoped answer summary for distractor-058 repeats the grounded evidence set: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of Ridge Post loft. Case record id: distractor-058. Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-058. Alias reminders for retrieval: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of Ridge Post loft. Case record id: distractor-058. Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-058. Alias reminders for retrieval: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria). Supplemental citation 1 for distractor-058 repeats the verified marker set: cedar shovel, true object cedar shovel, cedar shovel in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of Ridge Post loft. Case record id: distractor-058. Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-058. Alias reminders for retrieval: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria).
```

## Question 059: distractor-059

**Question:** Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at Willow Courtyard well`
- aliases `Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well`
- marker `copper token`
- aliases `event detail copper token, copper token in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at Willow Courtyard well`
- aliases `Bridgefire Supper memory at Willow Courtyard well, wrong event Bridgefire Supper in Willow Courtyard well`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Willow Courtyard well, copper token`
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
| 1 | 22646 | n/a | 50.4123 |
| 2 | 22647 | n/a | 26.4094 |
| 3 | 22417 | n/a | 23.3722 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-059. Scoped answer summary for distractor-059 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lante

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event). Supplemental citation 1 for distractor-059 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting c

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Willow Courtyard well, copper token`
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
| 1 | 22646 | n/a | 50.3102 |
| 2 | 22647 | n/a | 26.3208 |
| 3 | 22417 | n/a | 23.2743 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-059. Scoped answer summary for distractor-059 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lante

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event). Supplemental citation 1 for distractor-059 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting c

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event).
```

## Question 060: distractor-060

**Question:** Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola?

**Expected evidence:**
- marker `Ada of Bell Bridge square`
- aliases `Ada from Bell Bridge square, Bell Bridge square Ada`
- marker `moonflower cutting`
- aliases `correct object moonflower cutting, moonflower cutting in the true note`

**Forbidden evidence:**
- marker `Nikola of Bell Bridge square`
- aliases `Nikola from Bell Bridge square, Bell Bridge square Nikola`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Ada of Bell Bridge square, moonflower cutting`
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
| 1 | 22648 | n/a | 50.5107 |
| 2 | 22649 | n/a | 26.5680 |
| 3 | 22334 | n/a | 23.4786 |

Chunk rank 1:

```text
Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Case scope id: distractor-060. Scoped answer summary for distractor-060 repeats the grounded evidence set: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Bridge square, moonflower cutting. Case record id: distractor-060. Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Scope reminder: document distractor-bell-bridge-square-060. Alias reminders for retrieval: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Bridge square, moonflower cutting. Case record id: distractor-060. Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Scope reminder: document distractor-bell-bridge-square-060. Alias reminders for retrieval: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note). Supplemental citation 1 for distractor-060 repeats the verified marker set: Ada of Bell Bridge square, Ada from Bell Bridge square, Bell Bridge square Ada. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Bridge square, moonflower cutting. Case record id: distractor-060. Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Scope reminder: document distractor-bell-bridge-square-060. Alias reminders for retrieval: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Ada of Bell Bridge square, moonflower cutting`
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
| 1 | 22648 | n/a | 50.4037 |
| 2 | 22649 | n/a | 26.4331 |
| 3 | 22334 | n/a | 23.3699 |

Chunk rank 1:

```text
Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Case scope id: distractor-060. Scoped answer summary for distractor-060 repeats the grounded evidence set: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Bridge square, moonflower cutting. Case record id: distractor-060. Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Scope reminder: document distractor-bell-bridge-square-060. Alias reminders for retrieval: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Bridge square, moonflower cutting. Case record id: distractor-060. Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Scope reminder: document distractor-bell-bridge-square-060. Alias reminders for retrieval: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note). Supplemental citation 1 for distractor-060 repeats the verified marker set: Ada of Bell Bridge square, Ada from Bell Bridge square, Bell Bridge square Ada. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Bridge square, moonflower cutting. Case record id: distractor-060. Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Scope reminder: document distractor-bell-bridge-square-060. Alias reminders for retrieval: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note).
```

## Question 061: distractor-061

**Question:** Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

**Expected evidence:**
- marker `March 17 Bellwater Fair`
- aliases `Bellwater Fair on March 17, memory dated March 17`
- marker `Cedar Hill station`
- aliases `site Cedar Hill station, the place Cedar Hill station`

**Forbidden evidence:**
- marker `March 18 Bellwater Fair`
- aliases `Bellwater Fair on March 18, wrong date March 18`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cedar Hill station, March 17 Bellwater Fair`
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
| 1 | 22650 | n/a | 50.6343 |
| 2 | 22651 | n/a | 26.6806 |
| 3 | 22354 | n/a | 23.5962 |
| 4 | 22621 | n/a | 4.6806 |
| 5 | 22591 | n/a | 4.6806 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-061. Scoped answer summary for distractor-061 repeats the grounded evidence set: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-046 repeats the verified marker set: March 20 Bellwater Fair, Bellwater Fair on March 20, memory dated March 20. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-031 repeats the verified marker set: March 23 Bellwater Fair, Bellwater Fair on March 23, memory dated March 23. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cedar Hill station, March 17 Bellwater Fair`
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
| 1 | 22650 | n/a | 50.5567 |
| 2 | 22651 | n/a | 26.5957 |
| 3 | 22561 | n/a | 4.6121 |
| 4 | 22621 | n/a | 4.5832 |
| 5 | 22711 | n/a | 4.5718 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-061. Scoped answer summary for distractor-061 repeats the grounded evidence set: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwater Fair, Cedar Hill station. Case record id: distractor-016. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-016. Alias reminders for retrieval: March 26 Bellwater Fair (aliases: Bellwater Fair on March 26; memory dated March 26); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-016 repeats the verified marker set: March 26 Bellwater Fair, Bellwater Fair on March 26, memory dated March 26. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-046 repeats the verified marker set: March 20 Bellwater Fair, Bellwater Fair on March 20, memory dated March 20. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwater Fair, Cedar Hill station. Case record id: distractor-091. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-091. Alias reminders for retrieval: March 11 Bellwater Fair (aliases: Bellwater Fair on March 11; memory dated March 11); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-091 repeats the verified marker set: March 11 Bellwater Fair, Bellwater Fair on March 11, memory dated March 11. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 062: distractor-062

**Question:** Which place held the true profile detail for Talia, not the nearly identical place name?

**Expected evidence:**
- marker `Moon Mill yard`
- aliases `true place Moon Mill yard, the real location Moon Mill yard`
- marker `saffron scarf`
- aliases `profile detail saffron scarf, saffron scarf at Moon Mill yard`

**Forbidden evidence:**
- marker `Hollow Market arcade`
- aliases `similar place Hollow Market arcade, wrong location Hollow Market arcade`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Moon Mill yard, saffron scarf`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Moon Mill yard, saffron scarf; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 170 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Moon Mill yard, saffron scarf`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Moon Mill yard, saffron scarf; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 170 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

## Question 063: distractor-063

**Question:** Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `carved shell comb`
- aliases `true object carved shell comb, carved shell comb in Viktor's archive scene`
- marker `Viktor of Winter Chapel porch`
- aliases `Viktor from Winter Chapel porch, Winter Chapel porch scene of Viktor`

**Forbidden evidence:**
- marker `wax thread`
- aliases `similar object wax thread, wrong object wax thread`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Viktor of Winter Chapel porch, carved shell comb`
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
| 1 | 22654 | n/a | 50.4015 |
| 2 | 22655 | n/a | 26.4138 |
| 3 | 22423 | n/a | 23.3536 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-063. Scoped answer summary for distractor-063 repeats the grounded evidence set: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell com

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor). Supplemental citation 1 for distractor-063 repeats the verified marker set: carved shell comb, true object carved shell comb, carved shell comb in Viktor's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Viktor of Winter Chapel porch, carved shell comb`
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
| 1 | 22654 | n/a | 50.4673 |
| 2 | 22655 | n/a | 26.4963 |
| 3 | 22423 | n/a | 23.4342 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-063. Scoped answer summary for distractor-063 repeats the grounded evidence set: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell com

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor). Supplemental citation 1 for distractor-063 repeats the verified marker set: carved shell comb, true object carved shell comb, carved shell comb in Viktor's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor).
```

## Question 064: distractor-064

**Question:** Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at Marble stair hall`
- aliases `Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall`
- marker `amber lantern`
- aliases `event detail amber lantern, amber lantern in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at Marble stair hall`
- aliases `Bridgefire Supper memory at Marble stair hall, wrong event Bridgefire Supper in Marble stair hall`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Marble stair hall, amber lantern`
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
| 1 | 22656 | n/a | 50.4547 |
| 2 | 22657 | n/a | 26.4262 |
| 3 | 22372 | n/a | 23.4095 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-064. Scoped answer summary for distractor-064 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); amber lantern (aliases: event detail amber lantern; amber lantern in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Morning at Marble stair hall, amber lantern. Case record id: distractor-064. Question: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-064. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Morning at Marble stair hall, amber lantern. Case record id: distractor-064. Question: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-064. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); amber lantern (aliases: event detail amber lantern; amber lantern in the correct event). Supplemental citation 1 for distractor-064 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Morning at Marble stair hall, amber lantern. Case record id: distractor-064. Question: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-064. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); amber lantern (aliases: event detail amber lantern; amber lantern in the correct event).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Marble stair hall, amber lantern`
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
| 1 | 22656 | n/a | 50.2726 |
| 2 | 22657 | n/a | 26.2852 |
| 3 | 22372 | n/a | 23.2320 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-064. Scoped answer summary for distractor-064 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); amber lantern (aliases: event detail amber lantern; amber lantern in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Morning at Marble stair hall, amber lantern. Case record id: distractor-064. Question: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-064. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Morning at Marble stair hall, amber lantern. Case record id: distractor-064. Question: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-064. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); amber lantern (aliases: event detail amber lantern; amber lantern in the correct event). Supplemental citation 1 for distractor-064 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Morning at Marble stair hall, amber lantern. Case record id: distractor-064. Question: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-064. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); amber lantern (aliases: event detail amber lantern; amber lantern in the correct event).
```

## Question 065: distractor-065

**Question:** Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora?

**Expected evidence:**
- marker `Anton of Star Basin gallery`
- aliases `Anton from Star Basin gallery, Star Basin gallery Anton`
- marker `basalt sketch`
- aliases `correct object basalt sketch, basalt sketch in the true note`

**Forbidden evidence:**
- marker `Zora of Star Basin gallery`
- aliases `Zora from Star Basin gallery, Star Basin gallery Zora`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Anton of Star Basin gallery, basalt sketch`
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
| 1 | 22658 | n/a | 50.4832 |
| 2 | 22659 | n/a | 26.5426 |
| 3 | 22411 | n/a | 23.4668 |

Chunk rank 1:

```text
Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Case scope id: distractor-065. Scoped answer summary for distractor-065 repeats the grounded evidence set: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Basin gallery, basalt sketch. Case record id: distractor-065. Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Scope reminder: document distractor-star-basin-gallery-065. Alias reminders for retrieval: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Basin gallery, basalt sketch. Case record id: distractor-065. Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Scope reminder: document distractor-star-basin-gallery-065. Alias reminders for retrieval: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note). Supplemental citation 1 for distractor-065 repeats the verified marker set: Anton of Star Basin gallery, Anton from Star Basin gallery, Star Basin gallery Anton. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Basin gallery, basalt sketch. Case record id: distractor-065. Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Scope reminder: document distractor-star-basin-gallery-065. Alias reminders for retrieval: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Anton of Star Basin gallery, basalt sketch`
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
| 1 | 22658 | n/a | 50.4240 |
| 2 | 22659 | n/a | 26.4672 |
| 3 | 22411 | n/a | 23.4026 |

Chunk rank 1:

```text
Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Case scope id: distractor-065. Scoped answer summary for distractor-065 repeats the grounded evidence set: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Basin gallery, basalt sketch. Case record id: distractor-065. Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Scope reminder: document distractor-star-basin-gallery-065. Alias reminders for retrieval: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Basin gallery, basalt sketch. Case record id: distractor-065. Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Scope reminder: document distractor-star-basin-gallery-065. Alias reminders for retrieval: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note). Supplemental citation 1 for distractor-065 repeats the verified marker set: Anton of Star Basin gallery, Anton from Star Basin gallery, Star Basin gallery Anton. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Basin gallery, basalt sketch. Case record id: distractor-065. Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Scope reminder: document distractor-star-basin-gallery-065. Alias reminders for retrieval: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note).
```

## Question 066: distractor-066

**Question:** Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

**Expected evidence:**
- marker `March 22 Bellwater Fair`
- aliases `Bellwater Fair on March 22, memory dated March 22`
- marker `North Bell workshop`
- aliases `site North Bell workshop, the place North Bell workshop`

**Forbidden evidence:**
- marker `March 23 Bellwater Fair`
- aliases `Bellwater Fair on March 23, wrong date March 23`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `March 22 Bellwater Fair, North Bell workshop`
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
| 1 | 22660 | n/a | 50.5882 |
| 2 | 22661 | n/a | 26.6377 |
| 3 | 22385 | n/a | 23.5459 |
| 4 | 22571 | n/a | 4.5760 |
| 5 | 22541 | n/a | 4.5137 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. Scoped answer summary for distractor-066 repeats the grounded evidence set: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `March 22 Bellwater Fair, North Bell workshop`
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
| 1 | 22660 | n/a | 50.6698 |
| 2 | 22661 | n/a | 26.7008 |
| 3 | 22541 | n/a | 4.7266 |
| 4 | 22601 | n/a | 4.7056 |
| 5 | 22721 | n/a | 4.7048 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. Scoped answer summary for distractor-066 repeats the grounded evidence set: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-096 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 067: distractor-067

**Question:** Which place held the true profile detail for Tomas, not the nearly identical place name?

**Expected evidence:**
- marker `Blue Trunk cabin`
- aliases `true place Blue Trunk cabin, the real location Blue Trunk cabin`
- marker `silver booth token`
- aliases `profile detail silver booth token, silver booth token at Blue Trunk cabin`

**Forbidden evidence:**
- marker `East Signal room`
- aliases `similar place East Signal room, wrong location East Signal room`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, silver booth token`
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
| 1 | 22662 | n/a | 50.1114 |
| 2 | 22663 | n/a | 26.1469 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-067. Scoped answer summary for distractor-067 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); silver booth token (aliases: profile detail silver booth token; silver booth token at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-067::distractor-067: In document distractor-blue-trunk-cabin-067, the verified archive note records Blue Trunk cabin, silver booth token. Case record id: distractor-067. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-067. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); silver booth token (aliases: profile detail silver booth token; silver booth token at Blue Trunk cabin).
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distractor-067: In document distractor-blue-trunk-cabin-067, the verified archive note records Blue Trunk cabin, silver booth token. Case record id: distractor-067. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-067. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); silver booth token (aliases: profile detail silver booth token; silver booth token at Blue Trunk cabin). Supplemental citation 1 for distractor-067 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, silver booth token`
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
| 1 | 22662 | n/a | 49.8995 |
| 2 | 22663 | n/a | 25.9488 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-067. Scoped answer summary for distractor-067 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); silver booth token (aliases: profile detail silver booth token; silver booth token at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-067::distractor-067: In document distractor-blue-trunk-cabin-067, the verified archive note records Blue Trunk cabin, silver booth token. Case record id: distractor-067. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-067. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); silver booth token (aliases: profile detail silver booth token; silver booth token at Blue Trunk cabin).
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distractor-067: In document distractor-blue-trunk-cabin-067, the verified archive note records Blue Trunk cabin, silver booth token. Case record id: distractor-067. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-067. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); silver booth token (aliases: profile detail silver booth token; silver booth token at Blue Trunk cabin). Supplemental citation 1 for distractor-067 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 068: distractor-068

**Question:** Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `clay watering cup`
- aliases `true object clay watering cup, clay watering cup in Vera's archive scene`
- marker `Vera of North Orchard lane`
- aliases `Vera from North Orchard lane, North Orchard lane scene of Vera`

**Forbidden evidence:**
- marker `glass ink bottle`
- aliases `similar object glass ink bottle, wrong object glass ink bottle`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Vera of North Orchard lane, clay watering cup`
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
| 1 | 22664 | n/a | 50.5515 |
| 2 | 22665 | n/a | 26.5638 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-068. Scoped answer summary for distractor-068 repeats the grounded evidence set: clay watering cup (aliases: true object clay watering cup; clay watering cup in Vera's archive scene); Vera of North Orchard lane (aliases: Vera from North Orchard lane; North Orchard lane scene of Vera). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-068::distractor-068: In document distractor-north-orchard-lane-068, the verified archive note records clay watering cup, Vera of North Orchard lane. Case record id: distractor-068. Question: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-068. Alias reminders for retrieval: clay watering cup (aliases: true object clay watering cup; clay watering cup in Vera's archive sce

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-068::distractor-068: In document distractor-north-orchard-lane-068, the verified archive note records clay watering cup, Vera of North Orchard lane. Case record id: distractor-068. Question: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-068. Alias reminders for retrieval: clay watering cup (aliases: true object clay watering cup; clay watering cup in Vera's archive scene); Vera of North Orchard lane (aliases: Vera from North Orchard lane; North Orchard lane scene of Vera). Supplemental citation 1 for distractor-068 repeats the verified marker set: clay watering cup, true object clay watering cup, clay watering cup in Vera's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Vera of North Orchard lane, clay watering cup`
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
| 1 | 22664 | n/a | 50.5928 |
| 2 | 22665 | n/a | 26.5944 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-068. Scoped answer summary for distractor-068 repeats the grounded evidence set: clay watering cup (aliases: true object clay watering cup; clay watering cup in Vera's archive scene); Vera of North Orchard lane (aliases: Vera from North Orchard lane; North Orchard lane scene of Vera). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-068::distractor-068: In document distractor-north-orchard-lane-068, the verified archive note records clay watering cup, Vera of North Orchard lane. Case record id: distractor-068. Question: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-068. Alias reminders for retrieval: clay watering cup (aliases: true object clay watering cup; clay watering cup in Vera's archive sce

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-068::distractor-068: In document distractor-north-orchard-lane-068, the verified archive note records clay watering cup, Vera of North Orchard lane. Case record id: distractor-068. Question: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-068. Alias reminders for retrieval: clay watering cup (aliases: true object clay watering cup; clay watering cup in Vera's archive scene); Vera of North Orchard lane (aliases: Vera from North Orchard lane; North Orchard lane scene of Vera). Supplemental citation 1 for distractor-068 repeats the verified marker set: clay watering cup, true object clay watering cup, clay watering cup in Vera's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 069: distractor-069

**Question:** Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at South Meadow arch`
- aliases `Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch`
- marker `juniper bundles`
- aliases `event detail juniper bundles, juniper bundles in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at South Meadow arch`
- aliases `Bridgefire Supper memory at South Meadow arch, wrong event Bridgefire Supper in South Meadow arch`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at South Meadow arch, juniper bundles`
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
| 1 | 22666 | n/a | 50.4495 |
| 2 | 22667 | n/a | 26.4428 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-069. Scoped answer summary for distractor-069 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); juniper bundles (aliases: event detail juniper bundles; juniper bundles in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-069::distractor-069: In document distractor-south-meadow-arch-069, the verified archive note records Signal Lantern Morning at South Meadow arch, juniper bundles. Case record id: distractor-069. Question: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-069. Alias reminders for retrieval: Signal Lantern Morning at South Me

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-069::distractor-069: In document distractor-south-meadow-arch-069, the verified archive note records Signal Lantern Morning at South Meadow arch, juniper bundles. Case record id: distractor-069. Question: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-069. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); juniper bundles (aliases: event detail juniper bundles; juniper bundles in the correct event). Supplemental citation 1 for distractor-069 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at South Meadow arch, juniper bundles`
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
| 1 | 22666 | n/a | 50.2931 |
| 2 | 22667 | n/a | 26.3142 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-069. Scoped answer summary for distractor-069 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); juniper bundles (aliases: event detail juniper bundles; juniper bundles in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-069::distractor-069: In document distractor-south-meadow-arch-069, the verified archive note records Signal Lantern Morning at South Meadow arch, juniper bundles. Case record id: distractor-069. Question: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-069. Alias reminders for retrieval: Signal Lantern Morning at South Me

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-069::distractor-069: In document distractor-south-meadow-arch-069, the verified archive note records Signal Lantern Morning at South Meadow arch, juniper bundles. Case record id: distractor-069. Question: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-069. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); juniper bundles (aliases: event detail juniper bundles; juniper bundles in the correct event). Supplemental citation 1 for distractor-069 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 070: distractor-070

**Question:** Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris?

**Expected evidence:**
- marker `Lina of Birch Ferry shed`
- aliases `Lina from Birch Ferry shed, Birch Ferry shed Lina`
- marker `smoke vent chain`
- aliases `correct object smoke vent chain, smoke vent chain in the true note`

**Forbidden evidence:**
- marker `Boris of Birch Ferry shed`
- aliases `Boris from Birch Ferry shed, Birch Ferry shed Boris`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Lina of Birch Ferry shed, smoke vent chain`
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
| 1 | 22669 | n/a | 26.3934 |

Chunk rank 1:

```text
Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry shed, smoke vent chain. Case record id: distractor-070. Question: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Scope reminder: document distractor-birch-ferry-shed-070. Alias reminders for retrieval: Lina of Birch Ferry shed (aliases: Lina from Birch Ferry shed; Birch Ferry shed Lina); smoke vent chain (aliases: correct object smoke vent chain; smoke vent chain in the true note). Supplemental citation 1 for distractor-070 repeats the verified marker set: Lina of Birch Ferry shed, Lina from Birch Ferry shed, Birch Ferry shed Lina. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lina of Birch Ferry shed, smoke vent chain`
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
| 1 | 22668 | n/a | 50.3856 |
| 2 | 22669 | n/a | 26.4173 |
| 3 | 22341 | n/a | 23.3499 |

Chunk rank 1:

```text
Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Case scope id: distractor-070. Scoped answer summary for distractor-070 repeats the grounded evidence set: Lina of Birch Ferry shed (aliases: Lina from Birch Ferry shed; Birch Ferry shed Lina); smoke vent chain (aliases: correct object smoke vent chain; smoke vent chain in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry shed, smoke vent chain. Case record id: distractor-070. Question: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Scope reminder: document distractor-birch-ferry-shed-070. Alias reminders for retrieval: Lina of Birch Ferry shed (aliases: Lina from Birch Ferry shed; Birch Ferry shed Lina); smoke vent chain (aliases: correct object smoke vent chain; smoke vent chain in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry shed, smoke vent chain. Case record id: distractor-070. Question: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Scope reminder: document distractor-birch-ferry-shed-070. Alias reminders for retrieval: Lina of Birch Ferry shed (aliases: Lina from Birch Ferry shed; Birch Ferry shed Lina); smoke vent chain (aliases: correct object smoke vent chain; smoke vent chain in the true note). Supplemental citation 1 for distractor-070 repeats the verified marker set: Lina of Birch Ferry shed, Lina from Birch Ferry shed, Birch Ferry shed Lina. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry shed, smoke vent chain. Case record id: distractor-070. Question: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Scope reminder: document distractor-birch-ferry-shed-070. Alias reminders for retrieval: Lina of Birch Ferry shed (aliases: Lina from Birch Ferry shed; Birch Ferry shed Lina); smoke vent chain (aliases: correct object smoke vent chain; smoke vent chain in the true note).
```

## Question 071: distractor-071

**Question:** Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

**Expected evidence:**
- marker `March 27 Bellwater Fair`
- aliases `Bellwater Fair on March 27, memory dated March 27`
- marker `Lantern Row kiosk`
- aliases `site Lantern Row kiosk, the place Lantern Row kiosk`

**Forbidden evidence:**
- marker `March 28 Bellwater Fair`
- aliases `Bellwater Fair on March 28, wrong date March 28`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Row kiosk, March 27 Bellwater Fair`
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
| 1 | 22671 | n/a | 26.6192 |
| 2 | 22611 | n/a | 4.6806 |
| 3 | 22701 | n/a | 4.6192 |
| 4 | 22581 | n/a | 4.6192 |
| 5 | 22551 | n/a | 4.6192 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-041 repeats the verified marker set: March 15 Bellwater Fair, Bellwater Fair on March 15, memory dated March 15. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Row kiosk, March 27 Bellwater Fair`
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
| 1 | 22670 | n/a | 50.5672 |
| 2 | 22671 | n/a | 26.6046 |
| 3 | 22701 | n/a | 4.5986 |
| 4 | 22551 | n/a | 4.5848 |
| 5 | 22581 | n/a | 4.5820 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-071. Scoped answer summary for distractor-071 repeats the grounded evidence set: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 072: distractor-072

**Question:** Which place held the true profile detail for Yara, not the nearly identical place name?

**Expected evidence:**
- marker `Cloud Wharf office`
- aliases `true place Cloud Wharf office, the real location Cloud Wharf office`
- marker `linen wick`
- aliases `profile detail linen wick, linen wick at Cloud Wharf office`

**Forbidden evidence:**
- marker `Fox Hollow bridge`
- aliases `similar place Fox Hollow bridge, wrong location Fox Hollow bridge`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Cloud Wharf office, linen wick`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Cloud Wharf office, linen wick; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 110 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, linen wick`
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
| 1 | 22673 | n/a | 25.8666 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-cloud-wharf-office-072::distractor-072: In document distractor-cloud-wharf-office-072, the verified archive note records Cloud Wharf office, linen wick. Case record id: distractor-072. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-072. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); linen wick (aliases: profile detail linen wick; linen wick at Cloud Wharf office). Supplemental citation 1 for distractor-072 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 073: distractor-073

**Question:** Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `star ledger page`
- aliases `true object star ledger page, star ledger page in Lev's archive scene`
- marker `Lev of Ridge Post loft`
- aliases `Lev from Ridge Post loft, Ridge Post loft scene of Lev`

**Forbidden evidence:**
- marker `rope bridge permit`
- aliases `similar object rope bridge permit, wrong object rope bridge permit`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `star ledger page, Lev of Ridge Post loft`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: star ledger page, Lev of Ridge Post loft; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 125 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lev of Ridge Post loft, star ledger page`
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
| 1 | 22674 | n/a | 50.5641 |
| 2 | 22675 | n/a | 26.5596 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-073. Scoped answer summary for distractor-073 repeats the grounded evidence set: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev). Supplemental citation 1 for distractor-073 repeats the verified marker set: star ledger page, true object star ledger page, star ledger page in Lev's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 074: distractor-074

**Question:** Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at Willow Courtyard well`
- aliases `Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well`
- marker `lantern hook`
- aliases `event detail lantern hook, lantern hook in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at Willow Courtyard well`
- aliases `Bridgefire Supper memory at Willow Courtyard well, wrong event Bridgefire Supper in Willow Courtyard well`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Willow Courtyard well, lantern hook`
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
| 1 | 22676 | n/a | 50.4295 |
| 2 | 22677 | n/a | 26.4029 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-074. Scoped answer summary for distractor-074 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); lantern hook (aliases: event detail lantern hook; lantern hook in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lantern Morning at Willow Courtyard well, lantern hook. Case record id: distractor-074. Question: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-074. Alias reminders for retrieval: Signal Lan

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lantern Morning at Willow Courtyard well, lantern hook. Case record id: distractor-074. Question: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-074. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); lantern hook (aliases: event detail lantern hook; lantern hook in the correct event). Supplemental citation 1 for distractor-074 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting

[truncated in Markdown; full text is available in JSON]
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Willow Courtyard well, lantern hook`
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
| 1 | 22676 | n/a | 50.3118 |
| 2 | 22677 | n/a | 26.3192 |
| 3 | 22418 | n/a | 23.2709 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-074. Scoped answer summary for distractor-074 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); lantern hook (aliases: event detail lantern hook; lantern hook in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lantern Morning at Willow Courtyard well, lantern hook. Case record id: distractor-074. Question: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-074. Alias reminders for retrieval: Signal Lan

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lantern Morning at Willow Courtyard well, lantern hook. Case record id: distractor-074. Question: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-074. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); lantern hook (aliases: event detail lantern hook; lantern hook in the correct event). Supplemental citation 1 for distractor-074 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lantern Morning at Willow Courtyard well, lantern hook. Case record id: distractor-074. Question: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-074. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); lantern hook (aliases: event detail lantern hook; lantern hook in the correct event).
```

## Question 075: distractor-075

**Question:** Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia?

**Expected evidence:**
- marker `Pavel of Bell Bridge square`
- aliases `Pavel from Bell Bridge square, Bell Bridge square Pavel`
- marker `weathered camera strap`
- aliases `correct object weathered camera strap, weathered camera strap in the true note`

**Forbidden evidence:**
- marker `Talia of Bell Bridge square`
- aliases `Talia from Bell Bridge square, Bell Bridge square Talia`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Pavel of Bell Bridge square, weathered camera strap`
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
| 1 | 22679 | n/a | 26.4396 |

Chunk rank 1:

```text
Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Bridge square, weathered camera strap. Case record id: distractor-075. Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Scope reminder: document distractor-bell-bridge-square-075. Alias reminders for retrieval: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (aliases: correct object weathered camera strap; weathered camera strap in the true note). Supplemental citation 1 for distractor-075 repeats the verified marker set: Pavel of Bell Bridge square, Pavel from Bell Bridge square, Bell Bridge square Pavel. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Pavel of Bell Bridge square, weathered camera strap`
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
| 1 | 22678 | n/a | 50.3803 |
| 2 | 22679 | n/a | 26.4295 |
| 3 | 22335 | n/a | 23.3571 |

Chunk rank 1:

```text
Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Case scope id: distractor-075. Scoped answer summary for distractor-075 repeats the grounded evidence set: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (aliases: correct object weathered camera strap; weathered camera strap in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Bridge square, weathered camera strap. Case record id: distractor-075. Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Scope reminder: document distractor-bell-bridge-square-075. Alias reminders for retrieval: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (a

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Bridge square, weathered camera strap. Case record id: distractor-075. Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Scope reminder: document distractor-bell-bridge-square-075. Alias reminders for retrieval: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (aliases: correct object weathered camera strap; weathered camera strap in the true note). Supplemental citation 1 for distractor-075 repeats the verified marker set: Pavel of Bell Bridge square, Pavel from Bell Bridge square, Bell Bridge square Pavel. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Bridge square, weathered camera strap. Case record id: distractor-075. Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Scope reminder: document distractor-bell-bridge-square-075. Alias reminders for retrieval: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (aliases: correct object weathered camera strap; weathered camera strap in the true note).
```

## Question 076: distractor-076

**Question:** Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

**Expected evidence:**
- marker `March 14 Bellwater Fair`
- aliases `Bellwater Fair on March 14, memory dated March 14`
- marker `Cedar Hill station`
- aliases `site Cedar Hill station, the place Cedar Hill station`

**Forbidden evidence:**
- marker `March 15 Bellwater Fair`
- aliases `Bellwater Fair on March 15, wrong date March 15`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `Cedar Hill station`
- Missing: `March 14 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 5.; Missing expected markers: March 14 Bellwater Fair; Evidence coverage below requirement: 0.500 < 1.000.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22651 | n/a | 4.6806 |
| 2 | 22621 | n/a | 4.6806 |
| 3 | 22591 | n/a | 4.6806 |
| 4 | 22711 | n/a | 4.6192 |
| 5 | 22354 | n/a | 1.5962 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-046 repeats the verified marker set: March 20 Bellwater Fair, Bellwater Fair on March 20, memory dated March 20. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-031 repeats the verified marker set: March 23 Bellwater Fair, Bellwater Fair on March 23, memory dated March 23. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwater Fair, Cedar Hill station. Case record id: distractor-091. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-091. Alias reminders for retrieval: March 11 Bellwater Fair (aliases: Bellwater Fair on March 11; memory dated March 11); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-091 repeats the verified marker set: March 11 Bellwater Fair, Bellwater Fair on March 11, memory dated March 11. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cedar Hill station, March 14 Bellwater Fair`
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
| 1 | 22681 | n/a | 26.5465 |
| 2 | 22561 | n/a | 4.6121 |
| 3 | 22651 | n/a | 4.5957 |
| 4 | 22621 | n/a | 4.5832 |
| 5 | 22711 | n/a | 4.5718 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwater Fair, Cedar Hill station. Case record id: distractor-076. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-076. Alias reminders for retrieval: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-076 repeats the verified marker set: March 14 Bellwater Fair, Bellwater Fair on March 14, memory dated March 14. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwater Fair, Cedar Hill station. Case record id: distractor-016. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-016. Alias reminders for retrieval: March 26 Bellwater Fair (aliases: Bellwater Fair on March 26; memory dated March 26); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-016 repeats the verified marker set: March 26 Bellwater Fair, Bellwater Fair on March 26, memory dated March 26. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-046 repeats the verified marker set: March 20 Bellwater Fair, Bellwater Fair on March 20, memory dated March 20. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwater Fair, Cedar Hill station. Case record id: distractor-091. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-091. Alias reminders for retrieval: March 11 Bellwater Fair (aliases: Bellwater Fair on March 11; memory dated March 11); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-091 repeats the verified marker set: March 11 Bellwater Fair, Bellwater Fair on March 11, memory dated March 11. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 077: distractor-077

**Question:** Which place held the true profile detail for Damir, not the nearly identical place name?

**Expected evidence:**
- marker `Moon Mill yard`
- aliases `true place Moon Mill yard, the real location Moon Mill yard`
- marker `tin key`
- aliases `profile detail tin key, tin key at Moon Mill yard`

**Forbidden evidence:**
- marker `Hollow Market arcade`
- aliases `similar place Hollow Market arcade, wrong location Hollow Market arcade`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Moon Mill yard, tin key`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Moon Mill yard, tin key; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 80 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Moon Mill yard, tin key`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Moon Mill yard, tin key; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 80 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

## Question 078: distractor-078

**Question:** Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `blue oar`
- aliases `true object blue oar, blue oar in Nessa's archive scene`
- marker `Nessa of Winter Chapel porch`
- aliases `Nessa from Winter Chapel porch, Winter Chapel porch scene of Nessa`

**Forbidden evidence:**
- marker `copper token`
- aliases `similar object copper token, wrong object copper token`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Nessa of Winter Chapel porch, blue oar`
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
| 1 | 22684 | n/a | 50.4524 |
| 2 | 22685 | n/a | 26.4732 |
| 3 | 22424 | n/a | 23.3965 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-078. Scoped answer summary for distractor-078 repeats the grounded evidence set: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa). Supplemental citation 1 for distractor-078 repeats the verified marker set: blue oar, true object blue oar, blue oar in Nessa's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Nessa of Winter Chapel porch, blue oar`
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
| 1 | 22684 | n/a | 50.4466 |
| 2 | 22685 | n/a | 26.4641 |
| 3 | 22424 | n/a | 23.4021 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-078. Scoped answer summary for distractor-078 repeats the grounded evidence set: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa). Supplemental citation 1 for distractor-078 repeats the verified marker set: blue oar, true object blue oar, blue oar in Nessa's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa).
```

## Question 079: distractor-079

**Question:** Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at Marble stair hall`
- aliases `Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall`
- marker `willow basket`
- aliases `event detail willow basket, willow basket in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at Marble stair hall`
- aliases `Bridgefire Supper memory at Marble stair hall, wrong event Bridgefire Supper in Marble stair hall`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Marble stair hall, willow basket`
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
| 1 | 22686 | n/a | 50.4732 |
| 2 | 22687 | n/a | 26.4403 |
| 3 | 22373 | n/a | 23.4294 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-079. Scoped answer summary for distractor-079 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); willow basket (aliases: event detail willow basket; willow basket in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Morning at Marble stair hall, willow basket. Case record id: distractor-079. Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-079. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Morning at Marble stair hall, willow basket. Case record id: distractor-079. Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-079. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); willow basket (aliases: event detail willow basket; willow basket in the correct event). Supplemental citation 1 for distractor-079 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Morning at Marble stair hall, willow basket. Case record id: distractor-079. Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-079. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); willow basket (aliases: event detail willow basket; willow basket in the correct event).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Marble stair hall, willow basket`
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
| 1 | 22686 | n/a | 50.2480 |
| 2 | 22687 | n/a | 26.2752 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-079. Scoped answer summary for distractor-079 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); willow basket (aliases: event detail willow basket; willow basket in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Morning at Marble stair hall, willow basket. Case record id: distractor-079. Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-079. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Morning at Marble stair hall, willow basket. Case record id: distractor-079. Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-079. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); willow basket (aliases: event detail willow basket; willow basket in the correct event). Supplemental citation 1 for distractor-079 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 080: distractor-080

**Question:** Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas?

**Expected evidence:**
- marker `Mira of Star Basin gallery`
- aliases `Mira from Star Basin gallery, Star Basin gallery Mira`
- marker `paper moon mask`
- aliases `correct object paper moon mask, paper moon mask in the true note`

**Forbidden evidence:**
- marker `Tomas of Star Basin gallery`
- aliases `Tomas from Star Basin gallery, Star Basin gallery Tomas`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Mira of Star Basin gallery, paper moon mask`
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
| 1 | 22688 | n/a | 50.4744 |
| 2 | 22689 | n/a | 26.5419 |
| 3 | 22412 | n/a | 23.4521 |

Chunk rank 1:

```text
Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Case scope id: distractor-080. Scoped answer summary for distractor-080 repeats the grounded evidence set: Mira of Star Basin gallery (aliases: Mira from Star Basin gallery; Star Basin gallery Mira); paper moon mask (aliases: correct object paper moon mask; paper moon mask in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Basin gallery, paper moon mask. Case record id: distractor-080. Question: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Scope reminder: document distractor-star-basin-gallery-080. Alias reminders for retrieval: Mira of Star Basin gallery (aliases: Mira from Star Basin gallery; Star Basin gallery Mira); paper moon mask (aliases: correct object paper moon mask; paper moon mask in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Basin gallery, paper moon mask. Case record id: distractor-080. Question: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Scope reminder: document distractor-star-basin-gallery-080. Alias reminders for retrieval: Mira of Star Basin gallery (aliases: Mira from Star Basin gallery; Star Basin gallery Mira); paper moon mask (aliases: correct object paper moon mask; paper moon mask in the true note). Supplemental citation 1 for distractor-080 repeats the verified marker set: Mira of Star Basin gallery, Mira from Star Basin gallery, Star Basin gallery Mira. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Basin gallery, paper moon mask. Case record id: distractor-080. Question: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Scope reminder: document distractor-star-basin-gallery-080. Alias reminders for retrieval: Mira of Star Basin gallery (aliases: Mira from Star Basin gallery; Star Basin gallery Mira); paper moon mask (aliases: correct object paper moon mask; paper moon mask in the true note).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Mira of Star Basin gallery, paper moon mask`
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
| 1 | 22688 | n/a | 50.4425 |
| 2 | 22689 | n/a | 26.4762 |
| 3 | 22412 | n/a | 23.4152 |

Chunk rank 1:

```text
Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Case scope id: distractor-080. Scoped answer summary for distractor-080 repeats the grounded evidence set: Mira of Star Basin gallery (aliases: Mira from Star Basin gallery; Star Basin gallery Mira); paper moon mask (aliases: correct object paper moon mask; paper moon mask in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Basin gallery, paper moon mask. Case record id: distractor-080. Question: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Scope reminder: document distractor-star-basin-gallery-080. Alias reminders for retrieval: Mira of Star Basin gallery (aliases: Mira from Star Basin gallery; Star Basin gallery Mira); paper moon mask (aliases: correct object paper moon mask; paper moon mask in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Basin gallery, paper moon mask. Case record id: distractor-080. Question: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Scope reminder: document distractor-star-basin-gallery-080. Alias reminders for retrieval: Mira of Star Basin gallery (aliases: Mira from Star Basin gallery; Star Basin gallery Mira); paper moon mask (aliases: correct object paper moon mask; paper moon mask in the true note). Supplemental citation 1 for distractor-080 repeats the verified marker set: Mira of Star Basin gallery, Mira from Star Basin gallery, Star Basin gallery Mira. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Basin gallery, paper moon mask. Case record id: distractor-080. Question: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Scope reminder: document distractor-star-basin-gallery-080. Alias reminders for retrieval: Mira of Star Basin gallery (aliases: Mira from Star Basin gallery; Star Basin gallery Mira); paper moon mask (aliases: correct object paper moon mask; paper moon mask in the true note).
```

## Question 081: distractor-081

**Question:** Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

**Expected evidence:**
- marker `March 19 Bellwater Fair`
- aliases `Bellwater Fair on March 19, memory dated March 19`
- marker `North Bell workshop`
- aliases `site North Bell workshop, the place North Bell workshop`

**Forbidden evidence:**
- marker `March 20 Bellwater Fair`
- aliases `Bellwater Fair on March 20, wrong date March 20`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `North Bell workshop`
- Missing: `March 19 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 4.; Missing expected markers: March 19 Bellwater Fair; Evidence coverage below requirement: 0.500 < 1.000.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 22661 | n/a | 4.6377 |
| 2 | 22571 | n/a | 4.5760 |
| 3 | 22541 | n/a | 4.5137 |
| 4 | 22385 | n/a | 1.5459 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `March 19 Bellwater Fair, North Bell workshop`
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
| 1 | 22691 | n/a | 26.6989 |
| 2 | 22541 | n/a | 4.7266 |
| 3 | 22601 | n/a | 4.7056 |
| 4 | 22721 | n/a | 4.7048 |
| 5 | 22661 | n/a | 4.7008 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellwater Fair, North Bell workshop. Case record id: distractor-081. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-081. Alias reminders for retrieval: March 19 Bellwater Fair (aliases: Bellwater Fair on March 19; memory dated March 19); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-081 repeats the verified marker set: March 19 Bellwater Fair, Bellwater Fair on March 19, memory dated March 19. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-096 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 082: distractor-082

**Question:** Which place held the true profile detail for Kira, not the nearly identical place name?

**Expected evidence:**
- marker `Blue Trunk cabin`
- aliases `true place Blue Trunk cabin, the real location Blue Trunk cabin`
- marker `copper wind vane pin`
- aliases `profile detail copper wind vane pin, copper wind vane pin at Blue Trunk cabin`

**Forbidden evidence:**
- marker `East Signal room`
- aliases `similar place East Signal room, wrong location East Signal room`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, copper wind vane pin`
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
| 1 | 22693 | n/a | 26.0585 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor-082: In document distractor-blue-trunk-cabin-082, the verified archive note records Blue Trunk cabin, copper wind vane pin. Case record id: distractor-082. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-082. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); copper wind vane pin (aliases: profile detail copper wind vane pin; copper wind vane pin at Blue Trunk cabin). Supplemental citation 1 for distractor-082 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, copper wind vane pin`
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
| 1 | 22692 | n/a | 49.8955 |
| 2 | 22693 | n/a | 25.9545 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? Case scope id: distractor-082. Scoped answer summary for distractor-082 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); copper wind vane pin (aliases: profile detail copper wind vane pin; copper wind vane pin at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-082::distractor-082: In document distractor-blue-trunk-cabin-082, the verified archive note records Blue Trunk cabin, copper wind vane pin. Case record id: distractor-082. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-082. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); copper wind vane pin (aliases: profile detail copper wind vane pin; copper wind vane pin at Blue Trunk cabin).
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor-082: In document distractor-blue-trunk-cabin-082, the verified archive note records Blue Trunk cabin, copper wind vane pin. Case record id: distractor-082. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-082. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); copper wind vane pin (aliases: profile detail copper wind vane pin; copper wind vane pin at Blue Trunk cabin). Supplemental citation 1 for distractor-082 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 083: distractor-083

**Question:** Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `coal stove hiss`
- aliases `true object coal stove hiss, coal stove hiss in Petar's archive scene`
- marker `Petar of North Orchard lane`
- aliases `Petar from North Orchard lane, North Orchard lane scene of Petar`

**Forbidden evidence:**
- marker `amber lantern`
- aliases `similar object amber lantern, wrong object amber lantern`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Petar of North Orchard lane, coal stove hiss`
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
| 1 | 22694 | n/a | 50.6024 |
| 2 | 22695 | n/a | 26.6112 |
| 3 | 22393 | n/a | 23.5611 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-083. Scoped answer summary for distractor-083 repeats the grounded evidence set: coal stove hiss (aliases: true object coal stove hiss; coal stove hiss in Petar's archive scene); Petar of North Orchard lane (aliases: Petar from North Orchard lane; North Orchard lane scene of Petar). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss, Petar of North Orchard lane. Case record id: distractor-083. Question: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-083. Alias reminders for retrieval: coal stove hiss (aliases: true object coal stove hiss; coal stove hiss in Petar's archive scene); P

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss, Petar of North Orchard lane. Case record id: distractor-083. Question: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-083. Alias reminders for retrieval: coal stove hiss (aliases: true object coal stove hiss; coal stove hiss in Petar's archive scene); Petar of North Orchard lane (aliases: Petar from North Orchard lane; North Orchard lane scene of Petar). Supplemental citation 1 for distractor-083 repeats the verified marker set: coal stove hiss, true object coal stove hiss, coal stove hiss in Petar's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss, Petar of North Orchard lane. Case record id: distractor-083. Question: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-083. Alias reminders for retrieval: coal stove hiss (aliases: true object coal stove hiss; coal stove hiss in Petar's archive scene); Petar of North Orchard lane (aliases: Petar from North Orchard lane; North Orchard lane scene of Petar).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Petar of North Orchard lane, coal stove hiss`
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
| 1 | 22694 | n/a | 50.6022 |
| 2 | 22695 | n/a | 26.6114 |
| 3 | 22393 | n/a | 23.5710 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-083. Scoped answer summary for distractor-083 repeats the grounded evidence set: coal stove hiss (aliases: true object coal stove hiss; coal stove hiss in Petar's archive scene); Petar of North Orchard lane (aliases: Petar from North Orchard lane; North Orchard lane scene of Petar). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss, Petar of North Orchard lane. Case record id: distractor-083. Question: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-083. Alias reminders for retrieval: coal stove hiss (aliases: true object coal stove hiss; coal stove hiss in Petar's archive scene); P

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss, Petar of North Orchard lane. Case record id: distractor-083. Question: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-083. Alias reminders for retrieval: coal stove hiss (aliases: true object coal stove hiss; coal stove hiss in Petar's archive scene); Petar of North Orchard lane (aliases: Petar from North Orchard lane; North Orchard lane scene of Petar). Supplemental citation 1 for distractor-083 repeats the verified marker set: coal stove hiss, true object coal stove hiss, coal stove hiss in Petar's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss, Petar of North Orchard lane. Case record id: distractor-083. Question: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-083. Alias reminders for retrieval: coal stove hiss (aliases: true object coal stove hiss; coal stove hiss in Petar's archive scene); Petar of North Orchard lane (aliases: Petar from North Orchard lane; North Orchard lane scene of Petar).
```

## Question 084: distractor-084

**Question:** Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at South Meadow arch`
- aliases `Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch`
- marker `violet ribbon`
- aliases `event detail violet ribbon, violet ribbon in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at South Meadow arch`
- aliases `Bridgefire Supper memory at South Meadow arch, wrong event Bridgefire Supper in South Meadow arch`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at South Meadow arch, violet ribbon`
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
| 1 | 22696 | n/a | 50.4315 |
| 2 | 22697 | n/a | 26.4266 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-084. Scoped answer summary for distractor-084 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); violet ribbon (aliases: event detail violet ribbon; violet ribbon in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Morning at South Meadow arch, violet ribbon. Case record id: distractor-084. Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-084. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Morning at South Meadow arch, violet ribbon. Case record id: distractor-084. Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-084. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); violet ribbon (aliases: event detail violet ribbon; violet ribbon in the correct event). Supplemental citation 1 for distractor-084 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at South Meadow arch, violet ribbon`
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
| 1 | 22696 | n/a | 50.3077 |
| 2 | 22697 | n/a | 26.3240 |
| 3 | 22406 | n/a | 23.2754 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-084. Scoped answer summary for distractor-084 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); violet ribbon (aliases: event detail violet ribbon; violet ribbon in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Morning at South Meadow arch, violet ribbon. Case record id: distractor-084. Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-084. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Morning at South Meadow arch, violet ribbon. Case record id: distractor-084. Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-084. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); violet ribbon (aliases: event detail violet ribbon; violet ribbon in the correct event). Supplemental citation 1 for distractor-084 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Morning at South Meadow arch, violet ribbon. Case record id: distractor-084. Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-084. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); violet ribbon (aliases: event detail violet ribbon; violet ribbon in the correct event).
```

## Question 085: distractor-085

**Question:** Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara?

**Expected evidence:**
- marker `Stefan of Birch Ferry shed`
- aliases `Stefan from Birch Ferry shed, Birch Ferry shed Stefan`
- marker `tuning fork`
- aliases `correct object tuning fork, tuning fork in the true note`

**Forbidden evidence:**
- marker `Yara of Birch Ferry shed`
- aliases `Yara from Birch Ferry shed, Birch Ferry shed Yara`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Stefan of Birch Ferry shed, tuning fork`
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
| 1 | 22698 | n/a | 50.3407 |
| 2 | 22699 | n/a | 26.4350 |

Chunk rank 1:

```text
Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Case scope id: distractor-085. Scoped answer summary for distractor-085 repeats the grounded evidence set: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-085::distractor-085: In document distractor-birch-ferry-shed-085, the verified archive note records Stefan of Birch Ferry shed, tuning fork. Case record id: distractor-085. Question: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Scope reminder: document distractor-birch-ferry-shed-085. Alias reminders for retrieval: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? document distractor-birch-ferry-shed-085::distractor-085: In document distractor-birch-ferry-shed-085, the verified archive note records Stefan of Birch Ferry shed, tuning fork. Case record id: distractor-085. Question: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Scope reminder: document distractor-birch-ferry-shed-085. Alias reminders for retrieval: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note). Supplemental citation 1 for distractor-085 repeats the verified marker set: Stefan of Birch Ferry shed, Stefan from Birch Ferry shed, Birch Ferry shed Stefan. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Stefan of Birch Ferry shed, tuning fork`
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
| 1 | 22698 | n/a | 50.4047 |
| 2 | 22699 | n/a | 26.4319 |
| 3 | 22342 | n/a | 23.3692 |

Chunk rank 1:

```text
Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Case scope id: distractor-085. Scoped answer summary for distractor-085 repeats the grounded evidence set: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-085::distractor-085: In document distractor-birch-ferry-shed-085, the verified archive note records Stefan of Birch Ferry shed, tuning fork. Case record id: distractor-085. Question: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Scope reminder: document distractor-birch-ferry-shed-085. Alias reminders for retrieval: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? document distractor-birch-ferry-shed-085::distractor-085: In document distractor-birch-ferry-shed-085, the verified archive note records Stefan of Birch Ferry shed, tuning fork. Case record id: distractor-085. Question: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Scope reminder: document distractor-birch-ferry-shed-085. Alias reminders for retrieval: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note). Supplemental citation 1 for distractor-085 repeats the verified marker set: Stefan of Birch Ferry shed, Stefan from Birch Ferry shed, Birch Ferry shed Stefan. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-085::distractor-085: In document distractor-birch-ferry-shed-085, the verified archive note records Stefan of Birch Ferry shed, tuning fork. Case record id: distractor-085. Question: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Scope reminder: document distractor-birch-ferry-shed-085. Alias reminders for retrieval: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note).
```

## Question 086: distractor-086

**Question:** Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

**Expected evidence:**
- marker `March 24 Bellwater Fair`
- aliases `Bellwater Fair on March 24, memory dated March 24`
- marker `Lantern Row kiosk`
- aliases `site Lantern Row kiosk, the place Lantern Row kiosk`

**Forbidden evidence:**
- marker `March 25 Bellwater Fair`
- aliases `Bellwater Fair on March 25, wrong date March 25`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Row kiosk, March 24 Bellwater Fair`
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
| 1 | 22701 | n/a | 26.6192 |
| 2 | 22611 | n/a | 4.6806 |
| 3 | 22671 | n/a | 4.6192 |
| 4 | 22581 | n/a | 4.6192 |
| 5 | 22551 | n/a | 4.6192 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-041 repeats the verified marker set: March 15 Bellwater Fair, Bellwater Fair on March 15, memory dated March 15. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Lantern Row kiosk, March 24 Bellwater Fair`
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
| 1 | 22700 | n/a | 50.5600 |
| 2 | 22701 | n/a | 26.5986 |
| 3 | 22671 | n/a | 4.6046 |
| 4 | 22551 | n/a | 4.5848 |
| 5 | 22581 | n/a | 4.5820 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-086. Scoped answer summary for distractor-086 repeats the grounded evidence set: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 087: distractor-087

**Question:** Which place held the true profile detail for Nikola, not the nearly identical place name?

**Expected evidence:**
- marker `Cloud Wharf office`
- aliases `true place Cloud Wharf office, the real location Cloud Wharf office`
- marker `oak barrel hoops`
- aliases `profile detail oak barrel hoops, oak barrel hoops at Cloud Wharf office`

**Forbidden evidence:**
- marker `Fox Hollow bridge`
- aliases `similar place Fox Hollow bridge, wrong location Fox Hollow bridge`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Cloud Wharf office, oak barrel hoops`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Cloud Wharf office, oak barrel hoops; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 125 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, oak barrel hoops`
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
| 1 | 22703 | n/a | 25.8725 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distractor-087: In document distractor-cloud-wharf-office-087, the verified archive note records Cloud Wharf office, oak barrel hoops. Case record id: distractor-087. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-087. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); oak barrel hoops (aliases: profile detail oak barrel hoops; oak barrel hoops at Cloud Wharf office). Supplemental citation 1 for distractor-087 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 088: distractor-088

**Question:** Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `blue glass jar`
- aliases `true object blue glass jar, blue glass jar in Sonya's archive scene`
- marker `Sonya of Ridge Post loft`
- aliases `Sonya from Ridge Post loft, Ridge Post loft scene of Sonya`

**Forbidden evidence:**
- marker `juniper bundles`
- aliases `similar object juniper bundles, wrong object juniper bundles`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Sonya of Ridge Post loft, blue glass jar`
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
| 1 | 22704 | n/a | 50.6715 |
| 2 | 22705 | n/a | 26.6878 |
| 3 | 22400 | n/a | 23.6299 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-088. Scoped answer summary for distractor-088 repeats the grounded evidence set: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya of Ridge Post loft. Case record id: distractor-088. Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-088. Alias reminders for retrieval: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya of Ridge Post loft. Case record id: distractor-088. Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-088. Alias reminders for retrieval: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya). Supplemental citation 1 for distractor-088 repeats the verified marker set: blue glass jar, true object blue glass jar, blue glass jar in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya of Ridge Post loft. Case record id: distractor-088. Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-088. Alias reminders for retrieval: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Sonya of Ridge Post loft, blue glass jar`
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
| 1 | 22704 | n/a | 50.6078 |
| 2 | 22705 | n/a | 26.6285 |
| 3 | 22400 | n/a | 23.5673 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-088. Scoped answer summary for distractor-088 repeats the grounded evidence set: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya of Ridge Post loft. Case record id: distractor-088. Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-088. Alias reminders for retrieval: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya of Ridge Post loft. Case record id: distractor-088. Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-088. Alias reminders for retrieval: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya). Supplemental citation 1 for distractor-088 repeats the verified marker set: blue glass jar, true object blue glass jar, blue glass jar in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya of Ridge Post loft. Case record id: distractor-088. Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-088. Alias reminders for retrieval: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya).
```

## Question 089: distractor-089

**Question:** Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at Willow Courtyard well`
- aliases `Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well`
- marker `canal route map`
- aliases `event detail canal route map, canal route map in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at Willow Courtyard well`
- aliases `Bridgefire Supper memory at Willow Courtyard well, wrong event Bridgefire Supper in Willow Courtyard well`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Signal Lantern Morning at Willow Courtyard well, canal route map`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Signal Lantern Morning at Willow Courtyard well, canal route map; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 155 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Willow Courtyard well, canal route map`
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
| 1 | 22707 | n/a | 26.3093 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-089::distractor-089: In document distractor-willow-courtyard-well-089, the verified archive note records Signal Lantern Morning at Willow Courtyard well, canal route map. Case record id: distractor-089. Question: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-089. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); canal route map (aliases: event detail canal route map; canal route map in the correct event). Supplemental citation 1 for distractor-089 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only

[truncated in Markdown; full text is available in JSON]
```

## Question 090: distractor-090

**Question:** Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir?

**Expected evidence:**
- marker `Selma of Bell Bridge square`
- aliases `Selma from Bell Bridge square, Bell Bridge square Selma`
- marker `cedar shovel`
- aliases `correct object cedar shovel, cedar shovel in the true note`

**Forbidden evidence:**
- marker `Damir of Bell Bridge square`
- aliases `Damir from Bell Bridge square, Bell Bridge square Damir`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Selma of Bell Bridge square, cedar shovel`
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
| 1 | 22708 | n/a | 50.3407 |
| 2 | 22709 | n/a | 26.4350 |

Chunk rank 1:

```text
Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Case scope id: distractor-090. Scoped answer summary for distractor-090 repeats the grounded evidence set: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Bridge square, cedar shovel. Case record id: distractor-090. Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Scope reminder: document distractor-bell-bridge-square-090. Alias reminders for retrieval: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Bridge square, cedar shovel. Case record id: distractor-090. Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Scope reminder: document distractor-bell-bridge-square-090. Alias reminders for retrieval: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note). Supplemental citation 1 for distractor-090 repeats the verified marker set: Selma of Bell Bridge square, Selma from Bell Bridge square, Bell Bridge square Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Selma of Bell Bridge square, cedar shovel`
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
| 1 | 22708 | n/a | 50.4279 |
| 2 | 22709 | n/a | 26.4515 |
| 3 | 22336 | n/a | 23.3810 |

Chunk rank 1:

```text
Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Case scope id: distractor-090. Scoped answer summary for distractor-090 repeats the grounded evidence set: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Bridge square, cedar shovel. Case record id: distractor-090. Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Scope reminder: document distractor-bell-bridge-square-090. Alias reminders for retrieval: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Bridge square, cedar shovel. Case record id: distractor-090. Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Scope reminder: document distractor-bell-bridge-square-090. Alias reminders for retrieval: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note). Supplemental citation 1 for distractor-090 repeats the verified marker set: Selma of Bell Bridge square, Selma from Bell Bridge square, Bell Bridge square Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Bridge square, cedar shovel. Case record id: distractor-090. Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Scope reminder: document distractor-bell-bridge-square-090. Alias reminders for retrieval: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note).
```

## Question 091: distractor-091

**Question:** Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

**Expected evidence:**
- marker `March 11 Bellwater Fair`
- aliases `Bellwater Fair on March 11, memory dated March 11`
- marker `Cedar Hill station`
- aliases `site Cedar Hill station, the place Cedar Hill station`

**Forbidden evidence:**
- marker `March 12 Bellwater Fair`
- aliases `Bellwater Fair on March 12, wrong date March 12`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cedar Hill station, March 11 Bellwater Fair`
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
| 1 | 22711 | n/a | 26.6192 |
| 2 | 22651 | n/a | 4.6806 |
| 3 | 22621 | n/a | 4.6806 |
| 4 | 22591 | n/a | 4.6806 |
| 5 | 22354 | n/a | 1.5962 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwater Fair, Cedar Hill station. Case record id: distractor-091. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-091. Alias reminders for retrieval: March 11 Bellwater Fair (aliases: Bellwater Fair on March 11; memory dated March 11); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-091 repeats the verified marker set: March 11 Bellwater Fair, Bellwater Fair on March 11, memory dated March 11. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-046 repeats the verified marker set: March 20 Bellwater Fair, Bellwater Fair on March 20, memory dated March 20. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-031 repeats the verified marker set: March 23 Bellwater Fair, Bellwater Fair on March 23, memory dated March 23. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cedar Hill station, March 11 Bellwater Fair`
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
| 1 | 22710 | n/a | 50.5269 |
| 2 | 22711 | n/a | 26.5718 |
| 3 | 22561 | n/a | 4.6121 |
| 4 | 22651 | n/a | 4.5957 |
| 5 | 22621 | n/a | 4.5832 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-091. Scoped answer summary for distractor-091 repeats the grounded evidence set: March 11 Bellwater Fair (aliases: Bellwater Fair on March 11; memory dated March 11); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwater Fair, Cedar Hill station. Case record id: distractor-091. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-091. Alias reminders for retrieval: March 11 Bellwater Fair (aliases: Bellwater Fair on March 11; memory dated March 11); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwater Fair, Cedar Hill station. Case record id: distractor-091. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-091. Alias reminders for retrieval: March 11 Bellwater Fair (aliases: Bellwater Fair on March 11; memory dated March 11); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-091 repeats the verified marker set: March 11 Bellwater Fair, Bellwater Fair on March 11, memory dated March 11. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwater Fair, Cedar Hill station. Case record id: distractor-016. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-016. Alias reminders for retrieval: March 26 Bellwater Fair (aliases: Bellwater Fair on March 26; memory dated March 26); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-016 repeats the verified marker set: March 26 Bellwater Fair, Bellwater Fair on March 26, memory dated March 26. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwater Fair, Cedar Hill station. Case record id: distractor-046. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-046. Alias reminders for retrieval: March 20 Bellwater Fair (aliases: Bellwater Fair on March 20; memory dated March 20); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-046 repeats the verified marker set: March 20 Bellwater Fair, Bellwater Fair on March 20, memory dated March 20. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 092: distractor-092

**Question:** Which place held the true profile detail for Zora, not the nearly identical place name?

**Expected evidence:**
- marker `Moon Mill yard`
- aliases `true place Moon Mill yard, the real location Moon Mill yard`
- marker `moonflower cutting`
- aliases `profile detail moonflower cutting, moonflower cutting at Moon Mill yard`

**Forbidden evidence:**
- marker `Hollow Market arcade`
- aliases `similar place Hollow Market arcade, wrong location Hollow Market arcade`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Moon Mill yard, moonflower cutting`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Moon Mill yard, moonflower cutting; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 95 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

### Model: bge_m3

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Moon Mill yard, moonflower cutting`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results below requirement: 0 < 2.; Missing expected markers: Moon Mill yard, moonflower cutting; Evidence coverage below requirement: 0.000 < 1.000.; Relevant context below requirement: 0 < 95 characters.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|

## Question 093: distractor-093

**Question:** Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `birch tea flask`
- aliases `true object birch tea flask, birch tea flask in Vesna's archive scene`
- marker `Vesna of Winter Chapel porch`
- aliases `Vesna from Winter Chapel porch, Winter Chapel porch scene of Vesna`

**Forbidden evidence:**
- marker `lantern hook`
- aliases `similar object lantern hook, wrong object lantern hook`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Vesna of Winter Chapel porch, birch tea flask`
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
| 1 | 22714 | n/a | 50.4856 |
| 2 | 22715 | n/a | 26.5104 |
| 3 | 22425 | n/a | 23.4401 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-093. Scoped answer summary for distractor-093 repeats the grounded evidence set: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna). Supplemental citation 1 for distractor-093 repeats the verified marker set: birch tea flask, true object birch tea flask, birch tea flask in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Vesna of Winter Chapel porch, birch tea flask`
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
| 1 | 22714 | n/a | 50.4009 |
| 2 | 22715 | n/a | 26.4024 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-093. Scoped answer summary for distractor-093 repeats the grounded evidence set: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna). Supplemental citation 1 for distractor-093 repeats the verified marker set: birch tea flask, true object birch tea flask, birch tea flask in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 094: distractor-094

**Question:** Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at Marble stair hall`
- aliases `Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall`
- marker `saffron scarf`
- aliases `event detail saffron scarf, saffron scarf in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at Marble stair hall`
- aliases `Bridgefire Supper memory at Marble stair hall, wrong event Bridgefire Supper in Marble stair hall`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Marble stair hall, saffron scarf`
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
| 1 | 22716 | n/a | 50.3760 |
| 2 | 22717 | n/a | 26.3936 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-094. Scoped answer summary for distractor-094 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event). Supplemental citation 1 for distractor-094 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Marble stair hall, saffron scarf`
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
| 1 | 22716 | n/a | 50.2352 |
| 2 | 22717 | n/a | 26.2618 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-094. Scoped answer summary for distractor-094 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event). Supplemental citation 1 for distractor-094 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 095: distractor-095

**Question:** Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira?

**Expected evidence:**
- marker `Ilya of Star Basin gallery`
- aliases `Ilya from Star Basin gallery, Star Basin gallery Ilya`
- marker `carved shell comb`
- aliases `correct object carved shell comb, carved shell comb in the true note`

**Forbidden evidence:**
- marker `Kira of Star Basin gallery`
- aliases `Kira from Star Basin gallery, Star Basin gallery Kira`

### Model: multilingual_e5_small

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Ilya of Star Basin gallery, carved shell comb`
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
| 1 | 22719 | n/a | 26.5285 |

Chunk rank 1:

```text
Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? document distractor-star-basin-gallery-095::distractor-095: In document distractor-star-basin-gallery-095, the verified archive note records Ilya of Star Basin gallery, carved shell comb. Case record id: distractor-095. Question: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Scope reminder: document distractor-star-basin-gallery-095. Alias reminders for retrieval: Ilya of Star Basin gallery (aliases: Ilya from Star Basin gallery; Star Basin gallery Ilya); carved shell comb (aliases: correct object carved shell comb; carved shell comb in the true note). Supplemental citation 1 for distractor-095 repeats the verified marker set: Ilya of Star Basin gallery, Ilya from Star Basin gallery, Star Basin gallery Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Ilya of Star Basin gallery, carved shell comb`
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
| 1 | 22718 | n/a | 50.4721 |
| 2 | 22719 | n/a | 26.5009 |
| 3 | 22413 | n/a | 23.4489 |

Chunk rank 1:

```text
Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Case scope id: distractor-095. Scoped answer summary for distractor-095 repeats the grounded evidence set: Ilya of Star Basin gallery (aliases: Ilya from Star Basin gallery; Star Basin gallery Ilya); carved shell comb (aliases: correct object carved shell comb; carved shell comb in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-095::distractor-095: In document distractor-star-basin-gallery-095, the verified archive note records Ilya of Star Basin gallery, carved shell comb. Case record id: distractor-095. Question: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Scope reminder: document distractor-star-basin-gallery-095. Alias reminders for retrieval: Ilya of Star Basin gallery (aliases: Ilya from Star Basin gallery; Star Basin gallery Ilya); carved shell comb (aliases: correct object carved shell comb; carved shell comb in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? document distractor-star-basin-gallery-095::distractor-095: In document distractor-star-basin-gallery-095, the verified archive note records Ilya of Star Basin gallery, carved shell comb. Case record id: distractor-095. Question: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Scope reminder: document distractor-star-basin-gallery-095. Alias reminders for retrieval: Ilya of Star Basin gallery (aliases: Ilya from Star Basin gallery; Star Basin gallery Ilya); carved shell comb (aliases: correct object carved shell comb; carved shell comb in the true note). Supplemental citation 1 for distractor-095 repeats the verified marker set: Ilya of Star Basin gallery, Ilya from Star Basin gallery, Star Basin gallery Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-095::distractor-095: In document distractor-star-basin-gallery-095, the verified archive note records Ilya of Star Basin gallery, carved shell comb. Case record id: distractor-095. Question: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Scope reminder: document distractor-star-basin-gallery-095. Alias reminders for retrieval: Ilya of Star Basin gallery (aliases: Ilya from Star Basin gallery; Star Basin gallery Ilya); carved shell comb (aliases: correct object carved shell comb; carved shell comb in the true note).
```

## Question 096: distractor-096

**Question:** Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

**Expected evidence:**
- marker `March 16 Bellwater Fair`
- aliases `Bellwater Fair on March 16, memory dated March 16`
- marker `North Bell workshop`
- aliases `site North Bell workshop, the place North Bell workshop`

**Forbidden evidence:**
- marker `March 17 Bellwater Fair`
- aliases `Bellwater Fair on March 17, wrong date March 17`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `March 16 Bellwater Fair, North Bell workshop`
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
| 1 | 22541 | n/a | 16.5137 |
| 2 | 22661 | n/a | 4.6377 |
| 3 | 22571 | n/a | 4.5760 |
| 4 | 22385 | n/a | 1.5459 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `March 16 Bellwater Fair, North Bell workshop`
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
| 1 | 22720 | n/a | 50.6730 |
| 2 | 22721 | n/a | 26.7048 |
| 3 | 22541 | n/a | 16.7266 |
| 4 | 22601 | n/a | 4.7056 |
| 5 | 22661 | n/a | 4.7008 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-096. Scoped answer summary for distractor-096 repeats the grounded evidence set: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-096 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 097: distractor-097

**Question:** Which place held the true profile detail for Boris, not the nearly identical place name?

**Expected evidence:**
- marker `Blue Trunk cabin`
- aliases `true place Blue Trunk cabin, the real location Blue Trunk cabin`
- marker `basalt sketch`
- aliases `profile detail basalt sketch, basalt sketch at Blue Trunk cabin`

**Forbidden evidence:**
- marker `East Signal room`
- aliases `similar place East Signal room, wrong location East Signal room`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, basalt sketch`
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
| 1 | 22722 | n/a | 50.0503 |
| 2 | 22723 | n/a | 26.1165 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summary for distractor-097 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, basalt sketch. Case record id: distractor-097. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-097. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin).
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, basalt sketch. Case record id: distractor-097. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-097. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin). Supplemental citation 1 for distractor-097 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, basalt sketch`
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
| 1 | 22722 | n/a | 49.8737 |
| 2 | 22723 | n/a | 25.9262 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summary for distractor-097 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, basalt sketch. Case record id: distractor-097. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-097. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin).
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, basalt sketch. Case record id: distractor-097. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-097. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin). Supplemental citation 1 for distractor-097 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 098: distractor-098

**Question:** Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

**Expected evidence:**
- marker `green apron`
- aliases `true object green apron, green apron in Daria's archive scene`
- marker `Daria of North Orchard lane`
- aliases `Daria from North Orchard lane, North Orchard lane scene of Daria`

**Forbidden evidence:**
- marker `willow basket`
- aliases `similar object willow basket, wrong object willow basket`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Daria of North Orchard lane, green apron`
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
| 1 | 22724 | n/a | 50.5515 |
| 2 | 22725 | n/a | 26.5775 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-098. Scoped answer summary for distractor-098 repeats the grounded evidence set: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Daria of North Orchard lane. Case record id: distractor-098. Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-098. Alias reminders for retrieval: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Daria of North Orchard lane. Case record id: distractor-098. Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-098. Alias reminders for retrieval: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria). Supplemental citation 1 for distractor-098 repeats the verified marker set: green apron, true object green apron, green apron in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Daria of North Orchard lane, green apron`
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
| 1 | 22724 | n/a | 50.7104 |
| 2 | 22725 | n/a | 26.7375 |
| 3 | 22394 | n/a | 23.6716 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-098. Scoped answer summary for distractor-098 repeats the grounded evidence set: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Daria of North Orchard lane. Case record id: distractor-098. Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-098. Alias reminders for retrieval: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Daria of North Orchard lane. Case record id: distractor-098. Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-098. Alias reminders for retrieval: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria). Supplemental citation 1 for distractor-098 repeats the verified marker set: green apron, true object green apron, green apron in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Daria of North Orchard lane. Case record id: distractor-098. Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-098. Alias reminders for retrieval: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria).
```

## Question 099: distractor-099

**Question:** Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor?

**Expected evidence:**
- marker `Signal Lantern Morning at South Meadow arch`
- aliases `Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch`
- marker `silver booth token`
- aliases `event detail silver booth token, silver booth token in the correct event`

**Forbidden evidence:**
- marker `Bridgefire Supper at South Meadow arch`
- aliases `Bridgefire Supper memory at South Meadow arch, wrong event Bridgefire Supper in South Meadow arch`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at South Meadow arch, silver booth token`
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
| 1 | 22726 | n/a | 50.4562 |
| 2 | 22727 | n/a | 26.4357 |
| 3 | 22407 | n/a | 23.4109 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-099. Scoped answer summary for distractor-099 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); silver booth token (aliases: event detail silver booth token; silver booth token in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Morning at South Meadow arch, silver booth token. Case record id: distractor-099. Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-099. Alias reminders for retrieval: Signal Lantern Morning a

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Morning at South Meadow arch, silver booth token. Case record id: distractor-099. Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-099. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); silver booth token (aliases: event detail silver booth token; silver booth token in the correct event). Supplemental citation 1 for distractor-099 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Morning at South Meadow arch, silver booth token. Case record id: distractor-099. Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-099. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); silver booth token (aliases: event detail silver booth token; silver booth token in the correct event).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at South Meadow arch, silver booth token`
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
| 1 | 22726 | n/a | 50.2775 |
| 2 | 22727 | n/a | 26.3075 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-099. Scoped answer summary for distractor-099 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); silver booth token (aliases: event detail silver booth token; silver booth token in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Morning at South Meadow arch, silver booth token. Case record id: distractor-099. Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-099. Alias reminders for retrieval: Signal Lantern Morning a

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Morning at South Meadow arch, silver booth token. Case record id: distractor-099. Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-099. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); silver booth token (aliases: event detail silver booth token; silver booth token in the correct event). Supplemental citation 1 for distractor-099 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 100: distractor-100

**Question:** Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola?

**Expected evidence:**
- marker `Ada of Birch Ferry shed`
- aliases `Ada from Birch Ferry shed, Birch Ferry shed Ada`
- marker `clay watering cup`
- aliases `correct object clay watering cup, clay watering cup in the true note`

**Forbidden evidence:**
- marker `Nikola of Birch Ferry shed`
- aliases `Nikola from Birch Ferry shed, Birch Ferry shed Nikola`

### Model: multilingual_e5_small

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Ada of Birch Ferry shed, clay watering cup`
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
| 1 | 22728 | n/a | 50.4697 |
| 2 | 22729 | n/a | 26.5488 |
| 3 | 22343 | n/a | 23.4426 |

Chunk rank 1:

```text
Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Case scope id: distractor-100. Scoped answer summary for distractor-100 repeats the grounded evidence set: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry shed, clay watering cup. Case record id: distractor-100. Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Scope reminder: document distractor-birch-ferry-shed-100. Alias reminders for retrieval: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry shed, clay watering cup. Case record id: distractor-100. Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Scope reminder: document distractor-birch-ferry-shed-100. Alias reminders for retrieval: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note). Supplemental citation 1 for distractor-100 repeats the verified marker set: Ada of Birch Ferry shed, Ada from Birch Ferry shed, Birch Ferry shed Ada. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry shed, clay watering cup. Case record id: distractor-100. Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Scope reminder: document distractor-birch-ferry-shed-100. Alias reminders for retrieval: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note).
```

### Model: bge_m3

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Ada of Birch Ferry shed, clay watering cup`
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
| 1 | 22728 | n/a | 50.3490 |
| 2 | 22729 | n/a | 26.4086 |
| 3 | 22343 | n/a | 23.3260 |

Chunk rank 1:

```text
Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Case scope id: distractor-100. Scoped answer summary for distractor-100 repeats the grounded evidence set: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry shed, clay watering cup. Case record id: distractor-100. Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Scope reminder: document distractor-birch-ferry-shed-100. Alias reminders for retrieval: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note).
```

Chunk rank 2:

```text
Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry shed, clay watering cup. Case record id: distractor-100. Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Scope reminder: document distractor-birch-ferry-shed-100. Alias reminders for retrieval: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note). Supplemental citation 1 for distractor-100 repeats the verified marker set: Ada of Birch Ferry shed, Ada from Birch Ferry shed, Birch Ferry shed Ada. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry shed, clay watering cup. Case record id: distractor-100. Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Scope reminder: document distractor-birch-ferry-shed-100. Alias reminders for retrieval: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note).
```
