# Real Question Eval Full Results

## Run
- Run ID: `20260703_182938Z`
- Dataset: `Eternal World Distractor Validation V1`
- Dataset ID: `eternal-world-distractor-v1`
- Dataset file: `/app/app/modules/real_question_eval/datasets/eternal_world_distractor_v1.json`
- Run status: `COMPLETED`
- Quality status: `PASS`
- Models: `multilingual_e5_base, multilingual_e5_large`

## Question 001: distractor-twin-innkeepers

**Question:** Which Marta kept the North Inn ledger, and what detail identified her apron?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24131 | n/a | 0.8986 |
| 2 | 24130 | n/a | 0.8907 |

Chunk rank 1:

```text
Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Case record id: distractor-twin-innkeepers. Question: Which Marta kept the North Inn ledger, and what detail identified her apron? Scope reminder: document innkeeper-letters. Alias reminders for retrieval: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron). Supplemental citation 1 for distractor-twin-innkeepers repeats the verified marker set: Marta of North Inn, North Inn Marta, Marta from the North Inn. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? Case scope id: distractor-twin-innkeepers. Scoped answer summary for distractor-twin-innkeepers repeats the grounded evidence set: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Case record id: distractor-twin-innkeepers. Question: Which Marta kept the North Inn ledger, and what detail identified her apron? Scope reminder: document innkeeper-letters. Alias reminders for retrieval: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron).
```

### Model: multilingual_e5_large

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Marta of North Inn, green apron`
- Missing: `none`
- Forbidden hits: `Marta of River Inn`
- Distractor hits: `Marta of River Inn`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 4.; Forbidden markers found: Marta of River Inn`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24931 | n/a | 0.8859 |
| 2 | 24827 | n/a | 0.8756 |
| 3 | 24930 | n/a | 0.8702 |
| 4 | 24927 | n/a | 0.8117 |
| 5 | 24794 | n/a | 0.7994 |

Chunk rank 1:

```text
Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Case record id: distractor-twin-innkeepers. Question: Which Marta kept the North Inn ledger, and what detail identified her apron? Scope reminder: document innkeeper-letters. Alias reminders for retrieval: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron). Supplemental citation 1 for distractor-twin-innkeepers repeats the verified marker set: Marta of North Inn, North Inn Marta, Marta from the North Inn. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Case record id: distractor-twin-innkeepers. Question: Which Marta kept the North Inn ledger, and what detail identified her apron? Scope reminder: document innkeeper-letters. Alias reminders for retrieval: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron).
```

Chunk rank 3:

```text
Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? Case scope id: distractor-twin-innkeepers. Scoped answer summary for distractor-twin-innkeepers repeats the grounded evidence set: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Case record id: distractor-twin-innkeepers. Question: Which Marta kept the North Inn ledger, and what detail identified her apron? Scope reminder: document innkeeper-letters. Alias reminders for retrieval: Marta of North Inn (aliases: North Inn Marta; Marta from the North Inn); green apron (aliases: apron dyed green; green inn apron).
```

Chunk rank 4:

```text
document innkeeper-letters::distractor-twin-innkeepers::distractor: A conflicting note in document innkeeper-letters mentions Marta of River Inn (aliases: River Inn Marta; Marta from the river inn) as a misleading archival rumor. That rumor is explicitly different from the verified record for this source scope. Conflict marker only: Marta of River Inn remains archival noise.
```

Chunk rank 5:

```text
document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Daria of North Orchard lane. Case record id: distractor-098. Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-098. Alias reminders for retrieval: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria).
```

## Question 002: distractor-june-market-date

**Question:** Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24133 | n/a | 0.9097 |
| 2 | 24132 | n/a | 0.8964 |
| 3 | 24028 | n/a | 0.8954 |

Chunk rank 1:

```text
Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Bridge square. Case record id: distractor-june-market-date. Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Scope reminder: document market-announcements. Alias reminders for retrieval: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza). Supplemental citation 1 for distractor-june-market-date repeats the verified marker set: June 14 night market, night market on June 14, 14 June market at night. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Case scope id: distractor-june-market-date. Scoped answer summary for distractor-june-market-date repeats the grounded evidence set: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Bridge square. Case record id: distractor-june-market-date. Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Scope reminder: document market-announcements. Alias reminders for retrieval: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza).
```

Chunk rank 3:

```text
document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Bridge square. Case record id: distractor-june-market-date. Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Scope reminder: document market-announcements. Alias reminders for retrieval: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza).
```

### Model: multilingual_e5_large

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Bell Bridge square, June 14 night market`
- Missing: `none`
- Forbidden hits: `June 4 noon market`
- Distractor hits: `June 4 noon market`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 3.; Forbidden markers found: June 4 noon market`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24933 | n/a | 0.8991 |
| 2 | 24828 | n/a | 0.8923 |
| 3 | 24932 | n/a | 0.8912 |
| 4 | 24928 | n/a | 0.8285 |
| 5 | 25001 | n/a | 0.7908 |

Chunk rank 1:

```text
Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Bridge square. Case record id: distractor-june-market-date. Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Scope reminder: document market-announcements. Alias reminders for retrieval: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza). Supplemental citation 1 for distractor-june-market-date repeats the verified marker set: June 14 night market, night market on June 14, 14 June market at night. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Bridge square. Case record id: distractor-june-market-date. Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Scope reminder: document market-announcements. Alias reminders for retrieval: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza).
```

Chunk rank 3:

```text
Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Case scope id: distractor-june-market-date. Scoped answer summary for distractor-june-market-date repeats the grounded evidence set: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Bridge square. Case record id: distractor-june-market-date. Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Scope reminder: document market-announcements. Alias reminders for retrieval: June 14 night market (aliases: night market on June 14; 14 June market at night); Bell Bridge square (aliases: square by Bell Bridge; Bell Bridge plaza).
```

Chunk rank 4:

```text
document market-announcements::distractor-june-market-date::distractor: A conflicting note in document market-announcements mentions June 4 noon market (aliases: noon market on June 4; 4 June daytime market) as a misleading archival rumor. That rumor is explicitly different from the verified record for this source scope. Conflict marker only: June 4 noon market remains archival noise.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 003: distractor-two-levs

**Question:** Which Lev repaired the oak barrels, not the one who worked by the ferry?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24135 | n/a | 0.8726 |
| 2 | 24134 | n/a | 0.8508 |

Chunk rank 1:

```text
Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case record id: distractor-two-levs. Question: Which Lev repaired the oak barrels, not the one who worked by the ferry? Scope reminder: document workshop-accounts. Alias reminders for retrieval: Lev the cooper (aliases: cooper named Lev; Lev of the cooper's bench); oak barrel hoops (aliases: hoops for oak barrels; oak hoop repairs). Supplemental citation 1 for distractor-two-levs repeats the verified marker set: Lev the cooper, cooper named Lev, Lev of the cooper's bench. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? Case scope id: distractor-two-levs. Scoped answer summary for distractor-two-levs repeats the grounded evidence set: Lev the cooper (aliases: cooper named Lev; Lev of the cooper's bench); oak barrel hoops (aliases: hoops for oak barrels; oak hoop repairs). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case record id: distractor-two-levs. Question: Which Lev repaired the oak barrels, not the one who worked by the ferry? Scope reminder: document workshop-accounts. Alias reminders for retrieval: Lev the cooper (aliases: cooper named Lev; Lev of the cooper's bench); oak barrel hoops (aliases: hoops for oak barrels; oak hoop repairs).
```

### Model: multilingual_e5_large

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Lev the cooper, oak barrel hoops`
- Missing: `none`
- Forbidden hits: `Lev the ferryman`
- Distractor hits: `Lev the ferryman`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 4.; Forbidden markers found: Lev the ferryman`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24935 | n/a | 0.8645 |
| 2 | 24829 | n/a | 0.8472 |
| 3 | 24934 | n/a | 0.8416 |
| 4 | 24929 | n/a | 0.8061 |
| 5 | 24740 | n/a | 0.7912 |

Chunk rank 1:

```text
Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case record id: distractor-two-levs. Question: Which Lev repaired the oak barrels, not the one who worked by the ferry? Scope reminder: document workshop-accounts. Alias reminders for retrieval: Lev the cooper (aliases: cooper named Lev; Lev of the cooper's bench); oak barrel hoops (aliases: hoops for oak barrels; oak hoop repairs). Supplemental citation 1 for distractor-two-levs repeats the verified marker set: Lev the cooper, cooper named Lev, Lev of the cooper's bench. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case record id: distractor-two-levs. Question: Which Lev repaired the oak barrels, not the one who worked by the ferry? Scope reminder: document workshop-accounts. Alias reminders for retrieval: Lev the cooper (aliases: cooper named Lev; Lev of the cooper's bench); oak barrel hoops (aliases: hoops for oak barrels; oak hoop repairs).
```

Chunk rank 3:

```text
Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? Case scope id: distractor-two-levs. Scoped answer summary for distractor-two-levs repeats the grounded evidence set: Lev the cooper (aliases: cooper named Lev; Lev of the cooper's bench); oak barrel hoops (aliases: hoops for oak barrels; oak hoop repairs). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case record id: distractor-two-levs. Question: Which Lev repaired the oak barrels, not the one who worked by the ferry? Scope reminder: document workshop-accounts. Alias reminders for retrieval: Lev the cooper (aliases: cooper named Lev; Lev of the cooper's bench); oak barrel hoops (aliases: hoops for oak barrels; oak hoop repairs).
```

Chunk rank 4:

```text
document workshop-accounts::distractor-two-levs::distractor: A conflicting note in document workshop-accounts mentions Lev the ferryman (aliases: ferryman named Lev; Lev from the ferry dock) as a misleading archival rumor. That rumor is explicitly different from the verified record for this source scope. Conflict marker only: Lev the ferryman remains archival noise.
```

Chunk rank 5:

```text
document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note).
```

## Question 004: distractor-similar-islands

**Question:** Which island shed kept the painted blue oar, and which similar island name is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24026 | n/a | 0.8908 |
| 2 | 24137 | n/a | 0.8878 |
| 3 | 24136 | n/a | 0.8849 |

Chunk rank 1:

```text
document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oar. Case record id: distractor-similar-islands. Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Scope reminder: document ferry-shed-notes. Alias reminders for retrieval: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue).
```

Chunk rank 2:

```text
Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oar. Case record id: distractor-similar-islands. Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Scope reminder: document ferry-shed-notes. Alias reminders for retrieval: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue). Supplemental citation 1 for distractor-similar-islands repeats the verified marker set: Fog Island ferry shed, ferry shed on Fog Island, Fog Island shed. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Case scope id: distractor-similar-islands. Scoped answer summary for distractor-similar-islands repeats the grounded evidence set: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oar. Case record id: distractor-similar-islands. Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Scope reminder: document ferry-shed-notes. Alias reminders for retrieval: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue).
```

### Model: multilingual_e5_large

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
| 1 | 24937 | n/a | 0.8983 |
| 2 | 24826 | n/a | 0.8900 |
| 3 | 24936 | n/a | 0.8900 |
| 4 | 24921 | n/a | 0.8371 |
| 5 | 24824 | n/a | 0.8265 |

Chunk rank 1:

```text
Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oar. Case record id: distractor-similar-islands. Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Scope reminder: document ferry-shed-notes. Alias reminders for retrieval: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue). Supplemental citation 1 for distractor-similar-islands repeats the verified marker set: Fog Island ferry shed, ferry shed on Fog Island, Fog Island shed. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oar. Case record id: distractor-similar-islands. Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Scope reminder: document ferry-shed-notes. Alias reminders for retrieval: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue).
```

Chunk rank 3:

```text
Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Case scope id: distractor-similar-islands. Scoped answer summary for distractor-similar-islands repeats the grounded evidence set: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oar. Case record id: distractor-similar-islands. Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Scope reminder: document ferry-shed-notes. Alias reminders for retrieval: Fog Island ferry shed (aliases: ferry shed on Fog Island; Fog Island shed); painted blue oar (aliases: blue-painted oar; oar painted blue).
```

Chunk rank 4:

```text
document distractor-winter-chapel-porch-033::distractor-033::distractor: A conflicting note in document distractor-winter-chapel-porch-033 mentions blue oar (aliases: similar object blue oar; wrong object blue oar) as a misleading archival rumor. That rumor is explicitly different from the verified record for this source scope. Conflict marker only: blue oar remains archival noise.
```

Chunk rank 5:

```text
document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa).
```

## Question 005: distractor-letter-mixup

**Question:** Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24139 | n/a | 0.8861 |
| 2 | 24138 | n/a | 0.8845 |
| 3 | 23930 | n/a | 0.8537 |

Chunk rank 1:

```text
Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread. Case record id: distractor-letter-mixup. Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Scope reminder: document courier-bag-index. Alias reminders for retrieval: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread). Supplemental citation 1 for distractor-letter-mixup repeats the verified marker set: Ada's winter letter, winter letter from Ada, Ada winter letter. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Case scope id: distractor-letter-mixup. Scoped answer summary for distractor-letter-mixup repeats the grounded evidence set: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread. Case record id: distractor-letter-mixup. Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Scope reminder: document courier-bag-index. Alias reminders for retrieval: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread).
```

Chunk rank 3:

```text
document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread. Case record id: distractor-letter-mixup. Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Scope reminder: document courier-bag-index. Alias reminders for retrieval: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread).
```

### Model: multilingual_e5_large

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
| 1 | 24939 | n/a | 0.8838 |
| 2 | 24938 | n/a | 0.8752 |
| 3 | 24730 | n/a | 0.8628 |
| 4 | 24923 | n/a | 0.8315 |
| 5 | 24816 | n/a | 0.7932 |

Chunk rank 1:

```text
Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread. Case record id: distractor-letter-mixup. Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Scope reminder: document courier-bag-index. Alias reminders for retrieval: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread). Supplemental citation 1 for distractor-letter-mixup repeats the verified marker set: Ada's winter letter, winter letter from Ada, Ada winter letter. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Case scope id: distractor-letter-mixup. Scoped answer summary for distractor-letter-mixup repeats the grounded evidence set: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread. Case record id: distractor-letter-mixup. Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Scope reminder: document courier-bag-index. Alias reminders for retrieval: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread).
```

Chunk rank 3:

```text
document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread. Case record id: distractor-letter-mixup. Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Scope reminder: document courier-bag-index. Alias reminders for retrieval: Ada's winter letter (aliases: winter letter from Ada; Ada winter letter); violet wax thread (aliases: thread of violet wax; violet wax seal thread).
```

Chunk rank 4:

```text
document distractor-winter-chapel-porch-063::distractor-063::distractor: A conflicting note in document distractor-winter-chapel-porch-063 mentions wax thread (aliases: similar object wax thread; wrong object wax thread) as a misleading archival rumor. That rumor is explicitly different from the verified record for this source scope. Conflict marker only: wax thread remains archival noise.
```

Chunk rank 5:

```text
document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lantern Morning at Willow Courtyard well, wax thread. Case record id: distractor-044. Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-044. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); wax thread (aliases: event detail wax thread; wax thread in the correct event).
```

## Question 006: distractor-006

**Question:** Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `North Bell workshop`
- Missing: `March 16 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Missing expected evidence: March 16 Bellwater Fair`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24291 | n/a | 0.8980 |
| 2 | 24171 | n/a | 0.8961 |
| 3 | 24231 | n/a | 0.8948 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellwater Fair, North Bell workshop. Case record id: distractor-081. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-081. Alias reminders for retrieval: March 19 Bellwater Fair (aliases: Bellwater Fair on March 19; memory dated March 19); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-081 repeats the verified marker set: March 19 Bellwater Fair, Bellwater Fair on March 19, memory dated March 19. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-051::distractor-051: In document distractor-north-bell-workshop-051, the verified archive note records March 25 Bellwater Fair, North Bell workshop. Case record id: distractor-051. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-051. Alias reminders for retrieval: March 25 Bellwater Fair (aliases: Bellwater Fair on March 25; memory dated March 25); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-051 repeats the verified marker set: March 25 Bellwater Fair, Bellwater Fair on March 25, memory dated March 25. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25001 | n/a | 0.8858 |
| 2 | 25061 | n/a | 0.8847 |
| 3 | 25121 | n/a | 0.8845 |
| 4 | 25060 | n/a | 0.8840 |
| 5 | 24941 | n/a | 0.8835 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-096 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. Scoped answer summary for distractor-066 repeats the grounded evidence set: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 007: distractor-007

**Question:** Which place held the true profile detail for Nikola, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, brass compass`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `partial`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24303 | n/a | 0.8634 |
| 2 | 24223 | n/a | 0.8624 |
| 3 | 24143 | n/a | 0.8517 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distractor-087: In document distractor-cloud-wharf-office-087, the verified archive note records Cloud Wharf office, oak barrel hoops. Case record id: distractor-087. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-087. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); oak barrel hoops (aliases: profile detail oak barrel hoops; oak barrel hoops at Cloud Wharf office). Supplemental citation 1 for distractor-087 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-moon-mill-yard-047::distractor-047: In document distractor-moon-mill-yard-047, the verified archive note records Moon Mill yard, willow basket. Case record id: distractor-047. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-047. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); willow basket (aliases: profile detail willow basket; willow basket at Moon Mill yard). Supplemental citation 1 for distractor-047 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distractor-007: In document distractor-blue-trunk-cabin-007, the verified archive note records Blue Trunk cabin, brass compass. Case record id: distractor-007. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-007. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); brass compass (aliases: profile detail brass compass; brass compass at Blue Trunk cabin). Supplemental citation 1 for distractor-007 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25103 | n/a | 0.8328 |
| 2 | 25023 | n/a | 0.8240 |
| 3 | 25102 | n/a | 0.8195 |
| 4 | 24943 | n/a | 0.8162 |
| 5 | 25022 | n/a | 0.8099 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distractor-087: In document distractor-cloud-wharf-office-087, the verified archive note records Cloud Wharf office, oak barrel hoops. Case record id: distractor-087. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-087. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); oak barrel hoops (aliases: profile detail oak barrel hoops; oak barrel hoops at Cloud Wharf office). Supplemental citation 1 for distractor-087 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-moon-mill-yard-047::distractor-047: In document distractor-moon-mill-yard-047, the verified archive note records Moon Mill yard, willow basket. Case record id: distractor-047. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-047. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); willow basket (aliases: profile detail willow basket; willow basket at Moon Mill yard). Supplemental citation 1 for distractor-047 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-087. Scoped answer summary for distractor-087 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); oak barrel hoops (aliases: profile detail oak barrel hoops; oak barrel hoops at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-087::distractor-087: In document distractor-cloud-wharf-office-087, the verified archive note records Cloud Wharf office, oak barrel hoops. Case record id: distractor-087. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-087. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); oak barrel hoops (aliases: profile detail oak barrel hoops; oak barrel hoops at Cloud Wharf office).
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distractor-007: In document distractor-blue-trunk-cabin-007, the verified archive note records Blue Trunk cabin, brass compass. Case record id: distractor-007. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-007. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); brass compass (aliases: profile detail brass compass; brass compass at Blue Trunk cabin). Supplemental citation 1 for distractor-007 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-047. Scoped answer summary for distractor-047 repeats the grounded evidence set: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); willow basket (aliases: profile detail willow basket; willow basket at Moon Mill yard). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-moon-mill-yard-047::distractor-047: In document distractor-moon-mill-yard-047, the verified archive note records Moon Mill yard, willow basket. Case record id: distractor-047. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-047. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); willow basket (aliases: profile detail willow basket; willow basket at Moon Mill yard).
```

## Question 008: distractor-008

**Question:** Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24145 | n/a | 0.8913 |
| 2 | 23988 | n/a | 0.8907 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sonya of North Orchard lane. Case record id: distractor-008. Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-008. Alias reminders for retrieval: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya). Supplemental citation 1 for distractor-008 repeats the verified marker set: linen wick, true object linen wick, linen wick in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sonya of North Orchard lane. Case record id: distractor-008. Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-008. Alias reminders for retrieval: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya).
```

### Model: multilingual_e5_large

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
| 1 | 24945 | n/a | 0.8674 |
| 2 | 24944 | n/a | 0.8594 |
| 3 | 24788 | n/a | 0.8592 |
| 4 | 25025 | n/a | 0.8438 |
| 5 | 25125 | n/a | 0.8431 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sonya of North Orchard lane. Case record id: distractor-008. Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-008. Alias reminders for retrieval: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya). Supplemental citation 1 for distractor-008 repeats the verified marker set: linen wick, true object linen wick, linen wick in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-008. Scoped answer summary for distractor-008 repeats the grounded evidence set: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sonya of North Orchard lane. Case record id: distractor-008. Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-008. Alias reminders for retrieval: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya).
```

Chunk rank 3:

```text
document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sonya of North Orchard lane. Case record id: distractor-008. Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-008. Alias reminders for retrieval: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya).
```

Chunk rank 4:

```text
Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mask, Sonya of Winter Chapel porch. Case record id: distractor-048. Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-048. Alias reminders for retrieval: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive scene); Sonya of Winter Chapel porch (aliases: Sonya from Winter Chapel porch; Winter Chapel porch scene of Sonya). Supplemental citation 1 for distractor-048 repeats the verified marker set: paper moon mask, true object paper moon mask, paper moon mask in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Daria of North Orchard lane. Case record id: distractor-098. Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-098. Alias reminders for retrieval: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria). Supplemental citation 1 for distractor-098 repeats the verified marker set: green apron, true object green apron, green apron in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 009: distractor-009

**Question:** Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at South Meadow arch, star ledger page`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24001 | n/a | 0.8983 |
| 2 | 24147 | n/a | 0.8911 |

Chunk rank 1:

```text
document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Morning at South Meadow arch, star ledger page. Case record id: distractor-009. Question: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-009. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); star ledger page (aliases: event detail star ledger page; star ledger page in the correct event).
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Morning at South Meadow arch, star ledger page. Case record id: distractor-009. Question: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-009. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); star ledger page (aliases: event detail star ledger page; star ledger page in the correct event). Supplemental citation 1 for distractor-009 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at South Meadow arch, star ledger page`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24947 | n/a | 0.8960 |
| 2 | 24946 | n/a | 0.8896 |
| 3 | 25007 | n/a | 0.8811 |
| 4 | 25037 | n/a | 0.8792 |
| 5 | 25036 | n/a | 0.8782 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Morning at South Meadow arch, star ledger page. Case record id: distractor-009. Question: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-009. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); star ledger page (aliases: event detail star ledger page; star ledger page in the correct event). Supplemental citation 1 for distractor-009 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-009. Scoped answer summary for distractor-009 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); star ledger page (aliases: event detail star ledger page; star ledger page in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Morning at South Meadow arch, star ledger page. Case record id: distractor-009. Question: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-009. Alias reminders for retrieval: Signal Lantern Morning at South

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-039::distractor-039: In document distractor-south-meadow-arch-039, the verified archive note records Signal Lantern Morning at South Meadow arch, brass compass. Case record id: distractor-039. Question: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-039. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); brass compass (aliases: event detail brass compass; brass compass in the correct event). Supplemental citation 1 for distractor-039 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Morning at South Meadow arch, rope bridge permit. Case record id: distractor-054. Question: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-054. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); rope bridge permit (aliases: event detail rope bridge permit; rope bridge permit in the correct event). Supplemental citation 1 for distractor-054 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-054. Scoped answer summary for distractor-054 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); rope bridge permit (aliases: event detail rope bridge permit; rope bridge permit in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Morning at South Meadow arch, rope bridge permit. Case record id: distractor-054. Question: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-054. Alias reminders for retrieval: Signal Lantern Morning

[truncated in Markdown; full text is available in JSON]
```

## Question 010: distractor-010

**Question:** Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24149 | n/a | 0.8988 |
| 2 | 23937 | n/a | 0.8898 |
| 3 | 24148 | n/a | 0.8858 |

Chunk rank 1:

```text
Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry shed, lantern hook. Case record id: distractor-010. Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Scope reminder: document distractor-birch-ferry-shed-010. Alias reminders for retrieval: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note). Supplemental citation 1 for distractor-010 repeats the verified marker set: Selma of Birch Ferry shed, Selma from Birch Ferry shed, Birch Ferry shed Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry shed, lantern hook. Case record id: distractor-010. Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Scope reminder: document distractor-birch-ferry-shed-010. Alias reminders for retrieval: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note).
```

Chunk rank 3:

```text
Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Case scope id: distractor-010. Scoped answer summary for distractor-010 repeats the grounded evidence set: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry shed, lantern hook. Case record id: distractor-010. Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Scope reminder: document distractor-birch-ferry-shed-010. Alias reminders for retrieval: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 24949 | n/a | 0.8765 |
| 2 | 24948 | n/a | 0.8672 |
| 3 | 24737 | n/a | 0.8449 |
| 4 | 25109 | n/a | 0.8397 |
| 5 | 25108 | n/a | 0.8324 |

Chunk rank 1:

```text
Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry shed, lantern hook. Case record id: distractor-010. Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Scope reminder: document distractor-birch-ferry-shed-010. Alias reminders for retrieval: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note). Supplemental citation 1 for distractor-010 repeats the verified marker set: Selma of Birch Ferry shed, Selma from Birch Ferry shed, Birch Ferry shed Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Case scope id: distractor-010. Scoped answer summary for distractor-010 repeats the grounded evidence set: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry shed, lantern hook. Case record id: distractor-010. Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Scope reminder: document distractor-birch-ferry-shed-010. Alias reminders for retrieval: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note).
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry shed, lantern hook. Case record id: distractor-010. Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Scope reminder: document distractor-birch-ferry-shed-010. Alias reminders for retrieval: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Bridge square, cedar shovel. Case record id: distractor-090. Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Scope reminder: document distractor-bell-bridge-square-090. Alias reminders for retrieval: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note). Supplemental citation 1 for distractor-090 repeats the verified marker set: Selma of Bell Bridge square, Selma from Bell Bridge square, Bell Bridge square Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Case scope id: distractor-090. Scoped answer summary for distractor-090 repeats the grounded evidence set: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Bridge square, cedar shovel. Case record id: distractor-090. Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Scope reminder: document distractor-bell-bridge-square-090. Alias reminders for retrieval: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note).
```

## Question 011: distractor-011

**Question:** Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24271 | n/a | 0.9048 |
| 2 | 24151 | n/a | 0.9042 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 24981 | n/a | 0.8932 |
| 2 | 25101 | n/a | 0.8931 |
| 3 | 25011 | n/a | 0.8931 |
| 4 | 25041 | n/a | 0.8926 |
| 5 | 24951 | n/a | 0.8922 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-041 repeats the verified marker set: March 15 Bellwater Fair, Bellwater Fair on March 15, memory dated March 15. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-056::distractor-056: In document distractor-lantern-row-kiosk-056, the verified archive note records March 12 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-056. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-056. Alias reminders for retrieval: March 12 Bellwater Fair (aliases: Bellwater Fair on March 12; memory dated March 12); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-056 repeats the verified marker set: March 12 Bellwater Fair, Bellwater Fair on March 12, memory dated March 12. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 012: distractor-012

**Question:** Which place held the true profile detail for Zora, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, wax thread`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `partial`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24313 | n/a | 0.8566 |
| 2 | 24153 | n/a | 0.8559 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-092: In document distractor-moon-mill-yard-092, the verified archive note records Moon Mill yard, moonflower cutting. Case record id: distractor-092. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-092. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); moonflower cutting (aliases: profile detail moonflower cutting; moonflower cutting at Moon Mill yard). Supplemental citation 1 for distractor-092 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-cloud-wharf-office-012::distractor-012: In document distractor-cloud-wharf-office-012, the verified archive note records Cloud Wharf office, wax thread. Case record id: distractor-012. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-012. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); wax thread (aliases: profile detail wax thread; wax thread at Cloud Wharf office). Supplemental citation 1 for distractor-012 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, wax thread`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24953 | n/a | 0.8454 |
| 2 | 25033 | n/a | 0.8371 |
| 3 | 24952 | n/a | 0.8324 |
| 4 | 25113 | n/a | 0.8311 |
| 5 | 25032 | n/a | 0.8202 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-cloud-wharf-office-012::distractor-012: In document distractor-cloud-wharf-office-012, the verified archive note records Cloud Wharf office, wax thread. Case record id: distractor-012. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-012. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); wax thread (aliases: profile detail wax thread; wax thread at Cloud Wharf office). Supplemental citation 1 for distractor-012 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor-052: In document distractor-blue-trunk-cabin-052, the verified archive note records Blue Trunk cabin, violet ribbon. Case record id: distractor-052. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-052. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin). Supplemental citation 1 for distractor-052 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-012. Scoped answer summary for distractor-012 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); wax thread (aliases: profile detail wax thread; wax thread at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-012::distractor-012: In document distractor-cloud-wharf-office-012, the verified archive note records Cloud Wharf office, wax thread. Case record id: distractor-012. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-012. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); wax thread (aliases: profile detail wax thread; wax thread at Cloud Wharf office).
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-092: In document distractor-moon-mill-yard-092, the verified archive note records Moon Mill yard, moonflower cutting. Case record id: distractor-092. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-092. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); moonflower cutting (aliases: profile detail moonflower cutting; moonflower cutting at Moon Mill yard). Supplemental citation 1 for distractor-092 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary for distractor-052 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-052::distractor-052: In document distractor-blue-trunk-cabin-052, the verified archive note records Blue Trunk cabin, violet ribbon. Case record id: distractor-052. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-052. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin).
```

## Question 013: distractor-013

**Question:** Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24155 | n/a | 0.8820 |
| 2 | 24154 | n/a | 0.8741 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna). Supplemental citation 1 for distractor-013 repeats the verified marker set: tin key, true object tin key, tin key in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-013. Scoped answer summary for distractor-013 repeats the grounded evidence set: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna).
```

### Model: multilingual_e5_large

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
| 1 | 24955 | n/a | 0.8783 |
| 2 | 24954 | n/a | 0.8714 |
| 3 | 24795 | n/a | 0.8667 |
| 4 | 25075 | n/a | 0.8559 |
| 5 | 25074 | n/a | 0.8456 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna). Supplemental citation 1 for distractor-013 repeats the verified marker set: tin key, true object tin key, tin key in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-013. Scoped answer summary for distractor-013 repeats the grounded evidence set: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna).
```

Chunk rank 3:

```text
document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna).
```

Chunk rank 4:

```text
Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev). Supplemental citation 1 for distractor-073 repeats the verified marker set: star ledger page, true object star ledger page, star ledger page in Lev's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-073. Scoped answer summary for distractor-073 repeats the grounded evidence set: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev).
```

## Question 014: distractor-014

**Question:** Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24157 | n/a | 0.8947 |
| 2 | 24014 | n/a | 0.8929 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event). Supplemental citation 1 for distractor-014 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting chunk restates

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event).
```

### Model: multilingual_e5_large

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
| 1 | 24957 | n/a | 0.8914 |
| 2 | 24956 | n/a | 0.8889 |
| 3 | 25106 | n/a | 0.8767 |
| 4 | 25107 | n/a | 0.8761 |
| 5 | 25017 | n/a | 0.8737 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event). Supplemental citation 1 for distractor-014 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting chunk restates

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-014. Scoped answer summary for distractor-014 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-089. Scoped answer summary for distractor-089 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); canal route map (aliases: event detail canal route map; canal route map in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-089::distractor-089: In document distractor-willow-courtyard-well-089, the verified archive note records Signal Lantern Morning at Willow Courtyard well, canal route map. Case record id: distractor-089. Question: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-089. Alias reminders for retrieval:

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-089::distractor-089: In document distractor-willow-courtyard-well-089, the verified archive note records Signal Lantern Morning at Willow Courtyard well, canal route map. Case record id: distractor-089. Question: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-089. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); canal route map (aliases: event detail canal route map; canal route map in the correct event). Supplemental citation 1 for distractor-089 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lantern Morning at Willow Courtyard well, wax thread. Case record id: distractor-044. Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-044. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); wax thread (aliases: event detail wax thread; wax thread in the correct event). Supplemental citation 1 for distractor-044 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting chunk res

[truncated in Markdown; full text is available in JSON]
```

## Question 015: distractor-015

**Question:** Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24159 | n/a | 0.8780 |
| 2 | 24158 | n/a | 0.8669 |
| 3 | 23931 | n/a | 0.8651 |

Chunk rank 1:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). Supplemental citation 1 for distractor-015 repeats the verified marker set: Ilya of Bell Bridge square, Ilya from Bell Bridge square, Bell Bridge square Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer summary for distractor-015 repeats the grounded evidence set: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note).
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 24959 | n/a | 0.8860 |
| 2 | 24958 | n/a | 0.8782 |
| 3 | 24731 | n/a | 0.8697 |
| 4 | 25039 | n/a | 0.8386 |
| 5 | 25038 | n/a | 0.8340 |

Chunk rank 1:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). Supplemental citation 1 for distractor-015 repeats the verified marker set: Ilya of Bell Bridge square, Ilya from Bell Bridge square, Bell Bridge square Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer summary for distractor-015 repeats the grounded evidence set: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note).
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note). Supplemental citation 1 for distractor-055 repeats the verified marker set: Ilya of Birch Ferry shed, Ilya from Birch Ferry shed, Birch Ferry shed Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Case scope id: distractor-055. Scoped answer summary for distractor-055 repeats the grounded evidence set: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note).
```

## Question 016: distractor-016

**Question:** Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24161 | n/a | 0.9059 |
| 2 | 24251 | n/a | 0.9051 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwater Fair, Cedar Hill station. Case record id: distractor-016. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-016. Alias reminders for retrieval: March 26 Bellwater Fair (aliases: Bellwater Fair on March 26; memory dated March 26); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-016 repeats the verified marker set: March 26 Bellwater Fair, Bellwater Fair on March 26, memory dated March 26. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25081 | n/a | 0.8963 |
| 2 | 24990 | n/a | 0.8954 |
| 3 | 25050 | n/a | 0.8951 |
| 4 | 24991 | n/a | 0.8949 |
| 5 | 25080 | n/a | 0.8946 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwater Fair, Cedar Hill station. Case record id: distractor-076. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-076. Alias reminders for retrieval: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-076 repeats the verified marker set: March 14 Bellwater Fair, Bellwater Fair on March 14, memory dated March 14. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-031. Scoped answer summary for distractor-031 repeats the grounded evidence set: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-061. Scoped answer summary for distractor-061 repeats the grounded evidence set: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-031 repeats the verified marker set: March 23 Bellwater Fair, Bellwater Fair on March 23, memory dated March 23. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-076. Scoped answer summary for distractor-076 repeats the grounded evidence set: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwater Fair, Cedar Hill station. Case record id: distractor-076. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-076. Alias reminders for retrieval: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

## Question 017: distractor-017

**Question:** Which place held the true profile detail for Boris, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Moon Mill yard, glass ink bottle`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Missing expected evidence: Moon Mill yard, glass ink bottle`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24243 | n/a | 0.8630 |
| 2 | 24323 | n/a | 0.8624 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distractor-057: In document distractor-cloud-wharf-office-057, the verified archive note records Cloud Wharf office, canal route map. Case record id: distractor-057. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-057. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); canal route map (aliases: profile detail canal route map; canal route map at Cloud Wharf office). Supplemental citation 1 for distractor-057 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, basalt sketch. Case record id: distractor-097. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-097. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin). Supplemental citation 1 for distractor-097 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Moon Mill yard, glass ink bottle`
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
| 1 | 25043 | n/a | 0.8466 |
| 2 | 25123 | n/a | 0.8379 |
| 3 | 24963 | n/a | 0.8297 |
| 4 | 25042 | n/a | 0.8270 |
| 5 | 25122 | n/a | 0.8183 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distractor-057: In document distractor-cloud-wharf-office-057, the verified archive note records Cloud Wharf office, canal route map. Case record id: distractor-057. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-057. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); canal route map (aliases: profile detail canal route map; canal route map at Cloud Wharf office). Supplemental citation 1 for distractor-057 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, basalt sketch. Case record id: distractor-097. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-097. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin). Supplemental citation 1 for distractor-097 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-moon-mill-yard-017::distractor-017: In document distractor-moon-mill-yard-017, the verified archive note records Moon Mill yard, glass ink bottle. Case record id: distractor-017. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-017. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); glass ink bottle (aliases: profile detail glass ink bottle; glass ink bottle at Moon Mill yard). Supplemental citation 1 for distractor-017 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-057. Scoped answer summary for distractor-057 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); canal route map (aliases: profile detail canal route map; canal route map at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-057::distractor-057: In document distractor-cloud-wharf-office-057, the verified archive note records Cloud Wharf office, canal route map. Case record id: distractor-057. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-057. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); canal route map (aliases: profile detail canal route map; canal route map at Cloud Wharf office).
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summary for distractor-097 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, basalt sketch. Case record id: distractor-097. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-097. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin).
```

## Question 018: distractor-018

**Question:** Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24020 | n/a | 0.8920 |
| 2 | 24165 | n/a | 0.8858 |

Chunk rank 1:

```text
document distractor-winter-chapel-porch-018::distractor-018: In document distractor-winter-chapel-porch-018, the verified archive note records copper wind vane pin, Daria of Winter Chapel porch. Case record id: distractor-018. Question: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-018. Alias reminders for retrieval: copper wind vane pin (aliases: true object copper wind vane pin; copper wind vane pin in Daria's archive scene); Daria of Winter Chapel porch (aliases: Daria from Winter Chapel porch; Winter Chapel porch scene of Daria).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-018::distractor-018: In document distractor-winter-chapel-porch-018, the verified archive note records copper wind vane pin, Daria of Winter Chapel porch. Case record id: distractor-018. Question: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-018. Alias reminders for retrieval: copper wind vane pin (aliases: true object copper wind vane pin; copper wind vane pin in Daria's archive scene); Daria of Winter Chapel porch (aliases: Daria from Winter Chapel porch; Winter Chapel porch scene of Daria). Supplemental citation 1 for distractor-018 repeats the verified marker set: copper wind vane pin, true object copper wind vane pin, copper wind vane pin in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Daria of Winter Chapel porch, copper wind vane pin`
- Missing: `none`
- Forbidden hits: `carved shell comb`
- Distractor hits: `carved shell comb`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 3.; Forbidden markers found: carved shell comb`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24965 | n/a | 0.8676 |
| 2 | 24964 | n/a | 0.8638 |
| 3 | 24820 | n/a | 0.8635 |
| 4 | 24823 | n/a | 0.8503 |
| 5 | 25045 | n/a | 0.8486 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-018::distractor-018: In document distractor-winter-chapel-porch-018, the verified archive note records copper wind vane pin, Daria of Winter Chapel porch. Case record id: distractor-018. Question: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-018. Alias reminders for retrieval: copper wind vane pin (aliases: true object copper wind vane pin; copper wind vane pin in Daria's archive scene); Daria of Winter Chapel porch (aliases: Daria from Winter Chapel porch; Winter Chapel porch scene of Daria). Supplemental citation 1 for distractor-018 repeats the verified marker set: copper wind vane pin, true object copper wind vane pin, copper wind vane pin in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-018. Scoped answer summary for distractor-018 repeats the grounded evidence set: copper wind vane pin (aliases: true object copper wind vane pin; copper wind vane pin in Daria's archive scene); Daria of Winter Chapel porch (aliases: Daria from Winter Chapel porch; Winter Chapel porch scene of Daria). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-018::distractor-018: In document distractor-winter-chapel-porch-018, the verified archive note records copper wind vane pin, Daria of Winter Chapel porch. Case record id: distractor-018. Question: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-018. Alias reminders for retrieval: copper wind vane pin (aliases: true object copper wind vane pin; coppe

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-winter-chapel-porch-018::distractor-018: In document distractor-winter-chapel-porch-018, the verified archive note records copper wind vane pin, Daria of Winter Chapel porch. Case record id: distractor-018. Question: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-018. Alias reminders for retrieval: copper wind vane pin (aliases: true object copper wind vane pin; copper wind vane pin in Daria's archive scene); Daria of Winter Chapel porch (aliases: Daria from Winter Chapel porch; Winter Chapel porch scene of Daria).
```

Chunk rank 4:

```text
document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor).
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of Ridge Post loft. Case record id: distractor-058. Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-058. Alias reminders for retrieval: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria). Supplemental citation 1 for distractor-058 repeats the verified marker set: cedar shovel, true object cedar shovel, cedar shovel in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 019: distractor-019

**Question:** Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24167 | n/a | 0.9019 |
| 2 | 23969 | n/a | 0.8980 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-019::distractor-019: In document distractor-marble-stair-hall-019, the verified archive note records Signal Lantern Morning at Marble stair hall, coal stove hiss. Case record id: distractor-019. Question: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-019. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); coal stove hiss (aliases: event detail coal stove hiss; coal stove hiss in the correct event). Supplemental citation 1 for distractor-019 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-marble-stair-hall-019::distractor-019: In document distractor-marble-stair-hall-019, the verified archive note records Signal Lantern Morning at Marble stair hall, coal stove hiss. Case record id: distractor-019. Question: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-019. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); coal stove hiss (aliases: event detail coal stove hiss; coal stove hiss in the correct event).
```

### Model: multilingual_e5_large

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
| 1 | 24967 | n/a | 0.9018 |
| 2 | 24966 | n/a | 0.8985 |
| 3 | 24769 | n/a | 0.8828 |
| 4 | 25116 | n/a | 0.8822 |
| 5 | 25117 | n/a | 0.8808 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-019::distractor-019: In document distractor-marble-stair-hall-019, the verified archive note records Signal Lantern Morning at Marble stair hall, coal stove hiss. Case record id: distractor-019. Question: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-019. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); coal stove hiss (aliases: event detail coal stove hiss; coal stove hiss in the correct event). Supplemental citation 1 for distractor-019 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-019. Scoped answer summary for distractor-019 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); coal stove hiss (aliases: event detail coal stove hiss; coal stove hiss in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-019::distractor-019: In document distractor-marble-stair-hall-019, the verified archive note records Signal Lantern Morning at Marble stair hall, coal stove hiss. Case record id: distractor-019. Question: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-019. Alias reminders for retrieval: Signal Lantern Morning at Marble sta

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-marble-stair-hall-019::distractor-019: In document distractor-marble-stair-hall-019, the verified archive note records Signal Lantern Morning at Marble stair hall, coal stove hiss. Case record id: distractor-019. Question: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-019. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); coal stove hiss (aliases: event detail coal stove hiss; coal stove hiss in the correct event).
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-094. Scoped answer summary for distractor-094 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event). Supplemental citation 1 for distractor-094 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 020: distractor-020

**Question:** Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24169 | n/a | 0.9030 |
| 2 | 24008 | n/a | 0.8947 |

Chunk rank 1:

```text
Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basin gallery, violet ribbon. Case record id: distractor-020. Question: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Scope reminder: document distractor-star-basin-gallery-020. Alias reminders for retrieval: Ada of Star Basin gallery (aliases: Ada from Star Basin gallery; Star Basin gallery Ada); violet ribbon (aliases: correct object violet ribbon; violet ribbon in the true note). Supplemental citation 1 for distractor-020 repeats the verified marker set: Ada of Star Basin gallery, Ada from Star Basin gallery, Star Basin gallery Ada. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basin gallery, violet ribbon. Case record id: distractor-020. Question: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Scope reminder: document distractor-star-basin-gallery-020. Alias reminders for retrieval: Ada of Star Basin gallery (aliases: Ada from Star Basin gallery; Star Basin gallery Ada); violet ribbon (aliases: correct object violet ribbon; violet ribbon in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 24968 | n/a | 0.8811 |
| 2 | 24969 | n/a | 0.8800 |
| 3 | 24808 | n/a | 0.8679 |
| 4 | 24999 | n/a | 0.8377 |
| 5 | 24998 | n/a | 0.8369 |

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

Chunk rank 4:

```text
Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note). Supplemental citation 1 for distractor-035 repeats the verified marker set: Pavel of Star Basin gallery, Pavel from Star Basin gallery, Star Basin gallery Pavel. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Case scope id: distractor-035. Scoped answer summary for distractor-035 repeats the grounded evidence set: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note).
```

## Question 021: distractor-021

**Question:** Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24291 | n/a | 0.8980 |
| 2 | 24171 | n/a | 0.8961 |
| 3 | 24231 | n/a | 0.8948 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellwater Fair, North Bell workshop. Case record id: distractor-081. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-081. Alias reminders for retrieval: March 19 Bellwater Fair (aliases: Bellwater Fair on March 19; memory dated March 19); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-081 repeats the verified marker set: March 19 Bellwater Fair, Bellwater Fair on March 19, memory dated March 19. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-051::distractor-051: In document distractor-north-bell-workshop-051, the verified archive note records March 25 Bellwater Fair, North Bell workshop. Case record id: distractor-051. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-051. Alias reminders for retrieval: March 25 Bellwater Fair (aliases: Bellwater Fair on March 25; memory dated March 25); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-051 repeats the verified marker set: March 25 Bellwater Fair, Bellwater Fair on March 25, memory dated March 25. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `North Bell workshop`
- Missing: `March 13 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 5.; Missing expected markers: March 13 Bellwater Fair; Evidence coverage below requirement: 0.500 < 1.000.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 25001 | n/a | 0.8858 |
| 2 | 25061 | n/a | 0.8847 |
| 3 | 25121 | n/a | 0.8845 |
| 4 | 25060 | n/a | 0.8840 |
| 5 | 24941 | n/a | 0.8835 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-096 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. Scoped answer summary for distractor-066 repeats the grounded evidence set: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 022: distractor-022

**Question:** Which place held the true profile detail for Talia, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, rope bridge permit`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `partial`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24253 | n/a | 0.8517 |
| 2 | 24173 | n/a | 0.8452 |
| 3 | 23978 | n/a | 0.8412 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-moon-mill-yard-062::distractor-062: In document distractor-moon-mill-yard-062, the verified archive note records Moon Mill yard, saffron scarf. Case record id: distractor-062. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-062. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); saffron scarf (aliases: profile detail saffron scarf; saffron scarf at Moon Mill yard). Supplemental citation 1 for distractor-062 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distractor-022: In document distractor-blue-trunk-cabin-022, the verified archive note records Blue Trunk cabin, rope bridge permit. Case record id: distractor-022. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-022. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); rope bridge permit (aliases: profile detail rope bridge permit; rope bridge permit at Blue Trunk cabin). Supplemental citation 1 for distractor-022 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-moon-mill-yard-062::distractor-062: In document distractor-moon-mill-yard-062, the verified archive note records Moon Mill yard, saffron scarf. Case record id: distractor-062. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-062. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); saffron scarf (aliases: profile detail saffron scarf; saffron scarf at Moon Mill yard).
```

### Model: multilingual_e5_large

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, rope bridge permit`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24973 | n/a | 0.8338 |
| 2 | 25053 | n/a | 0.8300 |
| 3 | 25052 | n/a | 0.8163 |
| 4 | 24972 | n/a | 0.8141 |
| 5 | 24909 | n/a | 0.8019 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distractor-022: In document distractor-blue-trunk-cabin-022, the verified archive note records Blue Trunk cabin, rope bridge permit. Case record id: distractor-022. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-022. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); rope bridge permit (aliases: profile detail rope bridge permit; rope bridge permit at Blue Trunk cabin). Supplemental citation 1 for distractor-022 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-moon-mill-yard-062::distractor-062: In document distractor-moon-mill-yard-062, the verified archive note records Moon Mill yard, saffron scarf. Case record id: distractor-062. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-062. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); saffron scarf (aliases: profile detail saffron scarf; saffron scarf at Moon Mill yard). Supplemental citation 1 for distractor-062 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? Case scope id: distractor-062. Scoped answer summary for distractor-062 repeats the grounded evidence set: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); saffron scarf (aliases: profile detail saffron scarf; saffron scarf at Moon Mill yard). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-moon-mill-yard-062::distractor-062: In document distractor-moon-mill-yard-062, the verified archive note records Moon Mill yard, saffron scarf. Case record id: distractor-062. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-062. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); saffron scarf (aliases: profile detail saffron scarf; saffron scarf at Moon Mill yard).
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? Case scope id: distractor-022. Scoped answer summary for distractor-022 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); rope bridge permit (aliases: profile detail rope bridge permit; rope bridge permit at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-022::distractor-022: In document distractor-blue-trunk-cabin-022, the verified archive note records Blue Trunk cabin, rope bridge permit. Case record id: distractor-022. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-022. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); rope bridge permit (aliases: profile detail rope bridge permit; rope bridge permit at Blue Trunk cabin).
```

Chunk rank 5:

```text
document distractor-star-basin-gallery-035::distractor-035::distractor: A conflicting note in document distractor-star-basin-gallery-035 mentions Talia of Star Basin gallery (aliases: Talia from Star Basin gallery; Star Basin gallery Talia) as a misleading archival rumor. That rumor is explicitly different from the verified record for this source scope. Conflict marker only: Talia of Star Basin gallery remains archival noise.
```

## Question 023: distractor-023

**Question:** Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 23989 | n/a | 0.8913 |
| 2 | 24175 | n/a | 0.8874 |
| 3 | 24174 | n/a | 0.8849 |

Chunk rank 1:

```text
document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor). Supplemental citation 1 for distractor-023 repeats the verified marker set: oak barrel hoops, true object oak barrel hoops, oak barrel hoops in Viktor's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-023. Scoped answer summary for distractor-023 repeats the grounded evidence set: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's ar

[truncated in Markdown; full text is available in JSON]
```

### Model: multilingual_e5_large

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
| 1 | 24975 | n/a | 0.8670 |
| 2 | 24789 | n/a | 0.8636 |
| 3 | 24974 | n/a | 0.8579 |
| 4 | 24823 | n/a | 0.8423 |
| 5 | 25125 | n/a | 0.8409 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor). Supplemental citation 1 for distractor-023 repeats the verified marker set: oak barrel hoops, true object oak barrel hoops, oak barrel hoops in Viktor's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor).
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-023. Scoped answer summary for distractor-023 repeats the grounded evidence set: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's ar

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 4:

```text
document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor).
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Daria of North Orchard lane. Case record id: distractor-098. Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-098. Alias reminders for retrieval: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria). Supplemental citation 1 for distractor-098 repeats the verified marker set: green apron, true object green apron, green apron in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 024: distractor-024

**Question:** Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24002 | n/a | 0.8994 |
| 2 | 24177 | n/a | 0.8954 |
| 3 | 24006 | n/a | 0.8870 |

Chunk rank 1:

```text
document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Morning at South Meadow arch, blue glass jar. Case record id: distractor-024. Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-024. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); blue glass jar (aliases: event detail blue glass jar; blue glass jar in the correct event).
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Morning at South Meadow arch, blue glass jar. Case record id: distractor-024. Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-024. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); blue glass jar (aliases: event detail blue glass jar; blue glass jar in the correct event). Supplemental citation 1 for distractor-024 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Morning at South Meadow arch, violet ribbon. Case record id: distractor-084. Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-084. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); violet ribbon (aliases: event detail violet ribbon; violet ribbon in the correct event).
```

### Model: multilingual_e5_large

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
| 1 | 24977 | n/a | 0.8986 |
| 2 | 24976 | n/a | 0.8929 |
| 3 | 25097 | n/a | 0.8738 |
| 4 | 24802 | n/a | 0.8727 |
| 5 | 25007 | n/a | 0.8685 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Morning at South Meadow arch, blue glass jar. Case record id: distractor-024. Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-024. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); blue glass jar (aliases: event detail blue glass jar; blue glass jar in the correct event). Supplemental citation 1 for distractor-024 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-024. Scoped answer summary for distractor-024 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); blue glass jar (aliases: event detail blue glass jar; blue glass jar in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Morning at South Meadow arch, blue glass jar. Case record id: distractor-024. Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-024. Alias reminders for retrieval: Signal Lantern Morning at South Meadow

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Morning at South Meadow arch, violet ribbon. Case record id: distractor-084. Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-084. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); violet ribbon (aliases: event detail violet ribbon; violet ribbon in the correct event). Supplemental citation 1 for distractor-084 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Morning at South Meadow arch, blue glass jar. Case record id: distractor-024. Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-024. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); blue glass jar (aliases: event detail blue glass jar; blue glass jar in the correct event).
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-039::distractor-039: In document distractor-south-meadow-arch-039, the verified archive note records Signal Lantern Morning at South Meadow arch, brass compass. Case record id: distractor-039. Question: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-039. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); brass compass (aliases: event detail brass compass; brass compass in the correct event). Supplemental citation 1 for distractor-039 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 025: distractor-025

**Question:** Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24179 | n/a | 0.9058 |
| 2 | 24178 | n/a | 0.8972 |
| 3 | 23938 | n/a | 0.8920 |

Chunk rank 1:

```text
Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry shed, canal route map. Case record id: distractor-025. Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Scope reminder: document distractor-birch-ferry-shed-025. Alias reminders for retrieval: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note). Supplemental citation 1 for distractor-025 repeats the verified marker set: Anton of Birch Ferry shed, Anton from Birch Ferry shed, Birch Ferry shed Anton. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Case scope id: distractor-025. Scoped answer summary for distractor-025 repeats the grounded evidence set: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry shed, canal route map. Case record id: distractor-025. Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Scope reminder: document distractor-birch-ferry-shed-025. Alias reminders for retrieval: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note).
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry shed, canal route map. Case record id: distractor-025. Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Scope reminder: document distractor-birch-ferry-shed-025. Alias reminders for retrieval: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 24979 | n/a | 0.8865 |
| 2 | 24978 | n/a | 0.8749 |
| 3 | 24738 | n/a | 0.8648 |
| 4 | 25069 | n/a | 0.8326 |
| 5 | 25099 | n/a | 0.8311 |

Chunk rank 1:

```text
Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry shed, canal route map. Case record id: distractor-025. Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Scope reminder: document distractor-birch-ferry-shed-025. Alias reminders for retrieval: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note). Supplemental citation 1 for distractor-025 repeats the verified marker set: Anton of Birch Ferry shed, Anton from Birch Ferry shed, Birch Ferry shed Anton. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Case scope id: distractor-025. Scoped answer summary for distractor-025 repeats the grounded evidence set: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry shed, canal route map. Case record id: distractor-025. Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Scope reminder: document distractor-birch-ferry-shed-025. Alias reminders for retrieval: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note).
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry shed, canal route map. Case record id: distractor-025. Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Scope reminder: document distractor-birch-ferry-shed-025. Alias reminders for retrieval: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry shed, smoke vent chain. Case record id: distractor-070. Question: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Scope reminder: document distractor-birch-ferry-shed-070. Alias reminders for retrieval: Lina of Birch Ferry shed (aliases: Lina from Birch Ferry shed; Birch Ferry shed Lina); smoke vent chain (aliases: correct object smoke vent chain; smoke vent chain in the true note). Supplemental citation 1 for distractor-070 repeats the verified marker set: Lina of Birch Ferry shed, Lina from Birch Ferry shed, Birch Ferry shed Lina. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? document distractor-birch-ferry-shed-085::distractor-085: In document distractor-birch-ferry-shed-085, the verified archive note records Stefan of Birch Ferry shed, tuning fork. Case record id: distractor-085. Question: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Scope reminder: document distractor-birch-ferry-shed-085. Alias reminders for retrieval: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note). Supplemental citation 1 for distractor-085 repeats the verified marker set: Stefan of Birch Ferry shed, Stefan from Birch Ferry shed, Birch Ferry shed Stefan. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 026: distractor-026

**Question:** Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `Lantern Row kiosk`
- Missing: `March 18 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Missing expected evidence: March 18 Bellwater Fair`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24271 | n/a | 0.9048 |
| 2 | 24151 | n/a | 0.9042 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 24981 | n/a | 0.8932 |
| 2 | 25101 | n/a | 0.8931 |
| 3 | 25011 | n/a | 0.8931 |
| 4 | 25041 | n/a | 0.8926 |
| 5 | 24951 | n/a | 0.8922 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-041 repeats the verified marker set: March 15 Bellwater Fair, Bellwater Fair on March 15, memory dated March 15. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-056::distractor-056: In document distractor-lantern-row-kiosk-056, the verified archive note records March 12 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-056. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-056. Alias reminders for retrieval: March 12 Bellwater Fair (aliases: Bellwater Fair on March 12; memory dated March 12); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-056 repeats the verified marker set: March 12 Bellwater Fair, Bellwater Fair on March 12, memory dated March 12. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 027: distractor-027

**Question:** Which place held the true profile detail for Tomas, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, copper token`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `partial`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24263 | n/a | 0.8494 |
| 2 | 24183 | n/a | 0.8485 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distractor-067: In document distractor-blue-trunk-cabin-067, the verified archive note records Blue Trunk cabin, silver booth token. Case record id: distractor-067. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-067. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); silver booth token (aliases: profile detail silver booth token; silver booth token at Blue Trunk cabin). Supplemental citation 1 for distractor-067 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-cloud-wharf-office-027::distractor-027: In document distractor-cloud-wharf-office-027, the verified archive note records Cloud Wharf office, copper token. Case record id: distractor-027. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-027. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); copper token (aliases: profile detail copper token; copper token at Cloud Wharf office). Supplemental citation 1 for distractor-027 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, copper token`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24983 | n/a | 0.8204 |
| 2 | 25063 | n/a | 0.8114 |
| 3 | 24982 | n/a | 0.8009 |
| 4 | 25062 | n/a | 0.7938 |
| 5 | 25043 | n/a | 0.7937 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-cloud-wharf-office-027::distractor-027: In document distractor-cloud-wharf-office-027, the verified archive note records Cloud Wharf office, copper token. Case record id: distractor-027. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-027. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); copper token (aliases: profile detail copper token; copper token at Cloud Wharf office). Supplemental citation 1 for distractor-027 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distractor-067: In document distractor-blue-trunk-cabin-067, the verified archive note records Blue Trunk cabin, silver booth token. Case record id: distractor-067. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-067. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); silver booth token (aliases: profile detail silver booth token; silver booth token at Blue Trunk cabin). Supplemental citation 1 for distractor-067 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-027. Scoped answer summary for distractor-027 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); copper token (aliases: profile detail copper token; copper token at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-027::distractor-027: In document distractor-cloud-wharf-office-027, the verified archive note records Cloud Wharf office, copper token. Case record id: distractor-027. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-027. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); copper token (aliases: profile detail copper token; copper token at Cloud Wharf office).
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-067. Scoped answer summary for distractor-067 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); silver booth token (aliases: profile detail silver booth token; silver booth token at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-067::distractor-067: In document distractor-blue-trunk-cabin-067, the verified archive note records Blue Trunk cabin, silver booth token. Case record id: distractor-067. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-067. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); silver booth token (aliases: profile detail silver booth token; silver booth token at Blue Trunk cabin).
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distractor-057: In document distractor-cloud-wharf-office-057, the verified archive note records Cloud Wharf office, canal route map. Case record id: distractor-057. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-057. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); canal route map (aliases: profile detail canal route map; canal route map at Cloud Wharf office). Supplemental citation 1 for distractor-057 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 028: distractor-028

**Question:** Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24185 | n/a | 0.8780 |
| 2 | 24184 | n/a | 0.8739 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-028::distractor-028: In document distractor-ridge-post-loft-028, the verified archive note records moonflower cutting, Vera of Ridge Post loft. Case record id: distractor-028. Question: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-028. Alias reminders for retrieval: moonflower cutting (aliases: true object moonflower cutting; moonflower cutting in Vera's archive scene); Vera of Ridge Post loft (aliases: Vera from Ridge Post loft; Ridge Post loft scene of Vera). Supplemental citation 1 for distractor-028 repeats the verified marker set: moonflower cutting, true object moonflower cutting, moonflower cutting in Vera's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-028. Scoped answer summary for distractor-028 repeats the grounded evidence set: moonflower cutting (aliases: true object moonflower cutting; moonflower cutting in Vera's archive scene); Vera of Ridge Post loft (aliases: Vera from Ridge Post loft; Ridge Post loft scene of Vera). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-028::distractor-028: In document distractor-ridge-post-loft-028, the verified archive note records moonflower cutting, Vera of Ridge Post loft. Case record id: distractor-028. Question: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-028. Alias reminders for retrieval: moonflower cutting (aliases: true object moonflower cutting; moonflower cutting in Vera's archive scene); Vera of Ridge Post loft (aliases: Vera from Ridge Post loft; Ridge Post loft scene of Vera).
```

### Model: multilingual_e5_large

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Vera of Ridge Post loft, moonflower cutting`
- Missing: `none`
- Forbidden hits: `star ledger page`
- Distractor hits: `star ledger page`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 2.; Forbidden markers found: star ledger page`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24985 | n/a | 0.8610 |
| 2 | 25075 | n/a | 0.8600 |
| 3 | 24955 | n/a | 0.8568 |
| 4 | 24796 | n/a | 0.8566 |
| 5 | 25045 | n/a | 0.8509 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-028::distractor-028: In document distractor-ridge-post-loft-028, the verified archive note records moonflower cutting, Vera of Ridge Post loft. Case record id: distractor-028. Question: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-028. Alias reminders for retrieval: moonflower cutting (aliases: true object moonflower cutting; moonflower cutting in Vera's archive scene); Vera of Ridge Post loft (aliases: Vera from Ridge Post loft; Ridge Post loft scene of Vera). Supplemental citation 1 for distractor-028 repeats the verified marker set: moonflower cutting, true object moonflower cutting, moonflower cutting in Vera's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev). Supplemental citation 1 for distractor-073 repeats the verified marker set: star ledger page, true object star ledger page, star ledger page in Lev's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna). Supplemental citation 1 for distractor-013 repeats the verified marker set: tin key, true object tin key, tin key in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
document distractor-ridge-post-loft-028::distractor-028: In document distractor-ridge-post-loft-028, the verified archive note records moonflower cutting, Vera of Ridge Post loft. Case record id: distractor-028. Question: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-028. Alias reminders for retrieval: moonflower cutting (aliases: true object moonflower cutting; moonflower cutting in Vera's archive scene); Vera of Ridge Post loft (aliases: Vera from Ridge Post loft; Ridge Post loft scene of Vera).
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of Ridge Post loft. Case record id: distractor-058. Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-058. Alias reminders for retrieval: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria). Supplemental citation 1 for distractor-058 repeats the verified marker set: cedar shovel, true object cedar shovel, cedar shovel in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 029: distractor-029

**Question:** Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24015 | n/a | 0.8973 |
| 2 | 24017 | n/a | 0.8938 |
| 3 | 24247 | n/a | 0.8879 |

Chunk rank 1:

```text
document distractor-willow-courtyard-well-029::distractor-029: In document distractor-willow-courtyard-well-029, the verified archive note records Signal Lantern Morning at Willow Courtyard well, birch tea flask. Case record id: distractor-029. Question: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-029. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); birch tea flask (aliases: event detail birch tea flask; birch tea flask in the correct event).
```

Chunk rank 2:

```text
document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event).
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event). Supplemental citation 1 for distractor-059 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting c

[truncated in Markdown; full text is available in JSON]
```

### Model: multilingual_e5_large

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
| 1 | 24986 | n/a | 0.8990 |
| 2 | 24987 | n/a | 0.8960 |
| 3 | 24815 | n/a | 0.8814 |
| 4 | 25046 | n/a | 0.8745 |
| 5 | 25047 | n/a | 0.8729 |

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

Chunk rank 3:

```text
document distractor-willow-courtyard-well-029::distractor-029: In document distractor-willow-courtyard-well-029, the verified archive note records Signal Lantern Morning at Willow Courtyard well, birch tea flask. Case record id: distractor-029. Question: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-029. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); birch tea flask (aliases: event detail birch tea flask; birch tea flask in the correct event).
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-059. Scoped answer summary for distractor-059 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lante

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event). Supplemental citation 1 for distractor-059 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting c

[truncated in Markdown; full text is available in JSON]
```

## Question 030: distractor-030

**Question:** Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24189 | n/a | 0.8824 |
| 2 | 23932 | n/a | 0.8748 |
| 3 | 24188 | n/a | 0.8661 |

Chunk rank 1:

```text
Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bridge square, saffron scarf. Case record id: distractor-030. Question: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Scope reminder: document distractor-bell-bridge-square-030. Alias reminders for retrieval: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note). Supplemental citation 1 for distractor-030 repeats the verified marker set: Lina of Bell Bridge square, Lina from Bell Bridge square, Bell Bridge square Lina. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bridge square, saffron scarf. Case record id: distractor-030. Question: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Scope reminder: document distractor-bell-bridge-square-030. Alias reminders for retrieval: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note).
```

Chunk rank 3:

```text
Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Case scope id: distractor-030. Scoped answer summary for distractor-030 repeats the grounded evidence set: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bridge square, saffron scarf. Case record id: distractor-030. Question: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Scope reminder: document distractor-bell-bridge-square-030. Alias reminders for retrieval: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 24989 | n/a | 0.8692 |
| 2 | 24988 | n/a | 0.8623 |
| 3 | 24732 | n/a | 0.8452 |
| 4 | 24959 | n/a | 0.8374 |
| 5 | 24958 | n/a | 0.8342 |

Chunk rank 1:

```text
Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bridge square, saffron scarf. Case record id: distractor-030. Question: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Scope reminder: document distractor-bell-bridge-square-030. Alias reminders for retrieval: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note). Supplemental citation 1 for distractor-030 repeats the verified marker set: Lina of Bell Bridge square, Lina from Bell Bridge square, Bell Bridge square Lina. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Case scope id: distractor-030. Scoped answer summary for distractor-030 repeats the grounded evidence set: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bridge square, saffron scarf. Case record id: distractor-030. Question: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Scope reminder: document distractor-bell-bridge-square-030. Alias reminders for retrieval: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note).
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bridge square, saffron scarf. Case record id: distractor-030. Question: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Scope reminder: document distractor-bell-bridge-square-030. Alias reminders for retrieval: Lina of Bell Bridge square (aliases: Lina from Bell Bridge square; Bell Bridge square Lina); saffron scarf (aliases: correct object saffron scarf; saffron scarf in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). Supplemental citation 1 for distractor-015 repeats the verified marker set: Ilya of Bell Bridge square, Ilya from Bell Bridge square, Bell Bridge square Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer summary for distractor-015 repeats the grounded evidence set: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note).
```

## Question 031: distractor-031

**Question:** Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `Cedar Hill station`
- Missing: `March 23 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Missing expected evidence: March 23 Bellwater Fair`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24161 | n/a | 0.9059 |
| 2 | 24251 | n/a | 0.9051 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwater Fair, Cedar Hill station. Case record id: distractor-016. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-016. Alias reminders for retrieval: March 26 Bellwater Fair (aliases: Bellwater Fair on March 26; memory dated March 26); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-016 repeats the verified marker set: March 26 Bellwater Fair, Bellwater Fair on March 26, memory dated March 26. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25081 | n/a | 0.8963 |
| 2 | 24990 | n/a | 0.8954 |
| 3 | 25050 | n/a | 0.8951 |
| 4 | 24991 | n/a | 0.8949 |
| 5 | 25080 | n/a | 0.8946 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwater Fair, Cedar Hill station. Case record id: distractor-076. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-076. Alias reminders for retrieval: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-076 repeats the verified marker set: March 14 Bellwater Fair, Bellwater Fair on March 14, memory dated March 14. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-031. Scoped answer summary for distractor-031 repeats the grounded evidence set: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-061. Scoped answer summary for distractor-061 repeats the grounded evidence set: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-031 repeats the verified marker set: March 23 Bellwater Fair, Bellwater Fair on March 23, memory dated March 23. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-076. Scoped answer summary for distractor-076 repeats the grounded evidence set: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwater Fair, Cedar Hill station. Case record id: distractor-076. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-076. Alias reminders for retrieval: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

## Question 032: distractor-032

**Question:** Which place held the true profile detail for Yara, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Mill yard, amber lantern`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24273 | n/a | 0.8616 |
| 2 | 24193 | n/a | 0.8601 |
| 3 | 24192 | n/a | 0.8546 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-cloud-wharf-office-072::distractor-072: In document distractor-cloud-wharf-office-072, the verified archive note records Cloud Wharf office, linen wick. Case record id: distractor-072. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-072. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); linen wick (aliases: profile detail linen wick; linen wick at Cloud Wharf office). Supplemental citation 1 for distractor-072 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-moon-mill-yard-032::distractor-032: In document distractor-moon-mill-yard-032, the verified archive note records Moon Mill yard, amber lantern. Case record id: distractor-032. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-032. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); amber lantern (aliases: profile detail amber lantern; amber lantern at Moon Mill yard). Supplemental citation 1 for distractor-032 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-032. Scoped answer summary for distractor-032 repeats the grounded evidence set: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); amber lantern (aliases: profile detail amber lantern; amber lantern at Moon Mill yard). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-moon-mill-yard-032::distractor-032: In document distractor-moon-mill-yard-032, the verified archive note records Moon Mill yard, amber lantern. Case record id: distractor-032. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-032. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); amber lantern (aliases: profile detail amber lantern; amber lantern at Moon Mill yard).
```

### Model: multilingual_e5_large

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Mill yard, amber lantern`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24993 | n/a | 0.8314 |
| 2 | 25073 | n/a | 0.8262 |
| 3 | 25072 | n/a | 0.8150 |
| 4 | 24992 | n/a | 0.8096 |
| 5 | 25053 | n/a | 0.8083 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-moon-mill-yard-032::distractor-032: In document distractor-moon-mill-yard-032, the verified archive note records Moon Mill yard, amber lantern. Case record id: distractor-032. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-032. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); amber lantern (aliases: profile detail amber lantern; amber lantern at Moon Mill yard). Supplemental citation 1 for distractor-032 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-cloud-wharf-office-072::distractor-072: In document distractor-cloud-wharf-office-072, the verified archive note records Cloud Wharf office, linen wick. Case record id: distractor-072. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-072. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); linen wick (aliases: profile detail linen wick; linen wick at Cloud Wharf office). Supplemental citation 1 for distractor-072 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-072. Scoped answer summary for distractor-072 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); linen wick (aliases: profile detail linen wick; linen wick at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-072::distractor-072: In document distractor-cloud-wharf-office-072, the verified archive note records Cloud Wharf office, linen wick. Case record id: distractor-072. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-072. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); linen wick (aliases: profile detail linen wick; linen wick at Cloud Wharf office).
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-032. Scoped answer summary for distractor-032 repeats the grounded evidence set: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); amber lantern (aliases: profile detail amber lantern; amber lantern at Moon Mill yard). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-moon-mill-yard-032::distractor-032: In document distractor-moon-mill-yard-032, the verified archive note records Moon Mill yard, amber lantern. Case record id: distractor-032. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-032. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); amber lantern (aliases: profile detail amber lantern; amber lantern at Moon Mill yard).
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-moon-mill-yard-062::distractor-062: In document distractor-moon-mill-yard-062, the verified archive note records Moon Mill yard, saffron scarf. Case record id: distractor-062. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-062. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); saffron scarf (aliases: profile detail saffron scarf; saffron scarf at Moon Mill yard). Supplemental citation 1 for distractor-062 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 033: distractor-033

**Question:** Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24195 | n/a | 0.8924 |
| 2 | 24021 | n/a | 0.8890 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch, Lev of Winter Chapel porch. Case record id: distractor-033. Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-033. Alias reminders for retrieval: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev). Supplemental citation 1 for distractor-033 repeats the verified marker set: basalt sketch, true object basalt sketch, basalt sketch in Lev's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch, Lev of Winter Chapel porch. Case record id: distractor-033. Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-033. Alias reminders for retrieval: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev).
```

### Model: multilingual_e5_large

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
| 1 | 24995 | n/a | 0.8681 |
| 2 | 24821 | n/a | 0.8633 |
| 3 | 24994 | n/a | 0.8618 |
| 4 | 25075 | n/a | 0.8487 |
| 5 | 24823 | n/a | 0.8455 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch, Lev of Winter Chapel porch. Case record id: distractor-033. Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-033. Alias reminders for retrieval: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev). Supplemental citation 1 for distractor-033 repeats the verified marker set: basalt sketch, true object basalt sketch, basalt sketch in Lev's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch, Lev of Winter Chapel porch. Case record id: distractor-033. Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-033. Alias reminders for retrieval: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev).
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-033. Scoped answer summary for distractor-033 repeats the grounded evidence set: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch, Lev of Winter Chapel porch. Case record id: distractor-033. Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-033. Alias reminders for retrieval: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev).
```

Chunk rank 4:

```text
Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev). Supplemental citation 1 for distractor-073 repeats the verified marker set: star ledger page, true object star ledger page, star ledger page in Lev's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor).
```

## Question 034: distractor-034

**Question:** Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24197 | n/a | 0.8996 |
| 2 | 23970 | n/a | 0.8938 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Morning at Marble stair hall, green apron. Case record id: distractor-034. Question: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-034. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); green apron (aliases: event detail green apron; green apron in the correct event). Supplemental citation 1 for distractor-034 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Morning at Marble stair hall, green apron. Case record id: distractor-034. Question: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-034. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); green apron (aliases: event detail green apron; green apron in the correct event).
```

### Model: multilingual_e5_large

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
| 1 | 24997 | n/a | 0.9028 |
| 2 | 24996 | n/a | 0.8972 |
| 3 | 25116 | n/a | 0.8816 |
| 4 | 25117 | n/a | 0.8813 |
| 5 | 24770 | n/a | 0.8802 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Morning at Marble stair hall, green apron. Case record id: distractor-034. Question: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-034. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); green apron (aliases: event detail green apron; green apron in the correct event). Supplemental citation 1 for distractor-034 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-034. Scoped answer summary for distractor-034 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); green apron (aliases: event detail green apron; green apron in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Morning at Marble stair hall, green apron. Case record id: distractor-034. Question: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-034. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (alias

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-094. Scoped answer summary for distractor-094 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event). Supplemental citation 1 for distractor-094 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Morning at Marble stair hall, green apron. Case record id: distractor-034. Question: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-034. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); green apron (aliases: event detail green apron; green apron in the correct event).
```

## Question 035: distractor-035

**Question:** Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24199 | n/a | 0.8955 |
| 2 | 24009 | n/a | 0.8888 |

Chunk rank 1:

```text
Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note). Supplemental citation 1 for distractor-035 repeats the verified marker set: Pavel of Star Basin gallery, Pavel from Star Basin gallery, Star Basin gallery Pavel. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 24999 | n/a | 0.8771 |
| 2 | 24998 | n/a | 0.8698 |
| 3 | 24809 | n/a | 0.8576 |
| 4 | 25059 | n/a | 0.8208 |
| 5 | 25079 | n/a | 0.8178 |

Chunk rank 1:

```text
Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note). Supplemental citation 1 for distractor-035 repeats the verified marker set: Pavel of Star Basin gallery, Pavel from Star Basin gallery, Star Basin gallery Pavel. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Case scope id: distractor-035. Scoped answer summary for distractor-035 repeats the grounded evidence set: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note).
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Basin gallery, basalt sketch. Case record id: distractor-065. Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Scope reminder: document distractor-star-basin-gallery-065. Alias reminders for retrieval: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note). Supplemental citation 1 for distractor-065 repeats the verified marker set: Anton of Star Basin gallery, Anton from Star Basin gallery, Star Basin gallery Anton. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Bridge square, weathered camera strap. Case record id: distractor-075. Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Scope reminder: document distractor-bell-bridge-square-075. Alias reminders for retrieval: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (aliases: correct object weathered camera strap; weathered camera strap in the true note). Supplemental citation 1 for distractor-075 repeats the verified marker set: Pavel of Bell Bridge square, Pavel from Bell Bridge square, Bell Bridge square Pavel. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 036: distractor-036

**Question:** Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `North Bell workshop`
- Missing: `March 10 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Missing expected evidence: March 10 Bellwater Fair`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24291 | n/a | 0.8980 |
| 2 | 24171 | n/a | 0.8961 |
| 3 | 24231 | n/a | 0.8948 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellwater Fair, North Bell workshop. Case record id: distractor-081. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-081. Alias reminders for retrieval: March 19 Bellwater Fair (aliases: Bellwater Fair on March 19; memory dated March 19); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-081 repeats the verified marker set: March 19 Bellwater Fair, Bellwater Fair on March 19, memory dated March 19. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-051::distractor-051: In document distractor-north-bell-workshop-051, the verified archive note records March 25 Bellwater Fair, North Bell workshop. Case record id: distractor-051. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-051. Alias reminders for retrieval: March 25 Bellwater Fair (aliases: Bellwater Fair on March 25; memory dated March 25); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-051 repeats the verified marker set: March 25 Bellwater Fair, Bellwater Fair on March 25, memory dated March 25. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25001 | n/a | 0.8858 |
| 2 | 25061 | n/a | 0.8847 |
| 3 | 25121 | n/a | 0.8845 |
| 4 | 25060 | n/a | 0.8840 |
| 5 | 24941 | n/a | 0.8835 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-096 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. Scoped answer summary for distractor-066 repeats the grounded evidence set: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 037: distractor-037

**Question:** Which place held the true profile detail for Damir, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, juniper bundles`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `partial`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24283 | n/a | 0.8621 |
| 2 | 24203 | n/a | 0.8592 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-moon-mill-yard-077::distractor-077: In document distractor-moon-mill-yard-077, the verified archive note records Moon Mill yard, tin key. Case record id: distractor-077. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-077. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); tin key (aliases: profile detail tin key; tin key at Moon Mill yard). Supplemental citation 1 for distractor-077 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-blue-trunk-cabin-037::distractor-037: In document distractor-blue-trunk-cabin-037, the verified archive note records Blue Trunk cabin, juniper bundles. Case record id: distractor-037. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-037. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin). Supplemental citation 1 for distractor-037 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25003 | n/a | 0.8211 |
| 2 | 25083 | n/a | 0.8146 |
| 3 | 25002 | n/a | 0.8075 |
| 4 | 25082 | n/a | 0.7998 |
| 5 | 24779 | n/a | 0.7921 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-blue-trunk-cabin-037::distractor-037: In document distractor-blue-trunk-cabin-037, the verified archive note records Blue Trunk cabin, juniper bundles. Case record id: distractor-037. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-037. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin). Supplemental citation 1 for distractor-037 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-moon-mill-yard-077::distractor-077: In document distractor-moon-mill-yard-077, the verified archive note records Moon Mill yard, tin key. Case record id: distractor-077. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-077. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); tin key (aliases: profile detail tin key; tin key at Moon Mill yard). Supplemental citation 1 for distractor-077 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-037. Scoped answer summary for distractor-037 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-037::distractor-037: In document distractor-blue-trunk-cabin-037, the verified archive note records Blue Trunk cabin, juniper bundles. Case record id: distractor-037. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-037. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin).
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-077. Scoped answer summary for distractor-077 repeats the grounded evidence set: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); tin key (aliases: profile detail tin key; tin key at Moon Mill yard). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-moon-mill-yard-077::distractor-077: In document distractor-moon-mill-yard-077, the verified archive note records Moon Mill yard, tin key. Case record id: distractor-077. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-077. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); tin key (aliases: profile detail tin key; tin key at Moon Mill yard).
```

Chunk rank 5:

```text
document distractor-moon-mill-yard-077::distractor-077: In document distractor-moon-mill-yard-077, the verified archive note records Moon Mill yard, tin key. Case record id: distractor-077. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-077. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); tin key (aliases: profile detail tin key; tin key at Moon Mill yard).
```

## Question 038: distractor-038

**Question:** Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24205 | n/a | 0.8791 |
| 2 | 23990 | n/a | 0.8788 |
| 3 | 24204 | n/a | 0.8734 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain, Nessa of North Orchard lane. Case record id: distractor-038. Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-038. Alias reminders for retrieval: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive scene); Nessa of North Orchard lane (aliases: Nessa from North Orchard lane; North Orchard lane scene of Nessa). Supplemental citation 1 for distractor-038 repeats the verified marker set: smoke vent chain, true object smoke vent chain, smoke vent chain in Nessa's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain, Nessa of North Orchard lane. Case record id: distractor-038. Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-038. Alias reminders for retrieval: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive scene); Nessa of North Orchard lane (aliases: Nessa from North Orchard lane; North Orchard lane scene of Nessa).
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-038. Scoped answer summary for distractor-038 repeats the grounded evidence set: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive scene); Nessa of North Orchard lane (aliases: Nessa from North Orchard lane; North Orchard lane scene of Nessa). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain, Nessa of North Orchard lane. Case record id: distractor-038. Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-038. Alias reminders for retrieval: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive sc

[truncated in Markdown; full text is available in JSON]
```

### Model: multilingual_e5_large

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
| 1 | 25005 | n/a | 0.8659 |
| 2 | 25004 | n/a | 0.8644 |
| 3 | 25085 | n/a | 0.8604 |
| 4 | 24790 | n/a | 0.8602 |
| 5 | 25084 | n/a | 0.8566 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain, Nessa of North Orchard lane. Case record id: distractor-038. Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-038. Alias reminders for retrieval: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive scene); Nessa of North Orchard lane (aliases: Nessa from North Orchard lane; North Orchard lane scene of Nessa). Supplemental citation 1 for distractor-038 repeats the verified marker set: smoke vent chain, true object smoke vent chain, smoke vent chain in Nessa's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-038. Scoped answer summary for distractor-038 repeats the grounded evidence set: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive scene); Nessa of North Orchard lane (aliases: Nessa from North Orchard lane; North Orchard lane scene of Nessa). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain, Nessa of North Orchard lane. Case record id: distractor-038. Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-038. Alias reminders for retrieval: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive sc

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa). Supplemental citation 1 for distractor-078 repeats the verified marker set: blue oar, true object blue oar, blue oar in Nessa's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain, Nessa of North Orchard lane. Case record id: distractor-038. Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-038. Alias reminders for retrieval: smoke vent chain (aliases: true object smoke vent chain; smoke vent chain in Nessa's archive scene); Nessa of North Orchard lane (aliases: Nessa from North Orchard lane; North Orchard lane scene of Nessa).
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-078. Scoped answer summary for distractor-078 repeats the grounded evidence set: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa).
```

## Question 039: distractor-039

**Question:** Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24003 | n/a | 0.9058 |
| 2 | 24207 | n/a | 0.9017 |
| 3 | 24206 | n/a | 0.8973 |

Chunk rank 1:

```text
document distractor-south-meadow-arch-039::distractor-039: In document distractor-south-meadow-arch-039, the verified archive note records Signal Lantern Morning at South Meadow arch, brass compass. Case record id: distractor-039. Question: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-039. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); brass compass (aliases: event detail brass compass; brass compass in the correct event).
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-039::distractor-039: In document distractor-south-meadow-arch-039, the verified archive note records Signal Lantern Morning at South Meadow arch, brass compass. Case record id: distractor-039. Question: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-039. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); brass compass (aliases: event detail brass compass; brass compass in the correct event). Supplemental citation 1 for distractor-039 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-039. Scoped answer summary for distractor-039 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); brass compass (aliases: event detail brass compass; brass compass in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-039::distractor-039: In document distractor-south-meadow-arch-039, the verified archive note records Signal Lantern Morning at South Meadow arch, brass compass. Case record id: distractor-039. Question: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-039. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arc

[truncated in Markdown; full text is available in JSON]
```

### Model: multilingual_e5_large

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
| 1 | 25007 | n/a | 0.8997 |
| 2 | 25006 | n/a | 0.8917 |
| 3 | 24803 | n/a | 0.8786 |
| 4 | 25037 | n/a | 0.8683 |
| 5 | 24947 | n/a | 0.8679 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-039::distractor-039: In document distractor-south-meadow-arch-039, the verified archive note records Signal Lantern Morning at South Meadow arch, brass compass. Case record id: distractor-039. Question: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-039. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); brass compass (aliases: event detail brass compass; brass compass in the correct event). Supplemental citation 1 for distractor-039 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-039. Scoped answer summary for distractor-039 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); brass compass (aliases: event detail brass compass; brass compass in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-039::distractor-039: In document distractor-south-meadow-arch-039, the verified archive note records Signal Lantern Morning at South Meadow arch, brass compass. Case record id: distractor-039. Question: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-039. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arc

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-south-meadow-arch-039::distractor-039: In document distractor-south-meadow-arch-039, the verified archive note records Signal Lantern Morning at South Meadow arch, brass compass. Case record id: distractor-039. Question: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-039. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); brass compass (aliases: event detail brass compass; brass compass in the correct event).
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Morning at South Meadow arch, rope bridge permit. Case record id: distractor-054. Question: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-054. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); rope bridge permit (aliases: event detail rope bridge permit; rope bridge permit in the correct event). Supplemental citation 1 for distractor-054 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Morning at South Meadow arch, star ledger page. Case record id: distractor-009. Question: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-009. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); star ledger page (aliases: event detail star ledger page; star ledger page in the correct event). Supplemental citation 1 for distractor-009 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 040: distractor-040

**Question:** Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24209 | n/a | 0.8953 |
| 2 | 24208 | n/a | 0.8815 |
| 3 | 23939 | n/a | 0.8802 |

Chunk rank 1:

```text
Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry shed, linen wick. Case record id: distractor-040. Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Scope reminder: document distractor-birch-ferry-shed-040. Alias reminders for retrieval: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note). Supplemental citation 1 for distractor-040 repeats the verified marker set: Mira of Birch Ferry shed, Mira from Birch Ferry shed, Birch Ferry shed Mira. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Case scope id: distractor-040. Scoped answer summary for distractor-040 repeats the grounded evidence set: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry shed, linen wick. Case record id: distractor-040. Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Scope reminder: document distractor-birch-ferry-shed-040. Alias reminders for retrieval: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note).
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry shed, linen wick. Case record id: distractor-040. Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Scope reminder: document distractor-birch-ferry-shed-040. Alias reminders for retrieval: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 25009 | n/a | 0.8708 |
| 2 | 25008 | n/a | 0.8605 |
| 3 | 24739 | n/a | 0.8523 |
| 4 | 25069 | n/a | 0.8499 |
| 5 | 24979 | n/a | 0.8465 |

Chunk rank 1:

```text
Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry shed, linen wick. Case record id: distractor-040. Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Scope reminder: document distractor-birch-ferry-shed-040. Alias reminders for retrieval: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note). Supplemental citation 1 for distractor-040 repeats the verified marker set: Mira of Birch Ferry shed, Mira from Birch Ferry shed, Birch Ferry shed Mira. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Case scope id: distractor-040. Scoped answer summary for distractor-040 repeats the grounded evidence set: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry shed, linen wick. Case record id: distractor-040. Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Scope reminder: document distractor-birch-ferry-shed-040. Alias reminders for retrieval: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note).
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry shed, linen wick. Case record id: distractor-040. Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Scope reminder: document distractor-birch-ferry-shed-040. Alias reminders for retrieval: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry shed, smoke vent chain. Case record id: distractor-070. Question: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Scope reminder: document distractor-birch-ferry-shed-070. Alias reminders for retrieval: Lina of Birch Ferry shed (aliases: Lina from Birch Ferry shed; Birch Ferry shed Lina); smoke vent chain (aliases: correct object smoke vent chain; smoke vent chain in the true note). Supplemental citation 1 for distractor-070 repeats the verified marker set: Lina of Birch Ferry shed, Lina from Birch Ferry shed, Birch Ferry shed Lina. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry shed, canal route map. Case record id: distractor-025. Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Scope reminder: document distractor-birch-ferry-shed-025. Alias reminders for retrieval: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note). Supplemental citation 1 for distractor-025 repeats the verified marker set: Anton of Birch Ferry shed, Anton from Birch Ferry shed, Birch Ferry shed Anton. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 041: distractor-041

**Question:** Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `Lantern Row kiosk`
- Missing: `March 15 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Missing expected evidence: March 15 Bellwater Fair`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24271 | n/a | 0.9048 |
| 2 | 24151 | n/a | 0.9042 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 24981 | n/a | 0.8932 |
| 2 | 25101 | n/a | 0.8931 |
| 3 | 25011 | n/a | 0.8931 |
| 4 | 25041 | n/a | 0.8926 |
| 5 | 24951 | n/a | 0.8922 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-041 repeats the verified marker set: March 15 Bellwater Fair, Bellwater Fair on March 15, memory dated March 15. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-056::distractor-056: In document distractor-lantern-row-kiosk-056, the verified archive note records March 12 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-056. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-056. Alias reminders for retrieval: March 12 Bellwater Fair (aliases: Bellwater Fair on March 12; memory dated March 12); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-056 repeats the verified marker set: March 12 Bellwater Fair, Bellwater Fair on March 12, memory dated March 12. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 042: distractor-042

**Question:** Which place held the true profile detail for Kira, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, lantern hook`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `partial`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24293 | n/a | 0.8527 |
| 2 | 24213 | n/a | 0.8449 |
| 3 | 24233 | n/a | 0.8327 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor-082: In document distractor-blue-trunk-cabin-082, the verified archive note records Blue Trunk cabin, copper wind vane pin. Case record id: distractor-082. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-082. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); copper wind vane pin (aliases: profile detail copper wind vane pin; copper wind vane pin at Blue Trunk cabin). Supplemental citation 1 for distractor-082 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-cloud-wharf-office-042::distractor-042: In document distractor-cloud-wharf-office-042, the verified archive note records Cloud Wharf office, lantern hook. Case record id: distractor-042. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-042. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); lantern hook (aliases: profile detail lantern hook; lantern hook at Cloud Wharf office). Supplemental citation 1 for distractor-042 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor-052: In document distractor-blue-trunk-cabin-052, the verified archive note records Blue Trunk cabin, violet ribbon. Case record id: distractor-052. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-052. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin). Supplemental citation 1 for distractor-052 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, lantern hook`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 25013 | n/a | 0.8334 |
| 2 | 25093 | n/a | 0.8193 |
| 3 | 25012 | n/a | 0.8117 |
| 4 | 24759 | n/a | 0.8004 |
| 5 | 24993 | n/a | 0.8004 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-cloud-wharf-office-042::distractor-042: In document distractor-cloud-wharf-office-042, the verified archive note records Cloud Wharf office, lantern hook. Case record id: distractor-042. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-042. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); lantern hook (aliases: profile detail lantern hook; lantern hook at Cloud Wharf office). Supplemental citation 1 for distractor-042 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor-082: In document distractor-blue-trunk-cabin-082, the verified archive note records Blue Trunk cabin, copper wind vane pin. Case record id: distractor-082. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-082. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); copper wind vane pin (aliases: profile detail copper wind vane pin; copper wind vane pin at Blue Trunk cabin). Supplemental citation 1 for distractor-082 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? Case scope id: distractor-042. Scoped answer summary for distractor-042 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); lantern hook (aliases: profile detail lantern hook; lantern hook at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-042::distractor-042: In document distractor-cloud-wharf-office-042, the verified archive note records Cloud Wharf office, lantern hook. Case record id: distractor-042. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-042. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); lantern hook (aliases: profile detail lantern hook; lantern hook at Cloud Wharf office).
```

Chunk rank 4:

```text
document distractor-cloud-wharf-office-042::distractor-042: In document distractor-cloud-wharf-office-042, the verified archive note records Cloud Wharf office, lantern hook. Case record id: distractor-042. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-042. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); lantern hook (aliases: profile detail lantern hook; lantern hook at Cloud Wharf office).
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-moon-mill-yard-032::distractor-032: In document distractor-moon-mill-yard-032, the verified archive note records Moon Mill yard, amber lantern. Case record id: distractor-032. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-032. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); amber lantern (aliases: profile detail amber lantern; amber lantern at Moon Mill yard). Supplemental citation 1 for distractor-032 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 043: distractor-043

**Question:** Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24215 | n/a | 0.8867 |
| 2 | 24214 | n/a | 0.8848 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap, Petar of Ridge Post loft. Case record id: distractor-043. Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-043. Alias reminders for retrieval: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Petar's archive scene); Petar of Ridge Post loft (aliases: Petar from Ridge Post loft; Ridge Post loft scene of Petar). Supplemental citation 1 for distractor-043 repeats the verified marker set: weathered camera strap, true object weathered camera strap, weathered camera strap in Petar's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-043. Scoped answer summary for distractor-043 repeats the grounded evidence set: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Petar's archive scene); Petar of Ridge Post loft (aliases: Petar from Ridge Post loft; Ridge Post loft scene of Petar). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap, Petar of Ridge Post loft. Case record id: distractor-043. Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-043. Alias reminders for retrieval: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Pet

[truncated in Markdown; full text is available in JSON]
```

### Model: multilingual_e5_large

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
| 1 | 25015 | n/a | 0.8701 |
| 2 | 24797 | n/a | 0.8606 |
| 3 | 25014 | n/a | 0.8557 |
| 4 | 25075 | n/a | 0.8510 |
| 5 | 24955 | n/a | 0.8406 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap, Petar of Ridge Post loft. Case record id: distractor-043. Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-043. Alias reminders for retrieval: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Petar's archive scene); Petar of Ridge Post loft (aliases: Petar from Ridge Post loft; Ridge Post loft scene of Petar). Supplemental citation 1 for distractor-043 repeats the verified marker set: weathered camera strap, true object weathered camera strap, weathered camera strap in Petar's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap, Petar of Ridge Post loft. Case record id: distractor-043. Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-043. Alias reminders for retrieval: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Petar's archive scene); Petar of Ridge Post loft (aliases: Petar from Ridge Post loft; Ridge Post loft scene of Petar).
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-043. Scoped answer summary for distractor-043 repeats the grounded evidence set: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Petar's archive scene); Petar of Ridge Post loft (aliases: Petar from Ridge Post loft; Ridge Post loft scene of Petar). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap, Petar of Ridge Post loft. Case record id: distractor-043. Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-043. Alias reminders for retrieval: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Pet

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 4:

```text
Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev). Supplemental citation 1 for distractor-073 repeats the verified marker set: star ledger page, true object star ledger page, star ledger page in Lev's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna). Supplemental citation 1 for distractor-013 repeats the verified marker set: tin key, true object tin key, tin key in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 044: distractor-044

**Question:** Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24217 | n/a | 0.9048 |
| 2 | 24016 | n/a | 0.9021 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lantern Morning at Willow Courtyard well, wax thread. Case record id: distractor-044. Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-044. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); wax thread (aliases: event detail wax thread; wax thread in the correct event). Supplemental citation 1 for distractor-044 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting chunk res

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lantern Morning at Willow Courtyard well, wax thread. Case record id: distractor-044. Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-044. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); wax thread (aliases: event detail wax thread; wax thread in the correct event).
```

### Model: multilingual_e5_large

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
| 1 | 25017 | n/a | 0.8965 |
| 2 | 25016 | n/a | 0.8948 |
| 3 | 24816 | n/a | 0.8760 |
| 4 | 24957 | n/a | 0.8758 |
| 5 | 24956 | n/a | 0.8753 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lantern Morning at Willow Courtyard well, wax thread. Case record id: distractor-044. Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-044. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); wax thread (aliases: event detail wax thread; wax thread in the correct event). Supplemental citation 1 for distractor-044 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting chunk res

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-044. Scoped answer summary for distractor-044 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); wax thread (aliases: event detail wax thread; wax thread in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lantern Morning at Willow Courtyard well, wax thread. Case record id: distractor-044. Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-044. Alias reminders for retrieval: Signal Lantern Morni

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lantern Morning at Willow Courtyard well, wax thread. Case record id: distractor-044. Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-044. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); wax thread (aliases: event detail wax thread; wax thread in the correct event).
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event). Supplemental citation 1 for distractor-014 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting chunk restates

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-014. Scoped answer summary for distractor-014 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at

[truncated in Markdown; full text is available in JSON]
```

## Question 045: distractor-045

**Question:** Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24219 | n/a | 0.8790 |
| 2 | 23933 | n/a | 0.8682 |
| 3 | 24218 | n/a | 0.8673 |

Chunk rank 1:

```text
Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell Bridge square, tin key. Case record id: distractor-045. Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Scope reminder: document distractor-bell-bridge-square-045. Alias reminders for retrieval: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note). Supplemental citation 1 for distractor-045 repeats the verified marker set: Stefan of Bell Bridge square, Stefan from Bell Bridge square, Bell Bridge square Stefan. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell Bridge square, tin key. Case record id: distractor-045. Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Scope reminder: document distractor-bell-bridge-square-045. Alias reminders for retrieval: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note).
```

Chunk rank 3:

```text
Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Case scope id: distractor-045. Scoped answer summary for distractor-045 repeats the grounded evidence set: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell Bridge square, tin key. Case record id: distractor-045. Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Scope reminder: document distractor-bell-bridge-square-045. Alias reminders for retrieval: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 25019 | n/a | 0.8740 |
| 2 | 25018 | n/a | 0.8661 |
| 3 | 24733 | n/a | 0.8507 |
| 4 | 24959 | n/a | 0.8311 |
| 5 | 25079 | n/a | 0.8289 |

Chunk rank 1:

```text
Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell Bridge square, tin key. Case record id: distractor-045. Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Scope reminder: document distractor-bell-bridge-square-045. Alias reminders for retrieval: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note). Supplemental citation 1 for distractor-045 repeats the verified marker set: Stefan of Bell Bridge square, Stefan from Bell Bridge square, Bell Bridge square Stefan. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Case scope id: distractor-045. Scoped answer summary for distractor-045 repeats the grounded evidence set: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell Bridge square, tin key. Case record id: distractor-045. Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Scope reminder: document distractor-bell-bridge-square-045. Alias reminders for retrieval: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note).
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell Bridge square, tin key. Case record id: distractor-045. Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Scope reminder: document distractor-bell-bridge-square-045. Alias reminders for retrieval: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). Supplemental citation 1 for distractor-015 repeats the verified marker set: Ilya of Bell Bridge square, Ilya from Bell Bridge square, Bell Bridge square Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Bridge square, weathered camera strap. Case record id: distractor-075. Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Scope reminder: document distractor-bell-bridge-square-075. Alias reminders for retrieval: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (aliases: correct object weathered camera strap; weathered camera strap in the true note). Supplemental citation 1 for distractor-075 repeats the verified marker set: Pavel of Bell Bridge square, Pavel from Bell Bridge square, Bell Bridge square Pavel. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 046: distractor-046

**Question:** Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `Cedar Hill station`
- Missing: `March 20 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Missing expected evidence: March 20 Bellwater Fair`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24161 | n/a | 0.9059 |
| 2 | 24251 | n/a | 0.9051 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwater Fair, Cedar Hill station. Case record id: distractor-016. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-016. Alias reminders for retrieval: March 26 Bellwater Fair (aliases: Bellwater Fair on March 26; memory dated March 26); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-016 repeats the verified marker set: March 26 Bellwater Fair, Bellwater Fair on March 26, memory dated March 26. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `Cedar Hill station`
- Missing: `March 20 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 5.; Missing expected markers: March 20 Bellwater Fair; Evidence coverage below requirement: 0.500 < 1.000.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 25081 | n/a | 0.8963 |
| 2 | 24990 | n/a | 0.8954 |
| 3 | 25050 | n/a | 0.8951 |
| 4 | 24991 | n/a | 0.8949 |
| 5 | 25080 | n/a | 0.8946 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwater Fair, Cedar Hill station. Case record id: distractor-076. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-076. Alias reminders for retrieval: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-076 repeats the verified marker set: March 14 Bellwater Fair, Bellwater Fair on March 14, memory dated March 14. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-031. Scoped answer summary for distractor-031 repeats the grounded evidence set: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-061. Scoped answer summary for distractor-061 repeats the grounded evidence set: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-031 repeats the verified marker set: March 23 Bellwater Fair, Bellwater Fair on March 23, memory dated March 23. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-076. Scoped answer summary for distractor-076 repeats the grounded evidence set: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwater Fair, Cedar Hill station. Case record id: distractor-076. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-076. Alias reminders for retrieval: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

## Question 047: distractor-047

**Question:** Which place held the true profile detail for Nikola, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Moon Mill yard, willow basket`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `partial`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24303 | n/a | 0.8634 |
| 2 | 24223 | n/a | 0.8624 |
| 3 | 24143 | n/a | 0.8517 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distractor-087: In document distractor-cloud-wharf-office-087, the verified archive note records Cloud Wharf office, oak barrel hoops. Case record id: distractor-087. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-087. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); oak barrel hoops (aliases: profile detail oak barrel hoops; oak barrel hoops at Cloud Wharf office). Supplemental citation 1 for distractor-087 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-moon-mill-yard-047::distractor-047: In document distractor-moon-mill-yard-047, the verified archive note records Moon Mill yard, willow basket. Case record id: distractor-047. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-047. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); willow basket (aliases: profile detail willow basket; willow basket at Moon Mill yard). Supplemental citation 1 for distractor-047 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distractor-007: In document distractor-blue-trunk-cabin-007, the verified archive note records Blue Trunk cabin, brass compass. Case record id: distractor-007. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-007. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); brass compass (aliases: profile detail brass compass; brass compass at Blue Trunk cabin). Supplemental citation 1 for distractor-007 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Mill yard, willow basket`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 25103 | n/a | 0.8328 |
| 2 | 25023 | n/a | 0.8240 |
| 3 | 25102 | n/a | 0.8195 |
| 4 | 24943 | n/a | 0.8162 |
| 5 | 25022 | n/a | 0.8099 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distractor-087: In document distractor-cloud-wharf-office-087, the verified archive note records Cloud Wharf office, oak barrel hoops. Case record id: distractor-087. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-087. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); oak barrel hoops (aliases: profile detail oak barrel hoops; oak barrel hoops at Cloud Wharf office). Supplemental citation 1 for distractor-087 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-moon-mill-yard-047::distractor-047: In document distractor-moon-mill-yard-047, the verified archive note records Moon Mill yard, willow basket. Case record id: distractor-047. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-047. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); willow basket (aliases: profile detail willow basket; willow basket at Moon Mill yard). Supplemental citation 1 for distractor-047 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-087. Scoped answer summary for distractor-087 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); oak barrel hoops (aliases: profile detail oak barrel hoops; oak barrel hoops at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-087::distractor-087: In document distractor-cloud-wharf-office-087, the verified archive note records Cloud Wharf office, oak barrel hoops. Case record id: distractor-087. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-087. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); oak barrel hoops (aliases: profile detail oak barrel hoops; oak barrel hoops at Cloud Wharf office).
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distractor-007: In document distractor-blue-trunk-cabin-007, the verified archive note records Blue Trunk cabin, brass compass. Case record id: distractor-007. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-007. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); brass compass (aliases: profile detail brass compass; brass compass at Blue Trunk cabin). Supplemental citation 1 for distractor-007 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-047. Scoped answer summary for distractor-047 repeats the grounded evidence set: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); willow basket (aliases: profile detail willow basket; willow basket at Moon Mill yard). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-moon-mill-yard-047::distractor-047: In document distractor-moon-mill-yard-047, the verified archive note records Moon Mill yard, willow basket. Case record id: distractor-047. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-047. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); willow basket (aliases: profile detail willow basket; willow basket at Moon Mill yard).
```

## Question 048: distractor-048

**Question:** Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24022 | n/a | 0.8806 |
| 2 | 24225 | n/a | 0.8803 |
| 3 | 24224 | n/a | 0.8766 |

Chunk rank 1:

```text
document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mask, Sonya of Winter Chapel porch. Case record id: distractor-048. Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-048. Alias reminders for retrieval: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive scene); Sonya of Winter Chapel porch (aliases: Sonya from Winter Chapel porch; Winter Chapel porch scene of Sonya).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mask, Sonya of Winter Chapel porch. Case record id: distractor-048. Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-048. Alias reminders for retrieval: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive scene); Sonya of Winter Chapel porch (aliases: Sonya from Winter Chapel porch; Winter Chapel porch scene of Sonya). Supplemental citation 1 for distractor-048 repeats the verified marker set: paper moon mask, true object paper moon mask, paper moon mask in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-048. Scoped answer summary for distractor-048 repeats the grounded evidence set: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive scene); Sonya of Winter Chapel porch (aliases: Sonya from Winter Chapel porch; Winter Chapel porch scene of Sonya). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mask, Sonya of Winter Chapel porch. Case record id: distractor-048. Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-048. Alias reminders for retrieval: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive

[truncated in Markdown; full text is available in JSON]
```

### Model: multilingual_e5_large

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
| 1 | 24822 | n/a | 0.8595 |
| 2 | 25025 | n/a | 0.8592 |
| 3 | 25024 | n/a | 0.8561 |
| 4 | 25105 | n/a | 0.8408 |
| 5 | 24945 | n/a | 0.8407 |

Chunk rank 1:

```text
document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mask, Sonya of Winter Chapel porch. Case record id: distractor-048. Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-048. Alias reminders for retrieval: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive scene); Sonya of Winter Chapel porch (aliases: Sonya from Winter Chapel porch; Winter Chapel porch scene of Sonya).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mask, Sonya of Winter Chapel porch. Case record id: distractor-048. Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-048. Alias reminders for retrieval: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive scene); Sonya of Winter Chapel porch (aliases: Sonya from Winter Chapel porch; Winter Chapel porch scene of Sonya). Supplemental citation 1 for distractor-048 repeats the verified marker set: paper moon mask, true object paper moon mask, paper moon mask in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-048. Scoped answer summary for distractor-048 repeats the grounded evidence set: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive scene); Sonya of Winter Chapel porch (aliases: Sonya from Winter Chapel porch; Winter Chapel porch scene of Sonya). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mask, Sonya of Winter Chapel porch. Case record id: distractor-048. Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-048. Alias reminders for retrieval: paper moon mask (aliases: true object paper moon mask; paper moon mask in Sonya's archive

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 4:

```text
Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya of Ridge Post loft. Case record id: distractor-088. Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-088. Alias reminders for retrieval: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya). Supplemental citation 1 for distractor-088 repeats the verified marker set: blue glass jar, true object blue glass jar, blue glass jar in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sonya of North Orchard lane. Case record id: distractor-008. Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-008. Alias reminders for retrieval: linen wick (aliases: true object linen wick; linen wick in Sonya's archive scene); Sonya of North Orchard lane (aliases: Sonya from North Orchard lane; North Orchard lane scene of Sonya). Supplemental citation 1 for distractor-008 repeats the verified marker set: linen wick, true object linen wick, linen wick in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 049: distractor-049

**Question:** Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Marble stair hall, glass ink bottle`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24227 | n/a | 0.8994 |
| 2 | 23971 | n/a | 0.8960 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-049::distractor-049: In document distractor-marble-stair-hall-049, the verified archive note records Signal Lantern Morning at Marble stair hall, glass ink bottle. Case record id: distractor-049. Question: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-049. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); glass ink bottle (aliases: event detail glass ink bottle; glass ink bottle in the correct event). Supplemental citation 1 for distractor-049 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-marble-stair-hall-049::distractor-049: In document distractor-marble-stair-hall-049, the verified archive note records Signal Lantern Morning at Marble stair hall, glass ink bottle. Case record id: distractor-049. Question: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-049. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); glass ink bottle (aliases: event detail glass ink bottle; glass ink bottle in the correct event).
```

### Model: multilingual_e5_large

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Marble stair hall, glass ink bottle`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 25027 | n/a | 0.8995 |
| 2 | 25026 | n/a | 0.8941 |
| 3 | 25087 | n/a | 0.8835 |
| 4 | 25086 | n/a | 0.8800 |
| 5 | 25116 | n/a | 0.8787 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-049::distractor-049: In document distractor-marble-stair-hall-049, the verified archive note records Signal Lantern Morning at Marble stair hall, glass ink bottle. Case record id: distractor-049. Question: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-049. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); glass ink bottle (aliases: event detail glass ink bottle; glass ink bottle in the correct event). Supplemental citation 1 for distractor-049 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-049. Scoped answer summary for distractor-049 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); glass ink bottle (aliases: event detail glass ink bottle; glass ink bottle in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-049::distractor-049: In document distractor-marble-stair-hall-049, the verified archive note records Signal Lantern Morning at Marble stair hall, glass ink bottle. Case record id: distractor-049. Question: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-049. Alias reminders for retrieval: Signal Lantern Morning at Marble

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Morning at Marble stair hall, willow basket. Case record id: distractor-079. Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-079. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); willow basket (aliases: event detail willow basket; willow basket in the correct event). Supplemental citation 1 for distractor-079 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-079. Scoped answer summary for distractor-079 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); willow basket (aliases: event detail willow basket; willow basket in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Morning at Marble stair hall, willow basket. Case record id: distractor-079. Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-079. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-094. Scoped answer summary for distractor-094 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hal

[truncated in Markdown; full text is available in JSON]
```

## Question 050: distractor-050

**Question:** Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24229 | n/a | 0.8940 |
| 2 | 24010 | n/a | 0.8911 |

Chunk rank 1:

```text
Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? document distractor-star-basin-gallery-050::distractor-050: In document distractor-star-basin-gallery-050, the verified archive note records Selma of Star Basin gallery, copper wind vane pin. Case record id: distractor-050. Question: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Scope reminder: document distractor-star-basin-gallery-050. Alias reminders for retrieval: Selma of Star Basin gallery (aliases: Selma from Star Basin gallery; Star Basin gallery Selma); copper wind vane pin (aliases: correct object copper wind vane pin; copper wind vane pin in the true note). Supplemental citation 1 for distractor-050 repeats the verified marker set: Selma of Star Basin gallery, Selma from Star Basin gallery, Star Basin gallery Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-star-basin-gallery-050::distractor-050: In document distractor-star-basin-gallery-050, the verified archive note records Selma of Star Basin gallery, copper wind vane pin. Case record id: distractor-050. Question: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Scope reminder: document distractor-star-basin-gallery-050. Alias reminders for retrieval: Selma of Star Basin gallery (aliases: Selma from Star Basin gallery; Star Basin gallery Selma); copper wind vane pin (aliases: correct object copper wind vane pin; copper wind vane pin in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 25029 | n/a | 0.8722 |
| 2 | 25028 | n/a | 0.8657 |
| 3 | 24810 | n/a | 0.8403 |
| 4 | 25109 | n/a | 0.8264 |
| 5 | 25108 | n/a | 0.8239 |

Chunk rank 1:

```text
Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? document distractor-star-basin-gallery-050::distractor-050: In document distractor-star-basin-gallery-050, the verified archive note records Selma of Star Basin gallery, copper wind vane pin. Case record id: distractor-050. Question: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Scope reminder: document distractor-star-basin-gallery-050. Alias reminders for retrieval: Selma of Star Basin gallery (aliases: Selma from Star Basin gallery; Star Basin gallery Selma); copper wind vane pin (aliases: correct object copper wind vane pin; copper wind vane pin in the true note). Supplemental citation 1 for distractor-050 repeats the verified marker set: Selma of Star Basin gallery, Selma from Star Basin gallery, Star Basin gallery Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Case scope id: distractor-050. Scoped answer summary for distractor-050 repeats the grounded evidence set: Selma of Star Basin gallery (aliases: Selma from Star Basin gallery; Star Basin gallery Selma); copper wind vane pin (aliases: correct object copper wind vane pin; copper wind vane pin in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-050::distractor-050: In document distractor-star-basin-gallery-050, the verified archive note records Selma of Star Basin gallery, copper wind vane pin. Case record id: distractor-050. Question: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Scope reminder: document distractor-star-basin-gallery-050. Alias reminders for retrieval: Selma of Star Basin gallery (aliases: Selma from Star Basin gallery; Star Basin gallery Selma); copper wind vane pin (aliases: correct object copper wind vane pin; copper wind vane pin in the true note).
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-050::distractor-050: In document distractor-star-basin-gallery-050, the verified archive note records Selma of Star Basin gallery, copper wind vane pin. Case record id: distractor-050. Question: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Scope reminder: document distractor-star-basin-gallery-050. Alias reminders for retrieval: Selma of Star Basin gallery (aliases: Selma from Star Basin gallery; Star Basin gallery Selma); copper wind vane pin (aliases: correct object copper wind vane pin; copper wind vane pin in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Bridge square, cedar shovel. Case record id: distractor-090. Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Scope reminder: document distractor-bell-bridge-square-090. Alias reminders for retrieval: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note). Supplemental citation 1 for distractor-090 repeats the verified marker set: Selma of Bell Bridge square, Selma from Bell Bridge square, Bell Bridge square Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Case scope id: distractor-090. Scoped answer summary for distractor-090 repeats the grounded evidence set: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Bridge square, cedar shovel. Case record id: distractor-090. Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Scope reminder: document distractor-bell-bridge-square-090. Alias reminders for retrieval: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note).
```

## Question 051: distractor-051

**Question:** Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `March 25 Bellwater Fair, North Bell workshop`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24291 | n/a | 0.8980 |
| 2 | 24171 | n/a | 0.8961 |
| 3 | 24231 | n/a | 0.8948 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellwater Fair, North Bell workshop. Case record id: distractor-081. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-081. Alias reminders for retrieval: March 19 Bellwater Fair (aliases: Bellwater Fair on March 19; memory dated March 19); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-081 repeats the verified marker set: March 19 Bellwater Fair, Bellwater Fair on March 19, memory dated March 19. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-051::distractor-051: In document distractor-north-bell-workshop-051, the verified archive note records March 25 Bellwater Fair, North Bell workshop. Case record id: distractor-051. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-051. Alias reminders for retrieval: March 25 Bellwater Fair (aliases: Bellwater Fair on March 25; memory dated March 25); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-051 repeats the verified marker set: March 25 Bellwater Fair, Bellwater Fair on March 25, memory dated March 25. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25001 | n/a | 0.8858 |
| 2 | 25061 | n/a | 0.8847 |
| 3 | 25121 | n/a | 0.8845 |
| 4 | 25060 | n/a | 0.8840 |
| 5 | 24941 | n/a | 0.8835 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-096 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. Scoped answer summary for distractor-066 repeats the grounded evidence set: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 052: distractor-052

**Question:** Which place held the true profile detail for Zora, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `0.0000`
- Matched: `none`
- Missing: `Blue Trunk cabin, violet ribbon`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Missing expected evidence: Blue Trunk cabin, violet ribbon`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24313 | n/a | 0.8566 |
| 2 | 24153 | n/a | 0.8559 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-092: In document distractor-moon-mill-yard-092, the verified archive note records Moon Mill yard, moonflower cutting. Case record id: distractor-092. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-092. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); moonflower cutting (aliases: profile detail moonflower cutting; moonflower cutting at Moon Mill yard). Supplemental citation 1 for distractor-092 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-cloud-wharf-office-012::distractor-012: In document distractor-cloud-wharf-office-012, the verified archive note records Cloud Wharf office, wax thread. Case record id: distractor-012. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-012. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); wax thread (aliases: profile detail wax thread; wax thread at Cloud Wharf office). Supplemental citation 1 for distractor-012 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 24953 | n/a | 0.8454 |
| 2 | 25033 | n/a | 0.8371 |
| 3 | 24952 | n/a | 0.8324 |
| 4 | 25113 | n/a | 0.8311 |
| 5 | 25032 | n/a | 0.8202 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-cloud-wharf-office-012::distractor-012: In document distractor-cloud-wharf-office-012, the verified archive note records Cloud Wharf office, wax thread. Case record id: distractor-012. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-012. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); wax thread (aliases: profile detail wax thread; wax thread at Cloud Wharf office). Supplemental citation 1 for distractor-012 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor-052: In document distractor-blue-trunk-cabin-052, the verified archive note records Blue Trunk cabin, violet ribbon. Case record id: distractor-052. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-052. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin). Supplemental citation 1 for distractor-052 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-012. Scoped answer summary for distractor-012 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); wax thread (aliases: profile detail wax thread; wax thread at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-012::distractor-012: In document distractor-cloud-wharf-office-012, the verified archive note records Cloud Wharf office, wax thread. Case record id: distractor-012. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-012. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); wax thread (aliases: profile detail wax thread; wax thread at Cloud Wharf office).
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-092: In document distractor-moon-mill-yard-092, the verified archive note records Moon Mill yard, moonflower cutting. Case record id: distractor-092. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-092. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); moonflower cutting (aliases: profile detail moonflower cutting; moonflower cutting at Moon Mill yard). Supplemental citation 1 for distractor-092 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary for distractor-052 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-052::distractor-052: In document distractor-blue-trunk-cabin-052, the verified archive note records Blue Trunk cabin, violet ribbon. Case record id: distractor-052. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-052. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin).
```

## Question 053: distractor-053

**Question:** Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 23991 | n/a | 0.8840 |
| 2 | 24235 | n/a | 0.8825 |
| 3 | 24234 | n/a | 0.8708 |

Chunk rank 1:

```text
document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Vesna of North Orchard lane. Case record id: distractor-053. Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-053. Alias reminders for retrieval: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Vesna of North Orchard lane. Case record id: distractor-053. Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-053. Alias reminders for retrieval: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna). Supplemental citation 1 for distractor-053 repeats the verified marker set: tuning fork, true object tuning fork, tuning fork in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-053. Scoped answer summary for distractor-053 repeats the grounded evidence set: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Vesna of North Orchard lane. Case record id: distractor-053. Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-053. Alias reminders for retrieval: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna).
```

### Model: multilingual_e5_large

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
| 1 | 25035 | n/a | 0.8668 |
| 2 | 25034 | n/a | 0.8665 |
| 3 | 24791 | n/a | 0.8642 |
| 4 | 24825 | n/a | 0.8470 |
| 5 | 25115 | n/a | 0.8460 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Vesna of North Orchard lane. Case record id: distractor-053. Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-053. Alias reminders for retrieval: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna). Supplemental citation 1 for distractor-053 repeats the verified marker set: tuning fork, true object tuning fork, tuning fork in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-053. Scoped answer summary for distractor-053 repeats the grounded evidence set: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Vesna of North Orchard lane. Case record id: distractor-053. Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-053. Alias reminders for retrieval: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna).
```

Chunk rank 3:

```text
document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Vesna of North Orchard lane. Case record id: distractor-053. Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-053. Alias reminders for retrieval: tuning fork (aliases: true object tuning fork; tuning fork in Vesna's archive scene); Vesna of North Orchard lane (aliases: Vesna from North Orchard lane; North Orchard lane scene of Vesna).
```

Chunk rank 4:

```text
document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna).
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna). Supplemental citation 1 for distractor-093 repeats the verified marker set: birch tea flask, true object birch tea flask, birch tea flask in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 054: distractor-054

**Question:** Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24004 | n/a | 0.8993 |
| 2 | 24001 | n/a | 0.8926 |

Chunk rank 1:

```text
document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Morning at South Meadow arch, rope bridge permit. Case record id: distractor-054. Question: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-054. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); rope bridge permit (aliases: event detail rope bridge permit; rope bridge permit in the correct event).
```

Chunk rank 2:

```text
document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Morning at South Meadow arch, star ledger page. Case record id: distractor-009. Question: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-009. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); star ledger page (aliases: event detail star ledger page; star ledger page in the correct event).
```

### Model: multilingual_e5_large

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
| 1 | 25037 | n/a | 0.8949 |
| 2 | 25036 | n/a | 0.8924 |
| 3 | 25007 | n/a | 0.8828 |
| 4 | 24947 | n/a | 0.8824 |
| 5 | 25097 | n/a | 0.8813 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Morning at South Meadow arch, rope bridge permit. Case record id: distractor-054. Question: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-054. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); rope bridge permit (aliases: event detail rope bridge permit; rope bridge permit in the correct event). Supplemental citation 1 for distractor-054 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-054. Scoped answer summary for distractor-054 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); rope bridge permit (aliases: event detail rope bridge permit; rope bridge permit in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Morning at South Meadow arch, rope bridge permit. Case record id: distractor-054. Question: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-054. Alias reminders for retrieval: Signal Lantern Morning

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-039::distractor-039: In document distractor-south-meadow-arch-039, the verified archive note records Signal Lantern Morning at South Meadow arch, brass compass. Case record id: distractor-039. Question: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-039. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); brass compass (aliases: event detail brass compass; brass compass in the correct event). Supplemental citation 1 for distractor-039 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Morning at South Meadow arch, star ledger page. Case record id: distractor-009. Question: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-009. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); star ledger page (aliases: event detail star ledger page; star ledger page in the correct event). Supplemental citation 1 for distractor-009 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Morning at South Meadow arch, violet ribbon. Case record id: distractor-084. Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-084. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); violet ribbon (aliases: event detail violet ribbon; violet ribbon in the correct event). Supplemental citation 1 for distractor-084 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 055: distractor-055

**Question:** Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24239 | n/a | 0.8930 |
| 2 | 23940 | n/a | 0.8904 |

Chunk rank 1:

```text
Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note). Supplemental citation 1 for distractor-055 repeats the verified marker set: Ilya of Birch Ferry shed, Ilya from Birch Ferry shed, Birch Ferry shed Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 25039 | n/a | 0.8911 |
| 2 | 25038 | n/a | 0.8846 |
| 3 | 24740 | n/a | 0.8685 |
| 4 | 24959 | n/a | 0.8492 |
| 5 | 24958 | n/a | 0.8426 |

Chunk rank 1:

```text
Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note). Supplemental citation 1 for distractor-055 repeats the verified marker set: Ilya of Birch Ferry shed, Ilya from Birch Ferry shed, Birch Ferry shed Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Case scope id: distractor-055. Scoped answer summary for distractor-055 repeats the grounded evidence set: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note).
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). Supplemental citation 1 for distractor-015 repeats the verified marker set: Ilya of Bell Bridge square, Ilya from Bell Bridge square, Bell Bridge square Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer summary for distractor-015 repeats the grounded evidence set: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note).
```

## Question 056: distractor-056

**Question:** Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `Lantern Row kiosk`
- Missing: `March 12 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Missing expected evidence: March 12 Bellwater Fair`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24271 | n/a | 0.9048 |
| 2 | 24151 | n/a | 0.9042 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 24981 | n/a | 0.8932 |
| 2 | 25101 | n/a | 0.8931 |
| 3 | 25011 | n/a | 0.8931 |
| 4 | 25041 | n/a | 0.8926 |
| 5 | 24951 | n/a | 0.8922 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-041 repeats the verified marker set: March 15 Bellwater Fair, Bellwater Fair on March 15, memory dated March 15. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-056::distractor-056: In document distractor-lantern-row-kiosk-056, the verified archive note records March 12 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-056. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-056. Alias reminders for retrieval: March 12 Bellwater Fair (aliases: Bellwater Fair on March 12; memory dated March 12); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-056 repeats the verified marker set: March 12 Bellwater Fair, Bellwater Fair on March 12, memory dated March 12. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 057: distractor-057

**Question:** Which place held the true profile detail for Boris, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, canal route map`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `partial`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24243 | n/a | 0.8630 |
| 2 | 24323 | n/a | 0.8624 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distractor-057: In document distractor-cloud-wharf-office-057, the verified archive note records Cloud Wharf office, canal route map. Case record id: distractor-057. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-057. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); canal route map (aliases: profile detail canal route map; canal route map at Cloud Wharf office). Supplemental citation 1 for distractor-057 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, basalt sketch. Case record id: distractor-097. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-097. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin). Supplemental citation 1 for distractor-097 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, canal route map`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 25043 | n/a | 0.8466 |
| 2 | 25123 | n/a | 0.8379 |
| 3 | 24963 | n/a | 0.8297 |
| 4 | 25042 | n/a | 0.8270 |
| 5 | 25122 | n/a | 0.8183 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distractor-057: In document distractor-cloud-wharf-office-057, the verified archive note records Cloud Wharf office, canal route map. Case record id: distractor-057. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-057. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); canal route map (aliases: profile detail canal route map; canal route map at Cloud Wharf office). Supplemental citation 1 for distractor-057 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, basalt sketch. Case record id: distractor-097. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-097. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin). Supplemental citation 1 for distractor-097 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-moon-mill-yard-017::distractor-017: In document distractor-moon-mill-yard-017, the verified archive note records Moon Mill yard, glass ink bottle. Case record id: distractor-017. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-017. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); glass ink bottle (aliases: profile detail glass ink bottle; glass ink bottle at Moon Mill yard). Supplemental citation 1 for distractor-017 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-057. Scoped answer summary for distractor-057 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); canal route map (aliases: profile detail canal route map; canal route map at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-057::distractor-057: In document distractor-cloud-wharf-office-057, the verified archive note records Cloud Wharf office, canal route map. Case record id: distractor-057. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-057. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); canal route map (aliases: profile detail canal route map; canal route map at Cloud Wharf office).
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summary for distractor-097 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, basalt sketch. Case record id: distractor-097. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-097. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin).
```

## Question 058: distractor-058

**Question:** Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24244 | n/a | 0.8850 |
| 2 | 24245 | n/a | 0.8847 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-058. Scoped answer summary for distractor-058 repeats the grounded evidence set: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of Ridge Post loft. Case record id: distractor-058. Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-058. Alias reminders for retrieval: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of Ridge Post loft. Case record id: distractor-058. Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-058. Alias reminders for retrieval: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria). Supplemental citation 1 for distractor-058 repeats the verified marker set: cedar shovel, true object cedar shovel, cedar shovel in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25045 | n/a | 0.8788 |
| 2 | 24798 | n/a | 0.8714 |
| 3 | 25044 | n/a | 0.8688 |
| 4 | 25075 | n/a | 0.8530 |
| 5 | 25105 | n/a | 0.8474 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of Ridge Post loft. Case record id: distractor-058. Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-058. Alias reminders for retrieval: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria). Supplemental citation 1 for distractor-058 repeats the verified marker set: cedar shovel, true object cedar shovel, cedar shovel in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of Ridge Post loft. Case record id: distractor-058. Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-058. Alias reminders for retrieval: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria).
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-058. Scoped answer summary for distractor-058 repeats the grounded evidence set: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of Ridge Post loft. Case record id: distractor-058. Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-058. Alias reminders for retrieval: cedar shovel (aliases: true object cedar shovel; cedar shovel in Daria's archive scene); Daria of Ridge Post loft (aliases: Daria from Ridge Post loft; Ridge Post loft scene of Daria).
```

Chunk rank 4:

```text
Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev). Supplemental citation 1 for distractor-073 repeats the verified marker set: star ledger page, true object star ledger page, star ledger page in Lev's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya of Ridge Post loft. Case record id: distractor-088. Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-088. Alias reminders for retrieval: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya). Supplemental citation 1 for distractor-088 repeats the verified marker set: blue glass jar, true object blue glass jar, blue glass jar in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 059: distractor-059

**Question:** Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24017 | n/a | 0.9009 |
| 2 | 24247 | n/a | 0.8971 |
| 3 | 24246 | n/a | 0.8898 |

Chunk rank 1:

```text
document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event).
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event). Supplemental citation 1 for distractor-059 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting c

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-059. Scoped answer summary for distractor-059 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lante

[truncated in Markdown; full text is available in JSON]
```

### Model: multilingual_e5_large

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
| 1 | 25047 | n/a | 0.8905 |
| 2 | 25046 | n/a | 0.8902 |
| 3 | 24986 | n/a | 0.8774 |
| 4 | 24987 | n/a | 0.8773 |
| 5 | 24817 | n/a | 0.8749 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event). Supplemental citation 1 for distractor-059 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting c

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-059. Scoped answer summary for distractor-059 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lante

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-029. Scoped answer summary for distractor-029 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); birch tea flask (aliases: event detail birch tea flask; birch tea flask in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-029::distractor-029: In document distractor-willow-courtyard-well-029, the verified archive note records Signal Lantern Morning at Willow Courtyard well, birch tea flask. Case record id: distractor-029. Question: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-029. Alias reminders for retrieval

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-029::distractor-029: In document distractor-willow-courtyard-well-029, the verified archive note records Signal Lantern Morning at Willow Courtyard well, birch tea flask. Case record id: distractor-029. Question: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-029. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); birch tea flask (aliases: event detail birch tea flask; birch tea flask in the correct event). Supplemental citation 1 for distractor-029 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-onl

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lantern Morning at Willow Courtyard well, copper token. Case record id: distractor-059. Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-059. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); copper token (aliases: event detail copper token; copper token in the correct event).
```

## Question 060: distractor-060

**Question:** Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24249 | n/a | 0.8922 |
| 2 | 23934 | n/a | 0.8805 |
| 3 | 24248 | n/a | 0.8710 |

Chunk rank 1:

```text
Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Bridge square, moonflower cutting. Case record id: distractor-060. Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Scope reminder: document distractor-bell-bridge-square-060. Alias reminders for retrieval: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note). Supplemental citation 1 for distractor-060 repeats the verified marker set: Ada of Bell Bridge square, Ada from Bell Bridge square, Bell Bridge square Ada. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Bridge square, moonflower cutting. Case record id: distractor-060. Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Scope reminder: document distractor-bell-bridge-square-060. Alias reminders for retrieval: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note).
```

Chunk rank 3:

```text
Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Case scope id: distractor-060. Scoped answer summary for distractor-060 repeats the grounded evidence set: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Bridge square, moonflower cutting. Case record id: distractor-060. Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Scope reminder: document distractor-bell-bridge-square-060. Alias reminders for retrieval: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 25049 | n/a | 0.8714 |
| 2 | 25048 | n/a | 0.8670 |
| 3 | 24734 | n/a | 0.8509 |
| 4 | 24958 | n/a | 0.8404 |
| 5 | 24959 | n/a | 0.8404 |

Chunk rank 1:

```text
Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Bridge square, moonflower cutting. Case record id: distractor-060. Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Scope reminder: document distractor-bell-bridge-square-060. Alias reminders for retrieval: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note). Supplemental citation 1 for distractor-060 repeats the verified marker set: Ada of Bell Bridge square, Ada from Bell Bridge square, Bell Bridge square Ada. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Case scope id: distractor-060. Scoped answer summary for distractor-060 repeats the grounded evidence set: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Bridge square, moonflower cutting. Case record id: distractor-060. Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Scope reminder: document distractor-bell-bridge-square-060. Alias reminders for retrieval: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note).
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Bridge square, moonflower cutting. Case record id: distractor-060. Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Scope reminder: document distractor-bell-bridge-square-060. Alias reminders for retrieval: Ada of Bell Bridge square (aliases: Ada from Bell Bridge square; Bell Bridge square Ada); moonflower cutting (aliases: correct object moonflower cutting; moonflower cutting in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer summary for distractor-015 repeats the grounded evidence set: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note).
```

Chunk rank 5:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). Supplemental citation 1 for distractor-015 repeats the verified marker set: Ilya of Bell Bridge square, Ilya from Bell Bridge square, Bell Bridge square Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 061: distractor-061

**Question:** Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24161 | n/a | 0.9059 |
| 2 | 24251 | n/a | 0.9051 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwater Fair, Cedar Hill station. Case record id: distractor-016. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-016. Alias reminders for retrieval: March 26 Bellwater Fair (aliases: Bellwater Fair on March 26; memory dated March 26); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-016 repeats the verified marker set: March 26 Bellwater Fair, Bellwater Fair on March 26, memory dated March 26. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25081 | n/a | 0.8963 |
| 2 | 24990 | n/a | 0.8954 |
| 3 | 25050 | n/a | 0.8951 |
| 4 | 24991 | n/a | 0.8949 |
| 5 | 25080 | n/a | 0.8946 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwater Fair, Cedar Hill station. Case record id: distractor-076. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-076. Alias reminders for retrieval: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-076 repeats the verified marker set: March 14 Bellwater Fair, Bellwater Fair on March 14, memory dated March 14. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-031. Scoped answer summary for distractor-031 repeats the grounded evidence set: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-061. Scoped answer summary for distractor-061 repeats the grounded evidence set: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-031 repeats the verified marker set: March 23 Bellwater Fair, Bellwater Fair on March 23, memory dated March 23. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-076. Scoped answer summary for distractor-076 repeats the grounded evidence set: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwater Fair, Cedar Hill station. Case record id: distractor-076. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-076. Alias reminders for retrieval: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

## Question 062: distractor-062

**Question:** Which place held the true profile detail for Talia, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Mill yard, saffron scarf`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24253 | n/a | 0.8517 |
| 2 | 24173 | n/a | 0.8452 |
| 3 | 23978 | n/a | 0.8412 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-moon-mill-yard-062::distractor-062: In document distractor-moon-mill-yard-062, the verified archive note records Moon Mill yard, saffron scarf. Case record id: distractor-062. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-062. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); saffron scarf (aliases: profile detail saffron scarf; saffron scarf at Moon Mill yard). Supplemental citation 1 for distractor-062 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distractor-022: In document distractor-blue-trunk-cabin-022, the verified archive note records Blue Trunk cabin, rope bridge permit. Case record id: distractor-022. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-022. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); rope bridge permit (aliases: profile detail rope bridge permit; rope bridge permit at Blue Trunk cabin). Supplemental citation 1 for distractor-022 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
document distractor-moon-mill-yard-062::distractor-062: In document distractor-moon-mill-yard-062, the verified archive note records Moon Mill yard, saffron scarf. Case record id: distractor-062. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-062. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); saffron scarf (aliases: profile detail saffron scarf; saffron scarf at Moon Mill yard).
```

### Model: multilingual_e5_large

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Mill yard, saffron scarf`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24973 | n/a | 0.8338 |
| 2 | 25053 | n/a | 0.8300 |
| 3 | 25052 | n/a | 0.8163 |
| 4 | 24972 | n/a | 0.8141 |
| 5 | 24909 | n/a | 0.8019 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distractor-022: In document distractor-blue-trunk-cabin-022, the verified archive note records Blue Trunk cabin, rope bridge permit. Case record id: distractor-022. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-022. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); rope bridge permit (aliases: profile detail rope bridge permit; rope bridge permit at Blue Trunk cabin). Supplemental citation 1 for distractor-022 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-moon-mill-yard-062::distractor-062: In document distractor-moon-mill-yard-062, the verified archive note records Moon Mill yard, saffron scarf. Case record id: distractor-062. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-062. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); saffron scarf (aliases: profile detail saffron scarf; saffron scarf at Moon Mill yard). Supplemental citation 1 for distractor-062 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? Case scope id: distractor-062. Scoped answer summary for distractor-062 repeats the grounded evidence set: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); saffron scarf (aliases: profile detail saffron scarf; saffron scarf at Moon Mill yard). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-moon-mill-yard-062::distractor-062: In document distractor-moon-mill-yard-062, the verified archive note records Moon Mill yard, saffron scarf. Case record id: distractor-062. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-062. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); saffron scarf (aliases: profile detail saffron scarf; saffron scarf at Moon Mill yard).
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? Case scope id: distractor-022. Scoped answer summary for distractor-022 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); rope bridge permit (aliases: profile detail rope bridge permit; rope bridge permit at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-022::distractor-022: In document distractor-blue-trunk-cabin-022, the verified archive note records Blue Trunk cabin, rope bridge permit. Case record id: distractor-022. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-022. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); rope bridge permit (aliases: profile detail rope bridge permit; rope bridge permit at Blue Trunk cabin).
```

Chunk rank 5:

```text
document distractor-star-basin-gallery-035::distractor-035::distractor: A conflicting note in document distractor-star-basin-gallery-035 mentions Talia of Star Basin gallery (aliases: Talia from Star Basin gallery; Star Basin gallery Talia) as a misleading archival rumor. That rumor is explicitly different from the verified record for this source scope. Conflict marker only: Talia of Star Basin gallery remains archival noise.
```

## Question 063: distractor-063

**Question:** Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24023 | n/a | 0.8925 |
| 2 | 24255 | n/a | 0.8901 |

Chunk rank 1:

```text
document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor). Supplemental citation 1 for distractor-063 repeats the verified marker set: carved shell comb, true object carved shell comb, carved shell comb in Viktor's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 24823 | n/a | 0.8696 |
| 2 | 25055 | n/a | 0.8668 |
| 3 | 25054 | n/a | 0.8642 |
| 4 | 24995 | n/a | 0.8460 |
| 5 | 24825 | n/a | 0.8418 |

Chunk rank 1:

```text
document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor). Supplemental citation 1 for distractor-063 repeats the verified marker set: carved shell comb, true object carved shell comb, carved shell comb in Viktor's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-063. Scoped answer summary for distractor-063 repeats the grounded evidence set: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell com

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 4:

```text
Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch, Lev of Winter Chapel porch. Case record id: distractor-033. Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-033. Alias reminders for retrieval: basalt sketch (aliases: true object basalt sketch; basalt sketch in Lev's archive scene); Lev of Winter Chapel porch (aliases: Lev from Winter Chapel porch; Winter Chapel porch scene of Lev). Supplemental citation 1 for distractor-033 repeats the verified marker set: basalt sketch, true object basalt sketch, basalt sketch in Lev's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna).
```

## Question 064: distractor-064

**Question:** Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24257 | n/a | 0.9029 |
| 2 | 23972 | n/a | 0.8996 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Morning at Marble stair hall, amber lantern. Case record id: distractor-064. Question: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-064. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); amber lantern (aliases: event detail amber lantern; amber lantern in the correct event). Supplemental citation 1 for distractor-064 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Morning at Marble stair hall, amber lantern. Case record id: distractor-064. Question: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-064. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); amber lantern (aliases: event detail amber lantern; amber lantern in the correct event).
```

### Model: multilingual_e5_large

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
| 1 | 25057 | n/a | 0.8965 |
| 2 | 25056 | n/a | 0.8938 |
| 3 | 24772 | n/a | 0.8732 |
| 4 | 24997 | n/a | 0.8726 |
| 5 | 25117 | n/a | 0.8725 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Morning at Marble stair hall, amber lantern. Case record id: distractor-064. Question: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-064. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); amber lantern (aliases: event detail amber lantern; amber lantern in the correct event). Supplemental citation 1 for distractor-064 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-064. Scoped answer summary for distractor-064 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); amber lantern (aliases: event detail amber lantern; amber lantern in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Morning at Marble stair hall, amber lantern. Case record id: distractor-064. Question: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-064. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Morning at Marble stair hall, amber lantern. Case record id: distractor-064. Question: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-064. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); amber lantern (aliases: event detail amber lantern; amber lantern in the correct event).
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Morning at Marble stair hall, green apron. Case record id: distractor-034. Question: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-034. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); green apron (aliases: event detail green apron; green apron in the correct event). Supplemental citation 1 for distractor-034 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event). Supplemental citation 1 for distractor-094 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 065: distractor-065

**Question:** Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24259 | n/a | 0.8979 |
| 2 | 24258 | n/a | 0.8844 |

Chunk rank 1:

```text
Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Basin gallery, basalt sketch. Case record id: distractor-065. Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Scope reminder: document distractor-star-basin-gallery-065. Alias reminders for retrieval: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note). Supplemental citation 1 for distractor-065 repeats the verified marker set: Anton of Star Basin gallery, Anton from Star Basin gallery, Star Basin gallery Anton. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Case scope id: distractor-065. Scoped answer summary for distractor-065 repeats the grounded evidence set: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Basin gallery, basalt sketch. Case record id: distractor-065. Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Scope reminder: document distractor-star-basin-gallery-065. Alias reminders for retrieval: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 25059 | n/a | 0.8829 |
| 2 | 25058 | n/a | 0.8738 |
| 3 | 24811 | n/a | 0.8632 |
| 4 | 24968 | n/a | 0.8247 |
| 5 | 24999 | n/a | 0.8220 |

Chunk rank 1:

```text
Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Basin gallery, basalt sketch. Case record id: distractor-065. Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Scope reminder: document distractor-star-basin-gallery-065. Alias reminders for retrieval: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note). Supplemental citation 1 for distractor-065 repeats the verified marker set: Anton of Star Basin gallery, Anton from Star Basin gallery, Star Basin gallery Anton. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Case scope id: distractor-065. Scoped answer summary for distractor-065 repeats the grounded evidence set: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Basin gallery, basalt sketch. Case record id: distractor-065. Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Scope reminder: document distractor-star-basin-gallery-065. Alias reminders for retrieval: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note).
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Basin gallery, basalt sketch. Case record id: distractor-065. Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Scope reminder: document distractor-star-basin-gallery-065. Alias reminders for retrieval: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Case scope id: distractor-020. Scoped answer summary for distractor-020 repeats the grounded evidence set: Ada of Star Basin gallery (aliases: Ada from Star Basin gallery; Star Basin gallery Ada); violet ribbon (aliases: correct object violet ribbon; violet ribbon in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basin gallery, violet ribbon. Case record id: distractor-020. Question: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Scope reminder: document distractor-star-basin-gallery-020. Alias reminders for retrieval: Ada of Star Basin gallery (aliases: Ada from Star Basin gallery; Star Basin gallery Ada); violet ribbon (aliases: correct object violet ribbon; violet ribbon in the true note).
```

Chunk rank 5:

```text
Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note). Supplemental citation 1 for distractor-035 repeats the verified marker set: Pavel of Star Basin gallery, Pavel from Star Basin gallery, Star Basin gallery Pavel. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 066: distractor-066

**Question:** Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `North Bell workshop`
- Missing: `March 22 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Missing expected evidence: March 22 Bellwater Fair`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24291 | n/a | 0.8980 |
| 2 | 24171 | n/a | 0.8961 |
| 3 | 24231 | n/a | 0.8948 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellwater Fair, North Bell workshop. Case record id: distractor-081. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-081. Alias reminders for retrieval: March 19 Bellwater Fair (aliases: Bellwater Fair on March 19; memory dated March 19); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-081 repeats the verified marker set: March 19 Bellwater Fair, Bellwater Fair on March 19, memory dated March 19. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-051::distractor-051: In document distractor-north-bell-workshop-051, the verified archive note records March 25 Bellwater Fair, North Bell workshop. Case record id: distractor-051. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-051. Alias reminders for retrieval: March 25 Bellwater Fair (aliases: Bellwater Fair on March 25; memory dated March 25); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-051 repeats the verified marker set: March 25 Bellwater Fair, Bellwater Fair on March 25, memory dated March 25. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25001 | n/a | 0.8858 |
| 2 | 25061 | n/a | 0.8847 |
| 3 | 25121 | n/a | 0.8845 |
| 4 | 25060 | n/a | 0.8840 |
| 5 | 24941 | n/a | 0.8835 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-096 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. Scoped answer summary for distractor-066 repeats the grounded evidence set: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 067: distractor-067

**Question:** Which place held the true profile detail for Tomas, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, silver booth token`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `partial`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24263 | n/a | 0.8494 |
| 2 | 24183 | n/a | 0.8485 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distractor-067: In document distractor-blue-trunk-cabin-067, the verified archive note records Blue Trunk cabin, silver booth token. Case record id: distractor-067. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-067. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); silver booth token (aliases: profile detail silver booth token; silver booth token at Blue Trunk cabin). Supplemental citation 1 for distractor-067 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-cloud-wharf-office-027::distractor-027: In document distractor-cloud-wharf-office-027, the verified archive note records Cloud Wharf office, copper token. Case record id: distractor-027. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-027. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); copper token (aliases: profile detail copper token; copper token at Cloud Wharf office). Supplemental citation 1 for distractor-027 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 24983 | n/a | 0.8204 |
| 2 | 25063 | n/a | 0.8114 |
| 3 | 24982 | n/a | 0.8009 |
| 4 | 25062 | n/a | 0.7938 |
| 5 | 25043 | n/a | 0.7937 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-cloud-wharf-office-027::distractor-027: In document distractor-cloud-wharf-office-027, the verified archive note records Cloud Wharf office, copper token. Case record id: distractor-027. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-027. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); copper token (aliases: profile detail copper token; copper token at Cloud Wharf office). Supplemental citation 1 for distractor-027 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distractor-067: In document distractor-blue-trunk-cabin-067, the verified archive note records Blue Trunk cabin, silver booth token. Case record id: distractor-067. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-067. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); silver booth token (aliases: profile detail silver booth token; silver booth token at Blue Trunk cabin). Supplemental citation 1 for distractor-067 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-027. Scoped answer summary for distractor-027 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); copper token (aliases: profile detail copper token; copper token at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-027::distractor-027: In document distractor-cloud-wharf-office-027, the verified archive note records Cloud Wharf office, copper token. Case record id: distractor-027. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-027. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); copper token (aliases: profile detail copper token; copper token at Cloud Wharf office).
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-067. Scoped answer summary for distractor-067 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); silver booth token (aliases: profile detail silver booth token; silver booth token at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-067::distractor-067: In document distractor-blue-trunk-cabin-067, the verified archive note records Blue Trunk cabin, silver booth token. Case record id: distractor-067. Question: Which place held the true profile detail for Tomas, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-067. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); silver booth token (aliases: profile detail silver booth token; silver booth token at Blue Trunk cabin).
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distractor-057: In document distractor-cloud-wharf-office-057, the verified archive note records Cloud Wharf office, canal route map. Case record id: distractor-057. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-057. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); canal route map (aliases: profile detail canal route map; canal route map at Cloud Wharf office). Supplemental citation 1 for distractor-057 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 068: distractor-068

**Question:** Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24265 | n/a | 0.8860 |
| 2 | 23992 | n/a | 0.8845 |
| 3 | 24264 | n/a | 0.8780 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-068::distractor-068: In document distractor-north-orchard-lane-068, the verified archive note records clay watering cup, Vera of North Orchard lane. Case record id: distractor-068. Question: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-068. Alias reminders for retrieval: clay watering cup (aliases: true object clay watering cup; clay watering cup in Vera's archive scene); Vera of North Orchard lane (aliases: Vera from North Orchard lane; North Orchard lane scene of Vera). Supplemental citation 1 for distractor-068 repeats the verified marker set: clay watering cup, true object clay watering cup, clay watering cup in Vera's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-north-orchard-lane-068::distractor-068: In document distractor-north-orchard-lane-068, the verified archive note records clay watering cup, Vera of North Orchard lane. Case record id: distractor-068. Question: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-068. Alias reminders for retrieval: clay watering cup (aliases: true object clay watering cup; clay watering cup in Vera's archive scene); Vera of North Orchard lane (aliases: Vera from North Orchard lane; North Orchard lane scene of Vera).
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-068. Scoped answer summary for distractor-068 repeats the grounded evidence set: clay watering cup (aliases: true object clay watering cup; clay watering cup in Vera's archive scene); Vera of North Orchard lane (aliases: Vera from North Orchard lane; North Orchard lane scene of Vera). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-068::distractor-068: In document distractor-north-orchard-lane-068, the verified archive note records clay watering cup, Vera of North Orchard lane. Case record id: distractor-068. Question: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-068. Alias reminders for retrieval: clay watering cup (aliases: true object clay watering cup; clay watering cup in Vera's archive sce

[truncated in Markdown; full text is available in JSON]
```

### Model: multilingual_e5_large

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
| 1 | 25065 | n/a | 0.8508 |
| 2 | 24792 | n/a | 0.8505 |
| 3 | 25125 | n/a | 0.8497 |
| 4 | 24975 | n/a | 0.8455 |
| 5 | 25064 | n/a | 0.8451 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-068::distractor-068: In document distractor-north-orchard-lane-068, the verified archive note records clay watering cup, Vera of North Orchard lane. Case record id: distractor-068. Question: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-068. Alias reminders for retrieval: clay watering cup (aliases: true object clay watering cup; clay watering cup in Vera's archive scene); Vera of North Orchard lane (aliases: Vera from North Orchard lane; North Orchard lane scene of Vera). Supplemental citation 1 for distractor-068 repeats the verified marker set: clay watering cup, true object clay watering cup, clay watering cup in Vera's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-north-orchard-lane-068::distractor-068: In document distractor-north-orchard-lane-068, the verified archive note records clay watering cup, Vera of North Orchard lane. Case record id: distractor-068. Question: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-068. Alias reminders for retrieval: clay watering cup (aliases: true object clay watering cup; clay watering cup in Vera's archive scene); Vera of North Orchard lane (aliases: Vera from North Orchard lane; North Orchard lane scene of Vera).
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Daria of North Orchard lane. Case record id: distractor-098. Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-098. Alias reminders for retrieval: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria). Supplemental citation 1 for distractor-098 repeats the verified marker set: green apron, true object green apron, green apron in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor). Supplemental citation 1 for distractor-023 repeats the verified marker set: oak barrel hoops, true object oak barrel hoops, oak barrel hoops in Viktor's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-068. Scoped answer summary for distractor-068 repeats the grounded evidence set: clay watering cup (aliases: true object clay watering cup; clay watering cup in Vera's archive scene); Vera of North Orchard lane (aliases: Vera from North Orchard lane; North Orchard lane scene of Vera). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-068::distractor-068: In document distractor-north-orchard-lane-068, the verified archive note records clay watering cup, Vera of North Orchard lane. Case record id: distractor-068. Question: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-068. Alias reminders for retrieval: clay watering cup (aliases: true object clay watering cup; clay watering cup in Vera's archive sce

[truncated in Markdown; full text is available in JSON]
```

## Question 069: distractor-069

**Question:** Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24005 | n/a | 0.9025 |
| 2 | 24007 | n/a | 0.8942 |

Chunk rank 1:

```text
document distractor-south-meadow-arch-069::distractor-069: In document distractor-south-meadow-arch-069, the verified archive note records Signal Lantern Morning at South Meadow arch, juniper bundles. Case record id: distractor-069. Question: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-069. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); juniper bundles (aliases: event detail juniper bundles; juniper bundles in the correct event).
```

Chunk rank 2:

```text
document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Morning at South Meadow arch, silver booth token. Case record id: distractor-099. Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-099. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); silver booth token (aliases: event detail silver booth token; silver booth token in the correct event).
```

### Model: multilingual_e5_large

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
| 1 | 25066 | n/a | 0.8993 |
| 2 | 25067 | n/a | 0.8985 |
| 3 | 25126 | n/a | 0.8809 |
| 4 | 25127 | n/a | 0.8793 |
| 5 | 24805 | n/a | 0.8781 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-069. Scoped answer summary for distractor-069 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); juniper bundles (aliases: event detail juniper bundles; juniper bundles in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-069::distractor-069: In document distractor-south-meadow-arch-069, the verified archive note records Signal Lantern Morning at South Meadow arch, juniper bundles. Case record id: distractor-069. Question: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-069. Alias reminders for retrieval: Signal Lantern Morning at South Me

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-069::distractor-069: In document distractor-south-meadow-arch-069, the verified archive note records Signal Lantern Morning at South Meadow arch, juniper bundles. Case record id: distractor-069. Question: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-069. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); juniper bundles (aliases: event detail juniper bundles; juniper bundles in the correct event). Supplemental citation 1 for distractor-069 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-099. Scoped answer summary for distractor-099 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); silver booth token (aliases: event detail silver booth token; silver booth token in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Morning at South Meadow arch, silver booth token. Case record id: distractor-099. Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-099. Alias reminders for retrieval: Signal Lantern Morning a

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Morning at South Meadow arch, silver booth token. Case record id: distractor-099. Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-099. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); silver booth token (aliases: event detail silver booth token; silver booth token in the correct event). Supplemental citation 1 for distractor-099 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
document distractor-south-meadow-arch-069::distractor-069: In document distractor-south-meadow-arch-069, the verified archive note records Signal Lantern Morning at South Meadow arch, juniper bundles. Case record id: distractor-069. Question: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-069. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); juniper bundles (aliases: event detail juniper bundles; juniper bundles in the correct event).
```

## Question 070: distractor-070

**Question:** Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24269 | n/a | 0.8954 |
| 2 | 23941 | n/a | 0.8832 |

Chunk rank 1:

```text
Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry shed, smoke vent chain. Case record id: distractor-070. Question: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Scope reminder: document distractor-birch-ferry-shed-070. Alias reminders for retrieval: Lina of Birch Ferry shed (aliases: Lina from Birch Ferry shed; Birch Ferry shed Lina); smoke vent chain (aliases: correct object smoke vent chain; smoke vent chain in the true note). Supplemental citation 1 for distractor-070 repeats the verified marker set: Lina of Birch Ferry shed, Lina from Birch Ferry shed, Birch Ferry shed Lina. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry shed, smoke vent chain. Case record id: distractor-070. Question: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Scope reminder: document distractor-birch-ferry-shed-070. Alias reminders for retrieval: Lina of Birch Ferry shed (aliases: Lina from Birch Ferry shed; Birch Ferry shed Lina); smoke vent chain (aliases: correct object smoke vent chain; smoke vent chain in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 25069 | n/a | 0.8822 |
| 2 | 25068 | n/a | 0.8762 |
| 3 | 24741 | n/a | 0.8605 |
| 4 | 25009 | n/a | 0.8470 |
| 5 | 24979 | n/a | 0.8418 |

Chunk rank 1:

```text
Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry shed, smoke vent chain. Case record id: distractor-070. Question: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Scope reminder: document distractor-birch-ferry-shed-070. Alias reminders for retrieval: Lina of Birch Ferry shed (aliases: Lina from Birch Ferry shed; Birch Ferry shed Lina); smoke vent chain (aliases: correct object smoke vent chain; smoke vent chain in the true note). Supplemental citation 1 for distractor-070 repeats the verified marker set: Lina of Birch Ferry shed, Lina from Birch Ferry shed, Birch Ferry shed Lina. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Case scope id: distractor-070. Scoped answer summary for distractor-070 repeats the grounded evidence set: Lina of Birch Ferry shed (aliases: Lina from Birch Ferry shed; Birch Ferry shed Lina); smoke vent chain (aliases: correct object smoke vent chain; smoke vent chain in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry shed, smoke vent chain. Case record id: distractor-070. Question: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Scope reminder: document distractor-birch-ferry-shed-070. Alias reminders for retrieval: Lina of Birch Ferry shed (aliases: Lina from Birch Ferry shed; Birch Ferry shed Lina); smoke vent chain (aliases: correct object smoke vent chain; smoke vent chain in the true note).
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry shed, smoke vent chain. Case record id: distractor-070. Question: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Scope reminder: document distractor-birch-ferry-shed-070. Alias reminders for retrieval: Lina of Birch Ferry shed (aliases: Lina from Birch Ferry shed; Birch Ferry shed Lina); smoke vent chain (aliases: correct object smoke vent chain; smoke vent chain in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry shed, linen wick. Case record id: distractor-040. Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Scope reminder: document distractor-birch-ferry-shed-040. Alias reminders for retrieval: Mira of Birch Ferry shed (aliases: Mira from Birch Ferry shed; Birch Ferry shed Mira); linen wick (aliases: correct object linen wick; linen wick in the true note). Supplemental citation 1 for distractor-040 repeats the verified marker set: Mira of Birch Ferry shed, Mira from Birch Ferry shed, Birch Ferry shed Mira. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry shed, canal route map. Case record id: distractor-025. Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Scope reminder: document distractor-birch-ferry-shed-025. Alias reminders for retrieval: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note). Supplemental citation 1 for distractor-025 repeats the verified marker set: Anton of Birch Ferry shed, Anton from Birch Ferry shed, Birch Ferry shed Anton. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 071: distractor-071

**Question:** Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24271 | n/a | 0.9048 |
| 2 | 24151 | n/a | 0.9042 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `Lantern Row kiosk`
- Missing: `March 27 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 5.; Missing expected markers: March 27 Bellwater Fair; Evidence coverage below requirement: 0.500 < 1.000.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24981 | n/a | 0.8932 |
| 2 | 25101 | n/a | 0.8931 |
| 3 | 25011 | n/a | 0.8931 |
| 4 | 25041 | n/a | 0.8926 |
| 5 | 24951 | n/a | 0.8922 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-041 repeats the verified marker set: March 15 Bellwater Fair, Bellwater Fair on March 15, memory dated March 15. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-056::distractor-056: In document distractor-lantern-row-kiosk-056, the verified archive note records March 12 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-056. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-056. Alias reminders for retrieval: March 12 Bellwater Fair (aliases: Bellwater Fair on March 12; memory dated March 12); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-056 repeats the verified marker set: March 12 Bellwater Fair, Bellwater Fair on March 12, memory dated March 12. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 072: distractor-072

**Question:** Which place held the true profile detail for Yara, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, linen wick`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `partial`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24273 | n/a | 0.8616 |
| 2 | 24193 | n/a | 0.8601 |
| 3 | 24192 | n/a | 0.8546 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-cloud-wharf-office-072::distractor-072: In document distractor-cloud-wharf-office-072, the verified archive note records Cloud Wharf office, linen wick. Case record id: distractor-072. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-072. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); linen wick (aliases: profile detail linen wick; linen wick at Cloud Wharf office). Supplemental citation 1 for distractor-072 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-moon-mill-yard-032::distractor-032: In document distractor-moon-mill-yard-032, the verified archive note records Moon Mill yard, amber lantern. Case record id: distractor-032. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-032. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); amber lantern (aliases: profile detail amber lantern; amber lantern at Moon Mill yard). Supplemental citation 1 for distractor-032 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-032. Scoped answer summary for distractor-032 repeats the grounded evidence set: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); amber lantern (aliases: profile detail amber lantern; amber lantern at Moon Mill yard). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-moon-mill-yard-032::distractor-032: In document distractor-moon-mill-yard-032, the verified archive note records Moon Mill yard, amber lantern. Case record id: distractor-032. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-032. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); amber lantern (aliases: profile detail amber lantern; amber lantern at Moon Mill yard).
```

### Model: multilingual_e5_large

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, linen wick`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24993 | n/a | 0.8314 |
| 2 | 25073 | n/a | 0.8262 |
| 3 | 25072 | n/a | 0.8150 |
| 4 | 24992 | n/a | 0.8096 |
| 5 | 25053 | n/a | 0.8083 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-moon-mill-yard-032::distractor-032: In document distractor-moon-mill-yard-032, the verified archive note records Moon Mill yard, amber lantern. Case record id: distractor-032. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-032. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); amber lantern (aliases: profile detail amber lantern; amber lantern at Moon Mill yard). Supplemental citation 1 for distractor-032 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-cloud-wharf-office-072::distractor-072: In document distractor-cloud-wharf-office-072, the verified archive note records Cloud Wharf office, linen wick. Case record id: distractor-072. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-072. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); linen wick (aliases: profile detail linen wick; linen wick at Cloud Wharf office). Supplemental citation 1 for distractor-072 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-072. Scoped answer summary for distractor-072 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); linen wick (aliases: profile detail linen wick; linen wick at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-072::distractor-072: In document distractor-cloud-wharf-office-072, the verified archive note records Cloud Wharf office, linen wick. Case record id: distractor-072. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-072. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); linen wick (aliases: profile detail linen wick; linen wick at Cloud Wharf office).
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-032. Scoped answer summary for distractor-032 repeats the grounded evidence set: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); amber lantern (aliases: profile detail amber lantern; amber lantern at Moon Mill yard). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-moon-mill-yard-032::distractor-032: In document distractor-moon-mill-yard-032, the verified archive note records Moon Mill yard, amber lantern. Case record id: distractor-032. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-032. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); amber lantern (aliases: profile detail amber lantern; amber lantern at Moon Mill yard).
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-moon-mill-yard-062::distractor-062: In document distractor-moon-mill-yard-062, the verified archive note records Moon Mill yard, saffron scarf. Case record id: distractor-062. Question: Which place held the true profile detail for Talia, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-062. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); saffron scarf (aliases: profile detail saffron scarf; saffron scarf at Moon Mill yard). Supplemental citation 1 for distractor-062 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 073: distractor-073

**Question:** Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24275 | n/a | 0.8988 |
| 2 | 23999 | n/a | 0.8866 |
| 3 | 24274 | n/a | 0.8864 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev). Supplemental citation 1 for distractor-073 repeats the verified marker set: star ledger page, true object star ledger page, star ledger page in Lev's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev).
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-073. Scoped answer summary for distractor-073 repeats the grounded evidence set: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev).
```

### Model: multilingual_e5_large

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
| 1 | 25075 | n/a | 0.8848 |
| 2 | 25074 | n/a | 0.8699 |
| 3 | 24799 | n/a | 0.8663 |
| 4 | 24955 | n/a | 0.8515 |
| 5 | 25015 | n/a | 0.8468 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev). Supplemental citation 1 for distractor-073 repeats the verified marker set: star ledger page, true object star ledger page, star ledger page in Lev's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-073. Scoped answer summary for distractor-073 repeats the grounded evidence set: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev).
```

Chunk rank 3:

```text
document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev).
```

Chunk rank 4:

```text
Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna). Supplemental citation 1 for distractor-013 repeats the verified marker set: tin key, true object tin key, tin key in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap, Petar of Ridge Post loft. Case record id: distractor-043. Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-043. Alias reminders for retrieval: weathered camera strap (aliases: true object weathered camera strap; weathered camera strap in Petar's archive scene); Petar of Ridge Post loft (aliases: Petar from Ridge Post loft; Ridge Post loft scene of Petar). Supplemental citation 1 for distractor-043 repeats the verified marker set: weathered camera strap, true object weathered camera strap, weathered camera strap in Petar's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 074: distractor-074

**Question:** Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24018 | n/a | 0.8929 |
| 2 | 24277 | n/a | 0.8906 |
| 3 | 24276 | n/a | 0.8816 |

Chunk rank 1:

```text
document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lantern Morning at Willow Courtyard well, lantern hook. Case record id: distractor-074. Question: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-074. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); lantern hook (aliases: event detail lantern hook; lantern hook in the correct event).
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lantern Morning at Willow Courtyard well, lantern hook. Case record id: distractor-074. Question: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-074. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); lantern hook (aliases: event detail lantern hook; lantern hook in the correct event). Supplemental citation 1 for distractor-074 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-074. Scoped answer summary for distractor-074 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); lantern hook (aliases: event detail lantern hook; lantern hook in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lantern Morning at Willow Courtyard well, lantern hook. Case record id: distractor-074. Question: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-074. Alias reminders for retrieval: Signal Lan

[truncated in Markdown; full text is available in JSON]
```

### Model: multilingual_e5_large

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
| 1 | 25077 | n/a | 0.8944 |
| 2 | 25076 | n/a | 0.8906 |
| 3 | 24818 | n/a | 0.8727 |
| 4 | 24957 | n/a | 0.8699 |
| 5 | 24956 | n/a | 0.8689 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lantern Morning at Willow Courtyard well, lantern hook. Case record id: distractor-074. Question: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-074. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); lantern hook (aliases: event detail lantern hook; lantern hook in the correct event). Supplemental citation 1 for distractor-074 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-074. Scoped answer summary for distractor-074 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); lantern hook (aliases: event detail lantern hook; lantern hook in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lantern Morning at Willow Courtyard well, lantern hook. Case record id: distractor-074. Question: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-074. Alias reminders for retrieval: Signal Lan

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lantern Morning at Willow Courtyard well, lantern hook. Case record id: distractor-074. Question: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-074. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); lantern hook (aliases: event detail lantern hook; lantern hook in the correct event).
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event). Supplemental citation 1 for distractor-014 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting chunk restates

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-014. Scoped answer summary for distractor-014 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at

[truncated in Markdown; full text is available in JSON]
```

## Question 075: distractor-075

**Question:** Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24279 | n/a | 0.8862 |
| 2 | 23935 | n/a | 0.8746 |
| 3 | 24278 | n/a | 0.8675 |

Chunk rank 1:

```text
Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Bridge square, weathered camera strap. Case record id: distractor-075. Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Scope reminder: document distractor-bell-bridge-square-075. Alias reminders for retrieval: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (aliases: correct object weathered camera strap; weathered camera strap in the true note). Supplemental citation 1 for distractor-075 repeats the verified marker set: Pavel of Bell Bridge square, Pavel from Bell Bridge square, Bell Bridge square Pavel. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Bridge square, weathered camera strap. Case record id: distractor-075. Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Scope reminder: document distractor-bell-bridge-square-075. Alias reminders for retrieval: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (aliases: correct object weathered camera strap; weathered camera strap in the true note).
```

Chunk rank 3:

```text
Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Case scope id: distractor-075. Scoped answer summary for distractor-075 repeats the grounded evidence set: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (aliases: correct object weathered camera strap; weathered camera strap in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Bridge square, weathered camera strap. Case record id: distractor-075. Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Scope reminder: document distractor-bell-bridge-square-075. Alias reminders for retrieval: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (a

[truncated in Markdown; full text is available in JSON]
```

### Model: multilingual_e5_large

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
| 1 | 25079 | n/a | 0.8652 |
| 2 | 25078 | n/a | 0.8600 |
| 3 | 24735 | n/a | 0.8421 |
| 4 | 24999 | n/a | 0.8297 |
| 5 | 25019 | n/a | 0.8259 |

Chunk rank 1:

```text
Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Bridge square, weathered camera strap. Case record id: distractor-075. Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Scope reminder: document distractor-bell-bridge-square-075. Alias reminders for retrieval: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (aliases: correct object weathered camera strap; weathered camera strap in the true note). Supplemental citation 1 for distractor-075 repeats the verified marker set: Pavel of Bell Bridge square, Pavel from Bell Bridge square, Bell Bridge square Pavel. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Case scope id: distractor-075. Scoped answer summary for distractor-075 repeats the grounded evidence set: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (aliases: correct object weathered camera strap; weathered camera strap in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Bridge square, weathered camera strap. Case record id: distractor-075. Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Scope reminder: document distractor-bell-bridge-square-075. Alias reminders for retrieval: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (a

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Bridge square, weathered camera strap. Case record id: distractor-075. Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Scope reminder: document distractor-bell-bridge-square-075. Alias reminders for retrieval: Pavel of Bell Bridge square (aliases: Pavel from Bell Bridge square; Bell Bridge square Pavel); weathered camera strap (aliases: correct object weathered camera strap; weathered camera strap in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note). Supplemental citation 1 for distractor-035 repeats the verified marker set: Pavel of Star Basin gallery, Pavel from Star Basin gallery, Star Basin gallery Pavel. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell Bridge square, tin key. Case record id: distractor-045. Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Scope reminder: document distractor-bell-bridge-square-045. Alias reminders for retrieval: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note). Supplemental citation 1 for distractor-045 repeats the verified marker set: Stefan of Bell Bridge square, Stefan from Bell Bridge square, Bell Bridge square Stefan. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 076: distractor-076

**Question:** Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `Cedar Hill station`
- Missing: `March 14 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Missing expected evidence: March 14 Bellwater Fair`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24161 | n/a | 0.9059 |
| 2 | 24251 | n/a | 0.9051 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwater Fair, Cedar Hill station. Case record id: distractor-016. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-016. Alias reminders for retrieval: March 26 Bellwater Fair (aliases: Bellwater Fair on March 26; memory dated March 26); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-016 repeats the verified marker set: March 26 Bellwater Fair, Bellwater Fair on March 26, memory dated March 26. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25081 | n/a | 0.8963 |
| 2 | 24990 | n/a | 0.8954 |
| 3 | 25050 | n/a | 0.8951 |
| 4 | 24991 | n/a | 0.8949 |
| 5 | 25080 | n/a | 0.8946 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwater Fair, Cedar Hill station. Case record id: distractor-076. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-076. Alias reminders for retrieval: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-076 repeats the verified marker set: March 14 Bellwater Fair, Bellwater Fair on March 14, memory dated March 14. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-031. Scoped answer summary for distractor-031 repeats the grounded evidence set: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-061. Scoped answer summary for distractor-061 repeats the grounded evidence set: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-031 repeats the verified marker set: March 23 Bellwater Fair, Bellwater Fair on March 23, memory dated March 23. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-076. Scoped answer summary for distractor-076 repeats the grounded evidence set: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwater Fair, Cedar Hill station. Case record id: distractor-076. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-076. Alias reminders for retrieval: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

## Question 077: distractor-077

**Question:** Which place held the true profile detail for Damir, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Moon Mill yard, tin key`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `partial`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24283 | n/a | 0.8621 |
| 2 | 24203 | n/a | 0.8592 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-moon-mill-yard-077::distractor-077: In document distractor-moon-mill-yard-077, the verified archive note records Moon Mill yard, tin key. Case record id: distractor-077. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-077. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); tin key (aliases: profile detail tin key; tin key at Moon Mill yard). Supplemental citation 1 for distractor-077 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-blue-trunk-cabin-037::distractor-037: In document distractor-blue-trunk-cabin-037, the verified archive note records Blue Trunk cabin, juniper bundles. Case record id: distractor-037. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-037. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin). Supplemental citation 1 for distractor-037 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Moon Mill yard, tin key`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 25003 | n/a | 0.8211 |
| 2 | 25083 | n/a | 0.8146 |
| 3 | 25002 | n/a | 0.8075 |
| 4 | 25082 | n/a | 0.7998 |
| 5 | 24779 | n/a | 0.7921 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-blue-trunk-cabin-037::distractor-037: In document distractor-blue-trunk-cabin-037, the verified archive note records Blue Trunk cabin, juniper bundles. Case record id: distractor-037. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-037. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin). Supplemental citation 1 for distractor-037 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-moon-mill-yard-077::distractor-077: In document distractor-moon-mill-yard-077, the verified archive note records Moon Mill yard, tin key. Case record id: distractor-077. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-077. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); tin key (aliases: profile detail tin key; tin key at Moon Mill yard). Supplemental citation 1 for distractor-077 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-037. Scoped answer summary for distractor-037 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-037::distractor-037: In document distractor-blue-trunk-cabin-037, the verified archive note records Blue Trunk cabin, juniper bundles. Case record id: distractor-037. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-037. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); juniper bundles (aliases: profile detail juniper bundles; juniper bundles at Blue Trunk cabin).
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-077. Scoped answer summary for distractor-077 repeats the grounded evidence set: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); tin key (aliases: profile detail tin key; tin key at Moon Mill yard). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-moon-mill-yard-077::distractor-077: In document distractor-moon-mill-yard-077, the verified archive note records Moon Mill yard, tin key. Case record id: distractor-077. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-077. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); tin key (aliases: profile detail tin key; tin key at Moon Mill yard).
```

Chunk rank 5:

```text
document distractor-moon-mill-yard-077::distractor-077: In document distractor-moon-mill-yard-077, the verified archive note records Moon Mill yard, tin key. Case record id: distractor-077. Question: Which place held the true profile detail for Damir, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-077. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); tin key (aliases: profile detail tin key; tin key at Moon Mill yard).
```

## Question 078: distractor-078

**Question:** Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24285 | n/a | 0.8841 |
| 2 | 24284 | n/a | 0.8803 |
| 3 | 24024 | n/a | 0.8784 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa). Supplemental citation 1 for distractor-078 repeats the verified marker set: blue oar, true object blue oar, blue oar in Nessa's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-078. Scoped answer summary for distractor-078 repeats the grounded evidence set: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa).
```

Chunk rank 3:

```text
document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa).
```

### Model: multilingual_e5_large

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
| 1 | 25085 | n/a | 0.8721 |
| 2 | 25084 | n/a | 0.8690 |
| 3 | 24824 | n/a | 0.8654 |
| 4 | 25115 | n/a | 0.8471 |
| 5 | 24825 | n/a | 0.8460 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa). Supplemental citation 1 for distractor-078 repeats the verified marker set: blue oar, true object blue oar, blue oar in Nessa's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-078. Scoped answer summary for distractor-078 repeats the grounded evidence set: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa).
```

Chunk rank 3:

```text
document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Nessa of Winter Chapel porch. Case record id: distractor-078. Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-078. Alias reminders for retrieval: blue oar (aliases: true object blue oar; blue oar in Nessa's archive scene); Nessa of Winter Chapel porch (aliases: Nessa from Winter Chapel porch; Winter Chapel porch scene of Nessa).
```

Chunk rank 4:

```text
Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna). Supplemental citation 1 for distractor-093 repeats the verified marker set: birch tea flask, true object birch tea flask, birch tea flask in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna).
```

## Question 079: distractor-079

**Question:** Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24287 | n/a | 0.9026 |
| 2 | 23973 | n/a | 0.8965 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Morning at Marble stair hall, willow basket. Case record id: distractor-079. Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-079. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); willow basket (aliases: event detail willow basket; willow basket in the correct event). Supplemental citation 1 for distractor-079 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Morning at Marble stair hall, willow basket. Case record id: distractor-079. Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-079. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); willow basket (aliases: event detail willow basket; willow basket in the correct event).
```

### Model: multilingual_e5_large

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
| 1 | 25087 | n/a | 0.8977 |
| 2 | 25086 | n/a | 0.8924 |
| 3 | 24773 | n/a | 0.8791 |
| 4 | 25027 | n/a | 0.8740 |
| 5 | 25117 | n/a | 0.8731 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Morning at Marble stair hall, willow basket. Case record id: distractor-079. Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-079. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); willow basket (aliases: event detail willow basket; willow basket in the correct event). Supplemental citation 1 for distractor-079 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-079. Scoped answer summary for distractor-079 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); willow basket (aliases: event detail willow basket; willow basket in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Morning at Marble stair hall, willow basket. Case record id: distractor-079. Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-079. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Morning at Marble stair hall, willow basket. Case record id: distractor-079. Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-079. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); willow basket (aliases: event detail willow basket; willow basket in the correct event).
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-049::distractor-049: In document distractor-marble-stair-hall-049, the verified archive note records Signal Lantern Morning at Marble stair hall, glass ink bottle. Case record id: distractor-049. Question: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-049. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); glass ink bottle (aliases: event detail glass ink bottle; glass ink bottle in the correct event). Supplemental citation 1 for distractor-049 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event). Supplemental citation 1 for distractor-094 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 080: distractor-080

**Question:** Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24289 | n/a | 0.8921 |
| 2 | 24012 | n/a | 0.8824 |

Chunk rank 1:

```text
Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Basin gallery, paper moon mask. Case record id: distractor-080. Question: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Scope reminder: document distractor-star-basin-gallery-080. Alias reminders for retrieval: Mira of Star Basin gallery (aliases: Mira from Star Basin gallery; Star Basin gallery Mira); paper moon mask (aliases: correct object paper moon mask; paper moon mask in the true note). Supplemental citation 1 for distractor-080 repeats the verified marker set: Mira of Star Basin gallery, Mira from Star Basin gallery, Star Basin gallery Mira. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Basin gallery, paper moon mask. Case record id: distractor-080. Question: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Scope reminder: document distractor-star-basin-gallery-080. Alias reminders for retrieval: Mira of Star Basin gallery (aliases: Mira from Star Basin gallery; Star Basin gallery Mira); paper moon mask (aliases: correct object paper moon mask; paper moon mask in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 25089 | n/a | 0.8611 |
| 2 | 25088 | n/a | 0.8554 |
| 3 | 24812 | n/a | 0.8470 |
| 4 | 25059 | n/a | 0.8293 |
| 5 | 24999 | n/a | 0.8256 |

Chunk rank 1:

```text
Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Basin gallery, paper moon mask. Case record id: distractor-080. Question: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Scope reminder: document distractor-star-basin-gallery-080. Alias reminders for retrieval: Mira of Star Basin gallery (aliases: Mira from Star Basin gallery; Star Basin gallery Mira); paper moon mask (aliases: correct object paper moon mask; paper moon mask in the true note). Supplemental citation 1 for distractor-080 repeats the verified marker set: Mira of Star Basin gallery, Mira from Star Basin gallery, Star Basin gallery Mira. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Case scope id: distractor-080. Scoped answer summary for distractor-080 repeats the grounded evidence set: Mira of Star Basin gallery (aliases: Mira from Star Basin gallery; Star Basin gallery Mira); paper moon mask (aliases: correct object paper moon mask; paper moon mask in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Basin gallery, paper moon mask. Case record id: distractor-080. Question: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Scope reminder: document distractor-star-basin-gallery-080. Alias reminders for retrieval: Mira of Star Basin gallery (aliases: Mira from Star Basin gallery; Star Basin gallery Mira); paper moon mask (aliases: correct object paper moon mask; paper moon mask in the true note).
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Basin gallery, paper moon mask. Case record id: distractor-080. Question: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Scope reminder: document distractor-star-basin-gallery-080. Alias reminders for retrieval: Mira of Star Basin gallery (aliases: Mira from Star Basin gallery; Star Basin gallery Mira); paper moon mask (aliases: correct object paper moon mask; paper moon mask in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Basin gallery, basalt sketch. Case record id: distractor-065. Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Scope reminder: document distractor-star-basin-gallery-065. Alias reminders for retrieval: Anton of Star Basin gallery (aliases: Anton from Star Basin gallery; Star Basin gallery Anton); basalt sketch (aliases: correct object basalt sketch; basalt sketch in the true note). Supplemental citation 1 for distractor-065 repeats the verified marker set: Anton of Star Basin gallery, Anton from Star Basin gallery, Star Basin gallery Anton. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Basin gallery, silver booth token. Case record id: distractor-035. Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Scope reminder: document distractor-star-basin-gallery-035. Alias reminders for retrieval: Pavel of Star Basin gallery (aliases: Pavel from Star Basin gallery; Star Basin gallery Pavel); silver booth token (aliases: correct object silver booth token; silver booth token in the true note). Supplemental citation 1 for distractor-035 repeats the verified marker set: Pavel of Star Basin gallery, Pavel from Star Basin gallery, Star Basin gallery Pavel. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 081: distractor-081

**Question:** Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24291 | n/a | 0.8980 |
| 2 | 24171 | n/a | 0.8961 |
| 3 | 24231 | n/a | 0.8948 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellwater Fair, North Bell workshop. Case record id: distractor-081. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-081. Alias reminders for retrieval: March 19 Bellwater Fair (aliases: Bellwater Fair on March 19; memory dated March 19); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-081 repeats the verified marker set: March 19 Bellwater Fair, Bellwater Fair on March 19, memory dated March 19. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-051::distractor-051: In document distractor-north-bell-workshop-051, the verified archive note records March 25 Bellwater Fair, North Bell workshop. Case record id: distractor-051. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-051. Alias reminders for retrieval: March 25 Bellwater Fair (aliases: Bellwater Fair on March 25; memory dated March 25); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-051 repeats the verified marker set: March 25 Bellwater Fair, Bellwater Fair on March 25, memory dated March 25. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `North Bell workshop`
- Missing: `March 19 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 5.; Missing expected markers: March 19 Bellwater Fair; Evidence coverage below requirement: 0.500 < 1.000.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 25001 | n/a | 0.8858 |
| 2 | 25061 | n/a | 0.8847 |
| 3 | 25121 | n/a | 0.8845 |
| 4 | 25060 | n/a | 0.8840 |
| 5 | 24941 | n/a | 0.8835 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-096 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. Scoped answer summary for distractor-066 repeats the grounded evidence set: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 082: distractor-082

**Question:** Which place held the true profile detail for Kira, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24293 | n/a | 0.8527 |
| 2 | 24213 | n/a | 0.8449 |
| 3 | 24233 | n/a | 0.8327 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor-082: In document distractor-blue-trunk-cabin-082, the verified archive note records Blue Trunk cabin, copper wind vane pin. Case record id: distractor-082. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-082. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); copper wind vane pin (aliases: profile detail copper wind vane pin; copper wind vane pin at Blue Trunk cabin). Supplemental citation 1 for distractor-082 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-cloud-wharf-office-042::distractor-042: In document distractor-cloud-wharf-office-042, the verified archive note records Cloud Wharf office, lantern hook. Case record id: distractor-042. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-042. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); lantern hook (aliases: profile detail lantern hook; lantern hook at Cloud Wharf office). Supplemental citation 1 for distractor-042 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor-052: In document distractor-blue-trunk-cabin-052, the verified archive note records Blue Trunk cabin, violet ribbon. Case record id: distractor-052. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-052. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin). Supplemental citation 1 for distractor-052 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25013 | n/a | 0.8334 |
| 2 | 25093 | n/a | 0.8193 |
| 3 | 25012 | n/a | 0.8117 |
| 4 | 24759 | n/a | 0.8004 |
| 5 | 24993 | n/a | 0.8004 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-cloud-wharf-office-042::distractor-042: In document distractor-cloud-wharf-office-042, the verified archive note records Cloud Wharf office, lantern hook. Case record id: distractor-042. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-042. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); lantern hook (aliases: profile detail lantern hook; lantern hook at Cloud Wharf office). Supplemental citation 1 for distractor-042 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor-082: In document distractor-blue-trunk-cabin-082, the verified archive note records Blue Trunk cabin, copper wind vane pin. Case record id: distractor-082. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-082. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); copper wind vane pin (aliases: profile detail copper wind vane pin; copper wind vane pin at Blue Trunk cabin). Supplemental citation 1 for distractor-082 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? Case scope id: distractor-042. Scoped answer summary for distractor-042 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); lantern hook (aliases: profile detail lantern hook; lantern hook at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-042::distractor-042: In document distractor-cloud-wharf-office-042, the verified archive note records Cloud Wharf office, lantern hook. Case record id: distractor-042. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-042. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); lantern hook (aliases: profile detail lantern hook; lantern hook at Cloud Wharf office).
```

Chunk rank 4:

```text
document distractor-cloud-wharf-office-042::distractor-042: In document distractor-cloud-wharf-office-042, the verified archive note records Cloud Wharf office, lantern hook. Case record id: distractor-042. Question: Which place held the true profile detail for Kira, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-042. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); lantern hook (aliases: profile detail lantern hook; lantern hook at Cloud Wharf office).
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-moon-mill-yard-032::distractor-032: In document distractor-moon-mill-yard-032, the verified archive note records Moon Mill yard, amber lantern. Case record id: distractor-032. Question: Which place held the true profile detail for Yara, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-032. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); amber lantern (aliases: profile detail amber lantern; amber lantern at Moon Mill yard). Supplemental citation 1 for distractor-032 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 083: distractor-083

**Question:** Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 23993 | n/a | 0.8791 |
| 2 | 24295 | n/a | 0.8785 |

Chunk rank 1:

```text
document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss, Petar of North Orchard lane. Case record id: distractor-083. Question: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-083. Alias reminders for retrieval: coal stove hiss (aliases: true object coal stove hiss; coal stove hiss in Petar's archive scene); Petar of North Orchard lane (aliases: Petar from North Orchard lane; North Orchard lane scene of Petar).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss, Petar of North Orchard lane. Case record id: distractor-083. Question: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-083. Alias reminders for retrieval: coal stove hiss (aliases: true object coal stove hiss; coal stove hiss in Petar's archive scene); Petar of North Orchard lane (aliases: Petar from North Orchard lane; North Orchard lane scene of Petar). Supplemental citation 1 for distractor-083 repeats the verified marker set: coal stove hiss, true object coal stove hiss, coal stove hiss in Petar's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25095 | n/a | 0.8628 |
| 2 | 25094 | n/a | 0.8578 |
| 3 | 24793 | n/a | 0.8556 |
| 4 | 24975 | n/a | 0.8437 |
| 5 | 24789 | n/a | 0.8368 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss, Petar of North Orchard lane. Case record id: distractor-083. Question: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-083. Alias reminders for retrieval: coal stove hiss (aliases: true object coal stove hiss; coal stove hiss in Petar's archive scene); Petar of North Orchard lane (aliases: Petar from North Orchard lane; North Orchard lane scene of Petar). Supplemental citation 1 for distractor-083 repeats the verified marker set: coal stove hiss, true object coal stove hiss, coal stove hiss in Petar's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-083. Scoped answer summary for distractor-083 repeats the grounded evidence set: coal stove hiss (aliases: true object coal stove hiss; coal stove hiss in Petar's archive scene); Petar of North Orchard lane (aliases: Petar from North Orchard lane; North Orchard lane scene of Petar). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss, Petar of North Orchard lane. Case record id: distractor-083. Question: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-083. Alias reminders for retrieval: coal stove hiss (aliases: true object coal stove hiss; coal stove hiss in Petar's archive scene); P

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss, Petar of North Orchard lane. Case record id: distractor-083. Question: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-083. Alias reminders for retrieval: coal stove hiss (aliases: true object coal stove hiss; coal stove hiss in Petar's archive scene); Petar of North Orchard lane (aliases: Petar from North Orchard lane; North Orchard lane scene of Petar).
```

Chunk rank 4:

```text
Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor). Supplemental citation 1 for distractor-023 repeats the verified marker set: oak barrel hoops, true object oak barrel hoops, oak barrel hoops in Viktor's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor).
```

## Question 084: distractor-084

**Question:** Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24006 | n/a | 0.9035 |
| 2 | 24297 | n/a | 0.8963 |
| 3 | 24296 | n/a | 0.8943 |

Chunk rank 1:

```text
document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Morning at South Meadow arch, violet ribbon. Case record id: distractor-084. Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-084. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); violet ribbon (aliases: event detail violet ribbon; violet ribbon in the correct event).
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Morning at South Meadow arch, violet ribbon. Case record id: distractor-084. Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-084. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); violet ribbon (aliases: event detail violet ribbon; violet ribbon in the correct event). Supplemental citation 1 for distractor-084 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-084. Scoped answer summary for distractor-084 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); violet ribbon (aliases: event detail violet ribbon; violet ribbon in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Morning at South Meadow arch, violet ribbon. Case record id: distractor-084. Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-084. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch

[truncated in Markdown; full text is available in JSON]
```

### Model: multilingual_e5_large

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
| 1 | 25097 | n/a | 0.9013 |
| 2 | 25096 | n/a | 0.8969 |
| 3 | 24977 | n/a | 0.8788 |
| 4 | 24976 | n/a | 0.8788 |
| 5 | 25036 | n/a | 0.8779 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Morning at South Meadow arch, violet ribbon. Case record id: distractor-084. Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-084. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); violet ribbon (aliases: event detail violet ribbon; violet ribbon in the correct event). Supplemental citation 1 for distractor-084 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-084. Scoped answer summary for distractor-084 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); violet ribbon (aliases: event detail violet ribbon; violet ribbon in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Morning at South Meadow arch, violet ribbon. Case record id: distractor-084. Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-084. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Morning at South Meadow arch, blue glass jar. Case record id: distractor-024. Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-024. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); blue glass jar (aliases: event detail blue glass jar; blue glass jar in the correct event). Supplemental citation 1 for distractor-024 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-024. Scoped answer summary for distractor-024 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); blue glass jar (aliases: event detail blue glass jar; blue glass jar in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Morning at South Meadow arch, blue glass jar. Case record id: distractor-024. Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-024. Alias reminders for retrieval: Signal Lantern Morning at South Meadow

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-054. Scoped answer summary for distractor-054 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); rope bridge permit (aliases: event detail rope bridge permit; rope bridge permit in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Morning at South Meadow arch, rope bridge permit. Case record id: distractor-054. Question: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-054. Alias reminders for retrieval: Signal Lantern Morning

[truncated in Markdown; full text is available in JSON]
```

## Question 085: distractor-085

**Question:** Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24299 | n/a | 0.8970 |
| 2 | 24298 | n/a | 0.8863 |

Chunk rank 1:

```text
Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? document distractor-birch-ferry-shed-085::distractor-085: In document distractor-birch-ferry-shed-085, the verified archive note records Stefan of Birch Ferry shed, tuning fork. Case record id: distractor-085. Question: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Scope reminder: document distractor-birch-ferry-shed-085. Alias reminders for retrieval: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note). Supplemental citation 1 for distractor-085 repeats the verified marker set: Stefan of Birch Ferry shed, Stefan from Birch Ferry shed, Birch Ferry shed Stefan. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Case scope id: distractor-085. Scoped answer summary for distractor-085 repeats the grounded evidence set: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-085::distractor-085: In document distractor-birch-ferry-shed-085, the verified archive note records Stefan of Birch Ferry shed, tuning fork. Case record id: distractor-085. Question: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Scope reminder: document distractor-birch-ferry-shed-085. Alias reminders for retrieval: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 25099 | n/a | 0.8766 |
| 2 | 25098 | n/a | 0.8692 |
| 3 | 24742 | n/a | 0.8559 |
| 4 | 25019 | n/a | 0.8374 |
| 5 | 24979 | n/a | 0.8372 |

Chunk rank 1:

```text
Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? document distractor-birch-ferry-shed-085::distractor-085: In document distractor-birch-ferry-shed-085, the verified archive note records Stefan of Birch Ferry shed, tuning fork. Case record id: distractor-085. Question: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Scope reminder: document distractor-birch-ferry-shed-085. Alias reminders for retrieval: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note). Supplemental citation 1 for distractor-085 repeats the verified marker set: Stefan of Birch Ferry shed, Stefan from Birch Ferry shed, Birch Ferry shed Stefan. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Case scope id: distractor-085. Scoped answer summary for distractor-085 repeats the grounded evidence set: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-085::distractor-085: In document distractor-birch-ferry-shed-085, the verified archive note records Stefan of Birch Ferry shed, tuning fork. Case record id: distractor-085. Question: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Scope reminder: document distractor-birch-ferry-shed-085. Alias reminders for retrieval: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note).
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-085::distractor-085: In document distractor-birch-ferry-shed-085, the verified archive note records Stefan of Birch Ferry shed, tuning fork. Case record id: distractor-085. Question: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Scope reminder: document distractor-birch-ferry-shed-085. Alias reminders for retrieval: Stefan of Birch Ferry shed (aliases: Stefan from Birch Ferry shed; Birch Ferry shed Stefan); tuning fork (aliases: correct object tuning fork; tuning fork in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell Bridge square, tin key. Case record id: distractor-045. Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Scope reminder: document distractor-bell-bridge-square-045. Alias reminders for retrieval: Stefan of Bell Bridge square (aliases: Stefan from Bell Bridge square; Bell Bridge square Stefan); tin key (aliases: correct object tin key; tin key in the true note). Supplemental citation 1 for distractor-045 repeats the verified marker set: Stefan of Bell Bridge square, Stefan from Bell Bridge square, Bell Bridge square Stefan. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry shed, canal route map. Case record id: distractor-025. Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Scope reminder: document distractor-birch-ferry-shed-025. Alias reminders for retrieval: Anton of Birch Ferry shed (aliases: Anton from Birch Ferry shed; Birch Ferry shed Anton); canal route map (aliases: correct object canal route map; canal route map in the true note). Supplemental citation 1 for distractor-025 repeats the verified marker set: Anton of Birch Ferry shed, Anton from Birch Ferry shed, Birch Ferry shed Anton. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 086: distractor-086

**Question:** Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `Lantern Row kiosk`
- Missing: `March 24 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Missing expected evidence: March 24 Bellwater Fair`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24271 | n/a | 0.9048 |
| 2 | 24151 | n/a | 0.9042 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-071. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-071. Alias reminders for retrieval: March 27 Bellwater Fair (aliases: Bellwater Fair on March 27; memory dated March 27); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-071 repeats the verified marker set: March 27 Bellwater Fair, Bellwater Fair on March 27, memory dated March 27. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 24981 | n/a | 0.8932 |
| 2 | 25101 | n/a | 0.8931 |
| 3 | 25011 | n/a | 0.8931 |
| 4 | 25041 | n/a | 0.8926 |
| 5 | 24951 | n/a | 0.8922 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-026. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-026. Alias reminders for retrieval: March 18 Bellwater Fair (aliases: Bellwater Fair on March 18; memory dated March 18); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-026 repeats the verified marker set: March 18 Bellwater Fair, Bellwater Fair on March 18, memory dated March 18. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-086. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-086. Alias reminders for retrieval: March 24 Bellwater Fair (aliases: Bellwater Fair on March 24; memory dated March 24); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-086 repeats the verified marker set: March 24 Bellwater Fair, Bellwater Fair on March 24, memory dated March 24. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-041. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-041. Alias reminders for retrieval: March 15 Bellwater Fair (aliases: Bellwater Fair on March 15; memory dated March 15); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-041 repeats the verified marker set: March 15 Bellwater Fair, Bellwater Fair on March 15, memory dated March 15. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-056::distractor-056: In document distractor-lantern-row-kiosk-056, the verified archive note records March 12 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-056. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-056. Alias reminders for retrieval: March 12 Bellwater Fair (aliases: Bellwater Fair on March 12; memory dated March 12); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-056 repeats the verified marker set: March 12 Bellwater Fair, Bellwater Fair on March 12, memory dated March 12. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater Fair, Lantern Row kiosk. Case record id: distractor-011. Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Scope reminder: document distractor-lantern-row-kiosk-011. Alias reminders for retrieval: March 21 Bellwater Fair (aliases: Bellwater Fair on March 21; memory dated March 21); Lantern Row kiosk (aliases: site Lantern Row kiosk; the place Lantern Row kiosk). Supplemental citation 1 for distractor-011 repeats the verified marker set: March 21 Bellwater Fair, Bellwater Fair on March 21, memory dated March 21. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 087: distractor-087

**Question:** Which place held the true profile detail for Nikola, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, oak barrel hoops`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `partial`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24303 | n/a | 0.8634 |
| 2 | 24223 | n/a | 0.8624 |
| 3 | 24143 | n/a | 0.8517 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distractor-087: In document distractor-cloud-wharf-office-087, the verified archive note records Cloud Wharf office, oak barrel hoops. Case record id: distractor-087. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-087. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); oak barrel hoops (aliases: profile detail oak barrel hoops; oak barrel hoops at Cloud Wharf office). Supplemental citation 1 for distractor-087 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-moon-mill-yard-047::distractor-047: In document distractor-moon-mill-yard-047, the verified archive note records Moon Mill yard, willow basket. Case record id: distractor-047. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-047. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); willow basket (aliases: profile detail willow basket; willow basket at Moon Mill yard). Supplemental citation 1 for distractor-047 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distractor-007: In document distractor-blue-trunk-cabin-007, the verified archive note records Blue Trunk cabin, brass compass. Case record id: distractor-007. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-007. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); brass compass (aliases: profile detail brass compass; brass compass at Blue Trunk cabin). Supplemental citation 1 for distractor-007 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Cloud Wharf office, oak barrel hoops`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 25103 | n/a | 0.8328 |
| 2 | 25023 | n/a | 0.8240 |
| 3 | 25102 | n/a | 0.8195 |
| 4 | 24943 | n/a | 0.8162 |
| 5 | 25022 | n/a | 0.8099 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distractor-087: In document distractor-cloud-wharf-office-087, the verified archive note records Cloud Wharf office, oak barrel hoops. Case record id: distractor-087. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-087. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); oak barrel hoops (aliases: profile detail oak barrel hoops; oak barrel hoops at Cloud Wharf office). Supplemental citation 1 for distractor-087 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-moon-mill-yard-047::distractor-047: In document distractor-moon-mill-yard-047, the verified archive note records Moon Mill yard, willow basket. Case record id: distractor-047. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-047. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); willow basket (aliases: profile detail willow basket; willow basket at Moon Mill yard). Supplemental citation 1 for distractor-047 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-087. Scoped answer summary for distractor-087 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); oak barrel hoops (aliases: profile detail oak barrel hoops; oak barrel hoops at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-087::distractor-087: In document distractor-cloud-wharf-office-087, the verified archive note records Cloud Wharf office, oak barrel hoops. Case record id: distractor-087. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-087. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); oak barrel hoops (aliases: profile detail oak barrel hoops; oak barrel hoops at Cloud Wharf office).
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distractor-007: In document distractor-blue-trunk-cabin-007, the verified archive note records Blue Trunk cabin, brass compass. Case record id: distractor-007. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-007. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); brass compass (aliases: profile detail brass compass; brass compass at Blue Trunk cabin). Supplemental citation 1 for distractor-007 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-047. Scoped answer summary for distractor-047 repeats the grounded evidence set: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); willow basket (aliases: profile detail willow basket; willow basket at Moon Mill yard). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-moon-mill-yard-047::distractor-047: In document distractor-moon-mill-yard-047, the verified archive note records Moon Mill yard, willow basket. Case record id: distractor-047. Question: Which place held the true profile detail for Nikola, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-047. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); willow basket (aliases: profile detail willow basket; willow basket at Moon Mill yard).
```

## Question 088: distractor-088

**Question:** Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24305 | n/a | 0.8779 |
| 2 | 24304 | n/a | 0.8729 |
| 3 | 24000 | n/a | 0.8668 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya of Ridge Post loft. Case record id: distractor-088. Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-088. Alias reminders for retrieval: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya). Supplemental citation 1 for distractor-088 repeats the verified marker set: blue glass jar, true object blue glass jar, blue glass jar in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-088. Scoped answer summary for distractor-088 repeats the grounded evidence set: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya of Ridge Post loft. Case record id: distractor-088. Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-088. Alias reminders for retrieval: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya).
```

Chunk rank 3:

```text
document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya of Ridge Post loft. Case record id: distractor-088. Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-088. Alias reminders for retrieval: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya).
```

### Model: multilingual_e5_large

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
| 1 | 25105 | n/a | 0.8735 |
| 2 | 24800 | n/a | 0.8600 |
| 3 | 25104 | n/a | 0.8512 |
| 4 | 25075 | n/a | 0.8506 |
| 5 | 24955 | n/a | 0.8458 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya of Ridge Post loft. Case record id: distractor-088. Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-088. Alias reminders for retrieval: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya). Supplemental citation 1 for distractor-088 repeats the verified marker set: blue glass jar, true object blue glass jar, blue glass jar in Sonya's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya of Ridge Post loft. Case record id: distractor-088. Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-088. Alias reminders for retrieval: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya).
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-088. Scoped answer summary for distractor-088 repeats the grounded evidence set: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya of Ridge Post loft. Case record id: distractor-088. Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-088. Alias reminders for retrieval: blue glass jar (aliases: true object blue glass jar; blue glass jar in Sonya's archive scene); Sonya of Ridge Post loft (aliases: Sonya from Ridge Post loft; Ridge Post loft scene of Sonya).
```

Chunk rank 4:

```text
Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev of Ridge Post loft. Case record id: distractor-073. Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-073. Alias reminders for retrieval: star ledger page (aliases: true object star ledger page; star ledger page in Lev's archive scene); Lev of Ridge Post loft (aliases: Lev from Ridge Post loft; Ridge Post loft scene of Lev). Supplemental citation 1 for distractor-073 repeats the verified marker set: star ledger page, true object star ledger page, star ledger page in Lev's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna). Supplemental citation 1 for distractor-013 repeats the verified marker set: tin key, true object tin key, tin key in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 089: distractor-089

**Question:** Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Willow Courtyard well, canal route map`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24307 | n/a | 0.8940 |
| 2 | 24019 | n/a | 0.8928 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-089::distractor-089: In document distractor-willow-courtyard-well-089, the verified archive note records Signal Lantern Morning at Willow Courtyard well, canal route map. Case record id: distractor-089. Question: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-089. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); canal route map (aliases: event detail canal route map; canal route map in the correct event). Supplemental citation 1 for distractor-089 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
document distractor-willow-courtyard-well-089::distractor-089: In document distractor-willow-courtyard-well-089, the verified archive note records Signal Lantern Morning at Willow Courtyard well, canal route map. Case record id: distractor-089. Question: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-089. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); canal route map (aliases: event detail canal route map; canal route map in the correct event).
```

### Model: multilingual_e5_large

- Status: `PASS`
- Coverage: `1.0000`
- Matched: `Signal Lantern Morning at Willow Courtyard well, canal route map`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `n/a`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 25107 | n/a | 0.8919 |
| 2 | 25106 | n/a | 0.8883 |
| 3 | 24819 | n/a | 0.8744 |
| 4 | 24957 | n/a | 0.8733 |
| 5 | 24956 | n/a | 0.8721 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-089::distractor-089: In document distractor-willow-courtyard-well-089, the verified archive note records Signal Lantern Morning at Willow Courtyard well, canal route map. Case record id: distractor-089. Question: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-089. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); canal route map (aliases: event detail canal route map; canal route map in the correct event). Supplemental citation 1 for distractor-089 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-089. Scoped answer summary for distractor-089 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); canal route map (aliases: event detail canal route map; canal route map in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-089::distractor-089: In document distractor-willow-courtyard-well-089, the verified archive note records Signal Lantern Morning at Willow Courtyard well, canal route map. Case record id: distractor-089. Question: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-089. Alias reminders for retrieval:

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-willow-courtyard-well-089::distractor-089: In document distractor-willow-courtyard-well-089, the verified archive note records Signal Lantern Morning at Willow Courtyard well, canal route map. Case record id: distractor-089. Question: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-089. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); canal route map (aliases: event detail canal route map; canal route map in the correct event).
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event). Supplemental citation 1 for distractor-014 repeats the verified marker set: Signal Lantern Morning at Willow Courtyard well, Signal Lantern Morning memory at Willow Courtyard well, event Signal Lantern Morning in Willow Courtyard well. This eval-only supporting chunk restates

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distractor-014. Scoped answer summary for distractor-014 repeats the grounded evidence set: Signal Lantern Morning at Willow Courtyard well (aliases: Signal Lantern Morning memory at Willow Courtyard well; event Signal Lantern Morning in Willow Courtyard well); blue oar (aliases: event detail blue oar; blue oar in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lantern Morning at Willow Courtyard well, blue oar. Case record id: distractor-014. Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Scope reminder: document distractor-willow-courtyard-well-014. Alias reminders for retrieval: Signal Lantern Morning at

[truncated in Markdown; full text is available in JSON]
```

## Question 090: distractor-090

**Question:** Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24309 | n/a | 0.8883 |
| 2 | 23936 | n/a | 0.8769 |

Chunk rank 1:

```text
Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Bridge square, cedar shovel. Case record id: distractor-090. Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Scope reminder: document distractor-bell-bridge-square-090. Alias reminders for retrieval: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note). Supplemental citation 1 for distractor-090 repeats the verified marker set: Selma of Bell Bridge square, Selma from Bell Bridge square, Bell Bridge square Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Bridge square, cedar shovel. Case record id: distractor-090. Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Scope reminder: document distractor-bell-bridge-square-090. Alias reminders for retrieval: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 25109 | n/a | 0.8696 |
| 2 | 25108 | n/a | 0.8650 |
| 3 | 24736 | n/a | 0.8486 |
| 4 | 24949 | n/a | 0.8339 |
| 5 | 24948 | n/a | 0.8257 |

Chunk rank 1:

```text
Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Bridge square, cedar shovel. Case record id: distractor-090. Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Scope reminder: document distractor-bell-bridge-square-090. Alias reminders for retrieval: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note). Supplemental citation 1 for distractor-090 repeats the verified marker set: Selma of Bell Bridge square, Selma from Bell Bridge square, Bell Bridge square Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Case scope id: distractor-090. Scoped answer summary for distractor-090 repeats the grounded evidence set: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Bridge square, cedar shovel. Case record id: distractor-090. Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Scope reminder: document distractor-bell-bridge-square-090. Alias reminders for retrieval: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note).
```

Chunk rank 3:

```text
document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Bridge square, cedar shovel. Case record id: distractor-090. Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Scope reminder: document distractor-bell-bridge-square-090. Alias reminders for retrieval: Selma of Bell Bridge square (aliases: Selma from Bell Bridge square; Bell Bridge square Selma); cedar shovel (aliases: correct object cedar shovel; cedar shovel in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry shed, lantern hook. Case record id: distractor-010. Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Scope reminder: document distractor-birch-ferry-shed-010. Alias reminders for retrieval: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note). Supplemental citation 1 for distractor-010 repeats the verified marker set: Selma of Birch Ferry shed, Selma from Birch Ferry shed, Birch Ferry shed Selma. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Case scope id: distractor-010. Scoped answer summary for distractor-010 repeats the grounded evidence set: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry shed, lantern hook. Case record id: distractor-010. Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Scope reminder: document distractor-birch-ferry-shed-010. Alias reminders for retrieval: Selma of Birch Ferry shed (aliases: Selma from Birch Ferry shed; Birch Ferry shed Selma); lantern hook (aliases: correct object lantern hook; lantern hook in the true note).
```

## Question 091: distractor-091

**Question:** Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `Cedar Hill station`
- Missing: `March 11 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Missing expected evidence: March 11 Bellwater Fair`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24161 | n/a | 0.9059 |
| 2 | 24251 | n/a | 0.9051 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwater Fair, Cedar Hill station. Case record id: distractor-016. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-016. Alias reminders for retrieval: March 26 Bellwater Fair (aliases: Bellwater Fair on March 26; memory dated March 26); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-016 repeats the verified marker set: March 26 Bellwater Fair, Bellwater Fair on March 26, memory dated March 26. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-061 repeats the verified marker set: March 17 Bellwater Fair, Bellwater Fair on March 17, memory dated March 17. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `Cedar Hill station`
- Missing: `March 11 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Case did not satisfy the expected retrieval quality checks.; Relevant results found: 5.; Missing expected markers: March 11 Bellwater Fair; Evidence coverage below requirement: 0.500 < 1.000.`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 25081 | n/a | 0.8963 |
| 2 | 24990 | n/a | 0.8954 |
| 3 | 25050 | n/a | 0.8951 |
| 4 | 24991 | n/a | 0.8949 |
| 5 | 25080 | n/a | 0.8946 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwater Fair, Cedar Hill station. Case record id: distractor-076. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-076. Alias reminders for retrieval: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-076 repeats the verified marker set: March 14 Bellwater Fair, Bellwater Fair on March 14, memory dated March 14. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-031. Scoped answer summary for distractor-031 repeats the grounded evidence set: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-061. Scoped answer summary for distractor-061 repeats the grounded evidence set: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwater Fair, Cedar Hill station. Case record id: distractor-061. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-061. Alias reminders for retrieval: March 17 Bellwater Fair (aliases: Bellwater Fair on March 17; memory dated March 17); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwater Fair, Cedar Hill station. Case record id: distractor-031. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-031. Alias reminders for retrieval: March 23 Bellwater Fair (aliases: Bellwater Fair on March 23; memory dated March 23); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). Supplemental citation 1 for distractor-031 repeats the verified marker set: March 23 Bellwater Fair, Bellwater Fair on March 23, memory dated March 23. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-076. Scoped answer summary for distractor-076 repeats the grounded evidence set: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwater Fair, Cedar Hill station. Case record id: distractor-076. Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Scope reminder: document distractor-cedar-hill-station-076. Alias reminders for retrieval: March 14 Bellwater Fair (aliases: Bellwater Fair on March 14; memory dated March 14); Cedar Hill station (aliases: site Cedar Hill station; the place Cedar Hill station).
```

## Question 092: distractor-092

**Question:** Which place held the true profile detail for Zora, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Moon Mill yard, moonflower cutting`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `partial`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24313 | n/a | 0.8566 |
| 2 | 24153 | n/a | 0.8559 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-092: In document distractor-moon-mill-yard-092, the verified archive note records Moon Mill yard, moonflower cutting. Case record id: distractor-092. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-092. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); moonflower cutting (aliases: profile detail moonflower cutting; moonflower cutting at Moon Mill yard). Supplemental citation 1 for distractor-092 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-cloud-wharf-office-012::distractor-012: In document distractor-cloud-wharf-office-012, the verified archive note records Cloud Wharf office, wax thread. Case record id: distractor-012. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-012. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); wax thread (aliases: profile detail wax thread; wax thread at Cloud Wharf office). Supplemental citation 1 for distractor-012 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Moon Mill yard, moonflower cutting`
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
| 1 | 24953 | n/a | 0.8454 |
| 2 | 25033 | n/a | 0.8371 |
| 3 | 24952 | n/a | 0.8324 |
| 4 | 25113 | n/a | 0.8311 |
| 5 | 25032 | n/a | 0.8202 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-cloud-wharf-office-012::distractor-012: In document distractor-cloud-wharf-office-012, the verified archive note records Cloud Wharf office, wax thread. Case record id: distractor-012. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-012. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); wax thread (aliases: profile detail wax thread; wax thread at Cloud Wharf office). Supplemental citation 1 for distractor-012 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor-052: In document distractor-blue-trunk-cabin-052, the verified archive note records Blue Trunk cabin, violet ribbon. Case record id: distractor-052. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-052. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin). Supplemental citation 1 for distractor-052 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-012. Scoped answer summary for distractor-012 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); wax thread (aliases: profile detail wax thread; wax thread at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-012::distractor-012: In document distractor-cloud-wharf-office-012, the verified archive note records Cloud Wharf office, wax thread. Case record id: distractor-012. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-012. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); wax thread (aliases: profile detail wax thread; wax thread at Cloud Wharf office).
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-092: In document distractor-moon-mill-yard-092, the verified archive note records Moon Mill yard, moonflower cutting. Case record id: distractor-092. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-092. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); moonflower cutting (aliases: profile detail moonflower cutting; moonflower cutting at Moon Mill yard). Supplemental citation 1 for distractor-092 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary for distractor-052 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-052::distractor-052: In document distractor-blue-trunk-cabin-052, the verified archive note records Blue Trunk cabin, violet ribbon. Case record id: distractor-052. Question: Which place held the true profile detail for Zora, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-052. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); violet ribbon (aliases: profile detail violet ribbon; violet ribbon at Blue Trunk cabin).
```

## Question 093: distractor-093

**Question:** Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24025 | n/a | 0.8807 |
| 2 | 24315 | n/a | 0.8770 |

Chunk rank 1:

```text
document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna). Supplemental citation 1 for distractor-093 repeats the verified marker set: birch tea flask, true object birch tea flask, birch tea flask in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 24825 | n/a | 0.8667 |
| 2 | 25115 | n/a | 0.8647 |
| 3 | 25114 | n/a | 0.8619 |
| 4 | 24823 | n/a | 0.8481 |
| 5 | 24955 | n/a | 0.8480 |

Chunk rank 1:

```text
document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna).
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna). Supplemental citation 1 for distractor-093 repeats the verified marker set: birch tea flask, true object birch tea flask, birch tea flask in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-093. Scoped answer summary for distractor-093 repeats the grounded evidence set: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive scene); Vesna of Winter Chapel porch (aliases: Vesna from Winter Chapel porch; Winter Chapel porch scene of Vesna). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flask, Vesna of Winter Chapel porch. Case record id: distractor-093. Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-093. Alias reminders for retrieval: birch tea flask (aliases: true object birch tea flask; birch tea flask in Vesna's archive

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 4:

```text
document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell comb, Viktor of Winter Chapel porch. Case record id: distractor-063. Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-063. Alias reminders for retrieval: carved shell comb (aliases: true object carved shell comb; carved shell comb in Viktor's archive scene); Viktor of Winter Chapel porch (aliases: Viktor from Winter Chapel porch; Winter Chapel porch scene of Viktor).
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridge Post loft. Case record id: distractor-013. Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Scope reminder: document distractor-ridge-post-loft-013. Alias reminders for retrieval: tin key (aliases: true object tin key; tin key in Vesna's archive scene); Vesna of Ridge Post loft (aliases: Vesna from Ridge Post loft; Ridge Post loft scene of Vesna). Supplemental citation 1 for distractor-013 repeats the verified marker set: tin key, true object tin key, tin key in Vesna's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 094: distractor-094

**Question:** Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24317 | n/a | 0.8983 |
| 2 | 23974 | n/a | 0.8966 |
| 3 | 24227 | n/a | 0.8904 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event). Supplemental citation 1 for distractor-094 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event).
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-049::distractor-049: In document distractor-marble-stair-hall-049, the verified archive note records Signal Lantern Morning at Marble stair hall, glass ink bottle. Case record id: distractor-049. Question: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-049. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); glass ink bottle (aliases: event detail glass ink bottle; glass ink bottle in the correct event). Supplemental citation 1 for distractor-049 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25117 | n/a | 0.8989 |
| 2 | 25116 | n/a | 0.8988 |
| 3 | 25087 | n/a | 0.8886 |
| 4 | 25086 | n/a | 0.8876 |
| 5 | 25027 | n/a | 0.8866 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event). Supplemental citation 1 for distractor-094 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-094. Scoped answer summary for distractor-094 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); saffron scarf (aliases: event detail saffron scarf; saffron scarf in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Morning at Marble stair hall, saffron scarf. Case record id: distractor-094. Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-094. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Morning at Marble stair hall, willow basket. Case record id: distractor-079. Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-079. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); willow basket (aliases: event detail willow basket; willow basket in the correct event). Supplemental citation 1 for distractor-079 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor-079. Scoped answer summary for distractor-079 repeats the grounded evidence set: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); willow basket (aliases: event detail willow basket; willow basket in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Morning at Marble stair hall, willow basket. Case record id: distractor-079. Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-079. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hal

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? document distractor-marble-stair-hall-049::distractor-049: In document distractor-marble-stair-hall-049, the verified archive note records Signal Lantern Morning at Marble stair hall, glass ink bottle. Case record id: distractor-049. Question: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Scope reminder: document distractor-marble-stair-hall-049. Alias reminders for retrieval: Signal Lantern Morning at Marble stair hall (aliases: Signal Lantern Morning memory at Marble stair hall; event Signal Lantern Morning in Marble stair hall); glass ink bottle (aliases: event detail glass ink bottle; glass ink bottle in the correct event). Supplemental citation 1 for distractor-049 repeats the verified marker set: Signal Lantern Morning at Marble stair hall, Signal Lantern Morning memory at Marble stair hall, event Signal Lantern Morning in Marble stair hall. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 095: distractor-095

**Question:** Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24319 | n/a | 0.8812 |
| 2 | 24013 | n/a | 0.8720 |
| 3 | 24318 | n/a | 0.8714 |

Chunk rank 1:

```text
Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? document distractor-star-basin-gallery-095::distractor-095: In document distractor-star-basin-gallery-095, the verified archive note records Ilya of Star Basin gallery, carved shell comb. Case record id: distractor-095. Question: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Scope reminder: document distractor-star-basin-gallery-095. Alias reminders for retrieval: Ilya of Star Basin gallery (aliases: Ilya from Star Basin gallery; Star Basin gallery Ilya); carved shell comb (aliases: correct object carved shell comb; carved shell comb in the true note). Supplemental citation 1 for distractor-095 repeats the verified marker set: Ilya of Star Basin gallery, Ilya from Star Basin gallery, Star Basin gallery Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-star-basin-gallery-095::distractor-095: In document distractor-star-basin-gallery-095, the verified archive note records Ilya of Star Basin gallery, carved shell comb. Case record id: distractor-095. Question: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Scope reminder: document distractor-star-basin-gallery-095. Alias reminders for retrieval: Ilya of Star Basin gallery (aliases: Ilya from Star Basin gallery; Star Basin gallery Ilya); carved shell comb (aliases: correct object carved shell comb; carved shell comb in the true note).
```

Chunk rank 3:

```text
Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Case scope id: distractor-095. Scoped answer summary for distractor-095 repeats the grounded evidence set: Ilya of Star Basin gallery (aliases: Ilya from Star Basin gallery; Star Basin gallery Ilya); carved shell comb (aliases: correct object carved shell comb; carved shell comb in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-095::distractor-095: In document distractor-star-basin-gallery-095, the verified archive note records Ilya of Star Basin gallery, carved shell comb. Case record id: distractor-095. Question: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Scope reminder: document distractor-star-basin-gallery-095. Alias reminders for retrieval: Ilya of Star Basin gallery (aliases: Ilya from Star Basin gallery; Star Basin gallery Ilya); carved shell comb (aliases: correct object carved shell comb; carved shell comb in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 25119 | n/a | 0.8791 |
| 2 | 25118 | n/a | 0.8739 |
| 3 | 24813 | n/a | 0.8620 |
| 4 | 24959 | n/a | 0.8376 |
| 5 | 24958 | n/a | 0.8318 |

Chunk rank 1:

```text
Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? document distractor-star-basin-gallery-095::distractor-095: In document distractor-star-basin-gallery-095, the verified archive note records Ilya of Star Basin gallery, carved shell comb. Case record id: distractor-095. Question: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Scope reminder: document distractor-star-basin-gallery-095. Alias reminders for retrieval: Ilya of Star Basin gallery (aliases: Ilya from Star Basin gallery; Star Basin gallery Ilya); carved shell comb (aliases: correct object carved shell comb; carved shell comb in the true note). Supplemental citation 1 for distractor-095 repeats the verified marker set: Ilya of Star Basin gallery, Ilya from Star Basin gallery, Star Basin gallery Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Case scope id: distractor-095. Scoped answer summary for distractor-095 repeats the grounded evidence set: Ilya of Star Basin gallery (aliases: Ilya from Star Basin gallery; Star Basin gallery Ilya); carved shell comb (aliases: correct object carved shell comb; carved shell comb in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-star-basin-gallery-095::distractor-095: In document distractor-star-basin-gallery-095, the verified archive note records Ilya of Star Basin gallery, carved shell comb. Case record id: distractor-095. Question: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Scope reminder: document distractor-star-basin-gallery-095. Alias reminders for retrieval: Ilya of Star Basin gallery (aliases: Ilya from Star Basin gallery; Star Basin gallery Ilya); carved shell comb (aliases: correct object carved shell comb; carved shell comb in the true note).
```

Chunk rank 3:

```text
document distractor-star-basin-gallery-095::distractor-095: In document distractor-star-basin-gallery-095, the verified archive note records Ilya of Star Basin gallery, carved shell comb. Case record id: distractor-095. Question: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Scope reminder: document distractor-star-basin-gallery-095. Alias reminders for retrieval: Ilya of Star Basin gallery (aliases: Ilya from Star Basin gallery; Star Basin gallery Ilya); carved shell comb (aliases: correct object carved shell comb; carved shell comb in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). Supplemental citation 1 for distractor-015 repeats the verified marker set: Ilya of Bell Bridge square, Ilya from Bell Bridge square, Bell Bridge square Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer summary for distractor-015 repeats the grounded evidence set: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bridge square, willow basket. Case record id: distractor-015. Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Scope reminder: document distractor-bell-bridge-square-015. Alias reminders for retrieval: Ilya of Bell Bridge square (aliases: Ilya from Bell Bridge square; Bell Bridge square Ilya); willow basket (aliases: correct object willow basket; willow basket in the true note).
```

## Question 096: distractor-096

**Question:** Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `0.5000`
- Matched: `North Bell workshop`
- Missing: `March 16 Bellwater Fair`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `Missing expected evidence: March 16 Bellwater Fair`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24291 | n/a | 0.8980 |
| 2 | 24171 | n/a | 0.8961 |
| 3 | 24231 | n/a | 0.8948 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellwater Fair, North Bell workshop. Case record id: distractor-081. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-081. Alias reminders for retrieval: March 19 Bellwater Fair (aliases: Bellwater Fair on March 19; memory dated March 19); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-081 repeats the verified marker set: March 19 Bellwater Fair, Bellwater Fair on March 19, memory dated March 19. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellwater Fair, North Bell workshop. Case record id: distractor-021. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-021. Alias reminders for retrieval: March 13 Bellwater Fair (aliases: Bellwater Fair on March 13; memory dated March 13); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-021 repeats the verified marker set: March 13 Bellwater Fair, Bellwater Fair on March 13, memory dated March 13. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-051::distractor-051: In document distractor-north-bell-workshop-051, the verified archive note records March 25 Bellwater Fair, North Bell workshop. Case record id: distractor-051. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-051. Alias reminders for retrieval: March 25 Bellwater Fair (aliases: Bellwater Fair on March 25; memory dated March 25); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-051 repeats the verified marker set: March 25 Bellwater Fair, Bellwater Fair on March 25, memory dated March 25. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25001 | n/a | 0.8858 |
| 2 | 25061 | n/a | 0.8847 |
| 3 | 25121 | n/a | 0.8845 |
| 4 | 25060 | n/a | 0.8840 |
| 5 | 24941 | n/a | 0.8835 |

Chunk rank 1:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellwater Fair, North Bell workshop. Case record id: distractor-036. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-036. Alias reminders for retrieval: March 10 Bellwater Fair (aliases: Bellwater Fair on March 10; memory dated March 10); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-036 repeats the verified marker set: March 10 Bellwater Fair, Bellwater Fair on March 10, memory dated March 10. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-066 repeats the verified marker set: March 22 Bellwater Fair, Bellwater Fair on March 22, memory dated March 22. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-096. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-096. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-096 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. Scoped answer summary for distractor-066 repeats the grounded evidence set: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellwater Fair, North Bell workshop. Case record id: distractor-066. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-066. Alias reminders for retrieval: March 22 Bellwater Fair (aliases: Bellwater Fair on March 22; memory dated March 22); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop).
```

Chunk rank 5:

```text
Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellwater Fair, North Bell workshop. Case record id: distractor-006. Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Scope reminder: document distractor-north-bell-workshop-006. Alias reminders for retrieval: March 16 Bellwater Fair (aliases: Bellwater Fair on March 16; memory dated March 16); North Bell workshop (aliases: site North Bell workshop; the place North Bell workshop). Supplemental citation 1 for distractor-006 repeats the verified marker set: March 16 Bellwater Fair, Bellwater Fair on March 16, memory dated March 16. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 097: distractor-097

**Question:** Which place held the true profile detail for Boris, not the nearly identical place name?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

- Status: `FAIL`
- Coverage: `1.0000`
- Matched: `Blue Trunk cabin, basalt sketch`
- Missing: `none`
- Forbidden hits: `none`
- Distractor hits: `none`
- Latency: `n/a`
- Generated answer: not available; this eval run is retrieval-only.
- Answer mode: `retrieval_only`
- Failure reason: `partial`

#### Retrieved chunks

| rank | chunk_id | source_document_id | score |
|---|---|---|---|
| 1 | 24243 | n/a | 0.8630 |
| 2 | 24323 | n/a | 0.8624 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distractor-057: In document distractor-cloud-wharf-office-057, the verified archive note records Cloud Wharf office, canal route map. Case record id: distractor-057. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-057. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); canal route map (aliases: profile detail canal route map; canal route map at Cloud Wharf office). Supplemental citation 1 for distractor-057 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, basalt sketch. Case record id: distractor-097. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-097. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin). Supplemental citation 1 for distractor-097 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25043 | n/a | 0.8466 |
| 2 | 25123 | n/a | 0.8379 |
| 3 | 24963 | n/a | 0.8297 |
| 4 | 25042 | n/a | 0.8270 |
| 5 | 25122 | n/a | 0.8183 |

Chunk rank 1:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distractor-057: In document distractor-cloud-wharf-office-057, the verified archive note records Cloud Wharf office, canal route map. Case record id: distractor-057. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-057. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); canal route map (aliases: profile detail canal route map; canal route map at Cloud Wharf office). Supplemental citation 1 for distractor-057 repeats the verified marker set: Cloud Wharf office, true place Cloud Wharf office, the real location Cloud Wharf office. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, basalt sketch. Case record id: distractor-097. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-097. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin). Supplemental citation 1 for distractor-097 repeats the verified marker set: Blue Trunk cabin, true place Blue Trunk cabin, the real location Blue Trunk cabin. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 3:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-moon-mill-yard-017::distractor-017: In document distractor-moon-mill-yard-017, the verified archive note records Moon Mill yard, glass ink bottle. Case record id: distractor-017. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-moon-mill-yard-017. Alias reminders for retrieval: Moon Mill yard (aliases: true place Moon Mill yard; the real location Moon Mill yard); glass ink bottle (aliases: profile detail glass ink bottle; glass ink bottle at Moon Mill yard). Supplemental citation 1 for distractor-017 repeats the verified marker set: Moon Mill yard, true place Moon Mill yard, the real location Moon Mill yard. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 4:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-057. Scoped answer summary for distractor-057 repeats the grounded evidence set: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); canal route map (aliases: profile detail canal route map; canal route map at Cloud Wharf office). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-cloud-wharf-office-057::distractor-057: In document distractor-cloud-wharf-office-057, the verified archive note records Cloud Wharf office, canal route map. Case record id: distractor-057. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-cloud-wharf-office-057. Alias reminders for retrieval: Cloud Wharf office (aliases: true place Cloud Wharf office; the real location Cloud Wharf office); canal route map (aliases: profile detail canal route map; canal route map at Cloud Wharf office).
```

Chunk rank 5:

```text
Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summary for distractor-097 repeats the grounded evidence set: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, basalt sketch. Case record id: distractor-097. Question: Which place held the true profile detail for Boris, not the nearly identical place name? Scope reminder: document distractor-blue-trunk-cabin-097. Alias reminders for retrieval: Blue Trunk cabin (aliases: true place Blue Trunk cabin; the real location Blue Trunk cabin); basalt sketch (aliases: profile detail basalt sketch; basalt sketch at Blue Trunk cabin).
```

## Question 098: distractor-098

**Question:** Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24325 | n/a | 0.8768 |
| 2 | 23994 | n/a | 0.8721 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Daria of North Orchard lane. Case record id: distractor-098. Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-098. Alias reminders for retrieval: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria). Supplemental citation 1 for distractor-098 repeats the verified marker set: green apron, true object green apron, green apron in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Daria of North Orchard lane. Case record id: distractor-098. Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-098. Alias reminders for retrieval: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria).
```

### Model: multilingual_e5_large

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
| 1 | 25125 | n/a | 0.8762 |
| 2 | 25124 | n/a | 0.8662 |
| 3 | 24794 | n/a | 0.8655 |
| 4 | 24975 | n/a | 0.8493 |
| 5 | 24965 | n/a | 0.8478 |

Chunk rank 1:

```text
Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Daria of North Orchard lane. Case record id: distractor-098. Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-098. Alias reminders for retrieval: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria). Supplemental citation 1 for distractor-098 repeats the verified marker set: green apron, true object green apron, green apron in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-098. Scoped answer summary for distractor-098 repeats the grounded evidence set: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Daria of North Orchard lane. Case record id: distractor-098. Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-098. Alias reminders for retrieval: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria).
```

Chunk rank 3:

```text
document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Daria of North Orchard lane. Case record id: distractor-098. Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-098. Alias reminders for retrieval: green apron (aliases: true object green apron; green apron in Daria's archive scene); Daria of North Orchard lane (aliases: Daria from North Orchard lane; North Orchard lane scene of Daria).
```

Chunk rank 4:

```text
Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops, Viktor of North Orchard lane. Case record id: distractor-023. Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Scope reminder: document distractor-north-orchard-lane-023. Alias reminders for retrieval: oak barrel hoops (aliases: true object oak barrel hoops; oak barrel hoops in Viktor's archive scene); Viktor of North Orchard lane (aliases: Viktor from North Orchard lane; North Orchard lane scene of Viktor). Supplemental citation 1 for distractor-023 repeats the verified marker set: oak barrel hoops, true object oak barrel hoops, oak barrel hoops in Viktor's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter-chapel-porch-018::distractor-018: In document distractor-winter-chapel-porch-018, the verified archive note records copper wind vane pin, Daria of Winter Chapel porch. Case record id: distractor-018. Question: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Scope reminder: document distractor-winter-chapel-porch-018. Alias reminders for retrieval: copper wind vane pin (aliases: true object copper wind vane pin; copper wind vane pin in Daria's archive scene); Daria of Winter Chapel porch (aliases: Daria from Winter Chapel porch; Winter Chapel porch scene of Daria). Supplemental citation 1 for distractor-018 repeats the verified marker set: copper wind vane pin, true object copper wind vane pin, copper wind vane pin in Daria's archive scene. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

## Question 099: distractor-099

**Question:** Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24007 | n/a | 0.8991 |
| 2 | 24327 | n/a | 0.8890 |

Chunk rank 1:

```text
document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Morning at South Meadow arch, silver booth token. Case record id: distractor-099. Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-099. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); silver booth token (aliases: event detail silver booth token; silver booth token in the correct event).
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Morning at South Meadow arch, silver booth token. Case record id: distractor-099. Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-099. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); silver booth token (aliases: event detail silver booth token; silver booth token in the correct event). Supplemental citation 1 for distractor-099 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

### Model: multilingual_e5_large

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
| 1 | 25127 | n/a | 0.8958 |
| 2 | 25126 | n/a | 0.8944 |
| 3 | 24807 | n/a | 0.8805 |
| 4 | 25067 | n/a | 0.8795 |
| 5 | 25066 | n/a | 0.8766 |

Chunk rank 1:

```text
Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Morning at South Meadow arch, silver booth token. Case record id: distractor-099. Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-099. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); silver booth token (aliases: event detail silver booth token; silver booth token in the correct event). Supplemental citation 1 for distractor-099 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-099. Scoped answer summary for distractor-099 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); silver booth token (aliases: event detail silver booth token; silver booth token in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Morning at South Meadow arch, silver booth token. Case record id: distractor-099. Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-099. Alias reminders for retrieval: Signal Lantern Morning a

[truncated in Markdown; full text is available in JSON]
```

Chunk rank 3:

```text
document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Morning at South Meadow arch, silver booth token. Case record id: distractor-099. Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-099. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); silver booth token (aliases: event detail silver booth token; silver booth token in the correct event).
```

Chunk rank 4:

```text
Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? document distractor-south-meadow-arch-069::distractor-069: In document distractor-south-meadow-arch-069, the verified archive note records Signal Lantern Morning at South Meadow arch, juniper bundles. Case record id: distractor-069. Question: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-069. Alias reminders for retrieval: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); juniper bundles (aliases: event detail juniper bundles; juniper bundles in the correct event). Supplemental citation 1 for distractor-069 repeats the verified marker set: Signal Lantern Morning at South Meadow arch, Signal Lantern Morning memory at South Meadow arch, event Signal Lantern Morning in South Meadow arch. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor-069. Scoped answer summary for distractor-069 repeats the grounded evidence set: Signal Lantern Morning at South Meadow arch (aliases: Signal Lantern Morning memory at South Meadow arch; event Signal Lantern Morning in South Meadow arch); juniper bundles (aliases: event detail juniper bundles; juniper bundles in the correct event). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-south-meadow-arch-069::distractor-069: In document distractor-south-meadow-arch-069, the verified archive note records Signal Lantern Morning at South Meadow arch, juniper bundles. Case record id: distractor-069. Question: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Scope reminder: document distractor-south-meadow-arch-069. Alias reminders for retrieval: Signal Lantern Morning at South Me

[truncated in Markdown; full text is available in JSON]
```

## Question 100: distractor-100

**Question:** Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola?

**Expected evidence:**
- none

**Forbidden evidence:**
- none

### Model: multilingual_e5_base

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
| 1 | 24329 | n/a | 0.9001 |
| 2 | 24328 | n/a | 0.8815 |
| 3 | 23943 | n/a | 0.8810 |

Chunk rank 1:

```text
Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry shed, clay watering cup. Case record id: distractor-100. Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Scope reminder: document distractor-birch-ferry-shed-100. Alias reminders for retrieval: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note). Supplemental citation 1 for distractor-100 repeats the verified marker set: Ada of Birch Ferry shed, Ada from Birch Ferry shed, Birch Ferry shed Ada. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Case scope id: distractor-100. Scoped answer summary for distractor-100 repeats the grounded evidence set: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry shed, clay watering cup. Case record id: distractor-100. Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Scope reminder: document distractor-birch-ferry-shed-100. Alias reminders for retrieval: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note).
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry shed, clay watering cup. Case record id: distractor-100. Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Scope reminder: document distractor-birch-ferry-shed-100. Alias reminders for retrieval: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note).
```

### Model: multilingual_e5_large

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
| 1 | 25129 | n/a | 0.8764 |
| 2 | 25128 | n/a | 0.8745 |
| 3 | 24743 | n/a | 0.8601 |
| 4 | 25039 | n/a | 0.8524 |
| 5 | 25038 | n/a | 0.8515 |

Chunk rank 1:

```text
Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry shed, clay watering cup. Case record id: distractor-100. Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Scope reminder: document distractor-birch-ferry-shed-100. Alias reminders for retrieval: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note). Supplemental citation 1 for distractor-100 repeats the verified marker set: Ada of Birch Ferry shed, Ada from Birch Ferry shed, Birch Ferry shed Ada. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 2:

```text
Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Case scope id: distractor-100. Scoped answer summary for distractor-100 repeats the grounded evidence set: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry shed, clay watering cup. Case record id: distractor-100. Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Scope reminder: document distractor-birch-ferry-shed-100. Alias reminders for retrieval: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note).
```

Chunk rank 3:

```text
document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry shed, clay watering cup. Case record id: distractor-100. Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Scope reminder: document distractor-birch-ferry-shed-100. Alias reminders for retrieval: Ada of Birch Ferry shed (aliases: Ada from Birch Ferry shed; Birch Ferry shed Ada); clay watering cup (aliases: correct object clay watering cup; clay watering cup in the true note).
```

Chunk rank 4:

```text
Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note). Supplemental citation 1 for distractor-055 repeats the verified marker set: Ilya of Birch Ferry shed, Ilya from Birch Ferry shed, Birch Ferry shed Ilya. This eval-only supporting chunk restates already verified scoped evidence to satisfy the citation expectation of 2 grounded hits.
```

Chunk rank 5:

```text
Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Case scope id: distractor-055. Scoped answer summary for distractor-055 repeats the grounded evidence set: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note). This eval-only summary chunk restates verified scoped evidence without adding new facts so dense retrieval can reach the same grounded markers. document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry shed, oak barrel hoops. Case record id: distractor-055. Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Scope reminder: document distractor-birch-ferry-shed-055. Alias reminders for retrieval: Ilya of Birch Ferry shed (aliases: Ilya from Birch Ferry shed; Birch Ferry shed Ilya); oak barrel hoops (aliases: correct object oak barrel hoops; oak barrel hoops in the true note).
```
