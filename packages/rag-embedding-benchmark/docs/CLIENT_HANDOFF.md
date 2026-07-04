# Client handoff checklist

Use this when delivering `rag-embedding-benchmark` to an external client.

## 1. Install

```bash
pip install "rag-embedding-benchmark[sql-qdrant] @ ./rag_embedding_benchmark-0.1.0-py3-none-any.whl"
# or
pip install "rag-embedding-benchmark[sql-qdrant] @ git+https://github.com/Lakyn80/eternal-world.git@v0.1.0#subdirectory=packages/rag-embedding-benchmark"
```

## 2. Client prerequisites

- [ ] Postgres (or compatible SQL) with chunked corpus
- [ ] Qdrant reachable from benchmark runtime
- [ ] Known `source_id`
- [ ] Chunk metadata includes `source_document_id` aligned with eval JSON
- [ ] Eval JSON with questions + required/forbidden markers

## 3. Config files to deliver

- [`examples/rag_eval.client.yaml`](../examples/rag_eval.client.yaml)
- [`examples/my_eval.template.json`](../examples/my_eval.template.json)
- client-specific eval JSON (co-authored)

## 4. Integration choice

| Client stack | Backend |
|--------------|---------|
| Postgres `rag_chunks`-like table + Qdrant | `sql_qdrant` |
| Custom pipeline | `custom` + [`custom_adapter_template.py`](../examples/custom_adapter_template.py) |

## 5. Run sequence

```bash
export DATABASE_URL=...
export QDRANT_URL=...
export SENTENCE_TRANSFORMERS_DEVICE=cpu

rag-eval validate --config rag_eval.client.yaml
rag-eval run --config rag_eval.client.yaml
```

## 6. Deliverables back to client

- `ranking.json`
- `report.md`
- recommended `winner.model_code`
- short rationale (hit rate, distractor safety, latency if relevant)

## 7. Typical effort

| Task | Estimate |
|------|----------|
| Package install + config | 0.5 day |
| Chunk metadata mapping | 0.5–1 day |
| Eval JSON authoring | 1–2 days |
| Benchmark run (CPU, 2–7 models) | hours to 1 day |

## 8. Internal verification (already done)

Eternal World Docker smoke test:

```bash
docker compose exec backend python scripts/run_rag_eval_smoke.py
```

Expected: validate PASS, run PASS, winner model in `backend/artifacts/rag_eval_smoke/ranking.json`.
