# Roadmap v2

Items intentionally deferred after v0.1 client-ready release.

## Retrieval modes

- BGE-M3 hybrid Batch D (`dense+sparse`, `dense+sparse+multivector`)
- optional FlagEmbedding integration

## Dataset tooling

- eval JSON generator from corpus + heuristics
- marker suggestion assistant for client onboarding

## Runtime

- async/Celery execution for long multi-model runs
- progress reporting and resumable benchmark batches

## Distribution

- public PyPI publish
- GitHub Actions release workflow (wheel + tag)

## Eternal World integration

- replace parts of `run_real_question_eval.py` with `rag-eval` CLI
- shared registry source instead of copied `registry.py`

## Adapter ecosystem

- documented adapter conformance tests
- optional Redis/Weaviate backends
