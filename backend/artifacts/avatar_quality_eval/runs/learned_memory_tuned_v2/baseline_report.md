# Task 64.4 Baseline Report

- Run ID: `20260712_144516Z_ecab5764`
- Run label: `tuned_v2`
- Dataset: `/app/app/modules/avatar_quality_evaluation/datasets/learned_memory_answer_eval_v1.jsonl`
- Repeat count: `3`
- Total cases: 12
- Total runs: 36

## Gate Metrics

- Retrieval hit rate: 0.750
- Evidence-present-but-ignored count: 9
- Unsupported-detail count: 11
- Over-refusal count: 6
- Persona failures: 21
- Perspective failures: 3
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
| `owner-corrected-bedtime-song` | 1 | `owner_corrected_memory` | fail | evidence_present_but_ignored, over_refusal, persona_cold_or_technical |
| `owner-corrected-bedtime-song` | 2 | `owner_corrected_memory` | fail | evidence_present_but_ignored, over_refusal, persona_cold_or_technical |
| `owner-corrected-bedtime-song` | 3 | `owner_corrected_memory` | fail | evidence_present_but_ignored, over_refusal, persona_cold_or_technical |
| `multiple-perspectives-song` | 1 | `multiple_perspectives` | fail | evidence_present_but_ignored, persona_cold_or_technical, perspective_collapsed |
| `multiple-perspectives-song` | 2 | `multiple_perspectives` | fail | evidence_present_but_ignored, persona_cold_or_technical, perspective_collapsed |
| `multiple-perspectives-song` | 3 | `multiple_perspectives` | fail | evidence_present_but_ignored, persona_cold_or_technical, perspective_collapsed |
| `pending-unindexed-song` | 1 | `pending_unindexed_memory` | fail | persona_cold_or_technical |
| `pending-unindexed-song` | 2 | `pending_unindexed_memory` | fail | persona_cold_or_technical |
| `pending-unindexed-song` | 3 | `pending_unindexed_memory` | fail | persona_cold_or_technical |
| `rejected-memory-song` | 1 | `rejected_memory` | fail | unsupported_detail, persona_cold_or_technical |
| `rejected-memory-song` | 2 | `rejected_memory` | fail | unsupported_detail, persona_cold_or_technical |
| `rejected-memory-song` | 3 | `rejected_memory` | fail | unsupported_detail, persona_cold_or_technical |
| `private-memory-blocked` | 1 | `private_memory_blocked` | fail | persona_cold_or_technical |
| `private-memory-blocked` | 2 | `private_memory_blocked` | fail | unsupported_detail, persona_cold_or_technical |
| `private-memory-blocked` | 3 | `private_memory_blocked` | fail | unsupported_detail, persona_cold_or_technical |
| `unknown-factual-paris` | 1 | `unknown_factual_question` | fail | unsupported_detail |
| `unknown-factual-paris` | 2 | `unknown_factual_question` | fail | unsupported_detail |
| `unknown-factual-paris` | 3 | `unknown_factual_question` | fail | unsupported_detail |
| `emotional-heavy-day` | 1 | `emotional_persona_question` | pass | none |
| `emotional-heavy-day` | 2 | `emotional_persona_question` | pass | none |
| `emotional-heavy-day` | 3 | `emotional_persona_question` | fail | persona_cold_or_technical |
| `sensitive-political-prison` | 1 | `sensitive_subject` | fail | retrieval_failure, evidence_present_but_ignored, over_refusal, persona_cold_or_technical |
| `sensitive-political-prison` | 2 | `sensitive_subject` | fail | retrieval_failure, evidence_present_but_ignored, over_refusal, persona_cold_or_technical |
| `sensitive-political-prison` | 3 | `sensitive_subject` | fail | retrieval_failure, evidence_present_but_ignored, over_refusal, persona_cold_or_technical |
| `repeat-learned-bedtime-song` | 1 | `repeat_answer_stability` | pass | none |
| `repeat-learned-bedtime-song` | 2 | `repeat_answer_stability` | pass | none |
| `repeat-learned-bedtime-song` | 3 | `repeat_answer_stability` | pass | none |
| `profile-isolation-other-avatar` | 1 | `profile_isolation` | fail | profile_contamination, unsupported_detail, persona_cold_or_technical |
| `profile-isolation-other-avatar` | 2 | `profile_isolation` | fail | profile_contamination, unsupported_detail |
| `profile-isolation-other-avatar` | 3 | `profile_isolation` | fail | profile_contamination, unsupported_detail, persona_cold_or_technical |

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
