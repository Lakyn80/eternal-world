# Real Question Eval Summary

## Run
- Run ID: `20260703_191345Z`
- Created: `2026-07-03T19:13:45.098906+00:00`
- Mode: `full_version_batch_c_real_eval`
- Dataset: `Eternal World Distractor Validation V1`
- Dataset ID: `eternal-world-distractor-v1`
- Dataset file: `/app/app/modules/real_question_eval/datasets/eternal_world_distractor_v1.json`
- Run status: `COMPLETED`
- Quality status: `PASS`
- Quality gate: `n/a >= n/a`
- Overall winner: `jina_embeddings_v3`
- Overall winner reason: `n/a`
- Preflight validation: `n/a`
- Preflight missing marker count: `n/a`
- Total questions: `100`

## Model Results

| model | status | passed | total | pass_rate | coverage | missing | distractors | latency_ms | winner |
|---|---|---|---|---|---|---|---|---|---|
| multilingual_e5_base | FAIL | 72 | 100 | 0.7200 | 0.9200 | 16 | 0 | 212.3 | no |
| jina_embeddings_v3 | FAIL | 82 | 100 | 0.8200 | 0.9800 | 4 | 7 | 331.9 | yes |

## Question Results

| question_id | test_type | model | status | coverage | missing | forbidden_hits | distractors | latency_ms |
|---|---|---|---|---|---|---|---|---|
| distractor-twin-innkeepers | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-twin-innkeepers | distractor | jina_embeddings_v3 | FAIL | 1.0000 | none | Marta of River Inn | Marta of River Inn | n/a |
| distractor-june-market-date | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-june-market-date | distractor | jina_embeddings_v3 | FAIL | 1.0000 | none | June 4 noon market | June 4 noon market | n/a |
| distractor-two-levs | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-two-levs | distractor | jina_embeddings_v3 | FAIL | 1.0000 | none | Lev the ferryman | Lev the ferryman | n/a |
| distractor-similar-islands | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-similar-islands | distractor | jina_embeddings_v3 | FAIL | 1.0000 | none | Fox Island ferry shed | Fox Island ferry shed | n/a |
| distractor-letter-mixup | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-letter-mixup | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-006 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 16 Bellwater Fair | none | none | n/a |
| distractor-006 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-007 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-007 | distractor | jina_embeddings_v3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-008 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-008 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-009 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-009 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-010 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-010 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-011 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-011 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-012 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-012 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-013 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-013 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-014 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-014 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-015 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-015 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-016 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-016 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-017 | distractor | multilingual_e5_base | FAIL | 0.0000 | Moon Mill yard, glass ink bottle | none | none | n/a |
| distractor-017 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-018 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-018 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-019 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-019 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-020 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-020 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-021 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-021 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-022 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-022 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-023 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-023 | distractor | jina_embeddings_v3 | FAIL | 1.0000 | none | clay watering cup | clay watering cup | n/a |
| distractor-024 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-024 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-025 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-025 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-026 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 18 Bellwater Fair | none | none | n/a |
| distractor-026 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-027 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-027 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-028 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-028 | distractor | jina_embeddings_v3 | FAIL | 1.0000 | none | star ledger page | star ledger page | n/a |
| distractor-029 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-029 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-030 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-030 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-031 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 23 Bellwater Fair | none | none | n/a |
| distractor-031 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-032 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-032 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-033 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-033 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-034 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-034 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-035 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-035 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-036 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 10 Bellwater Fair | none | none | n/a |
| distractor-036 | distractor | jina_embeddings_v3 | FAIL | 0.5000 | March 10 Bellwater Fair | none | none | n/a |
| distractor-037 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-037 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-038 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-038 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-039 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-039 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-040 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-040 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-041 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 15 Bellwater Fair | none | none | n/a |
| distractor-041 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-042 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-042 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-043 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-043 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-044 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-044 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-045 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-045 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-046 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 20 Bellwater Fair | none | none | n/a |
| distractor-046 | distractor | jina_embeddings_v3 | FAIL | 0.5000 | March 20 Bellwater Fair | none | none | n/a |
| distractor-047 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-047 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-048 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-048 | distractor | jina_embeddings_v3 | FAIL | 1.0000 | none | birch tea flask | birch tea flask | n/a |
| distractor-049 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-049 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-050 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-050 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-051 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-051 | distractor | jina_embeddings_v3 | FAIL | 0.5000 | March 25 Bellwater Fair | none | none | n/a |
| distractor-052 | distractor | multilingual_e5_base | FAIL | 0.0000 | Blue Trunk cabin, violet ribbon | none | none | n/a |
| distractor-052 | distractor | jina_embeddings_v3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-053 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-053 | distractor | jina_embeddings_v3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-054 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-054 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-055 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-055 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-056 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 12 Bellwater Fair | none | none | n/a |
| distractor-056 | distractor | jina_embeddings_v3 | FAIL | 0.5000 | March 12 Bellwater Fair | none | none | n/a |
| distractor-057 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-057 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-058 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-058 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-059 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-059 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-060 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-060 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-061 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-061 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-062 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-062 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-063 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-063 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-064 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-064 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-065 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-065 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-066 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 22 Bellwater Fair | none | none | n/a |
| distractor-066 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-067 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-067 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-068 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-068 | distractor | jina_embeddings_v3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-069 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-069 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-070 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-070 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-071 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-071 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-072 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-072 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-073 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-073 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-074 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-074 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-075 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-075 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-076 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 14 Bellwater Fair | none | none | n/a |
| distractor-076 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-077 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-077 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-078 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-078 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-079 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-079 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-080 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-080 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-081 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-081 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-082 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-082 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-083 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-083 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-084 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-084 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-085 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-085 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-086 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 24 Bellwater Fair | none | none | n/a |
| distractor-086 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-087 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-087 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-088 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-088 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-089 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-089 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-090 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-090 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-091 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 11 Bellwater Fair | none | none | n/a |
| distractor-091 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-092 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-092 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-093 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-093 | distractor | jina_embeddings_v3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-094 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-094 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-095 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-095 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-096 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 16 Bellwater Fair | none | none | n/a |
| distractor-096 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-097 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-097 | distractor | jina_embeddings_v3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-098 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-098 | distractor | jina_embeddings_v3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-099 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-099 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-100 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-100 | distractor | jina_embeddings_v3 | PASS | 1.0000 | none | none | none | n/a |
