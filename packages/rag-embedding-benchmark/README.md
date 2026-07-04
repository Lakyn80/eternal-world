# rag-embedding-benchmark

Compare RAG embedding models against a custom eval dataset using your existing database, Qdrant, and chunked corpus.

## What you need before running

- Postgres (or compatible DB) with RAG chunks for a known `source_id`
- Qdrant reachable from the runtime
- Eval JSON with questions, required/forbidden evidence markers, and source scope
- CPU-only runs by default (`device: cpu`)

## Install

```bash
cd packages/rag-embedding-benchmark
pip install -e ".[sql-qdrant,dev]"
```

For Eternal World internal development:

```bash
pip install -e ".[eternal-world,dev]"
```

Distribution for clients:

```bash
pip install git+https://github.com/you/rag-embedding-benchmark.git@v0.1.0
# or
pip install rag_embedding_benchmark-0.1.0-py3-none-any.whl
```

## Quick start for external clients (recommended)

1. Copy [`examples/rag_eval.client.yaml`](examples/rag_eval.client.yaml) and [`examples/my_eval.template.json`](examples/my_eval.template.json)
2. Set `DATABASE_URL`, `QDRANT_URL`, `source_id`, and model list
3. Validate, then run:

```bash
export DATABASE_URL=postgresql+psycopg://...
export QDRANT_URL=http://localhost:6333
rag-eval validate --config rag_eval.client.yaml
rag-eval run --config rag_eval.client.yaml
```

Outputs land in `artifact_dir`:

- `ranking.json`
- `report.md`
- `runs/<timestamp>/...`

See [`docs/CLIENT_ONBOARDING.md`](docs/CLIENT_ONBOARDING.md) for the full client checklist.

## Backend options

| `backend` | Use case |
|-----------|----------|
| `sql_qdrant` | Generic Postgres chunks + SentenceTransformers + Qdrant |
| `custom` | Client implements `RagEvalBackend` (see [`examples/custom_adapter_template.py`](examples/custom_adapter_template.py)) |
| `eternal_world` | Internal Eternal World stack only ([`examples/rag_eval.yaml`](examples/rag_eval.yaml)) |

Custom adapter config:

```yaml
backend: custom
adapter:
  module: my_project.rag_eval_adapter
  class: MyProjectRagEvalBackend
  kwargs:
    database_url: ${DATABASE_URL}
    qdrant_url: ${QDRANT_URL}
```

## Optional high-RAM models

Qwen 4B and 8B are opt-in because they can OOM on typical Docker memory limits:

```yaml
models:
  include_optional: true
```

## Custom corpus contract

Your eval JSON must align with the corpus already chunked in DB:

- `cases[].required_evidence` / `forbidden_evidence` markers must exist in scoped source text or chunks
- `source_scope.document_ids` must match chunk metadata such as `source_document_id`
- distractor cases also require forbidden markers to be present in the scoped corpus

Use `rag-eval validate` before a long benchmark run.

## Internal Docker smoke test

From repo root:

```bash
docker compose exec backend python scripts/run_rag_eval_smoke.py
```

Uses `sql_qdrant` against the sample eval dataset with two lightweight models.

See [`docs/CLIENT_HANDOFF.md`](docs/CLIENT_HANDOFF.md) for the full client checklist.

## Build wheel

From repo root (recommended when host pip/build has network issues):

```bash
docker compose exec backend bash -lc "pip install -q build && cd /packages/rag-embedding-benchmark && python -m build"
```

Wheel output: `packages/rag-embedding-benchmark/dist/rag_embedding_benchmark-0.1.0-py3-none-any.whl`

On host:

```powershell
packages/rag-embedding-benchmark/scripts/build_wheel.ps1
```

## Tests

```bash
pytest
```

The in-memory adapter tests run without Docker, DB, or Qdrant.

## MVP scope

Included in v0.1:

- `sql_qdrant` generic adapter
- custom adapter plugin loading
- Eternal World adapter for internal dev
- dense SentenceTransformers models from the shared registry
- dataset JSON loader + preflight validation
- ranking report and failed-model capture (OOM/load errors do not abort the whole run)

Planned for v2:

- BGE hybrid Batch D modes
- async/Celery execution
- eval JSON generator from corpus
