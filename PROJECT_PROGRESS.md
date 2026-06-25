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

- Backend tests passing locally: `260 passed`
- Backend tests passing in Docker: `258 passed, 2 skipped`
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
- RAG Evaluation Harness verified with local pytest coverage, Docker backend verification, existing Alembic head `20260622_0012`, and `/health/runtime`
- Celery RAG Pipeline Orchestration verified with local pytest coverage, Docker backend verification, existing Alembic head `20260622_0012`, and `/health/runtime`
- End-to-End Demo Seed/Smoke Flow verified with local pytest coverage, Docker backend verification, existing Alembic head `20260622_0012`, `/health/runtime`, and Docker smoke script PASS

## 28. Task 22 RAG Evaluation Harness

Changed area:

- backend-only evaluation foundation for the grounded Brain Agent + Qdrant RAG flow

What was added:

- new module `backend/app/modules/rag_evaluation/`
- deterministic evaluation case schema for profile facts, memory evidence, retrieved RAG evidence, expected behavior, expected markers, forbidden claims, and minimum evidence requirements
- pure evaluation logic that classifies answers as `grounded_answer`, `lack_of_evidence`, or `partial_answer_with_uncertainty`
- structured pass/fail results with reasons, evidence counts, missing markers, forbidden-claim detection, answer preview, provider name, and response metadata
- service methods for `build_chat_request`, `run_eval_case`, and `run_eval_suite`
- foundation eval cases for grounded context present vs. lack-of-evidence behavior
- backend tests covering grounded pass/fail, forbidden-claim detection, lack-of-evidence pass/fail, no external AI HTTP client use in tests, no stored query embeddings, and suite summary aggregation

Intentionally not implemented:

- no frontend UI or dashboard
- no new billing, subscription, tariff, or payment logic
- no Qdrant indexing behavior changes
- no embedding persistence changes
- no stored query embeddings for evaluation requests
- no Celery worker architecture changes
- no API router for the eval harness in this slice
- no LLM-as-judge or external observability tooling

Verification commands and results:

- `python -m pytest` -> `243 passed`
- `docker compose up -d --build` -> success
- `docker compose exec backend alembic upgrade head` -> success
- `docker compose exec backend alembic current` -> `20260622_0012 (head)`
- `docker compose exec backend python -m pytest` -> `241 passed, 2 skipped`
- `Invoke-RestMethod http://localhost:8033/health/runtime` -> `{"status":"ok","database":"ok","redis":"ok"}`

## 29. Task 23 Celery RAG Pipeline Orchestration

Changed area:

- backend-only tracked orchestration for processing one owned RAG source through chunking, embedding generation, and Qdrant indexing

What was added:

- new module `backend/app/modules/rag_pipeline/`
- authenticated `POST /api/rag-sources/{source_id}/process` endpoint
- new Celery task `app.worker.tasks.run_rag_source_processing_job`
- pipeline service that creates a `BackgroundJob`, enqueues Celery, stores the Celery task id, and delegates worker execution to existing RAG services
- minimal `job_tracking.create_job` extension to allow initial progress fields without changing existing callers
- tests for authentication, own-source access, cross-user 404s, queued job creation, Celery task id storage, progress updates, success payloads, failure payloads, service usage, no Brain Agent calls, no retrieval behavior calls, no query embedding creation, existing chunk reuse on rerun, eager Celery compatibility, and job visibility through existing job endpoints

How the tracked pipeline works:

- API validates ownership of the requested `RagSource`
- API creates a `BackgroundJob` with `job_type = rag_source_ingestion`, `status = queued`, `progress_current = 0`, and `progress_total = 4`
- API enqueues `run_rag_source_processing_job` and stores `celery_task_id` on the `BackgroundJob`
- worker marks the job `running`
- worker validates source ownership and updates progress to `1/4`
- worker reuses existing chunks on rerun, otherwise calls existing `chunk_rag_source`, then updates progress to `2/4`
- worker calls existing `embed_source_chunks` and updates progress to `3/4`
- worker calls existing `index_source_embeddings` and updates progress to `4/4`
- worker marks the job `succeeded` with result counts, or `failed` with a structured error payload
- existing `/api/jobs` and `/api/jobs/{job_id}` remain the tracking read surface

Result payload structure:

- `source_id`
- `profile_id`
- `chunks_total`
- `chunks_valid`
- `chunks_warning`
- `chunks_invalid`
- `embeddings_total`
- `embeddings_created`
- `embeddings_skipped`
- `embeddings_failed`
- `indexed_total`
- `embeddings_indexed`
- `indexing_skipped`
- `indexing_failed`
- `model_code`
- `qdrant_collection`
- `completed_at`

Error payload structure:

- `code`
- `message`
- `step`
- `details.job_id`
- `details.source_id`
- `details.exception_type`

Intentionally not implemented:

- no frontend UI
- no billing, subscription, tariff, or payment changes
- no Brain Agent behavior changes
- no RAG retrieval behavior changes
- no Qdrant indexing semantic changes
- no new embedding providers
- no external AI/API calls
- no Celery broker or worker architecture changes
- no deletion of existing chunks, embeddings, vector indexes, or Qdrant points by the orchestration layer

Verification commands and results:

- `python -m pytest` -> `254 passed`
- `docker compose up -d --build` -> success
- `docker compose exec backend alembic upgrade head` -> success
- `docker compose exec backend alembic current` -> `20260622_0012 (head)`
- `docker compose exec backend python -m pytest` -> `252 passed, 2 skipped`
- `Invoke-RestMethod http://localhost:8033/health/runtime` -> `{"status":"ok","database":"ok","redis":"ok"}`

## 30. Task 24 End-to-End Demo Seed/Smoke Flow

Changed area:

- backend-only demo smoke flow proving the seeded RAG pipeline works end to end

What was added:

- new module `backend/app/modules/demo_smoke/`
- new script `backend/scripts/run_e2e_demo_smoke.py`
- deterministic safe demo user/profile/source seed flow using fictional data only
- script support for `--email`, `--profile-name`, `--json`, `--timeout-seconds`, and `--poll-interval-seconds`
- smoke runner that creates or reuses demo records, triggers the existing Celery RAG pipeline, polls the tracked `BackgroundJob`, verifies chunks, embeddings, Qdrant indexing records, retrieval evidence, chat/Brain Agent output, and the RAG evaluation harness
- tests covering safe fictional data, seed idempotency, required stage checks, PASS/FAIL behavior, no external AI calls, and no stored query embeddings

How to run the smoke script:

- Local backend working directory: `python scripts/run_e2e_demo_smoke.py`
- Docker backend container: `docker compose exec backend python scripts/run_e2e_demo_smoke.py`
- JSON output: `docker compose exec backend python scripts/run_e2e_demo_smoke.py --json`

What the script verifies:

- demo user/profile
- demo RAG source
- tracked Celery RAG pipeline job
- `BackgroundJob` success and progress `4/4`
- chunks exist
- embedded records exist
- Qdrant indexing records exist
- retrieval returns seeded evidence containing `sunflower`
- chat flow reaches the existing Brain Agent with grounded metadata
- answer contains the expected seeded marker
- RAG evaluation harness passes the grounded answer case

Docker smoke result:

```text
E2E DEMO SMOKE RESULT: PASS

[PASS] user/profile
[PASS] profile
[PASS] source
[PASS] job
[PASS] job_status
[PASS] chunks
[PASS] embeddings
[PASS] qdrant_indexing
[PASS] retrieval
[PASS] retrieval_marker
[PASS] chat/brain_answer
[PASS] chat_grounding
[PASS] evaluation
```

Intentionally not implemented:

- no frontend UI
- no billing, subscription, tariff, or payment changes
- no Brain Agent behavior changes
- no RAG retrieval behavior changes
- no Qdrant indexing semantic changes
- no Celery worker architecture changes
- no new AI providers or embedding providers
- no real external AI/API calls
- no database wipe, Qdrant wipe, or deletion of unrelated data

Verification commands and results:

- `python -m pytest` -> `260 passed`
- `docker compose up -d --build` -> success
- `docker compose exec backend alembic upgrade head` -> success
- `docker compose exec backend alembic current` -> `20260622_0012 (head)`
- `docker compose exec backend python -m pytest` -> `258 passed, 2 skipped`
- `docker compose exec backend python scripts/run_e2e_demo_smoke.py` -> `E2E DEMO SMOKE RESULT: PASS`
- `Invoke-RestMethod http://localhost:8033/health/runtime` -> `{"status":"ok","database":"ok","redis":"ok"}`

## 31. Task 25 Real Brain Provider Integration

Changed area:

- backend-only Brain Agent provider integration on top of the existing OpenAI-compatible provider foundation

What was added:

- production-ready `OpenAICompatibleBrainAgentProvider` request builder with normalized `/chat/completions` URL handling
- safe configuration support for `AI_BRAIN_TEMPERATURE` and `AI_BRAIN_MAX_TOKENS`
- strict request construction using the existing grounded Brain prompt without duplicating prompt-building or retrieval logic
- deterministic lack-of-evidence short-circuiting shared across Brain providers so factual questions with no evidence never call the real provider
- safe provider request/response error handling for timeout, network, HTTP status, invalid JSON, and invalid response shape cases
- response metadata enrichment with provider type, model, grounding status, latency, and token usage when returned
- dedicated provider tests covering config loading, payload construction, timeout/network/API failures, invalid responses, metadata safety, and no-evidence behavior

How to configure the OpenAI-compatible provider:

- `AI_BRAIN_PROVIDER=openai_compatible`
- `AI_BRAIN_MODEL=<provider model name>`
- `AI_BRAIN_API_KEY=<secret token>`
- `AI_BRAIN_BASE_URL=<provider base URL such as https://api.openai.com/v1>`
- `AI_BRAIN_TIMEOUT_SECONDS=<positive float>`
- optional `AI_BRAIN_TEMPERATURE=<0..2>`
- optional `AI_BRAIN_MAX_TOKENS=<positive integer>`

Exact provider behavior:

- default/test behavior remains `AI_BRAIN_PROVIDER=mock`
- when `AI_BRAIN_PROVIDER=openai_compatible`, the Brain Agent sends the existing grounded prompt as a single chat-completions user message
- the provider posts to `{AI_BRAIN_BASE_URL}/chat/completions` unless the configured base URL already ends with `/chat/completions`
- the request includes `model`, `messages`, `temperature`, and optional `max_tokens`
- the API key is only sent in the `Authorization` header and is not returned in metadata, errors, or API responses
- responses are parsed strictly from `choices[0].message.content`, with support for plain string content and text-part arrays

Intentionally not implemented:

- no frontend changes
- no billing, subscription, tariff, or payment changes
- no Qdrant indexing semantic changes
- no RAG retrieval semantic changes
- no Celery worker architecture changes
- no embedding generation or embedding persistence changes
- no new stored query embeddings
- no new RAG pipeline behavior
- no direct real external AI API calls in tests

Verification commands and results:

- `python -m pytest` -> `272 passed`
- `docker compose up -d --build` -> success
- `docker compose exec backend alembic upgrade head` -> success
- `docker compose exec backend alembic current` -> `20260622_0012 (head)`
- `docker compose exec backend python -m pytest` -> `270 passed, 2 skipped`
- `docker compose exec backend python scripts/run_e2e_demo_smoke.py` -> `E2E DEMO SMOKE RESULT: PASS`
- `Invoke-RestMethod http://localhost:8033/health/runtime` -> `{"status":"ok","database":"ok","redis":"ok"}`

## 32. Task 26 Universal RAG Quality Evaluation Foundation

Changed area:

- backend-only universal retrieval quality evaluation foundation for reusable cross-project RAG comparison

What was added:

- new module `backend/app/modules/rag_quality/`
- pure reusable schemas for datasets, eval cases, retrieval config candidates, generic retrieval results, case evaluations, config evaluations, dataset evaluations, and selection output
- deterministic retrieval-quality evaluator for case-level matching of expected markers, expected source IDs, expected chunk IDs, forbidden markers, and lack-of-evidence cases
- deterministic metrics for `hit_rate`, `recall_at_k`, `mrr`, `forbidden_marker_rate`, `average_latency_ms`, `cost_estimate_total`, `evidence_marker_coverage`, `missing_expected_marker_count`, and `false_positive_count`
- transparent best-config selector with structured ranking factors, reasons, warnings, and a safety override when a near-equal config has materially lower forbidden-marker risk
- small reusable foundation cases/dataset plus a lightweight adapter from current `rag_retrieval` response objects into generic `rag_quality` inputs
- dedicated tests covering schemas, metrics, selector behavior, generic-input support, no external API calls, and no stored query embeddings

How this differs from the existing `rag_evaluation` module:

- `rag_evaluation` checks Brain Agent answer groundedness and lack-of-evidence behavior after answer generation
- `rag_quality` evaluates retrieval/config quality before answer generation using deterministic retrieval evidence metrics only
- `rag_evaluation` is Brain-Agent-oriented and answer-oriented
- `rag_quality` is retrieval-model/config-oriented and dataset/candidate-oriented
- `rag_quality` does not replace `rag_evaluation`; it complements it

How this supports future multi-embedding comparison:

- datasets and eval cases are independent from Eternal World database entities
- retrieval config candidates model multiple embedding/retrieval combinations without creating providers or Qdrant collections yet
- dataset-level evaluation can compare multiple candidate configs side by side
- selector output is structured so future tasks can plug in real per-model execution and choose the best config by deterministic metrics
- the current adapter allows future reuse with existing `rag_retrieval` outputs while keeping the core evaluator generic

Exact module structure:

- `backend/app/modules/rag_quality/__init__.py`
- `backend/app/modules/rag_quality/cases.py`
- `backend/app/modules/rag_quality/datasets.py`
- `backend/app/modules/rag_quality/evaluator.py`
- `backend/app/modules/rag_quality/metrics.py`
- `backend/app/modules/rag_quality/schemas.py`
- `backend/app/modules/rag_quality/selectors.py`
- `backend/app/modules/rag_quality/service.py`

Intentionally not implemented:

- no frontend changes
- no billing, subscription, tariff, or payment changes
- no Brain Agent behavior changes
- no Qdrant indexing semantic changes
- no RAG retrieval semantic changes
- no Celery worker architecture changes
- no new embedding providers
- no multi-model execution
- no new Qdrant collections
- no production runtime retrieval auto-selection
- no public API endpoints for `rag_quality`
- no LLM judge or non-deterministic scoring
- no real external AI/API calls in tests

Verification commands and results:

- `python -m pytest` -> `284 passed`
- `docker compose up -d --build` -> success
- `docker compose exec backend alembic upgrade head` -> success
- `docker compose exec backend alembic current` -> `20260622_0012 (head)`
- `docker compose exec backend python -m pytest` -> `282 passed, 2 skipped`
- `docker compose exec backend python scripts/run_e2e_demo_smoke.py` -> `E2E DEMO SMOKE RESULT: PASS`
- `Invoke-RestMethod http://localhost:8033/health/runtime` -> `{"status":"ok","database":"ok","redis":"ok"}`

## 33. Task 27 Multi-Embedding Provider Execution

Changed area:

- backend-only multi-candidate embedding/retrieval execution foundation integrated with the existing `rag_quality` evaluator

What was added:

- new module `backend/app/modules/multi_embedding_eval/`
- authenticated endpoint `POST /api/rag-sources/{source_id}/multi-embedding-eval`
- Celery task `app.worker.tasks.run_multi_embedding_eval_job`
- orchestration service that:
  - validates owned `RagSource`
  - reuses existing chunks or chunks once when needed
  - runs each candidate through existing embedding generation
  - indexes each candidate into its own Qdrant collection
  - runs retrieval for each eval case query
  - converts retrieval results into generic `rag_quality` case inputs
  - delegates scoring and best-config selection to `rag_quality`
  - returns structured partial-success or failed job payloads
- candidate execution warnings/results schemas for safe per-candidate failure reporting
- minimal internal collection-override support in existing Qdrant indexing and retrieval services so evaluation can benchmark separate collections without changing production chat/runtime behavior
- dedicated tests covering auth, ownership, background job creation, Celery task id storage, per-candidate model/collection usage, chunk reuse, reuse of embedding/indexing services, `rag_quality` integration, partial success, total failure, no Brain Agent calls, no stored query embeddings, and no external API calls

How it uses `rag_quality`:

- `multi_embedding_eval` does not score candidates itself
- each candidate is converted into an existing `RagQualityRetrievalConfigCandidate`
- each retrieval response is converted through `RagQualityService.adapt_rag_retrieval_response`
- final comparison and best-config selection run through `RagQualityService.run_quality_evaluation`
- selector logic remains centralized in `rag_quality`

Why each embedding model/config has its own Qdrant collection:

- different embedding models can produce vectors in incompatible vector spaces and dimensions
- keeping one collection per candidate avoids mixing heterogeneous vector spaces
- separate collections preserve deterministic comparison between candidates
- the implementation is non-destructive: no collection wipe, no point deletion, and no cross-model mixing

Exact module structure:

- `backend/app/modules/multi_embedding_eval/__init__.py`
- `backend/app/modules/multi_embedding_eval/exceptions.py`
- `backend/app/modules/multi_embedding_eval/router.py`
- `backend/app/modules/multi_embedding_eval/schemas.py`
- `backend/app/modules/multi_embedding_eval/service.py`

Intentionally not implemented:

- no frontend changes
- no billing, subscription, tariff, or payment changes
- no Brain Agent behavior changes
- no production chat behavior changes
- no automatic production switch to the winning config
- no new embedding providers
- no pip package extraction
- no destructive Qdrant deletion/wipe behavior
- no new public retrieval selection semantics
- no real external AI/API calls in tests

Verification commands and results:

- `python -m pytest` -> `297 passed`
- `docker compose up -d --build` -> success
- `docker compose exec backend alembic upgrade head` -> success
- `docker compose exec backend alembic current` -> `20260622_0012 (head)`
- `docker compose exec backend python -m pytest` -> `295 passed, 2 skipped`
- `docker compose exec backend python scripts/run_e2e_demo_smoke.py` -> `E2E DEMO SMOKE RESULT: PASS`
- `Invoke-RestMethod http://localhost:8033/health/runtime` -> `{"status":"ok","database":"ok","redis":"ok"}`

## 34. Task 28 Active Retrieval Config Selection

Changed area:

- backend-only active retrieval configuration persistence and runtime selection on top of the existing `multi_embedding_eval` and `rag_quality` foundations

What was added:

- new module `backend/app/modules/active_retrieval_config/`
- authenticated endpoints:
  - `GET /api/memory-profiles/{profile_id}/active-retrieval-config`
  - `POST /api/memory-profiles/{profile_id}/active-retrieval-config`
  - `POST /api/rag-sources/{source_id}/multi-embedding-eval/{job_id}/activate-best`
- new `ActiveRetrievalConfig` SQLAlchemy model and Alembic migration `20260624_0013`
- ownership-scoped service/repository layer for reading and updating one active retrieval config per owned profile
- explicit activation path that reads a successful `multi_embedding_eval` job result, finds the winning candidate in the original request payload, and persists the selected runtime retrieval config with audit metadata
- minimal runtime retrieval integration so `rag_retrieval.retrieve_profile_rag` can use an active config when present while preserving the existing fallback path when none exists
- small JWT decode leeway to tolerate minor container clock skew observed during full Docker verification without changing auth semantics for normal callers

How active config is stored:

- one `active_retrieval_configs` row per profile
- `profile_id` is unique in this backend-only foundation, so updates overwrite the existing active row instead of keeping historical inactive rows
- stored fields include:
  - owner/profile ownership keys
  - `model_code`
  - `collection_name`
  - `top_k`
  - optional `score_threshold`
  - `retrieval_mode`
  - optional `source_eval_job_id`
  - optional `source_eval_dataset_id`
  - optional `selected_metrics`
  - optional `all_config_scores`
  - optional `selection_reason`
  - optional `warnings`
  - `is_active`
  - `selected_at`
  - `created_at`
  - `updated_at`

How runtime retrieval uses the selected config:

- `Brain Agent` chat flow was not changed to call a new subsystem directly
- chat still calls the existing `retrieve_profile_rag(...)` service abstraction
- `retrieve_profile_rag(...)` now looks up an active config for the owned profile before building the retrieval request
- when an active config exists and the caller did not explicitly override the model:
  - retrieval uses the active `model_code`
  - retrieval uses the active `collection_name`
- when the caller did not explicitly override limit or threshold:
  - retrieval uses active `top_k`
  - retrieval uses active `score_threshold`
- if no active config exists, the previous default retrieval behavior remains unchanged
- if a caller explicitly supplies `model_code`, retrieval keeps normal default collection-name resolution for that explicit model instead of forcing the active collection from a different model

How this relates to `multi_embedding_eval` and `rag_quality`:

- `multi_embedding_eval` still executes candidate embeddings/retrievals and delegates scoring to `rag_quality`
- `rag_quality` still remains the place that evaluates and ranks candidates
- `active_retrieval_config` does not rescore or reevaluate candidates
- explicit activation reads the successful `multi_embedding_eval` job result payload, uses `best_config`, `selected_metrics`, `all_config_scores`, and `warnings`, and stores the winning candidate as the runtime config for the profile
- failed `multi_embedding_eval` jobs are rejected for activation and do not change runtime retrieval behavior

Intentionally not implemented:

- no frontend changes
- no billing, subscription, tariff, or payment changes
- no Brain Agent answer-generation behavior changes beyond using the existing retrieval abstraction
- no automatic activation on every successful evaluation job
- no historical inactive config table rows yet
- no production chat multi-model evaluation per request
- no new embedding providers
- no Qdrant indexing semantic changes
- no real external AI/API calls in tests

Verification commands and results:

- focused verification:
  - `python -m pytest tests/test_models.py tests/test_alembic.py tests/test_active_retrieval_config.py` -> `13 passed`
  - `python -m pytest tests/test_rag_retrieval.py tests/test_multi_embedding_eval.py tests/test_ai_agents.py` -> `48 passed`
- required full verification:
  - `python -m pytest` -> `306 passed`
  - `docker compose up -d --build` -> success
  - `docker compose exec backend alembic upgrade head` -> success
  - `docker compose exec backend alembic current` -> `20260624_0013 (head)`
  - `docker compose exec backend python -m pytest` -> `304 passed, 2 skipped`
  - `Invoke-RestMethod http://localhost:8033/health/runtime` -> `{"status":"ok","database":"ok","redis":"ok"}`
  - `docker compose exec backend python scripts/run_e2e_demo_smoke.py` -> `E2E DEMO SMOKE RESULT: PASS`

## 35. Task 29 Real Local Embedding Provider - multilingual_e5_small

Changed area:

- backend-only real local embedding execution for `multilingual_e5_small` using lazy `SentenceTransformers` integration while preserving the existing mock-default behavior

What was added:

- new provider module `backend/app/modules/embeddings/providers/sentence_transformers.py`
- provider resolver logic in `backend/app/modules/embeddings/providers/__init__.py`
- optional settings:
  - `EMBEDDING_PROVIDER`
  - `SENTENCE_TRANSFORMERS_DEVICE`
  - `SENTENCE_TRANSFORMERS_CACHE_DIR`
- `sentence-transformers==3.3.1` added to backend requirements
- chunk embedding now calls provider `embed_passage(...)`
- retrieval query embedding now calls provider `embed_query(...)`
- `BaseEmbeddingProvider` gained default `embed_query(...)` and `embed_passage(...)` helpers so existing mock behavior stays compatible
- fake-model tests covering provider resolution, lazy loading, E5 query/passage formatting, safe provider failures, no-network behavior, and targeted integration coverage for chunk embedding, retrieval query embedding, Qdrant indexing, and `multi_embedding_eval`

Why only one real provider was added in this slice:

- this slice enables the first production-relevant local provider without widening the dependency, config, and CI surface to multiple heavy embedding backends at once
- `multilingual_e5_small` is already the existing default model profile in the registry and is the narrowest useful path for validating real local execution through the current embedding, retrieval, indexing, and evaluation pipeline
- `bge_m3`, Jina, and OpenAI-compatible embeddings were intentionally left out so the project can harden one local provider path first

How mock remains default for tests/dev:

- `EMBEDDING_PROVIDER` defaults to `mock`
- when `EMBEDDING_PROVIDER=mock`, even `multilingual_e5_small` continues to use the deterministic mock provider
- `mock_embedding` always resolves to `MockEmbeddingProvider`
- all existing tests and the demo smoke flow continue to run without downloading any real model
- the real provider path is exercised in tests only through fake `SentenceTransformer` loader/inference stubs

How to configure and use `multilingual_e5_small`:

- set `EMBEDDING_PROVIDER=sentence_transformers`
- optionally set `SENTENCE_TRANSFORMERS_DEVICE=cpu` or another supported local device string
- optionally set `SENTENCE_TRANSFORMERS_CACHE_DIR` if model cache location should be controlled explicitly
- then existing embedding generation and retrieval flows can use `model_code=multilingual_e5_small` and will resolve to local `SentenceTransformers` execution
- no public API rename was required; the existing chunk embedding, source embedding, retrieval, Qdrant indexing, and `multi_embedding_eval` paths keep the same route surface

How `multilingual_e5_small` is executed:

- the provider is resolved through the existing model-code path, not a new public API
- when enabled, `multilingual_e5_small` maps to Hugging Face model `intfloat/multilingual-e5-small`
- model loading is lazy and cached per provider instance
- import and model construction happen only when the provider is actually used
- chunk/source embeddings are treated as passages
- retrieval query embeddings are treated as queries
- vector length is validated against the registry dimension `384`

How query versus passage/chunk text is handled:

- query text is normalized and prefixed as `query: ...`
- chunk/passage text is normalized and prefixed as `passage: ...`
- this keeps the E5 usage pattern explicit while preserving the existing storage and retrieval contracts

Intentionally not implemented:

- no frontend changes
- no billing, subscription, tariff, or payment changes
- no Brain Agent behavior changes
- no production chat behavior changes
- no active retrieval config behavior changes
- no `rag_quality` selector/scoring changes
- no `multi_embedding_eval` orchestration redesign
- no BGE-M3 real provider
- no Jina real provider
- no OpenAI-compatible embedding provider
- no GPU requirement
- no external API calls
- no query embedding persistence
- no Qdrant wipe or point deletion

Verification commands and results:

- focused verification:
  - `python -m pytest tests/test_embeddings_sentence_transformers.py tests/test_embeddings.py tests/test_rag_retrieval.py tests/test_qdrant_indexing.py tests/test_multi_embedding_eval.py` -> `69 passed`
  - `python -m pytest tests/test_embedding_models.py tests/test_active_retrieval_config.py tests/test_rag_quality.py` -> `36 passed`
- required full verification:
  - `python -m pytest` -> `318 passed`
  - `docker compose up -d --build` -> success
  - `docker compose exec backend alembic upgrade head` -> success
  - `docker compose exec backend alembic current` -> `20260624_0013 (head)`
  - `docker compose exec backend python -m pytest` -> `316 passed, 2 skipped`
  - `Invoke-RestMethod http://localhost:8033/health/runtime` -> `{"status":"ok","database":"ok","redis":"ok"}`
  - `docker compose exec backend python scripts/run_e2e_demo_smoke.py` -> `E2E DEMO SMOKE RESULT: PASS`

## 36. Task 30 BGE-M3 Embedding Provider

Changed area:

- backend-only extension of the existing local `SentenceTransformers` embedding path so `model_code=bge_m3` can execute against `BAAI/bge-m3` without changing default mock behavior

What was added:

- `SentenceTransformersEmbeddingProvider` now supports both:
  - `multilingual_e5_small` -> `intfloat/multilingual-e5-small`
  - `bge_m3` -> `BAAI/bge-m3`
- existing provider resolution now allows `bge_m3` to use the real local provider only when `EMBEDDING_PROVIDER=sentence_transformers`
- BGE-M3 query embedding support through the current retrieval path
- BGE-M3 passage/chunk embedding support through the current chunk/source embedding path
- model-specific input preparation:
  - E5 keeps `query:` / `passage:` prefixes
  - BGE-M3 uses normalized raw text without those prefixes
- fake-model test coverage for:
  - BGE provider resolution
  - BGE lazy loading
  - BGE query/passage formatting
  - BGE vector dimension validation
  - chunk embedding with `bge_m3`
  - query embedding with `bge_m3` without persisted query embeddings
  - Qdrant indexing compatibility for `bge_m3`
  - `multi_embedding_eval` support for a `bge_m3` candidate

Why BGE-M3 was added as a separate slice after `multilingual_e5_small`:

- Task 29 established the reusable local `SentenceTransformers` execution path with the narrower `multilingual_e5_small` model first
- this slice extends that already-proven path to a second production-relevant local model without widening the architecture to new provider families
- shipping BGE-M3 separately keeps the change surface constrained while validating that the current embedding, indexing, retrieval, and evaluation pipeline can support multiple real local dense models behind the same provider gate

How mock remains default for tests/dev:

- `EMBEDDING_PROVIDER` still defaults to `mock`
- `mock_embedding` still always resolves to `MockEmbeddingProvider`
- real local `SentenceTransformers` execution is only used when explicitly enabled
- tests use fake loader/inference stubs and do not download real models

How to configure and use `bge_m3`:

- set `EMBEDDING_PROVIDER=sentence_transformers`
- optionally set `SENTENCE_TRANSFORMERS_DEVICE`
- optionally set `SENTENCE_TRANSFORMERS_CACHE_DIR`
- use existing embedding/retrieval flows with `model_code=bge_m3`
- chunk/source embedding persists dense BGE-M3 vectors through the existing `RagEmbedding` path
- retrieval query embedding uses BGE-M3 at request time and still does not persist query embeddings

How `bge_m3` is executed:

- provider resolution stays inside `backend/app/modules/embeddings/providers/__init__.py`
- `bge_m3` maps to `BAAI/bge-m3` inside `backend/app/modules/embeddings/providers/sentence_transformers.py`
- model import and construction are lazy and happen only when the provider is first used
- loaded model instances are cached per provider instance by normalized model code
- dense output vectors are validated against the registry dimension `1024`
- Qdrant indexing keeps one dense-vector collection per model/config and remains non-destructive

Intentionally not implemented:

- no frontend changes
- no billing, subscription, tariff, or payment changes
- no Brain Agent behavior changes
- no production chat behavior changes
- no active retrieval config behavior changes
- no `rag_quality` selector/scoring changes
- no `multi_embedding_eval` orchestration redesign beyond using the existing embedding service with `bge_m3`
- no Jina provider
- no OpenAI-compatible embedding provider
- no sparse retrieval
- no ColBERT / multi-vector retrieval
- no pip package extraction
- no external API calls

Verification commands and results:

- focused verification:
  - `python -m pytest tests/test_embeddings_sentence_transformers.py tests/test_embeddings.py tests/test_rag_retrieval.py tests/test_qdrant_indexing.py tests/test_multi_embedding_eval.py` -> `77 passed`
  - `python -m pytest tests/test_embedding_models.py tests/test_active_retrieval_config.py tests/test_rag_quality.py` -> `36 passed`
- required full verification:
  - `python -m pytest` -> `326 passed`
  - `docker compose up -d --build` -> success
  - `docker compose exec backend alembic upgrade head` -> success
  - `docker compose exec backend alembic current` -> `20260624_0013 (head)`
  - `docker compose exec backend python -m pytest` -> `324 passed, 2 skipped`
  - `Invoke-RestMethod http://localhost:8033/health/runtime` -> `{"status":"ok","database":"ok","redis":"ok"}`
  - `docker compose exec backend python scripts/run_e2e_demo_smoke.py` -> `E2E DEMO SMOKE RESULT: PASS`

## 37. Task 31 Real Multi-Embedding Evaluation Smoke Test

Changed area:

- backend-only smoke/evaluation orchestration for the already implemented real local embedding candidates `multilingual_e5_small` and `bge_m3`

What was added:

- new module `backend/app/modules/real_multi_embedding_eval_smoke/`
- new script `backend/scripts/run_real_multi_embedding_eval_smoke.py`
- new test `backend/tests/test_real_multi_embedding_eval_smoke.py`
- synchronous smoke runner that reuses existing module boundaries instead of duplicating evaluation logic:
  - creates or reuses a safe fictional smoke user
  - creates or reuses a dedicated profile and RAG source
  - runs `multi_embedding_eval` for exactly two candidates:
    - `multilingual_e5_small`
    - `bge_m3`
  - indexes each candidate into its own Qdrant collection
  - passes retrieval results into the existing `rag_quality` flow
  - activates the winning config through the existing `active_retrieval_config` service
  - verifies runtime retrieval resolves the activated config without changing production chat behavior
- default fake `SentenceTransformer` model objects for the smoke script/test path so CI and normal verification do not download real Hugging Face models
- optional explicit real-local-model execution path for manual runs when desired

What the smoke flow verifies:

- the source can be created or reused safely
- chunking is available for the evaluation source
- both embedding candidates can generate chunk embeddings through the existing `SentenceTransformers` provider path
- both candidates can be indexed into separate Qdrant collections
- both candidates can be evaluated through `multi_embedding_eval`
- `rag_quality` receives both candidate result sets and selects a winner
- the winning candidate can be activated into `active_retrieval_config`
- runtime retrieval resolves the activated config and uses the winning collection/model

How `multilingual_e5_small` and `bge_m3` are compared:

- the smoke request builds exactly two candidates in one `MultiEmbeddingEvalRequest`
- both candidates use the same smoke dataset and query
- both candidates run through the existing embedding, indexing, retrieval, and `rag_quality` selection path
- the default fake-model mode intentionally makes the two candidates produce different retrieval quality so the winning config is deterministic in the smoke fixture

How Qdrant collections are kept separate:

- the smoke runner assigns explicit per-candidate collection names:
  - `eternal_world_rag_chunks__multilingual_e5_small__real_multi_eval_smoke`
  - `eternal_world_rag_chunks__bge_m3__real_multi_eval_smoke`
- indexing remains non-destructive
- existing collections are not wiped
- existing points are not deleted

How the selected config is activated:

- after synchronous `process_multi_embedding_eval_job(...)` completes successfully, the smoke runner calls `activate_best_multi_embedding_eval_result(...)`
- the existing activation service reads the winning candidate from the evaluation job payload and upserts one active config row for the profile
- the runner then reads the stored active config back through `get_active_retrieval_config(...)`

How tests avoid real model downloads/network:

- the smoke runner defaults to `use_real_local_models=False`
- in that default mode it forces the existing `SentenceTransformers` provider path but monkeypatches model loading to a deterministic in-memory fake class
- tests use a fake Qdrant client and explicit HTTP failure guards
- no real external API calls are used in the smoke tests

How to run the new smoke flow:

- default fake/mock-safe path:
  - `docker compose exec backend python scripts/run_real_multi_embedding_eval_smoke.py`
- optional explicit real local model path:
  - `docker compose exec backend sh -lc "REAL_MULTI_EMBEDDING_SMOKE_USE_REAL_LOCAL_MODELS=1 EMBEDDING_PROVIDER=sentence_transformers python scripts/run_real_multi_embedding_eval_smoke.py --use-real-local-models"`

Intentionally not implemented:

- no new embedding provider
- no Jina provider
- no OpenAI-compatible embedding provider
- no sparse retrieval
- no ColBERT / multi-vector retrieval
- no frontend changes
- no billing, subscription, tariff, or payment changes
- no pip package extraction

Verification commands and results:

- focused verification:
  - `python -m pytest tests/test_real_multi_embedding_eval_smoke.py tests/test_multi_embedding_eval.py tests/test_active_retrieval_config.py tests/test_rag_retrieval.py tests/test_qdrant_indexing.py` -> `54 passed`
  - `python -m pytest tests/test_embeddings_sentence_transformers.py tests/test_embeddings.py tests/test_rag_quality.py` -> `45 passed`
- required full verification:
  - `python -m pytest` -> `328 passed`
  - `docker compose up -d --build` -> success
  - `docker compose exec backend alembic upgrade head` -> success
  - `docker compose exec backend alembic current` -> `20260624_0013 (head)`
  - `docker compose exec backend python -m pytest` -> `326 passed, 2 skipped`
  - `Invoke-RestMethod http://localhost:8033/health/runtime` -> `{"status":"ok","database":"ok","redis":"ok"}`
  - `docker compose exec backend python scripts/run_e2e_demo_smoke.py` -> `E2E DEMO SMOKE RESULT: PASS`
  - `docker compose exec backend python scripts/run_real_multi_embedding_eval_smoke.py` -> `REAL MULTI-EMBEDDING SMOKE RESULT: PASS`

## 38. Task 32 Real Local Model Question Evaluation

Changed area:

- backend-only real question-based retrieval evaluation for the already implemented local embedding candidates `multilingual_e5_small` and `bge_m3`

What was added:

- new module `backend/app/modules/real_question_eval/`
  - `__init__.py`
  - `schemas.py`
  - `service.py`
  - `report.py`
- new script `backend/scripts/run_real_question_eval.py`
- new focused test `backend/tests/test_real_question_eval.py`
- a deterministic fictional evaluation fixture that:
  - creates or reuses one dedicated evaluation user/profile/source
  - builds a multi-question dataset with real retrieval queries
  - reuses the existing chunking, embedding, indexing, retrieval, `multi_embedding_eval`, `rag_quality`, and `active_retrieval_config` services
  - writes a human-readable markdown artifact to `backend/artifacts/real_question_eval/real_question_eval_report.md`
- default fake `SentenceTransformers` runtime for tests and default script runs
- explicit opt-in real-local-model mode through:
  - env flag `REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1`
  - CLI flag `--use-real-local-models`

Why this task was added before Jina/OpenAI-compatible providers:

- the project already had two local dense candidates wired through the same provider family and selector path
- this slice answers the first product-critical retrieval question before widening provider surface area:
  - which current local model actually retrieves better evidence for real questions
- running a question-based comparison now hardens the current local retrieval path before adding Jina, OpenAI-compatible embeddings, sparse retrieval, or ColBERT-style changes

Question fixture used:

- safe fictional archive-style corpus stored in one deterministic manual-text RAG source
- topics covered:
  - old village house / `sunflower seeds` / `blue gate latch`
  - winter trip / `overnight train ticket` / `wooden thermos`
  - grandmother soup / `dried mushrooms` / `oak stove`
  - one shared distractor section with:
    - `rose market poster`
    - `summer bus timetable`
    - `vanilla jam`
- dataset size:
  - 3 real questions
  - 2 candidates per question
  - top-k retrieval recorded per candidate

How questions are evaluated:

- the runner submits exactly these two candidates into one `MultiEmbeddingEvalRequest`:
  - `multilingual_e5_small`
  - `bge_m3`
- `process_multi_embedding_eval_job(...)` remains the official selector path and still performs:
  - chunk reuse/creation
  - model-specific source embeddings
  - per-candidate Qdrant indexing
  - per-question retrieval
  - aggregate `rag_quality` scoring
  - best-config selection
- after the official eval completes, the new runner performs another deterministic retrieval pass per question/per candidate to capture report details:
  - top chunks
  - chunk ids
  - scores
  - previews
  - matched expected markers
  - missing expected markers
  - distractor markers
  - evidence coverage
  - first relevant rank
  - deterministic answer summary
  - groundedness verdict

How `multilingual_e5_small` and `bge_m3` are compared:

- both candidates index the same chunk corpus into different Qdrant collections
- both candidates receive the same 3 real questions
- the markdown report shows the actual retrieved chunks and evidence differences for every question
- `rag_quality` remains the official aggregate selector for activation
- the per-question winner shown in the report is derived from retrieval evidence quality, with priority on:
  - passed/failed retrieval quality
  - evidence coverage
  - distractor count
  - first relevant rank
  - top retrieval score

How markdown report is produced:

- `backend/app/modules/real_question_eval/report.py` renders a VS Code-friendly markdown file
- the report includes:
  - timestamp
  - dataset/model summary
  - per-question expectations
  - per-model retrieved chunks with scores and previews
  - matched/missing/distractor markers
  - deterministic answer summaries and groundedness verdicts
  - per-question winner and reason
  - aggregate model metrics
  - final activation/runtime verification details

Task 32 artifact export completion update:

- current runtime export now writes only into:
  - `backend/artifacts/real_question_eval/latest_real/`
  - `backend/artifacts/real_question_eval/latest_fake/`
  - `backend/artifacts/real_question_eval/runs/<run_id>_real/`
  - `backend/artifacts/real_question_eval/runs/<run_id>_fake/`
- each run writes both:
  - `real_question_eval_report.md`
  - `real_question_eval_result.json`
- fake runs update only `latest_fake/` and never overwrite `latest_real/`
- if `latest_real/` is missing, the exporter can backfill it from the newest existing historical real run artifact on disk without rerunning real-local models
- the root-level artifact file is kept only as historical evidence from the earlier manual real-local run and is not used as the current output target
- markdown is now intentionally ordered as:
  - `## Client Summary`
  - `## Artifact Files`
  - `## Client Question Breakdown`
  - `## Aggregate Client Decision`
  - `## Developer Details`
- JSON is now intentionally split into:
  - `client_view`
  - `developer_view`
- JSON now also includes `run_type` with `real` or `fake`
- artifact paths are embedded in both markdown and JSON so the latest and archived files are easy to open in VS Code

Historical real-local evidence handling:

- an existing manual real-local report on disk remains valid historical evidence
- follow-up export-fix work does not require inventing new real-local results
- in the final constrained follow-up run, real-local evaluation was intentionally not rerun by user instruction

How Qdrant collections are kept separate:

- the runner uses explicit candidate collection names:
  - `eternal_world_rag_chunks__multilingual_e5_small__real_question_eval`
  - `eternal_world_rag_chunks__bge_m3__real_question_eval`
- model-specific dimensions remain separate:
  - `multilingual_e5_small` -> `384`
  - `bge_m3` -> `1024`
- indexing remains non-destructive
- existing Qdrant collections are not wiped
- existing Qdrant points are not deleted

How the selected config is activated:

- after `multi_embedding_eval` succeeds, the runner calls `activate_best_multi_embedding_eval_result(...)`
- the existing activation service reads the winning candidate from the successful background job payload
- the selected candidate is stored in `active_retrieval_config` with:
  - model code
  - collection name
  - top_k
  - source eval job id
  - source eval dataset id
  - selected metrics
  - all config scores

How runtime retrieval is verified:

- after activation, the runner calls `get_active_retrieval_config(...)`
- then it calls `retrieve_profile_rag(...)` without overriding `model_code`
- verification passes only if runtime retrieval resolves:
  - the activated model code
  - the activated collection name
  - the expected active-config top-k path

How tests avoid real model downloads and network:

- tests default to fake local models and never enable real local model loading
- the runner temporarily forces the existing `sentence_transformers` provider path but swaps in deterministic fake `SentenceTransformer` objects
- fake vectors preserve the real configured dimensions:
  - `multilingual_e5_small` -> `384`
  - `bge_m3` -> `1024`
- tests use a fake in-memory Qdrant client
- tests install explicit HTTP failure guards so external network calls fail immediately
- no real external API calls are used in tests

What is intentionally not implemented:

- no new embedding provider
- no Jina provider
- no OpenAI-compatible embedding provider
- no sparse retrieval
- no ColBERT / multi-vector retrieval
- no frontend changes
- no billing, subscription, tariff, or payment changes
- no Brain Agent production answer-behavior changes
- no production chat behavior changes
- no pip package extraction
- no real external API calls in tests

Verification commands and results:

- focused verification:
  - `python -m pytest tests/test_real_question_eval.py tests/test_real_multi_embedding_eval_smoke.py tests/test_multi_embedding_eval.py tests/test_active_retrieval_config.py tests/test_rag_retrieval.py tests/test_qdrant_indexing.py` -> `56 passed in 58.48s`
  - `python -m pytest tests/test_embeddings_sentence_transformers.py tests/test_embeddings.py tests/test_rag_quality.py` -> `45 passed in 22.27s`
- required full verification:
  - `python -m pytest` -> `330 passed in 294.62s`
  - `docker compose up -d --build` -> success
  - `docker compose exec backend alembic upgrade head` -> success
  - `docker compose exec backend alembic current` -> `20260624_0013 (head)`
  - `docker compose exec backend python -m pytest` -> `328 passed, 2 skipped, 1 warning in 253.77s`
  - `Invoke-RestMethod http://localhost:8033/health/runtime` -> `{"status":"ok","database":"ok","redis":"ok"}`
  - `docker compose exec backend python scripts/run_e2e_demo_smoke.py` -> `E2E DEMO SMOKE RESULT: PASS`
  - `docker compose exec backend python scripts/run_real_multi_embedding_eval_smoke.py` -> `REAL MULTI-EMBEDDING SMOKE RESULT: PASS`
  - `docker compose exec backend python scripts/run_real_question_eval.py` -> `REAL QUESTION EVAL RESULT: PASS`
    - overall winner: `bge_m3`
    - per-question winners:
      - `question-sunflower-house` -> `bge_m3`
      - `question-winter-trip` -> `bge_m3`
      - `question-grandmother-soup` -> `bge_m3`
    - report path inside container: `/app/artifacts/real_question_eval/real_question_eval_report.md`
- notes:
  - no transient failures or retries were required
  - existing pytest warnings remained:
    - local runs emit the existing `pytest_asyncio` default-loop-scope deprecation warning
    - docker pytest emits the existing `passlib` `crypt` deprecation warning

Artifact export follow-up verification:

- constrained verification only, per user instruction:
  - `python -m pytest tests/test_real_question_eval.py` -> `5 passed in 21.20s`
  - `docker compose exec backend python scripts/run_real_question_eval.py` -> `REAL QUESTION EVAL RESULT: PASS`
    - used fake models: `true`
    - overall winner: `bge_m3`
    - activated: `true`
    - runtime verified: `true`
    - latest markdown: `/app/artifacts/real_question_eval/latest_fake/real_question_eval_report.md`
    - latest json: `/app/artifacts/real_question_eval/latest_fake/real_question_eval_result.json`
    - archived markdown: `/app/artifacts/real_question_eval/runs/20260625_131055Z_fake/real_question_eval_report.md`
    - archived json: `/app/artifacts/real_question_eval/runs/20260625_131055Z_fake/real_question_eval_result.json`
    - preserved historical real latest slot: `latest_real/` was not overwritten by the fake run
- intentionally not rerun in this constrained follow-up:
  - full local pytest
  - full Docker pytest matrix
  - real-local model evaluation

## Úkol 33 Runtime Guardrails for Evaluation vs Production Retrieval

Changed area:

- backend-only guardrails for `real_question_eval` execution mode separation and artifact safety

What was added:

- explicit evaluation execution-mode persistence in `real_question_eval` JSON artifacts:
  - `fake_eval`
  - `real_eval`
- manual-only real-local evaluation guard in `backend/scripts/run_real_question_eval.py`
  - real-local eval now requires both:
    - CLI flag `--use-real-local-models`
    - env var `REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1`
  - if only one signal is present, the script fails fast with a clear error
  - if neither signal is present, the script defaults to fake-safe mode
- fake/report validation remains isolated from preserved real artifacts:
  - fake runs write only to `latest_fake/` and `runs/<run_id>_fake/`
  - fake runs do not overwrite `latest_real/`
- production retrieval remains separated from evaluation flow:
  - this task adds runtime guardrails to the evaluation path only
  - no production chat or retrieval behavior was modified to execute evaluation
- focused test coverage now verifies:
  - default mode resolves to `execution_mode=fake_eval`
  - persisted JSON contains `execution_mode`
  - client and developer views remain present
  - artifact paths remain separated
  - real-local mode requires both manual signals
  - CLI-only and env-only real-local requests fail fast

Verification commands and results:

- `python -m pytest tests/test_real_question_eval.py -q` -> `9 passed`
- `docker compose exec backend python scripts/run_real_question_eval.py` -> `REAL QUESTION EVAL RESULT: PASS`
  - `execution_mode: fake_eval`
  - `used_fake_models: true`
  - `overall_winner: bge_m3`
  - `latest_markdown_report: /app/artifacts/real_question_eval/latest_fake/real_question_eval_report.md`
  - `latest_json_result: /app/artifacts/real_question_eval/latest_fake/real_question_eval_result.json`
  - `archived_markdown_report: /app/artifacts/real_question_eval/runs/20260625_135748Z_fake/real_question_eval_report.md`
  - `archived_json_result: /app/artifacts/real_question_eval/runs/20260625_135748Z_fake/real_question_eval_result.json`
  - preserved `latest_real/` was not targeted by the fake-safe run

## Úkol 34 Production Retrieval Runtime Smoke

Changed area:

- backend-only runtime smoke coverage for normal production retrieval using the active retrieval config path

What was added:

- new focused test `backend/tests/test_production_retrieval_runtime_smoke.py`
- fake-safe production retrieval smoke proving that a normal retrieval request:
  - reads and uses `active_retrieval_config` when present
  - performs one normal retrieval flow through `rag_retrieval`
  - does not execute evaluation flow entrypoints
  - does not write `real_question_eval` artifacts
- the smoke uses:
  - deterministic local test data
  - fake in-memory Qdrant behavior
  - the normal retrieval endpoint `/api/memory-profiles/{profile_id}/rag/retrieve`
- the smoke adds explicit test guards for:
  - preserved `real_question_eval` artifact tree remaining byte-for-byte unchanged
  - no eval artifact directory creation or file writes under `backend/artifacts/real_question_eval/`
  - no execution of loaded eval entrypoints from:
    - `real_question_eval`
    - `multi_embedding_eval`
    - `rag_quality`
- no production chat behavior, embedding providers, or real-local eval execution were modified

Verification commands and results:

- `python -m pytest tests/test_real_question_eval.py tests/test_production_retrieval_runtime_smoke.py -q` -> `10 passed`
- `python -m pytest -q` -> `338 passed`
- `python -m pytest --collect-only -q` -> `338 tests collected`

Runtime smoke outcome:

- production retrieval used the selected active config collection at query time
- production retrieval stayed on the normal retrieval path and did not execute eval
- production retrieval did not write `latest_real/`, `latest_fake/`, or `runs/` eval artifacts
- the test remained fake-safe throughout
- no real-local model evaluation was run

## Úkol 35 Add Next Embedding Provider Adapter

Changed area:

- backend-only embedding registry and SentenceTransformers adapter expansion for a third dense multilingual local baseline

What was added:

- added provider key `paraphrase_multilingual_mpnet_base_v2`
- mapped it to the SentenceTransformers model name:
  - `sentence-transformers/paraphrase-multilingual-mpnet-base-v2`
- kept the provider on the dense-only local SentenceTransformers path
- registered the new model as an enabled multilingual local embedding candidate alongside:
  - `multilingual_e5_small`
  - `bge_m3`
- extended fake-safe tests to verify:
  - registry/config accepts the new provider key
  - provider resolution uses the expected SentenceTransformers model name
  - fake SentenceTransformers execution returns the expected registry dimension `768`
  - the model can be included in multi-embedding evaluation configuration without real model loading
  - existing providers still resolve and work
  - mock/fake default behavior remains unchanged

What was intentionally not run:

- no real-local model evaluation
- no real SentenceTransformers model downloads
- no BGE-M3 real inference
- no MPNet real inference
- no DeepSeek/OpenAI/external embedding API calls

Next planned task:

- three-model retrieval evaluation smoke using:
  - `multilingual_e5_small`
  - `bge_m3`
  - `paraphrase_multilingual_mpnet_base_v2`

Verification commands and results:

- `python -m pytest tests/test_embedding_models.py tests/test_embeddings.py tests/test_embeddings_sentence_transformers.py tests/test_multi_embedding_eval.py tests/test_rag_quality.py -q` -> `83 passed`
- `python -m pytest -q` -> `345 passed`
- `python -m pytest --collect-only -q` -> `345 tests collected`

## Úkol 36 Add multilingual_e5_base Provider Adapter

Changed area:

- backend-only embedding registry and SentenceTransformers adapter expansion for another dense multilingual local baseline

What was added:

- added provider key `multilingual_e5_base`
- mapped it to the SentenceTransformers model name:
  - `intfloat/multilingual-e5-base`
- registered dimension `768`
- kept the provider on the dense-only local `sentence_transformers` path
- aligned formatting behavior with the existing E5 family:
  - query inputs use `query:`
  - passage inputs use `passage:`
- extended fake-safe tests to verify:
  - registry/config accepts the new provider key
  - provider resolution uses the expected SentenceTransformers model name
  - the provider dimension is `768`
  - the model can be included in multi-embedding evaluation configuration without real model loading
  - existing providers still resolve and work
  - mock/fake default behavior remains unchanged

What was intentionally not run:

- no real-local model evaluation
- no real SentenceTransformers model downloads
- no BGE-M3 real inference
- no MPNet real inference
- no `multilingual_e5_base` real inference
- no DeepSeek/OpenAI/external embedding API calls

Next planned task:

- real incremental evaluation for the two new providers:
  - `paraphrase_multilingual_mpnet_base_v2`
  - `multilingual_e5_base`

Verification commands and results:

- `python -m pytest tests/test_embedding_models.py tests/test_embeddings.py tests/test_embeddings_sentence_transformers.py tests/test_multi_embedding_eval.py tests/test_rag_quality.py -q` -> `90 passed`
- `python -m pytest -q` -> `352 passed`
- `python -m pytest --collect-only -q` -> `352 tests collected`

## Úkol 37 Incremental Real Eval for New Embedding Providers

Changed area:

- backend-only incremental real question evaluation flow for new local embedding providers while preserving the historical Task 32 baseline

What was added:

- explicit incremental real eval mode in `scripts/run_real_question_eval.py`:
  - `--incremental-real-providers paraphrase_multilingual_mpnet_base_v2,multilingual_e5_base`
- incremental mode requires:
  - `REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1`
- historical providers are preserved and not rerun:
  - `multilingual_e5_small`
  - `bge_m3`
- incremental comparison reads the preserved historical real artifact and combines it with a fresh real run for only:
  - `paraphrase_multilingual_mpnet_base_v2`
  - `multilingual_e5_base`
- the exact Task 32 dataset remained unchanged:
  - `question-sunflower-house`
  - `question-winter-trip`
  - `question-grandmother-soup`
- the exact fictional dataset text, evidence markers, distractors, chunking, scoring, and selector rules were preserved
- incremental comparison artifacts now write to:
  - `backend/artifacts/real_question_eval/latest_incremental_new_providers/`
  - `backend/artifacts/real_question_eval/runs/<run_id>_incremental_new_providers/`
- historical `latest_real/` is preserved and is not overwritten by incremental runs

Real incremental run outcome:

- exact command run:
  - `docker compose exec -e REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1 backend python scripts/run_real_question_eval.py --incremental-real-providers paraphrase_multilingual_mpnet_base_v2,multilingual_e5_base`
- historical providers were not rerun
- real model inference ran only for:
  - `paraphrase_multilingual_mpnet_base_v2`
  - `multilingual_e5_base`
- final per-question winners:
  - `question-sunflower-house` -> `multilingual_e5_small`
  - `question-winter-trip` -> `multilingual_e5_base`
  - `question-grandmother-soup` -> `multilingual_e5_base`
- final overall winner:
  - `multilingual_e5_base`
- comparison against the historical winner:
  - `multilingual_e5_base` beat historical `bge_m3`
  - `paraphrase_multilingual_mpnet_base_v2` did not beat `bge_m3`
- final production recommendation:
  - promote `multilingual_e5_base` after reviewing the incremental real comparison artifact

Comparison artifact paths:

- latest:
  - `backend/artifacts/real_question_eval/latest_incremental_new_providers/real_question_eval_report.md`
  - `backend/artifacts/real_question_eval/latest_incremental_new_providers/real_question_eval_result.json`
- archived:
  - `backend/artifacts/real_question_eval/runs/20260625_181027Z_incremental_new_providers/real_question_eval_report.md`
  - `backend/artifacts/real_question_eval/runs/20260625_181027Z_incremental_new_providers/real_question_eval_result.json`

Verification commands and results:

- `python -m pytest tests/test_real_question_eval.py tests/test_embeddings_sentence_transformers.py tests/test_multi_embedding_eval.py -q` -> `50 passed`
- `python -m pytest -q` -> `356 passed`
- `python -m pytest --collect-only -q` -> `356 tests collected`

## 39. Commit Tracking

Current `git log --oneline` history:

- `07bb407` Add Celery RAG pipeline orchestration
- `4712333` Add RAG evaluation harness
- `6235880` Connect Brain Agent to Qdrant RAG retrieval
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
- The Brain Agent Qdrant RAG Integration foundation is committed as `6235880 Connect Brain Agent to Qdrant RAG retrieval`.
- The RAG Evaluation Harness is committed as `4712333 Add RAG evaluation harness`.
- The Celery RAG Pipeline Orchestration is committed as `07bb407 Add Celery RAG pipeline orchestration`.
- The Real Local Embedding Provider - multilingual_e5_small foundation is the current uncommitted slice in the working tree.

Future commit entry format:

```md
### YYYY-MM-DD - Commit message
- Changed area:
- What was added:
- Tests run:
- Migration status:
- Docker verified:
```

## 40. Mandatory Future Rule

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

## Úkol 38 Fix Incremental Eval Winner Count Consistency

Changed area:

- `backend/app/modules/real_question_eval/`
- `backend/tests/test_real_question_eval.py`
- incremental comparison artifacts in `backend/artifacts/real_question_eval/latest_incremental_new_providers/` and `backend/artifacts/real_question_eval/runs/20260625_181027Z_incremental_new_providers/`

What was added:

- fixed the mismatch between per-question winners and aggregate `question_wins` by recomputing aggregate wins from persisted question winners during incremental result assembly
- added artifact-only incremental re-render support from existing JSON so the stale incremental report can be normalized without rerunning embeddings or retrieval
- added regression coverage proving the incremental artifact cannot keep stale `question_wins` values that disagree with question-level winners
- overall winner remains `multilingual_e5_base`

Verification commands and results:

- `python -m pytest tests/test_real_question_eval.py -q` -> `14 passed`
- `python -m pytest -q` -> timed out twice in shell (`246.9s` and `604.1s`), no failing assertion was returned before timeout
- `Select-String -Path ".\backend\artifacts\real_question_eval\latest_incremental_new_providers\real_question_eval_report.md" -Pattern "Question wins:"` -> visible counts corrected to `1, 0, 0, 2`

Safety / runtime notes:

- no real-local eval was rerun
- no embeddings were recomputed
- no model downloads or inference were run for this fix

Next planned work:

- broader full-version embedding benchmark plan
