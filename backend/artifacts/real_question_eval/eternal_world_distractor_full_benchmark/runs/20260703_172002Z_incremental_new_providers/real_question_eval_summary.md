# Real Question Eval Summary

## Run
- Run ID: `20260703_172002Z`
- Created: `2026-07-03T17:20:02.971494+00:00`
- Mode: `incremental_real_eval`
- Dataset: `Eternal World Distractor Validation V1`
- Dataset ID: `eternal-world-distractor-v1`
- Dataset file: `/app/app/modules/real_question_eval/datasets/eternal_world_distractor_v1.json`
- Run status: `COMPLETED`
- Quality status: `FAIL`
- Quality gate: `n/a >= n/a`
- Overall winner: `bge_m3`
- Overall winner reason: `n/a`
- Preflight validation: `n/a`
- Preflight missing marker count: `n/a`
- Total questions: `100`

## Model Results

| model | status | passed | total | pass_rate | coverage | missing | distractors | latency_ms | winner |
|---|---|---|---|---|---|---|---|---|---|
| multilingual_e5_small | FAIL | 69 | 100 | 0.6900 | 0.9800 | 4 | 23 | 1519.6 | no |
| bge_m3 | FAIL | 85 | 100 | 0.8500 | 0.9550 | 9 | 5 | 419.7 | yes |
| paraphrase_multilingual_mpnet_base_v2 | FAIL | 76 | 100 | 0.7600 | 0.8800 | 24 | 0 | 222.7 | no |
| multilingual_e5_base | FAIL | 72 | 100 | 0.7200 | 0.9200 | 16 | 0 | 212.3 | no |

## Question Results

| question_id | test_type | model | status | coverage | missing | forbidden_hits | distractors | latency_ms |
|---|---|---|---|---|---|---|---|---|
| distractor-twin-innkeepers | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Marta of River Inn | Marta of River Inn | n/a |
| distractor-twin-innkeepers | distractor | bge_m3 | FAIL | 1.0000 | none | Marta of River Inn | Marta of River Inn | n/a |
| distractor-twin-innkeepers | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-twin-innkeepers | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-june-market-date | distractor | multilingual_e5_small | FAIL | 1.0000 | none | June 4 noon market | June 4 noon market | n/a |
| distractor-june-market-date | distractor | bge_m3 | FAIL | 1.0000 | none | June 4 noon market | June 4 noon market | n/a |
| distractor-june-market-date | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-june-market-date | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-two-levs | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Lev the ferryman | Lev the ferryman | n/a |
| distractor-two-levs | distractor | bge_m3 | FAIL | 1.0000 | none | Lev the ferryman | Lev the ferryman | n/a |
| distractor-two-levs | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-two-levs | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-similar-islands | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-similar-islands | distractor | bge_m3 | FAIL | 1.0000 | none | Fox Island ferry shed | Fox Island ferry shed | n/a |
| distractor-similar-islands | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-similar-islands | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-letter-mixup | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-letter-mixup | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-letter-mixup | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-letter-mixup | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-006 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-006 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-006 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.5000 | March 16 Bellwater Fair | none | none | n/a |
| distractor-006 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 16 Bellwater Fair | none | none | n/a |
| distractor-007 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-007 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-007 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-007 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-008 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-008 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-008 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-008 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-009 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-009 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-009 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-009 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-010 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Damir of Birch Ferry shed | Damir of Birch Ferry shed | n/a |
| distractor-010 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-010 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-010 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-011 | distractor | multilingual_e5_small | FAIL | 0.5000 | March 21 Bellwater Fair | none | none | n/a |
| distractor-011 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-011 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.5000 | March 21 Bellwater Fair | none | none | n/a |
| distractor-011 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-012 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-012 | distractor | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-012 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.0000 | Cloud Wharf office, wax thread | none | none | n/a |
| distractor-012 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-013 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-013 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-013 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-013 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-014 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-014 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-014 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-014 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-015 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Kira of Bell Bridge square | Kira of Bell Bridge square | n/a |
| distractor-015 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-015 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-015 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-016 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-016 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-016 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-016 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-017 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-017 | distractor | bge_m3 | FAIL | 0.0000 | Moon Mill yard, glass ink bottle | none | none | n/a |
| distractor-017 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.0000 | Moon Mill yard, glass ink bottle | none | none | n/a |
| distractor-017 | distractor | multilingual_e5_base | FAIL | 0.0000 | Moon Mill yard, glass ink bottle | none | none | n/a |
| distractor-018 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-018 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-018 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-018 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-019 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-019 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-019 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-019 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-020 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Nikola of Star Basin gallery | Nikola of Star Basin gallery | n/a |
| distractor-020 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-020 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-020 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-021 | distractor | multilingual_e5_small | FAIL | 0.5000 | March 13 Bellwater Fair | none | none | n/a |
| distractor-021 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-021 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.5000 | March 13 Bellwater Fair | none | none | n/a |
| distractor-021 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-022 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-022 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-022 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-022 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-023 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-023 | distractor | bge_m3 | FAIL | 1.0000 | none | clay watering cup | clay watering cup | n/a |
| distractor-023 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-023 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-024 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-024 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-024 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-024 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-025 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Zora of Birch Ferry shed | Zora of Birch Ferry shed | n/a |
| distractor-025 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-025 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-025 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-026 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-026 | distractor | bge_m3 | FAIL | 0.5000 | March 18 Bellwater Fair | none | none | n/a |
| distractor-026 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.5000 | March 18 Bellwater Fair | none | none | n/a |
| distractor-026 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 18 Bellwater Fair | none | none | n/a |
| distractor-027 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-027 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-027 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.0000 | Cloud Wharf office, copper token | none | none | n/a |
| distractor-027 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-028 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-028 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-028 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-028 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-029 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-029 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-029 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-029 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-030 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Boris of Bell Bridge square | Boris of Bell Bridge square | n/a |
| distractor-030 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-030 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-030 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-031 | distractor | multilingual_e5_small | FAIL | 0.5000 | March 23 Bellwater Fair | none | none | n/a |
| distractor-031 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-031 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.5000 | March 23 Bellwater Fair | none | none | n/a |
| distractor-031 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 23 Bellwater Fair | none | none | n/a |
| distractor-032 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-032 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-032 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-032 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-033 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-033 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-033 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-033 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-034 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-034 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-034 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-034 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-035 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Talia of Star Basin gallery | Talia of Star Basin gallery | n/a |
| distractor-035 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-035 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-035 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-036 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-036 | distractor | bge_m3 | FAIL | 0.5000 | March 10 Bellwater Fair | none | none | n/a |
| distractor-036 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.5000 | March 10 Bellwater Fair | none | none | n/a |
| distractor-036 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 10 Bellwater Fair | none | none | n/a |
| distractor-037 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-037 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-037 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-037 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-038 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-038 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-038 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-038 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-039 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-039 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-039 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-039 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-040 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Tomas of Birch Ferry shed | Tomas of Birch Ferry shed | n/a |
| distractor-040 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-040 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-040 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-041 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-041 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-041 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.5000 | March 15 Bellwater Fair | none | none | n/a |
| distractor-041 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 15 Bellwater Fair | none | none | n/a |
| distractor-042 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-042 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-042 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-042 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-043 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | blue glass jar | blue glass jar | n/a |
| distractor-043 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-043 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-043 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-044 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-044 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-044 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-044 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-045 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Yara of Bell Bridge square | Yara of Bell Bridge square | n/a |
| distractor-045 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-045 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-045 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-046 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-046 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-046 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.5000 | March 20 Bellwater Fair | none | none | n/a |
| distractor-046 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 20 Bellwater Fair | none | none | n/a |
| distractor-047 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | none | none | n/a |
| distractor-047 | distractor | bge_m3 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-047 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-047 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-048 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | birch tea flask | birch tea flask | n/a |
| distractor-048 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-048 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-048 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-049 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-049 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-049 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-049 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-050 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Damir of Star Basin gallery | Damir of Star Basin gallery | n/a |
| distractor-050 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-050 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-050 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-051 | distractor | multilingual_e5_small | FAIL | 0.5000 | March 25 Bellwater Fair | none | none | n/a |
| distractor-051 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-051 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-051 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-052 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-052 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-052 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-052 | distractor | multilingual_e5_base | FAIL | 0.0000 | Blue Trunk cabin, violet ribbon | none | none | n/a |
| distractor-053 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-053 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-053 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-053 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-054 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-054 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-054 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-054 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-055 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Kira of Birch Ferry shed | Kira of Birch Ferry shed | n/a |
| distractor-055 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-055 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-055 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-056 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-056 | distractor | bge_m3 | FAIL | 0.5000 | March 12 Bellwater Fair | none | none | n/a |
| distractor-056 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.5000 | March 12 Bellwater Fair | none | none | n/a |
| distractor-056 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 12 Bellwater Fair | none | none | n/a |
| distractor-057 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-057 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-057 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.0000 | Cloud Wharf office, canal route map | none | none | n/a |
| distractor-057 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-058 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-058 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-058 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-058 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-059 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-059 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-059 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-059 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-060 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Nikola of Bell Bridge square | Nikola of Bell Bridge square | n/a |
| distractor-060 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-060 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-060 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-061 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-061 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-061 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.5000 | March 17 Bellwater Fair | none | none | n/a |
| distractor-061 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-062 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-062 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-062 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.0000 | Moon Mill yard, saffron scarf | none | none | n/a |
| distractor-062 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-063 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-063 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-063 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-063 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-064 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-064 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-064 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-064 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-065 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Zora of Star Basin gallery | Zora of Star Basin gallery | n/a |
| distractor-065 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-065 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-065 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-066 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-066 | distractor | bge_m3 | FAIL | 0.5000 | March 22 Bellwater Fair | none | none | n/a |
| distractor-066 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-066 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 22 Bellwater Fair | none | none | n/a |
| distractor-067 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-067 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-067 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-067 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-068 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-068 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-068 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-068 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-069 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-069 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-069 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-069 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-070 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-070 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-070 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-070 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-071 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-071 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-071 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-071 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-072 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-072 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-072 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-072 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-073 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-073 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-073 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-073 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-074 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-074 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-074 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-074 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-075 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Talia of Bell Bridge square | Talia of Bell Bridge square | n/a |
| distractor-075 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-075 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-075 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-076 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-076 | distractor | bge_m3 | FAIL | 0.5000 | March 14 Bellwater Fair | none | none | n/a |
| distractor-076 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-076 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 14 Bellwater Fair | none | none | n/a |
| distractor-077 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-077 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-077 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-077 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-078 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-078 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-078 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-078 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-079 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-079 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-079 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-079 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-080 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Tomas of Star Basin gallery | Tomas of Star Basin gallery | n/a |
| distractor-080 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-080 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-080 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-081 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-081 | distractor | bge_m3 | FAIL | 0.5000 | March 19 Bellwater Fair | none | none | n/a |
| distractor-081 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-081 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-082 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-082 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-082 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-082 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-083 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-083 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-083 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-083 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-084 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-084 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-084 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-084 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-085 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Yara of Birch Ferry shed | Yara of Birch Ferry shed | n/a |
| distractor-085 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-085 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-085 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-086 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-086 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-086 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-086 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 24 Bellwater Fair | none | none | n/a |
| distractor-087 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-087 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-087 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.0000 | Cloud Wharf office, oak barrel hoops | none | none | n/a |
| distractor-087 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-088 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-088 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-088 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-088 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-089 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-089 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-089 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-089 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-090 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Damir of Bell Bridge square | Damir of Bell Bridge square | n/a |
| distractor-090 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-090 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-090 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-091 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-091 | distractor | bge_m3 | FAIL | 0.5000 | March 11 Bellwater Fair | none | none | n/a |
| distractor-091 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.5000 | March 11 Bellwater Fair | none | none | n/a |
| distractor-091 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 11 Bellwater Fair | none | none | n/a |
| distractor-092 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-092 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-092 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 1.0000 | none | none | none | n/a |
| distractor-092 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-093 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-093 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-093 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-093 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-094 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-094 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-094 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-094 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-095 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Kira of Star Basin gallery | Kira of Star Basin gallery | n/a |
| distractor-095 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-095 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-095 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-096 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-096 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-096 | distractor | paraphrase_multilingual_mpnet_base_v2 | FAIL | 0.5000 | March 16 Bellwater Fair | none | none | n/a |
| distractor-096 | distractor | multilingual_e5_base | FAIL | 0.5000 | March 16 Bellwater Fair | none | none | n/a |
| distractor-097 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-097 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-097 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-097 | distractor | multilingual_e5_base | FAIL | 1.0000 | none | none | none | n/a |
| distractor-098 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-098 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-098 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-098 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-099 | distractor | multilingual_e5_small | PASS | 1.0000 | none | none | none | n/a |
| distractor-099 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-099 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-099 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
| distractor-100 | distractor | multilingual_e5_small | FAIL | 1.0000 | none | Nikola of Birch Ferry shed | Nikola of Birch Ferry shed | n/a |
| distractor-100 | distractor | bge_m3 | PASS | 1.0000 | none | none | none | n/a |
| distractor-100 | distractor | paraphrase_multilingual_mpnet_base_v2 | PASS | 1.0000 | none | none | none | n/a |
| distractor-100 | distractor | multilingual_e5_base | PASS | 1.0000 | none | none | none | n/a |
