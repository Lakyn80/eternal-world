# Eternal World

Production-ready MVP base for AI memory social platform.

## Stack

- Backend: FastAPI
- Frontend: Next.js + React + TypeScript
- Database: PostgreSQL
- Containers: Docker Compose
- Backend tests: pytest
- Frontend tests: Vitest
- CI: GitHub Actions

## Dual Production Deploy (Russia + Hetzner)

Canonical guide: [`docs/DUAL_PRODUCTION_DEPLOYMENT.md`](docs/DUAL_PRODUCTION_DEPLOYMENT.md).

- Workflow: `.github/workflows/deploy-production.yml`
- Production branch: `staging/eternalworld-lukiora-20260715`
- One GHCR build per commit SHA → deploy to Russia and/or Hetzner
- Manual `workflow_dispatch` input `deployment_target`: `both` | `russia` | `hetzner`
- Environments: `production-russia`, `production-hetzner`
- Hetzner compose/nginx: `deploy/hetzner/`
- Hetzner ports (loopback): backend `8133`, frontend `3117`

## Staging Deploy (legacy Russia-only)

The test server target is `https://eternalworld.lukiora.ru`.

Prefer the dual production workflow above for new deploys. The legacy
manual Russia-only workflow remains available:

Key runtime decisions:

- Production deploy uses prebuilt GHCR images, so the server does not `pip install` the backend on every deploy.
- Heavy Python AI dependencies are shared through the GHCR base image `ghcr.io/lakyn80/python-ai-base-py312:py312-v1`, so projects built from the same base reuse identical Docker layers on the server.
- Hugging Face model downloads are shared across projects through the external Docker volume `shared_huggingface_cache`.
- The backend stays on Python `3.12` to match the repo runtime; the older `ghcr.io/lakyn80/python-ai-base:1` image is Python `3.11` and is intentionally not used here.

Files involved:

- Shared AI base image: `backend/Dockerfile.ai-base`
- Compose: `docker-compose.prod.yml`
- Backend image: `backend/Dockerfile.prod`
- Frontend image: `frontend/Dockerfile.prod`
- Nginx templates: `infra/nginx/eternalworld.lukiora.ru*.conf`
- Workflow: `.github/workflows/deploy-staging.yml`

Required GitHub repository secrets:

- `STAGING_SSH_PRIVATE_KEY`
- `STAGING_POSTGRES_DB`
- `STAGING_POSTGRES_USER`
- `STAGING_POSTGRES_PASSWORD`
- `STAGING_JWT_SECRET_KEY`
- `STAGING_AI_BRAIN_PROVIDER`
- `STAGING_AI_BRAIN_BASE_URL`
- `STAGING_AI_BRAIN_MODEL`
- `STAGING_AI_BRAIN_API_KEY`
- `STAGING_CONTENT_TRANSLATION_PROVIDER`
- `STAGING_CONTENT_TRANSLATION_BASE_URL`
- `STAGING_CONTENT_TRANSLATION_MODEL`
- `STAGING_CONTENT_TRANSLATION_API_KEY`

Optional GitHub repository secrets:

- `LETSENCRYPT_EMAIL`

What the workflow does:

1. Builds and pushes the shared Python `3.12` AI base image to GHCR.
2. Builds and pushes backend/frontend images to GHCR.
3. Copies `docker-compose.prod.yml`, `.env.prod`, and nginx config to `/opt/eternal-world`.
4. Ensures the shared model cache volume exists.
5. Bootstraps nginx and Let's Encrypt for `eternalworld.lukiora.ru`.
6. Starts `db`, `redis`, and `qdrant`.
7. Runs Alembic migrations.
8. Prefetches the BGE-M3 model into the shared Hugging Face cache.
9. Ensures the active retrieval Qdrant collection exists (`python scripts/ensure_active_retrieval_collection.py`).
10. Seeds the RU E2E demo profile with `python scripts/bootstrap_family_avatar_ru_e2e.py`.
11. Starts `backend`, `celery_worker`, and `frontend`.

Manual server-side verification after deploy:

```bash
cd /opt/eternal-world
docker compose --env-file .env.prod -f docker-compose.prod.yml ps
curl http://127.0.0.1:8033/health/runtime
curl -I https://eternalworld.lukiora.ru/cs
```

## Local Monitoring

The backend exposes Prometheus metrics at `http://localhost:8033/metrics`.

Start Eternal World metrics collection without a second Grafana:

```bash
docker compose up -d backend prometheus
```

### Local Celery observability (optional profile)

Flower (UI) + `celery-exporter` (Prometheus metrics) are **local-only** and
gated behind Compose profile `celery-observability`. They are not part of
default `docker compose up` and are **not** deployed to staging.

```bash
docker compose --profile celery-observability up -d flower celery_exporter
# reload Prometheus so it can scrape the new target (if Prometheus already ran)
docker compose up -d prometheus
```

- Flower UI: `http://127.0.0.1:5555` (basic auth `admin` / `local-flower-dev`)
- Exporter metrics: scraped only inside Docker as `celery_exporter:9808` (no host port)
- Prometheus job: `eternal_world_celery_exporter`

Stop when done:

```bash
docker compose --profile celery-observability stop flower celery_exporter
docker compose --profile celery-observability rm -f flower celery_exporter
```

Notes:

- Flower does not push to Prometheus; Prometheus scrapes `celery_exporter`.
- App metrics (`async_jobs_*`, `async_queue_depth`, …) on `backend:8000/metrics` stay unchanged.
- Richer Celery *task event* series from the exporter may be sparse until workers emit events; broker queue visibility still works without changing worker commands.

Local URLs:

- Prometheus: `http://localhost:9090`
- Shared Grafana (owned by the sibling NALUS stack): `http://localhost:3002`
- Eternal World dashboard: `http://localhost:3002/d/eternal-world-fa-chat`

The shared Grafana reads Eternal World Prometheus through datasource UID
`eternal-world-prometheus`; NALUS and Eternal World retain separate Prometheus storage.

The standalone Eternal World Grafana remains available for troubleshooting only:

```bash
docker compose --profile standalone-grafana up -d grafana
```

It uses `http://localhost:3001` and the configured local-development credentials. **Do not leave it running** alongside the shared UI — day-to-day use `http://localhost:3002` only. Stop and remove the container after troubleshooting:

```bash
docker compose stop grafana
docker compose rm -f grafana
```

Do not remove its named volume (`eternal_world_grafana_data`).

Direct dashboard URL (shared UI only):

`http://localhost:3002/d/eternal-world-fa-chat`

Empty panels usually mean **No data** for that metric in the selected time range (for example `fa_chat_*` until someone sends a Family Avatar chat), not a broken Grafana. Confirm datasource health and `up{job="eternal_world_backend"}==1` in Explore with datasource **Eternal World Prometheus**.

Provisioned files:

- Prometheus config: `monitoring/prometheus/prometheus.yml`
- Grafana datasource: `monitoring/grafana/provisioning/datasources/prometheus.yml`
- Grafana dashboards: `monitoring/grafana/dashboards/fa_chat_observability.json`

Verification:

```bash
docker compose config --quiet
docker compose --profile standalone-grafana config --quiet
docker compose --profile celery-observability config --quiet
curl http://localhost:8033/metrics
curl http://localhost:9090/-/ready
curl http://localhost:3002/api/health
```
