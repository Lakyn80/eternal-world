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
- Qdrant external: `6335`
- Qdrant internal: `qdrant:6333`

## 4. Docker Setup Summary

The root `docker-compose.yml` defines six services:

- `db`: `postgres:16-alpine`
- `redis`: `redis:7-alpine`
- `qdrant`: `qdrant/qdrant:v1.13.6`
- `backend`: FastAPI application container built from `backend/Dockerfile`
- `celery_worker`: Celery worker container built from `backend/Dockerfile`
- `frontend`: Next.js application container built from `frontend/Dockerfile`

Current container names:

- `eternal_world_db`
- `eternal_world_redis`
- `eternal_world_qdrant`
- `eternal_world_backend`
- `eternal_world_celery_worker`
- `eternal_world_frontend`

Current Docker wiring:

- Backend connects to PostgreSQL through `DATABASE_URL=postgresql+psycopg://eternal_user:eternal_password@db:5432/eternal_world`
- Backend connects to Redis through `REDIS_URL=redis://redis:6379/0`
- Backend connects to Qdrant through `QDRANT_URL=http://qdrant:6333`
- Backend and Celery worker share `CELERY_BROKER_URL=redis://redis:6379/1`
- Backend Brain Agent defaults to `AI_BRAIN_PROVIDER=mock` in Docker/local dev
- Backend media storage is configured through `MEDIA_STORAGE_PROVIDER=local`, `MEDIA_ROOT=/app/media`, and `MEDIA_PUBLIC_BASE_URL=/media`
- Backend Qdrant indexing defaults to `QDRANT_COLLECTION_NAME=eternal_world_rag_chunks`, `QDRANT_TIMEOUT_SECONDS=10`, and `QDRANT_INDEXING_ENABLED=true`
- Celery worker runs `celery -A app.worker.celery_app.celery_app worker --loglevel=info`
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
- `backend/app/modules/embeddings`
- `backend/app/modules/embedding_models`
- `backend/app/modules/memories`
- `backend/app/modules/media`
- `backend/app/modules/job_tracking`
- `backend/app/modules/rag_retrieval`
- `backend/app/modules/qdrant_indexing`
- `backend/app/modules/rag_chunks`
- `backend/app/modules/rag_sources`
- `backend/app/modules/users`
- `backend/app/modules/memory_profiles`
- `backend/app/modules/ai_agents`
- `backend/app/worker`
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
- `RagChunk`
- `RagEmbedding`
- `RagVectorIndex`
- `BackgroundJob`

Current migration history:

- `20260616_0001` create core tables
- `20260616_0002` add `users.full_name`
- `20260616_0003` update `memory_profiles` for CRUD support
- `20260616_0004` drop legacy memory-profile columns that were replaced by the CRUD-oriented schema
- `20260617_0005` create `media_assets` table
- `20260617_0006` add `memory_profiles.main_photo_media_id`
- `20260619_0007` add timeline memory fields and `memories.media_id`
- `20260620_0008` create `rag_sources` table for profile-scoped RAG source ingestion
- `20260620_0009` create `rag_chunks` table for sentence-aware chunk persistence and validation audit
- `20260620_0010` create `rag_embeddings` table for chunk-level embedding storage and metadata
- `20260620_0011` create `rag_vector_indexes` table for Qdrant indexing state and deterministic point tracking
- `20260622_0012` create `background_jobs` table for Celery-backed job tracking and historical milestone audit rows

Current Alembic head:

- `20260622_0012`

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

## 19. Sentence-aware Chunking + Chunk Validation Foundation Summary

The sentence-aware chunking and chunk-validation foundation is implemented and available through:

- `POST /api/rag-sources/{source_id}/chunk`
- `GET /api/rag-sources/{source_id}/chunks`
- `GET /api/rag-chunks/{chunk_id}`

Current `rag_chunks` module structure:

- `backend/app/modules/rag_chunks/__init__.py`
- `backend/app/modules/rag_chunks/router.py`
- `backend/app/modules/rag_chunks/schemas.py`
- `backend/app/modules/rag_chunks/service.py`
- `backend/app/modules/rag_chunks/repository.py`
- `backend/app/modules/rag_chunks/chunker.py`
- `backend/app/modules/rag_chunks/validation.py`

Current chunking behavior:

- all chunking endpoints require JWT authentication
- chunking is ownership-scoped through the current user and the owned `RagSource`
- cross-user chunk/list/read access returns `404`, not `403`
- chunking uses `normalized_text` when present, otherwise `raw_text`
- safe normalization currently standardizes line endings, trims repeated whitespace, and preserves paragraph boundaries
- sentence-aware chunking prefers paragraph and sentence boundaries before any hard split fallback
- chunk grouping targets roughly `1100` characters, allows up to `1800`, and uses `1` sentence of overlap when safe
- extremely long single sentences fall back to deterministic hard splitting instead of crashing
- successful chunking replaces previous chunks for the same source in one DB transaction
- successful chunking updates `RagSource.normalized_text`, sets `status=chunked`, and clears `processing_error`
- chunking failures roll back partial chunk writes, set `status=failed`, and store only the safe short error `Chunking failed`

Current `RagChunk` fields persisted:

- `id`
- `owner_user_id`
- `profile_id`
- `source_id`
- `chunk_index`
- `chunk_text`
- `text_hash`
- `token_estimate`
- `char_count`
- `sentence_count`
- `language`
- `chunk_metadata`
- `validation_status`
- `validation_errors`
- `created_at`
- `updated_at`

Current chunk validation behavior:

- empty chunks are rejected at validation time
- duplicate chunk hashes within one source are flagged as invalid
- chunk text is trimmed before persistence
- overlong chunks are flagged unless they came from the hard-split fallback
- suspicious lowercase continuation starts are flagged when avoidable
- suspicious mid-sentence endings are flagged when avoidable
- suspicious broken-word endings are flagged heuristically
- missing owner/profile/source identifiers are flagged as invalid
- a source-level summary returns chunk counts plus any coverage warnings

Chunking and validation test coverage currently includes:

- authenticated user can chunk own source
- unauthenticated user cannot chunk source
- user cannot chunk another user’s source
- chunking creates ordered chunks with `chunk_index` starting at `0`
- chunking replaces previous chunks for the same source
- list chunks returns only owned source chunks
- user cannot list chunks for another user’s source
- user can read own chunk
- user cannot read another user’s chunk
- chunker preserves sentence boundaries on normal text
- chunker preserves Russian, Czech, and English punctuation endings
- chunker does not create empty chunks
- duplicate chunks are detected by validation
- validation flags suspicious mid-sentence starts and ends
- very long sentence fallback does not crash
- source status becomes `chunked` after success
- source processing error is cleared after success
- failure path sets source status to `failed` with a safe error
- chunking endpoints do not call external HTTP helpers

Current retrieval-readiness note:

- chunks are now persisted per owner/profile/source with stable ordering, hashes, validation metadata, and token estimates
- this prepares the system for future embeddings, Qdrant indexing, hybrid retrieval, reranking, and RAG evaluation without adding those features yet

## 20. Embedding Model Registry Foundation Summary

The embedding model registry foundation is implemented and available through:

- `GET /api/embedding-models`
- `GET /api/embedding-models/default`
- `GET /api/embedding-models/{model_code}`

Current `embedding_models` module structure:

- `backend/app/modules/embedding_models/__init__.py`
- `backend/app/modules/embedding_models/router.py`
- `backend/app/modules/embedding_models/schemas.py`
- `backend/app/modules/embedding_models/service.py`
- `backend/app/modules/embedding_models/registry.py`
- `backend/app/modules/embedding_models/exceptions.py`

Current registry behavior:

- the embedding model catalog is static and code-defined for this slice
- no database table is used because no per-profile model choice is stored yet
- the default model is the stable local profile `multilingual_e5_small`
- disabled models are hidden from the public list response unless `include_disabled=true`
- multilingual candidate selection includes models that explicitly support the requested language or the `multilingual` capability
- unknown model codes return a safe `404`
- the disabled external profile `jina_embeddings_v3` is registered but not returned by default
- the deterministic `mock_embedding` profile is available for tests and future local pipeline mocks

Current registered model profiles:

- `multilingual_e5_small`
- `bge_m3`
- `jina_embeddings_v3`
- `mock_embedding`

Current registry metadata exposed by the API:

- `code`
- `display_name`
- `provider_type`
- `dimension`
- `languages`
- `max_input_tokens`
- `normalized_vectors`
- `supports_batching`
- `enabled`
- `is_default`
- `recommended_for`
- `notes`

Current slice constraints:

- no real embedding generation is implemented yet
- no model packages are installed or downloaded in this slice
- no external embedding providers are called
- no Qdrant indexing or retrieval changes are implemented yet
- no Alembic migration is required for this static registry foundation

Embedding model registry test coverage currently includes:

- list endpoint returns enabled models by default
- disabled external model is hidden unless `include_disabled=true`
- default endpoint returns the configured default model
- get by code returns a known model
- unknown model code returns `404`
- model codes are stable
- exactly one default model exists
- default model is enabled
- candidate selection for `ru` includes multilingual-capable models
- candidate selection for `cs` includes multilingual-capable models
- candidate selection for unknown language still returns multilingual/default candidates
- mock embedding model is available for tests
- embedding model registry endpoints do not call external HTTP helpers
- `PROJECT_PROGRESS.md` is updated for this slice

Current future-readiness note:

- this registry now provides stable internal model metadata for later embedding execution, Qdrant indexing, hybrid retrieval, retrieval-quality comparisons, and automatic best-model selection
- provider type, vector dimension, normalization behavior, and batching capability are now centralized before any real embedding pipeline is introduced

## 21. Embedding Generation Foundation Summary

The embedding generation foundation is implemented and available through:

- `POST /api/rag-chunks/{chunk_id}/embed`
- `POST /api/rag-sources/{source_id}/embed-chunks`
- `GET /api/rag-chunks/{chunk_id}/embeddings`
- `GET /api/rag-embeddings/{embedding_id}`

Current `embeddings` module structure:

- `backend/app/modules/embeddings/__init__.py`
- `backend/app/modules/embeddings/router.py`
- `backend/app/modules/embeddings/schemas.py`
- `backend/app/modules/embeddings/service.py`
- `backend/app/modules/embeddings/repository.py`
- `backend/app/modules/embeddings/exceptions.py`
- `backend/app/modules/embeddings/providers/__init__.py`
- `backend/app/modules/embeddings/providers/base.py`
- `backend/app/modules/embeddings/providers/mock.py`

Current embedding-generation behavior:

- embedding generation is ownership-scoped through the current user and the owned `RagChunk` or `RagSource`
- cross-user embed/list/read access returns `404`, not `403`
- the default embedding model comes from the committed embedding model registry foundation
- embedding generation currently uses a deterministic mock provider only
- no external API calls, model downloads, or heavy embedding packages are used in this slice
- successful embedding upserts one row per `chunk_id + model_code`
- vectors are stored in PostgreSQL JSON for this foundation slice only
- source-level embedding skips chunks with `validation_status=invalid`
- chunk validation and source chunking status are not changed by embedding generation

Current `RagEmbedding` fields persisted:

- `id`
- `owner_user_id`
- `profile_id`
- `source_id`
- `chunk_id`
- `model_code`
- `vector`
- `vector_dimension`
- `text_hash`
- `status`
- `error_message`
- `embedding_metadata`
- `created_at`
- `updated_at`

Current provider behavior:

- `providers/base.py` defines the provider interface for single-text and batch embedding
- `providers/mock.py` implements deterministic vector generation using registry dimensions
- the mock provider supports `mock_embedding` and the enabled local registry models without any network calls
- vector dimensions are validated against the embedding model registry before persistence

Embedding generation test coverage currently includes:

- authenticated user can embed own chunk with default model
- unauthenticated user cannot embed chunk
- user cannot embed another user’s chunk
- unknown model code is rejected safely
- disabled external model is rejected safely
- embedding vector dimension matches model registry dimension
- mock provider is deterministic
- repeated embed for the same chunk and model upserts instead of duplicating
- source-level embed embeds all valid chunks
- source-level embed skips invalid chunks
- user cannot embed chunks for another user’s source
- user can list embeddings for own chunk
- user cannot list embeddings for another user’s chunk
- user can read own embedding metadata
- user cannot read another user’s embedding
- optional `include_vector=true` behavior is covered
- no external HTTP calls are made
- no model downloads are required for the mock provider
- provider failure can be persisted safely as `status=failed`
- `PROJECT_PROGRESS.md` is updated for this slice

Current future-readiness note:

- the system now has durable per-chunk embedding records keyed by chunk and model profile
- this prepares later Qdrant indexing, hybrid retrieval, retrieval comparisons, and automatic embedding-model evaluation without implementing those flows yet

## 22. Qdrant Indexing Foundation Summary

The Qdrant Indexing Foundation is implemented and available through:

- `POST /api/rag-embeddings/{embedding_id}/index`
- `POST /api/rag-sources/{source_id}/index-embeddings`
- `GET /api/rag-embeddings/{embedding_id}/index`

Current `qdrant_indexing` module structure:

- `backend/app/modules/qdrant_indexing/__init__.py`
- `backend/app/modules/qdrant_indexing/router.py`
- `backend/app/modules/qdrant_indexing/schemas.py`
- `backend/app/modules/qdrant_indexing/service.py`
- `backend/app/modules/qdrant_indexing/repository.py`
- `backend/app/modules/qdrant_indexing/client.py`
- `backend/app/modules/qdrant_indexing/exceptions.py`

Current Qdrant indexing behavior:

- indexing is ownership-scoped through the current user and the owned `RagEmbedding` or `RagSource`
- cross-user index/list/read access returns `404`, not `403`
- this slice only indexes already persisted `RagEmbedding` rows from PostgreSQL
- no embedding generation, hybrid retrieval, Brain Agent Qdrant retrieval, or external AI API calls are introduced here
- source-level indexing scans stored embeddings for one owned source and skips rows that are not in `status=embedded` or do not have a vector
- collection creation is checked lazily before upsert and is non-destructive
- collection names are derived per embedding model as `{QDRANT_COLLECTION_NAME}__{model_code}` so vector dimensions stay isolated by model
- repeated indexing reuses the same deterministic Qdrant point id and updates the same point through upsert semantics
- repeated indexing reuses the same PostgreSQL `RagVectorIndex` row for `embedding_id + qdrant_collection`
- collection dimension mismatches return a safe configuration error instead of recreating or deleting the collection

Current `RagVectorIndex` fields persisted:

- `id`
- `owner_user_id`
- `profile_id`
- `source_id`
- `chunk_id`
- `embedding_id`
- `model_code`
- `qdrant_collection`
- `qdrant_point_id`
- `status`
- `error_message`
- `indexed_at`
- `created_at`
- `updated_at`

Current Qdrant payload behavior:

- each point payload stores `owner_user_id`, `profile_id`, `source_id`, `chunk_id`, `embedding_id`, `model_code`, `text_hash`, `language`, `validation_status`, `source_type`, `chunk_index`, and `indexed_at`
- raw chunk text, raw source text, absolute local file paths, storage keys, media binary content, and secrets are intentionally excluded

Current determinism and isolation behavior:

- point ids are derived as UUIDv5 from `qdrant_collection + embedding_id`
- ownership is enforced through joined lookups across `RagEmbedding`, `RagChunk`, `RagSource`, and `MemoryProfile`
- Qdrant payload metadata now carries enough owner/profile/source/chunk context for future filtered retrieval and evaluation without exposing sensitive local paths

Qdrant indexing test coverage currently includes:

- authenticated user can index own embedding
- unauthenticated user cannot index embedding
- user cannot index another user’s embedding
- deterministic point id generation is stable
- repeated indexing upserts the same index row instead of duplicating
- source-level indexing indexes all embedded records for one owned source
- source-level indexing skips failed embeddings
- user cannot index another user’s source embeddings
- user can read own index metadata
- user cannot read another user’s index metadata
- Qdrant payload includes required ownership and chunk metadata
- Qdrant payload excludes absolute file paths
- collection creation is requested when missing
- collection dimension mismatch returns a safe error
- indexing existing embeddings does not trigger embedding generation
- `PROJECT_PROGRESS.md` is updated for this slice

Current future-readiness note:

- the system now has a dedicated indexing layer between PostgreSQL embedding persistence and future vector retrieval
- this prepares later hybrid retrieval, search evaluation, and grounded Brain Agent retrieval without implementing any retrieval pipeline yet

## 23. Hybrid Retrieval Foundation Summary

The Hybrid Retrieval Foundation is implemented and available through:

- `POST /api/memory-profiles/{profile_id}/rag/retrieve`

Current `rag_retrieval` module structure:

- `backend/app/modules/rag_retrieval/__init__.py`
- `backend/app/modules/rag_retrieval/exceptions.py`
- `backend/app/modules/rag_retrieval/ranking.py`
- `backend/app/modules/rag_retrieval/repository.py`
- `backend/app/modules/rag_retrieval/router.py`
- `backend/app/modules/rag_retrieval/schemas.py`
- `backend/app/modules/rag_retrieval/service.py`

Current retrieval behavior:

- retrieval requires JWT authentication
- retrieval is scoped to one owned `MemoryProfile`
- cross-user and cross-profile access returns `404`, not `403`
- query embeddings are generated in memory only and are never persisted to PostgreSQL
- retrieval reuses the existing embedding model registry and the current local embedding provider mechanism
- Qdrant collection names follow the existing model-specific pattern `{QDRANT_COLLECTION_NAME}__{model_code}`
- Qdrant search always filters by `owner_user_id` and `profile_id`
- optional `language` and `source_type` filters are forwarded to Qdrant and then rechecked against PostgreSQL-backed evidence rows
- Qdrant is treated as the vector index only, while PostgreSQL remains the source of truth for returned chunk text and metadata
- missing Qdrant collections or empty search results return a safe empty `results` list
- no Brain Agent call, no final AI answer generation, and no reranking LLM is added in this slice

Current response evidence fields:

- `chunk_id`
- `source_id`
- `embedding_id`
- `score`
- `text`
- `chunk_index`
- `language`
- `source_type`
- `validation_status`
- `text_hash`
- `qdrant_collection`
- `payload_metadata`

Current ranking behavior:

- ranking preserves the Qdrant similarity score
- result sorting is deterministic by score desc with stable tie-breakers
- optional `score_threshold` filtering is supported
- no keyword engine and no advanced reranking is implemented yet

What is intentionally not implemented:

- no Brain Agent integration with Qdrant
- no hybrid keyword search engine
- no final answer synthesis
- no query embedding persistence
- no new chunk embeddings or reindexing during retrieval

Hybrid retrieval test coverage currently includes:

- retrieval endpoint requires authentication
- retrieval is scoped to `owner_user_id` and `profile_id`
- cross-user profile access returns `404`
- query embedding is generated but not persisted as `RagEmbedding`
- Qdrant search receives owner and profile filters
- empty Qdrant results return an empty list
- existing indexed chunks can be returned as evidence
- retrieval does not call Brain Agent
- retrieval does not create new stored chunk embeddings
- `PROJECT_PROGRESS.md` is updated for this slice

Current future-readiness note:

- the backend now has a dedicated profile-scoped evidence retrieval layer over Qdrant indexing
- this prepares later grounded answer generation, retrieval evaluation, and richer hybrid retrieval without coupling search to the Brain Agent yet

## 24. Celery Job Tracking Foundation Summary

The Celery Job Tracking Foundation is implemented and available through:

- `GET /api/jobs`
- `GET /api/jobs/{job_id}`
- `POST /api/jobs/smoke-test`

Current `job_tracking` module structure:

- `backend/app/modules/job_tracking/__init__.py`
- `backend/app/modules/job_tracking/enums.py`
- `backend/app/modules/job_tracking/exceptions.py`
- `backend/app/modules/job_tracking/repository.py`
- `backend/app/modules/job_tracking/router.py`
- `backend/app/modules/job_tracking/schemas.py`
- `backend/app/modules/job_tracking/service.py`

Current worker structure:

- `backend/app/worker/__init__.py`
- `backend/app/worker/celery_app.py`
- `backend/app/worker/tasks.py`

Current job-tracking behavior:

- PostgreSQL is the authoritative background-job tracking store
- Celery task ids are stored only as technical worker references
- every job is owned by `owner_user_id`
- `profile_id` is optional and ownership-validated when provided
- users can list and read only their own jobs
- cross-user job access returns `404`, not `403`
- reusable service methods now cover queued creation, running state, progress updates, success completion, and failure completion
- the optional smoke-test endpoint creates a harmless job and can dispatch a reusable Celery smoke task
- the smoke task updates one `BackgroundJob` through `queued -> running -> succeeded`
- no existing Brain Agent, retrieval, embedding, or Qdrant behavior is moved to Celery in this slice

Current `BackgroundJob` fields persisted:

- `id`
- `owner_user_id`
- `profile_id`
- `job_type`
- `status`
- `progress_current`
- `progress_total`
- `celery_task_id`
- `input_payload`
- `result_payload`
- `error_payload`
- `error_message`
- `started_at`
- `finished_at`
- `created_at`
- `updated_at`

Current job-type/status foundation:

- job types currently include `smoke_test`, `system_milestone`, `rag_source_ingestion`, `rag_chunking`, `embedding_generation`, `qdrant_indexing`, `rag_retrieval`, `brain_agent_generation`, `media_processing`, `voice_generation`, and `video_generation`
- job statuses currently include `queued`, `running`, `succeeded`, `failed`, and `cancelled`

Historical milestone backfill behavior:

- `backend/scripts/backfill_job_tracking_milestones.py` provides an explicit manual backfill entrypoint
- backfill is not automatic and does not run on startup
- backfill requires an explicit `--owner-user-id`
- backfilled records are marked as `job_type=system_milestone` and `status=succeeded`
- known milestones currently include Task 18 `a44be88` and Task 19 `b46e39c`
- backfilled rows include source/note fields that explicitly state runtime progress was not recorded at execution time
- the backfill service is idempotent and skips milestones already present for the owner

What is intentionally not implemented:

- no automatic Celery integration for all existing modules yet
- no public job cancellation flow
- no retry-heavy orchestration for AI or media pipelines
- no fabricated historical runtime timestamps or progress logs

Job tracking test coverage currently includes:

- `BackgroundJob` metadata registration
- Alembic head coverage for the new migration
- auth required for job endpoints
- users can list only their own jobs
- users can read their own jobs
- cross-user job access returns `404`
- `create_job` creates queued rows
- `mark_running` sets running and `started_at`
- `update_progress` updates progress fields
- `mark_succeeded` sets succeeded and `finished_at`
- `mark_failed` sets failed and error fields
- Celery smoke task can update a job in test/eager mode without external services
- historical milestone backfill is idempotent
- backfilled milestone jobs are marked as `system_milestone` and `succeeded`
- `PROJECT_PROGRESS.md` is updated for this slice

Current future-readiness note:

- the backend now has a reusable worker/job state layer that future long-running RAG, media, and generation pipelines can adopt without changing user-facing auth or profile ownership rules

## 25. Brain Agent Qdrant RAG Integration Summary

The Brain Agent Qdrant RAG integration is implemented inside the existing chat/Brain flow.

Current integration behavior:

- profile chat still validates ownership before any Brain or retrieval work runs
- chat now calls the existing `rag_retrieval` service for the current user, selected profile, and current user message
- retrieval remains fully ownership-scoped through `owner_user_id` and `profile_id`
- retrieved evidence chunks are converted into grounded Brain context items instead of duplicating Qdrant logic inside the Brain Agent
- PostgreSQL remains the source of truth for returned RAG evidence text, while Qdrant remains the vector index
- query embeddings are still generated only in memory and are never persisted as `RagEmbedding` rows

Current Brain grounding behavior:

- the Brain prompt now includes retrieved evidence chunks alongside the earlier memory/timeline evidence
- retrieved evidence is formatted with:
  - `chunk_id`
  - `source_id`
  - `embedding_id`
  - `score`
  - `language`
  - `validation_status`
  - `text_hash`
  - preview text
- if retrieval is disabled, unavailable, misconfigured, or returns no results, chat continues safely without crashing

Current anti-hallucination behavior:

- personality and tone are still allowed to influence style only
- factual grounding is explicitly limited to profile facts, stored memories, and retrieved evidence
- when no relevant grounded evidence exists, the mock Brain provider now returns a safe lack-of-evidence response for factual queries
- no cross-user or cross-profile retrieval data is exposed through chat

What is intentionally not implemented:

- no new public RAG/Brain API endpoints
- no change to Qdrant indexing behavior
- no persisted query embeddings
- no automatic job-tracking orchestration for chat retrieval
- no final citation UX in the frontend

Brain/RAG integration test coverage currently includes:

- chat flow calls retrieval for the correct owner/profile/query
- retrieved chunks are injected into Brain grounded context
- cross-user profile access does not trigger retrieval
- no-result retrieval path returns a safe lack-of-evidence response
- chat does not create new `RagEmbedding` rows for user queries
- Brain chat flow uses the `rag_retrieval` service abstraction instead of direct Qdrant calls
- existing Brain Agent/provider/chat tests remain green
- existing `rag_retrieval` tests remain green
- existing `job_tracking` tests remain green

Current future-readiness note:

- the Brain Agent can now consume profile-scoped Qdrant retrieval evidence as grounded context, which prepares later richer grounded answer generation without changing indexing or embedding persistence architecture

## 26. Billing Foundation Summary

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

## 27. Current Verification Status

Current local verification completed on `2026-06-22`:

- Backend tests passing locally: `235 passed`
- Backend tests passing in Docker: `233 passed, 2 skipped`
- Docker working: confirmed with `docker compose up -d --build`
- Docker worker stack verified: `backend`, `frontend`, `db`, `redis`, `qdrant`, `celery_worker`
- Alembic migrations working: confirmed with `docker compose exec backend alembic upgrade head` and `docker compose exec backend alembic current` -> `20260622_0012 (head)`
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
- Sentence-aware Chunking + Chunk Validation foundation verified with local pytest coverage and Docker backend verification
- Embedding Model Registry foundation verified with local pytest coverage and Docker backend verification
- Embedding Generation foundation verified with local pytest coverage and Docker backend verification
- Qdrant Indexing foundation verified with local pytest coverage, Docker backend verification, Alembic head `20260620_0011`, and `/health/runtime`
- Hybrid Retrieval foundation verified with local pytest coverage, Docker backend verification, existing Alembic head `20260620_0011`, and `/health/runtime`
- Celery Job Tracking foundation verified with local pytest coverage, Docker backend verification, Alembic head `20260622_0012`, and `/health/runtime`
- Brain Agent Qdrant RAG Integration verified with local pytest coverage, Docker backend verification, existing Alembic head `20260622_0012`, and `/health/runtime`

## 28. Commit Tracking

Current `git log --oneline` history:

- `936dc82` Add Celery job tracking foundation
- `b46e39c` Add hybrid retrieval foundation
- `a44be88` Add Qdrant indexing foundation
- `130ad5d` Add embedding generation foundation
- `0138188` Add embedding model registry foundation
- `e178fb3` Add sentence-aware RAG chunking foundation
- `1860342` Add RAG source ingestion foundation
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

- The Sentence-aware Chunking + Chunk Validation foundation is committed as `e178fb3 Add sentence-aware RAG chunking foundation`.
- The Embedding Model Registry foundation is committed as `0138188 Add embedding model registry foundation`.
- The Embedding Generation foundation is committed as `130ad5d Add embedding generation foundation`.
- The Qdrant Indexing foundation is committed as `a44be88 Add Qdrant indexing foundation`.
- The Hybrid Retrieval foundation is committed as `b46e39c Add hybrid retrieval foundation`.
- The Celery Job Tracking foundation is committed as `936dc82 Add Celery job tracking foundation`.
- The Brain Agent Qdrant RAG Integration is the current uncommitted slice in the working tree.

Future commit entry format:

```md
### YYYY-MM-DD - Commit message
- Changed area:
- What was added:
- Tests run:
- Migration status:
- Docker verified:
```

## 29. Mandatory Future Rule

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
