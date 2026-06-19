from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.cache.redis_client import get_redis_client
from app.core.config import settings
from app.core.errors import install_error_handlers
from app.core.logging import configure_logging
from app.core.middleware import install_middleware
from app.db.session import engine
from app.modules.auth.router import router as auth_router
from app.modules.billing.router import router as billing_router
from app.modules.chat.router import router as chat_router
from app.modules.memories.router import router as memories_router
from app.modules.media.router import public_router as media_public_router
from app.modules.media.router import router as media_router
from app.modules.memory_profiles.router import router as memory_profiles_router


configure_logging()
app = FastAPI(title=settings.app_name)
install_error_handlers(app)
install_middleware(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(billing_router)
app.include_router(chat_router)
app.include_router(memories_router)
app.include_router(media_router)
app.include_router(media_public_router)
app.include_router(memory_profiles_router)


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
