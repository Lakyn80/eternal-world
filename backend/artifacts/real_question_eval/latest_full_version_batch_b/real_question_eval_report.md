# Real Question Evaluation Report

## Client Summary
- Batch label: `Batch B`
- Source dataset: deterministic fictional eval corpus
- Real client/user data: no
- Purpose: retrieval quality testing
- Models compared:
  - `multilingual_e5_base`
  - `qwen3_embedding_0_6b`
- Baseline provider: `multilingual_e5_base`
- Newly evaluated provider: `qwen3_embedding_0_6b`
- Comparison scope: Only multilingual_e5_base and qwen3_embedding_0_6b are included in the final Batch B comparison; weaker historical providers, Jina, and larger Qwen candidates are excluded.
- Weaker historical providers intentionally excluded: multilingual_e5_small, bge_m3, paraphrase_multilingual_mpnet_base_v2, multilingual_e5_large, jina_embeddings_v3, qwen3_embedding_4b, qwen3_embedding_8b
- Winner: `multilingual_e5_base`
- Recommendation: Batch B does not show a clear enough win over the baseline `multilingual_e5_base`; keep `multilingual_e5_base` as the production recommendation.

## Technical Summary
- Run type: `full_version_batch_b`
- Execution mode: `full_version_batch_b_real_eval`
- Benchmark status: `completed`
- Used fake models: `false`
- Historical current winner before Batch B: `multilingual_e5_base`
- Any new provider beat baseline/current winner: `false`
- Timestamp: 2026-06-28T20:55:20.955297+00:00

## Dataset Questions Used
- Question 1: `question-sunflower-house` -> What details show which flower was kept at the old village house and what part of the entrance is mentioned?
- Question 2: `question-winter-trip` -> During the winter trip, what travel item was saved and what container kept everyone warm?
- Question 3: `question-grandmother-soup` -> Which ingredients and cooking setup explain why grandmother's soup tasted smoky?

## Baseline Provider
- `multilingual_e5_base`

## Newly Evaluated Provider
- `qwen3_embedding_0_6b`

## Per-Question Result Comparison
### Question 1 - question-sunflower-house
- Question text: What details show which flower was kept at the old village house and what part of the entrance is mentioned?
- Final evaluated answer: Grounded by retrieved evidence for: blue gate latch, sunflower seeds.
- Correctness verdict: grounded
- Evidence used: blue gate latch, sunflower seeds
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=partial coverage=0.5
- Winner: `multilingual_e5_base`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- Losing model issue: missing blue gate latch; distractors rose market poster
- Distractors / false positives: rose market poster

### Question 2 - question-winter-trip
- Question text: During the winter trip, what travel item was saved and what container kept everyone warm?
- Final evaluated answer: Grounded by retrieved evidence for: overnight train ticket, wooden thermos.
- Correctness verdict: grounded
- Evidence used: overnight train ticket, wooden thermos
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 3 - question-grandmother-soup
- Question text: Which ingredients and cooking setup explain why grandmother's soup tasted smoky?
- Final evaluated answer: Grounded by retrieved evidence for: dried mushrooms, oak stove.
- Correctness verdict: grounded
- Evidence used: dried mushrooms, oak stove
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; qwen3_embedding_0_6b -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

## Aggregate Metrics

### multilingual_e5_base
- Question wins: 3
- Passed questions: 3
- Evidence coverage: 1.0
- Missing evidence count: 0
- False-positive count: 0
- Latency comparison value: 7938.929
- First relevant rank average: 1.0

### qwen3_embedding_0_6b
- Question wins: 0
- Passed questions: 2
- Evidence coverage: 0.8333
- Missing evidence count: 1
- False-positive count: 1
- Latency comparison value: 356.5163333333333
- First relevant rank average: 1.0

## Winner
- Batch B winner: `multilingual_e5_base`

## Recommendation
- Recommended active model: `multilingual_e5_base`
- Production recommendation: Batch B does not show a clear enough win over the baseline `multilingual_e5_base`; keep `multilingual_e5_base` as the production recommendation.

## Safety Notes
- Only newly run provider: `qwen3_embedding_0_6b`
- Baseline reused from existing artifact: `multilingual_e5_base`
- Excluded weaker historical providers: multilingual_e5_small, bge_m3, paraphrase_multilingual_mpnet_base_v2, multilingual_e5_large, jina_embeddings_v3, qwen3_embedding_4b, qwen3_embedding_8b
- Latest real artifacts overwritten: `false`
- Latest fake artifacts overwritten: `false`
- Latest incremental artifacts overwritten: `false`
- Latest full-version Batch A artifacts overwritten: `false`
- Jina Embeddings v3 was not rerun and is not compared in Batch B.

## Artifact Files
- Latest Markdown: `/app/artifacts/real_question_eval/latest_full_version_batch_b/real_question_eval_report.md`
- Latest JSON: `/app/artifacts/real_question_eval/latest_full_version_batch_b/real_question_eval_result.json`
- Archived Markdown: `/app/artifacts/real_question_eval/runs/20260628_205520Z_full_version_batch_b/real_question_eval_report.md`
- Archived JSON: `/app/artifacts/real_question_eval/runs/20260628_205520Z_full_version_batch_b/real_question_eval_result.json`

## Developer Details

### question-sunflower-house
- Winner: `multilingual_e5_base`
- Reason: Higher evidence coverage (1.00 vs 0.50).
#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval`
- Matched markers: blue gate latch, sunflower seeds
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue gate latch, sunflower seeds.
- Verdict: grounded

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval`
- Matched markers: sunflower seeds
- Missing markers: blue gate latch
- Distractors: rose market poster
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: sunflower seeds. Missing: blue gate latch. Distractors present: rose market poster.
- Verdict: partial

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

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval`
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

#### qwen3_embedding_0_6b
- Collection: `eternal_world_rag_chunks__qwen3_embedding_0_6b__real_question_eval`
- Matched markers: dried mushrooms, oak stove
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: dried mushrooms, oak stove.
- Verdict: grounded
