# Full-Version Embedding Benchmark Runbook

## Status

- Runbook only.
- Do not execute this benchmark as part of the current task.
- Real benchmark execution must happen later in controlled manual batches.

## Goal

Benchmark the next full-version embedding candidates without rerunning historical providers unnecessarily and without overwriting preserved production-facing artifacts.

## Planned Batch Order

- Batch A: `multilingual_e5_large`
- Batch B: `qwen3_embedding_0_6b`
- Batch C: `jina_embeddings_v3`
- Batch D: optional `qwen3_embedding_4b`
- Batch E: optional `qwen3_embedding_8b`
- Batch F: BGE-M3 full hybrid mode after design implementation

## Why Not Run All Real Models At Once

- RAM pressure becomes harder to predict.
- Large model downloads can hide unrelated benchmark failures.
- Runtime duration becomes too long for targeted debugging.
- Mixed failure causes make it unclear whether the problem is one model, one provider path, or one dataset slice.
- Artifact interpretation becomes harder when several new models fail at different stages in one run.

## Manual-Only Guardrails

- Require `REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1`.
- Require an explicit provider list for non-historical benchmark batches.
- Never rerun historical providers unless explicitly requested.
- Never overwrite preserved production-facing artifacts such as `latest_real`.
- Keep fake/report validation separate from real benchmark execution.
- Run one real model batch at a time.

## Suggested Preflight Test Order

1. Focused registry tests.
2. Provider metadata tests.
3. Dataset invariant tests.
4. Fake-safe benchmark config tests.
5. Full backend pytest.
6. One real model batch at a time.

## Recommended Focused Test Batches

### Batch 1

- `python -m pytest tests/test_embedding_models.py tests/test_embedding_benchmark_foundation.py -q`

### Batch 2

- `python -m pytest tests/test_embeddings_sentence_transformers.py tests/test_embeddings.py -q`

### Batch 3

- `python -m pytest tests/test_multi_embedding_eval.py tests/test_real_question_eval.py -q`

### Batch 4

- `python -m pytest -q`

## Future Manual Benchmark Execution Pattern

### Batch A example

- Use the future manual command path with provider list limited to `multilingual_e5_large`.
- Confirm artifact output is written to a clearly separated benchmark location.
- Review memory use, runtime, and retrieval traces before moving to Batch B.

### Batch B example

- Limit provider list to `qwen3_embedding_0_6b`.
- Keep model loading and artifact review isolated from Batch A.

### Batch C example

- Limit provider list to `jina_embeddings_v3`.
- Confirm long-context and task-adapter benchmark cases are included only if the manual dataset slice calls for them.

## Historical Provider Rule

- `multilingual_e5_small`, `bge_m3`, `paraphrase_multilingual_mpnet_base_v2`, and `multilingual_e5_base` already have established benchmark context.
- Do not rerun historical providers as part of the next batch sequence unless the user explicitly requests a fresh comparison or a compatibility rerun.

## Artifact Safety

- Keep planning artifacts separate from result artifacts.
- Keep future benchmark outputs separate from:
  - `backend/artifacts/real_question_eval/latest_real/`
  - `backend/artifacts/real_question_eval/latest_incremental_new_providers/`
- Require batch-specific output folders before the real benchmark starts.
