# Real Question Evaluation Report

## Client Summary
- Source dataset: deterministic fictional eval corpus
- Real client/user data: no
- Purpose: retrieval quality testing
- Models compared:
  - `multilingual_e5_small`
  - `bge_m3`
- Run type: `real`
- Used fake models: `false`
- Recommended active model: `bge_m3`
- Production recommendation: bge_m3 is safer for evidence-based retrieval because it had full evidence coverage, zero missing markers, and zero distractors.
- Speed vs accuracy tradeoff: multilingual_e5_small was faster and won two simple questions by score tie-break, but bge_m3 was more complete and safer.
- Overall winner: `bge_m3`
- Activated: `true`
- Runtime retrieval verified: `true`
- Timestamp: 2026-06-25T12:27:32.747249+00:00

## Artifact Files
- Latest Markdown: `/app/artifacts/real_question_eval/latest_real/real_question_eval_report.md`
- Latest JSON: `/app/artifacts/real_question_eval/latest_real/real_question_eval_result.json`
- Archived Markdown: `/app/artifacts/real_question_eval/runs/20260625_122732Z_real/real_question_eval_report.md`
- Archived JSON: `/app/artifacts/real_question_eval/runs/20260625_122732Z_real/real_question_eval_result.json`

## Client Question Breakdown
### Question 1 - question-sunflower-house
Question: What details show which flower was kept at the old village house and what part of the entrance is mentioned?
- Final evaluated answer: The old village house kept sunflower seeds, and the entrance detail was the blue gate latch.
- Correctness verdict: grounded
- Evidence used: sunflower seeds; blue gate latch
- Model comparison: Both models were grounded; multilingual_e5_small won on stronger top retrieval score.
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: No evidence gap; it lost only on top retrieval score tie-break.
- Distractors / false positives: none

Expected evidence:
- sunflower seeds
- blue gate latch

Expected distractors:
- rose market poster

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue gate latch, sunflower seeds missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue gate latch, sunflower seeds missing=none distractors=none

### Question 2 - question-winter-trip
Question: During the winter trip, what travel item was saved and what container kept everyone warm?
- Final evaluated answer: The saved travel item was an overnight train ticket, and the container that kept everyone warm was a wooden thermos.
- Correctness verdict: grounded
- Evidence used: overnight train ticket; wooden thermos
- Model comparison: Both models were grounded; multilingual_e5_small won on stronger top retrieval score.
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: No evidence gap; it lost only on top retrieval score tie-break.
- Distractors / false positives: none

Expected evidence:
- overnight train ticket
- wooden thermos

Expected distractors:
- summer bus timetable

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=overnight train ticket, wooden thermos missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=overnight train ticket, wooden thermos missing=none distractors=none

### Question 3 - question-grandmother-soup
Question: Which ingredients and cooking setup explain why grandmother's soup tasted smoky?
- Final evaluated answer: Grandmother's soup tasted smoky because it used dried mushrooms and was cooked on an oak stove.
- Correctness verdict: grounded
- Evidence used: dried mushrooms; oak stove
- Model comparison: bge_m3 was grounded; multilingual_e5_small was partial.
- Winner: `bge_m3`
- Why it won: Higher evidence coverage (1.00 vs 0.50).
- What the losing model missed or got wrong: multilingual_e5_small missed oak stove and retrieved the vanilla jam distractor.
- Distractors / false positives: vanilla jam

Expected evidence:
- dried mushrooms
- oak stove

Expected distractors:
- vanilla jam

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=dried mushrooms missing=oak stove distractors=vanilla jam
  - `bge_m3`: verdict=grounded coverage=1.0 matched=dried mushrooms, oak stove missing=none distractors=none

## Aggregate Client Decision
- Recommended active model: `bge_m3`
- Overall winner: `bge_m3`
- Activation state: `true`
- Runtime retrieval verified: `true`
- Production recommendation: bge_m3 is safer for evidence-based retrieval because it had full evidence coverage, zero missing markers, and zero distractors.

## Developer Details

### Question 1 - question-sunflower-house
Question: What details show which flower was kept at the old village house and what part of the entrance is mentioned?

Expected evidence:
- sunflower seeds
- blue gate latch

Expected distractors:
- rose market poster

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval`
- Top chunks:
  1. score=0.834285 chunk_id=7 preview=The old village house kept a paper envelope of sunflower seeds beneath the porch bench so spring planting would not be forgotten. Sunflower section archive s...
  2. score=0.772903 chunk_id=8 preview=Sunflower section archive sentence 6 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. Every...
- Matched markers: blue gate latch, sunflower seeds
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue gate latch, sunflower seeds.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval`
- Top chunks:
  1. score=0.581808 chunk_id=7 preview=The old village house kept a paper envelope of sunflower seeds beneath the porch bench so spring planting would not be forgotten. Sunflower section archive s...
  2. score=0.471936 chunk_id=8 preview=Sunflower section archive sentence 6 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. Every...
- Matched markers: blue gate latch, sunflower seeds
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue gate latch, sunflower seeds.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 2 - question-winter-trip
Question: During the winter trip, what travel item was saved and what container kept everyone warm?

Expected evidence:
- overnight train ticket
- wooden thermos

Expected distractors:
- summer bus timetable

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval`
- Top chunks:
  1. score=0.828848 chunk_id=9 preview=Gate section archive sentence 5 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. Gate secti...
  2. score=0.824045 chunk_id=10 preview=Winter ticket section archive sentence 4 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. W...
- Matched markers: overnight train ticket, wooden thermos
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: overnight train ticket, wooden thermos.
- Verdict: grounded

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval`
- Top chunks:
  1. score=0.566484 chunk_id=10 preview=Winter ticket section archive sentence 4 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. W...
  2. score=0.548187 chunk_id=9 preview=Gate section archive sentence 5 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. Gate secti...
- Matched markers: overnight train ticket, wooden thermos
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: overnight train ticket, wooden thermos.
- Verdict: grounded

- Winner:
  - `multilingual_e5_small`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Question 3 - question-grandmother-soup
Question: Which ingredients and cooking setup explain why grandmother's soup tasted smoky?

Expected evidence:
- dried mushrooms
- oak stove

Expected distractors:
- vanilla jam

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval`
- Top chunks:
  1. score=0.813236 chunk_id=11 preview=Winter thermos section archive sentence 3 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details....
  2. score=0.802530 chunk_id=13 preview=Stove section archive sentence 1 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. Stove sec...
- Matched markers: dried mushrooms
- Missing markers: oak stove
- Distractors: vanilla jam
- Evidence coverage: 0.5
- First relevant rank: 1
- Answer summary: Partially grounded by: dried mushrooms. Missing: oak stove. Distractors present: vanilla jam.
- Verdict: partial

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval`
- Top chunks:
  1. score=0.509956 chunk_id=11 preview=Winter thermos section archive sentence 3 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details....
  2. score=0.487953 chunk_id=12 preview=Mushroom section archive sentence 2 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. Mushro...
- Matched markers: dried mushrooms, oak stove
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: dried mushrooms, oak stove.
- Verdict: grounded

- Winner:
  - `bge_m3`
  - Higher evidence coverage (1.00 vs 0.50).

### Aggregate Results

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval`
- Question wins: 2
- Passed questions: 2
- Average evidence coverage: 0.8333
- Average first relevant rank: 1.0
- Total matched markers: 5
- Total missing markers: 1
- Total false-positive markers: 1
- Official metrics: {'hit_rate': 0.6666666666666666, 'recall_at_k': 0.8333333333333334, 'mrr': 1.0, 'forbidden_marker_rate': 0.16666666666666666, 'average_latency_ms': 7182.6410000000005, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.8333333333333334, 'missing_expected_marker_count': 1, 'false_positive_count': 1}

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval`
- Question wins: 1
- Passed questions: 3
- Average evidence coverage: 1.0
- Average first relevant rank: 1.0
- Total matched markers: 6
- Total missing markers: 0
- Total false-positive markers: 0
- Official metrics: {'hit_rate': 1.0, 'recall_at_k': 1.0, 'mrr': 1.0, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 15471.300333333333, 'cost_estimate_total': None, 'evidence_marker_coverage': 1.0, 'missing_expected_marker_count': 0, 'false_positive_count': 0}

### Runtime Activation
- Selected config: {'best_config_id': 'bge_m3', 'best_model_code': 'bge_m3', 'best_collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval', 'selected_metrics': {'hit_rate': 1.0, 'recall_at_k': 1.0, 'mrr': 1.0, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 15471.300333333333, 'cost_estimate_total': None, 'evidence_marker_coverage': 1.0, 'missing_expected_marker_count': 0, 'false_positive_count': 0}}
- Activated config: {'id': 2, 'profile_id': 6, 'model_code': 'bge_m3', 'collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval', 'top_k': 2, 'score_threshold': None, 'retrieval_mode': 'hybrid', 'source_eval_job_id': 19, 'source_eval_dataset_id': 'real-question-eval-dataset'}
- Runtime retrieval verification: {'model_code': 'bge_m3', 'result_count': 2, 'qdrant_collection': 'eternal_world_rag_chunks__bge_m3__real_question_eval', 'top_chunk_id': 7}
