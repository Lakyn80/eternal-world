from __future__ import annotations

import json
from pathlib import Path

from pydantic import SecretStr
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


settings = Settings()
