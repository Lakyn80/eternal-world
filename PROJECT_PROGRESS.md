# Project Progress

## 1. Project Overview

Eternal World is a production-oriented AI memory social platform under active backend-first development. The repository currently contains:

- A FastAPI backend
- A Next.js + TypeScript frontend
- PostgreSQL for persistent relational data
- Redis for runtime cache/connectivity checks
- Docker Compose for local orchestration
- GitHub Actions CI for backend and frontend validation

The backend currently includes infrastructure foundations, authentication, Memory Profiles CRUD, a chat backend MVP with a prepared multi-agent architecture tree, a media storage foundation with local server storage abstraction, local media serving plus Memory Profile photo binding for dev/MVP use, a configurable Brain Agent provider foundation with deterministic mock defaults, and a static billing / tariff foundation. The frontend remains minimal and was not expanded as part of the backend slices completed so far.

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
- Backend Brain Agent defaults to `AI_BRAIN_PROVIDER=mock` in Docker/local dev
- Backend media storage is configured through `MEDIA_STORAGE_PROVIDER=local`, `MEDIA_ROOT=/app/media`, and `MEDIA_PUBLIC_BASE_URL=/media`
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
- `backend/app/modules/billing`
- `backend/app/modules/chat`
- `backend/app/modules/memories`
- `backend/app/modules/media`
- `backend/app/modules/rag_sources`
- `backend/app/modules/users`
- `backend/app/modules/memory_profiles`
- `backend/app/modules/ai_agents`
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
- `MediaAsset`
- `RagSource`

Current migration history:

- `20260616_0001` create core tables
- `20260616_0002` add `users.full_name`
- `20260616_0003` update `memory_profiles` for CRUD support
- `20260616_0004` drop legacy memory-profile columns that were replaced by the CRUD-oriented schema
- `20260617_0005` create `media_assets` table
- `20260617_0006` add `memory_profiles.main_photo_media_id`
- `20260619_0007` add timeline memory fields and `memories.media_id`
- `20260620_0008` create `rag_sources` table for profile-scoped RAG source ingestion

Current Alembic head:

- `20260620_0008`

Chat backend note:

- The chat MVP reuses the existing `ChatMessage` model for stored user and assistant messages
- No additional Alembic migration was required for the chat slice

Media storage note:

- The media storage foundation adds a dedicated `MediaAsset` metadata model
- Raw file contents are stored on disk, while PostgreSQL stores metadata and storage identifiers only

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

- `photo_media_id` optional
- `photo_url` optional response field
- `name` required
- `birth_date` optional
- `death_date` optional
- `biography` optional
- `personality` optional
- `catchphrases` optional
- `is_public` optional boolean

Current CRUD behavior:

- create profile for authenticated user
- Memory Profile creation now enforces the current plan entitlement before insert
- list only profiles owned by the current user
- get only a profile owned by the current user
- update only a profile owned by the current user
- delete only a profile owned by the current user
- assign an owned uploaded image as the main profile photo
- remove/unset the current main profile photo
- cross-user access returns `404`, not `403`
- profile path parameter is constrained to positive integer IDs
- optional text fields are normalized safely
- profile responses can include `photo_media_id` and a usable relative `photo_url`
- the default `free` plan currently allows up to 1 Memory Profile per user
- profile limit exceeded responses return safe `403` JSON with machine-readable codes

Memory Profiles test coverage currently includes:

- create memory profile with authenticated user
- free user can create the first Memory Profile
- free user cannot create the second Memory Profile
- profile limit checks count only the current user's profiles
- another user's profiles do not affect the current user's limit
- list only own profiles
- get own profile
- update own profile
- delete own profile
- unauthenticated request rejected
- user cannot access another user’s profile
- SQL-like text input handled safely without breaking the API
- authenticated user can assign own uploaded image to own Memory Profile
- authenticated user can unset profile photo
- non-image media cannot be assigned as profile photo
- cross-user profile-photo binding attempts return `404`

## 11. Memory Entries / Timeline Foundation Summary

The Memory Entries / Timeline foundation is implemented and available through:

- `POST /api/memory-profiles/{profile_id}/memories`
- `GET /api/memory-profiles/{profile_id}/memories`
- `GET /api/memories/{memory_id}`
- `PATCH /api/memories/{memory_id}`
- `DELETE /api/memories/{memory_id}`

Current memory fields supported by the API:

- `id`
- `profile_id`
- `owner_user_id`
- `title`
- `content`
- `memory_type`
- `occurred_at`
- `occurred_year`
- `media_id`
- `created_at`
- `updated_at`

Current memory behavior:

- all memory endpoints require JWT authentication
- memories can only be created under Memory Profiles owned by the current user
- memory reads, updates, and deletes are ownership-scoped and return `404` for cross-user access
- titles are trimmed, required, and must not be empty
- content is optional and trimmed safely
- supported `memory_type` values are `text`, `photo`, `audio`, and `video`
- timeline ordering is newest first by `occurred_at desc`, then `occurred_year desc`, then `created_at desc`
- optional media linkage is ownership-checked and MIME-type-validated
- text memories do not require media
- memory creation now enforces the current billing entitlement for `max_memories`
- the default `free` plan currently allows up to 10 memories per user
- limit exceeded responses return safe `403` JSON with `error=limit_exceeded` and `code=memory_limit_exceeded`

Current memory/media compatibility rules:

- `photo` memories allow `image/jpeg`, `image/png`, `image/webp`
- `audio` memories allow `audio/mpeg`, `audio/wav`
- `video` memories allow `video/mp4`
- media that belongs to another user returns `404`
- incompatible media returns safe `400`

Memory timeline test coverage currently includes:

- authenticated user can create a text memory under own profile
- unauthenticated user cannot create memory
- user cannot create memory under another user’s profile
- user can list only own profile memories
- user can read own memory
- user cannot read another user’s memory
- user can update own memory
- user cannot update another user’s memory
- user can delete own memory
- user cannot delete another user’s memory
- memory list is timeline ordered
- free user cannot create more than 10 memories
- memory limit counts only current user’s memories
- media ownership is enforced when linking `media_id`
- media type compatibility is enforced
- memory CRUD does not call external HTTP helpers

## 12. Chat Backend MVP and Agent Architecture Summary

The chat backend MVP is implemented and available through:

- `POST /api/chat/{profile_id}/messages`
- `GET /api/chat/{profile_id}/messages`

Current chat behavior:

- all chat endpoints require JWT authentication
- chat access is limited to Memory Profiles owned by the current user
- cross-user profile access returns `404`, not `403`
- user messages and assistant replies are stored in the existing `ChatMessage` model
- the send endpoint returns:
  - message id
  - profile id
  - user message
  - AI response text
  - `audio_url` nullable
  - `video_url` nullable
  - `created_at`

Current chat flow:

- chat router
- chat service
- agent orchestrator
- brain agent service
- mock brain provider

Prepared agent architecture tree now present in the backend:

- `backend/app/modules/ai_agents/orchestrator.py`
- `backend/app/modules/ai_agents/schemas.py`
- `backend/app/modules/ai_agents/brain/`
- `backend/app/modules/ai_agents/brain/providers/`
- `backend/app/modules/ai_agents/voice/`
- `backend/app/modules/ai_agents/face/`
- `backend/app/modules/ai_agents/director/`

Agent implementation status:

- Brain Agent: implemented as a text-only skeleton for this slice
- Brain prompt builder: implemented using current user message, Memory Profile fields, and recent chat history
- Brain provider factory: implemented with config-based provider selection
- Brain mock provider: implemented as the deterministic default for runtime, tests, Docker, and CI
- Brain OpenAI-compatible provider: implemented as a non-default skeleton for future OpenAI/DeepSeek-style usage through environment configuration
- Voice Agent: placeholder only, not called
- Face / Lip-Sync Agent: placeholder only, not called
- Director Agent: placeholder only, not called

Chat and agent test coverage currently includes:

- authenticated user can send chat message to own profile
- chat message stores user message and AI response text
- authenticated user can list own chat history
- unauthenticated send is rejected
- unauthenticated history request is rejected
- user cannot send message to another user’s profile
- user cannot read another user’s chat history
- SQL-injection-like message text is treated safely as normal text
- mock Brain Agent provider is deterministic
- agent orchestrator calls Brain Agent only for this slice

## 13. Observability Foundation Summary

The observability foundation currently includes:

- structured JSON logging in `backend/app/core/logging.py`
- request context middleware in `backend/app/core/middleware.py`
- safe global error handling in `backend/app/core/errors.py`
- request correlation through `X-Request-ID`

Current observability behavior:

- every backend request receives a `request_id`
- a safe client-provided `X-Request-ID` is reused
- an unsafe or oversized `X-Request-ID` is replaced with a generated UUID
- every response includes `X-Request-ID`
- request lifecycle logs emit structured JSON for request start and completion
- log fields include timestamp, level, event, request id, method, path, status code, and duration when available
- unexpected backend exceptions return a safe generic JSON response with the request id
- logging helpers sanitize sensitive keys before writing structured fields

Current log-safety safeguards:

- `password` is redacted
- `access_token` is redacted
- `authorization` is redacted
- `secret` is redacted
- `api_key` is redacted
- raw request bodies are not logged

Observability test coverage currently includes:

- request without `X-Request-ID` returns a generated request id
- request with safe `X-Request-ID` returns the same request id
- unsafe request id input is replaced safely
- `/health` still works with the middleware installed
- `/health/runtime` still works with the middleware installed
- unexpected exception handling returns safe JSON and includes the request id
- sensitive logging fields are sanitized before output

## 14. Media Storage Foundation Summary

The media storage foundation is implemented and available through:

- `POST /api/media/upload`
- `GET /api/media`
- `GET /api/media/{media_id}`
- `DELETE /api/media/{media_id}`
- `GET /media/{storage_key:path}` for local/dev serving

Current media module structure:

- `backend/app/modules/media/router.py`
- `backend/app/modules/media/schemas.py`
- `backend/app/modules/media/service.py`
- `backend/app/modules/media/repository.py`
- `backend/app/modules/media/storage/base.py`
- `backend/app/modules/media/storage/local.py`
- `backend/app/modules/media/storage/yandex_s3.py`

Current storage behavior:

- all media endpoints require JWT authentication
- local file storage is implemented now through a storage-provider abstraction
- local media files can be served safely through `/media/{storage_key:path}` in dev/MVP mode
- future Yandex Object Storage integration is reserved behind a placeholder provider
- uploaded files are written under the configured media root
- file paths are generated internally through storage keys, not trusted filenames
- PostgreSQL stores metadata only:
  - owner id
  - optional profile id
  - media type
  - storage provider
  - storage key
  - sanitized original filename
  - MIME type
  - file size
- public URLs are returned as relative media paths and do not expose absolute server paths
- profile-linked uploads verify that the referenced Memory Profile belongs to the current user
- cross-user media access returns `404`, not `403`
- local media serving returns `404` for missing files and rejects path traversal through validated storage-key resolution

Current media validation and safety behavior:

- allowed MIME types:
  - `image/jpeg`
  - `image/png`
  - `image/webp`
  - `audio/mpeg`
  - `audio/wav`
  - `video/mp4`
- maximum file size is controlled by settings and defaults to `20 MB`
- original filenames are sanitized before metadata persistence
- path traversal in uploaded filenames cannot escape the configured media root
- local storage keys are generated internally and do not depend on the uploaded filename
- absolute filesystem paths are not returned in API metadata responses

Media test coverage currently includes:

- authenticated user can upload allowed file
- unauthenticated upload is rejected
- unsupported MIME type is rejected
- too large file is rejected
- path traversal filename is sanitized and remains inside the media root
- local media route serves an uploaded local file safely
- local media route rejects path traversal
- local media route returns `404` for missing files
- user can list only own media
- user can get own media metadata
- user cannot get another user’s media
- user can delete own media metadata and local file
- user cannot delete another user’s media
- upload with another user’s profile id returns `404`
- local storage provider generates safe storage keys
- storage provider metadata responses do not expose absolute filesystem paths
- no raw file bytes are stored in the database model

## 15. Local Media Serving and MemoryProfile Photo Binding Summary

The local media serving and profile-photo slice is implemented through:

- `GET /media/{storage_key:path}`
- `POST /api/memory-profiles/{profile_id}/photo`
- `DELETE /api/memory-profiles/{profile_id}/photo`

Current behavior:

- local media serving uses the configured `MEDIA_ROOT` and resolves only validated storage keys
- only files inside `MEDIA_ROOT` are served
- missing files return `404`
- path traversal attempts are rejected safely and return `404`
- Memory Profile photo binding stores a durable media reference through `main_photo_media_id`
- uploaded image media can be assigned only when both the profile and the media asset belong to the current user
- only image media (`jpeg`, `png`, `webp`) can be bound as profile photos
- profile photo removal unsets the media reference without touching the stored media metadata
- profile responses expose only relative media URLs and never absolute filesystem paths

Test coverage for this slice includes:

- safe local media serving for uploaded files
- local media route missing-file handling
- local media route path-traversal rejection
- successful profile-photo assignment
- successful profile-photo removal
- cross-user media assignment blocked with `404`
- cross-user profile assignment blocked with `404`
- non-image profile-photo binding rejected safely
- unauthenticated profile-photo binding rejected
- usable `photo_media_id` and `photo_url` fields returned in profile responses

## 16. Real Brain Agent Provider Foundation Summary

The Brain Agent provider foundation now includes:

- provider selection through `AI_BRAIN_PROVIDER`
- deterministic `mock` provider as the default
- `openai_compatible` provider skeleton for future real-provider usage
- safe AI configuration fields:
  - `AI_BRAIN_PROVIDER`
  - `AI_BRAIN_MODEL`
  - `AI_BRAIN_API_KEY`
  - `AI_BRAIN_BASE_URL`
  - `AI_BRAIN_TIMEOUT_SECONDS`

Current provider behavior:

- default provider remains `mock`
- tests, CI, and local Docker continue to use the deterministic mock path unless configuration is explicitly changed
- `openai_compatible` is available only when explicitly selected
- `openai_compatible` validates required configuration before use
- unknown provider names fail with a clear configuration error
- AI API keys are stored through secret-aware settings and are not logged in plaintext
- no database migration was required for this slice

Current Brain Agent provider structure:

- `backend/app/modules/ai_agents/brain/service.py`
- `backend/app/modules/ai_agents/brain/provider.py`
- `backend/app/modules/ai_agents/brain/prompt_builder.py`
- `backend/app/modules/ai_agents/brain/providers/__init__.py`
- `backend/app/modules/ai_agents/brain/providers/mock.py`
- `backend/app/modules/ai_agents/brain/providers/openai_compatible.py`

Brain-provider test coverage currently includes:

- default Brain provider is mock
- mock provider is deterministic
- provider factory selects mock
- provider factory rejects unknown provider
- openai-compatible provider requires API key when selected
- openai-compatible provider does not run in normal tests unless explicitly mocked
- chat endpoint still works with mock provider
- sensitive AI config values are not exposed in logs or API responses

## 17. Grounded Memory Context / RAG-lite Foundation Summary

The grounded memory context / RAG-lite foundation is implemented inside the Brain Agent flow and currently works through:

- `backend/app/modules/ai_agents/brain/context.py`
- `backend/app/modules/ai_agents/brain/prompt_builder.py`
- `backend/app/modules/chat/service.py`

Current grounded-context behavior:

- chat requests still validate the owned Memory Profile first
- profile context is loaded from the selected Memory Profile only
- memory evidence is loaded only from memories owned by the current user and attached to the selected profile
- evidence selection is deterministic and does not use embeddings, vector search, or external AI calls
- memory ranking uses simple keyword overlap against memory `title` and `content`
- when keyword matches exist, matched memories are preferred
- when keyword matches do not exist, latest timeline memories are used as fallback context
- timeline tie-breaking remains `occurred_at desc`, `occurred_year desc`, `created_at desc`, `id desc`
- evidence items are capped at 10
- prompt text now separates avatar identity/style, verified memory evidence, and grounding instructions
- factual answers are restricted to stored evidence and profile facts already present in context
- the prompt explicitly tells the model not to invent unknown facts and to say when information is not available in stored memories/context
- personality and catchphrases can influence tone, but not create facts
- prompt sanitization removes absolute local filesystem paths before they can reach the provider prompt
- no media binary data, storage keys, or local file paths are included in grounded prompt context
- no new database fields or Alembic migration were required for this slice

Current grounded-context structures include:

- `BrainProfileContext`
- `BrainMemoryEvidence`
- `BrainGroundedContext`

Grounded-context test coverage currently includes:

- chat response generation still works with no memories
- generated Brain prompt includes profile context
- generated Brain prompt includes selected memory evidence when memories exist
- factual grounding instructions are present in the prompt
- the prompt tells the model not to invent unknown facts
- the prompt tells the model to say when information is missing from stored memories/context
- only the selected profile’s memories are included
- another user’s memories are not included
- memory evidence count is capped at 10
- memory evidence is deterministic and timeline ordered for fallback
- keyword-matching memory is preferred over unrelated latest memory
- prompt does not include absolute local file paths
- grounded memory context makes no external HTTP calls

## 18. RAG Source Ingestion Foundation Summary

The RAG source ingestion foundation is implemented and available through:

- `POST /api/memory-profiles/{profile_id}/rag-sources`
- `GET /api/memory-profiles/{profile_id}/rag-sources`
- `GET /api/rag-sources/{source_id}`
- `PATCH /api/rag-sources/{source_id}`
- `DELETE /api/rag-sources/{source_id}`

Current RAG source fields supported by the API:

- `id`
- `owner_user_id`
- `profile_id`
- `source_type`
- `title`
- `raw_text`
- `normalized_text`
- `language`
- `status`
- `processing_error`
- `source_metadata`
- `created_at`
- `updated_at`

Current RAG source behavior:

- all RAG source endpoints require JWT authentication
- sources can only be created under Memory Profiles owned by the current user
- source reads, updates, deletes, and lists are ownership-scoped and return `404` for cross-user access
- `title` is trimmed, required, and must not be empty
- `raw_text` is trimmed, required, and must not be empty
- `source_type` is validated against the allowed ingestion categories
- `language` is optional and normalized for values like `ru`, `cs`, `en`, or `unknown`
- `source_metadata` is an optional JSON object for future ingestion pipeline hints
- new sources default to `ready_for_cleaning`
- `normalized_text` is currently stored as the minimally normalized raw text only
- updating `raw_text` resets `status` to `ready_for_cleaning` and clears `processing_error`
- source lists are ordered newest first by `created_at desc`, then `id desc`
- ingestion metadata is isolated from timeline memories and does not duplicate the `Memory` model
- no new billing enforcement was added in this slice

Current ingestion-preparation behavior:

- the system now has a durable per-profile source corpus table
- source rows persist raw input and pipeline state for future cleaning/chunking/embedding
- indexes exist for `owner_user_id`, `profile_id`, `status`, `source_type`, `created_at`
- compound indexes exist for `owner_user_id + profile_id` and `profile_id + status`
- no chunking, embeddings, Qdrant indexing, or hybrid retrieval is implemented yet

RAG source test coverage currently includes:

- authenticated user can create RAG source under own profile
- unauthenticated user cannot create RAG source
- user cannot create RAG source under another user’s profile
- user can list only own profile sources
- user can read own source
- user cannot read another user’s source
- user can update own source
- updating `raw_text` resets status to `ready_for_cleaning`
- user cannot update another user’s source
- user can delete own source
- user cannot delete another user’s source
- title is trimmed and cannot be empty
- raw_text is trimmed and cannot be empty
- invalid `source_type` is rejected
- list is ordered newest first
- RAG source CRUD does not call external HTTP helpers

## 19. Billing Foundation Summary

The billing / tariff foundation is implemented and available through:

- `GET /api/billing/plans`
- `GET /api/billing/me`
- `GET /api/billing/limits`

Current billing module structure:

- `backend/app/modules/billing/__init__.py`
- `backend/app/modules/billing/router.py`
- `backend/app/modules/billing/schemas.py`
- `backend/app/modules/billing/service.py`
- `backend/app/modules/billing/plans.py`
- `backend/app/modules/billing/limits.py`
- `backend/app/modules/billing/entitlements.py`
- `backend/app/modules/billing/usage.py`
- `backend/app/modules/billing/exceptions.py`

Current billing behavior:

- plan codes are stable and lowercase:
  - `free`
  - `basic`
  - `premium`
  - `family`
- `GET /api/billing/plans` is public and returns the tariff catalog in stable order
- authenticated users default to the `free` plan
- `GET /api/billing/me` returns the effective plan for the current user
- `GET /api/billing/limits` returns the effective limits plus placeholder usage values
- reusable entitlement checks now live inside the billing module
- Memory Profile creation calls billing entitlement logic before persistence
- Memory creation calls billing entitlement logic before persistence
- `free` users can have up to 1 Memory Profile
- `basic` users can have up to 3 Memory Profiles
- `premium` users have unlimited Memory Profiles
- `family` users have unlimited Memory Profiles
- limit violations return safe `403` responses with `error=limit_exceeded` and `code=profile_limit_exceeded`
- `free` users can have up to 10 memories
- `basic`, `premium`, and `family` users have unlimited memories
- memory limit violations return safe `403` responses with `error=limit_exceeded` and `code=memory_limit_exceeded`
- future usage checks can reuse the same billing entitlement helpers for memories, audio minutes, videos, and family-member limits
- tariffs are static for this slice and separated from auth, chat, media, and memory-profile logic
- prices are stored as integer rubles
- unlimited numeric limits are represented as `null`
- no payment provider, invoice flow, or subscription purchase flow is implemented yet
- a database migration was required for the timeline memory fields slice

Current supported billing limits:

- `max_profiles`
- `max_memories`
- `max_audio_minutes`
- `max_videos_per_month`
- `max_video_seconds`
- `allow_watermark_removal`
- `allow_unlimited_chat`
- `allow_priority_support`
- `allow_family_members`
- `allow_shared_memories`
- `allow_family_tree`
- `max_family_members`
- `max_video_quality`

Billing test coverage currently includes:

- list plans returns all four plans
- plan codes are stable and ordered as `free`, `basic`, `premium`, `family`
- unauthenticated user can list public plans
- authenticated user defaults to `free`
- `/api/billing/me` rejects unauthenticated users
- `/api/billing/limits` rejects unauthenticated users
- `free` plan has correct limits
- `basic` plan has correct limits
- `premium` plan has unlimited values where expected
- `family` plan includes family-specific flags
- the reusable billing limit checker allows unlimited plans
- `basic` Memory Profile limit logic allows 3 profiles and rejects the 4th
- `premium` Memory Profile limit logic supports unlimited profiles
- `family` Memory Profile limit logic supports unlimited profiles
- `free` memory limit logic allows 10 memories and rejects the 11th
- `basic`, `premium`, and `family` memory limit logic supports unlimited memories
- billing endpoints do not call external HTTP helpers
- `PROJECT_PROGRESS.md` is updated for this slice

## 20. Current Verification Status

Current local verification completed on `2026-06-20`:

- Backend tests passing locally: `134 passed`
- Backend tests passing in Docker: `133 passed, 1 skipped`
- Docker working: confirmed with `docker compose up -d --build`
- Alembic migrations working: confirmed with `docker compose exec backend alembic upgrade head` and `docker compose exec backend alembic current` -> `20260620_0008 (head)`
- Runtime health OK: `{"status":"ok","database":"ok","redis":"ok"}`
- Observability foundation verified previously with live `X-Request-ID` response header
- Media storage foundation verified with local pytest coverage and Docker backend startup after rebuild
- Local media serving and profile-photo binding verified with local pytest coverage and Docker backend verification
- Brain Agent provider foundation verified with local pytest coverage and Docker backend verification
- Grounded Memory Context / RAG-lite foundation verified with local pytest coverage and Docker backend verification
- RAG Source Ingestion foundation verified with local pytest coverage and Docker backend verification
- Billing / tariff foundation verified with local pytest coverage and Docker backend verification
- Usage Limits / Entitlements foundation verified with local pytest coverage and Docker backend verification
- Memory Entries / Timeline foundation verified with local pytest coverage and Docker backend verification

## 21. Commit Tracking

Current `git log --oneline` history:

- `6eb90d2` Add Brain Agent provider foundation
- `c079d85` Add local media serving and profile photo binding
- `3115d71` Add media storage foundation
- `44268be` Add backend observability foundation
- `065ea8f` Add chat backend and agent architecture skeleton
- `0ce4a0e` Add project progress tracking
- `893b0f0` Add memory profiles backend CRUD
- `7983c1a` Add backend authentication MVP
- `ebb6805` Pin bcrypt for passlib compatibility
- `1fb0aff` Add database models migrations and security foundation
- `cbe87e3` Add PostgreSQL and Redis runtime health checks
- `e6c57cb` Fix CI backend and frontend test setup
- `7e57238` Configure Docker services and local ports
- `1166f00` Add backend and frontend MVP base
- `1e3da05` Initial production project structure

Current working tree note:

- The RAG Source Ingestion foundation slice is implemented in the working tree and is not yet represented by a committed hash.

Future commit entry format:

```md
### YYYY-MM-DD - Commit message
- Changed area:
- What was added:
- Tests run:
- Migration status:
- Docker verified:
```

## 22. Mandatory Future Rule

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
