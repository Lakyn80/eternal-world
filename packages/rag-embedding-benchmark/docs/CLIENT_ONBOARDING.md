# Client onboarding for rag-embedding-benchmark

Use this checklist before offering or running a client benchmark.

## What the client must have ready

1. **Chunked corpus in DB** for a known `source_id`
2. **Qdrant** reachable from the benchmark runtime
3. **Eval JSON** with aligned questions, markers, and `source_scope`
4. **Chunk metadata** containing `source_document_id` values that match eval scope document IDs
5. **CPU runtime** with enough RAM for chosen models (Qwen 4B/8B are opt-in)

## Integration paths

| Path | When to use |
|------|-------------|
| `backend: sql_qdrant` | Client has Postgres-like chunks table + Qdrant; fastest start |
| `backend: custom` | Client has non-standard schema or custom embed/index pipeline |
| `backend: eternal_world` | Internal Eternal World development only |

## Recommended client flow

```bash
pip install "rag-embedding-benchmark[sql-qdrant]"

export DATABASE_URL=postgresql+psycopg://...
export QDRANT_URL=http://localhost:6333
export SENTENCE_TRANSFORMERS_DEVICE=cpu

rag-eval validate --config rag_eval.client.yaml
rag-eval run --config rag_eval.client.yaml
```

Deliverables to client:

- `ranking.json`
- `report.md`
- recommended `winner.model_code`

## Eval JSON contract

Each case needs:

- `question`
- `test_type` (`short_fact`, `page_level`, `multi_document`, `negative`, `distractor`)
- `source_scope` with `document_ids` aligned to chunk metadata
- `required_evidence` markers present in scoped corpus/chunks
- for `distractor`, `forbidden_evidence` markers must also exist in scoped corpus

Run `rag-eval validate` before any long benchmark. Fix all preflight issues first.

## Distribution options

| Channel | Command |
|---------|---------|
| Private git | `pip install git+https://github.com/you/rag-embedding-benchmark.git@v0.1.0` |
| Wheel handoff | `pip install rag_embedding_benchmark-0.1.0-py3-none-any.whl` |
| Editable monorepo dev | `pip install -e packages/rag-embedding-benchmark[sql-qdrant,dev]` |

## Commercial handoff package

What you deliver:

1. installed wheel or git tag
2. filled `rag_eval.client.yaml`
3. client-specific eval JSON (or co-authored template)
4. adapter implementation if `backend: custom`
5. final ranking report + model recommendation

Typical effort beyond the pip package itself: mapping chunk metadata + writing eval JSON (1–3 days depending on corpus size).
