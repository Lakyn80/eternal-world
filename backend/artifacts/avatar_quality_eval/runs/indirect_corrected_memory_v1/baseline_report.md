# Task 64.4 Baseline Report

- Run ID: `20260712_222548Z_8cd472e7`
- Run label: `indirect_corrected_memory_v1`
- Dataset: `/app/app/modules/avatar_quality_evaluation/datasets/learned_memory_answer_eval_v1.jsonl`
- Repeat count: `3`
- Total cases: 12
- Total runs: 36

## Gate Metrics

- Retrieval hit rate: 1.000
- Evidence-present-but-ignored count: 2
- Unsupported-detail count: 0
- Over-refusal count: 0
- Persona failures: 0
- Perspective failures: 0
- Stability failures: 1

## Per-Case Table

| Case | Run | Category | Result | Failures |
| --- | ---: | --- | --- | --- |
| `original-popice-childhood` | 1 | `original_seeded_memory` | pass | none |
| `original-popice-childhood` | 2 | `original_seeded_memory` | pass | none |
| `original-popice-childhood` | 3 | `original_seeded_memory` | pass | none |
| `learned-bedtime-song-indexed` | 1 | `learned_indexed_memory` | pass | none |
| `learned-bedtime-song-indexed` | 2 | `learned_indexed_memory` | pass | none |
| `learned-bedtime-song-indexed` | 3 | `learned_indexed_memory` | pass | none |
| `owner-corrected-bedtime-song` | 1 | `owner_corrected_memory` | pass | none |
| `owner-corrected-bedtime-song` | 2 | `owner_corrected_memory` | pass | none |
| `owner-corrected-bedtime-song` | 3 | `owner_corrected_memory` | pass | none |
| `multiple-perspectives-song` | 1 | `multiple_perspectives` | pass | none |
| `multiple-perspectives-song` | 2 | `multiple_perspectives` | pass | none |
| `multiple-perspectives-song` | 3 | `multiple_perspectives` | pass | none |
| `pending-unindexed-song` | 1 | `pending_unindexed_memory` | pass | none |
| `pending-unindexed-song` | 2 | `pending_unindexed_memory` | pass | none |
| `pending-unindexed-song` | 3 | `pending_unindexed_memory` | pass | none |
| `rejected-memory-song` | 1 | `rejected_memory` | pass | none |
| `rejected-memory-song` | 2 | `rejected_memory` | pass | none |
| `rejected-memory-song` | 3 | `rejected_memory` | pass | none |
| `private-memory-blocked` | 1 | `private_memory_blocked` | pass | none |
| `private-memory-blocked` | 2 | `private_memory_blocked` | pass | none |
| `private-memory-blocked` | 3 | `private_memory_blocked` | pass | none |
| `unknown-factual-paris` | 1 | `unknown_factual_question` | pass | none |
| `unknown-factual-paris` | 2 | `unknown_factual_question` | pass | none |
| `unknown-factual-paris` | 3 | `unknown_factual_question` | pass | none |
| `emotional-heavy-day` | 1 | `emotional_persona_question` | pass | none |
| `emotional-heavy-day` | 2 | `emotional_persona_question` | pass | none |
| `emotional-heavy-day` | 3 | `emotional_persona_question` | pass | none |
| `sensitive-political-prison` | 1 | `sensitive_subject` | fail | evidence_present_but_ignored |
| `sensitive-political-prison` | 2 | `sensitive_subject` | pass | none |
| `sensitive-political-prison` | 3 | `sensitive_subject` | fail | evidence_present_but_ignored |
| `repeat-learned-bedtime-song` | 1 | `repeat_answer_stability` | pass | none |
| `repeat-learned-bedtime-song` | 2 | `repeat_answer_stability` | pass | none |
| `repeat-learned-bedtime-song` | 3 | `repeat_answer_stability` | pass | none |
| `profile-isolation-other-avatar` | 1 | `profile_isolation` | pass | none |
| `profile-isolation-other-avatar` | 2 | `profile_isolation` | pass | none |
| `profile-isolation-other-avatar` | 3 | `profile_isolation` | pass | none |

## Metric Definitions

- `retrieval_evidence_hit_rate`: Grounded runs whose returned evidence matched required evidence markers or metadata.
- `required_marker_rate`: Runs where all required answer markers were present.
- `unsupported_detail_rate`: Runs containing forbidden unsupported answer markers.
- `over_refusal_rate`: Grounded runs that answered with lack-of-evidence behavior despite expected support.
- `lack_of_evidence_correctness_rate`: Lack-of-evidence runs that did not use forbidden facts.
- `persona_consistency_rate`: Runs with persona_applied=true and no cold/technical forbidden style.
- `forbidden_style_rate`: Runs containing prohibited technical or assistant-style phrasing.
- `learned_memory_answer_support_rate`: Learned indexed memory runs that used the required learned markers.
- `corrected_memory_preference_rate`: Owner-corrected runs that used the approved marker and not rejected markers.
- `perspective_preservation_rate`: Perspective runs that preserved expected attribution behavior.
- `answer_stability_rate`: Repeated case groups whose factual required/forbidden marker outcome stayed stable.
- `profile_contamination_count`: Runs where evidence contained markers forbidden for profile isolation.
- `evaluated_case_count`: Number of unique dataset cases evaluated.
- `passed_case_count`: Unique cases whose every repeat run passed.
- `failed_case_count`: Unique cases with at least one failed repeat run.
