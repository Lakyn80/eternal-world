# Eternal World Distractor Real Eval Aggregate Report

Generated at: `2026-07-03T22:37:27.489627+00:00`
Artifact root: `artifacts/real_question_eval/eternal_world_distractor_full_benchmark`
Dataset: `Eternal World Distractor Validation V1` (`eternal-world-distractor-v1`)

## Completed Stages
- `base_real_eval`: COMPLETED | run `20260703_162457Z` | quality `PASS` | winner `bge_m3` | artifact `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/latest_real`
- `incremental_new_providers`: COMPLETED | run `20260703_172002Z` | quality `FAIL` | winner `bge_m3` | artifact `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/latest_incremental_new_providers`
- `full_version_batch_a`: COMPLETED | run `20260703_182938Z` | quality `PASS` | winner `multilingual_e5_large` | artifact `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/latest_full_version_batch_a`
- `full_version_batch_b`: COMPLETED | run `20260703_185340Z` | quality `PASS` | winner `qwen3_embedding_0_6b` | artifact `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/latest_full_version_batch_b`
- `full_version_batch_c`: COMPLETED | run `20260703_191345Z` | quality `PASS` | winner `jina_embeddings_v3` | artifact `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/latest_full_version_batch_c`
- `full_version_batch_d`: COMPLETED | run `20260703_205145Z` | quality `PASS` | winner `bge_m3_dense_sparse` | artifact `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/latest_full_version_batch_d`

## Final Ranking From Available Results
| rank | model | passed | total | pass_rate | coverage | missing | distractors | latency_ms |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | `bge_m3` | 85 | 100 | 0.8500 | 0.9550 | 9 | 5 | 419.7 |
| 2 | `multilingual_e5_large` | 84 | 100 | 0.8400 | 0.9650 | 7 | 5 | 471.1 |
| 3 | `bge_m3_dense_sparse` | 84 | 100 | 0.8400 | 0.9400 | 12 | 3 | 496.6 |
| 4 | `bge_m3_dense_sparse_multivector` | 83 | 100 | 0.8300 | 0.9550 | 9 | 7 | 13567.7 |
| 5 | `jina_embeddings_v3` | 82 | 100 | 0.8200 | 0.9800 | 4 | 7 | 331.9 |
| 6 | `qwen3_embedding_0_6b` | 82 | 100 | 0.8200 | 0.9750 | 5 | 10 | 420.1 |
| 7 | `paraphrase_multilingual_mpnet_base_v2` | 76 | 100 | 0.7600 | 0.8800 | 24 | 0 | 222.7 |
| 8 | `multilingual_e5_base` | 72 | 100 | 0.7200 | 0.9200 | 16 | 0 | 212.3 |
| 9 | `multilingual_e5_small` | 69 | 100 | 0.6900 | 0.9800 | 4 | 23 | 1519.6 |

## Acceptance Verdict
- Available-results gate: `PASS`
- Best available model bge_m3 passed 85/100 (0.8500).
- Full benchmark completion: `COMPLETE`
- All repository-supported real local providers are accounted for.

## Missing Or Skipped Configs
- `excluded_config` / `mock_embedding`: SKIPPED - Mock embedding is a test/dev provider and is not a real local model benchmark candidate.
- `full_version_batch_e` / `qwen3_embedding_4b`: OOM - Log contains out-of-memory evidence. See log `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/run_logs/batch_e_qwen3_embedding_4b.log`.
- `full_version_batch_f` / `qwen3_embedding_8b`: OOM - Log contains out-of-memory evidence. See log `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/run_logs/batch_f_qwen3_embedding_8b.log`.

## Run Logs

- `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/run_logs/batch_a_multilingual_e5_large.log` (287647 bytes)
- `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/run_logs/batch_b_qwen3_embedding_0_6b.log` (565470 bytes)
- `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/run_logs/batch_c_jina_embeddings_v3.log` (565124 bytes)
- `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/run_logs/batch_d_bge_m3_hybrid.log` (45268 bytes)
- `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/run_logs/batch_d_bge_m3_hybrid_retry.log` (344137 bytes)
- `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/run_logs/batch_d_bge_m3_hybrid_retry2.log` (394756 bytes)
- `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/run_logs/batch_e_qwen3_embedding_4b.log` (1393 bytes)
- `artifacts/real_question_eval/eternal_world_distractor_full_benchmark/run_logs/batch_f_qwen3_embedding_8b.log` (915 bytes)

## Notes
- Existing completed base/incremental artifacts were preserved; only missing batch stages were executed in this pass.
