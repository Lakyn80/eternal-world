import httpx
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.config import settings
from app.db.base import Base
from app.db.session import get_db, set_session_factory_override
from app.main import app
from app.modules.embeddings.providers.bge_m3_hybrid import clear_bge_m3_hybrid_shared_model_cache


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
def _chat_admission_in_memory_redis(monkeypatch):
    """Task 65.13.11 — hermetic lease/rate store for every test process.

    Production uses Redis Lua scripts; tests inject InMemoryAdmissionRedis so
    chat paths stay deterministic without a live Redis dependency and without
    disabling admission (which would hide regressions).
    """

    from app.modules.chat import admission as chat_admission

    store = chat_admission.InMemoryAdmissionRedis()
    monkeypatch.setattr(chat_admission, "get_redis_client", lambda: store)


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
    real_async_send = httpx.AsyncClient.send

    def guarded_send(self, request, *args, **kwargs):
        if request.url.host in _BLOCKED_PROVIDER_HOSTS:
            raise AssertionError(
                f"Automated test attempted a real HTTP call to {request.url.host} - "
                "provider calls must be mocked/injected in tests, never real."
            )
        return real_send(self, request, *args, **kwargs)

    async def guarded_async_send(self, request, *args, **kwargs):
        if request.url.host in _BLOCKED_PROVIDER_HOSTS:
            raise AssertionError(
                f"Automated test attempted a real async HTTP call to {request.url.host} - "
                "provider calls must be mocked/injected in tests, never real."
            )
        return await real_async_send(self, request, *args, **kwargs)

    monkeypatch.setattr(httpx.Client, "send", guarded_send)
    monkeypatch.setattr(httpx.AsyncClient, "send", guarded_async_send)


@pytest.fixture(autouse=True)
def _reset_bge_m3_hybrid_shared_model_cache():
    """Task 65.11: importing `app.main` above (required for the `client`
    fixture and for every test module that imports FastAPI dependencies
    from it) now enables the process-wide BGE-M3 hybrid shared model cache
    ContextVar as a deliberate side effect of module import - it must stay
    on for real request-serving processes. Left unguarded, that would leak
    a shared `_shared_models`/`_shared_model_encode_locks` state across
    every test in this process: a test's `monkeypatch.setattr` on
    `_import_bge_m3_flag_model_class`/`resolve_bge_m3_model_load_path`
    would be silently skipped whenever an earlier test already populated
    the shared cache for the same cache key. Clearing the shared dicts
    (not the ContextVar itself, which stays True - that mirrors production)
    before and after every test restores full per-test isolation: each
    test that constructs a `BgeM3HybridEmbeddingProvider` still gets a
    guaranteed cache miss on its first `_get_or_load_model()` call, so its
    own monkeypatches are always honored."""

    clear_bge_m3_hybrid_shared_model_cache()
    yield
    clear_bge_m3_hybrid_shared_model_cache()


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
    set_session_factory_override(testing_session_local)

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    set_session_factory_override(None)
    if hasattr(app.state, "testing_session_local"):
        delattr(app.state, "testing_session_local")
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
