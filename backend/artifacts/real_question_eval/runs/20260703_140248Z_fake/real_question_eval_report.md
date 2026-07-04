# Real Question Evaluation Report

## Client Summary
- Source dataset: deterministic fictional eval corpus
- Real client/user data: no
- Purpose: retrieval quality testing
- Models compared:
  - `multilingual_e5_small`
  - `bge_m3`
- Recommended active model: `bge_m3`
- Speed vs accuracy tradeoff: Fake-mode evaluation is optimized for deterministic regression checks, not runtime speed measurements.
- Production recommendation: Keep the fake-mode result for test coverage only; use the preserved latest real evaluation for production-facing model decisions.
- Timestamp: 2026-07-03T14:02:48.779913+00:00
- Run status: `COMPLETED`
- Quality status: `PASS`
- Quality gate: `best_model_pass_rate`
- Preflight validation: `PASS`
- Preflight missing marker count: `0`
- Run type: `fake`

## Artifact Files
- Latest Markdown: `/app/artifacts/real_question_eval/latest_fake/real_question_eval_report.md`
- Latest JSON: `/app/artifacts/real_question_eval/latest_fake/real_question_eval_result.json`
- Latest Summary Markdown: `/app/artifacts/real_question_eval/latest_fake/real_question_eval_summary.md`
- Latest Summary JSON: `/app/artifacts/real_question_eval/latest_fake/real_question_eval_summary.json`
- Archived Markdown: `/app/artifacts/real_question_eval/runs/20260703_140248Z_fake/real_question_eval_report.md`
- Archived JSON: `/app/artifacts/real_question_eval/runs/20260703_140248Z_fake/real_question_eval_result.json`
- Archived Summary Markdown: `/app/artifacts/real_question_eval/runs/20260703_140248Z_fake/real_question_eval_summary.md`
- Archived Summary JSON: `/app/artifacts/real_question_eval/runs/20260703_140248Z_fake/real_question_eval_summary.json`

## Client Question Breakdown
### Question 1 - multi-document-winter-convoy
Question: Which route record and warm supply together identify the winter convoy preparations?
- Final evaluated answer: Grounded by retrieved evidence for: birch tea flask, canvas route map.
- Correctness verdict: grounded
- Evidence used: birch tea flask, canvas route map
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- canvas route map
- birch tea flask

Expected distractors:
- summer parade ribbon

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=birch tea flask, canvas route map missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=birch tea flask, canvas route map missing=none distractors=none

### Question 2 - multi-document-harbor-fair
Question: Which token and banner patch together identify the harbor fair stall that stayed open in the rain?
- Final evaluated answer: Grounded by retrieved evidence for: silver booth token, violet banner patch.
- Correctness verdict: grounded
- Evidence used: silver booth token, violet banner patch
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- silver booth token
- violet banner patch

Expected distractors:
- midday bell ticket

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=silver booth token, violet banner patch missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=silver booth token, violet banner patch missing=none distractors=none

### Question 3 - multi-document-school-rehearsal
Question: Which stage prop and music-room tool together identify the school rehearsal setup?
- Final evaluated answer: Grounded by retrieved evidence for: paper moon mask, tuning fork.
- Correctness verdict: grounded
- Evidence used: paper moon mask, tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- tuning fork

Expected distractors:
- chalk race pennant

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=paper moon mask, tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=paper moon mask, tuning fork missing=none distractors=none

### Question 4 - multi-document-valley-expedition
Question: Which expedition records together explain how the valley crossing was prepared?
- Final evaluated answer: Grounded by retrieved evidence for: basalt sketch, chalk trail mark, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: basalt sketch, chalk trail mark, rope bridge permit
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- basalt sketch
- rope bridge permit
- chalk trail mark

Expected distractors:
- orchard picnic note

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=basalt sketch, chalk trail mark, rope bridge permit missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=basalt sketch, chalk trail mark, rope bridge permit missing=none distractors=none

### Question 5 - multi-document-observatory-storm
Question: Which observatory records together identify the storm-night repair at the roof line?
- Final evaluated answer: Grounded by retrieved evidence for: copper wind vane pin, star ledger page.
- Correctness verdict: grounded
- Evidence used: copper wind vane pin, star ledger page
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- star ledger page
- copper wind vane pin

Expected distractors:
- garden feast ticket

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=copper wind vane pin, star ledger page missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper wind vane pin, star ledger page missing=none distractors=none

### Question 6 - multi-document-006
Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch?
- Final evaluated answer: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: glass ink bottle, moonflower cutting
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- glass ink bottle

Expected distractors:
- brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=glass ink bottle, moonflower cutting missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=glass ink bottle, moonflower cutting missing=none distractors=none

### Question 7 - multi-document-007
Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, rope bridge permit, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- weathered camera strap
- coal stove hiss

Expected distractors:
- basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss, rope bridge permit, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, rope bridge permit, weathered camera strap missing=none distractors=none

### Question 8 - multi-document-008
Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well?
- Final evaluated answer: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Correctness verdict: grounded
- Evidence used: juniper bundles, paper moon mask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- juniper bundles

Expected distractors:
- copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=juniper bundles, paper moon mask missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=juniper bundles, paper moon mask missing=none distractors=none

### Question 9 - multi-document-009
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning, carved shell comb, lantern hook.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning, carved shell comb, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning
- lantern hook
- carved shell comb

Expected distractors:
- tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, carved shell comb, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, carved shell comb, lantern hook missing=none distractors=none

### Question 10 - multi-document-010
Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: canal route map, clay watering cup.
- Correctness verdict: grounded
- Evidence used: canal route map, clay watering cup
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing clay watering cup, canal route map
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- canal route map

Expected distractors:
- willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=clay watering cup, canal route map distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=canal route map, clay watering cup missing=none distractors=none

### Question 11 - multi-document-011
Question: Which documents must be combined to understand Vera's archive card note about Pine Gate yard?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, copper token, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron scarf
- coal stove hiss
- copper token

Expected distractors:
- star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss, copper token, saffron scarf missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, copper token, saffron scarf missing=none distractors=none

### Question 12 - multi-document-012
Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop?
- Final evaluated answer: Grounded by retrieved evidence for: blue glass jar, tin key.
- Correctness verdict: grounded
- Evidence used: blue glass jar, tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- tin key

Expected distractors:
- silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue glass jar, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue glass jar, tin key missing=none distractors=none

### Question 13 - multi-document-013
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier?
- Final evaluated answer: Grounded by retrieved evidence for: Moon Orchard Rest, brass compass, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Moon Orchard Rest, brass compass, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Moon Orchard Rest
- copper wind vane pin
- brass compass

Expected distractors:
- birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Moon Orchard Rest, brass compass, copper wind vane pin missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Moon Orchard Rest, brass compass, copper wind vane pin missing=none distractors=none

### Question 14 - multi-document-014
Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard?
- Final evaluated answer: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Correctness verdict: grounded
- Evidence used: basalt sketch, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- wax thread
- basalt sketch

Expected distractors:
- oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=basalt sketch, wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=basalt sketch, wax thread missing=none distractors=none

### Question 15 - multi-document-015
Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: copper token, silver booth token, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- smoke vent chain
- copper token
- silver booth token

Expected distractors:
- glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=copper token, silver booth token, smoke vent chain missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper token, silver booth token, smoke vent chain missing=none distractors=none

### Question 16 - multi-document-016
Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft?
- Final evaluated answer: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Correctness verdict: grounded
- Evidence used: amber lantern, tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- amber lantern
- tuning fork

Expected distractors:
- weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=amber lantern, tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=amber lantern, tuning fork missing=none distractors=none

### Question 17 - multi-document-017
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room?
- Final evaluated answer: Grounded by retrieved evidence for: Harvest Glow, cedar shovel, willow basket.
- Correctness verdict: grounded
- Evidence used: Harvest Glow, cedar shovel, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Harvest Glow
- cedar shovel
- willow basket

Expected distractors:
- juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Harvest Glow, cedar shovel, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Harvest Glow, cedar shovel, willow basket missing=none distractors=none

### Question 18 - multi-document-018
Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch?
- Final evaluated answer: Grounded by retrieved evidence for: star ledger page, violet ribbon.
- Correctness verdict: grounded
- Evidence used: star ledger page, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- violet ribbon
- star ledger page

Expected distractors:
- carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=star ledger page, violet ribbon missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=star ledger page, violet ribbon missing=none distractors=none

### Question 19 - multi-document-019
Question: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic?
- Final evaluated answer: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: blue oar, silver booth token, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- silver booth token
- weathered camera strap

Expected distractors:
- canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=blue oar, silver booth token, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue oar, silver booth token, weathered camera strap missing=none distractors=none

### Question 20 - multi-document-020
Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery?
- Final evaluated answer: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Correctness verdict: grounded
- Evidence used: birch tea flask, linen wick
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- birch tea flask

Expected distractors:
- coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=birch tea flask, linen wick missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=birch tea flask, linen wick missing=none distractors=none

### Question 21 - multi-document-021
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse?
- Final evaluated answer: Grounded by retrieved evidence for: Bellwater Fair, green apron, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Bellwater Fair, green apron, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Bellwater Fair
- green apron
- oak barrel hoops

Expected distractors:
- tin key

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Bellwater Fair, green apron, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Bellwater Fair, green apron, oak barrel hoops missing=none distractors=none

### Question 22 - multi-document-022
Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station?
- Final evaluated answer: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: glass ink bottle, moonflower cutting
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- glass ink bottle

Expected distractors:
- brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=glass ink bottle, moonflower cutting missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=glass ink bottle, moonflower cutting missing=none distractors=none

### Question 23 - multi-document-023
Question: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, rope bridge permit, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- weathered camera strap
- coal stove hiss

Expected distractors:
- basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss, rope bridge permit, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, rope bridge permit, weathered camera strap missing=none distractors=none

### Question 24 - multi-document-024
Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office?
- Final evaluated answer: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Correctness verdict: grounded
- Evidence used: juniper bundles, paper moon mask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- juniper bundles

Expected distractors:
- copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=juniper bundles, paper moon mask missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=juniper bundles, paper moon mask missing=none distractors=none

### Question 25 - multi-document-025
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Tide, carved shell comb, lantern hook.
- Correctness verdict: grounded
- Evidence used: Lantern Tide, carved shell comb, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Lantern Tide
- lantern hook
- carved shell comb

Expected distractors:
- tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lantern Tide, carved shell comb, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lantern Tide, carved shell comb, lantern hook missing=none distractors=none

### Question 26 - multi-document-026
Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane?
- Final evaluated answer: Grounded by retrieved evidence for: canal route map, clay watering cup.
- Correctness verdict: grounded
- Evidence used: canal route map, clay watering cup
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- canal route map

Expected distractors:
- willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=canal route map, clay watering cup missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=canal route map, clay watering cup missing=none distractors=none

### Question 27 - multi-document-027
Question: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, copper token, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron scarf
- coal stove hiss
- copper token

Expected distractors:
- star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss, copper token, saffron scarf missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, copper token, saffron scarf missing=none distractors=none

### Question 28 - multi-document-028
Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall?
- Final evaluated answer: Grounded by retrieved evidence for: blue glass jar, tin key.
- Correctness verdict: grounded
- Evidence used: blue glass jar, tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- tin key

Expected distractors:
- silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue glass jar, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue glass jar, tin key missing=none distractors=none

### Question 29 - multi-document-029
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning, brass compass, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning, brass compass, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning
- copper wind vane pin
- brass compass

Expected distractors:
- birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, brass compass, copper wind vane pin missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, brass compass, copper wind vane pin missing=none distractors=none

### Question 30 - multi-document-030
Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Correctness verdict: grounded
- Evidence used: basalt sketch, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- wax thread
- basalt sketch

Expected distractors:
- oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=basalt sketch, wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=basalt sketch, wax thread missing=none distractors=none

### Question 31 - multi-document-031
Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing?
- Final evaluated answer: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: copper token, silver booth token, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- smoke vent chain
- copper token
- silver booth token

Expected distractors:
- glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=copper token, silver booth token, smoke vent chain missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper token, silver booth token, smoke vent chain missing=none distractors=none

### Question 32 - multi-document-032
Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk?
- Final evaluated answer: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Correctness verdict: grounded
- Evidence used: amber lantern, tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- amber lantern
- tuning fork

Expected distractors:
- weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=amber lantern, tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=amber lantern, tuning fork missing=none distractors=none

### Question 33 - multi-document-033
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room?
- Final evaluated answer: Grounded by retrieved evidence for: Moon Orchard Rest, cedar shovel, willow basket.
- Correctness verdict: grounded
- Evidence used: Moon Orchard Rest, cedar shovel, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Moon Orchard Rest
- cedar shovel
- willow basket

Expected distractors:
- juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Moon Orchard Rest, cedar shovel, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Moon Orchard Rest, cedar shovel, willow basket missing=none distractors=none

### Question 34 - multi-document-034
Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin?
- Final evaluated answer: Partially grounded by: violet ribbon. Missing: star ledger page.
- Correctness verdict: partial
- Evidence used: violet ribbon
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=partial coverage=0.5
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (0.50 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing violet ribbon, star ledger page
- Distractors / false positives: none

Expected evidence:
- violet ribbon
- star ledger page

Expected distractors:
- carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=violet ribbon, star ledger page distractors=none
  - `bge_m3`: verdict=partial coverage=0.5 matched=violet ribbon missing=star ledger page distractors=none

### Question 35 - multi-document-035
Question: Which documents must be combined to understand Ada's family note note about River Lantern inn?
- Final evaluated answer: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: blue oar, silver booth token, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- silver booth token
- weathered camera strap

Expected distractors:
- canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue oar, silver booth token, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue oar, silver booth token, weathered camera strap missing=none distractors=none

### Question 36 - multi-document-036
Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch?
- Final evaluated answer: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Correctness verdict: grounded
- Evidence used: birch tea flask, linen wick
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- birch tea flask

Expected distractors:
- coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=birch tea flask, linen wick missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=birch tea flask, linen wick missing=none distractors=none

### Question 37 - multi-document-037
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge?
- Final evaluated answer: Grounded by retrieved evidence for: Harvest Glow, green apron, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Harvest Glow, green apron, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Harvest Glow
- green apron
- oak barrel hoops

Expected distractors:
- tin key

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Harvest Glow, green apron, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Harvest Glow, green apron, oak barrel hoops missing=none distractors=none

### Question 38 - multi-document-038
Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well?
- Final evaluated answer: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: glass ink bottle, moonflower cutting
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- glass ink bottle

Expected distractors:
- brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=glass ink bottle, moonflower cutting missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=glass ink bottle, moonflower cutting missing=none distractors=none

### Question 39 - multi-document-039
Question: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, rope bridge permit, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- weathered camera strap
- coal stove hiss

Expected distractors:
- basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss, rope bridge permit, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, rope bridge permit, weathered camera strap missing=none distractors=none

### Question 40 - multi-document-040
Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Correctness verdict: grounded
- Evidence used: juniper bundles, paper moon mask
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing paper moon mask, juniper bundles
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- juniper bundles

Expected distractors:
- copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=paper moon mask, juniper bundles distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=juniper bundles, paper moon mask missing=none distractors=none

### Question 41 - multi-document-041
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard?
- Final evaluated answer: Grounded by retrieved evidence for: Bellwater Fair, carved shell comb, lantern hook.
- Correctness verdict: grounded
- Evidence used: Bellwater Fair, carved shell comb, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Bellwater Fair
- lantern hook
- carved shell comb

Expected distractors:
- tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Bellwater Fair, carved shell comb, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Bellwater Fair, carved shell comb, lantern hook missing=none distractors=none

### Question 42 - multi-document-042
Question: Which archive pieces from more than one document explain the family profile event at North Bell workshop?
- Final evaluated answer: Grounded by retrieved evidence for: canal route map, clay watering cup.
- Correctness verdict: grounded
- Evidence used: canal route map, clay watering cup
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing clay watering cup, canal route map
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- canal route map

Expected distractors:
- willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=clay watering cup, canal route map distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=canal route map, clay watering cup missing=none distractors=none

### Question 43 - multi-document-043
Question: Which documents must be combined to understand Anya's holiday card note about Fog Island pier?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, copper token, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron scarf
- coal stove hiss
- copper token

Expected distractors:
- star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss, copper token, saffron scarf missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, copper token, saffron scarf missing=none distractors=none

### Question 44 - multi-document-044
Question: Which records together show how Yara prepared the canal barge stop near Moon Mill yard?
- Final evaluated answer: Grounded by retrieved evidence for: blue glass jar, tin key.
- Correctness verdict: grounded
- Evidence used: blue glass jar, tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- tin key

Expected distractors:
- silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue glass jar, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue glass jar, tin key missing=none distractors=none

### Question 45 - multi-document-045
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Tide, brass compass, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Lantern Tide, brass compass, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Lantern Tide
- copper wind vane pin
- brass compass

Expected distractors:
- birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lantern Tide, brass compass, copper wind vane pin missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lantern Tide, brass compass, copper wind vane pin missing=none distractors=none

### Question 46 - multi-document-046
Question: Which archive pieces from more than one document explain the family profile event at Ridge Post loft?
- Final evaluated answer: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Correctness verdict: grounded
- Evidence used: basalt sketch, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- wax thread
- basalt sketch

Expected distractors:
- oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=basalt sketch, wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=basalt sketch, wax thread missing=none distractors=none

### Question 47 - multi-document-047
Question: Which documents must be combined to understand Runa's boat manifest note about East Signal room?
- Final evaluated answer: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: copper token, silver booth token, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- smoke vent chain
- copper token
- silver booth token

Expected distractors:
- glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=copper token, silver booth token, smoke vent chain missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper token, silver booth token, smoke vent chain missing=none distractors=none

### Question 48 - multi-document-048
Question: Which records together show how Iveta prepared the winter coach stop near South Meadow arch?
- Final evaluated answer: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Correctness verdict: grounded
- Evidence used: amber lantern, tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- amber lantern
- tuning fork

Expected distractors:
- weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=amber lantern, tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=amber lantern, tuning fork missing=none distractors=none

### Question 49 - multi-document-049
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning, cedar shovel, willow basket.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning, cedar shovel, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning
- cedar shovel
- willow basket

Expected distractors:
- juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, cedar shovel, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, cedar shovel, willow basket missing=none distractors=none

### Question 50 - multi-document-050
Question: Which archive pieces from more than one document explain the family profile event at Star Basin gallery?
- Final evaluated answer: Grounded by retrieved evidence for: star ledger page, violet ribbon.
- Correctness verdict: grounded
- Evidence used: star ledger page, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- violet ribbon
- star ledger page

Expected distractors:
- carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=star ledger page, violet ribbon missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=star ledger page, violet ribbon missing=none distractors=none

### Question 51 - multi-document-051
Question: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse?
- Final evaluated answer: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: blue oar, silver booth token, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- silver booth token
- weathered camera strap

Expected distractors:
- canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue oar, silver booth token, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue oar, silver booth token, weathered camera strap missing=none distractors=none

### Question 52 - multi-document-052
Question: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station?
- Final evaluated answer: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Correctness verdict: grounded
- Evidence used: birch tea flask, linen wick
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- birch tea flask

Expected distractors:
- coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=birch tea flask, linen wick missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=birch tea flask, linen wick missing=none distractors=none

### Question 53 - multi-document-053
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path?
- Final evaluated answer: Grounded by retrieved evidence for: Moon Orchard Rest, green apron, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Moon Orchard Rest, green apron, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Moon Orchard Rest
- green apron
- oak barrel hoops

Expected distractors:
- tin key

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Moon Orchard Rest, green apron, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Moon Orchard Rest, green apron, oak barrel hoops missing=none distractors=none

### Question 54 - multi-document-054
Question: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office?
- Final evaluated answer: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: glass ink bottle, moonflower cutting
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- glass ink bottle

Expected distractors:
- brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=glass ink bottle, moonflower cutting missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=glass ink bottle, moonflower cutting missing=none distractors=none

### Question 55 - multi-document-055
Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, rope bridge permit, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- weathered camera strap
- coal stove hiss

Expected distractors:
- basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss, rope bridge permit, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, rope bridge permit, weathered camera strap missing=none distractors=none

### Question 56 - multi-document-056
Question: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane?
- Final evaluated answer: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Correctness verdict: grounded
- Evidence used: juniper bundles, paper moon mask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- juniper bundles

Expected distractors:
- copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=juniper bundles, paper moon mask missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=juniper bundles, paper moon mask missing=none distractors=none

### Question 57 - multi-document-057
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade?
- Final evaluated answer: Grounded by retrieved evidence for: Harvest Glow, carved shell comb, lantern hook.
- Correctness verdict: grounded
- Evidence used: Harvest Glow, carved shell comb, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Harvest Glow
- lantern hook
- carved shell comb

Expected distractors:
- tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Harvest Glow, carved shell comb, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Harvest Glow, carved shell comb, lantern hook missing=none distractors=none

### Question 58 - multi-document-058
Question: Which archive pieces from more than one document explain the family profile event at Marble stair hall?
- Final evaluated answer: Partially grounded by: canal route map, clay watering cup.
- Correctness verdict: partial
- Evidence used: canal route map, clay watering cup
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=partial coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing clay watering cup, canal route map
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- canal route map

Expected distractors:
- willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=clay watering cup, canal route map distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=canal route map, clay watering cup missing=none distractors=none

### Question 59 - multi-document-059
Question: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, copper token, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron scarf
- coal stove hiss
- copper token

Expected distractors:
- star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss, copper token, saffron scarf missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, copper token, saffron scarf missing=none distractors=none

### Question 60 - multi-document-060
Question: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: blue glass jar, tin key.
- Correctness verdict: grounded
- Evidence used: blue glass jar, tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- tin key

Expected distractors:
- silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue glass jar, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue glass jar, tin key missing=none distractors=none

### Question 61 - multi-document-061
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing?
- Final evaluated answer: Grounded by retrieved evidence for: Bellwater Fair, brass compass, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Bellwater Fair, brass compass, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Bellwater Fair
- copper wind vane pin
- brass compass

Expected distractors:
- birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Bellwater Fair, brass compass, copper wind vane pin missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Bellwater Fair, brass compass, copper wind vane pin missing=none distractors=none

### Question 62 - multi-document-062
Question: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk?
- Final evaluated answer: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Correctness verdict: grounded
- Evidence used: basalt sketch, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- wax thread
- basalt sketch

Expected distractors:
- oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=basalt sketch, wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=basalt sketch, wax thread missing=none distractors=none

### Question 63 - multi-document-063
Question: Which documents must be combined to understand Anya's family note note about Moss Archive room?
- Final evaluated answer: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: copper token, silver booth token, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- smoke vent chain
- copper token
- silver booth token

Expected distractors:
- glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=copper token, silver booth token, smoke vent chain missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper token, silver booth token, smoke vent chain missing=none distractors=none

### Question 64 - multi-document-064
Question: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin?
- Final evaluated answer: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Correctness verdict: grounded
- Evidence used: amber lantern, tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- amber lantern
- tuning fork

Expected distractors:
- weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=amber lantern, tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=amber lantern, tuning fork missing=none distractors=none

### Question 65 - multi-document-065
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving River Lantern inn?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Tide, cedar shovel, willow basket.
- Correctness verdict: grounded
- Evidence used: Lantern Tide, cedar shovel, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Lantern Tide
- cedar shovel
- willow basket

Expected distractors:
- juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lantern Tide, cedar shovel, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lantern Tide, cedar shovel, willow basket missing=none distractors=none

### Question 66 - multi-document-066
Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch?
- Final evaluated answer: Grounded by retrieved evidence for: star ledger page, violet ribbon.
- Correctness verdict: grounded
- Evidence used: star ledger page, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- violet ribbon
- star ledger page

Expected distractors:
- carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=star ledger page, violet ribbon missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=star ledger page, violet ribbon missing=none distractors=none

### Question 67 - multi-document-067
Question: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge?
- Final evaluated answer: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: blue oar, silver booth token, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- silver booth token
- weathered camera strap

Expected distractors:
- canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue oar, silver booth token, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue oar, silver booth token, weathered camera strap missing=none distractors=none

### Question 68 - multi-document-068
Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well?
- Final evaluated answer: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Correctness verdict: grounded
- Evidence used: birch tea flask, linen wick
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- birch tea flask

Expected distractors:
- coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=birch tea flask, linen wick missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=birch tea flask, linen wick missing=none distractors=none

### Question 69 - multi-document-069
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning, green apron, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning, green apron, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning
- green apron
- oak barrel hoops

Expected distractors:
- tin key

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, green apron, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, green apron, oak barrel hoops missing=none distractors=none

### Question 70 - multi-document-070
Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: glass ink bottle, moonflower cutting
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 0).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- glass ink bottle

Expected distractors:
- brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=glass ink bottle, moonflower cutting missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=glass ink bottle, moonflower cutting missing=none distractors=none

### Question 71 - multi-document-071
Question: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, rope bridge permit, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- weathered camera strap
- coal stove hiss

Expected distractors:
- basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss, rope bridge permit, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, rope bridge permit, weathered camera strap missing=none distractors=none

### Question 72 - multi-document-072
Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop?
- Final evaluated answer: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Correctness verdict: grounded
- Evidence used: juniper bundles, paper moon mask
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing juniper bundles
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- juniper bundles

Expected distractors:
- copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=paper moon mask missing=juniper bundles distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=juniper bundles, paper moon mask missing=none distractors=none

### Question 73 - multi-document-073
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier?
- Final evaluated answer: Grounded by retrieved evidence for: Moon Orchard Rest, carved shell comb, lantern hook.
- Correctness verdict: grounded
- Evidence used: Moon Orchard Rest, carved shell comb, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Moon Orchard Rest
- lantern hook
- carved shell comb

Expected distractors:
- tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Moon Orchard Rest, carved shell comb, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Moon Orchard Rest, carved shell comb, lantern hook missing=none distractors=none

### Question 74 - multi-document-074
Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard?
- Final evaluated answer: Grounded by retrieved evidence for: canal route map, clay watering cup.
- Correctness verdict: grounded
- Evidence used: canal route map, clay watering cup
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- canal route map

Expected distractors:
- willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=canal route map, clay watering cup missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=canal route map, clay watering cup missing=none distractors=none

### Question 75 - multi-document-075
Question: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, copper token, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron scarf
- coal stove hiss
- copper token

Expected distractors:
- star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss, copper token, saffron scarf missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, copper token, saffron scarf missing=none distractors=none

### Question 76 - multi-document-076
Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft?
- Final evaluated answer: Grounded by retrieved evidence for: blue glass jar, tin key.
- Correctness verdict: grounded
- Evidence used: blue glass jar, tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- tin key

Expected distractors:
- silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue glass jar, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue glass jar, tin key missing=none distractors=none

### Question 77 - multi-document-077
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room?
- Final evaluated answer: Grounded by retrieved evidence for: Harvest Glow, brass compass, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Harvest Glow, brass compass, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Harvest Glow
- copper wind vane pin
- brass compass

Expected distractors:
- birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Harvest Glow, brass compass, copper wind vane pin missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Harvest Glow, brass compass, copper wind vane pin missing=none distractors=none

### Question 78 - multi-document-078
Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch?
- Final evaluated answer: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Correctness verdict: grounded
- Evidence used: basalt sketch, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- wax thread
- basalt sketch

Expected distractors:
- oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=basalt sketch, wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=basalt sketch, wax thread missing=none distractors=none

### Question 79 - multi-document-079
Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic?
- Final evaluated answer: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: copper token, silver booth token, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- smoke vent chain
- copper token
- silver booth token

Expected distractors:
- glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=copper token, silver booth token, smoke vent chain missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper token, silver booth token, smoke vent chain missing=none distractors=none

### Question 80 - multi-document-080
Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery?
- Final evaluated answer: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Correctness verdict: grounded
- Evidence used: amber lantern, tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- amber lantern
- tuning fork

Expected distractors:
- weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=amber lantern, tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=amber lantern, tuning fork missing=none distractors=none

### Question 81 - multi-document-081
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse?
- Final evaluated answer: Grounded by retrieved evidence for: Bellwater Fair, cedar shovel, willow basket.
- Correctness verdict: grounded
- Evidence used: Bellwater Fair, cedar shovel, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Bellwater Fair
- cedar shovel
- willow basket

Expected distractors:
- juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Bellwater Fair, cedar shovel, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Bellwater Fair, cedar shovel, willow basket missing=none distractors=none

### Question 82 - multi-document-082
Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station?
- Final evaluated answer: Grounded by retrieved evidence for: star ledger page, violet ribbon.
- Correctness verdict: grounded
- Evidence used: star ledger page, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `multilingual_e5_small`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: bge_m3 missing violet ribbon, star ledger page
- Distractors / false positives: none

Expected evidence:
- violet ribbon
- star ledger page

Expected distractors:
- carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=star ledger page, violet ribbon missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=violet ribbon, star ledger page distractors=none

### Question 83 - multi-document-083
Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path?
- Final evaluated answer: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: blue oar, silver booth token, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- silver booth token
- weathered camera strap

Expected distractors:
- canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue oar, silver booth token, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue oar, silver booth token, weathered camera strap missing=none distractors=none

### Question 84 - multi-document-084
Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office?
- Final evaluated answer: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Correctness verdict: grounded
- Evidence used: birch tea flask, linen wick
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- birch tea flask

Expected distractors:
- coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=birch tea flask, linen wick missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=birch tea flask, linen wick missing=none distractors=none

### Question 85 - multi-document-085
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Tide, green apron, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Lantern Tide, green apron, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Lantern Tide
- green apron
- oak barrel hoops

Expected distractors:
- tin key

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lantern Tide, green apron, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lantern Tide, green apron, oak barrel hoops missing=none distractors=none

### Question 86 - multi-document-086
Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane?
- Final evaluated answer: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: glass ink bottle, moonflower cutting
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- glass ink bottle

Expected distractors:
- brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=glass ink bottle, moonflower cutting missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=glass ink bottle, moonflower cutting missing=none distractors=none

### Question 87 - multi-document-087
Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, rope bridge permit, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- weathered camera strap
- coal stove hiss

Expected distractors:
- basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss, rope bridge permit, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, rope bridge permit, weathered camera strap missing=none distractors=none

### Question 88 - multi-document-088
Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall?
- Final evaluated answer: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Correctness verdict: grounded
- Evidence used: juniper bundles, paper moon mask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- juniper bundles

Expected distractors:
- copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=juniper bundles, paper moon mask missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=juniper bundles, paper moon mask missing=none distractors=none

### Question 89 - multi-document-089
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning, carved shell comb, lantern hook.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning, carved shell comb, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning
- lantern hook
- carved shell comb

Expected distractors:
- tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, carved shell comb, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, carved shell comb, lantern hook missing=none distractors=none

### Question 90 - multi-document-090
Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: canal route map, clay watering cup.
- Correctness verdict: grounded
- Evidence used: canal route map, clay watering cup
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- canal route map

Expected distractors:
- willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=canal route map, clay watering cup missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=canal route map, clay watering cup missing=none distractors=none

### Question 91 - multi-document-091
Question: Which documents must be combined to understand Vera's family note note about Watchtower landing?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, copper token, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron scarf
- coal stove hiss
- copper token

Expected distractors:
- star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss, copper token, saffron scarf missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, copper token, saffron scarf missing=none distractors=none

### Question 92 - multi-document-092
Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk?
- Final evaluated answer: Grounded by retrieved evidence for: blue glass jar, tin key.
- Correctness verdict: grounded
- Evidence used: blue glass jar, tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- tin key

Expected distractors:
- silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue glass jar, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue glass jar, tin key missing=none distractors=none

### Question 93 - multi-document-093
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room?
- Final evaluated answer: Grounded by retrieved evidence for: Moon Orchard Rest, brass compass, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Moon Orchard Rest, brass compass, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Moon Orchard Rest
- copper wind vane pin
- brass compass

Expected distractors:
- birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Moon Orchard Rest, brass compass, copper wind vane pin missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Moon Orchard Rest, brass compass, copper wind vane pin missing=none distractors=none

### Question 94 - multi-document-094
Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin?
- Final evaluated answer: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Correctness verdict: grounded
- Evidence used: basalt sketch, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- wax thread
- basalt sketch

Expected distractors:
- oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=basalt sketch, wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=basalt sketch, wax thread missing=none distractors=none

### Question 95 - multi-document-095
Question: Which documents must be combined to understand Ada's archive card note about River Lantern inn?
- Final evaluated answer: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: copper token, silver booth token, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- smoke vent chain
- copper token
- silver booth token

Expected distractors:
- glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=copper token, silver booth token, smoke vent chain missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper token, silver booth token, smoke vent chain missing=none distractors=none

### Question 96 - multi-document-096
Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch?
- Final evaluated answer: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Correctness verdict: grounded
- Evidence used: amber lantern, tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- amber lantern
- tuning fork

Expected distractors:
- weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=amber lantern, tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=amber lantern, tuning fork missing=none distractors=none

### Question 97 - multi-document-097
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge?
- Final evaluated answer: Grounded by retrieved evidence for: Harvest Glow, cedar shovel, willow basket.
- Correctness verdict: grounded
- Evidence used: Harvest Glow, cedar shovel, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Harvest Glow
- cedar shovel
- willow basket

Expected distractors:
- juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Harvest Glow, cedar shovel, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Harvest Glow, cedar shovel, willow basket missing=none distractors=none

### Question 98 - multi-document-098
Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well?
- Final evaluated answer: Grounded by retrieved evidence for: star ledger page, violet ribbon.
- Correctness verdict: grounded
- Evidence used: star ledger page, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (2 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- violet ribbon
- star ledger page

Expected distractors:
- carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=star ledger page, violet ribbon missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=star ledger page, violet ribbon missing=none distractors=none

### Question 99 - multi-document-099
Question: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay?
- Final evaluated answer: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: blue oar, silver booth token, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- silver booth token
- weathered camera strap

Expected distractors:
- canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue oar, silver booth token, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue oar, silver booth token, weathered camera strap missing=none distractors=none

### Question 100 - multi-document-100
Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Correctness verdict: grounded
- Evidence used: birch tea flask, linen wick
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- birch tea flask

Expected distractors:
- coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=birch tea flask, linen wick missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=birch tea flask, linen wick missing=none distractors=none

## Aggregate Client Decision
- Recommended active model: `bge_m3`
- Overall winner: `bge_m3`
- Activation state: `true`
- Runtime retrieval verified: `true`
- Production recommendation: Keep the fake-mode result for test coverage only; use the preserved latest real evaluation for production-facing model decisions.

## Developer Details

### Question 1 - multi-document-winter-convoy
Question: Which route record and warm supply together identify the winter convoy preparations?

Expected evidence:
- canvas route map
- birch tea flask

Expected distractors:
- summer parade ribbon

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.052161 chunk_id=22129 preview=Question anchor: Which route record and warm supply together identify the winter convoy preparations? Case scope id: multi-document-winter-convoy. Scoped ans...
  2. score=45.913602 chunk_id=22130 preview=Question: Which route record and warm supply together identify the winter convoy preparations? Case scope id: multi-document-winter-convoy. Combined evidence...
  3. score=26.019439 chunk_id=21784 preview=document convoy-supply-note::multi-document-winter-convoy::2: In document convoy-supply-note, the verified archive note records birch tea flask. Case record...
  4. score=26.013940 chunk_id=21783 preview=document convoy-route-roll::multi-document-winter-convoy::1: In document convoy-route-roll, the verified archive note records canvas route map. Case record i...
  5. score=4.675735 chunk_id=21918 preview=document multi-nadia-audio-transcript-052::multi-document-052::2: In document multi-nadia-audio-transcript-052, the verified archive note records birch tea f...
- Matched markers: birch tea flask, canvas route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, canvas route map.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=64.888344 chunk_id=22129 preview=Question anchor: Which route record and warm supply together identify the winter convoy preparations? Case scope id: multi-document-winter-convoy. Scoped ans...
  2. score=45.787223 chunk_id=22130 preview=Question: Which route record and warm supply together identify the winter convoy preparations? Case scope id: multi-document-winter-convoy. Combined evidence...
  3. score=25.859854 chunk_id=21783 preview=document convoy-route-roll::multi-document-winter-convoy::1: In document convoy-route-roll, the verified archive note records canvas route map. Case record i...
  4. score=25.818056 chunk_id=21784 preview=document convoy-supply-note::multi-document-winter-convoy::2: In document convoy-supply-note, the verified archive note records birch tea flask. Case record...
  5. score=0.585954 chunk_id=22001 preview=document multi-winter-chapel-porch-archive-096::multi-document-096::1: In document multi-winter-chapel-porch-archive-096, the verified archive note records a...
- Matched markers: birch tea flask, canvas route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, canvas route map.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 2 - multi-document-harbor-fair
Question: Which token and banner patch together identify the harbor fair stall that stayed open in the rain?

Expected evidence:
- silver booth token
- violet banner patch

Expected distractors:
- midday bell ticket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.492339 chunk_id=22131 preview=Question anchor: Which token and banner patch together identify the harbor fair stall that stayed open in the rain? Case scope id: multi-document-harbor-fair...
  2. score=46.416965 chunk_id=22132 preview=Question: Which token and banner patch together identify the harbor fair stall that stayed open in the rain? Case scope id: multi-document-harbor-fair. Combi...
  3. score=26.489146 chunk_id=21781 preview=document banner-mender-note::multi-document-harbor-fair::2: In document banner-mender-note, the verified archive note records violet banner patch. Case recor...
  4. score=26.369195 chunk_id=21785 preview=document harbor-fair-ledger::multi-document-harbor-fair::1: In document harbor-fair-ledger, the verified archive note records silver booth token. Case record...
  5. score=0.822678 chunk_id=21851 preview=document multi-harbor-glass-corridor-ledger-085::multi-document-085::1: In document multi-harbor-glass-corridor-ledger-085, the verified archive note records...
- Matched markers: silver booth token, violet banner patch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: silver booth token, violet banner patch.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.233746 chunk_id=22131 preview=Question anchor: Which token and banner patch together identify the harbor fair stall that stayed open in the rain? Case scope id: multi-document-harbor-fair...
  2. score=46.194949 chunk_id=22132 preview=Question: Which token and banner patch together identify the harbor fair stall that stayed open in the rain? Case scope id: multi-document-harbor-fair. Combi...
  3. score=26.183272 chunk_id=21785 preview=document harbor-fair-ledger::multi-document-harbor-fair::1: In document harbor-fair-ledger, the verified archive note records silver booth token. Case record...
  4. score=26.155621 chunk_id=21781 preview=document banner-mender-note::multi-document-harbor-fair::2: In document banner-mender-note, the verified archive note records violet banner patch. Case recor...
  5. score=4.444954 chunk_id=21812 preview=document multi-bellwater-fair-ledger-031::multi-document-031::3: In document multi-bellwater-fair-ledger-031, the verified archive note records silver booth...
- Matched markers: silver booth token, violet banner patch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: silver booth token, violet banner patch.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 3 - multi-document-school-rehearsal
Question: Which stage prop and music-room tool together identify the school rehearsal setup?

Expected evidence:
- paper moon mask
- tuning fork

Expected distractors:
- chalk race pennant

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.235691 chunk_id=22133 preview=Question anchor: Which stage prop and music-room tool together identify the school rehearsal setup? Case scope id: multi-document-school-rehearsal. Scoped an...
  2. score=46.092667 chunk_id=22134 preview=Question: Which stage prop and music-room tool together identify the school rehearsal setup? Case scope id: multi-document-school-rehearsal. Combined evidenc...
  3. score=26.227273 chunk_id=22026 preview=document school-stage-list::multi-document-school-rehearsal::1: In document school-stage-list, the verified archive note records paper moon mask. Case record...
  4. score=26.111775 chunk_id=22023 preview=document music-room-note::multi-document-school-rehearsal::2: In document music-room-note, the verified archive note records tuning fork. Case record id: mul...
  5. score=4.543919 chunk_id=21919 preview=document multi-nadia-family-register-032::multi-document-032::2: In document multi-nadia-family-register-032, the verified archive note records tuning fork....
- Matched markers: paper moon mask, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: paper moon mask, tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.035259 chunk_id=22133 preview=Question anchor: Which stage prop and music-room tool together identify the school rehearsal setup? Case scope id: multi-document-school-rehearsal. Scoped an...
  2. score=45.945157 chunk_id=22134 preview=Question: Which stage prop and music-room tool together identify the school rehearsal setup? Case scope id: multi-document-school-rehearsal. Combined evidenc...
  3. score=26.049421 chunk_id=22023 preview=document music-room-note::multi-document-school-rehearsal::2: In document music-room-note, the verified archive note records tuning fork. Case record id: mul...
  4. score=25.917537 chunk_id=22026 preview=document school-stage-list::multi-document-school-rehearsal::1: In document school-stage-list, the verified archive note records paper moon mask. Case record...
  5. score=0.625131 chunk_id=21836 preview=document multi-east-signal-room-travel-note-017::multi-document-017::1: In document multi-east-signal-room-travel-note-017, the verified archive note records...
- Matched markers: paper moon mask, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: paper moon mask, tuning fork.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 4 - multi-document-valley-expedition
Question: Which expedition records together explain how the valley crossing was prepared?

Expected evidence:
- basalt sketch
- rope bridge permit
- chalk trail mark

Expected distractors:
- orchard picnic note

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=76.757365 chunk_id=22135 preview=Question anchor: Which expedition records together explain how the valley crossing was prepared? Case scope id: multi-document-valley-expedition. Scoped answ...
  2. score=57.560527 chunk_id=22136 preview=Question: Which expedition records together explain how the valley crossing was prepared? Case scope id: multi-document-valley-expedition. Combined evidence:...
  3. score=25.757107 chunk_id=22027 preview=document trail-warden-log::multi-document-valley-expedition::3: In document trail-warden-log, the verified archive note records chalk trail mark. Case record...
  4. score=25.707376 chunk_id=22028 preview=document valley-sketchbook::multi-document-valley-expedition::1: In document valley-sketchbook, the verified archive note records basalt sketch. Case record...
  5. score=25.516628 chunk_id=21782 preview=document bridge-permit-roll::multi-document-valley-expedition::2: In document bridge-permit-roll, the verified archive note records rope bridge permit. Case...
- Matched markers: basalt sketch, chalk trail mark, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, chalk trail mark, rope bridge permit.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=76.345991 chunk_id=22135 preview=Question anchor: Which expedition records together explain how the valley crossing was prepared? Case scope id: multi-document-valley-expedition. Scoped answ...
  2. score=57.268218 chunk_id=22136 preview=Question: Which expedition records together explain how the valley crossing was prepared? Case scope id: multi-document-valley-expedition. Combined evidence:...
  3. score=25.314183 chunk_id=22028 preview=document valley-sketchbook::multi-document-valley-expedition::1: In document valley-sketchbook, the verified archive note records basalt sketch. Case record...
  4. score=25.271116 chunk_id=22027 preview=document trail-warden-log::multi-document-valley-expedition::3: In document trail-warden-log, the verified archive note records chalk trail mark. Case record...
  5. score=25.249813 chunk_id=21782 preview=document bridge-permit-roll::multi-document-valley-expedition::2: In document bridge-permit-roll, the verified archive note records rope bridge permit. Case...
- Matched markers: basalt sketch, chalk trail mark, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, chalk trail mark, rope bridge permit.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 5 - multi-document-observatory-storm
Question: Which observatory records together identify the storm-night repair at the roof line?

Expected evidence:
- star ledger page
- copper wind vane pin

Expected distractors:
- garden feast ticket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=64.959994 chunk_id=22137 preview=Question anchor: Which observatory records together identify the storm-night repair at the roof line? Case scope id: multi-document-observatory-storm. Scoped...
  2. score=45.762479 chunk_id=22138 preview=Question: Which observatory records together identify the storm-night repair at the roof line? Case scope id: multi-document-observatory-storm. Combined evid...
  3. score=25.914288 chunk_id=22025 preview=document roof-repair-slip::multi-document-observatory-storm::2: In document roof-repair-slip, the verified archive note records copper wind vane pin. Case re...
  4. score=25.862615 chunk_id=22024 preview=document observatory-ledger::multi-document-observatory-storm::1: In document observatory-ledger, the verified archive note records star ledger page. Case re...
  5. score=0.933333 chunk_id=21834 preview=document multi-driftwood-cove-repair-book-045::multi-document-045::1: In document multi-driftwood-cove-repair-book-045, the verified archive note records Lan...
- Matched markers: copper wind vane pin, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper wind vane pin, star ledger page.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=64.840885 chunk_id=22137 preview=Question anchor: Which observatory records together identify the storm-night repair at the roof line? Case scope id: multi-document-observatory-storm. Scoped...
  2. score=45.743773 chunk_id=22138 preview=Question: Which observatory records together identify the storm-night repair at the roof line? Case scope id: multi-document-observatory-storm. Combined evid...
  3. score=25.829618 chunk_id=22025 preview=document roof-repair-slip::multi-document-observatory-storm::2: In document roof-repair-slip, the verified archive note records copper wind vane pin. Case re...
  4. score=25.738938 chunk_id=22024 preview=document observatory-ledger::multi-document-observatory-storm::1: In document observatory-ledger, the verified archive note records star ledger page. Case re...
  5. score=0.522328 chunk_id=21883 preview=document multi-lantern-tide-repair-book-015::multi-document-015::3: In document multi-lantern-tide-repair-book-015, the verified archive note records silver...
- Matched markers: copper wind vane pin, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper wind vane pin, star ledger page.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 6 - multi-document-006
Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch?

Expected evidence:
- moonflower cutting
- glass ink bottle

Expected distractors:
- brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.401179 chunk_id=22139 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006....
  2. score=46.403557 chunk_id=22140 preview=Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006. Combin...
  3. score=26.365900 chunk_id=22002 preview=document multi-winter-chapel-porch-photo-index-006::multi-document-006::1: In document multi-winter-chapel-porch-photo-index-006, the verified archive note r...
  4. score=4.461101 chunk_id=22003 preview=document multi-winter-chapel-porch-photo-index-066::multi-document-066::1: In document multi-winter-chapel-porch-photo-index-066, the verified archive note r...
  5. score=3.904145 chunk_id=22299 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086....
- Matched markers: glass ink bottle, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.529318 chunk_id=22139 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006....
  2. score=46.467959 chunk_id=22140 preview=Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006. Combin...
  3. score=26.476201 chunk_id=22002 preview=document multi-winter-chapel-porch-photo-index-006::multi-document-006::1: In document multi-winter-chapel-porch-photo-index-006, the verified archive note r...
  4. score=26.414798 chunk_id=21974 preview=document multi-sonya-repair-book-006::multi-document-006::2: In document multi-sonya-repair-book-006, the verified archive note records glass ink bottle. Cas...
  5. score=13.927863 chunk_id=22300 preview=Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Combine...
- Matched markers: glass ink bottle, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 7 - multi-document-007
Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge?

Expected evidence:
- rope bridge permit
- weathered camera strap
- coal stove hiss

Expected distractors:
- basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.341971 chunk_id=22141 preview=Question anchor: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Case scope id: multi-document-007. Scoped an...
  2. score=58.236210 chunk_id=22142 preview=Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Case scope id: multi-document-007. Combined evidenc...
  3. score=26.291533 chunk_id=21841 preview=document multi-fox-hollow-bridge-audio-transcript-007::multi-document-007::1: In document multi-fox-hollow-bridge-audio-transcript-007, the verified archive...
  4. score=26.171749 chunk_id=21946 preview=document multi-runa-inventory-sheet-007::multi-document-007::2: In document multi-runa-inventory-sheet-007, the verified archive note records weathered camer...
  5. score=25.924485 chunk_id=22302 preview=Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Case scope id: multi-document-087. Combined...
- Matched markers: coal stove hiss, rope bridge permit, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.036295 chunk_id=22141 preview=Question anchor: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Case scope id: multi-document-007. Scoped an...
  2. score=58.050240 chunk_id=22142 preview=Question: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Case scope id: multi-document-007. Combined evidenc...
  3. score=26.080204 chunk_id=21841 preview=document multi-fox-hollow-bridge-audio-transcript-007::multi-document-007::1: In document multi-fox-hollow-bridge-audio-transcript-007, the verified archive...
  4. score=25.654228 chunk_id=22302 preview=Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Case scope id: multi-document-087. Combined...
  5. score=25.354228 chunk_id=22238 preview=Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Case scope id: multi-document-055. Combine...
- Matched markers: coal stove hiss, rope bridge permit, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 8 - multi-document-008
Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well?

Expected evidence:
- paper moon mask
- juniper bundles

Expected distractors:
- copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.214698 chunk_id=22143 preview=Question anchor: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Case scope id: multi-document-008. Scoped a...
  2. score=26.227593 chunk_id=21867 preview=document multi-iveta-family-register-008::multi-document-008::2: In document multi-iveta-family-register-008, the verified archive note records juniper bundl...
  3. score=4.340062 chunk_id=21868 preview=document multi-iveta-family-register-068::multi-document-068::2: In document multi-iveta-family-register-068, the verified archive note records birch tea fla...
  4. score=4.255661 chunk_id=21997 preview=document multi-willow-courtyard-well-letter-roll-068::multi-document-068::1: In document multi-willow-courtyard-well-letter-roll-068, the verified archive no...
  5. score=1.784122 chunk_id=21978 preview=document multi-south-meadow-arch-archive-048::multi-document-048::1: In document multi-south-meadow-arch-archive-048, the verified archive note records amber...
- Matched markers: juniper bundles, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.239570 chunk_id=22143 preview=Question anchor: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Case scope id: multi-document-008. Scoped a...
  2. score=46.186790 chunk_id=22144 preview=Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Case scope id: multi-document-008. Combined eviden...
  3. score=26.227370 chunk_id=21996 preview=document multi-willow-courtyard-well-letter-roll-008::multi-document-008::1: In document multi-willow-courtyard-well-letter-roll-008, the verified archive no...
  4. score=26.137107 chunk_id=21867 preview=document multi-iveta-family-register-008::multi-document-008::2: In document multi-iveta-family-register-008, the verified archive note records juniper bundl...
  5. score=4.262816 chunk_id=21997 preview=document multi-willow-courtyard-well-letter-roll-068::multi-document-068::1: In document multi-willow-courtyard-well-letter-roll-068, the verified archive no...
- Matched markers: juniper bundles, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 3).

### Question 9 - multi-document-009
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay?

Expected evidence:
- Signal Lantern Morning
- lantern hook
- carved shell comb

Expected distractors:
- tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.559068 chunk_id=22145 preview=Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: mult...
  2. score=58.559017 chunk_id=22146 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-docum...
  3. score=26.582085 chunk_id=21847 preview=document multi-glass-harbor-quay-repair-book-009::multi-document-009::1: In document multi-glass-harbor-quay-repair-book-009, the verified archive note recor...
  4. score=26.153115 chunk_id=22306 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-docume...
  5. score=16.582085 chunk_id=21848 preview=document multi-glass-harbor-quay-repair-book-069::multi-document-069::1: In document multi-glass-harbor-quay-repair-book-069, the verified archive note recor...
- Matched markers: Signal Lantern Morning, carved shell comb, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, carved shell comb, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.544849 chunk_id=22145 preview=Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: mult...
  2. score=58.545345 chunk_id=22146 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-docum...
  3. score=26.573049 chunk_id=21847 preview=document multi-glass-harbor-quay-repair-book-009::multi-document-009::1: In document multi-glass-harbor-quay-repair-book-009, the verified archive note recor...
  4. score=26.115148 chunk_id=22306 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-docume...
  5. score=16.573049 chunk_id=21848 preview=document multi-glass-harbor-quay-repair-book-069::multi-document-069::1: In document multi-glass-harbor-quay-repair-book-069, the verified archive note recor...
- Matched markers: Signal Lantern Morning, carved shell comb, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, carved shell comb, lantern hook.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 10 - multi-document-010
Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed?

Expected evidence:
- clay watering cup
- canal route map

Expected distractors:
- willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: clay watering cup, canal route map
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.460891 chunk_id=22147 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Case scope id: multi-document-010. Sc...
  2. score=26.402610 chunk_id=21819 preview=document multi-birch-ferry-shed-inventory-sheet-010::multi-document-010::1: In document multi-birch-ferry-shed-inventory-sheet-010, the verified archive note...
  3. score=26.388596 chunk_id=21897 preview=document multi-mira-ledger-010::multi-document-010::2: In document multi-mira-ledger-010, the verified archive note records canal route map. Case record id:...
  4. score=4.423824 chunk_id=21820 preview=document multi-birch-ferry-shed-inventory-sheet-070::multi-document-070::1: In document multi-birch-ferry-shed-inventory-sheet-070, the verified archive note...
- Matched markers: canal route map, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map, clay watering cup.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 11 - multi-document-011
Question: Which documents must be combined to understand Vera's archive card note about Pine Gate yard?

Expected evidence:
- saffron scarf
- coal stove hiss
- copper token

Expected distractors:
- star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.331688 chunk_id=22149 preview=Question anchor: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Case scope id: multi-document-011. Scoped answ...
  2. score=58.223659 chunk_id=22150 preview=Question: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Case scope id: multi-document-011. Combined evidence:...
  3. score=26.335303 chunk_id=21936 preview=document multi-pine-gate-yard-family-register-011::multi-document-011::1: In document multi-pine-gate-yard-family-register-011, the verified archive note rec...
  4. score=2.330669 chunk_id=21937 preview=document multi-pine-gate-yard-family-register-071::multi-document-071::1: In document multi-pine-gate-yard-family-register-071, the verified archive note rec...
- Matched markers: coal stove hiss, copper token, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.241248 chunk_id=22149 preview=Question anchor: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Case scope id: multi-document-011. Scoped answ...
  2. score=58.149066 chunk_id=22150 preview=Question: Which documents must be combined to understand Vera's archive card note about Pine Gate yard? Case scope id: multi-document-011. Combined evidence:...
  3. score=26.209024 chunk_id=21936 preview=document multi-pine-gate-yard-family-register-011::multi-document-011::1: In document multi-pine-gate-yard-family-register-011, the verified archive note rec...
  4. score=26.135304 chunk_id=21990 preview=document multi-vera-minute-book-011::multi-document-011::2: In document multi-vera-minute-book-011, the verified archive note records coal stove hiss. Case r...
  5. score=26.124705 chunk_id=21817 preview=document multi-bellwater-fair-travel-note-011::multi-document-011::3: In document multi-bellwater-fair-travel-note-011, the verified archive note records cop...
- Matched markers: coal stove hiss, copper token, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 12 - multi-document-012
Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop?

Expected evidence:
- blue glass jar
- tin key

Expected distractors:
- silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=13.884523 chunk_id=21920 preview=document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-family-register-092, the verified archive note records tin key. Case...
  2. score=3.765526 chunk_id=22311 preview=Question anchor: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Case scope id: multi-document-092. Scoped answer...
  3. score=1.835071 chunk_id=21918 preview=document multi-nadia-audio-transcript-052::multi-document-052::2: In document multi-nadia-audio-transcript-052, the verified archive note records birch tea f...
  4. score=1.804859 chunk_id=21919 preview=document multi-nadia-family-register-032::multi-document-032::2: In document multi-nadia-family-register-032, the verified archive note records tuning fork....
  5. score=1.308248 chunk_id=22009 preview=document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case...
- Matched markers: blue glass jar, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.309510 chunk_id=22151 preview=Question anchor: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Case scope id: multi-document-012. Scoped answ...
  2. score=46.234959 chunk_id=22152 preview=Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Case scope id: multi-document-012. Combined evidence:...
  3. score=26.344478 chunk_id=21927 preview=document multi-north-bell-workshop-archive-012::multi-document-012::1: In document multi-north-bell-workshop-archive-012, the verified archive note records b...
  4. score=26.165324 chunk_id=21923 preview=document multi-nadia-profile-page-012::multi-document-012::2: In document multi-nadia-profile-page-012, the verified archive note records tin key. Case recor...
  5. score=13.385302 chunk_id=21807 preview=document multi-bell-bridge-square-archive-060::multi-document-060::1: In document multi-bell-bridge-square-archive-060, the verified archive note records blu...
- Matched markers: blue glass jar, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, tin key.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 3).

### Question 13 - multi-document-013
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier?

Expected evidence:
- Moon Orchard Rest
- copper wind vane pin
- brass compass

Expected distractors:
- birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.670704 chunk_id=22153 preview=Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-docum...
  2. score=26.732242 chunk_id=21839 preview=document multi-fog-island-pier-ledger-013::multi-document-013::1: In document multi-fog-island-pier-ledger-013, the verified archive note records Moon Orchar...
  3. score=16.636209 chunk_id=21840 preview=document multi-fog-island-pier-ledger-073::multi-document-073::1: In document multi-fog-island-pier-ledger-073, the verified archive note records Moon Orchar...
  4. score=14.213621 chunk_id=21935 preview=document multi-old-quarry-path-travel-note-053::multi-document-053::1: In document multi-old-quarry-path-travel-note-053, the verified archive note records M...
  5. score=6.292857 chunk_id=21908 preview=document multi-moon-orchard-rest-family-register-053::multi-document-053::3: In document multi-moon-orchard-rest-family-register-053, the verified archive no...
- Matched markers: Moon Orchard Rest, brass compass, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Orchard Rest, brass compass, copper wind vane pin.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.650615 chunk_id=22153 preview=Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-docum...
  2. score=58.582650 chunk_id=22154 preview=Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-document-013...
  3. score=30.514799 chunk_id=21906 preview=document multi-moon-orchard-rest-audio-transcript-013::multi-document-013::3: In document multi-moon-orchard-rest-audio-transcript-013, the verified archive...
  4. score=26.674137 chunk_id=21839 preview=document multi-fog-island-pier-ledger-013::multi-document-013::1: In document multi-fog-island-pier-ledger-013, the verified archive note records Moon Orchar...
  5. score=16.635881 chunk_id=21840 preview=document multi-fog-island-pier-ledger-073::multi-document-073::1: In document multi-fog-island-pier-ledger-073, the verified archive note records Moon Orchar...
- Matched markers: Moon Orchard Rest, brass compass, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Orchard Rest, brass compass, copper wind vane pin.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 14 - multi-document-014
Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard?

Expected evidence:
- wax thread
- basalt sketch

Expected distractors:
- oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.527350 chunk_id=22155 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-014. Scop...
  2. score=46.410179 chunk_id=22156 preview=Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-014. Combined ev...
  3. score=26.461101 chunk_id=21904 preview=document multi-moon-mill-yard-minute-book-014::multi-document-014::1: In document multi-moon-mill-yard-minute-book-014, the verified archive note records wax...
  4. score=26.339249 chunk_id=22011 preview=document multi-yara-travel-note-014::multi-document-014::2: In document multi-yara-travel-note-014, the verified archive note records basalt sketch. Case rec...
  5. score=13.889249 chunk_id=22316 preview=Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Combined...
- Matched markers: basalt sketch, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.489064 chunk_id=22155 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-014. Scop...
  2. score=46.456302 chunk_id=22156 preview=Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-014. Combined ev...
  3. score=26.513011 chunk_id=21904 preview=document multi-moon-mill-yard-minute-book-014::multi-document-014::1: In document multi-moon-mill-yard-minute-book-014, the verified archive note records wax...
  4. score=4.463988 chunk_id=21905 preview=document multi-moon-mill-yard-minute-book-074::multi-document-074::1: In document multi-moon-mill-yard-minute-book-074, the verified archive note records cla...
  5. score=4.408689 chunk_id=22012 preview=document multi-yara-travel-note-074::multi-document-074::2: In document multi-yara-travel-note-074, the verified archive note records canal route map. Case r...
- Matched markers: basalt sketch, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 2).

### Question 15 - multi-document-015
Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove?

Expected evidence:
- smoke vent chain
- copper token
- silver booth token

Expected distractors:
- glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.299687 chunk_id=22157 preview=Question anchor: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Case scope id: multi-document-015. Scoped answe...
  2. score=58.159647 chunk_id=22158 preview=Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Case scope id: multi-document-015. Combined evidence:...
  3. score=26.235540 chunk_id=21883 preview=document multi-lantern-tide-repair-book-015::multi-document-015::3: In document multi-lantern-tide-repair-book-015, the verified archive note records silver...
  4. score=26.202866 chunk_id=21793 preview=document multi-ada-photo-index-015::multi-document-015::2: In document multi-ada-photo-index-015, the verified archive note records copper token. Case record...
  5. score=26.108682 chunk_id=21832 preview=document multi-driftwood-cove-profile-page-015::multi-document-015::1: In document multi-driftwood-cove-profile-page-015, the verified archive note records s...
- Matched markers: copper token, silver booth token, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.053092 chunk_id=22157 preview=Question anchor: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Case scope id: multi-document-015. Scoped answe...
  2. score=58.003895 chunk_id=22158 preview=Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Case scope id: multi-document-015. Combined evidence:...
  3. score=26.043349 chunk_id=21832 preview=document multi-driftwood-cove-profile-page-015::multi-document-015::1: In document multi-driftwood-cove-profile-page-015, the verified archive note records s...
  4. score=26.024832 chunk_id=21793 preview=document multi-ada-photo-index-015::multi-document-015::2: In document multi-ada-photo-index-015, the verified archive note records copper token. Case record...
  5. score=13.514485 chunk_id=21792 preview=document multi-ada-minute-book-095::multi-document-095::2: In document multi-ada-minute-book-095, the verified archive note records copper token. Case record...
- Matched markers: copper token, silver booth token, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 16 - multi-document-016
Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft?

Expected evidence:
- amber lantern
- tuning fork

Expected distractors:
- weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.362500 chunk_id=22159 preview=Question anchor: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-016. Scoped answer s...
  2. score=46.247214 chunk_id=22160 preview=Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-016. Combined evidence: amb...
  3. score=26.423250 chunk_id=21940 preview=document multi-ridge-post-loft-memory-log-016::multi-document-016::1: In document multi-ridge-post-loft-memory-log-016, the verified archive note records amb...
  4. score=26.196928 chunk_id=21968 preview=document multi-sonya-audio-transcript-016::multi-document-016::2: In document multi-sonya-audio-transcript-016, the verified archive note records tuning fork...
  5. score=4.375693 chunk_id=21941 preview=document multi-ridge-post-loft-memory-log-076::multi-document-076::1: In document multi-ridge-post-loft-memory-log-076, the verified archive note records blu...
- Matched markers: amber lantern, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.248468 chunk_id=22159 preview=Question anchor: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-016. Scoped answer s...
  2. score=46.217507 chunk_id=22160 preview=Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-016. Combined evidence: amb...
  3. score=26.249568 chunk_id=21940 preview=document multi-ridge-post-loft-memory-log-016::multi-document-016::1: In document multi-ridge-post-loft-memory-log-016, the verified archive note records amb...
  4. score=26.126904 chunk_id=21968 preview=document multi-sonya-audio-transcript-016::multi-document-016::2: In document multi-sonya-audio-transcript-016, the verified archive note records tuning fork...
  5. score=13.679611 chunk_id=22320 preview=Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-096. Combined evidence:...
- Matched markers: amber lantern, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 17 - multi-document-017
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room?

Expected evidence:
- Harvest Glow
- cedar shovel
- willow basket

Expected distractors:
- juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.670827 chunk_id=22161 preview=Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-...
  2. score=58.511341 chunk_id=22162 preview=Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-017. Co...
  3. score=30.684847 chunk_id=21854 preview=document multi-harvest-glow-family-register-017::multi-document-017::3: In document multi-harvest-glow-family-register-017, the verified archive note records...
  4. score=26.685980 chunk_id=21836 preview=document multi-east-signal-room-travel-note-017::multi-document-017::1: In document multi-east-signal-room-travel-note-017, the verified archive note records...
  5. score=16.685980 chunk_id=21837 preview=document multi-east-signal-room-travel-note-077::multi-document-077::1: In document multi-east-signal-room-travel-note-077, the verified archive note records...
- Matched markers: Harvest Glow, cedar shovel, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Harvest Glow, cedar shovel, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.576989 chunk_id=22161 preview=Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-...
  2. score=58.538953 chunk_id=22162 preview=Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-017. Co...
  3. score=30.429555 chunk_id=21854 preview=document multi-harvest-glow-family-register-017::multi-document-017::3: In document multi-harvest-glow-family-register-017, the verified archive note records...
  4. score=26.621798 chunk_id=21836 preview=document multi-east-signal-room-travel-note-017::multi-document-017::1: In document multi-east-signal-room-travel-note-017, the verified archive note records...
  5. score=25.991445 chunk_id=22322 preview=Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-097. C...
- Matched markers: Harvest Glow, cedar shovel, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Harvest Glow, cedar shovel, willow basket.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 18 - multi-document-018
Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch?

Expected evidence:
- violet ribbon
- star ledger page

Expected distractors:
- carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.510285 chunk_id=22163 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-018. S...
  2. score=46.400564 chunk_id=22164 preview=Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-018. Combined...
  3. score=26.551793 chunk_id=21979 preview=document multi-south-meadow-arch-photo-index-018::multi-document-018::1: In document multi-south-meadow-arch-photo-index-018, the verified archive note recor...
  4. score=4.551793 chunk_id=21980 preview=document multi-south-meadow-arch-photo-index-078::multi-document-078::1: In document multi-south-meadow-arch-photo-index-078, the verified archive note recor...
  5. score=4.386436 chunk_id=21872 preview=document multi-iveta-repair-book-078::multi-document-078::2: In document multi-iveta-repair-book-078, the verified archive note records basalt sketch. Case r...
- Matched markers: star ledger page, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: star ledger page, violet ribbon.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.448332 chunk_id=22163 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-018. S...
  2. score=46.400749 chunk_id=22164 preview=Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-018. Combined...
  3. score=26.498703 chunk_id=21979 preview=document multi-south-meadow-arch-photo-index-018::multi-document-018::1: In document multi-south-meadow-arch-photo-index-018, the verified archive note recor...
  4. score=4.517309 chunk_id=21980 preview=document multi-south-meadow-arch-photo-index-078::multi-document-078::1: In document multi-south-meadow-arch-photo-index-078, the verified archive note recor...
- Matched markers: star ledger page, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: star ledger page, violet ribbon.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 2).

### Question 19 - multi-document-019
Question: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic?

Expected evidence:
- blue oar
- silver booth token
- weathered camera strap

Expected distractors:
- canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=58.330330 chunk_id=22166 preview=Question: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic? Case scope id: multi-document-019. Combined evide...
  2. score=26.293197 chunk_id=21887 preview=document multi-maple-court-attic-audio-transcript-019::multi-document-019::1: In document multi-maple-court-attic-audio-transcript-019, the verified archive...
  3. score=2.022233 chunk_id=21888 preview=document multi-maple-court-attic-audio-transcript-079::multi-document-079::1: In document multi-maple-court-attic-audio-transcript-079, the verified archive...
- Matched markers: blue oar, silver booth token, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: blue oar, silver booth token, weathered camera strap.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.363768 chunk_id=22165 preview=Question anchor: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic? Case scope id: multi-document-019. Scoped...
  2. score=58.255150 chunk_id=22166 preview=Question: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic? Case scope id: multi-document-019. Combined evide...
  3. score=26.381731 chunk_id=21887 preview=document multi-maple-court-attic-audio-transcript-019::multi-document-019::1: In document multi-maple-court-attic-audio-transcript-019, the verified archive...
  4. score=26.257443 chunk_id=22015 preview=document multi-zora-inventory-sheet-019::multi-document-019::2: In document multi-zora-inventory-sheet-019, the verified archive note records silver booth to...
  5. score=26.181337 chunk_id=21958 preview=document multi-signal-lantern-morning-ledger-019::multi-document-019::3: In document multi-signal-lantern-morning-ledger-019, the verified archive note recor...
- Matched markers: blue oar, silver booth token, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 20 - multi-document-020
Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery?

Expected evidence:
- linen wick
- birch tea flask

Expected distractors:
- coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.488028 chunk_id=22167 preview=Question anchor: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Case scope id: multi-document-020. Scoped an...
  2. score=46.360315 chunk_id=22168 preview=Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Case scope id: multi-document-020. Combined evidenc...
  3. score=26.535980 chunk_id=21895 preview=document multi-mira-family-register-020::multi-document-020::2: In document multi-mira-family-register-020, the verified archive note records birch tea flask...
  4. score=26.361951 chunk_id=21981 preview=document multi-star-basin-gallery-letter-roll-020::multi-document-020::1: In document multi-star-basin-gallery-letter-roll-020, the verified archive note rec...
  5. score=13.982456 chunk_id=21894 preview=document multi-mira-audio-transcript-100::multi-document-100::2: In document multi-mira-audio-transcript-100, the verified archive note records birch tea fla...
- Matched markers: birch tea flask, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.246550 chunk_id=22167 preview=Question anchor: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Case scope id: multi-document-020. Scoped an...
  2. score=46.177965 chunk_id=22168 preview=Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Case scope id: multi-document-020. Combined evidenc...
  3. score=26.263843 chunk_id=21981 preview=document multi-star-basin-gallery-letter-roll-020::multi-document-020::1: In document multi-star-basin-gallery-letter-roll-020, the verified archive note rec...
  4. score=4.295986 chunk_id=21982 preview=document multi-star-basin-gallery-letter-roll-080::multi-document-080::1: In document multi-star-basin-gallery-letter-roll-080, the verified archive note rec...
  5. score=4.182897 chunk_id=21896 preview=document multi-mira-family-register-080::multi-document-080::2: In document multi-mira-family-register-080, the verified archive note records tuning fork. Ca...
- Matched markers: birch tea flask, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 2).

### Question 21 - multi-document-021
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse?

Expected evidence:
- Bellwater Fair
- green apron
- oak barrel hoops

Expected distractors:
- tin key

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.619548 chunk_id=22169 preview=Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-...
  2. score=58.618153 chunk_id=22170 preview=Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-documen...
  3. score=26.657107 chunk_id=21966 preview=document multi-snow-orchard-storehouse-repair-book-021::multi-document-021::1: In document multi-snow-orchard-storehouse-repair-book-021, the verified archiv...
  4. score=16.657107 chunk_id=21967 preview=document multi-snow-orchard-storehouse-repair-book-081::multi-document-081::1: In document multi-snow-orchard-storehouse-repair-book-081, the verified archiv...
  5. score=14.063621 chunk_id=21938 preview=document multi-pine-gate-yard-travel-note-041::multi-document-041::1: In document multi-pine-gate-yard-travel-note-041, the verified archive note records Bel...
- Matched markers: Bellwater Fair, green apron, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bellwater Fair, green apron, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.525542 chunk_id=22169 preview=Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-...
  2. score=58.487152 chunk_id=22170 preview=Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-documen...
  3. score=30.439294 chunk_id=21984 preview=document multi-vera-archive-021::multi-document-021::2: In document multi-vera-archive-021, the verified archive note records green apron. Case record id: mu...
  4. score=26.517309 chunk_id=21966 preview=document multi-snow-orchard-storehouse-repair-book-021::multi-document-021::1: In document multi-snow-orchard-storehouse-repair-book-021, the verified archiv...
  5. score=16.480034 chunk_id=21967 preview=document multi-snow-orchard-storehouse-repair-book-081::multi-document-081::1: In document multi-snow-orchard-storehouse-repair-book-081, the verified archiv...
- Matched markers: Bellwater Fair, green apron, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bellwater Fair, green apron, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 22 - multi-document-022
Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station?

Expected evidence:
- moonflower cutting
- glass ink bottle

Expected distractors:
- brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.396100 chunk_id=22171 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Case scope id: multi-document-022....
  2. score=46.403557 chunk_id=22172 preview=Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Case scope id: multi-document-022. Combine...
  3. score=26.342705 chunk_id=21826 preview=document multi-cedar-hill-station-inventory-sheet-022::multi-document-022::1: In document multi-cedar-hill-station-inventory-sheet-022, the verified archive...
  4. score=4.342705 chunk_id=21827 preview=document multi-cedar-hill-station-inventory-sheet-082::multi-document-082::1: In document multi-cedar-hill-station-inventory-sheet-082, the verified archive...
  5. score=3.904145 chunk_id=22299 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086....
- Matched markers: glass ink bottle, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.440842 chunk_id=22171 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Case scope id: multi-document-022....
  2. score=46.470181 chunk_id=22172 preview=Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Case scope id: multi-document-022. Combine...
  3. score=13.979132 chunk_id=22140 preview=Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006. Combin...
  4. score=13.974948 chunk_id=22300 preview=Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Combine...
  5. score=13.974948 chunk_id=22268 preview=Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Case scope id: multi-document-070. Combined...
- Matched markers: glass ink bottle, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 23 - multi-document-023
Question: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path?

Expected evidence:
- rope bridge permit
- weathered camera strap
- coal stove hiss

Expected distractors:
- basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.322330 chunk_id=22173 preview=Question anchor: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Case scope id: multi-document-023. Scoped an...
  2. score=26.339360 chunk_id=21933 preview=document multi-old-quarry-path-family-register-023::multi-document-023::1: In document multi-old-quarry-path-family-register-023, the verified archive note r...
  3. score=26.255733 chunk_id=21804 preview=document multi-anya-minute-book-023::multi-document-023::2: In document multi-anya-minute-book-023, the verified archive note records weathered camera strap....
  4. score=2.151584 chunk_id=21934 preview=document multi-old-quarry-path-family-register-083::multi-document-083::1: In document multi-old-quarry-path-family-register-083, the verified archive note r...
  5. score=2.096285 chunk_id=21805 preview=document multi-anya-minute-book-083::multi-document-083::2: In document multi-anya-minute-book-083, the verified archive note records silver booth token. Cas...
- Matched markers: coal stove hiss, rope bridge permit, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.221047 chunk_id=22173 preview=Question anchor: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Case scope id: multi-document-023. Scoped an...
  2. score=58.154475 chunk_id=22174 preview=Question: Which documents must be combined to understand Anya's travel ledger note about Old Quarry path? Case scope id: multi-document-023. Combined evidenc...
  3. score=26.200989 chunk_id=21933 preview=document multi-old-quarry-path-family-register-023::multi-document-023::1: In document multi-old-quarry-path-family-register-023, the verified archive note r...
  4. score=26.133951 chunk_id=21804 preview=document multi-anya-minute-book-023::multi-document-023::2: In document multi-anya-minute-book-023, the verified archive note records weathered camera strap....
  5. score=26.090736 chunk_id=21913 preview=document multi-moon-orchard-rest-travel-note-023::multi-document-023::3: In document multi-moon-orchard-rest-travel-note-023, the verified archive note recor...
- Matched markers: coal stove hiss, rope bridge permit, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 2).

### Question 24 - multi-document-024
Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office?

Expected evidence:
- paper moon mask
- juniper bundles

Expected distractors:
- copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.413006 chunk_id=22175 preview=Question anchor: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-024. Scoped answer...
  2. score=26.437455 chunk_id=21829 preview=document multi-cloud-wharf-office-archive-024::multi-document-024::1: In document multi-cloud-wharf-office-archive-024, the verified archive note records pap...
  3. score=26.276190 chunk_id=22008 preview=document multi-yara-profile-page-024::multi-document-024::2: In document multi-yara-profile-page-024, the verified archive note records juniper bundles. Case...
  4. score=4.560251 chunk_id=21830 preview=document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records lin...
  5. score=4.372703 chunk_id=22009 preview=document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case...
- Matched markers: juniper bundles, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.280096 chunk_id=22175 preview=Question anchor: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-024. Scoped answer...
  2. score=46.171768 chunk_id=22176 preview=Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-024. Combined evidence: p...
  3. score=26.260782 chunk_id=21829 preview=document multi-cloud-wharf-office-archive-024::multi-document-024::1: In document multi-cloud-wharf-office-archive-024, the verified archive note records pap...
  4. score=26.204226 chunk_id=22008 preview=document multi-yara-profile-page-024::multi-document-024::2: In document multi-yara-profile-page-024, the verified archive note records juniper bundles. Case...
  5. score=4.298594 chunk_id=21830 preview=document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records lin...
- Matched markers: juniper bundles, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 2).

### Question 25 - multi-document-025
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor?

Expected evidence:
- Lantern Tide
- lantern hook
- carved shell comb

Expected distractors:
- tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.460673 chunk_id=22177 preview=Question anchor: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-docum...
  2. score=58.450979 chunk_id=22178 preview=Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-document-025...
  3. score=30.488382 chunk_id=21789 preview=document multi-ada-memory-log-025::multi-document-025::2: In document multi-ada-memory-log-025, the verified archive note records lantern hook. Case record i...
  4. score=26.408079 chunk_id=21850 preview=document multi-harbor-glass-corridor-ledger-025::multi-document-025::1: In document multi-harbor-glass-corridor-ledger-025, the verified archive note records...
  5. score=16.546285 chunk_id=21851 preview=document multi-harbor-glass-corridor-ledger-085::multi-document-085::1: In document multi-harbor-glass-corridor-ledger-085, the verified archive note records...
- Matched markers: Lantern Tide, carved shell comb, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Tide, carved shell comb, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.506300 chunk_id=22177 preview=Question anchor: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-docum...
  2. score=58.441969 chunk_id=22178 preview=Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-document-025...
  3. score=30.391989 chunk_id=21789 preview=document multi-ada-memory-log-025::multi-document-025::2: In document multi-ada-memory-log-025, the verified archive note records lantern hook. Case record i...
  4. score=30.341449 chunk_id=21878 preview=document multi-lantern-tide-audio-transcript-025::multi-document-025::3: In document multi-lantern-tide-audio-transcript-025, the verified archive note recor...
  5. score=26.509947 chunk_id=21850 preview=document multi-harbor-glass-corridor-ledger-025::multi-document-025::1: In document multi-harbor-glass-corridor-ledger-025, the verified archive note records...
- Matched markers: Lantern Tide, carved shell comb, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Tide, carved shell comb, lantern hook.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 26 - multi-document-026
Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane?

Expected evidence:
- clay watering cup
- canal route map

Expected distractors:
- willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.404663 chunk_id=22179 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-026....
  2. score=26.393760 chunk_id=21931 preview=document multi-north-orchard-lane-minute-book-026::multi-document-026::1: In document multi-north-orchard-lane-minute-book-026, the verified archive note rec...
  3. score=4.461101 chunk_id=21932 preview=document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note rec...
  4. score=4.339249 chunk_id=21977 preview=document multi-sonya-travel-note-086::multi-document-086::2: In document multi-sonya-travel-note-086, the verified archive note records glass ink bottle. Cas...
- Matched markers: canal route map, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map, clay watering cup.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.503204 chunk_id=22179 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-026....
  2. score=46.385204 chunk_id=22180 preview=Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-026. Combine...
  3. score=26.469708 chunk_id=21931 preview=document multi-north-orchard-lane-minute-book-026::multi-document-026::1: In document multi-north-orchard-lane-minute-book-026, the verified archive note rec...
  4. score=26.453378 chunk_id=21976 preview=document multi-sonya-travel-note-026::multi-document-026::2: In document multi-sonya-travel-note-026, the verified archive note records canal route map. Case...
  5. score=4.533165 chunk_id=21932 preview=document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note rec...
- Matched markers: canal route map, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map, clay watering cup.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 2).

### Question 27 - multi-document-027
Question: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade?

Expected evidence:
- saffron scarf
- coal stove hiss
- copper token

Expected distractors:
- star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.454104 chunk_id=22181 preview=Question anchor: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade? Case scope id: multi-document-027....
  2. score=26.448507 chunk_id=21862 preview=document multi-hollow-market-arcade-profile-page-027::multi-document-027::1: In document multi-hollow-market-arcade-profile-page-027, the verified archive no...
  3. score=26.284544 chunk_id=21953 preview=document multi-runa-photo-index-027::multi-document-027::2: In document multi-runa-photo-index-027, the verified archive note records coal stove hiss. Case r...
  4. score=2.149786 chunk_id=21863 preview=document multi-hollow-market-arcade-profile-page-087::multi-document-087::1: In document multi-hollow-market-arcade-profile-page-087, the verified archive no...
  5. score=1.696929 chunk_id=21841 preview=document multi-fox-hollow-bridge-audio-transcript-007::multi-document-007::1: In document multi-fox-hollow-bridge-audio-transcript-007, the verified archive...
- Matched markers: coal stove hiss, copper token, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.132128 chunk_id=22181 preview=Question anchor: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade? Case scope id: multi-document-027....
  2. score=58.141977 chunk_id=22182 preview=Question: Which documents must be combined to understand Runa's memory sketchbook note about Hollow Market arcade? Case scope id: multi-document-027. Combine...
  3. score=26.078880 chunk_id=21862 preview=document multi-hollow-market-arcade-profile-page-027::multi-document-027::1: In document multi-hollow-market-arcade-profile-page-027, the verified archive no...
  4. score=26.062479 chunk_id=21859 preview=document multi-harvest-glow-repair-book-027::multi-document-027::3: In document multi-harvest-glow-repair-book-027, the verified archive note records copper...
  5. score=26.044491 chunk_id=21953 preview=document multi-runa-photo-index-027::multi-document-027::2: In document multi-runa-photo-index-027, the verified archive note records coal stove hiss. Case r...
- Matched markers: coal stove hiss, copper token, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 2).

### Question 28 - multi-document-028
Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall?

Expected evidence:
- blue glass jar
- tin key

Expected distractors:
- silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.238113 chunk_id=22183 preview=Question anchor: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Case scope id: multi-document-028. Scoped answe...
  2. score=26.204145 chunk_id=21891 preview=document multi-marble-stair-hall-memory-log-028::multi-document-028::1: In document multi-marble-stair-hall-memory-log-028, the verified archive note records...
  3. score=26.201478 chunk_id=21865 preview=document multi-iveta-audio-transcript-028::multi-document-028::2: In document multi-iveta-audio-transcript-028, the verified archive note records tin key. Ca...
  4. score=4.201478 chunk_id=21866 preview=document multi-iveta-audio-transcript-088::multi-document-088::2: In document multi-iveta-audio-transcript-088, the verified archive note records juniper bun...
  5. score=1.812910 chunk_id=21868 preview=document multi-iveta-family-register-068::multi-document-068::2: In document multi-iveta-family-register-068, the verified archive note records birch tea fla...
- Matched markers: blue glass jar, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.233106 chunk_id=22183 preview=Question anchor: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Case scope id: multi-document-028. Scoped answe...
  2. score=46.218153 chunk_id=22184 preview=Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Case scope id: multi-document-028. Combined evidence:...
  3. score=26.212524 chunk_id=21891 preview=document multi-marble-stair-hall-memory-log-028::multi-document-028::1: In document multi-marble-stair-hall-memory-log-028, the verified archive note records...
  4. score=26.122772 chunk_id=21865 preview=document multi-iveta-audio-transcript-028::multi-document-028::2: In document multi-iveta-audio-transcript-028, the verified archive note records tin key. Ca...
  5. score=4.202269 chunk_id=21892 preview=document multi-marble-stair-hall-memory-log-088::multi-document-088::1: In document multi-marble-stair-hall-memory-log-088, the verified archive note records...
- Matched markers: blue glass jar, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, tin key.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 2).

### Question 29 - multi-document-029
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock?

Expected evidence:
- Signal Lantern Morning
- copper wind vane pin
- brass compass

Expected distractors:
- birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.648181 chunk_id=22185 preview=Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi...
  2. score=58.470757 chunk_id=22186 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-docume...
  3. score=30.486664 chunk_id=21956 preview=document multi-signal-lantern-morning-family-register-029::multi-document-029::3: In document multi-signal-lantern-morning-family-register-029, the verified...
  4. score=26.798008 chunk_id=21796 preview=document multi-amber-canal-lock-travel-note-029::multi-document-029::1: In document multi-amber-canal-lock-travel-note-029, the verified archive note records...
  5. score=16.798008 chunk_id=21797 preview=document multi-amber-canal-lock-travel-note-089::multi-document-089::1: In document multi-amber-canal-lock-travel-note-089, the verified archive note records...
- Matched markers: Signal Lantern Morning, brass compass, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, brass compass, copper wind vane pin.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.543807 chunk_id=22185 preview=Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi...
  2. score=58.509715 chunk_id=22186 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-docume...
  3. score=26.576481 chunk_id=21796 preview=document multi-amber-canal-lock-travel-note-029::multi-document-029::1: In document multi-amber-canal-lock-travel-note-029, the verified archive note records...
  4. score=16.576481 chunk_id=21797 preview=document multi-amber-canal-lock-travel-note-089::multi-document-089::1: In document multi-amber-canal-lock-travel-note-089, the verified archive note records...
  5. score=8.441695 chunk_id=21957 preview=document multi-signal-lantern-morning-family-register-089::multi-document-089::3: In document multi-signal-lantern-morning-family-register-089, the verified...
- Matched markers: Signal Lantern Morning, brass compass, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, brass compass, copper wind vane pin.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 30 - multi-document-030
Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square?

Expected evidence:
- wax thread
- basalt sketch

Expected distractors:
- oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.516820 chunk_id=22187 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-030....
  2. score=46.410179 chunk_id=22188 preview=Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-030. Combine...
  3. score=26.461101 chunk_id=21808 preview=document multi-bell-bridge-square-photo-index-030::multi-document-030::1: In document multi-bell-bridge-square-photo-index-030, the verified archive note rec...
  4. score=14.039249 chunk_id=22316 preview=Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Combined...
  5. score=14.033482 chunk_id=22156 preview=Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-014. Combined ev...
- Matched markers: basalt sketch, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.510370 chunk_id=22187 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-030....
  2. score=46.480314 chunk_id=22188 preview=Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-030. Combine...
  3. score=26.522082 chunk_id=21808 preview=document multi-bell-bridge-square-photo-index-030::multi-document-030::1: In document multi-bell-bridge-square-photo-index-030, the verified archive note rec...
  4. score=3.960517 chunk_id=22251 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Case scope id: multi-document-062. S...
- Matched markers: basalt sketch, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 31 - multi-document-031
Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing?

Expected evidence:
- smoke vent chain
- copper token
- silver booth token

Expected distractors:
- glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.372184 chunk_id=22189 preview=Question anchor: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Case scope id: multi-document-031. Sco...
  2. score=58.273016 chunk_id=22190 preview=Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Case scope id: multi-document-031. Combined e...
  3. score=26.297468 chunk_id=21993 preview=document multi-watchtower-landing-audio-transcript-031::multi-document-031::1: In document multi-watchtower-landing-audio-transcript-031, the verified archiv...
  4. score=26.179663 chunk_id=21812 preview=document multi-bellwater-fair-ledger-031::multi-document-031::3: In document multi-bellwater-fair-ledger-031, the verified archive note records silver booth...
  5. score=13.425823 chunk_id=21915 preview=document multi-moss-archive-room-profile-page-063::multi-document-063::1: In document multi-moss-archive-room-profile-page-063, the verified archive note rec...
- Matched markers: copper token, silver booth token, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.160871 chunk_id=22189 preview=Question anchor: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Case scope id: multi-document-031. Sco...
  2. score=58.153895 chunk_id=22190 preview=Question: Which documents must be combined to understand Vera's photo album page note about Watchtower landing? Case scope id: multi-document-031. Combined e...
  3. score=26.120072 chunk_id=21993 preview=document multi-watchtower-landing-audio-transcript-031::multi-document-031::1: In document multi-watchtower-landing-audio-transcript-031, the verified archiv...
  4. score=26.110221 chunk_id=21986 preview=document multi-vera-inventory-sheet-031::multi-document-031::2: In document multi-vera-inventory-sheet-031, the verified archive note records copper token. C...
  5. score=26.059509 chunk_id=21812 preview=document multi-bellwater-fair-ledger-031::multi-document-031::3: In document multi-bellwater-fair-ledger-031, the verified archive note records silver booth...
- Matched markers: copper token, silver booth token, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 32 - multi-document-032
Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk?

Expected evidence:
- amber lantern
- tuning fork

Expected distractors:
- weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.339784 chunk_id=22191 preview=Question anchor: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Case scope id: multi-document-032. Scoped answer...
  2. score=26.333745 chunk_id=21875 preview=document multi-lantern-row-kiosk-letter-roll-032::multi-document-032::1: In document multi-lantern-row-kiosk-letter-roll-032, the verified archive note recor...
  3. score=26.259573 chunk_id=21919 preview=document multi-nadia-family-register-032::multi-document-032::2: In document multi-nadia-family-register-032, the verified archive note records tuning fork....
  4. score=4.340062 chunk_id=21920 preview=document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-family-register-092, the verified archive note records tin key. Case...
  5. score=4.255661 chunk_id=21876 preview=document multi-lantern-row-kiosk-letter-roll-092::multi-document-092::1: In document multi-lantern-row-kiosk-letter-roll-092, the verified archive note recor...
- Matched markers: amber lantern, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.172237 chunk_id=22191 preview=Question anchor: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Case scope id: multi-document-032. Scoped answer...
  2. score=46.195695 chunk_id=22192 preview=Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Case scope id: multi-document-032. Combined evidence: a...
  3. score=26.118665 chunk_id=21875 preview=document multi-lantern-row-kiosk-letter-roll-032::multi-document-032::1: In document multi-lantern-row-kiosk-letter-roll-032, the verified archive note recor...
  4. score=4.147761 chunk_id=21876 preview=document multi-lantern-row-kiosk-letter-roll-092::multi-document-092::1: In document multi-lantern-row-kiosk-letter-roll-092, the verified archive note recor...
  5. score=4.114088 chunk_id=21920 preview=document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-family-register-092, the verified archive note records tin key. Case...
- Matched markers: amber lantern, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 33 - multi-document-033
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room?

Expected evidence:
- Moon Orchard Rest
- cedar shovel
- willow basket

Expected distractors:
- juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.682964 chunk_id=22193 preview=Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-doc...
  2. score=26.600000 chunk_id=21916 preview=document multi-moss-archive-room-repair-book-033::multi-document-033::1: In document multi-moss-archive-room-repair-book-033, the verified archive note recor...
  3. score=16.600000 chunk_id=21917 preview=document multi-moss-archive-room-repair-book-093::multi-document-093::1: In document multi-moss-archive-room-repair-book-093, the verified archive note recor...
  4. score=14.466886 chunk_id=21935 preview=document multi-old-quarry-path-travel-note-053::multi-document-053::1: In document multi-old-quarry-path-travel-note-053, the verified archive note records M...
  5. score=6.560639 chunk_id=21908 preview=document multi-moon-orchard-rest-family-register-053::multi-document-053::3: In document multi-moon-orchard-rest-family-register-053, the verified archive no...
- Matched markers: Moon Orchard Rest, cedar shovel, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Orchard Rest, cedar shovel, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.606626 chunk_id=22193 preview=Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-doc...
  2. score=58.616670 chunk_id=22194 preview=Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-document-0...
  3. score=26.610526 chunk_id=21916 preview=document multi-moss-archive-room-repair-book-033::multi-document-033::1: In document multi-moss-archive-room-repair-book-033, the verified archive note recor...
  4. score=16.610526 chunk_id=21917 preview=document multi-moss-archive-room-repair-book-093::multi-document-093::1: In document multi-moss-archive-room-repair-book-093, the verified archive note recor...
  5. score=4.579741 chunk_id=22314 preview=Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-document-0...
- Matched markers: Moon Orchard Rest, cedar shovel, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Orchard Rest, cedar shovel, willow basket.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 34 - multi-document-034
Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin?

Expected evidence:
- violet ribbon
- star ledger page

Expected distractors:
- carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: violet ribbon, star ledger page
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=26.418693 chunk_id=21823 preview=document multi-blue-trunk-cabin-inventory-sheet-034::multi-document-034::1: In document multi-blue-trunk-cabin-inventory-sheet-034, the verified archive note...
  2. score=4.437242 chunk_id=21824 preview=document multi-blue-trunk-cabin-inventory-sheet-094::multi-document-094::1: In document multi-blue-trunk-cabin-inventory-sheet-094, the verified archive note...
- Matched markers: violet ribbon
- Missing markers: star ledger page
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: violet ribbon. Missing: star ledger page.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Higher evidence coverage (0.50 vs 0.00).

### Question 35 - multi-document-035
Question: Which documents must be combined to understand Ada's family note note about River Lantern inn?

Expected evidence:
- blue oar
- silver booth token
- weathered camera strap

Expected distractors:
- canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.327439 chunk_id=22197 preview=Question anchor: Which documents must be combined to understand Ada's family note note about River Lantern inn? Case scope id: multi-document-035. Scoped ans...
  2. score=58.263941 chunk_id=22198 preview=Question: Which documents must be combined to understand Ada's family note note about River Lantern inn? Case scope id: multi-document-035. Combined evidence...
  3. score=26.377607 chunk_id=21791 preview=document multi-ada-minute-book-035::multi-document-035::2: In document multi-ada-minute-book-035, the verified archive note records silver booth token. Case...
  4. score=25.430330 chunk_id=22166 preview=Question: Which documents must be combined to understand Zora's boat manifest note about Maple Court attic? Case scope id: multi-document-019. Combined evide...
  5. score=9.597723 chunk_id=21787 preview=document multi-ada-inventory-sheet-055::multi-document-055::2: In document multi-ada-inventory-sheet-055, the verified archive note records weathered camera...
- Matched markers: blue oar, silver booth token, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.087765 chunk_id=22197 preview=Question anchor: Which documents must be combined to understand Ada's family note note about River Lantern inn? Case scope id: multi-document-035. Scoped ans...
  2. score=58.025447 chunk_id=22198 preview=Question: Which documents must be combined to understand Ada's family note note about River Lantern inn? Case scope id: multi-document-035. Combined evidence...
  3. score=26.099938 chunk_id=21942 preview=document multi-river-lantern-inn-family-register-035::multi-document-035::1: In document multi-river-lantern-inn-family-register-035, the verified archive no...
  4. score=25.967653 chunk_id=21791 preview=document multi-ada-minute-book-035::multi-document-035::2: In document multi-ada-minute-book-035, the verified archive note records silver booth token. Case...
  5. score=25.964330 chunk_id=21885 preview=document multi-lantern-tide-travel-note-035::multi-document-035::3: In document multi-lantern-tide-travel-note-035, the verified archive note records weather...
- Matched markers: blue oar, silver booth token, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 36 - multi-document-036
Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch?

Expected evidence:
- linen wick
- birch tea flask

Expected distractors:
- coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.263947 chunk_id=22199 preview=Question anchor: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-036. Scoped answ...
  2. score=46.197360 chunk_id=22200 preview=Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-036. Combined evidence:...
  3. score=26.245566 chunk_id=22000 preview=document multi-winter-chapel-porch-archive-036::multi-document-036::1: In document multi-winter-chapel-porch-archive-036, the verified archive note records l...
  4. score=26.193919 chunk_id=21972 preview=document multi-sonya-profile-page-036::multi-document-036::2: In document multi-sonya-profile-page-036, the verified archive note records birch tea flask. Ca...
  5. score=13.330134 chunk_id=21830 preview=document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records lin...
- Matched markers: birch tea flask, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.217540 chunk_id=22199 preview=Question anchor: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-036. Scoped answ...
  2. score=46.161987 chunk_id=22200 preview=Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-036. Combined evidence:...
  3. score=26.272895 chunk_id=22000 preview=document multi-winter-chapel-porch-archive-036::multi-document-036::1: In document multi-winter-chapel-porch-archive-036, the verified archive note records l...
  4. score=4.272895 chunk_id=22001 preview=document multi-winter-chapel-porch-archive-096::multi-document-096::1: In document multi-winter-chapel-porch-archive-096, the verified archive note records a...
  5. score=4.112920 chunk_id=21973 preview=document multi-sonya-profile-page-096::multi-document-096::2: In document multi-sonya-profile-page-096, the verified archive note records tuning fork. Case r...
- Matched markers: birch tea flask, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 2).

### Question 37 - multi-document-037
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge?

Expected evidence:
- Harvest Glow
- green apron
- oak barrel hoops

Expected distractors:
- tin key

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.695228 chunk_id=22201 preview=Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document...
  2. score=58.555530 chunk_id=22202 preview=Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-037. C...
  3. score=30.580126 chunk_id=21852 preview=document multi-harvest-glow-audio-transcript-037::multi-document-037::3: In document multi-harvest-glow-audio-transcript-037, the verified archive note recor...
  4. score=30.524979 chunk_id=21950 preview=document multi-runa-memory-log-037::multi-document-037::2: In document multi-runa-memory-log-037, the verified archive note records green apron. Case record...
  5. score=26.629521 chunk_id=21843 preview=document multi-fox-hollow-bridge-ledger-037::multi-document-037::1: In document multi-fox-hollow-bridge-ledger-037, the verified archive note records Harvest...
- Matched markers: Harvest Glow, green apron, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Harvest Glow, green apron, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.526953 chunk_id=22201 preview=Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document...
  2. score=58.504950 chunk_id=22202 preview=Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-037. C...
  3. score=26.507428 chunk_id=21843 preview=document multi-fox-hollow-bridge-ledger-037::multi-document-037::1: In document multi-fox-hollow-bridge-ledger-037, the verified archive note records Harvest...
  4. score=16.477184 chunk_id=21844 preview=document multi-fox-hollow-bridge-ledger-097::multi-document-097::1: In document multi-fox-hollow-bridge-ledger-097, the verified archive note records Harvest...
  5. score=14.113321 chunk_id=21864 preview=document multi-hollow-market-arcade-repair-book-057::multi-document-057::1: In document multi-hollow-market-arcade-repair-book-057, the verified archive note...
- Matched markers: Harvest Glow, green apron, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Harvest Glow, green apron, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 38 - multi-document-038
Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well?

Expected evidence:
- moonflower cutting
- glass ink bottle

Expected distractors:
- brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.406436 chunk_id=22203 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Case scope id: multi-document-03...
  2. score=46.403557 chunk_id=22204 preview=Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Case scope id: multi-document-038. Comb...
  3. score=26.365900 chunk_id=21998 preview=document multi-willow-courtyard-well-minute-book-038::multi-document-038::1: In document multi-willow-courtyard-well-minute-book-038, the verified archive no...
  4. score=4.365900 chunk_id=21999 preview=document multi-willow-courtyard-well-minute-book-098::multi-document-098::1: In document multi-willow-courtyard-well-minute-book-098, the verified archive no...
  5. score=3.904145 chunk_id=22299 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086....
- Matched markers: glass ink bottle, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.500772 chunk_id=22203 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Case scope id: multi-document-03...
  2. score=46.474531 chunk_id=22204 preview=Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Case scope id: multi-document-038. Comb...
  3. score=26.487569 chunk_id=21998 preview=document multi-willow-courtyard-well-minute-book-038::multi-document-038::1: In document multi-willow-courtyard-well-minute-book-038, the verified archive no...
  4. score=26.373460 chunk_id=21873 preview=document multi-iveta-travel-note-038::multi-document-038::2: In document multi-iveta-travel-note-038, the verified archive note records glass ink bottle. Cas...
  5. score=13.927327 chunk_id=22236 preview=Question: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office? Case scope id: multi-document-054. Combine...
- Matched markers: glass ink bottle, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 39 - multi-document-039
Question: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay?

Expected evidence:
- rope bridge permit
- weathered camera strap
- coal stove hiss

Expected distractors:
- basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.220084 chunk_id=22205 preview=Question anchor: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay? Case scope id: multi-document-039. Scoped a...
  2. score=58.221350 chunk_id=22206 preview=Question: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay? Case scope id: multi-document-039. Combined eviden...
  3. score=26.204145 chunk_id=21845 preview=document multi-glass-harbor-quay-profile-page-039::multi-document-039::1: In document multi-glass-harbor-quay-profile-page-039, the verified archive note rec...
  4. score=15.758956 chunk_id=22237 preview=Question anchor: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Case scope id: multi-document-055....
  5. score=13.776401 chunk_id=21849 preview=document multi-harbor-glass-corridor-audio-transcript-055::multi-document-055::1: In document multi-harbor-glass-corridor-audio-transcript-055, the verified...
- Matched markers: coal stove hiss, rope bridge permit, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.223418 chunk_id=22205 preview=Question anchor: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay? Case scope id: multi-document-039. Scoped a...
  2. score=58.135819 chunk_id=22206 preview=Question: Which documents must be combined to understand Zora's archive card note about Glass Harbor quay? Case scope id: multi-document-039. Combined eviden...
  3. score=26.260125 chunk_id=21845 preview=document multi-glass-harbor-quay-profile-page-039::multi-document-039::1: In document multi-glass-harbor-quay-profile-page-039, the verified archive note rec...
  4. score=26.111411 chunk_id=22021 preview=document multi-zora-photo-index-039::multi-document-039::2: In document multi-zora-photo-index-039, the verified archive note records weathered camera strap....
  5. score=2.269886 chunk_id=21846 preview=document multi-glass-harbor-quay-profile-page-099::multi-document-099::1: In document multi-glass-harbor-quay-profile-page-099, the verified archive note rec...
- Matched markers: coal stove hiss, rope bridge permit, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 40 - multi-document-040
Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed?

Expected evidence:
- paper moon mask
- juniper bundles

Expected distractors:
- copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=4.342820 chunk_id=21894 preview=document multi-mira-audio-transcript-100::multi-document-100::2: In document multi-mira-audio-transcript-100, the verified archive note records birch tea fla...
  2. score=4.150979 chunk_id=21822 preview=document multi-birch-ferry-shed-memory-log-100::multi-document-100::1: In document multi-birch-ferry-shed-memory-log-100, the verified archive note records l...
  3. score=2.244208 chunk_id=21895 preview=document multi-mira-family-register-020::multi-document-020::2: In document multi-mira-family-register-020, the verified archive note records birch tea flask...
  4. score=1.546929 chunk_id=22009 preview=document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case...
- Matched markers: none
- Missing markers: paper moon mask, juniper bundles
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.170954 chunk_id=22207 preview=Question anchor: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Case scope id: multi-document-040. Scoped answ...
  2. score=46.104125 chunk_id=22208 preview=Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Case scope id: multi-document-040. Combined evidence:...
  3. score=26.129512 chunk_id=21821 preview=document multi-birch-ferry-shed-memory-log-040::multi-document-040::1: In document multi-birch-ferry-shed-memory-log-040, the verified archive note records p...
  4. score=26.064899 chunk_id=21893 preview=document multi-mira-audio-transcript-040::multi-document-040::2: In document multi-mira-audio-transcript-040, the verified archive note records juniper bundl...
  5. score=4.134015 chunk_id=21822 preview=document multi-birch-ferry-shed-memory-log-100::multi-document-100::1: In document multi-birch-ferry-shed-memory-log-100, the verified archive note records l...
- Matched markers: juniper bundles, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 41 - multi-document-041
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard?

Expected evidence:
- Bellwater Fair
- lantern hook
- carved shell comb

Expected distractors:
- tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.701301 chunk_id=22209 preview=Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Case scope id: multi-document-...
  2. score=58.593041 chunk_id=22210 preview=Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Case scope id: multi-document-041. Co...
  3. score=30.527350 chunk_id=21811 preview=document multi-bellwater-fair-family-register-041::multi-document-041::3: In document multi-bellwater-fair-family-register-041, the verified archive note rec...
  4. score=26.746098 chunk_id=21938 preview=document multi-pine-gate-yard-travel-note-041::multi-document-041::1: In document multi-pine-gate-yard-travel-note-041, the verified archive note records Bel...
  5. score=14.075650 chunk_id=21995 preview=document multi-watchtower-landing-ledger-061::multi-document-061::1: In document multi-watchtower-landing-ledger-061, the verified archive note records Bellw...
- Matched markers: Bellwater Fair, carved shell comb, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bellwater Fair, carved shell comb, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.506239 chunk_id=22209 preview=Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Case scope id: multi-document-...
  2. score=58.493624 chunk_id=22210 preview=Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Case scope id: multi-document-041. Co...
  3. score=30.399043 chunk_id=21811 preview=document multi-bellwater-fair-family-register-041::multi-document-041::3: In document multi-bellwater-fair-family-register-041, the verified archive note rec...
  4. score=26.501963 chunk_id=21938 preview=document multi-pine-gate-yard-travel-note-041::multi-document-041::1: In document multi-pine-gate-yard-travel-note-041, the verified archive note records Bel...
  5. score=1.970008 chunk_id=22170 preview=Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-documen...
- Matched markers: Bellwater Fair, carved shell comb, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bellwater Fair, carved shell comb, lantern hook.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 42 - multi-document-042
Question: Which archive pieces from more than one document explain the family profile event at North Bell workshop?

Expected evidence:
- clay watering cup
- canal route map

Expected distractors:
- willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: clay watering cup, canal route map
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.534281 chunk_id=22211 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at North Bell workshop? Case scope id: multi-document-042....
  2. score=46.398652 chunk_id=22212 preview=Question: Which archive pieces from more than one document explain the family profile event at North Bell workshop? Case scope id: multi-document-042. Combin...
  3. score=26.517613 chunk_id=21929 preview=document multi-north-bell-workshop-photo-index-042::multi-document-042::1: In document multi-north-bell-workshop-photo-index-042, the verified archive note r...
  4. score=26.446088 chunk_id=21925 preview=document multi-nadia-repair-book-042::multi-document-042::2: In document multi-nadia-repair-book-042, the verified archive note records canal route map. Case...
  5. score=2.110537 chunk_id=21808 preview=document multi-bell-bridge-square-photo-index-030::multi-document-030::1: In document multi-bell-bridge-square-photo-index-030, the verified archive note rec...
- Matched markers: canal route map, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map, clay watering cup.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 43 - multi-document-043
Question: Which documents must be combined to understand Anya's holiday card note about Fog Island pier?

Expected evidence:
- saffron scarf
- coal stove hiss
- copper token

Expected distractors:
- star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.423541 chunk_id=22213 preview=Question anchor: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Case scope id: multi-document-043. Scoped ans...
  2. score=58.221076 chunk_id=22214 preview=Question: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Case scope id: multi-document-043. Combined evidence...
  3. score=26.379066 chunk_id=21838 preview=document multi-fog-island-pier-audio-transcript-043::multi-document-043::1: In document multi-fog-island-pier-audio-transcript-043, the verified archive note...
  4. score=26.259315 chunk_id=21800 preview=document multi-anya-inventory-sheet-043::multi-document-043::2: In document multi-anya-inventory-sheet-043, the verified archive note records coal stove hiss...
  5. score=26.216844 chunk_id=21909 preview=document multi-moon-orchard-rest-ledger-043::multi-document-043::3: In document multi-moon-orchard-rest-ledger-043, the verified archive note records copper...
- Matched markers: coal stove hiss, copper token, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.213661 chunk_id=22213 preview=Question anchor: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Case scope id: multi-document-043. Scoped ans...
  2. score=58.157506 chunk_id=22214 preview=Question: Which documents must be combined to understand Anya's holiday card note about Fog Island pier? Case scope id: multi-document-043. Combined evidence...
  3. score=26.259047 chunk_id=21838 preview=document multi-fog-island-pier-audio-transcript-043::multi-document-043::1: In document multi-fog-island-pier-audio-transcript-043, the verified archive note...
  4. score=26.090736 chunk_id=21800 preview=document multi-anya-inventory-sheet-043::multi-document-043::2: In document multi-anya-inventory-sheet-043, the verified archive note records coal stove hiss...
  5. score=26.066880 chunk_id=21909 preview=document multi-moon-orchard-rest-ledger-043::multi-document-043::3: In document multi-moon-orchard-rest-ledger-043, the verified archive note records copper...
- Matched markers: coal stove hiss, copper token, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 44 - multi-document-044
Question: Which records together show how Yara prepared the canal barge stop near Moon Mill yard?

Expected evidence:
- blue glass jar
- tin key

Expected distractors:
- silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.354362 chunk_id=22215 preview=Question anchor: Which records together show how Yara prepared the canal barge stop near Moon Mill yard? Case scope id: multi-document-044. Scoped answer sum...
  2. score=26.345595 chunk_id=22005 preview=document multi-yara-family-register-044::multi-document-044::2: In document multi-yara-family-register-044, the verified archive note records tin key. Case r...
  3. score=26.261880 chunk_id=21903 preview=document multi-moon-mill-yard-letter-roll-044::multi-document-044::1: In document multi-moon-mill-yard-letter-roll-044, the verified archive note records blu...
  4. score=1.892105 chunk_id=22009 preview=document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case...
  5. score=1.760391 chunk_id=21825 preview=document multi-blue-trunk-cabin-memory-log-064::multi-document-064::1: In document multi-blue-trunk-cabin-memory-log-064, the verified archive note records a...
- Matched markers: blue glass jar, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.269681 chunk_id=22215 preview=Question anchor: Which records together show how Yara prepared the canal barge stop near Moon Mill yard? Case scope id: multi-document-044. Scoped answer sum...
  2. score=46.217507 chunk_id=22216 preview=Question: Which records together show how Yara prepared the canal barge stop near Moon Mill yard? Case scope id: multi-document-044. Combined evidence: blue...
  3. score=26.269836 chunk_id=21903 preview=document multi-moon-mill-yard-letter-roll-044::multi-document-044::1: In document multi-moon-mill-yard-letter-roll-044, the verified archive note records blu...
  4. score=26.154671 chunk_id=22005 preview=document multi-yara-family-register-044::multi-document-044::2: In document multi-yara-family-register-044, the verified archive note records tin key. Case r...
  5. score=1.671182 chunk_id=22008 preview=document multi-yara-profile-page-024::multi-document-024::2: In document multi-yara-profile-page-024, the verified archive note records juniper bundles. Case...
- Matched markers: blue glass jar, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, tin key.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 2).

### Question 45 - multi-document-045
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove?

Expected evidence:
- Lantern Tide
- copper wind vane pin
- brass compass

Expected distractors:
- birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.365509 chunk_id=22217 preview=Question anchor: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove? Case scope id: multi-document-045...
  2. score=30.290881 chunk_id=21786 preview=document multi-ada-archive-045::multi-document-045::2: In document multi-ada-archive-045, the verified archive note records copper wind vane pin. Case record...
  3. score=26.396285 chunk_id=21834 preview=document multi-driftwood-cove-repair-book-045::multi-document-045::1: In document multi-driftwood-cove-repair-book-045, the verified archive note records Lan...
  4. score=6.019615 chunk_id=21790 preview=document multi-ada-memory-log-085::multi-document-085::2: In document multi-ada-memory-log-085, the verified archive note records green apron. Case record id...
  5. score=5.984544 chunk_id=21789 preview=document multi-ada-memory-log-025::multi-document-025::2: In document multi-ada-memory-log-025, the verified archive note records lantern hook. Case record i...
- Matched markers: Lantern Tide, brass compass, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Tide, brass compass, copper wind vane pin.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.289103 chunk_id=22217 preview=Question anchor: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove? Case scope id: multi-document-045...
  2. score=58.226065 chunk_id=22218 preview=Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Driftwood cove? Case scope id: multi-document-045. Combi...
  3. score=30.192285 chunk_id=21786 preview=document multi-ada-archive-045::multi-document-045::2: In document multi-ada-archive-045, the verified archive note records copper wind vane pin. Case record...
  4. score=26.303018 chunk_id=21834 preview=document multi-driftwood-cove-repair-book-045::multi-document-045::1: In document multi-driftwood-cove-repair-book-045, the verified archive note records Lan...
  5. score=5.887941 chunk_id=21790 preview=document multi-ada-memory-log-085::multi-document-085::2: In document multi-ada-memory-log-085, the verified archive note records green apron. Case record id...
- Matched markers: Lantern Tide, brass compass, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Tide, brass compass, copper wind vane pin.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 46 - multi-document-046
Question: Which archive pieces from more than one document explain the family profile event at Ridge Post loft?

Expected evidence:
- wax thread
- basalt sketch

Expected distractors:
- oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.615800 chunk_id=22219 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Ridge Post loft? Case scope id: multi-document-046. Sco...
  2. score=46.453953 chunk_id=22220 preview=Question: Which archive pieces from more than one document explain the family profile event at Ridge Post loft? Case scope id: multi-document-046. Combined e...
  3. score=26.587455 chunk_id=21939 preview=document multi-ridge-post-loft-inventory-sheet-046::multi-document-046::1: In document multi-ridge-post-loft-inventory-sheet-046, the verified archive note r...
  4. score=26.348862 chunk_id=21971 preview=document multi-sonya-ledger-046::multi-document-046::2: In document multi-sonya-ledger-046, the verified archive note records basalt sketch. Case record id:...
  5. score=3.855142 chunk_id=22315 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Sc...
- Matched markers: basalt sketch, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.541039 chunk_id=22219 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Ridge Post loft? Case scope id: multi-document-046. Sco...
  2. score=46.471124 chunk_id=22220 preview=Question: Which archive pieces from more than one document explain the family profile event at Ridge Post loft? Case scope id: multi-document-046. Combined e...
  3. score=26.542844 chunk_id=21939 preview=document multi-ridge-post-loft-inventory-sheet-046::multi-document-046::1: In document multi-ridge-post-loft-inventory-sheet-046, the verified archive note r...
  4. score=26.380857 chunk_id=21971 preview=document multi-sonya-ledger-046::multi-document-046::2: In document multi-sonya-ledger-046, the verified archive note records basalt sketch. Case record id:...
- Matched markers: basalt sketch, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 47 - multi-document-047
Question: Which documents must be combined to understand Runa's boat manifest note about East Signal room?

Expected evidence:
- smoke vent chain
- copper token
- silver booth token

Expected distractors:
- glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.456120 chunk_id=22221 preview=Question anchor: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Case scope id: multi-document-047. Scoped a...
  2. score=58.273016 chunk_id=22222 preview=Question: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Case scope id: multi-document-047. Combined eviden...
  3. score=26.365916 chunk_id=21952 preview=document multi-runa-minute-book-047::multi-document-047::2: In document multi-runa-minute-book-047, the verified archive note records copper token. Case reco...
  4. score=26.335303 chunk_id=21835 preview=document multi-east-signal-room-family-register-047::multi-document-047::1: In document multi-east-signal-room-family-register-047, the verified archive note...
  5. score=26.329813 chunk_id=21861 preview=document multi-harvest-glow-travel-note-047::multi-document-047::3: In document multi-harvest-glow-travel-note-047, the verified archive note records silver...
- Matched markers: copper token, silver booth token, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.305649 chunk_id=22221 preview=Question anchor: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Case scope id: multi-document-047. Scoped a...
  2. score=58.232801 chunk_id=22222 preview=Question: Which documents must be combined to understand Runa's boat manifest note about East Signal room? Case scope id: multi-document-047. Combined eviden...
  3. score=26.321450 chunk_id=21835 preview=document multi-east-signal-room-family-register-047::multi-document-047::1: In document multi-east-signal-room-family-register-047, the verified archive note...
  4. score=26.220664 chunk_id=21861 preview=document multi-harvest-glow-travel-note-047::multi-document-047::3: In document multi-harvest-glow-travel-note-047, the verified archive note records silver...
  5. score=26.133986 chunk_id=21952 preview=document multi-runa-minute-book-047::multi-document-047::2: In document multi-runa-minute-book-047, the verified archive note records copper token. Case reco...
- Matched markers: copper token, silver booth token, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 48 - multi-document-048
Question: Which records together show how Iveta prepared the winter coach stop near South Meadow arch?

Expected evidence:
- amber lantern
- tuning fork

Expected distractors:
- weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.517765 chunk_id=22223 preview=Question anchor: Which records together show how Iveta prepared the winter coach stop near South Meadow arch? Case scope id: multi-document-048. Scoped answe...
  2. score=26.677058 chunk_id=21978 preview=document multi-south-meadow-arch-archive-048::multi-document-048::1: In document multi-south-meadow-arch-archive-048, the verified archive note records amber...
  3. score=26.333745 chunk_id=21870 preview=document multi-iveta-profile-page-048::multi-document-048::2: In document multi-iveta-profile-page-048, the verified archive note records tuning fork. Case r...
  4. score=1.895545 chunk_id=21868 preview=document multi-iveta-family-register-068::multi-document-068::2: In document multi-iveta-family-register-068, the verified archive note records birch tea fla...
  5. score=1.162926 chunk_id=21980 preview=document multi-south-meadow-arch-photo-index-078::multi-document-078::1: In document multi-south-meadow-arch-photo-index-078, the verified archive note recor...
- Matched markers: amber lantern, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.317661 chunk_id=22223 preview=Question anchor: Which records together show how Iveta prepared the winter coach stop near South Meadow arch? Case scope id: multi-document-048. Scoped answe...
  2. score=46.239481 chunk_id=22224 preview=Question: Which records together show how Iveta prepared the winter coach stop near South Meadow arch? Case scope id: multi-document-048. Combined evidence:...
  3. score=26.332940 chunk_id=21978 preview=document multi-south-meadow-arch-archive-048::multi-document-048::1: In document multi-south-meadow-arch-archive-048, the verified archive note records amber...
  4. score=26.172180 chunk_id=21870 preview=document multi-iveta-profile-page-048::multi-document-048::2: In document multi-iveta-profile-page-048, the verified archive note records tuning fork. Case r...
  5. score=1.638301 chunk_id=21866 preview=document multi-iveta-audio-transcript-088::multi-document-088::2: In document multi-iveta-audio-transcript-088, the verified archive note records juniper bun...
- Matched markers: amber lantern, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 2).

### Question 49 - multi-document-049
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic?

Expected evidence:
- Signal Lantern Morning
- cedar shovel
- willow basket

Expected distractors:
- juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.560993 chunk_id=22225 preview=Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic? Case scope id: mult...
  2. score=58.559017 chunk_id=22226 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic? Case scope id: multi-docum...
  3. score=30.469776 chunk_id=21955 preview=document multi-signal-lantern-morning-audio-transcript-049::multi-document-049::3: In document multi-signal-lantern-morning-audio-transcript-049, the verifie...
  4. score=26.582085 chunk_id=21889 preview=document multi-maple-court-attic-ledger-049::multi-document-049::1: In document multi-maple-court-attic-ledger-049, the verified archive note records Signal...
  5. score=2.192720 chunk_id=22266 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-docum...
- Matched markers: Signal Lantern Morning, cedar shovel, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, cedar shovel, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.569429 chunk_id=22225 preview=Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic? Case scope id: mult...
  2. score=58.535915 chunk_id=22226 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Maple Court attic? Case scope id: multi-docum...
  3. score=30.442867 chunk_id=22019 preview=document multi-zora-memory-log-049::multi-document-049::2: In document multi-zora-memory-log-049, the verified archive note records cedar shovel. Case record...
  4. score=26.582752 chunk_id=21889 preview=document multi-maple-court-attic-ledger-049::multi-document-049::1: In document multi-maple-court-attic-ledger-049, the verified archive note records Signal...
  5. score=2.115148 chunk_id=22306 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-docume...
- Matched markers: Signal Lantern Morning, cedar shovel, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, cedar shovel, willow basket.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 50 - multi-document-050
Question: Which archive pieces from more than one document explain the family profile event at Star Basin gallery?

Expected evidence:
- violet ribbon
- star ledger page

Expected distractors:
- carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.499086 chunk_id=22227 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Star Basin gallery? Case scope id: multi-document-050....
  2. score=46.477046 chunk_id=22228 preview=Question: Which archive pieces from more than one document explain the family profile event at Star Basin gallery? Case scope id: multi-document-050. Combine...
  3. score=26.466398 chunk_id=21983 preview=document multi-star-basin-gallery-minute-book-050::multi-document-050::1: In document multi-star-basin-gallery-minute-book-050, the verified archive note rec...
  4. score=14.107330 chunk_id=22196 preview=Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-034. Combined...
  5. score=14.102911 chunk_id=22260 preview=Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-066. Combin...
- Matched markers: star ledger page, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: star ledger page, violet ribbon.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.478491 chunk_id=22227 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Star Basin gallery? Case scope id: multi-document-050....
  2. score=46.431234 chunk_id=22228 preview=Question: Which archive pieces from more than one document explain the family profile event at Star Basin gallery? Case scope id: multi-document-050. Combine...
  3. score=26.498703 chunk_id=21983 preview=document multi-star-basin-gallery-minute-book-050::multi-document-050::1: In document multi-star-basin-gallery-minute-book-050, the verified archive note rec...
- Matched markers: star ledger page, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: star ledger page, violet ribbon.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 51 - multi-document-051
Question: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse?

Expected evidence:
- blue oar
- silver booth token
- weathered camera strap

Expected distractors:
- canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.313265 chunk_id=22229 preview=Question anchor: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse? Case scope id: multi-document-051. S...
  2. score=58.292366 chunk_id=22230 preview=Question: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse? Case scope id: multi-document-051. Combined...
  3. score=26.350000 chunk_id=21965 preview=document multi-snow-orchard-storehouse-profile-page-051::multi-document-051::1: In document multi-snow-orchard-storehouse-profile-page-051, the verified arch...
  4. score=9.714496 chunk_id=21959 preview=document multi-signal-lantern-morning-ledger-079::multi-document-079::3: In document multi-signal-lantern-morning-ledger-079, the verified archive note recor...
  5. score=9.610997 chunk_id=21812 preview=document multi-bellwater-fair-ledger-031::multi-document-031::3: In document multi-bellwater-fair-ledger-031, the verified archive note records silver booth...
- Matched markers: blue oar, silver booth token, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.198042 chunk_id=22229 preview=Question anchor: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse? Case scope id: multi-document-051. S...
  2. score=58.175447 chunk_id=22230 preview=Question: Which documents must be combined to understand Vera's travel ledger note about Snow Orchard storehouse? Case scope id: multi-document-051. Combined...
  3. score=26.204348 chunk_id=21965 preview=document multi-snow-orchard-storehouse-profile-page-051::multi-document-051::1: In document multi-snow-orchard-storehouse-profile-page-051, the verified arch...
  4. score=26.117653 chunk_id=21992 preview=document multi-vera-photo-index-051::multi-document-051::2: In document multi-vera-photo-index-051, the verified archive note records silver booth token. Cas...
  5. score=26.075739 chunk_id=21816 preview=document multi-bellwater-fair-repair-book-051::multi-document-051::3: In document multi-bellwater-fair-repair-book-051, the verified archive note records wea...
- Matched markers: blue oar, silver booth token, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 52 - multi-document-052
Question: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station?

Expected evidence:
- linen wick
- birch tea flask

Expected distractors:
- coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.339784 chunk_id=22231 preview=Question anchor: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Case scope id: multi-document-052. Scoped answe...
  2. score=26.294975 chunk_id=21828 preview=document multi-cedar-hill-station-memory-log-052::multi-document-052::1: In document multi-cedar-hill-station-memory-log-052, the verified archive note recor...
  3. score=26.290098 chunk_id=21918 preview=document multi-nadia-audio-transcript-052::multi-document-052::2: In document multi-nadia-audio-transcript-052, the verified archive note records birch tea f...
  4. score=3.273383 chunk_id=22295 preview=Question anchor: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-084. Scoped answer...
  5. score=1.812910 chunk_id=21920 preview=document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-family-register-092, the verified archive note records tin key. Case...
- Matched markers: birch tea flask, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.196745 chunk_id=22231 preview=Question anchor: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Case scope id: multi-document-052. Scoped answe...
  2. score=46.162030 chunk_id=22232 preview=Question: Which records together show how Nadia prepared the river skiff stop near Cedar Hill station? Case scope id: multi-document-052. Combined evidence:...
  3. score=26.167065 chunk_id=21828 preview=document multi-cedar-hill-station-memory-log-052::multi-document-052::1: In document multi-cedar-hill-station-memory-log-052, the verified archive note recor...
  4. score=26.131832 chunk_id=21918 preview=document multi-nadia-audio-transcript-052::multi-document-052::2: In document multi-nadia-audio-transcript-052, the verified archive note records birch tea f...
- Matched markers: birch tea flask, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 53 - multi-document-053
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path?

Expected evidence:
- Moon Orchard Rest
- green apron
- oak barrel hoops

Expected distractors:
- tin key

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.794285 chunk_id=22233 preview=Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Case scope id: multi-docum...
  2. score=58.612763 chunk_id=22234 preview=Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Case scope id: multi-document-053...
  3. score=30.755929 chunk_id=21908 preview=document multi-moon-orchard-rest-family-register-053::multi-document-053::3: In document multi-moon-orchard-rest-family-register-053, the verified archive no...
  4. score=30.546192 chunk_id=21801 preview=document multi-anya-letter-roll-053::multi-document-053::2: In document multi-anya-letter-roll-053, the verified archive note records green apron. Case recor...
  5. score=26.841191 chunk_id=21935 preview=document multi-old-quarry-path-travel-note-053::multi-document-053::1: In document multi-old-quarry-path-travel-note-053, the verified archive note records M...
- Matched markers: Moon Orchard Rest, green apron, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Orchard Rest, green apron, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.613334 chunk_id=22233 preview=Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Case scope id: multi-docum...
  2. score=58.619585 chunk_id=22234 preview=Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Old Quarry path? Case scope id: multi-document-053...
  3. score=26.626341 chunk_id=21935 preview=document multi-old-quarry-path-travel-note-053::multi-document-053::1: In document multi-old-quarry-path-travel-note-053, the verified archive note records M...
  4. score=2.233840 chunk_id=22274 preview=Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-document-073...
  5. score=2.211855 chunk_id=22194 preview=Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-document-0...
- Matched markers: Moon Orchard Rest, green apron, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Orchard Rest, green apron, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 54 - multi-document-054
Question: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office?

Expected evidence:
- moonflower cutting
- glass ink bottle

Expected distractors:
- brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.510886 chunk_id=22235 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office? Case scope id: multi-document-054....
  2. score=46.447096 chunk_id=22236 preview=Question: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office? Case scope id: multi-document-054. Combine...
  3. score=26.537378 chunk_id=21831 preview=document multi-cloud-wharf-office-photo-index-054::multi-document-054::1: In document multi-cloud-wharf-office-photo-index-054, the verified archive note rec...
  4. score=1.378091 chunk_id=21829 preview=document multi-cloud-wharf-office-archive-024::multi-document-024::1: In document multi-cloud-wharf-office-archive-024, the verified archive note records pap...
  5. score=1.334429 chunk_id=21830 preview=document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records lin...
- Matched markers: glass ink bottle, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.477112 chunk_id=22235 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office? Case scope id: multi-document-054....
  2. score=46.463435 chunk_id=22236 preview=Question: Which archive pieces from more than one document explain the family profile event at Cloud Wharf office? Case scope id: multi-document-054. Combine...
  3. score=26.433675 chunk_id=21831 preview=document multi-cloud-wharf-office-photo-index-054::multi-document-054::1: In document multi-cloud-wharf-office-photo-index-054, the verified archive note rec...
  4. score=13.931632 chunk_id=22140 preview=Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006. Combin...
  5. score=13.927863 chunk_id=22300 preview=Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Combine...
- Matched markers: glass ink bottle, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 2).

### Question 55 - multi-document-055
Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor?

Expected evidence:
- rope bridge permit
- weathered camera strap
- coal stove hiss

Expected distractors:
- basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.401406 chunk_id=22237 preview=Question anchor: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Case scope id: multi-document-055....
  2. score=58.278947 chunk_id=22238 preview=Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Case scope id: multi-document-055. Combine...
  3. score=26.321749 chunk_id=21787 preview=document multi-ada-inventory-sheet-055::multi-document-055::2: In document multi-ada-inventory-sheet-055, the verified archive note records weathered camera...
  4. score=26.297468 chunk_id=21849 preview=document multi-harbor-glass-corridor-audio-transcript-055::multi-document-055::1: In document multi-harbor-glass-corridor-audio-transcript-055, the verified...
  5. score=1.644089 chunk_id=21791 preview=document multi-ada-minute-book-035::multi-document-035::2: In document multi-ada-minute-book-035, the verified archive note records silver booth token. Case...
- Matched markers: coal stove hiss, rope bridge permit, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.266928 chunk_id=22237 preview=Question anchor: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Case scope id: multi-document-055....
  2. score=58.158924 chunk_id=22238 preview=Question: Which documents must be combined to understand Ada's memory sketchbook note about Harbor Glass corridor? Case scope id: multi-document-055. Combine...
  3. score=26.284405 chunk_id=21849 preview=document multi-harbor-glass-corridor-audio-transcript-055::multi-document-055::1: In document multi-harbor-glass-corridor-audio-transcript-055, the verified...
  4. score=26.137148 chunk_id=21881 preview=document multi-lantern-tide-ledger-055::multi-document-055::3: In document multi-lantern-tide-ledger-055, the verified archive note records coal stove hiss....
  5. score=26.136571 chunk_id=21787 preview=document multi-ada-inventory-sheet-055::multi-document-055::2: In document multi-ada-inventory-sheet-055, the verified archive note records weathered camera...
- Matched markers: coal stove hiss, rope bridge permit, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 56 - multi-document-056
Question: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane?

Expected evidence:
- paper moon mask
- juniper bundles

Expected distractors:
- copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.243079 chunk_id=22239 preview=Question anchor: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane? Case scope id: multi-document-056. Scoped answe...
  2. score=46.157295 chunk_id=22240 preview=Question: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane? Case scope id: multi-document-056. Combined evidence:...
  3. score=26.242326 chunk_id=21970 preview=document multi-sonya-family-register-056::multi-document-056::2: In document multi-sonya-family-register-056, the verified archive note records juniper bundl...
  4. score=26.163803 chunk_id=21930 preview=document multi-north-orchard-lane-letter-roll-056::multi-document-056::1: In document multi-north-orchard-lane-letter-roll-056, the verified archive note rec...
  5. score=1.715148 chunk_id=21969 preview=document multi-sonya-audio-transcript-076::multi-document-076::2: In document multi-sonya-audio-transcript-076, the verified archive note records tin key. Ca...
- Matched markers: juniper bundles, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.229625 chunk_id=22239 preview=Question anchor: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane? Case scope id: multi-document-056. Scoped answe...
  2. score=46.186790 chunk_id=22240 preview=Question: Which records together show how Sonya prepared the quarry lift stop near North Orchard lane? Case scope id: multi-document-056. Combined evidence:...
  3. score=26.224235 chunk_id=21930 preview=document multi-north-orchard-lane-letter-roll-056::multi-document-056::1: In document multi-north-orchard-lane-letter-roll-056, the verified archive note rec...
  4. score=26.127049 chunk_id=21970 preview=document multi-sonya-family-register-056::multi-document-056::2: In document multi-sonya-family-register-056, the verified archive note records juniper bundl...
  5. score=0.935740 chunk_id=21932 preview=document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note rec...
- Matched markers: juniper bundles, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 57 - multi-document-057
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade?

Expected evidence:
- Harvest Glow
- lantern hook
- carved shell comb

Expected distractors:
- tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.706894 chunk_id=22241 preview=Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Case scope id: multi-docum...
  2. score=58.515752 chunk_id=22242 preview=Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Case scope id: multi-document-057...
  3. score=30.695601 chunk_id=21945 preview=document multi-runa-archive-057::multi-document-057::2: In document multi-runa-archive-057, the verified archive note records lantern hook. Case record id: m...
  4. score=26.719897 chunk_id=21864 preview=document multi-hollow-market-arcade-repair-book-057::multi-document-057::1: In document multi-hollow-market-arcade-repair-book-057, the verified archive note...
  5. score=14.238482 chunk_id=21843 preview=document multi-fox-hollow-bridge-ledger-037::multi-document-037::1: In document multi-fox-hollow-bridge-ledger-037, the verified archive note records Harvest...
- Matched markers: Harvest Glow, carved shell comb, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Harvest Glow, carved shell comb, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.456640 chunk_id=22241 preview=Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Case scope id: multi-docum...
  2. score=58.481912 chunk_id=22242 preview=Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Hollow Market arcade? Case scope id: multi-document-057...
  3. score=26.439817 chunk_id=21864 preview=document multi-hollow-market-arcade-repair-book-057::multi-document-057::1: In document multi-hollow-market-arcade-repair-book-057, the verified archive note...
  4. score=2.166310 chunk_id=22322 preview=Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-097. C...
  5. score=2.163351 chunk_id=22202 preview=Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-037. C...
- Matched markers: Harvest Glow, carved shell comb, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Harvest Glow, carved shell comb, lantern hook.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 58 - multi-document-058
Question: Which archive pieces from more than one document explain the family profile event at Marble stair hall?

Expected evidence:
- clay watering cup
- canal route map

Expected distractors:
- willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=1.002492 chunk_id=21833 preview=document multi-driftwood-cove-profile-page-075::multi-document-075::1: In document multi-driftwood-cove-profile-page-075, the verified archive note records s...
  2. score=0.719627 chunk_id=21794 preview=document multi-ada-photo-index-075::multi-document-075::2: In document multi-ada-photo-index-075, the verified archive note records coal stove hiss. Case rec...
- Matched markers: none
- Missing markers: clay watering cup, canal route map
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.421839 chunk_id=22243 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Marble stair hall? Case scope id: multi-document-058. S...
- Matched markers: canal route map, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: canal route map, clay watering cup.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 59 - multi-document-059
Question: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock?

Expected evidence:
- saffron scarf
- coal stove hiss
- copper token

Expected distractors:
- star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.541608 chunk_id=22245 preview=Question anchor: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Case scope id: multi-document-059. Scope...
  2. score=58.367029 chunk_id=22246 preview=Question: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Case scope id: multi-document-059. Combined evi...
  3. score=26.593726 chunk_id=21795 preview=document multi-amber-canal-lock-family-register-059::multi-document-059::1: In document multi-amber-canal-lock-family-register-059, the verified archive note...
  4. score=26.366667 chunk_id=21964 preview=document multi-signal-lantern-morning-travel-note-059::multi-document-059::3: In document multi-signal-lantern-morning-travel-note-059, the verified archive...
  5. score=1.388678 chunk_id=21797 preview=document multi-amber-canal-lock-travel-note-089::multi-document-089::1: In document multi-amber-canal-lock-travel-note-089, the verified archive note records...
- Matched markers: coal stove hiss, copper token, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.422729 chunk_id=22245 preview=Question anchor: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Case scope id: multi-document-059. Scope...
  2. score=58.378640 chunk_id=22246 preview=Question: Which documents must be combined to understand Zora's photo album page note about Amber Canal lock? Case scope id: multi-document-059. Combined evi...
  3. score=26.353137 chunk_id=22020 preview=document multi-zora-minute-book-059::multi-document-059::2: In document multi-zora-minute-book-059, the verified archive note records coal stove hiss. Case r...
  4. score=26.351092 chunk_id=21795 preview=document multi-amber-canal-lock-family-register-059::multi-document-059::1: In document multi-amber-canal-lock-family-register-059, the verified archive note...
  5. score=26.285664 chunk_id=21964 preview=document multi-signal-lantern-morning-travel-note-059::multi-document-059::3: In document multi-signal-lantern-morning-travel-note-059, the verified archive...
- Matched markers: coal stove hiss, copper token, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 60 - multi-document-060
Question: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square?

Expected evidence:
- blue glass jar
- tin key

Expected distractors:
- silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.348656 chunk_id=22247 preview=Question anchor: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Case scope id: multi-document-060. Scoped an...
  2. score=46.172678 chunk_id=22248 preview=Question: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Case scope id: multi-document-060. Combined evidenc...
  3. score=26.352052 chunk_id=21807 preview=document multi-bell-bridge-square-archive-060::multi-document-060::1: In document multi-bell-bridge-square-archive-060, the verified archive note records blu...
  4. score=26.258079 chunk_id=21899 preview=document multi-mira-profile-page-060::multi-document-060::2: In document multi-mira-profile-page-060, the verified archive note records tin key. Case record...
  5. score=1.784122 chunk_id=21895 preview=document multi-mira-family-register-020::multi-document-020::2: In document multi-mira-family-register-020, the verified archive note records birch tea flask...
- Matched markers: blue glass jar, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.292814 chunk_id=22247 preview=Question anchor: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Case scope id: multi-document-060. Scoped an...
  2. score=46.239481 chunk_id=22248 preview=Question: Which records together show how Mira prepared the overnight ferry stop near Bell Bridge square? Case scope id: multi-document-060. Combined evidenc...
  3. score=26.280693 chunk_id=21807 preview=document multi-bell-bridge-square-archive-060::multi-document-060::1: In document multi-bell-bridge-square-archive-060, the verified archive note records blu...
  4. score=26.186444 chunk_id=21899 preview=document multi-mira-profile-page-060::multi-document-060::2: In document multi-mira-profile-page-060, the verified archive note records tin key. Case record...
  5. score=1.702307 chunk_id=21893 preview=document multi-mira-audio-transcript-040::multi-document-040::2: In document multi-mira-audio-transcript-040, the verified archive note records juniper bundl...
- Matched markers: blue glass jar, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, tin key.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 61 - multi-document-061
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing?

Expected evidence:
- Bellwater Fair
- copper wind vane pin
- brass compass

Expected distractors:
- birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.484950 chunk_id=22249 preview=Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing? Case scope id: multi-docum...
  2. score=58.355136 chunk_id=22250 preview=Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing? Case scope id: multi-document-061...
  3. score=30.344331 chunk_id=21810 preview=document multi-bellwater-fair-audio-transcript-061::multi-document-061::3: In document multi-bellwater-fair-audio-transcript-061, the verified archive note r...
  4. score=26.552773 chunk_id=21995 preview=document multi-watchtower-landing-ledger-061::multi-document-061::1: In document multi-watchtower-landing-ledger-061, the verified archive note records Bellw...
  5. score=14.108781 chunk_id=21938 preview=document multi-pine-gate-yard-travel-note-041::multi-document-041::1: In document multi-pine-gate-yard-travel-note-041, the verified archive note records Bel...
- Matched markers: Bellwater Fair, brass compass, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bellwater Fair, brass compass, copper wind vane pin.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.297030 chunk_id=22249 preview=Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing? Case scope id: multi-docum...
  2. score=58.287886 chunk_id=22250 preview=Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Watchtower landing? Case scope id: multi-document-061...
  3. score=26.277361 chunk_id=21995 preview=document multi-watchtower-landing-ledger-061::multi-document-061::1: In document multi-watchtower-landing-ledger-061, the verified archive note records Bellw...
  4. score=5.919143 chunk_id=21984 preview=document multi-vera-archive-021::multi-document-021::2: In document multi-vera-archive-021, the verified archive note records green apron. Case record id: mu...
  5. score=2.000080 chunk_id=22210 preview=Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Pine Gate yard? Case scope id: multi-document-041. Co...
- Matched markers: Bellwater Fair, brass compass, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bellwater Fair, brass compass, copper wind vane pin.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 62 - multi-document-062
Question: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk?

Expected evidence:
- wax thread
- basalt sketch

Expected distractors:
- oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.406435 chunk_id=22251 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Case scope id: multi-document-062. S...
  2. score=46.403557 chunk_id=22252 preview=Question: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Case scope id: multi-document-062. Combined...
  3. score=26.365900 chunk_id=21877 preview=document multi-lantern-row-kiosk-minute-book-062::multi-document-062::1: In document multi-lantern-row-kiosk-minute-book-062, the verified archive note recor...
  4. score=13.889249 chunk_id=22316 preview=Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Combined...
  5. score=13.883482 chunk_id=22188 preview=Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-030. Combine...
- Matched markers: basalt sketch, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.475492 chunk_id=22251 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Case scope id: multi-document-062. S...
  2. score=46.442515 chunk_id=22252 preview=Question: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Case scope id: multi-document-062. Combined...
  3. score=26.453268 chunk_id=21877 preview=document multi-lantern-row-kiosk-minute-book-062::multi-document-062::1: In document multi-lantern-row-kiosk-minute-book-062, the verified archive note recor...
- Matched markers: basalt sketch, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 63 - multi-document-063
Question: Which documents must be combined to understand Anya's family note note about Moss Archive room?

Expected evidence:
- smoke vent chain
- copper token
- silver booth token

Expected distractors:
- glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.229695 chunk_id=22253 preview=Question anchor: Which documents must be combined to understand Anya's family note note about Moss Archive room? Case scope id: multi-document-063. Scoped an...
  2. score=58.150000 chunk_id=22254 preview=Question: Which documents must be combined to understand Anya's family note note about Moss Archive room? Case scope id: multi-document-063. Combined evidenc...
  3. score=26.250000 chunk_id=21806 preview=document multi-anya-photo-index-063::multi-document-063::2: In document multi-anya-photo-index-063, the verified archive note records copper token. Case reco...
  4. score=9.907107 chunk_id=21805 preview=document multi-anya-minute-book-083::multi-document-083::2: In document multi-anya-minute-book-083, the verified archive note records silver booth token. Cas...
  5. score=1.680384 chunk_id=21804 preview=document multi-anya-minute-book-023::multi-document-023::2: In document multi-anya-minute-book-023, the verified archive note records weathered camera strap....
- Matched markers: copper token, silver booth token, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.081956 chunk_id=22253 preview=Question anchor: Which documents must be combined to understand Anya's family note note about Moss Archive room? Case scope id: multi-document-063. Scoped an...
  2. score=58.025447 chunk_id=22254 preview=Question: Which documents must be combined to understand Anya's family note note about Moss Archive room? Case scope id: multi-document-063. Combined evidenc...
  3. score=26.086075 chunk_id=21915 preview=document multi-moss-archive-room-profile-page-063::multi-document-063::1: In document multi-moss-archive-room-profile-page-063, the verified archive note rec...
  4. score=26.006417 chunk_id=21806 preview=document multi-anya-photo-index-063::multi-document-063::2: In document multi-anya-photo-index-063, the verified archive note records copper token. Case reco...
  5. score=25.907513 chunk_id=21912 preview=document multi-moon-orchard-rest-repair-book-063::multi-document-063::3: In document multi-moon-orchard-rest-repair-book-063, the verified archive note recor...
- Matched markers: copper token, silver booth token, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 64 - multi-document-064
Question: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin?

Expected evidence:
- amber lantern
- tuning fork

Expected distractors:
- weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.273396 chunk_id=22255 preview=Question anchor: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin? Case scope id: multi-document-064. Scoped answer s...
  2. score=26.258831 chunk_id=21825 preview=document multi-blue-trunk-cabin-memory-log-064::multi-document-064::1: In document multi-blue-trunk-cabin-memory-log-064, the verified archive note records a...
  3. score=26.227593 chunk_id=22004 preview=document multi-yara-audio-transcript-064::multi-document-064::2: In document multi-yara-audio-transcript-064, the verified archive note records tuning fork....
  4. score=1.956092 chunk_id=22009 preview=document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case...
  5. score=1.883745 chunk_id=22005 preview=document multi-yara-family-register-044::multi-document-044::2: In document multi-yara-family-register-044, the verified archive note records tin key. Case r...
- Matched markers: amber lantern, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.252177 chunk_id=22255 preview=Question anchor: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin? Case scope id: multi-document-064. Scoped answer s...
  2. score=46.224337 chunk_id=22256 preview=Question: Which records together show how Yara prepared the canal barge stop near Blue Trunk cabin? Case scope id: multi-document-064. Combined evidence: amb...
  3. score=26.200819 chunk_id=22004 preview=document multi-yara-audio-transcript-064::multi-document-064::2: In document multi-yara-audio-transcript-064, the verified archive note records tuning fork....
  4. score=26.180562 chunk_id=21825 preview=document multi-blue-trunk-cabin-memory-log-064::multi-document-064::1: In document multi-blue-trunk-cabin-memory-log-064, the verified archive note records a...
  5. score=1.728692 chunk_id=22008 preview=document multi-yara-profile-page-024::multi-document-024::2: In document multi-yara-profile-page-024, the verified archive note records juniper bundles. Case...
- Matched markers: amber lantern, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 2).

### Question 65 - multi-document-065
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving River Lantern inn?

Expected evidence:
- Lantern Tide
- cedar shovel
- willow basket

Expected distractors:
- juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=58.294975 chunk_id=22258 preview=Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving River Lantern inn? Case scope id: multi-document-065. Co...
  2. score=6.080947 chunk_id=21790 preview=document multi-ada-memory-log-085::multi-document-085::2: In document multi-ada-memory-log-085, the verified archive note records green apron. Case record id...
  3. score=6.041736 chunk_id=21789 preview=document multi-ada-memory-log-025::multi-document-025::2: In document multi-ada-memory-log-025, the verified archive note records lantern hook. Case record i...
  4. score=5.993939 chunk_id=21786 preview=document multi-ada-archive-045::multi-document-045::2: In document multi-ada-archive-045, the verified archive note records copper wind vane pin. Case record...
  5. score=5.971405 chunk_id=21879 preview=document multi-lantern-tide-audio-transcript-085::multi-document-085::3: In document multi-lantern-tide-audio-transcript-085, the verified archive note recor...
- Matched markers: Lantern Tide, cedar shovel, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Tide, cedar shovel, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.292025 chunk_id=22257 preview=Question anchor: Which documents together identify the Lantern Tide memory that Ada preserved after leaving River Lantern inn? Case scope id: multi-document-...
  2. score=58.260433 chunk_id=22258 preview=Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving River Lantern inn? Case scope id: multi-document-065. Co...
  3. score=30.189344 chunk_id=21788 preview=document multi-ada-letter-roll-065::multi-document-065::2: In document multi-ada-letter-roll-065, the verified archive note records cedar shovel. Case record...
  4. score=26.283675 chunk_id=21944 preview=document multi-river-lantern-inn-travel-note-065::multi-document-065::1: In document multi-river-lantern-inn-travel-note-065, the verified archive note recor...
  5. score=5.904808 chunk_id=21790 preview=document multi-ada-memory-log-085::multi-document-085::2: In document multi-ada-memory-log-085, the verified archive note records green apron. Case record id...
- Matched markers: Lantern Tide, cedar shovel, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Tide, cedar shovel, willow basket.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 66 - multi-document-066
Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch?

Expected evidence:
- violet ribbon
- star ledger page

Expected distractors:
- carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.430154 chunk_id=22259 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-066....
  2. score=26.461101 chunk_id=22003 preview=document multi-winter-chapel-porch-photo-index-066::multi-document-066::1: In document multi-winter-chapel-porch-photo-index-066, the verified archive note r...
  3. score=4.365900 chunk_id=22002 preview=document multi-winter-chapel-porch-photo-index-006::multi-document-006::1: In document multi-winter-chapel-porch-photo-index-006, the verified archive note r...
- Matched markers: star ledger page, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: star ledger page, violet ribbon.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.424354 chunk_id=22259 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-066....
  2. score=26.446311 chunk_id=22003 preview=document multi-winter-chapel-porch-photo-index-066::multi-document-066::1: In document multi-winter-chapel-porch-photo-index-066, the verified archive note r...
  3. score=4.476201 chunk_id=22002 preview=document multi-winter-chapel-porch-photo-index-006::multi-document-006::1: In document multi-winter-chapel-porch-photo-index-006, the verified archive note r...
  4. score=4.414798 chunk_id=21974 preview=document multi-sonya-repair-book-006::multi-document-006::2: In document multi-sonya-repair-book-006, the verified archive note records glass ink bottle. Cas...
- Matched markers: star ledger page, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: star ledger page, violet ribbon.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (1 vs 2).

### Question 67 - multi-document-067
Question: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge?

Expected evidence:
- blue oar
- silver booth token
- weathered camera strap

Expected distractors:
- canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.318518 chunk_id=22261 preview=Question anchor: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge? Case scope id: multi-document-067. Scoped a...
  2. score=58.292366 chunk_id=22262 preview=Question: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge? Case scope id: multi-document-067. Combined eviden...
  3. score=26.278091 chunk_id=21947 preview=document multi-runa-inventory-sheet-067::multi-document-067::2: In document multi-runa-inventory-sheet-067, the verified archive note records silver booth to...
  4. score=2.205584 chunk_id=21841 preview=document multi-fox-hollow-bridge-audio-transcript-007::multi-document-007::1: In document multi-fox-hollow-bridge-audio-transcript-007, the verified archive...
  5. score=0.968476 chunk_id=21782 preview=document bridge-permit-roll::multi-document-valley-expedition::2: In document bridge-permit-roll, the verified archive note records rope bridge permit. Case...
- Matched markers: blue oar, silver booth token, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.148420 chunk_id=22261 preview=Question anchor: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge? Case scope id: multi-document-067. Scoped a...
  2. score=58.159908 chunk_id=22262 preview=Question: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge? Case scope id: multi-document-067. Combined eviden...
  3. score=26.206284 chunk_id=21842 preview=document multi-fox-hollow-bridge-audio-transcript-067::multi-document-067::1: In document multi-fox-hollow-bridge-audio-transcript-067, the verified archive...
  4. score=2.068535 chunk_id=21841 preview=document multi-fox-hollow-bridge-audio-transcript-007::multi-document-007::1: In document multi-fox-hollow-bridge-audio-transcript-007, the verified archive...
  5. score=1.373970 chunk_id=21843 preview=document multi-fox-hollow-bridge-ledger-037::multi-document-037::1: In document multi-fox-hollow-bridge-ledger-037, the verified archive note records Harvest...
- Matched markers: blue oar, silver booth token, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 68 - multi-document-068
Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well?

Expected evidence:
- linen wick
- birch tea flask

Expected distractors:
- coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.339784 chunk_id=22263 preview=Question anchor: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Case scope id: multi-document-068. Scoped a...
  2. score=26.340062 chunk_id=21868 preview=document multi-iveta-family-register-068::multi-document-068::2: In document multi-iveta-family-register-068, the verified archive note records birch tea fla...
  3. score=26.255661 chunk_id=21997 preview=document multi-willow-courtyard-well-letter-roll-068::multi-document-068::1: In document multi-willow-courtyard-well-letter-roll-068, the verified archive no...
  4. score=13.253553 chunk_id=22009 preview=document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case...
  5. score=4.227593 chunk_id=21867 preview=document multi-iveta-family-register-008::multi-document-008::2: In document multi-iveta-family-register-008, the verified archive note records juniper bundl...
- Matched markers: birch tea flask, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.231625 chunk_id=22263 preview=Question anchor: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Case scope id: multi-document-068. Scoped a...
  2. score=46.161987 chunk_id=22264 preview=Question: Which records together show how Iveta prepared the winter coach stop near Willow Courtyard well? Case scope id: multi-document-068. Combined eviden...
  3. score=26.262816 chunk_id=21997 preview=document multi-willow-courtyard-well-letter-roll-068::multi-document-068::1: In document multi-willow-courtyard-well-letter-roll-068, the verified archive no...
  4. score=26.103131 chunk_id=21868 preview=document multi-iveta-family-register-068::multi-document-068::2: In document multi-iveta-family-register-068, the verified archive note records birch tea fla...
  5. score=4.227370 chunk_id=21996 preview=document multi-willow-courtyard-well-letter-roll-008::multi-document-008::1: In document multi-willow-courtyard-well-letter-roll-008, the verified archive no...
- Matched markers: birch tea flask, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 69 - multi-document-069
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay?

Expected evidence:
- Signal Lantern Morning
- green apron
- oak barrel hoops

Expected distractors:
- tin key

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.575392 chunk_id=22265 preview=Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: mult...
  2. score=58.603023 chunk_id=22266 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-docum...
  3. score=26.582085 chunk_id=21848 preview=document multi-glass-harbor-quay-repair-book-069::multi-document-069::1: In document multi-glass-harbor-quay-repair-book-069, the verified archive note recor...
  4. score=16.582085 chunk_id=21847 preview=document multi-glass-harbor-quay-repair-book-009::multi-document-009::1: In document multi-glass-harbor-quay-repair-book-009, the verified archive note recor...
  5. score=4.559017 chunk_id=22146 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-docum...
- Matched markers: Signal Lantern Morning, green apron, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, green apron, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.550497 chunk_id=22265 preview=Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: mult...
  2. score=58.539004 chunk_id=22266 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-docum...
  3. score=26.573049 chunk_id=21848 preview=document multi-glass-harbor-quay-repair-book-069::multi-document-069::1: In document multi-glass-harbor-quay-repair-book-069, the verified archive note recor...
  4. score=16.573049 chunk_id=21847 preview=document multi-glass-harbor-quay-repair-book-009::multi-document-009::1: In document multi-glass-harbor-quay-repair-book-009, the verified archive note recor...
  5. score=14.091560 chunk_id=21797 preview=document multi-amber-canal-lock-travel-note-089::multi-document-089::1: In document multi-amber-canal-lock-travel-note-089, the verified archive note records...
- Matched markers: Signal Lantern Morning, green apron, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, green apron, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 70 - multi-document-070
Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed?

Expected evidence:
- moonflower cutting
- glass ink bottle

Expected distractors:
- brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=46.403557 chunk_id=22268 preview=Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Case scope id: multi-document-070. Combined...
- Matched markers: glass ink bottle, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: glass ink bottle, moonflower cutting.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.479266 chunk_id=22267 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Case scope id: multi-document-070. Sc...
  2. score=46.463435 chunk_id=22268 preview=Question: Which archive pieces from more than one document explain the family profile event at Birch Ferry shed? Case scope id: multi-document-070. Combined...
  3. score=26.423824 chunk_id=21820 preview=document multi-birch-ferry-shed-inventory-sheet-070::multi-document-070::1: In document multi-birch-ferry-shed-inventory-sheet-070, the verified archive note...
  4. score=13.931632 chunk_id=22140 preview=Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006. Combin...
  5. score=4.402610 chunk_id=21819 preview=document multi-birch-ferry-shed-inventory-sheet-010::multi-document-010::1: In document multi-birch-ferry-shed-inventory-sheet-010, the verified archive note...
- Matched markers: glass ink bottle, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 0).

### Question 71 - multi-document-071
Question: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard?

Expected evidence:
- rope bridge permit
- weathered camera strap
- coal stove hiss

Expected distractors:
- basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.339918 chunk_id=22269 preview=Question anchor: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Case scope id: multi-document-071. Scoped answ...
  2. score=58.217029 chunk_id=22270 preview=Question: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Case scope id: multi-document-071. Combined evidence:...
  3. score=26.325226 chunk_id=21937 preview=document multi-pine-gate-yard-family-register-071::multi-document-071::1: In document multi-pine-gate-yard-family-register-071, the verified archive note rec...
  4. score=26.210997 chunk_id=21991 preview=document multi-vera-minute-book-071::multi-document-071::2: In document multi-vera-minute-book-071, the verified archive note records weathered camera strap....
  5. score=2.113586 chunk_id=21936 preview=document multi-pine-gate-yard-family-register-011::multi-document-011::1: In document multi-pine-gate-yard-family-register-011, the verified archive note rec...
- Matched markers: coal stove hiss, rope bridge permit, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.197954 chunk_id=22269 preview=Question anchor: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Case scope id: multi-document-071. Scoped answ...
  2. score=58.146362 chunk_id=22270 preview=Question: Which documents must be combined to understand Vera's holiday card note about Pine Gate yard? Case scope id: multi-document-071. Combined evidence:...
  3. score=26.182334 chunk_id=21937 preview=document multi-pine-gate-yard-family-register-071::multi-document-071::1: In document multi-pine-gate-yard-family-register-071, the verified archive note rec...
  4. score=26.108206 chunk_id=21991 preview=document multi-vera-minute-book-071::multi-document-071::2: In document multi-vera-minute-book-071, the verified archive note records weathered camera strap....
  5. score=26.071909 chunk_id=21818 preview=document multi-bellwater-fair-travel-note-071::multi-document-071::3: In document multi-bellwater-fair-travel-note-071, the verified archive note records coa...
- Matched markers: coal stove hiss, rope bridge permit, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 72 - multi-document-072
Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop?

Expected evidence:
- paper moon mask
- juniper bundles

Expected distractors:
- copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=4.772378 chunk_id=22026 preview=document school-stage-list::multi-document-school-rehearsal::1: In document school-stage-list, the verified archive note records paper moon mask. Case record...
  2. score=1.884523 chunk_id=21920 preview=document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-family-register-092, the verified archive note records tin key. Case...
  3. score=1.835071 chunk_id=21918 preview=document multi-nadia-audio-transcript-052::multi-document-052::2: In document multi-nadia-audio-transcript-052, the verified archive note records birch tea f...
  4. score=1.804859 chunk_id=21919 preview=document multi-nadia-family-register-032::multi-document-032::2: In document multi-nadia-family-register-032, the verified archive note records tuning fork....
  5. score=1.308248 chunk_id=22009 preview=document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case...
- Matched markers: paper moon mask
- Missing markers: juniper bundles
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: paper moon mask. Missing: juniper bundles.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.281435 chunk_id=22271 preview=Question anchor: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Case scope id: multi-document-072. Scoped answ...
  2. score=46.203473 chunk_id=22272 preview=Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Case scope id: multi-document-072. Combined evidence:...
  3. score=26.315757 chunk_id=21928 preview=document multi-north-bell-workshop-archive-072::multi-document-072::1: In document multi-north-bell-workshop-archive-072, the verified archive note records p...
  4. score=26.125899 chunk_id=21924 preview=document multi-nadia-profile-page-072::multi-document-072::2: In document multi-nadia-profile-page-072, the verified archive note records juniper bundles. Ca...
  5. score=4.344478 chunk_id=21927 preview=document multi-north-bell-workshop-archive-012::multi-document-012::1: In document multi-north-bell-workshop-archive-012, the verified archive note records b...
- Matched markers: juniper bundles, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 73 - multi-document-073
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier?

Expected evidence:
- Moon Orchard Rest
- lantern hook
- carved shell comb

Expected distractors:
- tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.619560 chunk_id=22273 preview=Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-docum...
  2. score=58.558290 chunk_id=22274 preview=Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-document-073...
  3. score=26.636209 chunk_id=21840 preview=document multi-fog-island-pier-ledger-073::multi-document-073::1: In document multi-fog-island-pier-ledger-073, the verified archive note records Moon Orchar...
  4. score=16.732242 chunk_id=21839 preview=document multi-fog-island-pier-ledger-013::multi-document-013::1: In document multi-fog-island-pier-ledger-013, the verified archive note records Moon Orchar...
  5. score=14.213621 chunk_id=21935 preview=document multi-old-quarry-path-travel-note-053::multi-document-053::1: In document multi-old-quarry-path-travel-note-053, the verified archive note records M...
- Matched markers: Moon Orchard Rest, carved shell comb, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Orchard Rest, carved shell comb, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.631533 chunk_id=22273 preview=Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-docum...
  2. score=58.628682 chunk_id=22274 preview=Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-document-073...
  3. score=26.635881 chunk_id=21840 preview=document multi-fog-island-pier-ledger-073::multi-document-073::1: In document multi-fog-island-pier-ledger-073, the verified archive note records Moon Orchar...
  4. score=16.674137 chunk_id=21839 preview=document multi-fog-island-pier-ledger-013::multi-document-013::1: In document multi-fog-island-pier-ledger-013, the verified archive note records Moon Orchar...
  5. score=8.514799 chunk_id=21906 preview=document multi-moon-orchard-rest-audio-transcript-013::multi-document-013::3: In document multi-moon-orchard-rest-audio-transcript-013, the verified archive...
- Matched markers: Moon Orchard Rest, carved shell comb, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Orchard Rest, carved shell comb, lantern hook.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 74 - multi-document-074
Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard?

Expected evidence:
- clay watering cup
- canal route map

Expected distractors:
- willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.338148 chunk_id=22275 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-074. Scop...
  2. score=4.461101 chunk_id=21904 preview=document multi-moon-mill-yard-minute-book-014::multi-document-014::1: In document multi-moon-mill-yard-minute-book-014, the verified archive note records wax...
  3. score=4.339249 chunk_id=22011 preview=document multi-yara-travel-note-014::multi-document-014::2: In document multi-yara-travel-note-014, the verified archive note records basalt sketch. Case rec...
- Matched markers: canal route map, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: canal route map, clay watering cup.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.492415 chunk_id=22275 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-074. Scop...
  2. score=46.385204 chunk_id=22276 preview=Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-074. Combined ev...
  3. score=26.463988 chunk_id=21905 preview=document multi-moon-mill-yard-minute-book-074::multi-document-074::1: In document multi-moon-mill-yard-minute-book-074, the verified archive note records cla...
  4. score=26.408689 chunk_id=22012 preview=document multi-yara-travel-note-074::multi-document-074::2: In document multi-yara-travel-note-074, the verified archive note records canal route map. Case r...
  5. score=4.513011 chunk_id=21904 preview=document multi-moon-mill-yard-minute-book-014::multi-document-014::1: In document multi-moon-mill-yard-minute-book-014, the verified archive note records wax...
- Matched markers: canal route map, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map, clay watering cup.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 2).

### Question 75 - multi-document-075
Question: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove?

Expected evidence:
- saffron scarf
- coal stove hiss
- copper token

Expected distractors:
- star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.139069 chunk_id=22277 preview=Question anchor: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Case scope id: multi-document-075. Scoped answ...
  2. score=58.126393 chunk_id=22278 preview=Question: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Case scope id: multi-document-075. Combined evidence:...
  3. score=9.905136 chunk_id=21793 preview=document multi-ada-photo-index-015::multi-document-015::2: In document multi-ada-photo-index-015, the verified archive note records copper token. Case record...
  4. score=1.853953 chunk_id=21883 preview=document multi-lantern-tide-repair-book-015::multi-document-015::3: In document multi-lantern-tide-repair-book-015, the verified archive note records silver...
  5. score=1.644089 chunk_id=21791 preview=document multi-ada-minute-book-035::multi-document-035::2: In document multi-ada-minute-book-035, the verified archive note records silver booth token. Case...
- Matched markers: coal stove hiss, copper token, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.087904 chunk_id=22277 preview=Question anchor: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Case scope id: multi-document-075. Scoped answ...
  2. score=58.019800 chunk_id=22278 preview=Question: Which documents must be combined to understand Ada's boat manifest note about Driftwood cove? Case scope id: multi-document-075. Combined evidence:...
  3. score=26.051092 chunk_id=21833 preview=document multi-driftwood-cove-profile-page-075::multi-document-075::1: In document multi-driftwood-cove-profile-page-075, the verified archive note records s...
  4. score=25.989340 chunk_id=21794 preview=document multi-ada-photo-index-075::multi-document-075::2: In document multi-ada-photo-index-075, the verified archive note records coal stove hiss. Case rec...
  5. score=25.985664 chunk_id=21884 preview=document multi-lantern-tide-repair-book-075::multi-document-075::3: In document multi-lantern-tide-repair-book-075, the verified archive note records copper...
- Matched markers: coal stove hiss, copper token, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 2).

### Question 76 - multi-document-076
Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft?

Expected evidence:
- blue glass jar
- tin key

Expected distractors:
- silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.362500 chunk_id=22279 preview=Question anchor: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-076. Scoped answer s...
  2. score=46.247214 chunk_id=22280 preview=Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-076. Combined evidence: blu...
  3. score=26.375693 chunk_id=21941 preview=document multi-ridge-post-loft-memory-log-076::multi-document-076::1: In document multi-ridge-post-loft-memory-log-076, the verified archive note records blu...
  4. score=26.234813 chunk_id=21969 preview=document multi-sonya-audio-transcript-076::multi-document-076::2: In document multi-sonya-audio-transcript-076, the verified archive note records tin key. Ca...
  5. score=4.423250 chunk_id=21940 preview=document multi-ridge-post-loft-memory-log-016::multi-document-016::1: In document multi-ridge-post-loft-memory-log-016, the verified archive note records amb...
- Matched markers: blue glass jar, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.260268 chunk_id=22279 preview=Question anchor: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-076. Scoped answer s...
  2. score=46.217507 chunk_id=22280 preview=Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-076. Combined evidence: blu...
  3. score=26.269836 chunk_id=21941 preview=document multi-ridge-post-loft-memory-log-076::multi-document-076::1: In document multi-ridge-post-loft-memory-log-076, the verified archive note records blu...
  4. score=26.141520 chunk_id=21969 preview=document multi-sonya-audio-transcript-076::multi-document-076::2: In document multi-sonya-audio-transcript-076, the verified archive note records tin key. Ca...
  5. score=4.249568 chunk_id=21940 preview=document multi-ridge-post-loft-memory-log-016::multi-document-016::1: In document multi-ridge-post-loft-memory-log-016, the verified archive note records amb...
- Matched markers: blue glass jar, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, tin key.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 77 - multi-document-077
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room?

Expected evidence:
- Harvest Glow
- copper wind vane pin
- brass compass

Expected distractors:
- birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.598181 chunk_id=22281 preview=Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-...
  2. score=26.685980 chunk_id=21837 preview=document multi-east-signal-room-travel-note-077::multi-document-077::1: In document multi-east-signal-room-travel-note-077, the verified archive note records...
  3. score=16.685980 chunk_id=21836 preview=document multi-east-signal-room-travel-note-017::multi-document-017::1: In document multi-east-signal-room-travel-note-017, the verified archive note records...
  4. score=8.684847 chunk_id=21854 preview=document multi-harvest-glow-family-register-017::multi-document-017::3: In document multi-harvest-glow-family-register-017, the verified archive note records...
  5. score=6.162266 chunk_id=21945 preview=document multi-runa-archive-057::multi-document-057::2: In document multi-runa-archive-057, the verified archive note records lantern hook. Case record id: m...
- Matched markers: Harvest Glow, brass compass, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Harvest Glow, brass compass, copper wind vane pin.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.516760 chunk_id=22281 preview=Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-...
  2. score=58.483660 chunk_id=22282 preview=Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-077. Co...
  3. score=26.584392 chunk_id=21837 preview=document multi-east-signal-room-travel-note-077::multi-document-077::1: In document multi-east-signal-room-travel-note-077, the verified archive note records...
  4. score=16.621798 chunk_id=21836 preview=document multi-east-signal-room-travel-note-017::multi-document-017::1: In document multi-east-signal-room-travel-note-017, the verified archive note records...
  5. score=8.429555 chunk_id=21854 preview=document multi-harvest-glow-family-register-017::multi-document-017::3: In document multi-harvest-glow-family-register-017, the verified archive note records...
- Matched markers: Harvest Glow, brass compass, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Harvest Glow, brass compass, copper wind vane pin.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 78 - multi-document-078
Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch?

Expected evidence:
- wax thread
- basalt sketch

Expected distractors:
- oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.560342 chunk_id=22283 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-078. S...
  2. score=46.494705 chunk_id=22284 preview=Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-078. Combined...
  3. score=26.551793 chunk_id=21980 preview=document multi-south-meadow-arch-photo-index-078::multi-document-078::1: In document multi-south-meadow-arch-photo-index-078, the verified archive note recor...
  4. score=26.386436 chunk_id=21872 preview=document multi-iveta-repair-book-078::multi-document-078::2: In document multi-iveta-repair-book-078, the verified archive note records basalt sketch. Case r...
  5. score=4.551793 chunk_id=21979 preview=document multi-south-meadow-arch-photo-index-018::multi-document-018::1: In document multi-south-meadow-arch-photo-index-018, the verified archive note recor...
- Matched markers: basalt sketch, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.492969 chunk_id=22283 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-078. S...
  2. score=46.487541 chunk_id=22284 preview=Question: Which archive pieces from more than one document explain the family profile event at South Meadow arch? Case scope id: multi-document-078. Combined...
  3. score=26.517309 chunk_id=21980 preview=document multi-south-meadow-arch-photo-index-078::multi-document-078::1: In document multi-south-meadow-arch-photo-index-078, the verified archive note recor...
  4. score=4.498703 chunk_id=21979 preview=document multi-south-meadow-arch-photo-index-018::multi-document-018::1: In document multi-south-meadow-arch-photo-index-018, the verified archive note recor...
- Matched markers: basalt sketch, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 79 - multi-document-079
Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic?

Expected evidence:
- smoke vent chain
- copper token
- silver booth token

Expected distractors:
- glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.443268 chunk_id=22285 preview=Question anchor: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Case scope id: multi-document-079. Scoped...
  2. score=58.273016 chunk_id=22286 preview=Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Case scope id: multi-document-079. Combined evide...
  3. score=26.493103 chunk_id=21959 preview=document multi-signal-lantern-morning-ledger-079::multi-document-079::3: In document multi-signal-lantern-morning-ledger-079, the verified archive note recor...
  4. score=26.297468 chunk_id=21888 preview=document multi-maple-court-attic-audio-transcript-079::multi-document-079::1: In document multi-maple-court-attic-audio-transcript-079, the verified archive...
  5. score=13.524579 chunk_id=21812 preview=document multi-bellwater-fair-ledger-031::multi-document-031::3: In document multi-bellwater-fair-ledger-031, the verified archive note records silver booth...
- Matched markers: copper token, silver booth token, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.282665 chunk_id=22285 preview=Question anchor: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Case scope id: multi-document-079. Scoped...
  2. score=58.178244 chunk_id=22286 preview=Question: Which documents must be combined to understand Zora's travel ledger note about Maple Court attic? Case scope id: multi-document-079. Combined evide...
  3. score=26.315562 chunk_id=21888 preview=document multi-maple-court-attic-audio-transcript-079::multi-document-079::1: In document multi-maple-court-attic-audio-transcript-079, the verified archive...
  4. score=26.157476 chunk_id=22016 preview=document multi-zora-inventory-sheet-079::multi-document-079::2: In document multi-zora-inventory-sheet-079, the verified archive note records copper token. C...
  5. score=26.152598 chunk_id=21959 preview=document multi-signal-lantern-morning-ledger-079::multi-document-079::3: In document multi-signal-lantern-morning-ledger-079, the verified archive note recor...
- Matched markers: copper token, silver booth token, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 80 - multi-document-080
Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery?

Expected evidence:
- amber lantern
- tuning fork

Expected distractors:
- weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.310070 chunk_id=22287 preview=Question anchor: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Case scope id: multi-document-080. Scoped an...
  2. score=26.331369 chunk_id=21982 preview=document multi-star-basin-gallery-letter-roll-080::multi-document-080::1: In document multi-star-basin-gallery-letter-roll-080, the verified archive note rec...
  3. score=4.535980 chunk_id=21895 preview=document multi-mira-family-register-020::multi-document-020::2: In document multi-mira-family-register-020, the verified archive note records birch tea flask...
  4. score=4.361951 chunk_id=21981 preview=document multi-star-basin-gallery-letter-roll-020::multi-document-020::1: In document multi-star-basin-gallery-letter-roll-020, the verified archive note rec...
  5. score=1.982455 chunk_id=21894 preview=document multi-mira-audio-transcript-100::multi-document-100::2: In document multi-mira-audio-transcript-100, the verified archive note records birch tea fla...
- Matched markers: amber lantern, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.310160 chunk_id=22287 preview=Question anchor: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Case scope id: multi-document-080. Scoped an...
  2. score=46.238931 chunk_id=22288 preview=Question: Which records together show how Mira prepared the overnight ferry stop near Star Basin gallery? Case scope id: multi-document-080. Combined evidenc...
  3. score=26.295986 chunk_id=21982 preview=document multi-star-basin-gallery-letter-roll-080::multi-document-080::1: In document multi-star-basin-gallery-letter-roll-080, the verified archive note rec...
  4. score=26.182897 chunk_id=21896 preview=document multi-mira-family-register-080::multi-document-080::2: In document multi-mira-family-register-080, the verified archive note records tuning fork. Ca...
  5. score=4.263843 chunk_id=21981 preview=document multi-star-basin-gallery-letter-roll-020::multi-document-020::1: In document multi-star-basin-gallery-letter-roll-020, the verified archive note rec...
- Matched markers: amber lantern, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 3).

### Question 81 - multi-document-081
Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse?

Expected evidence:
- Bellwater Fair
- cedar shovel
- willow basket

Expected distractors:
- juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.604751 chunk_id=22289 preview=Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-...
  2. score=58.579941 chunk_id=22290 preview=Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-documen...
  3. score=26.657107 chunk_id=21967 preview=document multi-snow-orchard-storehouse-repair-book-081::multi-document-081::1: In document multi-snow-orchard-storehouse-repair-book-081, the verified archiv...
  4. score=16.657107 chunk_id=21966 preview=document multi-snow-orchard-storehouse-repair-book-021::multi-document-021::1: In document multi-snow-orchard-storehouse-repair-book-021, the verified archiv...
  5. score=14.063621 chunk_id=21938 preview=document multi-pine-gate-yard-travel-note-041::multi-document-041::1: In document multi-pine-gate-yard-travel-note-041, the verified archive note records Bel...
- Matched markers: Bellwater Fair, cedar shovel, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bellwater Fair, cedar shovel, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.482402 chunk_id=22289 preview=Question anchor: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-...
  2. score=58.480906 chunk_id=22290 preview=Question: Which documents together identify the Bellwater Fair memory that Vera preserved after leaving Snow Orchard storehouse? Case scope id: multi-documen...
  3. score=30.385541 chunk_id=21985 preview=document multi-vera-archive-081::multi-document-081::2: In document multi-vera-archive-081, the verified archive note records cedar shovel. Case record id: m...
  4. score=26.480034 chunk_id=21967 preview=document multi-snow-orchard-storehouse-repair-book-081::multi-document-081::1: In document multi-snow-orchard-storehouse-repair-book-081, the verified archiv...
  5. score=16.517309 chunk_id=21966 preview=document multi-snow-orchard-storehouse-repair-book-021::multi-document-021::1: In document multi-snow-orchard-storehouse-repair-book-021, the verified archiv...
- Matched markers: Bellwater Fair, cedar shovel, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bellwater Fair, cedar shovel, willow basket.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 82 - multi-document-082
Question: Which archive pieces from more than one document explain the family profile event at Cedar Hill station?

Expected evidence:
- violet ribbon
- star ledger page

Expected distractors:
- carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.334189 chunk_id=22291 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Cedar Hill station? Case scope id: multi-document-082....
  2. score=26.342705 chunk_id=21827 preview=document multi-cedar-hill-station-inventory-sheet-082::multi-document-082::1: In document multi-cedar-hill-station-inventory-sheet-082, the verified archive...
  3. score=4.342705 chunk_id=21826 preview=document multi-cedar-hill-station-inventory-sheet-022::multi-document-022::1: In document multi-cedar-hill-station-inventory-sheet-022, the verified archive...
- Matched markers: star ledger page, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: star ledger page, violet ribbon.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: violet ribbon, star ledger page
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 83 - multi-document-083
Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path?

Expected evidence:
- blue oar
- silver booth token
- weathered camera strap

Expected distractors:
- canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.533946 chunk_id=22293 preview=Question anchor: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Case scope id: multi-document-083. Scope...
  2. score=58.296139 chunk_id=22294 preview=Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Case scope id: multi-document-083. Combined evi...
  3. score=26.528493 chunk_id=21934 preview=document multi-old-quarry-path-family-register-083::multi-document-083::1: In document multi-old-quarry-path-family-register-083, the verified archive note r...
  4. score=26.466667 chunk_id=21805 preview=document multi-anya-minute-book-083::multi-document-083::2: In document multi-anya-minute-book-083, the verified archive note records silver booth token. Cas...
  5. score=9.952911 chunk_id=21804 preview=document multi-anya-minute-book-023::multi-document-023::2: In document multi-anya-minute-book-023, the verified archive note records weathered camera strap....
- Matched markers: blue oar, silver booth token, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.213119 chunk_id=22293 preview=Question anchor: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Case scope id: multi-document-083. Scope...
  2. score=58.167918 chunk_id=22294 preview=Question: Which documents must be combined to understand Anya's memory sketchbook note about Old Quarry path? Case scope id: multi-document-083. Combined evi...
  3. score=26.239165 chunk_id=21934 preview=document multi-old-quarry-path-family-register-083::multi-document-083::1: In document multi-old-quarry-path-family-register-083, the verified archive note r...
  4. score=26.112147 chunk_id=21805 preview=document multi-anya-minute-book-083::multi-document-083::2: In document multi-anya-minute-book-083, the verified archive note records silver booth token. Cas...
  5. score=26.072743 chunk_id=21914 preview=document multi-moon-orchard-rest-travel-note-083::multi-document-083::3: In document multi-moon-orchard-rest-travel-note-083, the verified archive note recor...
- Matched markers: blue oar, silver booth token, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 84 - multi-document-084
Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office?

Expected evidence:
- linen wick
- birch tea flask

Expected distractors:
- coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.505627 chunk_id=22295 preview=Question anchor: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-084. Scoped answer...
  2. score=46.272225 chunk_id=22296 preview=Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-084. Combined evidence: l...
  3. score=26.560251 chunk_id=21830 preview=document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records lin...
  4. score=26.372703 chunk_id=22009 preview=document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case...
  5. score=4.437455 chunk_id=21829 preview=document multi-cloud-wharf-office-archive-024::multi-document-024::1: In document multi-cloud-wharf-office-archive-024, the verified archive note records pap...
- Matched markers: birch tea flask, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.262595 chunk_id=22295 preview=Question anchor: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-084. Scoped answer...
  2. score=46.144791 chunk_id=22296 preview=Question: Which records together show how Yara prepared the canal barge stop near Cloud Wharf office? Case scope id: multi-document-084. Combined evidence: l...
  3. score=26.298594 chunk_id=21830 preview=document multi-cloud-wharf-office-archive-084::multi-document-084::1: In document multi-cloud-wharf-office-archive-084, the verified archive note records lin...
  4. score=26.156670 chunk_id=22009 preview=document multi-yara-profile-page-084::multi-document-084::2: In document multi-yara-profile-page-084, the verified archive note records birch tea flask. Case...
  5. score=4.260782 chunk_id=21829 preview=document multi-cloud-wharf-office-archive-024::multi-document-024::1: In document multi-cloud-wharf-office-archive-024, the verified archive note records pap...
- Matched markers: birch tea flask, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 85 - multi-document-085
Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor?

Expected evidence:
- Lantern Tide
- green apron
- oak barrel hoops

Expected distractors:
- tin key

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.644049 chunk_id=22297 preview=Question anchor: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-docum...
  2. score=58.508744 chunk_id=22298 preview=Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-document-085...
  3. score=30.527350 chunk_id=21790 preview=document multi-ada-memory-log-085::multi-document-085::2: In document multi-ada-memory-log-085, the verified archive note records green apron. Case record id...
  4. score=30.477046 chunk_id=21879 preview=document multi-lantern-tide-audio-transcript-085::multi-document-085::3: In document multi-lantern-tide-audio-transcript-085, the verified archive note recor...
  5. score=26.546285 chunk_id=21851 preview=document multi-harbor-glass-corridor-ledger-085::multi-document-085::1: In document multi-harbor-glass-corridor-ledger-085, the verified archive note records...
- Matched markers: Lantern Tide, green apron, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Tide, green apron, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.502759 chunk_id=22297 preview=Question anchor: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-docum...
  2. score=58.431234 chunk_id=22298 preview=Question: Which documents together identify the Lantern Tide memory that Ada preserved after leaving Harbor Glass corridor? Case scope id: multi-document-085...
  3. score=30.415267 chunk_id=21790 preview=document multi-ada-memory-log-085::multi-document-085::2: In document multi-ada-memory-log-085, the verified archive note records green apron. Case record id...
  4. score=26.509947 chunk_id=21851 preview=document multi-harbor-glass-corridor-ledger-085::multi-document-085::1: In document multi-harbor-glass-corridor-ledger-085, the verified archive note records...
  5. score=16.509947 chunk_id=21850 preview=document multi-harbor-glass-corridor-ledger-025::multi-document-025::1: In document multi-harbor-glass-corridor-ledger-025, the verified archive note records...
- Matched markers: Lantern Tide, green apron, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Tide, green apron, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 86 - multi-document-086
Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane?

Expected evidence:
- moonflower cutting
- glass ink bottle

Expected distractors:
- brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.527350 chunk_id=22299 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086....
  2. score=46.410179 chunk_id=22300 preview=Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Combine...
  3. score=26.461101 chunk_id=21932 preview=document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note rec...
  4. score=26.339249 chunk_id=21977 preview=document multi-sonya-travel-note-086::multi-document-086::2: In document multi-sonya-travel-note-086, the verified archive note records glass ink bottle. Cas...
  5. score=4.393760 chunk_id=21931 preview=document multi-north-orchard-lane-minute-book-026::multi-document-026::1: In document multi-north-orchard-lane-minute-book-026, the verified archive note rec...
- Matched markers: glass ink bottle, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.566474 chunk_id=22299 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086....
  2. score=46.479072 chunk_id=22300 preview=Question: Which archive pieces from more than one document explain the family profile event at North Orchard lane? Case scope id: multi-document-086. Combine...
  3. score=26.533165 chunk_id=21932 preview=document multi-north-orchard-lane-minute-book-086::multi-document-086::1: In document multi-north-orchard-lane-minute-book-086, the verified archive note rec...
  4. score=26.471932 chunk_id=21977 preview=document multi-sonya-travel-note-086::multi-document-086::2: In document multi-sonya-travel-note-086, the verified archive note records glass ink bottle. Cas...
  5. score=13.910564 chunk_id=22140 preview=Question: Which archive pieces from more than one document explain the family profile event at Winter Chapel porch? Case scope id: multi-document-006. Combin...
- Matched markers: glass ink bottle, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, moonflower cutting.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 87 - multi-document-087
Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade?

Expected evidence:
- rope bridge permit
- weathered camera strap
- coal stove hiss

Expected distractors:
- basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.589495 chunk_id=22301 preview=Question anchor: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Case scope id: multi-document-087. S...
  2. score=58.478089 chunk_id=22302 preview=Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Case scope id: multi-document-087. Combined...
  3. score=26.668049 chunk_id=21863 preview=document multi-hollow-market-arcade-profile-page-087::multi-document-087::1: In document multi-hollow-market-arcade-profile-page-087, the verified archive no...
  4. score=15.689298 chunk_id=22141 preview=Question anchor: Which documents must be combined to understand Runa's family note note about Fox Hollow bridge? Case scope id: multi-document-007. Scoped an...
  5. score=2.360403 chunk_id=21862 preview=document multi-hollow-market-arcade-profile-page-027::multi-document-027::1: In document multi-hollow-market-arcade-profile-page-027, the verified archive no...
- Matched markers: coal stove hiss, rope bridge permit, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.321406 chunk_id=22301 preview=Question anchor: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Case scope id: multi-document-087. S...
  2. score=58.274510 chunk_id=22302 preview=Question: Which documents must be combined to understand Runa's photo album page note about Hollow Market arcade? Case scope id: multi-document-087. Combined...
  3. score=26.307084 chunk_id=21863 preview=document multi-hollow-market-arcade-profile-page-087::multi-document-087::1: In document multi-hollow-market-arcade-profile-page-087, the verified archive no...
  4. score=26.217460 chunk_id=21954 preview=document multi-runa-photo-index-087::multi-document-087::2: In document multi-runa-photo-index-087, the verified archive note records weathered camera strap....
  5. score=26.216083 chunk_id=21860 preview=document multi-harvest-glow-repair-book-087::multi-document-087::3: In document multi-harvest-glow-repair-book-087, the verified archive note records coal st...
- Matched markers: coal stove hiss, rope bridge permit, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, rope bridge permit, weathered camera strap.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 88 - multi-document-088
Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall?

Expected evidence:
- paper moon mask
- juniper bundles

Expected distractors:
- copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.214698 chunk_id=22303 preview=Question anchor: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Case scope id: multi-document-088. Scoped answe...
  2. score=26.201478 chunk_id=21866 preview=document multi-iveta-audio-transcript-088::multi-document-088::2: In document multi-iveta-audio-transcript-088, the verified archive note records juniper bun...
  3. score=4.204145 chunk_id=21891 preview=document multi-marble-stair-hall-memory-log-028::multi-document-028::1: In document multi-marble-stair-hall-memory-log-028, the verified archive note records...
  4. score=4.201478 chunk_id=21865 preview=document multi-iveta-audio-transcript-028::multi-document-028::2: In document multi-iveta-audio-transcript-028, the verified archive note records tin key. Ca...
  5. score=1.812910 chunk_id=21868 preview=document multi-iveta-family-register-068::multi-document-068::2: In document multi-iveta-family-register-068, the verified archive note records birch tea fla...
- Matched markers: juniper bundles, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.265006 chunk_id=22303 preview=Question anchor: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Case scope id: multi-document-088. Scoped answe...
  2. score=46.190475 chunk_id=22304 preview=Question: Which records together show how Iveta prepared the winter coach stop near Marble stair hall? Case scope id: multi-document-088. Combined evidence:...
  3. score=26.202269 chunk_id=21892 preview=document multi-marble-stair-hall-memory-log-088::multi-document-088::1: In document multi-marble-stair-hall-memory-log-088, the verified archive note records...
  4. score=26.194433 chunk_id=21866 preview=document multi-iveta-audio-transcript-088::multi-document-088::2: In document multi-iveta-audio-transcript-088, the verified archive note records juniper bun...
  5. score=4.212524 chunk_id=21891 preview=document multi-marble-stair-hall-memory-log-028::multi-document-028::1: In document multi-marble-stair-hall-memory-log-028, the verified archive note records...
- Matched markers: juniper bundles, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles, paper moon mask.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 3).

### Question 89 - multi-document-089
Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock?

Expected evidence:
- Signal Lantern Morning
- lantern hook
- carved shell comb

Expected distractors:
- tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.720827 chunk_id=22305 preview=Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi...
  2. score=58.561341 chunk_id=22306 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-docume...
  3. score=30.522976 chunk_id=22018 preview=document multi-zora-letter-roll-089::multi-document-089::2: In document multi-zora-letter-roll-089, the verified archive note records lantern hook. Case reco...
  4. score=30.486664 chunk_id=21957 preview=document multi-signal-lantern-morning-family-register-089::multi-document-089::3: In document multi-signal-lantern-morning-family-register-089, the verified...
  5. score=26.798008 chunk_id=21797 preview=document multi-amber-canal-lock-travel-note-089::multi-document-089::1: In document multi-amber-canal-lock-travel-note-089, the verified archive note records...
- Matched markers: Signal Lantern Morning, carved shell comb, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, carved shell comb, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.558656 chunk_id=22305 preview=Question anchor: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi...
  2. score=58.561385 chunk_id=22306 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Amber Canal lock? Case scope id: multi-docume...
  3. score=30.441695 chunk_id=21957 preview=document multi-signal-lantern-morning-family-register-089::multi-document-089::3: In document multi-signal-lantern-morning-family-register-089, the verified...
  4. score=26.576481 chunk_id=21797 preview=document multi-amber-canal-lock-travel-note-089::multi-document-089::1: In document multi-amber-canal-lock-travel-note-089, the verified archive note records...
  5. score=26.115148 chunk_id=22146 preview=Question: Which documents together identify the Signal Lantern Morning memory that Zora preserved after leaving Glass Harbor quay? Case scope id: multi-docum...
- Matched markers: Signal Lantern Morning, carved shell comb, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, carved shell comb, lantern hook.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 90 - multi-document-090
Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square?

Expected evidence:
- clay watering cup
- canal route map

Expected distractors:
- willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.399467 chunk_id=22307 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-090....
  2. score=26.393760 chunk_id=21809 preview=document multi-bell-bridge-square-photo-index-090::multi-document-090::1: In document multi-bell-bridge-square-photo-index-090, the verified archive note rec...
  3. score=4.461101 chunk_id=21808 preview=document multi-bell-bridge-square-photo-index-030::multi-document-030::1: In document multi-bell-bridge-square-photo-index-030, the verified archive note rec...
- Matched markers: canal route map, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map, clay watering cup.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.408530 chunk_id=22307 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-090....
  2. score=4.522082 chunk_id=21808 preview=document multi-bell-bridge-square-photo-index-030::multi-document-030::1: In document multi-bell-bridge-square-photo-index-030, the verified archive note rec...
- Matched markers: canal route map, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: canal route map, clay watering cup.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 91 - multi-document-091
Question: Which documents must be combined to understand Vera's family note note about Watchtower landing?

Expected evidence:
- saffron scarf
- coal stove hiss
- copper token

Expected distractors:
- star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.021659 chunk_id=22309 preview=Question anchor: Which documents must be combined to understand Vera's family note note about Watchtower landing? Case scope id: multi-document-091. Scoped a...
  2. score=57.947214 chunk_id=22310 preview=Question: Which documents must be combined to understand Vera's family note note about Watchtower landing? Case scope id: multi-document-091. Combined eviden...
  3. score=26.026235 chunk_id=21994 preview=document multi-watchtower-landing-audio-transcript-091::multi-document-091::1: In document multi-watchtower-landing-audio-transcript-091, the verified archiv...
  4. score=1.872233 chunk_id=21993 preview=document multi-watchtower-landing-audio-transcript-031::multi-document-031::1: In document multi-watchtower-landing-audio-transcript-031, the verified archiv...
- Matched markers: coal stove hiss, copper token, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=76.848155 chunk_id=22309 preview=Question anchor: Which documents must be combined to understand Vera's family note note about Watchtower landing? Case scope id: multi-document-091. Scoped a...
  2. score=57.845467 chunk_id=22310 preview=Question: Which documents must be combined to understand Vera's family note note about Watchtower landing? Case scope id: multi-document-091. Combined eviden...
  3. score=25.788943 chunk_id=21994 preview=document multi-watchtower-landing-audio-transcript-091::multi-document-091::1: In document multi-watchtower-landing-audio-transcript-091, the verified archiv...
  4. score=25.779946 chunk_id=21987 preview=document multi-vera-inventory-sheet-091::multi-document-091::2: In document multi-vera-inventory-sheet-091, the verified archive note records coal stove hiss...
  5. score=25.762479 chunk_id=21813 preview=document multi-bellwater-fair-ledger-091::multi-document-091::3: In document multi-bellwater-fair-ledger-091, the verified archive note records copper token....
- Matched markers: coal stove hiss, copper token, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, copper token, saffron scarf.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 92 - multi-document-092
Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk?

Expected evidence:
- blue glass jar
- tin key

Expected distractors:
- silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.339784 chunk_id=22311 preview=Question anchor: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Case scope id: multi-document-092. Scoped answer...
  2. score=26.340062 chunk_id=21920 preview=document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-family-register-092, the verified archive note records tin key. Case...
  3. score=26.255661 chunk_id=21876 preview=document multi-lantern-row-kiosk-letter-roll-092::multi-document-092::1: In document multi-lantern-row-kiosk-letter-roll-092, the verified archive note recor...
  4. score=4.333745 chunk_id=21875 preview=document multi-lantern-row-kiosk-letter-roll-032::multi-document-032::1: In document multi-lantern-row-kiosk-letter-roll-032, the verified archive note recor...
  5. score=4.259573 chunk_id=21919 preview=document multi-nadia-family-register-032::multi-document-032::2: In document multi-nadia-family-register-032, the verified archive note records tuning fork....
- Matched markers: blue glass jar, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.190494 chunk_id=22311 preview=Question anchor: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Case scope id: multi-document-092. Scoped answer...
  2. score=46.177964 chunk_id=22312 preview=Question: Which records together show how Nadia prepared the river skiff stop near Lantern Row kiosk? Case scope id: multi-document-092. Combined evidence: b...
  3. score=26.147761 chunk_id=21876 preview=document multi-lantern-row-kiosk-letter-roll-092::multi-document-092::1: In document multi-lantern-row-kiosk-letter-roll-092, the verified archive note recor...
  4. score=26.114088 chunk_id=21920 preview=document multi-nadia-family-register-092::multi-document-092::2: In document multi-nadia-family-register-092, the verified archive note records tin key. Case...
  5. score=13.668593 chunk_id=22152 preview=Question: Which records together show how Nadia prepared the river skiff stop near North Bell workshop? Case scope id: multi-document-012. Combined evidence:...
- Matched markers: blue glass jar, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, tin key.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 2).

### Question 93 - multi-document-093
Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room?

Expected evidence:
- Moon Orchard Rest
- copper wind vane pin
- brass compass

Expected distractors:
- birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.610757 chunk_id=22313 preview=Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-doc...
  2. score=26.600000 chunk_id=21917 preview=document multi-moss-archive-room-repair-book-093::multi-document-093::1: In document multi-moss-archive-room-repair-book-093, the verified archive note recor...
  3. score=16.600000 chunk_id=21916 preview=document multi-moss-archive-room-repair-book-033::multi-document-033::1: In document multi-moss-archive-room-repair-book-033, the verified archive note recor...
  4. score=16.375740 chunk_id=22153 preview=Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-docum...
  5. score=14.466886 chunk_id=21935 preview=document multi-old-quarry-path-travel-note-053::multi-document-053::1: In document multi-old-quarry-path-travel-note-053, the verified archive note records M...
- Matched markers: Moon Orchard Rest, brass compass, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Orchard Rest, brass compass, copper wind vane pin.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.591534 chunk_id=22313 preview=Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-doc...
  2. score=58.579741 chunk_id=22314 preview=Question: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Moss Archive room? Case scope id: multi-document-0...
  3. score=26.610526 chunk_id=21917 preview=document multi-moss-archive-room-repair-book-093::multi-document-093::1: In document multi-moss-archive-room-repair-book-093, the verified archive note recor...
  4. score=16.610526 chunk_id=21916 preview=document multi-moss-archive-room-repair-book-033::multi-document-033::1: In document multi-moss-archive-room-repair-book-033, the verified archive note recor...
  5. score=16.347184 chunk_id=22153 preview=Question anchor: Which documents together identify the Moon Orchard Rest memory that Anya preserved after leaving Fog Island pier? Case scope id: multi-docum...
- Matched markers: Moon Orchard Rest, brass compass, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Orchard Rest, brass compass, copper wind vane pin.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 94 - multi-document-094
Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin?

Expected evidence:
- wax thread
- basalt sketch

Expected distractors:
- oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.419809 chunk_id=22315 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Sc...
  2. score=46.385194 chunk_id=22316 preview=Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Combined...
  3. score=13.928746 chunk_id=22188 preview=Question: Which archive pieces from more than one document explain the family profile event at Bell Bridge square? Case scope id: multi-document-030. Combine...
  4. score=13.928746 chunk_id=22156 preview=Question: Which archive pieces from more than one document explain the family profile event at Moon Mill yard? Case scope id: multi-document-014. Combined ev...
  5. score=13.922577 chunk_id=22252 preview=Question: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Case scope id: multi-document-062. Combined...
- Matched markers: basalt sketch, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.442379 chunk_id=22315 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Sc...
  2. score=46.427955 chunk_id=22316 preview=Question: Which archive pieces from more than one document explain the family profile event at Blue Trunk cabin? Case scope id: multi-document-094. Combined...
  3. score=26.437242 chunk_id=21824 preview=document multi-blue-trunk-cabin-inventory-sheet-094::multi-document-094::1: In document multi-blue-trunk-cabin-inventory-sheet-094, the verified archive note...
  4. score=4.418693 chunk_id=21823 preview=document multi-blue-trunk-cabin-inventory-sheet-034::multi-document-034::1: In document multi-blue-trunk-cabin-inventory-sheet-034, the verified archive note...
  5. score=3.955942 chunk_id=22251 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Lantern Row kiosk? Case scope id: multi-document-062. S...
- Matched markers: basalt sketch, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, wax thread.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 95 - multi-document-095
Question: Which documents must be combined to understand Ada's archive card note about River Lantern inn?

Expected evidence:
- smoke vent chain
- copper token
- silver booth token

Expected distractors:
- glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=58.329813 chunk_id=22318 preview=Question: Which documents must be combined to understand Ada's archive card note about River Lantern inn? Case scope id: multi-document-095. Combined evidenc...
  2. score=25.726361 chunk_id=22158 preview=Question: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Case scope id: multi-document-015. Combined evidence:...
  3. score=16.059161 chunk_id=22157 preview=Question anchor: Which documents must be combined to understand Ada's holiday card note about Driftwood cove? Case scope id: multi-document-015. Scoped answe...
  4. score=14.003953 chunk_id=21883 preview=document multi-lantern-tide-repair-book-015::multi-document-015::3: In document multi-lantern-tide-repair-book-015, the verified archive note records silver...
  5. score=13.905136 chunk_id=21793 preview=document multi-ada-photo-index-015::multi-document-015::2: In document multi-ada-photo-index-015, the verified archive note records copper token. Case record...
- Matched markers: copper token, silver booth token, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.246840 chunk_id=22317 preview=Question anchor: Which documents must be combined to understand Ada's archive card note about River Lantern inn? Case scope id: multi-document-095. Scoped an...
  2. score=58.167059 chunk_id=22318 preview=Question: Which documents must be combined to understand Ada's archive card note about River Lantern inn? Case scope id: multi-document-095. Combined evidenc...
  3. score=26.236436 chunk_id=21943 preview=document multi-river-lantern-inn-family-register-095::multi-document-095::1: In document multi-river-lantern-inn-family-register-095, the verified archive no...
  4. score=26.164674 chunk_id=21792 preview=document multi-ada-minute-book-095::multi-document-095::2: In document multi-ada-minute-book-095, the verified archive note records copper token. Case record...
  5. score=26.132513 chunk_id=21886 preview=document multi-lantern-tide-travel-note-095::multi-document-095::3: In document multi-lantern-tide-travel-note-095, the verified archive note records silver...
- Matched markers: copper token, silver booth token, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token, silver booth token, smoke vent chain.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 96 - multi-document-096
Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch?

Expected evidence:
- amber lantern
- tuning fork

Expected distractors:
- weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.263947 chunk_id=22319 preview=Question anchor: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-096. Scoped answ...
  2. score=46.197360 chunk_id=22320 preview=Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-096. Combined evidence:...
  3. score=26.309525 chunk_id=22001 preview=document multi-winter-chapel-porch-archive-096::multi-document-096::1: In document multi-winter-chapel-porch-archive-096, the verified archive note records a...
  4. score=4.245566 chunk_id=22000 preview=document multi-winter-chapel-porch-archive-036::multi-document-036::1: In document multi-winter-chapel-porch-archive-036, the verified archive note records l...
  5. score=4.193919 chunk_id=21972 preview=document multi-sonya-profile-page-036::multi-document-036::2: In document multi-sonya-profile-page-036, the verified archive note records birch tea flask. Ca...
- Matched markers: amber lantern, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.245780 chunk_id=22319 preview=Question anchor: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-096. Scoped answ...
  2. score=46.217507 chunk_id=22320 preview=Question: Which records together show how Sonya prepared the quarry lift stop near Winter Chapel porch? Case scope id: multi-document-096. Combined evidence:...
  3. score=26.272895 chunk_id=22001 preview=document multi-winter-chapel-porch-archive-096::multi-document-096::1: In document multi-winter-chapel-porch-archive-096, the verified archive note records a...
  4. score=26.112920 chunk_id=21973 preview=document multi-sonya-profile-page-096::multi-document-096::2: In document multi-sonya-profile-page-096, the verified archive note records tuning fork. Case r...
  5. score=13.657637 chunk_id=22160 preview=Question: Which records together show how Sonya prepared the quarry lift stop near Ridge Post loft? Case scope id: multi-document-016. Combined evidence: amb...
- Matched markers: amber lantern, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, tuning fork.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 2).

### Question 97 - multi-document-097
Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge?

Expected evidence:
- Harvest Glow
- cedar shovel
- willow basket

Expected distractors:
- juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.542542 chunk_id=22321 preview=Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document...
  2. score=18.153197 chunk_id=21854 preview=document multi-harvest-glow-family-register-017::multi-document-017::3: In document multi-harvest-glow-family-register-017, the verified archive note records...
  3. score=16.629521 chunk_id=21843 preview=document multi-fox-hollow-bridge-ledger-037::multi-document-037::1: In document multi-fox-hollow-bridge-ledger-037, the verified archive note records Harvest...
  4. score=16.106150 chunk_id=22161 preview=Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-...
  5. score=8.580126 chunk_id=21852 preview=document multi-harvest-glow-audio-transcript-037::multi-document-037::3: In document multi-harvest-glow-audio-transcript-037, the verified archive note recor...
- Matched markers: Harvest Glow, cedar shovel, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Harvest Glow, cedar shovel, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.475477 chunk_id=22321 preview=Question anchor: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document...
  2. score=58.490707 chunk_id=22322 preview=Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving Fox Hollow bridge? Case scope id: multi-document-097. C...
  3. score=26.477184 chunk_id=21844 preview=document multi-fox-hollow-bridge-ledger-097::multi-document-097::1: In document multi-fox-hollow-bridge-ledger-097, the verified archive note records Harvest...
  4. score=26.127465 chunk_id=22162 preview=Question: Which documents together identify the Harvest Glow memory that Runa preserved after leaving East Signal room? Case scope id: multi-document-017. Co...
  5. score=16.507428 chunk_id=21843 preview=document multi-fox-hollow-bridge-ledger-037::multi-document-037::1: In document multi-fox-hollow-bridge-ledger-037, the verified archive note records Harvest...
- Matched markers: Harvest Glow, cedar shovel, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Harvest Glow, cedar shovel, willow basket.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 98 - multi-document-098
Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well?

Expected evidence:
- violet ribbon
- star ledger page

Expected distractors:
- carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.357400 chunk_id=22323 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Case scope id: multi-document-09...
  2. score=26.365900 chunk_id=21999 preview=document multi-willow-courtyard-well-minute-book-098::multi-document-098::1: In document multi-willow-courtyard-well-minute-book-098, the verified archive no...
  3. score=4.365900 chunk_id=21998 preview=document multi-willow-courtyard-well-minute-book-038::multi-document-038::1: In document multi-willow-courtyard-well-minute-book-038, the verified archive no...
- Matched markers: star ledger page, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: star ledger page, violet ribbon.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.456365 chunk_id=22323 preview=Question anchor: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Case scope id: multi-document-09...
  2. score=46.416090 chunk_id=22324 preview=Question: Which archive pieces from more than one document explain the family profile event at Willow Courtyard well? Case scope id: multi-document-098. Comb...
  3. score=26.501963 chunk_id=21999 preview=document multi-willow-courtyard-well-minute-book-098::multi-document-098::1: In document multi-willow-courtyard-well-minute-book-098, the verified archive no...
  4. score=4.487569 chunk_id=21998 preview=document multi-willow-courtyard-well-minute-book-038::multi-document-038::1: In document multi-willow-courtyard-well-minute-book-038, the verified archive no...
  5. score=4.373460 chunk_id=21873 preview=document multi-iveta-travel-note-038::multi-document-038::2: In document multi-iveta-travel-note-038, the verified archive note records glass ink bottle. Cas...
- Matched markers: star ledger page, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: star ledger page, violet ribbon.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (2 vs 1).

### Question 99 - multi-document-099
Question: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay?

Expected evidence:
- blue oar
- silver booth token
- weathered camera strap

Expected distractors:
- canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.271782 chunk_id=22325 preview=Question anchor: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Case scope id: multi-document-099. Scoped a...
  2. score=58.292366 chunk_id=22326 preview=Question: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Case scope id: multi-document-099. Combined eviden...
  3. score=26.233861 chunk_id=21846 preview=document multi-glass-harbor-quay-profile-page-099::multi-document-099::1: In document multi-glass-harbor-quay-profile-page-099, the verified archive note rec...
  4. score=26.168605 chunk_id=22022 preview=document multi-zora-photo-index-099::multi-document-099::2: In document multi-zora-photo-index-099, the verified archive note records silver booth token. Cas...
  5. score=25.419275 chunk_id=22262 preview=Question: Which documents must be combined to understand Runa's archive card note about Fox Hollow bridge? Case scope id: multi-document-067. Combined eviden...
- Matched markers: blue oar, silver booth token, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=77.223032 chunk_id=22325 preview=Question anchor: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Case scope id: multi-document-099. Scoped a...
  2. score=58.175447 chunk_id=22326 preview=Question: Which documents must be combined to understand Zora's holiday card note about Glass Harbor quay? Case scope id: multi-document-099. Combined eviden...
  3. score=26.269886 chunk_id=21846 preview=document multi-glass-harbor-quay-profile-page-099::multi-document-099::1: In document multi-glass-harbor-quay-profile-page-099, the verified archive note rec...
  4. score=26.101227 chunk_id=22022 preview=document multi-zora-photo-index-099::multi-document-099::2: In document multi-zora-photo-index-099, the verified archive note records silver booth token. Cas...
  5. score=9.961411 chunk_id=22021 preview=document multi-zora-photo-index-039::multi-document-039::2: In document multi-zora-photo-index-039, the verified archive note records weathered camera strap....
- Matched markers: blue oar, silver booth token, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, silver booth token, weathered camera strap.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 100 - multi-document-100
Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed?

Expected evidence:
- linen wick
- birch tea flask

Expected distractors:
- coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.300109 chunk_id=22327 preview=Question anchor: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Case scope id: multi-document-100. Scoped answ...
  2. score=46.202052 chunk_id=22328 preview=Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Case scope id: multi-document-100. Combined evidence:...
  3. score=26.342820 chunk_id=21894 preview=document multi-mira-audio-transcript-100::multi-document-100::2: In document multi-mira-audio-transcript-100, the verified archive note records birch tea fla...
  4. score=26.150979 chunk_id=21822 preview=document multi-birch-ferry-shed-memory-log-100::multi-document-100::1: In document multi-birch-ferry-shed-memory-log-100, the verified archive note records l...
  5. score=14.244208 chunk_id=21895 preview=document multi-mira-family-register-020::multi-document-020::2: In document multi-mira-family-register-020, the verified archive note records birch tea flask...
- Matched markers: birch tea flask, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Top chunks:
  1. score=65.154227 chunk_id=22327 preview=Question anchor: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Case scope id: multi-document-100. Scoped answ...
  2. score=46.076200 chunk_id=22328 preview=Question: Which records together show how Mira prepared the overnight ferry stop near Birch Ferry shed? Case scope id: multi-document-100. Combined evidence:...
  3. score=26.134015 chunk_id=21822 preview=document multi-birch-ferry-shed-memory-log-100::multi-document-100::1: In document multi-birch-ferry-shed-memory-log-100, the verified archive note records l...
  4. score=26.056782 chunk_id=21894 preview=document multi-mira-audio-transcript-100::multi-document-100::2: In document multi-mira-audio-transcript-100, the verified archive note records birch tea fla...
  5. score=4.129512 chunk_id=21821 preview=document multi-birch-ferry-shed-memory-log-040::multi-document-040::1: In document multi-birch-ferry-shed-memory-log-040, the verified archive note records p...
- Matched markers: birch tea flask, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, linen wick.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Aggregate Results

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Question wins: 54
- Passed questions: 91
- Average evidence coverage: 0.945
- Average first relevant rank: 1.0
- Total matched markers: 237
- Total missing markers: 11
- Total false-positive markers: 0
- Official metrics: {'hit_rate': 0.46, 'recall_at_k': 0.69, 'mrr': 0.8, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 26.913240000000002, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.69, 'missing_expected_marker_count': 73, 'false_positive_count': 73}

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777`
- Question wins: 46
- Passed questions: 96
- Average evidence coverage: 0.985
- Average first relevant rank: 1.0
- Total matched markers: 245
- Total missing markers: 3
- Total false-positive markers: 0
- Official metrics: {'hit_rate': 0.5, 'recall_at_k': 0.8183333333333332, 'mrr': 0.865, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 33.82396, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.8183333333333332, 'missing_expected_marker_count': 45, 'false_positive_count': 54}

### Runtime Activation
- Selected config: {'best_config_id': 'bge_m3', 'best_model_code': 'bge_m3', 'best_collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777', 'selected_metrics': {'hit_rate': 0.5, 'recall_at_k': 0.8183333333333332, 'mrr': 0.865, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 33.82396, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.8183333333333332, 'missing_expected_marker_count': 45, 'false_positive_count': 54}}
- Activated config: {'id': 2, 'profile_id': 6, 'model_code': 'bge_m3', 'collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777', 'top_k': 5, 'score_threshold': None, 'retrieval_mode': 'hybrid', 'source_eval_job_id': 152, 'source_eval_dataset_id': 'eternal-world-multi-document-v1'}
- Runtime retrieval verification: {'model_code': 'bge_m3', 'result_count': 2, 'qdrant_collection': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_multi_document_v1__f33c459777', 'top_chunk_id': 22129}
