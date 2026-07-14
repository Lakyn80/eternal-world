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
    backend_cors_origins: str = "http://localhost:8017"
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
