# Task 64.4.2 — Baseline → Tuned v2 → Task 64.4.1 → Task 64.4.2 Comparison

| Metric | Baseline | Tuned v2 | Task 64.4.1 | Task 64.4.2 (final) | Gate | Met |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| profile_contamination_count | 3 | 3 | 0 | **0** | == 0 | ✅ |
| retrieval_evidence_hit_rate | 0.750 | 0.750 | 0.958 | **1.000** | == 1.00 | ✅ |
| learned_memory_answer_support_rate | 0.000 | 1.000 | 1.000 | **1.000** | == 1.00 | ✅ |
| corrected_memory_preference_rate | 0.000 | 0.000 | 0.667 | **1.000** | == 1.00 | ✅ |
| perspective_preservation_rate | 0.000 | 0.000 | 1.000 | **1.000** | >= 0.90 | ✅ |
| lack_of_evidence_correctness_rate | 0.500 | 0.333 | 1.000 | **1.000** | >= 0.90 | ✅ |
| unsupported_detail_rate | 0.417 | 0.306 | 0.000 | **0.000** | <= 0.10 | ✅ |
| over_refusal_rate | 0.250 | 0.250 | 0.042 | **0.000** | <= 0.10 | ✅ |
| persona_consistency_rate | 0.111 | 0.417 | 1.000 | **1.000** | >= 0.80 | ✅ |
| answer_stability_rate | 0.667 | 0.750 | 0.917 | **0.917** | >= 0.90 | ✅ |
| passed_case_count | 0/12 | 3/12 | 11/12 | **11/12** | >= 11/12 | ✅ |

**Final overall gate: PASS — 11 of 11 checks pass.**

`owner-corrected-bedtime-song`: fail / fail / fail(2 of 3) → **pass 3 of 3** (hard requirement met).

## Improved cases (Task 64.4.1 final → Task 64.4.2 final)

- `owner-corrected-bedtime-song`: 2/3 → **3/3** (the task's primary target).
- `unknown-factual-paris`: intermittent `incorrect_lack_of_evidence` (evaluator/output-guard denial-detection gap) → stable pass.
- `rejected-memory-song`: intermittent `unsupported_detail` (two separate evaluator false positives — cross-sentence proximity match, and "но не X" negation-scope bug) → stable pass.

## Unchanged (already passing in both runs)

`original-popice-childhood`, `learned-bedtime-song-indexed`, `multiple-perspectives-song`, `pending-unindexed-song`, `private-memory-blocked`, `emotional-heavy-day` (mostly stable; 1 of 3 runs intermittently misses the specific word "рядом" — genuine LLM phrasing choice, unrelated to this task), `repeat-learned-bedtime-song`, `profile-isolation-other-avatar`.

## Regressed cases

None. `sensitive-political-prison` intermittently fails on the literal-word-choice dimension in both the Task 64.4.1 final run and this run — not a new regression, and confirmed via live sampling to be independent of every change made in this task.

## Rejected approaches

- **Global retrieval `top_k` increase** — rejected outright per hard restrictions; not attempted.
- **Global recency boost for verified memories** — rejected; would have made the newly-indexed multiple-perspectives fixture always "win" over the older, correct settled fact for ordinary questions (observed as a real regression during iteration, reverted before being kept).
- **Relying on prompt wording alone to fix Brain evidence-use reliability** — tried three times with escalating specificity (abstract rule → per-item inline annotation → still ~60-80% reliable); replaced with deterministic evidence reordering + capping per the task's own explicit guidance to prefer deterministic pre-Brain resolution over prompt wording, which reached 100% in live sampling (15/15).
- **Broadly rewriting the Brain prompt** — rejected; only two narrow, documented clarifications were added to the existing `learned_memory_answer_policy_v3` section, versioned as `v3_1`.

## Latency / retrieval count / cache behavior

- Ordinary questions (the common case): unchanged — one retrieval call, default top_k, no behavior change from Task 64.4.1.
- Corrected-memory-intent questions only: two retrieval calls instead of one (original + one generic expansion query), each still using the real BGE-M3 embedding provider and Redis embedding cache exactly as before — cache key semantics were not touched, and each of the two queries is cached independently under its own (unchanged) key derivation.
- No change to Qdrant collection, hybrid weighting, or RRF/BM25 behavior for either path.
