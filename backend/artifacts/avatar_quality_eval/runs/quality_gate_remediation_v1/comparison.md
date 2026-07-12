# Task 64.4.1 — Baseline vs Tuned v2 vs Final Remediation Comparison

Dataset: `learned_memory_answer_eval_v1.jsonl` (12 cases, repeat_count=3, 36 total runs per full evaluation) — unchanged throughout. No case was removed, no scoring threshold was relaxed, no expected marker was broadened.

| Metric | Baseline | Tuned v2 (committed) | Final (`quality_gate_remediation_v1`) | Gate | Gate met |
| --- | ---: | ---: | ---: | --- | --- |
| profile_contamination_count | 3 | 3 | **0** | == 0 (hard gate) | ✅ |
| learned_memory_answer_support_rate | 0.000 | 1.000 | **1.000** | >= 1.00 | ✅ |
| corrected_memory_preference_rate | 0.000 | 0.000 | **0.667** | >= 1.00 | ❌ |
| perspective_preservation_rate | 0.000 | 0.000 | **1.000** | >= 0.90 | ✅ |
| unsupported_detail_rate | 0.417 | 0.306 | **0.000** | <= 0.10 | ✅ |
| over_refusal_rate | 0.250 | 0.250 | **0.042** | <= 0.10 | ✅ |
| persona_consistency_rate | 0.111 | 0.417 | **1.000** | >= 0.80 | ✅ |
| answer_stability_rate | 0.667 | 0.750 | **0.917** | >= 0.90 | ✅ |
| passed_case_count | 0/12 | 3/12 | **11/12** | >= 10/12 | ✅ |
| lack_of_evidence_correctness_rate | 0.500 | 0.333 | **1.000** | (informational) | — |
| retrieval_evidence_hit_rate | 0.750 | 0.750 | **1.000** | (informational) | — |
| forbidden_style_rate | 0.889 | 0.583 | **0.000** | (informational) | — |

**Overall gate: 8 of 9 PASS. Hard gate (profile contamination) PASS. Overall FAIL** — one metric, `corrected_memory_preference_rate`, remains below its 1.00 threshold.

## Improved cases (baseline → final)

- `original-popice-childhood` — stable pass throughout (unaffected regression check).
- `learned-bedtime-song-indexed` — fail → pass (evidence contract fix).
- `multiple-perspectives-song` — fail → pass (test-data-setup + intent-gated evidence filter).
- `pending-unindexed-song` — fail (false persona flag) → pass (evaluator fix).
- `rejected-memory-song` — fail (false unsupported-detail flag) → pass (negation-aware evaluator fix).
- `private-memory-blocked` — fail (false flags) → pass (evaluator + output_guard fixes).
- `unknown-factual-paris` — fail (false unsupported-detail flag on object-first negation) → pass (bidirectional negation fix).
- `emotional-heavy-day` — fail (false persona flag) → pass (evaluator fix).
- `sensitive-political-prison` — fail (no citable evidence existed) → pass (test-data-setup).
- `repeat-learned-bedtime-song` — fail → pass (evidence contract + intent-gated filter).
- `profile-isolation-other-avatar` — fail (false contamination) → pass (evaluator proximity fix confirms zero real leakage).

## Remaining failure

- `owner-corrected-bedtime-song` — passes 2 of 3 repeat runs. The 1 failing run is a genuine retrieval-relevance miss (the target memory does not appear in the top-4 retrieved items for this case's specific abstract question phrasing, confirmed by live sampling: 4/5 hit rate across independent calls). This is out of this task's scope to fix (retrieval ranking/top_k changes are explicitly forbidden).

## Regressions

None accepted. One regression was introduced and then reverted/fixed within this task's own iteration (Run B → Run C → Run D): adding the multiple-perspectives test-data-setup memory initially caused the dispute content to leak into unrelated plain factual and corrected-memory questions (`learned_memory_answer_support_rate` dropped to 0.0–0.33 in intermediate runs). This was fully resolved by the deterministic, content-agnostic evidence-intent filter (see `root_cause_matrix.json`, cluster "dispute memory leaking into plain factual / corrected-memory questions") before the final run.

## Rejected changes

- A "prefer the most-recently-indexed verified item" recency rule for conflicting learned memories was tried and rejected: it caused the newly-indexed dispute memory to be treated as authoritative over the older, correct settled fact for ordinary questions — backwards from the desired behavior. Replaced with the question-intent-gated evidence filter.
- Relying solely on prose prompt instructions ("ignore this evidence item for ordinary questions") to gate dispute-memory visibility was tried and rejected as unreliable across repeat LLM calls (non-deterministic compliance, observed leaking in up to 2 of 3 runs). Replaced with a deterministic downstream evidence filter that does not depend on LLM instruction-following.
