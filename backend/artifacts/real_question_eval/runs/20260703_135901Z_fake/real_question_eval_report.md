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
- Timestamp: 2026-07-03T13:59:01.255039+00:00
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
- Archived Markdown: `/app/artifacts/real_question_eval/runs/20260703_135901Z_fake/real_question_eval_report.md`
- Archived JSON: `/app/artifacts/real_question_eval/runs/20260703_135901Z_fake/real_question_eval_result.json`
- Archived Summary Markdown: `/app/artifacts/real_question_eval/runs/20260703_135901Z_fake/real_question_eval_summary.md`
- Archived Summary JSON: `/app/artifacts/real_question_eval/runs/20260703_135901Z_fake/real_question_eval_summary.json`

## Client Question Breakdown
### Question 1 - short-fact-ferry-lantern
Question: Which lantern hung above the ferry workshop bench?
- Final evaluated answer: Grounded by retrieved evidence for: amber lantern.
- Correctness verdict: grounded
- Evidence used: amber lantern
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (3 vs 4).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- amber lantern

Expected distractors:
- silver quay flag

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=amber lantern missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=amber lantern missing=none distractors=none

### Question 2 - short-fact-orchard-key
Question: What small object was tied to the orchard ledger with a ribbon?
- Final evaluated answer: Grounded by retrieved evidence for: cherry ribbon, tin key.
- Correctness verdict: grounded
- Evidence used: cherry ribbon, tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- tin key
- cherry ribbon

Expected distractors:
- plum ribbon

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cherry ribbon, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cherry ribbon, tin key missing=none distractors=none

### Question 3 - short-fact-postmaster-map
Question: Which map did the postmaster keep rolled inside the cedar tube?
- Final evaluated answer: Grounded by retrieved evidence for: brass corner clasp, folded canal map.
- Correctness verdict: grounded
- Evidence used: brass corner clasp, folded canal map
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- folded canal map
- brass corner clasp

Expected distractors:
- hill road sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=brass corner clasp, folded canal map missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=brass corner clasp, folded canal map missing=none distractors=none

### Question 4 - short-fact-clocktower-bell
Question: What held the clocktower bell rope in place after the repair?
- Final evaluated answer: Grounded by retrieved evidence for: brass hook, green bell rope.
- Correctness verdict: grounded
- Evidence used: brass hook, green bell rope
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- green bell rope
- brass hook

Expected distractors:
- iron bucket handle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=brass hook, green bell rope missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=brass hook, green bell rope missing=none distractors=none

### Question 5 - short-fact-river-mill-basket
Question: What container was left beside the river mill flour stones?
- Final evaluated answer: Grounded by retrieved evidence for: flour chalk mark, willow basket.
- Correctness verdict: grounded
- Evidence used: flour chalk mark, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- willow basket
- flour chalk mark

Expected distractors:
- pine crate

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=flour chalk mark, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=flour chalk mark, willow basket missing=none distractors=none

### Question 6 - short-fact-market-tokens
Question: Which market tokens were counted together in the rain ledger?
- Final evaluated answer: Grounded by retrieved evidence for: copper rain token, east gate token.
- Correctness verdict: grounded
- Evidence used: copper rain token, east gate token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- copper rain token
- east gate token

Expected distractors:
- harvest ribbon token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=copper rain token, east gate token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper rain token, east gate token missing=none distractors=none

### Question 7 - short-fact-garden-journal
Question: What cutting was stored inside the gardener's folded journal leaf?
- Final evaluated answer: Grounded by retrieved evidence for: clay watering cup, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: clay watering cup, moonflower cutting
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- clay watering cup

Expected distractors:
- mint bundle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=clay watering cup, moonflower cutting missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=clay watering cup, moonflower cutting missing=none distractors=none

### Question 8 - short-fact-snow-shed
Question: Which tool was noted in the snow shed after the thaw?
- Final evaluated answer: Grounded by retrieved evidence for: cedar shovel, rope handle.
- Correctness verdict: grounded
- Evidence used: cedar shovel, rope handle
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- cedar shovel
- rope handle

Expected distractors:
- iron rake

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar shovel, rope handle missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar shovel, rope handle missing=none distractors=none

### Question 9 - short-fact-009
Question: What exact keepsake was listed beside Snow Orchard storehouse in Petar's river diary page?
- Final evaluated answer: Grounded by retrieved evidence for: Snow Orchard storehouse, river diary page, star ledger page.
- Correctness verdict: grounded
- Evidence used: Snow Orchard storehouse, river diary page, star ledger page
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- star ledger page
- Snow Orchard storehouse
- river diary page

Expected distractors:
- wrong blue glass jar

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Snow Orchard storehouse, river diary page, star ledger page missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Snow Orchard storehouse, river diary page, star ledger page missing=none distractors=none

### Question 10 - short-fact-010
Question: Which small object in the cedar tube proved that Lina stopped at Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: Bell Bridge square, lantern hook.
- Correctness verdict: grounded
- Evidence used: Bell Bridge square, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- lantern hook
- Bell Bridge square

Expected distractors:
- wrong canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Bell Bridge square, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Bell Bridge square, lantern hook missing=none distractors=none

### Question 11 - short-fact-011
Question: Which direct fact from the winter letter identifies the item recorded for Boris at Glass Harbor quay?
- Final evaluated answer: Grounded by retrieved evidence for: weathered camera strap.
- Correctness verdict: grounded
- Evidence used: weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- weathered camera strap

Expected distractors:
- wrong cedar shovel

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=weathered camera strap missing=none distractors=none

### Question 12 - short-fact-012
Question: Which item did Anya tuck inside the cedar tube mentioned in the station transcript?
- Final evaluated answer: Grounded by retrieved evidence for: cedar tube, wax thread.
- Correctness verdict: grounded
- Evidence used: cedar tube, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- wax thread
- cedar tube

Expected distractors:
- wrong copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar tube, wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar tube, wax thread missing=none distractors=none

### Question 13 - short-fact-013
Question: What object and color detail identified Marek's keepsake at Hollow Market arcade?
- Final evaluated answer: Grounded by retrieved evidence for: saffron tin key.
- Correctness verdict: grounded
- Evidence used: saffron tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron tin key

Expected distractors:
- wrong moonflower cutting

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=saffron tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron tin key missing=none distractors=none

### Question 14 - short-fact-014
Question: Which fact in the audio reel shows what Daria's twin sister left near Winter Chapel porch?
- Final evaluated answer: Grounded by retrieved evidence for: blue oar, twin sister.
- Correctness verdict: grounded
- Evidence used: blue oar, twin sister
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- twin sister

Expected distractors:
- wrong birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue oar, twin sister missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue oar, twin sister missing=none distractors=none

### Question 15 - short-fact-015
Question: What exact keepsake was listed beside Driftwood cove in Stefan's profile page?
- Final evaluated answer: Grounded by retrieved evidence for: Driftwood cove, profile page, willow basket.
- Correctness verdict: grounded
- Evidence used: Driftwood cove, profile page, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- willow basket
- Driftwood cove
- profile page

Expected distractors:
- wrong saffron scarf

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Driftwood cove, profile page, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Driftwood cove, profile page, willow basket missing=none distractors=none

### Question 16 - short-fact-016
Question: Which small object in the cedar tube proved that Yara stopped at Cloud Wharf office?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, paper moon mask.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, paper moon mask
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing paper moon mask
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- Cloud Wharf office

Expected distractors:
- wrong carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=Cloud Wharf office missing=paper moon mask distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, paper moon mask missing=none distractors=none

### Question 17 - short-fact-017
Question: Which direct fact from the festival minutes identifies the item recorded for Oren at Moss Archive room?
- Final evaluated answer: Grounded by retrieved evidence for: glass ink bottle.
- Correctness verdict: grounded
- Evidence used: glass ink bottle
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- glass ink bottle

Expected distractors:
- wrong amber lantern

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=glass ink bottle missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=glass ink bottle missing=none distractors=none

### Question 18 - short-fact-018
Question: Which item did Milena tuck inside the cedar tube mentioned in the winter letter?
- Final evaluated answer: Grounded by retrieved evidence for: cedar tube, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: cedar tube, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- copper wind vane pin
- cedar tube

Expected distractors:
- wrong basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar tube, copper wind vane pin missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar tube, copper wind vane pin missing=none distractors=none

### Question 19 - short-fact-019
Question: What object and color detail identified Lev's keepsake at Snow Orchard storehouse?
- Final evaluated answer: Grounded by retrieved evidence for: saffron coal stove hiss.
- Correctness verdict: grounded
- Evidence used: saffron coal stove hiss
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing saffron coal stove hiss
- Distractors / false positives: none

Expected evidence:
- saffron coal stove hiss

Expected distractors:
- wrong green apron

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=saffron coal stove hiss distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron coal stove hiss missing=none distractors=none

### Question 20 - short-fact-020
Question: Which fact in the field recording shows what Ada's stepfather left near Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: stepfather, violet ribbon.
- Correctness verdict: grounded
- Evidence used: stepfather, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- violet ribbon
- stepfather

Expected distractors:
- wrong silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=stepfather, violet ribbon missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=stepfather, violet ribbon missing=none distractors=none

### Question 21 - short-fact-021
Question: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel?
- Final evaluated answer: Grounded by retrieved evidence for: Glass Harbor quay, audio reel, tuning fork.
- Correctness verdict: grounded
- Evidence used: Glass Harbor quay, audio reel, tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- tuning fork
- Glass Harbor quay
- audio reel

Expected distractors:
- wrong clay watering cup

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Glass Harbor quay, audio reel, tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Glass Harbor quay, audio reel, tuning fork missing=none distractors=none

### Question 22 - short-fact-022
Question: Which small object in the cedar tube proved that Raisa stopped at South Meadow arch?
- Final evaluated answer: Grounded by retrieved evidence for: South Meadow arch, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: South Meadow arch, rope bridge permit
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing rope bridge permit
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- South Meadow arch

Expected distractors:
- wrong juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=South Meadow arch missing=rope bridge permit distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=South Meadow arch, rope bridge permit missing=none distractors=none

### Question 23 - short-fact-023
Question: Which direct fact from the river diary page identifies the item recorded for Galen at Hollow Market arcade?
- Final evaluated answer: Grounded by retrieved evidence for: oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- oak barrel hoops

Expected distractors:
- wrong smoke vent chain

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=oak barrel hoops missing=none distractors=none

### Question 24 - short-fact-024
Question: Which item did Sonya tuck inside the cedar tube mentioned in the festival minutes?
- Final evaluated answer: Grounded by retrieved evidence for: blue glass jar, cedar tube.
- Correctness verdict: grounded
- Evidence used: blue glass jar, cedar tube
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- cedar tube

Expected distractors:
- wrong brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue glass jar, cedar tube missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue glass jar, cedar tube missing=none distractors=none

### Question 25 - short-fact-025
Question: What object and color detail identified Pavel's keepsake at Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: saffron canal route map.
- Correctness verdict: grounded
- Evidence used: saffron canal route map
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing saffron canal route map
- Distractors / false positives: none

Expected evidence:
- saffron canal route map

Expected distractors:
- wrong linen wick

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=saffron canal route map distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron canal route map missing=none distractors=none

### Question 26 - short-fact-026
Question: Which fact in the station transcript shows what Talia's cousin left near Cloud Wharf office?
- Final evaluated answer: Grounded by retrieved evidence for: cedar shovel, cousin.
- Correctness verdict: grounded
- Evidence used: cedar shovel, cousin
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- cedar shovel
- cousin

Expected distractors:
- wrong star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar shovel, cousin missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar shovel, cousin missing=none distractors=none

### Question 27 - short-fact-027
Question: What exact keepsake was listed beside Moss Archive room in Emil's field recording?
- Final evaluated answer: Grounded by retrieved evidence for: Moss Archive room, copper token, field recording.
- Correctness verdict: grounded
- Evidence used: Moss Archive room, copper token, field recording
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- copper token
- Moss Archive room
- field recording

Expected distractors:
- wrong lantern hook

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Moss Archive room, copper token, field recording missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Moss Archive room, copper token, field recording missing=none distractors=none

### Question 28 - short-fact-028
Question: Which small object in the cedar tube proved that Runa stopped at North Bell workshop?
- Final evaluated answer: Grounded by retrieved evidence for: North Bell workshop, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: North Bell workshop, moonflower cutting
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- North Bell workshop

Expected distractors:
- wrong weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=North Bell workshop, moonflower cutting missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=North Bell workshop, moonflower cutting missing=none distractors=none

### Question 29 - short-fact-029
Question: Which direct fact from the profile page identifies the item recorded for Viktor at Snow Orchard storehouse?
- Final evaluated answer: Grounded by retrieved evidence for: birch tea flask.
- Correctness verdict: grounded
- Evidence used: birch tea flask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- birch tea flask

Expected distractors:
- wrong wax thread

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=birch tea flask missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=birch tea flask missing=none distractors=none

### Question 30 - short-fact-030
Question: Which item did Selma tuck inside the cedar tube mentioned in the river diary page?
- Final evaluated answer: Grounded by retrieved evidence for: cedar tube, saffron scarf.
- Correctness verdict: grounded
- Evidence used: cedar tube, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron scarf
- cedar tube

Expected distractors:
- wrong tin key

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar tube, saffron scarf missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar tube, saffron scarf missing=none distractors=none

### Question 31 - short-fact-031
Question: What object and color detail identified Damir's keepsake at Glass Harbor quay?
- Final evaluated answer: Grounded by retrieved evidence for: saffron carved shell comb.
- Correctness verdict: grounded
- Evidence used: saffron carved shell comb
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron carved shell comb

Expected distractors:
- wrong blue oar

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=saffron carved shell comb missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron carved shell comb missing=none distractors=none

### Question 32 - short-fact-032
Question: Which fact in the winter letter shows what Iveta's older sister left near South Meadow arch?
- Final evaluated answer: Grounded by retrieved evidence for: amber lantern, older sister.
- Correctness verdict: grounded
- Evidence used: amber lantern, older sister
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- amber lantern
- older sister

Expected distractors:
- wrong willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=amber lantern, older sister missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=amber lantern, older sister missing=none distractors=none

### Question 33 - short-fact-033
Question: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript?
- Final evaluated answer: Grounded by retrieved evidence for: Hollow Market arcade, basalt sketch, station transcript.
- Correctness verdict: grounded
- Evidence used: Hollow Market arcade, basalt sketch, station transcript
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- basalt sketch
- Hollow Market arcade
- station transcript

Expected distractors:
- wrong paper moon mask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Hollow Market arcade, basalt sketch, station transcript missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Hollow Market arcade, basalt sketch, station transcript missing=none distractors=none

### Question 34 - short-fact-034
Question: Which small object in the cedar tube proved that Nessa stopped at Winter Chapel porch?
- Final evaluated answer: Grounded by retrieved evidence for: Winter Chapel porch, green apron.
- Correctness verdict: grounded
- Evidence used: Winter Chapel porch, green apron
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- green apron
- Winter Chapel porch

Expected distractors:
- wrong glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Winter Chapel porch, green apron missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Winter Chapel porch, green apron missing=none distractors=none

### Question 35 - short-fact-035
Question: Which direct fact from the audio reel identifies the item recorded for Anton at Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: silver booth token.
- Correctness verdict: grounded
- Evidence used: silver booth token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `multilingual_e5_small`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: bge_m3 missing silver booth token
- Distractors / false positives: none

Expected evidence:
- silver booth token

Expected distractors:
- wrong copper wind vane pin

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=silver booth token missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=silver booth token distractors=none

### Question 36 - short-fact-036
Question: Which item did Zora tuck inside the cedar tube mentioned in the profile page?
- Final evaluated answer: Grounded by retrieved evidence for: cedar tube, clay watering cup.
- Correctness verdict: grounded
- Evidence used: cedar tube, clay watering cup
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing clay watering cup
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- cedar tube

Expected distractors:
- wrong coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=cedar tube missing=clay watering cup distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar tube, clay watering cup missing=none distractors=none

### Question 37 - short-fact-037
Question: What object and color detail identified Milan's keepsake at Moss Archive room?
- Final evaluated answer: Grounded by retrieved evidence for: saffron juniper bundles.
- Correctness verdict: grounded
- Evidence used: saffron juniper bundles
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing saffron juniper bundles
- Distractors / false positives: none

Expected evidence:
- saffron juniper bundles

Expected distractors:
- wrong violet ribbon

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=saffron juniper bundles distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron juniper bundles missing=none distractors=none

### Question 38 - short-fact-038
Question: Which fact in the festival minutes shows what Ilia's twin sister left near North Bell workshop?
- Final evaluated answer: Grounded by retrieved evidence for: smoke vent chain, twin sister.
- Correctness verdict: grounded
- Evidence used: smoke vent chain, twin sister
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- smoke vent chain
- twin sister

Expected distractors:
- wrong tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=smoke vent chain, twin sister missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=smoke vent chain, twin sister missing=none distractors=none

### Question 39 - short-fact-039
Question: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter?
- Final evaluated answer: Grounded by retrieved evidence for: Snow Orchard storehouse, brass compass, winter letter.
- Correctness verdict: grounded
- Evidence used: Snow Orchard storehouse, brass compass, winter letter
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- brass compass
- Snow Orchard storehouse
- winter letter

Expected distractors:
- wrong rope bridge permit

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Snow Orchard storehouse, brass compass, winter letter missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Snow Orchard storehouse, brass compass, winter letter missing=none distractors=none

### Question 40 - short-fact-040
Question: Which small object in the cedar tube proved that Mira stopped at Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: Bell Bridge square, linen wick.
- Correctness verdict: grounded
- Evidence used: Bell Bridge square, linen wick
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- Bell Bridge square

Expected distractors:
- wrong oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Bell Bridge square, linen wick missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Bell Bridge square, linen wick missing=none distractors=none

### Question 41 - short-fact-041
Question: Which direct fact from the field recording identifies the item recorded for Tomas at Glass Harbor quay?
- Final evaluated answer: Grounded by retrieved evidence for: star ledger page.
- Correctness verdict: grounded
- Evidence used: star ledger page
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `multilingual_e5_small`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: bge_m3 missing star ledger page
- Distractors / false positives: none

Expected evidence:
- star ledger page

Expected distractors:
- wrong blue glass jar

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=star ledger page missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=star ledger page distractors=none

### Question 42 - short-fact-042
Question: Which item did Elena tuck inside the cedar tube mentioned in the audio reel?
- Final evaluated answer: Grounded by retrieved evidence for: cedar tube, lantern hook.
- Correctness verdict: grounded
- Evidence used: cedar tube, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- lantern hook
- cedar tube

Expected distractors:
- wrong canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar tube, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar tube, lantern hook missing=none distractors=none

### Question 43 - short-fact-043
Question: What object and color detail identified Radin's keepsake at Hollow Market arcade?
- Final evaluated answer: Grounded by retrieved evidence for: saffron weathered camera strap.
- Correctness verdict: grounded
- Evidence used: saffron weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron weathered camera strap

Expected distractors:
- wrong cedar shovel

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=saffron weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron weathered camera strap missing=none distractors=none

### Question 44 - short-fact-044
Question: Which fact in the river diary page shows what Vera's stepfather left near Winter Chapel porch?
- Final evaluated answer: Grounded by retrieved evidence for: stepfather, wax thread.
- Correctness verdict: grounded
- Evidence used: stepfather, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- wax thread
- stepfather

Expected distractors:
- wrong copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=stepfather, wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=stepfather, wax thread missing=none distractors=none

### Question 45 - short-fact-045
Question: What exact keepsake was listed beside Driftwood cove in Ilya's festival minutes?
- Final evaluated answer: Grounded by retrieved evidence for: Driftwood cove, festival minutes, tin key.
- Correctness verdict: grounded
- Evidence used: Driftwood cove, festival minutes, tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- tin key
- Driftwood cove
- festival minutes

Expected distractors:
- wrong moonflower cutting

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Driftwood cove, festival minutes, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Driftwood cove, festival minutes, tin key missing=none distractors=none

### Question 46 - short-fact-046
Question: Which small object in the cedar tube proved that Kira stopped at Cloud Wharf office?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, blue oar.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, blue oar
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- Cloud Wharf office

Expected distractors:
- wrong birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, blue oar missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, blue oar missing=none distractors=none

### Question 47 - short-fact-047
Question: Which direct fact from the station transcript identifies the item recorded for Soren at Moss Archive room?
- Final evaluated answer: Grounded by retrieved evidence for: willow basket.
- Correctness verdict: grounded
- Evidence used: willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (3 vs 4).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- willow basket

Expected distractors:
- wrong saffron scarf

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=willow basket missing=none distractors=none

### Question 48 - short-fact-048
Question: Which item did Nadia tuck inside the cedar tube mentioned in the field recording?
- Final evaluated answer: Grounded by retrieved evidence for: cedar tube, paper moon mask.
- Correctness verdict: grounded
- Evidence used: cedar tube, paper moon mask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_small`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: bge_m3 missing paper moon mask
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- cedar tube

Expected distractors:
- wrong carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar tube, paper moon mask missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=0.5 matched=cedar tube missing=paper moon mask distractors=none

### Question 49 - short-fact-049
Question: What object and color detail identified Petar's keepsake at Snow Orchard storehouse?
- Final evaluated answer: Grounded by retrieved evidence for: saffron glass ink bottle.
- Correctness verdict: grounded
- Evidence used: saffron glass ink bottle
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron glass ink bottle

Expected distractors:
- wrong amber lantern

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=saffron glass ink bottle missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron glass ink bottle missing=none distractors=none

### Question 50 - short-fact-050
Question: Which fact in the profile page shows what Lina's cousin left near Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: copper wind vane pin, cousin.
- Correctness verdict: grounded
- Evidence used: copper wind vane pin, cousin
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- copper wind vane pin
- cousin

Expected distractors:
- wrong basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=copper wind vane pin, cousin missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper wind vane pin, cousin missing=none distractors=none

### Question 51 - short-fact-051
Question: What exact keepsake was listed beside Glass Harbor quay in Boris's river diary page?
- Final evaluated answer: Grounded by retrieved evidence for: Glass Harbor quay, coal stove hiss, river diary page.
- Correctness verdict: grounded
- Evidence used: Glass Harbor quay, coal stove hiss, river diary page
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- coal stove hiss
- Glass Harbor quay
- river diary page

Expected distractors:
- wrong green apron

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Glass Harbor quay, coal stove hiss, river diary page missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Glass Harbor quay, coal stove hiss, river diary page missing=none distractors=none

### Question 52 - short-fact-052
Question: Which small object in the cedar tube proved that Anya stopped at South Meadow arch?
- Final evaluated answer: Grounded by retrieved evidence for: South Meadow arch, violet ribbon.
- Correctness verdict: grounded
- Evidence used: South Meadow arch, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- violet ribbon
- South Meadow arch

Expected distractors:
- wrong silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=South Meadow arch, violet ribbon missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=South Meadow arch, violet ribbon missing=none distractors=none

### Question 53 - short-fact-053
Question: Which direct fact from the winter letter identifies the item recorded for Marek at Hollow Market arcade?
- Final evaluated answer: Grounded by retrieved evidence for: tuning fork.
- Correctness verdict: grounded
- Evidence used: tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- tuning fork

Expected distractors:
- wrong clay watering cup

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=tuning fork missing=none distractors=none

### Question 54 - short-fact-054
Question: Which item did Daria tuck inside the cedar tube mentioned in the station transcript?
- Final evaluated answer: Grounded by retrieved evidence for: cedar tube, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: cedar tube, rope bridge permit
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing rope bridge permit
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- cedar tube

Expected distractors:
- wrong juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=cedar tube missing=rope bridge permit distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar tube, rope bridge permit missing=none distractors=none

### Question 55 - short-fact-055
Question: What object and color detail identified Stefan's keepsake at Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: saffron oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: saffron oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron oak barrel hoops

Expected distractors:
- wrong smoke vent chain

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=saffron oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron oak barrel hoops missing=none distractors=none

### Question 56 - short-fact-056
Question: Which fact in the audio reel shows what Yara's older sister left near Cloud Wharf office?
- Final evaluated answer: Grounded by retrieved evidence for: blue glass jar, older sister.
- Correctness verdict: grounded
- Evidence used: blue glass jar, older sister
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- older sister

Expected distractors:
- wrong brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue glass jar, older sister missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue glass jar, older sister missing=none distractors=none

### Question 57 - short-fact-057
Question: What exact keepsake was listed beside Moss Archive room in Oren's profile page?
- Final evaluated answer: Grounded by retrieved evidence for: Moss Archive room, canal route map, profile page.
- Correctness verdict: grounded
- Evidence used: Moss Archive room, canal route map, profile page
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- canal route map
- Moss Archive room
- profile page

Expected distractors:
- wrong linen wick

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Moss Archive room, canal route map, profile page missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Moss Archive room, canal route map, profile page missing=none distractors=none

### Question 58 - short-fact-058
Question: Which small object in the cedar tube proved that Milena stopped at North Bell workshop?
- Final evaluated answer: Grounded by retrieved evidence for: North Bell workshop, cedar shovel.
- Correctness verdict: grounded
- Evidence used: North Bell workshop, cedar shovel
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- cedar shovel
- North Bell workshop

Expected distractors:
- wrong star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=North Bell workshop, cedar shovel missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=North Bell workshop, cedar shovel missing=none distractors=none

### Question 59 - short-fact-059
Question: Which direct fact from the festival minutes identifies the item recorded for Lev at Snow Orchard storehouse?
- Final evaluated answer: Grounded by retrieved evidence for: copper token.
- Correctness verdict: grounded
- Evidence used: copper token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- copper token

Expected distractors:
- wrong lantern hook

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=copper token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper token missing=none distractors=none

### Question 60 - short-fact-060
Question: Which item did Ada tuck inside the cedar tube mentioned in the winter letter?
- Final evaluated answer: Grounded by retrieved evidence for: cedar tube, moonflower cutting.
- Correctness verdict: grounded
- Evidence used: cedar tube, moonflower cutting
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- cedar tube

Expected distractors:
- wrong weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar tube, moonflower cutting missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar tube, moonflower cutting missing=none distractors=none

### Question 61 - short-fact-061
Question: What object and color detail identified Nikola's keepsake at Glass Harbor quay?
- Final evaluated answer: Grounded by retrieved evidence for: saffron birch tea flask.
- Correctness verdict: grounded
- Evidence used: saffron birch tea flask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `multilingual_e5_small`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: bge_m3 missing saffron birch tea flask
- Distractors / false positives: none

Expected evidence:
- saffron birch tea flask

Expected distractors:
- wrong wax thread

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=saffron birch tea flask missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=saffron birch tea flask distractors=none

### Question 62 - short-fact-062
Question: Which fact in the field recording shows what Raisa's twin sister left near South Meadow arch?
- Final evaluated answer: Grounded by retrieved evidence for: saffron scarf, twin sister.
- Correctness verdict: grounded
- Evidence used: saffron scarf, twin sister
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron scarf
- twin sister

Expected distractors:
- wrong tin key

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=saffron scarf, twin sister missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron scarf, twin sister missing=none distractors=none

### Question 63 - short-fact-063
Question: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel?
- Final evaluated answer: Grounded by retrieved evidence for: Hollow Market arcade, audio reel, carved shell comb.
- Correctness verdict: grounded
- Evidence used: Hollow Market arcade, audio reel, carved shell comb
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- carved shell comb
- Hollow Market arcade
- audio reel

Expected distractors:
- wrong blue oar

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Hollow Market arcade, audio reel, carved shell comb missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Hollow Market arcade, audio reel, carved shell comb missing=none distractors=none

### Question 64 - short-fact-064
Question: Which small object in the cedar tube proved that Sonya stopped at Winter Chapel porch?
- Final evaluated answer: Grounded by retrieved evidence for: Winter Chapel porch, amber lantern.
- Correctness verdict: grounded
- Evidence used: Winter Chapel porch, amber lantern
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- amber lantern
- Winter Chapel porch

Expected distractors:
- wrong willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Winter Chapel porch, amber lantern missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Winter Chapel porch, amber lantern missing=none distractors=none

### Question 65 - short-fact-065
Question: Which direct fact from the river diary page identifies the item recorded for Pavel at Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: basalt sketch.
- Correctness verdict: grounded
- Evidence used: basalt sketch
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (3 vs 4).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- basalt sketch

Expected distractors:
- wrong paper moon mask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=basalt sketch missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=basalt sketch missing=none distractors=none

### Question 66 - short-fact-066
Question: Which item did Talia tuck inside the cedar tube mentioned in the festival minutes?
- Final evaluated answer: Grounded by retrieved evidence for: cedar tube, green apron.
- Correctness verdict: grounded
- Evidence used: cedar tube, green apron
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- green apron
- cedar tube

Expected distractors:
- wrong glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar tube, green apron missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar tube, green apron missing=none distractors=none

### Question 67 - short-fact-067
Question: What object and color detail identified Emil's keepsake at Moss Archive room?
- Final evaluated answer: Grounded by retrieved evidence for: saffron silver booth token.
- Correctness verdict: grounded
- Evidence used: saffron silver booth token
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing saffron silver booth token
- Distractors / false positives: none

Expected evidence:
- saffron silver booth token

Expected distractors:
- wrong copper wind vane pin

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=saffron silver booth token distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron silver booth token missing=none distractors=none

### Question 68 - short-fact-068
Question: Which fact in the station transcript shows what Runa's stepfather left near North Bell workshop?
- Final evaluated answer: Grounded by retrieved evidence for: clay watering cup, stepfather.
- Correctness verdict: grounded
- Evidence used: clay watering cup, stepfather
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- stepfather

Expected distractors:
- wrong coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=clay watering cup, stepfather missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=clay watering cup, stepfather missing=none distractors=none

### Question 69 - short-fact-069
Question: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording?
- Final evaluated answer: Grounded by retrieved evidence for: Snow Orchard storehouse, field recording, juniper bundles.
- Correctness verdict: grounded
- Evidence used: Snow Orchard storehouse, field recording, juniper bundles
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- juniper bundles
- Snow Orchard storehouse
- field recording

Expected distractors:
- wrong violet ribbon

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Snow Orchard storehouse, field recording, juniper bundles missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Snow Orchard storehouse, field recording, juniper bundles missing=none distractors=none

### Question 70 - short-fact-070
Question: Which small object in the cedar tube proved that Selma stopped at Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: Bell Bridge square, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: Bell Bridge square, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing smoke vent chain
- Distractors / false positives: none

Expected evidence:
- smoke vent chain
- Bell Bridge square

Expected distractors:
- wrong tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=Bell Bridge square missing=smoke vent chain distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Bell Bridge square, smoke vent chain missing=none distractors=none

### Question 71 - short-fact-071
Question: Which direct fact from the profile page identifies the item recorded for Damir at Glass Harbor quay?
- Final evaluated answer: Grounded by retrieved evidence for: brass compass.
- Correctness verdict: grounded
- Evidence used: brass compass
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- brass compass

Expected distractors:
- wrong rope bridge permit

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=brass compass missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=brass compass missing=none distractors=none

### Question 72 - short-fact-072
Question: Which item did Iveta tuck inside the cedar tube mentioned in the river diary page?
- Final evaluated answer: Grounded by retrieved evidence for: cedar tube, linen wick.
- Correctness verdict: grounded
- Evidence used: cedar tube, linen wick
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- cedar tube

Expected distractors:
- wrong oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar tube, linen wick missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar tube, linen wick missing=none distractors=none

### Question 73 - short-fact-073
Question: What object and color detail identified Rafi's keepsake at Hollow Market arcade?
- Final evaluated answer: Grounded by retrieved evidence for: saffron star ledger page.
- Correctness verdict: grounded
- Evidence used: saffron star ledger page
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing saffron star ledger page
- Distractors / false positives: none

Expected evidence:
- saffron star ledger page

Expected distractors:
- wrong blue glass jar

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=saffron star ledger page distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron star ledger page missing=none distractors=none

### Question 74 - short-fact-074
Question: Which fact in the winter letter shows what Nessa's cousin left near Winter Chapel porch?
- Final evaluated answer: Grounded by retrieved evidence for: cousin, lantern hook.
- Correctness verdict: grounded
- Evidence used: cousin, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- lantern hook
- cousin

Expected distractors:
- wrong canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cousin, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cousin, lantern hook missing=none distractors=none

### Question 75 - short-fact-075
Question: What exact keepsake was listed beside Driftwood cove in Anton's station transcript?
- Final evaluated answer: Grounded by retrieved evidence for: Driftwood cove, station transcript, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: Driftwood cove, station transcript, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- weathered camera strap
- Driftwood cove
- station transcript

Expected distractors:
- wrong cedar shovel

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Driftwood cove, station transcript, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Driftwood cove, station transcript, weathered camera strap missing=none distractors=none

### Question 76 - short-fact-076
Question: Which small object in the cedar tube proved that Zora stopped at Cloud Wharf office?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, wax thread.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, wax thread
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing wax thread
- Distractors / false positives: none

Expected evidence:
- wax thread
- Cloud Wharf office

Expected distractors:
- wrong copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=Cloud Wharf office missing=wax thread distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, wax thread missing=none distractors=none

### Question 77 - short-fact-077
Question: Which direct fact from the audio reel identifies the item recorded for Milan at Moss Archive room?
- Final evaluated answer: Grounded by retrieved evidence for: tin key.
- Correctness verdict: grounded
- Evidence used: tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `multilingual_e5_small`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: bge_m3 missing tin key
- Distractors / false positives: none

Expected evidence:
- tin key

Expected distractors:
- wrong moonflower cutting

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=tin key missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=tin key distractors=none

### Question 78 - short-fact-078
Question: Which item did Ilia tuck inside the cedar tube mentioned in the profile page?
- Final evaluated answer: Grounded by retrieved evidence for: blue oar, cedar tube.
- Correctness verdict: grounded
- Evidence used: blue oar, cedar tube
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- cedar tube

Expected distractors:
- wrong birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue oar, cedar tube missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue oar, cedar tube missing=none distractors=none

### Question 79 - short-fact-079
Question: What object and color detail identified Vesna's keepsake at Snow Orchard storehouse?
- Final evaluated answer: Grounded by retrieved evidence for: saffron willow basket.
- Correctness verdict: grounded
- Evidence used: saffron willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron willow basket

Expected distractors:
- wrong saffron scarf

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=saffron willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron willow basket missing=none distractors=none

### Question 80 - short-fact-080
Question: Which fact in the festival minutes shows what Mira's older sister left near Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: older sister, paper moon mask.
- Correctness verdict: grounded
- Evidence used: older sister, paper moon mask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- older sister

Expected distractors:
- wrong carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=older sister, paper moon mask missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=older sister, paper moon mask missing=none distractors=none

### Question 81 - short-fact-081
Question: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter?
- Final evaluated answer: Grounded by retrieved evidence for: Glass Harbor quay, glass ink bottle, winter letter.
- Correctness verdict: grounded
- Evidence used: Glass Harbor quay, glass ink bottle, winter letter
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- glass ink bottle
- Glass Harbor quay
- winter letter

Expected distractors:
- wrong amber lantern

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Glass Harbor quay, glass ink bottle, winter letter missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Glass Harbor quay, glass ink bottle, winter letter missing=none distractors=none

### Question 82 - short-fact-082
Question: Which small object in the cedar tube proved that Elena stopped at South Meadow arch?
- Final evaluated answer: Grounded by retrieved evidence for: South Meadow arch, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: South Meadow arch, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing copper wind vane pin
- Distractors / false positives: none

Expected evidence:
- copper wind vane pin
- South Meadow arch

Expected distractors:
- wrong basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=South Meadow arch missing=copper wind vane pin distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=South Meadow arch, copper wind vane pin missing=none distractors=none

### Question 83 - short-fact-083
Question: Which direct fact from the field recording identifies the item recorded for Radin at Hollow Market arcade?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss.
- Correctness verdict: grounded
- Evidence used: coal stove hiss
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- coal stove hiss

Expected distractors:
- wrong green apron

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss missing=none distractors=none

### Question 84 - short-fact-084
Question: Which item did Vera tuck inside the cedar tube mentioned in the audio reel?
- Final evaluated answer: Grounded by retrieved evidence for: cedar tube, violet ribbon.
- Correctness verdict: grounded
- Evidence used: cedar tube, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- violet ribbon
- cedar tube

Expected distractors:
- wrong silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar tube, violet ribbon missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar tube, violet ribbon missing=none distractors=none

### Question 85 - short-fact-085
Question: What object and color detail identified Ilya's keepsake at Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: saffron tuning fork.
- Correctness verdict: grounded
- Evidence used: saffron tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron tuning fork

Expected distractors:
- wrong clay watering cup

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=saffron tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron tuning fork missing=none distractors=none

### Question 86 - short-fact-086
Question: Which fact in the river diary page shows what Kira's twin sister left near Cloud Wharf office?
- Final evaluated answer: Grounded by retrieved evidence for: rope bridge permit, twin sister.
- Correctness verdict: grounded
- Evidence used: rope bridge permit, twin sister
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- twin sister

Expected distractors:
- wrong juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=rope bridge permit, twin sister missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=rope bridge permit, twin sister missing=none distractors=none

### Question 87 - short-fact-087
Question: What exact keepsake was listed beside Moss Archive room in Soren's festival minutes?
- Final evaluated answer: Grounded by retrieved evidence for: Moss Archive room, festival minutes, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Moss Archive room, festival minutes, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- oak barrel hoops
- Moss Archive room
- festival minutes

Expected distractors:
- wrong smoke vent chain

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Moss Archive room, festival minutes, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Moss Archive room, festival minutes, oak barrel hoops missing=none distractors=none

### Question 88 - short-fact-088
Question: Which small object in the cedar tube proved that Nadia stopped at North Bell workshop?
- Final evaluated answer: Grounded by retrieved evidence for: North Bell workshop, blue glass jar.
- Correctness verdict: grounded
- Evidence used: North Bell workshop, blue glass jar
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- North Bell workshop

Expected distractors:
- wrong brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=North Bell workshop, blue glass jar missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=North Bell workshop, blue glass jar missing=none distractors=none

### Question 89 - short-fact-089
Question: Which direct fact from the station transcript identifies the item recorded for Petar at Snow Orchard storehouse?
- Final evaluated answer: Grounded by retrieved evidence for: canal route map.
- Correctness verdict: grounded
- Evidence used: canal route map
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- canal route map

Expected distractors:
- wrong linen wick

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=canal route map missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=canal route map missing=none distractors=none

### Question 90 - short-fact-090
Question: Which item did Lina tuck inside the cedar tube mentioned in the field recording?
- Final evaluated answer: Grounded by retrieved evidence for: cedar shovel, cedar tube.
- Correctness verdict: grounded
- Evidence used: cedar shovel, cedar tube
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- cedar shovel
- cedar tube

Expected distractors:
- wrong star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar shovel, cedar tube missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar shovel, cedar tube missing=none distractors=none

### Question 91 - short-fact-091
Question: What object and color detail identified Boris's keepsake at Glass Harbor quay?
- Final evaluated answer: Grounded by retrieved evidence for: saffron copper token.
- Correctness verdict: grounded
- Evidence used: saffron copper token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `multilingual_e5_small`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: bge_m3 missing saffron copper token
- Distractors / false positives: none

Expected evidence:
- saffron copper token

Expected distractors:
- wrong lantern hook

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=saffron copper token missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=saffron copper token distractors=none

### Question 92 - short-fact-092
Question: Which fact in the profile page shows what Anya's stepfather left near South Meadow arch?
- Final evaluated answer: Grounded by retrieved evidence for: moonflower cutting, stepfather.
- Correctness verdict: grounded
- Evidence used: moonflower cutting, stepfather
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- stepfather

Expected distractors:
- wrong weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=moonflower cutting, stepfather missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=moonflower cutting, stepfather missing=none distractors=none

### Question 93 - short-fact-093
Question: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page?
- Final evaluated answer: Grounded by retrieved evidence for: Hollow Market arcade, birch tea flask, river diary page.
- Correctness verdict: grounded
- Evidence used: Hollow Market arcade, birch tea flask, river diary page
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- birch tea flask
- Hollow Market arcade
- river diary page

Expected distractors:
- wrong wax thread

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Hollow Market arcade, birch tea flask, river diary page missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Hollow Market arcade, birch tea flask, river diary page missing=none distractors=none

### Question 94 - short-fact-094
Question: Which small object in the cedar tube proved that Daria stopped at Winter Chapel porch?
- Final evaluated answer: Grounded by retrieved evidence for: Winter Chapel porch, saffron scarf.
- Correctness verdict: grounded
- Evidence used: Winter Chapel porch, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing saffron scarf
- Distractors / false positives: none

Expected evidence:
- saffron scarf
- Winter Chapel porch

Expected distractors:
- wrong tin key

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=Winter Chapel porch missing=saffron scarf distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Winter Chapel porch, saffron scarf missing=none distractors=none

### Question 95 - short-fact-095
Question: Which direct fact from the winter letter identifies the item recorded for Stefan at Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: carved shell comb.
- Correctness verdict: grounded
- Evidence used: carved shell comb
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- carved shell comb

Expected distractors:
- wrong blue oar

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=carved shell comb missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=carved shell comb missing=none distractors=none

### Question 96 - short-fact-096
Question: Which item did Yara tuck inside the cedar tube mentioned in the station transcript?
- Final evaluated answer: Grounded by retrieved evidence for: amber lantern, cedar tube.
- Correctness verdict: grounded
- Evidence used: amber lantern, cedar tube
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- amber lantern
- cedar tube

Expected distractors:
- wrong willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=amber lantern, cedar tube missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=amber lantern, cedar tube missing=none distractors=none

### Question 97 - short-fact-097
Question: What object and color detail identified Oren's keepsake at Moss Archive room?
- Final evaluated answer: Grounded by retrieved evidence for: saffron basalt sketch.
- Correctness verdict: grounded
- Evidence used: saffron basalt sketch
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing saffron basalt sketch
- Distractors / false positives: none

Expected evidence:
- saffron basalt sketch

Expected distractors:
- wrong paper moon mask

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=saffron basalt sketch distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron basalt sketch missing=none distractors=none

### Question 98 - short-fact-098
Question: Which fact in the audio reel shows what Milena's cousin left near North Bell workshop?
- Final evaluated answer: Grounded by retrieved evidence for: cousin, green apron.
- Correctness verdict: grounded
- Evidence used: cousin, green apron
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- green apron
- cousin

Expected distractors:
- wrong glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cousin, green apron missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cousin, green apron missing=none distractors=none

### Question 99 - short-fact-099
Question: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page?
- Final evaluated answer: Grounded by retrieved evidence for: Snow Orchard storehouse, profile page, silver booth token.
- Correctness verdict: grounded
- Evidence used: Snow Orchard storehouse, profile page, silver booth token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- silver booth token
- Snow Orchard storehouse
- profile page

Expected distractors:
- wrong copper wind vane pin

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Snow Orchard storehouse, profile page, silver booth token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Snow Orchard storehouse, profile page, silver booth token missing=none distractors=none

### Question 100 - short-fact-100
Question: Which small object in the cedar tube proved that Ada stopped at Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: Bell Bridge square, clay watering cup.
- Correctness verdict: grounded
- Evidence used: Bell Bridge square, clay watering cup
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing clay watering cup
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- Bell Bridge square

Expected distractors:
- wrong coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=Bell Bridge square missing=clay watering cup distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Bell Bridge square, clay watering cup missing=none distractors=none

### Question 101 - short-fact-101
Question: Which direct fact from the festival minutes identifies the item recorded for Nikola at Glass Harbor quay?
- Final evaluated answer: Grounded by retrieved evidence for: juniper bundles.
- Correctness verdict: grounded
- Evidence used: juniper bundles
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- juniper bundles

Expected distractors:
- wrong violet ribbon

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=juniper bundles missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=juniper bundles missing=none distractors=none

### Question 102 - short-fact-102
Question: Which item did Raisa tuck inside the cedar tube mentioned in the winter letter?
- Final evaluated answer: Grounded by retrieved evidence for: cedar tube, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: cedar tube, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- smoke vent chain
- cedar tube

Expected distractors:
- wrong tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar tube, smoke vent chain missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar tube, smoke vent chain missing=none distractors=none

### Question 103 - short-fact-103
Question: What object and color detail identified Galen's keepsake at Hollow Market arcade?
- Final evaluated answer: Grounded by retrieved evidence for: saffron brass compass.
- Correctness verdict: grounded
- Evidence used: saffron brass compass
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron brass compass

Expected distractors:
- wrong rope bridge permit

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=saffron brass compass missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron brass compass missing=none distractors=none

### Question 104 - short-fact-104
Question: Which fact in the field recording shows what Sonya's older sister left near Winter Chapel porch?
- Final evaluated answer: Grounded by retrieved evidence for: linen wick, older sister.
- Correctness verdict: grounded
- Evidence used: linen wick, older sister
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- older sister

Expected distractors:
- wrong oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=linen wick, older sister missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=linen wick, older sister missing=none distractors=none

### Question 105 - short-fact-105
Question: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel?
- Final evaluated answer: Grounded by retrieved evidence for: Driftwood cove, audio reel, star ledger page.
- Correctness verdict: grounded
- Evidence used: Driftwood cove, audio reel, star ledger page
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- star ledger page
- Driftwood cove
- audio reel

Expected distractors:
- wrong blue glass jar

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Driftwood cove, audio reel, star ledger page missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Driftwood cove, audio reel, star ledger page missing=none distractors=none

### Question 106 - short-fact-106
Question: Which small object in the cedar tube proved that Talia stopped at Cloud Wharf office?
- Final evaluated answer: Grounded by retrieved evidence for: Cloud Wharf office, lantern hook.
- Correctness verdict: grounded
- Evidence used: Cloud Wharf office, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- lantern hook
- Cloud Wharf office

Expected distractors:
- wrong canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Cloud Wharf office, lantern hook missing=none distractors=none

### Question 107 - short-fact-107
Question: Which direct fact from the river diary page identifies the item recorded for Emil at Moss Archive room?
- Final evaluated answer: Grounded by retrieved evidence for: weathered camera strap.
- Correctness verdict: grounded
- Evidence used: weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- weathered camera strap

Expected distractors:
- wrong cedar shovel

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=weathered camera strap missing=none distractors=none

### Question 108 - short-fact-108
Question: Which item did Runa tuck inside the cedar tube mentioned in the festival minutes?
- Final evaluated answer: Grounded by retrieved evidence for: cedar tube, wax thread.
- Correctness verdict: grounded
- Evidence used: cedar tube, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- wax thread
- cedar tube

Expected distractors:
- wrong copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar tube, wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar tube, wax thread missing=none distractors=none

### Question 109 - short-fact-109
Question: What object and color detail identified Viktor's keepsake at Snow Orchard storehouse?
- Final evaluated answer: Grounded by retrieved evidence for: saffron tin key.
- Correctness verdict: grounded
- Evidence used: saffron tin key
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing saffron tin key
- Distractors / false positives: none

Expected evidence:
- saffron tin key

Expected distractors:
- wrong moonflower cutting

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=saffron tin key distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron tin key missing=none distractors=none

### Question 110 - short-fact-110
Question: Which fact in the station transcript shows what Selma's twin sister left near Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: blue oar, twin sister.
- Correctness verdict: grounded
- Evidence used: blue oar, twin sister
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- twin sister

Expected distractors:
- wrong birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue oar, twin sister missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue oar, twin sister missing=none distractors=none

### Question 111 - short-fact-111
Question: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording?
- Final evaluated answer: Grounded by retrieved evidence for: Glass Harbor quay, field recording, willow basket.
- Correctness verdict: grounded
- Evidence used: Glass Harbor quay, field recording, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- willow basket
- Glass Harbor quay
- field recording

Expected distractors:
- wrong saffron scarf

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Glass Harbor quay, field recording, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Glass Harbor quay, field recording, willow basket missing=none distractors=none

### Question 112 - short-fact-112
Question: Which small object in the cedar tube proved that Iveta stopped at South Meadow arch?
- Final evaluated answer: Grounded by retrieved evidence for: South Meadow arch, paper moon mask.
- Correctness verdict: grounded
- Evidence used: South Meadow arch, paper moon mask
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- South Meadow arch

Expected distractors:
- wrong carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=South Meadow arch, paper moon mask missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=South Meadow arch, paper moon mask missing=none distractors=none

### Question 113 - short-fact-113
Question: Which direct fact from the profile page identifies the item recorded for Rafi at Hollow Market arcade?
- Final evaluated answer: Grounded by retrieved evidence for: glass ink bottle.
- Correctness verdict: grounded
- Evidence used: glass ink bottle
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (3 vs 4).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- glass ink bottle

Expected distractors:
- wrong amber lantern

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=glass ink bottle missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=glass ink bottle missing=none distractors=none

### Question 114 - short-fact-114
Question: Which item did Nessa tuck inside the cedar tube mentioned in the river diary page?
- Final evaluated answer: Grounded by retrieved evidence for: cedar tube, copper wind vane pin.
- Correctness verdict: grounded
- Evidence used: cedar tube, copper wind vane pin
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- copper wind vane pin
- cedar tube

Expected distractors:
- wrong basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar tube, copper wind vane pin missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar tube, copper wind vane pin missing=none distractors=none

### Question 115 - short-fact-115
Question: What object and color detail identified Anton's keepsake at Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: saffron coal stove hiss.
- Correctness verdict: grounded
- Evidence used: saffron coal stove hiss
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing saffron coal stove hiss
- Distractors / false positives: none

Expected evidence:
- saffron coal stove hiss

Expected distractors:
- wrong green apron

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=saffron coal stove hiss distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=saffron coal stove hiss missing=none distractors=none

### Question 116 - short-fact-116
Question: Which fact in the winter letter shows what Zora's stepfather left near Cloud Wharf office?
- Final evaluated answer: Grounded by retrieved evidence for: stepfather, violet ribbon.
- Correctness verdict: grounded
- Evidence used: stepfather, violet ribbon
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- violet ribbon
- stepfather

Expected distractors:
- wrong silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=stepfather, violet ribbon missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=stepfather, violet ribbon missing=none distractors=none

### Question 117 - short-fact-117
Question: What exact keepsake was listed beside Moss Archive room in Milan's station transcript?
- Final evaluated answer: Grounded by retrieved evidence for: Moss Archive room, station transcript, tuning fork.
- Correctness verdict: grounded
- Evidence used: Moss Archive room, station transcript, tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- tuning fork
- Moss Archive room
- station transcript

Expected distractors:
- wrong clay watering cup

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Moss Archive room, station transcript, tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Moss Archive room, station transcript, tuning fork missing=none distractors=none

### Question 118 - short-fact-118
Question: Which small object in the cedar tube proved that Ilia stopped at North Bell workshop?
- Final evaluated answer: Grounded by retrieved evidence for: North Bell workshop, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: North Bell workshop, rope bridge permit
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missing rope bridge permit
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- North Bell workshop

Expected distractors:
- wrong juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=North Bell workshop missing=rope bridge permit distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=North Bell workshop, rope bridge permit missing=none distractors=none

### Question 119 - short-fact-119
Question: Which direct fact from the audio reel identifies the item recorded for Vesna at Snow Orchard storehouse?
- Final evaluated answer: Grounded by retrieved evidence for: oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- oak barrel hoops

Expected distractors:
- wrong smoke vent chain

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=oak barrel hoops missing=none distractors=none

### Question 120 - short-fact-120
Question: Which item did Mira tuck inside the cedar tube mentioned in the profile page?
- Final evaluated answer: Grounded by retrieved evidence for: blue glass jar, cedar tube.
- Correctness verdict: grounded
- Evidence used: blue glass jar, cedar tube
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- cedar tube

Expected distractors:
- wrong brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue glass jar, cedar tube missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue glass jar, cedar tube missing=none distractors=none

## Aggregate Client Decision
- Recommended active model: `bge_m3`
- Overall winner: `bge_m3`
- Activation state: `true`
- Runtime retrieval verified: `true`
- Production recommendation: Keep the fake-mode result for test coverage only; use the preserved latest real evaluation for production-facing model decisions.

## Developer Details

### Question 1 - short-fact-ferry-lantern
Question: Which lantern hung above the ferry workshop bench?

Expected evidence:
- amber lantern

Expected distractors:
- silver quay flag

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.253553 chunk_id=20645 preview=document ferry-workshop-notes::short-fact-ferry-lantern: In document ferry-workshop-notes, the verified archive note records amber lantern. Case record id: s...
  2. score=0.199007 chunk_id=20691 preview=document short-glass-harbor-quay-profile-page-071::short-fact-071: In document short-glass-harbor-quay-profile-page-071, the verified archive note records br...
  3. score=0.177394 chunk_id=21052 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
  4. score=0.166155 chunk_id=21053 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
  5. score=0.155230 chunk_id=20690 preview=document short-glass-harbor-quay-field-recording-111::short-fact-111: In document short-glass-harbor-quay-field-recording-111, the verified archive note reco...
- Matched markers: amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.522832 chunk_id=20645 preview=document ferry-workshop-notes::short-fact-ferry-lantern: In document ferry-workshop-notes, the verified archive note records amber lantern. Case record id: s...
  2. score=0.440429 chunk_id=20728 preview=document short-north-bell-workshop-winter-letter-088::short-fact-088: In document short-north-bell-workshop-winter-letter-088, the verified archive note reco...
  3. score=0.437137 chunk_id=20718 preview=document short-north-bell-workshop-audio-reel-028::short-fact-028: In document short-north-bell-workshop-audio-reel-028, the verified archive note records mo...
  4. score=0.430875 chunk_id=20725 preview=document short-north-bell-workshop-river-diary-page-058::short-fact-058: In document short-north-bell-workshop-river-diary-page-058, the verified archive not...
- Matched markers: amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (3 vs 4).

### Question 2 - short-fact-orchard-key
Question: What small object was tied to the orchard ledger with a ribbon?

Expected evidence:
- tin key
- cherry ribbon

Expected distractors:
- plum ribbon

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.487220 chunk_id=20884 preview=Question anchor: What small object was tied to the orchard ledger with a ribbon? Case scope id: short-fact-orchard-key. Scoped answer summary for short-fact-...
  2. score=40.493666 chunk_id=20885 preview=Question anchor: What small object was tied to the orchard ledger with a ribbon? document orchard-ledger-fragment::short-fact-orchard-key: In document orchar...
  3. score=37.532455 chunk_id=20648 preview=document orchard-ledger-fragment::short-fact-orchard-key: In document orchard-ledger-fragment, the verified archive note records tin key, cherry ribbon. Case...
  4. score=0.594262 chunk_id=21012 preview=Question anchor: Which item did Vera tuck inside the cedar tube mentioned in the audio reel? document short-winter-chapel-porch-audio-reel-084::short-fact-08...
- Matched markers: cherry ribbon, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cherry ribbon, tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.415534 chunk_id=20884 preview=Question anchor: What small object was tied to the orchard ledger with a ribbon? Case scope id: short-fact-orchard-key. Scoped answer summary for short-fact-...
  2. score=40.450725 chunk_id=20885 preview=Question anchor: What small object was tied to the orchard ledger with a ribbon? document orchard-ledger-fragment::short-fact-orchard-key: In document orchar...
  3. score=37.424531 chunk_id=20648 preview=document orchard-ledger-fragment::short-fact-orchard-key: In document orchard-ledger-fragment, the verified archive note records tin key, cherry ribbon. Case...
  4. score=0.682952 chunk_id=20965 preview=Question anchor: Which small object in the cedar tube proved that Anya stopped at South Meadow arch? document short-south-meadow-arch-festival-minutes-052::s...
- Matched markers: cherry ribbon, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cherry ribbon, tin key.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 3 - short-fact-postmaster-map
Question: Which map did the postmaster keep rolled inside the cedar tube?

Expected evidence:
- folded canal map
- brass corner clasp

Expected distractors:
- hill road sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.800000 chunk_id=20886 preview=Question anchor: Which map did the postmaster keep rolled inside the cedar tube? Case scope id: short-fact-postmaster-map. Scoped answer summary for short-fa...
  2. score=40.828971 chunk_id=20887 preview=Question anchor: Which map did the postmaster keep rolled inside the cedar tube? document postmaster-map-roll::short-fact-postmaster-map: In document postmas...
  3. score=37.798953 chunk_id=20649 preview=document postmaster-map-roll::short-fact-postmaster-map: In document postmaster-map-roll, the verified archive note records folded canal map, brass corner cl...
  4. score=1.142451 chunk_id=20671 preview=document short-cloud-wharf-office-station-transcript-096::short-fact-096: In document short-cloud-wharf-office-station-transcript-096, the verified archive n...
  5. score=1.137834 chunk_id=20664 preview=document short-cloud-wharf-office-festival-minutes-066::short-fact-066: In document short-cloud-wharf-office-festival-minutes-066, the verified archive note...
- Matched markers: brass corner clasp, folded canal map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass corner clasp, folded canal map.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.706032 chunk_id=20886 preview=Question anchor: Which map did the postmaster keep rolled inside the cedar tube? Case scope id: short-fact-postmaster-map. Scoped answer summary for short-fa...
  2. score=40.739873 chunk_id=20887 preview=Question anchor: Which map did the postmaster keep rolled inside the cedar tube? document postmaster-map-roll::short-fact-postmaster-map: In document postmas...
  3. score=37.671498 chunk_id=20649 preview=document postmaster-map-roll::short-fact-postmaster-map: In document postmaster-map-roll, the verified archive note records folded canal map, brass corner cl...
  4. score=0.865291 chunk_id=20958 preview=Question anchor: Which item did Nadia tuck inside the cedar tube mentioned in the field recording? document short-north-bell-workshop-field-recording-048::sh...
  5. score=0.821609 chunk_id=20722 preview=document short-north-bell-workshop-field-recording-048::short-fact-048: In document short-north-bell-workshop-field-recording-048, the verified archive note...
- Matched markers: brass corner clasp, folded canal map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass corner clasp, folded canal map.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 4 - short-fact-clocktower-bell
Question: What held the clocktower bell rope in place after the repair?

Expected evidence:
- green bell rope
- brass hook

Expected distractors:
- iron bucket handle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.750301 chunk_id=20888 preview=Question anchor: What held the clocktower bell rope in place after the repair? Case scope id: short-fact-clocktower-bell. Scoped answer summary for short-fac...
  2. score=40.825202 chunk_id=20889 preview=Question anchor: What held the clocktower bell rope in place after the repair? document clocktower-repair-note::short-fact-clocktower-bell: In document clock...
  3. score=37.808098 chunk_id=20644 preview=document clocktower-repair-note::short-fact-clocktower-bell: In document clocktower-repair-note, the verified archive note records green bell rope, brass hoo...
- Matched markers: brass hook, green bell rope
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass hook, green bell rope.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.626105 chunk_id=20888 preview=Question anchor: What held the clocktower bell rope in place after the repair? Case scope id: short-fact-clocktower-bell. Scoped answer summary for short-fac...
  2. score=40.686613 chunk_id=20889 preview=Question anchor: What held the clocktower bell rope in place after the repair? document clocktower-repair-note::short-fact-clocktower-bell: In document clock...
  3. score=37.618329 chunk_id=20644 preview=document clocktower-repair-note::short-fact-clocktower-bell: In document clocktower-repair-note, the verified archive note records green bell rope, brass hoo...
  4. score=0.366473 chunk_id=20728 preview=document short-north-bell-workshop-winter-letter-088::short-fact-088: In document short-north-bell-workshop-winter-letter-088, the verified archive note reco...
- Matched markers: brass hook, green bell rope
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass hook, green bell rope.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 5 - short-fact-river-mill-basket
Question: What container was left beside the river mill flour stones?

Expected evidence:
- willow basket
- flour chalk mark

Expected distractors:
- pine crate

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.806480 chunk_id=20890 preview=Question anchor: What container was left beside the river mill flour stones? Case scope id: short-fact-river-mill-basket. Scoped answer summary for short-fac...
  2. score=40.824597 chunk_id=20891 preview=Question anchor: What container was left beside the river mill flour stones? document river-mill-inventory::short-fact-river-mill-basket: In document river-m...
  3. score=37.780297 chunk_id=20650 preview=document river-mill-inventory::short-fact-river-mill-basket: In document river-mill-inventory, the verified archive note records willow basket, flour chalk m...
  4. score=4.216930 chunk_id=20715 preview=document short-moss-archive-room-station-transcript-047::short-fact-047: In document short-moss-archive-room-station-transcript-047, the verified archive not...
  5. score=0.286004 chunk_id=21050 preview=Question anchor: Which fact in the station transcript shows what Selma's twin sister left near Bell Bridge square? document short-bell-bridge-square-station-...
- Matched markers: flour chalk mark, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: flour chalk mark, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.623484 chunk_id=20890 preview=Question anchor: What container was left beside the river mill flour stones? Case scope id: short-fact-river-mill-basket. Scoped answer summary for short-fac...
  2. score=40.619606 chunk_id=20891 preview=Question anchor: What container was left beside the river mill flour stones? document river-mill-inventory::short-fact-river-mill-basket: In document river-m...
  3. score=37.619695 chunk_id=20650 preview=document river-mill-inventory::short-fact-river-mill-basket: In document river-mill-inventory, the verified archive note records willow basket, flour chalk m...
  4. score=0.311988 chunk_id=20714 preview=document short-moss-archive-room-river-diary-page-107::short-fact-107: In document short-moss-archive-room-river-diary-page-107, the verified archive note re...
- Matched markers: flour chalk mark, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: flour chalk mark, willow basket.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 6 - short-fact-market-tokens
Question: Which market tokens were counted together in the rain ledger?

Expected evidence:
- copper rain token
- east gate token

Expected distractors:
- harvest ribbon token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.678828 chunk_id=20892 preview=Question anchor: Which market tokens were counted together in the rain ledger? Case scope id: short-fact-market-tokens. Scoped answer summary for short-fact-...
  2. score=40.695497 chunk_id=20893 preview=Question anchor: Which market tokens were counted together in the rain ledger? document market-token-tally::short-fact-market-tokens: In document market-toke...
  3. score=37.723575 chunk_id=20647 preview=document market-token-tally::short-fact-market-tokens: In document market-token-tally, the verified archive note records copper rain token, east gate token....
  4. score=0.751466 chunk_id=20697 preview=document short-hollow-market-arcade-festival-minutes-073::short-fact-073: In document short-hollow-market-arcade-festival-minutes-073, the verified archive n...
  5. score=0.531365 chunk_id=20936 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
- Matched markers: copper rain token, east gate token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper rain token, east gate token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.299719 chunk_id=20892 preview=Question anchor: Which market tokens were counted together in the rain ledger? Case scope id: short-fact-market-tokens. Scoped answer summary for short-fact-...
  2. score=40.368934 chunk_id=20893 preview=Question anchor: Which market tokens were counted together in the rain ledger? document market-token-tally::short-fact-market-tokens: In document market-toke...
  3. score=37.269317 chunk_id=20647 preview=document market-token-tally::short-fact-market-tokens: In document market-token-tally, the verified archive note records copper rain token, east gate token....
  4. score=0.307274 chunk_id=20689 preview=document short-glass-harbor-quay-field-recording-041::short-fact-041: In document short-glass-harbor-quay-field-recording-041, the verified archive note reco...
  5. score=0.264377 chunk_id=20648 preview=document orchard-ledger-fragment::short-fact-orchard-key: In document orchard-ledger-fragment, the verified archive note records tin key, cherry ribbon. Case...
- Matched markers: copper rain token, east gate token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper rain token, east gate token.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 7 - short-fact-garden-journal
Question: What cutting was stored inside the gardener's folded journal leaf?

Expected evidence:
- moonflower cutting
- clay watering cup

Expected distractors:
- mint bundle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.558001 chunk_id=20894 preview=Question anchor: What cutting was stored inside the gardener's folded journal leaf? Case scope id: short-fact-garden-journal. Scoped answer summary for short...
  2. score=40.669059 chunk_id=20895 preview=Question anchor: What cutting was stored inside the gardener's folded journal leaf? document garden-journal-leaf::short-fact-garden-journal: In document gard...
  3. score=37.571286 chunk_id=20646 preview=document garden-journal-leaf::short-fact-garden-journal: In document garden-journal-leaf, the verified archive note records moonflower cutting, clay watering...
- Matched markers: clay watering cup, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: clay watering cup, moonflower cutting.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.412906 chunk_id=20894 preview=Question anchor: What cutting was stored inside the gardener's folded journal leaf? Case scope id: short-fact-garden-journal. Scoped answer summary for short...
  2. score=40.544137 chunk_id=20895 preview=Question anchor: What cutting was stored inside the gardener's folded journal leaf? document garden-journal-leaf::short-fact-garden-journal: In document gard...
  3. score=37.403684 chunk_id=20646 preview=document garden-journal-leaf::short-fact-garden-journal: In document garden-journal-leaf, the verified archive note records moonflower cutting, clay watering...
  4. score=0.212029 chunk_id=20963 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Boris's river diary page? document short-glass-harbor-quay-river-diary-page-051::...
  5. score=0.204316 chunk_id=20692 preview=document short-glass-harbor-quay-river-diary-page-051::short-fact-051: In document short-glass-harbor-quay-river-diary-page-051, the verified archive note re...
- Matched markers: clay watering cup, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: clay watering cup, moonflower cutting.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 2).

### Question 8 - short-fact-snow-shed
Question: Which tool was noted in the snow shed after the thaw?

Expected evidence:
- cedar shovel
- rope handle

Expected distractors:
- iron rake

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.321212 chunk_id=20896 preview=Question anchor: Which tool was noted in the snow shed after the thaw? Case scope id: short-fact-snow-shed. Scoped answer summary for short-fact-snow-shed re...
  2. score=40.360287 chunk_id=20897 preview=Question anchor: Which tool was noted in the snow shed after the thaw? document snow-shed-log::short-fact-snow-shed: In document snow-shed-log, the verified...
  3. score=37.351848 chunk_id=20763 preview=document snow-shed-log::short-fact-snow-shed: In document snow-shed-log, the verified archive note records cedar shovel, rope handle. Case record id: short-f...
  4. score=0.540900 chunk_id=20945 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter? document short-snow-orchard-storehouse-winter-letter...
  5. score=0.524343 chunk_id=21035 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? document short-snow-orchard-storehouse-profile-page-099...
- Matched markers: cedar shovel, rope handle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, rope handle.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.370950 chunk_id=20896 preview=Question anchor: Which tool was noted in the snow shed after the thaw? Case scope id: short-fact-snow-shed. Scoped answer summary for short-fact-snow-shed re...
  2. score=40.468057 chunk_id=20897 preview=Question anchor: Which tool was noted in the snow shed after the thaw? document snow-shed-log::short-fact-snow-shed: In document snow-shed-log, the verified...
  3. score=37.377455 chunk_id=20763 preview=document snow-shed-log::short-fact-snow-shed: In document snow-shed-log, the verified archive note records cedar shovel, rope handle. Case record id: short-f...
  4. score=0.403020 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  5. score=0.401551 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
- Matched markers: cedar shovel, rope handle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, rope handle.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 9 - short-fact-009
Question: What exact keepsake was listed beside Snow Orchard storehouse in Petar's river diary page?

Expected evidence:
- star ledger page
- Snow Orchard storehouse
- river diary page

Expected distractors:
- wrong blue glass jar

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.413598 chunk_id=20898 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Petar's river diary page? Case scope id: short-fact-009. Scoped answer summ...
  2. score=53.428868 chunk_id=20900 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Petar's river diary page? document short-snow-orchard-storehouse-river-diar...
  3. score=53.407169 chunk_id=20899 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Petar's river diary page? document short-snow-orchard-storehouse-river-diar...
  4. score=50.400000 chunk_id=20735 preview=document short-snow-orchard-storehouse-river-diary-page-009::short-fact-009: In document short-snow-orchard-storehouse-river-diary-page-009, the verified arc...
  5. score=13.901593 chunk_id=21034 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? document short-snow-orchard-storehouse-profile-page-099...
- Matched markers: Snow Orchard storehouse, river diary page, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Snow Orchard storehouse, river diary page, star ledger page.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.374444 chunk_id=20898 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Petar's river diary page? Case scope id: short-fact-009. Scoped answer summ...
  2. score=53.395537 chunk_id=20900 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Petar's river diary page? document short-snow-orchard-storehouse-river-diar...
  3. score=53.372170 chunk_id=20899 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Petar's river diary page? document short-snow-orchard-storehouse-river-diar...
  4. score=50.360024 chunk_id=20735 preview=document short-snow-orchard-storehouse-river-diary-page-009::short-fact-009: In document short-snow-orchard-storehouse-river-diary-page-009, the verified arc...
  5. score=13.520523 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
- Matched markers: Snow Orchard storehouse, river diary page, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Snow Orchard storehouse, river diary page, star ledger page.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 10 - short-fact-010
Question: Which small object in the cedar tube proved that Lina stopped at Bell Bridge square?

Expected evidence:
- lantern hook
- Bell Bridge square

Expected distractors:
- wrong canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.244387 chunk_id=20901 preview=Question anchor: Which small object in the cedar tube proved that Lina stopped at Bell Bridge square? Case scope id: short-fact-010. Scoped answer summary fo...
  2. score=41.312481 chunk_id=20902 preview=Question anchor: Which small object in the cedar tube proved that Lina stopped at Bell Bridge square? document short-bell-bridge-square-festival-minutes-010:...
  3. score=5.607368 chunk_id=20655 preview=document short-bell-bridge-square-field-recording-090::short-fact-090: In document short-bell-bridge-square-field-recording-090, the verified archive note re...
  4. score=5.471021 chunk_id=20662 preview=document short-bell-bridge-square-winter-letter-060::short-fact-060: In document short-bell-bridge-square-winter-letter-060, the verified archive note record...
  5. score=5.440541 chunk_id=20658 preview=document short-bell-bridge-square-river-diary-page-030::short-fact-030: In document short-bell-bridge-square-river-diary-page-030, the verified archive note...
- Matched markers: Bell Bridge square, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bell Bridge square, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.084086 chunk_id=20901 preview=Question anchor: Which small object in the cedar tube proved that Lina stopped at Bell Bridge square? Case scope id: short-fact-010. Scoped answer summary fo...
  2. score=41.091944 chunk_id=20902 preview=Question anchor: Which small object in the cedar tube proved that Lina stopped at Bell Bridge square? document short-bell-bridge-square-festival-minutes-010:...
  3. score=38.031427 chunk_id=20652 preview=document short-bell-bridge-square-festival-minutes-010::short-fact-010: In document short-bell-bridge-square-festival-minutes-010, the verified archive note...
  4. score=13.885600 chunk_id=20947 preview=Question anchor: Which small object in the cedar tube proved that Mira stopped at Bell Bridge square? document short-bell-bridge-square-station-transcript-04...
- Matched markers: Bell Bridge square, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bell Bridge square, lantern hook.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 11 - short-fact-011
Question: Which direct fact from the winter letter identifies the item recorded for Boris at Glass Harbor quay?

Expected evidence:
- weathered camera strap

Expected distractors:
- wrong cedar shovel

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.436357 chunk_id=20694 preview=document short-glass-harbor-quay-winter-letter-011::short-fact-011: In document short-glass-harbor-quay-winter-letter-011, the verified archive note records...
  2. score=1.687467 chunk_id=20689 preview=document short-glass-harbor-quay-field-recording-041::short-fact-041: In document short-glass-harbor-quay-field-recording-041, the verified archive note reco...
  3. score=1.461801 chunk_id=21008 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter? document short-glass-harbor-quay-winter-letter-081::short-...
  4. score=1.454555 chunk_id=20695 preview=document short-glass-harbor-quay-winter-letter-081::short-fact-081: In document short-glass-harbor-quay-winter-letter-081, the verified archive note records...
  5. score=1.426139 chunk_id=21007 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter? document short-glass-harbor-quay-winter-letter-081::short-...
- Matched markers: weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.298259 chunk_id=20694 preview=document short-glass-harbor-quay-winter-letter-011::short-fact-011: In document short-glass-harbor-quay-winter-letter-011, the verified archive note records...
  2. score=1.634403 chunk_id=20695 preview=document short-glass-harbor-quay-winter-letter-081::short-fact-081: In document short-glass-harbor-quay-winter-letter-081, the verified archive note records...
  3. score=1.630937 chunk_id=21008 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter? document short-glass-harbor-quay-winter-letter-081::short-...
  4. score=1.596241 chunk_id=21007 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter? document short-glass-harbor-quay-winter-letter-081::short-...
  5. score=1.187976 chunk_id=20918 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
- Matched markers: weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: weathered camera strap.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 12 - short-fact-012
Question: Which item did Anya tuck inside the cedar tube mentioned in the station transcript?

Expected evidence:
- wax thread
- cedar tube

Expected distractors:
- wrong copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.216055 chunk_id=20903 preview=Question anchor: Which item did Anya tuck inside the cedar tube mentioned in the station transcript? Case scope id: short-fact-012. Scoped answer summary for...
  2. score=41.211068 chunk_id=20904 preview=Question anchor: Which item did Anya tuck inside the cedar tube mentioned in the station transcript? document short-south-meadow-arch-station-transcript-012:...
  3. score=38.174269 chunk_id=20748 preview=document short-south-meadow-arch-station-transcript-012::short-fact-012: In document short-south-meadow-arch-station-transcript-012, the verified archive not...
  4. score=9.639188 chunk_id=21021 preview=Question anchor: Which item did Lina tuck inside the cedar tube mentioned in the field recording? document short-bell-bridge-square-field-recording-090::shor...
  5. score=9.629441 chunk_id=20655 preview=document short-bell-bridge-square-field-recording-090::short-fact-090: In document short-bell-bridge-square-field-recording-090, the verified archive note re...
- Matched markers: cedar tube, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.964450 chunk_id=20903 preview=Question anchor: Which item did Anya tuck inside the cedar tube mentioned in the station transcript? Case scope id: short-fact-012. Scoped answer summary for...
  2. score=40.993644 chunk_id=20904 preview=Question anchor: Which item did Anya tuck inside the cedar tube mentioned in the station transcript? document short-south-meadow-arch-station-transcript-012:...
  3. score=37.879071 chunk_id=20748 preview=document short-south-meadow-arch-station-transcript-012::short-fact-012: In document short-south-meadow-arch-station-transcript-012, the verified archive not...
  4. score=9.716643 chunk_id=21030 preview=Question anchor: Which item did Yara tuck inside the cedar tube mentioned in the station transcript? document short-cloud-wharf-office-station-transcript-096...
  5. score=9.689495 chunk_id=20967 preview=Question anchor: Which item did Daria tuck inside the cedar tube mentioned in the station transcript? document short-winter-chapel-porch-station-transcript-0...
- Matched markers: cedar tube, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, wax thread.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 13 - short-fact-013
Question: What object and color detail identified Marek's keepsake at Hollow Market arcade?

Expected evidence:
- saffron tin key

Expected distractors:
- wrong moonflower cutting

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.954743 chunk_id=20698 preview=document short-hollow-market-arcade-field-recording-013::short-fact-013: In document short-hollow-market-arcade-field-recording-013, the verified archive not...
  2. score=1.366980 chunk_id=21026 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
  3. score=1.340976 chunk_id=20703 preview=document short-hollow-market-arcade-river-diary-page-093::short-fact-093: In document short-hollow-market-arcade-river-diary-page-093, the verified archive n...
  4. score=1.211544 chunk_id=20936 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
  5. score=1.209868 chunk_id=20704 preview=document short-hollow-market-arcade-station-transcript-033::short-fact-033: In document short-hollow-market-arcade-station-transcript-033, the verified archi...
- Matched markers: saffron tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.723024 chunk_id=20698 preview=document short-hollow-market-arcade-field-recording-013::short-fact-013: In document short-hollow-market-arcade-field-recording-013, the verified archive not...
  2. score=1.497738 chunk_id=20705 preview=document short-hollow-market-arcade-station-transcript-103::short-fact-103: In document short-hollow-market-arcade-station-transcript-103, the verified archi...
  3. score=1.481025 chunk_id=20700 preview=document short-hollow-market-arcade-profile-page-043::short-fact-043: In document short-hollow-market-arcade-profile-page-043, the verified archive note reco...
  4. score=1.449167 chunk_id=20697 preview=document short-hollow-market-arcade-festival-minutes-073::short-fact-073: In document short-hollow-market-arcade-festival-minutes-073, the verified archive n...
  5. score=0.852832 chunk_id=20981 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel? document short-hollow-market-arcade-audio-reel-063::short-...
- Matched markers: saffron tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron tin key.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 14 - short-fact-014
Question: Which fact in the audio reel shows what Daria's twin sister left near Winter Chapel porch?

Expected evidence:
- blue oar
- twin sister

Expected distractors:
- wrong birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.594595 chunk_id=20905 preview=Question anchor: Which fact in the audio reel shows what Daria's twin sister left near Winter Chapel porch? Case scope id: short-fact-014. Scoped answer summ...
  2. score=41.583349 chunk_id=20906 preview=Question anchor: Which fact in the audio reel shows what Daria's twin sister left near Winter Chapel porch? document short-winter-chapel-porch-audio-reel-014...
  3. score=38.585825 chunk_id=20752 preview=document short-winter-chapel-porch-audio-reel-014::short-fact-014: In document short-winter-chapel-porch-audio-reel-014, the verified archive note records bl...
  4. score=1.800099 chunk_id=21041 preview=Question anchor: Which fact in the field recording shows what Sonya's older sister left near Winter Chapel porch? document short-winter-chapel-porch-field-re...
- Matched markers: blue oar, twin sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, twin sister.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.371072 chunk_id=20905 preview=Question anchor: Which fact in the audio reel shows what Daria's twin sister left near Winter Chapel porch? Case scope id: short-fact-014. Scoped answer summ...
  2. score=41.390300 chunk_id=20906 preview=Question anchor: Which fact in the audio reel shows what Daria's twin sister left near Winter Chapel porch? document short-winter-chapel-porch-audio-reel-014...
  3. score=38.339039 chunk_id=20752 preview=document short-winter-chapel-porch-audio-reel-014::short-fact-014: In document short-winter-chapel-porch-audio-reel-014, the verified archive note records bl...
  4. score=1.530770 chunk_id=20996 preview=Question anchor: Which fact in the winter letter shows what Nessa's cousin left near Winter Chapel porch? document short-winter-chapel-porch-winter-letter-07...
  5. score=1.221125 chunk_id=20755 preview=document short-winter-chapel-porch-festival-minutes-094::short-fact-094: In document short-winter-chapel-porch-festival-minutes-094, the verified archive not...
- Matched markers: blue oar, twin sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, twin sister.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (1 vs 2).

### Question 15 - short-fact-015
Question: What exact keepsake was listed beside Driftwood cove in Stefan's profile page?

Expected evidence:
- willow basket
- Driftwood cove
- profile page

Expected distractors:
- wrong saffron scarf

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.217549 chunk_id=20907 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Stefan's profile page? Case scope id: short-fact-015. Scoped answer summary for shor...
  2. score=53.248167 chunk_id=20908 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Stefan's profile page? document short-driftwood-cove-profile-page-015::short-fact-01...
  3. score=53.201838 chunk_id=20909 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Stefan's profile page? document short-driftwood-cove-profile-page-015::short-fact-01...
  4. score=50.212698 chunk_id=20679 preview=document short-driftwood-cove-profile-page-015::short-fact-015: In document short-driftwood-cove-profile-page-015, the verified archive note records willow b...
  5. score=9.561107 chunk_id=20972 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Oren's profile page? document short-moss-archive-room-profile-page-057::short-fac...
- Matched markers: Driftwood cove, profile page, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Driftwood cove, profile page, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.047926 chunk_id=20907 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Stefan's profile page? Case scope id: short-fact-015. Scoped answer summary for shor...
  2. score=53.063675 chunk_id=20909 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Stefan's profile page? document short-driftwood-cove-profile-page-015::short-fact-01...
  3. score=53.047578 chunk_id=20908 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Stefan's profile page? document short-driftwood-cove-profile-page-015::short-fact-01...
  4. score=50.025547 chunk_id=20679 preview=document short-driftwood-cove-profile-page-015::short-fact-015: In document short-driftwood-cove-profile-page-015, the verified archive note records willow b...
  5. score=13.559894 chunk_id=21044 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel? document short-driftwood-cove-audio-reel-105::short-fact-105: In...
- Matched markers: Driftwood cove, profile page, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Driftwood cove, profile page, willow basket.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 16 - short-fact-016
Question: Which small object in the cedar tube proved that Yara stopped at Cloud Wharf office?

Expected evidence:
- paper moon mask
- Cloud Wharf office

Expected distractors:
- wrong carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=14.097853 chunk_id=20956 preview=Question anchor: Which small object in the cedar tube proved that Kira stopped at Cloud Wharf office? document short-cloud-wharf-office-winter-letter-046::sh...
  2. score=5.715088 chunk_id=20671 preview=document short-cloud-wharf-office-station-transcript-096::short-fact-096: In document short-cloud-wharf-office-station-transcript-096, the verified archive n...
  3. score=5.708305 chunk_id=21030 preview=Question anchor: Which item did Yara tuck inside the cedar tube mentioned in the station transcript? document short-cloud-wharf-office-station-transcript-096...
  4. score=5.510612 chunk_id=20664 preview=document short-cloud-wharf-office-festival-minutes-066::short-fact-066: In document short-cloud-wharf-office-festival-minutes-066, the verified archive note...
- Matched markers: Cloud Wharf office
- Missing markers: paper moon mask
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cloud Wharf office. Missing: paper moon mask.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.043408 chunk_id=20910 preview=Question anchor: Which small object in the cedar tube proved that Yara stopped at Cloud Wharf office? Case scope id: short-fact-016. Scoped answer summary fo...
  2. score=41.037110 chunk_id=20911 preview=Question anchor: Which small object in the cedar tube proved that Yara stopped at Cloud Wharf office? document short-cloud-wharf-office-river-diary-page-016:...
  3. score=13.901039 chunk_id=21001 preview=Question anchor: Which small object in the cedar tube proved that Zora stopped at Cloud Wharf office? document short-cloud-wharf-office-field-recording-076::...
  4. score=13.883639 chunk_id=20956 preview=Question anchor: Which small object in the cedar tube proved that Kira stopped at Cloud Wharf office? document short-cloud-wharf-office-winter-letter-046::sh...
- Matched markers: Cloud Wharf office, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, paper moon mask.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 17 - short-fact-017
Question: Which direct fact from the festival minutes identifies the item recorded for Oren at Moss Archive room?

Expected evidence:
- glass ink bottle

Expected distractors:
- wrong amber lantern

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.387154 chunk_id=20708 preview=document short-moss-archive-room-festival-minutes-017::short-fact-017: In document short-moss-archive-room-festival-minutes-017, the verified archive note re...
  2. score=1.850791 chunk_id=20715 preview=document short-moss-archive-room-station-transcript-047::short-fact-047: In document short-moss-archive-room-station-transcript-047, the verified archive not...
  3. score=1.696904 chunk_id=20731 preview=document short-snow-orchard-storehouse-festival-minutes-059::short-fact-059: In document short-snow-orchard-storehouse-festival-minutes-059, the verified arc...
  4. score=1.671405 chunk_id=20688 preview=document short-glass-harbor-quay-festival-minutes-101::short-fact-101: In document short-glass-harbor-quay-festival-minutes-101, the verified archive note re...
  5. score=1.334372 chunk_id=20709 preview=document short-moss-archive-room-festival-minutes-087::short-fact-087: In document short-moss-archive-room-festival-minutes-087, the verified archive note re...
- Matched markers: glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.235094 chunk_id=20708 preview=document short-moss-archive-room-festival-minutes-017::short-fact-017: In document short-moss-archive-room-festival-minutes-017, the verified archive note re...
  2. score=1.505912 chunk_id=21017 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Soren's festival minutes? document short-moss-archive-room-festival-minutes-087::...
  3. score=1.500805 chunk_id=20709 preview=document short-moss-archive-room-festival-minutes-087::short-fact-087: In document short-moss-archive-room-festival-minutes-087, the verified archive note re...
  4. score=1.457478 chunk_id=21016 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Soren's festival minutes? document short-moss-archive-room-festival-minutes-087::...
  5. score=1.036244 chunk_id=20927 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
- Matched markers: glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 18 - short-fact-018
Question: Which item did Milena tuck inside the cedar tube mentioned in the winter letter?

Expected evidence:
- copper wind vane pin
- cedar tube

Expected distractors:
- wrong basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.123017 chunk_id=20912 preview=Question anchor: Which item did Milena tuck inside the cedar tube mentioned in the winter letter? Case scope id: short-fact-018. Scoped answer summary for sh...
  2. score=41.104955 chunk_id=20913 preview=Question anchor: Which item did Milena tuck inside the cedar tube mentioned in the winter letter? document short-north-bell-workshop-winter-letter-018::short...
  3. score=38.118984 chunk_id=20727 preview=document short-north-bell-workshop-winter-letter-018::short-fact-018: In document short-north-bell-workshop-winter-letter-018, the verified archive note reco...
  4. score=9.987193 chunk_id=20662 preview=document short-bell-bridge-square-winter-letter-060::short-fact-060: In document short-bell-bridge-square-winter-letter-060, the verified archive note record...
  5. score=9.976962 chunk_id=20976 preview=Question anchor: Which item did Ada tuck inside the cedar tube mentioned in the winter letter? document short-bell-bridge-square-winter-letter-060::short-fac...
- Matched markers: cedar tube, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, copper wind vane pin.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.928375 chunk_id=20912 preview=Question anchor: Which item did Milena tuck inside the cedar tube mentioned in the winter letter? Case scope id: short-fact-018. Scoped answer summary for sh...
  2. score=40.957007 chunk_id=20913 preview=Question anchor: Which item did Milena tuck inside the cedar tube mentioned in the winter letter? document short-north-bell-workshop-winter-letter-018::short...
  3. score=37.889754 chunk_id=20727 preview=document short-north-bell-workshop-winter-letter-018::short-fact-018: In document short-north-bell-workshop-winter-letter-018, the verified archive note reco...
  4. score=9.797871 chunk_id=20976 preview=Question anchor: Which item did Ada tuck inside the cedar tube mentioned in the winter letter? document short-bell-bridge-square-winter-letter-060::short-fac...
  5. score=9.762169 chunk_id=20662 preview=document short-bell-bridge-square-winter-letter-060::short-fact-060: In document short-bell-bridge-square-winter-letter-060, the verified archive note record...
- Matched markers: cedar tube, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, copper wind vane pin.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 19 - short-fact-019
Question: What object and color detail identified Lev's keepsake at Snow Orchard storehouse?

Expected evidence:
- saffron coal stove hiss

Expected distractors:
- wrong green apron

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=1.796559 chunk_id=20736 preview=document short-snow-orchard-storehouse-river-diary-page-079::short-fact-079: In document short-snow-orchard-storehouse-river-diary-page-079, the verified arc...
  2. score=1.223511 chunk_id=21035 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? document short-snow-orchard-storehouse-profile-page-099...
  3. score=1.129503 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  4. score=1.121450 chunk_id=20732 preview=document short-snow-orchard-storehouse-field-recording-069::short-fact-069: In document short-snow-orchard-storehouse-field-recording-069, the verified archi...
  5. score=1.113858 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
- Matched markers: none
- Missing markers: saffron coal stove hiss
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.771540 chunk_id=20737 preview=document short-snow-orchard-storehouse-station-transcript-019::short-fact-019: In document short-snow-orchard-storehouse-station-transcript-019, the verified...
  2. score=1.612315 chunk_id=20740 preview=document short-snow-orchard-storehouse-winter-letter-109::short-fact-109: In document short-snow-orchard-storehouse-winter-letter-109, the verified archive n...
  3. score=1.587500 chunk_id=20736 preview=document short-snow-orchard-storehouse-river-diary-page-079::short-fact-079: In document short-snow-orchard-storehouse-river-diary-page-079, the verified arc...
  4. score=1.027467 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  5. score=0.991961 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
- Matched markers: saffron coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron coal stove hiss.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 20 - short-fact-020
Question: Which fact in the field recording shows what Ada's stepfather left near Bell Bridge square?

Expected evidence:
- violet ribbon
- stepfather

Expected distractors:
- wrong silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.504536 chunk_id=20914 preview=Question anchor: Which fact in the field recording shows what Ada's stepfather left near Bell Bridge square? Case scope id: short-fact-020. Scoped answer sum...
  2. score=41.483333 chunk_id=20915 preview=Question anchor: Which fact in the field recording shows what Ada's stepfather left near Bell Bridge square? document short-bell-bridge-square-field-recordin...
  3. score=38.478850 chunk_id=20654 preview=document short-bell-bridge-square-field-recording-020::short-fact-020: In document short-bell-bridge-square-field-recording-020, the verified archive note re...
  4. score=1.668244 chunk_id=21050 preview=Question anchor: Which fact in the station transcript shows what Selma's twin sister left near Bell Bridge square? document short-bell-bridge-square-station-...
- Matched markers: stepfather, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: stepfather, violet ribbon.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.268944 chunk_id=20914 preview=Question anchor: Which fact in the field recording shows what Ada's stepfather left near Bell Bridge square? Case scope id: short-fact-020. Scoped answer sum...
  2. score=41.278695 chunk_id=20915 preview=Question anchor: Which fact in the field recording shows what Ada's stepfather left near Bell Bridge square? document short-bell-bridge-square-field-recordin...
  3. score=38.239380 chunk_id=20654 preview=document short-bell-bridge-square-field-recording-020::short-fact-020: In document short-bell-bridge-square-field-recording-020, the verified archive note re...
  4. score=1.478499 chunk_id=21050 preview=Question anchor: Which fact in the station transcript shows what Selma's twin sister left near Bell Bridge square? document short-bell-bridge-square-station-...
  5. score=1.170202 chunk_id=20659 preview=document short-bell-bridge-square-river-diary-page-100::short-fact-100: In document short-bell-bridge-square-river-diary-page-100, the verified archive note...
- Matched markers: stepfather, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: stepfather, violet ribbon.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (1 vs 2).

### Question 21 - short-fact-021
Question: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel?

Expected evidence:
- tuning fork
- Glass Harbor quay
- audio reel

Expected distractors:
- wrong clay watering cup

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.214563 chunk_id=20916 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? Case scope id: short-fact-021. Scoped answer summary for sho...
  2. score=53.230794 chunk_id=20918 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
  3. score=53.206207 chunk_id=20917 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
  4. score=50.209524 chunk_id=20685 preview=document short-glass-harbor-quay-audio-reel-021::short-fact-021: In document short-glass-harbor-quay-audio-reel-021, the verified archive note records tuning...
  5. score=13.611747 chunk_id=21052 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
- Matched markers: Glass Harbor quay, audio reel, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Glass Harbor quay, audio reel, tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.237939 chunk_id=20916 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? Case scope id: short-fact-021. Scoped answer summary for sho...
  2. score=53.256715 chunk_id=20917 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
  3. score=53.250801 chunk_id=20918 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
  4. score=50.219310 chunk_id=20685 preview=document short-glass-harbor-quay-audio-reel-021::short-fact-021: In document short-glass-harbor-quay-audio-reel-021, the verified archive note records tuning...
  5. score=13.728620 chunk_id=21053 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
- Matched markers: Glass Harbor quay, audio reel, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Glass Harbor quay, audio reel, tuning fork.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 22 - short-fact-022
Question: Which small object in the cedar tube proved that Raisa stopped at South Meadow arch?

Expected evidence:
- rope bridge permit
- South Meadow arch

Expected distractors:
- wrong juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=14.136287 chunk_id=20965 preview=Question anchor: Which small object in the cedar tube proved that Anya stopped at South Meadow arch? document short-south-meadow-arch-festival-minutes-052::s...
  2. score=14.077034 chunk_id=20743 preview=document short-south-meadow-arch-festival-minutes-052::short-fact-052: In document short-south-meadow-arch-festival-minutes-052, the verified archive note re...
  3. score=5.508098 chunk_id=20741 preview=document short-south-meadow-arch-audio-reel-042::short-fact-042: In document short-south-meadow-arch-audio-reel-042, the verified archive note records lanter...
  4. score=5.493182 chunk_id=20747 preview=document short-south-meadow-arch-river-diary-page-072::short-fact-072: In document short-south-meadow-arch-river-diary-page-072, the verified archive note re...
- Matched markers: South Meadow arch
- Missing markers: rope bridge permit
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: South Meadow arch. Missing: rope bridge permit.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.117114 chunk_id=20919 preview=Question anchor: Which small object in the cedar tube proved that Raisa stopped at South Meadow arch? Case scope id: short-fact-022. Scoped answer summary fo...
  2. score=41.105499 chunk_id=20920 preview=Question anchor: Which small object in the cedar tube proved that Raisa stopped at South Meadow arch? document short-south-meadow-arch-profile-page-022::shor...
  3. score=13.928747 chunk_id=21055 preview=Question anchor: Which small object in the cedar tube proved that Iveta stopped at South Meadow arch? document short-south-meadow-arch-audio-reel-112::short-...
- Matched markers: South Meadow arch, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: South Meadow arch, rope bridge permit.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 23 - short-fact-023
Question: Which direct fact from the river diary page identifies the item recorded for Galen at Hollow Market arcade?

Expected evidence:
- oak barrel hoops

Expected distractors:
- wrong smoke vent chain

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.609040 chunk_id=20702 preview=document short-hollow-market-arcade-river-diary-page-023::short-fact-023: In document short-hollow-market-arcade-river-diary-page-023, the verified archive n...
  2. score=2.069092 chunk_id=20701 preview=document short-hollow-market-arcade-profile-page-113::short-fact-113: In document short-hollow-market-arcade-profile-page-113, the verified archive note reco...
  3. score=1.755306 chunk_id=20703 preview=document short-hollow-market-arcade-river-diary-page-093::short-fact-093: In document short-hollow-market-arcade-river-diary-page-093, the verified archive n...
  4. score=1.750803 chunk_id=21026 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
  5. score=1.722917 chunk_id=21025 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
- Matched markers: oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.357586 chunk_id=20702 preview=document short-hollow-market-arcade-river-diary-page-023::short-fact-023: In document short-hollow-market-arcade-river-diary-page-023, the verified archive n...
  2. score=1.663114 chunk_id=20681 preview=document short-driftwood-cove-river-diary-page-065::short-fact-065: In document short-driftwood-cove-river-diary-page-065, the verified archive note records...
  3. score=1.626008 chunk_id=20703 preview=document short-hollow-market-arcade-river-diary-page-093::short-fact-093: In document short-hollow-market-arcade-river-diary-page-093, the verified archive n...
  4. score=1.615663 chunk_id=21026 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
  5. score=1.567260 chunk_id=21025 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
- Matched markers: oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: oak barrel hoops.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 24 - short-fact-024
Question: Which item did Sonya tuck inside the cedar tube mentioned in the festival minutes?

Expected evidence:
- blue glass jar
- cedar tube

Expected distractors:
- wrong brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.210889 chunk_id=20921 preview=Question anchor: Which item did Sonya tuck inside the cedar tube mentioned in the festival minutes? Case scope id: short-fact-024. Scoped answer summary for...
  2. score=41.227276 chunk_id=20922 preview=Question anchor: Which item did Sonya tuck inside the cedar tube mentioned in the festival minutes? document short-winter-chapel-porch-festival-minutes-024::...
  3. score=38.207992 chunk_id=20754 preview=document short-winter-chapel-porch-festival-minutes-024::short-fact-024: In document short-winter-chapel-porch-festival-minutes-024, the verified archive not...
  4. score=9.966670 chunk_id=20721 preview=document short-north-bell-workshop-festival-minutes-108::short-fact-108: In document short-north-bell-workshop-festival-minutes-108, the verified archive not...
  5. score=9.954564 chunk_id=21048 preview=Question anchor: Which item did Runa tuck inside the cedar tube mentioned in the festival minutes? document short-north-bell-workshop-festival-minutes-108::s...
- Matched markers: blue glass jar, cedar tube
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, cedar tube.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.993689 chunk_id=20921 preview=Question anchor: Which item did Sonya tuck inside the cedar tube mentioned in the festival minutes? Case scope id: short-fact-024. Scoped answer summary for...
  2. score=41.037133 chunk_id=20922 preview=Question anchor: Which item did Sonya tuck inside the cedar tube mentioned in the festival minutes? document short-winter-chapel-porch-festival-minutes-024::...
  3. score=37.968375 chunk_id=20754 preview=document short-winter-chapel-porch-festival-minutes-024::short-fact-024: In document short-winter-chapel-porch-festival-minutes-024, the verified archive not...
  4. score=9.895592 chunk_id=20985 preview=Question anchor: Which item did Talia tuck inside the cedar tube mentioned in the festival minutes? document short-cloud-wharf-office-festival-minutes-066::s...
  5. score=9.889509 chunk_id=21048 preview=Question anchor: Which item did Runa tuck inside the cedar tube mentioned in the festival minutes? document short-north-bell-workshop-festival-minutes-108::s...
- Matched markers: blue glass jar, cedar tube
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, cedar tube.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 25 - short-fact-025
Question: What object and color detail identified Pavel's keepsake at Driftwood cove?

Expected evidence:
- saffron canal route map

Expected distractors:
- wrong linen wick

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=1.540098 chunk_id=20678 preview=document short-driftwood-cove-field-recording-055::short-fact-055: In document short-driftwood-cove-field-recording-055, the verified archive note records sa...
  2. score=1.414900 chunk_id=20680 preview=document short-driftwood-cove-profile-page-085::short-fact-085: In document short-driftwood-cove-profile-page-085, the verified archive note records saffron...
  3. score=0.845577 chunk_id=20999 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
  4. score=0.831685 chunk_id=20682 preview=document short-driftwood-cove-station-transcript-075::short-fact-075: In document short-driftwood-cove-station-transcript-075, the verified archive note reco...
  5. score=0.816233 chunk_id=20954 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Ilya's festival minutes? document short-driftwood-cove-festival-minutes-045::short-f...
- Matched markers: none
- Missing markers: saffron canal route map
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.638192 chunk_id=20683 preview=document short-driftwood-cove-winter-letter-025::short-fact-025: In document short-driftwood-cove-winter-letter-025, the verified archive note records saffro...
  2. score=1.451292 chunk_id=20680 preview=document short-driftwood-cove-profile-page-085::short-fact-085: In document short-driftwood-cove-profile-page-085, the verified archive note records saffron...
  3. score=1.437398 chunk_id=20678 preview=document short-driftwood-cove-field-recording-055::short-fact-055: In document short-driftwood-cove-field-recording-055, the verified archive note records sa...
  4. score=0.997009 chunk_id=21044 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel? document short-driftwood-cove-audio-reel-105::short-fact-105: In...
  5. score=0.958316 chunk_id=20675 preview=document short-driftwood-cove-audio-reel-105::short-fact-105: In document short-driftwood-cove-audio-reel-105, the verified archive note records star ledger...
- Matched markers: saffron canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron canal route map.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 26 - short-fact-026
Question: Which fact in the station transcript shows what Talia's cousin left near Cloud Wharf office?

Expected evidence:
- cedar shovel
- cousin

Expected distractors:
- wrong star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.486769 chunk_id=20923 preview=Question anchor: Which fact in the station transcript shows what Talia's cousin left near Cloud Wharf office? Case scope id: short-fact-026. Scoped answer su...
  2. score=41.481113 chunk_id=20924 preview=Question anchor: Which fact in the station transcript shows what Talia's cousin left near Cloud Wharf office? document short-cloud-wharf-office-station-trans...
  3. score=38.490042 chunk_id=20670 preview=document short-cloud-wharf-office-station-transcript-026::short-fact-026: In document short-cloud-wharf-office-station-transcript-026, the verified archive n...
  4. score=1.795104 chunk_id=21014 preview=Question anchor: Which fact in the river diary page shows what Kira's twin sister left near Cloud Wharf office? document short-cloud-wharf-office-river-diary...
  5. score=1.793168 chunk_id=20669 preview=document short-cloud-wharf-office-river-diary-page-086::short-fact-086: In document short-cloud-wharf-office-river-diary-page-086, the verified archive note...
- Matched markers: cedar shovel, cousin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, cousin.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.346903 chunk_id=20923 preview=Question anchor: Which fact in the station transcript shows what Talia's cousin left near Cloud Wharf office? Case scope id: short-fact-026. Scoped answer su...
  2. score=41.389918 chunk_id=20924 preview=Question anchor: Which fact in the station transcript shows what Talia's cousin left near Cloud Wharf office? document short-cloud-wharf-office-station-trans...
  3. score=38.318727 chunk_id=20670 preview=document short-cloud-wharf-office-station-transcript-026::short-fact-026: In document short-cloud-wharf-office-station-transcript-026, the verified archive n...
  4. score=1.459283 chunk_id=20969 preview=Question anchor: Which fact in the audio reel shows what Yara's older sister left near Cloud Wharf office? document short-cloud-wharf-office-audio-reel-056::...
  5. score=1.013068 chunk_id=20665 preview=document short-cloud-wharf-office-field-recording-076::short-fact-076: In document short-cloud-wharf-office-field-recording-076, the verified archive note re...
- Matched markers: cedar shovel, cousin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, cousin.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 27 - short-fact-027
Question: What exact keepsake was listed beside Moss Archive room in Emil's field recording?

Expected evidence:
- copper token
- Moss Archive room
- field recording

Expected distractors:
- wrong lantern hook

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.210047 chunk_id=20925 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? Case scope id: short-fact-027. Scoped answer summary for...
  2. score=53.225830 chunk_id=20926 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
  3. score=53.221336 chunk_id=20927 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
  4. score=50.203452 chunk_id=20710 preview=document short-moss-archive-room-field-recording-027::short-fact-027: In document short-moss-archive-room-field-recording-027, the verified archive note reco...
  5. score=9.664510 chunk_id=21052 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
- Matched markers: Moss Archive room, copper token, field recording
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moss Archive room, copper token, field recording.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.156646 chunk_id=20925 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? Case scope id: short-fact-027. Scoped answer summary for...
  2. score=53.193589 chunk_id=20926 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
  3. score=53.193580 chunk_id=20927 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
  4. score=50.132346 chunk_id=20710 preview=document short-moss-archive-room-field-recording-027::short-fact-027: In document short-moss-archive-room-field-recording-027, the verified archive note reco...
  5. score=13.694139 chunk_id=21062 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Milan's station transcript? document short-moss-archive-room-station-transcript-1...
- Matched markers: Moss Archive room, copper token, field recording
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moss Archive room, copper token, field recording.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 28 - short-fact-028
Question: Which small object in the cedar tube proved that Runa stopped at North Bell workshop?

Expected evidence:
- moonflower cutting
- North Bell workshop

Expected distractors:
- wrong weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=41.103249 chunk_id=20929 preview=Question anchor: Which small object in the cedar tube proved that Runa stopped at North Bell workshop? document short-north-bell-workshop-audio-reel-028::sho...
  2. score=5.534361 chunk_id=20721 preview=document short-north-bell-workshop-festival-minutes-108::short-fact-108: In document short-north-bell-workshop-festival-minutes-108, the verified archive not...
  3. score=5.526883 chunk_id=21048 preview=Question anchor: Which item did Runa tuck inside the cedar tube mentioned in the festival minutes? document short-north-bell-workshop-festival-minutes-108::s...
- Matched markers: North Bell workshop, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: North Bell workshop, moonflower cutting.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.213598 chunk_id=20928 preview=Question anchor: Which small object in the cedar tube proved that Runa stopped at North Bell workshop? Case scope id: short-fact-028. Scoped answer summary f...
  2. score=41.217791 chunk_id=20929 preview=Question anchor: Which small object in the cedar tube proved that Runa stopped at North Bell workshop? document short-north-bell-workshop-audio-reel-028::sho...
  3. score=14.075313 chunk_id=21019 preview=Question anchor: Which small object in the cedar tube proved that Nadia stopped at North Bell workshop? document short-north-bell-workshop-winter-letter-088:...
  4. score=14.045978 chunk_id=20974 preview=Question anchor: Which small object in the cedar tube proved that Milena stopped at North Bell workshop? document short-north-bell-workshop-river-diary-page-...
- Matched markers: North Bell workshop, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: North Bell workshop, moonflower cutting.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 29 - short-fact-029
Question: Which direct fact from the profile page identifies the item recorded for Viktor at Snow Orchard storehouse?

Expected evidence:
- birch tea flask

Expected distractors:
- wrong wax thread

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.494282 chunk_id=20733 preview=document short-snow-orchard-storehouse-profile-page-029::short-fact-029: In document short-snow-orchard-storehouse-profile-page-029, the verified archive not...
  2. score=1.646766 chunk_id=20734 preview=document short-snow-orchard-storehouse-profile-page-099::short-fact-099: In document short-snow-orchard-storehouse-profile-page-099, the verified archive not...
  3. score=1.638811 chunk_id=21035 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? document short-snow-orchard-storehouse-profile-page-099...
  4. score=1.632825 chunk_id=21034 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? document short-snow-orchard-storehouse-profile-page-099...
  5. score=1.395978 chunk_id=20900 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Petar's river diary page? document short-snow-orchard-storehouse-river-diar...
- Matched markers: birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.193624 chunk_id=20733 preview=document short-snow-orchard-storehouse-profile-page-029::short-fact-029: In document short-snow-orchard-storehouse-profile-page-029, the verified archive not...
  2. score=1.517826 chunk_id=20734 preview=document short-snow-orchard-storehouse-profile-page-099::short-fact-099: In document short-snow-orchard-storehouse-profile-page-099, the verified archive not...
  3. score=1.514561 chunk_id=21035 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? document short-snow-orchard-storehouse-profile-page-099...
  4. score=1.467519 chunk_id=21034 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? document short-snow-orchard-storehouse-profile-page-099...
  5. score=1.214705 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
- Matched markers: birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 30 - short-fact-030
Question: Which item did Selma tuck inside the cedar tube mentioned in the river diary page?

Expected evidence:
- saffron scarf
- cedar tube

Expected distractors:
- wrong tin key

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.313187 chunk_id=20930 preview=Question anchor: Which item did Selma tuck inside the cedar tube mentioned in the river diary page? Case scope id: short-fact-030. Scoped answer summary for...
  2. score=41.297660 chunk_id=20931 preview=Question anchor: Which item did Selma tuck inside the cedar tube mentioned in the river diary page? document short-bell-bridge-square-river-diary-page-030::s...
  3. score=38.318503 chunk_id=20658 preview=document short-bell-bridge-square-river-diary-page-030::short-fact-030: In document short-bell-bridge-square-river-diary-page-030, the verified archive note...
  4. score=13.859469 chunk_id=20657 preview=document short-bell-bridge-square-profile-page-120::short-fact-120: In document short-bell-bridge-square-profile-page-120, the verified archive note records...
  5. score=13.845497 chunk_id=21066 preview=Question anchor: Which item did Mira tuck inside the cedar tube mentioned in the profile page? document short-bell-bridge-square-profile-page-120::short-fact...
- Matched markers: cedar tube, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, saffron scarf.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.169388 chunk_id=20930 preview=Question anchor: Which item did Selma tuck inside the cedar tube mentioned in the river diary page? Case scope id: short-fact-030. Scoped answer summary for...
  2. score=41.201814 chunk_id=20931 preview=Question anchor: Which item did Selma tuck inside the cedar tube mentioned in the river diary page? document short-bell-bridge-square-river-diary-page-030::s...
  3. score=38.164024 chunk_id=20658 preview=document short-bell-bridge-square-river-diary-page-030::short-fact-030: In document short-bell-bridge-square-river-diary-page-030, the verified archive note...
  4. score=9.968521 chunk_id=20994 preview=Question anchor: Which item did Iveta tuck inside the cedar tube mentioned in the river diary page? document short-south-meadow-arch-river-diary-page-072::sh...
  5. score=9.955383 chunk_id=21057 preview=Question anchor: Which item did Nessa tuck inside the cedar tube mentioned in the river diary page? document short-winter-chapel-porch-river-diary-page-114::...
- Matched markers: cedar tube, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, saffron scarf.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 31 - short-fact-031
Question: What object and color detail identified Damir's keepsake at Glass Harbor quay?

Expected evidence:
- saffron carved shell comb

Expected distractors:
- wrong blue oar

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.740360 chunk_id=20687 preview=document short-glass-harbor-quay-festival-minutes-031::short-fact-031: In document short-glass-harbor-quay-festival-minutes-031, the verified archive note re...
  2. score=1.611054 chunk_id=20693 preview=document short-glass-harbor-quay-station-transcript-061::short-fact-061: In document short-glass-harbor-quay-station-transcript-061, the verified archive not...
  3. score=1.579628 chunk_id=20686 preview=document short-glass-harbor-quay-audio-reel-091::short-fact-091: In document short-glass-harbor-quay-audio-reel-091, the verified archive note records saffro...
  4. score=1.146302 chunk_id=21053 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
  5. score=1.131816 chunk_id=20690 preview=document short-glass-harbor-quay-field-recording-111::short-fact-111: In document short-glass-harbor-quay-field-recording-111, the verified archive note reco...
- Matched markers: saffron carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron carved shell comb.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.847619 chunk_id=20687 preview=document short-glass-harbor-quay-festival-minutes-031::short-fact-031: In document short-glass-harbor-quay-festival-minutes-031, the verified archive note re...
  2. score=1.253891 chunk_id=21053 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
  3. score=1.103104 chunk_id=21008 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter? document short-glass-harbor-quay-winter-letter-081::short-...
  4. score=1.102074 chunk_id=20918 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
  5. score=1.085621 chunk_id=20685 preview=document short-glass-harbor-quay-audio-reel-021::short-fact-021: In document short-glass-harbor-quay-audio-reel-021, the verified archive note records tuning...
- Matched markers: saffron carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron carved shell comb.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 32 - short-fact-032
Question: Which fact in the winter letter shows what Iveta's older sister left near South Meadow arch?

Expected evidence:
- amber lantern
- older sister

Expected distractors:
- wrong willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.745381 chunk_id=20932 preview=Question anchor: Which fact in the winter letter shows what Iveta's older sister left near South Meadow arch? Case scope id: short-fact-032. Scoped answer su...
  2. score=41.745358 chunk_id=20933 preview=Question anchor: Which fact in the winter letter shows what Iveta's older sister left near South Meadow arch? document short-south-meadow-arch-winter-letter-...
  3. score=38.732393 chunk_id=20750 preview=document short-south-meadow-arch-winter-letter-032::short-fact-032: In document short-south-meadow-arch-winter-letter-032, the verified archive note records...
  4. score=1.855668 chunk_id=20978 preview=Question anchor: Which fact in the field recording shows what Raisa's twin sister left near South Meadow arch? document short-south-meadow-arch-field-recordi...
  5. score=1.849409 chunk_id=20744 preview=document short-south-meadow-arch-field-recording-062::short-fact-062: In document short-south-meadow-arch-field-recording-062, the verified archive note reco...
- Matched markers: amber lantern, older sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, older sister.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.485640 chunk_id=20932 preview=Question anchor: Which fact in the winter letter shows what Iveta's older sister left near South Meadow arch? Case scope id: short-fact-032. Scoped answer su...
  2. score=41.503584 chunk_id=20933 preview=Question anchor: Which fact in the winter letter shows what Iveta's older sister left near South Meadow arch? document short-south-meadow-arch-winter-letter-...
  3. score=38.465113 chunk_id=20750 preview=document short-south-meadow-arch-winter-letter-032::short-fact-032: In document short-south-meadow-arch-winter-letter-032, the verified archive note records...
  4. score=1.642042 chunk_id=20978 preview=Question anchor: Which fact in the field recording shows what Raisa's twin sister left near South Meadow arch? document short-south-meadow-arch-field-recordi...
  5. score=1.377041 chunk_id=20751 preview=document short-south-meadow-arch-winter-letter-102::short-fact-102: In document short-south-meadow-arch-winter-letter-102, the verified archive note records...
- Matched markers: amber lantern, older sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, older sister.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 33 - short-fact-033
Question: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript?

Expected evidence:
- basalt sketch
- Hollow Market arcade
- station transcript

Expected distractors:
- wrong paper moon mask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.314822 chunk_id=20934 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? Case scope id: short-fact-033. Scoped answer summar...
  2. score=53.321605 chunk_id=20935 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
  3. score=53.312976 chunk_id=20936 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
  4. score=50.305118 chunk_id=20704 preview=document short-hollow-market-arcade-station-transcript-033::short-fact-033: In document short-hollow-market-arcade-station-transcript-033, the verified archi...
  5. score=13.764016 chunk_id=21026 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
- Matched markers: Hollow Market arcade, basalt sketch, station transcript
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Hollow Market arcade, basalt sketch, station transcript.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.056827 chunk_id=20934 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? Case scope id: short-fact-033. Scoped answer summar...
  2. score=53.076105 chunk_id=20936 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
  3. score=53.059568 chunk_id=20935 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
  4. score=49.997859 chunk_id=20704 preview=document short-hollow-market-arcade-station-transcript-033::short-fact-033: In document short-hollow-market-arcade-station-transcript-033, the verified archi...
  5. score=13.492861 chunk_id=20980 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel? document short-hollow-market-arcade-audio-reel-063::short-...
- Matched markers: Hollow Market arcade, basalt sketch, station transcript
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Hollow Market arcade, basalt sketch, station transcript.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 34 - short-fact-034
Question: Which small object in the cedar tube proved that Nessa stopped at Winter Chapel porch?

Expected evidence:
- green apron
- Winter Chapel porch

Expected distractors:
- wrong glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.162729 chunk_id=20937 preview=Question anchor: Which small object in the cedar tube proved that Nessa stopped at Winter Chapel porch? Case scope id: short-fact-034. Scoped answer summary...
  2. score=41.206006 chunk_id=20938 preview=Question anchor: Which small object in the cedar tube proved that Nessa stopped at Winter Chapel porch? document short-winter-chapel-porch-field-recording-03...
  3. score=14.073194 chunk_id=20983 preview=Question anchor: Which small object in the cedar tube proved that Sonya stopped at Winter Chapel porch? document short-winter-chapel-porch-profile-page-064::...
  4. score=5.424453 chunk_id=20754 preview=document short-winter-chapel-porch-festival-minutes-024::short-fact-024: In document short-winter-chapel-porch-festival-minutes-024, the verified archive not...
- Matched markers: Winter Chapel porch, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Winter Chapel porch, green apron.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.106640 chunk_id=20937 preview=Question anchor: Which small object in the cedar tube proved that Nessa stopped at Winter Chapel porch? Case scope id: short-fact-034. Scoped answer summary...
  2. score=41.125666 chunk_id=20938 preview=Question anchor: Which small object in the cedar tube proved that Nessa stopped at Winter Chapel porch? document short-winter-chapel-porch-field-recording-03...
  3. score=38.058429 chunk_id=20756 preview=document short-winter-chapel-porch-field-recording-034::short-fact-034: In document short-winter-chapel-porch-field-recording-034, the verified archive note...
  4. score=13.957020 chunk_id=20983 preview=Question anchor: Which small object in the cedar tube proved that Sonya stopped at Winter Chapel porch? document short-winter-chapel-porch-profile-page-064::...
  5. score=13.898744 chunk_id=20758 preview=document short-winter-chapel-porch-profile-page-064::short-fact-064: In document short-winter-chapel-porch-profile-page-064, the verified archive note record...
- Matched markers: Winter Chapel porch, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Winter Chapel porch, green apron.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 35 - short-fact-035
Question: Which direct fact from the audio reel identifies the item recorded for Anton at Driftwood cove?

Expected evidence:
- silver booth token

Expected distractors:
- wrong copper wind vane pin

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.394427 chunk_id=20674 preview=document short-driftwood-cove-audio-reel-035::short-fact-035: In document short-driftwood-cove-audio-reel-035, the verified archive note records silver booth...
  2. score=1.688877 chunk_id=20707 preview=document short-moss-archive-room-audio-reel-077::short-fact-077: In document short-moss-archive-room-audio-reel-077, the verified archive note records tin ke...
  3. score=1.400791 chunk_id=20715 preview=document short-moss-archive-room-station-transcript-047::short-fact-047: In document short-moss-archive-room-station-transcript-047, the verified archive not...
  4. score=1.321289 chunk_id=21044 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel? document short-driftwood-cove-audio-reel-105::short-fact-105: In...
  5. score=1.304287 chunk_id=20675 preview=document short-driftwood-cove-audio-reel-105::short-fact-105: In document short-driftwood-cove-audio-reel-105, the verified archive note records star ledger...
- Matched markers: silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: silver booth token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=1.242724 chunk_id=21044 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel? document short-driftwood-cove-audio-reel-105::short-fact-105: In...
  2. score=1.206840 chunk_id=20675 preview=document short-driftwood-cove-audio-reel-105::short-fact-105: In document short-driftwood-cove-audio-reel-105, the verified archive note records star ledger...
  3. score=1.130034 chunk_id=20999 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
  4. score=1.089700 chunk_id=20682 preview=document short-driftwood-cove-station-transcript-075::short-fact-075: In document short-driftwood-cove-station-transcript-075, the verified archive note reco...
  5. score=1.061576 chunk_id=20998 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
- Matched markers: none
- Missing markers: silver booth token
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 36 - short-fact-036
Question: Which item did Zora tuck inside the cedar tube mentioned in the profile page?

Expected evidence:
- clay watering cup
- cedar tube

Expected distractors:
- wrong coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=10.085790 chunk_id=20657 preview=document short-bell-bridge-square-profile-page-120::short-fact-120: In document short-bell-bridge-square-profile-page-120, the verified archive note records...
  2. score=10.080677 chunk_id=21066 preview=Question anchor: Which item did Mira tuck inside the cedar tube mentioned in the profile page? document short-bell-bridge-square-profile-page-120::short-fact...
  3. score=10.064527 chunk_id=20724 preview=document short-north-bell-workshop-profile-page-078::short-fact-078: In document short-north-bell-workshop-profile-page-078, the verified archive note record...
  4. score=10.057475 chunk_id=21003 preview=Question anchor: Which item did Ilia tuck inside the cedar tube mentioned in the profile page? document short-north-bell-workshop-profile-page-078::short-fac...
- Matched markers: cedar tube
- Missing markers: clay watering cup
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: cedar tube. Missing: clay watering cup.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.933793 chunk_id=20939 preview=Question anchor: Which item did Zora tuck inside the cedar tube mentioned in the profile page? Case scope id: short-fact-036. Scoped answer summary for short...
  2. score=40.944767 chunk_id=20940 preview=Question anchor: Which item did Zora tuck inside the cedar tube mentioned in the profile page? document short-cloud-wharf-office-profile-page-036::short-fact...
  3. score=37.906481 chunk_id=20666 preview=document short-cloud-wharf-office-profile-page-036::short-fact-036: In document short-cloud-wharf-office-profile-page-036, the verified archive note records...
  4. score=9.776101 chunk_id=21066 preview=Question anchor: Which item did Mira tuck inside the cedar tube mentioned in the profile page? document short-bell-bridge-square-profile-page-120::short-fact...
  5. score=9.749303 chunk_id=21003 preview=Question anchor: Which item did Ilia tuck inside the cedar tube mentioned in the profile page? document short-north-bell-workshop-profile-page-078::short-fac...
- Matched markers: cedar tube, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, clay watering cup.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 37 - short-fact-037
Question: What object and color detail identified Milan's keepsake at Moss Archive room?

Expected evidence:
- saffron juniper bundles

Expected distractors:
- wrong violet ribbon

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=0.450376 chunk_id=20722 preview=document short-north-bell-workshop-field-recording-048::short-fact-048: In document short-north-bell-workshop-field-recording-048, the verified archive note...
  2. score=0.450376 chunk_id=20662 preview=document short-bell-bridge-square-winter-letter-060::short-fact-060: In document short-bell-bridge-square-winter-letter-060, the verified archive note record...
- Matched markers: none
- Missing markers: saffron juniper bundles
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.736449 chunk_id=20713 preview=document short-moss-archive-room-river-diary-page-037::short-fact-037: In document short-moss-archive-room-river-diary-page-037, the verified archive note re...
  2. score=1.139258 chunk_id=21062 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Milan's station transcript? document short-moss-archive-room-station-transcript-1...
  3. score=0.991801 chunk_id=20927 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
  4. score=0.968449 chunk_id=20710 preview=document short-moss-archive-room-field-recording-027::short-fact-027: In document short-moss-archive-room-field-recording-027, the verified archive note reco...
  5. score=0.967446 chunk_id=20926 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
- Matched markers: saffron juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron juniper bundles.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 38 - short-fact-038
Question: Which fact in the festival minutes shows what Ilia's twin sister left near North Bell workshop?

Expected evidence:
- smoke vent chain
- twin sister

Expected distractors:
- wrong tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.452399 chunk_id=20941 preview=Question anchor: Which fact in the festival minutes shows what Ilia's twin sister left near North Bell workshop? Case scope id: short-fact-038. Scoped answer...
  2. score=41.419677 chunk_id=20942 preview=Question anchor: Which fact in the festival minutes shows what Ilia's twin sister left near North Bell workshop? document short-north-bell-workshop-festival-...
  3. score=38.403388 chunk_id=20720 preview=document short-north-bell-workshop-festival-minutes-038::short-fact-038: In document short-north-bell-workshop-festival-minutes-038, the verified archive not...
  4. score=1.672192 chunk_id=21005 preview=Question anchor: Which fact in the festival minutes shows what Mira's older sister left near Bell Bridge square? document short-bell-bridge-square-festival-m...
- Matched markers: smoke vent chain, twin sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: smoke vent chain, twin sister.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.570569 chunk_id=20941 preview=Question anchor: Which fact in the festival minutes shows what Ilia's twin sister left near North Bell workshop? Case scope id: short-fact-038. Scoped answer...
  2. score=41.594002 chunk_id=20942 preview=Question anchor: Which fact in the festival minutes shows what Ilia's twin sister left near North Bell workshop? document short-north-bell-workshop-festival-...
  3. score=38.553694 chunk_id=20720 preview=document short-north-bell-workshop-festival-minutes-038::short-fact-038: In document short-north-bell-workshop-festival-minutes-038, the verified archive not...
  4. score=1.477007 chunk_id=20721 preview=document short-north-bell-workshop-festival-minutes-108::short-fact-108: In document short-north-bell-workshop-festival-minutes-108, the verified archive not...
  5. score=1.307200 chunk_id=20723 preview=document short-north-bell-workshop-field-recording-118::short-fact-118: In document short-north-bell-workshop-field-recording-118, the verified archive note...
- Matched markers: smoke vent chain, twin sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: smoke vent chain, twin sister.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (1 vs 2).

### Question 39 - short-fact-039
Question: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter?

Expected evidence:
- brass compass
- Snow Orchard storehouse
- winter letter

Expected distractors:
- wrong rope bridge permit

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.261093 chunk_id=20943 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter? Case scope id: short-fact-039. Scoped answer summary...
  2. score=53.263861 chunk_id=20945 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter? document short-snow-orchard-storehouse-winter-letter...
  3. score=53.239923 chunk_id=20944 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter? document short-snow-orchard-storehouse-winter-letter...
  4. score=50.249269 chunk_id=20739 preview=document short-snow-orchard-storehouse-winter-letter-039::short-fact-039: In document short-snow-orchard-storehouse-winter-letter-039, the verified archive n...
  5. score=13.648489 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
- Matched markers: Snow Orchard storehouse, brass compass, winter letter
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Snow Orchard storehouse, brass compass, winter letter.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.198352 chunk_id=20943 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter? Case scope id: short-fact-039. Scoped answer summary...
  2. score=53.219401 chunk_id=20945 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter? document short-snow-orchard-storehouse-winter-letter...
  3. score=53.202124 chunk_id=20944 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter? document short-snow-orchard-storehouse-winter-letter...
  4. score=50.173537 chunk_id=20739 preview=document short-snow-orchard-storehouse-winter-letter-039::short-fact-039: In document short-snow-orchard-storehouse-winter-letter-039, the verified archive n...
  5. score=13.555423 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
- Matched markers: Snow Orchard storehouse, brass compass, winter letter
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Snow Orchard storehouse, brass compass, winter letter.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 40 - short-fact-040
Question: Which small object in the cedar tube proved that Mira stopped at Bell Bridge square?

Expected evidence:
- linen wick
- Bell Bridge square

Expected distractors:
- wrong oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=41.177121 chunk_id=20947 preview=Question anchor: Which small object in the cedar tube proved that Mira stopped at Bell Bridge square? document short-bell-bridge-square-station-transcript-04...
  2. score=14.110007 chunk_id=20902 preview=Question anchor: Which small object in the cedar tube proved that Lina stopped at Bell Bridge square? document short-bell-bridge-square-festival-minutes-010:...
  3. score=5.595141 chunk_id=20657 preview=document short-bell-bridge-square-profile-page-120::short-fact-120: In document short-bell-bridge-square-profile-page-120, the verified archive note records...
  4. score=5.424453 chunk_id=20662 preview=document short-bell-bridge-square-winter-letter-060::short-fact-060: In document short-bell-bridge-square-winter-letter-060, the verified archive note record...
- Matched markers: Bell Bridge square, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bell Bridge square, linen wick.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.093353 chunk_id=20946 preview=Question anchor: Which small object in the cedar tube proved that Mira stopped at Bell Bridge square? Case scope id: short-fact-040. Scoped answer summary fo...
  2. score=41.107014 chunk_id=20947 preview=Question anchor: Which small object in the cedar tube proved that Mira stopped at Bell Bridge square? document short-bell-bridge-square-station-transcript-04...
  3. score=38.047153 chunk_id=20660 preview=document short-bell-bridge-square-station-transcript-040::short-fact-040: In document short-bell-bridge-square-station-transcript-040, the verified archive n...
  4. score=13.872303 chunk_id=20902 preview=Question anchor: Which small object in the cedar tube proved that Lina stopped at Bell Bridge square? document short-bell-bridge-square-festival-minutes-010:...
  5. score=13.866900 chunk_id=20992 preview=Question anchor: Which small object in the cedar tube proved that Selma stopped at Bell Bridge square? document short-bell-bridge-square-audio-reel-070::shor...
- Matched markers: Bell Bridge square, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bell Bridge square, linen wick.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 41 - short-fact-041
Question: Which direct fact from the field recording identifies the item recorded for Tomas at Glass Harbor quay?

Expected evidence:
- star ledger page

Expected distractors:
- wrong blue glass jar

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.299955 chunk_id=20689 preview=document short-glass-harbor-quay-field-recording-041::short-fact-041: In document short-glass-harbor-quay-field-recording-041, the verified archive note reco...
  2. score=1.888063 chunk_id=20694 preview=document short-glass-harbor-quay-winter-letter-011::short-fact-011: In document short-glass-harbor-quay-winter-letter-011, the verified archive note records...
  3. score=1.502038 chunk_id=20690 preview=document short-glass-harbor-quay-field-recording-111::short-fact-111: In document short-glass-harbor-quay-field-recording-111, the verified archive note reco...
  4. score=1.487880 chunk_id=21053 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
  5. score=1.344089 chunk_id=20715 preview=document short-moss-archive-room-station-transcript-047::short-fact-047: In document short-moss-archive-room-station-transcript-047, the verified archive not...
- Matched markers: star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: star ledger page.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=1.525202 chunk_id=21053 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
  2. score=1.503877 chunk_id=20690 preview=document short-glass-harbor-quay-field-recording-111::short-fact-111: In document short-glass-harbor-quay-field-recording-111, the verified archive note reco...
  3. score=1.349813 chunk_id=21008 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter? document short-glass-harbor-quay-winter-letter-081::short-...
  4. score=1.250033 chunk_id=20918 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
  5. score=1.239021 chunk_id=20685 preview=document short-glass-harbor-quay-audio-reel-021::short-fact-021: In document short-glass-harbor-quay-audio-reel-021, the verified archive note records tuning...
- Matched markers: none
- Missing markers: star ledger page
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 42 - short-fact-042
Question: Which item did Elena tuck inside the cedar tube mentioned in the audio reel?

Expected evidence:
- lantern hook
- cedar tube

Expected distractors:
- wrong canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.170602 chunk_id=20948 preview=Question anchor: Which item did Elena tuck inside the cedar tube mentioned in the audio reel? Case scope id: short-fact-042. Scoped answer summary for short-...
  2. score=41.202527 chunk_id=20949 preview=Question anchor: Which item did Elena tuck inside the cedar tube mentioned in the audio reel? document short-south-meadow-arch-audio-reel-042::short-fact-042...
  3. score=38.118984 chunk_id=20741 preview=document short-south-meadow-arch-audio-reel-042::short-fact-042: In document short-south-meadow-arch-audio-reel-042, the verified archive note records lanter...
  4. score=9.954564 chunk_id=21012 preview=Question anchor: Which item did Vera tuck inside the cedar tube mentioned in the audio reel? document short-winter-chapel-porch-audio-reel-084::short-fact-08...
  5. score=9.942157 chunk_id=20753 preview=document short-winter-chapel-porch-audio-reel-084::short-fact-084: In document short-winter-chapel-porch-audio-reel-084, the verified archive note records vi...
- Matched markers: cedar tube, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.896295 chunk_id=20948 preview=Question anchor: Which item did Elena tuck inside the cedar tube mentioned in the audio reel? Case scope id: short-fact-042. Scoped answer summary for short-...
  2. score=40.919409 chunk_id=20949 preview=Question anchor: Which item did Elena tuck inside the cedar tube mentioned in the audio reel? document short-south-meadow-arch-audio-reel-042::short-fact-042...
  3. score=37.823423 chunk_id=20741 preview=document short-south-meadow-arch-audio-reel-042::short-fact-042: In document short-south-meadow-arch-audio-reel-042, the verified archive note records lanter...
  4. score=9.655788 chunk_id=21012 preview=Question anchor: Which item did Vera tuck inside the cedar tube mentioned in the audio reel? document short-winter-chapel-porch-audio-reel-084::short-fact-08...
  5. score=9.376183 chunk_id=21021 preview=Question anchor: Which item did Lina tuck inside the cedar tube mentioned in the field recording? document short-bell-bridge-square-field-recording-090::shor...
- Matched markers: cedar tube, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, lantern hook.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 43 - short-fact-043
Question: What object and color detail identified Radin's keepsake at Hollow Market arcade?

Expected evidence:
- saffron weathered camera strap

Expected distractors:
- wrong cedar shovel

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.929239 chunk_id=20700 preview=document short-hollow-market-arcade-profile-page-043::short-fact-043: In document short-hollow-market-arcade-profile-page-043, the verified archive note reco...
  2. score=1.766947 chunk_id=20698 preview=document short-hollow-market-arcade-field-recording-013::short-fact-013: In document short-hollow-market-arcade-field-recording-013, the verified archive not...
  3. score=1.211544 chunk_id=20936 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
  4. score=1.209868 chunk_id=20704 preview=document short-hollow-market-arcade-station-transcript-033::short-fact-033: In document short-hollow-market-arcade-station-transcript-033, the verified archi...
  5. score=1.172910 chunk_id=21026 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
- Matched markers: saffron weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.660207 chunk_id=20700 preview=document short-hollow-market-arcade-profile-page-043::short-fact-043: In document short-hollow-market-arcade-profile-page-043, the verified archive note reco...
  2. score=1.520256 chunk_id=20698 preview=document short-hollow-market-arcade-field-recording-013::short-fact-013: In document short-hollow-market-arcade-field-recording-013, the verified archive not...
  3. score=1.473879 chunk_id=20705 preview=document short-hollow-market-arcade-station-transcript-103::short-fact-103: In document short-hollow-market-arcade-station-transcript-103, the verified archi...
  4. score=1.429200 chunk_id=20697 preview=document short-hollow-market-arcade-festival-minutes-073::short-fact-073: In document short-hollow-market-arcade-festival-minutes-073, the verified archive n...
  5. score=0.832571 chunk_id=20981 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel? document short-hollow-market-arcade-audio-reel-063::short-...
- Matched markers: saffron weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron weathered camera strap.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 44 - short-fact-044
Question: Which fact in the river diary page shows what Vera's stepfather left near Winter Chapel porch?

Expected evidence:
- wax thread
- stepfather

Expected distractors:
- wrong copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.616326 chunk_id=20950 preview=Question anchor: Which fact in the river diary page shows what Vera's stepfather left near Winter Chapel porch? Case scope id: short-fact-044. Scoped answer...
  2. score=41.617275 chunk_id=20951 preview=Question anchor: Which fact in the river diary page shows what Vera's stepfather left near Winter Chapel porch? document short-winter-chapel-porch-river-diar...
  3. score=38.614191 chunk_id=20759 preview=document short-winter-chapel-porch-river-diary-page-044::short-fact-044: In document short-winter-chapel-porch-river-diary-page-044, the verified archive not...
  4. score=1.640937 chunk_id=20906 preview=Question anchor: Which fact in the audio reel shows what Daria's twin sister left near Winter Chapel porch? document short-winter-chapel-porch-audio-reel-014...
- Matched markers: stepfather, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: stepfather, wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.534239 chunk_id=20950 preview=Question anchor: Which fact in the river diary page shows what Vera's stepfather left near Winter Chapel porch? Case scope id: short-fact-044. Scoped answer...
  2. score=41.562760 chunk_id=20951 preview=Question anchor: Which fact in the river diary page shows what Vera's stepfather left near Winter Chapel porch? document short-winter-chapel-porch-river-diar...
  3. score=38.514045 chunk_id=20759 preview=document short-winter-chapel-porch-river-diary-page-044::short-fact-044: In document short-winter-chapel-porch-river-diary-page-044, the verified archive not...
  4. score=1.456237 chunk_id=20760 preview=document short-winter-chapel-porch-river-diary-page-114::short-fact-114: In document short-winter-chapel-porch-river-diary-page-114, the verified archive not...
  5. score=0.979939 chunk_id=20703 preview=document short-hollow-market-arcade-river-diary-page-093::short-fact-093: In document short-hollow-market-arcade-river-diary-page-093, the verified archive n...
- Matched markers: stepfather, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: stepfather, wax thread.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (1 vs 2).

### Question 45 - short-fact-045
Question: What exact keepsake was listed beside Driftwood cove in Ilya's festival minutes?

Expected evidence:
- tin key
- Driftwood cove
- festival minutes

Expected distractors:
- wrong moonflower cutting

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.135825 chunk_id=20952 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Ilya's festival minutes? Case scope id: short-fact-045. Scoped answer summary for sh...
  2. score=53.147724 chunk_id=20953 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Ilya's festival minutes? document short-driftwood-cove-festival-minutes-045::short-f...
  3. score=53.138811 chunk_id=20954 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Ilya's festival minutes? document short-driftwood-cove-festival-minutes-045::short-f...
  4. score=50.137008 chunk_id=20676 preview=document short-driftwood-cove-festival-minutes-045::short-fact-045: In document short-driftwood-cove-festival-minutes-045, the verified archive note records...
  5. score=13.485795 chunk_id=20998 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
- Matched markers: Driftwood cove, festival minutes, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Driftwood cove, festival minutes, tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.088831 chunk_id=20952 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Ilya's festival minutes? Case scope id: short-fact-045. Scoped answer summary for sh...
  2. score=53.103098 chunk_id=20953 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Ilya's festival minutes? document short-driftwood-cove-festival-minutes-045::short-f...
  3. score=53.094297 chunk_id=20954 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Ilya's festival minutes? document short-driftwood-cove-festival-minutes-045::short-f...
  4. score=50.062741 chunk_id=20676 preview=document short-driftwood-cove-festival-minutes-045::short-fact-045: In document short-driftwood-cove-festival-minutes-045, the verified archive note records...
  5. score=13.382081 chunk_id=21044 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel? document short-driftwood-cove-audio-reel-105::short-fact-105: In...
- Matched markers: Driftwood cove, festival minutes, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Driftwood cove, festival minutes, tin key.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 46 - short-fact-046
Question: Which small object in the cedar tube proved that Kira stopped at Cloud Wharf office?

Expected evidence:
- blue oar
- Cloud Wharf office

Expected distractors:
- wrong birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=41.288306 chunk_id=20956 preview=Question anchor: Which small object in the cedar tube proved that Kira stopped at Cloud Wharf office? document short-cloud-wharf-office-winter-letter-046::sh...
  2. score=14.136549 chunk_id=21046 preview=Question anchor: Which small object in the cedar tube proved that Talia stopped at Cloud Wharf office? document short-cloud-wharf-office-profile-page-106::sh...
  3. score=5.558638 chunk_id=20671 preview=document short-cloud-wharf-office-station-transcript-096::short-fact-096: In document short-cloud-wharf-office-station-transcript-096, the verified archive n...
  4. score=5.551756 chunk_id=20664 preview=document short-cloud-wharf-office-festival-minutes-066::short-fact-066: In document short-cloud-wharf-office-festival-minutes-066, the verified archive note...
- Matched markers: Cloud Wharf office, blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, blue oar.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.101594 chunk_id=20955 preview=Question anchor: Which small object in the cedar tube proved that Kira stopped at Cloud Wharf office? Case scope id: short-fact-046. Scoped answer summary fo...
  2. score=41.105910 chunk_id=20956 preview=Question anchor: Which small object in the cedar tube proved that Kira stopped at Cloud Wharf office? document short-cloud-wharf-office-winter-letter-046::sh...
  3. score=13.949042 chunk_id=21001 preview=Question anchor: Which small object in the cedar tube proved that Zora stopped at Cloud Wharf office? document short-cloud-wharf-office-field-recording-076::...
  4. score=13.928048 chunk_id=21046 preview=Question anchor: Which small object in the cedar tube proved that Talia stopped at Cloud Wharf office? document short-cloud-wharf-office-profile-page-106::sh...
- Matched markers: Cloud Wharf office, blue oar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, blue oar.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 47 - short-fact-047
Question: Which direct fact from the station transcript identifies the item recorded for Soren at Moss Archive room?

Expected evidence:
- willow basket

Expected distractors:
- wrong saffron scarf

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.490168 chunk_id=20715 preview=document short-moss-archive-room-station-transcript-047::short-fact-047: In document short-moss-archive-room-station-transcript-047, the verified archive not...
  2. score=4.712479 chunk_id=20650 preview=document river-mill-inventory::short-fact-river-mill-basket: In document river-mill-inventory, the verified archive note records willow basket, flour chalk m...
  3. score=1.694872 chunk_id=20707 preview=document short-moss-archive-room-audio-reel-077::short-fact-077: In document short-moss-archive-room-audio-reel-077, the verified archive note records tin ke...
  4. score=1.675831 chunk_id=20708 preview=document short-moss-archive-room-festival-minutes-017::short-fact-017: In document short-moss-archive-room-festival-minutes-017, the verified archive note re...
  5. score=1.394872 chunk_id=20674 preview=document short-driftwood-cove-audio-reel-035::short-fact-035: In document short-driftwood-cove-audio-reel-035, the verified archive note records silver booth...
- Matched markers: willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.156532 chunk_id=20715 preview=document short-moss-archive-room-station-transcript-047::short-fact-047: In document short-moss-archive-room-station-transcript-047, the verified archive not...
  2. score=1.506977 chunk_id=21062 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Milan's station transcript? document short-moss-archive-room-station-transcript-1...
  3. score=1.503107 chunk_id=20716 preview=document short-moss-archive-room-station-transcript-117::short-fact-117: In document short-moss-archive-room-station-transcript-117, the verified archive not...
  4. score=1.461098 chunk_id=21061 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Milan's station transcript? document short-moss-archive-room-station-transcript-1...
  5. score=1.120185 chunk_id=20927 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
- Matched markers: willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: willow basket.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (3 vs 4).

### Question 48 - short-fact-048
Question: Which item did Nadia tuck inside the cedar tube mentioned in the field recording?

Expected evidence:
- paper moon mask
- cedar tube

Expected distractors:
- wrong carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.213653 chunk_id=20957 preview=Question anchor: Which item did Nadia tuck inside the cedar tube mentioned in the field recording? Case scope id: short-fact-048. Scoped answer summary for s...
  2. score=41.197863 chunk_id=20958 preview=Question anchor: Which item did Nadia tuck inside the cedar tube mentioned in the field recording? document short-north-bell-workshop-field-recording-048::sh...
  3. score=38.207992 chunk_id=20722 preview=document short-north-bell-workshop-field-recording-048::short-fact-048: In document short-north-bell-workshop-field-recording-048, the verified archive note...
  4. score=10.007376 chunk_id=21021 preview=Question anchor: Which item did Lina tuck inside the cedar tube mentioned in the field recording? document short-bell-bridge-square-field-recording-090::shor...
  5. score=9.996500 chunk_id=20655 preview=document short-bell-bridge-square-field-recording-090::short-fact-090: In document short-bell-bridge-square-field-recording-090, the verified archive note re...
- Matched markers: cedar tube, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, paper moon mask.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=13.405953 chunk_id=21048 preview=Question anchor: Which item did Runa tuck inside the cedar tube mentioned in the festival minutes? document short-north-bell-workshop-festival-minutes-108::s...
  2. score=9.700391 chunk_id=21021 preview=Question anchor: Which item did Lina tuck inside the cedar tube mentioned in the field recording? document short-bell-bridge-square-field-recording-090::shor...
  3. score=9.409966 chunk_id=20985 preview=Question anchor: Which item did Talia tuck inside the cedar tube mentioned in the festival minutes? document short-cloud-wharf-office-festival-minutes-066::s...
  4. score=9.404385 chunk_id=20922 preview=Question anchor: Which item did Sonya tuck inside the cedar tube mentioned in the festival minutes? document short-winter-chapel-porch-festival-minutes-024::...
  5. score=9.396731 chunk_id=21012 preview=Question anchor: Which item did Vera tuck inside the cedar tube mentioned in the audio reel? document short-winter-chapel-porch-audio-reel-084::short-fact-08...
- Matched markers: cedar tube
- Missing markers: paper moon mask
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: cedar tube. Missing: paper moon mask.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 49 - short-fact-049
Question: What object and color detail identified Petar's keepsake at Snow Orchard storehouse?

Expected evidence:
- saffron glass ink bottle

Expected distractors:
- wrong amber lantern

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.819237 chunk_id=20729 preview=document short-snow-orchard-storehouse-audio-reel-049::short-fact-049: In document short-snow-orchard-storehouse-audio-reel-049, the verified archive note re...
  2. score=1.744581 chunk_id=20736 preview=document short-snow-orchard-storehouse-river-diary-page-079::short-fact-079: In document short-snow-orchard-storehouse-river-diary-page-079, the verified arc...
  3. score=1.220566 chunk_id=20900 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Petar's river diary page? document short-snow-orchard-storehouse-river-diar...
  4. score=1.083368 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  5. score=1.076017 chunk_id=20732 preview=document short-snow-orchard-storehouse-field-recording-069::short-fact-069: In document short-snow-orchard-storehouse-field-recording-069, the verified archi...
- Matched markers: saffron glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron glass ink bottle.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.757434 chunk_id=20729 preview=document short-snow-orchard-storehouse-audio-reel-049::short-fact-049: In document short-snow-orchard-storehouse-audio-reel-049, the verified archive note re...
  2. score=1.583844 chunk_id=20740 preview=document short-snow-orchard-storehouse-winter-letter-109::short-fact-109: In document short-snow-orchard-storehouse-winter-letter-109, the verified archive n...
  3. score=1.575370 chunk_id=20737 preview=document short-snow-orchard-storehouse-station-transcript-019::short-fact-019: In document short-snow-orchard-storehouse-station-transcript-019, the verified...
  4. score=0.997950 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  5. score=0.964896 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
- Matched markers: saffron glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron glass ink bottle.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 50 - short-fact-050
Question: Which fact in the profile page shows what Lina's cousin left near Bell Bridge square?

Expected evidence:
- copper wind vane pin
- cousin

Expected distractors:
- wrong basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.359795 chunk_id=20959 preview=Question anchor: Which fact in the profile page shows what Lina's cousin left near Bell Bridge square? Case scope id: short-fact-050. Scoped answer summary f...
  2. score=41.348233 chunk_id=20960 preview=Question anchor: Which fact in the profile page shows what Lina's cousin left near Bell Bridge square? document short-bell-bridge-square-profile-page-050::sh...
  3. score=38.348068 chunk_id=20656 preview=document short-bell-bridge-square-profile-page-050::short-fact-050: In document short-bell-bridge-square-profile-page-050, the verified archive note records...
  4. score=1.668244 chunk_id=21050 preview=Question anchor: Which fact in the station transcript shows what Selma's twin sister left near Bell Bridge square? document short-bell-bridge-square-station-...
  5. score=1.633717 chunk_id=20661 preview=document short-bell-bridge-square-station-transcript-110::short-fact-110: In document short-bell-bridge-square-station-transcript-110, the verified archive n...
- Matched markers: copper wind vane pin, cousin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper wind vane pin, cousin.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.270885 chunk_id=20959 preview=Question anchor: Which fact in the profile page shows what Lina's cousin left near Bell Bridge square? Case scope id: short-fact-050. Scoped answer summary f...
  2. score=41.283798 chunk_id=20960 preview=Question anchor: Which fact in the profile page shows what Lina's cousin left near Bell Bridge square? document short-bell-bridge-square-profile-page-050::sh...
  3. score=38.261704 chunk_id=20656 preview=document short-bell-bridge-square-profile-page-050::short-fact-050: In document short-bell-bridge-square-profile-page-050, the verified archive note records...
  4. score=1.257176 chunk_id=20657 preview=document short-bell-bridge-square-profile-page-120::short-fact-120: In document short-bell-bridge-square-profile-page-120, the verified archive note records...
  5. score=1.134656 chunk_id=20659 preview=document short-bell-bridge-square-river-diary-page-100::short-fact-100: In document short-bell-bridge-square-river-diary-page-100, the verified archive note...
- Matched markers: copper wind vane pin, cousin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper wind vane pin, cousin.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 51 - short-fact-051
Question: What exact keepsake was listed beside Glass Harbor quay in Boris's river diary page?

Expected evidence:
- coal stove hiss
- Glass Harbor quay
- river diary page

Expected distractors:
- wrong green apron

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.354429 chunk_id=20961 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Boris's river diary page? Case scope id: short-fact-051. Scoped answer summary fo...
  2. score=53.364962 chunk_id=20963 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Boris's river diary page? document short-glass-harbor-quay-river-diary-page-051::...
  3. score=53.341455 chunk_id=20962 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Boris's river diary page? document short-glass-harbor-quay-river-diary-page-051::...
  4. score=50.338796 chunk_id=20692 preview=document short-glass-harbor-quay-river-diary-page-051::short-fact-051: In document short-glass-harbor-quay-river-diary-page-051, the verified archive note re...
  5. score=13.552442 chunk_id=21052 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
- Matched markers: Glass Harbor quay, coal stove hiss, river diary page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Glass Harbor quay, coal stove hiss, river diary page.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.467606 chunk_id=20961 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Boris's river diary page? Case scope id: short-fact-051. Scoped answer summary fo...
  2. score=53.474977 chunk_id=20963 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Boris's river diary page? document short-glass-harbor-quay-river-diary-page-051::...
  3. score=53.461394 chunk_id=20962 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Boris's river diary page? document short-glass-harbor-quay-river-diary-page-051::...
  4. score=50.471025 chunk_id=20692 preview=document short-glass-harbor-quay-river-diary-page-051::short-fact-051: In document short-glass-harbor-quay-river-diary-page-051, the verified archive note re...
  5. score=13.655380 chunk_id=20917 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
- Matched markers: Glass Harbor quay, coal stove hiss, river diary page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Glass Harbor quay, coal stove hiss, river diary page.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 52 - short-fact-052
Question: Which small object in the cedar tube proved that Anya stopped at South Meadow arch?

Expected evidence:
- violet ribbon
- South Meadow arch

Expected distractors:
- wrong silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.245676 chunk_id=20964 preview=Question anchor: Which small object in the cedar tube proved that Anya stopped at South Meadow arch? Case scope id: short-fact-052. Scoped answer summary for...
  2. score=41.277680 chunk_id=20965 preview=Question anchor: Which small object in the cedar tube proved that Anya stopped at South Meadow arch? document short-south-meadow-arch-festival-minutes-052::s...
  3. score=5.740042 chunk_id=20748 preview=document short-south-meadow-arch-station-transcript-012::short-fact-012: In document short-south-meadow-arch-station-transcript-012, the verified archive not...
  4. score=5.670962 chunk_id=20904 preview=Question anchor: Which item did Anya tuck inside the cedar tube mentioned in the station transcript? document short-south-meadow-arch-station-transcript-012:...
  5. score=5.469195 chunk_id=20741 preview=document short-south-meadow-arch-audio-reel-042::short-fact-042: In document short-south-meadow-arch-audio-reel-042, the verified archive note records lanter...
- Matched markers: South Meadow arch, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: South Meadow arch, violet ribbon.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.117524 chunk_id=20964 preview=Question anchor: Which small object in the cedar tube proved that Anya stopped at South Meadow arch? Case scope id: short-fact-052. Scoped answer summary for...
  2. score=41.131554 chunk_id=20965 preview=Question anchor: Which small object in the cedar tube proved that Anya stopped at South Meadow arch? document short-south-meadow-arch-festival-minutes-052::s...
  3. score=38.082654 chunk_id=20743 preview=document short-south-meadow-arch-festival-minutes-052::short-fact-052: In document short-south-meadow-arch-festival-minutes-052, the verified archive note re...
  4. score=13.928747 chunk_id=21055 preview=Question anchor: Which small object in the cedar tube proved that Iveta stopped at South Meadow arch? document short-south-meadow-arch-audio-reel-112::short-...
- Matched markers: South Meadow arch, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: South Meadow arch, violet ribbon.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 53 - short-fact-053
Question: Which direct fact from the winter letter identifies the item recorded for Marek at Hollow Market arcade?

Expected evidence:
- tuning fork

Expected distractors:
- wrong clay watering cup

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.434464 chunk_id=20706 preview=document short-hollow-market-arcade-winter-letter-053::short-fact-053: In document short-hollow-market-arcade-winter-letter-053, the verified archive note re...
  2. score=1.806780 chunk_id=20702 preview=document short-hollow-market-arcade-river-diary-page-023::short-fact-023: In document short-hollow-market-arcade-river-diary-page-023, the verified archive n...
  3. score=1.368356 chunk_id=21026 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
  4. score=1.216050 chunk_id=20936 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
  5. score=1.212737 chunk_id=20704 preview=document short-hollow-market-arcade-station-transcript-033::short-fact-033: In document short-hollow-market-arcade-station-transcript-033, the verified archi...
- Matched markers: tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.149137 chunk_id=20706 preview=document short-hollow-market-arcade-winter-letter-053::short-fact-053: In document short-hollow-market-arcade-winter-letter-053, the verified archive note re...
  2. score=1.417785 chunk_id=20684 preview=document short-driftwood-cove-winter-letter-095::short-fact-095: In document short-driftwood-cove-winter-letter-095, the verified archive note records carved...
  3. score=0.806417 chunk_id=20762 preview=document short-winter-chapel-porch-winter-letter-074::short-fact-074: In document short-winter-chapel-porch-winter-letter-074, the verified archive note reco...
  4. score=0.799667 chunk_id=20739 preview=document short-snow-orchard-storehouse-winter-letter-039::short-fact-039: In document short-snow-orchard-storehouse-winter-letter-039, the verified archive n...
  5. score=0.785903 chunk_id=20695 preview=document short-glass-harbor-quay-winter-letter-081::short-fact-081: In document short-glass-harbor-quay-winter-letter-081, the verified archive note records...
- Matched markers: tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: tuning fork.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 54 - short-fact-054
Question: Which item did Daria tuck inside the cedar tube mentioned in the station transcript?

Expected evidence:
- rope bridge permit
- cedar tube

Expected distractors:
- wrong juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=9.708733 chunk_id=21021 preview=Question anchor: Which item did Lina tuck inside the cedar tube mentioned in the field recording? document short-bell-bridge-square-field-recording-090::shor...
  2. score=9.697834 chunk_id=20655 preview=document short-bell-bridge-square-field-recording-090::short-fact-090: In document short-bell-bridge-square-field-recording-090, the verified archive note re...
- Matched markers: cedar tube
- Missing markers: rope bridge permit
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: cedar tube. Missing: rope bridge permit.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.916979 chunk_id=20966 preview=Question anchor: Which item did Daria tuck inside the cedar tube mentioned in the station transcript? Case scope id: short-fact-054. Scoped answer summary fo...
  2. score=40.940086 chunk_id=20967 preview=Question anchor: Which item did Daria tuck inside the cedar tube mentioned in the station transcript? document short-winter-chapel-porch-station-transcript-0...
  3. score=37.863749 chunk_id=20761 preview=document short-winter-chapel-porch-station-transcript-054::short-fact-054: In document short-winter-chapel-porch-station-transcript-054, the verified archive...
  4. score=9.730811 chunk_id=20904 preview=Question anchor: Which item did Anya tuck inside the cedar tube mentioned in the station transcript? document short-south-meadow-arch-station-transcript-012:...
  5. score=9.716643 chunk_id=21030 preview=Question anchor: Which item did Yara tuck inside the cedar tube mentioned in the station transcript? document short-cloud-wharf-office-station-transcript-096...
- Matched markers: cedar tube, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, rope bridge permit.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 55 - short-fact-055
Question: What object and color detail identified Stefan's keepsake at Driftwood cove?

Expected evidence:
- saffron oak barrel hoops

Expected distractors:
- wrong smoke vent chain

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.690098 chunk_id=20678 preview=document short-driftwood-cove-field-recording-055::short-fact-055: In document short-driftwood-cove-field-recording-055, the verified archive note records sa...
  2. score=1.414900 chunk_id=20680 preview=document short-driftwood-cove-profile-page-085::short-fact-085: In document short-driftwood-cove-profile-page-085, the verified archive note records saffron...
  3. score=0.845577 chunk_id=20999 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
  4. score=0.831685 chunk_id=20682 preview=document short-driftwood-cove-station-transcript-075::short-fact-075: In document short-driftwood-cove-station-transcript-075, the verified archive note reco...
  5. score=0.816233 chunk_id=20954 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Ilya's festival minutes? document short-driftwood-cove-festival-minutes-045::short-f...
- Matched markers: saffron oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.640225 chunk_id=20678 preview=document short-driftwood-cove-field-recording-055::short-fact-055: In document short-driftwood-cove-field-recording-055, the verified archive note records sa...
  2. score=1.451292 chunk_id=20680 preview=document short-driftwood-cove-profile-page-085::short-fact-085: In document short-driftwood-cove-profile-page-085, the verified archive note records saffron...
  3. score=1.435609 chunk_id=20683 preview=document short-driftwood-cove-winter-letter-025::short-fact-025: In document short-driftwood-cove-winter-letter-025, the verified archive note records saffro...
  4. score=0.955374 chunk_id=20909 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Stefan's profile page? document short-driftwood-cove-profile-page-015::short-fact-01...
  5. score=0.829324 chunk_id=20999 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
- Matched markers: saffron oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron oak barrel hoops.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 56 - short-fact-056
Question: Which fact in the audio reel shows what Yara's older sister left near Cloud Wharf office?

Expected evidence:
- blue glass jar
- older sister

Expected distractors:
- wrong brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.645359 chunk_id=20968 preview=Question anchor: Which fact in the audio reel shows what Yara's older sister left near Cloud Wharf office? Case scope id: short-fact-056. Scoped answer summa...
  2. score=41.640602 chunk_id=20969 preview=Question anchor: Which fact in the audio reel shows what Yara's older sister left near Cloud Wharf office? document short-cloud-wharf-office-audio-reel-056::...
  3. score=38.626869 chunk_id=20663 preview=document short-cloud-wharf-office-audio-reel-056::short-fact-056: In document short-cloud-wharf-office-audio-reel-056, the verified archive note records blue...
  4. score=1.910429 chunk_id=21014 preview=Question anchor: Which fact in the river diary page shows what Kira's twin sister left near Cloud Wharf office? document short-cloud-wharf-office-river-diary...
  5. score=1.908583 chunk_id=20669 preview=document short-cloud-wharf-office-river-diary-page-086::short-fact-086: In document short-cloud-wharf-office-river-diary-page-086, the verified archive note...
- Matched markers: blue glass jar, older sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, older sister.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.436547 chunk_id=20968 preview=Question anchor: Which fact in the audio reel shows what Yara's older sister left near Cloud Wharf office? Case scope id: short-fact-056. Scoped answer summa...
  2. score=41.444931 chunk_id=20969 preview=Question anchor: Which fact in the audio reel shows what Yara's older sister left near Cloud Wharf office? document short-cloud-wharf-office-audio-reel-056::...
  3. score=38.396859 chunk_id=20663 preview=document short-cloud-wharf-office-audio-reel-056::short-fact-056: In document short-cloud-wharf-office-audio-reel-056, the verified archive note records blue...
  4. score=1.491105 chunk_id=20924 preview=Question anchor: Which fact in the station transcript shows what Talia's cousin left near Cloud Wharf office? document short-cloud-wharf-office-station-trans...
  5. score=0.996545 chunk_id=20665 preview=document short-cloud-wharf-office-field-recording-076::short-fact-076: In document short-cloud-wharf-office-field-recording-076, the verified archive note re...
- Matched markers: blue glass jar, older sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, older sister.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 57 - short-fact-057
Question: What exact keepsake was listed beside Moss Archive room in Oren's profile page?

Expected evidence:
- canal route map
- Moss Archive room
- profile page

Expected distractors:
- wrong linen wick

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.203011 chunk_id=20970 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Oren's profile page? Case scope id: short-fact-057. Scoped answer summary for sho...
  2. score=53.240440 chunk_id=20972 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Oren's profile page? document short-moss-archive-room-profile-page-057::short-fac...
  3. score=53.176768 chunk_id=20971 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Oren's profile page? document short-moss-archive-room-profile-page-057::short-fac...
  4. score=50.200978 chunk_id=20712 preview=document short-moss-archive-room-profile-page-057::short-fact-057: In document short-moss-archive-room-profile-page-057, the verified archive note records ca...
  5. score=9.688171 chunk_id=20908 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Stefan's profile page? document short-driftwood-cove-profile-page-015::short-fact-01...
- Matched markers: Moss Archive room, canal route map, profile page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moss Archive room, canal route map, profile page.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.221123 chunk_id=20970 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Oren's profile page? Case scope id: short-fact-057. Scoped answer summary for sho...
  2. score=53.239321 chunk_id=20971 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Oren's profile page? document short-moss-archive-room-profile-page-057::short-fac...
  3. score=53.232542 chunk_id=20972 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Oren's profile page? document short-moss-archive-room-profile-page-057::short-fac...
  4. score=50.193397 chunk_id=20712 preview=document short-moss-archive-room-profile-page-057::short-fact-057: In document short-moss-archive-room-profile-page-057, the verified archive note records ca...
  5. score=13.558955 chunk_id=20926 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
- Matched markers: Moss Archive room, canal route map, profile page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moss Archive room, canal route map, profile page.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 58 - short-fact-058
Question: Which small object in the cedar tube proved that Milena stopped at North Bell workshop?

Expected evidence:
- cedar shovel
- North Bell workshop

Expected distractors:
- wrong star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.106143 chunk_id=20973 preview=Question anchor: Which small object in the cedar tube proved that Milena stopped at North Bell workshop? Case scope id: short-fact-058. Scoped answer summary...
  2. score=41.138172 chunk_id=20974 preview=Question anchor: Which small object in the cedar tube proved that Milena stopped at North Bell workshop? document short-north-bell-workshop-river-diary-page-...
- Matched markers: North Bell workshop, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: North Bell workshop, cedar shovel.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.197387 chunk_id=20973 preview=Question anchor: Which small object in the cedar tube proved that Milena stopped at North Bell workshop? Case scope id: short-fact-058. Scoped answer summary...
  2. score=41.202184 chunk_id=20974 preview=Question anchor: Which small object in the cedar tube proved that Milena stopped at North Bell workshop? document short-north-bell-workshop-river-diary-page-...
  3. score=14.014896 chunk_id=21019 preview=Question anchor: Which small object in the cedar tube proved that Nadia stopped at North Bell workshop? document short-north-bell-workshop-winter-letter-088:...
  4. score=14.008194 chunk_id=20929 preview=Question anchor: Which small object in the cedar tube proved that Runa stopped at North Bell workshop? document short-north-bell-workshop-audio-reel-028::sho...
- Matched markers: North Bell workshop, cedar shovel
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: North Bell workshop, cedar shovel.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 59 - short-fact-059
Question: Which direct fact from the festival minutes identifies the item recorded for Lev at Snow Orchard storehouse?

Expected evidence:
- copper token

Expected distractors:
- wrong lantern hook

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.466497 chunk_id=20731 preview=document short-snow-orchard-storehouse-festival-minutes-059::short-fact-059: In document short-snow-orchard-storehouse-festival-minutes-059, the verified arc...
  2. score=1.789506 chunk_id=20730 preview=document short-snow-orchard-storehouse-audio-reel-119::short-fact-119: In document short-snow-orchard-storehouse-audio-reel-119, the verified archive note re...
  3. score=1.780319 chunk_id=20733 preview=document short-snow-orchard-storehouse-profile-page-029::short-fact-029: In document short-snow-orchard-storehouse-profile-page-029, the verified archive not...
  4. score=1.768711 chunk_id=20738 preview=document short-snow-orchard-storehouse-station-transcript-089::short-fact-089: In document short-snow-orchard-storehouse-station-transcript-089, the verified...
  5. score=1.652464 chunk_id=20688 preview=document short-glass-harbor-quay-festival-minutes-101::short-fact-101: In document short-glass-harbor-quay-festival-minutes-101, the verified archive note re...
- Matched markers: copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.305072 chunk_id=20731 preview=document short-snow-orchard-storehouse-festival-minutes-059::short-fact-059: In document short-snow-orchard-storehouse-festival-minutes-059, the verified arc...
  2. score=1.159652 chunk_id=21035 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? document short-snow-orchard-storehouse-profile-page-099...
  3. score=1.090399 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  4. score=1.053802 chunk_id=20732 preview=document short-snow-orchard-storehouse-field-recording-069::short-fact-069: In document short-snow-orchard-storehouse-field-recording-069, the verified archi...
  5. score=1.046285 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
- Matched markers: copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 60 - short-fact-060
Question: Which item did Ada tuck inside the cedar tube mentioned in the winter letter?

Expected evidence:
- moonflower cutting
- cedar tube

Expected distractors:
- wrong weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.224066 chunk_id=20975 preview=Question anchor: Which item did Ada tuck inside the cedar tube mentioned in the winter letter? Case scope id: short-fact-060. Scoped answer summary for short...
  2. score=41.227276 chunk_id=20976 preview=Question anchor: Which item did Ada tuck inside the cedar tube mentioned in the winter letter? document short-bell-bridge-square-winter-letter-060::short-fac...
  3. score=38.207992 chunk_id=20662 preview=document short-bell-bridge-square-winter-letter-060::short-fact-060: In document short-bell-bridge-square-winter-letter-060, the verified archive note record...
  4. score=9.907086 chunk_id=20727 preview=document short-north-bell-workshop-winter-letter-018::short-fact-018: In document short-north-bell-workshop-winter-letter-018, the verified archive note reco...
- Matched markers: cedar tube, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, moonflower cutting.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.005493 chunk_id=20975 preview=Question anchor: Which item did Ada tuck inside the cedar tube mentioned in the winter letter? Case scope id: short-fact-060. Scoped answer summary for short...
  2. score=41.047398 chunk_id=20976 preview=Question anchor: Which item did Ada tuck inside the cedar tube mentioned in the winter letter? document short-bell-bridge-square-winter-letter-060::short-fac...
  3. score=37.978116 chunk_id=20662 preview=document short-bell-bridge-square-winter-letter-060::short-fact-060: In document short-bell-bridge-square-winter-letter-060, the verified archive note record...
  4. score=9.759112 chunk_id=21039 preview=Question anchor: Which item did Raisa tuck inside the cedar tube mentioned in the winter letter? document short-south-meadow-arch-winter-letter-102::short-fa...
  5. score=9.721983 chunk_id=20913 preview=Question anchor: Which item did Milena tuck inside the cedar tube mentioned in the winter letter? document short-north-bell-workshop-winter-letter-018::short...
- Matched markers: cedar tube, moonflower cutting
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, moonflower cutting.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 61 - short-fact-061
Question: What object and color detail identified Nikola's keepsake at Glass Harbor quay?

Expected evidence:
- saffron birch tea flask

Expected distractors:
- wrong wax thread

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.809573 chunk_id=20693 preview=document short-glass-harbor-quay-station-transcript-061::short-fact-061: In document short-glass-harbor-quay-station-transcript-061, the verified archive not...
  2. score=1.624437 chunk_id=20686 preview=document short-glass-harbor-quay-audio-reel-091::short-fact-091: In document short-glass-harbor-quay-audio-reel-091, the verified archive note records saffro...
  3. score=1.581881 chunk_id=20687 preview=document short-glass-harbor-quay-festival-minutes-031::short-fact-031: In document short-glass-harbor-quay-festival-minutes-031, the verified archive note re...
  4. score=1.089297 chunk_id=20918 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
  5. score=0.960002 chunk_id=21053 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
- Matched markers: saffron birch tea flask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron birch tea flask.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=1.273903 chunk_id=20918 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
  2. score=1.256286 chunk_id=20685 preview=document short-glass-harbor-quay-audio-reel-021::short-fact-021: In document short-glass-harbor-quay-audio-reel-021, the verified archive note records tuning...
  3. score=1.254582 chunk_id=20917 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
  4. score=1.103104 chunk_id=21008 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter? document short-glass-harbor-quay-winter-letter-081::short-...
  5. score=1.082896 chunk_id=21053 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
- Matched markers: none
- Missing markers: saffron birch tea flask
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 62 - short-fact-062
Question: Which fact in the field recording shows what Raisa's twin sister left near South Meadow arch?

Expected evidence:
- saffron scarf
- twin sister

Expected distractors:
- wrong tin key

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.560205 chunk_id=20977 preview=Question anchor: Which fact in the field recording shows what Raisa's twin sister left near South Meadow arch? Case scope id: short-fact-062. Scoped answer s...
  2. score=41.550958 chunk_id=20978 preview=Question anchor: Which fact in the field recording shows what Raisa's twin sister left near South Meadow arch? document short-south-meadow-arch-field-recordi...
  3. score=38.534303 chunk_id=20744 preview=document short-south-meadow-arch-field-recording-062::short-fact-062: In document short-south-meadow-arch-field-recording-062, the verified archive note reco...
  4. score=2.011603 chunk_id=20933 preview=Question anchor: Which fact in the winter letter shows what Iveta's older sister left near South Meadow arch? document short-south-meadow-arch-winter-letter-...
  5. score=1.948066 chunk_id=20750 preview=document short-south-meadow-arch-winter-letter-032::short-fact-032: In document short-south-meadow-arch-winter-letter-032, the verified archive note records...
- Matched markers: saffron scarf, twin sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron scarf, twin sister.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.437399 chunk_id=20977 preview=Question anchor: Which fact in the field recording shows what Raisa's twin sister left near South Meadow arch? Case scope id: short-fact-062. Scoped answer s...
  2. score=41.445101 chunk_id=20978 preview=Question anchor: Which fact in the field recording shows what Raisa's twin sister left near South Meadow arch? document short-south-meadow-arch-field-recordi...
  3. score=38.434062 chunk_id=20744 preview=document short-south-meadow-arch-field-recording-062::short-fact-062: In document short-south-meadow-arch-field-recording-062, the verified archive note reco...
  4. score=1.140551 chunk_id=20742 preview=document short-south-meadow-arch-audio-reel-112::short-fact-112: In document short-south-meadow-arch-audio-reel-112, the verified archive note records paper...
  5. score=1.139900 chunk_id=20749 preview=document short-south-meadow-arch-station-transcript-082::short-fact-082: In document short-south-meadow-arch-station-transcript-082, the verified archive not...
- Matched markers: saffron scarf, twin sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron scarf, twin sister.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 63 - short-fact-063
Question: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel?

Expected evidence:
- carved shell comb
- Hollow Market arcade
- audio reel

Expected distractors:
- wrong blue oar

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.320208 chunk_id=20979 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel? Case scope id: short-fact-063. Scoped answer summary for s...
  2. score=53.327391 chunk_id=20981 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel? document short-hollow-market-arcade-audio-reel-063::short-...
  3. score=53.312410 chunk_id=20980 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel? document short-hollow-market-arcade-audio-reel-063::short-...
  4. score=50.316740 chunk_id=20696 preview=document short-hollow-market-arcade-audio-reel-063::short-fact-063: In document short-hollow-market-arcade-audio-reel-063, the verified archive note records...
  5. score=13.758795 chunk_id=20935 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
- Matched markers: Hollow Market arcade, audio reel, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Hollow Market arcade, audio reel, carved shell comb.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.027719 chunk_id=20979 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel? Case scope id: short-fact-063. Scoped answer summary for s...
  2. score=53.076551 chunk_id=20980 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel? document short-hollow-market-arcade-audio-reel-063::short-...
  3. score=53.059308 chunk_id=20981 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel? document short-hollow-market-arcade-audio-reel-063::short-...
  4. score=49.989762 chunk_id=20696 preview=document short-hollow-market-arcade-audio-reel-063::short-fact-063: In document short-hollow-market-arcade-audio-reel-063, the verified archive note records...
  5. score=13.429792 chunk_id=20936 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
- Matched markers: Hollow Market arcade, audio reel, carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Hollow Market arcade, audio reel, carved shell comb.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 64 - short-fact-064
Question: Which small object in the cedar tube proved that Sonya stopped at Winter Chapel porch?

Expected evidence:
- amber lantern
- Winter Chapel porch

Expected distractors:
- wrong willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.214563 chunk_id=20982 preview=Question anchor: Which small object in the cedar tube proved that Sonya stopped at Winter Chapel porch? Case scope id: short-fact-064. Scoped answer summary...
  2. score=41.273070 chunk_id=20983 preview=Question anchor: Which small object in the cedar tube proved that Sonya stopped at Winter Chapel porch? document short-winter-chapel-porch-profile-page-064::...
  3. score=38.146393 chunk_id=20758 preview=document short-winter-chapel-porch-profile-page-064::short-fact-064: In document short-winter-chapel-porch-profile-page-064, the verified archive note record...
  4. score=14.010457 chunk_id=20938 preview=Question anchor: Which small object in the cedar tube proved that Nessa stopped at Winter Chapel porch? document short-winter-chapel-porch-field-recording-03...
  5. score=5.635767 chunk_id=20754 preview=document short-winter-chapel-porch-festival-minutes-024::short-fact-024: In document short-winter-chapel-porch-festival-minutes-024, the verified archive not...
- Matched markers: Winter Chapel porch, amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Winter Chapel porch, amber lantern.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.104462 chunk_id=20982 preview=Question anchor: Which small object in the cedar tube proved that Sonya stopped at Winter Chapel porch? Case scope id: short-fact-064. Scoped answer summary...
  2. score=41.107020 chunk_id=20983 preview=Question anchor: Which small object in the cedar tube proved that Sonya stopped at Winter Chapel porch? document short-winter-chapel-porch-profile-page-064::...
  3. score=38.048744 chunk_id=20758 preview=document short-winter-chapel-porch-profile-page-064::short-fact-064: In document short-winter-chapel-porch-profile-page-064, the verified archive note record...
  4. score=13.975666 chunk_id=20938 preview=Question anchor: Which small object in the cedar tube proved that Nessa stopped at Winter Chapel porch? document short-winter-chapel-porch-field-recording-03...
  5. score=13.908429 chunk_id=20756 preview=document short-winter-chapel-porch-field-recording-034::short-fact-034: In document short-winter-chapel-porch-field-recording-034, the verified archive note...
- Matched markers: Winter Chapel porch, amber lantern
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Winter Chapel porch, amber lantern.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 65 - short-fact-065
Question: Which direct fact from the river diary page identifies the item recorded for Pavel at Driftwood cove?

Expected evidence:
- basalt sketch

Expected distractors:
- wrong paper moon mask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.309966 chunk_id=20681 preview=document short-driftwood-cove-river-diary-page-065::short-fact-065: In document short-driftwood-cove-river-diary-page-065, the verified archive note records...
  2. score=1.688877 chunk_id=20674 preview=document short-driftwood-cove-audio-reel-035::short-fact-035: In document short-driftwood-cove-audio-reel-035, the verified archive note records silver booth...
  3. score=1.400791 chunk_id=20715 preview=document short-moss-archive-room-station-transcript-047::short-fact-047: In document short-moss-archive-room-station-transcript-047, the verified archive not...
  4. score=1.165216 chunk_id=20679 preview=document short-driftwood-cove-profile-page-015::short-fact-015: In document short-driftwood-cove-profile-page-015, the verified archive note records willow b...
  5. score=1.160420 chunk_id=20909 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Stefan's profile page? document short-driftwood-cove-profile-page-015::short-fact-01...
- Matched markers: basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.249560 chunk_id=20681 preview=document short-driftwood-cove-river-diary-page-065::short-fact-065: In document short-driftwood-cove-river-diary-page-065, the verified archive note records...
  2. score=1.176456 chunk_id=21044 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel? document short-driftwood-cove-audio-reel-105::short-fact-105: In...
  3. score=1.159725 chunk_id=20675 preview=document short-driftwood-cove-audio-reel-105::short-fact-105: In document short-driftwood-cove-audio-reel-105, the verified archive note records star ledger...
  4. score=1.034477 chunk_id=20703 preview=document short-hollow-market-arcade-river-diary-page-093::short-fact-093: In document short-hollow-market-arcade-river-diary-page-093, the verified archive n...
- Matched markers: basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (3 vs 4).

### Question 66 - short-fact-066
Question: Which item did Talia tuck inside the cedar tube mentioned in the festival minutes?

Expected evidence:
- green apron
- cedar tube

Expected distractors:
- wrong glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=41.140184 chunk_id=20985 preview=Question anchor: Which item did Talia tuck inside the cedar tube mentioned in the festival minutes? document short-cloud-wharf-office-festival-minutes-066::s...
  2. score=10.048010 chunk_id=20754 preview=document short-winter-chapel-porch-festival-minutes-024::short-fact-024: In document short-winter-chapel-porch-festival-minutes-024, the verified archive not...
  3. score=10.036803 chunk_id=20922 preview=Question anchor: Which item did Sonya tuck inside the cedar tube mentioned in the festival minutes? document short-winter-chapel-porch-festival-minutes-024::...
  4. score=10.025528 chunk_id=20721 preview=document short-north-bell-workshop-festival-minutes-108::short-fact-108: In document short-north-bell-workshop-festival-minutes-108, the verified archive not...
  5. score=10.012266 chunk_id=21048 preview=Question anchor: Which item did Runa tuck inside the cedar tube mentioned in the festival minutes? document short-north-bell-workshop-festival-minutes-108::s...
- Matched markers: cedar tube, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, green apron.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.997674 chunk_id=20984 preview=Question anchor: Which item did Talia tuck inside the cedar tube mentioned in the festival minutes? Case scope id: short-fact-066. Scoped answer summary for...
  2. score=41.045592 chunk_id=20985 preview=Question anchor: Which item did Talia tuck inside the cedar tube mentioned in the festival minutes? document short-cloud-wharf-office-festival-minutes-066::s...
  3. score=9.889509 chunk_id=21048 preview=Question anchor: Which item did Runa tuck inside the cedar tube mentioned in the festival minutes? document short-north-bell-workshop-festival-minutes-108::s...
  4. score=9.887133 chunk_id=20922 preview=Question anchor: Which item did Sonya tuck inside the cedar tube mentioned in the festival minutes? document short-winter-chapel-porch-festival-minutes-024::...
  5. score=9.818375 chunk_id=20754 preview=document short-winter-chapel-porch-festival-minutes-024::short-fact-024: In document short-winter-chapel-porch-festival-minutes-024, the verified archive not...
- Matched markers: cedar tube, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, green apron.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 67 - short-fact-067
Question: What object and color detail identified Emil's keepsake at Moss Archive room?

Expected evidence:
- saffron silver booth token

Expected distractors:
- wrong copper wind vane pin

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=0.450376 chunk_id=20722 preview=document short-north-bell-workshop-field-recording-048::short-fact-048: In document short-north-bell-workshop-field-recording-048, the verified archive note...
  2. score=0.450376 chunk_id=20662 preview=document short-bell-bridge-square-winter-letter-060::short-fact-060: In document short-bell-bridge-square-winter-letter-060, the verified archive note record...
- Matched markers: none
- Missing markers: saffron silver booth token
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.742915 chunk_id=20717 preview=document short-moss-archive-room-winter-letter-067::short-fact-067: In document short-moss-archive-room-winter-letter-067, the verified archive note records...
  2. score=1.583611 chunk_id=20711 preview=document short-moss-archive-room-field-recording-097::short-fact-097: In document short-moss-archive-room-field-recording-097, the verified archive note reco...
  3. score=1.170861 chunk_id=20927 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
  4. score=1.145778 chunk_id=20710 preview=document short-moss-archive-room-field-recording-027::short-fact-027: In document short-moss-archive-room-field-recording-027, the verified archive note reco...
  5. score=1.144700 chunk_id=20926 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
- Matched markers: saffron silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron silver booth token.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 68 - short-fact-068
Question: Which fact in the station transcript shows what Runa's stepfather left near North Bell workshop?

Expected evidence:
- clay watering cup
- stepfather

Expected distractors:
- wrong coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.387737 chunk_id=20986 preview=Question anchor: Which fact in the station transcript shows what Runa's stepfather left near North Bell workshop? Case scope id: short-fact-068. Scoped answe...
  2. score=41.342992 chunk_id=20987 preview=Question anchor: Which fact in the station transcript shows what Runa's stepfather left near North Bell workshop? document short-north-bell-workshop-station-...
  3. score=38.351068 chunk_id=20726 preview=document short-north-bell-workshop-station-transcript-068::short-fact-068: In document short-north-bell-workshop-station-transcript-068, the verified archive...
  4. score=5.340624 chunk_id=21059 preview=Question anchor: Which fact in the winter letter shows what Zora's stepfather left near Cloud Wharf office? document short-cloud-wharf-office-winter-letter-1...
  5. score=5.330098 chunk_id=20951 preview=Question anchor: Which fact in the river diary page shows what Vera's stepfather left near Winter Chapel porch? document short-winter-chapel-porch-river-diar...
- Matched markers: clay watering cup, stepfather
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: clay watering cup, stepfather.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.328027 chunk_id=20986 preview=Question anchor: Which fact in the station transcript shows what Runa's stepfather left near North Bell workshop? Case scope id: short-fact-068. Scoped answe...
  2. score=41.349286 chunk_id=20987 preview=Question anchor: Which fact in the station transcript shows what Runa's stepfather left near North Bell workshop? document short-north-bell-workshop-station-...
  3. score=38.332500 chunk_id=20726 preview=document short-north-bell-workshop-station-transcript-068::short-fact-068: In document short-north-bell-workshop-station-transcript-068, the verified archive...
  4. score=1.186878 chunk_id=20728 preview=document short-north-bell-workshop-winter-letter-088::short-fact-088: In document short-north-bell-workshop-winter-letter-088, the verified archive note reco...
  5. score=1.183460 chunk_id=20723 preview=document short-north-bell-workshop-field-recording-118::short-fact-118: In document short-north-bell-workshop-field-recording-118, the verified archive note...
- Matched markers: clay watering cup, stepfather
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: clay watering cup, stepfather.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 2).

### Question 69 - short-fact-069
Question: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording?

Expected evidence:
- juniper bundles
- Snow Orchard storehouse
- field recording

Expected distractors:
- wrong violet ribbon

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.324013 chunk_id=20988 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? Case scope id: short-fact-069. Scoped answer summ...
  2. score=53.332805 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  3. score=53.311905 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  4. score=50.305877 chunk_id=20732 preview=document short-snow-orchard-storehouse-field-recording-069::short-fact-069: In document short-snow-orchard-storehouse-field-recording-069, the verified archi...
  5. score=13.677576 chunk_id=20945 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter? document short-snow-orchard-storehouse-winter-letter...
- Matched markers: Snow Orchard storehouse, field recording, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Snow Orchard storehouse, field recording, juniper bundles.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.159601 chunk_id=20988 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? Case scope id: short-fact-069. Scoped answer summ...
  2. score=53.181824 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  3. score=53.177217 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  4. score=50.132082 chunk_id=20732 preview=document short-snow-orchard-storehouse-field-recording-069::short-fact-069: In document short-snow-orchard-storehouse-field-recording-069, the verified archi...
  5. score=13.576718 chunk_id=20945 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter? document short-snow-orchard-storehouse-winter-letter...
- Matched markers: Snow Orchard storehouse, field recording, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Snow Orchard storehouse, field recording, juniper bundles.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 70 - short-fact-070
Question: Which small object in the cedar tube proved that Selma stopped at Bell Bridge square?

Expected evidence:
- smoke vent chain
- Bell Bridge square

Expected distractors:
- wrong tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=14.162481 chunk_id=20902 preview=Question anchor: Which small object in the cedar tube proved that Lina stopped at Bell Bridge square? document short-bell-bridge-square-festival-minutes-010:...
  2. score=5.590541 chunk_id=20658 preview=document short-bell-bridge-square-river-diary-page-030::short-fact-030: In document short-bell-bridge-square-river-diary-page-030, the verified archive note...
  3. score=5.471021 chunk_id=20662 preview=document short-bell-bridge-square-winter-letter-060::short-fact-060: In document short-bell-bridge-square-winter-letter-060, the verified archive note record...
  4. score=5.457368 chunk_id=20655 preview=document short-bell-bridge-square-field-recording-090::short-fact-090: In document short-bell-bridge-square-field-recording-090, the verified archive note re...
- Matched markers: Bell Bridge square
- Missing markers: smoke vent chain
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Bell Bridge square. Missing: smoke vent chain.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.083324 chunk_id=20991 preview=Question anchor: Which small object in the cedar tube proved that Selma stopped at Bell Bridge square? Case scope id: short-fact-070. Scoped answer summary f...
  2. score=41.097307 chunk_id=20992 preview=Question anchor: Which small object in the cedar tube proved that Selma stopped at Bell Bridge square? document short-bell-bridge-square-audio-reel-070::shor...
  3. score=38.031427 chunk_id=20651 preview=document short-bell-bridge-square-audio-reel-070::short-fact-070: In document short-bell-bridge-square-audio-reel-070, the verified archive note records smok...
  4. score=13.897503 chunk_id=20947 preview=Question anchor: Which small object in the cedar tube proved that Mira stopped at Bell Bridge square? document short-bell-bridge-square-station-transcript-04...
  5. score=13.883910 chunk_id=20902 preview=Question anchor: Which small object in the cedar tube proved that Lina stopped at Bell Bridge square? document short-bell-bridge-square-festival-minutes-010:...
- Matched markers: Bell Bridge square, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bell Bridge square, smoke vent chain.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 71 - short-fact-071
Question: Which direct fact from the profile page identifies the item recorded for Damir at Glass Harbor quay?

Expected evidence:
- brass compass

Expected distractors:
- wrong rope bridge permit

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.402177 chunk_id=20691 preview=document short-glass-harbor-quay-profile-page-071::short-fact-071: In document short-glass-harbor-quay-profile-page-071, the verified archive note records br...
  2. score=1.876524 chunk_id=20689 preview=document short-glass-harbor-quay-field-recording-041::short-fact-041: In document short-glass-harbor-quay-field-recording-041, the verified archive note reco...
  3. score=1.587271 chunk_id=20733 preview=document short-snow-orchard-storehouse-profile-page-029::short-fact-029: In document short-snow-orchard-storehouse-profile-page-029, the verified archive not...
  4. score=1.300019 chunk_id=20715 preview=document short-moss-archive-room-station-transcript-047::short-fact-047: In document short-moss-archive-room-station-transcript-047, the verified archive not...
  5. score=1.256793 chunk_id=20963 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Boris's river diary page? document short-glass-harbor-quay-river-diary-page-051::...
- Matched markers: brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass compass.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.249560 chunk_id=20691 preview=document short-glass-harbor-quay-profile-page-071::short-fact-071: In document short-glass-harbor-quay-profile-page-071, the verified archive note records br...
  2. score=1.294209 chunk_id=21053 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
  3. score=1.274788 chunk_id=20690 preview=document short-glass-harbor-quay-field-recording-111::short-fact-111: In document short-glass-harbor-quay-field-recording-111, the verified archive note reco...
  4. score=1.140860 chunk_id=20918 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
  5. score=1.131698 chunk_id=20685 preview=document short-glass-harbor-quay-audio-reel-021::short-fact-021: In document short-glass-harbor-quay-audio-reel-021, the verified archive note records tuning...
- Matched markers: brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass compass.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 72 - short-fact-072
Question: Which item did Iveta tuck inside the cedar tube mentioned in the river diary page?

Expected evidence:
- linen wick
- cedar tube

Expected distractors:
- wrong oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.350784 chunk_id=20993 preview=Question anchor: Which item did Iveta tuck inside the cedar tube mentioned in the river diary page? Case scope id: short-fact-072. Scoped answer summary for...
  2. score=41.355167 chunk_id=20994 preview=Question anchor: Which item did Iveta tuck inside the cedar tube mentioned in the river diary page? document short-south-meadow-arch-river-diary-page-072::sh...
  3. score=38.332656 chunk_id=20747 preview=document short-south-meadow-arch-river-diary-page-072::short-fact-072: In document short-south-meadow-arch-river-diary-page-072, the verified archive note re...
  4. score=10.110257 chunk_id=20658 preview=document short-bell-bridge-square-river-diary-page-030::short-fact-030: In document short-bell-bridge-square-river-diary-page-030, the verified archive note...
  5. score=9.802010 chunk_id=20657 preview=document short-bell-bridge-square-profile-page-120::short-fact-120: In document short-bell-bridge-square-profile-page-120, the verified archive note records...
- Matched markers: cedar tube, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, linen wick.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.157729 chunk_id=20993 preview=Question anchor: Which item did Iveta tuck inside the cedar tube mentioned in the river diary page? Case scope id: short-fact-072. Scoped answer summary for...
  2. score=41.201814 chunk_id=20994 preview=Question anchor: Which item did Iveta tuck inside the cedar tube mentioned in the river diary page? document short-south-meadow-arch-river-diary-page-072::sh...
  3. score=38.136531 chunk_id=20747 preview=document short-south-meadow-arch-river-diary-page-072::short-fact-072: In document short-south-meadow-arch-river-diary-page-072, the verified archive note re...
  4. score=9.968521 chunk_id=20931 preview=Question anchor: Which item did Selma tuck inside the cedar tube mentioned in the river diary page? document short-bell-bridge-square-river-diary-page-030::s...
  5. score=9.956910 chunk_id=20658 preview=document short-bell-bridge-square-river-diary-page-030::short-fact-030: In document short-bell-bridge-square-river-diary-page-030, the verified archive note...
- Matched markers: cedar tube, linen wick
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, linen wick.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 73 - short-fact-073
Question: What object and color detail identified Rafi's keepsake at Hollow Market arcade?

Expected evidence:
- saffron star ledger page

Expected distractors:
- wrong blue glass jar

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=1.766947 chunk_id=20698 preview=document short-hollow-market-arcade-field-recording-013::short-fact-013: In document short-hollow-market-arcade-field-recording-013, the verified archive not...
  2. score=1.408586 chunk_id=20936 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
  3. score=1.405043 chunk_id=20704 preview=document short-hollow-market-arcade-station-transcript-033::short-fact-033: In document short-hollow-market-arcade-station-transcript-033, the verified archi...
  4. score=1.372357 chunk_id=20935 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
  5. score=1.172910 chunk_id=21026 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
- Matched markers: none
- Missing markers: saffron star ledger page
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.628315 chunk_id=20697 preview=document short-hollow-market-arcade-festival-minutes-073::short-fact-073: In document short-hollow-market-arcade-festival-minutes-073, the verified archive n...
  2. score=1.520256 chunk_id=20698 preview=document short-hollow-market-arcade-field-recording-013::short-fact-013: In document short-hollow-market-arcade-field-recording-013, the verified archive not...
  3. score=1.473879 chunk_id=20705 preview=document short-hollow-market-arcade-station-transcript-103::short-fact-103: In document short-hollow-market-arcade-station-transcript-103, the verified archi...
  4. score=1.458505 chunk_id=20700 preview=document short-hollow-market-arcade-profile-page-043::short-fact-043: In document short-hollow-market-arcade-profile-page-043, the verified archive note reco...
  5. score=0.984100 chunk_id=20936 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
- Matched markers: saffron star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron star ledger page.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 74 - short-fact-074
Question: Which fact in the winter letter shows what Nessa's cousin left near Winter Chapel porch?

Expected evidence:
- lantern hook
- cousin

Expected distractors:
- wrong canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.335398 chunk_id=20995 preview=Question anchor: Which fact in the winter letter shows what Nessa's cousin left near Winter Chapel porch? Case scope id: short-fact-074. Scoped answer summar...
  2. score=41.347026 chunk_id=20996 preview=Question anchor: Which fact in the winter letter shows what Nessa's cousin left near Winter Chapel porch? document short-winter-chapel-porch-winter-letter-07...
  3. score=38.300095 chunk_id=20762 preview=document short-winter-chapel-porch-winter-letter-074::short-fact-074: In document short-winter-chapel-porch-winter-letter-074, the verified archive note reco...
  4. score=1.602771 chunk_id=20906 preview=Question anchor: Which fact in the audio reel shows what Daria's twin sister left near Winter Chapel porch? document short-winter-chapel-porch-audio-reel-014...
  5. score=1.570416 chunk_id=20752 preview=document short-winter-chapel-porch-audio-reel-014::short-fact-014: In document short-winter-chapel-porch-audio-reel-014, the verified archive note records bl...
- Matched markers: cousin, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cousin, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.211337 chunk_id=20995 preview=Question anchor: Which fact in the winter letter shows what Nessa's cousin left near Winter Chapel porch? Case scope id: short-fact-074. Scoped answer summar...
  2. score=41.244805 chunk_id=20996 preview=Question anchor: Which fact in the winter letter shows what Nessa's cousin left near Winter Chapel porch? document short-winter-chapel-porch-winter-letter-07...
  3. score=38.216115 chunk_id=20762 preview=document short-winter-chapel-porch-winter-letter-074::short-fact-074: In document short-winter-chapel-porch-winter-letter-074, the verified archive note reco...
  4. score=1.200080 chunk_id=20756 preview=document short-winter-chapel-porch-field-recording-034::short-fact-034: In document short-winter-chapel-porch-field-recording-034, the verified archive note...
  5. score=1.053018 chunk_id=20755 preview=document short-winter-chapel-porch-festival-minutes-094::short-fact-094: In document short-winter-chapel-porch-festival-minutes-094, the verified archive not...
- Matched markers: cousin, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cousin, lantern hook.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 75 - short-fact-075
Question: What exact keepsake was listed beside Driftwood cove in Anton's station transcript?

Expected evidence:
- weathered camera strap
- Driftwood cove
- station transcript

Expected distractors:
- wrong cedar shovel

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.007669 chunk_id=20997 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? Case scope id: short-fact-075. Scoped answer summary for...
  2. score=53.026418 chunk_id=20998 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
  3. score=53.017592 chunk_id=20999 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
  4. score=49.986613 chunk_id=20682 preview=document short-driftwood-cove-station-transcript-075::short-fact-075: In document short-driftwood-cove-station-transcript-075, the verified archive note reco...
  5. score=13.525054 chunk_id=20953 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Ilya's festival minutes? document short-driftwood-cove-festival-minutes-045::short-f...
- Matched markers: Driftwood cove, station transcript, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Driftwood cove, station transcript, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.015512 chunk_id=20997 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? Case scope id: short-fact-075. Scoped answer summary for...
  2. score=53.034568 chunk_id=20999 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
  3. score=53.014825 chunk_id=20998 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
  4. score=49.983115 chunk_id=20682 preview=document short-driftwood-cove-station-transcript-075::short-fact-075: In document short-driftwood-cove-station-transcript-075, the verified archive note reco...
  5. score=13.413999 chunk_id=21044 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel? document short-driftwood-cove-audio-reel-105::short-fact-105: In...
- Matched markers: Driftwood cove, station transcript, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Driftwood cove, station transcript, weathered camera strap.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 76 - short-fact-076
Question: Which small object in the cedar tube proved that Zora stopped at Cloud Wharf office?

Expected evidence:
- wax thread
- Cloud Wharf office

Expected distractors:
- wrong copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=14.138306 chunk_id=20956 preview=Question anchor: Which small object in the cedar tube proved that Kira stopped at Cloud Wharf office? document short-cloud-wharf-office-winter-letter-046::sh...
  2. score=14.136549 chunk_id=21046 preview=Question anchor: Which small object in the cedar tube proved that Talia stopped at Cloud Wharf office? document short-cloud-wharf-office-profile-page-106::sh...
  3. score=5.558638 chunk_id=20671 preview=document short-cloud-wharf-office-station-transcript-096::short-fact-096: In document short-cloud-wharf-office-station-transcript-096, the verified archive n...
  4. score=5.551756 chunk_id=20664 preview=document short-cloud-wharf-office-festival-minutes-066::short-fact-066: In document short-cloud-wharf-office-festival-minutes-066, the verified archive note...
- Matched markers: Cloud Wharf office
- Missing markers: wax thread
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Cloud Wharf office. Missing: wax thread.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.099405 chunk_id=21000 preview=Question anchor: Which small object in the cedar tube proved that Zora stopped at Cloud Wharf office? Case scope id: short-fact-076. Scoped answer summary fo...
  2. score=41.124511 chunk_id=21001 preview=Question anchor: Which small object in the cedar tube proved that Zora stopped at Cloud Wharf office? document short-cloud-wharf-office-field-recording-076::...
  3. score=38.047153 chunk_id=20665 preview=document short-cloud-wharf-office-field-recording-076::short-fact-076: In document short-cloud-wharf-office-field-recording-076, the verified archive note re...
  4. score=13.883639 chunk_id=20956 preview=Question anchor: Which small object in the cedar tube proved that Kira stopped at Cloud Wharf office? document short-cloud-wharf-office-winter-letter-046::sh...
  5. score=13.859101 chunk_id=21046 preview=Question anchor: Which small object in the cedar tube proved that Talia stopped at Cloud Wharf office? document short-cloud-wharf-office-profile-page-106::sh...
- Matched markers: Cloud Wharf office, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, wax thread.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 77 - short-fact-077
Question: Which direct fact from the audio reel identifies the item recorded for Milan at Moss Archive room?

Expected evidence:
- tin key

Expected distractors:
- wrong moonflower cutting

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.364286 chunk_id=20707 preview=document short-moss-archive-room-audio-reel-077::short-fact-077: In document short-moss-archive-room-audio-reel-077, the verified archive note records tin ke...
  2. score=1.927607 chunk_id=20715 preview=document short-moss-archive-room-station-transcript-047::short-fact-047: In document short-moss-archive-room-station-transcript-047, the verified archive not...
  3. score=1.914286 chunk_id=20674 preview=document short-driftwood-cove-audio-reel-035::short-fact-035: In document short-driftwood-cove-audio-reel-035, the verified archive note records silver booth...
  4. score=1.715711 chunk_id=20730 preview=document short-snow-orchard-storehouse-audio-reel-119::short-fact-119: In document short-snow-orchard-storehouse-audio-reel-119, the verified archive note re...
  5. score=1.612082 chunk_id=20708 preview=document short-moss-archive-room-festival-minutes-017::short-fact-017: In document short-moss-archive-room-festival-minutes-017, the verified archive note re...
- Matched markers: tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=1.319815 chunk_id=21062 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Milan's station transcript? document short-moss-archive-room-station-transcript-1...
  2. score=1.286095 chunk_id=20716 preview=document short-moss-archive-room-station-transcript-117::short-fact-117: In document short-moss-archive-room-station-transcript-117, the verified archive not...
  3. score=1.271951 chunk_id=21061 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Milan's station transcript? document short-moss-archive-room-station-transcript-1...
  4. score=1.133523 chunk_id=20927 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
- Matched markers: none
- Missing markers: tin key
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 78 - short-fact-078
Question: Which item did Ilia tuck inside the cedar tube mentioned in the profile page?

Expected evidence:
- blue oar
- cedar tube

Expected distractors:
- wrong birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.220185 chunk_id=21002 preview=Question anchor: Which item did Ilia tuck inside the cedar tube mentioned in the profile page? Case scope id: short-fact-078. Scoped answer summary for short...
  2. score=41.239510 chunk_id=21003 preview=Question anchor: Which item did Ilia tuck inside the cedar tube mentioned in the profile page? document short-north-bell-workshop-profile-page-078::short-fac...
  3. score=38.221662 chunk_id=20724 preview=document short-north-bell-workshop-profile-page-078::short-fact-078: In document short-north-bell-workshop-profile-page-078, the verified archive note record...
  4. score=10.031209 chunk_id=20657 preview=document short-bell-bridge-square-profile-page-120::short-fact-120: In document short-bell-bridge-square-profile-page-120, the verified archive note records...
  5. score=10.026475 chunk_id=21066 preview=Question anchor: Which item did Mira tuck inside the cedar tube mentioned in the profile page? document short-bell-bridge-square-profile-page-120::short-fact...
- Matched markers: blue oar, cedar tube
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, cedar tube.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.957737 chunk_id=21002 preview=Question anchor: Which item did Ilia tuck inside the cedar tube mentioned in the profile page? Case scope id: short-fact-078. Scoped answer summary for short...
  2. score=40.990572 chunk_id=21003 preview=Question anchor: Which item did Ilia tuck inside the cedar tube mentioned in the profile page? document short-north-bell-workshop-profile-page-078::short-fac...
  3. score=37.904272 chunk_id=20724 preview=document short-north-bell-workshop-profile-page-078::short-fact-078: In document short-north-bell-workshop-profile-page-078, the verified archive note record...
  4. score=9.824798 chunk_id=21066 preview=Question anchor: Which item did Mira tuck inside the cedar tube mentioned in the profile page? document short-bell-bridge-square-profile-page-120::short-fact...
  5. score=9.781627 chunk_id=20657 preview=document short-bell-bridge-square-profile-page-120::short-fact-120: In document short-bell-bridge-square-profile-page-120, the verified archive note records...
- Matched markers: blue oar, cedar tube
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, cedar tube.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 79 - short-fact-079
Question: What object and color detail identified Vesna's keepsake at Snow Orchard storehouse?

Expected evidence:
- saffron willow basket

Expected distractors:
- wrong saffron scarf

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.944089 chunk_id=20736 preview=document short-snow-orchard-storehouse-river-diary-page-079::short-fact-079: In document short-snow-orchard-storehouse-river-diary-page-079, the verified arc...
  2. score=1.253454 chunk_id=20945 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter? document short-snow-orchard-storehouse-winter-letter...
  3. score=1.218293 chunk_id=20739 preview=document short-snow-orchard-storehouse-winter-letter-039::short-fact-039: In document short-snow-orchard-storehouse-winter-letter-039, the verified archive n...
  4. score=1.083368 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  5. score=1.076017 chunk_id=20732 preview=document short-snow-orchard-storehouse-field-recording-069::short-fact-069: In document short-snow-orchard-storehouse-field-recording-069, the verified archi...
- Matched markers: saffron willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.762524 chunk_id=20736 preview=document short-snow-orchard-storehouse-river-diary-page-079::short-fact-079: In document short-snow-orchard-storehouse-river-diary-page-079, the verified arc...
  2. score=1.593337 chunk_id=20740 preview=document short-snow-orchard-storehouse-winter-letter-109::short-fact-109: In document short-snow-orchard-storehouse-winter-letter-109, the verified archive n...
  3. score=1.584653 chunk_id=20737 preview=document short-snow-orchard-storehouse-station-transcript-019::short-fact-019: In document short-snow-orchard-storehouse-station-transcript-019, the verified...
  4. score=1.118782 chunk_id=20945 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter? document short-snow-orchard-storehouse-winter-letter...
  5. score=1.007791 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
- Matched markers: saffron willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron willow basket.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 80 - short-fact-080
Question: Which fact in the festival minutes shows what Mira's older sister left near Bell Bridge square?

Expected evidence:
- paper moon mask
- older sister

Expected distractors:
- wrong carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.501123 chunk_id=21004 preview=Question anchor: Which fact in the festival minutes shows what Mira's older sister left near Bell Bridge square? Case scope id: short-fact-080. Scoped answer...
  2. score=41.477606 chunk_id=21005 preview=Question anchor: Which fact in the festival minutes shows what Mira's older sister left near Bell Bridge square? document short-bell-bridge-square-festival-m...
  3. score=38.468153 chunk_id=20653 preview=document short-bell-bridge-square-festival-minutes-080::short-fact-080: In document short-bell-bridge-square-festival-minutes-080, the verified archive note...
  4. score=1.832194 chunk_id=21050 preview=Question anchor: Which fact in the station transcript shows what Selma's twin sister left near Bell Bridge square? document short-bell-bridge-square-station-...
  5. score=1.824020 chunk_id=20661 preview=document short-bell-bridge-square-station-transcript-110::short-fact-110: In document short-bell-bridge-square-station-transcript-110, the verified archive n...
- Matched markers: older sister, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: older sister, paper moon mask.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.489101 chunk_id=21004 preview=Question anchor: Which fact in the festival minutes shows what Mira's older sister left near Bell Bridge square? Case scope id: short-fact-080. Scoped answer...
  2. score=41.486470 chunk_id=21005 preview=Question anchor: Which fact in the festival minutes shows what Mira's older sister left near Bell Bridge square? document short-bell-bridge-square-festival-m...
  3. score=38.477040 chunk_id=20653 preview=document short-bell-bridge-square-festival-minutes-080::short-fact-080: In document short-bell-bridge-square-festival-minutes-080, the verified archive note...
  4. score=1.338901 chunk_id=20652 preview=document short-bell-bridge-square-festival-minutes-010::short-fact-010: In document short-bell-bridge-square-festival-minutes-010, the verified archive note...
  5. score=1.285692 chunk_id=20902 preview=Question anchor: Which small object in the cedar tube proved that Lina stopped at Bell Bridge square? document short-bell-bridge-square-festival-minutes-010:...
- Matched markers: older sister, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: older sister, paper moon mask.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 81 - short-fact-081
Question: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter?

Expected evidence:
- glass ink bottle
- Glass Harbor quay
- winter letter

Expected distractors:
- wrong amber lantern

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.313803 chunk_id=21006 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter? Case scope id: short-fact-081. Scoped answer summary for s...
  2. score=53.305605 chunk_id=21007 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter? document short-glass-harbor-quay-winter-letter-081::short-...
  3. score=53.298765 chunk_id=21008 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter? document short-glass-harbor-quay-winter-letter-081::short-...
  4. score=50.306800 chunk_id=20695 preview=document short-glass-harbor-quay-winter-letter-081::short-fact-081: In document short-glass-harbor-quay-winter-letter-081, the verified archive note records...
  5. score=13.296019 chunk_id=20694 preview=document short-glass-harbor-quay-winter-letter-011::short-fact-011: In document short-glass-harbor-quay-winter-letter-011, the verified archive note records...
- Matched markers: Glass Harbor quay, glass ink bottle, winter letter
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Glass Harbor quay, glass ink bottle, winter letter.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.264668 chunk_id=21006 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter? Case scope id: short-fact-081. Scoped answer summary for s...
  2. score=53.267902 chunk_id=21008 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter? document short-glass-harbor-quay-winter-letter-081::short-...
  3. score=53.260023 chunk_id=21007 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter? document short-glass-harbor-quay-winter-letter-081::short-...
  4. score=50.239389 chunk_id=20695 preview=document short-glass-harbor-quay-winter-letter-081::short-fact-081: In document short-glass-harbor-quay-winter-letter-081, the verified archive note records...
  5. score=13.655380 chunk_id=20917 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
- Matched markers: Glass Harbor quay, glass ink bottle, winter letter
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Glass Harbor quay, glass ink bottle, winter letter.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 82 - short-fact-082
Question: Which small object in the cedar tube proved that Elena stopped at South Meadow arch?

Expected evidence:
- copper wind vane pin
- South Meadow arch

Expected distractors:
- wrong basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=14.095938 chunk_id=20965 preview=Question anchor: Which small object in the cedar tube proved that Anya stopped at South Meadow arch? document short-south-meadow-arch-festival-minutes-052::s...
  2. score=5.667141 chunk_id=20741 preview=document short-south-meadow-arch-audio-reel-042::short-fact-042: In document short-south-meadow-arch-audio-reel-042, the verified archive note records lanter...
  3. score=5.650587 chunk_id=20949 preview=Question anchor: Which item did Elena tuck inside the cedar tube mentioned in the audio reel? document short-south-meadow-arch-audio-reel-042::short-fact-042...
  4. score=5.455044 chunk_id=20747 preview=document short-south-meadow-arch-river-diary-page-072::short-fact-072: In document short-south-meadow-arch-river-diary-page-072, the verified archive note re...
- Matched markers: South Meadow arch
- Missing markers: copper wind vane pin
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: South Meadow arch. Missing: copper wind vane pin.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.132884 chunk_id=21009 preview=Question anchor: Which small object in the cedar tube proved that Elena stopped at South Meadow arch? Case scope id: short-fact-082. Scoped answer summary fo...
  2. score=41.129253 chunk_id=21010 preview=Question anchor: Which small object in the cedar tube proved that Elena stopped at South Meadow arch? document short-south-meadow-arch-station-transcript-082...
  3. score=38.101046 chunk_id=20749 preview=document short-south-meadow-arch-station-transcript-082::short-fact-082: In document short-south-meadow-arch-station-transcript-082, the verified archive not...
  4. score=13.928747 chunk_id=21055 preview=Question anchor: Which small object in the cedar tube proved that Iveta stopped at South Meadow arch? document short-south-meadow-arch-audio-reel-112::short-...
  5. score=13.927421 chunk_id=20965 preview=Question anchor: Which small object in the cedar tube proved that Anya stopped at South Meadow arch? document short-south-meadow-arch-festival-minutes-052::s...
- Matched markers: South Meadow arch, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: South Meadow arch, copper wind vane pin.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 83 - short-fact-083
Question: Which direct fact from the field recording identifies the item recorded for Radin at Hollow Market arcade?

Expected evidence:
- coal stove hiss

Expected distractors:
- wrong green apron

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.434464 chunk_id=20699 preview=document short-hollow-market-arcade-field-recording-083::short-fact-083: In document short-hollow-market-arcade-field-recording-083, the verified archive not...
  2. score=1.806780 chunk_id=20702 preview=document short-hollow-market-arcade-river-diary-page-023::short-fact-023: In document short-hollow-market-arcade-river-diary-page-023, the verified archive n...
  3. score=1.501041 chunk_id=20698 preview=document short-hollow-market-arcade-field-recording-013::short-fact-013: In document short-hollow-market-arcade-field-recording-013, the verified archive not...
  4. score=1.230718 chunk_id=20936 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
  5. score=1.212737 chunk_id=20704 preview=document short-hollow-market-arcade-station-transcript-033::short-fact-033: In document short-hollow-market-arcade-station-transcript-033, the verified archi...
- Matched markers: coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.970256 chunk_id=20699 preview=document short-hollow-market-arcade-field-recording-083::short-fact-083: In document short-hollow-market-arcade-field-recording-083, the verified archive not...
  2. score=0.886772 chunk_id=20981 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel? document short-hollow-market-arcade-audio-reel-063::short-...
  3. score=0.874497 chunk_id=20696 preview=document short-hollow-market-arcade-audio-reel-063::short-fact-063: In document short-hollow-market-arcade-audio-reel-063, the verified archive note records...
  4. score=0.842065 chunk_id=20980 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel? document short-hollow-market-arcade-audio-reel-063::short-...
  5. score=0.833675 chunk_id=20936 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
- Matched markers: coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 84 - short-fact-084
Question: Which item did Vera tuck inside the cedar tube mentioned in the audio reel?

Expected evidence:
- violet ribbon
- cedar tube

Expected distractors:
- wrong silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.163187 chunk_id=21011 preview=Question anchor: Which item did Vera tuck inside the cedar tube mentioned in the audio reel? Case scope id: short-fact-084. Scoped answer summary for short-f...
  2. score=41.162266 chunk_id=21012 preview=Question anchor: Which item did Vera tuck inside the cedar tube mentioned in the audio reel? document short-winter-chapel-porch-audio-reel-084::short-fact-08...
  3. score=38.148675 chunk_id=20753 preview=document short-winter-chapel-porch-audio-reel-084::short-fact-084: In document short-winter-chapel-porch-audio-reel-084, the verified archive note records vi...
  4. score=10.013431 chunk_id=20949 preview=Question anchor: Which item did Elena tuck inside the cedar tube mentioned in the audio reel? document short-south-meadow-arch-audio-reel-042::short-fact-042...
  5. score=9.960257 chunk_id=20741 preview=document short-south-meadow-arch-audio-reel-042::short-fact-042: In document short-south-meadow-arch-audio-reel-042, the verified archive note records lanter...
- Matched markers: cedar tube, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, violet ribbon.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.908127 chunk_id=21011 preview=Question anchor: Which item did Vera tuck inside the cedar tube mentioned in the audio reel? Case scope id: short-fact-084. Scoped answer summary for short-f...
  2. score=40.941694 chunk_id=21012 preview=Question anchor: Which item did Vera tuck inside the cedar tube mentioned in the audio reel? document short-winter-chapel-porch-audio-reel-084::short-fact-08...
  3. score=37.849215 chunk_id=20753 preview=document short-winter-chapel-porch-audio-reel-084::short-fact-084: In document short-winter-chapel-porch-audio-reel-084, the verified archive note records vi...
  4. score=13.378165 chunk_id=20922 preview=Question anchor: Which item did Sonya tuck inside the cedar tube mentioned in the festival minutes? document short-winter-chapel-porch-festival-minutes-024::...
  5. score=9.359016 chunk_id=21021 preview=Question anchor: Which item did Lina tuck inside the cedar tube mentioned in the field recording? document short-bell-bridge-square-field-recording-090::shor...
- Matched markers: cedar tube, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, violet ribbon.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 85 - short-fact-085
Question: What object and color detail identified Ilya's keepsake at Driftwood cove?

Expected evidence:
- saffron tuning fork

Expected distractors:
- wrong clay watering cup

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.564900 chunk_id=20680 preview=document short-driftwood-cove-profile-page-085::short-fact-085: In document short-driftwood-cove-profile-page-085, the verified archive note records saffron...
  2. score=1.540098 chunk_id=20678 preview=document short-driftwood-cove-field-recording-055::short-fact-055: In document short-driftwood-cove-field-recording-055, the verified archive note records sa...
  3. score=0.966233 chunk_id=20954 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Ilya's festival minutes? document short-driftwood-cove-festival-minutes-045::short-f...
  4. score=0.845577 chunk_id=20999 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
  5. score=0.831685 chunk_id=20682 preview=document short-driftwood-cove-station-transcript-075::short-fact-075: In document short-driftwood-cove-station-transcript-075, the verified archive note reco...
- Matched markers: saffron tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.642504 chunk_id=20680 preview=document short-driftwood-cove-profile-page-085::short-fact-085: In document short-driftwood-cove-profile-page-085, the verified archive note records saffron...
  2. score=1.430438 chunk_id=20678 preview=document short-driftwood-cove-field-recording-055::short-fact-055: In document short-driftwood-cove-field-recording-055, the verified archive note records sa...
  3. score=1.428681 chunk_id=20683 preview=document short-driftwood-cove-winter-letter-025::short-fact-025: In document short-driftwood-cove-winter-letter-025, the verified archive note records saffro...
  4. score=0.944138 chunk_id=20954 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Ilya's festival minutes? document short-driftwood-cove-festival-minutes-045::short-f...
  5. score=0.806313 chunk_id=20999 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
- Matched markers: saffron tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron tuning fork.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 86 - short-fact-086
Question: Which fact in the river diary page shows what Kira's twin sister left near Cloud Wharf office?

Expected evidence:
- rope bridge permit
- twin sister

Expected distractors:
- wrong juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.782030 chunk_id=21013 preview=Question anchor: Which fact in the river diary page shows what Kira's twin sister left near Cloud Wharf office? Case scope id: short-fact-086. Scoped answer...
  2. score=41.772720 chunk_id=21014 preview=Question anchor: Which fact in the river diary page shows what Kira's twin sister left near Cloud Wharf office? document short-cloud-wharf-office-river-diary...
  3. score=38.789061 chunk_id=20669 preview=document short-cloud-wharf-office-river-diary-page-086::short-fact-086: In document short-cloud-wharf-office-river-diary-page-086, the verified archive note...
  4. score=1.942426 chunk_id=20969 preview=Question anchor: Which fact in the audio reel shows what Yara's older sister left near Cloud Wharf office? document short-cloud-wharf-office-audio-reel-056::...
  5. score=1.781993 chunk_id=21059 preview=Question anchor: Which fact in the winter letter shows what Zora's stepfather left near Cloud Wharf office? document short-cloud-wharf-office-winter-letter-1...
- Matched markers: rope bridge permit, twin sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: rope bridge permit, twin sister.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.593605 chunk_id=21013 preview=Question anchor: Which fact in the river diary page shows what Kira's twin sister left near Cloud Wharf office? Case scope id: short-fact-086. Scoped answer...
  2. score=41.615640 chunk_id=21014 preview=Question anchor: Which fact in the river diary page shows what Kira's twin sister left near Cloud Wharf office? document short-cloud-wharf-office-river-diary...
  3. score=38.617003 chunk_id=20669 preview=document short-cloud-wharf-office-river-diary-page-086::short-fact-086: In document short-cloud-wharf-office-river-diary-page-086, the verified archive note...
  4. score=1.563915 chunk_id=20668 preview=document short-cloud-wharf-office-river-diary-page-016::short-fact-016: In document short-cloud-wharf-office-river-diary-page-016, the verified archive note...
  5. score=1.034477 chunk_id=20703 preview=document short-hollow-market-arcade-river-diary-page-093::short-fact-093: In document short-hollow-market-arcade-river-diary-page-093, the verified archive n...
- Matched markers: rope bridge permit, twin sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: rope bridge permit, twin sister.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 87 - short-fact-087
Question: What exact keepsake was listed beside Moss Archive room in Soren's festival minutes?

Expected evidence:
- oak barrel hoops
- Moss Archive room
- festival minutes

Expected distractors:
- wrong smoke vent chain

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.200140 chunk_id=21015 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Soren's festival minutes? Case scope id: short-fact-087. Scoped answer summary fo...
  2. score=53.244070 chunk_id=21016 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Soren's festival minutes? document short-moss-archive-room-festival-minutes-087::...
  3. score=53.172166 chunk_id=21017 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Soren's festival minutes? document short-moss-archive-room-festival-minutes-087::...
  4. score=50.172927 chunk_id=20709 preview=document short-moss-archive-room-festival-minutes-087::short-fact-087: In document short-moss-archive-room-festival-minutes-087, the verified archive note re...
  5. score=9.609259 chunk_id=20953 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Ilya's festival minutes? document short-driftwood-cove-festival-minutes-045::short-f...
- Matched markers: Moss Archive room, festival minutes, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moss Archive room, festival minutes, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.290938 chunk_id=21015 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Soren's festival minutes? Case scope id: short-fact-087. Scoped answer summary fo...
  2. score=53.310853 chunk_id=21017 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Soren's festival minutes? document short-moss-archive-room-festival-minutes-087::...
  3. score=53.305247 chunk_id=21016 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Soren's festival minutes? document short-moss-archive-room-festival-minutes-087::...
  4. score=50.285668 chunk_id=20709 preview=document short-moss-archive-room-festival-minutes-087::short-fact-087: In document short-moss-archive-room-festival-minutes-087, the verified archive note re...
  5. score=13.614584 chunk_id=20926 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
- Matched markers: Moss Archive room, festival minutes, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moss Archive room, festival minutes, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 88 - short-fact-088
Question: Which small object in the cedar tube proved that Nadia stopped at North Bell workshop?

Expected evidence:
- blue glass jar
- North Bell workshop

Expected distractors:
- wrong brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=41.103249 chunk_id=21019 preview=Question anchor: Which small object in the cedar tube proved that Nadia stopped at North Bell workshop? document short-north-bell-workshop-winter-letter-088:...
  2. score=5.555474 chunk_id=20722 preview=document short-north-bell-workshop-field-recording-048::short-fact-048: In document short-north-bell-workshop-field-recording-048, the verified archive note...
  3. score=5.503023 chunk_id=20958 preview=Question anchor: Which item did Nadia tuck inside the cedar tube mentioned in the field recording? document short-north-bell-workshop-field-recording-048::sh...
- Matched markers: North Bell workshop, blue glass jar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: North Bell workshop, blue glass jar.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.225866 chunk_id=21018 preview=Question anchor: Which small object in the cedar tube proved that Nadia stopped at North Bell workshop? Case scope id: short-fact-088. Scoped answer summary...
  2. score=41.225313 chunk_id=21019 preview=Question anchor: Which small object in the cedar tube proved that Nadia stopped at North Bell workshop? document short-north-bell-workshop-winter-letter-088:...
  3. score=14.067791 chunk_id=20929 preview=Question anchor: Which small object in the cedar tube proved that Runa stopped at North Bell workshop? document short-north-bell-workshop-audio-reel-028::sho...
  4. score=14.045978 chunk_id=20974 preview=Question anchor: Which small object in the cedar tube proved that Milena stopped at North Bell workshop? document short-north-bell-workshop-river-diary-page-...
- Matched markers: North Bell workshop, blue glass jar
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: North Bell workshop, blue glass jar.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 89 - short-fact-089
Question: Which direct fact from the station transcript identifies the item recorded for Petar at Snow Orchard storehouse?

Expected evidence:
- canal route map

Expected distractors:
- wrong linen wick

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.299956 chunk_id=20738 preview=document short-snow-orchard-storehouse-station-transcript-089::short-fact-089: In document short-snow-orchard-storehouse-station-transcript-089, the verified...
  2. score=1.835053 chunk_id=20731 preview=document short-snow-orchard-storehouse-festival-minutes-059::short-fact-059: In document short-snow-orchard-storehouse-festival-minutes-059, the verified arc...
  3. score=1.789506 chunk_id=20730 preview=document short-snow-orchard-storehouse-audio-reel-119::short-fact-119: In document short-snow-orchard-storehouse-audio-reel-119, the verified archive note re...
  4. score=1.780319 chunk_id=20733 preview=document short-snow-orchard-storehouse-profile-page-029::short-fact-029: In document short-snow-orchard-storehouse-profile-page-029, the verified archive not...
  5. score=1.644089 chunk_id=20715 preview=document short-moss-archive-room-station-transcript-047::short-fact-047: In document short-moss-archive-room-station-transcript-047, the verified archive not...
- Matched markers: canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.141076 chunk_id=20738 preview=document short-snow-orchard-storehouse-station-transcript-089::short-fact-089: In document short-snow-orchard-storehouse-station-transcript-089, the verified...
  2. score=1.055370 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  3. score=1.037595 chunk_id=20732 preview=document short-snow-orchard-storehouse-field-recording-069::short-fact-069: In document short-snow-orchard-storehouse-field-recording-069, the verified archi...
  4. score=1.009094 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  5. score=0.989669 chunk_id=21035 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? document short-snow-orchard-storehouse-profile-page-099...
- Matched markers: canal route map
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 90 - short-fact-090
Question: Which item did Lina tuck inside the cedar tube mentioned in the field recording?

Expected evidence:
- cedar shovel
- cedar tube

Expected distractors:
- wrong star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.223693 chunk_id=21020 preview=Question anchor: Which item did Lina tuck inside the cedar tube mentioned in the field recording? Case scope id: short-fact-090. Scoped answer summary for sh...
  2. score=41.220119 chunk_id=21021 preview=Question anchor: Which item did Lina tuck inside the cedar tube mentioned in the field recording? document short-bell-bridge-square-field-recording-090::shor...
  3. score=38.208205 chunk_id=20655 preview=document short-bell-bridge-square-field-recording-090::short-fact-090: In document short-bell-bridge-square-field-recording-090, the verified archive note re...
  4. score=10.048010 chunk_id=20722 preview=document short-north-bell-workshop-field-recording-048::short-fact-048: In document short-north-bell-workshop-field-recording-048, the verified archive note...
  5. score=10.012541 chunk_id=20958 preview=Question anchor: Which item did Nadia tuck inside the cedar tube mentioned in the field recording? document short-north-bell-workshop-field-recording-048::sh...
- Matched markers: cedar shovel, cedar tube
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, cedar tube.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.908856 chunk_id=21020 preview=Question anchor: Which item did Lina tuck inside the cedar tube mentioned in the field recording? Case scope id: short-fact-090. Scoped answer summary for sh...
  2. score=40.946356 chunk_id=21021 preview=Question anchor: Which item did Lina tuck inside the cedar tube mentioned in the field recording? document short-bell-bridge-square-field-recording-090::shor...
  3. score=37.830409 chunk_id=20655 preview=document short-bell-bridge-square-field-recording-090::short-fact-090: In document short-bell-bridge-square-field-recording-090, the verified archive note re...
  4. score=9.355788 chunk_id=21012 preview=Question anchor: Which item did Vera tuck inside the cedar tube mentioned in the audio reel? document short-winter-chapel-porch-audio-reel-084::short-fact-08...
  5. score=9.340360 chunk_id=20949 preview=Question anchor: Which item did Elena tuck inside the cedar tube mentioned in the audio reel? document short-south-meadow-arch-audio-reel-042::short-fact-042...
- Matched markers: cedar shovel, cedar tube
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, cedar tube.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 91 - short-fact-091
Question: What object and color detail identified Boris's keepsake at Glass Harbor quay?

Expected evidence:
- saffron copper token

Expected distractors:
- wrong lantern hook

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.783861 chunk_id=20686 preview=document short-glass-harbor-quay-audio-reel-091::short-fact-091: In document short-glass-harbor-quay-audio-reel-091, the verified archive note records saffro...
  2. score=0.623365 chunk_id=20758 preview=document short-winter-chapel-porch-profile-page-064::short-fact-064: In document short-winter-chapel-porch-profile-page-064, the verified archive note record...
  3. score=0.623160 chunk_id=20983 preview=Question anchor: Which small object in the cedar tube proved that Sonya stopped at Winter Chapel porch? document short-winter-chapel-porch-profile-page-064::...
  4. score=0.608732 chunk_id=20756 preview=document short-winter-chapel-porch-field-recording-034::short-fact-034: In document short-winter-chapel-porch-field-recording-034, the verified archive note...
  5. score=0.582113 chunk_id=20938 preview=Question anchor: Which small object in the cedar tube proved that Nessa stopped at Winter Chapel porch? document short-winter-chapel-porch-field-recording-03...
- Matched markers: saffron copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron copper token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=1.135595 chunk_id=21008 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Tomas's winter letter? document short-glass-harbor-quay-winter-letter-081::short-...
  2. score=1.134498 chunk_id=20918 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
  3. score=1.116983 chunk_id=20685 preview=document short-glass-harbor-quay-audio-reel-021::short-fact-021: In document short-glass-harbor-quay-audio-reel-021, the verified archive note records tuning...
  4. score=1.114081 chunk_id=21053 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
  5. score=1.111589 chunk_id=20917 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
- Matched markers: none
- Missing markers: saffron copper token
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 92 - short-fact-092
Question: Which fact in the profile page shows what Anya's stepfather left near South Meadow arch?

Expected evidence:
- moonflower cutting
- stepfather

Expected distractors:
- wrong weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.529453 chunk_id=21022 preview=Question anchor: Which fact in the profile page shows what Anya's stepfather left near South Meadow arch? Case scope id: short-fact-092. Scoped answer summar...
  2. score=41.527475 chunk_id=21023 preview=Question anchor: Which fact in the profile page shows what Anya's stepfather left near South Meadow arch? document short-south-meadow-arch-profile-page-092::...
  3. score=38.527269 chunk_id=20746 preview=document short-south-meadow-arch-profile-page-092::short-fact-092: In document short-south-meadow-arch-profile-page-092, the verified archive note records mo...
  4. score=1.742137 chunk_id=20933 preview=Question anchor: Which fact in the winter letter shows what Iveta's older sister left near South Meadow arch? document short-south-meadow-arch-winter-letter-...
  5. score=1.705668 chunk_id=20978 preview=Question anchor: Which fact in the field recording shows what Raisa's twin sister left near South Meadow arch? document short-south-meadow-arch-field-recordi...
- Matched markers: moonflower cutting, stepfather
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: moonflower cutting, stepfather.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.385097 chunk_id=21022 preview=Question anchor: Which fact in the profile page shows what Anya's stepfather left near South Meadow arch? Case scope id: short-fact-092. Scoped answer summar...
  2. score=41.402230 chunk_id=21023 preview=Question anchor: Which fact in the profile page shows what Anya's stepfather left near South Meadow arch? document short-south-meadow-arch-profile-page-092::...
  3. score=38.379120 chunk_id=20746 preview=document short-south-meadow-arch-profile-page-092::short-fact-092: In document short-south-meadow-arch-profile-page-092, the verified archive note records mo...
  4. score=1.404458 chunk_id=20745 preview=document short-south-meadow-arch-profile-page-022::short-fact-022: In document short-south-meadow-arch-profile-page-022, the verified archive note records ro...
  5. score=1.346889 chunk_id=20920 preview=Question anchor: Which small object in the cedar tube proved that Raisa stopped at South Meadow arch? document short-south-meadow-arch-profile-page-022::shor...
- Matched markers: moonflower cutting, stepfather
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: moonflower cutting, stepfather.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 93 - short-fact-093
Question: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page?

Expected evidence:
- birch tea flask
- Hollow Market arcade
- river diary page

Expected distractors:
- wrong wax thread

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.492836 chunk_id=21024 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? Case scope id: short-fact-093. Scoped answer summary...
  2. score=53.497268 chunk_id=21025 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
  3. score=53.487330 chunk_id=21026 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
  4. score=50.485518 chunk_id=20703 preview=document short-hollow-market-arcade-river-diary-page-093::short-fact-093: In document short-hollow-market-arcade-river-diary-page-093, the verified archive n...
  5. score=13.758795 chunk_id=20935 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
- Matched markers: Hollow Market arcade, birch tea flask, river diary page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Hollow Market arcade, birch tea flask, river diary page.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.373272 chunk_id=21024 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? Case scope id: short-fact-093. Scoped answer summary...
  2. score=53.397825 chunk_id=21026 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
  3. score=53.363461 chunk_id=21025 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
  4. score=50.375770 chunk_id=20703 preview=document short-hollow-market-arcade-river-diary-page-093::short-fact-093: In document short-hollow-market-arcade-river-diary-page-093, the verified archive n...
  5. score=9.541932 chunk_id=20899 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Petar's river diary page? document short-snow-orchard-storehouse-river-diar...
- Matched markers: Hollow Market arcade, birch tea flask, river diary page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Hollow Market arcade, birch tea flask, river diary page.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 94 - short-fact-094
Question: Which small object in the cedar tube proved that Daria stopped at Winter Chapel porch?

Expected evidence:
- saffron scarf
- Winter Chapel porch

Expected distractors:
- wrong tin key

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=14.123127 chunk_id=20983 preview=Question anchor: Which small object in the cedar tube proved that Sonya stopped at Winter Chapel porch? document short-winter-chapel-porch-profile-page-064::...
  2. score=14.056058 chunk_id=20938 preview=Question anchor: Which small object in the cedar tube proved that Nessa stopped at Winter Chapel porch? document short-winter-chapel-porch-field-recording-03...
  3. score=5.471021 chunk_id=20754 preview=document short-winter-chapel-porch-festival-minutes-024::short-fact-024: In document short-winter-chapel-porch-festival-minutes-024, the verified archive not...
  4. score=5.420059 chunk_id=20753 preview=document short-winter-chapel-porch-audio-reel-084::short-fact-084: In document short-winter-chapel-porch-audio-reel-084, the verified archive note records vi...
- Matched markers: Winter Chapel porch
- Missing markers: saffron scarf
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Winter Chapel porch. Missing: saffron scarf.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.037104 chunk_id=21027 preview=Question anchor: Which small object in the cedar tube proved that Daria stopped at Winter Chapel porch? Case scope id: short-fact-094. Scoped answer summary...
  2. score=41.022452 chunk_id=21028 preview=Question anchor: Which small object in the cedar tube proved that Daria stopped at Winter Chapel porch? document short-winter-chapel-porch-festival-minutes-0...
  3. score=13.901039 chunk_id=20938 preview=Question anchor: Which small object in the cedar tube proved that Nessa stopped at Winter Chapel porch? document short-winter-chapel-porch-field-recording-03...
  4. score=13.884617 chunk_id=20983 preview=Question anchor: Which small object in the cedar tube proved that Sonya stopped at Winter Chapel porch? document short-winter-chapel-porch-profile-page-064::...
  5. score=13.848571 chunk_id=20756 preview=document short-winter-chapel-porch-field-recording-034::short-fact-034: In document short-winter-chapel-porch-field-recording-034, the verified archive note...
- Matched markers: Winter Chapel porch, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Winter Chapel porch, saffron scarf.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 95 - short-fact-095
Question: Which direct fact from the winter letter identifies the item recorded for Stefan at Driftwood cove?

Expected evidence:
- carved shell comb

Expected distractors:
- wrong blue oar

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.108121 chunk_id=20684 preview=document short-driftwood-cove-winter-letter-095::short-fact-095: In document short-driftwood-cove-winter-letter-095, the verified archive note records carved...
  2. score=1.688877 chunk_id=20674 preview=document short-driftwood-cove-audio-reel-035::short-fact-035: In document short-driftwood-cove-audio-reel-035, the verified archive note records silver booth...
  3. score=1.588382 chunk_id=20694 preview=document short-glass-harbor-quay-winter-letter-011::short-fact-011: In document short-glass-harbor-quay-winter-letter-011, the verified archive note records...
  4. score=1.521405 chunk_id=20681 preview=document short-driftwood-cove-river-diary-page-065::short-fact-065: In document short-driftwood-cove-river-diary-page-065, the verified archive note records...
  5. score=1.400791 chunk_id=20715 preview=document short-moss-archive-room-station-transcript-047::short-fact-047: In document short-moss-archive-room-station-transcript-047, the verified archive not...
- Matched markers: carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: carved shell comb.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.128695 chunk_id=20684 preview=document short-driftwood-cove-winter-letter-095::short-fact-095: In document short-driftwood-cove-winter-letter-095, the verified archive note records carved...
  2. score=1.261698 chunk_id=20683 preview=document short-driftwood-cove-winter-letter-025::short-fact-025: In document short-driftwood-cove-winter-letter-025, the verified archive note records saffro...
  3. score=0.978902 chunk_id=20909 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Stefan's profile page? document short-driftwood-cove-profile-page-015::short-fact-01...
  4. score=0.843058 chunk_id=21044 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel? document short-driftwood-cove-audio-reel-105::short-fact-105: In...
  5. score=0.842620 chunk_id=20999 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
- Matched markers: carved shell comb
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: carved shell comb.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 96 - short-fact-096
Question: Which item did Yara tuck inside the cedar tube mentioned in the station transcript?

Expected evidence:
- amber lantern
- cedar tube

Expected distractors:
- wrong willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.119512 chunk_id=21029 preview=Question anchor: Which item did Yara tuck inside the cedar tube mentioned in the station transcript? Case scope id: short-fact-096. Scoped answer summary for...
  2. score=41.138018 chunk_id=21030 preview=Question anchor: Which item did Yara tuck inside the cedar tube mentioned in the station transcript? document short-cloud-wharf-office-station-transcript-096...
  3. score=9.639188 chunk_id=21021 preview=Question anchor: Which item did Lina tuck inside the cedar tube mentioned in the field recording? document short-bell-bridge-square-field-recording-090::shor...
  4. score=9.629441 chunk_id=20655 preview=document short-bell-bridge-square-field-recording-090::short-fact-090: In document short-bell-bridge-square-field-recording-090, the verified archive note re...
- Matched markers: amber lantern, cedar tube
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, cedar tube.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.952602 chunk_id=21029 preview=Question anchor: Which item did Yara tuck inside the cedar tube mentioned in the station transcript? Case scope id: short-fact-096. Scoped answer summary for...
  2. score=40.988858 chunk_id=21030 preview=Question anchor: Which item did Yara tuck inside the cedar tube mentioned in the station transcript? document short-cloud-wharf-office-station-transcript-096...
  3. score=37.877720 chunk_id=20671 preview=document short-cloud-wharf-office-station-transcript-096::short-fact-096: In document short-cloud-wharf-office-station-transcript-096, the verified archive n...
  4. score=9.744915 chunk_id=20904 preview=Question anchor: Which item did Anya tuck inside the cedar tube mentioned in the station transcript? document short-south-meadow-arch-station-transcript-012:...
  5. score=9.702069 chunk_id=20967 preview=Question anchor: Which item did Daria tuck inside the cedar tube mentioned in the station transcript? document short-winter-chapel-porch-station-transcript-0...
- Matched markers: amber lantern, cedar tube
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, cedar tube.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 97 - short-fact-097
Question: What object and color detail identified Oren's keepsake at Moss Archive room?

Expected evidence:
- saffron basalt sketch

Expected distractors:
- wrong paper moon mask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=0.410133 chunk_id=20722 preview=document short-north-bell-workshop-field-recording-048::short-fact-048: In document short-north-bell-workshop-field-recording-048, the verified archive note...
  2. score=0.410133 chunk_id=20662 preview=document short-bell-bridge-square-winter-letter-060::short-fact-060: In document short-bell-bridge-square-winter-letter-060, the verified archive note record...
- Matched markers: none
- Missing markers: saffron basalt sketch
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.755821 chunk_id=20711 preview=document short-moss-archive-room-field-recording-097::short-fact-097: In document short-moss-archive-room-field-recording-097, the verified archive note reco...
  2. score=1.118415 chunk_id=20972 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Oren's profile page? document short-moss-archive-room-profile-page-057::short-fac...
  3. score=1.000912 chunk_id=20927 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
  4. score=0.977115 chunk_id=20926 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
  5. score=0.972334 chunk_id=21062 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Milan's station transcript? document short-moss-archive-room-station-transcript-1...
- Matched markers: saffron basalt sketch
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron basalt sketch.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 98 - short-fact-098
Question: Which fact in the audio reel shows what Milena's cousin left near North Bell workshop?

Expected evidence:
- green apron
- cousin

Expected distractors:
- wrong glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.407175 chunk_id=21031 preview=Question anchor: Which fact in the audio reel shows what Milena's cousin left near North Bell workshop? Case scope id: short-fact-098. Scoped answer summary...
  2. score=41.392982 chunk_id=21032 preview=Question anchor: Which fact in the audio reel shows what Milena's cousin left near North Bell workshop? document short-north-bell-workshop-audio-reel-098::sh...
  3. score=38.365678 chunk_id=20719 preview=document short-north-bell-workshop-audio-reel-098::short-fact-098: In document short-north-bell-workshop-audio-reel-098, the verified archive note records gr...
- Matched markers: cousin, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cousin, green apron.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.404125 chunk_id=21031 preview=Question anchor: Which fact in the audio reel shows what Milena's cousin left near North Bell workshop? Case scope id: short-fact-098. Scoped answer summary...
  2. score=41.429052 chunk_id=21032 preview=Question anchor: Which fact in the audio reel shows what Milena's cousin left near North Bell workshop? document short-north-bell-workshop-audio-reel-098::sh...
  3. score=38.385870 chunk_id=20719 preview=document short-north-bell-workshop-audio-reel-098::short-fact-098: In document short-north-bell-workshop-audio-reel-098, the verified archive note records gr...
  4. score=1.193184 chunk_id=20723 preview=document short-north-bell-workshop-field-recording-118::short-fact-118: In document short-north-bell-workshop-field-recording-118, the verified archive note...
  5. score=1.186878 chunk_id=20728 preview=document short-north-bell-workshop-winter-letter-088::short-fact-088: In document short-north-bell-workshop-winter-letter-088, the verified archive note reco...
- Matched markers: cousin, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cousin, green apron.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 2).

### Question 99 - short-fact-099
Question: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page?

Expected evidence:
- silver booth token
- Snow Orchard storehouse
- profile page

Expected distractors:
- wrong copper wind vane pin

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.363361 chunk_id=21033 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? Case scope id: short-fact-099. Scoped answer summary fo...
  2. score=53.381489 chunk_id=21034 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? document short-snow-orchard-storehouse-profile-page-099...
  3. score=53.347883 chunk_id=21035 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? document short-snow-orchard-storehouse-profile-page-099...
  4. score=50.351410 chunk_id=20734 preview=document short-snow-orchard-storehouse-profile-page-099::short-fact-099: In document short-snow-orchard-storehouse-profile-page-099, the verified archive not...
  5. score=13.946415 chunk_id=20900 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Petar's river diary page? document short-snow-orchard-storehouse-river-diar...
- Matched markers: Snow Orchard storehouse, profile page, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Snow Orchard storehouse, profile page, silver booth token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.248418 chunk_id=21033 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? Case scope id: short-fact-099. Scoped answer summary fo...
  2. score=53.268201 chunk_id=21035 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? document short-snow-orchard-storehouse-profile-page-099...
  3. score=53.250590 chunk_id=21034 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Lev's profile page? document short-snow-orchard-storehouse-profile-page-099...
  4. score=50.246055 chunk_id=20734 preview=document short-snow-orchard-storehouse-profile-page-099::short-fact-099: In document short-snow-orchard-storehouse-profile-page-099, the verified archive not...
  5. score=13.599453 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
- Matched markers: Snow Orchard storehouse, profile page, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Snow Orchard storehouse, profile page, silver booth token.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 100 - short-fact-100
Question: Which small object in the cedar tube proved that Ada stopped at Bell Bridge square?

Expected evidence:
- clay watering cup
- Bell Bridge square

Expected distractors:
- wrong coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=14.110007 chunk_id=20902 preview=Question anchor: Which small object in the cedar tube proved that Lina stopped at Bell Bridge square? document short-bell-bridge-square-festival-minutes-010:...
  2. score=5.635767 chunk_id=20662 preview=document short-bell-bridge-square-winter-letter-060::short-fact-060: In document short-bell-bridge-square-winter-letter-060, the verified archive note record...
  3. score=5.594996 chunk_id=20976 preview=Question anchor: Which item did Ada tuck inside the cedar tube mentioned in the winter letter? document short-bell-bridge-square-winter-letter-060::short-fac...
  4. score=5.411683 chunk_id=20655 preview=document short-bell-bridge-square-field-recording-090::short-fact-090: In document short-bell-bridge-square-field-recording-090, the verified archive note re...
- Matched markers: Bell Bridge square
- Missing markers: clay watering cup
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: Bell Bridge square. Missing: clay watering cup.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.024364 chunk_id=21036 preview=Question anchor: Which small object in the cedar tube proved that Ada stopped at Bell Bridge square? Case scope id: short-fact-100. Scoped answer summary for...
  2. score=13.885600 chunk_id=20947 preview=Question anchor: Which small object in the cedar tube proved that Mira stopped at Bell Bridge square? document short-bell-bridge-square-station-transcript-04...
  3. score=13.872303 chunk_id=20902 preview=Question anchor: Which small object in the cedar tube proved that Lina stopped at Bell Bridge square? document short-bell-bridge-square-festival-minutes-010:...
- Matched markers: Bell Bridge square, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Bell Bridge square, clay watering cup.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 101 - short-fact-101
Question: Which direct fact from the festival minutes identifies the item recorded for Nikola at Glass Harbor quay?

Expected evidence:
- juniper bundles

Expected distractors:
- wrong violet ribbon

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.309966 chunk_id=20688 preview=document short-glass-harbor-quay-festival-minutes-101::short-fact-101: In document short-glass-harbor-quay-festival-minutes-101, the verified archive note re...
  2. score=1.814295 chunk_id=20708 preview=document short-moss-archive-room-festival-minutes-017::short-fact-017: In document short-moss-archive-room-festival-minutes-017, the verified archive note re...
  3. score=1.738382 chunk_id=20694 preview=document short-glass-harbor-quay-winter-letter-011::short-fact-011: In document short-glass-harbor-quay-winter-letter-011, the verified archive note records...
  4. score=1.644994 chunk_id=20691 preview=document short-glass-harbor-quay-profile-page-071::short-fact-071: In document short-glass-harbor-quay-profile-page-071, the verified archive note records br...
  5. score=1.644994 chunk_id=20689 preview=document short-glass-harbor-quay-field-recording-041::short-fact-041: In document short-glass-harbor-quay-field-recording-041, the verified archive note reco...
- Matched markers: juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.283245 chunk_id=20688 preview=document short-glass-harbor-quay-festival-minutes-101::short-fact-101: In document short-glass-harbor-quay-festival-minutes-101, the verified archive note re...
  2. score=1.324143 chunk_id=20918 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
  3. score=1.305329 chunk_id=20685 preview=document short-glass-harbor-quay-audio-reel-021::short-fact-021: In document short-glass-harbor-quay-audio-reel-021, the verified archive note records tuning...
  4. score=1.290376 chunk_id=20917 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
  5. score=1.128203 chunk_id=21053 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
- Matched markers: juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 102 - short-fact-102
Question: Which item did Raisa tuck inside the cedar tube mentioned in the winter letter?

Expected evidence:
- smoke vent chain
- cedar tube

Expected distractors:
- wrong tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.098817 chunk_id=21038 preview=Question anchor: Which item did Raisa tuck inside the cedar tube mentioned in the winter letter? Case scope id: short-fact-102. Scoped answer summary for sho...
  2. score=10.048010 chunk_id=20662 preview=document short-bell-bridge-square-winter-letter-060::short-fact-060: In document short-bell-bridge-square-winter-letter-060, the verified archive note record...
  3. score=10.036803 chunk_id=20976 preview=Question anchor: Which item did Ada tuck inside the cedar tube mentioned in the winter letter? document short-bell-bridge-square-winter-letter-060::short-fac...
  4. score=9.960257 chunk_id=20727 preview=document short-north-bell-workshop-winter-letter-018::short-fact-018: In document short-north-bell-workshop-winter-letter-018, the verified archive note reco...
- Matched markers: cedar tube, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, smoke vent chain.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.972535 chunk_id=21038 preview=Question anchor: Which item did Raisa tuck inside the cedar tube mentioned in the winter letter? Case scope id: short-fact-102. Scoped answer summary for sho...
  2. score=41.002623 chunk_id=21039 preview=Question anchor: Which item did Raisa tuck inside the cedar tube mentioned in the winter letter? document short-south-meadow-arch-winter-letter-102::short-fa...
  3. score=37.924291 chunk_id=20751 preview=document short-south-meadow-arch-winter-letter-102::short-fact-102: In document short-south-meadow-arch-winter-letter-102, the verified archive note records...
  4. score=9.797871 chunk_id=20976 preview=Question anchor: Which item did Ada tuck inside the cedar tube mentioned in the winter letter? document short-bell-bridge-square-winter-letter-060::short-fac...
  5. score=9.762169 chunk_id=20662 preview=document short-bell-bridge-square-winter-letter-060::short-fact-060: In document short-bell-bridge-square-winter-letter-060, the verified archive note record...
- Matched markers: cedar tube, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, smoke vent chain.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 103 - short-fact-103
Question: What object and color detail identified Galen's keepsake at Hollow Market arcade?

Expected evidence:
- saffron brass compass

Expected distractors:
- wrong rope bridge permit

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.934627 chunk_id=20705 preview=document short-hollow-market-arcade-station-transcript-103::short-fact-103: In document short-hollow-market-arcade-station-transcript-103, the verified archi...
  2. score=1.359657 chunk_id=20981 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel? document short-hollow-market-arcade-audio-reel-063::short-...
  3. score=1.327694 chunk_id=20696 preview=document short-hollow-market-arcade-audio-reel-063::short-fact-063: In document short-hollow-market-arcade-audio-reel-063, the verified archive note records...
  4. score=1.211544 chunk_id=20936 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Rafi's station transcript? document short-hollow-market-arcade-station-transcr...
  5. score=1.209868 chunk_id=20704 preview=document short-hollow-market-arcade-station-transcript-033::short-fact-033: In document short-hollow-market-arcade-station-transcript-033, the verified archi...
- Matched markers: saffron brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron brass compass.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.702130 chunk_id=20705 preview=document short-hollow-market-arcade-station-transcript-103::short-fact-103: In document short-hollow-market-arcade-station-transcript-103, the verified archi...
  2. score=1.543132 chunk_id=20698 preview=document short-hollow-market-arcade-field-recording-013::short-fact-013: In document short-hollow-market-arcade-field-recording-013, the verified archive not...
  3. score=1.475739 chunk_id=20700 preview=document short-hollow-market-arcade-profile-page-043::short-fact-043: In document short-hollow-market-arcade-profile-page-043, the verified archive note reco...
  4. score=1.023613 chunk_id=20981 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel? document short-hollow-market-arcade-audio-reel-063::short-...
  5. score=1.009303 chunk_id=20980 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Galen's audio reel? document short-hollow-market-arcade-audio-reel-063::short-...
- Matched markers: saffron brass compass
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron brass compass.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 104 - short-fact-104
Question: Which fact in the field recording shows what Sonya's older sister left near Winter Chapel porch?

Expected evidence:
- linen wick
- older sister

Expected distractors:
- wrong oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.638746 chunk_id=21040 preview=Question anchor: Which fact in the field recording shows what Sonya's older sister left near Winter Chapel porch? Case scope id: short-fact-104. Scoped answe...
  2. score=41.608122 chunk_id=21041 preview=Question anchor: Which fact in the field recording shows what Sonya's older sister left near Winter Chapel porch? document short-winter-chapel-porch-field-re...
  3. score=38.610441 chunk_id=20757 preview=document short-winter-chapel-porch-field-recording-104::short-fact-104: In document short-winter-chapel-porch-field-recording-104, the verified archive note...
  4. score=1.817798 chunk_id=20906 preview=Question anchor: Which fact in the audio reel shows what Daria's twin sister left near Winter Chapel porch? document short-winter-chapel-porch-audio-reel-014...
  5. score=1.756349 chunk_id=20752 preview=document short-winter-chapel-porch-audio-reel-014::short-fact-014: In document short-winter-chapel-porch-audio-reel-014, the verified archive note records bl...
- Matched markers: linen wick, older sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: linen wick, older sister.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.385082 chunk_id=21040 preview=Question anchor: Which fact in the field recording shows what Sonya's older sister left near Winter Chapel porch? Case scope id: short-fact-104. Scoped answe...
  2. score=41.416238 chunk_id=21041 preview=Question anchor: Which fact in the field recording shows what Sonya's older sister left near Winter Chapel porch? document short-winter-chapel-porch-field-re...
  3. score=38.364879 chunk_id=20757 preview=document short-winter-chapel-porch-field-recording-104::short-fact-104: In document short-winter-chapel-porch-field-recording-104, the verified archive note...
  4. score=1.669212 chunk_id=20906 preview=Question anchor: Which fact in the audio reel shows what Daria's twin sister left near Winter Chapel porch? document short-winter-chapel-porch-audio-reel-014...
  5. score=1.530770 chunk_id=20996 preview=Question anchor: Which fact in the winter letter shows what Nessa's cousin left near Winter Chapel porch? document short-winter-chapel-porch-winter-letter-07...
- Matched markers: linen wick, older sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: linen wick, older sister.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 105 - short-fact-105
Question: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel?

Expected evidence:
- star ledger page
- Driftwood cove
- audio reel

Expected distractors:
- wrong blue glass jar

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.035506 chunk_id=21042 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel? Case scope id: short-fact-105. Scoped answer summary for short-f...
  2. score=53.065367 chunk_id=21044 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel? document short-driftwood-cove-audio-reel-105::short-fact-105: In...
  3. score=53.015912 chunk_id=21043 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel? document short-driftwood-cove-audio-reel-105::short-fact-105: In...
  4. score=50.034944 chunk_id=20675 preview=document short-driftwood-cove-audio-reel-105::short-fact-105: In document short-driftwood-cove-audio-reel-105, the verified archive note records star ledger...
  5. score=13.485795 chunk_id=20998 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
- Matched markers: Driftwood cove, audio reel, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Driftwood cove, audio reel, star ledger page.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=76.950233 chunk_id=21042 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel? Case scope id: short-fact-105. Scoped answer summary for short-f...
  2. score=52.996242 chunk_id=21044 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel? document short-driftwood-cove-audio-reel-105::short-fact-105: In...
  3. score=52.948286 chunk_id=21043 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Pavel's audio reel? document short-driftwood-cove-audio-reel-105::short-fact-105: In...
  4. score=49.931960 chunk_id=20675 preview=document short-driftwood-cove-audio-reel-105::short-fact-105: In document short-driftwood-cove-audio-reel-105, the verified archive note records star ledger...
  5. score=13.478743 chunk_id=20999 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
- Matched markers: Driftwood cove, audio reel, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Driftwood cove, audio reel, star ledger page.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 106 - short-fact-106
Question: Which small object in the cedar tube proved that Talia stopped at Cloud Wharf office?

Expected evidence:
- lantern hook
- Cloud Wharf office

Expected distractors:
- wrong canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=41.286549 chunk_id=21046 preview=Question anchor: Which small object in the cedar tube proved that Talia stopped at Cloud Wharf office? document short-cloud-wharf-office-profile-page-106::sh...
  2. score=14.138306 chunk_id=20956 preview=Question anchor: Which small object in the cedar tube proved that Kira stopped at Cloud Wharf office? document short-cloud-wharf-office-winter-letter-046::sh...
  3. score=5.701756 chunk_id=20664 preview=document short-cloud-wharf-office-festival-minutes-066::short-fact-066: In document short-cloud-wharf-office-festival-minutes-066, the verified archive note...
  4. score=5.558638 chunk_id=20671 preview=document short-cloud-wharf-office-station-transcript-096::short-fact-096: In document short-cloud-wharf-office-station-transcript-096, the verified archive n...
- Matched markers: Cloud Wharf office, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.078124 chunk_id=21045 preview=Question anchor: Which small object in the cedar tube proved that Talia stopped at Cloud Wharf office? Case scope id: short-fact-106. Scoped answer summary f...
  2. score=41.078048 chunk_id=21046 preview=Question anchor: Which small object in the cedar tube proved that Talia stopped at Cloud Wharf office? document short-cloud-wharf-office-profile-page-106::sh...
  3. score=13.955910 chunk_id=20956 preview=Question anchor: Which small object in the cedar tube proved that Kira stopped at Cloud Wharf office? document short-cloud-wharf-office-winter-letter-046::sh...
  4. score=13.949042 chunk_id=21001 preview=Question anchor: Which small object in the cedar tube proved that Zora stopped at Cloud Wharf office? document short-cloud-wharf-office-field-recording-076::...
- Matched markers: Cloud Wharf office, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Cloud Wharf office, lantern hook.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 107 - short-fact-107
Question: Which direct fact from the river diary page identifies the item recorded for Emil at Moss Archive room?

Expected evidence:
- weathered camera strap

Expected distractors:
- wrong cedar shovel

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.381238 chunk_id=20714 preview=document short-moss-archive-room-river-diary-page-107::short-fact-107: In document short-moss-archive-room-river-diary-page-107, the verified archive note re...
  2. score=1.927607 chunk_id=20715 preview=document short-moss-archive-room-station-transcript-047::short-fact-047: In document short-moss-archive-room-station-transcript-047, the verified archive not...
  3. score=1.877046 chunk_id=20681 preview=document short-driftwood-cove-river-diary-page-065::short-fact-065: In document short-driftwood-cove-river-diary-page-065, the verified archive note records...
  4. score=1.826731 chunk_id=20702 preview=document short-hollow-market-arcade-river-diary-page-023::short-fact-023: In document short-hollow-market-arcade-river-diary-page-023, the verified archive n...
  5. score=1.557673 chunk_id=20733 preview=document short-snow-orchard-storehouse-profile-page-029::short-fact-029: In document short-snow-orchard-storehouse-profile-page-029, the verified archive not...
- Matched markers: weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.441043 chunk_id=20714 preview=document short-moss-archive-room-river-diary-page-107::short-fact-107: In document short-moss-archive-room-river-diary-page-107, the verified archive note re...
  2. score=1.537377 chunk_id=20713 preview=document short-moss-archive-room-river-diary-page-037::short-fact-037: In document short-moss-archive-room-river-diary-page-037, the verified archive note re...
  3. score=1.222326 chunk_id=20703 preview=document short-hollow-market-arcade-river-diary-page-093::short-fact-093: In document short-hollow-market-arcade-river-diary-page-093, the verified archive n...
  4. score=1.198523 chunk_id=20972 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Oren's profile page? document short-moss-archive-room-profile-page-057::short-fac...
  5. score=1.191025 chunk_id=21026 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
- Matched markers: weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: weathered camera strap.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 108 - short-fact-108
Question: Which item did Runa tuck inside the cedar tube mentioned in the festival minutes?

Expected evidence:
- wax thread
- cedar tube

Expected distractors:
- wrong copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.190670 chunk_id=21047 preview=Question anchor: Which item did Runa tuck inside the cedar tube mentioned in the festival minutes? Case scope id: short-fact-108. Scoped answer summary for s...
  2. score=41.201294 chunk_id=21048 preview=Question anchor: Which item did Runa tuck inside the cedar tube mentioned in the festival minutes? document short-north-bell-workshop-festival-minutes-108::s...
  3. score=38.185189 chunk_id=20721 preview=document short-north-bell-workshop-festival-minutes-108::short-fact-108: In document short-north-bell-workshop-festival-minutes-108, the verified archive not...
  4. score=9.987193 chunk_id=20754 preview=document short-winter-chapel-porch-festival-minutes-024::short-fact-024: In document short-winter-chapel-porch-festival-minutes-024, the verified archive not...
  5. score=9.976962 chunk_id=20922 preview=Question anchor: Which item did Sonya tuck inside the cedar tube mentioned in the festival minutes? document short-winter-chapel-porch-festival-minutes-024::...
- Matched markers: cedar tube, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.991344 chunk_id=21047 preview=Question anchor: Which item did Runa tuck inside the cedar tube mentioned in the festival minutes? Case scope id: short-fact-108. Scoped answer summary for s...
  2. score=41.039509 chunk_id=21048 preview=Question anchor: Which item did Runa tuck inside the cedar tube mentioned in the festival minutes? document short-north-bell-workshop-festival-minutes-108::s...
  3. score=9.895592 chunk_id=20985 preview=Question anchor: Which item did Talia tuck inside the cedar tube mentioned in the festival minutes? document short-cloud-wharf-office-festival-minutes-066::s...
  4. score=9.887133 chunk_id=20922 preview=Question anchor: Which item did Sonya tuck inside the cedar tube mentioned in the festival minutes? document short-winter-chapel-porch-festival-minutes-024::...
  5. score=9.818375 chunk_id=20754 preview=document short-winter-chapel-porch-festival-minutes-024::short-fact-024: In document short-winter-chapel-porch-festival-minutes-024, the verified archive not...
- Matched markers: cedar tube, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, wax thread.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 109 - short-fact-109
Question: What object and color detail identified Viktor's keepsake at Snow Orchard storehouse?

Expected evidence:
- saffron tin key

Expected distractors:
- wrong moonflower cutting

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=1.796559 chunk_id=20736 preview=document short-snow-orchard-storehouse-river-diary-page-079::short-fact-079: In document short-snow-orchard-storehouse-river-diary-page-079, the verified arc...
  2. score=1.279503 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  3. score=1.271450 chunk_id=20732 preview=document short-snow-orchard-storehouse-field-recording-069::short-fact-069: In document short-snow-orchard-storehouse-field-recording-069, the verified archi...
  4. score=1.263858 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  5. score=1.094454 chunk_id=20945 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter? document short-snow-orchard-storehouse-winter-letter...
- Matched markers: none
- Missing markers: saffron tin key
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.803634 chunk_id=20740 preview=document short-snow-orchard-storehouse-winter-letter-109::short-fact-109: In document short-snow-orchard-storehouse-winter-letter-109, the verified archive n...
  2. score=1.592432 chunk_id=20737 preview=document short-snow-orchard-storehouse-station-transcript-019::short-fact-019: In document short-snow-orchard-storehouse-station-transcript-019, the verified...
  3. score=1.184127 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  4. score=1.153306 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  5. score=1.151730 chunk_id=20732 preview=document short-snow-orchard-storehouse-field-recording-069::short-fact-069: In document short-snow-orchard-storehouse-field-recording-069, the verified archi...
- Matched markers: saffron tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron tin key.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 110 - short-fact-110
Question: Which fact in the station transcript shows what Selma's twin sister left near Bell Bridge square?

Expected evidence:
- blue oar
- twin sister

Expected distractors:
- wrong birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.564704 chunk_id=21049 preview=Question anchor: Which fact in the station transcript shows what Selma's twin sister left near Bell Bridge square? Case scope id: short-fact-110. Scoped answ...
  2. score=41.548022 chunk_id=21050 preview=Question anchor: Which fact in the station transcript shows what Selma's twin sister left near Bell Bridge square? document short-bell-bridge-square-station-...
  3. score=38.538350 chunk_id=20661 preview=document short-bell-bridge-square-station-transcript-110::short-fact-110: In document short-bell-bridge-square-station-transcript-110, the verified archive n...
  4. score=1.768987 chunk_id=21005 preview=Question anchor: Which fact in the festival minutes shows what Mira's older sister left near Bell Bridge square? document short-bell-bridge-square-festival-m...
  5. score=1.629751 chunk_id=20915 preview=Question anchor: Which fact in the field recording shows what Ada's stepfather left near Bell Bridge square? document short-bell-bridge-square-field-recordin...
- Matched markers: blue oar, twin sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, twin sister.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.387422 chunk_id=21049 preview=Question anchor: Which fact in the station transcript shows what Selma's twin sister left near Bell Bridge square? Case scope id: short-fact-110. Scoped answ...
  2. score=41.415967 chunk_id=21050 preview=Question anchor: Which fact in the station transcript shows what Selma's twin sister left near Bell Bridge square? document short-bell-bridge-square-station-...
  3. score=38.362050 chunk_id=20661 preview=document short-bell-bridge-square-station-transcript-110::short-fact-110: In document short-bell-bridge-square-station-transcript-110, the verified archive n...
  4. score=1.346113 chunk_id=20660 preview=document short-bell-bridge-square-station-transcript-040::short-fact-040: In document short-bell-bridge-square-station-transcript-040, the verified archive n...
  5. score=1.005712 chunk_id=20659 preview=document short-bell-bridge-square-river-diary-page-100::short-fact-100: In document short-bell-bridge-square-river-diary-page-100, the verified archive note...
- Matched markers: blue oar, twin sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, twin sister.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 111 - short-fact-111
Question: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording?

Expected evidence:
- willow basket
- Glass Harbor quay
- field recording

Expected distractors:
- wrong saffron scarf

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.313957 chunk_id=21051 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? Case scope id: short-fact-111. Scoped answer summary for...
  2. score=53.346217 chunk_id=21052 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
  3. score=53.292604 chunk_id=21053 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
  4. score=50.298342 chunk_id=20690 preview=document short-glass-harbor-quay-field-recording-111::short-fact-111: In document short-glass-harbor-quay-field-recording-111, the verified archive note reco...
  5. score=9.462226 chunk_id=20926 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
- Matched markers: Glass Harbor quay, field recording, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Glass Harbor quay, field recording, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.198958 chunk_id=21051 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? Case scope id: short-fact-111. Scoped answer summary for...
  2. score=53.222122 chunk_id=21053 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
  3. score=53.198897 chunk_id=21052 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Damir's field recording? document short-glass-harbor-quay-field-recording-111::sh...
  4. score=13.756932 chunk_id=20917 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
  5. score=13.755572 chunk_id=20918 preview=Question anchor: What exact keepsake was listed beside Glass Harbor quay in Nikola's audio reel? document short-glass-harbor-quay-audio-reel-021::short-fact-...
- Matched markers: Glass Harbor quay, field recording, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Glass Harbor quay, field recording, willow basket.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 112 - short-fact-112
Question: Which small object in the cedar tube proved that Iveta stopped at South Meadow arch?

Expected evidence:
- paper moon mask
- South Meadow arch

Expected distractors:
- wrong carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.258441 chunk_id=21054 preview=Question anchor: Which small object in the cedar tube proved that Iveta stopped at South Meadow arch? Case scope id: short-fact-112. Scoped answer summary fo...
  2. score=41.261019 chunk_id=21055 preview=Question anchor: Which small object in the cedar tube proved that Iveta stopped at South Meadow arch? document short-south-meadow-arch-audio-reel-112::short-...
  3. score=14.161339 chunk_id=20965 preview=Question anchor: Which small object in the cedar tube proved that Anya stopped at South Meadow arch? document short-south-meadow-arch-festival-minutes-052::s...
  4. score=14.127778 chunk_id=20743 preview=document short-south-meadow-arch-festival-minutes-052::short-fact-052: In document short-south-meadow-arch-festival-minutes-052, the verified archive note re...
  5. score=5.664292 chunk_id=20747 preview=document short-south-meadow-arch-river-diary-page-072::short-fact-072: In document short-south-meadow-arch-river-diary-page-072, the verified archive note re...
- Matched markers: South Meadow arch, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: South Meadow arch, paper moon mask.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.130424 chunk_id=21054 preview=Question anchor: Which small object in the cedar tube proved that Iveta stopped at South Meadow arch? Case scope id: short-fact-112. Scoped answer summary fo...
  2. score=41.131360 chunk_id=21055 preview=Question anchor: Which small object in the cedar tube proved that Iveta stopped at South Meadow arch? document short-south-meadow-arch-audio-reel-112::short-...
  3. score=38.098383 chunk_id=20742 preview=document short-south-meadow-arch-audio-reel-112::short-fact-112: In document short-south-meadow-arch-audio-reel-112, the verified archive note records paper...
  4. score=13.927421 chunk_id=20965 preview=Question anchor: Which small object in the cedar tube proved that Anya stopped at South Meadow arch? document short-south-meadow-arch-festival-minutes-052::s...
  5. score=13.925317 chunk_id=21010 preview=Question anchor: Which small object in the cedar tube proved that Elena stopped at South Meadow arch? document short-south-meadow-arch-station-transcript-082...
- Matched markers: South Meadow arch, paper moon mask
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: South Meadow arch, paper moon mask.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 113 - short-fact-113
Question: Which direct fact from the profile page identifies the item recorded for Rafi at Hollow Market arcade?

Expected evidence:
- glass ink bottle

Expected distractors:
- wrong amber lantern

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.512867 chunk_id=20701 preview=document short-hollow-market-arcade-profile-page-113::short-fact-113: In document short-hollow-market-arcade-profile-page-113, the verified archive note reco...
  2. score=2.049206 chunk_id=20702 preview=document short-hollow-market-arcade-river-diary-page-023::short-fact-023: In document short-hollow-market-arcade-river-diary-page-023, the verified archive n...
  3. score=1.538551 chunk_id=20700 preview=document short-hollow-market-arcade-profile-page-043::short-fact-043: In document short-hollow-market-arcade-profile-page-043, the verified archive note reco...
  4. score=1.423679 chunk_id=21026 preview=Question anchor: What exact keepsake was listed beside Hollow Market arcade in Marek's river diary page? document short-hollow-market-arcade-river-diary-page...
  5. score=1.414969 chunk_id=20703 preview=document short-hollow-market-arcade-river-diary-page-093::short-fact-093: In document short-hollow-market-arcade-river-diary-page-093, the verified archive n...
- Matched markers: glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.159702 chunk_id=20701 preview=document short-hollow-market-arcade-profile-page-113::short-fact-113: In document short-hollow-market-arcade-profile-page-113, the verified archive note reco...
  2. score=0.767470 chunk_id=20712 preview=document short-moss-archive-room-profile-page-057::short-fact-057: In document short-moss-archive-room-profile-page-057, the verified archive note records ca...
  3. score=0.759298 chunk_id=20734 preview=document short-snow-orchard-storehouse-profile-page-099::short-fact-099: In document short-snow-orchard-storehouse-profile-page-099, the verified archive not...
  4. score=0.759298 chunk_id=20679 preview=document short-driftwood-cove-profile-page-015::short-fact-015: In document short-driftwood-cove-profile-page-015, the verified archive note records willow b...
- Matched markers: glass ink bottle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (3 vs 4).

### Question 114 - short-fact-114
Question: Which item did Nessa tuck inside the cedar tube mentioned in the river diary page?

Expected evidence:
- copper wind vane pin
- cedar tube

Expected distractors:
- wrong basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.287736 chunk_id=21056 preview=Question anchor: Which item did Nessa tuck inside the cedar tube mentioned in the river diary page? Case scope id: short-fact-114. Scoped answer summary for...
  2. score=41.271397 chunk_id=21057 preview=Question anchor: Which item did Nessa tuck inside the cedar tube mentioned in the river diary page? document short-winter-chapel-porch-river-diary-page-114::...
  3. score=38.285642 chunk_id=20760 preview=document short-winter-chapel-porch-river-diary-page-114::short-fact-114: In document short-winter-chapel-porch-river-diary-page-114, the verified archive not...
  4. score=10.110257 chunk_id=20658 preview=document short-bell-bridge-square-river-diary-page-030::short-fact-030: In document short-bell-bridge-square-river-diary-page-030, the verified archive note...
  5. score=9.802010 chunk_id=20657 preview=document short-bell-bridge-square-profile-page-120::short-fact-120: In document short-bell-bridge-square-profile-page-120, the verified archive note records...
- Matched markers: cedar tube, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, copper wind vane pin.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.131638 chunk_id=21056 preview=Question anchor: Which item did Nessa tuck inside the cedar tube mentioned in the river diary page? Case scope id: short-fact-114. Scoped answer summary for...
  2. score=41.160900 chunk_id=21057 preview=Question anchor: Which item did Nessa tuck inside the cedar tube mentioned in the river diary page? document short-winter-chapel-porch-river-diary-page-114::...
  3. score=38.129067 chunk_id=20760 preview=document short-winter-chapel-porch-river-diary-page-114::short-fact-114: In document short-winter-chapel-porch-river-diary-page-114, the verified archive not...
  4. score=10.003273 chunk_id=20994 preview=Question anchor: Which item did Iveta tuck inside the cedar tube mentioned in the river diary page? document short-south-meadow-arch-river-diary-page-072::sh...
  5. score=10.003273 chunk_id=20931 preview=Question anchor: Which item did Selma tuck inside the cedar tube mentioned in the river diary page? document short-bell-bridge-square-river-diary-page-030::s...
- Matched markers: cedar tube, copper wind vane pin
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar tube, copper wind vane pin.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 115 - short-fact-115
Question: What object and color detail identified Anton's keepsake at Driftwood cove?

Expected evidence:
- saffron coal stove hiss

Expected distractors:
- wrong green apron

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=1.540098 chunk_id=20678 preview=document short-driftwood-cove-field-recording-055::short-fact-055: In document short-driftwood-cove-field-recording-055, the verified archive note records sa...
  2. score=1.414900 chunk_id=20680 preview=document short-driftwood-cove-profile-page-085::short-fact-085: In document short-driftwood-cove-profile-page-085, the verified archive note records saffron...
  3. score=0.995577 chunk_id=20999 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
  4. score=0.981685 chunk_id=20682 preview=document short-driftwood-cove-station-transcript-075::short-fact-075: In document short-driftwood-cove-station-transcript-075, the verified archive note reco...
  5. score=0.939145 chunk_id=20998 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
- Matched markers: none
- Missing markers: saffron coal stove hiss
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=25.581025 chunk_id=20677 preview=document short-driftwood-cove-festival-minutes-115::short-fact-115: In document short-driftwood-cove-festival-minutes-115, the verified archive note records...
  2. score=1.451292 chunk_id=20680 preview=document short-driftwood-cove-profile-page-085::short-fact-085: In document short-driftwood-cove-profile-page-085, the verified archive note records saffron...
  3. score=1.437398 chunk_id=20678 preview=document short-driftwood-cove-field-recording-055::short-fact-055: In document short-driftwood-cove-field-recording-055, the verified archive note records sa...
  4. score=1.435609 chunk_id=20683 preview=document short-driftwood-cove-winter-letter-025::short-fact-025: In document short-driftwood-cove-winter-letter-025, the verified archive note records saffro...
  5. score=1.005187 chunk_id=20999 preview=Question anchor: What exact keepsake was listed beside Driftwood cove in Anton's station transcript? document short-driftwood-cove-station-transcript-075::sh...
- Matched markers: saffron coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: saffron coal stove hiss.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 116 - short-fact-116
Question: Which fact in the winter letter shows what Zora's stepfather left near Cloud Wharf office?

Expected evidence:
- violet ribbon
- stepfather

Expected distractors:
- wrong silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.531655 chunk_id=21058 preview=Question anchor: Which fact in the winter letter shows what Zora's stepfather left near Cloud Wharf office? Case scope id: short-fact-116. Scoped answer summ...
  2. score=41.536950 chunk_id=21059 preview=Question anchor: Which fact in the winter letter shows what Zora's stepfather left near Cloud Wharf office? document short-cloud-wharf-office-winter-letter-1...
  3. score=38.537537 chunk_id=20673 preview=document short-cloud-wharf-office-winter-letter-116::short-fact-116: In document short-cloud-wharf-office-winter-letter-116, the verified archive note record...
  4. score=1.760429 chunk_id=21014 preview=Question anchor: Which fact in the river diary page shows what Kira's twin sister left near Cloud Wharf office? document short-cloud-wharf-office-river-diary...
  5. score=1.610384 chunk_id=20672 preview=document short-cloud-wharf-office-winter-letter-046::short-fact-046: In document short-cloud-wharf-office-winter-letter-046, the verified archive note record...
- Matched markers: stepfather, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: stepfather, violet ribbon.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.311215 chunk_id=21058 preview=Question anchor: Which fact in the winter letter shows what Zora's stepfather left near Cloud Wharf office? Case scope id: short-fact-116. Scoped answer summ...
  2. score=41.329058 chunk_id=21059 preview=Question anchor: Which fact in the winter letter shows what Zora's stepfather left near Cloud Wharf office? document short-cloud-wharf-office-winter-letter-1...
  3. score=38.296990 chunk_id=20673 preview=document short-cloud-wharf-office-winter-letter-116::short-fact-116: In document short-cloud-wharf-office-winter-letter-116, the verified archive note record...
  4. score=1.427740 chunk_id=20924 preview=Question anchor: Which fact in the station transcript shows what Talia's cousin left near Cloud Wharf office? document short-cloud-wharf-office-station-trans...
  5. score=1.356095 chunk_id=20672 preview=document short-cloud-wharf-office-winter-letter-046::short-fact-046: In document short-cloud-wharf-office-winter-letter-046, the verified archive note record...
- Matched markers: stepfather, violet ribbon
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: stepfather, violet ribbon.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 117 - short-fact-117
Question: What exact keepsake was listed beside Moss Archive room in Milan's station transcript?

Expected evidence:
- tuning fork
- Moss Archive room
- station transcript

Expected distractors:
- wrong clay watering cup

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=76.876288 chunk_id=21060 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Milan's station transcript? Case scope id: short-fact-117. Scoped answer summary...
  2. score=52.909316 chunk_id=21061 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Milan's station transcript? document short-moss-archive-room-station-transcript-1...
  3. score=52.892232 chunk_id=21062 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Milan's station transcript? document short-moss-archive-room-station-transcript-1...
  4. score=13.478845 chunk_id=21016 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Soren's festival minutes? document short-moss-archive-room-festival-minutes-087::...
  5. score=13.445092 chunk_id=20926 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
- Matched markers: Moss Archive room, station transcript, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moss Archive room, station transcript, tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=77.163331 chunk_id=21060 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Milan's station transcript? Case scope id: short-fact-117. Scoped answer summary...
  2. score=53.187016 chunk_id=21061 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Milan's station transcript? document short-moss-archive-room-station-transcript-1...
  3. score=53.181833 chunk_id=21062 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Milan's station transcript? document short-moss-archive-room-station-transcript-1...
  4. score=50.128120 chunk_id=20716 preview=document short-moss-archive-room-station-transcript-117::short-fact-117: In document short-moss-archive-room-station-transcript-117, the verified archive not...
  5. score=13.603293 chunk_id=20926 preview=Question anchor: What exact keepsake was listed beside Moss Archive room in Emil's field recording? document short-moss-archive-room-field-recording-027::sho...
- Matched markers: Moss Archive room, station transcript, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Moss Archive room, station transcript, tuning fork.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 118 - short-fact-118
Question: Which small object in the cedar tube proved that Ilia stopped at North Bell workshop?

Expected evidence:
- rope bridge permit
- North Bell workshop

Expected distractors:
- wrong juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=5.501385 chunk_id=20724 preview=document short-north-bell-workshop-profile-page-078::short-fact-078: In document short-north-bell-workshop-profile-page-078, the verified archive note record...
  2. score=1.048542 chunk_id=20655 preview=document short-bell-bridge-square-field-recording-090::short-fact-090: In document short-bell-bridge-square-field-recording-090, the verified archive note re...
- Matched markers: North Bell workshop
- Missing markers: rope bridge permit
- Distractors: none
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: North Bell workshop. Missing: rope bridge permit.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.182554 chunk_id=21063 preview=Question anchor: Which small object in the cedar tube proved that Ilia stopped at North Bell workshop? Case scope id: short-fact-118. Scoped answer summary f...
  2. score=41.181535 chunk_id=21064 preview=Question anchor: Which small object in the cedar tube proved that Ilia stopped at North Bell workshop? document short-north-bell-workshop-field-recording-118...
  3. score=38.157678 chunk_id=20723 preview=document short-north-bell-workshop-field-recording-118::short-fact-118: In document short-north-bell-workshop-field-recording-118, the verified archive note...
  4. score=14.023104 chunk_id=21019 preview=Question anchor: Which small object in the cedar tube proved that Nadia stopped at North Bell workshop? document short-north-bell-workshop-winter-letter-088:...
  5. score=14.008194 chunk_id=20929 preview=Question anchor: Which small object in the cedar tube proved that Runa stopped at North Bell workshop? document short-north-bell-workshop-audio-reel-028::sho...
- Matched markers: North Bell workshop, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: North Bell workshop, rope bridge permit.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

### Question 119 - short-fact-119
Question: Which direct fact from the audio reel identifies the item recorded for Vesna at Snow Orchard storehouse?

Expected evidence:
- oak barrel hoops

Expected distractors:
- wrong smoke vent chain

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.429681 chunk_id=20730 preview=document short-snow-orchard-storehouse-audio-reel-119::short-fact-119: In document short-snow-orchard-storehouse-audio-reel-119, the verified archive note re...
  2. score=1.787945 chunk_id=20731 preview=document short-snow-orchard-storehouse-festival-minutes-059::short-fact-059: In document short-snow-orchard-storehouse-festival-minutes-059, the verified arc...
  3. score=1.737271 chunk_id=20733 preview=document short-snow-orchard-storehouse-profile-page-029::short-fact-029: In document short-snow-orchard-storehouse-profile-page-029, the verified archive not...
  4. score=1.726524 chunk_id=20738 preview=document short-snow-orchard-storehouse-station-transcript-089::short-fact-089: In document short-snow-orchard-storehouse-station-transcript-089, the verified...
  5. score=1.589949 chunk_id=20707 preview=document short-moss-archive-room-audio-reel-077::short-fact-077: In document short-moss-archive-room-audio-reel-077, the verified archive note records tin ke...
- Matched markers: oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=26.084188 chunk_id=20730 preview=document short-snow-orchard-storehouse-audio-reel-119::short-fact-119: In document short-snow-orchard-storehouse-audio-reel-119, the verified archive note re...
  2. score=1.223286 chunk_id=20945 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Vesna's winter letter? document short-snow-orchard-storehouse-winter-letter...
  3. score=1.116341 chunk_id=20990 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
  4. score=1.096186 chunk_id=20732 preview=document short-snow-orchard-storehouse-field-recording-069::short-fact-069: In document short-snow-orchard-storehouse-field-recording-069, the verified archi...
  5. score=1.063869 chunk_id=20989 preview=Question anchor: What exact keepsake was listed beside Snow Orchard storehouse in Viktor's field recording? document short-snow-orchard-storehouse-field-reco...
- Matched markers: oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: oak barrel hoops.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 120 - short-fact-120
Question: Which item did Mira tuck inside the cedar tube mentioned in the profile page?

Expected evidence:
- blue glass jar
- cedar tube

Expected distractors:
- wrong brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=65.239610 chunk_id=21065 preview=Question anchor: Which item did Mira tuck inside the cedar tube mentioned in the profile page? Case scope id: short-fact-120. Scoped answer summary for short...
  2. score=41.263763 chunk_id=21066 preview=Question anchor: Which item did Mira tuck inside the cedar tube mentioned in the profile page? document short-bell-bridge-square-profile-page-120::short-fact...
  3. score=38.243137 chunk_id=20657 preview=document short-bell-bridge-square-profile-page-120::short-fact-120: In document short-bell-bridge-square-profile-page-120, the verified archive note records...
  4. score=10.011523 chunk_id=20724 preview=document short-north-bell-workshop-profile-page-078::short-fact-078: In document short-north-bell-workshop-profile-page-078, the verified archive note record...
  5. score=10.004995 chunk_id=21003 preview=Question anchor: Which item did Ilia tuck inside the cedar tube mentioned in the profile page? document short-north-bell-workshop-profile-page-078::short-fac...
- Matched markers: blue glass jar, cedar tube
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, cedar tube.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Top chunks:
  1. score=64.980498 chunk_id=21065 preview=Question anchor: Which item did Mira tuck inside the cedar tube mentioned in the profile page? Case scope id: short-fact-120. Scoped answer summary for short...
  2. score=41.023496 chunk_id=21066 preview=Question anchor: Which item did Mira tuck inside the cedar tube mentioned in the profile page? document short-bell-bridge-square-profile-page-120::short-fact...
  3. score=37.947613 chunk_id=20657 preview=document short-bell-bridge-square-profile-page-120::short-fact-120: In document short-bell-bridge-square-profile-page-120, the verified archive note records...
  4. score=9.749303 chunk_id=21003 preview=Question anchor: Which item did Ilia tuck inside the cedar tube mentioned in the profile page? document short-north-bell-workshop-profile-page-078::short-fac...
  5. score=9.712019 chunk_id=20940 preview=Question anchor: Which item did Zora tuck inside the cedar tube mentioned in the profile page? document short-cloud-wharf-office-profile-page-036::short-fact...
- Matched markers: blue glass jar, cedar tube
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, cedar tube.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Aggregate Results

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Question wins: 77
- Passed questions: 102
- Average evidence coverage: 0.8917
- Average first relevant rank: 1.0
- Total matched markers: 203
- Total missing markers: 18
- Total false-positive markers: 0
- Official metrics: {'hit_rate': 0.575, 'recall_at_k': 0.7611111111111111, 'mrr': 0.8416666666666667, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 29.296516666666665, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.7611111111111111, 'missing_expected_marker_count': 41, 'false_positive_count': 54}

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b`
- Question wins: 43
- Passed questions: 114
- Average evidence coverage: 0.9542
- Average first relevant rank: 1.0
- Total matched markers: 215
- Total missing markers: 6
- Total false-positive markers: 0
- Official metrics: {'hit_rate': 0.675, 'recall_at_k': 0.85, 'mrr': 0.8625, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 29.470408333333335, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.85, 'missing_expected_marker_count': 21, 'false_positive_count': 46}

### Runtime Activation
- Selected config: {'best_config_id': 'bge_m3', 'best_model_code': 'bge_m3', 'best_collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b', 'selected_metrics': {'hit_rate': 0.675, 'recall_at_k': 0.85, 'mrr': 0.8625, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 29.470408333333335, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.85, 'missing_expected_marker_count': 21, 'false_positive_count': 46}}
- Activated config: {'id': 2, 'profile_id': 6, 'model_code': 'bge_m3', 'collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b', 'top_k': 5, 'score_threshold': None, 'retrieval_mode': 'hybrid', 'source_eval_job_id': 150, 'source_eval_dataset_id': 'eternal-world-short-fact-v1'}
- Runtime retrieval verification: {'model_code': 'bge_m3', 'result_count': 2, 'qdrant_collection': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_short_fact_v1__6ee264026b', 'top_chunk_id': 20645}
