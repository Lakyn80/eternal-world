# Real Question Eval Summary

## Run
- Run ID: `20260703_140317Z`
- Created: `2026-07-03T14:03:17.603692+00:00`
- Mode: `fake_eval`
- Dataset: `Eternal World Negative Validation V1`
- Dataset ID: `eternal-world-negative-v1`
- Dataset file: `/app/app/modules/real_question_eval/datasets/eternal_world_negative_v1.json`
- Run status: `COMPLETED`
- Quality status: `PASS`
- Quality gate: `best_model_pass_rate >= 0.8`
- Overall winner: `multilingual_e5_small`
- Overall winner reason: `AGGREGATE_QUALITY_RANKING`
- Preflight validation: `PASS`
- Preflight missing marker count: `0`
- Total questions: `80`

## Model Results

| model | status | passed | total | pass_rate | coverage | missing | distractors | latency_ms | winner |
|---|---|---|---|---|---|---|---|---|---|
| multilingual_e5_small | PASS | 80 | 80 | 1.0000 | 0.0000 | 0 | 0 | 27.9 | yes |
| bge_m3 | FAIL | 53 | 80 | 0.6625 | 0.0000 | 0 | 0 | 25.6 | no |

## Question Results

| question_id | test_type | model | status | coverage | missing | forbidden_hits | distractors | latency_ms |
|---|---|---|---|---|---|---|---|---|
| negative-missing-compass-serial | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-missing-compass-serial | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-mill-tunnel-password | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-mill-tunnel-password | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-mayor-hidden-daughter | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-mayor-hidden-daughter | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-sapphire-weight | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-sapphire-weight | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-sixth-bell-verse | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-sixth-bell-verse | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-006 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-006 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-007 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-007 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-008 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-008 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-009 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-009 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-010 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-010 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-011 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-011 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-012 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-012 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-013 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-013 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-014 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-014 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-015 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-015 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-016 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-016 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-017 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-017 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-018 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-018 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-019 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-019 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-020 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-020 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-021 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-021 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-022 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-022 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-023 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-023 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-024 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-024 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-025 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-025 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-026 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-026 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-027 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-027 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-028 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-028 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-029 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-029 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-030 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-030 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-031 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-031 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-032 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-032 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-033 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-033 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-034 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-034 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-035 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-035 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-036 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-036 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-037 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-037 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-038 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-038 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-039 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-039 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-040 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-040 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-041 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-041 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-042 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-042 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-043 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-043 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-044 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-044 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-045 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-045 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-046 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-046 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-047 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-047 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-048 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-048 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-049 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-049 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-050 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-050 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-051 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-051 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-052 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-052 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-053 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-053 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-054 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-054 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-055 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-055 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-056 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-056 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-057 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-057 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-058 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-058 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-059 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-059 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-060 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-060 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-061 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-061 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-062 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-062 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-063 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-063 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-064 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-064 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-065 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-065 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-066 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-066 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-067 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-067 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-068 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-068 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-069 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-069 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-070 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-070 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-071 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-071 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-072 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-072 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-073 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-073 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-074 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-074 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-075 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-075 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-076 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-076 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-077 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-077 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-078 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-078 | negative | bge_m3 | FAIL | n/a | none | none | none | n/a |
| negative-079 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-079 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
| negative-080 | negative | multilingual_e5_small | PASS | n/a | none | none | none | n/a |
| negative-080 | negative | bge_m3 | PASS | n/a | none | none | none | n/a |
