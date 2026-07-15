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

## Staging Deploy

The test server target is `https://eternalworld.lukiora.ru`.

Key runtime decisions:

- Production deploy uses prebuilt GHCR images, so the server does not `pip install` the backend on every deploy.
- Hugging Face model downloads are shared across projects through the external Docker volume `shared_huggingface_cache`.
- The backend stays on Python `3.12` to match the repo runtime; the existing `ghcr.io/lakyn80/python-ai-base:1` image is Python `3.11` and is not a drop-in base for this app yet.

Files involved:

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

- `GHCR_USERNAME`
- `GHCR_READ_TOKEN`
- `LETSENCRYPT_EMAIL`

What the workflow does:

1. Builds and pushes backend/frontend images to GHCR.
2. Copies `docker-compose.prod.yml`, `.env.prod`, and nginx config to `/opt/eternal-world`.
3. Ensures the shared model cache volume exists.
4. Bootstraps nginx and Let's Encrypt for `eternalworld.lukiora.ru`.
5. Starts `db`, `redis`, and `qdrant`.
6. Runs Alembic migrations.
7. Prefetches the BGE-M3 model into the shared Hugging Face cache.
8. Seeds the RU E2E demo profile with `python scripts/bootstrap_family_avatar_ru_e2e.py`.
9. Starts `backend`, `celery_worker`, and `frontend`.

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

It uses `http://localhost:3001` and the configured local-development credentials. Stop it
after troubleshooting with `docker compose stop grafana`. Do not remove its named volume.

Provisioned files:

- Prometheus config: `monitoring/prometheus/prometheus.yml`
- Grafana datasource: `monitoring/grafana/provisioning/datasources/prometheus.yml`
- Grafana dashboards: `monitoring/grafana/dashboards/fa_chat_observability.json`

Verification:

```bash
docker compose config --quiet
docker compose --profile standalone-grafana config --quiet
curl http://localhost:8033/metrics
curl http://localhost:9090/-/ready
curl http://localhost:3002/api/health
```
