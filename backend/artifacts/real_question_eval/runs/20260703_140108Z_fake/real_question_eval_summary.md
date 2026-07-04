# Real Question Eval Summary

## Run
- Run ID: `20260703_140108Z`
- Created: `2026-07-03T14:01:08.463282+00:00`
- Mode: `fake_eval`
- Dataset: `Eternal World Page Level Validation V1`
- Dataset ID: `eternal-world-page-level-v1`
- Dataset file: `/app/app/modules/real_question_eval/datasets/eternal_world_page_level_v1.json`
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
| multilingual_e5_small | FAIL | 71 | 100 | 0.7100 | 0.8467 | 40 | 3 | 32.4 | no |
| bge_m3 | FAIL | 94 | 100 | 0.9400 | 0.9833 | 5 | 0 | 33.1 | yes |

## Question Results

| question_id | test_type | model | status | coverage | missing | forbidden_hits | distractors | latency_ms |
|---|---|---|---|---|---|---|---|---|
| page-level-attic-instructions | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-attic-instructions | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-river-meeting | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-river-meeting | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-station-caretaker | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-station-caretaker | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-herbal-room | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-herbal-room | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-watchtower | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-watchtower | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-006 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-006 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-007 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-007 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-008 | page_level | multilingual_e5_small | FAIL | 0.3333 | paper moon mask, weathered camera strap | none | none | n/a |
| page-level-008 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-009 | page_level | multilingual_e5_small | FAIL | 0.0000 | saffron scarf, canal route map, brass compass | none | none | n/a |
| page-level-009 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-010 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-010 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-011 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-011 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-012 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-012 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-013 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-013 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-014 | page_level | multilingual_e5_small | FAIL | 0.0000 | clay watering cup, carved shell comb, tin key | none | none | n/a |
| page-level-014 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-015 | page_level | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| page-level-015 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-016 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-016 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-017 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-017 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-018 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-018 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-019 | page_level | multilingual_e5_small | FAIL | 0.0000 | lantern hook, juniper bundles, coal stove hiss | none | none | n/a |
| page-level-019 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-020 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-020 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-021 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-021 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-022 | page_level | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| page-level-022 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-023 | page_level | multilingual_e5_small | FAIL | 0.3333 | green apron, birch tea flask | none | none | n/a |
| page-level-023 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-024 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-024 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-025 | page_level | multilingual_e5_small | FAIL | 0.0000 | saffron scarf, canal route map | none | none | n/a |
| page-level-025 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-026 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-026 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-027 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-027 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-028 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-028 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-029 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-029 | page_level | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| page-level-030 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-030 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-031 | page_level | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| page-level-031 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-032 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-032 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-033 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-033 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-034 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-034 | page_level | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| page-level-035 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-035 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-036 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-036 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-037 | page_level | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| page-level-037 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-038 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-038 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-039 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-039 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-040 | page_level | multilingual_e5_small | FAIL | 0.0000 | paper moon mask, weathered camera strap | none | none | n/a |
| page-level-040 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-041 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-041 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-042 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-042 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-043 | page_level | multilingual_e5_small | FAIL | 1.0000 | none | glass ink bottle | glass ink bottle | n/a |
| page-level-043 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-044 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-044 | page_level | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| page-level-045 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-045 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-046 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-046 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-047 | page_level | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| page-level-047 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-048 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-048 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-049 | page_level | multilingual_e5_small | FAIL | 0.0000 | blue oar, star ledger page, oak barrel hoops | none | none | n/a |
| page-level-049 | page_level | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| page-level-050 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-050 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-051 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-051 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-052 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-052 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-053 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-053 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-054 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-054 | page_level | bge_m3 | FAIL | 0.0000 | violet ribbon, willow basket, birch tea flask | none | none | n/a |
| page-level-055 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-055 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-056 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-056 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-057 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-057 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-058 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-058 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-059 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-059 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-060 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-060 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-061 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-061 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-062 | page_level | multilingual_e5_small | FAIL | 0.0000 | clay watering cup, carved shell comb | none | none | n/a |
| page-level-062 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-063 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-063 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-064 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-064 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-065 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-065 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-066 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-066 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-067 | page_level | multilingual_e5_small | FAIL | 0.0000 | lantern hook, juniper bundles | none | none | n/a |
| page-level-067 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-068 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-068 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-069 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-069 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-070 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-070 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-071 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-071 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-072 | page_level | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| page-level-072 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-073 | page_level | multilingual_e5_small | FAIL | 0.3333 | saffron scarf, canal route map | none | none | n/a |
| page-level-073 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-074 | page_level | multilingual_e5_small | FAIL | 0.0000 | wax thread, brass compass, tuning fork | none | none | n/a |
| page-level-074 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-075 | page_level | multilingual_e5_small | FAIL | 0.0000 | cedar shovel, tuning fork | none | none | n/a |
| page-level-075 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-076 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-076 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-077 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-077 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-078 | page_level | multilingual_e5_small | FAIL | 0.3333 | clay watering cup, carved shell comb | copper token | copper token | n/a |
| page-level-078 | page_level | bge_m3 | FAIL | 0.3333 | clay watering cup, carved shell comb | none | none | n/a |
| page-level-079 | page_level | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| page-level-079 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-080 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-080 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-081 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-081 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-082 | page_level | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| page-level-082 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-083 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-083 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-084 | page_level | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| page-level-084 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-085 | page_level | multilingual_e5_small | FAIL | 0.0000 | smoke vent chain, basalt sketch | none | none | n/a |
| page-level-085 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-086 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-086 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-087 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-087 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-088 | page_level | multilingual_e5_small | FAIL | 0.3333 | paper moon mask, weathered camera strap | brass compass | brass compass | n/a |
| page-level-088 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-089 | page_level | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| page-level-089 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-090 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-090 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-091 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-091 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-092 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-092 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-093 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-093 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-094 | page_level | multilingual_e5_small | FAIL | 0.0000 | clay watering cup, carved shell comb, tin key | none | none | n/a |
| page-level-094 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-095 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-095 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-096 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-096 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-097 | page_level | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| page-level-097 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-098 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-098 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-099 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-099 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| page-level-100 | page_level | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| page-level-100 | page_level | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
