# Extended Real Eval Dataset Plan

## Scope

- This is a planning artifact only.
- It does not change the default real question eval flow.
- It does not execute retrieval, embedding generation, or Qdrant indexing.

## Preserved Core Questions

The original Task 32 question IDs must remain unchanged and stay at the core of the benchmark:

- `question-sunflower-house`
- `question-winter-trip`
- `question-grandmother-soup`

## Planned Benchmark Categories

- short factual lookup
- multi-evidence question
- distractor-heavy question
- Czech query
- Russian query
- English query
- answer-not-available question
- similar-document conflict question
- long-context / distant evidence question

## Planned Dataset Shape

- Keep the original 3 Task 32 questions unchanged.
- Add new cases incrementally as planning-only definitions first.
- Tag each future case by category so benchmark slices can be run selectively.
- Keep the extended dataset disconnected from default real runs until the manual benchmark task is explicitly executed.

## Category Goals

### Short factual lookup

- Validate whether a model can recover a single precise fact quickly.

### Multi-evidence question

- Validate whether a model retrieves more than one supporting marker from different chunks.

### Distractor-heavy question

- Stress lexical traps and false positives.

### Czech query

- Validate Czech retrieval quality on non-English queries.

### Russian query

- Validate Russian retrieval quality on non-English queries.

### English query

- Preserve comparability with the existing benchmark style.

### Answer-not-available question

- Ensure the benchmark can reward honest lack-of-evidence behavior instead of hallucinated answers.

### Similar-document conflict question

- Check whether retrieval can separate near-duplicate records that disagree on one critical fact.

### Long-context / distant evidence question

- Stress models that claim stronger long-context handling.

## Guardrails

- Do not connect this dataset to `python scripts/run_real_question_eval.py` by default.
- Do not replace the current preserved historical datasets.
- Do not overwrite `latest_real`.
- Do not mix planning-only cases into historical comparison artifacts.
- Add future dataset cases only behind explicit manual benchmark execution.
