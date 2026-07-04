# Real Question Eval Summary

## Run
- Run ID: `20260703_140427Z`
- Created: `2026-07-03T14:04:27.955121+00:00`
- Mode: `fake_eval`
- Dataset: `Eternal World Distractor Validation V1`
- Dataset ID: `eternal-world-distractor-v1`
- Dataset file: `/app/app/modules/real_question_eval/datasets/eternal_world_distractor_v1.json`
- Run status: `COMPLETED`
- Quality status: `PASS`
- Quality gate: `best_model_pass_rate >= 0.8`
- Overall winner: `bge_m3`
- Overall winner reason: `OFFICIAL_SELECTOR`
- Preflight validation: `PASS`
- Preflight missing marker count: `0`
- Total questions: `100`

## Model Results

| model | status | passed | total | pass_rate | coverage | missing | distractors | latency_ms | winner |
|---|---|---|---|---|---|---|---|---|---|
| multilingual_e5_small | FAIL | 66 | 100 | 0.6600 | 0.8000 | 40 | 0 | 25.0 | no |
| bge_m3 | FAIL | 82 | 100 | 0.8200 | 0.9150 | 17 | 0 | 23.3 | yes |

## Question Results

| question_id | test_type | model | status | coverage | missing | forbidden_hits | distractors | latency_ms |
|---|---|---|---|---|---|---|---|---|
| distractor-twin-innkeepers | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-twin-innkeepers | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-june-market-date | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-june-market-date | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-two-levs | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-two-levs | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-similar-islands | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-similar-islands | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-letter-mixup | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-letter-mixup | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-006 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-006 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-007 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-007 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-008 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-008 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-009 | distractor | multilingual_e5_small | FAIL | 0.0000 | Signal Lantern Morning at South Meadow arch, star ledger page | none | none | n/a |
| distractor-009 | distractor | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-010 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-010 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-011 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-011 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-012 | distractor | multilingual_e5_small | FAIL | 0.0000 | Cloud Wharf office, wax thread | none | none | n/a |
| distractor-012 | distractor | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-013 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-013 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-014 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-014 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-015 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-015 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-016 | distractor | multilingual_e5_small | FAIL | 0.5000 | March 26 Bellwater Fair | none | none | n/a |
| distractor-016 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-017 | distractor | multilingual_e5_small | FAIL | 0.0000 | Moon Mill yard, glass ink bottle | none | none | n/a |
| distractor-017 | distractor | bge_m3 | FAIL | 0.0000 | Moon Mill yard, glass ink bottle | none | none | n/a |
| distractor-018 | distractor | multilingual_e5_small | FAIL | 0.0000 | copper wind vane pin, Daria of Winter Chapel porch | none | none | n/a |
| distractor-018 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-019 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-019 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-020 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-020 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-021 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-021 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-022 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-022 | distractor | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-023 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-023 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-024 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-024 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-025 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-025 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-026 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-026 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-027 | distractor | multilingual_e5_small | FAIL | 0.0000 | Cloud Wharf office, copper token | none | none | n/a |
| distractor-027 | distractor | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-028 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-028 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-029 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-029 | distractor | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-030 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-030 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-031 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-031 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-032 | distractor | multilingual_e5_small | FAIL | 0.0000 | Moon Mill yard, amber lantern | none | none | n/a |
| distractor-032 | distractor | bge_m3 | FAIL | 0.0000 | Moon Mill yard, amber lantern | none | none | n/a |
| distractor-033 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-033 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-034 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-034 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-035 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-035 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-036 | distractor | multilingual_e5_small | FAIL | 0.5000 | March 10 Bellwater Fair | none | none | n/a |
| distractor-036 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-037 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-037 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-038 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-038 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-039 | distractor | multilingual_e5_small | FAIL | 0.0000 | Signal Lantern Morning at South Meadow arch, brass compass | none | none | n/a |
| distractor-039 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-040 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-040 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-041 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-041 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-042 | distractor | multilingual_e5_small | FAIL | 0.0000 | Cloud Wharf office, lantern hook | none | none | n/a |
| distractor-042 | distractor | bge_m3 | FAIL | 0.0000 | Cloud Wharf office, lantern hook | none | none | n/a |
| distractor-043 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-043 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-044 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-044 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-045 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-045 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-046 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-046 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-047 | distractor | multilingual_e5_small | FAIL | 0.0000 | Moon Mill yard, willow basket | none | none | n/a |
| distractor-047 | distractor | bge_m3 | FAIL | 0.0000 | Moon Mill yard, willow basket | none | none | n/a |
| distractor-048 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-048 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-049 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-049 | distractor | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-050 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-050 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-051 | distractor | multilingual_e5_small | FAIL | 0.5000 | March 25 Bellwater Fair | none | none | n/a |
| distractor-051 | distractor | bge_m3 | FAIL | 0.5000 | March 25 Bellwater Fair | none | none | n/a |
| distractor-052 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-052 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-053 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-053 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-054 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-054 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-055 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-055 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-056 | distractor | multilingual_e5_small | FAIL | 0.5000 | March 12 Bellwater Fair | none | none | n/a |
| distractor-056 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-057 | distractor | multilingual_e5_small | FAIL | 0.0000 | Cloud Wharf office, canal route map | none | none | n/a |
| distractor-057 | distractor | bge_m3 | FAIL | 0.0000 | Cloud Wharf office, canal route map | none | none | n/a |
| distractor-058 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-058 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-059 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-059 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-060 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-060 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-061 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-061 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-062 | distractor | multilingual_e5_small | FAIL | 0.0000 | Moon Mill yard, saffron scarf | none | none | n/a |
| distractor-062 | distractor | bge_m3 | FAIL | 0.0000 | Moon Mill yard, saffron scarf | none | none | n/a |
| distractor-063 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-063 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-064 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-064 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-065 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-065 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-066 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-066 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-067 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-067 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-068 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-068 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-069 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-069 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-070 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-070 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-071 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-071 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-072 | distractor | multilingual_e5_small | FAIL | 0.0000 | Cloud Wharf office, linen wick | none | none | n/a |
| distractor-072 | distractor | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-073 | distractor | multilingual_e5_small | FAIL | 0.0000 | star ledger page, Lev of Ridge Post loft | none | none | n/a |
| distractor-073 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-074 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-074 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-075 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-075 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-076 | distractor | multilingual_e5_small | FAIL | 0.5000 | March 14 Bellwater Fair | none | none | n/a |
| distractor-076 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-077 | distractor | multilingual_e5_small | FAIL | 0.0000 | Moon Mill yard, tin key | none | none | n/a |
| distractor-077 | distractor | bge_m3 | FAIL | 0.0000 | Moon Mill yard, tin key | none | none | n/a |
| distractor-078 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-078 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-079 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-079 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-080 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-080 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-081 | distractor | multilingual_e5_small | FAIL | 0.5000 | March 19 Bellwater Fair | none | none | n/a |
| distractor-081 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-082 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-082 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-083 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-083 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-084 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-084 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-085 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-085 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-086 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-086 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-087 | distractor | multilingual_e5_small | FAIL | 0.0000 | Cloud Wharf office, oak barrel hoops | none | none | n/a |
| distractor-087 | distractor | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-088 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-088 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-089 | distractor | multilingual_e5_small | FAIL | 0.0000 | Signal Lantern Morning at Willow Courtyard well, canal route map | none | none | n/a |
| distractor-089 | distractor | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-090 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-090 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-091 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-091 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-092 | distractor | multilingual_e5_small | FAIL | 0.0000 | Moon Mill yard, moonflower cutting | none | none | n/a |
| distractor-092 | distractor | bge_m3 | FAIL | 0.0000 | Moon Mill yard, moonflower cutting | none | none | n/a |
| distractor-093 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-093 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-094 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-094 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-095 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-095 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-096 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-096 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-097 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-097 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-098 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-098 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-099 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-099 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-100 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-100 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
