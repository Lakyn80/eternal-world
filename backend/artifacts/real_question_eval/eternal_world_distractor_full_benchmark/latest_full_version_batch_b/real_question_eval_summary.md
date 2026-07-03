# Real Question Eval Summary

## Run
- Run ID: `20260703_185340Z`
- Created: `2026-07-03T18:53:40.657850+00:00`
- Mode: `full_version_batch_b_real_eval`
- Dataset: `Eternal World Distractor Validation V1`
- Dataset ID: `eternal-world-distractor-v1`
- Dataset file: `/app/app/modules/real_question_eval/datasets/eternal_world_distractor_v1.json`
- Run status: `COMPLETED`
- Quality status: `PASS`
- Quality gate: `n/a >= n/a`
- Overall winner: `qwen3_embedding_0_6b`
- Overall winner reason: `n/a`
- Preflight validation: `n/a`
- Preflight missing marker count: `n/a`
- Total questions: `100`

## Model Results

| model | status | passed | total | pass_rate | coverage | missing | distractors | latency_ms | winner |
|---|---|---|---|---|---|---|---|---|---|
| multilingual_e5_base | FAIL | 72 | 100 | 0.7200 | 0.9200 | 16 | 0 | 212.3 | no |
| qwen3_embedding_0_6b | FAIL | 82 | 100 | 0.8200 | 0.9750 | 5 | 10 | 420.1 | yes |

## Question Results

| question_id | test_type | model | status | coverage | missing | forbidden_hits | distractors | latency_ms |
|---|---|---|---|---|---|---|---|---|
| distractor-twin-innkeepers | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-twin-innkeepers | distractor | qwen3_embedding_0_6b | FAIL | 1.0000 | none | Marta of River Inn | Marta of River Inn | n/a |
| distractor-june-market-date | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-june-market-date | distractor | qwen3_embedding_0_6b | FAIL | 1.0000 | none | June 4 noon market | June 4 noon market | n/a |
| distractor-two-levs | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-two-levs | distractor | qwen3_embedding_0_6b | FAIL | 1.0000 | none | Lev the ferryman | Lev the ferryman | n/a |
| distractor-similar-islands | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-similar-islands | distractor | qwen3_embedding_0_6b | FAIL | 1.0000 | none | Fox Island ferry shed | Fox Island ferry shed | n/a |
| distractor-letter-mixup | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-letter-mixup | distractor | qwen3_embedding_0_6b | FAIL | 1.0000 | none | Alda's spring letter | Alda's spring letter | n/a |
| distractor-006 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 16 Bellwater Fair | none | none | n/a |
| distractor-006 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-007 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-007 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-008 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-008 | distractor | qwen3_embedding_0_6b | FAIL | 1.0000 | none | tuning fork | tuning fork | n/a |
| distractor-009 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-009 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-010 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-010 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-011 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-011 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-012 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-012 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-013 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-013 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-014 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-014 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-015 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-015 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-016 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-016 | distractor | qwen3_embedding_0_6b | FAIL | 0.5000 | March 26 Bellwater Fair | none | none | n/a |
| distractor-017 | distractor | multilingual_e5_base | FAIL | 0.0000 | Moon Mill yard, glass ink bottle | none | none | n/a |
| distractor-017 | distractor | qwen3_embedding_0_6b | FAIL | 1.0000 | none | none | none | n/a |
| distractor-018 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-018 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-019 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-019 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-020 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-020 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-021 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-021 | distractor | qwen3_embedding_0_6b | FAIL | 0.5000 | March 13 Bellwater Fair | none | none | n/a |
| distractor-022 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-022 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-023 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-023 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-024 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-024 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-025 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-025 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-026 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 18 Bellwater Fair | none | none | n/a |
| distractor-026 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-027 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-027 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-028 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-028 | distractor | qwen3_embedding_0_6b | FAIL | 1.0000 | none | star ledger page | star ledger page | n/a |
| distractor-029 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-029 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-030 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-030 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-031 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 23 Bellwater Fair | none | none | n/a |
| distractor-031 | distractor | qwen3_embedding_0_6b | FAIL | 0.5000 | March 23 Bellwater Fair | none | none | n/a |
| distractor-032 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-032 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-033 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-033 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-034 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-034 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-035 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-035 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-036 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 10 Bellwater Fair | none | none | n/a |
| distractor-036 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-037 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-037 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-038 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-038 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-039 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-039 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-040 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-040 | distractor | qwen3_embedding_0_6b | FAIL | 1.0000 | none | Tomas of Birch Ferry shed | Tomas of Birch Ferry shed | n/a |
| distractor-041 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 15 Bellwater Fair | none | none | n/a |
| distractor-041 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-042 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-042 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-043 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-043 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-044 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-044 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-045 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-045 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-046 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 20 Bellwater Fair | none | none | n/a |
| distractor-046 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-047 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-047 | distractor | qwen3_embedding_0_6b | FAIL | 1.0000 | none | none | none | n/a |
| distractor-048 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-048 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-049 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-049 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-050 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-050 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-051 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-051 | distractor | qwen3_embedding_0_6b | FAIL | 0.5000 | March 25 Bellwater Fair | none | none | n/a |
| distractor-052 | distractor | multilingual_e5_base | FAIL | 0.0000 | Blue Trunk cabin, violet ribbon | none | none | n/a |
| distractor-052 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-053 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-053 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-054 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-054 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-055 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-055 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-056 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 12 Bellwater Fair | none | none | n/a |
| distractor-056 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-057 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-057 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-058 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-058 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-059 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-059 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-060 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-060 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-061 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-061 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-062 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-062 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-063 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-063 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-064 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-064 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-065 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-065 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-066 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 22 Bellwater Fair | none | none | n/a |
| distractor-066 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-067 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-067 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-068 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-068 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-069 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-069 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-070 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-070 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-071 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-071 | distractor | qwen3_embedding_0_6b | FAIL | 0.5000 | March 27 Bellwater Fair | none | none | n/a |
| distractor-072 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-072 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-073 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-073 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-074 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-074 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-075 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-075 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-076 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 14 Bellwater Fair | none | none | n/a |
| distractor-076 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-077 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-077 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-078 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-078 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-079 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-079 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-080 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-080 | distractor | qwen3_embedding_0_6b | FAIL | 1.0000 | none | Tomas of Star Basin gallery | Tomas of Star Basin gallery | n/a |
| distractor-081 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-081 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-082 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-082 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-083 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-083 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-084 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-084 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-085 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-085 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-086 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 24 Bellwater Fair | none | none | n/a |
| distractor-086 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-087 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-087 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-088 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-088 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-089 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-089 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-090 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-090 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-091 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 11 Bellwater Fair | none | none | n/a |
| distractor-091 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-092 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-092 | distractor | qwen3_embedding_0_6b | FAIL | 1.0000 | none | none | none | n/a |
| distractor-093 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-093 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-094 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-094 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-095 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-095 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-096 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 16 Bellwater Fair | none | none | n/a |
| distractor-096 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-097 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-097 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-098 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-098 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-099 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-099 | distractor | qwen3_embedding_0_6b | PASS | 1.0000 | none | none | none | n/a |
| distractor-100 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-100 | distractor | qwen3_embedding_0_6b | FAIL | 1.0000 | none | Nikola of Birch Ferry shed | Nikola of Birch Ferry shed | n/a |
