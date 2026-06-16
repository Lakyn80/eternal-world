from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Eternal World API"
    environment: str = "local"
    database_url: str = "postgresql+psycopg://eternal_user:eternal_password@db:5432/eternal_world"
    redis_url: str = "redis://redis:6379/0"
    backend_cors_origins: str = "http://localhost:8017"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
