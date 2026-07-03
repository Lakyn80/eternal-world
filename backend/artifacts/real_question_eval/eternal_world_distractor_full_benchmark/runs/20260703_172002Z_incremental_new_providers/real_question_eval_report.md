# Real Question Evaluation Report

## Client Summary
- Source dataset: deterministic fictional eval corpus
- Real client/user data: no
- Purpose: retrieval quality testing
- Models compared:
  - `multilingual_e5_small`
  - `bge_m3`
  - `paraphrase_multilingual_mpnet_base_v2`
  - `multilingual_e5_base`
- Recommended active model: `bge_m3`
- Speed vs accuracy tradeoff: Historical multilingual_e5_small and bge_m3 results were preserved and compared against the two new real-provider runs using the same dataset and selector rules.
- Production recommendation: No new provider beat historical `bge_m3`; keep `bge_m3` as the production recommendation.
- Timestamp: 2026-07-03T17:20:02.971494+00:00
- Run status: `COMPLETED`
- Quality status: `FAIL`
- Quality gate: `n/a`
- Preflight validation: `n/a`
- Preflight missing marker count: `n/a`
- Run type: `incremental_real`
- Historical baseline providers:
  - `multilingual_e5_small`
  - `bge_m3`
- New real run providers:
  - `paraphrase_multilingual_mpnet_base_v2`
  - `multilingual_e5_base`
- Historical overall winner: `bge_m3`
- Any new provider beat historical bge_m3: `false`

## Artifact Files
- Latest Markdown: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/latest_incremental_new_providers/real_question_eval_report.md`
- Latest JSON: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/latest_incremental_new_providers/real_question_eval_result.json`
- Latest Summary Markdown: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/latest_incremental_new_providers/real_question_eval_summary.md`
- Latest Summary JSON: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/latest_incremental_new_providers/real_question_eval_summary.json`
- Archived Markdown: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/runs/20260703_172002Z_incremental_new_providers/real_question_eval_report.md`
- Archived JSON: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/runs/20260703_172002Z_incremental_new_providers/real_question_eval_result.json`
- Archived Summary Markdown: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/runs/20260703_172002Z_incremental_new_providers/real_question_eval_summary.md`
- Archived Summary JSON: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/runs/20260703_172002Z_incremental_new_providers/real_question_eval_summary.json`

## Client Question Breakdown
### Question 1 - distractor-twin-innkeepers
Question: Which Marta kept the North Inn ledger, and what detail identified her apron?
- Final evaluated answer: Grounded by retrieved evidence for: Marta of North Inn, green apron.
- Correctness verdict: grounded
- Evidence used: Marta of North Inn, green apron
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=partial coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `paraphrase_multilingual_mpnet_base_v2`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Marta of River Inn; bge_m3 distractors Marta of River Inn
- Distractors / false positives: Marta of River Inn, Marta of River Inn

Expected evidence:
- Marta of North Inn
- green apron

Expected distractors:
- Marta of River Inn

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Marta of North Inn, green apron missing=none distractors=Marta of River Inn
  - `bge_m3`: verdict=partial coverage=1.0 matched=Marta of North Inn, green apron missing=none distractors=Marta of River Inn
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Marta of North Inn, green apron missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Marta of North Inn, green apron missing=none distractors=none

### Question 2 - distractor-june-market-date
Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice?
- Final evaluated answer: Grounded by retrieved evidence for: Bell Bridge square, June 14 night market.
- Correctness verdict: grounded
- Evidence used: Bell Bridge square, June 14 night market
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=partial coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors June 4 noon market; bge_m3 distractors June 4 noon market
- Distractors / false positives: June 4 noon market, June 4 noon market

Expected evidence:
- June 14 night market
- Bell Bridge square

Expected distractors:
- June 4 noon market

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Bell Bridge square, June 14 night market missing=none distractors=June 4 noon market
  - `bge_m3`: verdict=partial coverage=1.0 matched=Bell Bridge square, June 14 night market missing=none distractors=June 4 noon market
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Bell Bridge square, June 14 night market missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Bell Bridge square, June 14 night market missing=none distractors=none

### Question 3 - distractor-two-levs
Question: Which Lev repaired the oak barrels, not the one who worked by the ferry?
- Final evaluated answer: Grounded by retrieved evidence for: Lev the cooper, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Lev the cooper, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=partial coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `paraphrase_multilingual_mpnet_base_v2`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Lev the ferryman; bge_m3 distractors Lev the ferryman
- Distractors / false positives: Lev the ferryman, Lev the ferryman

Expected evidence:
- Lev the cooper
- oak barrel hoops

Expected distractors:
- Lev the ferryman

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Lev the cooper, oak barrel hoops missing=none distractors=Lev the ferryman
  - `bge_m3`: verdict=partial coverage=1.0 matched=Lev the cooper, oak barrel hoops missing=none distractors=Lev the ferryman
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Lev the cooper, oak barrel hoops missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Lev the cooper, oak barrel hoops missing=none distractors=none

### Question 4 - distractor-similar-islands
Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Fog Island ferry shed, painted blue oar.
- Correctness verdict: grounded
- Evidence used: Fog Island ferry shed, painted blue oar
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: bge_m3 distractors Fox Island ferry shed
- Distractors / false positives: Fox Island ferry shed

Expected evidence:
- Fog Island ferry shed
- painted blue oar

Expected distractors:
- Fox Island ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Fog Island ferry shed, painted blue oar missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=Fog Island ferry shed, painted blue oar missing=none distractors=Fox Island ferry shed
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Fog Island ferry shed, painted blue oar missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Fog Island ferry shed, painted blue oar missing=none distractors=none

### Question 5 - distractor-letter-mixup
Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season?
- Final evaluated answer: Grounded by retrieved evidence for: Ada's winter letter, violet wax thread.
- Correctness verdict: grounded
- Evidence used: Ada's winter letter, violet wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Ada's winter letter
- violet wax thread

Expected distractors:
- Alda's spring letter

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Ada's winter letter, violet wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Ada's winter letter, violet wax thread missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Ada's winter letter, violet wax thread missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Ada's winter letter, violet wax thread missing=none distractors=none

### Question 6 - distractor-006
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 16 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 16 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=0.5; multilingual_e5_base -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: paraphrase_multilingual_mpnet_base_v2 missing March 16 Bellwater Fair; multilingual_e5_base missing March 16 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 16 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 17 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=March 16 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=March 16 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 16 Bellwater Fair distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 16 Bellwater Fair distractors=none

### Question 7 - distractor-007
Question: Which place held the true profile detail for Nikola, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, brass compass.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, brass compass
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=partial coverage=1.0
- Winner: `bge_m3`
- Why it won: Earlier first relevant chunk (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Blue Trunk cabin
- brass compass

Expected distractors:
- East Signal room

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, brass compass missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, brass compass missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, brass compass missing=none distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=1.0 matched=Blue Trunk cabin, brass compass missing=none distractors=none

### Question 8 - distractor-008
Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Sonya of North Orchard lane, linen wick.
- Correctness verdict: grounded
- Evidence used: Sonya of North Orchard lane, linen wick
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- Sonya of North Orchard lane

Expected distractors:
- tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Sonya of North Orchard lane, linen wick missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Sonya of North Orchard lane, linen wick missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Sonya of North Orchard lane, linen wick missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Sonya of North Orchard lane, linen wick missing=none distractors=none

### Question 9 - distractor-009
Question: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, star ledger page.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, star ledger page
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- star ledger page

Expected distractors:
- Bridgefire Supper at South Meadow arch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, star ledger page missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, star ledger page missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, star ledger page missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, star ledger page missing=none distractors=none

### Question 10 - distractor-010
Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir?
- Final evaluated answer: Grounded by retrieved evidence for: Selma of Birch Ferry shed, lantern hook.
- Correctness verdict: grounded
- Evidence used: Selma of Birch Ferry shed, lantern hook
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Damir of Birch Ferry shed
- Distractors / false positives: Damir of Birch Ferry shed

Expected evidence:
- Selma of Birch Ferry shed
- lantern hook

Expected distractors:
- Damir of Birch Ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Selma of Birch Ferry shed, lantern hook missing=none distractors=Damir of Birch Ferry shed
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Selma of Birch Ferry shed, lantern hook missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Selma of Birch Ferry shed, lantern hook missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Selma of Birch Ferry shed, lantern hook missing=none distractors=none

### Question 11 - distractor-011
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 21 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 21 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=0.5; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small missing March 21 Bellwater Fair; paraphrase_multilingual_mpnet_base_v2 missing March 21 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 21 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 22 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=Lantern Row kiosk missing=March 21 Bellwater Fair distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 21 Bellwater Fair missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=0.5 matched=Lantern Row kiosk missing=March 21 Bellwater Fair distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 21 Bellwater Fair missing=none distractors=none

### Question 12 - distractor-012
Question: Which place held the true profile detail for Zora, not the nearly identical place name?
- Final evaluated answer: Partially grounded by: Cloud Wharf office, wax thread.
- Correctness verdict: partial
- Evidence used: Cloud Wharf office, wax thread
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=partial coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=no_evidence coverage=0.0; multilingual_e5_base -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Earlier first relevant chunk (2 vs 5).
- What the losing model missed or got wrong: paraphrase_multilingual_mpnet_base_v2 missing Cloud Wharf office, wax thread
- Distractors / false positives: none

Expected evidence:
- Cloud Wharf office
- wax thread

Expected distractors:
- Fox Hollow bridge

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Cloud Wharf office, wax thread missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=Cloud Wharf office, wax thread missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=no_evidence coverage=0.0 matched=none missing=Cloud Wharf office, wax thread distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=1.0 matched=Cloud Wharf office, wax thread missing=none distractors=none

### Question 13 - distractor-013
Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vesna of Ridge Post loft, tin key.
- Correctness verdict: grounded
- Evidence used: Vesna of Ridge Post loft, tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- tin key
- Vesna of Ridge Post loft

Expected distractors:
- cedar shovel

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Vesna of Ridge Post loft, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Vesna of Ridge Post loft, tin key missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Vesna of Ridge Post loft, tin key missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Vesna of Ridge Post loft, tin key missing=none distractors=none

### Question 14 - distractor-014
Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, blue oar.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, blue oar
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at Willow Courtyard well
- blue oar

Expected distractors:
- Bridgefire Supper at Willow Courtyard well

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, blue oar missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, blue oar missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, blue oar missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, blue oar missing=none distractors=none

### Question 15 - distractor-015
Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira?
- Final evaluated answer: Grounded by retrieved evidence for: Ilya of Bell Bridge square, willow basket.
- Correctness verdict: grounded
- Evidence used: Ilya of Bell Bridge square, willow basket
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Kira of Bell Bridge square
- Distractors / false positives: Kira of Bell Bridge square

Expected evidence:
- Ilya of Bell Bridge square
- willow basket

Expected distractors:
- Kira of Bell Bridge square

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Ilya of Bell Bridge square, willow basket missing=none distractors=Kira of Bell Bridge square
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Ilya of Bell Bridge square, willow basket missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Ilya of Bell Bridge square, willow basket missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Ilya of Bell Bridge square, willow basket missing=none distractors=none

### Question 16 - distractor-016
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 26 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 26 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- March 26 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 27 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 26 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 26 Bellwater Fair missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 26 Bellwater Fair missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 26 Bellwater Fair missing=none distractors=none

### Question 17 - distractor-017
Question: Which place held the true profile detail for Boris, not the nearly identical place name?
- Final evaluated answer: Partially grounded by: Moon Mill yard, glass ink bottle.
- Correctness verdict: partial
- Evidence used: Moon Mill yard, glass ink bottle
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=no_evidence coverage=0.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=no_evidence coverage=0.0; multilingual_e5_base -> verdict=no_evidence coverage=0.0
- Winner: `multilingual_e5_small`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: bge_m3 missing Moon Mill yard, glass ink bottle; paraphrase_multilingual_mpnet_base_v2 missing Moon Mill yard, glass ink bottle; multilingual_e5_base missing Moon Mill yard, glass ink bottle
- Distractors / false positives: none

Expected evidence:
- Moon Mill yard
- glass ink bottle

Expected distractors:
- Hollow Market arcade

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Moon Mill yard, glass ink bottle missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, glass ink bottle distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, glass ink bottle distractors=none
  - `multilingual_e5_base`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, glass ink bottle distractors=none

### Question 18 - distractor-018
Question: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Daria of Winter Chapel porch, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Daria of Winter Chapel porch, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- copper wind vane pin
- Daria of Winter Chapel porch

Expected distractors:
- carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Daria of Winter Chapel porch, copper wind vane pin missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Daria of Winter Chapel porch, copper wind vane pin missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Daria of Winter Chapel porch, copper wind vane pin missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Daria of Winter Chapel porch, copper wind vane pin missing=none distractors=none

### Question 19 - distractor-019
Question: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, coal stove hiss.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, coal stove hiss
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at Marble stair hall
- coal stove hiss

Expected distractors:
- Bridgefire Supper at Marble stair hall

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, coal stove hiss missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, coal stove hiss missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, coal stove hiss missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, coal stove hiss missing=none distractors=none

### Question 20 - distractor-020
Question: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola?
- Final evaluated answer: Grounded by retrieved evidence for: Ada of Star Basin gallery, violet ribbon.
- Correctness verdict: grounded
- Evidence used: Ada of Star Basin gallery, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Nikola of Star Basin gallery
- Distractors / false positives: Nikola of Star Basin gallery

Expected evidence:
- Ada of Star Basin gallery
- violet ribbon

Expected distractors:
- Nikola of Star Basin gallery

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Ada of Star Basin gallery, violet ribbon missing=none distractors=Nikola of Star Basin gallery
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Ada of Star Basin gallery, violet ribbon missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Ada of Star Basin gallery, violet ribbon missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Ada of Star Basin gallery, violet ribbon missing=none distractors=none

### Question 21 - distractor-021
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 13 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 13 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=0.5; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small missing March 13 Bellwater Fair; paraphrase_multilingual_mpnet_base_v2 missing March 13 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 13 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 14 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 13 Bellwater Fair distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=March 13 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 13 Bellwater Fair distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=March 13 Bellwater Fair, North Bell workshop missing=none distractors=none

### Question 22 - distractor-022
Question: Which place held the true profile detail for Talia, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, rope bridge permit
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=partial coverage=1.0
- Winner: `bge_m3`
- Why it won: Earlier first relevant chunk (2 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Blue Trunk cabin
- rope bridge permit

Expected distractors:
- East Signal room

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Blue Trunk cabin, rope bridge permit missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, rope bridge permit missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, rope bridge permit missing=none distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=1.0 matched=Blue Trunk cabin, rope bridge permit missing=none distractors=none

### Question 23 - distractor-023
Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Viktor of North Orchard lane, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Viktor of North Orchard lane, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: bge_m3 distractors clay watering cup
- Distractors / false positives: clay watering cup

Expected evidence:
- oak barrel hoops
- Viktor of North Orchard lane

Expected distractors:
- clay watering cup

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Viktor of North Orchard lane, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=Viktor of North Orchard lane, oak barrel hoops missing=none distractors=clay watering cup
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Viktor of North Orchard lane, oak barrel hoops missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Viktor of North Orchard lane, oak barrel hoops missing=none distractors=none

### Question 24 - distractor-024
Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, blue glass jar.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, blue glass jar
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- blue glass jar

Expected distractors:
- Bridgefire Supper at South Meadow arch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, blue glass jar missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, blue glass jar missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, blue glass jar missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, blue glass jar missing=none distractors=none

### Question 25 - distractor-025
Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora?
- Final evaluated answer: Grounded by retrieved evidence for: Anton of Birch Ferry shed, canal route map.
- Correctness verdict: grounded
- Evidence used: Anton of Birch Ferry shed, canal route map
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Zora of Birch Ferry shed
- Distractors / false positives: Zora of Birch Ferry shed

Expected evidence:
- Anton of Birch Ferry shed
- canal route map

Expected distractors:
- Zora of Birch Ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Anton of Birch Ferry shed, canal route map missing=none distractors=Zora of Birch Ferry shed
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Anton of Birch Ferry shed, canal route map missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Anton of Birch Ferry shed, canal route map missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Anton of Birch Ferry shed, canal route map missing=none distractors=none

### Question 26 - distractor-026
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 18 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 18 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=0.5; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=0.5; multilingual_e5_base -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_small`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: bge_m3 missing March 18 Bellwater Fair; paraphrase_multilingual_mpnet_base_v2 missing March 18 Bellwater Fair; multilingual_e5_base missing March 18 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 18 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 19 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 18 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=0.5 matched=Lantern Row kiosk missing=March 18 Bellwater Fair distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=0.5 matched=Lantern Row kiosk missing=March 18 Bellwater Fair distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=0.5 matched=Lantern Row kiosk missing=March 18 Bellwater Fair distractors=none

### Question 27 - distractor-027
Question: Which place held the true profile detail for Tomas, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, copper token.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, copper token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=no_evidence coverage=0.0; multilingual_e5_base -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Earlier first relevant chunk (1 vs 3).
- What the losing model missed or got wrong: paraphrase_multilingual_mpnet_base_v2 missing Cloud Wharf office, copper token
- Distractors / false positives: none

Expected evidence:
- Cloud Wharf office
- copper token

Expected distractors:
- Fox Hollow bridge

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, copper token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, copper token missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=no_evidence coverage=0.0 matched=none missing=Cloud Wharf office, copper token distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=1.0 matched=Cloud Wharf office, copper token missing=none distractors=none

### Question 28 - distractor-028
Question: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vera of Ridge Post loft, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: Vera of Ridge Post loft, moonflower cutting
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- Vera of Ridge Post loft

Expected distractors:
- star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Vera of Ridge Post loft, moonflower cutting missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Vera of Ridge Post loft, moonflower cutting missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Vera of Ridge Post loft, moonflower cutting missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Vera of Ridge Post loft, moonflower cutting missing=none distractors=none

### Question 29 - distractor-029
Question: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, birch tea flask.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, birch tea flask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at Willow Courtyard well
- birch tea flask

Expected distractors:
- Bridgefire Supper at Willow Courtyard well

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, birch tea flask missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, birch tea flask missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, birch tea flask missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, birch tea flask missing=none distractors=none

### Question 30 - distractor-030
Question: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris?
- Final evaluated answer: Grounded by retrieved evidence for: Lina of Bell Bridge square, saffron scarf.
- Correctness verdict: grounded
- Evidence used: Lina of Bell Bridge square, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Boris of Bell Bridge square
- Distractors / false positives: Boris of Bell Bridge square

Expected evidence:
- Lina of Bell Bridge square
- saffron scarf

Expected distractors:
- Boris of Bell Bridge square

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Lina of Bell Bridge square, saffron scarf missing=none distractors=Boris of Bell Bridge square
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lina of Bell Bridge square, saffron scarf missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Lina of Bell Bridge square, saffron scarf missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Lina of Bell Bridge square, saffron scarf missing=none distractors=none

### Question 31 - distractor-031
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 23 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 23 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=0.5; multilingual_e5_base -> verdict=partial coverage=0.5
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing March 23 Bellwater Fair; paraphrase_multilingual_mpnet_base_v2 missing March 23 Bellwater Fair; multilingual_e5_base missing March 23 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 23 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 24 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=Cedar Hill station missing=March 23 Bellwater Fair distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 23 Bellwater Fair missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=0.5 matched=Cedar Hill station missing=March 23 Bellwater Fair distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=0.5 matched=Cedar Hill station missing=March 23 Bellwater Fair distractors=none

### Question 32 - distractor-032
Question: Which place held the true profile detail for Yara, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Moon Mill yard, amber lantern.
- Correctness verdict: grounded
- Evidence used: Moon Mill yard, amber lantern
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Moon Mill yard
- amber lantern

Expected distractors:
- Hollow Market arcade

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Moon Mill yard, amber lantern missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Moon Mill yard, amber lantern missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Moon Mill yard, amber lantern missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Moon Mill yard, amber lantern missing=none distractors=none

### Question 33 - distractor-033
Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Lev of Winter Chapel porch, basalt sketch.
- Correctness verdict: grounded
- Evidence used: Lev of Winter Chapel porch, basalt sketch
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- basalt sketch
- Lev of Winter Chapel porch

Expected distractors:
- blue oar

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lev of Winter Chapel porch, basalt sketch missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lev of Winter Chapel porch, basalt sketch missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Lev of Winter Chapel porch, basalt sketch missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Lev of Winter Chapel porch, basalt sketch missing=none distractors=none

### Question 34 - distractor-034
Question: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, green apron.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, green apron
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at Marble stair hall
- green apron

Expected distractors:
- Bridgefire Supper at Marble stair hall

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, green apron missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, green apron missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, green apron missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, green apron missing=none distractors=none

### Question 35 - distractor-035
Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia?
- Final evaluated answer: Grounded by retrieved evidence for: Pavel of Star Basin gallery, silver booth token.
- Correctness verdict: grounded
- Evidence used: Pavel of Star Basin gallery, silver booth token
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Talia of Star Basin gallery
- Distractors / false positives: Talia of Star Basin gallery

Expected evidence:
- Pavel of Star Basin gallery
- silver booth token

Expected distractors:
- Talia of Star Basin gallery

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Pavel of Star Basin gallery, silver booth token missing=none distractors=Talia of Star Basin gallery
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Pavel of Star Basin gallery, silver booth token missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Pavel of Star Basin gallery, silver booth token missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Pavel of Star Basin gallery, silver booth token missing=none distractors=none

### Question 36 - distractor-036
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 10 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 10 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=0.5; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=0.5; multilingual_e5_base -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_small`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: bge_m3 missing March 10 Bellwater Fair; paraphrase_multilingual_mpnet_base_v2 missing March 10 Bellwater Fair; multilingual_e5_base missing March 10 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 10 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 11 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=March 10 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 10 Bellwater Fair distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 10 Bellwater Fair distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 10 Bellwater Fair distractors=none

### Question 37 - distractor-037
Question: Which place held the true profile detail for Damir, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, juniper bundles.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, juniper bundles
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=1.0; multilingual_e5_base -> verdict=partial coverage=1.0
- Winner: `bge_m3`
- Why it won: Earlier first relevant chunk (2 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Blue Trunk cabin
- juniper bundles

Expected distractors:
- East Signal room

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, juniper bundles missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, juniper bundles missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=1.0 matched=Blue Trunk cabin, juniper bundles missing=none distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=1.0 matched=Blue Trunk cabin, juniper bundles missing=none distractors=none

### Question 38 - distractor-038
Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Nessa of North Orchard lane, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: Nessa of North Orchard lane, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- smoke vent chain
- Nessa of North Orchard lane

Expected distractors:
- coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Nessa of North Orchard lane, smoke vent chain missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Nessa of North Orchard lane, smoke vent chain missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Nessa of North Orchard lane, smoke vent chain missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Nessa of North Orchard lane, smoke vent chain missing=none distractors=none

### Question 39 - distractor-039
Question: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, brass compass.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, brass compass
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- brass compass

Expected distractors:
- Bridgefire Supper at South Meadow arch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, brass compass missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, brass compass missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, brass compass missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, brass compass missing=none distractors=none

### Question 40 - distractor-040
Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas?
- Final evaluated answer: Grounded by retrieved evidence for: Mira of Birch Ferry shed, linen wick.
- Correctness verdict: grounded
- Evidence used: Mira of Birch Ferry shed, linen wick
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Tomas of Birch Ferry shed
- Distractors / false positives: Tomas of Birch Ferry shed

Expected evidence:
- Mira of Birch Ferry shed
- linen wick

Expected distractors:
- Tomas of Birch Ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Mira of Birch Ferry shed, linen wick missing=none distractors=Tomas of Birch Ferry shed
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Mira of Birch Ferry shed, linen wick missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Mira of Birch Ferry shed, linen wick missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Mira of Birch Ferry shed, linen wick missing=none distractors=none

### Question 41 - distractor-041
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 15 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 15 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=0.5; multilingual_e5_base -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: paraphrase_multilingual_mpnet_base_v2 missing March 15 Bellwater Fair; multilingual_e5_base missing March 15 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 15 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 16 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 15 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 15 Bellwater Fair missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=0.5 matched=Lantern Row kiosk missing=March 15 Bellwater Fair distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=0.5 matched=Lantern Row kiosk missing=March 15 Bellwater Fair distractors=none

### Question 42 - distractor-042
Question: Which place held the true profile detail for Kira, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, lantern hook.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=1.0; multilingual_e5_base -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Earlier first relevant chunk (2 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Cloud Wharf office
- lantern hook

Expected distractors:
- Fox Hollow bridge

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, lantern hook missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=1.0 matched=Cloud Wharf office, lantern hook missing=none distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=1.0 matched=Cloud Wharf office, lantern hook missing=none distractors=none

### Question 43 - distractor-043
Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Petar of Ridge Post loft, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: Petar of Ridge Post loft, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors blue glass jar
- Distractors / false positives: blue glass jar

Expected evidence:
- weathered camera strap
- Petar of Ridge Post loft

Expected distractors:
- blue glass jar

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Petar of Ridge Post loft, weathered camera strap missing=none distractors=blue glass jar
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Petar of Ridge Post loft, weathered camera strap missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Petar of Ridge Post loft, weathered camera strap missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Petar of Ridge Post loft, weathered camera strap missing=none distractors=none

### Question 44 - distractor-044
Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, wax thread.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at Willow Courtyard well
- wax thread

Expected distractors:
- Bridgefire Supper at Willow Courtyard well

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, wax thread missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, wax thread missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, wax thread missing=none distractors=none

### Question 45 - distractor-045
Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara?
- Final evaluated answer: Grounded by retrieved evidence for: Stefan of Bell Bridge square, tin key.
- Correctness verdict: grounded
- Evidence used: Stefan of Bell Bridge square, tin key
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Yara of Bell Bridge square
- Distractors / false positives: Yara of Bell Bridge square

Expected evidence:
- Stefan of Bell Bridge square
- tin key

Expected distractors:
- Yara of Bell Bridge square

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Stefan of Bell Bridge square, tin key missing=none distractors=Yara of Bell Bridge square
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Stefan of Bell Bridge square, tin key missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Stefan of Bell Bridge square, tin key missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Stefan of Bell Bridge square, tin key missing=none distractors=none

### Question 46 - distractor-046
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 20 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 20 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=0.5; multilingual_e5_base -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: paraphrase_multilingual_mpnet_base_v2 missing March 20 Bellwater Fair; multilingual_e5_base missing March 20 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 20 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 21 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 20 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 20 Bellwater Fair missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=0.5 matched=Cedar Hill station missing=March 20 Bellwater Fair distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=0.5 matched=Cedar Hill station missing=March 20 Bellwater Fair distractors=none

### Question 47 - distractor-047
Question: Which place held the true profile detail for Nikola, not the nearly identical place name?
- Final evaluated answer: Partially grounded by: Moon Mill yard, willow basket.
- Correctness verdict: partial
- Evidence used: Moon Mill yard, willow basket
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=partial coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=1.0; multilingual_e5_base -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Earlier first relevant chunk (1 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Moon Mill yard
- willow basket

Expected distractors:
- Hollow Market arcade

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Moon Mill yard, willow basket missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=Moon Mill yard, willow basket missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=1.0 matched=Moon Mill yard, willow basket missing=none distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=1.0 matched=Moon Mill yard, willow basket missing=none distractors=none

### Question 48 - distractor-048
Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Sonya of Winter Chapel porch, paper moon mask.
- Correctness verdict: grounded
- Evidence used: Sonya of Winter Chapel porch, paper moon mask
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors birch tea flask
- Distractors / false positives: birch tea flask

Expected evidence:
- paper moon mask
- Sonya of Winter Chapel porch

Expected distractors:
- birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Sonya of Winter Chapel porch, paper moon mask missing=none distractors=birch tea flask
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Sonya of Winter Chapel porch, paper moon mask missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Sonya of Winter Chapel porch, paper moon mask missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Sonya of Winter Chapel porch, paper moon mask missing=none distractors=none

### Question 49 - distractor-049
Question: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, glass ink bottle.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, glass ink bottle
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at Marble stair hall
- glass ink bottle

Expected distractors:
- Bridgefire Supper at Marble stair hall

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, glass ink bottle missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, glass ink bottle missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, glass ink bottle missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, glass ink bottle missing=none distractors=none

### Question 50 - distractor-050
Question: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir?
- Final evaluated answer: Grounded by retrieved evidence for: Selma of Star Basin gallery, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Selma of Star Basin gallery, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Damir of Star Basin gallery
- Distractors / false positives: Damir of Star Basin gallery

Expected evidence:
- Selma of Star Basin gallery
- copper wind vane pin

Expected distractors:
- Damir of Star Basin gallery

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Selma of Star Basin gallery, copper wind vane pin missing=none distractors=Damir of Star Basin gallery
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Selma of Star Basin gallery, copper wind vane pin missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Selma of Star Basin gallery, copper wind vane pin missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Selma of Star Basin gallery, copper wind vane pin missing=none distractors=none

### Question 51 - distractor-051
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 25 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 25 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small missing March 25 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 25 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 26 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 25 Bellwater Fair distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=March 25 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=March 25 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=March 25 Bellwater Fair, North Bell workshop missing=none distractors=none

### Question 52 - distractor-052
Question: Which place held the true profile detail for Zora, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, violet ribbon.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=no_evidence coverage=0.0
- Winner: `bge_m3`
- Why it won: Earlier first relevant chunk (1 vs 3).
- What the losing model missed or got wrong: multilingual_e5_base missing Blue Trunk cabin, violet ribbon
- Distractors / false positives: none

Expected evidence:
- Blue Trunk cabin
- violet ribbon

Expected distractors:
- East Signal room

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, violet ribbon missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, violet ribbon missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, violet ribbon missing=none distractors=none
  - `multilingual_e5_base`: verdict=no_evidence coverage=0.0 matched=none missing=Blue Trunk cabin, violet ribbon distractors=none

### Question 53 - distractor-053
Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vesna of North Orchard lane, tuning fork.
- Correctness verdict: grounded
- Evidence used: Vesna of North Orchard lane, tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- tuning fork
- Vesna of North Orchard lane

Expected distractors:
- green apron

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Vesna of North Orchard lane, tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Vesna of North Orchard lane, tuning fork missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Vesna of North Orchard lane, tuning fork missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Vesna of North Orchard lane, tuning fork missing=none distractors=none

### Question 54 - distractor-054
Question: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, rope bridge permit
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- rope bridge permit

Expected distractors:
- Bridgefire Supper at South Meadow arch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, rope bridge permit missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, rope bridge permit missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, rope bridge permit missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, rope bridge permit missing=none distractors=none

### Question 55 - distractor-055
Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira?
- Final evaluated answer: Grounded by retrieved evidence for: Ilya of Birch Ferry shed, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Ilya of Birch Ferry shed, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Kira of Birch Ferry shed
- Distractors / false positives: Kira of Birch Ferry shed

Expected evidence:
- Ilya of Birch Ferry shed
- oak barrel hoops

Expected distractors:
- Kira of Birch Ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Ilya of Birch Ferry shed, oak barrel hoops missing=none distractors=Kira of Birch Ferry shed
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Ilya of Birch Ferry shed, oak barrel hoops missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Ilya of Birch Ferry shed, oak barrel hoops missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Ilya of Birch Ferry shed, oak barrel hoops missing=none distractors=none

### Question 56 - distractor-056
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 12 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 12 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=0.5; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=0.5; multilingual_e5_base -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_small`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: bge_m3 missing March 12 Bellwater Fair; paraphrase_multilingual_mpnet_base_v2 missing March 12 Bellwater Fair; multilingual_e5_base missing March 12 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 12 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 13 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 12 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=0.5 matched=Lantern Row kiosk missing=March 12 Bellwater Fair distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=0.5 matched=Lantern Row kiosk missing=March 12 Bellwater Fair distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=0.5 matched=Lantern Row kiosk missing=March 12 Bellwater Fair distractors=none

### Question 57 - distractor-057
Question: Which place held the true profile detail for Boris, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, canal route map.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, canal route map
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=no_evidence coverage=0.0; multilingual_e5_base -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Earlier first relevant chunk (2 vs 3).
- What the losing model missed or got wrong: paraphrase_multilingual_mpnet_base_v2 missing Cloud Wharf office, canal route map
- Distractors / false positives: none

Expected evidence:
- Cloud Wharf office
- canal route map

Expected distractors:
- Fox Hollow bridge

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, canal route map missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, canal route map missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=no_evidence coverage=0.0 matched=none missing=Cloud Wharf office, canal route map distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=1.0 matched=Cloud Wharf office, canal route map missing=none distractors=none

### Question 58 - distractor-058
Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Daria of Ridge Post loft, cedar shovel.
- Correctness verdict: grounded
- Evidence used: Daria of Ridge Post loft, cedar shovel
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- cedar shovel
- Daria of Ridge Post loft

Expected distractors:
- brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Daria of Ridge Post loft, cedar shovel missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Daria of Ridge Post loft, cedar shovel missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Daria of Ridge Post loft, cedar shovel missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Daria of Ridge Post loft, cedar shovel missing=none distractors=none

### Question 59 - distractor-059
Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, copper token.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, copper token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at Willow Courtyard well
- copper token

Expected distractors:
- Bridgefire Supper at Willow Courtyard well

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, copper token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, copper token missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, copper token missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, copper token missing=none distractors=none

### Question 60 - distractor-060
Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola?
- Final evaluated answer: Grounded by retrieved evidence for: Ada of Bell Bridge square, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: Ada of Bell Bridge square, moonflower cutting
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Nikola of Bell Bridge square
- Distractors / false positives: Nikola of Bell Bridge square

Expected evidence:
- Ada of Bell Bridge square
- moonflower cutting

Expected distractors:
- Nikola of Bell Bridge square

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Ada of Bell Bridge square, moonflower cutting missing=none distractors=Nikola of Bell Bridge square
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Ada of Bell Bridge square, moonflower cutting missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Ada of Bell Bridge square, moonflower cutting missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Ada of Bell Bridge square, moonflower cutting missing=none distractors=none

### Question 61 - distractor-061
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 17 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 17 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=0.5; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: paraphrase_multilingual_mpnet_base_v2 missing March 17 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 17 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 18 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 17 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 17 Bellwater Fair missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=0.5 matched=Cedar Hill station missing=March 17 Bellwater Fair distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 17 Bellwater Fair missing=none distractors=none

### Question 62 - distractor-062
Question: Which place held the true profile detail for Talia, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Moon Mill yard, saffron scarf.
- Correctness verdict: grounded
- Evidence used: Moon Mill yard, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=no_evidence coverage=0.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: paraphrase_multilingual_mpnet_base_v2 missing Moon Mill yard, saffron scarf
- Distractors / false positives: none

Expected evidence:
- Moon Mill yard
- saffron scarf

Expected distractors:
- Hollow Market arcade

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Moon Mill yard, saffron scarf missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Moon Mill yard, saffron scarf missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, saffron scarf distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Moon Mill yard, saffron scarf missing=none distractors=none

### Question 63 - distractor-063
Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Viktor of Winter Chapel porch, carved shell comb.
- Correctness verdict: grounded
- Evidence used: Viktor of Winter Chapel porch, carved shell comb
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- carved shell comb
- Viktor of Winter Chapel porch

Expected distractors:
- wax thread

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Viktor of Winter Chapel porch, carved shell comb missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Viktor of Winter Chapel porch, carved shell comb missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Viktor of Winter Chapel porch, carved shell comb missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Viktor of Winter Chapel porch, carved shell comb missing=none distractors=none

### Question 64 - distractor-064
Question: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, amber lantern.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, amber lantern
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at Marble stair hall
- amber lantern

Expected distractors:
- Bridgefire Supper at Marble stair hall

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, amber lantern missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, amber lantern missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, amber lantern missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, amber lantern missing=none distractors=none

### Question 65 - distractor-065
Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora?
- Final evaluated answer: Grounded by retrieved evidence for: Anton of Star Basin gallery, basalt sketch.
- Correctness verdict: grounded
- Evidence used: Anton of Star Basin gallery, basalt sketch
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Zora of Star Basin gallery
- Distractors / false positives: Zora of Star Basin gallery

Expected evidence:
- Anton of Star Basin gallery
- basalt sketch

Expected distractors:
- Zora of Star Basin gallery

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Anton of Star Basin gallery, basalt sketch missing=none distractors=Zora of Star Basin gallery
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Anton of Star Basin gallery, basalt sketch missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Anton of Star Basin gallery, basalt sketch missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Anton of Star Basin gallery, basalt sketch missing=none distractors=none

### Question 66 - distractor-066
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 22 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 22 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=0.5; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: bge_m3 missing March 22 Bellwater Fair; multilingual_e5_base missing March 22 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 22 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 23 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=March 22 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 22 Bellwater Fair distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=March 22 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 22 Bellwater Fair distractors=none

### Question 67 - distractor-067
Question: Which place held the true profile detail for Tomas, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, silver booth token.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, silver booth token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=partial coverage=1.0
- Winner: `bge_m3`
- Why it won: Earlier first relevant chunk (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Blue Trunk cabin
- silver booth token

Expected distractors:
- East Signal room

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, silver booth token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, silver booth token missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, silver booth token missing=none distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=1.0 matched=Blue Trunk cabin, silver booth token missing=none distractors=none

### Question 68 - distractor-068
Question: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vera of North Orchard lane, clay watering cup.
- Correctness verdict: grounded
- Evidence used: Vera of North Orchard lane, clay watering cup
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- Vera of North Orchard lane

Expected distractors:
- glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Vera of North Orchard lane, clay watering cup missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Vera of North Orchard lane, clay watering cup missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Vera of North Orchard lane, clay watering cup missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Vera of North Orchard lane, clay watering cup missing=none distractors=none

### Question 69 - distractor-069
Question: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, juniper bundles.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, juniper bundles
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- juniper bundles

Expected distractors:
- Bridgefire Supper at South Meadow arch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, juniper bundles missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, juniper bundles missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, juniper bundles missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, juniper bundles missing=none distractors=none

### Question 70 - distractor-070
Question: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris?
- Final evaluated answer: Grounded by retrieved evidence for: Lina of Birch Ferry shed, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: Lina of Birch Ferry shed, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Lina of Birch Ferry shed
- smoke vent chain

Expected distractors:
- Boris of Birch Ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lina of Birch Ferry shed, smoke vent chain missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lina of Birch Ferry shed, smoke vent chain missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Lina of Birch Ferry shed, smoke vent chain missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Lina of Birch Ferry shed, smoke vent chain missing=none distractors=none

### Question 71 - distractor-071
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 27 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 27 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- March 27 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 28 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 27 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 27 Bellwater Fair missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 27 Bellwater Fair missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 27 Bellwater Fair missing=none distractors=none

### Question 72 - distractor-072
Question: Which place held the true profile detail for Yara, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, linen wick.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, linen wick
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=1.0; multilingual_e5_base -> verdict=partial coverage=1.0
- Winner: `bge_m3`
- Why it won: Earlier first relevant chunk (2 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Cloud Wharf office
- linen wick

Expected distractors:
- Fox Hollow bridge

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, linen wick missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, linen wick missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=1.0 matched=Cloud Wharf office, linen wick missing=none distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=1.0 matched=Cloud Wharf office, linen wick missing=none distractors=none

### Question 73 - distractor-073
Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Lev of Ridge Post loft, star ledger page.
- Correctness verdict: grounded
- Evidence used: Lev of Ridge Post loft, star ledger page
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- star ledger page
- Lev of Ridge Post loft

Expected distractors:
- rope bridge permit

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lev of Ridge Post loft, star ledger page missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lev of Ridge Post loft, star ledger page missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Lev of Ridge Post loft, star ledger page missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Lev of Ridge Post loft, star ledger page missing=none distractors=none

### Question 74 - distractor-074
Question: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, lantern hook.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at Willow Courtyard well
- lantern hook

Expected distractors:
- Bridgefire Supper at Willow Courtyard well

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, lantern hook missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, lantern hook missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, lantern hook missing=none distractors=none

### Question 75 - distractor-075
Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia?
- Final evaluated answer: Grounded by retrieved evidence for: Pavel of Bell Bridge square, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: Pavel of Bell Bridge square, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Talia of Bell Bridge square
- Distractors / false positives: Talia of Bell Bridge square

Expected evidence:
- Pavel of Bell Bridge square
- weathered camera strap

Expected distractors:
- Talia of Bell Bridge square

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Pavel of Bell Bridge square, weathered camera strap missing=none distractors=Talia of Bell Bridge square
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Pavel of Bell Bridge square, weathered camera strap missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Pavel of Bell Bridge square, weathered camera strap missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Pavel of Bell Bridge square, weathered camera strap missing=none distractors=none

### Question 76 - distractor-076
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 14 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 14 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=0.5; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: bge_m3 missing March 14 Bellwater Fair; multilingual_e5_base missing March 14 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 14 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 15 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 14 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=0.5 matched=Cedar Hill station missing=March 14 Bellwater Fair distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 14 Bellwater Fair missing=none distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=0.5 matched=Cedar Hill station missing=March 14 Bellwater Fair distractors=none

### Question 77 - distractor-077
Question: Which place held the true profile detail for Damir, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Moon Mill yard, tin key.
- Correctness verdict: grounded
- Evidence used: Moon Mill yard, tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=1.0; multilingual_e5_base -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Moon Mill yard
- tin key

Expected distractors:
- Hollow Market arcade

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Moon Mill yard, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Moon Mill yard, tin key missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=1.0 matched=Moon Mill yard, tin key missing=none distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=1.0 matched=Moon Mill yard, tin key missing=none distractors=none

### Question 78 - distractor-078
Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Nessa of Winter Chapel porch, blue oar.
- Correctness verdict: grounded
- Evidence used: Nessa of Winter Chapel porch, blue oar
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- Nessa of Winter Chapel porch

Expected distractors:
- copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Nessa of Winter Chapel porch, blue oar missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Nessa of Winter Chapel porch, blue oar missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Nessa of Winter Chapel porch, blue oar missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Nessa of Winter Chapel porch, blue oar missing=none distractors=none

### Question 79 - distractor-079
Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, willow basket.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at Marble stair hall
- willow basket

Expected distractors:
- Bridgefire Supper at Marble stair hall

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, willow basket missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, willow basket missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, willow basket missing=none distractors=none

### Question 80 - distractor-080
Question: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas?
- Final evaluated answer: Grounded by retrieved evidence for: Mira of Star Basin gallery, paper moon mask.
- Correctness verdict: grounded
- Evidence used: Mira of Star Basin gallery, paper moon mask
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Tomas of Star Basin gallery
- Distractors / false positives: Tomas of Star Basin gallery

Expected evidence:
- Mira of Star Basin gallery
- paper moon mask

Expected distractors:
- Tomas of Star Basin gallery

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Mira of Star Basin gallery, paper moon mask missing=none distractors=Tomas of Star Basin gallery
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Mira of Star Basin gallery, paper moon mask missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Mira of Star Basin gallery, paper moon mask missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Mira of Star Basin gallery, paper moon mask missing=none distractors=none

### Question 81 - distractor-081
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 19 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 19 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=0.5; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: bge_m3 missing March 19 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 19 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 20 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=March 19 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 19 Bellwater Fair distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=March 19 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=March 19 Bellwater Fair, North Bell workshop missing=none distractors=none

### Question 82 - distractor-082
Question: Which place held the true profile detail for Kira, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Blue Trunk cabin
- copper wind vane pin

Expected distractors:
- East Signal room

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, copper wind vane pin missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, copper wind vane pin missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, copper wind vane pin missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, copper wind vane pin missing=none distractors=none

### Question 83 - distractor-083
Question: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Petar of North Orchard lane, coal stove hiss.
- Correctness verdict: grounded
- Evidence used: Petar of North Orchard lane, coal stove hiss
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- coal stove hiss
- Petar of North Orchard lane

Expected distractors:
- amber lantern

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Petar of North Orchard lane, coal stove hiss missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Petar of North Orchard lane, coal stove hiss missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Petar of North Orchard lane, coal stove hiss missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Petar of North Orchard lane, coal stove hiss missing=none distractors=none

### Question 84 - distractor-084
Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, violet ribbon.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- violet ribbon

Expected distractors:
- Bridgefire Supper at South Meadow arch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, violet ribbon missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, violet ribbon missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, violet ribbon missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, violet ribbon missing=none distractors=none

### Question 85 - distractor-085
Question: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara?
- Final evaluated answer: Grounded by retrieved evidence for: Stefan of Birch Ferry shed, tuning fork.
- Correctness verdict: grounded
- Evidence used: Stefan of Birch Ferry shed, tuning fork
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Yara of Birch Ferry shed
- Distractors / false positives: Yara of Birch Ferry shed

Expected evidence:
- Stefan of Birch Ferry shed
- tuning fork

Expected distractors:
- Yara of Birch Ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Stefan of Birch Ferry shed, tuning fork missing=none distractors=Yara of Birch Ferry shed
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Stefan of Birch Ferry shed, tuning fork missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Stefan of Birch Ferry shed, tuning fork missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Stefan of Birch Ferry shed, tuning fork missing=none distractors=none

### Question 86 - distractor-086
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 24 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 24 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_base missing March 24 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 24 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 25 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 24 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 24 Bellwater Fair missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 24 Bellwater Fair missing=none distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=0.5 matched=Lantern Row kiosk missing=March 24 Bellwater Fair distractors=none

### Question 87 - distractor-087
Question: Which place held the true profile detail for Nikola, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=no_evidence coverage=0.0; multilingual_e5_base -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Earlier first relevant chunk (3 vs 4).
- What the losing model missed or got wrong: paraphrase_multilingual_mpnet_base_v2 missing Cloud Wharf office, oak barrel hoops
- Distractors / false positives: none

Expected evidence:
- Cloud Wharf office
- oak barrel hoops

Expected distractors:
- Fox Hollow bridge

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, oak barrel hoops missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=no_evidence coverage=0.0 matched=none missing=Cloud Wharf office, oak barrel hoops distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=1.0 matched=Cloud Wharf office, oak barrel hoops missing=none distractors=none

### Question 88 - distractor-088
Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Sonya of Ridge Post loft, blue glass jar.
- Correctness verdict: grounded
- Evidence used: Sonya of Ridge Post loft, blue glass jar
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- Sonya of Ridge Post loft

Expected distractors:
- juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Sonya of Ridge Post loft, blue glass jar missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Sonya of Ridge Post loft, blue glass jar missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Sonya of Ridge Post loft, blue glass jar missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Sonya of Ridge Post loft, blue glass jar missing=none distractors=none

### Question 89 - distractor-089
Question: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, canal route map.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, canal route map
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at Willow Courtyard well
- canal route map

Expected distractors:
- Bridgefire Supper at Willow Courtyard well

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, canal route map missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, canal route map missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, canal route map missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, canal route map missing=none distractors=none

### Question 90 - distractor-090
Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir?
- Final evaluated answer: Grounded by retrieved evidence for: Selma of Bell Bridge square, cedar shovel.
- Correctness verdict: grounded
- Evidence used: Selma of Bell Bridge square, cedar shovel
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Damir of Bell Bridge square
- Distractors / false positives: Damir of Bell Bridge square

Expected evidence:
- Selma of Bell Bridge square
- cedar shovel

Expected distractors:
- Damir of Bell Bridge square

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Selma of Bell Bridge square, cedar shovel missing=none distractors=Damir of Bell Bridge square
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Selma of Bell Bridge square, cedar shovel missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Selma of Bell Bridge square, cedar shovel missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Selma of Bell Bridge square, cedar shovel missing=none distractors=none

### Question 91 - distractor-091
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 11 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 11 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=0.5; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=0.5; multilingual_e5_base -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_small`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: bge_m3 missing March 11 Bellwater Fair; paraphrase_multilingual_mpnet_base_v2 missing March 11 Bellwater Fair; multilingual_e5_base missing March 11 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 11 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 12 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 11 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=0.5 matched=Cedar Hill station missing=March 11 Bellwater Fair distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=0.5 matched=Cedar Hill station missing=March 11 Bellwater Fair distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=0.5 matched=Cedar Hill station missing=March 11 Bellwater Fair distractors=none

### Question 92 - distractor-092
Question: Which place held the true profile detail for Zora, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Moon Mill yard, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: Moon Mill yard, moonflower cutting
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=1.0; multilingual_e5_base -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Earlier first relevant chunk (1 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Moon Mill yard
- moonflower cutting

Expected distractors:
- Hollow Market arcade

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Moon Mill yard, moonflower cutting missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Moon Mill yard, moonflower cutting missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=1.0 matched=Moon Mill yard, moonflower cutting missing=none distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=1.0 matched=Moon Mill yard, moonflower cutting missing=none distractors=none

### Question 93 - distractor-093
Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vesna of Winter Chapel porch, birch tea flask.
- Correctness verdict: grounded
- Evidence used: Vesna of Winter Chapel porch, birch tea flask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- birch tea flask
- Vesna of Winter Chapel porch

Expected distractors:
- lantern hook

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Vesna of Winter Chapel porch, birch tea flask missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Vesna of Winter Chapel porch, birch tea flask missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Vesna of Winter Chapel porch, birch tea flask missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Vesna of Winter Chapel porch, birch tea flask missing=none distractors=none

### Question 94 - distractor-094
Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, saffron scarf.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at Marble stair hall
- saffron scarf

Expected distractors:
- Bridgefire Supper at Marble stair hall

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, saffron scarf missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, saffron scarf missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, saffron scarf missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, saffron scarf missing=none distractors=none

### Question 95 - distractor-095
Question: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira?
- Final evaluated answer: Grounded by retrieved evidence for: Ilya of Star Basin gallery, carved shell comb.
- Correctness verdict: grounded
- Evidence used: Ilya of Star Basin gallery, carved shell comb
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Kira of Star Basin gallery
- Distractors / false positives: Kira of Star Basin gallery

Expected evidence:
- Ilya of Star Basin gallery
- carved shell comb

Expected distractors:
- Kira of Star Basin gallery

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Ilya of Star Basin gallery, carved shell comb missing=none distractors=Kira of Star Basin gallery
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Ilya of Star Basin gallery, carved shell comb missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Ilya of Star Basin gallery, carved shell comb missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Ilya of Star Basin gallery, carved shell comb missing=none distractors=none

### Question 96 - distractor-096
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 16 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 16 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=partial coverage=0.5; multilingual_e5_base -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: paraphrase_multilingual_mpnet_base_v2 missing March 16 Bellwater Fair; multilingual_e5_base missing March 16 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 16 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 17 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=March 16 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=March 16 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 16 Bellwater Fair distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 16 Bellwater Fair distractors=none

### Question 97 - distractor-097
Question: Which place held the true profile detail for Boris, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, basalt sketch.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, basalt sketch
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Blue Trunk cabin
- basalt sketch

Expected distractors:
- East Signal room

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, basalt sketch missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, basalt sketch missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, basalt sketch missing=none distractors=none
  - `multilingual_e5_base`: verdict=partial coverage=1.0 matched=Blue Trunk cabin, basalt sketch missing=none distractors=none

### Question 98 - distractor-098
Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Daria of North Orchard lane, green apron.
- Correctness verdict: grounded
- Evidence used: Daria of North Orchard lane, green apron
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- green apron
- Daria of North Orchard lane

Expected distractors:
- willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Daria of North Orchard lane, green apron missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Daria of North Orchard lane, green apron missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Daria of North Orchard lane, green apron missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Daria of North Orchard lane, green apron missing=none distractors=none

### Question 99 - distractor-099
Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, silver booth token.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, silver booth token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- silver booth token

Expected distractors:
- Bridgefire Supper at South Meadow arch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, silver booth token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, silver booth token missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, silver booth token missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, silver booth token missing=none distractors=none

### Question 100 - distractor-100
Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola?
- Final evaluated answer: Grounded by retrieved evidence for: Ada of Birch Ferry shed, clay watering cup.
- Correctness verdict: grounded
- Evidence used: Ada of Birch Ferry shed, clay watering cup
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors Nikola of Birch Ferry shed
- Distractors / false positives: Nikola of Birch Ferry shed

Expected evidence:
- Ada of Birch Ferry shed
- clay watering cup

Expected distractors:
- Nikola of Birch Ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Ada of Birch Ferry shed, clay watering cup missing=none distractors=Nikola of Birch Ferry shed
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Ada of Birch Ferry shed, clay watering cup missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=Ada of Birch Ferry shed, clay watering cup missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=Ada of Birch Ferry shed, clay watering cup missing=none distractors=none

## Aggregate Client Decision
- Recommended active model: `bge_m3`
- Overall winner: `bge_m3`
- Activation state: `false`
- Runtime retrieval verified: `false`
- Production recommendation: No new provider beat historical `bge_m3`; keep `bge_m3` as the production recommendation.

## Developer Details

### Question 1 - distractor-twin-innkeepers
Question: Which Marta kept the North Inn ledger, and what detail identified her apron?

Expected evidence:
- Marta of North Inn
- green apron

Expected distractors:
- Marta of River Inn

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.913165 chunk_id=23331 preview=Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? document innkeeper-letters::distractor-twin-innkeepers: In docu...
  2. score=0.907813 chunk_id=23227 preview=document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Cas...
  3. score=0.900617 chunk_id=23330 preview=Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? Case scope id: distractor-twin-innkeepers. Scoped answer summar...
  4. score=0.850764 chunk_id=23327 preview=document innkeeper-letters::distractor-twin-innkeepers::distractor: A conflicting note in document innkeeper-letters mentions Marta of River Inn (aliases: Ri...
  5. score=0.816448 chunk_id=23194 preview=document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Dar...
- Matched markers: Marta of North Inn, green apron
- Missing markers: none
- Distractors: Marta of River Inn
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Marta of North Inn, green apron. Distractors present: Marta of River Inn.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.795206 chunk_id=23227 preview=document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Cas...
  2. score=0.786192 chunk_id=23331 preview=Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? document innkeeper-letters::distractor-twin-innkeepers: In docu...
  3. score=0.778451 chunk_id=23330 preview=Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? Case scope id: distractor-twin-innkeepers. Scoped answer summar...
  4. score=0.561329 chunk_id=23327 preview=document innkeeper-letters::distractor-twin-innkeepers::distractor: A conflicting note in document innkeeper-letters mentions Marta of River Inn (aliases: Ri...
  5. score=0.504005 chunk_id=23170 preview=document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Mor...
- Matched markers: Marta of North Inn, green apron
- Missing markers: none
- Distractors: Marta of River Inn
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Marta of North Inn, green apron. Distractors present: Marta of River Inn.
- Verdict: partial

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.727402 chunk_id=24130 preview=Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? Case scope id: distractor-twin-innkeepers. Scoped answer summar...
  2. score=0.607366 chunk_id=24131 preview=Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? document innkeeper-letters::distractor-twin-innkeepers: In docu...
  3. score=0.597365 chunk_id=24027 preview=document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Cas...
- Matched markers: Marta of North Inn, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Marta of North Inn, green apron.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.898621 chunk_id=24131 preview=Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? document innkeeper-letters::distractor-twin-innkeepers: In docu...
  2. score=0.890687 chunk_id=24130 preview=Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? Case scope id: distractor-twin-innkeepers. Scoped answer summar...
- Matched markers: Marta of North Inn, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Marta of North Inn, green apron.
- Verdict: grounded

- Winner:
  - `paraphrase_multilingual_mpnet_base_v2`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 2 - distractor-june-market-date
Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice?

Expected evidence:
- June 14 night market
- Bell Bridge square

Expected distractors:
- June 4 noon market

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.928975 chunk_id=23228 preview=document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Br...
  2. score=0.920064 chunk_id=23333 preview=Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? document market-announcemen...
  3. score=0.915394 chunk_id=23332 preview=Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Case scope id: distractor-j...
  4. score=0.857906 chunk_id=23328 preview=document market-announcements::distractor-june-market-date::distractor: A conflicting note in document market-announcements mentions June 4 noon market (alia...
  5. score=0.827421 chunk_id=23234 preview=document distractor-bell-bridge-square-060::distractor-060::distractor: A conflicting note in document distractor-bell-bridge-square-060 mentions Nikola of B...
- Matched markers: Bell Bridge square, June 14 night market
- Missing markers: none
- Distractors: June 4 noon market
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Bell Bridge square, June 14 night market. Distractors present: June 4 noon market.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.776470 chunk_id=23333 preview=Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? document market-announcemen...
  2. score=0.773436 chunk_id=23332 preview=Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Case scope id: distractor-j...
  3. score=0.767346 chunk_id=23228 preview=document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Br...
  4. score=0.553881 chunk_id=23328 preview=document market-announcements::distractor-june-market-date::distractor: A conflicting note in document market-announcements mentions June 4 noon market (alia...
  5. score=0.515070 chunk_id=23449 preview=Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? document distractor-bell-bridge-square-060::...
- Matched markers: Bell Bridge square, June 14 night market
- Missing markers: none
- Distractors: June 4 noon market
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Bell Bridge square, June 14 night market. Distractors present: June 4 noon market.
- Verdict: partial

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.823486 chunk_id=24132 preview=Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Case scope id: distractor-j...
  2. score=0.788870 chunk_id=24133 preview=Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? document market-announcemen...
  3. score=0.770101 chunk_id=24028 preview=document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Br...
- Matched markers: Bell Bridge square, June 14 night market
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bell Bridge square, June 14 night market.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.909676 chunk_id=24133 preview=Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? document market-announcemen...
  2. score=0.896438 chunk_id=24132 preview=Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Case scope id: distractor-j...
  3. score=0.895390 chunk_id=24028 preview=document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Br...
- Matched markers: Bell Bridge square, June 14 night market
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bell Bridge square, June 14 night market.
- Verdict: grounded

- Winner:
  - `multilingual_e5_base`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 3 - distractor-two-levs
Question: Which Lev repaired the oak barrels, not the one who worked by the ferry?

Expected evidence:
- Lev the cooper
- oak barrel hoops

Expected distractors:
- Lev the ferryman

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.881482 chunk_id=23335 preview=Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? document workshop-accounts::distractor-two-levs: In document worksh...
  2. score=0.871256 chunk_id=23229 preview=document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case reco...
  3. score=0.867380 chunk_id=23334 preview=Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? Case scope id: distractor-two-levs. Scoped answer summary for distr...
  4. score=0.845203 chunk_id=23329 preview=document workshop-accounts::distractor-two-levs::distractor: A conflicting note in document workshop-accounts mentions Lev the ferryman (aliases: ferryman na...
  5. score=0.806446 chunk_id=23140 preview=document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry...
- Matched markers: Lev the cooper, oak barrel hoops
- Missing markers: none
- Distractors: Lev the ferryman
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Lev the cooper, oak barrel hoops. Distractors present: Lev the ferryman.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.746087 chunk_id=23335 preview=Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? document workshop-accounts::distractor-two-levs: In document worksh...
  2. score=0.725116 chunk_id=23334 preview=Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? Case scope id: distractor-two-levs. Scoped answer summary for distr...
  3. score=0.705438 chunk_id=23229 preview=document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case reco...
  4. score=0.556327 chunk_id=23329 preview=document workshop-accounts::distractor-two-levs::distractor: A conflicting note in document workshop-accounts mentions Lev the ferryman (aliases: ferryman na...
  5. score=0.462400 chunk_id=23394 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-...
- Matched markers: Lev the cooper, oak barrel hoops
- Missing markers: none
- Distractors: Lev the ferryman
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Lev the cooper, oak barrel hoops. Distractors present: Lev the ferryman.
- Verdict: partial

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.797535 chunk_id=24134 preview=Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? Case scope id: distractor-two-levs. Scoped answer summary for distr...
  2. score=0.759792 chunk_id=24135 preview=Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? document workshop-accounts::distractor-two-levs: In document worksh...
  3. score=0.593655 chunk_id=24029 preview=document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case reco...
- Matched markers: Lev the cooper, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev the cooper, oak barrel hoops.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.872618 chunk_id=24135 preview=Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? document workshop-accounts::distractor-two-levs: In document worksh...
  2. score=0.850821 chunk_id=24134 preview=Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? Case scope id: distractor-two-levs. Scoped answer summary for distr...
- Matched markers: Lev the cooper, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev the cooper, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `paraphrase_multilingual_mpnet_base_v2`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 4 - distractor-similar-islands
Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor?

Expected evidence:
- Fog Island ferry shed
- painted blue oar

Expected distractors:
- Fox Island ferry shed

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.916514 chunk_id=23226 preview=document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oa...
  2. score=0.913843 chunk_id=23336 preview=Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Case scope id: distractor-similar-islands....
  3. score=0.911438 chunk_id=23337 preview=Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? document ferry-shed-notes::distractor-simil...
  4. score=0.830295 chunk_id=23224 preview=document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Ness...
  5. score=0.826920 chunk_id=23321 preview=document distractor-winter-chapel-porch-033::distractor-033::distractor: A conflicting note in document distractor-winter-chapel-porch-033 mentions blue oar...
- Matched markers: Fog Island ferry shed, painted blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Fog Island ferry shed, painted blue oar.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.779505 chunk_id=23336 preview=Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Case scope id: distractor-similar-islands....
  2. score=0.777804 chunk_id=23337 preview=Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? document ferry-shed-notes::distractor-simil...
  3. score=0.755813 chunk_id=23226 preview=document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oa...
  4. score=0.541165 chunk_id=23321 preview=document distractor-winter-chapel-porch-033::distractor-033::distractor: A conflicting note in document distractor-winter-chapel-porch-033 mentions blue oar...
  5. score=0.539759 chunk_id=23326 preview=document ferry-shed-notes::distractor-similar-islands::distractor: A conflicting note in document ferry-shed-notes mentions Fox Island ferry shed (aliases: f...
- Matched markers: Fog Island ferry shed, painted blue oar
- Missing markers: none
- Distractors: Fox Island ferry shed
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Fog Island ferry shed, painted blue oar. Distractors present: Fox Island ferry shed.
- Verdict: partial

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.726770 chunk_id=24136 preview=Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Case scope id: distractor-similar-islands....
  2. score=0.658581 chunk_id=24137 preview=Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? document ferry-shed-notes::distractor-simil...
- Matched markers: Fog Island ferry shed, painted blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Fog Island ferry shed, painted blue oar.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.890751 chunk_id=24026 preview=document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oa...
  2. score=0.887804 chunk_id=24137 preview=Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? document ferry-shed-notes::distractor-simil...
  3. score=0.884936 chunk_id=24136 preview=Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Case scope id: distractor-similar-islands....
- Matched markers: Fog Island ferry shed, painted blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Fog Island ferry shed, painted blue oar.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 5 - distractor-letter-mixup
Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season?

Expected evidence:
- Ada's winter letter
- violet wax thread

Expected distractors:
- Alda's spring letter

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.907602 chunk_id=23339 preview=Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? document courier-bag-index::...
  2. score=0.895226 chunk_id=23338 preview=Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Case scope id: distractor-le...
  3. score=0.891391 chunk_id=23130 preview=document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread....
  4. score=0.846921 chunk_id=23323 preview=document distractor-winter-chapel-porch-063::distractor-063::distractor: A conflicting note in document distractor-winter-chapel-porch-063 mentions wax threa...
  5. score=0.817023 chunk_id=23216 preview=document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lan...
- Matched markers: Ada's winter letter, violet wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada's winter letter, violet wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.761799 chunk_id=23338 preview=Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Case scope id: distractor-le...
  2. score=0.758391 chunk_id=23339 preview=Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? document courier-bag-index::...
  3. score=0.734945 chunk_id=23130 preview=document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread....
  4. score=0.547784 chunk_id=23323 preview=document distractor-winter-chapel-porch-063::distractor-063::distractor: A conflicting note in document distractor-winter-chapel-porch-063 mentions wax threa...
  5. score=0.505148 chunk_id=23325 preview=document distractor-winter-chapel-porch-093::distractor-093::distractor: A conflicting note in document distractor-winter-chapel-porch-093 mentions lantern h...
- Matched markers: Ada's winter letter, violet wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada's winter letter, violet wax thread.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.776791 chunk_id=24138 preview=Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Case scope id: distractor-le...
  2. score=0.714009 chunk_id=24139 preview=Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? document courier-bag-index::...
  3. score=0.579036 chunk_id=23930 preview=document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread....
- Matched markers: Ada's winter letter, violet wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada's winter letter, violet wax thread.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.886064 chunk_id=24139 preview=Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? document courier-bag-index::...
  2. score=0.884501 chunk_id=24138 preview=Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Case scope id: distractor-le...
  3. score=0.853664 chunk_id=23930 preview=document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread....
- Matched markers: Ada's winter letter, violet wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada's winter letter, violet wax thread.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 6 - distractor-006
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

Expected evidence:
- March 16 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 17 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919557 chunk_id=23181 preview=document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellw...
  2. score=0.919384 chunk_id=23187 preview=document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellw...
  3. score=0.918695 chunk_id=23185 preview=document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellw...
  4. score=0.918667 chunk_id=23183 preview=document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellw...
  5. score=0.917342 chunk_id=23186 preview=document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellw...
- Matched markers: March 16 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 16 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.778081 chunk_id=23184 preview=document distractor-north-bell-workshop-051::distractor-051: In document distractor-north-bell-workshop-051, the verified archive note records March 25 Bellw...
  2. score=0.775997 chunk_id=23430 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-051. S...
  3. score=0.773384 chunk_id=23340 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-006. S...
  4. score=0.773188 chunk_id=23182 preview=document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellw...
  5. score=0.773136 chunk_id=23370 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-021. S...
- Matched markers: March 16 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 16 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.833872 chunk_id=24290 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-081. S...
  2. score=0.833841 chunk_id=24230 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-051. S...
  3. score=0.832436 chunk_id=24260 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. S...
- Matched markers: North Bell workshop
- Missing markers: March 16 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 16 Bellwater Fair.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.898039 chunk_id=24291 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=0.896125 chunk_id=24171 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=0.894784 chunk_id=24231 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
- Matched markers: North Bell workshop
- Missing markers: March 16 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 16 Bellwater Fair.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 7 - distractor-007
Question: Which place held the true profile detail for Nikola, not the nearly identical place name?

Expected evidence:
- Blue Trunk cabin
- brass compass

Expected distractors:
- East Signal room

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.868769 chunk_id=23423 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-moon-mill-yard-047::distractor...
  2. score=0.861599 chunk_id=23343 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distract...
  3. score=0.861501 chunk_id=23503 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distra...
  4. score=0.861106 chunk_id=23502 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-087. Scoped answer summa...
  5. score=0.855479 chunk_id=23342 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-007. Scoped answer summa...
- Matched markers: Blue Trunk cabin, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, brass compass.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.682292 chunk_id=23343 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distract...
  2. score=0.679367 chunk_id=23342 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-007. Scoped answer summa...
  3. score=0.664020 chunk_id=23422 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-047. Scoped answer summa...
  4. score=0.663204 chunk_id=23502 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-087. Scoped answer summa...
  5. score=0.661656 chunk_id=23503 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distra...
- Matched markers: Blue Trunk cabin, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, brass compass.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.728338 chunk_id=24143 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distract...
  2. score=0.727059 chunk_id=24142 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-007. Scoped answer summa...
  3. score=0.697391 chunk_id=24222 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-047. Scoped answer summa...
- Matched markers: Blue Trunk cabin, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, brass compass.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.863421 chunk_id=24303 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distra...
  2. score=0.862430 chunk_id=24223 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-moon-mill-yard-047::distractor...
  3. score=0.851683 chunk_id=24143 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distract...
- Matched markers: Blue Trunk cabin, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Partially grounded by: Blue Trunk cabin, brass compass.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Earlier first relevant chunk (1 vs 2).

### Question 8 - distractor-008
Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

Expected evidence:
- linen wick
- Sonya of North Orchard lane

Expected distractors:
- tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.917763 chunk_id=23188 preview=document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sony...
  2. score=0.909791 chunk_id=23344 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  3. score=0.907525 chunk_id=23345 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  4. score=0.877023 chunk_id=23200 preview=document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya...
  5. score=0.873864 chunk_id=23222 preview=document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mas...
- Matched markers: Sonya of North Orchard lane, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of North Orchard lane, linen wick.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.775981 chunk_id=23344 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=0.768037 chunk_id=23345 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=0.763965 chunk_id=23188 preview=document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sony...
  4. score=0.716979 chunk_id=23524 preview=Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  5. score=0.712039 chunk_id=23425 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
- Matched markers: Sonya of North Orchard lane, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of North Orchard lane, linen wick.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.803928 chunk_id=24144 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=0.771290 chunk_id=24145 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
- Matched markers: Sonya of North Orchard lane, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of North Orchard lane, linen wick.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.891274 chunk_id=24145 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  2. score=0.890744 chunk_id=23988 preview=document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sony...
- Matched markers: Sonya of North Orchard lane, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of North Orchard lane, linen wick.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 9 - distractor-009
Question: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- star ledger page

Expected distractors:
- Bridgefire Supper at South Meadow arch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.913847 chunk_id=23201 preview=document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Mor...
  2. score=0.904794 chunk_id=23347 preview=Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? document distractor-south...
  3. score=0.899960 chunk_id=23346 preview=Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  4. score=0.894022 chunk_id=23205 preview=document distractor-south-meadow-arch-069::distractor-069: In document distractor-south-meadow-arch-069, the verified archive note records Signal Lantern Mor...
  5. score=0.890755 chunk_id=23204 preview=document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at South Meadow arch, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, star ledger page.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.763533 chunk_id=23346 preview=Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  2. score=0.759807 chunk_id=23347 preview=Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? document distractor-south...
  3. score=0.698763 chunk_id=23201 preview=document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Mor...
  4. score=0.697652 chunk_id=23436 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  5. score=0.690798 chunk_id=23437 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
- Matched markers: Signal Lantern Morning at South Meadow arch, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, star ledger page.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.767435 chunk_id=24146 preview=Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  2. score=0.749741 chunk_id=24147 preview=Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? document distractor-south...
- Matched markers: Signal Lantern Morning at South Meadow arch, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, star ledger page.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.898320 chunk_id=24001 preview=document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Mor...
  2. score=0.891141 chunk_id=24147 preview=Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? document distractor-south...
- Matched markers: Signal Lantern Morning at South Meadow arch, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, star ledger page.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 10 - distractor-010
Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir?

Expected evidence:
- Selma of Birch Ferry shed
- lantern hook

Expected distractors:
- Damir of Birch Ferry shed

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.904975 chunk_id=23349 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? document distractor-birch-ferry-shed-010::dis...
  2. score=0.904192 chunk_id=23348 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Case scope id: distractor-010. Scoped answer...
  3. score=0.903076 chunk_id=23137 preview=document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry...
  4. score=0.882213 chunk_id=23237 preview=document distractor-birch-ferry-shed-010::distractor-010::distractor: A conflicting note in document distractor-birch-ferry-shed-010 mentions Damir of Birch...
  5. score=0.868577 chunk_id=23499 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? document distractor-birch-ferry-shed-085::dis...
- Matched markers: Selma of Birch Ferry shed, lantern hook
- Missing markers: none
- Distractors: Damir of Birch Ferry shed
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Selma of Birch Ferry shed, lantern hook. Distractors present: Damir of Birch Ferry shed.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.751406 chunk_id=23349 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? document distractor-birch-ferry-shed-010::dis...
  2. score=0.747131 chunk_id=23348 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Case scope id: distractor-010. Scoped answer...
  3. score=0.725355 chunk_id=23137 preview=document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry...
  4. score=0.653004 chunk_id=23429 preview=Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? document distractor-star-basin-gallery-050:...
  5. score=0.650519 chunk_id=23508 preview=Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Case scope id: distractor-090. Scoped answe...
- Matched markers: Selma of Birch Ferry shed, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Birch Ferry shed, lantern hook.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.858203 chunk_id=24148 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Case scope id: distractor-010. Scoped answer...
  2. score=0.814603 chunk_id=24149 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? document distractor-birch-ferry-shed-010::dis...
- Matched markers: Selma of Birch Ferry shed, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Birch Ferry shed, lantern hook.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.898757 chunk_id=24149 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? document distractor-birch-ferry-shed-010::dis...
  2. score=0.889772 chunk_id=23937 preview=document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry...
  3. score=0.885765 chunk_id=24148 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Case scope id: distractor-010. Scoped answer...
- Matched markers: Selma of Birch Ferry shed, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Birch Ferry shed, lantern hook.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 11 - distractor-011
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

Expected evidence:
- March 21 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 22 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.931622 chunk_id=23164 preview=document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater...
  2. score=0.930362 chunk_id=23166 preview=document distractor-lantern-row-kiosk-056::distractor-056: In document distractor-lantern-row-kiosk-056, the verified archive note records March 12 Bellwater...
  3. score=0.930210 chunk_id=23168 preview=document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater...
  4. score=0.929893 chunk_id=23167 preview=document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater...
  5. score=0.928965 chunk_id=23165 preview=document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater...
- Matched markers: Lantern Row kiosk
- Missing markers: March 21 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 21 Bellwater Fair.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.813781 chunk_id=23167 preview=document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater...
  2. score=0.811167 chunk_id=23163 preview=document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater...
  3. score=0.800529 chunk_id=23165 preview=document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater...
  4. score=0.799846 chunk_id=23470 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-071. Sco...
  5. score=0.797587 chunk_id=23168 preview=document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater...
- Matched markers: Lantern Row kiosk, March 21 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 21 Bellwater Fair.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.801536 chunk_id=24300 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-086. Sco...
  2. score=0.799668 chunk_id=24270 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-071. Sco...
- Matched markers: Lantern Row kiosk
- Missing markers: March 21 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 21 Bellwater Fair.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.904796 chunk_id=24271 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  2. score=0.904193 chunk_id=24151 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
- Matched markers: Lantern Row kiosk, March 21 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 21 Bellwater Fair.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 12 - distractor-012
Question: Which place held the true profile detail for Zora, not the nearly identical place name?

Expected evidence:
- Cloud Wharf office
- wax thread

Expected distractors:
- Fox Hollow bridge

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.867964 chunk_id=23513 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-0...
  2. score=0.861733 chunk_id=23353 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-cloud-wharf-office-012::distract...
  3. score=0.861349 chunk_id=23433 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor...
  4. score=0.856499 chunk_id=23512 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-092. Scoped answer summary...
  5. score=0.853114 chunk_id=23432 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary...
- Matched markers: Cloud Wharf office, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Cloud Wharf office, wax thread.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.697451 chunk_id=23432 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary...
  2. score=0.693872 chunk_id=23433 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor...
  3. score=0.689089 chunk_id=23512 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-092. Scoped answer summary...
  4. score=0.683521 chunk_id=23513 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-0...
  5. score=0.682850 chunk_id=23352 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-012. Scoped answer summary...
- Matched markers: Cloud Wharf office, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 5
- Answer summary: Partially grounded by: Cloud Wharf office, wax thread.
- Verdict: partial

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.748696 chunk_id=24232 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary...
  2. score=0.730016 chunk_id=24233 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor...
  3. score=0.710905 chunk_id=24313 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-0...
- Matched markers: none
- Missing markers: Cloud Wharf office, wax thread
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.856604 chunk_id=24313 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-0...
  2. score=0.855858 chunk_id=24153 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-cloud-wharf-office-012::distract...
- Matched markers: Cloud Wharf office, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Cloud Wharf office, wax thread.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Earlier first relevant chunk (2 vs 5).

### Question 13 - distractor-013
Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

Expected evidence:
- tin key
- Vesna of Ridge Post loft

Expected distractors:
- cedar shovel

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.920861 chunk_id=23195 preview=document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridg...
  2. score=0.914610 chunk_id=23354 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-01...
  3. score=0.914445 chunk_id=23355 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  4. score=0.887821 chunk_id=23200 preview=document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya...
  5. score=0.884633 chunk_id=23505 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
- Matched markers: Vesna of Ridge Post loft, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of Ridge Post loft, tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.774490 chunk_id=23355 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  2. score=0.773896 chunk_id=23195 preview=document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridg...
  3. score=0.769119 chunk_id=23354 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-01...
  4. score=0.701667 chunk_id=23475 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post...
  5. score=0.695022 chunk_id=23474 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-073....
- Matched markers: Vesna of Ridge Post loft, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of Ridge Post loft, tin key.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.833094 chunk_id=24154 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-01...
  2. score=0.801398 chunk_id=24155 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  3. score=0.737908 chunk_id=24314 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
- Matched markers: Vesna of Ridge Post loft, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of Ridge Post loft, tin key.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.882008 chunk_id=24155 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  2. score=0.874130 chunk_id=24154 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-01...
- Matched markers: Vesna of Ridge Post loft, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of Ridge Post loft, tin key.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 14 - distractor-014
Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at Willow Courtyard well
- blue oar

Expected distractors:
- Bridgefire Supper at Willow Courtyard well

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.905813 chunk_id=23214 preview=document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lan...
  2. score=0.899905 chunk_id=23356 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  3. score=0.893580 chunk_id=23357 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
  4. score=0.886410 chunk_id=23219 preview=document distractor-willow-courtyard-well-089::distractor-089: In document distractor-willow-courtyard-well-089, the verified archive note records Signal Lan...
  5. score=0.883679 chunk_id=23216 preview=document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lan...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, blue oar.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.780002 chunk_id=23357 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
  2. score=0.777229 chunk_id=23356 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  3. score=0.725029 chunk_id=23476 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  4. score=0.723561 chunk_id=23477 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
  5. score=0.722724 chunk_id=23214 preview=document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lan...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, blue oar.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.794225 chunk_id=24156 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  2. score=0.763369 chunk_id=24157 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, blue oar.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.894654 chunk_id=24157 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
  2. score=0.892922 chunk_id=24014 preview=document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lan...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, blue oar.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 15 - distractor-015
Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira?

Expected evidence:
- Ilya of Bell Bridge square
- willow basket

Expected distractors:
- Kira of Bell Bridge square

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.908089 chunk_id=23359 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::d...
  2. score=0.903476 chunk_id=23131 preview=document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bri...
  3. score=0.902073 chunk_id=23358 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer...
  4. score=0.866278 chunk_id=23231 preview=document distractor-bell-bridge-square-015::distractor-015::distractor: A conflicting note in document distractor-bell-bridge-square-015 mentions Kira of Bel...
  5. score=0.860754 chunk_id=23438 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Case scope id: distractor-055. Scoped answer su...
- Matched markers: Ilya of Bell Bridge square, willow basket
- Missing markers: none
- Distractors: Kira of Bell Bridge square
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Ilya of Bell Bridge square, willow basket. Distractors present: Kira of Bell Bridge square.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.761573 chunk_id=23358 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer...
  2. score=0.760957 chunk_id=23359 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::d...
  3. score=0.748186 chunk_id=23131 preview=document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bri...
  4. score=0.678559 chunk_id=23439 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? document distractor-birch-ferry-shed-055::distr...
  5. score=0.676557 chunk_id=23438 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Case scope id: distractor-055. Scoped answer su...
- Matched markers: Ilya of Bell Bridge square, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Bell Bridge square, willow basket.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.825520 chunk_id=24159 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::d...
  2. score=0.816512 chunk_id=24158 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer...
  3. score=0.739158 chunk_id=23931 preview=document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bri...
- Matched markers: Ilya of Bell Bridge square, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Bell Bridge square, willow basket.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.878015 chunk_id=24159 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::d...
  2. score=0.866867 chunk_id=24158 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer...
  3. score=0.865110 chunk_id=23931 preview=document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bri...
- Matched markers: Ilya of Bell Bridge square, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Bell Bridge square, willow basket.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 16 - distractor-016
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

Expected evidence:
- March 26 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 27 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919438 chunk_id=23153 preview=document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwat...
  2. score=0.918574 chunk_id=23151 preview=document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwat...
  3. score=0.917531 chunk_id=23155 preview=document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwat...
  4. score=0.917407 chunk_id=23156 preview=document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwat...
  5. score=0.917248 chunk_id=23154 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
- Matched markers: Cedar Hill station, March 26 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 26 Bellwater Fair.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.794214 chunk_id=23153 preview=document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwat...
  2. score=0.793285 chunk_id=23151 preview=document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwat...
  3. score=0.790958 chunk_id=23154 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
  4. score=0.790795 chunk_id=23152 preview=document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwat...
  5. score=0.789939 chunk_id=23390 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-031. Sc...
- Matched markers: Cedar Hill station, March 26 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 26 Bellwater Fair.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.827919 chunk_id=24280 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-076. Sc...
  2. score=0.827262 chunk_id=24160 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-016. Sc...
- Matched markers: Cedar Hill station, March 26 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 26 Bellwater Fair.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.905928 chunk_id=24161 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  2. score=0.905119 chunk_id=24251 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
- Matched markers: Cedar Hill station, March 26 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 26 Bellwater Fair.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 17 - distractor-017
Question: Which place held the true profile detail for Boris, not the nearly identical place name?

Expected evidence:
- Moon Mill yard
- glass ink bottle

Expected distractors:
- Hollow Market arcade

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.863999 chunk_id=23523 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distracto...
  2. score=0.859011 chunk_id=23443 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distrac...
  3. score=0.858929 chunk_id=23363 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-moon-mill-yard-017::distractor-...
  4. score=0.854487 chunk_id=23522 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summar...
  5. score=0.851230 chunk_id=23442 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-057. Scoped answer summar...
- Matched markers: Moon Mill yard, glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Partially grounded by: Moon Mill yard, glass ink bottle.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.729616 chunk_id=23523 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distracto...
  2. score=0.708255 chunk_id=23522 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summar...
  3. score=0.693435 chunk_id=23443 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distrac...
  4. score=0.690946 chunk_id=23150 preview=document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, ba...
  5. score=0.687760 chunk_id=23442 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-057. Scoped answer summar...
- Matched markers: none
- Missing markers: Moon Mill yard, glass ink bottle
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.694095 chunk_id=24323 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distracto...
  2. score=0.690519 chunk_id=24322 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summar...
- Matched markers: none
- Missing markers: Moon Mill yard, glass ink bottle
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.862998 chunk_id=24243 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distrac...
  2. score=0.862422 chunk_id=24323 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distracto...
- Matched markers: none
- Missing markers: Moon Mill yard, glass ink bottle
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 18 - distractor-018
Question: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

Expected evidence:
- copper wind vane pin
- Daria of Winter Chapel porch

Expected distractors:
- carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.922685 chunk_id=23364 preview=Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=0.920435 chunk_id=23220 preview=document distractor-winter-chapel-porch-018::distractor-018: In document distractor-winter-chapel-porch-018, the verified archive note records copper wind va...
  3. score=0.912144 chunk_id=23365 preview=Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  4. score=0.888169 chunk_id=23225 preview=document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flas...
  5. score=0.888062 chunk_id=23514 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
- Matched markers: Daria of Winter Chapel porch, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of Winter Chapel porch, copper wind vane pin.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.763078 chunk_id=23365 preview=Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  2. score=0.755012 chunk_id=23220 preview=document distractor-winter-chapel-porch-018::distractor-018: In document distractor-winter-chapel-porch-018, the verified archive note records copper wind va...
  3. score=0.753849 chunk_id=23364 preview=Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  4. score=0.710932 chunk_id=23425 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  5. score=0.698869 chunk_id=23222 preview=document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mas...
- Matched markers: Daria of Winter Chapel porch, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of Winter Chapel porch, copper wind vane pin.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.816526 chunk_id=24164 preview=Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=0.779862 chunk_id=24165 preview=Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
- Matched markers: Daria of Winter Chapel porch, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of Winter Chapel porch, copper wind vane pin.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.892012 chunk_id=24020 preview=document distractor-winter-chapel-porch-018::distractor-018: In document distractor-winter-chapel-porch-018, the verified archive note records copper wind va...
  2. score=0.885752 chunk_id=24165 preview=Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
- Matched markers: Daria of Winter Chapel porch, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of Winter Chapel porch, copper wind vane pin.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 19 - distractor-019
Question: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at Marble stair hall
- coal stove hiss

Expected distractors:
- Bridgefire Supper at Marble stair hall

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.904566 chunk_id=23169 preview=document distractor-marble-stair-hall-019::distractor-019: In document distractor-marble-stair-hall-019, the verified archive note records Signal Lantern Mor...
  2. score=0.900043 chunk_id=23170 preview=document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Mor...
  3. score=0.897511 chunk_id=23366 preview=Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor...
  4. score=0.896573 chunk_id=23367 preview=Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? document distractor-marbl...
  5. score=0.896150 chunk_id=23174 preview=document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at Marble stair hall, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, coal stove hiss.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.757662 chunk_id=23366 preview=Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor...
  2. score=0.749792 chunk_id=23367 preview=Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? document distractor-marbl...
  3. score=0.702364 chunk_id=23169 preview=document distractor-marble-stair-hall-019::distractor-019: In document distractor-marble-stair-hall-019, the verified archive note records Signal Lantern Mor...
  4. score=0.675256 chunk_id=23516 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  5. score=0.671321 chunk_id=23517 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
- Matched markers: Signal Lantern Morning at Marble stair hall, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, coal stove hiss.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.767186 chunk_id=24166 preview=Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor...
  2. score=0.747248 chunk_id=24226 preview=Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor...
  3. score=0.744714 chunk_id=24167 preview=Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? document distractor-marbl...
- Matched markers: Signal Lantern Morning at Marble stair hall, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, coal stove hiss.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.901886 chunk_id=24167 preview=Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? document distractor-marbl...
  2. score=0.898016 chunk_id=23969 preview=document distractor-marble-stair-hall-019::distractor-019: In document distractor-marble-stair-hall-019, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at Marble stair hall, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, coal stove hiss.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 20 - distractor-020
Question: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola?

Expected evidence:
- Ada of Star Basin gallery
- violet ribbon

Expected distractors:
- Nikola of Star Basin gallery

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.913599 chunk_id=23369 preview=Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? document distractor-star-basin-gallery-020::...
  2. score=0.913184 chunk_id=23368 preview=Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Case scope id: distractor-020. Scoped answer...
  3. score=0.909269 chunk_id=23208 preview=document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basi...
  4. score=0.880533 chunk_id=23308 preview=document distractor-star-basin-gallery-020::distractor-020::distractor: A conflicting note in document distractor-star-basin-gallery-020 mentions Nikola of S...
  5. score=0.865470 chunk_id=23459 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::...
- Matched markers: Ada of Star Basin gallery, violet ribbon
- Missing markers: none
- Distractors: Nikola of Star Basin gallery
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Ada of Star Basin gallery, violet ribbon. Distractors present: Nikola of Star Basin gallery.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.772986 chunk_id=23369 preview=Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? document distractor-star-basin-gallery-020::...
  2. score=0.766140 chunk_id=23208 preview=document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basi...
  3. score=0.763064 chunk_id=23368 preview=Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Case scope id: distractor-020. Scoped answer...
  4. score=0.646841 chunk_id=23211 preview=document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Ba...
  5. score=0.640058 chunk_id=23459 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::...
- Matched markers: Ada of Star Basin gallery, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Star Basin gallery, violet ribbon.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.853731 chunk_id=24168 preview=Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Case scope id: distractor-020. Scoped answer...
  2. score=0.837190 chunk_id=24169 preview=Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? document distractor-star-basin-gallery-020::...
  3. score=0.764352 chunk_id=24198 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Case scope id: distractor-035. Scoped answe...
- Matched markers: Ada of Star Basin gallery, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Star Basin gallery, violet ribbon.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.902996 chunk_id=24169 preview=Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? document distractor-star-basin-gallery-020::...
  2. score=0.894667 chunk_id=24008 preview=document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basi...
- Matched markers: Ada of Star Basin gallery, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Star Basin gallery, violet ribbon.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 21 - distractor-021
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

Expected evidence:
- March 13 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 14 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919557 chunk_id=23181 preview=document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellw...
  2. score=0.919384 chunk_id=23187 preview=document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellw...
  3. score=0.918695 chunk_id=23185 preview=document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellw...
  4. score=0.918667 chunk_id=23183 preview=document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellw...
  5. score=0.917342 chunk_id=23186 preview=document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellw...
- Matched markers: North Bell workshop
- Missing markers: March 13 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 13 Bellwater Fair.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.778081 chunk_id=23184 preview=document distractor-north-bell-workshop-051::distractor-051: In document distractor-north-bell-workshop-051, the verified archive note records March 25 Bellw...
  2. score=0.775997 chunk_id=23430 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-051. S...
  3. score=0.773384 chunk_id=23340 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-006. S...
  4. score=0.773188 chunk_id=23182 preview=document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellw...
  5. score=0.773136 chunk_id=23370 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-021. S...
- Matched markers: March 13 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 13 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.833872 chunk_id=24290 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-081. S...
  2. score=0.833841 chunk_id=24230 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-051. S...
  3. score=0.832436 chunk_id=24260 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. S...
- Matched markers: North Bell workshop
- Missing markers: March 13 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 13 Bellwater Fair.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.898039 chunk_id=24291 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=0.896125 chunk_id=24171 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=0.894784 chunk_id=24231 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
- Matched markers: March 13 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 13 Bellwater Fair, North Bell workshop.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 22 - distractor-022
Question: Which place held the true profile detail for Talia, not the nearly identical place name?

Expected evidence:
- Blue Trunk cabin
- rope bridge permit

Expected distractors:
- East Signal room

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.848770 chunk_id=23453 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-moon-mill-yard-062::distractor-...
  2. score=0.835635 chunk_id=23373 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distracto...
  3. score=0.834826 chunk_id=23309 preview=document distractor-star-basin-gallery-035::distractor-035::distractor: A conflicting note in document distractor-star-basin-gallery-035 mentions Talia of St...
  4. score=0.834271 chunk_id=23235 preview=document distractor-bell-bridge-square-075::distractor-075::distractor: A conflicting note in document distractor-bell-bridge-square-075 mentions Talia of Be...
  5. score=0.826403 chunk_id=23452 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? Case scope id: distractor-062. Scoped answer summar...
- Matched markers: Blue Trunk cabin, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Blue Trunk cabin, rope bridge permit.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.692824 chunk_id=23452 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? Case scope id: distractor-062. Scoped answer summar...
  2. score=0.679683 chunk_id=23373 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distracto...
  3. score=0.677065 chunk_id=23372 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? Case scope id: distractor-022. Scoped answer summar...
  4. score=0.658683 chunk_id=23453 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-moon-mill-yard-062::distractor-...
  5. score=0.638404 chunk_id=23178 preview=document distractor-moon-mill-yard-062::distractor-062: In document distractor-moon-mill-yard-062, the verified archive note records Moon Mill yard, saffron...
- Matched markers: Blue Trunk cabin, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, rope bridge permit.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.683242 chunk_id=24173 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distracto...
  2. score=0.678916 chunk_id=24172 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? Case scope id: distractor-022. Scoped answer summar...
- Matched markers: Blue Trunk cabin, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, rope bridge permit.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.851709 chunk_id=24253 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-moon-mill-yard-062::distractor-...
  2. score=0.845245 chunk_id=24173 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distracto...
  3. score=0.841174 chunk_id=23978 preview=document distractor-moon-mill-yard-062::distractor-062: In document distractor-moon-mill-yard-062, the verified archive note records Moon Mill yard, saffron...
- Matched markers: Blue Trunk cabin, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Blue Trunk cabin, rope bridge permit.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Earlier first relevant chunk (2 vs 1).

### Question 23 - distractor-023
Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

Expected evidence:
- oak barrel hoops
- Viktor of North Orchard lane

Expected distractors:
- clay watering cup

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.913862 chunk_id=23189 preview=document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops...
  2. score=0.912415 chunk_id=23375 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-nort...
  3. score=0.909328 chunk_id=23374 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distracto...
  4. score=0.899248 chunk_id=23188 preview=document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sony...
  5. score=0.893186 chunk_id=23345 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
- Matched markers: Viktor of North Orchard lane, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Viktor of North Orchard lane, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.771442 chunk_id=23374 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=0.760940 chunk_id=23375 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-nort...
  3. score=0.745032 chunk_id=23189 preview=document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops...
  4. score=0.710727 chunk_id=23465 preview=Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-...
  5. score=0.707878 chunk_id=23404 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
- Matched markers: Viktor of North Orchard lane, oak barrel hoops
- Missing markers: none
- Distractors: clay watering cup
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Viktor of North Orchard lane, oak barrel hoops. Distractors present: clay watering cup.
- Verdict: partial

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.799761 chunk_id=24175 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-nort...
  2. score=0.799667 chunk_id=24174 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distracto...
- Matched markers: Viktor of North Orchard lane, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Viktor of North Orchard lane, oak barrel hoops.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.891259 chunk_id=23989 preview=document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops...
  2. score=0.887396 chunk_id=24175 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-nort...
  3. score=0.884916 chunk_id=24174 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distracto...
- Matched markers: Viktor of North Orchard lane, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Viktor of North Orchard lane, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 24 - distractor-024
Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- blue glass jar

Expected distractors:
- Bridgefire Supper at South Meadow arch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.918691 chunk_id=23202 preview=document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Mor...
  2. score=0.909437 chunk_id=23377 preview=Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  3. score=0.908716 chunk_id=23376 preview=Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  4. score=0.896614 chunk_id=23201 preview=document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Mor...
  5. score=0.895132 chunk_id=23206 preview=document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at South Meadow arch, blue glass jar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, blue glass jar.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.758084 chunk_id=23377 preview=Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  2. score=0.751616 chunk_id=23376 preview=Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  3. score=0.702399 chunk_id=23202 preview=document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Mor...
  4. score=0.672835 chunk_id=23436 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  5. score=0.669845 chunk_id=23437 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
- Matched markers: Signal Lantern Morning at South Meadow arch, blue glass jar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, blue glass jar.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.784447 chunk_id=24176 preview=Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  2. score=0.759363 chunk_id=24177 preview=Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
- Matched markers: Signal Lantern Morning at South Meadow arch, blue glass jar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, blue glass jar.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.899396 chunk_id=24002 preview=document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Mor...
  2. score=0.895423 chunk_id=24177 preview=Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  3. score=0.886987 chunk_id=24006 preview=document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at South Meadow arch, blue glass jar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, blue glass jar.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 25 - distractor-025
Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora?

Expected evidence:
- Anton of Birch Ferry shed
- canal route map

Expected distractors:
- Zora of Birch Ferry shed

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.912667 chunk_id=23138 preview=document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry...
  2. score=0.911891 chunk_id=23379 preview=Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? document distractor-birch-ferry-shed-025::dist...
  3. score=0.911094 chunk_id=23378 preview=Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Case scope id: distractor-025. Scoped answer s...
  4. score=0.871430 chunk_id=23238 preview=document distractor-birch-ferry-shed-025::distractor-025::distractor: A conflicting note in document distractor-birch-ferry-shed-025 mentions Zora of Birch F...
  5. score=0.862280 chunk_id=23459 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::...
- Matched markers: Anton of Birch Ferry shed, canal route map
- Missing markers: none
- Distractors: Zora of Birch Ferry shed
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Anton of Birch Ferry shed, canal route map. Distractors present: Zora of Birch Ferry shed.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.782285 chunk_id=23378 preview=Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Case scope id: distractor-025. Scoped answer s...
  2. score=0.769538 chunk_id=23379 preview=Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? document distractor-birch-ferry-shed-025::dist...
  3. score=0.759682 chunk_id=23138 preview=document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry...
  4. score=0.637605 chunk_id=23458 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Case scope id: distractor-065. Scoped answer...
  5. score=0.636058 chunk_id=23468 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Case scope id: distractor-070. Scoped answer s...
- Matched markers: Anton of Birch Ferry shed, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Anton of Birch Ferry shed, canal route map.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.843107 chunk_id=24178 preview=Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Case scope id: distractor-025. Scoped answer s...
  2. score=0.793084 chunk_id=24179 preview=Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? document distractor-birch-ferry-shed-025::dist...
- Matched markers: Anton of Birch Ferry shed, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Anton of Birch Ferry shed, canal route map.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.905804 chunk_id=24179 preview=Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? document distractor-birch-ferry-shed-025::dist...
  2. score=0.897247 chunk_id=24178 preview=Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Case scope id: distractor-025. Scoped answer s...
  3. score=0.891985 chunk_id=23938 preview=document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry...
- Matched markers: Anton of Birch Ferry shed, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Anton of Birch Ferry shed, canal route map.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 26 - distractor-026
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

Expected evidence:
- March 18 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 19 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.931622 chunk_id=23164 preview=document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater...
  2. score=0.930362 chunk_id=23166 preview=document distractor-lantern-row-kiosk-056::distractor-056: In document distractor-lantern-row-kiosk-056, the verified archive note records March 12 Bellwater...
  3. score=0.930210 chunk_id=23168 preview=document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater...
  4. score=0.929893 chunk_id=23167 preview=document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater...
  5. score=0.928965 chunk_id=23165 preview=document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater...
- Matched markers: Lantern Row kiosk, March 18 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 18 Bellwater Fair.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.813781 chunk_id=23167 preview=document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater...
  2. score=0.811167 chunk_id=23163 preview=document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater...
  3. score=0.800529 chunk_id=23165 preview=document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater...
  4. score=0.799846 chunk_id=23470 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-071. Sco...
  5. score=0.797587 chunk_id=23168 preview=document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater...
- Matched markers: Lantern Row kiosk
- Missing markers: March 18 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 18 Bellwater Fair.
- Verdict: partial

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.801536 chunk_id=24300 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-086. Sco...
  2. score=0.799668 chunk_id=24270 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-071. Sco...
- Matched markers: Lantern Row kiosk
- Missing markers: March 18 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 18 Bellwater Fair.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.904796 chunk_id=24271 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  2. score=0.904193 chunk_id=24151 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
- Matched markers: Lantern Row kiosk
- Missing markers: March 18 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 18 Bellwater Fair.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 27 - distractor-027
Question: Which place held the true profile detail for Tomas, not the nearly identical place name?

Expected evidence:
- Cloud Wharf office
- copper token

Expected distractors:
- Fox Hollow bridge

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.830825 chunk_id=23383 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-cloud-wharf-office-027::distrac...
  2. score=0.824569 chunk_id=23463 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distracto...
  3. score=0.821804 chunk_id=23312 preview=document distractor-star-basin-gallery-080::distractor-080::distractor: A conflicting note in document distractor-star-basin-gallery-080 mentions Tomas of St...
  4. score=0.820433 chunk_id=23382 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-027. Scoped answer summar...
  5. score=0.813052 chunk_id=23462 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-067. Scoped answer summar...
- Matched markers: Cloud Wharf office, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, copper token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.693140 chunk_id=23463 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distracto...
  2. score=0.691478 chunk_id=23462 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-067. Scoped answer summar...
  3. score=0.689039 chunk_id=23382 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-027. Scoped answer summar...
  4. score=0.683050 chunk_id=23383 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-cloud-wharf-office-027::distrac...
  5. score=0.636371 chunk_id=23148 preview=document distractor-blue-trunk-cabin-067::distractor-067: In document distractor-blue-trunk-cabin-067, the verified archive note records Blue Trunk cabin, si...
- Matched markers: Cloud Wharf office, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, copper token.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.679751 chunk_id=24262 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-067. Scoped answer summar...
  2. score=0.674071 chunk_id=24263 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distracto...
- Matched markers: none
- Missing markers: Cloud Wharf office, copper token
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.849444 chunk_id=24263 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distracto...
  2. score=0.848492 chunk_id=24183 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-cloud-wharf-office-027::distrac...
- Matched markers: Cloud Wharf office, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Cloud Wharf office, copper token.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Earlier first relevant chunk (1 vs 3).

### Question 28 - distractor-028
Question: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

Expected evidence:
- moonflower cutting
- Vera of Ridge Post loft

Expected distractors:
- star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.912926 chunk_id=23196 preview=document distractor-ridge-post-loft-028::distractor-028: In document distractor-ridge-post-loft-028, the verified archive note records moonflower cutting, Ve...
  2. score=0.905874 chunk_id=23384 preview=Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-028...
  3. score=0.901206 chunk_id=23385 preview=Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-pos...
  4. score=0.889787 chunk_id=23200 preview=document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya...
  5. score=0.888450 chunk_id=23505 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
- Matched markers: Vera of Ridge Post loft, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vera of Ridge Post loft, moonflower cutting.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.778116 chunk_id=23385 preview=Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-pos...
  2. score=0.771910 chunk_id=23384 preview=Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-028...
  3. score=0.764446 chunk_id=23196 preview=document distractor-ridge-post-loft-028::distractor-028: In document distractor-ridge-post-loft-028, the verified archive note records moonflower cutting, Ve...
  4. score=0.736571 chunk_id=23355 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  5. score=0.730492 chunk_id=23354 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-01...
- Matched markers: Vera of Ridge Post loft, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vera of Ridge Post loft, moonflower cutting.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.814492 chunk_id=24184 preview=Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-028...
  2. score=0.774854 chunk_id=24185 preview=Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-pos...
- Matched markers: Vera of Ridge Post loft, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vera of Ridge Post loft, moonflower cutting.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.878041 chunk_id=24185 preview=Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-pos...
  2. score=0.873879 chunk_id=24184 preview=Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-028...
- Matched markers: Vera of Ridge Post loft, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vera of Ridge Post loft, moonflower cutting.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 29 - distractor-029
Question: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at Willow Courtyard well
- birch tea flask

Expected distractors:
- Bridgefire Supper at Willow Courtyard well

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.902647 chunk_id=23215 preview=document distractor-willow-courtyard-well-029::distractor-029: In document distractor-willow-courtyard-well-029, the verified archive note records Signal Lan...
  2. score=0.893005 chunk_id=23217 preview=document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lan...
  3. score=0.889840 chunk_id=23387 preview=Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
  4. score=0.888809 chunk_id=23446 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  5. score=0.887205 chunk_id=23386 preview=Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, birch tea flask.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.756180 chunk_id=23387 preview=Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
  2. score=0.755051 chunk_id=23386 preview=Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  3. score=0.725295 chunk_id=23446 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  4. score=0.724437 chunk_id=23447 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
  5. score=0.699653 chunk_id=23356 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, birch tea flask.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.790635 chunk_id=24186 preview=Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  2. score=0.784324 chunk_id=24187 preview=Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
  3. score=0.741202 chunk_id=24216 preview=Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, birch tea flask.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.897308 chunk_id=24015 preview=document distractor-willow-courtyard-well-029::distractor-029: In document distractor-willow-courtyard-well-029, the verified archive note records Signal Lan...
  2. score=0.893837 chunk_id=24017 preview=document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lan...
  3. score=0.887854 chunk_id=24247 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, birch tea flask.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 30 - distractor-030
Question: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris?

Expected evidence:
- Lina of Bell Bridge square
- saffron scarf

Expected distractors:
- Boris of Bell Bridge square

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.904959 chunk_id=23389 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? document distractor-bell-bridge-square-030::...
  2. score=0.896344 chunk_id=23388 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Case scope id: distractor-030. Scoped answer...
  3. score=0.894386 chunk_id=23132 preview=document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bri...
  4. score=0.868043 chunk_id=23232 preview=document distractor-bell-bridge-square-030::distractor-030::distractor: A conflicting note in document distractor-bell-bridge-square-030 mentions Boris of Be...
  5. score=0.863551 chunk_id=23133 preview=document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell B...
- Matched markers: Lina of Bell Bridge square, saffron scarf
- Missing markers: none
- Distractors: Boris of Bell Bridge square
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Lina of Bell Bridge square, saffron scarf. Distractors present: Boris of Bell Bridge square.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.752965 chunk_id=23388 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Case scope id: distractor-030. Scoped answer...
  2. score=0.749698 chunk_id=23389 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? document distractor-bell-bridge-square-030::...
  3. score=0.729284 chunk_id=23132 preview=document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bri...
  4. score=0.652009 chunk_id=23468 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Case scope id: distractor-070. Scoped answer s...
  5. score=0.650771 chunk_id=23469 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::dist...
- Matched markers: Lina of Bell Bridge square, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lina of Bell Bridge square, saffron scarf.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.799867 chunk_id=24188 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Case scope id: distractor-030. Scoped answer...
  2. score=0.782436 chunk_id=24189 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? document distractor-bell-bridge-square-030::...
- Matched markers: Lina of Bell Bridge square, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lina of Bell Bridge square, saffron scarf.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.882403 chunk_id=24189 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? document distractor-bell-bridge-square-030::...
  2. score=0.874774 chunk_id=23932 preview=document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bri...
  3. score=0.866120 chunk_id=24188 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Case scope id: distractor-030. Scoped answer...
- Matched markers: Lina of Bell Bridge square, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lina of Bell Bridge square, saffron scarf.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 31 - distractor-031
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

Expected evidence:
- March 23 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 24 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919438 chunk_id=23153 preview=document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwat...
  2. score=0.918574 chunk_id=23151 preview=document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwat...
  3. score=0.917531 chunk_id=23155 preview=document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwat...
  4. score=0.917407 chunk_id=23156 preview=document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwat...
  5. score=0.917248 chunk_id=23154 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
- Matched markers: Cedar Hill station
- Missing markers: March 23 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 23 Bellwater Fair.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.794214 chunk_id=23153 preview=document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwat...
  2. score=0.793285 chunk_id=23151 preview=document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwat...
  3. score=0.790958 chunk_id=23154 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
  4. score=0.790795 chunk_id=23152 preview=document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwat...
  5. score=0.789939 chunk_id=23390 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-031. Sc...
- Matched markers: Cedar Hill station, March 23 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 23 Bellwater Fair.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.827919 chunk_id=24280 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-076. Sc...
  2. score=0.827262 chunk_id=24160 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-016. Sc...
- Matched markers: Cedar Hill station
- Missing markers: March 23 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 23 Bellwater Fair.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.905928 chunk_id=24161 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  2. score=0.905119 chunk_id=24251 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
- Matched markers: Cedar Hill station
- Missing markers: March 23 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 23 Bellwater Fair.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 32 - distractor-032
Question: Which place held the true profile detail for Yara, not the nearly identical place name?

Expected evidence:
- Moon Mill yard
- amber lantern

Expected distractors:
- Hollow Market arcade

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.865289 chunk_id=23393 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-moon-mill-yard-032::distractor-0...
  2. score=0.852448 chunk_id=23392 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-032. Scoped answer summary...
  3. score=0.851507 chunk_id=23473 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-cloud-wharf-office-072::distract...
  4. score=0.849353 chunk_id=23472 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-072. Scoped answer summary...
  5. score=0.843170 chunk_id=23176 preview=document distractor-moon-mill-yard-032::distractor-032: In document distractor-moon-mill-yard-032, the verified archive note records Moon Mill yard, amber la...
- Matched markers: Moon Mill yard, amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, amber lantern.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.680391 chunk_id=23392 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-032. Scoped answer summary...
  2. score=0.680292 chunk_id=23472 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-072. Scoped answer summary...
  3. score=0.675812 chunk_id=23473 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-cloud-wharf-office-072::distract...
  4. score=0.672474 chunk_id=23393 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-moon-mill-yard-032::distractor-0...
  5. score=0.655243 chunk_id=23176 preview=document distractor-moon-mill-yard-032::distractor-032: In document distractor-moon-mill-yard-032, the verified archive note records Moon Mill yard, amber la...
- Matched markers: Moon Mill yard, amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, amber lantern.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.676179 chunk_id=24273 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-cloud-wharf-office-072::distract...
  2. score=0.671168 chunk_id=24193 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-moon-mill-yard-032::distractor-0...
  3. score=0.668407 chunk_id=24192 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-032. Scoped answer summary...
- Matched markers: Moon Mill yard, amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, amber lantern.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.861619 chunk_id=24273 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-cloud-wharf-office-072::distract...
  2. score=0.860143 chunk_id=24193 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-moon-mill-yard-032::distractor-0...
  3. score=0.854630 chunk_id=24192 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-032. Scoped answer summary...
- Matched markers: Moon Mill yard, amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, amber lantern.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 33 - distractor-033
Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

Expected evidence:
- basalt sketch
- Lev of Winter Chapel porch

Expected distractors:
- blue oar

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.922027 chunk_id=23221 preview=document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch,...
  2. score=0.918794 chunk_id=23394 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-...
  3. score=0.910012 chunk_id=23395 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter...
  4. score=0.885372 chunk_id=23475 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post...
  5. score=0.885362 chunk_id=23474 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-073....
- Matched markers: Lev of Winter Chapel porch, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev of Winter Chapel porch, basalt sketch.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.777380 chunk_id=23394 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-...
  2. score=0.766408 chunk_id=23395 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter...
  3. score=0.762608 chunk_id=23221 preview=document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch,...
  4. score=0.694472 chunk_id=23474 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-073....
  5. score=0.691754 chunk_id=23475 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post...
- Matched markers: Lev of Winter Chapel porch, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev of Winter Chapel porch, basalt sketch.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.819434 chunk_id=24194 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-...
  2. score=0.788492 chunk_id=24195 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter...
  3. score=0.752292 chunk_id=24254 preview=Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distract...
- Matched markers: Lev of Winter Chapel porch, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev of Winter Chapel porch, basalt sketch.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.892401 chunk_id=24195 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter...
  2. score=0.889030 chunk_id=24021 preview=document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch,...
- Matched markers: Lev of Winter Chapel porch, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev of Winter Chapel porch, basalt sketch.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 34 - distractor-034
Question: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at Marble stair hall
- green apron

Expected distractors:
- Bridgefire Supper at Marble stair hall

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.909244 chunk_id=23170 preview=document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Mor...
  2. score=0.900809 chunk_id=23396 preview=Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  3. score=0.896741 chunk_id=23397 preview=Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  4. score=0.890692 chunk_id=23173 preview=document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Mor...
  5. score=0.888831 chunk_id=23174 preview=document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at Marble stair hall, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, green apron.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.753443 chunk_id=23397 preview=Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  2. score=0.751426 chunk_id=23396 preview=Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  3. score=0.707801 chunk_id=23170 preview=document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Mor...
  4. score=0.661289 chunk_id=23516 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  5. score=0.657327 chunk_id=23457 preview=Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
- Matched markers: Signal Lantern Morning at Marble stair hall, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, green apron.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.797217 chunk_id=24196 preview=Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  2. score=0.748488 chunk_id=24197 preview=Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  3. score=0.713444 chunk_id=24286 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
- Matched markers: Signal Lantern Morning at Marble stair hall, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, green apron.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.899552 chunk_id=24197 preview=Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  2. score=0.893844 chunk_id=23970 preview=document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at Marble stair hall, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, green apron.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 35 - distractor-035
Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia?

Expected evidence:
- Pavel of Star Basin gallery
- silver booth token

Expected distractors:
- Talia of Star Basin gallery

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.907789 chunk_id=23399 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035:...
  2. score=0.902155 chunk_id=23398 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Case scope id: distractor-035. Scoped answe...
  3. score=0.900643 chunk_id=23209 preview=document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Ba...
  4. score=0.872006 chunk_id=23309 preview=document distractor-star-basin-gallery-035::distractor-035::distractor: A conflicting note in document distractor-star-basin-gallery-035 mentions Talia of St...
  5. score=0.852843 chunk_id=23479 preview=Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? document distractor-bell-bridge-square-075:...
- Matched markers: Pavel of Star Basin gallery, silver booth token
- Missing markers: none
- Distractors: Talia of Star Basin gallery
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Pavel of Star Basin gallery, silver booth token. Distractors present: Talia of Star Basin gallery.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.754833 chunk_id=23399 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035:...
  2. score=0.750608 chunk_id=23209 preview=document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Ba...
  3. score=0.745313 chunk_id=23398 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Case scope id: distractor-035. Scoped answe...
  4. score=0.620440 chunk_id=23479 preview=Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? document distractor-bell-bridge-square-075:...
  5. score=0.616146 chunk_id=23478 preview=Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Case scope id: distractor-075. Scoped answe...
- Matched markers: Pavel of Star Basin gallery, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Pavel of Star Basin gallery, silver booth token.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.855831 chunk_id=24198 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Case scope id: distractor-035. Scoped answe...
  2. score=0.816317 chunk_id=24199 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035:...
  3. score=0.755311 chunk_id=24009 preview=document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Ba...
- Matched markers: Pavel of Star Basin gallery, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Pavel of Star Basin gallery, silver booth token.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.895462 chunk_id=24199 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035:...
  2. score=0.888780 chunk_id=24009 preview=document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Ba...
- Matched markers: Pavel of Star Basin gallery, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Pavel of Star Basin gallery, silver booth token.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 36 - distractor-036
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

Expected evidence:
- March 10 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 11 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919557 chunk_id=23181 preview=document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellw...
  2. score=0.919384 chunk_id=23187 preview=document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellw...
  3. score=0.918695 chunk_id=23185 preview=document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellw...
  4. score=0.918667 chunk_id=23183 preview=document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellw...
  5. score=0.917342 chunk_id=23186 preview=document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellw...
- Matched markers: March 10 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 10 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.778081 chunk_id=23184 preview=document distractor-north-bell-workshop-051::distractor-051: In document distractor-north-bell-workshop-051, the verified archive note records March 25 Bellw...
  2. score=0.775997 chunk_id=23430 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-051. S...
  3. score=0.773384 chunk_id=23340 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-006. S...
  4. score=0.773188 chunk_id=23182 preview=document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellw...
  5. score=0.773136 chunk_id=23370 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-021. S...
- Matched markers: North Bell workshop
- Missing markers: March 10 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 10 Bellwater Fair.
- Verdict: partial

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.833872 chunk_id=24290 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-081. S...
  2. score=0.833841 chunk_id=24230 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-051. S...
  3. score=0.832436 chunk_id=24260 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. S...
- Matched markers: North Bell workshop
- Missing markers: March 10 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 10 Bellwater Fair.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.898039 chunk_id=24291 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=0.896125 chunk_id=24171 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=0.894784 chunk_id=24231 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
- Matched markers: North Bell workshop
- Missing markers: March 10 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 10 Bellwater Fair.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 37 - distractor-037
Question: Which place held the true profile detail for Damir, not the nearly identical place name?

Expected evidence:
- Blue Trunk cabin
- juniper bundles

Expected distractors:
- East Signal room

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.870004 chunk_id=23483 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-moon-mill-yard-077::distractor-...
  2. score=0.854946 chunk_id=23482 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-077. Scoped answer summar...
  3. score=0.854826 chunk_id=23403 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-blue-trunk-cabin-037::distracto...
  4. score=0.852169 chunk_id=23402 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-037. Scoped answer summar...
  5. score=0.850596 chunk_id=23236 preview=document distractor-bell-bridge-square-090::distractor-090::distractor: A conflicting note in document distractor-bell-bridge-square-090 mentions Damir of Be...
- Matched markers: Blue Trunk cabin, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, juniper bundles.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.675052 chunk_id=23482 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-077. Scoped answer summar...
  2. score=0.671307 chunk_id=23403 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-blue-trunk-cabin-037::distracto...
  3. score=0.671281 chunk_id=23402 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-037. Scoped answer summar...
  4. score=0.668988 chunk_id=23483 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-moon-mill-yard-077::distractor-...
  5. score=0.642893 chunk_id=23179 preview=document distractor-moon-mill-yard-077::distractor-077: In document distractor-moon-mill-yard-077, the verified archive note records Moon Mill yard, tin key....
- Matched markers: Blue Trunk cabin, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, juniper bundles.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.713515 chunk_id=24282 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-077. Scoped answer summar...
  2. score=0.708138 chunk_id=24202 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-037. Scoped answer summar...
- Matched markers: Blue Trunk cabin, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Blue Trunk cabin, juniper bundles.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.862122 chunk_id=24283 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-moon-mill-yard-077::distractor-...
  2. score=0.859158 chunk_id=24203 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-blue-trunk-cabin-037::distracto...
- Matched markers: Blue Trunk cabin, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Blue Trunk cabin, juniper bundles.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Earlier first relevant chunk (2 vs 3).

### Question 38 - distractor-038
Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

Expected evidence:
- smoke vent chain
- Nessa of North Orchard lane

Expected distractors:
- coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.905324 chunk_id=23190 preview=document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain...
  2. score=0.903791 chunk_id=23404 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  3. score=0.902103 chunk_id=23405 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  4. score=0.888541 chunk_id=23191 preview=document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Ves...
  5. score=0.882830 chunk_id=23224 preview=document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Ness...
- Matched markers: Nessa of North Orchard lane, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Nessa of North Orchard lane, smoke vent chain.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.786068 chunk_id=23404 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=0.774742 chunk_id=23405 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=0.763031 chunk_id=23190 preview=document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain...
  4. score=0.735252 chunk_id=23485 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  5. score=0.725268 chunk_id=23484 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
- Matched markers: Nessa of North Orchard lane, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Nessa of North Orchard lane, smoke vent chain.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.778865 chunk_id=24204 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=0.770425 chunk_id=24205 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=0.747792 chunk_id=24284 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
- Matched markers: Nessa of North Orchard lane, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Nessa of North Orchard lane, smoke vent chain.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.879136 chunk_id=24205 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  2. score=0.878819 chunk_id=23990 preview=document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain...
  3. score=0.873420 chunk_id=24204 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
- Matched markers: Nessa of North Orchard lane, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Nessa of North Orchard lane, smoke vent chain.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 39 - distractor-039
Question: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- brass compass

Expected distractors:
- Bridgefire Supper at South Meadow arch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.909298 chunk_id=23203 preview=document distractor-south-meadow-arch-039::distractor-039: In document distractor-south-meadow-arch-039, the verified archive note records Signal Lantern Mor...
  2. score=0.902223 chunk_id=23407 preview=Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  3. score=0.899443 chunk_id=23406 preview=Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  4. score=0.897138 chunk_id=23201 preview=document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Mor...
  5. score=0.894658 chunk_id=23206 preview=document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at South Meadow arch, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, brass compass.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.767790 chunk_id=23406 preview=Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  2. score=0.761120 chunk_id=23407 preview=Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  3. score=0.720906 chunk_id=23203 preview=document distractor-south-meadow-arch-039::distractor-039: In document distractor-south-meadow-arch-039, the verified archive note records Signal Lantern Mor...
  4. score=0.686481 chunk_id=23346 preview=Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  5. score=0.683334 chunk_id=23496 preview=Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
- Matched markers: Signal Lantern Morning at South Meadow arch, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, brass compass.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.799014 chunk_id=24206 preview=Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  2. score=0.787772 chunk_id=24207 preview=Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  3. score=0.737445 chunk_id=24286 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
- Matched markers: Signal Lantern Morning at South Meadow arch, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, brass compass.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.905783 chunk_id=24003 preview=document distractor-south-meadow-arch-039::distractor-039: In document distractor-south-meadow-arch-039, the verified archive note records Signal Lantern Mor...
  2. score=0.901707 chunk_id=24207 preview=Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  3. score=0.897279 chunk_id=24206 preview=Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
- Matched markers: Signal Lantern Morning at South Meadow arch, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, brass compass.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 40 - distractor-040
Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas?

Expected evidence:
- Mira of Birch Ferry shed
- linen wick

Expected distractors:
- Tomas of Birch Ferry shed

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.895359 chunk_id=23409 preview=Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? document distractor-birch-ferry-shed-040::dist...
  2. score=0.894103 chunk_id=23408 preview=Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Case scope id: distractor-040. Scoped answer s...
  3. score=0.888508 chunk_id=23139 preview=document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry...
  4. score=0.882805 chunk_id=23239 preview=document distractor-birch-ferry-shed-040::distractor-040::distractor: A conflicting note in document distractor-birch-ferry-shed-040 mentions Tomas of Birch...
  5. score=0.862427 chunk_id=23349 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? document distractor-birch-ferry-shed-010::dis...
- Matched markers: Mira of Birch Ferry shed, linen wick
- Missing markers: none
- Distractors: Tomas of Birch Ferry shed
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Mira of Birch Ferry shed, linen wick. Distractors present: Tomas of Birch Ferry shed.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.754543 chunk_id=23409 preview=Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? document distractor-birch-ferry-shed-040::dist...
  2. score=0.753269 chunk_id=23139 preview=document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry...
  3. score=0.750767 chunk_id=23408 preview=Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Case scope id: distractor-040. Scoped answer s...
  4. score=0.663871 chunk_id=23468 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Case scope id: distractor-070. Scoped answer s...
  5. score=0.660844 chunk_id=23469 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::dist...
- Matched markers: Mira of Birch Ferry shed, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Mira of Birch Ferry shed, linen wick.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.837908 chunk_id=24208 preview=Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Case scope id: distractor-040. Scoped answer s...
  2. score=0.783073 chunk_id=24209 preview=Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? document distractor-birch-ferry-shed-040::dist...
- Matched markers: Mira of Birch Ferry shed, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Mira of Birch Ferry shed, linen wick.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.895254 chunk_id=24209 preview=Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? document distractor-birch-ferry-shed-040::dist...
  2. score=0.881458 chunk_id=24208 preview=Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Case scope id: distractor-040. Scoped answer s...
  3. score=0.880173 chunk_id=23939 preview=document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry...
- Matched markers: Mira of Birch Ferry shed, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Mira of Birch Ferry shed, linen wick.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 41 - distractor-041
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

Expected evidence:
- March 15 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 16 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.931622 chunk_id=23164 preview=document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater...
  2. score=0.930362 chunk_id=23166 preview=document distractor-lantern-row-kiosk-056::distractor-056: In document distractor-lantern-row-kiosk-056, the verified archive note records March 12 Bellwater...
  3. score=0.930210 chunk_id=23168 preview=document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater...
  4. score=0.929893 chunk_id=23167 preview=document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater...
  5. score=0.928965 chunk_id=23165 preview=document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater...
- Matched markers: Lantern Row kiosk, March 15 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 15 Bellwater Fair.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.813781 chunk_id=23167 preview=document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater...
  2. score=0.811167 chunk_id=23163 preview=document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater...
  3. score=0.800529 chunk_id=23165 preview=document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater...
  4. score=0.799846 chunk_id=23470 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-071. Sco...
  5. score=0.797587 chunk_id=23168 preview=document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater...
- Matched markers: Lantern Row kiosk, March 15 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 15 Bellwater Fair.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.801536 chunk_id=24300 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-086. Sco...
  2. score=0.799668 chunk_id=24270 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-071. Sco...
- Matched markers: Lantern Row kiosk
- Missing markers: March 15 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 15 Bellwater Fair.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.904796 chunk_id=24271 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  2. score=0.904193 chunk_id=24151 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
- Matched markers: Lantern Row kiosk
- Missing markers: March 15 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 15 Bellwater Fair.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 42 - distractor-042
Question: Which place held the true profile detail for Kira, not the nearly identical place name?

Expected evidence:
- Cloud Wharf office
- lantern hook

Expected distractors:
- Fox Hollow bridge

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.845903 chunk_id=23493 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor...
  2. score=0.841617 chunk_id=23413 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-cloud-wharf-office-042::distract...
  3. score=0.833887 chunk_id=23412 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? Case scope id: distractor-042. Scoped answer summary...
  4. score=0.833689 chunk_id=23492 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? Case scope id: distractor-082. Scoped answer summary...
  5. score=0.822340 chunk_id=23313 preview=document distractor-star-basin-gallery-095::distractor-095::distractor: A conflicting note in document distractor-star-basin-gallery-095 mentions Kira of Sta...
- Matched markers: Cloud Wharf office, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.667478 chunk_id=23493 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor...
  2. score=0.662524 chunk_id=23492 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? Case scope id: distractor-082. Scoped answer summary...
  3. score=0.661373 chunk_id=23413 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-cloud-wharf-office-042::distract...
  4. score=0.660292 chunk_id=23412 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? Case scope id: distractor-042. Scoped answer summary...
  5. score=0.611391 chunk_id=23159 preview=document distractor-cloud-wharf-office-042::distractor-042: In document distractor-cloud-wharf-office-042, the verified archive note records Cloud Wharf offi...
- Matched markers: Cloud Wharf office, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, lantern hook.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.706678 chunk_id=24293 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor...
  2. score=0.702260 chunk_id=24292 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? Case scope id: distractor-082. Scoped answer summary...
  3. score=0.698868 chunk_id=24213 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-cloud-wharf-office-042::distract...
- Matched markers: Cloud Wharf office, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Partially grounded by: Cloud Wharf office, lantern hook.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.852699 chunk_id=24293 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor...
  2. score=0.844878 chunk_id=24213 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-cloud-wharf-office-042::distract...
  3. score=0.832716 chunk_id=24233 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor...
- Matched markers: Cloud Wharf office, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Cloud Wharf office, lantern hook.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Earlier first relevant chunk (2 vs 3).

### Question 43 - distractor-043
Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

Expected evidence:
- weathered camera strap
- Petar of Ridge Post loft

Expected distractors:
- blue glass jar

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.911213 chunk_id=23414 preview=Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-04...
  2. score=0.909878 chunk_id=23197 preview=document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap...
  3. score=0.898992 chunk_id=23415 preview=Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  4. score=0.883135 chunk_id=23200 preview=document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya...
  5. score=0.878586 chunk_id=23505 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
- Matched markers: Petar of Ridge Post loft, weathered camera strap
- Missing markers: none
- Distractors: blue glass jar
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Petar of Ridge Post loft, weathered camera strap. Distractors present: blue glass jar.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.788484 chunk_id=23414 preview=Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-04...
  2. score=0.788222 chunk_id=23197 preview=document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap...
  3. score=0.783201 chunk_id=23415 preview=Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  4. score=0.692447 chunk_id=23475 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post...
  5. score=0.685636 chunk_id=23199 preview=document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev...
- Matched markers: Petar of Ridge Post loft, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Petar of Ridge Post loft, weathered camera strap.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.815662 chunk_id=24214 preview=Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-04...
  2. score=0.785634 chunk_id=24215 preview=Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
- Matched markers: Petar of Ridge Post loft, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Petar of Ridge Post loft, weathered camera strap.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.886654 chunk_id=24215 preview=Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  2. score=0.884846 chunk_id=24214 preview=Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-04...
- Matched markers: Petar of Ridge Post loft, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Petar of Ridge Post loft, weathered camera strap.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 44 - distractor-044
Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at Willow Courtyard well
- wax thread

Expected distractors:
- Bridgefire Supper at Willow Courtyard well

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.911320 chunk_id=23216 preview=document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lan...
  2. score=0.903464 chunk_id=23416 preview=Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  3. score=0.895568 chunk_id=23417 preview=Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
  4. score=0.892438 chunk_id=23214 preview=document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lan...
  5. score=0.891462 chunk_id=23356 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.771436 chunk_id=23416 preview=Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  2. score=0.769799 chunk_id=23417 preview=Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
  3. score=0.715749 chunk_id=23216 preview=document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lan...
  4. score=0.713376 chunk_id=23357 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
  5. score=0.713025 chunk_id=23476 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, wax thread.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.794687 chunk_id=24216 preview=Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  2. score=0.742817 chunk_id=24217 preview=Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, wax thread.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.904815 chunk_id=24217 preview=Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
  2. score=0.902126 chunk_id=24016 preview=document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lan...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, wax thread.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 45 - distractor-045
Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara?

Expected evidence:
- Stefan of Bell Bridge square
- tin key

Expected distractors:
- Yara of Bell Bridge square

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.908716 chunk_id=23419 preview=Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? document distractor-bell-bridge-square-045:...
  2. score=0.903097 chunk_id=23418 preview=Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Case scope id: distractor-045. Scoped answe...
  3. score=0.894385 chunk_id=23133 preview=document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell B...
  4. score=0.877185 chunk_id=23233 preview=document distractor-bell-bridge-square-045::distractor-045::distractor: A conflicting note in document distractor-bell-bridge-square-045 mentions Yara of Bel...
  5. score=0.855836 chunk_id=23498 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Case scope id: distractor-085. Scoped answer...
- Matched markers: Stefan of Bell Bridge square, tin key
- Missing markers: none
- Distractors: Yara of Bell Bridge square
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Stefan of Bell Bridge square, tin key. Distractors present: Yara of Bell Bridge square.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.781670 chunk_id=23418 preview=Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Case scope id: distractor-045. Scoped answe...
  2. score=0.778259 chunk_id=23133 preview=document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell B...
  3. score=0.769825 chunk_id=23419 preview=Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? document distractor-bell-bridge-square-045:...
  4. score=0.665675 chunk_id=23498 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Case scope id: distractor-085. Scoped answer...
  5. score=0.647751 chunk_id=23499 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? document distractor-birch-ferry-shed-085::dis...
- Matched markers: Stefan of Bell Bridge square, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Stefan of Bell Bridge square, tin key.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.820394 chunk_id=24218 preview=Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Case scope id: distractor-045. Scoped answe...
  2. score=0.808381 chunk_id=24219 preview=Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? document distractor-bell-bridge-square-045:...
  3. score=0.733443 chunk_id=24159 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::d...
- Matched markers: Stefan of Bell Bridge square, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Stefan of Bell Bridge square, tin key.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.878957 chunk_id=24219 preview=Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? document distractor-bell-bridge-square-045:...
  2. score=0.868195 chunk_id=23933 preview=document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell B...
  3. score=0.867306 chunk_id=24218 preview=Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Case scope id: distractor-045. Scoped answe...
- Matched markers: Stefan of Bell Bridge square, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Stefan of Bell Bridge square, tin key.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 46 - distractor-046
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

Expected evidence:
- March 20 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 21 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919438 chunk_id=23153 preview=document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwat...
  2. score=0.918574 chunk_id=23151 preview=document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwat...
  3. score=0.917531 chunk_id=23155 preview=document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwat...
  4. score=0.917407 chunk_id=23156 preview=document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwat...
  5. score=0.917248 chunk_id=23154 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
- Matched markers: Cedar Hill station, March 20 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 20 Bellwater Fair.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.794214 chunk_id=23153 preview=document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwat...
  2. score=0.793285 chunk_id=23151 preview=document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwat...
  3. score=0.790958 chunk_id=23154 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
  4. score=0.790795 chunk_id=23152 preview=document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwat...
  5. score=0.789939 chunk_id=23390 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-031. Sc...
- Matched markers: Cedar Hill station, March 20 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 20 Bellwater Fair.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.827919 chunk_id=24280 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-076. Sc...
  2. score=0.827262 chunk_id=24160 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-016. Sc...
- Matched markers: Cedar Hill station
- Missing markers: March 20 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 20 Bellwater Fair.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.905928 chunk_id=24161 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  2. score=0.905119 chunk_id=24251 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
- Matched markers: Cedar Hill station
- Missing markers: March 20 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 20 Bellwater Fair.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 47 - distractor-047
Question: Which place held the true profile detail for Nikola, not the nearly identical place name?

Expected evidence:
- Moon Mill yard
- willow basket

Expected distractors:
- Hollow Market arcade

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.868769 chunk_id=23423 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-moon-mill-yard-047::distractor...
  2. score=0.861599 chunk_id=23343 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distract...
  3. score=0.861501 chunk_id=23503 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distra...
  4. score=0.861106 chunk_id=23502 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-087. Scoped answer summa...
  5. score=0.855479 chunk_id=23342 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-007. Scoped answer summa...
- Matched markers: Moon Mill yard, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Moon Mill yard, willow basket.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.682292 chunk_id=23343 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distract...
  2. score=0.679367 chunk_id=23342 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-007. Scoped answer summa...
  3. score=0.664020 chunk_id=23422 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-047. Scoped answer summa...
  4. score=0.663204 chunk_id=23502 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-087. Scoped answer summa...
  5. score=0.661656 chunk_id=23503 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distra...
- Matched markers: Moon Mill yard, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Partially grounded by: Moon Mill yard, willow basket.
- Verdict: partial

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.728338 chunk_id=24143 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distract...
  2. score=0.727059 chunk_id=24142 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-007. Scoped answer summa...
  3. score=0.697391 chunk_id=24222 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-047. Scoped answer summa...
- Matched markers: Moon Mill yard, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Partially grounded by: Moon Mill yard, willow basket.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.863421 chunk_id=24303 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distra...
  2. score=0.862430 chunk_id=24223 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-moon-mill-yard-047::distractor...
  3. score=0.851683 chunk_id=24143 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distract...
- Matched markers: Moon Mill yard, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Moon Mill yard, willow basket.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Earlier first relevant chunk (1 vs 3).

### Question 48 - distractor-048
Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

Expected evidence:
- paper moon mask
- Sonya of Winter Chapel porch

Expected distractors:
- birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.915502 chunk_id=23424 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=0.912381 chunk_id=23222 preview=document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mas...
  3. score=0.897508 chunk_id=23425 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  4. score=0.877546 chunk_id=23188 preview=document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sony...
  5. score=0.877106 chunk_id=23514 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
- Matched markers: Sonya of Winter Chapel porch, paper moon mask
- Missing markers: none
- Distractors: birch tea flask
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Sonya of Winter Chapel porch, paper moon mask. Distractors present: birch tea flask.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.783830 chunk_id=23425 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  2. score=0.780988 chunk_id=23424 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  3. score=0.776999 chunk_id=23222 preview=document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mas...
  4. score=0.695528 chunk_id=23344 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  5. score=0.683937 chunk_id=23365 preview=Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
- Matched markers: Sonya of Winter Chapel porch, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of Winter Chapel porch, paper moon mask.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.825738 chunk_id=24224 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=0.793924 chunk_id=24225 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  3. score=0.758419 chunk_id=24304 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-08...
- Matched markers: Sonya of Winter Chapel porch, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of Winter Chapel porch, paper moon mask.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.880567 chunk_id=24022 preview=document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mas...
  2. score=0.880266 chunk_id=24225 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  3. score=0.876570 chunk_id=24224 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
- Matched markers: Sonya of Winter Chapel porch, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of Winter Chapel porch, paper moon mask.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 49 - distractor-049
Question: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at Marble stair hall
- glass ink bottle

Expected distractors:
- Bridgefire Supper at Marble stair hall

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.898502 chunk_id=23171 preview=document distractor-marble-stair-hall-049::distractor-049: In document distractor-marble-stair-hall-049, the verified archive note records Signal Lantern Mor...
  2. score=0.895088 chunk_id=23173 preview=document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Mor...
  3. score=0.892452 chunk_id=23427 preview=Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? document distractor-marbl...
  4. score=0.890093 chunk_id=23172 preview=document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Mor...
  5. score=0.889589 chunk_id=23174 preview=document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at Marble stair hall, glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, glass ink bottle.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.766159 chunk_id=23427 preview=Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? document distractor-marbl...
  2. score=0.759867 chunk_id=23426 preview=Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor...
  3. score=0.729268 chunk_id=23171 preview=document distractor-marble-stair-hall-049::distractor-049: In document distractor-marble-stair-hall-049, the verified archive note records Signal Lantern Mor...
  4. score=0.691843 chunk_id=23516 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  5. score=0.684450 chunk_id=23517 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
- Matched markers: Signal Lantern Morning at Marble stair hall, glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, glass ink bottle.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.791590 chunk_id=24226 preview=Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor...
  2. score=0.732755 chunk_id=24227 preview=Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? document distractor-marbl...
  3. score=0.695704 chunk_id=24286 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
- Matched markers: Signal Lantern Morning at Marble stair hall, glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, glass ink bottle.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.899433 chunk_id=24227 preview=Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? document distractor-marbl...
  2. score=0.895985 chunk_id=23971 preview=document distractor-marble-stair-hall-049::distractor-049: In document distractor-marble-stair-hall-049, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at Marble stair hall, glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, glass ink bottle.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 50 - distractor-050
Question: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir?

Expected evidence:
- Selma of Star Basin gallery
- copper wind vane pin

Expected distractors:
- Damir of Star Basin gallery

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.906173 chunk_id=23429 preview=Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? document distractor-star-basin-gallery-050:...
  2. score=0.901590 chunk_id=23210 preview=document distractor-star-basin-gallery-050::distractor-050: In document distractor-star-basin-gallery-050, the verified archive note records Selma of Star Ba...
  3. score=0.899664 chunk_id=23428 preview=Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Case scope id: distractor-050. Scoped answe...
  4. score=0.877157 chunk_id=23310 preview=document distractor-star-basin-gallery-050::distractor-050::distractor: A conflicting note in document distractor-star-basin-gallery-050 mentions Damir of St...
  5. score=0.856105 chunk_id=23519 preview=Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? document distractor-star-basin-gallery-095::d...
- Matched markers: Selma of Star Basin gallery, copper wind vane pin
- Missing markers: none
- Distractors: Damir of Star Basin gallery
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Selma of Star Basin gallery, copper wind vane pin. Distractors present: Damir of Star Basin gallery.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.745067 chunk_id=23429 preview=Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? document distractor-star-basin-gallery-050:...
  2. score=0.725757 chunk_id=23428 preview=Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Case scope id: distractor-050. Scoped answe...
  3. score=0.702951 chunk_id=23210 preview=document distractor-star-basin-gallery-050::distractor-050: In document distractor-star-basin-gallery-050, the verified archive note records Selma of Star Ba...
  4. score=0.613697 chunk_id=23349 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? document distractor-birch-ferry-shed-010::dis...
  5. score=0.608542 chunk_id=23348 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Case scope id: distractor-010. Scoped answer...
- Matched markers: Selma of Star Basin gallery, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Star Basin gallery, copper wind vane pin.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.868434 chunk_id=24228 preview=Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Case scope id: distractor-050. Scoped answe...
  2. score=0.815558 chunk_id=24229 preview=Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? document distractor-star-basin-gallery-050:...
- Matched markers: Selma of Star Basin gallery, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Star Basin gallery, copper wind vane pin.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.893965 chunk_id=24229 preview=Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? document distractor-star-basin-gallery-050:...
  2. score=0.891117 chunk_id=24010 preview=document distractor-star-basin-gallery-050::distractor-050: In document distractor-star-basin-gallery-050, the verified archive note records Selma of Star Ba...
- Matched markers: Selma of Star Basin gallery, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Star Basin gallery, copper wind vane pin.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 51 - distractor-051
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

Expected evidence:
- March 25 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 26 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919557 chunk_id=23181 preview=document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellw...
  2. score=0.919384 chunk_id=23187 preview=document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellw...
  3. score=0.918695 chunk_id=23185 preview=document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellw...
  4. score=0.918667 chunk_id=23183 preview=document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellw...
  5. score=0.917342 chunk_id=23186 preview=document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellw...
- Matched markers: North Bell workshop
- Missing markers: March 25 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 25 Bellwater Fair.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.778081 chunk_id=23184 preview=document distractor-north-bell-workshop-051::distractor-051: In document distractor-north-bell-workshop-051, the verified archive note records March 25 Bellw...
  2. score=0.775997 chunk_id=23430 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-051. S...
  3. score=0.773384 chunk_id=23340 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-006. S...
  4. score=0.773188 chunk_id=23182 preview=document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellw...
  5. score=0.773136 chunk_id=23370 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-021. S...
- Matched markers: March 25 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 25 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.833872 chunk_id=24290 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-081. S...
  2. score=0.833841 chunk_id=24230 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-051. S...
  3. score=0.832436 chunk_id=24260 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. S...
- Matched markers: March 25 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 25 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.898039 chunk_id=24291 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=0.896125 chunk_id=24171 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=0.894784 chunk_id=24231 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
- Matched markers: March 25 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 25 Bellwater Fair, North Bell workshop.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 52 - distractor-052
Question: Which place held the true profile detail for Zora, not the nearly identical place name?

Expected evidence:
- Blue Trunk cabin
- violet ribbon

Expected distractors:
- East Signal room

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.867964 chunk_id=23513 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-0...
  2. score=0.861733 chunk_id=23353 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-cloud-wharf-office-012::distract...
  3. score=0.861349 chunk_id=23433 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor...
  4. score=0.856499 chunk_id=23512 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-092. Scoped answer summary...
  5. score=0.853114 chunk_id=23432 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary...
- Matched markers: Blue Trunk cabin, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, violet ribbon.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.697451 chunk_id=23432 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary...
  2. score=0.693872 chunk_id=23433 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor...
  3. score=0.689089 chunk_id=23512 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-092. Scoped answer summary...
  4. score=0.683521 chunk_id=23513 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-0...
  5. score=0.682850 chunk_id=23352 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-012. Scoped answer summary...
- Matched markers: Blue Trunk cabin, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, violet ribbon.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.748696 chunk_id=24232 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary...
  2. score=0.730016 chunk_id=24233 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor...
  3. score=0.710905 chunk_id=24313 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-0...
- Matched markers: Blue Trunk cabin, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, violet ribbon.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.856604 chunk_id=24313 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-0...
  2. score=0.855858 chunk_id=24153 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-cloud-wharf-office-012::distract...
- Matched markers: none
- Missing markers: Blue Trunk cabin, violet ribbon
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `bge_m3`
  - Earlier first relevant chunk (1 vs 3).

### Question 53 - distractor-053
Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

Expected evidence:
- tuning fork
- Vesna of North Orchard lane

Expected distractors:
- green apron

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.915927 chunk_id=23191 preview=document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Ves...
  2. score=0.910155 chunk_id=23434 preview=Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  3. score=0.905420 chunk_id=23435 preview=Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  4. score=0.893930 chunk_id=23404 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  5. score=0.891945 chunk_id=23190 preview=document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain...
- Matched markers: Vesna of North Orchard lane, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of North Orchard lane, tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.753667 chunk_id=23434 preview=Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=0.745049 chunk_id=23435 preview=Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=0.734416 chunk_id=23191 preview=document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Ves...
  4. score=0.709473 chunk_id=23404 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  5. score=0.700619 chunk_id=23405 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
- Matched markers: Vesna of North Orchard lane, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of North Orchard lane, tuning fork.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.788238 chunk_id=24234 preview=Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=0.771432 chunk_id=24235 preview=Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=0.770325 chunk_id=24154 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-01...
- Matched markers: Vesna of North Orchard lane, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of North Orchard lane, tuning fork.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.883984 chunk_id=23991 preview=document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Ves...
  2. score=0.882528 chunk_id=24235 preview=Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=0.870759 chunk_id=24234 preview=Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
- Matched markers: Vesna of North Orchard lane, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of North Orchard lane, tuning fork.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 54 - distractor-054
Question: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- rope bridge permit

Expected distractors:
- Bridgefire Supper at South Meadow arch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.908519 chunk_id=23204 preview=document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Mor...
  2. score=0.902083 chunk_id=23437 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  3. score=0.895635 chunk_id=23201 preview=document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Mor...
  4. score=0.895409 chunk_id=23436 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  5. score=0.894959 chunk_id=23206 preview=document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at South Meadow arch, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, rope bridge permit.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.767958 chunk_id=23436 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  2. score=0.767664 chunk_id=23437 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  3. score=0.711424 chunk_id=23204 preview=document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Mor...
  4. score=0.708277 chunk_id=23346 preview=Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  5. score=0.703097 chunk_id=23347 preview=Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? document distractor-south...
- Matched markers: Signal Lantern Morning at South Meadow arch, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, rope bridge permit.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.791356 chunk_id=24237 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  2. score=0.788604 chunk_id=24236 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
- Matched markers: Signal Lantern Morning at South Meadow arch, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, rope bridge permit.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.899255 chunk_id=24004 preview=document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Mor...
  2. score=0.892608 chunk_id=24001 preview=document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at South Meadow arch, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, rope bridge permit.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 55 - distractor-055
Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira?

Expected evidence:
- Ilya of Birch Ferry shed
- oak barrel hoops

Expected distractors:
- Kira of Birch Ferry shed

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.907858 chunk_id=23438 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Case scope id: distractor-055. Scoped answer su...
  2. score=0.907706 chunk_id=23140 preview=document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry...
  3. score=0.902951 chunk_id=23439 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? document distractor-birch-ferry-shed-055::distr...
  4. score=0.877565 chunk_id=23240 preview=document distractor-birch-ferry-shed-055::distractor-055::distractor: A conflicting note in document distractor-birch-ferry-shed-055 mentions Kira of Birch F...
  5. score=0.872075 chunk_id=23139 preview=document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry...
- Matched markers: Ilya of Birch Ferry shed, oak barrel hoops
- Missing markers: none
- Distractors: Kira of Birch Ferry shed
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Ilya of Birch Ferry shed, oak barrel hoops. Distractors present: Kira of Birch Ferry shed.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.770882 chunk_id=23438 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Case scope id: distractor-055. Scoped answer su...
  2. score=0.767115 chunk_id=23439 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? document distractor-birch-ferry-shed-055::distr...
  3. score=0.751989 chunk_id=23140 preview=document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry...
  4. score=0.665092 chunk_id=23518 preview=Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Case scope id: distractor-095. Scoped answer...
  5. score=0.649556 chunk_id=23519 preview=Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? document distractor-star-basin-gallery-095::d...
- Matched markers: Ilya of Birch Ferry shed, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Birch Ferry shed, oak barrel hoops.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.840046 chunk_id=24238 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Case scope id: distractor-055. Scoped answer su...
  2. score=0.802736 chunk_id=24239 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? document distractor-birch-ferry-shed-055::distr...
  3. score=0.749413 chunk_id=24158 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer...
- Matched markers: Ilya of Birch Ferry shed, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Birch Ferry shed, oak barrel hoops.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.893046 chunk_id=24239 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? document distractor-birch-ferry-shed-055::distr...
  2. score=0.890427 chunk_id=23940 preview=document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry...
- Matched markers: Ilya of Birch Ferry shed, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Birch Ferry shed, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 56 - distractor-056
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

Expected evidence:
- March 12 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 13 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.931622 chunk_id=23164 preview=document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater...
  2. score=0.930362 chunk_id=23166 preview=document distractor-lantern-row-kiosk-056::distractor-056: In document distractor-lantern-row-kiosk-056, the verified archive note records March 12 Bellwater...
  3. score=0.930210 chunk_id=23168 preview=document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater...
  4. score=0.929893 chunk_id=23167 preview=document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater...
  5. score=0.928965 chunk_id=23165 preview=document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater...
- Matched markers: Lantern Row kiosk, March 12 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 12 Bellwater Fair.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.813781 chunk_id=23167 preview=document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater...
  2. score=0.811167 chunk_id=23163 preview=document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater...
  3. score=0.800529 chunk_id=23165 preview=document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater...
  4. score=0.799846 chunk_id=23470 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-071. Sco...
  5. score=0.797587 chunk_id=23168 preview=document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater...
- Matched markers: Lantern Row kiosk
- Missing markers: March 12 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 12 Bellwater Fair.
- Verdict: partial

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.801536 chunk_id=24300 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-086. Sco...
  2. score=0.799668 chunk_id=24270 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-071. Sco...
- Matched markers: Lantern Row kiosk
- Missing markers: March 12 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 12 Bellwater Fair.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.904796 chunk_id=24271 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  2. score=0.904193 chunk_id=24151 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
- Matched markers: Lantern Row kiosk
- Missing markers: March 12 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 12 Bellwater Fair.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 57 - distractor-057
Question: Which place held the true profile detail for Boris, not the nearly identical place name?

Expected evidence:
- Cloud Wharf office
- canal route map

Expected distractors:
- Fox Hollow bridge

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.863999 chunk_id=23523 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distracto...
  2. score=0.859011 chunk_id=23443 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distrac...
  3. score=0.858929 chunk_id=23363 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-moon-mill-yard-017::distractor-...
  4. score=0.854487 chunk_id=23522 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summar...
  5. score=0.851230 chunk_id=23442 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-057. Scoped answer summar...
- Matched markers: Cloud Wharf office, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, canal route map.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.729616 chunk_id=23523 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distracto...
  2. score=0.708255 chunk_id=23522 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summar...
  3. score=0.693435 chunk_id=23443 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distrac...
  4. score=0.690946 chunk_id=23150 preview=document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, ba...
  5. score=0.687760 chunk_id=23442 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-057. Scoped answer summar...
- Matched markers: Cloud Wharf office, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, canal route map.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.694095 chunk_id=24323 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distracto...
  2. score=0.690519 chunk_id=24322 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summar...
- Matched markers: none
- Missing markers: Cloud Wharf office, canal route map
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.862998 chunk_id=24243 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distrac...
  2. score=0.862422 chunk_id=24323 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distracto...
- Matched markers: Cloud Wharf office, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Cloud Wharf office, canal route map.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Earlier first relevant chunk (2 vs 3).

### Question 58 - distractor-058
Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

Expected evidence:
- cedar shovel
- Daria of Ridge Post loft

Expected distractors:
- brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.916187 chunk_id=23198 preview=document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of...
  2. score=0.912302 chunk_id=23444 preview=Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-05...
  3. score=0.907267 chunk_id=23445 preview=Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  4. score=0.888875 chunk_id=23200 preview=document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya...
  5. score=0.886598 chunk_id=23504 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-08...
- Matched markers: Daria of Ridge Post loft, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of Ridge Post loft, cedar shovel.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.761229 chunk_id=23444 preview=Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-05...
  2. score=0.759831 chunk_id=23445 preview=Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  3. score=0.759380 chunk_id=23198 preview=document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of...
  4. score=0.716607 chunk_id=23505 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  5. score=0.714062 chunk_id=23200 preview=document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya...
- Matched markers: Daria of Ridge Post loft, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of Ridge Post loft, cedar shovel.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.813141 chunk_id=24244 preview=Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-05...
  2. score=0.784657 chunk_id=24245 preview=Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
- Matched markers: Daria of Ridge Post loft, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of Ridge Post loft, cedar shovel.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.885005 chunk_id=24244 preview=Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-05...
  2. score=0.884654 chunk_id=24245 preview=Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
- Matched markers: Daria of Ridge Post loft, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of Ridge Post loft, cedar shovel.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 59 - distractor-059
Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at Willow Courtyard well
- copper token

Expected distractors:
- Bridgefire Supper at Willow Courtyard well

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.906590 chunk_id=23217 preview=document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lan...
  2. score=0.899364 chunk_id=23214 preview=document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lan...
  3. score=0.897860 chunk_id=23446 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  4. score=0.895997 chunk_id=23356 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  5. score=0.893765 chunk_id=23215 preview=document distractor-willow-courtyard-well-029::distractor-029: In document distractor-willow-courtyard-well-029, the verified archive note records Signal Lan...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, copper token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.764740 chunk_id=23447 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
  2. score=0.761872 chunk_id=23446 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  3. score=0.725115 chunk_id=23386 preview=Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  4. score=0.724236 chunk_id=23387 preview=Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
  5. score=0.715416 chunk_id=23356 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, copper token.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.791002 chunk_id=24246 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  2. score=0.773599 chunk_id=24247 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, copper token.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.900911 chunk_id=24017 preview=document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lan...
  2. score=0.897127 chunk_id=24247 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
  3. score=0.889770 chunk_id=24246 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, copper token.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 60 - distractor-060
Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola?

Expected evidence:
- Ada of Bell Bridge square
- moonflower cutting

Expected distractors:
- Nikola of Bell Bridge square

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.905860 chunk_id=23449 preview=Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? document distractor-bell-bridge-square-060::...
  2. score=0.903529 chunk_id=23448 preview=Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Case scope id: distractor-060. Scoped answer...
  3. score=0.900143 chunk_id=23134 preview=document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Brid...
  4. score=0.876947 chunk_id=23234 preview=document distractor-bell-bridge-square-060::distractor-060::distractor: A conflicting note in document distractor-bell-bridge-square-060 mentions Nikola of B...
  5. score=0.865337 chunk_id=23369 preview=Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? document distractor-star-basin-gallery-020::...
- Matched markers: Ada of Bell Bridge square, moonflower cutting
- Missing markers: none
- Distractors: Nikola of Bell Bridge square
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Ada of Bell Bridge square, moonflower cutting. Distractors present: Nikola of Bell Bridge square.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.742954 chunk_id=23449 preview=Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? document distractor-bell-bridge-square-060::...
  2. score=0.740847 chunk_id=23448 preview=Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Case scope id: distractor-060. Scoped answer...
  3. score=0.725758 chunk_id=23134 preview=document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Brid...
  4. score=0.640951 chunk_id=23388 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Case scope id: distractor-030. Scoped answer...
  5. score=0.640708 chunk_id=23529 preview=Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? document distractor-birch-ferry-shed-100::dist...
- Matched markers: Ada of Bell Bridge square, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Bell Bridge square, moonflower cutting.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.801299 chunk_id=24248 preview=Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Case scope id: distractor-060. Scoped answer...
  2. score=0.784373 chunk_id=24249 preview=Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? document distractor-bell-bridge-square-060::...
- Matched markers: Ada of Bell Bridge square, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Bell Bridge square, moonflower cutting.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.892222 chunk_id=24249 preview=Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? document distractor-bell-bridge-square-060::...
  2. score=0.880455 chunk_id=23934 preview=document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Brid...
  3. score=0.870968 chunk_id=24248 preview=Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Case scope id: distractor-060. Scoped answer...
- Matched markers: Ada of Bell Bridge square, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Bell Bridge square, moonflower cutting.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 61 - distractor-061
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

Expected evidence:
- March 17 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 18 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919438 chunk_id=23153 preview=document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwat...
  2. score=0.918574 chunk_id=23151 preview=document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwat...
  3. score=0.917531 chunk_id=23155 preview=document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwat...
  4. score=0.917407 chunk_id=23156 preview=document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwat...
  5. score=0.917248 chunk_id=23154 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
- Matched markers: Cedar Hill station, March 17 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 17 Bellwater Fair.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.794214 chunk_id=23153 preview=document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwat...
  2. score=0.793285 chunk_id=23151 preview=document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwat...
  3. score=0.790958 chunk_id=23154 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
  4. score=0.790795 chunk_id=23152 preview=document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwat...
  5. score=0.789939 chunk_id=23390 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-031. Sc...
- Matched markers: Cedar Hill station, March 17 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 17 Bellwater Fair.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.827919 chunk_id=24280 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-076. Sc...
  2. score=0.827262 chunk_id=24160 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-016. Sc...
- Matched markers: Cedar Hill station
- Missing markers: March 17 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 17 Bellwater Fair.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.905928 chunk_id=24161 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  2. score=0.905119 chunk_id=24251 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
- Matched markers: Cedar Hill station, March 17 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 17 Bellwater Fair.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 62 - distractor-062
Question: Which place held the true profile detail for Talia, not the nearly identical place name?

Expected evidence:
- Moon Mill yard
- saffron scarf

Expected distractors:
- Hollow Market arcade

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.848770 chunk_id=23453 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-moon-mill-yard-062::distractor-...
  2. score=0.835635 chunk_id=23373 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distracto...
  3. score=0.834826 chunk_id=23309 preview=document distractor-star-basin-gallery-035::distractor-035::distractor: A conflicting note in document distractor-star-basin-gallery-035 mentions Talia of St...
  4. score=0.834271 chunk_id=23235 preview=document distractor-bell-bridge-square-075::distractor-075::distractor: A conflicting note in document distractor-bell-bridge-square-075 mentions Talia of Be...
  5. score=0.826403 chunk_id=23452 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? Case scope id: distractor-062. Scoped answer summar...
- Matched markers: Moon Mill yard, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, saffron scarf.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.692824 chunk_id=23452 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? Case scope id: distractor-062. Scoped answer summar...
  2. score=0.679683 chunk_id=23373 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distracto...
  3. score=0.677065 chunk_id=23372 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? Case scope id: distractor-022. Scoped answer summar...
  4. score=0.658683 chunk_id=23453 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-moon-mill-yard-062::distractor-...
  5. score=0.638404 chunk_id=23178 preview=document distractor-moon-mill-yard-062::distractor-062: In document distractor-moon-mill-yard-062, the verified archive note records Moon Mill yard, saffron...
- Matched markers: Moon Mill yard, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, saffron scarf.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.683242 chunk_id=24173 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distracto...
  2. score=0.678916 chunk_id=24172 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? Case scope id: distractor-022. Scoped answer summar...
- Matched markers: none
- Missing markers: Moon Mill yard, saffron scarf
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.851709 chunk_id=24253 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-moon-mill-yard-062::distractor-...
  2. score=0.845245 chunk_id=24173 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distracto...
  3. score=0.841174 chunk_id=23978 preview=document distractor-moon-mill-yard-062::distractor-062: In document distractor-moon-mill-yard-062, the verified archive note records Moon Mill yard, saffron...
- Matched markers: Moon Mill yard, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, saffron scarf.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 63 - distractor-063
Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

Expected evidence:
- carved shell comb
- Viktor of Winter Chapel porch

Expected distractors:
- wax thread

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.923901 chunk_id=23454 preview=Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distract...
  2. score=0.922833 chunk_id=23223 preview=document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell c...
  3. score=0.913447 chunk_id=23455 preview=Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-win...
  4. score=0.894365 chunk_id=23221 preview=document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch,...
  5. score=0.891754 chunk_id=23394 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-...
- Matched markers: Viktor of Winter Chapel porch, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Viktor of Winter Chapel porch, carved shell comb.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.758016 chunk_id=23455 preview=Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-win...
  2. score=0.748019 chunk_id=23454 preview=Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distract...
  3. score=0.742436 chunk_id=23223 preview=document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell c...
  4. score=0.701834 chunk_id=23374 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distracto...
  5. score=0.693544 chunk_id=23395 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter...
- Matched markers: Viktor of Winter Chapel porch, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Viktor of Winter Chapel porch, carved shell comb.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.817709 chunk_id=24254 preview=Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distract...
  2. score=0.793154 chunk_id=24255 preview=Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-win...
  3. score=0.736507 chunk_id=24194 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-...
- Matched markers: Viktor of Winter Chapel porch, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Viktor of Winter Chapel porch, carved shell comb.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.892517 chunk_id=24023 preview=document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell c...
  2. score=0.890126 chunk_id=24255 preview=Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-win...
- Matched markers: Viktor of Winter Chapel porch, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Viktor of Winter Chapel porch, carved shell comb.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 64 - distractor-064
Question: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at Marble stair hall
- amber lantern

Expected distractors:
- Bridgefire Supper at Marble stair hall

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.913115 chunk_id=23172 preview=document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Mor...
  2. score=0.906909 chunk_id=23456 preview=Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  3. score=0.905518 chunk_id=23457 preview=Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  4. score=0.890909 chunk_id=23173 preview=document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Mor...
  5. score=0.890661 chunk_id=23486 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
- Matched markers: Signal Lantern Morning at Marble stair hall, amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, amber lantern.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.756027 chunk_id=23457 preview=Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  2. score=0.740067 chunk_id=23456 preview=Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  3. score=0.707058 chunk_id=23172 preview=document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Mor...
  4. score=0.667275 chunk_id=23516 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  5. score=0.662378 chunk_id=23517 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
- Matched markers: Signal Lantern Morning at Marble stair hall, amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, amber lantern.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.764481 chunk_id=24256 preview=Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  2. score=0.719432 chunk_id=24286 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  3. score=0.719091 chunk_id=24226 preview=Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor...
- Matched markers: Signal Lantern Morning at Marble stair hall, amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, amber lantern.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.902860 chunk_id=24257 preview=Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  2. score=0.899569 chunk_id=23972 preview=document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at Marble stair hall, amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, amber lantern.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 65 - distractor-065
Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora?

Expected evidence:
- Anton of Star Basin gallery
- basalt sketch

Expected distractors:
- Zora of Star Basin gallery

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.921185 chunk_id=23459 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::...
  2. score=0.917746 chunk_id=23211 preview=document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Ba...
  3. score=0.911462 chunk_id=23458 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Case scope id: distractor-065. Scoped answer...
  4. score=0.871741 chunk_id=23311 preview=document distractor-star-basin-gallery-065::distractor-065::distractor: A conflicting note in document distractor-star-basin-gallery-065 mentions Zora of Sta...
  5. score=0.852834 chunk_id=23399 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035:...
- Matched markers: Anton of Star Basin gallery, basalt sketch
- Missing markers: none
- Distractors: Zora of Star Basin gallery
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Anton of Star Basin gallery, basalt sketch. Distractors present: Zora of Star Basin gallery.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.767192 chunk_id=23211 preview=document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Ba...
  2. score=0.765314 chunk_id=23458 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Case scope id: distractor-065. Scoped answer...
  3. score=0.765195 chunk_id=23459 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::...
  4. score=0.652032 chunk_id=23208 preview=document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basi...
  5. score=0.649569 chunk_id=23378 preview=Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Case scope id: distractor-025. Scoped answer s...
- Matched markers: Anton of Star Basin gallery, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Anton of Star Basin gallery, basalt sketch.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.875146 chunk_id=24258 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Case scope id: distractor-065. Scoped answer...
  2. score=0.844276 chunk_id=24259 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::...
  3. score=0.778687 chunk_id=24011 preview=document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Ba...
- Matched markers: Anton of Star Basin gallery, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Anton of Star Basin gallery, basalt sketch.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.897873 chunk_id=24259 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::...
  2. score=0.884413 chunk_id=24258 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Case scope id: distractor-065. Scoped answer...
- Matched markers: Anton of Star Basin gallery, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Anton of Star Basin gallery, basalt sketch.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 66 - distractor-066
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

Expected evidence:
- March 22 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 23 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919557 chunk_id=23181 preview=document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellw...
  2. score=0.919384 chunk_id=23187 preview=document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellw...
  3. score=0.918695 chunk_id=23185 preview=document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellw...
  4. score=0.918667 chunk_id=23183 preview=document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellw...
  5. score=0.917342 chunk_id=23186 preview=document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellw...
- Matched markers: March 22 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 22 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.778081 chunk_id=23184 preview=document distractor-north-bell-workshop-051::distractor-051: In document distractor-north-bell-workshop-051, the verified archive note records March 25 Bellw...
  2. score=0.775997 chunk_id=23430 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-051. S...
  3. score=0.773384 chunk_id=23340 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-006. S...
  4. score=0.773188 chunk_id=23182 preview=document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellw...
  5. score=0.773136 chunk_id=23370 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-021. S...
- Matched markers: North Bell workshop
- Missing markers: March 22 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 22 Bellwater Fair.
- Verdict: partial

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.833872 chunk_id=24290 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-081. S...
  2. score=0.833841 chunk_id=24230 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-051. S...
  3. score=0.832436 chunk_id=24260 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. S...
- Matched markers: March 22 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 22 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.898039 chunk_id=24291 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=0.896125 chunk_id=24171 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=0.894784 chunk_id=24231 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
- Matched markers: North Bell workshop
- Missing markers: March 22 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 22 Bellwater Fair.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 67 - distractor-067
Question: Which place held the true profile detail for Tomas, not the nearly identical place name?

Expected evidence:
- Blue Trunk cabin
- silver booth token

Expected distractors:
- East Signal room

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.830825 chunk_id=23383 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-cloud-wharf-office-027::distrac...
  2. score=0.824569 chunk_id=23463 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distracto...
  3. score=0.821804 chunk_id=23312 preview=document distractor-star-basin-gallery-080::distractor-080::distractor: A conflicting note in document distractor-star-basin-gallery-080 mentions Tomas of St...
  4. score=0.820433 chunk_id=23382 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-027. Scoped answer summar...
  5. score=0.813052 chunk_id=23462 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-067. Scoped answer summar...
- Matched markers: Blue Trunk cabin, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, silver booth token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.693140 chunk_id=23463 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distracto...
  2. score=0.691478 chunk_id=23462 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-067. Scoped answer summar...
  3. score=0.689039 chunk_id=23382 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-027. Scoped answer summar...
  4. score=0.683050 chunk_id=23383 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-cloud-wharf-office-027::distrac...
  5. score=0.636371 chunk_id=23148 preview=document distractor-blue-trunk-cabin-067::distractor-067: In document distractor-blue-trunk-cabin-067, the verified archive note records Blue Trunk cabin, si...
- Matched markers: Blue Trunk cabin, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, silver booth token.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.679751 chunk_id=24262 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-067. Scoped answer summar...
  2. score=0.674071 chunk_id=24263 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distracto...
- Matched markers: Blue Trunk cabin, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, silver booth token.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.849444 chunk_id=24263 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distracto...
  2. score=0.848492 chunk_id=24183 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-cloud-wharf-office-027::distrac...
- Matched markers: Blue Trunk cabin, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Blue Trunk cabin, silver booth token.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Earlier first relevant chunk (1 vs 2).

### Question 68 - distractor-068
Question: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

Expected evidence:
- clay watering cup
- Vera of North Orchard lane

Expected distractors:
- glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.905868 chunk_id=23464 preview=Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-...
  2. score=0.905473 chunk_id=23192 preview=document distractor-north-orchard-lane-068::distractor-068: In document distractor-north-orchard-lane-068, the verified archive note records clay watering cu...
  3. score=0.901188 chunk_id=23465 preview=Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-...
  4. score=0.882160 chunk_id=23194 preview=document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Dar...
  5. score=0.881606 chunk_id=23191 preview=document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Ves...
- Matched markers: Vera of North Orchard lane, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vera of North Orchard lane, clay watering cup.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.769814 chunk_id=23465 preview=Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-...
  2. score=0.767825 chunk_id=23464 preview=Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-...
  3. score=0.746620 chunk_id=23192 preview=document distractor-north-orchard-lane-068::distractor-068: In document distractor-north-orchard-lane-068, the verified archive note records clay watering cu...
  4. score=0.736044 chunk_id=23404 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  5. score=0.729505 chunk_id=23405 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
- Matched markers: Vera of North Orchard lane, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vera of North Orchard lane, clay watering cup.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.791694 chunk_id=24264 preview=Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-...
  2. score=0.780107 chunk_id=24265 preview=Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-...
  3. score=0.752586 chunk_id=24184 preview=Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-028...
- Matched markers: Vera of North Orchard lane, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vera of North Orchard lane, clay watering cup.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.886000 chunk_id=24265 preview=Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-...
  2. score=0.884460 chunk_id=23992 preview=document distractor-north-orchard-lane-068::distractor-068: In document distractor-north-orchard-lane-068, the verified archive note records clay watering cu...
  3. score=0.877960 chunk_id=24264 preview=Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-...
- Matched markers: Vera of North Orchard lane, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vera of North Orchard lane, clay watering cup.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 69 - distractor-069
Question: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- juniper bundles

Expected distractors:
- Bridgefire Supper at South Meadow arch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.913304 chunk_id=23205 preview=document distractor-south-meadow-arch-069::distractor-069: In document distractor-south-meadow-arch-069, the verified archive note records Signal Lantern Mor...
  2. score=0.904069 chunk_id=23467 preview=Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  3. score=0.901126 chunk_id=23201 preview=document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Mor...
  4. score=0.900572 chunk_id=23466 preview=Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  5. score=0.898491 chunk_id=23207 preview=document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at South Meadow arch, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, juniper bundles.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.744608 chunk_id=23526 preview=Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  2. score=0.739411 chunk_id=23467 preview=Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  3. score=0.738776 chunk_id=23527 preview=Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? document distractor-south...
  4. score=0.733593 chunk_id=23466 preview=Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  5. score=0.708849 chunk_id=23207 preview=document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at South Meadow arch, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, juniper bundles.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.804385 chunk_id=24266 preview=Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  2. score=0.801309 chunk_id=24267 preview=Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
- Matched markers: Signal Lantern Morning at South Meadow arch, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, juniper bundles.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.902456 chunk_id=24005 preview=document distractor-south-meadow-arch-069::distractor-069: In document distractor-south-meadow-arch-069, the verified archive note records Signal Lantern Mor...
  2. score=0.894186 chunk_id=24007 preview=document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at South Meadow arch, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, juniper bundles.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 70 - distractor-070
Question: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris?

Expected evidence:
- Lina of Birch Ferry shed
- smoke vent chain

Expected distractors:
- Boris of Birch Ferry shed

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.903054 chunk_id=23469 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::dist...
  2. score=0.900091 chunk_id=23468 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Case scope id: distractor-070. Scoped answer s...
  3. score=0.899021 chunk_id=23141 preview=document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry...
  4. score=0.879986 chunk_id=23139 preview=document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry...
  5. score=0.872901 chunk_id=23409 preview=Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? document distractor-birch-ferry-shed-040::dist...
- Matched markers: Lina of Birch Ferry shed, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lina of Birch Ferry shed, smoke vent chain.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.758948 chunk_id=23468 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Case scope id: distractor-070. Scoped answer s...
  2. score=0.752252 chunk_id=23469 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::dist...
  3. score=0.733353 chunk_id=23141 preview=document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry...
  4. score=0.656126 chunk_id=23389 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? document distractor-bell-bridge-square-030::...
  5. score=0.650126 chunk_id=23388 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Case scope id: distractor-030. Scoped answer...
- Matched markers: Lina of Birch Ferry shed, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lina of Birch Ferry shed, smoke vent chain.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.829730 chunk_id=24268 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Case scope id: distractor-070. Scoped answer s...
  2. score=0.777238 chunk_id=24269 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::dist...
- Matched markers: Lina of Birch Ferry shed, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lina of Birch Ferry shed, smoke vent chain.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.895449 chunk_id=24269 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::dist...
  2. score=0.883157 chunk_id=23941 preview=document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry...
- Matched markers: Lina of Birch Ferry shed, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lina of Birch Ferry shed, smoke vent chain.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 71 - distractor-071
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

Expected evidence:
- March 27 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 28 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.931622 chunk_id=23164 preview=document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater...
  2. score=0.930362 chunk_id=23166 preview=document distractor-lantern-row-kiosk-056::distractor-056: In document distractor-lantern-row-kiosk-056, the verified archive note records March 12 Bellwater...
  3. score=0.930210 chunk_id=23168 preview=document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater...
  4. score=0.929893 chunk_id=23167 preview=document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater...
  5. score=0.928965 chunk_id=23165 preview=document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater...
- Matched markers: Lantern Row kiosk, March 27 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 27 Bellwater Fair.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.813781 chunk_id=23167 preview=document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater...
  2. score=0.811167 chunk_id=23163 preview=document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater...
  3. score=0.800529 chunk_id=23165 preview=document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater...
  4. score=0.799846 chunk_id=23470 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-071. Sco...
  5. score=0.797587 chunk_id=23168 preview=document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater...
- Matched markers: Lantern Row kiosk, March 27 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 27 Bellwater Fair.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.801536 chunk_id=24300 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-086. Sco...
  2. score=0.799668 chunk_id=24270 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-071. Sco...
- Matched markers: Lantern Row kiosk, March 27 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 27 Bellwater Fair.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.904796 chunk_id=24271 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  2. score=0.904193 chunk_id=24151 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
- Matched markers: Lantern Row kiosk, March 27 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 27 Bellwater Fair.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 72 - distractor-072
Question: Which place held the true profile detail for Yara, not the nearly identical place name?

Expected evidence:
- Cloud Wharf office
- linen wick

Expected distractors:
- Fox Hollow bridge

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.865289 chunk_id=23393 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-moon-mill-yard-032::distractor-0...
  2. score=0.852448 chunk_id=23392 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-032. Scoped answer summary...
  3. score=0.851507 chunk_id=23473 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-cloud-wharf-office-072::distract...
  4. score=0.849353 chunk_id=23472 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-072. Scoped answer summary...
  5. score=0.843170 chunk_id=23176 preview=document distractor-moon-mill-yard-032::distractor-032: In document distractor-moon-mill-yard-032, the verified archive note records Moon Mill yard, amber la...
- Matched markers: Cloud Wharf office, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, linen wick.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.680391 chunk_id=23392 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-032. Scoped answer summary...
  2. score=0.680292 chunk_id=23472 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-072. Scoped answer summary...
  3. score=0.675812 chunk_id=23473 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-cloud-wharf-office-072::distract...
  4. score=0.672474 chunk_id=23393 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-moon-mill-yard-032::distractor-0...
  5. score=0.655243 chunk_id=23176 preview=document distractor-moon-mill-yard-032::distractor-032: In document distractor-moon-mill-yard-032, the verified archive note records Moon Mill yard, amber la...
- Matched markers: Cloud Wharf office, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, linen wick.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.676179 chunk_id=24273 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-cloud-wharf-office-072::distract...
  2. score=0.671168 chunk_id=24193 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-moon-mill-yard-032::distractor-0...
  3. score=0.668407 chunk_id=24192 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-032. Scoped answer summary...
- Matched markers: Cloud Wharf office, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Cloud Wharf office, linen wick.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.861619 chunk_id=24273 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-cloud-wharf-office-072::distract...
  2. score=0.860143 chunk_id=24193 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-moon-mill-yard-032::distractor-0...
  3. score=0.854630 chunk_id=24192 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? Case scope id: distractor-032. Scoped answer summary...
- Matched markers: Cloud Wharf office, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Cloud Wharf office, linen wick.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Earlier first relevant chunk (2 vs 3).

### Question 73 - distractor-073
Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

Expected evidence:
- star ledger page
- Lev of Ridge Post loft

Expected distractors:
- rope bridge permit

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919060 chunk_id=23199 preview=document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev...
  2. score=0.912328 chunk_id=23474 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-073....
  3. score=0.910522 chunk_id=23475 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post...
  4. score=0.884347 chunk_id=23200 preview=document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya...
  5. score=0.882477 chunk_id=23195 preview=document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridg...
- Matched markers: Lev of Ridge Post loft, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev of Ridge Post loft, star ledger page.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.794368 chunk_id=23474 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-073....
  2. score=0.791596 chunk_id=23475 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post...
  3. score=0.771069 chunk_id=23199 preview=document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev...
  4. score=0.698613 chunk_id=23414 preview=Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-04...
  5. score=0.697871 chunk_id=23415 preview=Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
- Matched markers: Lev of Ridge Post loft, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev of Ridge Post loft, star ledger page.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.805992 chunk_id=24274 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-073....
  2. score=0.792604 chunk_id=24275 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post...
- Matched markers: Lev of Ridge Post loft, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev of Ridge Post loft, star ledger page.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.898826 chunk_id=24275 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post...
  2. score=0.886557 chunk_id=23999 preview=document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev...
  3. score=0.886393 chunk_id=24274 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-073....
- Matched markers: Lev of Ridge Post loft, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev of Ridge Post loft, star ledger page.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 74 - distractor-074
Question: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at Willow Courtyard well
- lantern hook

Expected distractors:
- Bridgefire Supper at Willow Courtyard well

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.903452 chunk_id=23218 preview=document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lan...
  2. score=0.893119 chunk_id=23476 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  3. score=0.888594 chunk_id=23214 preview=document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lan...
  4. score=0.887717 chunk_id=23477 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
  5. score=0.886689 chunk_id=23356 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.778474 chunk_id=23477 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
  2. score=0.774287 chunk_id=23476 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  3. score=0.732431 chunk_id=23218 preview=document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lan...
  4. score=0.702158 chunk_id=23356 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  5. score=0.699225 chunk_id=23357 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, lantern hook.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.790946 chunk_id=24276 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  2. score=0.748456 chunk_id=24277 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, lantern hook.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.892896 chunk_id=24018 preview=document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lan...
  2. score=0.890595 chunk_id=24277 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
  3. score=0.881612 chunk_id=24276 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, lantern hook.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 75 - distractor-075
Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia?

Expected evidence:
- Pavel of Bell Bridge square
- weathered camera strap

Expected distractors:
- Talia of Bell Bridge square

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.907339 chunk_id=23479 preview=Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? document distractor-bell-bridge-square-075:...
  2. score=0.898340 chunk_id=23478 preview=Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Case scope id: distractor-075. Scoped answe...
  3. score=0.897649 chunk_id=23135 preview=document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Br...
  4. score=0.876816 chunk_id=23235 preview=document distractor-bell-bridge-square-075::distractor-075::distractor: A conflicting note in document distractor-bell-bridge-square-075 mentions Talia of Be...
  5. score=0.852628 chunk_id=23399 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035:...
- Matched markers: Pavel of Bell Bridge square, weathered camera strap
- Missing markers: none
- Distractors: Talia of Bell Bridge square
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Pavel of Bell Bridge square, weathered camera strap. Distractors present: Talia of Bell Bridge square.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.766478 chunk_id=23479 preview=Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? document distractor-bell-bridge-square-075:...
  2. score=0.751804 chunk_id=23478 preview=Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Case scope id: distractor-075. Scoped answe...
  3. score=0.735906 chunk_id=23135 preview=document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Br...
  4. score=0.642267 chunk_id=23209 preview=document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Ba...
  5. score=0.642107 chunk_id=23398 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Case scope id: distractor-035. Scoped answe...
- Matched markers: Pavel of Bell Bridge square, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Pavel of Bell Bridge square, weathered camera strap.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.832514 chunk_id=24278 preview=Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Case scope id: distractor-075. Scoped answe...
  2. score=0.824848 chunk_id=24279 preview=Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? document distractor-bell-bridge-square-075:...
- Matched markers: Pavel of Bell Bridge square, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Pavel of Bell Bridge square, weathered camera strap.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.886220 chunk_id=24279 preview=Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? document distractor-bell-bridge-square-075:...
  2. score=0.874647 chunk_id=23935 preview=document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Br...
  3. score=0.867526 chunk_id=24278 preview=Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Case scope id: distractor-075. Scoped answe...
- Matched markers: Pavel of Bell Bridge square, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Pavel of Bell Bridge square, weathered camera strap.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 76 - distractor-076
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

Expected evidence:
- March 14 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 15 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919438 chunk_id=23153 preview=document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwat...
  2. score=0.918574 chunk_id=23151 preview=document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwat...
  3. score=0.917531 chunk_id=23155 preview=document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwat...
  4. score=0.917407 chunk_id=23156 preview=document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwat...
  5. score=0.917248 chunk_id=23154 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
- Matched markers: Cedar Hill station, March 14 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 14 Bellwater Fair.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.794214 chunk_id=23153 preview=document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwat...
  2. score=0.793285 chunk_id=23151 preview=document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwat...
  3. score=0.790958 chunk_id=23154 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
  4. score=0.790795 chunk_id=23152 preview=document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwat...
  5. score=0.789939 chunk_id=23390 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-031. Sc...
- Matched markers: Cedar Hill station
- Missing markers: March 14 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 14 Bellwater Fair.
- Verdict: partial

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.827919 chunk_id=24280 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-076. Sc...
  2. score=0.827262 chunk_id=24160 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-016. Sc...
- Matched markers: Cedar Hill station, March 14 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 14 Bellwater Fair.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.905928 chunk_id=24161 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  2. score=0.905119 chunk_id=24251 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
- Matched markers: Cedar Hill station
- Missing markers: March 14 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 14 Bellwater Fair.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 77 - distractor-077
Question: Which place held the true profile detail for Damir, not the nearly identical place name?

Expected evidence:
- Moon Mill yard
- tin key

Expected distractors:
- Hollow Market arcade

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.870004 chunk_id=23483 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-moon-mill-yard-077::distractor-...
  2. score=0.854946 chunk_id=23482 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-077. Scoped answer summar...
  3. score=0.854826 chunk_id=23403 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-blue-trunk-cabin-037::distracto...
  4. score=0.852169 chunk_id=23402 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-037. Scoped answer summar...
  5. score=0.850596 chunk_id=23236 preview=document distractor-bell-bridge-square-090::distractor-090::distractor: A conflicting note in document distractor-bell-bridge-square-090 mentions Damir of Be...
- Matched markers: Moon Mill yard, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.675052 chunk_id=23482 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-077. Scoped answer summar...
  2. score=0.671307 chunk_id=23403 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-blue-trunk-cabin-037::distracto...
  3. score=0.671281 chunk_id=23402 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-037. Scoped answer summar...
  4. score=0.668988 chunk_id=23483 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-moon-mill-yard-077::distractor-...
  5. score=0.642893 chunk_id=23179 preview=document distractor-moon-mill-yard-077::distractor-077: In document distractor-moon-mill-yard-077, the verified archive note records Moon Mill yard, tin key....
- Matched markers: Moon Mill yard, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, tin key.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.713515 chunk_id=24282 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-077. Scoped answer summar...
  2. score=0.708138 chunk_id=24202 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-037. Scoped answer summar...
- Matched markers: Moon Mill yard, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Moon Mill yard, tin key.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.862122 chunk_id=24283 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-moon-mill-yard-077::distractor-...
  2. score=0.859158 chunk_id=24203 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-blue-trunk-cabin-037::distracto...
- Matched markers: Moon Mill yard, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Moon Mill yard, tin key.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 78 - distractor-078
Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

Expected evidence:
- blue oar
- Nessa of Winter Chapel porch

Expected distractors:
- copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.914597 chunk_id=23224 preview=document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Ness...
  2. score=0.910653 chunk_id=23484 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  3. score=0.906412 chunk_id=23485 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  4. score=0.897138 chunk_id=23225 preview=document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flas...
  5. score=0.894903 chunk_id=23514 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
- Matched markers: Nessa of Winter Chapel porch, blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Nessa of Winter Chapel porch, blue oar.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.769081 chunk_id=23485 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  2. score=0.767455 chunk_id=23484 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  3. score=0.759520 chunk_id=23224 preview=document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Ness...
  4. score=0.699458 chunk_id=23404 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  5. score=0.681701 chunk_id=23405 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
- Matched markers: Nessa of Winter Chapel porch, blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Nessa of Winter Chapel porch, blue oar.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.786244 chunk_id=24284 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=0.767846 chunk_id=24285 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  3. score=0.763710 chunk_id=24224 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
- Matched markers: Nessa of Winter Chapel porch, blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Nessa of Winter Chapel porch, blue oar.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.884128 chunk_id=24285 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  2. score=0.880290 chunk_id=24284 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  3. score=0.878387 chunk_id=24024 preview=document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Ness...
- Matched markers: Nessa of Winter Chapel porch, blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Nessa of Winter Chapel porch, blue oar.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 79 - distractor-079
Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at Marble stair hall
- willow basket

Expected distractors:
- Bridgefire Supper at Marble stair hall

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.910491 chunk_id=23173 preview=document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Mor...
  2. score=0.902926 chunk_id=23486 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  3. score=0.901612 chunk_id=23487 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  4. score=0.892963 chunk_id=23174 preview=document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Mor...
  5. score=0.888460 chunk_id=23170 preview=document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at Marble stair hall, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.750840 chunk_id=23487 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  2. score=0.748130 chunk_id=23486 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  3. score=0.707243 chunk_id=23173 preview=document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Mor...
  4. score=0.702577 chunk_id=23427 preview=Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? document distractor-marbl...
  5. score=0.696528 chunk_id=23516 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
- Matched markers: Signal Lantern Morning at Marble stair hall, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, willow basket.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.800649 chunk_id=24286 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  2. score=0.760159 chunk_id=24287 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
- Matched markers: Signal Lantern Morning at Marble stair hall, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, willow basket.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.902631 chunk_id=24287 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  2. score=0.896520 chunk_id=23973 preview=document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at Marble stair hall, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, willow basket.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 80 - distractor-080
Question: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas?

Expected evidence:
- Mira of Star Basin gallery
- paper moon mask

Expected distractors:
- Tomas of Star Basin gallery

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.887617 chunk_id=23489 preview=Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? document distractor-star-basin-gallery-080::...
  2. score=0.883294 chunk_id=23488 preview=Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Case scope id: distractor-080. Scoped answer...
  3. score=0.873981 chunk_id=23212 preview=document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Bas...
  4. score=0.872030 chunk_id=23312 preview=document distractor-star-basin-gallery-080::distractor-080::distractor: A conflicting note in document distractor-star-basin-gallery-080 mentions Tomas of St...
  5. score=0.852035 chunk_id=23429 preview=Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? document distractor-star-basin-gallery-050:...
- Matched markers: Mira of Star Basin gallery, paper moon mask
- Missing markers: none
- Distractors: Tomas of Star Basin gallery
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Mira of Star Basin gallery, paper moon mask. Distractors present: Tomas of Star Basin gallery.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.768546 chunk_id=23212 preview=document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Bas...
  2. score=0.767053 chunk_id=23489 preview=Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? document distractor-star-basin-gallery-080::...
  3. score=0.763168 chunk_id=23488 preview=Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Case scope id: distractor-080. Scoped answer...
  4. score=0.625775 chunk_id=23368 preview=Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Case scope id: distractor-020. Scoped answer...
  5. score=0.625509 chunk_id=23369 preview=Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? document distractor-star-basin-gallery-020::...
- Matched markers: Mira of Star Basin gallery, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Mira of Star Basin gallery, paper moon mask.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.843174 chunk_id=24288 preview=Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Case scope id: distractor-080. Scoped answer...
  2. score=0.818121 chunk_id=24289 preview=Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? document distractor-star-basin-gallery-080::...
  3. score=0.748821 chunk_id=24258 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Case scope id: distractor-065. Scoped answer...
- Matched markers: Mira of Star Basin gallery, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Mira of Star Basin gallery, paper moon mask.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.892091 chunk_id=24289 preview=Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? document distractor-star-basin-gallery-080::...
  2. score=0.882355 chunk_id=24012 preview=document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Bas...
- Matched markers: Mira of Star Basin gallery, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Mira of Star Basin gallery, paper moon mask.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 81 - distractor-081
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

Expected evidence:
- March 19 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 20 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919557 chunk_id=23181 preview=document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellw...
  2. score=0.919384 chunk_id=23187 preview=document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellw...
  3. score=0.918695 chunk_id=23185 preview=document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellw...
  4. score=0.918667 chunk_id=23183 preview=document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellw...
  5. score=0.917342 chunk_id=23186 preview=document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellw...
- Matched markers: March 19 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 19 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.778081 chunk_id=23184 preview=document distractor-north-bell-workshop-051::distractor-051: In document distractor-north-bell-workshop-051, the verified archive note records March 25 Bellw...
  2. score=0.775997 chunk_id=23430 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-051. S...
  3. score=0.773384 chunk_id=23340 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-006. S...
  4. score=0.773188 chunk_id=23182 preview=document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellw...
  5. score=0.773136 chunk_id=23370 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-021. S...
- Matched markers: North Bell workshop
- Missing markers: March 19 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 19 Bellwater Fair.
- Verdict: partial

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.833872 chunk_id=24290 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-081. S...
  2. score=0.833841 chunk_id=24230 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-051. S...
  3. score=0.832436 chunk_id=24260 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. S...
- Matched markers: March 19 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 19 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.898039 chunk_id=24291 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=0.896125 chunk_id=24171 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=0.894784 chunk_id=24231 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
- Matched markers: March 19 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 19 Bellwater Fair, North Bell workshop.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 82 - distractor-082
Question: Which place held the true profile detail for Kira, not the nearly identical place name?

Expected evidence:
- Blue Trunk cabin
- copper wind vane pin

Expected distractors:
- East Signal room

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.845903 chunk_id=23493 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor...
  2. score=0.841617 chunk_id=23413 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-cloud-wharf-office-042::distract...
  3. score=0.833887 chunk_id=23412 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? Case scope id: distractor-042. Scoped answer summary...
  4. score=0.833689 chunk_id=23492 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? Case scope id: distractor-082. Scoped answer summary...
  5. score=0.822340 chunk_id=23313 preview=document distractor-star-basin-gallery-095::distractor-095::distractor: A conflicting note in document distractor-star-basin-gallery-095 mentions Kira of Sta...
- Matched markers: Blue Trunk cabin, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, copper wind vane pin.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.667478 chunk_id=23493 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor...
  2. score=0.662524 chunk_id=23492 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? Case scope id: distractor-082. Scoped answer summary...
  3. score=0.661373 chunk_id=23413 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-cloud-wharf-office-042::distract...
  4. score=0.660292 chunk_id=23412 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? Case scope id: distractor-042. Scoped answer summary...
  5. score=0.611391 chunk_id=23159 preview=document distractor-cloud-wharf-office-042::distractor-042: In document distractor-cloud-wharf-office-042, the verified archive note records Cloud Wharf offi...
- Matched markers: Blue Trunk cabin, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, copper wind vane pin.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.706678 chunk_id=24293 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor...
  2. score=0.702260 chunk_id=24292 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? Case scope id: distractor-082. Scoped answer summary...
  3. score=0.698868 chunk_id=24213 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-cloud-wharf-office-042::distract...
- Matched markers: Blue Trunk cabin, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, copper wind vane pin.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.852699 chunk_id=24293 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor...
  2. score=0.844878 chunk_id=24213 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-cloud-wharf-office-042::distract...
  3. score=0.832716 chunk_id=24233 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor...
- Matched markers: Blue Trunk cabin, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, copper wind vane pin.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 83 - distractor-083
Question: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

Expected evidence:
- coal stove hiss
- Petar of North Orchard lane

Expected distractors:
- amber lantern

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.906139 chunk_id=23495 preview=Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  2. score=0.905115 chunk_id=23193 preview=document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss,...
  3. score=0.899154 chunk_id=23494 preview=Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  4. score=0.878507 chunk_id=23188 preview=document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sony...
  5. score=0.877485 chunk_id=23344 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
- Matched markers: Petar of North Orchard lane, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Petar of North Orchard lane, coal stove hiss.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.776189 chunk_id=23494 preview=Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=0.771318 chunk_id=23495 preview=Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=0.745967 chunk_id=23193 preview=document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss,...
  4. score=0.690994 chunk_id=23374 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distracto...
  5. score=0.687641 chunk_id=23375 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-nort...
- Matched markers: Petar of North Orchard lane, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Petar of North Orchard lane, coal stove hiss.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.777712 chunk_id=24294 preview=Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=0.769190 chunk_id=24295 preview=Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
- Matched markers: Petar of North Orchard lane, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Petar of North Orchard lane, coal stove hiss.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.879137 chunk_id=23993 preview=document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss,...
  2. score=0.878497 chunk_id=24295 preview=Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
- Matched markers: Petar of North Orchard lane, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Petar of North Orchard lane, coal stove hiss.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 84 - distractor-084
Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- violet ribbon

Expected distractors:
- Bridgefire Supper at South Meadow arch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.921430 chunk_id=23206 preview=document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Mor...
  2. score=0.912262 chunk_id=23496 preview=Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  3. score=0.907093 chunk_id=23497 preview=Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? document distractor-south...
  4. score=0.895356 chunk_id=23204 preview=document distractor-south-meadow-arch-054::distractor-054: In document distractor-south-meadow-arch-054, the verified archive note records Signal Lantern Mor...
  5. score=0.895177 chunk_id=23201 preview=document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at South Meadow arch, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, violet ribbon.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.758625 chunk_id=23496 preview=Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  2. score=0.757695 chunk_id=23497 preview=Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? document distractor-south...
  3. score=0.701658 chunk_id=23206 preview=document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Mor...
  4. score=0.693011 chunk_id=23437 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  5. score=0.690860 chunk_id=23436 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
- Matched markers: Signal Lantern Morning at South Meadow arch, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, violet ribbon.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.790640 chunk_id=24296 preview=Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  2. score=0.767093 chunk_id=24297 preview=Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? document distractor-south...
  3. score=0.728554 chunk_id=24237 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
- Matched markers: Signal Lantern Morning at South Meadow arch, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, violet ribbon.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.903493 chunk_id=24006 preview=document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Mor...
  2. score=0.896315 chunk_id=24297 preview=Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? document distractor-south...
  3. score=0.894309 chunk_id=24296 preview=Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
- Matched markers: Signal Lantern Morning at South Meadow arch, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, violet ribbon.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 85 - distractor-085
Question: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara?

Expected evidence:
- Stefan of Birch Ferry shed
- tuning fork

Expected distractors:
- Yara of Birch Ferry shed

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.910098 chunk_id=23498 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Case scope id: distractor-085. Scoped answer...
  2. score=0.909905 chunk_id=23499 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? document distractor-birch-ferry-shed-085::dis...
  3. score=0.907948 chunk_id=23142 preview=document distractor-birch-ferry-shed-085::distractor-085: In document distractor-birch-ferry-shed-085, the verified archive note records Stefan of Birch Ferr...
  4. score=0.882182 chunk_id=23242 preview=document distractor-birch-ferry-shed-085::distractor-085::distractor: A conflicting note in document distractor-birch-ferry-shed-085 mentions Yara of Birch F...
  5. score=0.858665 chunk_id=23137 preview=document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry...
- Matched markers: Stefan of Birch Ferry shed, tuning fork
- Missing markers: none
- Distractors: Yara of Birch Ferry shed
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Stefan of Birch Ferry shed, tuning fork. Distractors present: Yara of Birch Ferry shed.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.770355 chunk_id=23498 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Case scope id: distractor-085. Scoped answer...
  2. score=0.745991 chunk_id=23499 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? document distractor-birch-ferry-shed-085::dis...
  3. score=0.741353 chunk_id=23142 preview=document distractor-birch-ferry-shed-085::distractor-085: In document distractor-birch-ferry-shed-085, the verified archive note records Stefan of Birch Ferr...
  4. score=0.661779 chunk_id=23418 preview=Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Case scope id: distractor-045. Scoped answe...
  5. score=0.661475 chunk_id=23133 preview=document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell B...
- Matched markers: Stefan of Birch Ferry shed, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Stefan of Birch Ferry shed, tuning fork.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.833366 chunk_id=24298 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Case scope id: distractor-085. Scoped answer...
  2. score=0.788563 chunk_id=24299 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? document distractor-birch-ferry-shed-085::dis...
  3. score=0.748298 chunk_id=24238 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Case scope id: distractor-055. Scoped answer su...
- Matched markers: Stefan of Birch Ferry shed, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Stefan of Birch Ferry shed, tuning fork.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.896951 chunk_id=24299 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? document distractor-birch-ferry-shed-085::dis...
  2. score=0.886311 chunk_id=24298 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Case scope id: distractor-085. Scoped answer...
- Matched markers: Stefan of Birch Ferry shed, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Stefan of Birch Ferry shed, tuning fork.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 86 - distractor-086
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?

Expected evidence:
- March 24 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 25 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.931622 chunk_id=23164 preview=document distractor-lantern-row-kiosk-026::distractor-026: In document distractor-lantern-row-kiosk-026, the verified archive note records March 18 Bellwater...
  2. score=0.930362 chunk_id=23166 preview=document distractor-lantern-row-kiosk-056::distractor-056: In document distractor-lantern-row-kiosk-056, the verified archive note records March 12 Bellwater...
  3. score=0.930210 chunk_id=23168 preview=document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater...
  4. score=0.929893 chunk_id=23167 preview=document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater...
  5. score=0.928965 chunk_id=23165 preview=document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater...
- Matched markers: Lantern Row kiosk, March 24 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 24 Bellwater Fair.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.813781 chunk_id=23167 preview=document distractor-lantern-row-kiosk-071::distractor-071: In document distractor-lantern-row-kiosk-071, the verified archive note records March 27 Bellwater...
  2. score=0.811167 chunk_id=23163 preview=document distractor-lantern-row-kiosk-011::distractor-011: In document distractor-lantern-row-kiosk-011, the verified archive note records March 21 Bellwater...
  3. score=0.800529 chunk_id=23165 preview=document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater...
  4. score=0.799846 chunk_id=23470 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-071. Sco...
  5. score=0.797587 chunk_id=23168 preview=document distractor-lantern-row-kiosk-086::distractor-086: In document distractor-lantern-row-kiosk-086, the verified archive note records March 24 Bellwater...
- Matched markers: Lantern Row kiosk, March 24 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 24 Bellwater Fair.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.801536 chunk_id=24300 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-086. Sco...
  2. score=0.799668 chunk_id=24270 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-071. Sco...
- Matched markers: Lantern Row kiosk, March 24 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 24 Bellwater Fair.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.904796 chunk_id=24271 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  2. score=0.904193 chunk_id=24151 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
- Matched markers: Lantern Row kiosk
- Missing markers: March 24 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 24 Bellwater Fair.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 87 - distractor-087
Question: Which place held the true profile detail for Nikola, not the nearly identical place name?

Expected evidence:
- Cloud Wharf office
- oak barrel hoops

Expected distractors:
- Fox Hollow bridge

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.868769 chunk_id=23423 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-moon-mill-yard-047::distractor...
  2. score=0.861599 chunk_id=23343 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distract...
  3. score=0.861501 chunk_id=23503 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distra...
  4. score=0.861106 chunk_id=23502 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-087. Scoped answer summa...
  5. score=0.855479 chunk_id=23342 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-007. Scoped answer summa...
- Matched markers: Cloud Wharf office, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.682292 chunk_id=23343 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distract...
  2. score=0.679367 chunk_id=23342 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-007. Scoped answer summa...
  3. score=0.664020 chunk_id=23422 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-047. Scoped answer summa...
  4. score=0.663204 chunk_id=23502 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-087. Scoped answer summa...
  5. score=0.661656 chunk_id=23503 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distra...
- Matched markers: Cloud Wharf office, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 4
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, oak barrel hoops.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.728338 chunk_id=24143 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distract...
  2. score=0.727059 chunk_id=24142 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-007. Scoped answer summa...
  3. score=0.697391 chunk_id=24222 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-047. Scoped answer summa...
- Matched markers: none
- Missing markers: Cloud Wharf office, oak barrel hoops
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.863421 chunk_id=24303 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distra...
  2. score=0.862430 chunk_id=24223 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-moon-mill-yard-047::distractor...
  3. score=0.851683 chunk_id=24143 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distract...
- Matched markers: Cloud Wharf office, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Cloud Wharf office, oak barrel hoops.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Earlier first relevant chunk (3 vs 4).

### Question 88 - distractor-088
Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?

Expected evidence:
- blue glass jar
- Sonya of Ridge Post loft

Expected distractors:
- juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.918694 chunk_id=23200 preview=document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya...
  2. score=0.909000 chunk_id=23504 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-08...
  3. score=0.908863 chunk_id=23505 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  4. score=0.880438 chunk_id=23199 preview=document distractor-ridge-post-loft-073::distractor-073: In document distractor-ridge-post-loft-073, the verified archive note records star ledger page, Lev...
  5. score=0.879420 chunk_id=23195 preview=document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridg...
- Matched markers: Sonya of Ridge Post loft, blue glass jar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of Ridge Post loft, blue glass jar.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.776918 chunk_id=23504 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-08...
  2. score=0.775329 chunk_id=23200 preview=document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya...
  3. score=0.774278 chunk_id=23505 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  4. score=0.705021 chunk_id=23425 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  5. score=0.704692 chunk_id=23444 preview=Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-05...
- Matched markers: Sonya of Ridge Post loft, blue glass jar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of Ridge Post loft, blue glass jar.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.822299 chunk_id=24304 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-08...
  2. score=0.782016 chunk_id=24305 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  3. score=0.758925 chunk_id=24224 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
- Matched markers: Sonya of Ridge Post loft, blue glass jar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of Ridge Post loft, blue glass jar.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.877940 chunk_id=24305 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  2. score=0.872909 chunk_id=24304 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-08...
  3. score=0.866813 chunk_id=24000 preview=document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya...
- Matched markers: Sonya of Ridge Post loft, blue glass jar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of Ridge Post loft, blue glass jar.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 89 - distractor-089
Question: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at Willow Courtyard well
- canal route map

Expected distractors:
- Bridgefire Supper at Willow Courtyard well

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.907987 chunk_id=23219 preview=document distractor-willow-courtyard-well-089::distractor-089: In document distractor-willow-courtyard-well-089, the verified archive note records Signal Lan...
  2. score=0.896427 chunk_id=23506 preview=Question anchor: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  3. score=0.892025 chunk_id=23507 preview=Question anchor: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
  4. score=0.885986 chunk_id=23214 preview=document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lan...
  5. score=0.882926 chunk_id=23218 preview=document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lan...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, canal route map.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.773872 chunk_id=23507 preview=Question anchor: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
  2. score=0.772958 chunk_id=23506 preview=Question anchor: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  3. score=0.731344 chunk_id=23219 preview=document distractor-willow-courtyard-well-089::distractor-089: In document distractor-willow-courtyard-well-089, the verified archive note records Signal Lan...
  4. score=0.708933 chunk_id=23356 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  5. score=0.701802 chunk_id=23357 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, canal route map.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.755763 chunk_id=24306 preview=Question anchor: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  2. score=0.720009 chunk_id=24307 preview=Question anchor: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, canal route map.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.893986 chunk_id=24307 preview=Question anchor: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
  2. score=0.892836 chunk_id=24019 preview=document distractor-willow-courtyard-well-089::distractor-089: In document distractor-willow-courtyard-well-089, the verified archive note records Signal Lan...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, canal route map.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 90 - distractor-090
Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir?

Expected evidence:
- Selma of Bell Bridge square
- cedar shovel

Expected distractors:
- Damir of Bell Bridge square

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.910093 chunk_id=23509 preview=Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? document distractor-bell-bridge-square-090:...
  2. score=0.907490 chunk_id=23508 preview=Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Case scope id: distractor-090. Scoped answe...
  3. score=0.905072 chunk_id=23136 preview=document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Br...
  4. score=0.882337 chunk_id=23236 preview=document distractor-bell-bridge-square-090::distractor-090::distractor: A conflicting note in document distractor-bell-bridge-square-090 mentions Damir of Be...
  5. score=0.859857 chunk_id=23419 preview=Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? document distractor-bell-bridge-square-045:...
- Matched markers: Selma of Bell Bridge square, cedar shovel
- Missing markers: none
- Distractors: Damir of Bell Bridge square
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Selma of Bell Bridge square, cedar shovel. Distractors present: Damir of Bell Bridge square.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.745183 chunk_id=23508 preview=Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Case scope id: distractor-090. Scoped answe...
  2. score=0.730081 chunk_id=23509 preview=Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? document distractor-bell-bridge-square-090:...
  3. score=0.716692 chunk_id=23136 preview=document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Br...
  4. score=0.637513 chunk_id=23349 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? document distractor-birch-ferry-shed-010::dis...
  5. score=0.633176 chunk_id=23348 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Case scope id: distractor-010. Scoped answer...
- Matched markers: Selma of Bell Bridge square, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Bell Bridge square, cedar shovel.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.845436 chunk_id=24308 preview=Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Case scope id: distractor-090. Scoped answe...
  2. score=0.826213 chunk_id=24309 preview=Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? document distractor-bell-bridge-square-090:...
- Matched markers: Selma of Bell Bridge square, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Bell Bridge square, cedar shovel.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.888295 chunk_id=24309 preview=Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? document distractor-bell-bridge-square-090:...
  2. score=0.876873 chunk_id=23936 preview=document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Br...
- Matched markers: Selma of Bell Bridge square, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Bell Bridge square, cedar shovel.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 91 - distractor-091
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?

Expected evidence:
- March 11 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 12 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919438 chunk_id=23153 preview=document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwat...
  2. score=0.918574 chunk_id=23151 preview=document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwat...
  3. score=0.917531 chunk_id=23155 preview=document distractor-cedar-hill-station-076::distractor-076: In document distractor-cedar-hill-station-076, the verified archive note records March 14 Bellwat...
  4. score=0.917407 chunk_id=23156 preview=document distractor-cedar-hill-station-091::distractor-091: In document distractor-cedar-hill-station-091, the verified archive note records March 11 Bellwat...
  5. score=0.917248 chunk_id=23154 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
- Matched markers: Cedar Hill station, March 11 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 11 Bellwater Fair.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.794214 chunk_id=23153 preview=document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwat...
  2. score=0.793285 chunk_id=23151 preview=document distractor-cedar-hill-station-016::distractor-016: In document distractor-cedar-hill-station-016, the verified archive note records March 26 Bellwat...
  3. score=0.790958 chunk_id=23154 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
  4. score=0.790795 chunk_id=23152 preview=document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwat...
  5. score=0.789939 chunk_id=23390 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-031. Sc...
- Matched markers: Cedar Hill station
- Missing markers: March 11 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 11 Bellwater Fair.
- Verdict: partial

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.827919 chunk_id=24280 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-076. Sc...
  2. score=0.827262 chunk_id=24160 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-016. Sc...
- Matched markers: Cedar Hill station
- Missing markers: March 11 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 11 Bellwater Fair.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.905928 chunk_id=24161 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  2. score=0.905119 chunk_id=24251 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
- Matched markers: Cedar Hill station
- Missing markers: March 11 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 11 Bellwater Fair.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 92 - distractor-092
Question: Which place held the true profile detail for Zora, not the nearly identical place name?

Expected evidence:
- Moon Mill yard
- moonflower cutting

Expected distractors:
- Hollow Market arcade

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.867964 chunk_id=23513 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-0...
  2. score=0.861733 chunk_id=23353 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-cloud-wharf-office-012::distract...
  3. score=0.861349 chunk_id=23433 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor...
  4. score=0.856499 chunk_id=23512 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-092. Scoped answer summary...
  5. score=0.853114 chunk_id=23432 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary...
- Matched markers: Moon Mill yard, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, moonflower cutting.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.697451 chunk_id=23432 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary...
  2. score=0.693872 chunk_id=23433 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor...
  3. score=0.689089 chunk_id=23512 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-092. Scoped answer summary...
  4. score=0.683521 chunk_id=23513 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-0...
  5. score=0.682850 chunk_id=23352 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-012. Scoped answer summary...
- Matched markers: Moon Mill yard, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Grounded by retrieved evidence for: Moon Mill yard, moonflower cutting.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.748696 chunk_id=24232 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary...
  2. score=0.730016 chunk_id=24233 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor...
  3. score=0.710905 chunk_id=24313 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-0...
- Matched markers: Moon Mill yard, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 3
- Answer summary: Partially grounded by: Moon Mill yard, moonflower cutting.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.856604 chunk_id=24313 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-moon-mill-yard-092::distractor-0...
  2. score=0.855858 chunk_id=24153 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-cloud-wharf-office-012::distract...
- Matched markers: Moon Mill yard, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Moon Mill yard, moonflower cutting.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Earlier first relevant chunk (1 vs 3).

### Question 93 - distractor-093
Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?

Expected evidence:
- birch tea flask
- Vesna of Winter Chapel porch

Expected distractors:
- lantern hook

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919131 chunk_id=23225 preview=document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flas...
  2. score=0.917168 chunk_id=23514 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  3. score=0.904184 chunk_id=23515 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  4. score=0.898263 chunk_id=23224 preview=document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Ness...
  5. score=0.895502 chunk_id=23484 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
- Matched markers: Vesna of Winter Chapel porch, birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of Winter Chapel porch, birch tea flask.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.753495 chunk_id=23515 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  2. score=0.750021 chunk_id=23514 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  3. score=0.738546 chunk_id=23225 preview=document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flas...
  4. score=0.680085 chunk_id=23485 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  5. score=0.679343 chunk_id=23221 preview=document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch,...
- Matched markers: Vesna of Winter Chapel porch, birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of Winter Chapel porch, birch tea flask.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.808663 chunk_id=24314 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=0.798033 chunk_id=24315 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  3. score=0.764843 chunk_id=24154 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-01...
- Matched markers: Vesna of Winter Chapel porch, birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of Winter Chapel porch, birch tea flask.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.880724 chunk_id=24025 preview=document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flas...
  2. score=0.877031 chunk_id=24315 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
- Matched markers: Vesna of Winter Chapel porch, birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of Winter Chapel porch, birch tea flask.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 94 - distractor-094
Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at Marble stair hall
- saffron scarf

Expected distractors:
- Bridgefire Supper at Marble stair hall

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.911011 chunk_id=23174 preview=document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Mor...
  2. score=0.905114 chunk_id=23516 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  3. score=0.899727 chunk_id=23517 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  4. score=0.889958 chunk_id=23173 preview=document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Mor...
  5. score=0.886980 chunk_id=23170 preview=document distractor-marble-stair-hall-034::distractor-034: In document distractor-marble-stair-hall-034, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at Marble stair hall, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, saffron scarf.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.771234 chunk_id=23516 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  2. score=0.768639 chunk_id=23517 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  3. score=0.724170 chunk_id=23174 preview=document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Mor...
  4. score=0.699225 chunk_id=23427 preview=Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? document distractor-marbl...
  5. score=0.695932 chunk_id=23457 preview=Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
- Matched markers: Signal Lantern Morning at Marble stair hall, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, saffron scarf.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.776820 chunk_id=24316 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  2. score=0.744303 chunk_id=24317 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  3. score=0.722424 chunk_id=24286 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
- Matched markers: Signal Lantern Morning at Marble stair hall, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, saffron scarf.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.898303 chunk_id=24317 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  2. score=0.896571 chunk_id=23974 preview=document distractor-marble-stair-hall-094::distractor-094: In document distractor-marble-stair-hall-094, the verified archive note records Signal Lantern Mor...
  3. score=0.890385 chunk_id=24227 preview=Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? document distractor-marbl...
- Matched markers: Signal Lantern Morning at Marble stair hall, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, saffron scarf.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 95 - distractor-095
Question: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira?

Expected evidence:
- Ilya of Star Basin gallery
- carved shell comb

Expected distractors:
- Kira of Star Basin gallery

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.908417 chunk_id=23213 preview=document distractor-star-basin-gallery-095::distractor-095: In document distractor-star-basin-gallery-095, the verified archive note records Ilya of Star Bas...
  2. score=0.907827 chunk_id=23518 preview=Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Case scope id: distractor-095. Scoped answer...
  3. score=0.907330 chunk_id=23519 preview=Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? document distractor-star-basin-gallery-095::d...
  4. score=0.865312 chunk_id=23313 preview=document distractor-star-basin-gallery-095::distractor-095::distractor: A conflicting note in document distractor-star-basin-gallery-095 mentions Kira of Sta...
  5. score=0.860031 chunk_id=23359 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::d...
- Matched markers: Ilya of Star Basin gallery, carved shell comb
- Missing markers: none
- Distractors: Kira of Star Basin gallery
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Ilya of Star Basin gallery, carved shell comb. Distractors present: Kira of Star Basin gallery.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.761807 chunk_id=23518 preview=Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Case scope id: distractor-095. Scoped answer...
  2. score=0.758535 chunk_id=23519 preview=Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? document distractor-star-basin-gallery-095::d...
  3. score=0.742051 chunk_id=23213 preview=document distractor-star-basin-gallery-095::distractor-095: In document distractor-star-basin-gallery-095, the verified archive note records Ilya of Star Bas...
  4. score=0.635582 chunk_id=23438 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Case scope id: distractor-055. Scoped answer su...
  5. score=0.631462 chunk_id=23439 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? document distractor-birch-ferry-shed-055::distr...
- Matched markers: Ilya of Star Basin gallery, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Star Basin gallery, carved shell comb.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.852507 chunk_id=24318 preview=Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Case scope id: distractor-095. Scoped answer...
  2. score=0.826309 chunk_id=24319 preview=Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? document distractor-star-basin-gallery-095::d...
- Matched markers: Ilya of Star Basin gallery, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Star Basin gallery, carved shell comb.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.881193 chunk_id=24319 preview=Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? document distractor-star-basin-gallery-095::d...
  2. score=0.872008 chunk_id=24013 preview=document distractor-star-basin-gallery-095::distractor-095: In document distractor-star-basin-gallery-095, the verified archive note records Ilya of Star Bas...
  3. score=0.871419 chunk_id=24318 preview=Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Case scope id: distractor-095. Scoped answer...
- Matched markers: Ilya of Star Basin gallery, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Star Basin gallery, carved shell comb.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 96 - distractor-096
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?

Expected evidence:
- March 16 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 17 Bellwater Fair

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.919557 chunk_id=23181 preview=document distractor-north-bell-workshop-006::distractor-006: In document distractor-north-bell-workshop-006, the verified archive note records March 16 Bellw...
  2. score=0.919384 chunk_id=23187 preview=document distractor-north-bell-workshop-096::distractor-096: In document distractor-north-bell-workshop-096, the verified archive note records March 16 Bellw...
  3. score=0.918695 chunk_id=23185 preview=document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellw...
  4. score=0.918667 chunk_id=23183 preview=document distractor-north-bell-workshop-036::distractor-036: In document distractor-north-bell-workshop-036, the verified archive note records March 10 Bellw...
  5. score=0.917342 chunk_id=23186 preview=document distractor-north-bell-workshop-081::distractor-081: In document distractor-north-bell-workshop-081, the verified archive note records March 19 Bellw...
- Matched markers: March 16 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 16 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.778081 chunk_id=23184 preview=document distractor-north-bell-workshop-051::distractor-051: In document distractor-north-bell-workshop-051, the verified archive note records March 25 Bellw...
  2. score=0.775997 chunk_id=23430 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-051. S...
  3. score=0.773384 chunk_id=23340 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-006. S...
  4. score=0.773188 chunk_id=23182 preview=document distractor-north-bell-workshop-021::distractor-021: In document distractor-north-bell-workshop-021, the verified archive note records March 13 Bellw...
  5. score=0.773136 chunk_id=23370 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-021. S...
- Matched markers: March 16 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 16 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.833872 chunk_id=24290 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-081. S...
  2. score=0.833841 chunk_id=24230 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-051. S...
  3. score=0.832436 chunk_id=24260 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. S...
- Matched markers: North Bell workshop
- Missing markers: March 16 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 16 Bellwater Fair.
- Verdict: partial

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.898039 chunk_id=24291 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=0.896125 chunk_id=24171 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=0.894784 chunk_id=24231 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
- Matched markers: North Bell workshop
- Missing markers: March 16 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 16 Bellwater Fair.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 97 - distractor-097
Question: Which place held the true profile detail for Boris, not the nearly identical place name?

Expected evidence:
- Blue Trunk cabin
- basalt sketch

Expected distractors:
- East Signal room

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.863999 chunk_id=23523 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distracto...
  2. score=0.859011 chunk_id=23443 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distrac...
  3. score=0.858929 chunk_id=23363 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-moon-mill-yard-017::distractor-...
  4. score=0.854487 chunk_id=23522 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summar...
  5. score=0.851230 chunk_id=23442 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-057. Scoped answer summar...
- Matched markers: Blue Trunk cabin, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, basalt sketch.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.729616 chunk_id=23523 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distracto...
  2. score=0.708255 chunk_id=23522 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summar...
  3. score=0.693435 chunk_id=23443 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distrac...
  4. score=0.690946 chunk_id=23150 preview=document distractor-blue-trunk-cabin-097::distractor-097: In document distractor-blue-trunk-cabin-097, the verified archive note records Blue Trunk cabin, ba...
  5. score=0.687760 chunk_id=23442 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-057. Scoped answer summar...
- Matched markers: Blue Trunk cabin, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, basalt sketch.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.694095 chunk_id=24323 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distracto...
  2. score=0.690519 chunk_id=24322 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summar...
- Matched markers: Blue Trunk cabin, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, basalt sketch.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.862998 chunk_id=24243 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-cloud-wharf-office-057::distrac...
  2. score=0.862422 chunk_id=24323 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distracto...
- Matched markers: Blue Trunk cabin, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 2
- Answer summary: Partially grounded by: Blue Trunk cabin, basalt sketch.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 98 - distractor-098
Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?

Expected evidence:
- green apron
- Daria of North Orchard lane

Expected distractors:
- willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.912355 chunk_id=23524 preview=Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=0.911120 chunk_id=23194 preview=document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Dar...
  3. score=0.900992 chunk_id=23525 preview=Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  4. score=0.887447 chunk_id=23364 preview=Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  5. score=0.886194 chunk_id=23220 preview=document distractor-winter-chapel-porch-018::distractor-018: In document distractor-winter-chapel-porch-018, the verified archive note records copper wind va...
- Matched markers: Daria of North Orchard lane, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of North Orchard lane, green apron.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.782147 chunk_id=23524 preview=Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=0.778786 chunk_id=23525 preview=Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=0.765464 chunk_id=23194 preview=document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Dar...
  4. score=0.707800 chunk_id=23345 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  5. score=0.705404 chunk_id=23344 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
- Matched markers: Daria of North Orchard lane, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of North Orchard lane, green apron.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.800290 chunk_id=24324 preview=Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=0.778637 chunk_id=24325 preview=Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
- Matched markers: Daria of North Orchard lane, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of North Orchard lane, green apron.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.876832 chunk_id=24325 preview=Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  2. score=0.872116 chunk_id=23994 preview=document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Dar...
- Matched markers: Daria of North Orchard lane, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of North Orchard lane, green apron.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 99 - distractor-099
Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor?

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- silver booth token

Expected distractors:
- Bridgefire Supper at South Meadow arch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.910813 chunk_id=23207 preview=document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Mor...
  2. score=0.908206 chunk_id=23527 preview=Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? document distractor-south...
  3. score=0.899262 chunk_id=23526 preview=Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  4. score=0.897174 chunk_id=23205 preview=document distractor-south-meadow-arch-069::distractor-069: In document distractor-south-meadow-arch-069, the verified archive note records Signal Lantern Mor...
  5. score=0.897123 chunk_id=23201 preview=document distractor-south-meadow-arch-009::distractor-009: In document distractor-south-meadow-arch-009, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at South Meadow arch, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, silver booth token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.762637 chunk_id=23526 preview=Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  2. score=0.758190 chunk_id=23527 preview=Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? document distractor-south...
  3. score=0.709918 chunk_id=23207 preview=document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Mor...
  4. score=0.700438 chunk_id=23467 preview=Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  5. score=0.694143 chunk_id=23466 preview=Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
- Matched markers: Signal Lantern Morning at South Meadow arch, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, silver booth token.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.775701 chunk_id=24326 preview=Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  2. score=0.775030 chunk_id=24327 preview=Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? document distractor-south...
- Matched markers: Signal Lantern Morning at South Meadow arch, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, silver booth token.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.899099 chunk_id=24007 preview=document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Mor...
  2. score=0.889021 chunk_id=24327 preview=Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? document distractor-south...
- Matched markers: Signal Lantern Morning at South Meadow arch, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, silver booth token.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 100 - distractor-100
Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola?

Expected evidence:
- Ada of Birch Ferry shed
- clay watering cup

Expected distractors:
- Nikola of Birch Ferry shed

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.907459 chunk_id=23529 preview=Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? document distractor-birch-ferry-shed-100::dist...
  2. score=0.903072 chunk_id=23528 preview=Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Case scope id: distractor-100. Scoped answer s...
  3. score=0.901121 chunk_id=23143 preview=document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry s...
  4. score=0.880892 chunk_id=23243 preview=document distractor-birch-ferry-shed-100::distractor-100::distractor: A conflicting note in document distractor-birch-ferry-shed-100 mentions Nikola of Birch...
  5. score=0.872999 chunk_id=23139 preview=document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry...
- Matched markers: Ada of Birch Ferry shed, clay watering cup
- Missing markers: none
- Distractors: Nikola of Birch Ferry shed
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Ada of Birch Ferry shed, clay watering cup. Distractors present: Nikola of Birch Ferry shed.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.742902 chunk_id=23528 preview=Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Case scope id: distractor-100. Scoped answer s...
  2. score=0.741076 chunk_id=23529 preview=Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? document distractor-birch-ferry-shed-100::dist...
  3. score=0.717313 chunk_id=23143 preview=document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry s...
  4. score=0.648478 chunk_id=23469 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::dist...
  5. score=0.647556 chunk_id=23468 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Case scope id: distractor-070. Scoped answer s...
- Matched markers: Ada of Birch Ferry shed, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Birch Ferry shed, clay watering cup.
- Verdict: grounded

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.812285 chunk_id=24328 preview=Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Case scope id: distractor-100. Scoped answer s...
  2. score=0.782486 chunk_id=24329 preview=Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? document distractor-birch-ferry-shed-100::dist...
- Matched markers: Ada of Birch Ferry shed, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Birch Ferry shed, clay watering cup.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=0.900100 chunk_id=24329 preview=Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? document distractor-birch-ferry-shed-100::dist...
  2. score=0.881527 chunk_id=24328 preview=Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Case scope id: distractor-100. Scoped answer s...
  3. score=0.880967 chunk_id=23943 preview=document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry s...
- Matched markers: Ada of Birch Ferry shed, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Birch Ferry shed, clay watering cup.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Aggregate Results

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Question wins: 67
- Passed questions: 69
- Average evidence coverage: 0.98
- Average first relevant rank: 1.16
- Total matched markers: 196
- Total missing markers: 4
- Total false-positive markers: 23
- Official metrics: {'hit_rate': 0.96, 'recall_at_k': 0.98, 'mrr': 0.9366666666666668, 'forbidden_marker_rate': 0.04800000000000001, 'average_latency_ms': 1519.5619399999998, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.98, 'missing_expected_marker_count': 4, 'false_positive_count': 143}

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Question wins: 30
- Passed questions: 85
- Average evidence coverage: 0.955
- Average first relevant rank: 1.202
- Total matched markers: 191
- Total missing markers: 9
- Total false-positive markers: 5
- Official metrics: {'hit_rate': 0.97, 'recall_at_k': 0.955, 'mrr': 0.9261666666666666, 'forbidden_marker_rate': 0.01, 'average_latency_ms': 419.74913999999995, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.955, 'missing_expected_marker_count': 9, 'false_positive_count': 139}

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Question wins: 2
- Passed questions: 76
- Average evidence coverage: 0.88
- Average first relevant rank: 1.0851
- Total matched markers: 176
- Total missing markers: 24
- Total false-positive markers: 0
- Official metrics: {'hit_rate': 0.88, 'recall_at_k': 0.88, 'mrr': 0.91, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 222.71005000000002, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.88, 'missing_expected_marker_count': 24, 'false_positive_count': 44}

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Question wins: 1
- Passed questions: 72
- Average evidence coverage: 0.92
- Average first relevant rank: 1.102
- Total matched markers: 184
- Total missing markers: 16
- Total false-positive markers: 0
- Official metrics: {'hit_rate': 0.84, 'recall_at_k': 0.92, 'mrr': 0.9333333333333332, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 212.31009999999998, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.92, 'missing_expected_marker_count': 16, 'false_positive_count': 27}

### Runtime Activation
- Selected config: {'best_config_id': 'bge_m3', 'best_model_code': 'bge_m3', 'best_collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4', 'selected_metrics': {'hit_rate': 0.97, 'recall_at_k': 0.955, 'mrr': 0.9261666666666666, 'forbidden_marker_rate': 0.01, 'average_latency_ms': 419.74913999999995, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.955, 'missing_expected_marker_count': 9, 'false_positive_count': 139}, 'all_config_scores': [{'config_id': 'bge_m3', 'model_code': 'bge_m3', 'collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4', 'metrics': {'hit_rate': 0.97, 'recall_at_k': 0.955, 'mrr': 0.9261666666666666, 'forbidden_marker_rate': 0.01, 'average_latency_ms': 419.74913999999995, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.955, 'missing_expected_marker_count': 9, 'false_positive_count': 139}, 'acceptable_latency': True, 'acceptable_cost': True, 'ranking_factors': {'hit_rate': 0.97, 'evidence_marker_coverage': 0.955, 'recall_at_k': 0.955, 'mrr': 0.9261666666666666, 'forbidden_marker_rate': 0.01, 'acceptable_latency': True, 'acceptable_cost': True, 'average_latency_ms': 419.74913999999995, 'cost_estimate_total': None}, 'reasons': ['hit_rate=0.970', 'evidence_marker_coverage=0.955', 'recall_at_k=0.955', 'mrr=0.926', 'forbidden_marker_rate=0.010'], 'warnings': []}, {'config_id': 'multilingual_e5_small', 'model_code': 'multilingual_e5_small', 'collection_name': 'eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4', 'metrics': {'hit_rate': 0.96, 'recall_at_k': 0.98, 'mrr': 0.9366666666666668, 'forbidden_marker_rate': 0.04800000000000001, 'average_latency_ms': 1519.5619399999998, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.98, 'missing_expected_marker_count': 4, 'false_positive_count': 143}, 'acceptable_latency': True, 'acceptable_cost': True, 'ranking_factors': {'hit_rate': 0.96, 'evidence_marker_coverage': 0.98, 'recall_at_k': 0.98, 'mrr': 0.9366666666666668, 'forbidden_marker_rate': 0.04800000000000001, 'acceptable_latency': True, 'acceptable_cost': True, 'average_latency_ms': 1519.5619399999998, 'cost_estimate_total': None}, 'reasons': ['hit_rate=0.960', 'evidence_marker_coverage=0.980', 'recall_at_k=0.980', 'mrr=0.937', 'forbidden_marker_rate=0.048'], 'warnings': []}, {'config_id': 'paraphrase_multilingual_mpnet_base_v2', 'model_code': 'paraphrase_multilingual_mpnet_base_v2', 'collection_name': 'eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4', 'metrics': {'hit_rate': 0.88, 'recall_at_k': 0.88, 'mrr': 0.91, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 222.71005000000002, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.88, 'missing_expected_marker_count': 24, 'false_positive_count': 44}, 'acceptable_latency': True, 'acceptable_cost': True, 'ranking_factors': {'hit_rate': 0.88, 'evidence_marker_coverage': 0.88, 'recall_at_k': 0.88, 'mrr': 0.91, 'forbidden_marker_rate': 0.0, 'acceptable_latency': True, 'acceptable_cost': True, 'average_latency_ms': 222.71005000000002, 'cost_estimate_total': None}, 'reasons': ['hit_rate=0.880', 'evidence_marker_coverage=0.880', 'recall_at_k=0.880', 'mrr=0.910', 'forbidden_marker_rate=0.000'], 'warnings': []}, {'config_id': 'multilingual_e5_base', 'model_code': 'multilingual_e5_base', 'collection_name': 'eternal_world_rag_chunks__multilingual_e5_base__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4', 'metrics': {'hit_rate': 0.84, 'recall_at_k': 0.92, 'mrr': 0.9333333333333332, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 212.31009999999998, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.92, 'missing_expected_marker_count': 16, 'false_positive_count': 27}, 'acceptable_latency': True, 'acceptable_cost': True, 'ranking_factors': {'hit_rate': 0.84, 'evidence_marker_coverage': 0.92, 'recall_at_k': 0.92, 'mrr': 0.9333333333333332, 'forbidden_marker_rate': 0.0, 'acceptable_latency': True, 'acceptable_cost': True, 'average_latency_ms': 212.31009999999998, 'cost_estimate_total': None}, 'reasons': ['hit_rate=0.840', 'evidence_marker_coverage=0.920', 'recall_at_k=0.920', 'mrr=0.933', 'forbidden_marker_rate=0.000'], 'warnings': []}], 'reasons': ['Selection order: hit_rate/evidence marker coverage, recall_at_k, MRR, safety, latency, cost.'], 'warnings': ['Selected config still has a non-zero forbidden marker rate.']}
- Activated config: {}
- Runtime retrieval verification: {}
