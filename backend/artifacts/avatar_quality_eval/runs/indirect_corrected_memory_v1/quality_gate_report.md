# Task 64.4.2 — Quality Gate Report

Dataset: `learned_memory_answer_eval_v1.jsonl` v1 (unchanged), 12 cases, repeat_count=3, 36 total runs.
Real FA chat path: yes (real BGE-M3 local snapshot, real Redis, real Qdrant, real Brain provider). No mocked retrieval.
Brain prompt version: `learned_memory_answer_policy_v3_1`.

## Gate results

| Gate | Requirement | Actual | Result |
| --- | --- | --- | --- |
| Profile contamination | == 0 | 0 | **PASS** |
| Retrieval hit rate | == 1.00 | 1.000000 | **PASS** |
| Learned-memory support rate | == 1.00 | 1.000000 | **PASS** |
| Corrected-memory preference rate | == 1.00 | 1.000000 | **PASS** |
| Perspective preservation rate | >= 0.90 | 1.000000 | **PASS** |
| Lack-of-evidence correctness rate | >= 0.90 | 1.000000 | **PASS** |
| Unsupported-detail rate | <= 0.10 | 0.000000 | **PASS** |
| Over-refusal rate | <= 0.10 | 0.000000 | **PASS** |
| Persona consistency rate | >= 0.80 | 1.000000 | **PASS** |
| Answer stability rate | >= 0.90 | 0.916667 | **PASS** |
| Passed cases | >= 11/12 | 11/12 | **PASS** |

**Additional hard requirement — `owner-corrected-bedtime-song` must pass 3/3:** confirmed pass on run 1, 2, and 3. **MET.**

## Overall gate: PASS

## Remaining (non-blocking) failure

`sensitive-political-prison` failed 2 of 3 repeats with `evidence_present_but_ignored` — the Brain gave a respectful, evidence-consistent answer ("это было по политическим причинам... неохотно об этом рассказываю") without using the literal word "тюрьма"/"тюрьме" required by the case's marker. This is:

- **Not caused by any change in this task.** None of Task 64.4.2's code (query-intent classification, multi-query retrieval, evidence prioritization, data remediation) touches this question's path — its intent classifies as `direct_factual_memory` (no correction/disagreement markers), so it takes the single-query, unmodified-evidence branch, identical to Task 64.4.1's behavior.
- **Confirmed pre-existing and independent of my changes** by 5 live samples run before this evaluation, isolated from any code change: 4 of 5 used the word "тюрьме" correctly; 1 of 5 phrased the same true fact without the literal word. This matches genuine external Brain-provider (LLM) phrasing nondeterminism, not a defect in retrieval, evidence packaging, or the evaluator.
- Does not block the mandatory gate: `passed_case_count = 11/12` still meets the required `>= 11/12` threshold, and no aggregate metric is degraded below its required bound by this single case's partial failure.

## What was fixed (see `PROJECT_PROGRESS.md` and `corrected_memory_diagnostics.json` for full detail)

1. **Primary root cause (measured, not assumed):** two leftover, never-properly-finalized promotions from Task 64.2's ad-hoc smoke testing (candidate "swimming championship" and "smaragd club") carried raw, unprocessed candidate-proposal boilerplate text that spuriously dominated retrieval for any "do you remember..." phrased question. Measured via 20 retrieval-only probes: 65% raw top-5 hit rate for the target memory with the stale artifacts present, 95% without them (pure post-hoc simulation, no code change). Retired both (Qdrant point deletion + `failed` status with full audit trail) after explicit user confirmation.
2. **Deterministic query-intent classification** (`avatar_persona/memory_query_intent.py`): a narrow, marker-based classifier distinguishing `direct_factual_memory` / `corrected_memory_fact` / `correction_history` / `multiple_perspective_question` / `unknown_or_ambiguous`, with zero case-specific or fact-specific content (tested against an unrelated topic phrased the same way).
3. **Scoped multi-query retrieval** (`demo_fa_chat/service.py`), isolated to corrected-memory intent only: issues the original query (unchanged) plus one generic, fact-agnostic expansion query, merges deterministically by chunk_id, over-fetches a small bounded pool so the existing dispute-evidence filter can drop an item without shrinking the final evidence set below normal top_k. Ordinary questions take the exact single-query path unchanged.
4. **Deterministic evidence prioritization** (`ai_agents/brain/context.py`): floats a verified learned memory to the front of the evidence list and caps the count for corrected-memory-intent turns, reducing dilution from unrelated archival items — the single highest-impact fix for Brain answer reliability, found by directly following the task's own guidance to "prefer deterministic pre-Brain evidence resolution... do not rely only on prompt wording" after prompt-only iterations plateaued around 60-80% answer correctness.
5. **Narrow prompt refinement** (`learned_memory_answer_policy_v3_1`): two targeted clarifications (unrelated archival items don't indicate missing evidence; "what was corrected" questions want the current fact, not a correction-event narrative) plus a per-item inline annotation — applied only after evidence-ordering alone was measured insufficient, per Part K's explicit guidance.
6. **Three real evaluator precision bugs**, found via full frozen-evaluation runs against the real Brain provider (not assumed, each reproduced and fixed with a regression test):
   - Multi-word marker proximity matching spanning an unrelated sentence boundary (e.g. "...перед сном." + "А вот «Катюшу»..." falsely matching "Катюшу перед сном").
   - `"но не X"` ("but not X") incorrectly treated as resetting negation scope instead of continuing it.
   - `DIRECT_LACK_DENIAL_PREFIXES` requiring the denial at the literal start of the answer, which real answers (which open with a warm address) never satisfy.
   - A robustness gap where a single runtime/network failure among 36 evaluation calls crashed the entire summary computation instead of being recorded as one failed run.

## Generalization and safety confirmation

- No hardcoded song title, case ID, or dataset question anywhere in the new code (verified by a dedicated test using a completely different topic phrased the same way).
- No unrelated owner memory is ever boosted merely for being owner-approved — prioritization only applies within the already-retrieved, already-filtered candidate pool for turns classified as corrected-memory intent, and only distinguishes verified-vs-archival, not "owned by X".
- Ordinary factual retrieval is provably unchanged: the non-expansion branch issues the exact same single `retrieve_profile_rag` call with the exact same default `top_k` as before this task.
- `top_k` was never changed; a small, explicit, documented, tested pool over-fetch is used only for corrected-memory-intent turns and the final evidence count delivered to the Brain never exceeds the profile's configured top_k.
- No global recency boost was added.
