# Real Question Evaluation Report

## Client Summary
- Batch label: `Batch A`
- Source dataset: deterministic fictional eval corpus
- Real client/user data: no
- Purpose: retrieval quality testing
- Models compared:
  - `multilingual_e5_base`
  - `multilingual_e5_large`
- Baseline provider: `multilingual_e5_base`
- Newly evaluated provider: `multilingual_e5_large`
- Comparison scope: Only multilingual_e5_base and multilingual_e5_large are included in the final Batch A comparison; weaker historical providers are excluded.
- Weaker historical providers intentionally excluded: multilingual_e5_small, bge_m3, paraphrase_multilingual_mpnet_base_v2
- Winner: `multilingual_e5_base`
- Recommendation: Batch A does not show a clear enough win over the baseline multilingual_e5_base; keep multilingual_e5_base as the production recommendation.

## Technical Summary
- Run type: `full_version_batch_a`
- Execution mode: `full_version_batch_a_real_eval`
- Used fake models: `false`
- Historical current winner before Batch A: `multilingual_e5_base`
- Any new provider beat baseline/current winner: `false`
- Timestamp: 2026-06-26T22:09:07.029544+00:00

## Dataset Questions Used
- Question 1: `question-sunflower-house` -> What details show which flower was kept at the old village house and what part of the entrance is mentioned?
- Question 2: `question-winter-trip` -> During the winter trip, what travel item was saved and what container kept everyone warm?
- Question 3: `question-grandmother-soup` -> Which ingredients and cooking setup explain why grandmother's soup tasted smoky?

## Baseline Provider
- `multilingual_e5_base`

## Newly Evaluated Provider
- `multilingual_e5_large`

## Per-Question Result Comparison
### Question 1 - question-sunflower-house
- Question text: What details show which flower was kept at the old village house and what part of the entrance is mentioned?
- Final evaluated answer: Grounded by retrieved evidence for: blue gate latch, sunflower seeds.
- Correctness verdict: grounded
- Evidence used: blue gate latch, sunflower seeds
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; multilingual_e5_large -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_large`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 2 - question-winter-trip
- Question text: During the winter trip, what travel item was saved and what container kept everyone warm?
- Final evaluated answer: Grounded by retrieved evidence for: overnight train ticket, wooden thermos.
- Correctness verdict: grounded
- Evidence used: overnight train ticket, wooden thermos
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; multilingual_e5_large -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 3 - question-grandmother-soup
- Question text: Which ingredients and cooking setup explain why grandmother's soup tasted smoky?
- Final evaluated answer: Grounded by retrieved evidence for: dried mushrooms, oak stove.
- Correctness verdict: grounded
- Evidence used: dried mushrooms, oak stove
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; multilingual_e5_large -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

## Aggregate Metrics

### multilingual_e5_base
- Question wins: 2
- Passed questions: 3
- Evidence coverage: 1.0
- Missing evidence count: 0
- False-positive count: 0
- Latency comparison value: 7938.929
- First relevant rank average: 1.0

### multilingual_e5_large
- Question wins: 1
- Passed questions: 3
- Evidence coverage: 1.0
- Missing evidence count: 0
- False-positive count: 0
- Latency comparison value: 8687.417
- First relevant rank average: 1.0

## Winner
- Batch A winner: `multilingual_e5_base`

## Recommendation
- Recommended active model: `multilingual_e5_base`
- Production recommendation: Batch A does not show a clear enough win over the baseline multilingual_e5_base; keep multilingual_e5_base as the production recommendation.

## Safety Notes
- Only newly run provider: `multilingual_e5_large`
- Baseline reused from existing artifact: `multilingual_e5_base`
- Excluded weaker historical providers: multilingual_e5_small, bge_m3, paraphrase_multilingual_mpnet_base_v2
- Latest real artifacts overwritten: `false`
- Latest fake artifacts overwritten: `false`
- Latest incremental artifacts overwritten: `false`

## Artifact Files
- Latest Markdown: `/app/artifacts/real_question_eval/latest_full_version_batch_a/real_question_eval_report.md`
- Latest JSON: `/app/artifacts/real_question_eval/latest_full_version_batch_a/real_question_eval_result.json`
- Archived Markdown: `/app/artifacts/real_question_eval/runs/20260626_220907Z_full_version_batch_a/real_question_eval_report.md`
- Archived JSON: `/app/artifacts/real_question_eval/runs/20260626_220907Z_full_version_batch_a/real_question_eval_result.json`

## Developer Details

### question-sunflower-house
- Winner: `multilingual_e5_large`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval`
- Matched markers: blue gate latch, sunflower seeds
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue gate latch, sunflower seeds.
- Verdict: grounded

#### multilingual_e5_large
- Collection: `eternal_world_rag_chunks__multilingual_e5_large__real_question_eval`
- Matched markers: blue gate latch, sunflower seeds
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue gate latch, sunflower seeds.
- Verdict: grounded

### question-winter-trip
- Winner: `multilingual_e5_base`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval`
- Matched markers: overnight train ticket, wooden thermos
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: overnight train ticket, wooden thermos.
- Verdict: grounded

#### multilingual_e5_large
- Collection: `eternal_world_rag_chunks__multilingual_e5_large__real_question_eval`
- Matched markers: overnight train ticket, wooden thermos
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: overnight train ticket, wooden thermos.
- Verdict: grounded

### question-grandmother-soup
- Winner: `multilingual_e5_base`
- Reason: Tie broken by stronger top retrieval score and overall selector alignment.
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval`
- Matched markers: dried mushrooms, oak stove
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: dried mushrooms, oak stove.
- Verdict: grounded

#### multilingual_e5_large
- Collection: `eternal_world_rag_chunks__multilingual_e5_large__real_question_eval`
- Matched markers: dried mushrooms, oak stove
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: dried mushrooms, oak stove.
- Verdict: grounded
