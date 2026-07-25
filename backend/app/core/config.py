from __future__ import annotations

import json
from pathlib import Path

from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


BACKEND_DIR = Path(__file__).resolve().parents[2]
PROJECT_ROOT = BACKEND_DIR.parent
ENV_FILE_CANDIDATES = tuple(
    str(path)
    for path in (BACKEND_DIR / ".env", PROJECT_ROOT / ".env")
    if path.exists()
)


class Settings(BaseSettings):
    app_name: str = "Eternal World API"
    environment: str = "local"
    database_url: str = "postgresql+psycopg://eternal_user:eternal_password@db:5432/eternal_world"
    redis_url: str = "redis://redis:6379/0"
    backend_cors_origins: str = "http://localhost:8017,http://127.0.0.1:8017"
    sqlalchemy_echo: bool = False
    jwt_secret_key: SecretStr = SecretStr("unsafe-dev-jwt-secret-change-me")
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    jwt_issuer: str = "eternal-world"
    jwt_audience: str = "eternal-world-api"
    ai_brain_provider: str = "mock"
    ai_brain_model: str = ""
    ai_brain_api_key: SecretStr | None = None
    ai_brain_base_url: str = "https://api.openai.com/v1"
    ai_brain_timeout_seconds: float = Field(default=30, gt=0)
    ai_brain_temperature: float = Field(default=0.2, ge=0, le=2)
    ai_brain_max_tokens: int | None = Field(default=None, gt=0)
    ai_brain_memory_evidence_preview_length: int = Field(default=480, gt=0)
    ai_brain_rag_evidence_preview_length: int = Field(default=1200, gt=0)
    content_translation_provider: str = "mock"
    content_translation_model: str = ""
    content_translation_api_key: SecretStr | None = None
    content_translation_base_url: str = "https://api.openai.com/v1"
    content_translation_timeout_seconds: float = Field(default=20, gt=0)
    content_translation_max_retries: int = Field(default=1, ge=0)
    embedding_provider: str = "mock"
    sentence_transformers_device: str = "cpu"
    sentence_transformers_cache_dir: Path | None = None
    embedding_cache_enabled: bool = False
    embedding_cache_provider: str = "redis"
    embedding_cache_ttl_seconds: int = Field(default=0, ge=0)
    embedding_cache_key_prefix: str = "eternal_world"
    media_storage_provider: str = "local"
    media_root: Path = BACKEND_DIR / "media"
    media_public_base_url: str = "/media"
    media_max_file_size_bytes: int = Field(default=20 * 1024 * 1024, gt=0)
    qdrant_url: str = "http://qdrant:6333"
    qdrant_collection_name: str = "eternal_world_rag_chunks"
    qdrant_timeout_seconds: float = Field(default=10, gt=0)
    qdrant_indexing_enabled: bool = True
    celery_broker_url: str = "redis://redis:6379/1"
    celery_result_backend: str | None = "redis://redis:6379/1"
    celery_task_always_eager: bool = False
    celery_task_eager_propagates: bool = True
    #: Task 65.9 (Part O) - bounded task time limits. The soft limit is
    #: comfortably above real observed CPU BGE-M3 encode latency for a
    #: single short memory/biography chunk (seconds, not minutes) while
    #: still being far below "stuck forever"; the hard limit gives a
    #: grace window after the soft limit for cleanup before Celery kills
    #: the child process outright.
    celery_task_soft_time_limit_seconds: int = Field(default=180, gt=0)
    celery_task_time_limit_seconds: int = Field(default=240, gt=0)
    #: Task 65.7 - Redis-backed browser session cookie (in addition to, not
    #: replacing, the existing bearer JWT). Inactivity-based sliding TTL:
    #: refreshed on every resolved request, so a browser tab left open and
    #: actively used never hits a hard expiry (the previous 30-minute JWT
    #: had no refresh mechanism at all).
    browser_session_cookie_name: str = "eternal_world_session"
    browser_session_ttl_seconds: int = Field(default=60 * 60 * 24 * 14, gt=0)
    browser_session_cookie_secure: bool = Field(default=False)
    browser_session_cookie_domain: str | None = None

    #: Task 65.9 (Part Q) - async job backpressure. Shared/DB-backed (never
    #: an in-process counter), so it is correct across any number of API
    #: replicas. Deliberately generous defaults for a small/dev-scale
    #: deployment - operators must tune these for their own capacity, never
    #: interpreted as a proven concurrent-user capacity number.
    max_active_heavy_jobs_per_user: int = Field(default=10, gt=0)
    max_active_heavy_jobs_per_profile: int = Field(default=5, gt=0)
    global_heavy_job_saturation_limit: int = Field(default=1000, gt=0)
    global_saturation_retry_after_seconds: int = Field(default=30, gt=0)

    #: Task 65.9 (Part P) - a `running`/`recovery_pending` job whose
    #: heartbeat is older than this is considered stale (worker crashed)
    #: and becomes eligible for maintenance recovery.
    job_stale_heartbeat_timeout_seconds: int = Field(default=300, gt=0)

    #: Task 65.9 (Part E/G) - outbox dispatcher batch size per sweep.
    job_outbox_dispatch_batch_size: int = Field(default=50, gt=0)

    #: Task 65.9 (Part N) - real self-recycle (process exit, relying on the
    #: container's `restart: unless-stopped` policy) is gated behind this
    #: flag so it can only ever fire inside a container explicitly
    #: configured as the dedicated embedding worker - never inside
    #: FastAPI, the general Celery worker, or a test process.
    embedding_worker_self_recycle_enabled: bool = Field(default=False)

    #: Task 65.7C (Part E) - a Biographer candidate's oldest pending
    #: *required* clarification must be at least this old before
    #: `find_stuck_biographer_candidates`/repair will ever consider it
    #: "stuck". Without this floor, a candidate the owner is simply in the
    #: middle of answering right now (a normal, healthy, temporary state)
    #: would be indistinguishable from a genuinely abandoned one - the
    #: repair tool must never race a real user filling out the review form.
    biographer_stuck_clarification_min_age_hours: int = Field(default=24, gt=0)

    model_config = SettingsConfigDict(
        env_file=ENV_FILE_CANDIDATES,
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )

    @property
    def cors_origins(self) -> list[str]:
        normalized_value = self.backend_cors_origins.strip()

        if not normalized_value:
            return []

        if normalized_value.startswith("["):
            parsed_value = json.loads(normalized_value)
            if not isinstance(parsed_value, list):
                raise ValueError("BACKEND_CORS_ORIGINS JSON value must be a list")
            return [str(item).strip() for item in parsed_value if str(item).strip()]

        return [item.strip() for item in normalized_value.split(",") if item.strip()]

    @field_validator("ai_brain_provider")
    @classmethod
    def normalize_ai_brain_provider(cls, value: str) -> str:
        normalized_value = value.strip().lower()
        if not normalized_value:
            raise ValueError("AI_BRAIN_PROVIDER must not be empty")

        return normalized_value

    @field_validator("embedding_provider")
    @classmethod
    def normalize_embedding_provider(cls, value: str) -> str:
        normalized_value = value.strip().lower()
        if not normalized_value:
            raise ValueError("EMBEDDING_PROVIDER must not be empty")

        return normalized_value

    @field_validator("sentence_transformers_device")
    @classmethod
    def normalize_sentence_transformers_device(cls, value: str) -> str:
        normalized_value = value.strip().lower()
        return normalized_value or "cpu"

    @field_validator("embedding_cache_provider")
    @classmethod
    def normalize_embedding_cache_provider(cls, value: str) -> str:
        normalized_value = value.strip().lower()
        return normalized_value or "redis"

    @field_validator("embedding_cache_key_prefix")
    @classmethod
    def normalize_embedding_cache_key_prefix(cls, value: str) -> str:
        normalized_value = value.strip()
        return normalized_value or "eternal_world"

    @field_validator("ai_brain_model")
    @classmethod
    def normalize_ai_brain_model(cls, value: str) -> str:
        return value.strip()

    @field_validator("ai_brain_base_url")
    @classmethod
    def normalize_ai_brain_base_url(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            return "https://api.openai.com/v1"

        return normalized_value.rstrip("/")

    @field_validator("content_translation_provider")
    @classmethod
    def normalize_content_translation_provider(cls, value: str) -> str:
        normalized_value = value.strip().lower()
        if not normalized_value:
            raise ValueError("CONTENT_TRANSLATION_PROVIDER must not be empty")
        return normalized_value

    @field_validator("content_translation_model")
    @classmethod
    def normalize_content_translation_model(cls, value: str) -> str:
        return value.strip()

    @field_validator("content_translation_base_url")
    @classmethod
    def normalize_content_translation_base_url(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            return "https://api.openai.com/v1"
        return normalized_value.rstrip("/")

    @field_validator("media_storage_provider")
    @classmethod
    def normalize_media_storage_provider(cls, value: str) -> str:
        normalized_value = value.strip().lower()
        if not normalized_value:
            raise ValueError("MEDIA_STORAGE_PROVIDER must not be empty")

        return normalized_value

    @field_validator("media_public_base_url")
    @classmethod
    def normalize_media_public_base_url(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            return "/media"

        if not normalized_value.startswith("/"):
            normalized_value = f"/{normalized_value}"

        return normalized_value.rstrip("/") or "/media"

    @field_validator("qdrant_url")
    @classmethod
    def normalize_qdrant_url(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            return "http://qdrant:6333"

        return normalized_value.rstrip("/")

    @field_validator("qdrant_collection_name")
    @classmethod
    def normalize_qdrant_collection_name(cls, value: str) -> str:
        normalized_value = value.strip().lower()
        if not normalized_value:
            raise ValueError("QDRANT_COLLECTION_NAME must not be empty")

        return normalized_value

    @field_validator("celery_broker_url")
    @classmethod
    def normalize_celery_broker_url(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            return "redis://redis:6379/1"

        return normalized_value.rstrip("/")

    @field_validator("celery_result_backend")
    @classmethod
    def normalize_celery_result_backend(cls, value: str | None) -> str | None:
        if value is None:
            return None

        normalized_value = value.strip()
        return normalized_value.rstrip("/") or None


settings = Settings()
