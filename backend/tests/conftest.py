import httpx
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.config import settings
from app.db.base import Base
from app.db.session import get_db
from app.main import app


#: Task 65.7 (Part L) - this dev container's real environment sets
#: AI_BRAIN_PROVIDER/CONTENT_TRANSLATION_PROVIDER=openai_compatible with a
#: real DeepSeek key for live smoke testing. `app.core.config.settings` is
#: a process-level singleton, so an un-guarded pytest run inherits that same
#: real configuration - discovered and fixed as an incident during Task
#: 65.6 (see PROJECT_PROGRESS.md). This global, autouse, session-wide guard
#: closes the gap for every test file, not just the one that happened to
#: add its own local fixture: any test that forgets to mock its provider
#: path will fail immediately and loudly (never silently place a real,
#: billed call) the moment anything tries to reach the real provider host.
_BLOCKED_PROVIDER_HOSTS = frozenset({"api.deepseek.com", "api.openai.com"})


@pytest.fixture(autouse=True)
def _force_mock_ai_providers(monkeypatch):
    monkeypatch.setattr(settings, "ai_brain_provider", "mock")
    monkeypatch.setattr(settings, "content_translation_provider", "mock")


@pytest.fixture(autouse=True)
def _guard_against_real_provider_calls(monkeypatch):
    """Defense in depth beyond `_force_mock_ai_providers`: a test that
    explicitly re-enables a real provider (to unit-test that provider
    class's own logic) is still expected to inject its own fake
    `http_client_factory` per this repo's established seam pattern - if
    anything ever actually tries to open a real `httpx.Client` request to
    a known paid-provider host, fail immediately with a clear error rather
    than silently placing a billed call. Purely a host-based safety net -
    every other httpx.Client target (the local ASGI test app, Qdrant/Redis
    testcontainers if any) is untouched."""

    real_send = httpx.Client.send

    def guarded_send(self, request, *args, **kwargs):
        if request.url.host in _BLOCKED_PROVIDER_HOSTS:
            raise AssertionError(
                f"Automated test attempted a real HTTP call to {request.url.host} - "
                "provider calls must be mocked/injected in tests, never real."
            )
        return real_send(self, request, *args, **kwargs)

    monkeypatch.setattr(httpx.Client, "send", guarded_send)


@pytest.fixture
def client():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    testing_session_local = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
        expire_on_commit=False,
    )

    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = testing_session_local()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    app.state.testing_session_local = testing_session_local

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    if hasattr(app.state, "testing_session_local"):
        delattr(app.state, "testing_session_local")
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
