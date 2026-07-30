from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.cache.redis_client import get_redis_client
from app.core.config import settings
from app.core.errors import install_error_handlers
from app.core.logging import configure_logging
from app.core.middleware import install_middleware
from app.db.session import engine
from app.modules.embeddings.providers.bge_m3_hybrid import enable_bge_m3_hybrid_shared_model_cache
from app.modules.embeddings.router import router as embeddings_router
from app.modules.embedding_models.router import router as embedding_models_router
from app.modules.active_retrieval_config.router import router as active_retrieval_config_router
from app.modules.auth.router import router as auth_router
from app.modules.avatar_biographer.router import router as avatar_biographer_router
from app.modules.biography_ingestion.router import router as biography_ingestion_router
from app.modules.billing.router import router as billing_router
from app.modules.chat.router import router as chat_router
from app.modules.demo_fa_chat.router import router as demo_fa_chat_router
from app.modules.memories.router import router as memories_router
from app.modules.media.router import public_router as media_public_router
from app.modules.media.router import router as media_router
from app.modules.job_tracking.router import router as job_tracking_router
from app.modules.memorial_access.router import router as memorial_access_router
from app.modules.avatar_persona.router import router as avatar_persona_router
from app.modules.metrics.router import router as metrics_router
from app.modules.multi_embedding_eval.router import router as multi_embedding_eval_router
from app.modules.memory_profiles.router import router as memory_profiles_router
from app.modules.memorial_candidates.router import router as memorial_candidates_router
from app.modules.rag_retrieval.router import router as rag_retrieval_router
from app.modules.rag_chunks.router import router as rag_chunks_router
from app.modules.rag_sources.router import router as rag_sources_router
from app.modules.family_memory_enrichment.router import router as family_memory_enrichment_router
from app.modules.qdrant_indexing.router import router as qdrant_indexing_router
from app.modules.rag_pipeline.router import router as rag_pipeline_router


configure_logging()

#: Task 65.11: enable the process-wide BGE-M3 hybrid shared model cache
#: (`app/modules/embeddings/providers/bge_m3_hybrid.py`) for the lifetime
#: of this FastAPI/uvicorn process. Without this, every request that needs
#: a query embedding (chat RAG retrieval, AI biographer next-question,
#: etc.) constructed a brand-new ~2GB BGE-M3 model from disk from scratch
#: (`rag_retrieval/hybrid.py:default_encode_hybrid_query_vectors` and
#: `rag_retrieval/service.py` both call `build_embedding_provider`/
#: `BgeM3HybridEmbeddingProvider()` fresh per call, with no caching at that
#: layer) - multi-minute request latency, and concurrent overlapping loads
#: reliably reproduced `NotImplementedError: Cannot copy out of meta
#: tensor` failures from `transformers`/`accelerate`'s meta-device model
#: construction, which is not safe to run concurrently across threads in
#: one process. `_retrieve_rag_evidence_safely` in `chat/service.py`
#: swallows that exception and silently returns zero evidence, so the
#: avatar would claim "no memory" of things that were, in fact, correctly
#: indexed.
#:
#: This call is intentionally plain, synchronous, top-level module code -
#: NOT inside an `async def lifespan(...)` handler. `ContextVar` mutations
#: made inside one asyncio Task (e.g. the dedicated Task uvicorn/Starlette
#: runs the ASGI `lifespan` protocol in) do not propagate to *sibling*
#: Tasks created later by a different coroutine (e.g. the independent Task
#: uvicorn spawns per incoming connection) - each Task only inherits the
#: context that was ambient at its own `create_task()` call site, not
#: mutations made inside a sibling Task's own private context (verified
#: empirically in this repository's Task 65.11 investigation notes; this
#: is also documented Starlette/asyncio behavior). Executing this at true
#: module-import time, before uvicorn's event loop or any asyncio Task
#: exists, guarantees every later Task copies an ambient context in which
#: the flag is already `True`. The context manager is deliberately entered
#: and never exited - the shared cache must stay enabled for the entire
#: process lifetime, not just a scoped block.
#:
#: Never call `app.modules.embeddings.provider_lifecycle.get_or_initialize`
#: here or anywhere else in this module - see that module's docstring:
#: FastAPI's HTTP process must never use that heavier lifecycle/health-probe
#: singleton, only the lighter shared-model-cache mechanism used here.
#:
#: This context manager object MUST be kept alive in a module-level name
#: for the rest of the process's life. `enable_bge_m3_hybrid_shared_model_cache`
#: is implemented as a `@contextmanager`-wrapped generator: calling
#: `.set(True)` happens, then it suspends at `yield`. If the returned
#: `_GeneratorContextManager` is not referenced by anything, CPython's
#: refcounting GC finalizes it essentially immediately after this
#: statement runs, which calls `.close()` on the still-suspended
#: generator - triggering `GeneratorExit` at the `yield` point, which runs
#: the generator's `finally: _shared_model_cache_enabled.reset(token)`
#: block right away and silently undoes the `.set(True)` within the same
#: statement (confirmed empirically while building this fix - an earlier,
#: unreferenced `enable_bge_m3_hybrid_shared_model_cache().__enter__()`
#: one-liner here appeared to work but actually left the flag `False`).
_bge_m3_hybrid_shared_model_cache_context = enable_bge_m3_hybrid_shared_model_cache()
_bge_m3_hybrid_shared_model_cache_context.__enter__()

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
app.include_router(embeddings_router)
app.include_router(embedding_models_router)
app.include_router(active_retrieval_config_router)
app.include_router(auth_router)
app.include_router(billing_router)
app.include_router(chat_router)
app.include_router(demo_fa_chat_router)
app.include_router(job_tracking_router)
app.include_router(metrics_router)
app.include_router(multi_embedding_eval_router)
app.include_router(memories_router)
app.include_router(media_router)
app.include_router(media_public_router)
app.include_router(memorial_access_router)
app.include_router(avatar_persona_router)
app.include_router(memorial_candidates_router)
app.include_router(biography_ingestion_router)
app.include_router(avatar_biographer_router)
app.include_router(memory_profiles_router)
app.include_router(rag_retrieval_router)
app.include_router(qdrant_indexing_router)
app.include_router(rag_pipeline_router)
app.include_router(rag_chunks_router)
app.include_router(rag_sources_router)
app.include_router(family_memory_enrichment_router)


@app.get("/")
def root():
    return {"message": "Eternal World API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/health/runtime")
def runtime_health():
    """Task 65.9 (Part W): readiness only - never initializes the
    embedding provider (FastAPI must remain alive/ready even when BGE-M3
    has never been loaded anywhere). Outbox/job-queue visibility here is
    a cheap read of already-open connections, not a health dependency on
    the embedding worker itself - a degraded/offline embedding worker
    never makes this endpoint (or any other API endpoint) unavailable."""

    database_status = "ok"
    redis_status = "ok"
    qdrant_status = "ok"
    outbox_pending_backlog: int | None = None
    oldest_active_embedding_job_age_seconds: float | None = None

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except Exception as exc:
        database_status = f"error: {exc.__class__.__name__}"

    if database_status == "ok":
        # Best-effort only, and deliberately isolated from the basic
        # connectivity check above: these two extra readings use
        # PostgreSQL-specific SQL (`EXTRACT(EPOCH FROM ...)`) and must
        # never turn a healthy database connection into a reported
        # "error" just because a dialect-specific convenience query
        # (e.g. against the SQLite database used by the test suite)
        # doesn't apply.
        try:
            with engine.connect() as connection:
                outbox_row = connection.execute(
                    text("SELECT count(*) FROM job_outbox_events WHERE status = 'pending'")
                ).scalar()
                outbox_pending_backlog = int(outbox_row or 0)
        except Exception:
            outbox_pending_backlog = None

        try:
            with engine.connect() as connection:
                oldest_row = connection.execute(
                    text(
                        "SELECT EXTRACT(EPOCH FROM (now() - min(created_at))) FROM background_jobs "
                        "WHERE queue = 'embedding' AND status IN "
                        "('pending', 'queued', 'running', 'retry_scheduled', 'recovery_pending')"
                    )
                ).scalar()
                if oldest_row is not None:
                    oldest_active_embedding_job_age_seconds = round(float(oldest_row), 3)
        except Exception:
            oldest_active_embedding_job_age_seconds = None

    try:
        redis_client = get_redis_client()
        redis_client.ping()
    except Exception as exc:
        redis_status = f"error: {exc.__class__.__name__}"

    try:
        import httpx

        response = httpx.get(f"{settings.qdrant_url}/collections", timeout=2.0)
        if response.status_code >= 400:
            qdrant_status = f"error: http_{response.status_code}"
    except Exception as exc:
        qdrant_status = f"error: {exc.__class__.__name__}"

    overall_status = "ok"

    if database_status != "ok" or redis_status != "ok":
        overall_status = "degraded"

    return {
        "status": overall_status,
        "database": database_status,
        "redis": redis_status,
        "qdrant": qdrant_status,
        "outbox_pending_backlog": outbox_pending_backlog,
        "oldest_active_embedding_job_age_seconds": oldest_active_embedding_job_age_seconds,
    }
