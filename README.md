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
