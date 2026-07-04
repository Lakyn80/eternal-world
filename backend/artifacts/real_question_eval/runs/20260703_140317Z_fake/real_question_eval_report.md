# Real Question Evaluation Report

## Client Summary
- Source dataset: deterministic fictional eval corpus
- Real client/user data: no
- Purpose: retrieval quality testing
- Models compared:
  - `multilingual_e5_small`
  - `bge_m3`
- Recommended active model: `multilingual_e5_small`
- Speed vs accuracy tradeoff: Fake-mode evaluation is optimized for deterministic regression checks, not runtime speed measurements.
- Production recommendation: Keep the fake-mode result for test coverage only; use the preserved latest real evaluation for production-facing model decisions.
- Timestamp: 2026-07-03T14:03:17.603692+00:00
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
- Archived Markdown: `/app/artifacts/real_question_eval/runs/20260703_140317Z_fake/real_question_eval_report.md`
- Archived JSON: `/app/artifacts/real_question_eval/runs/20260703_140317Z_fake/real_question_eval_result.json`
- Archived Summary Markdown: `/app/artifacts/real_question_eval/runs/20260703_140317Z_fake/real_question_eval_summary.md`
- Archived Summary JSON: `/app/artifacts/real_question_eval/runs/20260703_140317Z_fake/real_question_eval_summary.json`

## Client Question Breakdown
### Question 1 - negative-missing-compass-serial
Question: What was the exact serial number engraved on the missing brass compass?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- invented serial number

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 2 - negative-mill-tunnel-password
Question: What password opened the secret tunnel beneath the old mill?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- moon password

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 3 - negative-mayor-hidden-daughter
Question: What was the name of the mayor's hidden daughter mentioned nowhere in the archive?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- Ilona Vey

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 4 - negative-sapphire-weight
Question: How much did the unopened sapphire parcel weigh before anyone recorded it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- twelve-gram sapphire

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 5 - negative-sixth-bell-verse
Question: What was the lost sixth verse of the river bell song?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- lost sixth bell verse

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 6 - negative-006
Question: What was the burned letter line that Selma supposedly mentioned at Winter Chapel porch, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- charcoal letter line

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 7 - negative-007
Question: Which exact unwritten wedding vow belonged to Anton's twin sister in the family note, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- winter vow text

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 8 - negative-008
Question: What is the missing hidden station code from the field recording connected to Marble stair hall?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- signal code 44

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 9 - negative-009
Question: What was the lost attic tally that Ilya supposedly mentioned at Cloud Wharf office, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- attic tally 19

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 10 - negative-010
Question: Which exact serial number belonged to Lina's stepfather in the winter letter, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- invented serial 8471

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 11 - negative-011
Question: What is the missing secret password from the holiday card connected to Ridge Post loft?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- moon-salt password

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 12 - negative-012
Question: What was the unrecorded middle name that Ada supposedly mentioned at North Bell workshop, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- Ilena Harbor name

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 13 - negative-013
Question: Which exact missing sixth verse belonged to Pavel's cousin in the boat manifest, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- lost bell verse

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 14 - negative-014
Question: What is the missing exact parcel weight from the audio reel connected to Blue Trunk cabin?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- twelve-gram parcel

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 15 - negative-015
Question: What was the private lock code that Anton supposedly mentioned at Bell Bridge square, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- glass-lock code

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 16 - negative-016
Question: Which exact burned letter line belonged to Mira's older sister in the station transcript, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- charcoal letter line

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 17 - negative-017
Question: What is the missing unwritten wedding vow from the memory sketchbook connected to Cedar Hill station?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- winter vow text

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 18 - negative-018
Question: What was the hidden station code that Lina supposedly mentioned at South Meadow arch, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- signal code 44

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 19 - negative-019
Question: Which exact lost attic tally belonged to Stefan's twin sister in the photo album page, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- attic tally 19

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 20 - negative-020
Question: What is the missing serial number from the profile page connected to Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- invented serial 8471

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 21 - negative-021
Question: What was the secret password that Pavel supposedly mentioned at Winter Chapel porch, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- moon-salt password

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 22 - negative-022
Question: Which exact unrecorded middle name belonged to Selma's stepfather in the field recording, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- Ilena Harbor name

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 23 - negative-023
Question: What is the missing missing sixth verse from the archive card connected to Marble stair hall?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- lost bell verse

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 24 - negative-024
Question: What was the exact parcel weight that Mira supposedly mentioned at Cloud Wharf office, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- twelve-gram parcel

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 25 - negative-025
Question: Which exact private lock code belonged to Ilya's cousin in the holiday card, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- glass-lock code

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 26 - negative-026
Question: What is the missing burned letter line from the river diary page connected to Ridge Post loft?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- charcoal letter line

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 27 - negative-027
Question: What was the unwritten wedding vow that Stefan supposedly mentioned at North Bell workshop, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- winter vow text

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 28 - negative-028
Question: Which exact hidden station code belonged to Ada's older sister in the audio reel, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- signal code 44

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 29 - negative-029
Question: What is the missing lost attic tally from the travel ledger connected to Blue Trunk cabin?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- attic tally 19

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 30 - negative-030
Question: What was the serial number that Selma supposedly mentioned at Bell Bridge square, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- invented serial 8471

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 31 - negative-031
Question: Which exact secret password belonged to Anton's twin sister in the memory sketchbook, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- moon-salt password

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 32 - negative-032
Question: What is the missing unrecorded middle name from the festival minutes connected to Cedar Hill station?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- Ilena Harbor name

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 33 - negative-033
Question: What was the missing sixth verse that Ilya supposedly mentioned at South Meadow arch, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- lost bell verse

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 34 - negative-034
Question: Which exact exact parcel weight belonged to Lina's stepfather in the profile page, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- twelve-gram parcel

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 35 - negative-035
Question: What is the missing private lock code from the family note connected to Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- glass-lock code

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 36 - negative-036
Question: What was the burned letter line that Ada supposedly mentioned at Winter Chapel porch, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- charcoal letter line

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 37 - negative-037
Question: Which exact unwritten wedding vow belonged to Pavel's cousin in the archive card, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- winter vow text

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 38 - negative-038
Question: What is the missing hidden station code from the winter letter connected to Marble stair hall?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- signal code 44

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 39 - negative-039
Question: What was the lost attic tally that Anton supposedly mentioned at Cloud Wharf office, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- attic tally 19

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 40 - negative-040
Question: Which exact serial number belonged to Mira's older sister in the river diary page, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- invented serial 8471

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 41 - negative-041
Question: What is the missing secret password from the boat manifest connected to Ridge Post loft?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- moon-salt password

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 42 - negative-042
Question: What was the unrecorded middle name that Lina supposedly mentioned at North Bell workshop, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- Ilena Harbor name

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 43 - negative-043
Question: Which exact missing sixth verse belonged to Stefan's twin sister in the travel ledger, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- lost bell verse

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 44 - negative-044
Question: What is the missing exact parcel weight from the station transcript connected to Blue Trunk cabin?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- twelve-gram parcel

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 45 - negative-045
Question: What was the private lock code that Pavel supposedly mentioned at Bell Bridge square, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- glass-lock code

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 46 - negative-046
Question: Which exact burned letter line belonged to Selma's stepfather in the festival minutes, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- charcoal letter line

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 47 - negative-047
Question: What is the missing unwritten wedding vow from the photo album page connected to Cedar Hill station?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- winter vow text

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 48 - negative-048
Question: What was the hidden station code that Mira supposedly mentioned at South Meadow arch, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- signal code 44

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 49 - negative-049
Question: Which exact lost attic tally belonged to Ilya's cousin in the family note, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- attic tally 19

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 50 - negative-050
Question: What is the missing serial number from the field recording connected to Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- invented serial 8471

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 51 - negative-051
Question: What was the secret password that Stefan supposedly mentioned at Winter Chapel porch, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- moon-salt password

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 52 - negative-052
Question: Which exact unrecorded middle name belonged to Ada's older sister in the winter letter, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- Ilena Harbor name

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 53 - negative-053
Question: What is the missing missing sixth verse from the holiday card connected to Marble stair hall?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- lost bell verse

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 54 - negative-054
Question: What was the exact parcel weight that Selma supposedly mentioned at Cloud Wharf office, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- twelve-gram parcel

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 55 - negative-055
Question: Which exact private lock code belonged to Anton's twin sister in the boat manifest, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- glass-lock code

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 56 - negative-056
Question: What is the missing burned letter line from the audio reel connected to Ridge Post loft?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- charcoal letter line

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 57 - negative-057
Question: What was the unwritten wedding vow that Ilya supposedly mentioned at North Bell workshop, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- winter vow text

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 58 - negative-058
Question: Which exact hidden station code belonged to Lina's stepfather in the station transcript, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- signal code 44

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 59 - negative-059
Question: What is the missing lost attic tally from the memory sketchbook connected to Blue Trunk cabin?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- attic tally 19

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 60 - negative-060
Question: What was the serial number that Ada supposedly mentioned at Bell Bridge square, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- invented serial 8471

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 61 - negative-061
Question: Which exact secret password belonged to Pavel's cousin in the photo album page, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- moon-salt password

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 62 - negative-062
Question: What is the missing unrecorded middle name from the profile page connected to Cedar Hill station?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- Ilena Harbor name

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 63 - negative-063
Question: What was the missing sixth verse that Anton supposedly mentioned at South Meadow arch, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- lost bell verse

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 64 - negative-064
Question: Which exact exact parcel weight belonged to Mira's older sister in the field recording, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- twelve-gram parcel

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 65 - negative-065
Question: What is the missing private lock code from the archive card connected to Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- glass-lock code

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 66 - negative-066
Question: What was the burned letter line that Lina supposedly mentioned at Winter Chapel porch, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- charcoal letter line

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 67 - negative-067
Question: Which exact unwritten wedding vow belonged to Stefan's twin sister in the holiday card, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- winter vow text

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 68 - negative-068
Question: What is the missing hidden station code from the river diary page connected to Marble stair hall?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- signal code 44

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 69 - negative-069
Question: What was the lost attic tally that Pavel supposedly mentioned at Cloud Wharf office, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- attic tally 19

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 70 - negative-070
Question: Which exact serial number belonged to Selma's stepfather in the audio reel, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- invented serial 8471

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 71 - negative-071
Question: What is the missing secret password from the travel ledger connected to Ridge Post loft?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- moon-salt password

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 72 - negative-072
Question: What was the unrecorded middle name that Mira supposedly mentioned at North Bell workshop, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- Ilena Harbor name

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 73 - negative-073
Question: Which exact missing sixth verse belonged to Ilya's cousin in the memory sketchbook, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- lost bell verse

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 74 - negative-074
Question: What is the missing exact parcel weight from the festival minutes connected to Blue Trunk cabin?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- twelve-gram parcel

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 75 - negative-075
Question: What was the private lock code that Stefan supposedly mentioned at Bell Bridge square, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- glass-lock code

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 76 - negative-076
Question: Which exact burned letter line belonged to Ada's older sister in the profile page, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- charcoal letter line

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 77 - negative-077
Question: What is the missing unwritten wedding vow from the family note connected to Cedar Hill station?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- winter vow text

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 78 - negative-078
Question: What was the hidden station code that Selma supposedly mentioned at South Meadow arch, even though no archive records it?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=no_evidence coverage=None
- Winner: `multilingual_e5_small`
- Why it won: Fewer distractors (0 vs 1).
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- signal code 44

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=no_evidence coverage=None matched=none missing=none distractors=none

### Question 79 - negative-079
Question: Which exact lost attic tally belonged to Anton's twin sister in the archive card, despite never being written down?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- attic tally 19

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

### Question 80 - negative-080
Question: What is the missing serial number from the winter letter connected to Birch Ferry shed?
- Final evaluated answer: Grounded by retrieved evidence for: .
- Correctness verdict: grounded
- Evidence used: none
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=None; bge_m3 -> verdict=grounded coverage=None
- Winner: `bge_m3`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:

Expected distractors:
- invented serial 8471

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=None matched=none missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=None matched=none missing=none distractors=none

## Aggregate Client Decision
- Recommended active model: `multilingual_e5_small`
- Overall winner: `multilingual_e5_small`
- Activation state: `true`
- Runtime retrieval verified: `true`
- Production recommendation: Keep the fake-mode result for test coverage only; use the preserved latest real evaluation for production-facing model decisions.

## Developer Details

### Question 1 - negative-missing-compass-serial
Question: What was the exact serial number engraved on the missing brass compass?

Expected evidence:

Expected distractors:
- invented serial number

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 2 - negative-mill-tunnel-password
Question: What password opened the secret tunnel beneath the old mill?

Expected evidence:

Expected distractors:
- moon password

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.097590 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 3 - negative-mayor-hidden-daughter
Question: What was the name of the mayor's hidden daughter mentioned nowhere in the archive?

Expected evidence:

Expected distractors:
- Ilona Vey

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 4 - negative-sapphire-weight
Question: How much did the unopened sapphire parcel weigh before anyone recorded it?

Expected evidence:

Expected distractors:
- twelve-gram sapphire

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 5 - negative-sixth-bell-verse
Question: What was the lost sixth verse of the river bell song?

Expected evidence:

Expected distractors:
- lost sixth bell verse

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.086066 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 6 - negative-006
Question: What was the burned letter line that Selma supposedly mentioned at Winter Chapel porch, even though no archive records it?

Expected evidence:

Expected distractors:
- charcoal letter line

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.059235 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 7 - negative-007
Question: Which exact unwritten wedding vow belonged to Anton's twin sister in the family note, despite never being written down?

Expected evidence:

Expected distractors:
- winter vow text

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 8 - negative-008
Question: What is the missing hidden station code from the field recording connected to Marble stair hall?

Expected evidence:

Expected distractors:
- signal code 44

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 9 - negative-009
Question: What was the lost attic tally that Ilya supposedly mentioned at Cloud Wharf office, even though no archive records it?

Expected evidence:

Expected distractors:
- attic tally 19

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.062622 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 10 - negative-010
Question: Which exact serial number belonged to Lina's stepfather in the winter letter, despite never being written down?

Expected evidence:

Expected distractors:
- invented serial 8471

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 11 - negative-011
Question: What is the missing secret password from the holiday card connected to Ridge Post loft?

Expected evidence:

Expected distractors:
- moon-salt password

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 12 - negative-012
Question: What was the unrecorded middle name that Ada supposedly mentioned at North Bell workshop, even though no archive records it?

Expected evidence:

Expected distractors:
- Ilena Harbor name

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.053838 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 13 - negative-013
Question: Which exact missing sixth verse belonged to Pavel's cousin in the boat manifest, despite never being written down?

Expected evidence:

Expected distractors:
- lost bell verse

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 14 - negative-014
Question: What is the missing exact parcel weight from the audio reel connected to Blue Trunk cabin?

Expected evidence:

Expected distractors:
- twelve-gram parcel

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 15 - negative-015
Question: What was the private lock code that Anton supposedly mentioned at Bell Bridge square, even though no archive records it?

Expected evidence:

Expected distractors:
- glass-lock code

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.059235 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 16 - negative-016
Question: Which exact burned letter line belonged to Mira's older sister in the station transcript, despite never being written down?

Expected evidence:

Expected distractors:
- charcoal letter line

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 17 - negative-017
Question: What is the missing unwritten wedding vow from the memory sketchbook connected to Cedar Hill station?

Expected evidence:

Expected distractors:
- winter vow text

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 18 - negative-018
Question: What was the hidden station code that Lina supposedly mentioned at South Meadow arch, even though no archive records it?

Expected evidence:

Expected distractors:
- signal code 44

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.062622 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 19 - negative-019
Question: Which exact lost attic tally belonged to Stefan's twin sister in the photo album page, despite never being written down?

Expected evidence:

Expected distractors:
- attic tally 19

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 20 - negative-020
Question: What is the missing serial number from the profile page connected to Birch Ferry shed?

Expected evidence:

Expected distractors:
- invented serial 8471

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 21 - negative-021
Question: What was the secret password that Pavel supposedly mentioned at Winter Chapel porch, even though no archive records it?

Expected evidence:

Expected distractors:
- moon-salt password

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.059235 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 22 - negative-022
Question: Which exact unrecorded middle name belonged to Selma's stepfather in the field recording, despite never being written down?

Expected evidence:

Expected distractors:
- Ilena Harbor name

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 23 - negative-023
Question: What is the missing missing sixth verse from the archive card connected to Marble stair hall?

Expected evidence:

Expected distractors:
- lost bell verse

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 24 - negative-024
Question: What was the exact parcel weight that Mira supposedly mentioned at Cloud Wharf office, even though no archive records it?

Expected evidence:

Expected distractors:
- twelve-gram parcel

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.062622 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 25 - negative-025
Question: Which exact private lock code belonged to Ilya's cousin in the holiday card, despite never being written down?

Expected evidence:

Expected distractors:
- glass-lock code

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 26 - negative-026
Question: What is the missing burned letter line from the river diary page connected to Ridge Post loft?

Expected evidence:

Expected distractors:
- charcoal letter line

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 27 - negative-027
Question: What was the unwritten wedding vow that Stefan supposedly mentioned at North Bell workshop, even though no archive records it?

Expected evidence:

Expected distractors:
- winter vow text

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.107676 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 28 - negative-028
Question: Which exact hidden station code belonged to Ada's older sister in the audio reel, despite never being written down?

Expected evidence:

Expected distractors:
- signal code 44

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 29 - negative-029
Question: What is the missing lost attic tally from the travel ledger connected to Blue Trunk cabin?

Expected evidence:

Expected distractors:
- attic tally 19

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 30 - negative-030
Question: What was the serial number that Selma supposedly mentioned at Bell Bridge square, even though no archive records it?

Expected evidence:

Expected distractors:
- invented serial 8471

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.062622 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 31 - negative-031
Question: Which exact secret password belonged to Anton's twin sister in the memory sketchbook, despite never being written down?

Expected evidence:

Expected distractors:
- moon-salt password

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 32 - negative-032
Question: What is the missing unrecorded middle name from the festival minutes connected to Cedar Hill station?

Expected evidence:

Expected distractors:
- Ilena Harbor name

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 33 - negative-033
Question: What was the missing sixth verse that Ilya supposedly mentioned at South Meadow arch, even though no archive records it?

Expected evidence:

Expected distractors:
- lost bell verse

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.056344 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 34 - negative-034
Question: Which exact exact parcel weight belonged to Lina's stepfather in the profile page, despite never being written down?

Expected evidence:

Expected distractors:
- twelve-gram parcel

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 35 - negative-035
Question: What is the missing private lock code from the family note connected to Birch Ferry shed?

Expected evidence:

Expected distractors:
- glass-lock code

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 36 - negative-036
Question: What was the burned letter line that Ada supposedly mentioned at Winter Chapel porch, even though no archive records it?

Expected evidence:

Expected distractors:
- charcoal letter line

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.059235 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 37 - negative-037
Question: Which exact unwritten wedding vow belonged to Pavel's cousin in the archive card, despite never being written down?

Expected evidence:

Expected distractors:
- winter vow text

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 38 - negative-038
Question: What is the missing hidden station code from the winter letter connected to Marble stair hall?

Expected evidence:

Expected distractors:
- signal code 44

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 39 - negative-039
Question: What was the lost attic tally that Anton supposedly mentioned at Cloud Wharf office, even though no archive records it?

Expected evidence:

Expected distractors:
- attic tally 19

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.062622 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 40 - negative-040
Question: Which exact serial number belonged to Mira's older sister in the river diary page, despite never being written down?

Expected evidence:

Expected distractors:
- invented serial 8471

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 41 - negative-041
Question: What is the missing secret password from the boat manifest connected to Ridge Post loft?

Expected evidence:

Expected distractors:
- moon-salt password

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 42 - negative-042
Question: What was the unrecorded middle name that Lina supposedly mentioned at North Bell workshop, even though no archive records it?

Expected evidence:

Expected distractors:
- Ilena Harbor name

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.053838 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 43 - negative-043
Question: Which exact missing sixth verse belonged to Stefan's twin sister in the travel ledger, despite never being written down?

Expected evidence:

Expected distractors:
- lost bell verse

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 44 - negative-044
Question: What is the missing exact parcel weight from the station transcript connected to Blue Trunk cabin?

Expected evidence:

Expected distractors:
- twelve-gram parcel

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 45 - negative-045
Question: What was the private lock code that Pavel supposedly mentioned at Bell Bridge square, even though no archive records it?

Expected evidence:

Expected distractors:
- glass-lock code

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.059235 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 46 - negative-046
Question: Which exact burned letter line belonged to Selma's stepfather in the festival minutes, despite never being written down?

Expected evidence:

Expected distractors:
- charcoal letter line

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 47 - negative-047
Question: What is the missing unwritten wedding vow from the photo album page connected to Cedar Hill station?

Expected evidence:

Expected distractors:
- winter vow text

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 48 - negative-048
Question: What was the hidden station code that Mira supposedly mentioned at South Meadow arch, even though no archive records it?

Expected evidence:

Expected distractors:
- signal code 44

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.062622 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 49 - negative-049
Question: Which exact lost attic tally belonged to Ilya's cousin in the family note, despite never being written down?

Expected evidence:

Expected distractors:
- attic tally 19

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 50 - negative-050
Question: What is the missing serial number from the field recording connected to Birch Ferry shed?

Expected evidence:

Expected distractors:
- invented serial 8471

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 51 - negative-051
Question: What was the secret password that Stefan supposedly mentioned at Winter Chapel porch, even though no archive records it?

Expected evidence:

Expected distractors:
- moon-salt password

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.062622 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 52 - negative-052
Question: Which exact unrecorded middle name belonged to Ada's older sister in the winter letter, despite never being written down?

Expected evidence:

Expected distractors:
- Ilena Harbor name

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 53 - negative-053
Question: What is the missing missing sixth verse from the holiday card connected to Marble stair hall?

Expected evidence:

Expected distractors:
- lost bell verse

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 54 - negative-054
Question: What was the exact parcel weight that Selma supposedly mentioned at Cloud Wharf office, even though no archive records it?

Expected evidence:

Expected distractors:
- twelve-gram parcel

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.062622 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 55 - negative-055
Question: Which exact private lock code belonged to Anton's twin sister in the boat manifest, despite never being written down?

Expected evidence:

Expected distractors:
- glass-lock code

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 56 - negative-056
Question: What is the missing burned letter line from the audio reel connected to Ridge Post loft?

Expected evidence:

Expected distractors:
- charcoal letter line

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 57 - negative-057
Question: What was the unwritten wedding vow that Ilya supposedly mentioned at North Bell workshop, even though no archive records it?

Expected evidence:

Expected distractors:
- winter vow text

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.053838 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 58 - negative-058
Question: Which exact hidden station code belonged to Lina's stepfather in the station transcript, despite never being written down?

Expected evidence:

Expected distractors:
- signal code 44

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 59 - negative-059
Question: What is the missing lost attic tally from the memory sketchbook connected to Blue Trunk cabin?

Expected evidence:

Expected distractors:
- attic tally 19

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 60 - negative-060
Question: What was the serial number that Ada supposedly mentioned at Bell Bridge square, even though no archive records it?

Expected evidence:

Expected distractors:
- invented serial 8471

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.062622 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 61 - negative-061
Question: Which exact secret password belonged to Pavel's cousin in the photo album page, despite never being written down?

Expected evidence:

Expected distractors:
- moon-salt password

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 62 - negative-062
Question: What is the missing unrecorded middle name from the profile page connected to Cedar Hill station?

Expected evidence:

Expected distractors:
- Ilena Harbor name

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 63 - negative-063
Question: What was the missing sixth verse that Anton supposedly mentioned at South Meadow arch, even though no archive records it?

Expected evidence:

Expected distractors:
- lost bell verse

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.056344 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 64 - negative-064
Question: Which exact exact parcel weight belonged to Mira's older sister in the field recording, despite never being written down?

Expected evidence:

Expected distractors:
- twelve-gram parcel

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 65 - negative-065
Question: What is the missing private lock code from the archive card connected to Birch Ferry shed?

Expected evidence:

Expected distractors:
- glass-lock code

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 66 - negative-066
Question: What was the burned letter line that Lina supposedly mentioned at Winter Chapel porch, even though no archive records it?

Expected evidence:

Expected distractors:
- charcoal letter line

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.059235 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 67 - negative-067
Question: Which exact unwritten wedding vow belonged to Stefan's twin sister in the holiday card, despite never being written down?

Expected evidence:

Expected distractors:
- winter vow text

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 68 - negative-068
Question: What is the missing hidden station code from the river diary page connected to Marble stair hall?

Expected evidence:

Expected distractors:
- signal code 44

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 69 - negative-069
Question: What was the lost attic tally that Pavel supposedly mentioned at Cloud Wharf office, even though no archive records it?

Expected evidence:

Expected distractors:
- attic tally 19

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.062622 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 70 - negative-070
Question: Which exact serial number belonged to Selma's stepfather in the audio reel, despite never being written down?

Expected evidence:

Expected distractors:
- invented serial 8471

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 71 - negative-071
Question: What is the missing secret password from the travel ledger connected to Ridge Post loft?

Expected evidence:

Expected distractors:
- moon-salt password

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 72 - negative-072
Question: What was the unrecorded middle name that Mira supposedly mentioned at North Bell workshop, even though no archive records it?

Expected evidence:

Expected distractors:
- Ilena Harbor name

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.053838 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 73 - negative-073
Question: Which exact missing sixth verse belonged to Ilya's cousin in the memory sketchbook, despite never being written down?

Expected evidence:

Expected distractors:
- lost bell verse

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 74 - negative-074
Question: What is the missing exact parcel weight from the festival minutes connected to Blue Trunk cabin?

Expected evidence:

Expected distractors:
- twelve-gram parcel

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 75 - negative-075
Question: What was the private lock code that Stefan supposedly mentioned at Bell Bridge square, even though no archive records it?

Expected evidence:

Expected distractors:
- glass-lock code

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.059235 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 76 - negative-076
Question: Which exact burned letter line belonged to Ada's older sister in the profile page, despite never being written down?

Expected evidence:

Expected distractors:
- charcoal letter line

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 77 - negative-077
Question: What is the missing unwritten wedding vow from the family note connected to Cedar Hill station?

Expected evidence:

Expected distractors:
- winter vow text

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 78 - negative-078
Question: What was the hidden station code that Selma supposedly mentioned at South Meadow arch, even though no archive records it?

Expected evidence:

Expected distractors:
- signal code 44

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. score=0.062622 chunk_id=22329 preview=Validation archive placeholder. This corpus intentionally contains no matching evidence for the requested question set.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: No grounded evidence markers were retrieved.
- Verdict: no_evidence

- Winner:
  - `multilingual_e5_small`
  - Fewer distractors (0 vs 1).

### Question 79 - negative-079
Question: Which exact lost attic tally belonged to Anton's twin sister in the archive card, despite never being written down?

Expected evidence:

Expected distractors:
- attic tally 19

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 80 - negative-080
Question: What is the missing serial number from the winter letter connected to Birch Ferry shed?

Expected evidence:

Expected distractors:
- invented serial 8471

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Top chunks:
  1. No retrieved chunks.
- Matched markers: none
- Missing markers: none
- Distractors: none
- Evidence coverage: n/a
- First relevant rank: n/a
- Answer summary: Grounded by retrieved evidence for: .
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Aggregate Results

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Question wins: 27
- Passed questions: 80
- Average evidence coverage: 0.0
- Average first relevant rank: n/a
- Total matched markers: 0
- Total missing markers: 0
- Total false-positive markers: 0
- Official metrics: {'hit_rate': 0.0, 'recall_at_k': 0.0, 'mrr': 0.0, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 27.9077875, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.0, 'missing_expected_marker_count': 0, 'false_positive_count': 80}

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2`
- Question wins: 53
- Passed questions: 53
- Average evidence coverage: 0.0
- Average first relevant rank: n/a
- Total matched markers: 0
- Total missing markers: 0
- Total false-positive markers: 0
- Official metrics: {'hit_rate': 0.0, 'recall_at_k': 0.0, 'mrr': 0.0, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 25.600775, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.0, 'missing_expected_marker_count': 0, 'false_positive_count': 80}

### Runtime Activation
- Selected config: {'best_config_id': 'bge_m3', 'best_model_code': 'bge_m3', 'best_collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2', 'selected_metrics': {'hit_rate': 0.0, 'recall_at_k': 0.0, 'mrr': 0.0, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 25.600775, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.0, 'missing_expected_marker_count': 0, 'false_positive_count': 80}}
- Activated config: {'id': 2, 'profile_id': 6, 'model_code': 'bge_m3', 'collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2', 'top_k': 5, 'score_threshold': None, 'retrieval_mode': 'hybrid', 'source_eval_job_id': 153, 'source_eval_dataset_id': 'eternal-world-negative-v1'}
- Runtime retrieval verification: {'model_code': 'bge_m3', 'result_count': 1, 'qdrant_collection': 'eternal_world_rag_chunks__bge_m3__real_question_eval__eternal_world_negative_v1__557ebda6e2', 'top_chunk_id': 22329}
