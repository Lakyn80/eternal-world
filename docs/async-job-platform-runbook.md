# Async Job Platform & Embedding Worker Runbook

Task 65.9 — Scalable Asynchronous Job Platform, Dedicated Embedding Workers,
Self-Healing Provider Recovery, and 100k-User Readiness Foundation.

All commands below are exact, repository-specific, and assume the local
dev stack (`docker-compose.yml`). For production (`docker-compose.prod.yml`)
substitute the compose file and container names accordingly.

## 1. API liveness and readiness

```bash
curl -s http://localhost:8033/health          # liveness only
curl -s http://localhost:8033/health/runtime   # DB + Redis reachability
```

`/health` must always return `200` even if Redis/Postgres/Qdrant/the
embedding provider are unavailable — it is process liveness only.
`/health/runtime` degrades explicitly (`"status": "degraded"`) rather than
raising. FastAPI never initializes BGE-M3, so a completely cold/never-warmed
embedding provider **does not** affect either endpoint.

## 2. Embedding worker health

The embedding worker never loads the model until its first real embedding
task; there is no dedicated `/health` port on it (no port is published at
all — Part N). Check its process and recent activity instead:

```bash
docker compose ps embedding_worker
docker compose logs --tail=200 embedding_worker
```

Look for `[bge_m3_hybrid] load success ...` (model loaded) vs repeated
`load failed` / `probe failed` lines. Provider health is also exposed as
Prometheus gauges (see §7): `embedding_provider_health{model_code=...,
state=...}` — the `state` label with value `1` is the current state.

## 3. Embedding queue depth

```bash
docker compose exec redis redis-cli -n 1 LLEN embedding
```

(Celery/Kombu with the Redis transport stores queued messages as a Redis
list per queue name; `1` is `CELERY_BROKER_URL`'s DB index in this repo.)

## 4. Oldest queued job age

```bash
docker compose exec db psql -U eternal_user -d eternal_world -c "
  SELECT id, job_type, queue, status, created_at,
         EXTRACT(EPOCH FROM (now() - created_at)) AS age_seconds
  FROM background_jobs
  WHERE status IN ('pending','queued','running','retry_scheduled','recovery_pending')
  ORDER BY created_at ASC LIMIT 10;"
```

Also exposed as the `async_oldest_job_age_seconds{queue="embedding"}`
gauge if a metrics-refresh task is wired to `set_async_oldest_job_age_seconds`
(see Known Limitations — this gauge's setter exists but is not yet
scheduled by default).

## 5. Outbox backlog

```bash
docker compose exec db psql -U eternal_user -d eternal_world -c "
  SELECT status, count(*) FROM job_outbox_events GROUP BY status;"
```

A growing `pending` count with `last_error` populated means the broker is
unreachable from the worker/dispatcher side — see §14.

## 6. Find a failed indexing job

```bash
docker compose exec db psql -U eternal_user -d eternal_world -c "
  SELECT id, job_type, queue, safe_error_category, error_message,
         attempt_count, provider_recovery_count, fresh_process_retry_used,
         worker_recycle_requested, finished_at
  FROM background_jobs
  WHERE status = 'failed'
  ORDER BY finished_at DESC LIMIT 20;"
```

`safe_error_category = 'provider_corrupt'` + `fresh_process_retry_used =
true` + `worker_recycle_requested = true` means the bounded self-healing
policy (Part M) ran its full 3-attempt bound and still failed — see §8/§9.

## 7. Provider-health metrics

```bash
curl -s http://localhost:8033/metrics | grep -E "embedding_provider_|async_jobs_|outbox_"
```

Key series: `embedding_provider_health`, `embedding_provider_initialization_total`,
`embedding_provider_meta_parameter_total`, `embedding_provider_reload_total`,
`embedding_provider_probe_failure_total`, `embedding_provider_recovery_total`,
`embedding_worker_recycle_request_total`, `embedding_indexing_final_failure_total`.

Note: these metrics are exposed by whichever process calls `/metrics` —
today that is the `backend` (FastAPI) process's own Prometheus registry.
Because FastAPI never initializes the embedding provider, **the embedding
worker's own provider-health series are only visible if `/metrics` is
scraped directly on the embedding worker process** in a future change that
exposes it there too; today, cross-process Prometheus registries are not
shared (each Python process has its own in-memory `prometheus_client`
registry). This is a known limitation — see §17.

## 8. Identifying meta-device corruption specifically

```bash
docker compose logs embedding_worker | grep -i "meta tensor\|cannot copy out of meta"
```

Or query jobs with `safe_error_category = 'provider_corrupt'` (§6). The
integrity probe (`app/modules/embeddings/provider_integrity.py`) uses the
fixed harmless string `PROVIDER_INTEGRITY_PROBE_TEXT` and classifies any
probe failure — meta-device or otherwise — the same way.

## 9. Retry one failed memory safely

Never edit the database by hand. Use the existing authorized endpoints:

- Approved conversation/biography memory: `POST
  /api/memorials/{profile_id}/candidates/{candidate_id}/index` (also the
  retry action for a `failed` promotion) — returns `202` with `job_id`.
- Memorial contribution: `POST
  /api/memorials/{profile_id}/contributions/{contribution_id}/retry-indexing`
  — returns `202`.

Then poll `GET /api/jobs/{job_id}` (owner-scoped) until `status` is
`succeeded` or `failed`.

## 10. Restart only the embedding worker

```bash
docker compose restart embedding_worker
```

This never restarts `backend`, `celery_worker`, `db`, `redis`, or `qdrant`.
PostgreSQL is the source of truth for job state, so any in-flight job is
recovered by the stale-job maintenance sweep (§13), not lost.

## 11. Scale embedding-worker replicas

```bash
docker compose up -d --scale embedding_worker=3
```

Each replica runs `--concurrency=1 --prefetch-multiplier=1`, so 3 replicas
means at most 3 embedding jobs processed concurrently — throughput scales
by adding replicas, never by raising concurrency against one loaded model.

## 12. Confirm exactly one deterministic Qdrant point exists

```bash
docker compose exec db psql -U eternal_user -d eternal_world -c "
  SELECT qdrant_point_id, target_collection_name, promotion_status
  FROM avatar_memory_promotions WHERE id = <promotion_id>;"
```

Then check Qdrant directly:

```bash
curl -s "http://localhost:6335/collections/<collection_name>/points/<qdrant_point_id>"
```

Point ids are `uuid5(NAMESPACE_URL, f"...promotion:{id}:...")` — deterministic
per promotion, so re-running indexing never creates a second point for the
same promotion.

## 13. Recover stale jobs

Automatic: the `maintenance_worker` container runs `run_stale_job_recovery_job`
on an embedded beat schedule (every 60s — see `app/worker/celery_app.py`'s
`beat_schedule`). To trigger it manually:

```bash
docker compose exec backend python -c "
from app.worker.tasks import run_stale_job_recovery_job
print(run_stale_job_recovery_job())"
```

## 14. Distinguishing broker failure from provider failure

- **Broker failure**: `job_outbox_events.status = 'pending'` with a growing
  `attempts`/`last_error` (e.g. `ConnectionError`); `background_jobs.status`
  stays `pending` (never `recovery_pending`/`failed` for this reason alone).
- **Provider failure**: `background_jobs.safe_error_category IN
  ('provider_corrupt','provider_initialization_failed','invalid_embedding_output')`
  with `status IN ('recovery_pending','failed')`.

These are structurally distinct code paths — a broker outage never touches
`provider_recovery_count`/`fresh_process_retry_used`, and a provider
corruption never touches the outbox's own `attempts`/`last_error`.

## 15. Why restarting the entire server is normally wrong

Restarting `backend`/`celery_worker` (a) discards no state (PostgreSQL is
authoritative) but (b) is a blunt, all-or-nothing action that briefly drops
every in-flight HTTP request and every other queue's in-flight task, not
just the one broken embedding process — exactly the manual, non-reproducible
recovery step Task 65.9 exists to make unnecessary. Restart only the
specific container implicated (§10), and only when automatic bounded
self-healing (Part M) has already been exhausted (`worker_recycle_requested
= true` and the job is still not resolved after the container's own
`restart: unless-stopped` policy should have already recreated it — if it
hasn't, that itself is worth investigating before restarting again).

## 16. Confirming PostgreSQL/Redis/Qdrant were not reset

```bash
docker compose exec db psql -U eternal_user -d eternal_world -c "\dt" | wc -l   # table count unchanged
docker volume ls | grep eternal_world   # eternal_world_postgres_data / _redis_data / _qdrant_data still present
```

None of Task 65.9's changes touch these volumes; restarting `embedding_worker`
or `maintenance_worker` never runs a migration or a data reset.

## 17. Alerts that require operator action

- `outbox_pending_total` growing and not draining for >5 minutes → broker
  unreachable from the dispatcher; check Redis connectivity.
- `embedding_indexing_final_failure_total` increasing → jobs are reaching
  permanent provider-corruption failure after the full bounded retry — the
  embedding worker's environment likely needs real investigation (model
  cache corruption, disk full, out-of-memory), not just another restart.
- `async_oldest_job_age_seconds{queue="embedding"}` above your SLO for
  indexing latency → scale up `embedding_worker` replicas (§11) or
  investigate a stuck worker.
- Repeated `embedding_worker_recycle_request_total` increments in a short
  window → the embedding worker's environment (not just one job) is
  unhealthy; investigate before it becomes a customer-visible outage.

## 18. Running smoke / scale / stress load profiles

```bash
# smoke - local, fake provider/broker, small dataset, fully hermetic
# (isolated in-memory SQLite, no shared dev data touched). Safe to run
# anytime, anywhere, including this dev container:
docker compose exec -T -e HF_HUB_OFFLINE=1 -e TRANSFORMERS_OFFLINE=1 backend \
  python scripts/run_async_job_load_smoke.py --profile smoke --users 25

# scale - isolated staging only, NEVER against this dev stack or production:
docker compose -f docker-compose.prod.yml exec backend \
  python scripts/run_async_job_load_smoke.py --profile scale \
  --users 20000 --api-concurrency 50 --worker-replicas 4

# stress - deliberately exceeds capacity, verifies backpressure/degradation,
# isolated staging only:
docker compose -f docker-compose.prod.yml exec backend \
  python scripts/run_async_job_load_smoke.py --profile stress \
  --users 5000 --api-concurrency 500 --worker-replicas 4
```

See `backend/scripts/run_async_job_load_smoke.py` for the exact metrics
each profile records and PROJECT_PROGRESS.md's Task 65.9 entry for the
actual local `smoke` result (only `smoke` was run this session —
`scale`/`stress` print the prepared command and exit without executing,
since no isolated staging environment was available this session).
