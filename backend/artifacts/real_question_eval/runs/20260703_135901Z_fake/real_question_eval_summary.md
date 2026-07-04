# Real Question Eval Summary

## Run
- Run ID: `20260703_135901Z`
- Created: `2026-07-03T13:59:01.255039+00:00`
- Mode: `fake_eval`
- Dataset: `Eternal World Short Fact Validation V1`
- Dataset ID: `eternal-world-short-fact-v1`
- Dataset file: `/app/app/modules/real_question_eval/datasets/eternal_world_short_fact_v1.json`
- Run status: `COMPLETED`
- Quality status: `PASS`
- Quality gate: `best_model_pass_rate >= 0.8`
- Overall winner: `bge_m3`
- Overall winner reason: `OFFICIAL_SELECTOR`
- Preflight validation: `PASS`
- Preflight missing marker count: `0`
- Total questions: `120`

## Model Results

| model | status | passed | total | pass_rate | coverage | missing | distractors | latency_ms | winner |
|---|---|---|---|---|---|---|---|---|---|
| multilingual_e5_small | FAIL | 102 | 120 | 0.8500 | 0.8917 | 18 | 0 | 29.3 | no |
| bge_m3 | FAIL | 114 | 120 | 0.9500 | 0.9542 | 6 | 0 | 29.5 | yes |

## Question Results

| question_id | test_type | model | status | coverage | missing | forbidden_hits | distractors | latency_ms |
|---|---|---|---|---|---|---|---|---|
| short-fact-ferry-lantern | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-ferry-lantern | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-orchard-key | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-orchard-key | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-postmaster-map | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-postmaster-map | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-clocktower-bell | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-clocktower-bell | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-river-mill-basket | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-river-mill-basket | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-market-tokens | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-market-tokens | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-garden-journal | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-garden-journal | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-snow-shed | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-snow-shed | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-009 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-009 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-010 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-010 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-011 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-011 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-012 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-012 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-013 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-013 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-014 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-014 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-015 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-015 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-016 | short_fact | multilingual_e5_small | FAIL | 0.5000 | paper moon mask | none | none | n/a |
| short-fact-016 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-017 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-017 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-018 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-018 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-019 | short_fact | multilingual_e5_small | FAIL | 0.0000 | saffron coal stove hiss | none | none | n/a |
| short-fact-019 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-020 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-020 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-021 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-021 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-022 | short_fact | multilingual_e5_small | FAIL | 0.5000 | rope bridge permit | none | none | n/a |
| short-fact-022 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-023 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-023 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-024 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-024 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-025 | short_fact | multilingual_e5_small | FAIL | 0.0000 | saffron canal route map | none | none | n/a |
| short-fact-025 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-026 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-026 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-027 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-027 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-028 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-028 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-029 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-029 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-030 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-030 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-031 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-031 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-032 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-032 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-033 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-033 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-034 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-034 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-035 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-035 | short_fact | bge_m3 | FAIL | 0.0000 | silver booth token | none | none | n/a |
| short-fact-036 | short_fact | multilingual_e5_small | FAIL | 0.5000 | clay watering cup | none | none | n/a |
| short-fact-036 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-037 | short_fact | multilingual_e5_small | FAIL | 0.0000 | saffron juniper bundles | none | none | n/a |
| short-fact-037 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-038 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-038 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-039 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-039 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-040 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-040 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-041 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-041 | short_fact | bge_m3 | FAIL | 0.0000 | star ledger page | none | none | n/a |
| short-fact-042 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-042 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-043 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-043 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-044 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-044 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-045 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-045 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-046 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-046 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-047 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-047 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-048 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-048 | short_fact | bge_m3 | FAIL | 0.5000 | paper moon mask | none | none | n/a |
| short-fact-049 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-049 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-050 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-050 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-051 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-051 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-052 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-052 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-053 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-053 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-054 | short_fact | multilingual_e5_small | FAIL | 0.5000 | rope bridge permit | none | none | n/a |
| short-fact-054 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-055 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-055 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-056 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-056 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-057 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-057 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-058 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-058 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-059 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-059 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-060 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-060 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-061 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-061 | short_fact | bge_m3 | FAIL | 0.0000 | saffron birch tea flask | none | none | n/a |
| short-fact-062 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-062 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-063 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-063 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-064 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-064 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-065 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-065 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-066 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-066 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-067 | short_fact | multilingual_e5_small | FAIL | 0.0000 | saffron silver booth token | none | none | n/a |
| short-fact-067 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-068 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-068 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-069 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-069 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-070 | short_fact | multilingual_e5_small | FAIL | 0.5000 | smoke vent chain | none | none | n/a |
| short-fact-070 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-071 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-071 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-072 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-072 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-073 | short_fact | multilingual_e5_small | FAIL | 0.0000 | saffron star ledger page | none | none | n/a |
| short-fact-073 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-074 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-074 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-075 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-075 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-076 | short_fact | multilingual_e5_small | FAIL | 0.5000 | wax thread | none | none | n/a |
| short-fact-076 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-077 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-077 | short_fact | bge_m3 | FAIL | 0.0000 | tin key | none | none | n/a |
| short-fact-078 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-078 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-079 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-079 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-080 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-080 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-081 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-081 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-082 | short_fact | multilingual_e5_small | FAIL | 0.5000 | copper wind vane pin | none | none | n/a |
| short-fact-082 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-083 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-083 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-084 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-084 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-085 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-085 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-086 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-086 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-087 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-087 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-088 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-088 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-089 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-089 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-090 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-090 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-091 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-091 | short_fact | bge_m3 | FAIL | 0.0000 | saffron copper token | none | none | n/a |
| short-fact-092 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-092 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-093 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-093 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-094 | short_fact | multilingual_e5_small | FAIL | 0.5000 | saffron scarf | none | none | n/a |
| short-fact-094 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-095 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-095 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-096 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-096 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-097 | short_fact | multilingual_e5_small | FAIL | 0.0000 | saffron basalt sketch | none | none | n/a |
| short-fact-097 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-098 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-098 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-099 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-099 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-100 | short_fact | multilingual_e5_small | FAIL | 0.5000 | clay watering cup | none | none | n/a |
| short-fact-100 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-101 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-101 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-102 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-102 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-103 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-103 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-104 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-104 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-105 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-105 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-106 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-106 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-107 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-107 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-108 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-108 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-109 | short_fact | multilingual_e5_small | FAIL | 0.0000 | saffron tin key | none | none | n/a |
| short-fact-109 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-110 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-110 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-111 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-111 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-112 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-112 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-113 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-113 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-114 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-114 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-115 | short_fact | multilingual_e5_small | FAIL | 0.0000 | saffron coal stove hiss | none | none | n/a |
| short-fact-115 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-116 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-116 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-117 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-117 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-118 | short_fact | multilingual_e5_small | FAIL | 0.5000 | rope bridge permit | none | none | n/a |
| short-fact-118 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-119 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-119 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| short-fact-120 | short_fact | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| short-fact-120 | short_fact | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
