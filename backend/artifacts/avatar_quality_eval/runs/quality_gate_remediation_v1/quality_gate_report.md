# Task 64.4.1 — Quality Gate Report

Run ID: `20260712_172419Z_450b171c` (label `quality_gate_remediation_v1`)
Dataset: `learned_memory_answer_eval_v1.jsonl` v1 (unchanged), 12 cases, repeat_count=3, 36 total runs.
Real FA chat path: yes (real BGE-M3 local snapshot, real Redis, real Qdrant, real Brain provider `openai_compatible`/`deepseek-chat`). No mocked retrieval.
Brain prompt version: `learned_memory_answer_policy_v3`.

## Gate results

| Gate | Requirement | Actual | Result |
| --- | --- | --- | --- |
| Profile contamination (hard gate) | == 0 | 0 | **PASS** |
| Learned-memory support rate | >= 1.00 | 1.000000 | **PASS** |
| Corrected-memory preference rate | >= 1.00 | 0.666667 | **FAIL** |
| Perspective preservation rate | >= 0.90 | 1.000000 | **PASS** |
| Unsupported-detail rate | <= 0.10 | 0.000000 | **PASS** |
| Over-refusal rate | <= 0.10 | 0.041667 | **PASS** |
| Persona consistency rate | >= 0.80 | 1.000000 | **PASS** |
| Answer stability rate | >= 0.90 | 0.916667 | **PASS** |
| Passed cases | >= 10/12 | 11/12 | **PASS** |

**Overall gate: FAIL** (8 of 9 checks pass; the hard gate — profile contamination — passes).

## Why the task is not marked complete

Per the task's own instruction: "Do not claim completion if contamination remains above zero" (satisfied — it is zero) and "If softer quality thresholds cannot all be reached safely: report exact remaining failures; do not fake completion; recommend a narrowly scoped follow-up task." One softer gate, `corrected_memory_preference_rate`, is not met: it is 0.667 (2 of 3 repeat runs of `owner-corrected-bedtime-song` pass; 1 does not).

The failing run's dimension breakdown is `retrieval: fail` — the required evidence item is genuinely absent from the top-4 retrieved results for that specific run, not present-but-ignored. This was independently verified by sampling 5 live calls to the same question outside the harness: 4 of 5 returned the target memory in evidence, 1 of 5 did not (`stability_check` sample in the session transcript). This is a retrieval-relevance limitation for this case's specific abstract, meta-referential question phrasing ("Ты помнишь, какую песню я называл, а владелец потом исправил?"), not a defect introduced or left in the code this task touched.

Fixing this would require changing retrieval scoring, hybrid weighting, or top_k for this evidence class — all explicitly forbidden by this task's hard restrictions ("do not change retrieval ranking," "do not change hybrid weighting," "do not change top_k"). No safe fix within scope was found.

## What was fixed (see `root_cause_matrix.json` and `comparison.md` for full detail)

1. Two false-positive bugs in the deterministic evaluator's marker-matching logic (`_contains_marker`) that produced most of the apparent `profile_contamination`, `persona_cold_or_technical`, and several `unsupported_detail` failures in the committed tuned_v2 result — confirmed via direct SQL inspection that no real cross-profile data ever existed.
2. Negation-unaware forbidden-marker detection that misclassified honest denials ("I don't remember singing you Katyusha") as asserting the denied fact.
3. A structural evidence-packaging gap: the Brain prompt never distinguished owner-approved "verified learned memory" evidence from ordinary archival document chunks, and did not surface `memory_status`/`provenance`/`promotion_id` metadata already present in the Qdrant payload.
4. Two missing test fixtures: no approved evidence existed for the multiple-perspectives case's dual attribution, and no approved evidence existed for the sensitive-subject case at all — both created via the existing, already-tested candidate → approve → index pipeline (Task 64.2), not by re-ingesting the corpus or changing indexing semantics.
5. A deterministic, content-agnostic evidence filter that prevents a dispute-shaped verified memory from leaking into unrelated plain factual questions, replacing an unreliable prose-only LLM instruction.
6. A source-level output-guard precision fix: the `lack_of_evidence` flag (which also drives memory-candidate extraction and the real API response, not just this evaluation) now checks only the answer's opening sentence rather than the whole text.

## Recommended next step

A narrowly scoped follow-up — **Task 64.4.2 — Retrieval recall for indirect/meta-referential memory queries** — is recommended before re-attempting the `corrected_memory_preference_rate` gate, since fixing it requires retrieval-layer changes this task was not permitted to make. Do not begin Task 64.5 (Minimal Family Memory Review UI) as a substitute for this — the roadmap's stated hard-gate contingency ("profile contamination must still be zero") is satisfied, so Task 64.5 remains the next planned task after this quality question is resolved.
