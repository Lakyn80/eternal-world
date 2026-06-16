# Project Progress

## 1. Project Overview

Eternal World is a production-oriented AI memory social platform under active backend-first development. The repository currently contains:

- A FastAPI backend
- A Next.js + TypeScript frontend
- PostgreSQL for persistent relational data
- Redis for runtime cache/connectivity checks
- Docker Compose for local orchestration
- GitHub Actions CI for backend and frontend validation

The backend currently includes infrastructure foundations, authentication, and Memory Profiles CRUD. The frontend remains minimal and was not expanded as part of the backend slices completed so far.

## 2. Production Architecture Decisions

- Backend framework: FastAPI
- Frontend framework: Next.js with TypeScript
- ORM: SQLAlchemy 2.x ORM
- Database migrations: Alembic
- Primary database: PostgreSQL
- Cache / supporting service: Redis
- Container orchestration: Docker Compose
- Backend auth strategy: JWT bearer tokens
- Password storage: hashed passwords only, never plaintext
- Backend code organization: modular structure with `core`, `db`, and `modules`
- CI strategy: backend `pytest`, frontend `vitest`, frontend production build

## 3. Current Local Ports

- Backend: `8033`
- Frontend: `8017`
- PostgreSQL external: `5543`
- PostgreSQL internal: `db:5432`
- Redis external: `6384`
- Redis internal: `redis:6379`

## 4. Docker Setup Summary

The root `docker-compose.yml` defines four services:

- `db`: `postgres:16-alpine`
- `redis`: `redis:7-alpine`
- `backend`: FastAPI application container built from `backend/Dockerfile`
- `frontend`: Next.js application container built from `frontend/Dockerfile`

Current container names:

- `eternal_world_db`
- `eternal_world_redis`
- `eternal_world_backend`
- `eternal_world_frontend`

Current Docker wiring:

- Backend connects to PostgreSQL through `DATABASE_URL=postgresql+psycopg://eternal_user:eternal_password@db:5432/eternal_world`
- Backend connects to Redis through `REDIS_URL=redis://redis:6379/0`
- Frontend is configured to call the backend through `NEXT_PUBLIC_API_URL=http://localhost:8033`
- Backend source is mounted into `/app`
- Frontend source is mounted into `/app`

## 5. GitHub Actions / CI Setup Summary

The repository contains `.github/workflows/ci.yml` with two jobs:

- `backend-tests`
  - Python `3.12`
  - installs `backend/requirements.txt`
  - runs `python -m pytest` from `backend`
- `frontend-tests`
  - Node.js `22`
  - runs `npm install`
  - runs `npm test`
  - runs `npm run build`

CI is designed to validate both backend test stability and frontend buildability on every push to `main` and on pull requests.

## 6. Backend Foundation Summary

The backend foundation currently includes:

- FastAPI application entrypoint in `backend/app/main.py`
- CORS middleware configuration from environment settings
- `GET /`
- `GET /health`
- `GET /health/runtime`

Health behavior:

- `/health` returns a simple application status
- `/health/runtime` performs runtime dependency checks against PostgreSQL and Redis
- Runtime health reports `ok` or `degraded`, with service-level status details

Current backend structure is modular:

- `backend/app/core`
- `backend/app/db`
- `backend/app/cache`
- `backend/app/modules/auth`
- `backend/app/modules/users`
- `backend/app/modules/memory_profiles`
- placeholder module packages also exist for future slices

## 7. Database Foundation Summary

The database foundation currently includes:

- SQLAlchemy ORM session and model base
- Alembic migration configuration
- PostgreSQL as the primary relational database

Current ORM models:

- `User`
- `MemoryProfile`
- `ChatMessage`
- `Memory`

Current migration history:

- `20260616_0001` create core tables
- `20260616_0002` add `users.full_name`
- `20260616_0003` update `memory_profiles` for CRUD support
- `20260616_0004` drop legacy memory-profile columns that were replaced by the CRUD-oriented schema

Current Alembic head:

- `20260616_0004`

## 8. Security Foundation Summary

The security foundation currently includes:

- Password hashing utilities in `backend/app/core/security.py`
- Password verification utilities
- JWT access token creation
- JWT access token decoding
- Settings-driven JWT configuration
- Input validation for auth and memory profile payloads
- Injection-focused validation/testing coverage

Security-related safeguards currently implemented:

- passwords must satisfy minimum validation before hashing
- auth endpoints normalize email input safely
- JWT-protected endpoints require bearer authentication
- ownership checks are enforced in service/repository-backed database lookups
- suspicious SQL-injection-like auth input is rejected through validation
- SQL-like text in profile content is treated as normal text, not executed

## 9. Auth Backend MVP Summary

The auth backend MVP is implemented and available through:

- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`

Auth behavior currently implemented:

- register user with email, password, and optional full name
- normalize and validate email input
- validate password length constraints
- hash password before persistence
- reject duplicate email
- issue JWT bearer access token on successful login
- resolve current user from JWT on protected routes
- return authenticated user data from `/api/auth/me`

Auth test coverage currently includes:

- successful registration
- duplicate email rejection
- successful login
- wrong password rejection
- `/me` with valid token
- `/me` without token rejected
- SQL-injection-like auth input rejected safely

## 10. Memory Profiles Backend CRUD Summary

The Memory Profiles backend CRUD slice is implemented and available through:

- `POST /api/memory-profiles`
- `GET /api/memory-profiles`
- `GET /api/memory-profiles/{profile_id}`
- `PATCH /api/memory-profiles/{profile_id}`
- `DELETE /api/memory-profiles/{profile_id}`

Current Memory Profile fields:

- `name` required
- `birth_date` optional
- `death_date` optional
- `biography` optional
- `personality` optional
- `catchphrases` optional
- `is_public` optional boolean

Current CRUD behavior:

- create profile for authenticated user
- list only profiles owned by the current user
- get only a profile owned by the current user
- update only a profile owned by the current user
- delete only a profile owned by the current user
- cross-user access returns `404`, not `403`
- profile path parameter is constrained to positive integer IDs
- optional text fields are normalized safely

Memory Profiles test coverage currently includes:

- create memory profile with authenticated user
- list only own profiles
- get own profile
- update own profile
- delete own profile
- unauthenticated request rejected
- user cannot access another user’s profile
- SQL-like text input handled safely without breaking the API

## 11. Current Verification Status

Current local verification completed on `2026-06-16`:

- Backend tests passing: `22 passed`
- Docker working: confirmed with `docker compose ps`
- Alembic migrations working: confirmed with `docker compose exec backend alembic current`
- Runtime health OK: `{"status":"ok","database":"ok","redis":"ok"}`

## 12. Commit Tracking

Current `git log --oneline` history:

- `893b0f0` Add memory profiles backend CRUD
- `7983c1a` Add backend authentication MVP
- `ebb6805` Pin bcrypt for passlib compatibility
- `1fb0aff` Add database models migrations and security foundation
- `cbe87e3` Add PostgreSQL and Redis runtime health checks
- `e6c57cb` Fix CI backend and frontend test setup
- `7e57238` Configure Docker services and local ports
- `1166f00` Add backend and frontend MVP base
- `1e3da05` Initial production project structure

Future commit entry format:

```md
### YYYY-MM-DD - Commit message
- Changed area:
- What was added:
- Tests run:
- Migration status:
- Docker verified:
```

## 13. Mandatory Future Rule

This file is mandatory project tracking documentation and must be maintained continuously.

Required rule for all future work:

- After every future code change and before every commit, `PROJECT_PROGRESS.md` must be updated.
- Every new commit must have a short entry added to this file.
- Do not create a commit without first updating this file.

Every new entry must include:

- date
- commit message
- changed area
- what was added
- tests run
- migration status if relevant
- whether Docker was verified
