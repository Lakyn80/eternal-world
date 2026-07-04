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
- Timestamp: 2026-07-03T14:01:08.463282+00:00
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
- Archived Markdown: `/app/artifacts/real_question_eval/runs/20260703_140108Z_fake/real_question_eval_report.md`
- Archived JSON: `/app/artifacts/real_question_eval/runs/20260703_140108Z_fake/real_question_eval_result.json`
- Archived Summary Markdown: `/app/artifacts/real_question_eval/runs/20260703_140108Z_fake/real_question_eval_summary.md`
- Archived Summary JSON: `/app/artifacts/real_question_eval/runs/20260703_140108Z_fake/real_question_eval_summary.json`

## Client Question Breakdown
### Question 1 - page-level-attic-instructions
Question: Which two maintenance details on the attic instruction page explain how the lamp smoke was controlled?
- Final evaluated answer: Grounded by retrieved evidence for: linen wick, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: linen wick, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- smoke vent chain

Expected distractors:
- cellar coal scoop

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=linen wick, smoke vent chain missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=linen wick, smoke vent chain missing=none distractors=none

### Question 2 - page-level-river-meeting
Question: Which two details on the river meeting page explain why the delegation arrived late?
- Final evaluated answer: Grounded by retrieved evidence for: flooded footbridge, late telegraph reply.
- Correctness verdict: grounded
- Evidence used: flooded footbridge, late telegraph reply
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- flooded footbridge
- late telegraph reply

Expected distractors:
- harvest parade rumor

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=flooded footbridge, late telegraph reply missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=flooded footbridge, late telegraph reply missing=none distractors=none

### Question 3 - page-level-station-caretaker
Question: What page-level details from the station caretaker log explain the cold draft on the night round?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, cracked west window.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, cracked west window
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- coal stove hiss
- cracked west window

Expected distractors:
- sealed ticket drawer

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss, cracked west window missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, cracked west window missing=none distractors=none

### Question 4 - page-level-herbal-room
Question: Which page-level inventory details identify the winter shelf in the herbal room?
- Final evaluated answer: Grounded by retrieved evidence for: blue glass jar, juniper bundles.
- Correctness verdict: grounded
- Evidence used: blue glass jar, juniper bundles
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- juniper bundles
- blue glass jar

Expected distractors:
- summer nettle basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue glass jar, juniper bundles missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue glass jar, juniper bundles missing=none distractors=none

### Question 5 - page-level-watchtower
Question: Which details on the watchtower repair page identify the upper landing hardware?
- Final evaluated answer: Grounded by retrieved evidence for: iron rung, lantern hook.
- Correctness verdict: grounded
- Evidence used: iron rung, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- iron rung
- lantern hook

Expected distractors:
- rope bucket pulley

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=iron rung, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=iron rung, lantern hook missing=none distractors=none

### Question 6 - page-level-006
Question: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: godmother, violet ribbon, willow basket.
- Correctness verdict: grounded
- Evidence used: godmother, violet ribbon, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- godmother
- violet ribbon
- willow basket

Expected distractors:
- weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=godmother, violet ribbon, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=godmother, violet ribbon, willow basket missing=none distractors=none

### Question 7 - page-level-007
Question: Which longer-page details in the family note describe the family memory scene at River Lantern inn?
- Final evaluated answer: Grounded by retrieved evidence for: birch tea flask, green apron.
- Correctness verdict: grounded
- Evidence used: birch tea flask, green apron
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- green apron
- birch tea flask

Expected distractors:
- canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=birch tea flask, green apron missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=birch tea flask, green apron missing=none distractors=none

### Question 8 - page-level-008
Question: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning, paper moon mask, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning, paper moon mask, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.3333333333333333; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.33).
- What the losing model missed or got wrong: multilingual_e5_small missing paper moon mask, weathered camera strap
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- weathered camera strap
- Signal Lantern Morning

Expected distractors:
- brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.3333333333333333 matched=Signal Lantern Morning missing=paper moon mask, weathered camera strap distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, paper moon mask, weathered camera strap missing=none distractors=none

### Question 9 - page-level-009
Question: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: brass compass, canal route map, saffron scarf.
- Correctness verdict: grounded
- Evidence used: brass compass, canal route map, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing saffron scarf, canal route map, brass compass
- Distractors / false positives: none

Expected evidence:
- saffron scarf
- canal route map
- brass compass

Expected distractors:
- tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=saffron scarf, canal route map, brass compass distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=brass compass, canal route map, saffron scarf missing=none distractors=none

### Question 10 - page-level-010
Question: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: brass compass, wax thread.
- Correctness verdict: grounded
- Evidence used: brass compass, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- wax thread
- brass compass

Expected distractors:
- silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=brass compass, wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=brass compass, wax thread missing=none distractors=none

### Question 11 - page-level-011
Question: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from Harbor Glass corridor?
- Final evaluated answer: Grounded by retrieved evidence for: cedar shovel, tuning fork, younger brother.
- Correctness verdict: grounded
- Evidence used: cedar shovel, tuning fork, younger brother
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- younger brother
- cedar shovel
- tuning fork

Expected distractors:
- glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar shovel, tuning fork, younger brother missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar shovel, tuning fork, younger brother missing=none distractors=none

### Question 12 - page-level-012
Question: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: linen wick, silver booth token.
- Correctness verdict: grounded
- Evidence used: linen wick, silver booth token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- silver booth token

Expected distractors:
- carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=linen wick, silver booth token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=linen wick, silver booth token missing=none distractors=none

### Question 13 - page-level-013
Question: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn?
- Final evaluated answer: Grounded by retrieved evidence for: Canal Night, glass ink bottle, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: Canal Night, glass ink bottle, rope bridge permit
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- glass ink bottle
- Canal Night

Expected distractors:
- tin key

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Canal Night, glass ink bottle, rope bridge permit missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Canal Night, glass ink bottle, rope bridge permit missing=none distractors=none

### Question 14 - page-level-014
Question: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: carved shell comb, clay watering cup, tin key.
- Correctness verdict: grounded
- Evidence used: carved shell comb, clay watering cup, tin key
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing clay watering cup, carved shell comb, tin key
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- carved shell comb
- tin key

Expected distractors:
- copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=clay watering cup, carved shell comb, tin key distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=carved shell comb, clay watering cup, tin key missing=none distractors=none

### Question 15 - page-level-015
Question: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: copper wind vane pin, tin key.
- Correctness verdict: grounded
- Evidence used: copper wind vane pin, tin key
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 4).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- copper wind vane pin
- tin key

Expected distractors:
- star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=copper wind vane pin, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper wind vane pin, tin key missing=none distractors=none

### Question 16 - page-level-016
Question: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Star Basin gallery?
- Final evaluated answer: Grounded by retrieved evidence for: amber lantern, copper token, older sister.
- Correctness verdict: grounded
- Evidence used: amber lantern, copper token, older sister
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- older sister
- amber lantern
- copper token

Expected distractors:
- oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=amber lantern, copper token, older sister missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=amber lantern, copper token, older sister missing=none distractors=none

### Question 17 - page-level-017
Question: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor?
- Final evaluated answer: Grounded by retrieved evidence for: blue oar, star ledger page.
- Correctness verdict: grounded
- Evidence used: blue oar, star ledger page
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- star ledger page

Expected distractors:
- juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue oar, star ledger page missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue oar, star ledger page missing=none distractors=none

### Question 18 - page-level-018
Question: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning, moonflower cutting, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning, moonflower cutting, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- oak barrel hoops
- Signal Lantern Morning

Expected distractors:
- coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, moonflower cutting, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, moonflower cutting, oak barrel hoops missing=none distractors=none

### Question 19 - page-level-019
Question: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, juniper bundles, lantern hook.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, juniper bundles, lantern hook
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing lantern hook, juniper bundles, coal stove hiss
- Distractors / false positives: none

Expected evidence:
- lantern hook
- juniper bundles
- coal stove hiss

Expected distractors:
- basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=lantern hook, juniper bundles, coal stove hiss distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, juniper bundles, lantern hook missing=none distractors=none

### Question 20 - page-level-020
Question: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: blue glass jar, coal stove hiss.
- Correctness verdict: grounded
- Evidence used: blue glass jar, coal stove hiss
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- coal stove hiss

Expected distractors:
- willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue glass jar, coal stove hiss missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue glass jar, coal stove hiss missing=none distractors=none

### Question 21 - page-level-021
Question: Which details on the profile page identify how Elena and the school friend prepared for the winter coach from Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: basalt sketch, school friend, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: basalt sketch, school friend, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- school friend
- smoke vent chain
- basalt sketch

Expected distractors:
- birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=basalt sketch, school friend, smoke vent chain missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=basalt sketch, school friend, smoke vent chain missing=none distractors=none

### Question 22 - page-level-022
Question: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery?
- Final evaluated answer: Grounded by retrieved evidence for: violet ribbon, willow basket.
- Correctness verdict: grounded
- Evidence used: violet ribbon, willow basket
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (2 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- violet ribbon
- willow basket

Expected distractors:
- weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=violet ribbon, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=violet ribbon, willow basket missing=none distractors=none

### Question 23 - page-level-023
Question: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor?
- Final evaluated answer: Grounded by retrieved evidence for: Canal Night, birch tea flask, green apron.
- Correctness verdict: grounded
- Evidence used: Canal Night, birch tea flask, green apron
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.3333333333333333; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.33).
- What the losing model missed or got wrong: multilingual_e5_small missing green apron, birch tea flask
- Distractors / false positives: none

Expected evidence:
- green apron
- birch tea flask
- Canal Night

Expected distractors:
- canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.3333333333333333 matched=Canal Night missing=green apron, birch tea flask distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Canal Night, birch tea flask, green apron missing=none distractors=none

### Question 24 - page-level-024
Question: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: canal route map, paper moon mask, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: canal route map, paper moon mask, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- weathered camera strap
- canal route map

Expected distractors:
- brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=canal route map, paper moon mask, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=canal route map, paper moon mask, weathered camera strap missing=none distractors=none

### Question 25 - page-level-025
Question: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: canal route map, saffron scarf.
- Correctness verdict: grounded
- Evidence used: canal route map, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing saffron scarf, canal route map
- Distractors / false positives: none

Expected evidence:
- saffron scarf
- canal route map

Expected distractors:
- tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=saffron scarf, canal route map distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=canal route map, saffron scarf missing=none distractors=none

### Question 26 - page-level-026
Question: Which details on the profile page identify how Anya and the widowed aunt prepared for the winter coach from Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: brass compass, wax thread, widowed aunt.
- Correctness verdict: grounded
- Evidence used: brass compass, wax thread, widowed aunt
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- widowed aunt
- wax thread
- brass compass

Expected distractors:
- silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=brass compass, wax thread, widowed aunt missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=brass compass, wax thread, widowed aunt missing=none distractors=none

### Question 27 - page-level-027
Question: Which longer-page details in the family note describe the family memory scene at Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: cedar shovel, tuning fork.
- Correctness verdict: grounded
- Evidence used: cedar shovel, tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- cedar shovel
- tuning fork

Expected distractors:
- glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar shovel, tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar shovel, tuning fork missing=none distractors=none

### Question 28 - page-level-028
Question: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning, linen wick, silver booth token.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning, linen wick, silver booth token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- silver booth token
- Signal Lantern Morning

Expected distractors:
- carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, linen wick, silver booth token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, linen wick, silver booth token missing=none distractors=none

### Question 29 - page-level-029
Question: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: carved shell comb, glass ink bottle, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: carved shell comb, glass ink bottle, rope bridge permit
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (1 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- glass ink bottle
- carved shell comb

Expected distractors:
- tin key

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=carved shell comb, glass ink bottle, rope bridge permit missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=carved shell comb, glass ink bottle, rope bridge permit missing=none distractors=none

### Question 30 - page-level-030
Question: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: carved shell comb, clay watering cup.
- Correctness verdict: grounded
- Evidence used: carved shell comb, clay watering cup
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (2 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- carved shell comb

Expected distractors:
- copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=carved shell comb, clay watering cup missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=carved shell comb, clay watering cup missing=none distractors=none

### Question 31 - page-level-031
Question: Which details on the profile page identify how Raisa and the foster son prepared for the winter coach from River Lantern inn?
- Final evaluated answer: Grounded by retrieved evidence for: copper wind vane pin, foster son, tin key.
- Correctness verdict: grounded
- Evidence used: copper wind vane pin, foster son, tin key
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- foster son
- copper wind vane pin
- tin key

Expected distractors:
- star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=copper wind vane pin, foster son, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper wind vane pin, foster son, tin key missing=none distractors=none

### Question 32 - page-level-032
Question: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: amber lantern, copper token.
- Correctness verdict: grounded
- Evidence used: amber lantern, copper token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- amber lantern
- copper token

Expected distractors:
- oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=amber lantern, copper token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=amber lantern, copper token missing=none distractors=none

### Question 33 - page-level-033
Question: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: Canal Night, blue oar, star ledger page.
- Correctness verdict: grounded
- Evidence used: Canal Night, blue oar, star ledger page
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- star ledger page
- Canal Night

Expected distractors:
- juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Canal Night, blue oar, star ledger page missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Canal Night, blue oar, star ledger page missing=none distractors=none

### Question 34 - page-level-034
Question: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: juniper bundles, moonflower cutting, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: juniper bundles, moonflower cutting, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- oak barrel hoops
- juniper bundles

Expected distractors:
- coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=juniper bundles, moonflower cutting, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=juniper bundles, moonflower cutting, oak barrel hoops missing=none distractors=none

### Question 35 - page-level-035
Question: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: juniper bundles, lantern hook.
- Correctness verdict: grounded
- Evidence used: juniper bundles, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- lantern hook
- juniper bundles

Expected distractors:
- basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=juniper bundles, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=juniper bundles, lantern hook missing=none distractors=none

### Question 36 - page-level-036
Question: Which details on the profile page identify how Iveta and the twin sister prepared for the winter coach from Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: blue glass jar, coal stove hiss, twin sister.
- Correctness verdict: grounded
- Evidence used: blue glass jar, coal stove hiss, twin sister
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- twin sister
- blue glass jar
- coal stove hiss

Expected distractors:
- willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue glass jar, coal stove hiss, twin sister missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue glass jar, coal stove hiss, twin sister missing=none distractors=none

### Question 37 - page-level-037
Question: Which longer-page details in the family note describe the family memory scene at River Lantern inn?
- Final evaluated answer: Grounded by retrieved evidence for: basalt sketch, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: basalt sketch, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (2 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- smoke vent chain
- basalt sketch

Expected distractors:
- birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=basalt sketch, smoke vent chain missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=basalt sketch, smoke vent chain missing=none distractors=none

### Question 38 - page-level-038
Question: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning, violet ribbon, willow basket.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning, violet ribbon, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- violet ribbon
- willow basket
- Signal Lantern Morning

Expected distractors:
- weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, violet ribbon, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, violet ribbon, willow basket missing=none distractors=none

### Question 39 - page-level-039
Question: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: birch tea flask, green apron, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: birch tea flask, green apron, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- green apron
- birch tea flask
- weathered camera strap

Expected distractors:
- canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=birch tea flask, green apron, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=birch tea flask, green apron, weathered camera strap missing=none distractors=none

### Question 40 - page-level-040
Question: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: paper moon mask, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: paper moon mask, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing paper moon mask, weathered camera strap
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- weathered camera strap

Expected distractors:
- brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=paper moon mask, weathered camera strap distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=paper moon mask, weathered camera strap missing=none distractors=none

### Question 41 - page-level-041
Question: Which details on the profile page identify how Elena and the nephew prepared for the winter coach from Harbor Glass corridor?
- Final evaluated answer: Grounded by retrieved evidence for: canal route map, nephew, saffron scarf.
- Correctness verdict: grounded
- Evidence used: canal route map, nephew, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- nephew
- saffron scarf
- canal route map

Expected distractors:
- tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=canal route map, nephew, saffron scarf missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=canal route map, nephew, saffron scarf missing=none distractors=none

### Question 42 - page-level-042
Question: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: brass compass, wax thread.
- Correctness verdict: grounded
- Evidence used: brass compass, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- wax thread
- brass compass

Expected distractors:
- silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=brass compass, wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=brass compass, wax thread missing=none distractors=none

### Question 43 - page-level-043
Question: Which profile-page details explain what Kira kept for the Canal Night after returning to River Lantern inn?
- Final evaluated answer: Grounded by retrieved evidence for: Canal Night, cedar shovel, tuning fork.
- Correctness verdict: grounded
- Evidence used: Canal Night, cedar shovel, tuning fork
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: multilingual_e5_small distractors glass ink bottle
- Distractors / false positives: glass ink bottle

Expected evidence:
- cedar shovel
- tuning fork
- Canal Night

Expected distractors:
- glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=Canal Night, cedar shovel, tuning fork missing=none distractors=glass ink bottle
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Canal Night, cedar shovel, tuning fork missing=none distractors=none

### Question 44 - page-level-044
Question: Which page-level notes from the audio reel show why Nadia's photo memory at Birch Ferry shed mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: glass ink bottle, linen wick, silver booth token.
- Correctness verdict: grounded
- Evidence used: glass ink bottle, linen wick, silver booth token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=partial coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- silver booth token
- glass ink bottle

Expected distractors:
- carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=glass ink bottle, linen wick, silver booth token missing=none distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=glass ink bottle, linen wick, silver booth token missing=none distractors=none

### Question 45 - page-level-045
Question: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: glass ink bottle, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: glass ink bottle, rope bridge permit
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- glass ink bottle

Expected distractors:
- tin key

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=glass ink bottle, rope bridge permit missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=glass ink bottle, rope bridge permit missing=none distractors=none

### Question 46 - page-level-046
Question: Which details on the profile page identify how Anya and the niece prepared for the winter coach from Star Basin gallery?
- Final evaluated answer: Grounded by retrieved evidence for: carved shell comb, clay watering cup, niece.
- Correctness verdict: grounded
- Evidence used: carved shell comb, clay watering cup, niece
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- niece
- clay watering cup
- carved shell comb

Expected distractors:
- copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=carved shell comb, clay watering cup, niece missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=carved shell comb, clay watering cup, niece missing=none distractors=none

### Question 47 - page-level-047
Question: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor?
- Final evaluated answer: Grounded by retrieved evidence for: copper wind vane pin, tin key.
- Correctness verdict: grounded
- Evidence used: copper wind vane pin, tin key
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- copper wind vane pin
- tin key

Expected distractors:
- star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=copper wind vane pin, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper wind vane pin, tin key missing=none distractors=none

### Question 48 - page-level-048
Question: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning, amber lantern, copper token.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning, amber lantern, copper token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- amber lantern
- copper token
- Signal Lantern Morning

Expected distractors:
- oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, amber lantern, copper token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, amber lantern, copper token missing=none distractors=none

### Question 49 - page-level-049
Question: Which page-level notes from the family note show why Milena's photo memory at River Lantern inn mattered later?
- Final evaluated answer: Partially grounded by: blue oar, oak barrel hoops, star ledger page.
- Correctness verdict: partial
- Evidence used: blue oar, oak barrel hoops, star ledger page
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=partial coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing blue oar, star ledger page, oak barrel hoops
- Distractors / false positives: none

Expected evidence:
- blue oar
- star ledger page
- oak barrel hoops

Expected distractors:
- juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=blue oar, star ledger page, oak barrel hoops distractors=none
  - `bge_m3`: verdict=partial coverage=1.0 matched=blue oar, oak barrel hoops, star ledger page missing=none distractors=none

### Question 50 - page-level-050
Question: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: moonflower cutting, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: moonflower cutting, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- oak barrel hoops

Expected distractors:
- coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=moonflower cutting, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=moonflower cutting, oak barrel hoops missing=none distractors=none

### Question 51 - page-level-051
Question: Which details on the profile page identify how Raisa and the godson prepared for the winter coach from Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: godson, juniper bundles, lantern hook.
- Correctness verdict: grounded
- Evidence used: godson, juniper bundles, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- godson
- lantern hook
- juniper bundles

Expected distractors:
- basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=godson, juniper bundles, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=godson, juniper bundles, lantern hook missing=none distractors=none

### Question 52 - page-level-052
Question: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery?
- Final evaluated answer: Grounded by retrieved evidence for: blue glass jar, coal stove hiss.
- Correctness verdict: grounded
- Evidence used: blue glass jar, coal stove hiss
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- coal stove hiss

Expected distractors:
- willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue glass jar, coal stove hiss missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue glass jar, coal stove hiss missing=none distractors=none

### Question 53 - page-level-053
Question: Which profile-page details explain what Talia kept for the Canal Night after returning to Harbor Glass corridor?
- Final evaluated answer: Grounded by retrieved evidence for: Canal Night, basalt sketch, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: Canal Night, basalt sketch, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- smoke vent chain
- basalt sketch
- Canal Night

Expected distractors:
- birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Canal Night, basalt sketch, smoke vent chain missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Canal Night, basalt sketch, smoke vent chain missing=none distractors=none

### Question 54 - page-level-054
Question: Which page-level notes from the audio reel show why Runa's photo memory at Bell Bridge square mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: birch tea flask, violet ribbon, willow basket.
- Correctness verdict: grounded
- Evidence used: birch tea flask, violet ribbon, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=no_evidence coverage=0.0
- Winner: `multilingual_e5_small`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: bge_m3 missing violet ribbon, willow basket, birch tea flask
- Distractors / false positives: none

Expected evidence:
- violet ribbon
- willow basket
- birch tea flask

Expected distractors:
- weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=birch tea flask, violet ribbon, willow basket missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=0.0 matched=none missing=violet ribbon, willow basket, birch tea flask distractors=none

### Question 55 - page-level-055
Question: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: birch tea flask, green apron.
- Correctness verdict: grounded
- Evidence used: birch tea flask, green apron
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- green apron
- birch tea flask

Expected distractors:
- canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=birch tea flask, green apron missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=birch tea flask, green apron missing=none distractors=none

### Question 56 - page-level-056
Question: Which details on the profile page identify how Iveta and the stepfather prepared for the winter coach from Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: paper moon mask, stepfather, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: paper moon mask, stepfather, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- stepfather
- paper moon mask
- weathered camera strap

Expected distractors:
- brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=paper moon mask, stepfather, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=paper moon mask, stepfather, weathered camera strap missing=none distractors=none

### Question 57 - page-level-057
Question: Which longer-page details in the family note describe the family memory scene at Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: canal route map, saffron scarf.
- Correctness verdict: grounded
- Evidence used: canal route map, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron scarf
- canal route map

Expected distractors:
- tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=canal route map, saffron scarf missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=canal route map, saffron scarf missing=none distractors=none

### Question 58 - page-level-058
Question: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning, brass compass, wax thread.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning, brass compass, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- wax thread
- brass compass
- Signal Lantern Morning

Expected distractors:
- silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, brass compass, wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, brass compass, wax thread missing=none distractors=none

### Question 59 - page-level-059
Question: Which page-level notes from the family note show why Ilia's photo memory at Harbor Glass corridor mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: cedar shovel, silver booth token, tuning fork.
- Correctness verdict: grounded
- Evidence used: cedar shovel, silver booth token, tuning fork
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- cedar shovel
- tuning fork
- silver booth token

Expected distractors:
- glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar shovel, silver booth token, tuning fork missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar shovel, silver booth token, tuning fork missing=none distractors=none

### Question 60 - page-level-060
Question: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: linen wick, silver booth token.
- Correctness verdict: grounded
- Evidence used: linen wick, silver booth token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- silver booth token

Expected distractors:
- carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=linen wick, silver booth token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=linen wick, silver booth token missing=none distractors=none

### Question 61 - page-level-061
Question: Which details on the profile page identify how Elena and the aunt prepared for the winter coach from River Lantern inn?
- Final evaluated answer: Grounded by retrieved evidence for: aunt, glass ink bottle, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: aunt, glass ink bottle, rope bridge permit
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- aunt
- rope bridge permit
- glass ink bottle

Expected distractors:
- tin key

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=aunt, glass ink bottle, rope bridge permit missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=aunt, glass ink bottle, rope bridge permit missing=none distractors=none

### Question 62 - page-level-062
Question: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: carved shell comb, clay watering cup.
- Correctness verdict: grounded
- Evidence used: carved shell comb, clay watering cup
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing clay watering cup, carved shell comb
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- carved shell comb

Expected distractors:
- copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=clay watering cup, carved shell comb distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=carved shell comb, clay watering cup missing=none distractors=none

### Question 63 - page-level-063
Question: Which profile-page details explain what Kira kept for the Canal Night after returning to Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: Canal Night, copper wind vane pin, tin key.
- Correctness verdict: grounded
- Evidence used: Canal Night, copper wind vane pin, tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- copper wind vane pin
- tin key
- Canal Night

Expected distractors:
- star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Canal Night, copper wind vane pin, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Canal Night, copper wind vane pin, tin key missing=none distractors=none

### Question 64 - page-level-064
Question: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: amber lantern, copper token, star ledger page.
- Correctness verdict: grounded
- Evidence used: amber lantern, copper token, star ledger page
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- amber lantern
- copper token
- star ledger page

Expected distractors:
- oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=amber lantern, copper token, star ledger page missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=amber lantern, copper token, star ledger page missing=none distractors=none

### Question 65 - page-level-065
Question: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: blue oar, star ledger page.
- Correctness verdict: grounded
- Evidence used: blue oar, star ledger page
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- star ledger page

Expected distractors:
- juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue oar, star ledger page missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue oar, star ledger page missing=none distractors=none

### Question 66 - page-level-066
Question: Which details on the profile page identify how Anya and the grandfather prepared for the winter coach from Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: grandfather, moonflower cutting, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: grandfather, moonflower cutting, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- grandfather
- moonflower cutting
- oak barrel hoops

Expected distractors:
- coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=grandfather, moonflower cutting, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=grandfather, moonflower cutting, oak barrel hoops missing=none distractors=none

### Question 67 - page-level-067
Question: Which longer-page details in the family note describe the family memory scene at River Lantern inn?
- Final evaluated answer: Grounded by retrieved evidence for: juniper bundles, lantern hook.
- Correctness verdict: grounded
- Evidence used: juniper bundles, lantern hook
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing lantern hook, juniper bundles
- Distractors / false positives: none

Expected evidence:
- lantern hook
- juniper bundles

Expected distractors:
- basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=lantern hook, juniper bundles distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=juniper bundles, lantern hook missing=none distractors=none

### Question 68 - page-level-068
Question: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning, blue glass jar, coal stove hiss.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning, blue glass jar, coal stove hiss
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- coal stove hiss
- Signal Lantern Morning

Expected distractors:
- willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, blue glass jar, coal stove hiss missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, blue glass jar, coal stove hiss missing=none distractors=none

### Question 69 - page-level-069
Question: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: basalt sketch, smoke vent chain, willow basket.
- Correctness verdict: grounded
- Evidence used: basalt sketch, smoke vent chain, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- smoke vent chain
- basalt sketch
- willow basket

Expected distractors:
- birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=basalt sketch, smoke vent chain, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=basalt sketch, smoke vent chain, willow basket missing=none distractors=none

### Question 70 - page-level-070
Question: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: violet ribbon, willow basket.
- Correctness verdict: grounded
- Evidence used: violet ribbon, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- violet ribbon
- willow basket

Expected distractors:
- weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=violet ribbon, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=violet ribbon, willow basket missing=none distractors=none

### Question 71 - page-level-071
Question: Which details on the profile page identify how Raisa and the grandmother prepared for the winter coach from Harbor Glass corridor?
- Final evaluated answer: Grounded by retrieved evidence for: birch tea flask, grandmother, green apron.
- Correctness verdict: grounded
- Evidence used: birch tea flask, grandmother, green apron
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- grandmother
- green apron
- birch tea flask

Expected distractors:
- canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=birch tea flask, grandmother, green apron missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=birch tea flask, grandmother, green apron missing=none distractors=none

### Question 72 - page-level-072
Question: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: paper moon mask, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: paper moon mask, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- paper moon mask
- weathered camera strap

Expected distractors:
- brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=paper moon mask, weathered camera strap missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=paper moon mask, weathered camera strap missing=none distractors=none

### Question 73 - page-level-073
Question: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn?
- Final evaluated answer: Grounded by retrieved evidence for: Canal Night, canal route map, saffron scarf.
- Correctness verdict: grounded
- Evidence used: Canal Night, canal route map, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.3333333333333333; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.33).
- What the losing model missed or got wrong: multilingual_e5_small missing saffron scarf, canal route map
- Distractors / false positives: none

Expected evidence:
- saffron scarf
- canal route map
- Canal Night

Expected distractors:
- tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.3333333333333333 matched=Canal Night missing=saffron scarf, canal route map distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Canal Night, canal route map, saffron scarf missing=none distractors=none

### Question 74 - page-level-074
Question: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: brass compass, tuning fork, wax thread.
- Correctness verdict: grounded
- Evidence used: brass compass, tuning fork, wax thread
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing wax thread, brass compass, tuning fork
- Distractors / false positives: none

Expected evidence:
- wax thread
- brass compass
- tuning fork

Expected distractors:
- silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=wax thread, brass compass, tuning fork distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=brass compass, tuning fork, wax thread missing=none distractors=none

### Question 75 - page-level-075
Question: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: cedar shovel, tuning fork.
- Correctness verdict: grounded
- Evidence used: cedar shovel, tuning fork
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing cedar shovel, tuning fork
- Distractors / false positives: none

Expected evidence:
- cedar shovel
- tuning fork

Expected distractors:
- glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=cedar shovel, tuning fork distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar shovel, tuning fork missing=none distractors=none

### Question 76 - page-level-076
Question: Which details on the profile page identify how Iveta and the cousin prepared for the winter coach from Star Basin gallery?
- Final evaluated answer: Grounded by retrieved evidence for: cousin, linen wick, silver booth token.
- Correctness verdict: grounded
- Evidence used: cousin, linen wick, silver booth token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- cousin
- linen wick
- silver booth token

Expected distractors:
- carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cousin, linen wick, silver booth token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cousin, linen wick, silver booth token missing=none distractors=none

### Question 77 - page-level-077
Question: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor?
- Final evaluated answer: Grounded by retrieved evidence for: glass ink bottle, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: glass ink bottle, rope bridge permit
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- glass ink bottle

Expected distractors:
- tin key

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=glass ink bottle, rope bridge permit missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=glass ink bottle, rope bridge permit missing=none distractors=none

### Question 78 - page-level-078
Question: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square?
- Final evaluated answer: Partially grounded by: Signal Lantern Morning. Missing: clay watering cup, carved shell comb. Distractors present: copper token.
- Correctness verdict: partial
- Evidence used: Signal Lantern Morning
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.3333333333333333; bge_m3 -> verdict=partial coverage=0.3333333333333333
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: bge_m3 missing clay watering cup, carved shell comb
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- carved shell comb
- Signal Lantern Morning

Expected distractors:
- copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.3333333333333333 matched=Signal Lantern Morning missing=clay watering cup, carved shell comb distractors=copper token
  - `bge_m3`: verdict=partial coverage=0.3333333333333333 matched=Signal Lantern Morning missing=clay watering cup, carved shell comb distractors=none

### Question 79 - page-level-079
Question: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: copper token, copper wind vane pin, tin key.
- Correctness verdict: grounded
- Evidence used: copper token, copper wind vane pin, tin key
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- copper wind vane pin
- tin key
- copper token

Expected distractors:
- star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=copper token, copper wind vane pin, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper token, copper wind vane pin, tin key missing=none distractors=none

### Question 80 - page-level-080
Question: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: amber lantern, copper token.
- Correctness verdict: grounded
- Evidence used: amber lantern, copper token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- amber lantern
- copper token

Expected distractors:
- oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=amber lantern, copper token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=amber lantern, copper token missing=none distractors=none

### Question 81 - page-level-081
Question: Which details on the profile page identify how Elena and the uncle prepared for the winter coach from Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: blue oar, star ledger page, uncle.
- Correctness verdict: grounded
- Evidence used: blue oar, star ledger page, uncle
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- uncle
- blue oar
- star ledger page

Expected distractors:
- juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue oar, star ledger page, uncle missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue oar, star ledger page, uncle missing=none distractors=none

### Question 82 - page-level-082
Question: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery?
- Final evaluated answer: Grounded by retrieved evidence for: moonflower cutting, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: moonflower cutting, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- oak barrel hoops

Expected distractors:
- coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=moonflower cutting, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=moonflower cutting, oak barrel hoops missing=none distractors=none

### Question 83 - page-level-083
Question: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor?
- Final evaluated answer: Grounded by retrieved evidence for: Canal Night, juniper bundles, lantern hook.
- Correctness verdict: grounded
- Evidence used: Canal Night, juniper bundles, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- lantern hook
- juniper bundles
- Canal Night

Expected distractors:
- basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Canal Night, juniper bundles, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Canal Night, juniper bundles, lantern hook missing=none distractors=none

### Question 84 - page-level-084
Question: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: basalt sketch, blue glass jar, coal stove hiss.
- Correctness verdict: grounded
- Evidence used: basalt sketch, blue glass jar, coal stove hiss
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- coal stove hiss
- basalt sketch

Expected distractors:
- willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=basalt sketch, blue glass jar, coal stove hiss missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=basalt sketch, blue glass jar, coal stove hiss missing=none distractors=none

### Question 85 - page-level-085
Question: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: basalt sketch, smoke vent chain.
- Correctness verdict: grounded
- Evidence used: basalt sketch, smoke vent chain
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing smoke vent chain, basalt sketch
- Distractors / false positives: none

Expected evidence:
- smoke vent chain
- basalt sketch

Expected distractors:
- birch tea flask

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=smoke vent chain, basalt sketch distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=basalt sketch, smoke vent chain missing=none distractors=none

### Question 86 - page-level-086
Question: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: godmother, violet ribbon, willow basket.
- Correctness verdict: grounded
- Evidence used: godmother, violet ribbon, willow basket
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- godmother
- violet ribbon
- willow basket

Expected distractors:
- weathered camera strap

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=godmother, violet ribbon, willow basket missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=godmother, violet ribbon, willow basket missing=none distractors=none

### Question 87 - page-level-087
Question: Which longer-page details in the family note describe the family memory scene at Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: birch tea flask, green apron.
- Correctness verdict: grounded
- Evidence used: birch tea flask, green apron
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (1 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- green apron
- birch tea flask

Expected distractors:
- canal route map

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=birch tea flask, green apron missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=birch tea flask, green apron missing=none distractors=none

### Question 88 - page-level-088
Question: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning, paper moon mask, weathered camera strap.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning, paper moon mask, weathered camera strap
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.3333333333333333; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.33).
- What the losing model missed or got wrong: multilingual_e5_small missing paper moon mask, weathered camera strap; multilingual_e5_small distractors brass compass
- Distractors / false positives: brass compass

Expected evidence:
- paper moon mask
- weathered camera strap
- Signal Lantern Morning

Expected distractors:
- brass compass

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.3333333333333333 matched=Signal Lantern Morning missing=paper moon mask, weathered camera strap distractors=brass compass
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, paper moon mask, weathered camera strap missing=none distractors=none

### Question 89 - page-level-089
Question: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: brass compass, canal route map, saffron scarf.
- Correctness verdict: grounded
- Evidence used: brass compass, canal route map, saffron scarf
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- saffron scarf
- canal route map
- brass compass

Expected distractors:
- tuning fork

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=brass compass, canal route map, saffron scarf missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=brass compass, canal route map, saffron scarf missing=none distractors=none

### Question 90 - page-level-090
Question: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: brass compass, wax thread.
- Correctness verdict: grounded
- Evidence used: brass compass, wax thread
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- wax thread
- brass compass

Expected distractors:
- silver booth token

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=brass compass, wax thread missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=brass compass, wax thread missing=none distractors=none

### Question 91 - page-level-091
Question: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from River Lantern inn?
- Final evaluated answer: Grounded by retrieved evidence for: cedar shovel, tuning fork, younger brother.
- Correctness verdict: grounded
- Evidence used: cedar shovel, tuning fork, younger brother
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- younger brother
- cedar shovel
- tuning fork

Expected distractors:
- glass ink bottle

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=cedar shovel, tuning fork, younger brother missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=cedar shovel, tuning fork, younger brother missing=none distractors=none

### Question 92 - page-level-092
Question: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: linen wick, silver booth token.
- Correctness verdict: grounded
- Evidence used: linen wick, silver booth token
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- linen wick
- silver booth token

Expected distractors:
- carved shell comb

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=linen wick, silver booth token missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=linen wick, silver booth token missing=none distractors=none

### Question 93 - page-level-093
Question: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove?
- Final evaluated answer: Grounded by retrieved evidence for: Canal Night, glass ink bottle, rope bridge permit.
- Correctness verdict: grounded
- Evidence used: Canal Night, glass ink bottle, rope bridge permit
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- rope bridge permit
- glass ink bottle
- Canal Night

Expected distractors:
- tin key

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Canal Night, glass ink bottle, rope bridge permit missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Canal Night, glass ink bottle, rope bridge permit missing=none distractors=none

### Question 94 - page-level-094
Question: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: carved shell comb, clay watering cup, tin key.
- Correctness verdict: grounded
- Evidence used: carved shell comb, clay watering cup, tin key
- Model comparison: multilingual_e5_small -> verdict=no_evidence coverage=0.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.00).
- What the losing model missed or got wrong: multilingual_e5_small missing clay watering cup, carved shell comb, tin key
- Distractors / false positives: none

Expected evidence:
- clay watering cup
- carved shell comb
- tin key

Expected distractors:
- copper token

- Model verdicts:
  - `multilingual_e5_small`: verdict=no_evidence coverage=0.0 matched=none missing=clay watering cup, carved shell comb, tin key distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=carved shell comb, clay watering cup, tin key missing=none distractors=none

### Question 95 - page-level-095
Question: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: copper wind vane pin, tin key.
- Correctness verdict: grounded
- Evidence used: copper wind vane pin, tin key
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- copper wind vane pin
- tin key

Expected distractors:
- star ledger page

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=copper wind vane pin, tin key missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=copper wind vane pin, tin key missing=none distractors=none

### Question 96 - page-level-096
Question: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Bell Bridge square?
- Final evaluated answer: Grounded by retrieved evidence for: amber lantern, copper token, older sister.
- Correctness verdict: grounded
- Evidence used: amber lantern, copper token, older sister
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- older sister
- amber lantern
- copper token

Expected distractors:
- oak barrel hoops

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=amber lantern, copper token, older sister missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=amber lantern, copper token, older sister missing=none distractors=none

### Question 97 - page-level-097
Question: Which longer-page details in the family note describe the family memory scene at River Lantern inn?
- Final evaluated answer: Grounded by retrieved evidence for: blue oar, star ledger page.
- Correctness verdict: grounded
- Evidence used: blue oar, star ledger page
- Model comparison: multilingual_e5_small -> verdict=partial coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (2 vs 3).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue oar
- star ledger page

Expected distractors:
- juniper bundles

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=1.0 matched=blue oar, star ledger page missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue oar, star ledger page missing=none distractors=none

### Question 98 - page-level-098
Question: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: Signal Lantern Morning, moonflower cutting, oak barrel hoops.
- Correctness verdict: grounded
- Evidence used: Signal Lantern Morning, moonflower cutting, oak barrel hoops
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- moonflower cutting
- oak barrel hoops
- Signal Lantern Morning

Expected distractors:
- coal stove hiss

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, moonflower cutting, oak barrel hoops missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=Signal Lantern Morning, moonflower cutting, oak barrel hoops missing=none distractors=none

### Question 99 - page-level-099
Question: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later?
- Final evaluated answer: Grounded by retrieved evidence for: coal stove hiss, juniper bundles, lantern hook.
- Correctness verdict: grounded
- Evidence used: coal stove hiss, juniper bundles, lantern hook
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `bge_m3`
- Why it won: Fewer distractors (0 vs 2).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- lantern hook
- juniper bundles
- coal stove hiss

Expected distractors:
- basalt sketch

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=coal stove hiss, juniper bundles, lantern hook missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=coal stove hiss, juniper bundles, lantern hook missing=none distractors=none

### Question 100 - page-level-100
Question: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed?
- Final evaluated answer: Grounded by retrieved evidence for: blue glass jar, coal stove hiss.
- Correctness verdict: grounded
- Evidence used: blue glass jar, coal stove hiss
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- blue glass jar
- coal stove hiss

Expected distractors:
- willow basket

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue glass jar, coal stove hiss missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue glass jar, coal stove hiss missing=none distractors=none

## Aggregate Client Decision
- Recommended active model: `bge_m3`
- Overall winner: `bge_m3`
- Activation state: `true`
- Runtime retrieval verified: `true`
- Production recommendation: Keep the fake-mode result for test coverage only; use the preserved latest real evaluation for production-facing model decisions.

## Developer Details

### Question 1 - page-level-attic-instructions
Question: Which two maintenance details on the attic instruction page explain how the lamp smoke was controlled?

Expected evidence:
- linen wick
- smoke vent chain

Expected distractors:
- cellar coal scoop

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.200621 chunk_id=21267 preview=Question anchor: Which two maintenance details on the attic instruction page explain how the lamp smoke was controlled? Case scope id: page-level-attic-instr...
  2. score=60.242826 chunk_id=21269 preview=Question anchor: Which two maintenance details on the attic instruction page explain how the lamp smoke was controlled? Case scope id: page-level-attic-instr...
  3. score=60.218411 chunk_id=21268 preview=Question anchor: Which two maintenance details on the attic instruction page explain how the lamp smoke was controlled? Case scope id: page-level-attic-instr...
  4. score=41.213074 chunk_id=21270 preview=Question anchor: Which two maintenance details on the attic instruction page explain how the lamp smoke was controlled? document attic-manual-archive::page-l...
  5. score=38.208205 chunk_id=21067 preview=document attic-manual-archive::page-level-attic-instructions, page 4, section attic-lamps: In document attic-manual-archive, page 4, section attic-lamps, the...
- Matched markers: linen wick, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: linen wick, smoke vent chain.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=64.967942 chunk_id=21267 preview=Question anchor: Which two maintenance details on the attic instruction page explain how the lamp smoke was controlled? Case scope id: page-level-attic-instr...
  2. score=60.006070 chunk_id=21269 preview=Question anchor: Which two maintenance details on the attic instruction page explain how the lamp smoke was controlled? Case scope id: page-level-attic-instr...
  3. score=60.005981 chunk_id=21268 preview=Question anchor: Which two maintenance details on the attic instruction page explain how the lamp smoke was controlled? Case scope id: page-level-attic-instr...
  4. score=41.010538 chunk_id=21270 preview=Question anchor: Which two maintenance details on the attic instruction page explain how the lamp smoke was controlled? document attic-manual-archive::page-l...
  5. score=37.925964 chunk_id=21067 preview=document attic-manual-archive::page-level-attic-instructions, page 4, section attic-lamps: In document attic-manual-archive, page 4, section attic-lamps, the...
- Matched markers: linen wick, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: linen wick, smoke vent chain.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 2 - page-level-river-meeting
Question: Which two details on the river meeting page explain why the delegation arrived late?

Expected evidence:
- flooded footbridge
- late telegraph reply

Expected distractors:
- harvest parade rumor

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.326214 chunk_id=21271 preview=Question anchor: Which two details on the river meeting page explain why the delegation arrived late? Case scope id: page-level-river-meeting. Scoped answer...
  2. score=60.370388 chunk_id=21273 preview=Question anchor: Which two details on the river meeting page explain why the delegation arrived late? Case scope id: page-level-river-meeting. Page-level cit...
  3. score=60.327738 chunk_id=21272 preview=Question anchor: Which two details on the river meeting page explain why the delegation arrived late? Case scope id: page-level-river-meeting. Page-level cit...
  4. score=41.318393 chunk_id=21274 preview=Question anchor: Which two details on the river meeting page explain why the delegation arrived late? document river-meeting-minutes::page-level-river-meetin...
  5. score=38.339254 chunk_id=21164 preview=document river-meeting-minutes::page-level-river-meeting, page 7, section delay-notes: In document river-meeting-minutes, page 7, section delay-notes, the ve...
- Matched markers: flooded footbridge, late telegraph reply
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: flooded footbridge, late telegraph reply.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.086412 chunk_id=21271 preview=Question anchor: Which two details on the river meeting page explain why the delegation arrived late? Case scope id: page-level-river-meeting. Scoped answer...
  2. score=60.144266 chunk_id=21273 preview=Question anchor: Which two details on the river meeting page explain why the delegation arrived late? Case scope id: page-level-river-meeting. Page-level cit...
  3. score=60.118228 chunk_id=21272 preview=Question anchor: Which two details on the river meeting page explain why the delegation arrived late? Case scope id: page-level-river-meeting. Page-level cit...
  4. score=41.111647 chunk_id=21274 preview=Question anchor: Which two details on the river meeting page explain why the delegation arrived late? document river-meeting-minutes::page-level-river-meetin...
  5. score=38.049606 chunk_id=21164 preview=document river-meeting-minutes::page-level-river-meeting, page 7, section delay-notes: In document river-meeting-minutes, page 7, section delay-notes, the ve...
- Matched markers: flooded footbridge, late telegraph reply
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: flooded footbridge, late telegraph reply.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 3 - page-level-station-caretaker
Question: What page-level details from the station caretaker log explain the cold draft on the night round?

Expected evidence:
- coal stove hiss
- cracked west window

Expected distractors:
- sealed ticket drawer

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.235409 chunk_id=21275 preview=Question anchor: What page-level details from the station caretaker log explain the cold draft on the night round? Case scope id: page-level-station-caretake...
  2. score=60.317823 chunk_id=21276 preview=Question anchor: What page-level details from the station caretaker log explain the cold draft on the night round? Case scope id: page-level-station-caretake...
  3. score=60.308737 chunk_id=21277 preview=Question anchor: What page-level details from the station caretaker log explain the cold draft on the night round? Case scope id: page-level-station-caretake...
  4. score=41.291941 chunk_id=21278 preview=Question anchor: What page-level details from the station caretaker log explain the cold draft on the night round? document station-caretaker-log::page-level...
  5. score=38.298181 chunk_id=21165 preview=document station-caretaker-log::page-level-station-caretaker, page 3, section night-round: In document station-caretaker-log, page 3, section night-round, th...
- Matched markers: coal stove hiss, cracked west window
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, cracked west window.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.134277 chunk_id=21275 preview=Question anchor: What page-level details from the station caretaker log explain the cold draft on the night round? Case scope id: page-level-station-caretake...
  2. score=60.233547 chunk_id=21276 preview=Question anchor: What page-level details from the station caretaker log explain the cold draft on the night round? Case scope id: page-level-station-caretake...
  3. score=60.203324 chunk_id=21277 preview=Question anchor: What page-level details from the station caretaker log explain the cold draft on the night round? Case scope id: page-level-station-caretake...
  4. score=41.190269 chunk_id=21278 preview=Question anchor: What page-level details from the station caretaker log explain the cold draft on the night round? document station-caretaker-log::page-level...
  5. score=38.094800 chunk_id=21165 preview=document station-caretaker-log::page-level-station-caretaker, page 3, section night-round: In document station-caretaker-log, page 3, section night-round, th...
- Matched markers: coal stove hiss, cracked west window
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, cracked west window.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 4 - page-level-herbal-room
Question: Which page-level inventory details identify the winter shelf in the herbal room?

Expected evidence:
- juniper bundles
- blue glass jar

Expected distractors:
- summer nettle basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=59.930319 chunk_id=21281 preview=Question anchor: Which page-level inventory details identify the winter shelf in the herbal room? Case scope id: page-level-herbal-room. Page-level citation...
  2. score=59.930319 chunk_id=21280 preview=Question anchor: Which page-level inventory details identify the winter shelf in the herbal room? Case scope id: page-level-herbal-room. Page-level citation...
  3. score=40.897723 chunk_id=21282 preview=Question anchor: Which page-level inventory details identify the winter shelf in the herbal room? document herbal-room-ledger::page-level-herbal-room, page 6...
  4. score=1.039256 chunk_id=21165 preview=document station-caretaker-log::page-level-station-caretaker, page 3, section night-round: In document station-caretaker-log, page 3, section night-round, th...
  5. score=1.006349 chunk_id=21278 preview=Question anchor: What page-level details from the station caretaker log explain the cold draft on the night round? document station-caretaker-log::page-level...
- Matched markers: blue glass jar, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, juniper bundles.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=64.932918 chunk_id=21279 preview=Question anchor: Which page-level inventory details identify the winter shelf in the herbal room? Case scope id: page-level-herbal-room. Scoped answer summar...
  2. score=60.011744 chunk_id=21281 preview=Question anchor: Which page-level inventory details identify the winter shelf in the herbal room? Case scope id: page-level-herbal-room. Page-level citation...
  3. score=59.996955 chunk_id=21280 preview=Question anchor: Which page-level inventory details identify the winter shelf in the herbal room? Case scope id: page-level-herbal-room. Page-level citation...
  4. score=40.952534 chunk_id=21282 preview=Question anchor: Which page-level inventory details identify the winter shelf in the herbal room? document herbal-room-ledger::page-level-herbal-room, page 6...
  5. score=37.885010 chunk_id=21068 preview=document herbal-room-ledger::page-level-herbal-room, page 6, section winter-shelf: In document herbal-room-ledger, page 6, section winter-shelf, the verified...
- Matched markers: blue glass jar, juniper bundles
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, juniper bundles.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 2).

### Question 5 - page-level-watchtower
Question: Which details on the watchtower repair page identify the upper landing hardware?

Expected evidence:
- iron rung
- lantern hook

Expected distractors:
- rope bucket pulley

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.008224 chunk_id=21283 preview=Question anchor: Which details on the watchtower repair page identify the upper landing hardware? Case scope id: page-level-watchtower. Scoped answer summary...
  2. score=60.050439 chunk_id=21285 preview=Question anchor: Which details on the watchtower repair page identify the upper landing hardware? Case scope id: page-level-watchtower. Page-level citation 2...
  3. score=60.027738 chunk_id=21284 preview=Question anchor: Which details on the watchtower repair page identify the upper landing hardware? Case scope id: page-level-watchtower. Page-level citation 1...
  4. score=41.022226 chunk_id=21286 preview=Question anchor: Which details on the watchtower repair page identify the upper landing hardware? document watchtower-repair-book::page-level-watchtower, pag...
  5. score=38.042927 chunk_id=21166 preview=document watchtower-repair-book::page-level-watchtower, page 9, section upper-landing: In document watchtower-repair-book, page 9, section upper-landing, the...
- Matched markers: iron rung, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: iron rung, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=64.853900 chunk_id=21283 preview=Question anchor: Which details on the watchtower repair page identify the upper landing hardware? Case scope id: page-level-watchtower. Scoped answer summary...
  2. score=59.911928 chunk_id=21284 preview=Question anchor: Which details on the watchtower repair page identify the upper landing hardware? Case scope id: page-level-watchtower. Page-level citation 1...
  3. score=59.870855 chunk_id=21285 preview=Question anchor: Which details on the watchtower repair page identify the upper landing hardware? Case scope id: page-level-watchtower. Page-level citation 2...
  4. score=40.916262 chunk_id=21286 preview=Question anchor: Which details on the watchtower repair page identify the upper landing hardware? document watchtower-repair-book::page-level-watchtower, pag...
  5. score=37.868763 chunk_id=21166 preview=document watchtower-repair-book::page-level-watchtower, page 9, section upper-landing: In document watchtower-repair-book, page 9, section upper-landing, the...
- Matched markers: iron rung, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: iron rung, lantern hook.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 6 - page-level-006
Question: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Bell Bridge square?

Expected evidence:
- godmother
- violet ribbon
- willow basket

Expected distractors:
- weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.443614 chunk_id=21288 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Bell Bridge square? Case scope id:...
  2. score=53.461300 chunk_id=21291 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Bell Bridge square? document page-b...
  3. score=37.980542 chunk_id=21707 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Birch Ferry shed? document page-bir...
  4. score=2.311300 chunk_id=21603 preview=Question anchor: Which details on the profile page identify how Anya and the grandfather prepared for the winter coach from Bell Bridge square? document page...
  5. score=2.295086 chunk_id=21604 preview=Question anchor: Which details on the profile page identify how Anya and the grandfather prepared for the winter coach from Bell Bridge square? document page...
- Matched markers: godmother, violet ribbon, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: godmother, violet ribbon, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.323665 chunk_id=21287 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Bell Bridge square? Case scope id:...
  2. score=72.407091 chunk_id=21288 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Bell Bridge square? Case scope id:...
  3. score=72.371550 chunk_id=21289 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Bell Bridge square? Case scope id:...
  4. score=72.338581 chunk_id=21290 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Bell Bridge square? Case scope id:...
  5. score=53.413461 chunk_id=21291 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Bell Bridge square? document page-b...
- Matched markers: godmother, violet ribbon, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: godmother, violet ribbon, willow basket.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 2).

### Question 7 - page-level-007
Question: Which longer-page details in the family note describe the family memory scene at River Lantern inn?

Expected evidence:
- green apron
- birch tea flask

Expected distractors:
- canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.318511 chunk_id=21293 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? Case scope id: page-level-007. Scoped an...
  2. score=60.347097 chunk_id=21294 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? Case scope id: page-level-007. Page-leve...
  3. score=60.343103 chunk_id=21295 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? Case scope id: page-level-007. Page-leve...
  4. score=41.342543 chunk_id=21296 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
  5. score=38.318946 chunk_id=21132 preview=document page-river-lantern-inn-family-note-007::page-level-007, page 9, section section-007: In document page-river-lantern-inn-family-note-007, page 9, sec...
- Matched markers: birch tea flask, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, green apron.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.308401 chunk_id=21294 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? Case scope id: page-level-007. Page-leve...
  2. score=41.313074 chunk_id=21296 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
  3. score=7.298607 chunk_id=21608 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
  4. score=7.297287 chunk_id=21452 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
  5. score=7.294621 chunk_id=21764 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
- Matched markers: birch tea flask, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, green apron.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 3).

### Question 8 - page-level-008
Question: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed?

Expected evidence:
- paper moon mask
- weathered camera strap
- Signal Lantern Morning

Expected distractors:
- brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=19.736883 chunk_id=21613 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  2. score=19.695764 chunk_id=21614 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  3. score=14.622827 chunk_id=21770 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  4. score=14.622827 chunk_id=21458 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  5. score=7.750583 chunk_id=21612 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? Case scope id: page-le...
- Matched markers: Signal Lantern Morning
- Missing markers: paper moon mask, weathered camera strap
- Distractors: none
- Evidence coverage: 0.3333333333333333
- First relevant rank: 1
- Answer summary: Partially grounded by: Signal Lantern Morning. Missing: paper moon mask, weathered camera strap.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=53.626219 chunk_id=21302 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  2. score=19.638181 chunk_id=21614 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  3. score=19.636516 chunk_id=21613 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  4. score=14.615650 chunk_id=21770 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  5. score=14.605042 chunk_id=21769 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
- Matched markers: Signal Lantern Morning, paper moon mask, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, paper moon mask, weathered camera strap.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.33).

### Question 9 - page-level-009
Question: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later?

Expected evidence:
- saffron scarf
- canal route map
- brass compass

Expected distractors:
- tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=7.615705 chunk_id=21620 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fa...
  2. score=2.635269 chunk_id=21464 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
  3. score=2.632779 chunk_id=21463 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
  4. score=2.631646 chunk_id=21106 preview=document page-driftwood-cove-family-note-039::page-level-039, page 7, section section-039: In document page-driftwood-cove-family-note-039, page 7, section s...
- Matched markers: none
- Missing markers: saffron scarf, canal route map, brass compass
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.566022 chunk_id=21305 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later? Case scope id: page-level-009....
  2. score=72.544369 chunk_id=21304 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later? Case scope id: page-level-009....
  3. score=72.539729 chunk_id=21306 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later? Case scope id: page-level-009....
  4. score=53.555355 chunk_id=21308 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fa...
  5. score=7.555526 chunk_id=21619 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fa...
- Matched markers: brass compass, canal route map, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass compass, canal route map, saffron scarf.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 10 - page-level-010
Question: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed?

Expected evidence:
- wax thread
- brass compass

Expected distractors:
- silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.679330 chunk_id=21310 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-level...
  2. score=60.639688 chunk_id=21311 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-level...
  3. score=41.679487 chunk_id=21312 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin-...
  4. score=38.651976 chunk_id=21148 preview=document page-star-basin-gallery-audio-reel-010::page-level-010, page 12, section section-010: In document page-star-basin-gallery-audio-reel-010, page 12, s...
  5. score=7.653897 chunk_id=21624 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin-...
- Matched markers: brass compass, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass compass, wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.580248 chunk_id=21309 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-level...
  2. score=60.664468 chunk_id=21310 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-level...
  3. score=60.611195 chunk_id=21311 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-level...
  4. score=41.657088 chunk_id=21312 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin-...
  5. score=7.567742 chunk_id=21624 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin-...
- Matched markers: brass compass, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass compass, wax thread.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 11 - page-level-011
Question: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from Harbor Glass corridor?

Expected evidence:
- younger brother
- cedar shovel
- tuning fork

Expected distractors:
- glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.668034 chunk_id=21314 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from Harbor Glass corridor? Case...
  2. score=72.587455 chunk_id=21315 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from Harbor Glass corridor? Case...
  3. score=72.585792 chunk_id=21316 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from Harbor Glass corridor? Case...
  4. score=53.674270 chunk_id=21317 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from Harbor Glass corridor? docum...
  5. score=53.586714 chunk_id=21318 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from Harbor Glass corridor? docum...
- Matched markers: cedar shovel, tuning fork, younger brother
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, tuning fork, younger brother.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.560625 chunk_id=21313 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from Harbor Glass corridor? Case...
  2. score=72.606565 chunk_id=21314 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from Harbor Glass corridor? Case...
  3. score=72.593283 chunk_id=21315 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from Harbor Glass corridor? Case...
  4. score=72.568393 chunk_id=21316 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from Harbor Glass corridor? Case...
  5. score=53.616226 chunk_id=21317 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from Harbor Glass corridor? docum...
- Matched markers: cedar shovel, tuning fork, younger brother
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, tuning fork, younger brother.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 12 - page-level-012
Question: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square?

Expected evidence:
- linen wick
- silver booth token

Expected distractors:
- carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.483426 chunk_id=21319 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? Case scope id: page-level-012. Scoped an...
  2. score=60.503562 chunk_id=21321 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? Case scope id: page-level-012. Page-leve...
  3. score=60.469439 chunk_id=21320 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? Case scope id: page-level-012. Page-leve...
  4. score=41.482184 chunk_id=21322 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? document page-bell-bridge-square-audio-r...
  5. score=38.458488 chunk_id=21070 preview=document page-bell-bridge-square-audio-reel-012::page-level-012, page 14, section section-012: In document page-bell-bridge-square-audio-reel-012, page 14, s...
- Matched markers: linen wick, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: linen wick, silver booth token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.377714 chunk_id=21320 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? Case scope id: page-level-012. Page-leve...
  2. score=60.361421 chunk_id=21321 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? Case scope id: page-level-012. Page-leve...
  3. score=41.376755 chunk_id=21322 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? document page-bell-bridge-square-audio-r...
  4. score=7.463887 chunk_id=21478 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? document page-bell-bridge-square-audio-r...
  5. score=4.378781 chunk_id=21075 preview=document page-bell-bridge-square-audio-reel-042::page-level-042, page 10, section section-042: In document page-bell-bridge-square-audio-reel-042, page 10, s...
- Matched markers: linen wick, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: linen wick, silver booth token.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 2).

### Question 13 - page-level-013
Question: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn?

Expected evidence:
- rope bridge permit
- glass ink bottle
- Canal Night

Expected distractors:
- tin key

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.718498 chunk_id=21326 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn? Case scope id: page-level-013....
  2. score=53.668106 chunk_id=21328 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn? document page-river-lantern-inn...
  3. score=22.224095 chunk_id=21742 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? Case scope id: page-level-093. Pag...
  4. score=14.282034 chunk_id=21691 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
  5. score=2.542858 chunk_id=21482 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to River Lantern inn? Case scope id: page-level-043. P...
- Matched markers: Canal Night, glass ink bottle, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, glass ink bottle, rope bridge permit.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.508501 chunk_id=21325 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn? Case scope id: page-level-013....
  2. score=72.504649 chunk_id=21326 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn? Case scope id: page-level-013....
  3. score=53.509277 chunk_id=21328 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn? document page-river-lantern-inn...
  4. score=19.523964 chunk_id=21640 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn? document page-river-lantern-inn...
  5. score=14.377421 chunk_id=21484 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to River Lantern inn? document page-river-lantern-inn-...
- Matched markers: Canal Night, glass ink bottle, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, glass ink bottle, rope bridge permit.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 14 - page-level-014
Question: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later?

Expected evidence:
- clay watering cup
- carved shell comb
- tin key

Expected distractors:
- copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=2.684672 chunk_id=21490 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Birch Ferry shed mattered later? document page-birch-ferry-shed-...
  2. score=2.511235 chunk_id=21438 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? document page-star-basin-galle...
  3. score=2.463992 chunk_id=21437 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? document page-star-basin-galle...
  4. score=2.158486 chunk_id=21464 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
- Matched markers: none
- Missing markers: clay watering cup, carved shell comb, tin key
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.557508 chunk_id=21331 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later? Case scope id: page-level-014. P...
  2. score=72.544897 chunk_id=21332 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later? Case scope id: page-level-014. P...
  3. score=53.548274 chunk_id=21334 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later? document page-birch-ferry-shed-a...
  4. score=7.615257 chunk_id=21645 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later? document page-birch-ferry-shed-a...
  5. score=7.587625 chunk_id=21646 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later? document page-birch-ferry-shed-a...
- Matched markers: carved shell comb, clay watering cup, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: carved shell comb, clay watering cup, tin key.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 15 - page-level-015
Question: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed?

Expected evidence:
- copper wind vane pin
- tin key

Expected distractors:
- star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.578638 chunk_id=21337 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? Case scope id: page-le...
  2. score=2.597175 chunk_id=21442 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-h...
  3. score=2.569814 chunk_id=21494 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? document page-driftwood...
  4. score=2.554051 chunk_id=21107 preview=document page-driftwood-cove-family-note-045::page-level-045, page 13, section section-045: In document page-driftwood-cove-family-note-045, page 13, section...
  5. score=2.541444 chunk_id=21121 preview=document page-harbor-glass-corridor-family-note-035::page-level-035, page 3, section section-035: In document page-harbor-glass-corridor-family-note-035, pag...
- Matched markers: copper wind vane pin, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: copper wind vane pin, tin key.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.575176 chunk_id=21337 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? Case scope id: page-le...
  2. score=60.570806 chunk_id=21336 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? Case scope id: page-le...
  3. score=41.560619 chunk_id=21338 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? document page-driftwoo...
  4. score=7.647464 chunk_id=21650 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? document page-driftwoo...
- Matched markers: copper wind vane pin, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper wind vane pin, tin key.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 4).

### Question 16 - page-level-016
Question: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Star Basin gallery?

Expected evidence:
- older sister
- amber lantern
- copper token

Expected distractors:
- oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.577931 chunk_id=21339 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Star Basin gallery? Case scope...
  2. score=72.612194 chunk_id=21340 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Star Basin gallery? Case scope...
  3. score=72.588690 chunk_id=21341 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Star Basin gallery? Case scope...
  4. score=72.564063 chunk_id=21342 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Star Basin gallery? Case scope...
  5. score=53.631316 chunk_id=21343 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Star Basin gallery? document pa...
- Matched markers: amber lantern, copper token, older sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, copper token, older sister.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.517547 chunk_id=21339 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Star Basin gallery? Case scope...
  2. score=72.563056 chunk_id=21340 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Star Basin gallery? Case scope...
  3. score=72.541066 chunk_id=21341 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Star Basin gallery? Case scope...
  4. score=72.528427 chunk_id=21342 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Star Basin gallery? Case scope...
  5. score=53.575626 chunk_id=21343 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Star Basin gallery? document pa...
- Matched markers: amber lantern, copper token, older sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, copper token, older sister.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 17 - page-level-017
Question: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor?

Expected evidence:
- blue oar
- star ledger page

Expected distractors:
- juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.328401 chunk_id=21345 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? Case scope id: page-level-017. Scope...
  2. score=60.351646 chunk_id=21346 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? Case scope id: page-level-017. Page-...
  3. score=60.336935 chunk_id=21347 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? Case scope id: page-level-017. Page-...
  4. score=41.357107 chunk_id=21348 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? document page-harbor-glass-corridor-...
  5. score=38.333604 chunk_id=21118 preview=document page-harbor-glass-corridor-family-note-017::page-level-017, page 2, section section-017: In document page-harbor-glass-corridor-family-note-017, pag...
- Matched markers: blue oar, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, star ledger page.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.340529 chunk_id=21346 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? Case scope id: page-level-017. Page-...
  2. score=60.308294 chunk_id=21347 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? Case scope id: page-level-017. Page-...
  3. score=41.340623 chunk_id=21348 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? document page-harbor-glass-corridor-...
  4. score=7.335041 chunk_id=21504 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? document page-harbor-glass-corridor-...
  5. score=4.294600 chunk_id=21123 preview=document page-harbor-glass-corridor-family-note-047::page-level-047, page 15, section section-047: In document page-harbor-glass-corridor-family-note-047, pa...
- Matched markers: blue oar, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, star ledger page.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 2).

### Question 18 - page-level-018
Question: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square?

Expected evidence:
- moonflower cutting
- oak barrel hoops
- Signal Lantern Morning

Expected distractors:
- coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.722764 chunk_id=21352 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  2. score=53.737045 chunk_id=21354 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? document page-bell-b...
  3. score=53.719263 chunk_id=21353 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? document page-bell-b...
  4. score=14.775000 chunk_id=21509 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square? document page-bell-b...
  5. score=14.723841 chunk_id=21510 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square? document page-bell-b...
- Matched markers: Signal Lantern Morning, moonflower cutting, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, moonflower cutting, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.615172 chunk_id=21349 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  2. score=72.632772 chunk_id=21352 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  3. score=72.630894 chunk_id=21351 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  4. score=72.614879 chunk_id=21350 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  5. score=53.643203 chunk_id=21354 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? document page-bell-b...
- Matched markers: Signal Lantern Morning, moonflower cutting, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, moonflower cutting, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 19 - page-level-019
Question: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later?

Expected evidence:
- lantern hook
- juniper bundles
- coal stove hiss

Expected distractors:
- basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=2.505668 chunk_id=21464 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
  2. score=2.499756 chunk_id=21463 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
  3. score=2.483265 chunk_id=21106 preview=document page-driftwood-cove-family-note-039::page-level-039, page 7, section section-039: In document page-driftwood-cove-family-note-039, page 7, section s...
- Matched markers: none
- Missing markers: lantern hook, juniper bundles, coal stove hiss
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.623361 chunk_id=21357 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later? Case scope id: page-level-019....
  2. score=72.619058 chunk_id=21356 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later? Case scope id: page-level-019....
  3. score=72.596326 chunk_id=21358 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later? Case scope id: page-level-019....
  4. score=53.611243 chunk_id=21360 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later? document page-river-lantern-in...
  5. score=53.606322 chunk_id=21359 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later? document page-river-lantern-in...
- Matched markers: coal stove hiss, juniper bundles, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, juniper bundles, lantern hook.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 20 - page-level-020
Question: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed?

Expected evidence:
- blue glass jar
- coal stove hiss

Expected distractors:
- willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.662923 chunk_id=21362 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? Case scope id: page-level-...
  2. score=60.622623 chunk_id=21363 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? Case scope id: page-level-...
  3. score=41.667942 chunk_id=21364 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? document page-birch-ferry-...
  4. score=38.633054 chunk_id=21087 preview=document page-birch-ferry-shed-audio-reel-020::page-level-020, page 5, section section-020: In document page-birch-ferry-shed-audio-reel-020, page 5, section...
  5. score=26.445833 chunk_id=21780 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin...
- Matched markers: blue glass jar, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, coal stove hiss.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.573051 chunk_id=21362 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? Case scope id: page-level-...
  2. score=60.546263 chunk_id=21363 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? Case scope id: page-level-...
  3. score=41.575410 chunk_id=21364 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? document page-birch-ferry-...
  4. score=7.639208 chunk_id=21676 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? document page-birch-ferry-...
  5. score=4.544995 chunk_id=21097 preview=document page-birch-ferry-shed-audio-reel-080::page-level-080, page 14, section section-080: In document page-birch-ferry-shed-audio-reel-080, page 14, secti...
- Matched markers: blue glass jar, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, coal stove hiss.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 2).

### Question 21 - page-level-021
Question: Which details on the profile page identify how Elena and the school friend prepared for the winter coach from Driftwood cove?

Expected evidence:
- school friend
- smoke vent chain
- basalt sketch

Expected distractors:
- birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.462034 chunk_id=21365 preview=Question anchor: Which details on the profile page identify how Elena and the school friend prepared for the winter coach from Driftwood cove? Case scope id:...
  2. score=72.523499 chunk_id=21366 preview=Question anchor: Which details on the profile page identify how Elena and the school friend prepared for the winter coach from Driftwood cove? Case scope id:...
  3. score=72.447074 chunk_id=21368 preview=Question anchor: Which details on the profile page identify how Elena and the school friend prepared for the winter coach from Driftwood cove? Case scope id:...
  4. score=72.429748 chunk_id=21367 preview=Question anchor: Which details on the profile page identify how Elena and the school friend prepared for the winter coach from Driftwood cove? Case scope id:...
  5. score=53.538549 chunk_id=21369 preview=Question anchor: Which details on the profile page identify how Elena and the school friend prepared for the winter coach from Driftwood cove? document page-...
- Matched markers: basalt sketch, school friend, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, school friend, smoke vent chain.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.363512 chunk_id=21365 preview=Question anchor: Which details on the profile page identify how Elena and the school friend prepared for the winter coach from Driftwood cove? Case scope id:...
  2. score=72.439910 chunk_id=21366 preview=Question anchor: Which details on the profile page identify how Elena and the school friend prepared for the winter coach from Driftwood cove? Case scope id:...
  3. score=72.398230 chunk_id=21367 preview=Question anchor: Which details on the profile page identify how Elena and the school friend prepared for the winter coach from Driftwood cove? Case scope id:...
  4. score=72.365502 chunk_id=21368 preview=Question anchor: Which details on the profile page identify how Elena and the school friend prepared for the winter coach from Driftwood cove? Case scope id:...
  5. score=53.444877 chunk_id=21369 preview=Question anchor: Which details on the profile page identify how Elena and the school friend prepared for the winter coach from Driftwood cove? document page-...
- Matched markers: basalt sketch, school friend, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, school friend, smoke vent chain.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 22 - page-level-022
Question: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery?

Expected evidence:
- violet ribbon
- willow basket

Expected distractors:
- weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.545356 chunk_id=21373 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? Case scope id: page-level-022. Page-leve...
  2. score=7.563902 chunk_id=21530 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? document page-star-basin-gallery-audio-r...
  3. score=4.557033 chunk_id=21155 preview=document page-star-basin-gallery-audio-reel-052::page-level-052, page 3, section section-052: In document page-star-basin-gallery-audio-reel-052, page 3, sec...
  4. score=2.093168 chunk_id=21426 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
- Matched markers: violet ribbon, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: violet ribbon, willow basket.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.417853 chunk_id=21372 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? Case scope id: page-level-022. Page-leve...
  2. score=60.410575 chunk_id=21373 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? Case scope id: page-level-022. Page-leve...
  3. score=41.421341 chunk_id=21374 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? document page-star-basin-gallery-audio-r...
  4. score=7.502558 chunk_id=21686 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? document page-star-basin-gallery-audio-r...
  5. score=7.423362 chunk_id=21530 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? document page-star-basin-gallery-audio-r...
- Matched markers: violet ribbon, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: violet ribbon, willow basket.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (2 vs 3).

### Question 23 - page-level-023
Question: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor?

Expected evidence:
- green apron
- birch tea flask
- Canal Night

Expected distractors:
- canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=19.804911 chunk_id=21691 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
  2. score=19.750000 chunk_id=21692 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
  3. score=16.732024 chunk_id=21129 preview=document page-harbor-glass-corridor-family-note-083::page-level-083, page 17, section section-083: In document page-harbor-glass-corridor-family-note-083, pa...
  4. score=14.562770 chunk_id=21536 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-...
  5. score=7.779515 chunk_id=21688 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-08...
- Matched markers: Canal Night
- Missing markers: green apron, birch tea flask
- Distractors: none
- Evidence coverage: 0.3333333333333333
- First relevant rank: 1
- Answer summary: Partially grounded by: Canal Night. Missing: green apron, birch tea flask.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=53.529843 chunk_id=21379 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
  2. score=53.516437 chunk_id=21380 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
  3. score=19.567384 chunk_id=21692 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
  4. score=19.524890 chunk_id=21691 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
  5. score=14.392045 chunk_id=21536 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-...
- Matched markers: Canal Night, birch tea flask, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, birch tea flask, green apron.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.33).

### Question 24 - page-level-024
Question: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later?

Expected evidence:
- paper moon mask
- weathered camera strap
- canal route map

Expected distractors:
- brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.652655 chunk_id=21383 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? Case scope id: page-level-024...
  2. score=72.612905 chunk_id=21382 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? Case scope id: page-level-024...
  3. score=53.657925 chunk_id=21386 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? document page-bell-bridge-squ...
  4. score=53.615240 chunk_id=21385 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? document page-bell-bridge-squ...
  5. score=7.605063 chunk_id=21698 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? document page-bell-bridge-squ...
- Matched markers: canal route map, paper moon mask, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map, paper moon mask, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.575425 chunk_id=21384 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? Case scope id: page-level-024...
  2. score=72.569975 chunk_id=21383 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? Case scope id: page-level-024...
  3. score=72.560380 chunk_id=21382 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? Case scope id: page-level-024...
  4. score=53.554222 chunk_id=21386 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? document page-bell-bridge-squ...
  5. score=53.545562 chunk_id=21385 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? document page-bell-bridge-squ...
- Matched markers: canal route map, paper moon mask, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map, paper moon mask, weathered camera strap.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 25 - page-level-025
Question: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed?

Expected evidence:
- saffron scarf
- canal route map

Expected distractors:
- tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=2.658944 chunk_id=21442 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-h...
  2. score=2.597895 chunk_id=21121 preview=document page-harbor-glass-corridor-family-note-035::page-level-035, page 3, section section-035: In document page-harbor-glass-corridor-family-note-035, pag...
  3. score=2.568399 chunk_id=21546 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? document page-river...
  4. score=2.525224 chunk_id=21598 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-ha...
- Matched markers: none
- Missing markers: saffron scarf, canal route map
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.610421 chunk_id=21389 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? Case scope id: page-...
  2. score=60.599171 chunk_id=21388 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? Case scope id: page-...
  3. score=41.581307 chunk_id=21390 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? document page-river-...
  4. score=7.607602 chunk_id=21702 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? document page-river-...
  5. score=2.597942 chunk_id=21546 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? document page-river...
- Matched markers: canal route map, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map, saffron scarf.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 26 - page-level-026
Question: Which details on the profile page identify how Anya and the widowed aunt prepared for the winter coach from Birch Ferry shed?

Expected evidence:
- widowed aunt
- wax thread
- brass compass

Expected distractors:
- silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.610775 chunk_id=21391 preview=Question anchor: Which details on the profile page identify how Anya and the widowed aunt prepared for the winter coach from Birch Ferry shed? Case scope id:...
  2. score=72.693858 chunk_id=21392 preview=Question anchor: Which details on the profile page identify how Anya and the widowed aunt prepared for the winter coach from Birch Ferry shed? Case scope id:...
  3. score=72.626123 chunk_id=21393 preview=Question anchor: Which details on the profile page identify how Anya and the widowed aunt prepared for the winter coach from Birch Ferry shed? Case scope id:...
  4. score=72.597134 chunk_id=21394 preview=Question anchor: Which details on the profile page identify how Anya and the widowed aunt prepared for the winter coach from Birch Ferry shed? Case scope id:...
  5. score=53.694513 chunk_id=21395 preview=Question anchor: Which details on the profile page identify how Anya and the widowed aunt prepared for the winter coach from Birch Ferry shed? document page-...
- Matched markers: brass compass, wax thread, widowed aunt
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass compass, wax thread, widowed aunt.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.557695 chunk_id=21391 preview=Question anchor: Which details on the profile page identify how Anya and the widowed aunt prepared for the winter coach from Birch Ferry shed? Case scope id:...
  2. score=72.616595 chunk_id=21392 preview=Question anchor: Which details on the profile page identify how Anya and the widowed aunt prepared for the winter coach from Birch Ferry shed? Case scope id:...
  3. score=72.593537 chunk_id=21393 preview=Question anchor: Which details on the profile page identify how Anya and the widowed aunt prepared for the winter coach from Birch Ferry shed? Case scope id:...
  4. score=72.546271 chunk_id=21394 preview=Question anchor: Which details on the profile page identify how Anya and the widowed aunt prepared for the winter coach from Birch Ferry shed? Case scope id:...
  5. score=53.626077 chunk_id=21395 preview=Question anchor: Which details on the profile page identify how Anya and the widowed aunt prepared for the winter coach from Birch Ferry shed? document page-...
- Matched markers: brass compass, wax thread, widowed aunt
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass compass, wax thread, widowed aunt.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 27 - page-level-027
Question: Which longer-page details in the family note describe the family memory scene at Driftwood cove?

Expected evidence:
- cedar shovel
- tuning fork

Expected distractors:
- glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.175926 chunk_id=21399 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? Case scope id: page-level-027. Page-level c...
  2. score=60.165912 chunk_id=21398 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? Case scope id: page-level-027. Page-level c...
  3. score=41.159975 chunk_id=21400 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? document page-driftwood-cove-family-note-02...
  4. score=38.152463 chunk_id=21104 preview=document page-driftwood-cove-family-note-027::page-level-027, page 12, section section-027: In document page-driftwood-cove-family-note-027, page 12, section...
  5. score=7.154101 chunk_id=21712 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? document page-driftwood-cove-family-note-08...
- Matched markers: cedar shovel, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.144893 chunk_id=21397 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? Case scope id: page-level-027. Scoped answe...
  2. score=60.160535 chunk_id=21398 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? Case scope id: page-level-027. Page-level c...
  3. score=60.147046 chunk_id=21399 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? Case scope id: page-level-027. Page-level c...
  4. score=41.171819 chunk_id=21400 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? document page-driftwood-cove-family-note-02...
  5. score=7.200636 chunk_id=21712 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? document page-driftwood-cove-family-note-08...
- Matched markers: cedar shovel, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, tuning fork.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 28 - page-level-028
Question: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery?

Expected evidence:
- linen wick
- silver booth token
- Signal Lantern Morning

Expected distractors:
- carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.709795 chunk_id=21401 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  2. score=72.720378 chunk_id=21404 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  3. score=72.717870 chunk_id=21403 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  4. score=53.747310 chunk_id=21406 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? document page-star-b...
  5. score=53.721746 chunk_id=21405 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? document page-star-b...
- Matched markers: Signal Lantern Morning, linen wick, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, linen wick, silver booth token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.634943 chunk_id=21404 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  2. score=72.628939 chunk_id=21403 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  3. score=72.618762 chunk_id=21402 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  4. score=53.641449 chunk_id=21406 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? document page-star-b...
  5. score=53.636751 chunk_id=21405 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? document page-star-b...
- Matched markers: Signal Lantern Morning, linen wick, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, linen wick, silver booth token.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 29 - page-level-029
Question: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later?

Expected evidence:
- rope bridge permit
- glass ink bottle
- carved shell comb

Expected distractors:
- tin key

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.639242 chunk_id=21409 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later? Case scope id: page-leve...
  2. score=72.594945 chunk_id=21408 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later? Case scope id: page-leve...
  3. score=53.641532 chunk_id=21412 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later? document page-harbor-gla...
  4. score=53.593819 chunk_id=21411 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later? document page-harbor-gla...
  5. score=2.245102 chunk_id=21464 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
- Matched markers: carved shell comb, glass ink bottle, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: carved shell comb, glass ink bottle, rope bridge permit.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.595297 chunk_id=21409 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later? Case scope id: page-leve...
  2. score=72.591426 chunk_id=21410 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later? Case scope id: page-leve...
  3. score=7.606031 chunk_id=21724 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later? document page-harbor-gla...
  4. score=2.622063 chunk_id=21567 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Harbor Glass corridor mattered later? document page-harbor-glass...
  5. score=2.610625 chunk_id=21568 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Harbor Glass corridor mattered later? document page-harbor-glass...
- Matched markers: carved shell comb, glass ink bottle, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: carved shell comb, glass ink bottle, rope bridge permit.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (1 vs 3).

### Question 30 - page-level-030
Question: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed?

Expected evidence:
- clay watering cup
- carved shell comb

Expected distractors:
- copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.626783 chunk_id=21414 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? Case scope id: page-level...
  2. score=41.626550 chunk_id=21416 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? document page-bell-bridge...
  3. score=7.660622 chunk_id=21728 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? document page-bell-bridge...
  4. score=4.633054 chunk_id=21083 preview=document page-bell-bridge-square-audio-reel-090::page-level-090, page 7, section section-090: In document page-bell-bridge-square-audio-reel-090, page 7, sec...
  5. score=2.645881 chunk_id=21572 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? document page-bell-bridg...
- Matched markers: carved shell comb, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: carved shell comb, clay watering cup.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.567563 chunk_id=21415 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? Case scope id: page-level...
  2. score=60.533234 chunk_id=21414 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? Case scope id: page-level...
  3. score=41.513597 chunk_id=21416 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? document page-bell-bridge...
  4. score=7.552297 chunk_id=21728 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? document page-bell-bridge...
  5. score=2.515663 chunk_id=21572 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? document page-bell-bridg...
- Matched markers: carved shell comb, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: carved shell comb, clay watering cup.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (2 vs 3).

### Question 31 - page-level-031
Question: Which details on the profile page identify how Raisa and the foster son prepared for the winter coach from River Lantern inn?

Expected evidence:
- foster son
- copper wind vane pin
- tin key

Expected distractors:
- star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.557231 chunk_id=21418 preview=Question anchor: Which details on the profile page identify how Raisa and the foster son prepared for the winter coach from River Lantern inn? Case scope id:...
  2. score=53.552038 chunk_id=21421 preview=Question anchor: Which details on the profile page identify how Raisa and the foster son prepared for the winter coach from River Lantern inn? document page-...
  3. score=1.822366 chunk_id=21629 preview=Question anchor: Which details on the profile page identify how Raisa and the grandmother prepared for the winter coach from Harbor Glass corridor? document...
  4. score=1.636912 chunk_id=21707 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Birch Ferry shed? document page-bir...
- Matched markers: copper wind vane pin, foster son, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: copper wind vane pin, foster son, tin key.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.469164 chunk_id=21417 preview=Question anchor: Which details on the profile page identify how Raisa and the foster son prepared for the winter coach from River Lantern inn? Case scope id:...
  2. score=72.522493 chunk_id=21418 preview=Question anchor: Which details on the profile page identify how Raisa and the foster son prepared for the winter coach from River Lantern inn? Case scope id:...
  3. score=72.486895 chunk_id=21420 preview=Question anchor: Which details on the profile page identify how Raisa and the foster son prepared for the winter coach from River Lantern inn? Case scope id:...
  4. score=72.470064 chunk_id=21419 preview=Question anchor: Which details on the profile page identify how Raisa and the foster son prepared for the winter coach from River Lantern inn? Case scope id:...
  5. score=53.534114 chunk_id=21421 preview=Question anchor: Which details on the profile page identify how Raisa and the foster son prepared for the winter coach from River Lantern inn? document page-...
- Matched markers: copper wind vane pin, foster son, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper wind vane pin, foster son, tin key.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 2).

### Question 32 - page-level-032
Question: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed?

Expected evidence:
- amber lantern
- copper token

Expected distractors:
- oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.573927 chunk_id=21423 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? Case scope id: page-level-032. Scoped answ...
  2. score=60.595701 chunk_id=21424 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? Case scope id: page-level-032. Page-level...
  3. score=60.573532 chunk_id=21425 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? Case scope id: page-level-032. Page-level...
  4. score=41.614100 chunk_id=21426 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
  5. score=38.586583 chunk_id=21089 preview=document page-birch-ferry-shed-audio-reel-032::page-level-032, page 17, section section-032: In document page-birch-ferry-shed-audio-reel-032, page 17, secti...
- Matched markers: amber lantern, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, copper token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.416618 chunk_id=21423 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? Case scope id: page-level-032. Scoped answ...
  2. score=60.431124 chunk_id=21425 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? Case scope id: page-level-032. Page-level...
  3. score=60.424056 chunk_id=21424 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? Case scope id: page-level-032. Page-level...
  4. score=41.430943 chunk_id=21426 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
  5. score=7.458731 chunk_id=21738 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
- Matched markers: amber lantern, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, copper token.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 33 - page-level-033
Question: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove?

Expected evidence:
- blue oar
- star ledger page
- Canal Night

Expected distractors:
- juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.564119 chunk_id=21430 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? Case scope id: page-level-033. Pag...
  2. score=72.538177 chunk_id=21428 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? Case scope id: page-level-033. Pag...
  3. score=53.558426 chunk_id=21431 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
  4. score=19.553202 chunk_id=21744 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
  5. score=19.533333 chunk_id=21743 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
- Matched markers: Canal Night, blue oar, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, blue oar, star ledger page.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.321862 chunk_id=21429 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? Case scope id: page-level-033. Pag...
  2. score=72.316936 chunk_id=21430 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? Case scope id: page-level-033. Pag...
  3. score=53.335716 chunk_id=21432 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
  4. score=53.324132 chunk_id=21431 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
  5. score=19.329150 chunk_id=21744 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
- Matched markers: Canal Night, blue oar, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, blue oar, star ledger page.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 34 - page-level-034
Question: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later?

Expected evidence:
- moonflower cutting
- oak barrel hoops
- juniper bundles

Expected distractors:
- coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.731975 chunk_id=21435 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? Case scope id: page-level-034....
  2. score=72.690957 chunk_id=21434 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? Case scope id: page-level-034....
  3. score=72.679366 chunk_id=21436 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? Case scope id: page-level-034....
  4. score=53.749930 chunk_id=21438 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? document page-star-basin-galle...
  5. score=53.705139 chunk_id=21437 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? document page-star-basin-galle...
- Matched markers: juniper bundles, moonflower cutting, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles, moonflower cutting, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.577708 chunk_id=21434 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? Case scope id: page-level-034....
  2. score=53.572928 chunk_id=21437 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? document page-star-basin-galle...
  3. score=7.578261 chunk_id=21750 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? document page-star-basin-galle...
  4. score=2.620793 chunk_id=21594 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? document page-star-basin-gall...
  5. score=2.613463 chunk_id=21593 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? document page-star-basin-gall...
- Matched markers: juniper bundles, moonflower cutting, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: juniper bundles, moonflower cutting, oak barrel hoops.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 3).

### Question 35 - page-level-035
Question: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed?

Expected evidence:
- lantern hook
- juniper bundles

Expected distractors:
- basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.632455 chunk_id=21439 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? Case scope id:...
  2. score=60.688528 chunk_id=21440 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? Case scope id:...
  3. score=60.638311 chunk_id=21441 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? Case scope id:...
  4. score=41.711365 chunk_id=21442 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-h...
  5. score=38.646997 chunk_id=21121 preview=document page-harbor-glass-corridor-family-note-035::page-level-035, page 3, section section-035: In document page-harbor-glass-corridor-family-note-035, pag...
- Matched markers: juniper bundles, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.640313 chunk_id=21439 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? Case scope id:...
  2. score=60.685401 chunk_id=21440 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? Case scope id:...
  3. score=60.674108 chunk_id=21441 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? Case scope id:...
  4. score=41.685740 chunk_id=21442 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-h...
  5. score=38.616079 chunk_id=21121 preview=document page-harbor-glass-corridor-family-note-035::page-level-035, page 3, section section-035: In document page-harbor-glass-corridor-family-note-035, pag...
- Matched markers: juniper bundles, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles, lantern hook.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 36 - page-level-036
Question: Which details on the profile page identify how Iveta and the twin sister prepared for the winter coach from Bell Bridge square?

Expected evidence:
- twin sister
- blue glass jar
- coal stove hiss

Expected distractors:
- willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.569987 chunk_id=21444 preview=Question anchor: Which details on the profile page identify how Iveta and the twin sister prepared for the winter coach from Bell Bridge square? Case scope i...
  2. score=53.582456 chunk_id=21447 preview=Question anchor: Which details on the profile page identify how Iveta and the twin sister prepared for the winter coach from Bell Bridge square? document pag...
  3. score=53.528088 chunk_id=21448 preview=Question anchor: Which details on the profile page identify how Iveta and the twin sister prepared for the winter coach from Bell Bridge square? document pag...
  4. score=2.461300 chunk_id=21759 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Bell Bridge square? document pa...
  5. score=2.433102 chunk_id=21760 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Bell Bridge square? document pa...
- Matched markers: blue glass jar, coal stove hiss, twin sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, coal stove hiss, twin sister.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.468728 chunk_id=21444 preview=Question anchor: Which details on the profile page identify how Iveta and the twin sister prepared for the winter coach from Bell Bridge square? Case scope i...
  2. score=72.448801 chunk_id=21445 preview=Question anchor: Which details on the profile page identify how Iveta and the twin sister prepared for the winter coach from Bell Bridge square? Case scope i...
  3. score=72.424098 chunk_id=21446 preview=Question anchor: Which details on the profile page identify how Iveta and the twin sister prepared for the winter coach from Bell Bridge square? Case scope i...
  4. score=53.478300 chunk_id=21447 preview=Question anchor: Which details on the profile page identify how Iveta and the twin sister prepared for the winter coach from Bell Bridge square? document pag...
  5. score=53.456492 chunk_id=21448 preview=Question anchor: Which details on the profile page identify how Iveta and the twin sister prepared for the winter coach from Bell Bridge square? document pag...
- Matched markers: blue glass jar, coal stove hiss, twin sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, coal stove hiss, twin sister.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 2).

### Question 37 - page-level-037
Question: Which longer-page details in the family note describe the family memory scene at River Lantern inn?

Expected evidence:
- smoke vent chain
- basalt sketch

Expected distractors:
- birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.325664 chunk_id=21451 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? Case scope id: page-level-037. Page-leve...
  2. score=2.028064 chunk_id=21426 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
- Matched markers: basalt sketch, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: basalt sketch, smoke vent chain.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.289531 chunk_id=21450 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? Case scope id: page-level-037. Page-leve...
  2. score=41.297287 chunk_id=21452 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
  3. score=7.298607 chunk_id=21608 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
  4. score=7.294621 chunk_id=21764 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
- Matched markers: basalt sketch, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, smoke vent chain.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (2 vs 1).

### Question 38 - page-level-038
Question: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed?

Expected evidence:
- violet ribbon
- willow basket
- Signal Lantern Morning

Expected distractors:
- weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.722764 chunk_id=21456 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? Case scope id: page-le...
  2. score=53.737046 chunk_id=21458 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  3. score=19.737046 chunk_id=21770 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  4. score=14.711088 chunk_id=21613 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  5. score=14.374212 chunk_id=21562 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery? document page-star-b...
- Matched markers: Signal Lantern Morning, violet ribbon, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, violet ribbon, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.630194 chunk_id=21456 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? Case scope id: page-le...
  2. score=53.634117 chunk_id=21458 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  3. score=53.632689 chunk_id=21457 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  4. score=19.701631 chunk_id=21770 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  5. score=19.693200 chunk_id=21769 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
- Matched markers: Signal Lantern Morning, violet ribbon, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, violet ribbon, willow basket.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 39 - page-level-039
Question: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later?

Expected evidence:
- green apron
- birch tea flask
- weathered camera strap

Expected distractors:
- canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.681896 chunk_id=21459 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? Case scope id: page-level-039. Sc...
  2. score=72.720682 chunk_id=21461 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? Case scope id: page-level-039. Pa...
  3. score=72.719741 chunk_id=21460 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? Case scope id: page-level-039. Pa...
  4. score=72.714021 chunk_id=21462 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? Case scope id: page-level-039. Pa...
  5. score=53.721336 chunk_id=21464 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
- Matched markers: birch tea flask, green apron, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, green apron, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.572147 chunk_id=21460 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? Case scope id: page-level-039. Pa...
  2. score=72.539283 chunk_id=21462 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? Case scope id: page-level-039. Pa...
  3. score=72.535478 chunk_id=21461 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? Case scope id: page-level-039. Pa...
  4. score=53.564387 chunk_id=21463 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
  5. score=7.571971 chunk_id=21776 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
- Matched markers: birch tea flask, green apron, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, green apron, weathered camera strap.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 40 - page-level-040
Question: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed?

Expected evidence:
- paper moon mask
- weathered camera strap

Expected distractors:
- brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=7.694365 chunk_id=21780 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin...
  2. score=4.664292 chunk_id=21163 preview=document page-star-basin-gallery-audio-reel-100::page-level-100, page 17, section section-100: In document page-star-basin-gallery-audio-reel-100, page 17, s...
  3. score=2.617570 chunk_id=21624 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin-...
  4. score=2.418394 chunk_id=21364 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? document page-birch-ferry-...
- Matched markers: none
- Missing markers: paper moon mask, weathered camera strap
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.607978 chunk_id=21466 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-leve...
  2. score=60.601634 chunk_id=21467 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-leve...
  3. score=41.599466 chunk_id=21468 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin...
  4. score=7.654844 chunk_id=21780 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin...
- Matched markers: paper moon mask, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: paper moon mask, weathered camera strap.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 41 - page-level-041
Question: Which details on the profile page identify how Elena and the nephew prepared for the winter coach from Harbor Glass corridor?

Expected evidence:
- nephew
- saffron scarf
- canal route map

Expected distractors:
- tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.481932 chunk_id=21470 preview=Question anchor: Which details on the profile page identify how Elena and the nephew prepared for the winter coach from Harbor Glass corridor? Case scope id:...
  2. score=72.400481 chunk_id=21471 preview=Question anchor: Which details on the profile page identify how Elena and the nephew prepared for the winter coach from Harbor Glass corridor? Case scope id:...
  3. score=72.378858 chunk_id=21472 preview=Question anchor: Which details on the profile page identify how Elena and the nephew prepared for the winter coach from Harbor Glass corridor? Case scope id:...
  4. score=53.487885 chunk_id=21473 preview=Question anchor: Which details on the profile page identify how Elena and the nephew prepared for the winter coach from Harbor Glass corridor? document page-...
  5. score=53.397505 chunk_id=21474 preview=Question anchor: Which details on the profile page identify how Elena and the nephew prepared for the winter coach from Harbor Glass corridor? document page-...
- Matched markers: canal route map, nephew, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map, nephew, saffron scarf.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.350652 chunk_id=21470 preview=Question anchor: Which details on the profile page identify how Elena and the nephew prepared for the winter coach from Harbor Glass corridor? Case scope id:...
  2. score=72.331556 chunk_id=21472 preview=Question anchor: Which details on the profile page identify how Elena and the nephew prepared for the winter coach from Harbor Glass corridor? Case scope id:...
  3. score=72.313776 chunk_id=21471 preview=Question anchor: Which details on the profile page identify how Elena and the nephew prepared for the winter coach from Harbor Glass corridor? Case scope id:...
  4. score=53.362839 chunk_id=21473 preview=Question anchor: Which details on the profile page identify how Elena and the nephew prepared for the winter coach from Harbor Glass corridor? document page-...
  5. score=53.322043 chunk_id=21474 preview=Question anchor: Which details on the profile page identify how Elena and the nephew prepared for the winter coach from Harbor Glass corridor? document page-...
- Matched markers: canal route map, nephew, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map, nephew, saffron scarf.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 42 - page-level-042
Question: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square?

Expected evidence:
- wax thread
- brass compass

Expected distractors:
- silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.448431 chunk_id=21476 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? Case scope id: page-level-042. Page-leve...
  2. score=41.451370 chunk_id=21478 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? document page-bell-bridge-square-audio-r...
  3. score=2.006532 chunk_id=21426 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
- Matched markers: brass compass, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass compass, wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.418279 chunk_id=21475 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? Case scope id: page-level-042. Scoped an...
  2. score=60.473447 chunk_id=21476 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? Case scope id: page-level-042. Page-leve...
  3. score=60.433651 chunk_id=21477 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? Case scope id: page-level-042. Page-leve...
  4. score=41.463887 chunk_id=21478 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? document page-bell-bridge-square-audio-r...
  5. score=38.378781 chunk_id=21075 preview=document page-bell-bridge-square-audio-reel-042::page-level-042, page 10, section section-042: In document page-bell-bridge-square-audio-reel-042, page 10, s...
- Matched markers: brass compass, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass compass, wax thread.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 43 - page-level-043
Question: Which profile-page details explain what Kira kept for the Canal Night after returning to River Lantern inn?

Expected evidence:
- cedar shovel
- tuning fork
- Canal Night

Expected distractors:
- glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.692858 chunk_id=21482 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to River Lantern inn? Case scope id: page-level-043. P...
  2. score=14.432034 chunk_id=21691 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
  3. score=6.518106 chunk_id=21328 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn? document page-river-lantern-inn...
  4. score=2.414217 chunk_id=21690 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-08...
  5. score=2.413763 chunk_id=21688 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-08...
- Matched markers: Canal Night, cedar shovel, tuning fork
- Missing markers: none
- Distractors: glass ink bottle
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: Canal Night, cedar shovel, tuning fork. Distractors present: glass ink bottle.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.514152 chunk_id=21481 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to River Lantern inn? Case scope id: page-level-043. P...
  2. score=72.489331 chunk_id=21480 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to River Lantern inn? Case scope id: page-level-043. P...
  3. score=72.485867 chunk_id=21482 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to River Lantern inn? Case scope id: page-level-043. P...
  4. score=53.527421 chunk_id=21484 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to River Lantern inn? document page-river-lantern-inn-...
  5. score=53.505075 chunk_id=21483 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to River Lantern inn? document page-river-lantern-inn-...
- Matched markers: Canal Night, cedar shovel, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, cedar shovel, tuning fork.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 44 - page-level-044
Question: Which page-level notes from the audio reel show why Nadia's photo memory at Birch Ferry shed mattered later?

Expected evidence:
- linen wick
- silver booth token
- glass ink bottle

Expected distractors:
- carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.710311 chunk_id=21487 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Birch Ferry shed mattered later? Case scope id: page-level-044....
  2. score=72.665982 chunk_id=21486 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Birch Ferry shed mattered later? Case scope id: page-level-044....
  3. score=53.724947 chunk_id=21490 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Birch Ferry shed mattered later? document page-birch-ferry-shed-...
  4. score=53.676491 chunk_id=21489 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Birch Ferry shed mattered later? document page-birch-ferry-shed-...
  5. score=2.499206 chunk_id=21594 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? document page-star-basin-gall...
- Matched markers: glass ink bottle, linen wick, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, linen wick, silver booth token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.547982 chunk_id=21486 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Birch Ferry shed mattered later? Case scope id: page-level-044....
  2. score=2.615257 chunk_id=21645 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later? document page-birch-ferry-shed-a...
  3. score=2.587625 chunk_id=21646 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later? document page-birch-ferry-shed-a...
- Matched markers: glass ink bottle, linen wick, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: glass ink bottle, linen wick, silver booth token.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (1 vs 2).

### Question 45 - page-level-045
Question: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed?

Expected evidence:
- rope bridge permit
- glass ink bottle

Expected distractors:
- tin key

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.589256 chunk_id=21493 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? Case scope id: page-lev...
  2. score=60.570835 chunk_id=21492 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? Case scope id: page-lev...
  3. score=41.569814 chunk_id=21494 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? document page-driftwood...
  4. score=38.554051 chunk_id=21107 preview=document page-driftwood-cove-family-note-045::page-level-045, page 13, section section-045: In document page-driftwood-cove-family-note-045, page 13, section...
  5. score=2.447175 chunk_id=21442 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-h...
- Matched markers: glass ink bottle, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, rope bridge permit.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.564279 chunk_id=21491 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? Case scope id: page-lev...
  2. score=60.608676 chunk_id=21493 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? Case scope id: page-lev...
  3. score=60.604324 chunk_id=21492 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? Case scope id: page-lev...
  4. score=41.585073 chunk_id=21494 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? document page-driftwood...
  5. score=2.597660 chunk_id=21650 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? document page-driftwoo...
- Matched markers: glass ink bottle, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, rope bridge permit.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 46 - page-level-046
Question: Which details on the profile page identify how Anya and the niece prepared for the winter coach from Star Basin gallery?

Expected evidence:
- niece
- clay watering cup
- carved shell comb

Expected distractors:
- copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.504538 chunk_id=21496 preview=Question anchor: Which details on the profile page identify how Anya and the niece prepared for the winter coach from Star Basin gallery? Case scope id: page...
  2. score=72.428517 chunk_id=21497 preview=Question anchor: Which details on the profile page identify how Anya and the niece prepared for the winter coach from Star Basin gallery? Case scope id: page...
  3. score=72.426300 chunk_id=21498 preview=Question anchor: Which details on the profile page identify how Anya and the niece prepared for the winter coach from Star Basin gallery? Case scope id: page...
  4. score=53.513247 chunk_id=21499 preview=Question anchor: Which details on the profile page identify how Anya and the niece prepared for the winter coach from Star Basin gallery? document page-star-...
  5. score=53.429171 chunk_id=21500 preview=Question anchor: Which details on the profile page identify how Anya and the niece prepared for the winter coach from Star Basin gallery? document page-star-...
- Matched markers: carved shell comb, clay watering cup, niece
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: carved shell comb, clay watering cup, niece.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.348653 chunk_id=21495 preview=Question anchor: Which details on the profile page identify how Anya and the niece prepared for the winter coach from Star Basin gallery? Case scope id: page...
  2. score=72.418863 chunk_id=21496 preview=Question anchor: Which details on the profile page identify how Anya and the niece prepared for the winter coach from Star Basin gallery? Case scope id: page...
  3. score=72.387505 chunk_id=21498 preview=Question anchor: Which details on the profile page identify how Anya and the niece prepared for the winter coach from Star Basin gallery? Case scope id: page...
  4. score=72.377240 chunk_id=21497 preview=Question anchor: Which details on the profile page identify how Anya and the niece prepared for the winter coach from Star Basin gallery? Case scope id: page...
  5. score=53.429849 chunk_id=21499 preview=Question anchor: Which details on the profile page identify how Anya and the niece prepared for the winter coach from Star Basin gallery? document page-star-...
- Matched markers: carved shell comb, clay watering cup, niece
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: carved shell comb, clay watering cup, niece.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 47 - page-level-047
Question: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor?

Expected evidence:
- copper wind vane pin
- tin key

Expected distractors:
- star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.361660 chunk_id=21503 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? Case scope id: page-level-047. Page-...
  2. score=7.324019 chunk_id=21660 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? document page-harbor-glass-corridor-...
  3. score=4.328571 chunk_id=21128 preview=document page-harbor-glass-corridor-family-note-077::page-level-077, page 11, section section-077: In document page-harbor-glass-corridor-family-note-077, pa...
- Matched markers: copper wind vane pin, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: copper wind vane pin, tin key.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.325275 chunk_id=21501 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? Case scope id: page-level-047. Scope...
  2. score=60.368044 chunk_id=21503 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? Case scope id: page-level-047. Page-...
  3. score=60.339374 chunk_id=21502 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? Case scope id: page-level-047. Page-...
  4. score=41.335041 chunk_id=21504 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? document page-harbor-glass-corridor-...
  5. score=38.294600 chunk_id=21123 preview=document page-harbor-glass-corridor-family-note-047::page-level-047, page 15, section section-047: In document page-harbor-glass-corridor-family-note-047, pa...
- Matched markers: copper wind vane pin, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper wind vane pin, tin key.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 2).

### Question 48 - page-level-048
Question: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square?

Expected evidence:
- amber lantern
- copper token
- Signal Lantern Morning

Expected distractors:
- oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.742352 chunk_id=21505 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  2. score=72.776757 chunk_id=21506 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  3. score=72.772849 chunk_id=21508 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  4. score=72.731073 chunk_id=21507 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  5. score=53.798762 chunk_id=21509 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square? document page-bell-b...
- Matched markers: Signal Lantern Morning, amber lantern, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, amber lantern, copper token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.633369 chunk_id=21505 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  2. score=72.668269 chunk_id=21507 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  3. score=72.661574 chunk_id=21508 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  4. score=72.647006 chunk_id=21506 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  5. score=53.679657 chunk_id=21510 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square? document page-bell-b...
- Matched markers: Signal Lantern Morning, amber lantern, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, amber lantern, copper token.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 49 - page-level-049
Question: Which page-level notes from the family note show why Milena's photo memory at River Lantern inn mattered later?

Expected evidence:
- blue oar
- star ledger page
- oak barrel hoops

Expected distractors:
- juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=2.401568 chunk_id=21412 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later? document page-harbor-gla...
  2. score=2.315344 chunk_id=21464 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
  3. score=2.307346 chunk_id=21463 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
  4. score=2.306985 chunk_id=21106 preview=document page-driftwood-cove-family-note-039::page-level-039, page 7, section section-039: In document page-driftwood-cove-family-note-039, page 7, section s...
- Matched markers: none
- Missing markers: blue oar, star ledger page, oak barrel hoops
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.570792 chunk_id=21512 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at River Lantern inn mattered later? Case scope id: page-level-04...
  2. score=53.559948 chunk_id=21515 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at River Lantern inn mattered later? document page-river-lantern-...
  3. score=2.559383 chunk_id=21672 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later? document page-river-lantern-in...
- Matched markers: blue oar, oak barrel hoops, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: blue oar, oak barrel hoops, star ledger page.
- Verdict: partial

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 50 - page-level-050
Question: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed?

Expected evidence:
- moonflower cutting
- oak barrel hoops

Expected distractors:
- coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.613186 chunk_id=21517 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? Case scope id: page-level-0...
  2. score=60.615845 chunk_id=21519 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? Case scope id: page-level-0...
  3. score=60.608612 chunk_id=21518 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? Case scope id: page-level-0...
  4. score=41.619752 chunk_id=21520 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? document page-birch-ferry-s...
  5. score=2.431995 chunk_id=21312 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin-...
- Matched markers: moonflower cutting, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: moonflower cutting, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.561471 chunk_id=21518 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? Case scope id: page-level-0...
  2. score=60.534439 chunk_id=21519 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? Case scope id: page-level-0...
  3. score=41.555958 chunk_id=21520 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? document page-birch-ferry-s...
  4. score=2.581098 chunk_id=21676 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? document page-birch-ferry-...
  5. score=2.512936 chunk_id=21097 preview=document page-birch-ferry-shed-audio-reel-080::page-level-080, page 14, section section-080: In document page-birch-ferry-shed-audio-reel-080, page 14, secti...
- Matched markers: moonflower cutting, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: moonflower cutting, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (1 vs 2).

### Question 51 - page-level-051
Question: Which details on the profile page identify how Raisa and the godson prepared for the winter coach from Driftwood cove?

Expected evidence:
- godson
- lantern hook
- juniper bundles

Expected distractors:
- basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.290292 chunk_id=21521 preview=Question anchor: Which details on the profile page identify how Raisa and the godson prepared for the winter coach from Driftwood cove? Case scope id: page-l...
  2. score=72.325077 chunk_id=21522 preview=Question anchor: Which details on the profile page identify how Raisa and the godson prepared for the winter coach from Driftwood cove? Case scope id: page-l...
  3. score=72.298353 chunk_id=21523 preview=Question anchor: Which details on the profile page identify how Raisa and the godson prepared for the winter coach from Driftwood cove? Case scope id: page-l...
  4. score=72.272752 chunk_id=21524 preview=Question anchor: Which details on the profile page identify how Raisa and the godson prepared for the winter coach from Driftwood cove? Case scope id: page-l...
  5. score=53.342020 chunk_id=21525 preview=Question anchor: Which details on the profile page identify how Raisa and the godson prepared for the winter coach from Driftwood cove? document page-driftwo...
- Matched markers: godson, juniper bundles, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: godson, juniper bundles, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.175605 chunk_id=21521 preview=Question anchor: Which details on the profile page identify how Raisa and the godson prepared for the winter coach from Driftwood cove? Case scope id: page-l...
  2. score=72.222226 chunk_id=21522 preview=Question anchor: Which details on the profile page identify how Raisa and the godson prepared for the winter coach from Driftwood cove? Case scope id: page-l...
  3. score=72.191936 chunk_id=21523 preview=Question anchor: Which details on the profile page identify how Raisa and the godson prepared for the winter coach from Driftwood cove? Case scope id: page-l...
  4. score=72.186195 chunk_id=21524 preview=Question anchor: Which details on the profile page identify how Raisa and the godson prepared for the winter coach from Driftwood cove? Case scope id: page-l...
  5. score=53.229691 chunk_id=21525 preview=Question anchor: Which details on the profile page identify how Raisa and the godson prepared for the winter coach from Driftwood cove? document page-driftwo...
- Matched markers: godson, juniper bundles, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: godson, juniper bundles, lantern hook.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 52 - page-level-052
Question: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery?

Expected evidence:
- blue glass jar
- coal stove hiss

Expected distractors:
- willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.525011 chunk_id=21527 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? Case scope id: page-level-052. Scoped an...
  2. score=60.554760 chunk_id=21528 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? Case scope id: page-level-052. Page-leve...
  3. score=60.546914 chunk_id=21529 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? Case scope id: page-level-052. Page-leve...
  4. score=41.563902 chunk_id=21530 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? document page-star-basin-gallery-audio-r...
  5. score=38.557033 chunk_id=21155 preview=document page-star-basin-gallery-audio-reel-052::page-level-052, page 3, section section-052: In document page-star-basin-gallery-audio-reel-052, page 3, sec...
- Matched markers: blue glass jar, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, coal stove hiss.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.417242 chunk_id=21528 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? Case scope id: page-level-052. Page-leve...
  2. score=41.423362 chunk_id=21530 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? document page-star-basin-gallery-audio-r...
  3. score=7.502558 chunk_id=21686 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? document page-star-basin-gallery-audio-r...
  4. score=4.452462 chunk_id=21160 preview=document page-star-basin-gallery-audio-reel-082::page-level-082, page 16, section section-082: In document page-star-basin-gallery-audio-reel-082, page 16, s...
- Matched markers: blue glass jar, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, coal stove hiss.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 2).

### Question 53 - page-level-053
Question: Which profile-page details explain what Talia kept for the Canal Night after returning to Harbor Glass corridor?

Expected evidence:
- smoke vent chain
- basalt sketch
- Canal Night

Expected distractors:
- birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.740569 chunk_id=21534 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-0...
  2. score=72.695394 chunk_id=21533 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-0...
  3. score=53.712770 chunk_id=21536 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-...
  4. score=14.654911 chunk_id=21691 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
  5. score=14.600000 chunk_id=21692 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
- Matched markers: Canal Night, basalt sketch, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, basalt sketch, smoke vent chain.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.529689 chunk_id=21533 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-0...
  2. score=72.516393 chunk_id=21534 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-0...
  3. score=53.542045 chunk_id=21536 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-...
  4. score=53.521429 chunk_id=21535 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-...
  5. score=14.417385 chunk_id=21692 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
- Matched markers: Canal Night, basalt sketch, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, basalt sketch, smoke vent chain.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 54 - page-level-054
Question: Which page-level notes from the audio reel show why Runa's photo memory at Bell Bridge square mattered later?

Expected evidence:
- violet ribbon
- willow basket
- birch tea flask

Expected distractors:
- weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.605644 chunk_id=21537 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Bell Bridge square mattered later? Case scope id: page-level-054....
  2. score=72.650929 chunk_id=21539 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Bell Bridge square mattered later? Case scope id: page-level-054....
  3. score=72.611312 chunk_id=21538 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Bell Bridge square mattered later? Case scope id: page-level-054....
  4. score=72.606150 chunk_id=21540 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Bell Bridge square mattered later? Case scope id: page-level-054....
  5. score=53.668734 chunk_id=21542 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Bell Bridge square mattered later? document page-bell-bridge-squa...
- Matched markers: birch tea flask, violet ribbon, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, violet ribbon, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=2.558015 chunk_id=21697 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? document page-bell-bridge-squ...
  2. score=2.554826 chunk_id=21698 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? document page-bell-bridge-squ...
- Matched markers: none
- Missing markers: violet ribbon, willow basket, birch tea flask
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 55 - page-level-055
Question: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed?

Expected evidence:
- green apron
- birch tea flask

Expected distractors:
- canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.568812 chunk_id=21544 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? Case scope id: page...
  2. score=60.565414 chunk_id=21545 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? Case scope id: page...
  3. score=41.568399 chunk_id=21546 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? document page-river...
  4. score=2.708944 chunk_id=21442 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-h...
  5. score=2.647895 chunk_id=21121 preview=document page-harbor-glass-corridor-family-note-035::page-level-035, page 3, section section-035: In document page-harbor-glass-corridor-family-note-035, pag...
- Matched markers: birch tea flask, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, green apron.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.581847 chunk_id=21543 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? Case scope id: page...
  2. score=60.657350 chunk_id=21544 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? Case scope id: page...
  3. score=60.602766 chunk_id=21545 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? Case scope id: page...
  4. score=41.644535 chunk_id=21546 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? document page-river...
  5. score=2.561455 chunk_id=21702 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? document page-river-...
- Matched markers: birch tea flask, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, green apron.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 2).

### Question 56 - page-level-056
Question: Which details on the profile page identify how Iveta and the stepfather prepared for the winter coach from Birch Ferry shed?

Expected evidence:
- stepfather
- paper moon mask
- weathered camera strap

Expected distractors:
- brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.412077 chunk_id=21547 preview=Question anchor: Which details on the profile page identify how Iveta and the stepfather prepared for the winter coach from Birch Ferry shed? Case scope id:...
  2. score=72.476325 chunk_id=21548 preview=Question anchor: Which details on the profile page identify how Iveta and the stepfather prepared for the winter coach from Birch Ferry shed? Case scope id:...
  3. score=72.410342 chunk_id=21550 preview=Question anchor: Which details on the profile page identify how Iveta and the stepfather prepared for the winter coach from Birch Ferry shed? Case scope id:...
  4. score=72.391597 chunk_id=21549 preview=Question anchor: Which details on the profile page identify how Iveta and the stepfather prepared for the winter coach from Birch Ferry shed? Case scope id:...
  5. score=53.490292 chunk_id=21551 preview=Question anchor: Which details on the profile page identify how Iveta and the stepfather prepared for the winter coach from Birch Ferry shed? document page-b...
- Matched markers: paper moon mask, stepfather, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: paper moon mask, stepfather, weathered camera strap.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.280814 chunk_id=21547 preview=Question anchor: Which details on the profile page identify how Iveta and the stepfather prepared for the winter coach from Birch Ferry shed? Case scope id:...
  2. score=72.356455 chunk_id=21548 preview=Question anchor: Which details on the profile page identify how Iveta and the stepfather prepared for the winter coach from Birch Ferry shed? Case scope id:...
  3. score=72.312969 chunk_id=21550 preview=Question anchor: Which details on the profile page identify how Iveta and the stepfather prepared for the winter coach from Birch Ferry shed? Case scope id:...
  4. score=72.305824 chunk_id=21549 preview=Question anchor: Which details on the profile page identify how Iveta and the stepfather prepared for the winter coach from Birch Ferry shed? Case scope id:...
  5. score=53.360792 chunk_id=21551 preview=Question anchor: Which details on the profile page identify how Iveta and the stepfather prepared for the winter coach from Birch Ferry shed? document page-b...
- Matched markers: paper moon mask, stepfather, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: paper moon mask, stepfather, weathered camera strap.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 57 - page-level-057
Question: Which longer-page details in the family note describe the family memory scene at Driftwood cove?

Expected evidence:
- saffron scarf
- canal route map

Expected distractors:
- tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.160701 chunk_id=21554 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? Case scope id: page-level-057. Page-level c...
  2. score=60.146460 chunk_id=21555 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? Case scope id: page-level-057. Page-level c...
  3. score=41.154101 chunk_id=21556 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? document page-driftwood-cove-family-note-05...
  4. score=7.154101 chunk_id=21712 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? document page-driftwood-cove-family-note-08...
- Matched markers: canal route map, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map, saffron scarf.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.121952 chunk_id=21555 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? Case scope id: page-level-057. Page-level c...
  2. score=41.123310 chunk_id=21556 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? document page-driftwood-cove-family-note-05...
  3. score=7.200636 chunk_id=21712 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? document page-driftwood-cove-family-note-08...
- Matched markers: canal route map, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: canal route map, saffron scarf.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 58 - page-level-058
Question: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery?

Expected evidence:
- wax thread
- brass compass
- Signal Lantern Morning

Expected distractors:
- silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.760263 chunk_id=21557 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  2. score=72.775632 chunk_id=21560 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  3. score=72.767507 chunk_id=21559 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  4. score=72.747159 chunk_id=21558 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  5. score=53.779773 chunk_id=21562 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery? document page-star-b...
- Matched markers: Signal Lantern Morning, brass compass, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, brass compass, wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.658923 chunk_id=21557 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  2. score=72.674858 chunk_id=21559 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  3. score=72.667032 chunk_id=21560 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  4. score=72.664378 chunk_id=21558 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  5. score=53.687168 chunk_id=21562 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery? document page-star-b...
- Matched markers: Signal Lantern Morning, brass compass, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, brass compass, wax thread.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 59 - page-level-059
Question: Which page-level notes from the family note show why Ilia's photo memory at Harbor Glass corridor mattered later?

Expected evidence:
- cedar shovel
- tuning fork
- silver booth token

Expected distractors:
- glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.637455 chunk_id=21566 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Harbor Glass corridor mattered later? Case scope id: page-level-...
  2. score=72.629285 chunk_id=21565 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Harbor Glass corridor mattered later? Case scope id: page-level-...
  3. score=53.630165 chunk_id=21568 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Harbor Glass corridor mattered later? document page-harbor-glass...
  4. score=2.431169 chunk_id=21464 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
  5. score=2.425881 chunk_id=21463 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
- Matched markers: cedar shovel, silver booth token, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, silver booth token, tuning fork.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.589971 chunk_id=21563 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Harbor Glass corridor mattered later? Case scope id: page-level-...
  2. score=72.678793 chunk_id=21564 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Harbor Glass corridor mattered later? Case scope id: page-level-...
  3. score=72.665745 chunk_id=21565 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Harbor Glass corridor mattered later? Case scope id: page-level-...
  4. score=72.633217 chunk_id=21566 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Harbor Glass corridor mattered later? Case scope id: page-level-...
  5. score=53.672979 chunk_id=21567 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Harbor Glass corridor mattered later? document page-harbor-glass...
- Matched markers: cedar shovel, silver booth token, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, silver booth token, tuning fork.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 2).

### Question 60 - page-level-060
Question: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed?

Expected evidence:
- linen wick
- silver booth token

Expected distractors:
- carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.662477 chunk_id=21569 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? Case scope id: page-leve...
  2. score=60.687184 chunk_id=21571 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? Case scope id: page-leve...
  3. score=60.682191 chunk_id=21570 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? Case scope id: page-leve...
  4. score=41.690425 chunk_id=21572 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? document page-bell-bridg...
  5. score=38.668989 chunk_id=21078 preview=document page-bell-bridge-square-audio-reel-060::page-level-060, page 11, section section-060: In document page-bell-bridge-square-audio-reel-060, page 11, s...
- Matched markers: linen wick, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: linen wick, silver booth token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.517497 chunk_id=21569 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? Case scope id: page-leve...
  2. score=60.595966 chunk_id=21570 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? Case scope id: page-leve...
  3. score=60.564233 chunk_id=21571 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? Case scope id: page-leve...
  4. score=41.576843 chunk_id=21572 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? document page-bell-bridg...
  5. score=2.509813 chunk_id=21728 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? document page-bell-bridge...
- Matched markers: linen wick, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: linen wick, silver booth token.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 61 - page-level-061
Question: Which details on the profile page identify how Elena and the aunt prepared for the winter coach from River Lantern inn?

Expected evidence:
- aunt
- rope bridge permit
- glass ink bottle

Expected distractors:
- tin key

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.446997 chunk_id=21573 preview=Question anchor: Which details on the profile page identify how Elena and the aunt prepared for the winter coach from River Lantern inn? Case scope id: page-...
  2. score=72.534847 chunk_id=21574 preview=Question anchor: Which details on the profile page identify how Elena and the aunt prepared for the winter coach from River Lantern inn? Case scope id: page-...
  3. score=72.453197 chunk_id=21576 preview=Question anchor: Which details on the profile page identify how Elena and the aunt prepared for the winter coach from River Lantern inn? Case scope id: page-...
  4. score=72.429644 chunk_id=21575 preview=Question anchor: Which details on the profile page identify how Elena and the aunt prepared for the winter coach from River Lantern inn? Case scope id: page-...
  5. score=53.541941 chunk_id=21577 preview=Question anchor: Which details on the profile page identify how Elena and the aunt prepared for the winter coach from River Lantern inn? document page-river-...
- Matched markers: aunt, glass ink bottle, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: aunt, glass ink bottle, rope bridge permit.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.291271 chunk_id=21573 preview=Question anchor: Which details on the profile page identify how Elena and the aunt prepared for the winter coach from River Lantern inn? Case scope id: page-...
  2. score=72.351086 chunk_id=21574 preview=Question anchor: Which details on the profile page identify how Elena and the aunt prepared for the winter coach from River Lantern inn? Case scope id: page-...
  3. score=72.305328 chunk_id=21575 preview=Question anchor: Which details on the profile page identify how Elena and the aunt prepared for the winter coach from River Lantern inn? Case scope id: page-...
  4. score=72.305204 chunk_id=21576 preview=Question anchor: Which details on the profile page identify how Elena and the aunt prepared for the winter coach from River Lantern inn? Case scope id: page-...
  5. score=53.358193 chunk_id=21577 preview=Question anchor: Which details on the profile page identify how Elena and the aunt prepared for the winter coach from River Lantern inn? document page-river-...
- Matched markers: aunt, glass ink bottle, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: aunt, glass ink bottle, rope bridge permit.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 62 - page-level-062
Question: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed?

Expected evidence:
- clay watering cup
- carved shell comb

Expected distractors:
- copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=7.571392 chunk_id=21738 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
  2. score=4.586583 chunk_id=21099 preview=document page-birch-ferry-shed-audio-reel-092::page-level-092, page 9, section section-092: In document page-birch-ferry-shed-audio-reel-092, page 9, section...
- Matched markers: none
- Missing markers: clay watering cup, carved shell comb
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.461120 chunk_id=21581 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? Case scope id: page-level-062. Page-level...
  2. score=60.406635 chunk_id=21580 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? Case scope id: page-level-062. Page-level...
  3. score=7.458731 chunk_id=21738 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
- Matched markers: carved shell comb, clay watering cup
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: carved shell comb, clay watering cup.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 63 - page-level-063
Question: Which profile-page details explain what Kira kept for the Canal Night after returning to Driftwood cove?

Expected evidence:
- copper wind vane pin
- tin key
- Canal Night

Expected distractors:
- star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.566505 chunk_id=21586 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Driftwood cove? Case scope id: page-level-063. Page...
  2. score=72.522705 chunk_id=21585 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Driftwood cove? Case scope id: page-level-063. Page...
  3. score=53.537045 chunk_id=21588 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-family...
  4. score=14.403202 chunk_id=21744 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
  5. score=14.383333 chunk_id=21743 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
- Matched markers: Canal Night, copper wind vane pin, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, copper wind vane pin, tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.383873 chunk_id=21585 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Driftwood cove? Case scope id: page-level-063. Page...
  2. score=72.355866 chunk_id=21586 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Driftwood cove? Case scope id: page-level-063. Page...
  3. score=53.390438 chunk_id=21588 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-family...
  4. score=53.320733 chunk_id=21587 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-family...
  5. score=14.179150 chunk_id=21744 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
- Matched markers: Canal Night, copper wind vane pin, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, copper wind vane pin, tin key.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 64 - page-level-064
Question: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later?

Expected evidence:
- amber lantern
- copper token
- star ledger page

Expected distractors:
- oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.672367 chunk_id=21589 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? Case scope id: page-level-064...
  2. score=72.707651 chunk_id=21591 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? Case scope id: page-level-064...
  3. score=72.707107 chunk_id=21590 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? Case scope id: page-level-064...
  4. score=72.676123 chunk_id=21592 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? Case scope id: page-level-064...
  5. score=53.722820 chunk_id=21593 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? document page-star-basin-gall...
- Matched markers: amber lantern, copper token, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, copper token, star ledger page.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.627056 chunk_id=21591 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? Case scope id: page-level-064...
  2. score=72.620338 chunk_id=21590 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? Case scope id: page-level-064...
  3. score=72.589634 chunk_id=21592 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? Case scope id: page-level-064...
  4. score=53.620793 chunk_id=21594 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? document page-star-basin-gall...
  5. score=53.613463 chunk_id=21593 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? document page-star-basin-gall...
- Matched markers: amber lantern, copper token, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, copper token, star ledger page.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 65 - page-level-065
Question: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed?

Expected evidence:
- blue oar
- star ledger page

Expected distractors:
- juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.548047 chunk_id=21596 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? Case scope id: p...
  2. score=60.524107 chunk_id=21597 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? Case scope id: p...
  3. score=41.560864 chunk_id=21598 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-ha...
  4. score=2.468673 chunk_id=21754 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-h...
- Matched markers: blue oar, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, star ledger page.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.604171 chunk_id=21596 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? Case scope id: p...
  2. score=41.607709 chunk_id=21598 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-ha...
  3. score=2.561887 chunk_id=21754 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-h...
- Matched markers: blue oar, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, star ledger page.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 66 - page-level-066
Question: Which details on the profile page identify how Anya and the grandfather prepared for the winter coach from Bell Bridge square?

Expected evidence:
- grandfather
- moonflower cutting
- oak barrel hoops

Expected distractors:
- coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.536263 chunk_id=21599 preview=Question anchor: Which details on the profile page identify how Anya and the grandfather prepared for the winter coach from Bell Bridge square? Case scope id...
  2. score=72.581697 chunk_id=21600 preview=Question anchor: Which details on the profile page identify how Anya and the grandfather prepared for the winter coach from Bell Bridge square? Case scope id...
  3. score=72.537058 chunk_id=21602 preview=Question anchor: Which details on the profile page identify how Anya and the grandfather prepared for the winter coach from Bell Bridge square? Case scope id...
  4. score=72.513186 chunk_id=21601 preview=Question anchor: Which details on the profile page identify how Anya and the grandfather prepared for the winter coach from Bell Bridge square? Case scope id...
  5. score=53.595918 chunk_id=21603 preview=Question anchor: Which details on the profile page identify how Anya and the grandfather prepared for the winter coach from Bell Bridge square? document page...
- Matched markers: grandfather, moonflower cutting, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: grandfather, moonflower cutting, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.310995 chunk_id=21600 preview=Question anchor: Which details on the profile page identify how Anya and the grandfather prepared for the winter coach from Bell Bridge square? Case scope id...
  2. score=72.291104 chunk_id=21601 preview=Question anchor: Which details on the profile page identify how Anya and the grandfather prepared for the winter coach from Bell Bridge square? Case scope id...
  3. score=72.265985 chunk_id=21602 preview=Question anchor: Which details on the profile page identify how Anya and the grandfather prepared for the winter coach from Bell Bridge square? Case scope id...
  4. score=53.319579 chunk_id=21603 preview=Question anchor: Which details on the profile page identify how Anya and the grandfather prepared for the winter coach from Bell Bridge square? document page...
  5. score=53.297878 chunk_id=21604 preview=Question anchor: Which details on the profile page identify how Anya and the grandfather prepared for the winter coach from Bell Bridge square? document page...
- Matched markers: grandfather, moonflower cutting, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: grandfather, moonflower cutting, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 67 - page-level-067
Question: Which longer-page details in the family note describe the family memory scene at River Lantern inn?

Expected evidence:
- lantern hook
- juniper bundles

Expected distractors:
- basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=7.342543 chunk_id=21296 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
  2. score=4.318946 chunk_id=21132 preview=document page-river-lantern-inn-family-note-007::page-level-007, page 9, section section-007: In document page-river-lantern-inn-family-note-007, page 9, sec...
  3. score=2.028064 chunk_id=21426 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
- Matched markers: none
- Missing markers: lantern hook, juniper bundles
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.280315 chunk_id=21605 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? Case scope id: page-level-067. Scoped an...
  2. score=60.291929 chunk_id=21606 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? Case scope id: page-level-067. Page-leve...
  3. score=60.291907 chunk_id=21607 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? Case scope id: page-level-067. Page-leve...
  4. score=41.298607 chunk_id=21608 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
  5. score=7.313074 chunk_id=21296 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
- Matched markers: juniper bundles, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: juniper bundles, lantern hook.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 68 - page-level-068
Question: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed?

Expected evidence:
- blue glass jar
- coal stove hiss
- Signal Lantern Morning

Expected distractors:
- willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.679521 chunk_id=21609 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? Case scope id: page-le...
  2. score=72.750583 chunk_id=21612 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? Case scope id: page-le...
  3. score=72.722315 chunk_id=21610 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? Case scope id: page-le...
  4. score=72.682740 chunk_id=21611 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? Case scope id: page-le...
  5. score=53.736883 chunk_id=21613 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
- Matched markers: Signal Lantern Morning, blue glass jar, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, blue glass jar, coal stove hiss.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.632419 chunk_id=21612 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? Case scope id: page-le...
  2. score=53.638180 chunk_id=21614 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  3. score=53.636516 chunk_id=21613 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  4. score=19.626219 chunk_id=21302 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  5. score=14.615650 chunk_id=21770 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
- Matched markers: Signal Lantern Morning, blue glass jar, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, blue glass jar, coal stove hiss.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 69 - page-level-069
Question: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later?

Expected evidence:
- smoke vent chain
- basalt sketch
- willow basket

Expected distractors:
- birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.606552 chunk_id=21617 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later? Case scope id: page-level-069....
  2. score=72.594738 chunk_id=21618 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later? Case scope id: page-level-069....
  3. score=53.615705 chunk_id=21620 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fa...
- Matched markers: basalt sketch, smoke vent chain, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, smoke vent chain, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.564675 chunk_id=21616 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later? Case scope id: page-level-069....
  2. score=72.553848 chunk_id=21617 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later? Case scope id: page-level-069....
  3. score=72.542881 chunk_id=21618 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later? Case scope id: page-level-069....
  4. score=53.555526 chunk_id=21619 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fa...
  5. score=53.543673 chunk_id=21620 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fa...
- Matched markers: basalt sketch, smoke vent chain, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, smoke vent chain, willow basket.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 70 - page-level-070
Question: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed?

Expected evidence:
- violet ribbon
- willow basket

Expected distractors:
- weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.639448 chunk_id=21621 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-level...
  2. score=60.643947 chunk_id=21623 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-level...
  3. score=41.653897 chunk_id=21624 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin-...
  4. score=7.679487 chunk_id=21312 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin-...
  5. score=4.651976 chunk_id=21148 preview=document page-star-basin-gallery-audio-reel-010::page-level-010, page 12, section section-010: In document page-star-basin-gallery-audio-reel-010, page 12, s...
- Matched markers: violet ribbon, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: violet ribbon, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.573997 chunk_id=21622 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-level...
  2. score=41.567742 chunk_id=21624 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin-...
  3. score=7.657088 chunk_id=21312 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin-...
  4. score=2.599616 chunk_id=21780 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin...
- Matched markers: violet ribbon, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: violet ribbon, willow basket.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 71 - page-level-071
Question: Which details on the profile page identify how Raisa and the grandmother prepared for the winter coach from Harbor Glass corridor?

Expected evidence:
- grandmother
- green apron
- birch tea flask

Expected distractors:
- canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.407782 chunk_id=21625 preview=Question anchor: Which details on the profile page identify how Raisa and the grandmother prepared for the winter coach from Harbor Glass corridor? Case scop...
  2. score=72.491186 chunk_id=21626 preview=Question anchor: Which details on the profile page identify how Raisa and the grandmother prepared for the winter coach from Harbor Glass corridor? Case scop...
  3. score=72.451018 chunk_id=21627 preview=Question anchor: Which details on the profile page identify how Raisa and the grandmother prepared for the winter coach from Harbor Glass corridor? Case scop...
  4. score=72.447275 chunk_id=21628 preview=Question anchor: Which details on the profile page identify how Raisa and the grandmother prepared for the winter coach from Harbor Glass corridor? Case scop...
  5. score=53.503150 chunk_id=21629 preview=Question anchor: Which details on the profile page identify how Raisa and the grandmother prepared for the winter coach from Harbor Glass corridor? document...
- Matched markers: birch tea flask, grandmother, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, grandmother, green apron.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.350904 chunk_id=21626 preview=Question anchor: Which details on the profile page identify how Raisa and the grandmother prepared for the winter coach from Harbor Glass corridor? Case scop...
  2. score=72.350024 chunk_id=21627 preview=Question anchor: Which details on the profile page identify how Raisa and the grandmother prepared for the winter coach from Harbor Glass corridor? Case scop...
  3. score=53.360466 chunk_id=21629 preview=Question anchor: Which details on the profile page identify how Raisa and the grandmother prepared for the winter coach from Harbor Glass corridor? document...
  4. score=53.355855 chunk_id=21630 preview=Question anchor: Which details on the profile page identify how Raisa and the grandmother prepared for the winter coach from Harbor Glass corridor? document...
  5. score=2.242605 chunk_id=21318 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from Harbor Glass corridor? docum...
- Matched markers: birch tea flask, grandmother, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, grandmother, green apron.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 72 - page-level-072
Question: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square?

Expected evidence:
- paper moon mask
- weathered camera strap

Expected distractors:
- brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.462656 chunk_id=21633 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? Case scope id: page-level-072. Page-leve...
  2. score=7.482184 chunk_id=21322 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? document page-bell-bridge-square-audio-r...
  3. score=4.458488 chunk_id=21070 preview=document page-bell-bridge-square-audio-reel-012::page-level-012, page 14, section section-012: In document page-bell-bridge-square-audio-reel-012, page 14, s...
  4. score=2.006532 chunk_id=21426 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
- Matched markers: paper moon mask, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: paper moon mask, weathered camera strap.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.355928 chunk_id=21633 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? Case scope id: page-level-072. Page-leve...
  2. score=60.352708 chunk_id=21632 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? Case scope id: page-level-072. Page-leve...
  3. score=7.376755 chunk_id=21322 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Bell Bridge square? document page-bell-bridge-square-audio-r...
- Matched markers: paper moon mask, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: paper moon mask, weathered camera strap.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 3).

### Question 73 - page-level-073
Question: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn?

Expected evidence:
- saffron scarf
- canal route map
- Canal Night

Expected distractors:
- tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=19.668106 chunk_id=21328 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn? document page-river-lantern-inn...
  2. score=14.282034 chunk_id=21691 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
  3. score=7.718498 chunk_id=21326 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn? Case scope id: page-level-013....
  4. score=2.264217 chunk_id=21690 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-08...
  5. score=2.263763 chunk_id=21688 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-08...
- Matched markers: Canal Night
- Missing markers: saffron scarf, canal route map
- Distractors: none
- Evidence coverage: 0.3333333333333333
- First relevant rank: 1
- Answer summary: Partially grounded by: Canal Night. Missing: saffron scarf, canal route map.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.510309 chunk_id=21637 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn? Case scope id: page-level-073....
  2. score=53.523964 chunk_id=21640 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn? document page-river-lantern-inn...
  3. score=19.509277 chunk_id=21328 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn? document page-river-lantern-inn...
  4. score=7.508501 chunk_id=21325 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn? Case scope id: page-level-013....
  5. score=7.504649 chunk_id=21326 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to River Lantern inn? Case scope id: page-level-013....
- Matched markers: Canal Night, canal route map, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, canal route map, saffron scarf.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.33).

### Question 74 - page-level-074
Question: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later?

Expected evidence:
- wax thread
- brass compass
- tuning fork

Expected distractors:
- silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=2.511235 chunk_id=21438 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? document page-star-basin-galle...
  2. score=2.463992 chunk_id=21437 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? document page-star-basin-galle...
  3. score=2.317424 chunk_id=21594 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? document page-star-basin-gall...
  4. score=2.314456 chunk_id=21593 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Star Basin gallery mattered later? document page-star-basin-gall...
  5. score=2.158486 chunk_id=21464 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
- Matched markers: none
- Missing markers: wax thread, brass compass, tuning fork
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.556054 chunk_id=21641 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later? Case scope id: page-level-074. S...
  2. score=72.626655 chunk_id=21642 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later? Case scope id: page-level-074. P...
  3. score=72.601457 chunk_id=21643 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later? Case scope id: page-level-074. P...
  4. score=72.600910 chunk_id=21644 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later? Case scope id: page-level-074. P...
  5. score=53.615257 chunk_id=21645 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Birch Ferry shed mattered later? document page-birch-ferry-shed-a...
- Matched markers: brass compass, tuning fork, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass compass, tuning fork, wax thread.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 75 - page-level-075
Question: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed?

Expected evidence:
- cedar shovel
- tuning fork

Expected distractors:
- glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=2.597175 chunk_id=21442 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-h...
  2. score=2.541444 chunk_id=21121 preview=document page-harbor-glass-corridor-family-note-035::page-level-035, page 3, section section-035: In document page-harbor-glass-corridor-family-note-035, pag...
- Matched markers: none
- Missing markers: cedar shovel, tuning fork
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.599709 chunk_id=21647 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? Case scope id: page-le...
  2. score=60.658727 chunk_id=21648 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? Case scope id: page-le...
  3. score=60.626237 chunk_id=21649 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? Case scope id: page-le...
  4. score=41.647464 chunk_id=21650 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? document page-driftwoo...
  5. score=7.560619 chunk_id=21338 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Driftwood cove was delayed? document page-driftwoo...
- Matched markers: cedar shovel, tuning fork
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, tuning fork.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 76 - page-level-076
Question: Which details on the profile page identify how Iveta and the cousin prepared for the winter coach from Star Basin gallery?

Expected evidence:
- cousin
- linen wick
- silver booth token

Expected distractors:
- carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.453684 chunk_id=21651 preview=Question anchor: Which details on the profile page identify how Iveta and the cousin prepared for the winter coach from Star Basin gallery? Case scope id: pa...
  2. score=72.492847 chunk_id=21652 preview=Question anchor: Which details on the profile page identify how Iveta and the cousin prepared for the winter coach from Star Basin gallery? Case scope id: pa...
  3. score=72.452438 chunk_id=21654 preview=Question anchor: Which details on the profile page identify how Iveta and the cousin prepared for the winter coach from Star Basin gallery? Case scope id: pa...
  4. score=72.423795 chunk_id=21653 preview=Question anchor: Which details on the profile page identify how Iveta and the cousin prepared for the winter coach from Star Basin gallery? Case scope id: pa...
  5. score=53.508572 chunk_id=21655 preview=Question anchor: Which details on the profile page identify how Iveta and the cousin prepared for the winter coach from Star Basin gallery? document page-sta...
- Matched markers: cousin, linen wick, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cousin, linen wick, silver booth token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.339918 chunk_id=21651 preview=Question anchor: Which details on the profile page identify how Iveta and the cousin prepared for the winter coach from Star Basin gallery? Case scope id: pa...
  2. score=72.408171 chunk_id=21652 preview=Question anchor: Which details on the profile page identify how Iveta and the cousin prepared for the winter coach from Star Basin gallery? Case scope id: pa...
  3. score=72.378865 chunk_id=21653 preview=Question anchor: Which details on the profile page identify how Iveta and the cousin prepared for the winter coach from Star Basin gallery? Case scope id: pa...
  4. score=72.354480 chunk_id=21654 preview=Question anchor: Which details on the profile page identify how Iveta and the cousin prepared for the winter coach from Star Basin gallery? Case scope id: pa...
  5. score=53.417256 chunk_id=21655 preview=Question anchor: Which details on the profile page identify how Iveta and the cousin prepared for the winter coach from Star Basin gallery? document page-sta...
- Matched markers: cousin, linen wick, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cousin, linen wick, silver booth token.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 77 - page-level-077
Question: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor?

Expected evidence:
- rope bridge permit
- glass ink bottle

Expected distractors:
- tin key

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.368185 chunk_id=21659 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? Case scope id: page-level-077. Page-...
  2. score=60.328302 chunk_id=21658 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? Case scope id: page-level-077. Page-...
  3. score=41.324019 chunk_id=21660 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? document page-harbor-glass-corridor-...
  4. score=38.328571 chunk_id=21128 preview=document page-harbor-glass-corridor-family-note-077::page-level-077, page 11, section section-077: In document page-harbor-glass-corridor-family-note-077, pa...
  5. score=7.357107 chunk_id=21348 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? document page-harbor-glass-corridor-...
- Matched markers: glass ink bottle, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, rope bridge permit.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.301906 chunk_id=21659 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? Case scope id: page-level-077. Page-...
  2. score=60.292177 chunk_id=21658 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? Case scope id: page-level-077. Page-...
  3. score=7.340623 chunk_id=21348 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? document page-harbor-glass-corridor-...
- Matched markers: glass ink bottle, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: glass ink bottle, rope bridge permit.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 78 - page-level-078
Question: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square?

Expected evidence:
- clay watering cup
- carved shell comb
- Signal Lantern Morning

Expected distractors:
- copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=19.737045 chunk_id=21354 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? document page-bell-b...
  2. score=19.719263 chunk_id=21353 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? document page-bell-b...
  3. score=7.722764 chunk_id=21352 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  4. score=6.775000 chunk_id=21509 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square? document page-bell-b...
  5. score=6.723841 chunk_id=21510 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Bell Bridge square? document page-bell-b...
- Matched markers: Signal Lantern Morning
- Missing markers: clay watering cup, carved shell comb
- Distractors: copper token
- Evidence coverage: 0.3333333333333333
- First relevant rank: 1
- Answer summary: Partially grounded by: Signal Lantern Morning. Missing: clay watering cup, carved shell comb. Distractors present: copper token.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=19.643203 chunk_id=21354 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? document page-bell-b...
  2. score=19.628971 chunk_id=21353 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? document page-bell-b...
  3. score=7.632772 chunk_id=21352 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  4. score=7.630894 chunk_id=21351 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
  5. score=7.614879 chunk_id=21350 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Bell Bridge square? Case scope id: page-...
- Matched markers: Signal Lantern Morning
- Missing markers: clay watering cup, carved shell comb
- Distractors: none
- Evidence coverage: 0.3333333333333333
- First relevant rank: 1
- Answer summary: Partially grounded by: Signal Lantern Morning. Missing: clay watering cup, carved shell comb.
- Verdict: partial

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 79 - page-level-079
Question: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later?

Expected evidence:
- copper wind vane pin
- tin key
- copper token

Expected distractors:
- star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.599694 chunk_id=21669 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later? Case scope id: page-level-079....
  2. score=2.505668 chunk_id=21464 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
  3. score=2.499756 chunk_id=21463 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
  4. score=2.483265 chunk_id=21106 preview=document page-driftwood-cove-family-note-039::page-level-039, page 7, section section-039: In document page-driftwood-cove-family-note-039, page 7, section s...
- Matched markers: copper token, copper wind vane pin, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: copper token, copper wind vane pin, tin key.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.616259 chunk_id=21669 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later? Case scope id: page-level-079....
  2. score=72.602469 chunk_id=21670 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later? Case scope id: page-level-079....
  3. score=72.591978 chunk_id=21668 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later? Case scope id: page-level-079....
  4. score=53.603545 chunk_id=21672 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later? document page-river-lantern-in...
  5. score=53.577125 chunk_id=21671 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at River Lantern inn mattered later? document page-river-lantern-in...
- Matched markers: copper token, copper wind vane pin, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper token, copper wind vane pin, tin key.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 3).

### Question 80 - page-level-080
Question: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed?

Expected evidence:
- amber lantern
- copper token

Expected distractors:
- oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.630203 chunk_id=21674 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? Case scope id: page-level-...
  2. score=41.645833 chunk_id=21676 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? document page-birch-ferry-...
  3. score=7.667942 chunk_id=21364 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? document page-birch-ferry-...
  4. score=4.633054 chunk_id=21087 preview=document page-birch-ferry-shed-audio-reel-020::page-level-020, page 5, section section-020: In document page-birch-ferry-shed-audio-reel-020, page 5, section...
  5. score=2.445833 chunk_id=21780 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin...
- Matched markers: amber lantern, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, copper token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.590908 chunk_id=21673 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? Case scope id: page-level-...
  2. score=60.646110 chunk_id=21674 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? Case scope id: page-level-...
  3. score=60.631329 chunk_id=21675 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? Case scope id: page-level-...
  4. score=41.639208 chunk_id=21676 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Birch Ferry shed was delayed? document page-birch-ferry-...
  5. score=38.544995 chunk_id=21097 preview=document page-birch-ferry-shed-audio-reel-080::page-level-080, page 14, section section-080: In document page-birch-ferry-shed-audio-reel-080, page 14, secti...
- Matched markers: amber lantern, copper token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, copper token.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 3).

### Question 81 - page-level-081
Question: Which details on the profile page identify how Elena and the uncle prepared for the winter coach from Driftwood cove?

Expected evidence:
- uncle
- blue oar
- star ledger page

Expected distractors:
- juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.262622 chunk_id=21677 preview=Question anchor: Which details on the profile page identify how Elena and the uncle prepared for the winter coach from Driftwood cove? Case scope id: page-le...
  2. score=72.320225 chunk_id=21678 preview=Question anchor: Which details on the profile page identify how Elena and the uncle prepared for the winter coach from Driftwood cove? Case scope id: page-le...
  3. score=72.259640 chunk_id=21679 preview=Question anchor: Which details on the profile page identify how Elena and the uncle prepared for the winter coach from Driftwood cove? Case scope id: page-le...
  4. score=72.235057 chunk_id=21680 preview=Question anchor: Which details on the profile page identify how Elena and the uncle prepared for the winter coach from Driftwood cove? Case scope id: page-le...
  5. score=53.337406 chunk_id=21681 preview=Question anchor: Which details on the profile page identify how Elena and the uncle prepared for the winter coach from Driftwood cove? document page-driftwoo...
- Matched markers: blue oar, star ledger page, uncle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, star ledger page, uncle.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.128053 chunk_id=21677 preview=Question anchor: Which details on the profile page identify how Elena and the uncle prepared for the winter coach from Driftwood cove? Case scope id: page-le...
  2. score=72.188778 chunk_id=21678 preview=Question anchor: Which details on the profile page identify how Elena and the uncle prepared for the winter coach from Driftwood cove? Case scope id: page-le...
  3. score=72.157584 chunk_id=21679 preview=Question anchor: Which details on the profile page identify how Elena and the uncle prepared for the winter coach from Driftwood cove? Case scope id: page-le...
  4. score=72.125934 chunk_id=21680 preview=Question anchor: Which details on the profile page identify how Elena and the uncle prepared for the winter coach from Driftwood cove? Case scope id: page-le...
  5. score=53.201039 chunk_id=21681 preview=Question anchor: Which details on the profile page identify how Elena and the uncle prepared for the winter coach from Driftwood cove? document page-driftwoo...
- Matched markers: blue oar, star ledger page, uncle
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, star ledger page, uncle.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 82 - page-level-082
Question: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery?

Expected evidence:
- moonflower cutting
- oak barrel hoops

Expected distractors:
- coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.538465 chunk_id=21685 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? Case scope id: page-level-082. Page-leve...
  2. score=2.093168 chunk_id=21426 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
- Matched markers: moonflower cutting, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: moonflower cutting, oak barrel hoops.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.483913 chunk_id=21683 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? Case scope id: page-level-082. Scoped an...
  2. score=60.511683 chunk_id=21685 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? Case scope id: page-level-082. Page-leve...
  3. score=60.506105 chunk_id=21684 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? Case scope id: page-level-082. Page-leve...
  4. score=41.502558 chunk_id=21686 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Star Basin gallery? document page-star-basin-gallery-audio-r...
  5. score=38.452462 chunk_id=21160 preview=document page-star-basin-gallery-audio-reel-082::page-level-082, page 16, section section-082: In document page-star-basin-gallery-audio-reel-082, page 16, s...
- Matched markers: moonflower cutting, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: moonflower cutting, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 1).

### Question 83 - page-level-083
Question: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor?

Expected evidence:
- lantern hook
- juniper bundles
- Canal Night

Expected distractors:
- basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.740642 chunk_id=21687 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-08...
  2. score=72.779515 chunk_id=21688 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-08...
  3. score=72.774958 chunk_id=21690 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-08...
  4. score=72.727818 chunk_id=21689 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-08...
  5. score=53.804911 chunk_id=21691 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
- Matched markers: Canal Night, juniper bundles, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, juniper bundles, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.552160 chunk_id=21689 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-08...
  2. score=72.520989 chunk_id=21690 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? Case scope id: page-level-08...
  3. score=53.567385 chunk_id=21692 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
  4. score=53.524890 chunk_id=21691 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
  5. score=19.529843 chunk_id=21379 preview=Question anchor: Which profile-page details explain what Kira kept for the Canal Night after returning to Harbor Glass corridor? document page-harbor-glass-c...
- Matched markers: Canal Night, juniper bundles, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, juniper bundles, lantern hook.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 84 - page-level-084
Question: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later?

Expected evidence:
- blue glass jar
- coal stove hiss
- basalt sketch

Expected distractors:
- willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=53.605063 chunk_id=21698 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? document page-bell-bridge-squ...
  2. score=53.600665 chunk_id=21697 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? document page-bell-bridge-squ...
  3. score=7.657925 chunk_id=21386 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? document page-bell-bridge-squ...
  4. score=7.615240 chunk_id=21385 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? document page-bell-bridge-squ...
  5. score=2.424260 chunk_id=21490 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Birch Ferry shed mattered later? document page-birch-ferry-shed-...
- Matched markers: basalt sketch, blue glass jar, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: basalt sketch, blue glass jar, coal stove hiss.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.576324 chunk_id=21694 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? Case scope id: page-level-084...
  2. score=72.572982 chunk_id=21695 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? Case scope id: page-level-084...
  3. score=72.552736 chunk_id=21696 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? Case scope id: page-level-084...
  4. score=53.558015 chunk_id=21697 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? document page-bell-bridge-squ...
  5. score=53.554826 chunk_id=21698 preview=Question anchor: Which page-level notes from the audio reel show why Nadia's photo memory at Bell Bridge square mattered later? document page-bell-bridge-squ...
- Matched markers: basalt sketch, blue glass jar, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, blue glass jar, coal stove hiss.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 3).

### Question 85 - page-level-085
Question: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed?

Expected evidence:
- smoke vent chain
- basalt sketch

Expected distractors:
- birch tea flask

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=2.658944 chunk_id=21442 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-h...
  2. score=2.597895 chunk_id=21121 preview=document page-harbor-glass-corridor-family-note-035::page-level-035, page 3, section section-035: In document page-harbor-glass-corridor-family-note-035, pag...
  3. score=2.525224 chunk_id=21598 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-ha...
- Matched markers: none
- Missing markers: smoke vent chain, basalt sketch
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.551448 chunk_id=21699 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? Case scope id: page-...
  2. score=60.623133 chunk_id=21700 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? Case scope id: page-...
  3. score=60.588338 chunk_id=21701 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? Case scope id: page-...
  4. score=41.607602 chunk_id=21702 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? document page-river-...
  5. score=7.581307 chunk_id=21390 preview=Question anchor: Which page-level details on Lina's family note explain why the Glass Harbor Day visit to River Lantern inn was delayed? document page-river-...
- Matched markers: basalt sketch, smoke vent chain
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: basalt sketch, smoke vent chain.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 86 - page-level-086
Question: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Birch Ferry shed?

Expected evidence:
- godmother
- violet ribbon
- willow basket

Expected distractors:
- weathered camera strap

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.486626 chunk_id=21703 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Birch Ferry shed? Case scope id: pa...
  2. score=72.539600 chunk_id=21704 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Birch Ferry shed? Case scope id: pa...
  3. score=72.503094 chunk_id=21706 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Birch Ferry shed? Case scope id: pa...
  4. score=72.476252 chunk_id=21705 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Birch Ferry shed? Case scope id: pa...
  5. score=53.556650 chunk_id=21707 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Birch Ferry shed? document page-bir...
- Matched markers: godmother, violet ribbon, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: godmother, violet ribbon, willow basket.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.349356 chunk_id=21703 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Birch Ferry shed? Case scope id: pa...
  2. score=72.427681 chunk_id=21704 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Birch Ferry shed? Case scope id: pa...
  3. score=72.395735 chunk_id=21705 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Birch Ferry shed? Case scope id: pa...
  4. score=72.364545 chunk_id=21706 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Birch Ferry shed? Case scope id: pa...
  5. score=53.437615 chunk_id=21707 preview=Question anchor: Which details on the profile page identify how Anya and the godmother prepared for the winter coach from Birch Ferry shed? document page-bir...
- Matched markers: godmother, violet ribbon, willow basket
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: godmother, violet ribbon, willow basket.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 87 - page-level-087
Question: Which longer-page details in the family note describe the family memory scene at Driftwood cove?

Expected evidence:
- green apron
- birch tea flask

Expected distractors:
- canal route map

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.156330 chunk_id=21711 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? Case scope id: page-level-087. Page-level c...
  2. score=60.147150 chunk_id=21710 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? Case scope id: page-level-087. Page-level c...
  3. score=41.154101 chunk_id=21712 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? document page-driftwood-cove-family-note-08...
  4. score=7.159975 chunk_id=21400 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? document page-driftwood-cove-family-note-02...
  5. score=4.152463 chunk_id=21104 preview=document page-driftwood-cove-family-note-027::page-level-027, page 12, section section-027: In document page-driftwood-cove-family-note-027, page 12, section...
- Matched markers: birch tea flask, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, green apron.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.137037 chunk_id=21709 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? Case scope id: page-level-087. Scoped answe...
  2. score=60.202843 chunk_id=21710 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? Case scope id: page-level-087. Page-level c...
  3. score=60.145576 chunk_id=21711 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? Case scope id: page-level-087. Page-level c...
  4. score=41.200636 chunk_id=21712 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? document page-driftwood-cove-family-note-08...
  5. score=7.171819 chunk_id=21400 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Driftwood cove? document page-driftwood-cove-family-note-02...
- Matched markers: birch tea flask, green apron
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: birch tea flask, green apron.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (1 vs 2).

### Question 88 - page-level-088
Question: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery?

Expected evidence:
- paper moon mask
- weathered camera strap
- Signal Lantern Morning

Expected distractors:
- brass compass

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=19.747310 chunk_id=21406 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? document page-star-b...
  2. score=19.721746 chunk_id=21405 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? document page-star-b...
  3. score=7.720378 chunk_id=21404 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  4. score=7.717870 chunk_id=21403 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  5. score=6.671930 chunk_id=21562 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery? document page-star-b...
- Matched markers: Signal Lantern Morning
- Missing markers: paper moon mask, weathered camera strap
- Distractors: brass compass
- Evidence coverage: 0.3333333333333333
- First relevant rank: 1
- Answer summary: Partially grounded by: Signal Lantern Morning. Missing: paper moon mask, weathered camera strap. Distractors present: brass compass.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.667141 chunk_id=21716 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  2. score=72.658970 chunk_id=21715 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  3. score=72.629603 chunk_id=21714 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? Case scope id: page-...
  4. score=53.668383 chunk_id=21718 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? document page-star-b...
  5. score=53.646039 chunk_id=21717 preview=Question anchor: Which profile-page details explain what Yara kept for the Signal Lantern Morning after returning to Star Basin gallery? document page-star-b...
- Matched markers: Signal Lantern Morning, paper moon mask, weathered camera strap
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, paper moon mask, weathered camera strap.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.33).

### Question 89 - page-level-089
Question: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later?

Expected evidence:
- saffron scarf
- canal route map
- brass compass

Expected distractors:
- tuning fork

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.591744 chunk_id=21721 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later? Case scope id: page-leve...
  2. score=7.641532 chunk_id=21412 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later? document page-harbor-gla...
  3. score=7.593819 chunk_id=21411 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later? document page-harbor-gla...
  4. score=2.245102 chunk_id=21464 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
- Matched markers: brass compass, canal route map, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: brass compass, canal route map, saffron scarf.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.612131 chunk_id=21721 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later? Case scope id: page-leve...
  2. score=72.591189 chunk_id=21720 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later? Case scope id: page-leve...
  3. score=53.606031 chunk_id=21724 preview=Question anchor: Which page-level notes from the family note show why Milena's photo memory at Harbor Glass corridor mattered later? document page-harbor-gla...
- Matched markers: brass compass, canal route map, saffron scarf
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass compass, canal route map, saffron scarf.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 3).

### Question 90 - page-level-090
Question: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed?

Expected evidence:
- wax thread
- brass compass

Expected distractors:
- silver booth token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.662923 chunk_id=21726 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? Case scope id: page-level...
  2. score=41.660622 chunk_id=21728 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? document page-bell-bridge...
  3. score=38.633054 chunk_id=21083 preview=document page-bell-bridge-square-audio-reel-090::page-level-090, page 7, section section-090: In document page-bell-bridge-square-audio-reel-090, page 7, sec...
  4. score=7.626550 chunk_id=21416 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? document page-bell-bridge...
- Matched markers: brass compass, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass compass, wax thread.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.491094 chunk_id=21725 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? Case scope id: page-level...
  2. score=60.559106 chunk_id=21726 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? Case scope id: page-level...
  3. score=60.521561 chunk_id=21727 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? Case scope id: page-level...
  4. score=41.552297 chunk_id=21728 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? document page-bell-bridge...
  5. score=7.513597 chunk_id=21416 preview=Question anchor: Which page-level details on Ada's audio reel explain why the Lantern Tide visit to Bell Bridge square was delayed? document page-bell-bridge...
- Matched markers: brass compass, wax thread
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: brass compass, wax thread.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 91 - page-level-091
Question: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from River Lantern inn?

Expected evidence:
- younger brother
- cedar shovel
- tuning fork

Expected distractors:
- glass ink bottle

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.538348 chunk_id=21729 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from River Lantern inn? Case scop...
  2. score=72.646545 chunk_id=21730 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from River Lantern inn? Case scop...
  3. score=72.558121 chunk_id=21732 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from River Lantern inn? Case scop...
  4. score=72.557547 chunk_id=21731 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from River Lantern inn? Case scop...
  5. score=53.648909 chunk_id=21733 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from River Lantern inn? document...
- Matched markers: cedar shovel, tuning fork, younger brother
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, tuning fork, younger brother.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.508213 chunk_id=21729 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from River Lantern inn? Case scop...
  2. score=72.541137 chunk_id=21730 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from River Lantern inn? Case scop...
  3. score=72.523691 chunk_id=21731 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from River Lantern inn? Case scop...
  4. score=72.502752 chunk_id=21732 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from River Lantern inn? Case scop...
  5. score=53.554937 chunk_id=21733 preview=Question anchor: Which details on the profile page identify how Raisa and the younger brother prepared for the winter coach from River Lantern inn? document...
- Matched markers: cedar shovel, tuning fork, younger brother
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: cedar shovel, tuning fork, younger brother.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 92 - page-level-092
Question: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed?

Expected evidence:
- linen wick
- silver booth token

Expected distractors:
- carved shell comb

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.573927 chunk_id=21735 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? Case scope id: page-level-092. Scoped answ...
  2. score=60.611176 chunk_id=21737 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? Case scope id: page-level-092. Page-level...
  3. score=60.560078 chunk_id=21736 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? Case scope id: page-level-092. Page-level...
  4. score=41.571393 chunk_id=21738 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
  5. score=38.586583 chunk_id=21099 preview=document page-birch-ferry-shed-audio-reel-092::page-level-092, page 9, section section-092: In document page-birch-ferry-shed-audio-reel-092, page 9, section...
- Matched markers: linen wick, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: linen wick, silver booth token.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.422431 chunk_id=21735 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? Case scope id: page-level-092. Scoped answ...
  2. score=60.464341 chunk_id=21736 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? Case scope id: page-level-092. Page-level...
  3. score=60.445239 chunk_id=21737 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? Case scope id: page-level-092. Page-level...
  4. score=41.458731 chunk_id=21738 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
  5. score=7.430943 chunk_id=21426 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
- Matched markers: linen wick, silver booth token
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: linen wick, silver booth token.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 93 - page-level-093
Question: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove?

Expected evidence:
- rope bridge permit
- glass ink bottle
- Canal Night

Expected distractors:
- tin key

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.581647 chunk_id=21742 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? Case scope id: page-level-093. Pag...
  2. score=72.536982 chunk_id=21741 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? Case scope id: page-level-093. Pag...
  3. score=53.553202 chunk_id=21744 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
  4. score=53.533333 chunk_id=21743 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
  5. score=19.558426 chunk_id=21431 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
- Matched markers: Canal Night, glass ink bottle, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, glass ink bottle, rope bridge permit.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.322819 chunk_id=21741 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? Case scope id: page-level-093. Pag...
  2. score=53.329150 chunk_id=21744 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
  3. score=19.335716 chunk_id=21432 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
  4. score=19.324132 chunk_id=21431 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? document page-driftwood-cove-famil...
  5. score=7.321862 chunk_id=21429 preview=Question anchor: Which profile-page details explain what Talia kept for the Canal Night after returning to Driftwood cove? Case scope id: page-level-033. Pag...
- Matched markers: Canal Night, glass ink bottle, rope bridge permit
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Canal Night, glass ink bottle, rope bridge permit.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 94 - page-level-094
Question: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later?

Expected evidence:
- clay watering cup
- carved shell comb
- tin key

Expected distractors:
- copper token

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=7.749930 chunk_id=21438 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? document page-star-basin-galle...
  2. score=7.705139 chunk_id=21437 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? document page-star-basin-galle...
  3. score=4.695235 chunk_id=21152 preview=document page-star-basin-gallery-audio-reel-034::page-level-034, page 2, section section-034: In document page-star-basin-gallery-audio-reel-034, page 2, sec...
- Matched markers: none
- Missing markers: clay watering cup, carved shell comb, tin key
- Distractors: none
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.589288 chunk_id=21747 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? Case scope id: page-level-094....
  2. score=72.577556 chunk_id=21748 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? Case scope id: page-level-094....
  3. score=53.578261 chunk_id=21750 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? document page-star-basin-galle...
  4. score=7.572928 chunk_id=21437 preview=Question anchor: Which page-level notes from the audio reel show why Runa's photo memory at Star Basin gallery mattered later? document page-star-basin-galle...
- Matched markers: carved shell comb, clay watering cup, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: carved shell comb, clay watering cup, tin key.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.00).

### Question 95 - page-level-095
Question: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed?

Expected evidence:
- copper wind vane pin
- tin key

Expected distractors:
- star ledger page

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.544589 chunk_id=21753 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? Case scope id:...
  2. score=41.518673 chunk_id=21754 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-h...
  3. score=7.711365 chunk_id=21442 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-h...
  4. score=4.646997 chunk_id=21121 preview=document page-harbor-glass-corridor-family-note-035::page-level-035, page 3, section section-035: In document page-harbor-glass-corridor-family-note-035, pag...
- Matched markers: copper wind vane pin, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper wind vane pin, tin key.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.606311 chunk_id=21751 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? Case scope id:...
  2. score=60.658768 chunk_id=21753 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? Case scope id:...
  3. score=60.654108 chunk_id=21752 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? Case scope id:...
  4. score=41.648600 chunk_id=21754 preview=Question anchor: Which page-level details on Selma's family note explain why the Glass Harbor Day visit to Harbor Glass corridor was delayed? document page-h...
  5. score=38.580973 chunk_id=21131 preview=document page-harbor-glass-corridor-family-note-095::page-level-095, page 12, section section-095: In document page-harbor-glass-corridor-family-note-095, pa...
- Matched markers: copper wind vane pin, tin key
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: copper wind vane pin, tin key.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 2).

### Question 96 - page-level-096
Question: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Bell Bridge square?

Expected evidence:
- older sister
- amber lantern
- copper token

Expected distractors:
- oak barrel hoops

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.557790 chunk_id=21755 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Bell Bridge square? Case scope...
  2. score=72.593614 chunk_id=21756 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Bell Bridge square? Case scope...
  3. score=72.566236 chunk_id=21757 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Bell Bridge square? Case scope...
  4. score=72.542009 chunk_id=21758 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Bell Bridge square? Case scope...
  5. score=53.611300 chunk_id=21759 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Bell Bridge square? document pa...
- Matched markers: amber lantern, copper token, older sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, copper token, older sister.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.473094 chunk_id=21755 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Bell Bridge square? Case scope...
  2. score=72.518743 chunk_id=21756 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Bell Bridge square? Case scope...
  3. score=72.492277 chunk_id=21757 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Bell Bridge square? Case scope...
  4. score=72.477363 chunk_id=21758 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Bell Bridge square? Case scope...
  5. score=53.527183 chunk_id=21759 preview=Question anchor: Which details on the profile page identify how Iveta and the older sister prepared for the winter coach from Bell Bridge square? document pa...
- Matched markers: amber lantern, copper token, older sister
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: amber lantern, copper token, older sister.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 97 - page-level-097
Question: Which longer-page details in the family note describe the family memory scene at River Lantern inn?

Expected evidence:
- blue oar
- star ledger page

Expected distractors:
- juniper bundles

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=9.858281 chunk_id=21346 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at Harbor Glass corridor? Case scope id: page-level-017. Page-...
  2. score=7.342543 chunk_id=21296 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
  3. score=4.318946 chunk_id=21132 preview=document page-river-lantern-inn-family-note-007::page-level-007, page 9, section section-007: In document page-river-lantern-inn-family-note-007, page 9, sec...
  4. score=2.028064 chunk_id=21426 preview=Question anchor: Which longer-page details in the audio reel describe the family memory scene at Birch Ferry shed? document page-birch-ferry-shed-audio-reel-...
- Matched markers: blue oar, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Partially grounded by: blue oar, star ledger page.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=60.283100 chunk_id=21762 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? Case scope id: page-level-097. Page-leve...
  2. score=41.294621 chunk_id=21764 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
  3. score=7.313074 chunk_id=21296 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
  4. score=7.297287 chunk_id=21452 preview=Question anchor: Which longer-page details in the family note describe the family memory scene at River Lantern inn? document page-river-lantern-inn-family-n...
- Matched markers: blue oar, star ledger page
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue oar, star ledger page.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (2 vs 3).

### Question 98 - page-level-098
Question: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed?

Expected evidence:
- moonflower cutting
- oak barrel hoops
- Signal Lantern Morning

Expected distractors:
- coal stove hiss

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.722764 chunk_id=21768 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? Case scope id: page-le...
  2. score=53.737046 chunk_id=21770 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  3. score=19.737046 chunk_id=21458 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
  4. score=14.374212 chunk_id=21562 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery? document page-star-b...
  5. score=14.369431 chunk_id=21561 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Star Basin gallery? document page-star-b...
- Matched markers: Signal Lantern Morning, moonflower cutting, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, moonflower cutting, oak barrel hoops.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=77.671613 chunk_id=21765 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? Case scope id: page-le...
  2. score=72.691076 chunk_id=21768 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? Case scope id: page-le...
  3. score=72.689069 chunk_id=21767 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? Case scope id: page-le...
  4. score=72.676657 chunk_id=21766 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? Case scope id: page-le...
  5. score=53.701631 chunk_id=21770 preview=Question anchor: Which profile-page details explain what Zora kept for the Signal Lantern Morning after returning to Birch Ferry shed? document page-birch-fe...
- Matched markers: Signal Lantern Morning, moonflower cutting, oak barrel hoops
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: Signal Lantern Morning, moonflower cutting, oak barrel hoops.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 99 - page-level-099
Question: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later?

Expected evidence:
- lantern hook
- juniper bundles
- coal stove hiss

Expected distractors:
- basalt sketch

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.601993 chunk_id=21773 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? Case scope id: page-level-099. Pa...
  2. score=53.610312 chunk_id=21776 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
  3. score=53.604692 chunk_id=21775 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
  4. score=7.721336 chunk_id=21464 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
  5. score=7.720711 chunk_id=21463 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
- Matched markers: coal stove hiss, juniper bundles, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, juniper bundles, lantern hook.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=72.579036 chunk_id=21773 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? Case scope id: page-level-099. Pa...
  2. score=72.573788 chunk_id=21772 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? Case scope id: page-level-099. Pa...
  3. score=72.556698 chunk_id=21774 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? Case scope id: page-level-099. Pa...
  4. score=53.571971 chunk_id=21776 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
  5. score=53.566210 chunk_id=21775 preview=Question anchor: Which page-level notes from the family note show why Ilia's photo memory at Driftwood cove mattered later? document page-driftwood-cove-fami...
- Matched markers: coal stove hiss, juniper bundles, lantern hook
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: coal stove hiss, juniper bundles, lantern hook.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Fewer distractors (0 vs 2).

### Question 100 - page-level-100
Question: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed?

Expected evidence:
- blue glass jar
- coal stove hiss

Expected distractors:
- willow basket

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.626835 chunk_id=21777 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-leve...
  2. score=60.686274 chunk_id=21778 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-leve...
  3. score=60.645179 chunk_id=21779 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-leve...
  4. score=41.694365 chunk_id=21780 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin...
  5. score=38.664292 chunk_id=21163 preview=document page-star-basin-gallery-audio-reel-100::page-level-100, page 17, section section-100: In document page-star-basin-gallery-audio-reel-100, page 17, s...
- Matched markers: blue glass jar, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, coal stove hiss.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Top chunks:
  1. score=65.581094 chunk_id=21777 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-leve...
  2. score=60.657790 chunk_id=21778 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-leve...
  3. score=60.625846 chunk_id=21779 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? Case scope id: page-leve...
  4. score=41.654844 chunk_id=21780 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin...
  5. score=7.599466 chunk_id=21468 preview=Question anchor: Which page-level details on Mira's audio reel explain why the Lantern Tide visit to Star Basin gallery was delayed? document page-star-basin...
- Matched markers: blue glass jar, coal stove hiss
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue glass jar, coal stove hiss.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Aggregate Results

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Question wins: 50
- Passed questions: 71
- Average evidence coverage: 0.8467
- Average first relevant rank: 1.0
- Total matched markers: 217
- Total missing markers: 40
- Total false-positive markers: 3
- Official metrics: {'hit_rate': 0.3, 'recall_at_k': 0.5366666666666666, 'mrr': 0.5933333333333334, 'forbidden_marker_rate': 0.115, 'average_latency_ms': 32.40527, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.5366666666666666, 'missing_expected_marker_count': 114, 'false_positive_count': 111}

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1`
- Question wins: 50
- Passed questions: 94
- Average evidence coverage: 0.9833
- Average first relevant rank: 1.0
- Total matched markers: 252
- Total missing markers: 5
- Total false-positive markers: 0
- Official metrics: {'hit_rate': 0.32, 'recall_at_k': 0.6333333333333333, 'mrr': 0.67, 'forbidden_marker_rate': 0.105, 'average_latency_ms': 33.075630000000004, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.6333333333333333, 'missing_expected_marker_count': 91, 'false_positive_count': 83}

### Runtime Activation
- Selected config: {'best_config_id': 'bge_m3', 'best_model_code': 'bge_m3', 'best_collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1', 'selected_metrics': {'hit_rate': 0.32, 'recall_at_k': 0.6333333333333333, 'mrr': 0.67, 'forbidden_marker_rate': 0.105, 'average_latency_ms': 33.075630000000004, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.6333333333333333, 'missing_expected_marker_count': 91, 'false_positive_count': 83}}
- Activated config: {'id': 2, 'profile_id': 6, 'model_code': 'bge_m3', 'collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1', 'top_k': 5, 'score_threshold': None, 'retrieval_mode': 'hybrid', 'source_eval_job_id': 151, 'source_eval_dataset_id': 'eternal-world-page-level-v1'}
- Runtime retrieval verification: {'model_code': 'bge_m3', 'result_count': 2, 'qdrant_collection': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_page_level_v1__3a78bd86b1', 'top_chunk_id': 21270}
