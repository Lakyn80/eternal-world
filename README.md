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

To start the local monitoring stack:

```bash
docker compose up -d backend prometheus grafana
```

Local URLs:

- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3001`

Local Grafana login:

- username: `admin`
- password: `admin`

This default Grafana credential pair is for local development only and must be changed for production.

Provisioned files:

- Prometheus config: `monitoring/prometheus/prometheus.yml`
- Grafana datasource: `monitoring/grafana/provisioning/datasources/prometheus.yml`
- Grafana dashboards: `monitoring/grafana/dashboards/fa_chat_observability.json`

Verification:

```bash
docker compose config
curl http://localhost:8033/metrics
curl http://localhost:9090/-/ready
curl http://localhost:3001/api/health
```
