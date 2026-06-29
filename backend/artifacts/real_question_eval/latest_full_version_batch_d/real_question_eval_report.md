# Real Question Evaluation Report

## Client Summary
- Batch label: `Batch D`
- Source dataset: deterministic fictional eval corpus
- Real client/user data: no
- Purpose: retrieval quality testing
- Models compared:
  - `multilingual_e5_base`
  - `bge_m3_dense_sparse`
  - `bge_m3_dense_sparse_multivector`
- Baseline provider: `multilingual_e5_base`
- Newly evaluated providers: `bge_m3_dense_sparse`, `bge_m3_dense_sparse_multivector`
- Comparison scope: Only multilingual_e5_base, bge_m3_dense_sparse, and bge_m3_dense_sparse_multivector are included in the final Batch D comparison. BGE-M3 hybrid modes use a manual local reranking path because the current production Qdrant retrieval path is dense-only.
- Weaker historical providers intentionally excluded: multilingual_e5_small, bge_m3, paraphrase_multilingual_mpnet_base_v2, multilingual_e5_large, jina_embeddings_v3, qwen3_embedding_0_6b, qwen3_embedding_4b, qwen3_embedding_8b
- Winner: `bge_m3_dense_sparse`
- Recommendation: Batch D indicates `bge_m3_dense_sparse` beat the baseline `multilingual_e5_base`; review the successful BGE-M3 hybrid candidate for promotion.

## Technical Summary
- Run type: `full_version_batch_d`
- Execution mode: `full_version_batch_d_real_eval`
- Benchmark status: `completed`
- Used fake models: `false`
- Historical current winner before Batch D: `multilingual_e5_base`
- Any new provider beat baseline/current winner: `true`
- Timestamp: 2026-06-29T07:47:26.140140+00:00
- Note: Batch D keeps production retrieval unchanged and uses a manual local hybrid reranking path.

## Dataset Questions Used
- Question 1: `question-sunflower-house` -> What details show which flower was kept at the old village house and what part of the entrance is mentioned?
- Question 2: `question-winter-trip` -> During the winter trip, what travel item was saved and what container kept everyone warm?
- Question 3: `question-grandmother-soup` -> Which ingredients and cooking setup explain why grandmother's soup tasted smoky?

## Baseline Provider
- `multilingual_e5_base`

## Newly Evaluated Providers
- `bge_m3_dense_sparse`
- `bge_m3_dense_sparse_multivector`

## Per-Question Result Comparison
### Question 1 - question-sunflower-house
- Question text: What details show which flower was kept at the old village house and what part of the entrance is mentioned?
- Final evaluated answer: Grounded by retrieved evidence for: blue gate latch, sunflower seeds.
- Correctness verdict: grounded
- Evidence used: blue gate latch, sunflower seeds
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; bge_m3_dense_sparse -> verdict=grounded coverage=1.0; bge_m3_dense_sparse_multivector -> verdict=grounded coverage=1.0
- Winner: `bge_m3_dense_sparse`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 2 - question-winter-trip
- Question text: During the winter trip, what travel item was saved and what container kept everyone warm?
- Final evaluated answer: Grounded by retrieved evidence for: overnight train ticket, wooden thermos.
- Correctness verdict: grounded
- Evidence used: overnight train ticket, wooden thermos
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; bge_m3_dense_sparse -> verdict=grounded coverage=1.0; bge_m3_dense_sparse_multivector -> verdict=grounded coverage=1.0
- Winner: `bge_m3_dense_sparse_multivector`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

### Question 3 - question-grandmother-soup
- Question text: Which ingredients and cooking setup explain why grandmother's soup tasted smoky?
- Final evaluated answer: Grounded by retrieved evidence for: dried mushrooms, oak stove.
- Correctness verdict: grounded
- Evidence used: dried mushrooms, oak stove
- Model comparison: multilingual_e5_base -> verdict=grounded coverage=1.0; bge_m3_dense_sparse -> verdict=grounded coverage=1.0; bge_m3_dense_sparse_multivector -> verdict=grounded coverage=1.0
- Winner: `bge_m3_dense_sparse`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- Losing model issue: lower retrieval score despite comparable evidence
- Distractors / false positives: none

## Aggregate Metrics

### multilingual_e5_base
- Question wins: 0
- Passed questions: 3
- Evidence coverage: 1.0
- Missing evidence count: 0
- False-positive count: 0
- Latency comparison value: 7938.929
- First relevant rank average: 1.0

### bge_m3_dense_sparse
- Question wins: 2
- Passed questions: 3
- Evidence coverage: 1.0
- Missing evidence count: 0
- False-positive count: 0
- Latency comparison value: 1415.362
- First relevant rank average: 1.0

### bge_m3_dense_sparse_multivector
- Question wins: 1
- Passed questions: 3
- Evidence coverage: 1.0
- Missing evidence count: 0
- False-positive count: 0
- Latency comparison value: 9632.006
- First relevant rank average: 1.0

## Winner
- Batch D winner: `bge_m3_dense_sparse`

## Recommendation
- Recommended active model: `bge_m3_dense_sparse`
- Production recommendation: Batch D indicates `bge_m3_dense_sparse` beat the baseline `multilingual_e5_base`; review the successful BGE-M3 hybrid candidate for promotion.

## Safety Notes
- Newly run providers requested: `bge_m3_dense_sparse`, `bge_m3_dense_sparse_multivector`
- Baseline reused from existing artifact: `multilingual_e5_base`
- Excluded weaker historical providers: multilingual_e5_small, bge_m3, paraphrase_multilingual_mpnet_base_v2, multilingual_e5_large, jina_embeddings_v3, qwen3_embedding_0_6b, qwen3_embedding_4b, qwen3_embedding_8b
- Latest real artifacts overwritten: `false`
- Latest fake artifacts overwritten: `false`
- Latest incremental artifacts overwritten: `false`
- Latest full-version Batch A artifacts overwritten: `false`
- Latest full-version Batch B artifacts overwritten: `false`
- Latest full-version Batch C artifacts overwritten: `false`
- Batch D keeps production retrieval unchanged and uses a manual local hybrid reranking path.

## Artifact Files
- Latest Markdown: `/app/artifacts/real_question_eval/latest_full_version_batch_d/real_question_eval_report.md`
- Latest JSON: `/app/artifacts/real_question_eval/latest_full_version_batch_d/real_question_eval_result.json`
- Archived Markdown: `/app/artifacts/real_question_eval/runs/20260629_074726Z_full_version_batch_d/real_question_eval_report.md`
- Archived JSON: `/app/artifacts/real_question_eval/runs/20260629_074726Z_full_version_batch_d/real_question_eval_result.json`

## Developer Details

### question-sunflower-house
- Winner: `bge_m3_dense_sparse`
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

#### bge_m3_dense_sparse
- Collection: `eternal_world_rag_chunks__bge_m3_dense_sparse__manual_local_batch_d`
- Matched markers: blue gate latch, sunflower seeds
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue gate latch, sunflower seeds.
- Verdict: grounded

#### bge_m3_dense_sparse_multivector
- Collection: `eternal_world_rag_chunks__bge_m3_dense_sparse_multivector__manual_local_batch_d`
- Matched markers: blue gate latch, sunflower seeds
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue gate latch, sunflower seeds.
- Verdict: grounded

### question-winter-trip
- Winner: `bge_m3_dense_sparse_multivector`
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

#### bge_m3_dense_sparse
- Collection: `eternal_world_rag_chunks__bge_m3_dense_sparse__manual_local_batch_d`
- Matched markers: overnight train ticket, wooden thermos
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: overnight train ticket, wooden thermos.
- Verdict: grounded

#### bge_m3_dense_sparse_multivector
- Collection: `eternal_world_rag_chunks__bge_m3_dense_sparse_multivector__manual_local_batch_d`
- Matched markers: overnight train ticket, wooden thermos
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: overnight train ticket, wooden thermos.
- Verdict: grounded

### question-grandmother-soup
- Winner: `bge_m3_dense_sparse`
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

#### bge_m3_dense_sparse
- Collection: `eternal_world_rag_chunks__bge_m3_dense_sparse__manual_local_batch_d`
- Matched markers: dried mushrooms, oak stove
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: dried mushrooms, oak stove.
- Verdict: grounded

#### bge_m3_dense_sparse_multivector
- Collection: `eternal_world_rag_chunks__bge_m3_dense_sparse_multivector__manual_local_batch_d`
- Matched markers: dried mushrooms, oak stove
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: dried mushrooms, oak stove.
- Verdict: grounded
