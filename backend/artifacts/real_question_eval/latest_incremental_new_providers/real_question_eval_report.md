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
- Recommended active model: `multilingual_e5_base`
- Speed vs accuracy tradeoff: Historical multilingual_e5_small and bge_m3 results were preserved and compared against the two new real-provider runs using the same dataset and selector rules.
- Production recommendation: A new provider beat historical `bge_m3`; promote `multilingual_e5_base` after reviewing the incremental real comparison.
- Timestamp: 2026-06-25T18:10:27.590404+00:00
- Run type: `incremental_real`
- Historical baseline providers:
  - `multilingual_e5_small`
  - `bge_m3`
- New real run providers:
  - `paraphrase_multilingual_mpnet_base_v2`
  - `multilingual_e5_base`
- Historical overall winner: `bge_m3`
- Any new provider beat historical bge_m3: `true`

## Artifact Files
- Latest Markdown: `artifacts\real_question_eval\latest_incremental_new_providers\real_question_eval_report.md`
- Latest JSON: `artifacts\real_question_eval\latest_incremental_new_providers\real_question_eval_result.json`
- Archived Markdown: `artifacts\real_question_eval\runs\20260625_181027Z_incremental_new_providers\real_question_eval_report.md`
- Archived JSON: `artifacts\real_question_eval\runs\20260625_181027Z_incremental_new_providers\real_question_eval_result.json`

## Client Question Breakdown
### Question 1 - question-sunflower-house
Question: What details show which flower was kept at the old village house and what part of the entrance is mentioned?
- Final evaluated answer: Grounded by retrieved evidence for: blue gate latch, sunflower seeds.
- Correctness verdict: grounded
- Evidence used: blue gate latch, sunflower seeds
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_small`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- sunflower seeds
- blue gate latch

Expected distractors:
- rose market poster

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=blue gate latch, sunflower seeds missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=blue gate latch, sunflower seeds missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=blue gate latch, sunflower seeds missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=blue gate latch, sunflower seeds missing=none distractors=none

### Question 2 - question-winter-trip
Question: During the winter trip, what travel item was saved and what container kept everyone warm?
- Final evaluated answer: Grounded by retrieved evidence for: overnight train ticket, wooden thermos.
- Correctness verdict: grounded
- Evidence used: overnight train ticket, wooden thermos
- Model comparison: multilingual_e5_small -> verdict=grounded coverage=1.0; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=grounded coverage=1.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: lower retrieval score despite comparable evidence
- Distractors / false positives: none

Expected evidence:
- overnight train ticket
- wooden thermos

Expected distractors:
- summer bus timetable

- Model verdicts:
  - `multilingual_e5_small`: verdict=grounded coverage=1.0 matched=overnight train ticket, wooden thermos missing=none distractors=none
  - `bge_m3`: verdict=grounded coverage=1.0 matched=overnight train ticket, wooden thermos missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=grounded coverage=1.0 matched=overnight train ticket, wooden thermos missing=none distractors=none
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=overnight train ticket, wooden thermos missing=none distractors=none

### Question 3 - question-grandmother-soup
Question: Which ingredients and cooking setup explain why grandmother's soup tasted smoky?
- Final evaluated answer: Grounded by retrieved evidence for: dried mushrooms, oak stove.
- Correctness verdict: grounded
- Evidence used: dried mushrooms, oak stove
- Model comparison: multilingual_e5_small -> verdict=partial coverage=0.5; bge_m3 -> verdict=grounded coverage=1.0; paraphrase_multilingual_mpnet_base_v2 -> verdict=distracted coverage=0.0; multilingual_e5_base -> verdict=grounded coverage=1.0
- Winner: `multilingual_e5_base`
- Why it won: Tie broken by stronger top retrieval score and overall selector alignment.
- What the losing model missed or got wrong: missing oak stove; distractors vanilla jam
- Distractors / false positives: vanilla jam

Expected evidence:
- dried mushrooms
- oak stove

Expected distractors:
- vanilla jam

- Model verdicts:
  - `multilingual_e5_small`: verdict=partial coverage=0.5 matched=dried mushrooms missing=oak stove distractors=vanilla jam
  - `bge_m3`: verdict=grounded coverage=1.0 matched=dried mushrooms, oak stove missing=none distractors=none
  - `paraphrase_multilingual_mpnet_base_v2`: verdict=distracted coverage=0.0 matched=none missing=dried mushrooms, oak stove distractors=vanilla jam
  - `multilingual_e5_base`: verdict=grounded coverage=1.0 matched=dried mushrooms, oak stove missing=none distractors=none

## Aggregate Client Decision
- Recommended active model: `multilingual_e5_base`
- Overall winner: `multilingual_e5_base`
- Activation state: `false`
- Runtime retrieval verified: `false`
- Production recommendation: A new provider beat historical `bge_m3`; promote `multilingual_e5_base` after reviewing the incremental real comparison.

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

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval`
- Top chunks:
  1. score=0.530441 chunk_id=7 preview=The old village house kept a paper envelope of sunflower seeds beneath the porch bench so spring planting would not be forgotten. Sunflower section archive s...
  2. score=0.349074 chunk_id=8 preview=Sunflower section archive sentence 6 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. Every...
- Matched markers: blue gate latch, sunflower seeds
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: blue gate latch, sunflower seeds.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval`
- Top chunks:
  1. score=0.816151 chunk_id=7 preview=The old village house kept a paper envelope of sunflower seeds beneath the porch bench so spring planting would not be forgotten. Sunflower section archive s...
  2. score=0.766324 chunk_id=8 preview=Sunflower section archive sentence 6 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. Every...
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

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval`
- Top chunks:
  1. score=0.479226 chunk_id=10 preview=Winter ticket section archive sentence 4 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. W...
  2. score=0.469697 chunk_id=9 preview=Gate section archive sentence 5 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. Gate secti...
- Matched markers: overnight train ticket, wooden thermos
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: overnight train ticket, wooden thermos.
- Verdict: grounded

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval`
- Top chunks:
  1. score=0.831914 chunk_id=9 preview=Gate section archive sentence 5 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. Gate secti...
  2. score=0.826785 chunk_id=10 preview=Winter ticket section archive sentence 4 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. W...
- Matched markers: overnight train ticket, wooden thermos
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: overnight train ticket, wooden thermos.
- Verdict: grounded

- Winner:
  - `multilingual_e5_base`
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

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval`
- Top chunks:
  1. score=0.246899 chunk_id=7 preview=The old village house kept a paper envelope of sunflower seeds beneath the porch bench so spring planting would not be forgotten. Sunflower section archive s...
  2. score=0.241664 chunk_id=13 preview=Stove section archive sentence 1 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. Stove sec...
- Matched markers: none
- Missing markers: dried mushrooms, oak stove
- Distractors: vanilla jam
- Evidence coverage: 0.0
- First relevant rank: n/a
- Answer summary: Ungrounded. Retrieved distractors: vanilla jam.
- Verdict: distracted

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval`
- Top chunks:
  1. score=0.851768 chunk_id=11 preview=Winter thermos section archive sentence 3 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details....
  2. score=0.818127 chunk_id=12 preview=Mushroom section archive sentence 2 keeps the fictional diary section long enough for chunk separation while repeating only safe non-personal details. Mushro...
- Matched markers: dried mushrooms, oak stove
- Missing markers: none
- Distractors: none
- Evidence coverage: 1.0
- First relevant rank: 1
- Answer summary: Grounded by retrieved evidence for: dried mushrooms, oak stove.
- Verdict: grounded

- Winner:
  - `multilingual_e5_base`
  - Tie broken by stronger top retrieval score and overall selector alignment.

### Aggregate Results

#### multilingual_e5_small
- Collection: `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval`
- Question wins: 1
- Passed questions: 2
- Average evidence coverage: 0.8333
- Average first relevant rank: 1.0
- Total matched markers: 5
- Total missing markers: 1
- Total false-positive markers: 1
- Official metrics: {'hit_rate': 0.6666666666666666, 'recall_at_k': 0.8333333333333334, 'mrr': 1.0, 'forbidden_marker_rate': 0.16666666666666666, 'average_latency_ms': 7182.6410000000005, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.8333333333333334, 'missing_expected_marker_count': 1, 'false_positive_count': 1}

#### bge_m3
- Collection: `eternal_world_rag_chunks__bge_m3__real_question_eval`
- Question wins: 0
- Passed questions: 3
- Average evidence coverage: 1.0
- Average first relevant rank: 1.0
- Total matched markers: 6
- Total missing markers: 0
- Total false-positive markers: 0
- Official metrics: {'hit_rate': 1.0, 'recall_at_k': 1.0, 'mrr': 1.0, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 15471.300333333333, 'cost_estimate_total': None, 'evidence_marker_coverage': 1.0, 'missing_expected_marker_count': 0, 'false_positive_count': 0}

#### paraphrase_multilingual_mpnet_base_v2
- Collection: `eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval`
- Question wins: 0
- Passed questions: 2
- Average evidence coverage: 0.6667
- Average first relevant rank: 1.0
- Total matched markers: 4
- Total missing markers: 2
- Total false-positive markers: 1
- Official metrics: {'hit_rate': 0.6666666666666666, 'recall_at_k': 0.6666666666666666, 'mrr': 0.6666666666666666, 'forbidden_marker_rate': 0.16666666666666666, 'average_latency_ms': 7066.420333333333, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.6666666666666666, 'missing_expected_marker_count': 2, 'false_positive_count': 2}

#### multilingual_e5_base
- Collection: `eternal_world_rag_chunks__multilingual_e5_base__real_question_eval`
- Question wins: 2
- Passed questions: 3
- Average evidence coverage: 1.0
- Average first relevant rank: 1.0
- Total matched markers: 6
- Total missing markers: 0
- Total false-positive markers: 0
- Official metrics: {'hit_rate': 1.0, 'recall_at_k': 1.0, 'mrr': 1.0, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 7938.929, 'cost_estimate_total': None, 'evidence_marker_coverage': 1.0, 'missing_expected_marker_count': 0, 'false_positive_count': 0}

### Runtime Activation
- Selected config: {'best_config_id': 'multilingual_e5_base', 'best_model_code': 'multilingual_e5_base', 'best_collection_name': 'eternal_world_rag_chunks__multilingual_e5_base__real_question_eval', 'selected_metrics': {'hit_rate': 1.0, 'recall_at_k': 1.0, 'mrr': 1.0, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 7938.929, 'cost_estimate_total': None, 'evidence_marker_coverage': 1.0, 'missing_expected_marker_count': 0, 'false_positive_count': 0}, 'all_config_scores': [{'config_id': 'multilingual_e5_base', 'model_code': 'multilingual_e5_base', 'collection_name': 'eternal_world_rag_chunks__multilingual_e5_base__real_question_eval', 'metrics': {'hit_rate': 1.0, 'recall_at_k': 1.0, 'mrr': 1.0, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 7938.929, 'cost_estimate_total': None, 'evidence_marker_coverage': 1.0, 'missing_expected_marker_count': 0, 'false_positive_count': 0}, 'acceptable_latency': True, 'acceptable_cost': True, 'ranking_factors': {'hit_rate': 1.0, 'evidence_marker_coverage': 1.0, 'recall_at_k': 1.0, 'mrr': 1.0, 'forbidden_marker_rate': 0.0, 'acceptable_latency': True, 'acceptable_cost': True, 'average_latency_ms': 7938.929, 'cost_estimate_total': None}, 'reasons': ['hit_rate=1.000', 'evidence_marker_coverage=1.000', 'recall_at_k=1.000', 'mrr=1.000', 'forbidden_marker_rate=0.000'], 'warnings': []}, {'config_id': 'bge_m3', 'model_code': 'bge_m3', 'collection_name': 'eternal_world_rag_chunks__bge_m3__real_question_eval', 'metrics': {'hit_rate': 1.0, 'recall_at_k': 1.0, 'mrr': 1.0, 'forbidden_marker_rate': 0.0, 'average_latency_ms': 15471.300333333333, 'cost_estimate_total': None, 'evidence_marker_coverage': 1.0, 'missing_expected_marker_count': 0, 'false_positive_count': 0}, 'acceptable_latency': True, 'acceptable_cost': True, 'ranking_factors': {'hit_rate': 1.0, 'evidence_marker_coverage': 1.0, 'recall_at_k': 1.0, 'mrr': 1.0, 'forbidden_marker_rate': 0.0, 'acceptable_latency': True, 'acceptable_cost': True, 'average_latency_ms': 15471.300333333333, 'cost_estimate_total': None}, 'reasons': ['hit_rate=1.000', 'evidence_marker_coverage=1.000', 'recall_at_k=1.000', 'mrr=1.000', 'forbidden_marker_rate=0.000'], 'warnings': []}, {'config_id': 'multilingual_e5_small', 'model_code': 'multilingual_e5_small', 'collection_name': 'eternal_world_rag_chunks__multilingual_e5_small__real_question_eval', 'metrics': {'hit_rate': 0.6666666666666666, 'recall_at_k': 0.8333333333333334, 'mrr': 1.0, 'forbidden_marker_rate': 0.16666666666666666, 'average_latency_ms': 7182.6410000000005, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.8333333333333334, 'missing_expected_marker_count': 1, 'false_positive_count': 1}, 'acceptable_latency': True, 'acceptable_cost': True, 'ranking_factors': {'hit_rate': 0.6666666666666666, 'evidence_marker_coverage': 0.8333333333333334, 'recall_at_k': 0.8333333333333334, 'mrr': 1.0, 'forbidden_marker_rate': 0.16666666666666666, 'acceptable_latency': True, 'acceptable_cost': True, 'average_latency_ms': 7182.6410000000005, 'cost_estimate_total': None}, 'reasons': ['hit_rate=0.667', 'evidence_marker_coverage=0.833', 'recall_at_k=0.833', 'mrr=1.000', 'forbidden_marker_rate=0.167'], 'warnings': []}, {'config_id': 'paraphrase_multilingual_mpnet_base_v2', 'model_code': 'paraphrase_multilingual_mpnet_base_v2', 'collection_name': 'eternal_world_rag_chunks__paraphrase_multilingual_mpnet_base_v2__real_question_eval', 'metrics': {'hit_rate': 0.6666666666666666, 'recall_at_k': 0.6666666666666666, 'mrr': 0.6666666666666666, 'forbidden_marker_rate': 0.16666666666666666, 'average_latency_ms': 7066.420333333333, 'cost_estimate_total': None, 'evidence_marker_coverage': 0.6666666666666666, 'missing_expected_marker_count': 2, 'false_positive_count': 2}, 'acceptable_latency': True, 'acceptable_cost': True, 'ranking_factors': {'hit_rate': 0.6666666666666666, 'evidence_marker_coverage': 0.6666666666666666, 'recall_at_k': 0.6666666666666666, 'mrr': 0.6666666666666666, 'forbidden_marker_rate': 0.16666666666666666, 'acceptable_latency': True, 'acceptable_cost': True, 'average_latency_ms': 7066.420333333333, 'cost_estimate_total': None}, 'reasons': ['hit_rate=0.667', 'evidence_marker_coverage=0.667', 'recall_at_k=0.667', 'mrr=0.667', 'forbidden_marker_rate=0.167'], 'warnings': []}], 'reasons': ['Selection order: hit_rate/evidence marker coverage, recall_at_k, MRR, safety, latency, cost.'], 'warnings': []}
- Activated config: {}
- Runtime retrieval verification: {}
