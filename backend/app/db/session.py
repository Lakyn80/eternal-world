from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    echo=settings.sqlalchemy_echo,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,
)


#: Optional override used by TestClient (see ``tests/conftest.py``). Avoids
#: importing ``app.main`` from worker threads (deadlock risk under ASGI).
_session_factory_override: sessionmaker | None = None


def set_session_factory_override(factory: sessionmaker | None) -> None:
    global _session_factory_override
    _session_factory_override = factory


def get_session_factory() -> sessionmaker:
    """Return the active Session factory (test override or production)."""

    if _session_factory_override is not None:
        return _session_factory_override
    return SessionLocal


def get_db():
    db = get_session_factory()()
    try:
        yield db
    finally:
        db.close()
