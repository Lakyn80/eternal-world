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
- Timestamp: 2026-07-03T14:04:27.955121+00:00
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
- Archived Markdown: `/app/artifacts/real_question_eval/runs/20260703_140427Z_fake/real_question_eval_report.md`
- Archived JSON: `/app/artifacts/real_question_eval/runs/20260703_140427Z_fake/real_question_eval_result.json`
- Archived Summary Markdown: `/app/artifacts/real_question_eval/runs/20260703_140427Z_fake/real_question_eval_summary.md`
- Archived Summary JSON: `/app/artifacts/real_question_eval/runs/20260703_140427Z_fake/real_question_eval_summary.json`

## Client Question Breakdown
### Question 1 - distractor-twin-innkeepers
Question: Which Marta kept the North Inn ledger, and what detail identified her apron?
- Final evaluated answer: Grounded by retrieved evidence for: Marta of North Inn, green apron.
- Correctness verdict: grounded
- Evidence used: Marta of North Inn, green apron
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Marta of North Inn
- green apron

Expected distractors:
- Marta of River Inn

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Marta of North Inn, green apron missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Marta of North Inn, green apron missing=none distractors=none

### Question 2 - distractor-june-market-date
Question: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice?
- Final evaluated answer: Grounded by retrieved evidence for: Bell Bridge square, June 14 night market.
- Correctness verdict: grounded
- Evidence used: Bell Bridge square, June 14 night market
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- June 14 night market
- Bell Bridge square

Expected distractors:
- June 4 noon market

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Bell Bridge square, June 14 night market missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Bell Bridge square, June 14 night market missing=none distractors=none

### Question 3 - distractor-two-levs
Question: Which Lev repaired the oak barrels, not the one who worked by the ferry?
- Final evaluated answer: Grounded by retrieved evidence for: Lev the cooper, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Lev the cooper, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Lev the cooper
- oak barrel hoops

Expected distractors:
- Lev the ferryman

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lev the cooper, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lev the cooper, oak barrel hoops missing=none distractors=none

### Question 4 - distractor-similar-islands
Question: Which island shed kept the painted blue oar, and which similar island name is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Fog Island ferry shed, painted blue oar.
- Correctness verdict: grounded
- Evidence used: Fog Island ferry shed, painted blue oar
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Fog Island ferry shed
- painted blue oar

Expected distractors:
- Fox Island ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Fog Island ferry shed, painted blue oar missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Fog Island ferry shed, painted blue oar missing=none distractors=none

### Question 5 - distractor-letter-mixup
Question: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season?
- Final evaluated answer: Grounded by retrieved evidence for: Ada's winter letter, violet wax thread.
- Correctness verdict: grounded
- Evidence used: Ada's winter letter, violet wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 6 - distractor-006
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 16 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 16 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- March 16 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 17 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=March 16 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=March 16 Bellwater Fair, North Bell workshop missing=none distractors=none

### Question 7 - distractor-007
Question: Which place held the true profile detail for Nikola, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, brass compass.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, brass compass
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Blue Trunk cabin
- brass compass

Expected distractors:
- East Signal room

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Blue Trunk cabin, brass compass missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, brass compass missing=none distractors=none

### Question 8 - distractor-008
Question: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Sonya of North Orchard lane, linen wick.
- Correctness verdict: grounded
- Evidence used: Sonya of North Orchard lane, linen wick
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
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

### Question 9 - distractor-009
Question: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Partially grounded by: Signal Lantern Morning at South Meadow arch, star ledger page.
- Correctness verdict: partial
- Evidence used: Signal Lantern Morning at South Meadow arch, star ledger page
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=partial coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing Signal Lantern Morning at South Meadow arch, star ledger page
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- star ledger page

Expected distractors:
- Bridgefire Supper at South Meadow arch

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Signal Lantern Morning at South Meadow arch, star ledger page distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, star ledger page missing=none distractors=none

### Question 10 - distractor-010
Question: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir?
- Final evaluated answer: Grounded by retrieved evidence for: Selma of Birch Ferry shed, lantern hook.
- Correctness verdict: grounded
- Evidence used: Selma of Birch Ferry shed, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Selma of Birch Ferry shed
- lantern hook

Expected distractors:
- Damir of Birch Ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Selma of Birch Ferry shed, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Selma of Birch Ferry shed, lantern hook missing=none distractors=none

### Question 11 - distractor-011
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 21 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 21 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- March 21 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 22 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 21 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 21 Bellwater Fair missing=none distractors=none

### Question 12 - distractor-012
Question: Which place held the true profile detail for Zora, not the nearly identical place name?
- Final evaluated answer: Partially grounded by: Cloud Wharf office, wax thread.
- Correctness verdict: partial
- Evidence used: Cloud Wharf office, wax thread
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=partial coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing Cloud Wharf office, wax thread
- Distractors / false positives: none

Expected evidence:
- Cloud Wharf office
- wax thread

Expected distractors:
- Fox Hollow bridge

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Cloud Wharf office, wax thread distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=Cloud Wharf office, wax thread missing=none distractors=none

### Question 13 - distractor-013
Question: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vesna of Ridge Post loft, tin key.
- Correctness verdict: grounded
- Evidence used: Vesna of Ridge Post loft, tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 14 - distractor-014
Question: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, blue oar.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, blue oar
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 15 - distractor-015
Question: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira?
- Final evaluated answer: Grounded by retrieved evidence for: Ilya of Bell Bridge square, willow basket.
- Correctness verdict: grounded
- Evidence used: Ilya of Bell Bridge square, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Ilya of Bell Bridge square
- willow basket

Expected distractors:
- Kira of Bell Bridge square

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Ilya of Bell Bridge square, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Ilya of Bell Bridge square, willow basket missing=none distractors=none

### Question 16 - distractor-016
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 26 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 26 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing March 26 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 26 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 27 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=Cedar Hill station missing=March 26 Bellwater Fair distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 26 Bellwater Fair missing=none distractors=none

### Question 17 - distractor-017
Question: Which place held the true profile detail for Boris, not the nearly identical place name?
- Final evaluated answer: No winning answer summary available.
- Correctness verdict: unknown
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `none`
- Why it won: NO_MODEL_PASSED_QUESTION_QUALITY_GATE
- What the losing model missed or got wrong: multilingual_e5_small missing Moon Mill yard, glass ink bottle; bge_m3 missing Moon Mill yard, glass ink bottle
- Distractors / false positives: none

Expected evidence:
- Moon Mill yard
- glass ink bottle

Expected distractors:
- Hollow Market arcade

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, glass ink bottle distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, glass ink bottle distractors=none

### Question 18 - distractor-018
Question: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Daria of Winter Chapel porch, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Daria of Winter Chapel porch, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing copper wind vane pin, Daria of Winter Chapel porch
- Distractors / false positives: none

Expected evidence:
- copper wind vane pin
- Daria of Winter Chapel porch

Expected distractors:
- carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=copper wind vane pin, Daria of Winter Chapel porch distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Daria of Winter Chapel porch, copper wind vane pin missing=none distractors=none

### Question 19 - distractor-019
Question: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, coal stove hiss.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, coal stove hiss
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at Marble stair hall
- coal stove hiss

Expected distractors:
- Bridgefire Supper at Marble stair hall

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, coal stove hiss missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, coal stove hiss missing=none distractors=none

### Question 20 - distractor-020
Question: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola?
- Final evaluated answer: Grounded by retrieved evidence for: Ada of Star Basin gallery, violet ribbon.
- Correctness verdict: grounded
- Evidence used: Ada of Star Basin gallery, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Ada of Star Basin gallery
- violet ribbon

Expected distractors:
- Nikola of Star Basin gallery

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Ada of Star Basin gallery, violet ribbon missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Ada of Star Basin gallery, violet ribbon missing=none distractors=none

### Question 21 - distractor-021
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 13 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 13 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- March 13 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 14 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=March 13 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=March 13 Bellwater Fair, North Bell workshop missing=none distractors=none

### Question 22 - distractor-022
Question: Which place held the true profile detail for Talia, not the nearly identical place name?
- Final evaluated answer: Partially grounded by: Blue Trunk cabin, rope bridge permit.
- Correctness verdict: partial
- Evidence used: Blue Trunk cabin, rope bridge permit
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Blue Trunk cabin
- rope bridge permit

Expected distractors:
- East Signal room

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Blue Trunk cabin, rope bridge permit missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=Blue Trunk cabin, rope bridge permit missing=none distractors=none

### Question 23 - distractor-023
Question: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Viktor of North Orchard lane, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Viktor of North Orchard lane, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- oak barrel hoops
- Viktor of North Orchard lane

Expected distractors:
- clay watering cup

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Viktor of North Orchard lane, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Viktor of North Orchard lane, oak barrel hoops missing=none distractors=none

### Question 24 - distractor-024
Question: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, blue glass jar.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, blue glass jar
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 25 - distractor-025
Question: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora?
- Final evaluated answer: Grounded by retrieved evidence for: Anton of Birch Ferry shed, canal route map.
- Correctness verdict: grounded
- Evidence used: Anton of Birch Ferry shed, canal route map
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Anton of Birch Ferry shed
- canal route map

Expected distractors:
- Zora of Birch Ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Anton of Birch Ferry shed, canal route map missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Anton of Birch Ferry shed, canal route map missing=none distractors=none

### Question 26 - distractor-026
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 18 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 18 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- March 18 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 19 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 18 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 18 Bellwater Fair missing=none distractors=none

### Question 27 - distractor-027
Question: Which place held the true profile detail for Tomas, not the nearly identical place name?
- Final evaluated answer: Partially grounded by: Cloud Wharf office, copper token.
- Correctness verdict: partial
- Evidence used: Cloud Wharf office, copper token
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=partial coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing Cloud Wharf office, copper token
- Distractors / false positives: none

Expected evidence:
- Cloud Wharf office
- copper token

Expected distractors:
- Fox Hollow bridge

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Cloud Wharf office, copper token distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=Cloud Wharf office, copper token missing=none distractors=none

### Question 28 - distractor-028
Question: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vera of Ridge Post loft, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: Vera of Ridge Post loft, moonflower cutting
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 29 - distractor-029
Question: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, birch tea flask.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, birch tea flask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=1.0
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
  - `bge_m3`: verdict=partial coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, birch tea flask missing=none distractors=none

### Question 30 - distractor-030
Question: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris?
- Final evaluated answer: Grounded by retrieved evidence for: Lina of Bell Bridge square, saffron scarf.
- Correctness verdict: grounded
- Evidence used: Lina of Bell Bridge square, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Lina of Bell Bridge square
- saffron scarf

Expected distractors:
- Boris of Bell Bridge square

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lina of Bell Bridge square, saffron scarf missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lina of Bell Bridge square, saffron scarf missing=none distractors=none

### Question 31 - distractor-031
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 23 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 23 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- March 23 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 24 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 23 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 23 Bellwater Fair missing=none distractors=none

### Question 32 - distractor-032
Question: Which place held the true profile detail for Yara, not the nearly identical place name?
- Final evaluated answer: No winning answer summary available.
- Correctness verdict: unknown
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `none`
- Why it won: NO_MODEL_PASSED_QUESTION_QUALITY_GATE
- What the losing model missed or got wrong: multilingual_e5_small missing Moon Mill yard, amber lantern; bge_m3 missing Moon Mill yard, amber lantern
- Distractors / false positives: none

Expected evidence:
- Moon Mill yard
- amber lantern

Expected distractors:
- Hollow Market arcade

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, amber lantern distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, amber lantern distractors=none

### Question 33 - distractor-033
Question: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Lev of Winter Chapel porch, basalt sketch.
- Correctness verdict: grounded
- Evidence used: Lev of Winter Chapel porch, basalt sketch
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 34 - distractor-034
Question: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, green apron.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, green apron
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 35 - distractor-035
Question: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia?
- Final evaluated answer: Grounded by retrieved evidence for: Pavel of Star Basin gallery, silver booth token.
- Correctness verdict: grounded
- Evidence used: Pavel of Star Basin gallery, silver booth token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Pavel of Star Basin gallery
- silver booth token

Expected distractors:
- Talia of Star Basin gallery

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Pavel of Star Basin gallery, silver booth token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Pavel of Star Basin gallery, silver booth token missing=none distractors=none

### Question 36 - distractor-036
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 10 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 10 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing March 10 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 10 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 11 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 10 Bellwater Fair distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=March 10 Bellwater Fair, North Bell workshop missing=none distractors=none

### Question 37 - distractor-037
Question: Which place held the true profile detail for Damir, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, juniper bundles.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, juniper bundles
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
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

### Question 38 - distractor-038
Question: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Nessa of North Orchard lane, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: Nessa of North Orchard lane, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
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

### Question 39 - distractor-039
Question: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, brass compass.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, brass compass
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing Signal Lantern Morning at South Meadow arch, brass compass
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- brass compass

Expected distractors:
- Bridgefire Supper at South Meadow arch

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Signal Lantern Morning at South Meadow arch, brass compass distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, brass compass missing=none distractors=none

### Question 40 - distractor-040
Question: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas?
- Final evaluated answer: Grounded by retrieved evidence for: Mira of Birch Ferry shed, linen wick.
- Correctness verdict: grounded
- Evidence used: Mira of Birch Ferry shed, linen wick
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Mira of Birch Ferry shed
- linen wick

Expected distractors:
- Tomas of Birch Ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Mira of Birch Ferry shed, linen wick missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Mira of Birch Ferry shed, linen wick missing=none distractors=none

### Question 41 - distractor-041
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 15 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 15 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- March 15 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 16 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 15 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 15 Bellwater Fair missing=none distractors=none

### Question 42 - distractor-042
Question: Which place held the true profile detail for Kira, not the nearly identical place name?
- Final evaluated answer: No winning answer summary available.
- Correctness verdict: unknown
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `none`
- Why it won: NO_MODEL_PASSED_QUESTION_QUALITY_GATE
- What the losing model missed or got wrong: multilingual_e5_small missing Cloud Wharf office, lantern hook; bge_m3 missing Cloud Wharf office, lantern hook
- Distractors / false positives: none

Expected evidence:
- Cloud Wharf office
- lantern hook

Expected distractors:
- Fox Hollow bridge

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Cloud Wharf office, lantern hook distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=Cloud Wharf office, lantern hook distractors=none

### Question 43 - distractor-043
Question: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Petar of Ridge Post loft, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: Petar of Ridge Post loft, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- weathered camera strap
- Petar of Ridge Post loft

Expected distractors:
- blue glass jar

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Petar of Ridge Post loft, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Petar of Ridge Post loft, weathered camera strap missing=none distractors=none

### Question 44 - distractor-044
Question: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, wax thread.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 45 - distractor-045
Question: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara?
- Final evaluated answer: Grounded by retrieved evidence for: Stefan of Bell Bridge square, tin key.
- Correctness verdict: grounded
- Evidence used: Stefan of Bell Bridge square, tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Stefan of Bell Bridge square
- tin key

Expected distractors:
- Yara of Bell Bridge square

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Stefan of Bell Bridge square, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Stefan of Bell Bridge square, tin key missing=none distractors=none

### Question 46 - distractor-046
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 20 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 20 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- March 20 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 21 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 20 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 20 Bellwater Fair missing=none distractors=none

### Question 47 - distractor-047
Question: Which place held the true profile detail for Nikola, not the nearly identical place name?
- Final evaluated answer: No winning answer summary available.
- Correctness verdict: unknown
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `none`
- Why it won: NO_MODEL_PASSED_QUESTION_QUALITY_GATE
- What the losing model missed or got wrong: multilingual_e5_small missing Moon Mill yard, willow basket; bge_m3 missing Moon Mill yard, willow basket
- Distractors / false positives: none

Expected evidence:
- Moon Mill yard
- willow basket

Expected distractors:
- Hollow Market arcade

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, willow basket distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, willow basket distractors=none

### Question 48 - distractor-048
Question: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Sonya of Winter Chapel porch, paper moon mask.
- Correctness verdict: grounded
- Evidence used: Sonya of Winter Chapel porch, paper moon mask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- Sonya of Winter Chapel porch

Expected distractors:
- birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Sonya of Winter Chapel porch, paper moon mask missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Sonya of Winter Chapel porch, paper moon mask missing=none distractors=none

### Question 49 - distractor-049
Question: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Partially grounded by: Signal Lantern Morning at Marble stair hall, glass ink bottle.
- Correctness verdict: partial
- Evidence used: Signal Lantern Morning at Marble stair hall, glass ink bottle
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=partial coverage=1.0
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
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, glass ink bottle missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=Signal Lantern Morning at Marble stair hall, glass ink bottle missing=none distractors=none

### Question 50 - distractor-050
Question: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir?
- Final evaluated answer: Grounded by retrieved evidence for: Selma of Star Basin gallery, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Selma of Star Basin gallery, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Selma of Star Basin gallery
- copper wind vane pin

Expected distractors:
- Damir of Star Basin gallery

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Selma of Star Basin gallery, copper wind vane pin missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Selma of Star Basin gallery, copper wind vane pin missing=none distractors=none

### Question 51 - distractor-051
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Partially grounded by: North Bell workshop. Missing: March 25 Bellwater Fair.
- Correctness verdict: partial
- Evidence used: North Bell workshop
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=partial coverage=0.5
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
  - `bge_m3`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 25 Bellwater Fair distractors=none

### Question 52 - distractor-052
Question: Which place held the true profile detail for Zora, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, violet ribbon.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Blue Trunk cabin
- violet ribbon

Expected distractors:
- East Signal room

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, violet ribbon missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, violet ribbon missing=none distractors=none

### Question 53 - distractor-053
Question: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vesna of North Orchard lane, tuning fork.
- Correctness verdict: grounded
- Evidence used: Vesna of North Orchard lane, tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
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

### Question 54 - distractor-054
Question: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, rope bridge permit
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at South Meadow arch
- rope bridge permit

Expected distractors:
- Bridgefire Supper at South Meadow arch

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, rope bridge permit missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning at South Meadow arch, rope bridge permit missing=none distractors=none

### Question 55 - distractor-055
Question: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira?
- Final evaluated answer: Grounded by retrieved evidence for: Ilya of Birch Ferry shed, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Ilya of Birch Ferry shed, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Ilya of Birch Ferry shed
- oak barrel hoops

Expected distractors:
- Kira of Birch Ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Ilya of Birch Ferry shed, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Ilya of Birch Ferry shed, oak barrel hoops missing=none distractors=none

### Question 56 - distractor-056
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 12 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 12 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing March 12 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 12 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 13 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=Lantern Row kiosk missing=March 12 Bellwater Fair distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 12 Bellwater Fair missing=none distractors=none

### Question 57 - distractor-057
Question: Which place held the true profile detail for Boris, not the nearly identical place name?
- Final evaluated answer: No winning answer summary available.
- Correctness verdict: unknown
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `none`
- Why it won: NO_MODEL_PASSED_QUESTION_QUALITY_GATE
- What the losing model missed or got wrong: multilingual_e5_small missing Cloud Wharf office, canal route map; bge_m3 missing Cloud Wharf office, canal route map
- Distractors / false positives: none

Expected evidence:
- Cloud Wharf office
- canal route map

Expected distractors:
- Fox Hollow bridge

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Cloud Wharf office, canal route map distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=Cloud Wharf office, canal route map distractors=none

### Question 58 - distractor-058
Question: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Daria of Ridge Post loft, cedar shovel.
- Correctness verdict: grounded
- Evidence used: Daria of Ridge Post loft, cedar shovel
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
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

### Question 59 - distractor-059
Question: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, copper token.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, copper token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 60 - distractor-060
Question: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola?
- Final evaluated answer: Grounded by retrieved evidence for: Ada of Bell Bridge square, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: Ada of Bell Bridge square, moonflower cutting
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Ada of Bell Bridge square
- moonflower cutting

Expected distractors:
- Nikola of Bell Bridge square

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Ada of Bell Bridge square, moonflower cutting missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Ada of Bell Bridge square, moonflower cutting missing=none distractors=none

### Question 61 - distractor-061
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 17 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 17 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- March 17 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 18 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 17 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 17 Bellwater Fair missing=none distractors=none

### Question 62 - distractor-062
Question: Which place held the true profile detail for Talia, not the nearly identical place name?
- Final evaluated answer: No winning answer summary available.
- Correctness verdict: unknown
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `none`
- Why it won: NO_MODEL_PASSED_QUESTION_QUALITY_GATE
- What the losing model missed or got wrong: multilingual_e5_small missing Moon Mill yard, saffron scarf; bge_m3 missing Moon Mill yard, saffron scarf
- Distractors / false positives: none

Expected evidence:
- Moon Mill yard
- saffron scarf

Expected distractors:
- Hollow Market arcade

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, saffron scarf distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, saffron scarf distractors=none

### Question 63 - distractor-063
Question: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Viktor of Winter Chapel porch, carved shell comb.
- Correctness verdict: grounded
- Evidence used: Viktor of Winter Chapel porch, carved shell comb
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
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

### Question 64 - distractor-064
Question: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, amber lantern.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, amber lantern
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 65 - distractor-065
Question: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora?
- Final evaluated answer: Grounded by retrieved evidence for: Anton of Star Basin gallery, basalt sketch.
- Correctness verdict: grounded
- Evidence used: Anton of Star Basin gallery, basalt sketch
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Anton of Star Basin gallery
- basalt sketch

Expected distractors:
- Zora of Star Basin gallery

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Anton of Star Basin gallery, basalt sketch missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Anton of Star Basin gallery, basalt sketch missing=none distractors=none

### Question 66 - distractor-066
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 22 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 22 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- March 22 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 23 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=March 22 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=March 22 Bellwater Fair, North Bell workshop missing=none distractors=none

### Question 67 - distractor-067
Question: Which place held the true profile detail for Tomas, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, silver booth token.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, silver booth token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
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

### Question 68 - distractor-068
Question: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vera of North Orchard lane, clay watering cup.
- Correctness verdict: grounded
- Evidence used: Vera of North Orchard lane, clay watering cup
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
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

### Question 69 - distractor-069
Question: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, juniper bundles.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, juniper bundles
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 70 - distractor-070
Question: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris?
- Final evaluated answer: Grounded by retrieved evidence for: Lina of Birch Ferry shed, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: Lina of Birch Ferry shed, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Lina of Birch Ferry shed
- smoke vent chain

Expected distractors:
- Boris of Birch Ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Lina of Birch Ferry shed, smoke vent chain missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lina of Birch Ferry shed, smoke vent chain missing=none distractors=none

### Question 71 - distractor-071
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 27 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 27 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
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

### Question 72 - distractor-072
Question: Which place held the true profile detail for Yara, not the nearly identical place name?
- Final evaluated answer: Partially grounded by: Cloud Wharf office, linen wick.
- Correctness verdict: partial
- Evidence used: Cloud Wharf office, linen wick
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=partial coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing Cloud Wharf office, linen wick
- Distractors / false positives: none

Expected evidence:
- Cloud Wharf office
- linen wick

Expected distractors:
- Fox Hollow bridge

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Cloud Wharf office, linen wick distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=Cloud Wharf office, linen wick missing=none distractors=none

### Question 73 - distractor-073
Question: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Lev of Ridge Post loft, star ledger page.
- Correctness verdict: grounded
- Evidence used: Lev of Ridge Post loft, star ledger page
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing star ledger page, Lev of Ridge Post loft
- Distractors / false positives: none

Expected evidence:
- star ledger page
- Lev of Ridge Post loft

Expected distractors:
- rope bridge permit

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=star ledger page, Lev of Ridge Post loft distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lev of Ridge Post loft, star ledger page missing=none distractors=none

### Question 74 - distractor-074
Question: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, lantern hook.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Willow Courtyard well, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
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

### Question 75 - distractor-075
Question: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia?
- Final evaluated answer: Grounded by retrieved evidence for: Pavel of Bell Bridge square, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: Pavel of Bell Bridge square, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Pavel of Bell Bridge square
- weathered camera strap

Expected distractors:
- Talia of Bell Bridge square

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Pavel of Bell Bridge square, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Pavel of Bell Bridge square, weathered camera strap missing=none distractors=none

### Question 76 - distractor-076
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 14 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 14 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing March 14 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 14 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 15 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=Cedar Hill station missing=March 14 Bellwater Fair distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 14 Bellwater Fair missing=none distractors=none

### Question 77 - distractor-077
Question: Which place held the true profile detail for Damir, not the nearly identical place name?
- Final evaluated answer: No winning answer summary available.
- Correctness verdict: unknown
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `none`
- Why it won: NO_MODEL_PASSED_QUESTION_QUALITY_GATE
- What the losing model missed or got wrong: multilingual_e5_small missing Moon Mill yard, tin key; bge_m3 missing Moon Mill yard, tin key
- Distractors / false positives: none

Expected evidence:
- Moon Mill yard
- tin key

Expected distractors:
- Hollow Market arcade

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, tin key distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, tin key distractors=none

### Question 78 - distractor-078
Question: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Nessa of Winter Chapel porch, blue oar.
- Correctness verdict: grounded
- Evidence used: Nessa of Winter Chapel porch, blue oar
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 79 - distractor-079
Question: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, willow basket.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 80 - distractor-080
Question: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas?
- Final evaluated answer: Grounded by retrieved evidence for: Mira of Star Basin gallery, paper moon mask.
- Correctness verdict: grounded
- Evidence used: Mira of Star Basin gallery, paper moon mask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Mira of Star Basin gallery
- paper moon mask

Expected distractors:
- Tomas of Star Basin gallery

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Mira of Star Basin gallery, paper moon mask missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Mira of Star Basin gallery, paper moon mask missing=none distractors=none

### Question 81 - distractor-081
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 19 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 19 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing March 19 Bellwater Fair
- Distractors / false positives: none

Expected evidence:
- March 19 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 20 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=North Bell workshop missing=March 19 Bellwater Fair distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=March 19 Bellwater Fair, North Bell workshop missing=none distractors=none

### Question 82 - distractor-082
Question: Which place held the true profile detail for Kira, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Blue Trunk cabin
- copper wind vane pin

Expected distractors:
- East Signal room

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Blue Trunk cabin, copper wind vane pin missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Blue Trunk cabin, copper wind vane pin missing=none distractors=none

### Question 83 - distractor-083
Question: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Petar of North Orchard lane, coal stove hiss.
- Correctness verdict: grounded
- Evidence used: Petar of North Orchard lane, coal stove hiss
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 84 - distractor-084
Question: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, violet ribbon.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
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

### Question 85 - distractor-085
Question: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara?
- Final evaluated answer: Grounded by retrieved evidence for: Stefan of Birch Ferry shed, tuning fork.
- Correctness verdict: grounded
- Evidence used: Stefan of Birch Ferry shed, tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Stefan of Birch Ferry shed
- tuning fork

Expected distractors:
- Yara of Birch Ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Stefan of Birch Ferry shed, tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Stefan of Birch Ferry shed, tuning fork missing=none distractors=none

### Question 86 - distractor-086
Question: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Lantern Row kiosk, March 24 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Lantern Row kiosk, March 24 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- March 24 Bellwater Fair
- Lantern Row kiosk

Expected distractors:
- March 25 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 24 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Lantern Row kiosk, March 24 Bellwater Fair missing=none distractors=none

### Question 87 - distractor-087
Question: Which place held the true profile detail for Nikola, not the nearly identical place name?
- Final evaluated answer: Partially grounded by: Cloud Wharf office, oak barrel hoops.
- Correctness verdict: partial
- Evidence used: Cloud Wharf office, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=partial coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing Cloud Wharf office, oak barrel hoops
- Distractors / false positives: none

Expected evidence:
- Cloud Wharf office
- oak barrel hoops

Expected distractors:
- Fox Hollow bridge

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Cloud Wharf office, oak barrel hoops distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=Cloud Wharf office, oak barrel hoops missing=none distractors=none

### Question 88 - distractor-088
Question: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Sonya of Ridge Post loft, blue glass jar.
- Correctness verdict: grounded
- Evidence used: Sonya of Ridge Post loft, blue glass jar
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 89 - distractor-089
Question: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor?
- Final evaluated answer: Partially grounded by: Signal Lantern Morning at Willow Courtyard well, canal route map.
- Correctness verdict: partial
- Evidence used: Signal Lantern Morning at Willow Courtyard well, canal route map
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=partial coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing Signal Lantern Morning at Willow Courtyard well, canal route map
- Distractors / false positives: none

Expected evidence:
- Signal Lantern Morning at Willow Courtyard well
- canal route map

Expected distractors:
- Bridgefire Supper at Willow Courtyard well

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Signal Lantern Morning at Willow Courtyard well, canal route map distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=Signal Lantern Morning at Willow Courtyard well, canal route map missing=none distractors=none

### Question 90 - distractor-090
Question: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir?
- Final evaluated answer: Grounded by retrieved evidence for: Selma of Bell Bridge square, cedar shovel.
- Correctness verdict: grounded
- Evidence used: Selma of Bell Bridge square, cedar shovel
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Selma of Bell Bridge square
- cedar shovel

Expected distractors:
- Damir of Bell Bridge square

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Selma of Bell Bridge square, cedar shovel missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Selma of Bell Bridge square, cedar shovel missing=none distractors=none

### Question 91 - distractor-091
Question: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: Cedar Hill station, March 11 Bellwater Fair.
- Correctness verdict: grounded
- Evidence used: Cedar Hill station, March 11 Bellwater Fair
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- March 11 Bellwater Fair
- Cedar Hill station

Expected distractors:
- March 12 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 11 Bellwater Fair missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cedar Hill station, March 11 Bellwater Fair missing=none distractors=none

### Question 92 - distractor-092
Question: Which place held the true profile detail for Zora, not the nearly identical place name?
- Final evaluated answer: No winning answer summary available.
- Correctness verdict: unknown
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `none`
- Why it won: NO_MODEL_PASSED_QUESTION_QUALITY_GATE
- What the losing model missed or got wrong: multilingual_e5_small missing Moon Mill yard, moonflower cutting; bge_m3 missing Moon Mill yard, moonflower cutting
- Distractors / false positives: none

Expected evidence:
- Moon Mill yard
- moonflower cutting

Expected distractors:
- Hollow Market arcade

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, moonflower cutting distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=Moon Mill yard, moonflower cutting distractors=none

### Question 93 - distractor-093
Question: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Vesna of Winter Chapel porch, birch tea flask.
- Correctness verdict: grounded
- Evidence used: Vesna of Winter Chapel porch, birch tea flask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 94 - distractor-094
Question: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, saffron scarf.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at Marble stair hall, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 95 - distractor-095
Question: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira?
- Final evaluated answer: Grounded by retrieved evidence for: Ilya of Star Basin gallery, carved shell comb.
- Correctness verdict: grounded
- Evidence used: Ilya of Star Basin gallery, carved shell comb
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Ilya of Star Basin gallery
- carved shell comb

Expected distractors:
- Kira of Star Basin gallery

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Ilya of Star Basin gallery, carved shell comb missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Ilya of Star Basin gallery, carved shell comb missing=none distractors=none

### Question 96 - distractor-096
Question: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice?
- Final evaluated answer: Grounded by retrieved evidence for: March 16 Bellwater Fair, North Bell workshop.
- Correctness verdict: grounded
- Evidence used: March 16 Bellwater Fair, North Bell workshop
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- March 16 Bellwater Fair
- North Bell workshop

Expected distractors:
- March 17 Bellwater Fair

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=March 16 Bellwater Fair, North Bell workshop missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=March 16 Bellwater Fair, North Bell workshop missing=none distractors=none

### Question 97 - distractor-097
Question: Which place held the true profile detail for Boris, not the nearly identical place name?
- Final evaluated answer: Grounded by retrieved evidence for: Blue Trunk cabin, basalt sketch.
- Correctness verdict: grounded
- Evidence used: Blue Trunk cabin, basalt sketch
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 98 - distractor-098
Question: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve?
- Final evaluated answer: Grounded by retrieved evidence for: Daria of North Orchard lane, green apron.
- Correctness verdict: grounded
- Evidence used: Daria of North Orchard lane, green apron
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
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

### Question 99 - distractor-099
Question: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, silver booth token.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning at South Meadow arch, silver booth token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
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

### Question 100 - distractor-100
Question: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola?
- Final evaluated answer: Grounded by retrieved evidence for: Ada of Birch Ferry shed, clay watering cup.
- Correctness verdict: grounded
- Evidence used: Ada of Birch Ferry shed, clay watering cup
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- Ada of Birch Ferry shed
- clay watering cup

Expected distractors:
- Nikola of Birch Ferry shed

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Ada of Birch Ferry shed, clay watering cup missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Ada of Birch Ferry shed, clay watering cup missing=none distractors=none

## Aggregate Client Decision
- Recommended active model: `bge_m3`
- Overall winner: `bge_m3`
- Activation state: `true`
- Runtime retrieval verified: `true`
- Production recommendation: Keep the fake-mode result for test coverage only; use the preserved latest real evaluation for production-facing model decisions.

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
  1. score=50.040476 chunk_id=22530 preview=Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? Case scope id: distractor-twin-innkeepers. Scoped answer summar...
  2. score=26.086485 chunk_id=22531 preview=Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? document innkeeper-letters::distractor-twin-innkeepers: In docu...
  3. score=23.018153 chunk_id=22427 preview=document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Cas...
- Matched markers: Marta of North Inn, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Marta of North Inn, green apron.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=49.948366 chunk_id=22530 preview=Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? Case scope id: distractor-twin-innkeepers. Scoped answer summar...
  2. score=25.994571 chunk_id=22531 preview=Question anchor: Which Marta kept the North Inn ledger, and what detail identified her apron? document innkeeper-letters::distractor-twin-innkeepers: In docu...
  3. score=22.913400 chunk_id=22427 preview=document innkeeper-letters::distractor-twin-innkeepers: In document innkeeper-letters, the verified archive note records Marta of North Inn, green apron. Cas...
- Matched markers: Marta of North Inn, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Marta of North Inn, green apron.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. score=50.764277 chunk_id=22532 preview=Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Case scope id: distractor-j...
  2. score=26.756369 chunk_id=22533 preview=Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? document market-announcemen...
  3. score=23.760443 chunk_id=22428 preview=document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Br...
- Matched markers: Bell Bridge square, June 14 night market
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bell Bridge square, June 14 night market.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.601771 chunk_id=22532 preview=Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? Case scope id: distractor-j...
  2. score=26.602912 chunk_id=22533 preview=Question anchor: Which June market date belongs to the night market at Bell Bridge square rather than the similar daytime notice? document market-announcemen...
  3. score=23.562348 chunk_id=22428 preview=document market-announcements::distractor-june-market-date: In document market-announcements, the verified archive note records June 14 night market, Bell Br...
- Matched markers: Bell Bridge square, June 14 night market
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bell Bridge square, June 14 night market.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. score=25.584900 chunk_id=22535 preview=Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? document workshop-accounts::distractor-two-levs: In document worksh...
  2. score=22.553553 chunk_id=22429 preview=document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case reco...
- Matched markers: Lev the cooper, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev the cooper, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=49.527928 chunk_id=22534 preview=Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? Case scope id: distractor-two-levs. Scoped answer summary for distr...
  2. score=25.565827 chunk_id=22535 preview=Question anchor: Which Lev repaired the oak barrels, not the one who worked by the ferry? document workshop-accounts::distractor-two-levs: In document worksh...
  3. score=22.458199 chunk_id=22429 preview=document workshop-accounts::distractor-two-levs: In document workshop-accounts, the verified archive note records Lev the cooper, oak barrel hoops. Case reco...
- Matched markers: Lev the cooper, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev the cooper, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=50.381235 chunk_id=22536 preview=Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Case scope id: distractor-similar-islands....
  2. score=26.429899 chunk_id=22537 preview=Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? document ferry-shed-notes::distractor-simil...
  3. score=23.379427 chunk_id=22426 preview=document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oa...
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
  1. score=50.163865 chunk_id=22536 preview=Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? Case scope id: distractor-similar-islands....
  2. score=26.174795 chunk_id=22537 preview=Question anchor: Which island shed kept the painted blue oar, and which similar island name is only a distractor? document ferry-shed-notes::distractor-simil...
  3. score=23.121082 chunk_id=22426 preview=document ferry-shed-notes::distractor-similar-islands: In document ferry-shed-notes, the verified archive note records Fog Island ferry shed, painted blue oa...
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
  1. score=50.417664 chunk_id=22538 preview=Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Case scope id: distractor-le...
  2. score=26.418647 chunk_id=22539 preview=Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? document courier-bag-index::...
  3. score=23.383874 chunk_id=22330 preview=document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread....
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
  1. score=50.368763 chunk_id=22538 preview=Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? Case scope id: distractor-le...
  2. score=26.428971 chunk_id=22539 preview=Question anchor: Which winter letter carried the violet wax thread, and which nearly identical name belongs to the wrong season? document courier-bag-index::...
  3. score=23.351033 chunk_id=22330 preview=document courier-bag-index::distractor-letter-mixup: In document courier-bag-index, the verified archive note records Ada's winter letter, violet wax thread....
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
  1. score=26.513654 chunk_id=22541 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=4.637682 chunk_id=22661 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=4.575969 chunk_id=22571 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  4. score=1.545854 chunk_id=22385 preview=document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellw...
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
  1. score=50.690982 chunk_id=22540 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-006. S...
  2. score=26.726622 chunk_id=22541 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=16.704807 chunk_id=22721 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  4. score=4.705554 chunk_id=22601 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  5. score=4.700826 chunk_id=22661 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
- Matched markers: March 16 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 16 Bellwater Fair, North Bell workshop.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=26.131454 chunk_id=22543 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distract...
- Matched markers: Blue Trunk cabin, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Blue Trunk cabin, brass compass.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=49.882175 chunk_id=22542 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? Case scope id: distractor-007. Scoped answer summa...
  2. score=25.939878 chunk_id=22543 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-blue-trunk-cabin-007::distract...
- Matched markers: Blue Trunk cabin, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, brass compass.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

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
  1. score=50.602400 chunk_id=22544 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=26.623244 chunk_id=22545 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=23.546481 chunk_id=22388 preview=document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sony...
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
  1. score=50.637558 chunk_id=22544 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=26.641077 chunk_id=22545 preview=Question anchor: Which object belongs to Sonya's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=23.595689 chunk_id=22388 preview=document distractor-north-orchard-lane-008::distractor-008: In document distractor-north-orchard-lane-008, the verified archive note records linen wick, Sony...
- Matched markers: Sonya of North Orchard lane, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of North Orchard lane, linen wick.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Signal Lantern Morning at South Meadow arch, star ledger page
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=26.302715 chunk_id=22547 preview=Question anchor: Which memory event is the correct one for Emil at South Meadow arch, and which similar event is only a distractor? document distractor-south...
- Matched markers: Signal Lantern Morning at South Meadow arch, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Signal Lantern Morning at South Meadow arch, star ledger page.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

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
  1. score=50.440184 chunk_id=22548 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Case scope id: distractor-010. Scoped answer...
  2. score=26.480414 chunk_id=22549 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? document distractor-birch-ferry-shed-010::dis...
  3. score=23.403023 chunk_id=22337 preview=document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry...
- Matched markers: Selma of Birch Ferry shed, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Birch Ferry shed, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.402832 chunk_id=22548 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? Case scope id: distractor-010. Scoped answer...
  2. score=26.430017 chunk_id=22549 preview=Question anchor: Which Selma kept the correct memory note at Birch Ferry shed, not the similar entry for Damir? document distractor-birch-ferry-shed-010::dis...
  3. score=23.370300 chunk_id=22337 preview=document distractor-birch-ferry-shed-010::distractor-010: In document distractor-birch-ferry-shed-010, the verified archive note records Selma of Birch Ferry...
- Matched markers: Selma of Birch Ferry shed, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Birch Ferry shed, lantern hook.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. score=50.590411 chunk_id=22550 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-011. Sco...
  2. score=26.619163 chunk_id=22551 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  3. score=4.680632 chunk_id=22611 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  4. score=4.619163 chunk_id=22701 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  5. score=4.619163 chunk_id=22671 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
- Matched markers: Lantern Row kiosk, March 21 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 21 Bellwater Fair.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.552242 chunk_id=22550 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-011. Sco...
  2. score=26.584784 chunk_id=22551 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  3. score=4.604621 chunk_id=22671 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  4. score=4.598588 chunk_id=22701 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  5. score=4.581994 chunk_id=22581 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
- Matched markers: Lantern Row kiosk, March 21 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 21 Bellwater Fair.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Cloud Wharf office, wax thread
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=25.873080 chunk_id=22553 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-cloud-wharf-office-012::distract...
- Matched markers: Cloud Wharf office, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Cloud Wharf office, wax thread.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

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
  1. score=50.694446 chunk_id=22554 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-01...
  2. score=26.715014 chunk_id=22555 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  3. score=23.658312 chunk_id=22395 preview=document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridg...
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
  1. score=50.634258 chunk_id=22554 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-01...
  2. score=26.669394 chunk_id=22555 preview=Question anchor: Which object belongs to Vesna's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  3. score=23.594430 chunk_id=22395 preview=document distractor-ridge-post-loft-013::distractor-013: In document distractor-ridge-post-loft-013, the verified archive note records tin key, Vesna of Ridg...
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
  1. score=50.412316 chunk_id=22556 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  2. score=26.409411 chunk_id=22557 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
  3. score=23.372235 chunk_id=22414 preview=document distractor-willow-courtyard-well-014::distractor-014: In document distractor-willow-courtyard-well-014, the verified archive note records Signal Lan...
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
  1. score=50.293126 chunk_id=22556 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  2. score=26.307318 chunk_id=22557 preview=Question anchor: Which memory event is the correct one for Elena at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
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
  1. score=50.470820 chunk_id=22558 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer...
  2. score=26.513746 chunk_id=22559 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::d...
  3. score=23.441533 chunk_id=22331 preview=document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bri...
- Matched markers: Ilya of Bell Bridge square, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Bell Bridge square, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.363568 chunk_id=22558 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? Case scope id: distractor-015. Scoped answer...
  2. score=26.416536 chunk_id=22559 preview=Question anchor: Which Ilya kept the correct memory note at Bell Bridge square, not the similar entry for Kira? document distractor-bell-bridge-square-015::d...
  3. score=23.341977 chunk_id=22331 preview=document distractor-bell-bridge-square-015::distractor-015: In document distractor-bell-bridge-square-015, the verified archive note records Ilya of Bell Bri...
- Matched markers: Ilya of Bell Bridge square, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Bell Bridge square, willow basket.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. score=4.680632 chunk_id=22651 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  2. score=4.680632 chunk_id=22621 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  3. score=4.680632 chunk_id=22591 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  4. score=4.619163 chunk_id=22711 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  5. score=1.596230 chunk_id=22354 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
- Matched markers: Cedar Hill station
- Missing markers: March 26 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 26 Bellwater Fair.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.562593 chunk_id=22560 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-016. Sc...
  2. score=26.612089 chunk_id=22561 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  3. score=4.595706 chunk_id=22651 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  4. score=4.583206 chunk_id=22621 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  5. score=4.571784 chunk_id=22711 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
- Matched markers: Cedar Hill station, March 26 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 26 Bellwater Fair.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Moon Mill yard, glass ink bottle
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Moon Mill yard, glass ink bottle
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `none`
  - NO_MODEL_PASSED_QUESTION_QUALITY_GATE

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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: copper wind vane pin, Daria of Winter Chapel porch
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.446422 chunk_id=22564 preview=Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=26.451214 chunk_id=22565 preview=Question anchor: Which object belongs to Daria's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  3. score=23.406583 chunk_id=22420 preview=document distractor-winter-chapel-porch-018::distractor-018: In document distractor-winter-chapel-porch-018, the verified archive note records copper wind va...
- Matched markers: Daria of Winter Chapel porch, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of Winter Chapel porch, copper wind vane pin.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

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
  1. score=26.361438 chunk_id=22567 preview=Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? document distractor-marbl...
- Matched markers: Signal Lantern Morning at Marble stair hall, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Signal Lantern Morning at Marble stair hall, coal stove hiss.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.284887 chunk_id=22566 preview=Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor...
  2. score=26.297157 chunk_id=22567 preview=Question anchor: Which memory event is the correct one for Oren at Marble stair hall, and which similar event is only a distractor? document distractor-marbl...
  3. score=23.246955 chunk_id=22369 preview=document distractor-marble-stair-hall-019::distractor-019: In document distractor-marble-stair-hall-019, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at Marble stair hall, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Marble stair hall, coal stove hiss.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=50.575567 chunk_id=22568 preview=Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Case scope id: distractor-020. Scoped answer...
  2. score=26.619465 chunk_id=22569 preview=Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? document distractor-star-basin-gallery-020::...
  3. score=23.553318 chunk_id=22408 preview=document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basi...
- Matched markers: Ada of Star Basin gallery, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Star Basin gallery, violet ribbon.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.432682 chunk_id=22568 preview=Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? Case scope id: distractor-020. Scoped answer...
  2. score=26.468230 chunk_id=22569 preview=Question anchor: Which Ada kept the correct memory note at Star Basin gallery, not the similar entry for Nikola? document distractor-star-basin-gallery-020::...
  3. score=23.408002 chunk_id=22408 preview=document distractor-star-basin-gallery-020::distractor-020: In document distractor-star-basin-gallery-020, the verified archive note records Ada of Star Basi...
- Matched markers: Ada of Star Basin gallery, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Star Basin gallery, violet ribbon.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. score=50.522566 chunk_id=22570 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-021. S...
  2. score=26.575969 chunk_id=22571 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=4.637682 chunk_id=22661 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  4. score=4.513654 chunk_id=22541 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  5. score=1.545854 chunk_id=22385 preview=document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellw...
- Matched markers: March 13 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 13 Bellwater Fair, North Bell workshop.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=26.686666 chunk_id=22571 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=4.726622 chunk_id=22541 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=4.705554 chunk_id=22601 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  4. score=4.704807 chunk_id=22721 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  5. score=4.700826 chunk_id=22661 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
- Matched markers: March 13 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 13 Bellwater Fair, North Bell workshop.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. score=26.081988 chunk_id=22573 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distracto...
- Matched markers: Blue Trunk cabin, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Blue Trunk cabin, rope bridge permit.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=25.926180 chunk_id=22573 preview=Question anchor: Which place held the true profile detail for Talia, not the nearly identical place name? document distractor-blue-trunk-cabin-022::distracto...
- Matched markers: Blue Trunk cabin, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Blue Trunk cabin, rope bridge permit.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

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
  1. score=50.592345 chunk_id=22574 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=26.638530 chunk_id=22575 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-nort...
  3. score=23.517504 chunk_id=22389 preview=document distractor-north-orchard-lane-023::distractor-023: In document distractor-north-orchard-lane-023, the verified archive note records oak barrel hoops...
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
  1. score=50.611018 chunk_id=22574 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=26.620110 chunk_id=22575 preview=Question anchor: Which object belongs to Viktor's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-nort...
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
  1. score=50.505458 chunk_id=22576 preview=Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  2. score=26.504120 chunk_id=22577 preview=Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  3. score=23.483535 chunk_id=22402 preview=document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Mor...
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
  1. score=50.319581 chunk_id=22576 preview=Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  2. score=26.328564 chunk_id=22577 preview=Question anchor: Which memory event is the correct one for Iveta at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
  3. score=23.282802 chunk_id=22402 preview=document distractor-south-meadow-arch-024::distractor-024: In document distractor-south-meadow-arch-024, the verified archive note records Signal Lantern Mor...
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
  1. score=26.404040 chunk_id=22579 preview=Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? document distractor-birch-ferry-shed-025::dist...
- Matched markers: Anton of Birch Ferry shed, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Anton of Birch Ferry shed, canal route map.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.404721 chunk_id=22578 preview=Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? Case scope id: distractor-025. Scoped answer s...
  2. score=26.431859 chunk_id=22579 preview=Question anchor: Which Anton kept the correct memory note at Birch Ferry shed, not the similar entry for Zora? document distractor-birch-ferry-shed-025::dist...
  3. score=23.370755 chunk_id=22338 preview=document distractor-birch-ferry-shed-025::distractor-025: In document distractor-birch-ferry-shed-025, the verified archive note records Anton of Birch Ferry...
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
  1. score=50.590411 chunk_id=22580 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-026. Sco...
  2. score=26.619163 chunk_id=22581 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  3. score=4.680632 chunk_id=22611 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  4. score=4.619163 chunk_id=22701 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  5. score=4.619163 chunk_id=22671 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
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
  1. score=50.543440 chunk_id=22580 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-026. Sco...
  2. score=26.581994 chunk_id=22581 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  3. score=4.604621 chunk_id=22671 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  4. score=4.598588 chunk_id=22701 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  5. score=4.584784 chunk_id=22551 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
- Matched markers: Lantern Row kiosk, March 18 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 18 Bellwater Fair.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Cloud Wharf office, copper token
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=25.877652 chunk_id=22583 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-cloud-wharf-office-027::distrac...
- Matched markers: Cloud Wharf office, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Cloud Wharf office, copper token.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

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
  1. score=50.640705 chunk_id=22584 preview=Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-028...
  2. score=26.659881 chunk_id=22585 preview=Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-pos...
  3. score=23.596371 chunk_id=22396 preview=document distractor-ridge-post-loft-028::distractor-028: In document distractor-ridge-post-loft-028, the verified archive note records moonflower cutting, Ve...
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
  1. score=50.597716 chunk_id=22584 preview=Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-028...
  2. score=26.624375 chunk_id=22585 preview=Question anchor: Which object belongs to Vera's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-pos...
  3. score=23.556589 chunk_id=22396 preview=document distractor-ridge-post-loft-028::distractor-028: In document distractor-ridge-post-loft-028, the verified archive note records moonflower cutting, Ve...
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
  1. score=50.429484 chunk_id=22586 preview=Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  2. score=26.423021 chunk_id=22587 preview=Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
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
  1. score=26.298559 chunk_id=22587 preview=Question anchor: Which memory event is the correct one for Soren at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Signal Lantern Morning at Willow Courtyard well, birch tea flask.
- Verdict: partial

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
  1. score=50.340738 chunk_id=22588 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Case scope id: distractor-030. Scoped answer...
  2. score=26.435001 chunk_id=22589 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? document distractor-bell-bridge-square-030::...
- Matched markers: Lina of Bell Bridge square, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lina of Bell Bridge square, saffron scarf.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.382147 chunk_id=22588 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? Case scope id: distractor-030. Scoped answer...
  2. score=26.431132 chunk_id=22589 preview=Question anchor: Which Lina kept the correct memory note at Bell Bridge square, not the similar entry for Boris? document distractor-bell-bridge-square-030::...
  3. score=23.358570 chunk_id=22332 preview=document distractor-bell-bridge-square-030::distractor-030: In document distractor-bell-bridge-square-030, the verified archive note records Lina of Bell Bri...
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
  1. score=50.634257 chunk_id=22590 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-031. Sc...
  2. score=26.680632 chunk_id=22591 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  3. score=23.596230 chunk_id=22352 preview=document distractor-cedar-hill-station-031::distractor-031: In document distractor-cedar-hill-station-031, the verified archive note records March 23 Bellwat...
  4. score=4.680632 chunk_id=22651 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  5. score=4.680632 chunk_id=22621 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
- Matched markers: Cedar Hill station, March 23 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 23 Bellwater Fair.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=26.560308 chunk_id=22591 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  2. score=4.612089 chunk_id=22561 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  3. score=4.595706 chunk_id=22651 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  4. score=4.583206 chunk_id=22621 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  5. score=4.571784 chunk_id=22711 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
- Matched markers: Cedar Hill station, March 23 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 23 Bellwater Fair.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Moon Mill yard, amber lantern
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Moon Mill yard, amber lantern
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `none`
  - NO_MODEL_PASSED_QUESTION_QUALITY_GATE

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
  1. score=50.442345 chunk_id=22594 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-...
  2. score=26.470608 chunk_id=22595 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter...
  3. score=23.386967 chunk_id=22421 preview=document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch,...
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
  1. score=50.418969 chunk_id=22594 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distractor-...
  2. score=26.419457 chunk_id=22595 preview=Question anchor: Which object belongs to Lev's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-winter...
  3. score=23.379841 chunk_id=22421 preview=document distractor-winter-chapel-porch-033::distractor-033: In document distractor-winter-chapel-porch-033, the verified archive note records basalt sketch,...
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
  1. score=50.429484 chunk_id=22596 preview=Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  2. score=26.423021 chunk_id=22597 preview=Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
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
  1. score=50.264632 chunk_id=22596 preview=Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  2. score=26.275676 chunk_id=22597 preview=Question anchor: Which memory event is the correct one for Raisa at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
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
  1. score=50.565466 chunk_id=22598 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Case scope id: distractor-035. Scoped answe...
  2. score=26.594998 chunk_id=22599 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035:...
  3. score=23.546391 chunk_id=22409 preview=document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Ba...
- Matched markers: Pavel of Star Basin gallery, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Pavel of Star Basin gallery, silver booth token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.424273 chunk_id=22598 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? Case scope id: distractor-035. Scoped answe...
  2. score=26.472658 chunk_id=22599 preview=Question anchor: Which Pavel kept the correct memory note at Star Basin gallery, not the similar entry for Talia? document distractor-star-basin-gallery-035:...
  3. score=23.410546 chunk_id=22409 preview=document distractor-star-basin-gallery-035::distractor-035: In document distractor-star-basin-gallery-035, the verified archive note records Pavel of Star Ba...
- Matched markers: Pavel of Star Basin gallery, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Pavel of Star Basin gallery, silver booth token.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. score=4.637682 chunk_id=22661 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=4.575969 chunk_id=22571 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=4.513654 chunk_id=22541 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  4. score=1.545854 chunk_id=22385 preview=document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellw...
- Matched markers: North Bell workshop
- Missing markers: March 10 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 10 Bellwater Fair.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.672995 chunk_id=22600 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-036. S...
  2. score=26.705554 chunk_id=22601 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=4.726622 chunk_id=22541 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  4. score=4.704807 chunk_id=22721 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  5. score=4.700826 chunk_id=22661 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
- Matched markers: March 10 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 10 Bellwater Fair, North Bell workshop.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=50.111395 chunk_id=22602 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-037. Scoped answer summar...
  2. score=26.192219 chunk_id=22603 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-blue-trunk-cabin-037::distracto...
  3. score=23.030330 chunk_id=22346 preview=document distractor-blue-trunk-cabin-037::distractor-037: In document distractor-blue-trunk-cabin-037, the verified archive note records Blue Trunk cabin, ju...
- Matched markers: Blue Trunk cabin, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, juniper bundles.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=49.923079 chunk_id=22602 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? Case scope id: distractor-037. Scoped answer summar...
  2. score=25.972885 chunk_id=22603 preview=Question anchor: Which place held the true profile detail for Damir, not the nearly identical place name? document distractor-blue-trunk-cabin-037::distracto...
- Matched markers: Blue Trunk cabin, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, juniper bundles.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

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
  1. score=50.573625 chunk_id=22604 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=26.580880 chunk_id=22605 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=23.522848 chunk_id=22390 preview=document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain...
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
  1. score=50.639611 chunk_id=22604 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=26.656750 chunk_id=22605 preview=Question anchor: Which object belongs to Nessa's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=23.603636 chunk_id=22390 preview=document distractor-north-orchard-lane-038::distractor-038: In document distractor-north-orchard-lane-038, the verified archive note records smoke vent chain...
- Matched markers: Nessa of North Orchard lane, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Nessa of North Orchard lane, smoke vent chain.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Signal Lantern Morning at South Meadow arch, brass compass
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.267952 chunk_id=22606 preview=Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  2. score=26.297281 chunk_id=22607 preview=Question anchor: Which memory event is the correct one for Milan at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
- Matched markers: Signal Lantern Morning at South Meadow arch, brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, brass compass.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

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
  1. score=50.430584 chunk_id=22608 preview=Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Case scope id: distractor-040. Scoped answer s...
  2. score=26.494225 chunk_id=22609 preview=Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? document distractor-birch-ferry-shed-040::dist...
  3. score=23.391864 chunk_id=22339 preview=document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry...
- Matched markers: Mira of Birch Ferry shed, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Mira of Birch Ferry shed, linen wick.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.411246 chunk_id=22608 preview=Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? Case scope id: distractor-040. Scoped answer s...
  2. score=26.427922 chunk_id=22609 preview=Question anchor: Which Mira kept the correct memory note at Birch Ferry shed, not the similar entry for Tomas? document distractor-birch-ferry-shed-040::dist...
  3. score=23.370755 chunk_id=22339 preview=document distractor-birch-ferry-shed-040::distractor-040: In document distractor-birch-ferry-shed-040, the verified archive note records Mira of Birch Ferry...
- Matched markers: Mira of Birch Ferry shed, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Mira of Birch Ferry shed, linen wick.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. score=50.634257 chunk_id=22610 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-041. Sco...
  2. score=26.680632 chunk_id=22611 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  3. score=23.596230 chunk_id=22365 preview=document distractor-lantern-row-kiosk-041::distractor-041: In document distractor-lantern-row-kiosk-041, the verified archive note records March 15 Bellwater...
  4. score=4.619163 chunk_id=22701 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  5. score=4.619163 chunk_id=22671 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
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
  1. score=26.547566 chunk_id=22611 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  2. score=4.604621 chunk_id=22671 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  3. score=4.598588 chunk_id=22701 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  4. score=4.584784 chunk_id=22551 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  5. score=4.581994 chunk_id=22581 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
- Matched markers: Lantern Row kiosk, March 15 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 15 Bellwater Fair.
- Verdict: grounded

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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Cloud Wharf office, lantern hook
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Cloud Wharf office, lantern hook
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `none`
  - NO_MODEL_PASSED_QUESTION_QUALITY_GATE

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
  1. score=50.694446 chunk_id=22614 preview=Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-04...
  2. score=26.715014 chunk_id=22615 preview=Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  3. score=23.658312 chunk_id=22397 preview=document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap...
- Matched markers: Petar of Ridge Post loft, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Petar of Ridge Post loft, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.607624 chunk_id=22614 preview=Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-04...
  2. score=26.634445 chunk_id=22615 preview=Question anchor: Which object belongs to Petar's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  3. score=23.578305 chunk_id=22397 preview=document distractor-ridge-post-loft-043::distractor-043: In document distractor-ridge-post-loft-043, the verified archive note records weathered camera strap...
- Matched markers: Petar of Ridge Post loft, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Petar of Ridge Post loft, weathered camera strap.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. score=50.412316 chunk_id=22616 preview=Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  2. score=26.409411 chunk_id=22617 preview=Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
  3. score=23.372235 chunk_id=22416 preview=document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lan...
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
  1. score=50.305589 chunk_id=22616 preview=Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  2. score=26.311878 chunk_id=22617 preview=Question anchor: Which memory event is the correct one for Anya at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
  3. score=23.263142 chunk_id=22416 preview=document distractor-willow-courtyard-well-044::distractor-044: In document distractor-willow-courtyard-well-044, the verified archive note records Signal Lan...
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
  1. score=50.384206 chunk_id=22618 preview=Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Case scope id: distractor-045. Scoped answe...
  2. score=26.456532 chunk_id=22619 preview=Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? document distractor-bell-bridge-square-045:...
  3. score=23.359503 chunk_id=22333 preview=document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell B...
- Matched markers: Stefan of Bell Bridge square, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Stefan of Bell Bridge square, tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.400909 chunk_id=22618 preview=Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? Case scope id: distractor-045. Scoped answe...
  2. score=26.432319 chunk_id=22619 preview=Question anchor: Which Stefan kept the correct memory note at Bell Bridge square, not the similar entry for Yara? document distractor-bell-bridge-square-045:...
  3. score=23.366664 chunk_id=22333 preview=document distractor-bell-bridge-square-045::distractor-045: In document distractor-bell-bridge-square-045, the verified archive note records Stefan of Bell B...
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
  1. score=50.634257 chunk_id=22620 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-046. Sc...
  2. score=26.680632 chunk_id=22621 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  3. score=23.596230 chunk_id=22353 preview=document distractor-cedar-hill-station-046::distractor-046: In document distractor-cedar-hill-station-046, the verified archive note records March 20 Bellwat...
  4. score=4.680632 chunk_id=22651 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  5. score=4.680632 chunk_id=22591 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
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
  1. score=50.539879 chunk_id=22620 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-046. Sc...
  2. score=26.583206 chunk_id=22621 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  3. score=4.612089 chunk_id=22561 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  4. score=4.595706 chunk_id=22651 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  5. score=4.571784 chunk_id=22711 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
- Matched markers: Cedar Hill station, March 20 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 20 Bellwater Fair.
- Verdict: grounded

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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Moon Mill yard, willow basket
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Moon Mill yard, willow basket
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `none`
  - NO_MODEL_PASSED_QUESTION_QUALITY_GATE

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
  1. score=50.452400 chunk_id=22624 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=26.461180 chunk_id=22625 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  3. score=23.411131 chunk_id=22422 preview=document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mas...
- Matched markers: Sonya of Winter Chapel porch, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of Winter Chapel porch, paper moon mask.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.440163 chunk_id=22624 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=26.443793 chunk_id=22625 preview=Question anchor: Which object belongs to Sonya's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  3. score=23.405291 chunk_id=22422 preview=document distractor-winter-chapel-porch-048::distractor-048: In document distractor-winter-chapel-porch-048, the verified archive note records paper moon mas...
- Matched markers: Sonya of Winter Chapel porch, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Sonya of Winter Chapel porch, paper moon mask.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. score=50.392071 chunk_id=22626 preview=Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? Case scope id: distractor...
- Matched markers: Signal Lantern Morning at Marble stair hall, glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Signal Lantern Morning at Marble stair hall, glass ink bottle.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=26.262314 chunk_id=22627 preview=Question anchor: Which memory event is the correct one for Emil at Marble stair hall, and which similar event is only a distractor? document distractor-marbl...
- Matched markers: Signal Lantern Morning at Marble stair hall, glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Signal Lantern Morning at Marble stair hall, glass ink bottle.
- Verdict: partial

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
  1. score=26.479162 chunk_id=22629 preview=Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? document distractor-star-basin-gallery-050:...
- Matched markers: Selma of Star Basin gallery, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Selma of Star Basin gallery, copper wind vane pin.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.414575 chunk_id=22628 preview=Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? Case scope id: distractor-050. Scoped answe...
  2. score=26.459418 chunk_id=22629 preview=Question anchor: Which Selma kept the correct memory note at Star Basin gallery, not the similar entry for Damir? document distractor-star-basin-gallery-050:...
  3. score=23.392178 chunk_id=22410 preview=document distractor-star-basin-gallery-050::distractor-050: In document distractor-star-basin-gallery-050, the verified archive note records Selma of Star Ba...
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
  1. score=4.637682 chunk_id=22661 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=4.575969 chunk_id=22571 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=4.513654 chunk_id=22541 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  4. score=1.545854 chunk_id=22385 preview=document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellw...
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
  1. score=4.726622 chunk_id=22541 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=4.705554 chunk_id=22601 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=4.704807 chunk_id=22721 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  4. score=4.700826 chunk_id=22661 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  5. score=4.698904 chunk_id=22691 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
- Matched markers: North Bell workshop
- Missing markers: March 25 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 25 Bellwater Fair.
- Verdict: partial

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
  1. score=50.107158 chunk_id=22632 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary...
  2. score=26.185674 chunk_id=22633 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor...
- Matched markers: Blue Trunk cabin, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, violet ribbon.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=49.903439 chunk_id=22632 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? Case scope id: distractor-052. Scoped answer summary...
  2. score=25.950163 chunk_id=22633 preview=Question anchor: Which place held the true profile detail for Zora, not the nearly identical place name? document distractor-blue-trunk-cabin-052::distractor...
- Matched markers: Blue Trunk cabin, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, violet ribbon.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

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
  1. score=50.602400 chunk_id=22634 preview=Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=26.611180 chunk_id=22635 preview=Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=23.561131 chunk_id=22391 preview=document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Ves...
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
  1. score=50.635451 chunk_id=22634 preview=Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=26.659906 chunk_id=22635 preview=Question anchor: Which object belongs to Vesna's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=23.597737 chunk_id=22391 preview=document distractor-north-orchard-lane-053::distractor-053: In document distractor-north-orchard-lane-053, the verified archive note records tuning fork, Ves...
- Matched markers: Vesna of North Orchard lane, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vesna of North Orchard lane, tuning fork.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=26.417835 chunk_id=22637 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
- Matched markers: Signal Lantern Morning at South Meadow arch, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Signal Lantern Morning at South Meadow arch, rope bridge permit.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.274415 chunk_id=22636 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  2. score=26.303101 chunk_id=22637 preview=Question anchor: Which memory event is the correct one for Elena at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
- Matched markers: Signal Lantern Morning at South Meadow arch, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, rope bridge permit.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=50.470820 chunk_id=22638 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Case scope id: distractor-055. Scoped answer su...
  2. score=26.513746 chunk_id=22639 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? document distractor-birch-ferry-shed-055::distr...
  3. score=23.441533 chunk_id=22340 preview=document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry...
- Matched markers: Ilya of Birch Ferry shed, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Birch Ferry shed, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.383846 chunk_id=22638 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? Case scope id: distractor-055. Scoped answer su...
  2. score=26.430711 chunk_id=22639 preview=Question anchor: Which Ilya kept the correct memory note at Birch Ferry shed, not the similar entry for Kira? document distractor-birch-ferry-shed-055::distr...
  3. score=23.361048 chunk_id=22340 preview=document distractor-birch-ferry-shed-055::distractor-055: In document distractor-birch-ferry-shed-055, the verified archive note records Ilya of Birch Ferry...
- Matched markers: Ilya of Birch Ferry shed, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ilya of Birch Ferry shed, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. score=4.680632 chunk_id=22611 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  2. score=4.619163 chunk_id=22701 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  3. score=4.619163 chunk_id=22671 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  4. score=4.619163 chunk_id=22581 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  5. score=4.619163 chunk_id=22551 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
- Matched markers: Lantern Row kiosk
- Missing markers: March 12 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Lantern Row kiosk. Missing: March 12 Bellwater Fair.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=26.552740 chunk_id=22641 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  2. score=4.604621 chunk_id=22671 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  3. score=4.598588 chunk_id=22701 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  4. score=4.584784 chunk_id=22551 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  5. score=4.581994 chunk_id=22581 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
- Matched markers: Lantern Row kiosk, March 12 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 12 Bellwater Fair.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Cloud Wharf office, canal route map
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Cloud Wharf office, canal route map
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `none`
  - NO_MODEL_PASSED_QUESTION_QUALITY_GATE

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
  1. score=50.617285 chunk_id=22644 preview=Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-05...
  2. score=26.624200 chunk_id=22645 preview=Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
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
  1. score=50.643128 chunk_id=22644 preview=Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-05...
  2. score=26.675343 chunk_id=22645 preview=Question anchor: Which object belongs to Daria's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  3. score=23.592462 chunk_id=22398 preview=document distractor-ridge-post-loft-058::distractor-058: In document distractor-ridge-post-loft-058, the verified archive note records cedar shovel, Daria of...
- Matched markers: Daria of Ridge Post loft, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of Ridge Post loft, cedar shovel.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=50.412316 chunk_id=22646 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  2. score=26.409411 chunk_id=22647 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
  3. score=23.372235 chunk_id=22417 preview=document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lan...
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
  1. score=50.310219 chunk_id=22646 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distra...
  2. score=26.320755 chunk_id=22647 preview=Question anchor: Which memory event is the correct one for Oren at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
  3. score=23.274251 chunk_id=22417 preview=document distractor-willow-courtyard-well-059::distractor-059: In document distractor-willow-courtyard-well-059, the verified archive note records Signal Lan...
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
  1. score=50.510742 chunk_id=22648 preview=Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Case scope id: distractor-060. Scoped answer...
  2. score=26.567988 chunk_id=22649 preview=Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? document distractor-bell-bridge-square-060::...
  3. score=23.478551 chunk_id=22334 preview=document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Brid...
- Matched markers: Ada of Bell Bridge square, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Bell Bridge square, moonflower cutting.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.403663 chunk_id=22648 preview=Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? Case scope id: distractor-060. Scoped answer...
  2. score=26.433140 chunk_id=22649 preview=Question anchor: Which Ada kept the correct memory note at Bell Bridge square, not the similar entry for Nikola? document distractor-bell-bridge-square-060::...
  3. score=23.369939 chunk_id=22334 preview=document distractor-bell-bridge-square-060::distractor-060: In document distractor-bell-bridge-square-060, the verified archive note records Ada of Bell Brid...
- Matched markers: Ada of Bell Bridge square, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Bell Bridge square, moonflower cutting.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. score=50.634257 chunk_id=22650 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-061. Sc...
  2. score=26.680632 chunk_id=22651 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  3. score=23.596230 chunk_id=22354 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
  4. score=4.680632 chunk_id=22621 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  5. score=4.680632 chunk_id=22591 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
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
  1. score=50.556700 chunk_id=22650 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-061. Sc...
  2. score=26.595706 chunk_id=22651 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  3. score=4.612089 chunk_id=22561 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  4. score=4.583206 chunk_id=22621 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  5. score=4.571784 chunk_id=22711 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Moon Mill yard, saffron scarf
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Moon Mill yard, saffron scarf
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `none`
  - NO_MODEL_PASSED_QUESTION_QUALITY_GATE

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
  1. score=50.401506 chunk_id=22654 preview=Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distract...
  2. score=26.413798 chunk_id=22655 preview=Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-win...
  3. score=23.353637 chunk_id=22423 preview=document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell c...
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
  1. score=50.467308 chunk_id=22654 preview=Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distract...
  2. score=26.496311 chunk_id=22655 preview=Question anchor: Which object belongs to Viktor's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-win...
  3. score=23.434232 chunk_id=22423 preview=document distractor-winter-chapel-porch-063::distractor-063: In document distractor-winter-chapel-porch-063, the verified archive note records carved shell c...
- Matched markers: Viktor of Winter Chapel porch, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Viktor of Winter Chapel porch, carved shell comb.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=50.454674 chunk_id=22656 preview=Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  2. score=26.426242 chunk_id=22657 preview=Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  3. score=23.409536 chunk_id=22372 preview=document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Mor...
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
  1. score=50.272588 chunk_id=22656 preview=Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  2. score=26.285232 chunk_id=22657 preview=Question anchor: Which memory event is the correct one for Iveta at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  3. score=23.232027 chunk_id=22372 preview=document distractor-marble-stair-hall-064::distractor-064: In document distractor-marble-stair-hall-064, the verified archive note records Signal Lantern Mor...
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
  1. score=50.483231 chunk_id=22658 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Case scope id: distractor-065. Scoped answer...
  2. score=26.542611 chunk_id=22659 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::...
  3. score=23.466769 chunk_id=22411 preview=document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Ba...
- Matched markers: Anton of Star Basin gallery, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Anton of Star Basin gallery, basalt sketch.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.423969 chunk_id=22658 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? Case scope id: distractor-065. Scoped answer...
  2. score=26.467168 chunk_id=22659 preview=Question anchor: Which Anton kept the correct memory note at Star Basin gallery, not the similar entry for Zora? document distractor-star-basin-gallery-065::...
  3. score=23.402567 chunk_id=22411 preview=document distractor-star-basin-gallery-065::distractor-065: In document distractor-star-basin-gallery-065, the verified archive note records Anton of Star Ba...
- Matched markers: Anton of Star Basin gallery, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Anton of Star Basin gallery, basalt sketch.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. score=50.588244 chunk_id=22660 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. S...
  2. score=26.637682 chunk_id=22661 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=23.545854 chunk_id=22385 preview=document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellw...
  4. score=4.575969 chunk_id=22571 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  5. score=4.513654 chunk_id=22541 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
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
  1. score=50.669845 chunk_id=22660 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-066. S...
  2. score=26.700826 chunk_id=22661 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=4.726622 chunk_id=22541 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  4. score=4.705554 chunk_id=22601 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  5. score=4.704807 chunk_id=22721 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
- Matched markers: March 22 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 22 Bellwater Fair, North Bell workshop.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=50.111395 chunk_id=22662 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-067. Scoped answer summar...
  2. score=26.146926 chunk_id=22663 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distracto...
- Matched markers: Blue Trunk cabin, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, silver booth token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=49.899522 chunk_id=22662 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? Case scope id: distractor-067. Scoped answer summar...
  2. score=25.948775 chunk_id=22663 preview=Question anchor: Which place held the true profile detail for Tomas, not the nearly identical place name? document distractor-blue-trunk-cabin-067::distracto...
- Matched markers: Blue Trunk cabin, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, silver booth token.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

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
  1. score=50.551506 chunk_id=22664 preview=Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-...
  2. score=26.563798 chunk_id=22665 preview=Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-...
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
  1. score=50.592794 chunk_id=22664 preview=Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor-...
  2. score=26.594356 chunk_id=22665 preview=Question anchor: Which object belongs to Vera's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north-...
- Matched markers: Vera of North Orchard lane, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Vera of North Orchard lane, clay watering cup.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=50.449507 chunk_id=22666 preview=Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  2. score=26.442825 chunk_id=22667 preview=Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
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
  1. score=50.293135 chunk_id=22666 preview=Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? Case scope id: distracto...
  2. score=26.314226 chunk_id=22667 preview=Question anchor: Which memory event is the correct one for Soren at South Meadow arch, and which similar event is only a distractor? document distractor-sout...
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
  1. score=26.393391 chunk_id=22669 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::dist...
- Matched markers: Lina of Birch Ferry shed, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Lina of Birch Ferry shed, smoke vent chain.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.385583 chunk_id=22668 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? Case scope id: distractor-070. Scoped answer s...
  2. score=26.417259 chunk_id=22669 preview=Question anchor: Which Lina kept the correct memory note at Birch Ferry shed, not the similar entry for Boris? document distractor-birch-ferry-shed-070::dist...
  3. score=23.349909 chunk_id=22341 preview=document distractor-birch-ferry-shed-070::distractor-070: In document distractor-birch-ferry-shed-070, the verified archive note records Lina of Birch Ferry...
- Matched markers: Lina of Birch Ferry shed, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lina of Birch Ferry shed, smoke vent chain.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=26.619163 chunk_id=22671 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  2. score=4.680632 chunk_id=22611 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  3. score=4.619163 chunk_id=22701 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  4. score=4.619163 chunk_id=22581 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  5. score=4.619163 chunk_id=22551 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
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
  1. score=50.567201 chunk_id=22670 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-071. Sco...
  2. score=26.604622 chunk_id=22671 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  3. score=4.598588 chunk_id=22701 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  4. score=4.584784 chunk_id=22551 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  5. score=4.581994 chunk_id=22581 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
- Matched markers: Lantern Row kiosk, March 27 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 27 Bellwater Fair.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Cloud Wharf office, linen wick
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=25.866638 chunk_id=22673 preview=Question anchor: Which place held the true profile detail for Yara, not the nearly identical place name? document distractor-cloud-wharf-office-072::distract...
- Matched markers: Cloud Wharf office, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Cloud Wharf office, linen wick.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: star ledger page, Lev of Ridge Post loft
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.564052 chunk_id=22674 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-073....
  2. score=26.559603 chunk_id=22675 preview=Question anchor: Which object belongs to Lev's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-post...
- Matched markers: Lev of Ridge Post loft, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lev of Ridge Post loft, star ledger page.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

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
  1. score=50.429484 chunk_id=22676 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  2. score=26.402886 chunk_id=22677 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
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
  1. score=50.311802 chunk_id=22676 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? Case scope id: distr...
  2. score=26.319163 chunk_id=22677 preview=Question anchor: Which memory event is the correct one for Raisa at Willow Courtyard well, and which similar event is only a distractor? document distractor-...
  3. score=23.270855 chunk_id=22418 preview=document distractor-willow-courtyard-well-074::distractor-074: In document distractor-willow-courtyard-well-074, the verified archive note records Signal Lan...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at Willow Courtyard well, lantern hook.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=26.439602 chunk_id=22679 preview=Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? document distractor-bell-bridge-square-075:...
- Matched markers: Pavel of Bell Bridge square, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Pavel of Bell Bridge square, weathered camera strap.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.380334 chunk_id=22678 preview=Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? Case scope id: distractor-075. Scoped answe...
  2. score=26.429542 chunk_id=22679 preview=Question anchor: Which Pavel kept the correct memory note at Bell Bridge square, not the similar entry for Talia? document distractor-bell-bridge-square-075:...
  3. score=23.357086 chunk_id=22335 preview=document distractor-bell-bridge-square-075::distractor-075: In document distractor-bell-bridge-square-075, the verified archive note records Pavel of Bell Br...
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
  1. score=4.680632 chunk_id=22651 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  2. score=4.680632 chunk_id=22621 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  3. score=4.680632 chunk_id=22591 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  4. score=4.619163 chunk_id=22711 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  5. score=1.596230 chunk_id=22354 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
- Matched markers: Cedar Hill station
- Missing markers: March 14 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cedar Hill station. Missing: March 14 Bellwater Fair.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=26.546547 chunk_id=22681 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  2. score=4.612089 chunk_id=22561 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  3. score=4.595706 chunk_id=22651 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  4. score=4.583206 chunk_id=22621 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  5. score=4.571784 chunk_id=22711 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
- Matched markers: Cedar Hill station, March 14 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 14 Bellwater Fair.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Moon Mill yard, tin key
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Moon Mill yard, tin key
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `none`
  - NO_MODEL_PASSED_QUESTION_QUALITY_GATE

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
  1. score=50.452400 chunk_id=22684 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=26.473244 chunk_id=22685 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  3. score=23.396481 chunk_id=22424 preview=document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Ness...
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
  1. score=50.446629 chunk_id=22684 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=26.464052 chunk_id=22685 preview=Question anchor: Which object belongs to Nessa's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  3. score=23.402122 chunk_id=22424 preview=document distractor-winter-chapel-porch-078::distractor-078: In document distractor-winter-chapel-porch-078, the verified archive note records blue oar, Ness...
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
  1. score=50.473193 chunk_id=22686 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  2. score=26.440345 chunk_id=22687 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
  3. score=23.429423 chunk_id=22373 preview=document distractor-marble-stair-hall-079::distractor-079: In document distractor-marble-stair-hall-079, the verified archive note records Signal Lantern Mor...
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
  1. score=50.247986 chunk_id=22686 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  2. score=26.275238 chunk_id=22687 preview=Question anchor: Which memory event is the correct one for Milan at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
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
  1. score=50.474401 chunk_id=22688 preview=Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Case scope id: distractor-080. Scoped answer...
  2. score=26.541907 chunk_id=22689 preview=Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? document distractor-star-basin-gallery-080::...
  3. score=23.452051 chunk_id=22412 preview=document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Bas...
- Matched markers: Mira of Star Basin gallery, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Mira of Star Basin gallery, paper moon mask.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.442526 chunk_id=22688 preview=Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? Case scope id: distractor-080. Scoped answer...
  2. score=26.476160 chunk_id=22689 preview=Question anchor: Which Mira kept the correct memory note at Star Basin gallery, not the similar entry for Tomas? document distractor-star-basin-gallery-080::...
  3. score=23.415184 chunk_id=22412 preview=document distractor-star-basin-gallery-080::distractor-080: In document distractor-star-basin-gallery-080, the verified archive note records Mira of Star Bas...
- Matched markers: Mira of Star Basin gallery, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Mira of Star Basin gallery, paper moon mask.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
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
  1. score=4.637682 chunk_id=22661 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=4.575969 chunk_id=22571 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=4.513654 chunk_id=22541 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  4. score=1.545854 chunk_id=22385 preview=document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellw...
- Matched markers: North Bell workshop
- Missing markers: March 19 Bellwater Fair
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: March 19 Bellwater Fair.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=26.698904 chunk_id=22691 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=4.726622 chunk_id=22541 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=4.705554 chunk_id=22601 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  4. score=4.704807 chunk_id=22721 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  5. score=4.700826 chunk_id=22661 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
- Matched markers: March 19 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 19 Bellwater Fair, North Bell workshop.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

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
  1. score=26.058463 chunk_id=22693 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor...
- Matched markers: Blue Trunk cabin, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Blue Trunk cabin, copper wind vane pin.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=49.895472 chunk_id=22692 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? Case scope id: distractor-082. Scoped answer summary...
  2. score=25.954459 chunk_id=22693 preview=Question anchor: Which place held the true profile detail for Kira, not the nearly identical place name? document distractor-blue-trunk-cabin-082::distractor...
- Matched markers: Blue Trunk cabin, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, copper wind vane pin.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=50.602400 chunk_id=22694 preview=Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=26.611180 chunk_id=22695 preview=Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=23.561131 chunk_id=22393 preview=document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss,...
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
  1. score=50.602173 chunk_id=22694 preview=Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=26.611364 chunk_id=22695 preview=Question anchor: Which object belongs to Petar's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=23.570988 chunk_id=22393 preview=document distractor-north-orchard-lane-083::distractor-083: In document distractor-north-orchard-lane-083, the verified archive note records coal stove hiss,...
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
  1. score=50.431550 chunk_id=22696 preview=Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  2. score=26.426598 chunk_id=22697 preview=Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? document distractor-south...
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
  1. score=50.307667 chunk_id=22696 preview=Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  2. score=26.324045 chunk_id=22697 preview=Question anchor: Which memory event is the correct one for Anya at South Meadow arch, and which similar event is only a distractor? document distractor-south...
  3. score=23.275395 chunk_id=22406 preview=document distractor-south-meadow-arch-084::distractor-084: In document distractor-south-meadow-arch-084, the verified archive note records Signal Lantern Mor...
- Matched markers: Signal Lantern Morning at South Meadow arch, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning at South Meadow arch, violet ribbon.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=50.340738 chunk_id=22698 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Case scope id: distractor-085. Scoped answer...
  2. score=26.435001 chunk_id=22699 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? document distractor-birch-ferry-shed-085::dis...
- Matched markers: Stefan of Birch Ferry shed, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Stefan of Birch Ferry shed, tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.404721 chunk_id=22698 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? Case scope id: distractor-085. Scoped answer...
  2. score=26.431859 chunk_id=22699 preview=Question anchor: Which Stefan kept the correct memory note at Birch Ferry shed, not the similar entry for Yara? document distractor-birch-ferry-shed-085::dis...
  3. score=23.369181 chunk_id=22342 preview=document distractor-birch-ferry-shed-085::distractor-085: In document distractor-birch-ferry-shed-085, the verified archive note records Stefan of Birch Ferr...
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
  1. score=26.619163 chunk_id=22701 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  2. score=4.680632 chunk_id=22611 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  3. score=4.619163 chunk_id=22671 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  4. score=4.619163 chunk_id=22581 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  5. score=4.619163 chunk_id=22551 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
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
  1. score=50.560035 chunk_id=22700 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? Case scope id: distractor-086. Sco...
  2. score=26.598588 chunk_id=22701 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  3. score=4.604621 chunk_id=22671 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  4. score=4.584784 chunk_id=22551 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
  5. score=4.581994 chunk_id=22581 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Lantern Row kiosk rather than the similar notice? document distractor-lantern-row-ki...
- Matched markers: Lantern Row kiosk, March 24 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Lantern Row kiosk, March 24 Bellwater Fair.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Cloud Wharf office, oak barrel hoops
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=25.872530 chunk_id=22703 preview=Question anchor: Which place held the true profile detail for Nikola, not the nearly identical place name? document distractor-cloud-wharf-office-087::distra...
- Matched markers: Cloud Wharf office, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Cloud Wharf office, oak barrel hoops.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

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
  1. score=50.671491 chunk_id=22704 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-08...
  2. score=26.687792 chunk_id=22705 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  3. score=23.629900 chunk_id=22400 preview=document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya...
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
  1. score=50.607791 chunk_id=22704 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? Case scope id: distractor-08...
  2. score=26.628513 chunk_id=22705 preview=Question anchor: Which object belongs to Sonya's archive scene at Ridge Post loft, not the similar object from Winter Choir Eve? document distractor-ridge-po...
  3. score=23.567296 chunk_id=22400 preview=document distractor-ridge-post-loft-088::distractor-088: In document distractor-ridge-post-loft-088, the verified archive note records blue glass jar, Sonya...
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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Signal Lantern Morning at Willow Courtyard well, canal route map
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=26.309256 chunk_id=22707 preview=Question anchor: Which memory event is the correct one for Emil at Willow Courtyard well, and which similar event is only a distractor? document distractor-w...
- Matched markers: Signal Lantern Morning at Willow Courtyard well, canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Signal Lantern Morning at Willow Courtyard well, canal route map.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

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
  1. score=50.340738 chunk_id=22708 preview=Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Case scope id: distractor-090. Scoped answe...
  2. score=26.435001 chunk_id=22709 preview=Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? document distractor-bell-bridge-square-090:...
- Matched markers: Selma of Bell Bridge square, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Selma of Bell Bridge square, cedar shovel.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.427862 chunk_id=22708 preview=Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? Case scope id: distractor-090. Scoped answe...
  2. score=26.451470 chunk_id=22709 preview=Question anchor: Which Selma kept the correct memory note at Bell Bridge square, not the similar entry for Damir? document distractor-bell-bridge-square-090:...
  3. score=23.380956 chunk_id=22336 preview=document distractor-bell-bridge-square-090::distractor-090: In document distractor-bell-bridge-square-090, the verified archive note records Selma of Bell Br...
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
  1. score=26.619163 chunk_id=22711 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  2. score=4.680632 chunk_id=22651 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  3. score=4.680632 chunk_id=22621 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  4. score=4.680632 chunk_id=22591 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  5. score=1.596230 chunk_id=22354 preview=document distractor-cedar-hill-station-061::distractor-061: In document distractor-cedar-hill-station-061, the verified archive note records March 17 Bellwat...
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
  1. score=50.526860 chunk_id=22710 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? Case scope id: distractor-091. Sc...
  2. score=26.571784 chunk_id=22711 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  3. score=4.612089 chunk_id=22561 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  4. score=4.595706 chunk_id=22651 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
  5. score=4.583206 chunk_id=22621 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at Cedar Hill station rather than the similar notice? document distractor-cedar-hill-st...
- Matched markers: Cedar Hill station, March 11 Bellwater Fair
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cedar Hill station, March 11 Bellwater Fair.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

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
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Moon Mill yard, moonflower cutting
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: Moon Mill yard, moonflower cutting
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `none`
  - NO_MODEL_PASSED_QUESTION_QUALITY_GATE

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
  1. score=50.485565 chunk_id=22714 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=26.510445 chunk_id=22715 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
  3. score=23.440076 chunk_id=22425 preview=document distractor-winter-chapel-porch-093::distractor-093: In document distractor-winter-chapel-porch-093, the verified archive note records birch tea flas...
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
  1. score=50.400887 chunk_id=22714 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? Case scope id: distracto...
  2. score=26.402411 chunk_id=22715 preview=Question anchor: Which object belongs to Vesna's archive scene at Winter Chapel porch, not the similar object from Winter Choir Eve? document distractor-wint...
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
  1. score=50.376011 chunk_id=22716 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  2. score=26.393629 chunk_id=22717 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
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
  1. score=50.235180 chunk_id=22716 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? Case scope id: distracto...
  2. score=26.261783 chunk_id=22717 preview=Question anchor: Which memory event is the correct one for Elena at Marble stair hall, and which similar event is only a distractor? document distractor-marb...
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
  1. score=26.528464 chunk_id=22719 preview=Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? document distractor-star-basin-gallery-095::d...
- Matched markers: Ilya of Star Basin gallery, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Ilya of Star Basin gallery, carved shell comb.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.472105 chunk_id=22718 preview=Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? Case scope id: distractor-095. Scoped answer...
  2. score=26.500867 chunk_id=22719 preview=Question anchor: Which Ilya kept the correct memory note at Star Basin gallery, not the similar entry for Kira? document distractor-star-basin-gallery-095::d...
  3. score=23.448857 chunk_id=22413 preview=document distractor-star-basin-gallery-095::distractor-095: In document distractor-star-basin-gallery-095, the verified archive note records Ilya of Star Bas...
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
  1. score=16.513654 chunk_id=22541 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  2. score=4.637682 chunk_id=22661 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=4.575969 chunk_id=22571 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  4. score=1.545854 chunk_id=22385 preview=document distractor-north-bell-workshop-066::distractor-066: In document distractor-north-bell-workshop-066, the verified archive note records March 22 Bellw...
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
  1. score=50.672995 chunk_id=22720 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? Case scope id: distractor-096. S...
  2. score=26.704807 chunk_id=22721 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  3. score=16.726622 chunk_id=22541 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  4. score=4.705554 chunk_id=22601 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
  5. score=4.700826 chunk_id=22661 preview=Question anchor: Which date belongs to the real Bellwater Fair memory at North Bell workshop rather than the similar notice? document distractor-north-bell-w...
- Matched markers: March 16 Bellwater Fair, North Bell workshop
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: March 16 Bellwater Fair, North Bell workshop.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=50.050282 chunk_id=22722 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summar...
  2. score=26.116465 chunk_id=22723 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distracto...
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
  1. score=49.873675 chunk_id=22722 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? Case scope id: distractor-097. Scoped answer summar...
  2. score=25.926180 chunk_id=22723 preview=Question anchor: Which place held the true profile detail for Boris, not the nearly identical place name? document distractor-blue-trunk-cabin-097::distracto...
- Matched markers: Blue Trunk cabin, basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Blue Trunk cabin, basalt sketch.
- Verdict: grounded

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
  1. score=50.551506 chunk_id=22724 preview=Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=26.577451 chunk_id=22725 preview=Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
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
  1. score=50.710381 chunk_id=22724 preview=Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? Case scope id: distractor...
  2. score=26.737473 chunk_id=22725 preview=Question anchor: Which object belongs to Daria's archive scene at North Orchard lane, not the similar object from Winter Choir Eve? document distractor-north...
  3. score=23.671610 chunk_id=22394 preview=document distractor-north-orchard-lane-098::distractor-098: In document distractor-north-orchard-lane-098, the verified archive note records green apron, Dar...
- Matched markers: Daria of North Orchard lane, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Daria of North Orchard lane, green apron.
- Verdict: grounded

- Winner:
  - `bge_m3`
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
  1. score=50.456159 chunk_id=22726 preview=Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  2. score=26.435668 chunk_id=22727 preview=Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? document distractor-south...
  3. score=23.410886 chunk_id=22407 preview=document distractor-south-meadow-arch-099::distractor-099: In document distractor-south-meadow-arch-099, the verified archive note records Signal Lantern Mor...
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
  1. score=50.277456 chunk_id=22726 preview=Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? Case scope id: distractor...
  2. score=26.307541 chunk_id=22727 preview=Question anchor: Which memory event is the correct one for Oren at South Meadow arch, and which similar event is only a distractor? document distractor-south...
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
  1. score=50.469711 chunk_id=22728 preview=Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Case scope id: distractor-100. Scoped answer s...
  2. score=26.548845 chunk_id=22729 preview=Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? document distractor-birch-ferry-shed-100::dist...
  3. score=23.442575 chunk_id=22343 preview=document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry s...
- Matched markers: Ada of Birch Ferry shed, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Birch Ferry shed, clay watering cup.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Top chunks:
  1. score=50.349004 chunk_id=22728 preview=Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? Case scope id: distractor-100. Scoped answer s...
  2. score=26.408574 chunk_id=22729 preview=Question anchor: Which Ada kept the correct memory note at Birch Ferry shed, not the similar entry for Nikola? document distractor-birch-ferry-shed-100::dist...
  3. score=23.326028 chunk_id=22343 preview=document distractor-birch-ferry-shed-100::distractor-100: In document distractor-birch-ferry-shed-100, the verified archive note records Ada of Birch Ferry s...
- Matched markers: Ada of Birch Ferry shed, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Ada of Birch Ferry shed, clay watering cup.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Aggregate Results

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Question wins: 48
- Passed questions: 66
- Average evidence coverage: 0.8
- Average first relevant rank: 1.0
- Total matched markers: 160
- Total missing markers: 40
- Total false-positive markers: 0
- Official metrics: {'hit_rate': 0.69, 'recall_at_k': 0.63, 'mrr': 0.7483333333333333, 'forbidden_marker_rate': 0.003333333333333333, 'average_latency_ms': 24.97605, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.63, 'missing_expected_marker_count': 74, 'false_positive_count': 71}

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4`
- Question wins: 44
- Passed questions: 82
- Average evidence coverage: 0.915
- Average first relevant rank: 1.0
- Total matched markers: 183
- Total missing markers: 17
- Total false-positive markers: 0
- Official metrics: {'hit_rate': 0.78, 'recall_at_k': 0.715, 'mrr': 0.7983333333333333, 'forbidden_marker_rate': 0.01, 'average_latency_ms': 23.25891, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.715, 'missing_expected_marker_count': 57, 'false_positive_count': 59}

### Runtime Activation
- Selected config: {'best_config_id': 'bge_m3', 'best_model_code': 'bge_m3', 'best_collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4', 'selected_metrics': {'hit_rate': 0.78, 'recall_at_k': 0.715, 'mrr': 0.7983333333333333, 'forbidden_marker_rate': 0.01, 'average_latency_ms': 23.25891, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.715, 'missing_expected_marker_count': 57, 'false_positive_count': 59}}
- Activated config: {'id': 2, 'profile_id': 6, 'model_code': 'bge_m3', 'collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4', 'top_k': 5, 'score_threshold': None, 'retrieval_mode': 'hybrid', 'source_eval_job_id': 154, 'source_eval_dataset_id': 'eternal-world-distractor-v1'}
- Runtime retrieval verification: {'model_code': 'bge_m3', 'result_count': 3, 'qdrant_collection': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_distractor_v1__d1bea5c7f4', 'top_chunk_id': 22531}
