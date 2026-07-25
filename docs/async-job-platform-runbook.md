# Async Job Platform & Embedding Worker Runbook

Task 65.9 — Scalable Asynchronous Job Platform, Dedicated Embedding Workers,
Self-Healing Provider Recovery, and 100k-User Readiness Foundation.
Extended by Task 65.9.1 — Queue Isolation, Async Status Polling, and
Production Scale Verification Closure (worker `-Q` restriction, §0/§13/§19;
periodic queue/job metric updater, §4a; expanded backpressure coverage;
disposable scale/stress profiles, §18/§20).

All commands below are exact, repository-specific, and assume the local
dev stack (`docker-compose.yml`). For production (`docker-compose.prod.yml`)
substitute the compose file and production container names.

## 0. Inspecting each worker's queue subscription (Task 65.9.1, Part D)

```bash
docker compose exec celery_worker celery -A app.worker.celery_app.celery_app inspect active_queues
docker compose exec embedding_worker celery -A app.worker.celery_app.celery_app inspect active_queues
docker compose exec maintenance_worker celery -A app.worker.celery_app.celery_app inspect active_queues
```

Each should report exactly the queues declared in that container's `-Q`
flag in `docker-compose.yml` — nothing else. Confirm the raw command lines
directly (no Celery broker round-trip needed):

```bash
docker compose exec celery_worker sh -c "ps aux | grep '[c]elery.*worker'"
```

should show `-Q document_processing,ai_generation,media,notifications`;
`embedding_worker` should show `-Q embedding`; `maintenance_worker` should
show `-Q maintenance`. The static Compose-topology contract test asserts
the same thing structurally (see §19).

## 0a. Confirming the general worker cannot consume `embedding`

```bash
docker compose exec celery_worker celery -A app.worker.celery_app.celery_app inspect active_queues | grep -i embedding
```

Must return **no output** — `celery_worker`'s `-Q` flag never includes
`embedding`. Cross-check the source of truth directly:

```bash
docker compose exec backend python -c "
from app.worker.celery_app import GENERAL_WORKER_QUEUES
assert 'embedding' not in GENERAL_WORKER_QUEUES
assert 'maintenance' not in GENERAL_WORKER_QUEUES
print(GENERAL_WORKER_QUEUES)"
```

## 0b. Confirming `embedding_worker` consumes only `embedding`

```bash
docker compose exec embedding_worker celery -A app.worker.celery_app.celery_app inspect active_queues
```

Must show exactly one queue, `embedding`. This is also the only container
with `EMBEDDING_WORKER_SELF_RECYCLE_ENABLED=true` (§10) and
`--concurrency=1 --prefetch-multiplier=1`.

## 0c. Confirming `maintenance_worker` consumes only `maintenance`

```bash
docker compose exec maintenance_worker celery -A app.worker.celery_app.celery_app inspect active_queues
```

Must show exactly one queue, `maintenance`. This container also runs the
embedded Beat scheduler (`-B`) — `outbox dispatch (15s)`,
`stale-job recovery (60s)`, and `async queue/job metric refresh (20s,
Task 65.9.1 §4a)` all run here, never on `celery_worker`/`embedding_worker`.

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

Also exposed as the `async_oldest_job_age_seconds{queue="embedding"}` gauge,
refreshed every 20 seconds by the maintenance worker's Beat schedule (§4a) —
no manual scrape timing assumptions needed.

## 4a. Periodic queue/job metric updater (Task 65.9.1, Part H)

`async_queue_depth{queue=...}` and `async_oldest_job_age_seconds{queue=...}`
existed as gauge *setters* since Task 65.9 but had no scheduled caller —
Task 65.9.1 wired a new Beat entry, `refresh-async-queue-metrics`, running
every **20 seconds** in `maintenance_worker` (`app.worker.celery_app`'s
`beat_schedule`). 20s: frequent enough that a backlog is visible within
roughly one scrape interval, cheap enough (a handful of grouped
`COUNT`/`MIN` queries over `background_jobs.status`/`.queue`/`.created_at`)
that it is negligible load even 3x more often than stale-job recovery, and
safely idempotent under any number of concurrent `maintenance_worker`
replicas (each run is a full re-read-and-set from the current
authoritative Postgres counts, never an increment).

Inspect directly:

```bash
curl -s http://localhost:8033/metrics | grep -E "^async_queue_depth|^async_oldest_job_age_seconds"
```

Every one of the six declared queues (`embedding`, `document_processing`,
`ai_generation`, `media`, `notifications`, `maintenance`) is always present
— a queue with zero active jobs reports `0`/`0.0` explicitly rather than
being absent or holding a stale prior value. A database failure during
refresh increments `async_queue_metrics_refresh_failure_total` (also
scraped above) and logs one structured `async_queue_metrics_refresh_failed`
event — it never raises into the Beat scheduler and never affects API
liveness (this task runs only in `maintenance_worker`, not `backend`).

Trigger it manually (e.g. right after seeding test jobs):

```bash
docker compose exec backend python -c "
from app.worker.tasks import run_async_queue_metrics_refresh_job
print(run_async_queue_metrics_refresh_job())"
```

## 4b. Inspecting stuck polling states (frontend/API perspective)

The frontend job-status poller (`frontend/react-export/src/hooks/
useJobStatusPoller.ts`) polls `GET /api/jobs/{job_id}` until a terminal
state. If a user reports a stuck "pending"/"processing" indicator:

```bash
# 1. Confirm the job the frontend is polling actually exists and is owned
#    by that account (a 404 here means the frontend has a stale/foreign
#    job id - it should already have cleared it per Part F.11):
curl -s -H "Authorization: Bearer <token>" http://localhost:8033/api/jobs/<job_id>

# 2. Check whether the job is *genuinely* stuck server-side vs. still
#    correctly polling (this is the same job-freshness check as §4/§6):
docker compose exec db psql -U eternal_user -d eternal_world -c "
  SELECT id, status, queue, heartbeat_at, next_attempt_at, attempt_count,
         max_attempts, safe_error_category
  FROM background_jobs WHERE id = <job_id>;"
```

- `status IN ('pending','queued')` with no `heartbeat_at` for longer than
  the outbox dispatch interval (15s) → check §5 (outbox backlog) — the
  job may be stuck at the broker-publish step, not the worker.
- `status = 'running'` with a stale `heartbeat_at` → will self-heal via
  stale-job recovery (§13) within `JOB_STALE_HEARTBEAT_TIMEOUT_SECONDS`.
- `status = 'recovery_pending'` → provider self-healing in progress (§8);
  expected to resolve within the bounded 3-attempt policy.
- Frontend never shows "stuck" indefinitely without cause: the poller
  backs off to a 12s cap (never polls forever at 1s) and pauses to a 20s
  cadence while the tab is hidden, resuming immediately on refocus.

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

## 11a. Comparing queue drain throughput before/after scaling

```bash
# 1. Snapshot queue depth and oldest age before scaling:
curl -s http://localhost:8033/metrics | grep 'queue="embedding"'

# 2. Scale up (or down):
docker compose up -d --scale embedding_worker=3

# 3. Generate a burst of embedding-queue work (isolated disposable
#    environment only - see §18/§20, never against this dev stack's real
#    data), then repeatedly sample the same series and time how long
#    async_queue_depth{queue="embedding"} takes to return to 0:
watch -n 5 "curl -s http://localhost:8033/metrics | grep 'queue=\"embedding\"'"
```

Adding embedding-worker replicas is expected to increase drain throughput
(more concurrent `--concurrency=1` processes = more jobs in flight at
once) — decreasing replicas must never affect *correctness* (no lost job,
no duplicate point), only how long draining the same backlog takes. If a
scale-up does not measurably reduce drain time, that is a result to report
honestly (Part L.8: "the result is documented honestly"), not evidence to
suppress.

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

All three profiles (Task 65.9.1) run inside **this same `backend`
container** — they are hermetic (in-memory SQLite database, fake
embedding provider, fake Qdrant writer, `unittest.mock.patch`-replaced
outbox sender) and never touch the real `db`/`redis`/`qdrant` services or
the shared dev/staging/production data those services hold. No
`docker compose down -v`, no reused production volume name, no real
DeepSeek call, no model download, in any of the three profiles.

```bash
# smoke - small dataset, quick correctness validation.
docker compose exec -T -e HF_HUB_OFFLINE=1 -e TRANSFORMERS_OFFLINE=1 backend \
  python scripts/run_async_job_load_smoke.py --profile smoke --users 25 --json

# scale - configurable registered-user cardinality (bulk SQL insert, up to
# 100,000+), a smaller "daily active" subset driven through the real HTTP
# flow at configurable concurrency, and a configurable simulated worker-
# replica count (reporting only - the actual draining loop is single-
# process, see the script's own module docstring for the exact, honest
# scope of what this measures):
docker compose exec -T -e HF_HUB_OFFLINE=1 -e TRANSFORMERS_OFFLINE=1 backend \
  python scripts/run_async_job_load_smoke.py --profile scale \
  --registered-users 100000 --daily-active-users 200 \
  --api-concurrency 16 --worker-replicas 2 --json

# stress - deliberately tightens per-user/global backpressure limits and
# drives a concurrent approval/indexing burst until 429/503 is observed,
# stopping on max-duration / error-rate / max-queued-job bounds:
docker compose exec -T -e HF_HUB_OFFLINE=1 -e TRANSFORMERS_OFFLINE=1 backend \
  python scripts/run_async_job_load_smoke.py --profile stress \
  --api-concurrency 32 --max-duration-seconds 60 \
  --error-rate-threshold 0.3 --max-queued-jobs 50 --json
```

To run any of these three profiles against **real** Postgres/Redis/Qdrant
in a genuinely separate, disposable environment (never this dev stack,
never staging/production), stand up an isolated Compose project first:

```bash
# A distinct COMPOSE_PROJECT_NAME gives every container/volume/network a
# distinct name (e.g. eternalworldloadtest_db, never eternal_world_db) -
# nothing here can collide with or be confused for the normal project.
COMPOSE_PROJECT_NAME=eternalworldloadtest docker compose \
  -f docker-compose.yml up -d db redis qdrant backend

# Run the same script inside that disposable project's backend container:
COMPOSE_PROJECT_NAME=eternalworldloadtest docker compose \
  -f docker-compose.yml exec -T backend \
  python scripts/run_async_job_load_smoke.py --profile scale \
  --registered-users 100000 --daily-active-users 200 --api-concurrency 16 --json

# Deterministic, disposable-only cleanup (never touches eternal_world_*):
COMPOSE_PROJECT_NAME=eternalworldloadtest docker compose \
  -f docker-compose.yml down -v
```

See `backend/scripts/run_async_job_load_smoke.py`'s module docstring for
the exact metrics each profile records, and PROJECT_PROGRESS.md's Task
65.9.1 entry for the actual measured local results (environment, exact
commands, and honest limitations of what was/was not executed this
session).

## 19. Static Compose-topology contract test

```bash
python -m pytest backend/tests_infra -q
```

Runs entirely with the **host** Python interpreter (see that module's
docstring: `docker-compose.yml`/`docker-compose.prod.yml` are not visible
from inside the `backend` container's bind-mounted `./backend` directory,
so this specific test cannot run via `docker compose exec backend
pytest`). Structurally parses both Compose files (never string-grep) and
asserts: `celery_worker` has an explicit `-Q document_processing,
ai_generation,media,notifications`; `embedding_worker` has `-Q embedding`
with `--concurrency=1 --prefetch-multiplier=1`; `maintenance_worker` has
`-Q maintenance`; none of the three worker services mount the Docker
socket, run privileged, or publish a port.

## 20. Detecting backpressure activation

```bash
# During/after a stress run, count 429/503 responses directly from the
# script's own JSON output (`status_counts`), or independently from the
# API layer:
curl -s -o /dev/null -w "%{http_code}\n" -X POST \
  -H "Authorization: Bearer <token>" \
  http://localhost:8033/api/rag-sources/<source_id>/process
```

`429` → per-user/per-profile active-heavy-job limit
(`max_active_heavy_jobs_per_user`/`_per_profile` in typed settings).
`503` with a `Retry-After` header → global saturation
(`global_heavy_job_saturation_limit`). Both are read straight from
PostgreSQL (`count_active_heavy_jobs_for_user/_profile/_global` in
`app/modules/job_tracking/repository.py`) on every API replica — never a
process-local counter, so the same limit holds regardless of which
replica serves the request (verified by the multi-replica harness, see
`backend/tests/test_task_65_9_1_multi_replica_harness.py`).

## 21. Cleaning only disposable test data safely

- **Hermetic smoke/scale/stress runs** (§18, in-container): nothing to
  clean up — the in-memory SQLite database and its `TestClient` app
  overrides are torn down automatically when the script process exits;
  nothing was ever written to the real `db`/`redis`/`qdrant` services.
- **Disposable Compose-project runs** (§18's `COMPOSE_PROJECT_NAME`
  variant): `docker compose -f docker-compose.yml down -v` **using that
  same `COMPOSE_PROJECT_NAME`** removes only that project's containers and
  volumes. Never run `down -v` without an explicit, verified
  `COMPOSE_PROJECT_NAME` pointing at the disposable project — see §22.

## 22. Confirming normal project volumes were not touched

```bash
docker volume ls | grep eternal_world
# expected: eternal_world_postgres_data, eternal_world_redis_data,
# eternal_world_qdrant_data, eternal_world_prometheus_data,
# eternal_world_grafana_data, eternal_world_bge_m3_cache - all present,
# none newly created/recreated (check timestamps if in doubt: `docker
# volume inspect eternal_world_postgres_data`).
docker compose ps   # normal project's containers still the same ones
  # (same CONTAINER ID / uptime as before the load test - a disposable
  # COMPOSE_PROJECT_NAME run never restarts or recreates these).
```
