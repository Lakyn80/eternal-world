# Real Question Eval Summary

## Run
- Run ID: `20260703_140248Z`
- Created: `2026-07-03T14:02:48.779913+00:00`
- Mode: `fake_eval`
- Dataset: `Eternal World Multi Document Validation V1`
- Dataset ID: `eternal-world-multi-document-v1`
- Dataset file: `/app/app/modules/real_question_eval/datasets/eternal_world_multi_document_v1.json`
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
| multilingual_e5_small | FAIL | 91 | 100 | 0.9100 | 0.9450 | 11 | 0 | 26.9 | no |
| bge_m3 | FAIL | 96 | 100 | 0.9600 | 0.9850 | 3 | 0 | 33.8 | yes |

## Question Results

| question_id | test_type | model | status | coverage | missing | forbidden_hits | distractors | latency_ms |
|---|---|---|---|---|---|---|---|---|
| multi-document-winter-convoy | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-winter-convoy | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-harbor-fair | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-harbor-fair | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-school-rehearsal | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-school-rehearsal | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-valley-expedition | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-valley-expedition | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-observatory-storm | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-observatory-storm | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-006 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-006 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-007 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-007 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-008 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-008 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-009 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-009 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-010 | multi_document | multilingual_e5_small | FAIL | 0.0000 | clay watering cup, canal route map | none | none | n/a |
| multi-document-010 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-011 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-011 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-012 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-012 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-013 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-013 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-014 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-014 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-015 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-015 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-016 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-016 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-017 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-017 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-018 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-018 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-019 | multi_document | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| multi-document-019 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-020 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-020 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-021 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-021 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-022 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-022 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-023 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-023 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-024 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-024 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-025 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-025 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-026 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-026 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-027 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-027 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-028 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-028 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-029 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-029 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-030 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-030 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-031 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-031 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-032 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-032 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-033 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-033 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-034 | multi_document | multilingual_e5_small | FAIL | 0.0000 | violet ribbon, star ledger page | none | none | n/a |
| multi-document-034 | multi_document | bge_m3 | FAIL | 0.5000 | star ledger page | none | none | n/a |
| multi-document-035 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-035 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-036 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-036 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-037 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-037 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-038 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-038 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-039 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-039 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-040 | multi_document | multilingual_e5_small | FAIL | 0.0000 | paper moon mask, juniper bundles | none | none | n/a |
| multi-document-040 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-041 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-041 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-042 | multi_document | multilingual_e5_small | FAIL | 0.0000 | clay watering cup, canal route map | none | none | n/a |
| multi-document-042 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-043 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-043 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-044 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-044 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-045 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-045 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-046 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-046 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-047 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-047 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-048 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-048 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-049 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-049 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-050 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-050 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-051 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-051 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-052 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-052 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-053 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-053 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-054 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-054 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-055 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-055 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-056 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-056 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-057 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-057 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-058 | multi_document | multilingual_e5_small | FAIL | 0.0000 | clay watering cup, canal route map | none | none | n/a |
| multi-document-058 | multi_document | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| multi-document-059 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-059 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-060 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-060 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-061 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-061 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-062 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-062 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-063 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-063 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-064 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-064 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-065 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-065 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-066 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-066 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-067 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-067 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-068 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-068 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-069 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-069 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-070 | multi_document | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| multi-document-070 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-071 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-071 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-072 | multi_document | multilingual_e5_small | FAIL | 0.5000 | juniper bundles | none | none | n/a |
| multi-document-072 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-073 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-073 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-074 | multi_document | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| multi-document-074 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-075 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-075 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-076 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-076 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-077 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-077 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-078 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-078 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-079 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-079 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-080 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-080 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-081 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-081 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-082 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-082 | multi_document | bge_m3 | FAIL | 0.0000 | violet ribbon, star ledger page | none | none | n/a |
| multi-document-083 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-083 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-084 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-084 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-085 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-085 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-086 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-086 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-087 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-087 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-088 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-088 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-089 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-089 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-090 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-090 | multi_document | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| multi-document-091 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-091 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-092 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-092 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-093 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-093 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-094 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-094 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-095 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-095 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-096 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-096 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-097 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-097 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-098 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-098 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-099 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-099 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| multi-document-100 | multi_document | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| multi-document-100 | multi_document | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
