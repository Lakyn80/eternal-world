from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.cache.redis_client import get_redis_client
from app.core.config import settings
from app.db.session import engine


app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Eternal World API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/health/runtime")
def runtime_health():
    database_status = "ok"
    redis_status = "ok"

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except Exception as exc:
        database_status = f"error: {exc.__class__.__name__}"

    try:
        redis_client = get_redis_client()
        redis_client.ping()
    except Exception as exc:
        redis_status = f"error: {exc.__class__.__name__}"

    overall_status = "ok"

    if database_status != "ok" or redis_status != "ok":
        overall_status = "degraded"

    return {
        "status": overall_status,
        "database": database_status,
        "redis": redis_status,
    }
