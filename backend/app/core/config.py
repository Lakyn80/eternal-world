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
    media_storage_provider: str = "local"
    media_root: Path = BACKEND_DIR / "media"
    media_public_base_url: str = "/media"
    media_max_file_size_bytes: int = Field(default=20 * 1024 * 1024, gt=0)

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


settings = Settings()
