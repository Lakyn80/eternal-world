"""Task 65.11: BGE-M3 hybrid embedding provider per-request reload fix.

Regression coverage for the fix to a live incident: every request that
needed a query embedding (chat RAG retrieval, AI biographer next-question)
constructed a brand-new ~2GB BGE-M3 model from disk from scratch, because
`build_embedding_provider`/`BgeM3HybridEmbeddingProvider()` were called
fresh per request with the process-wide shared model cache
(`enable_bge_m3_hybrid_shared_model_cache`) never entered anywhere in the
FastAPI request-serving path. Under concurrent load this reliably produced
`NotImplementedError: Cannot copy out of meta tensor` failures (concurrent
`transformers`/`accelerate` meta-device model construction is not
thread-safe), which `chat/service.py::_retrieve_rag_evidence_safely`
silently swallowed - the avatar would then claim "no memory" of things
that were, in fact, correctly indexed.

These tests use the exact fake-model mocking pattern already proven in
`tests/test_real_question_eval.py` (`_install_fake_bge_m3_hybrid_model`,
`_FakeBGEM3FlagModel`) rather than inventing a new strategy, and never
load the real ~2GB model.
"""

from __future__ import annotations

import contextvars
import threading
import time

import pytest

from app.core.config import settings
from app.modules.embedding_models.registry import BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE
from app.modules.embeddings.embedding_cache import (
    NullEmbeddingCache,
    build_cache_key,
    build_cached_embedding_payload,
)
from app.modules.embeddings.providers import build_embedding_provider
from app.modules.embeddings.providers.bge_m3_hybrid import (
    BgeM3HybridEmbeddingAdapter,
    BgeM3HybridEmbeddingProvider,
    _shared_model_cache_enabled,
    clear_bge_m3_hybrid_shared_model_cache,
)


#: Task 65.11.3A: message raised by the hard Redis-access guard below.
REDIS_ACCESS_FORBIDDEN_MESSAGE = "Shared-model lifecycle tests must never access Redis"


class _EmbeddingCacheIsolationGuard:
    """Records what the hermetic-cache fixture observed, so individual
    tests can assert *positively* that no live Redis seam was ever
    touched (rather than only implicitly relying on it)."""

    def __init__(self) -> None:
        self.injected_caches: list[object] = []
        self.redis_access_attempts: list[str] = []

    @property
    def redis_was_never_accessed(self) -> bool:
        return not self.redis_access_attempts

    def assert_only_null_caches_were_injected(self, *, minimum_expected: int = 1) -> None:
        assert len(self.injected_caches) >= minimum_expected, (
            "expected at least "
            f"{minimum_expected} provider cache construction(s), got {len(self.injected_caches)}"
        )
        assert all(isinstance(cache, NullEmbeddingCache) for cache in self.injected_caches), (
            "every BGE-M3 provider built by these tests must receive a NullEmbeddingCache"
        )
        assert self.redis_was_never_accessed, (
            f"{REDIS_ACCESS_FORBIDDEN_MESSAGE} (attempts: {self.redis_access_attempts})"
        )


@pytest.fixture(autouse=True)
def embedding_cache_guard(monkeypatch) -> _EmbeddingCacheIsolationGuard:
    """Task 65.11.3A - make this whole file hermetic with respect to the
    embedding cache.

    These tests are about *shared model lifecycle*: model reuse across
    separately constructed adapters, the per-shared-model encode lock, and
    serialization of concurrent `.encode()` calls. They are **not**
    cache-integration tests - that contract lives in
    `tests/test_task_65_11_1_embedding_cache_activation.py`.

    They were written during Task 65.11, when `embedding_cache_enabled`
    was `False` in every runtime, so they never neutralized the cache.
    Once Task 65.11.1 genuinely activated the Redis embedding cache
    (`embedding_cache_enabled=True`, `embedding_cache_provider=redis`),
    `BgeM3HybridEmbeddingProvider.__init__` started building a *real*
    Redis-backed cache, live Redis already held entries for these tests'
    literal query strings (written by their own earlier runs), and the
    provider satisfied every `embed_query()` from Redis **without ever
    calling the fake model**. The encode-count assertions (`== 2`, `== 8`)
    then measured Redis contents instead of the behavior under test, and
    every miss wrote a fake `[1.0] * 1024` / `{"stub": 1.0}` vector into
    the production-identical `eternal_world:embedding_cache:*` namespace.

    The fix closes the actual construction seam: `bge_m3_hybrid.py` calls
    `build_embedding_cache()` imported into *its own* module namespace, so
    that is the name that must be patched - patching
    `settings.embedding_cache_enabled` alone would be an indirect,
    easily-bypassed proxy for the same thing. On top of that, every real
    Redis entry point is replaced with a hard failure, so any future edit
    that reintroduces a live-Redis dependency in this file fails loudly
    and immediately instead of silently becoming environment-dependent
    again."""

    guard = _EmbeddingCacheIsolationGuard()

    def _null_embedding_cache_factory(**_kwargs) -> NullEmbeddingCache:
        cache = NullEmbeddingCache()
        guard.injected_caches.append(cache)
        return cache

    # The construction seam the provider actually uses (module-level
    # `from ... import build_embedding_cache` in bge_m3_hybrid.py).
    monkeypatch.setattr(
        "app.modules.embeddings.providers.bge_m3_hybrid.build_embedding_cache",
        _null_embedding_cache_factory,
    )

    def _forbid_redis(seam: str):
        def _raise(*_args, **_kwargs):
            guard.redis_access_attempts.append(seam)
            raise AssertionError(REDIS_ACCESS_FORBIDDEN_MESSAGE)

        return _raise

    # Belt and suspenders: even if some other code path reached the real
    # `build_embedding_cache()`, neither the Redis client factory nor the
    # Redis-backed cache class can be constructed from this test file.
    monkeypatch.setattr(
        "app.cache.redis_client.get_redis_client",
        _forbid_redis("app.cache.redis_client.get_redis_client"),
    )
    monkeypatch.setattr(
        "app.cache.redis_client.Redis.from_url",
        _forbid_redis("redis.Redis.from_url"),
    )
    monkeypatch.setattr(
        "app.modules.embeddings.embedding_cache.RedisEmbeddingCache",
        _forbid_redis("RedisEmbeddingCache"),
    )

    yield guard

    assert guard.redis_was_never_accessed, (
        f"{REDIS_ACCESS_FORBIDDEN_MESSAGE} (attempts: {guard.redis_access_attempts})"
    )
    assert all(isinstance(cache, NullEmbeddingCache) for cache in guard.injected_caches), (
        "every BGE-M3 provider built by these tests must receive a NullEmbeddingCache"
    )


class _FakeBGEM3FlagModel:
    """Mirrors `tests/test_real_question_eval.py`'s
    `_FakeBGEM3FlagModel`/`tests/test_bge_m3_embedding_cache.py`'s fake
    class: tracks constructor calls (proves whether the ~2GB model would
    have been reloaded) and encode calls, and can simulate the time window
    during which a real model load/encode is in flight so concurrency
    tests can reliably force overlap."""

    init_calls: list[dict[str, object]] = []
    encode_calls: list[dict[str, object]] = []
    max_concurrent_encode_calls = 0
    _active_encode_calls = 0
    _active_lock = threading.Lock()
    init_delay_seconds = 0.0
    encode_delay_seconds = 0.0

    def __init__(self, model_name: str, **kwargs) -> None:
        if self.init_delay_seconds:
            time.sleep(self.init_delay_seconds)
        self.model_name = model_name
        self.kwargs = dict(kwargs)
        self.__class__.init_calls.append({"model_name": model_name, "kwargs": dict(kwargs)})

    def encode(
        self,
        texts,
        *,
        batch_size: int,
        max_length: int,
        return_dense: bool,
        return_sparse: bool,
        return_colbert_vecs: bool,
    ):
        cls = self.__class__
        with cls._active_lock:
            cls._active_encode_calls += 1
            cls.max_concurrent_encode_calls = max(
                cls.max_concurrent_encode_calls, cls._active_encode_calls
            )
        try:
            if cls.encode_delay_seconds:
                time.sleep(cls.encode_delay_seconds)
            materialized_texts = list(texts)
            cls.encode_calls.append(
                {
                    "texts": materialized_texts,
                    "batch_size": batch_size,
                    "return_colbert_vecs": return_colbert_vecs,
                }
            )
            # Matches the real `bge_m3_dense_sparse` registry dimension
            # (1024) so tests can go through `BgeM3HybridEmbeddingAdapter`
            # (which validates dense vector length against the registry),
            # not just the lower-level `BgeM3HybridEmbeddingProvider`.
            dense_vecs = [[1.0] * 1024 for _ in materialized_texts]
            lexical_weights = [{"stub": 1.0} for _ in materialized_texts]
            return {"dense_vecs": dense_vecs, "lexical_weights": lexical_weights}
        finally:
            with cls._active_lock:
                cls._active_encode_calls -= 1


def _start_thread_with_copied_context(target, *args) -> threading.Thread:
    """Plain `threading.Thread(target=...)` does NOT inherit the calling
    thread's `contextvars.Context` (unlike `asyncio.Task`, which copies it
    automatically) - each new OS thread otherwise starts with a fresh,
    empty context, where `_shared_model_cache_enabled` would read back its
    class default of `False` regardless of what the main thread set.
    Starlette's `run_in_threadpool` (used to run sync path operations /
    dependencies, which is how a real request ends up calling into this
    provider) uses `anyio.to_thread.run_sync`, which explicitly captures
    `contextvars.copy_context()` from the calling async task and runs the
    worker-thread function inside that copied context - this helper
    reproduces that exact context-propagation behavior for the thread
    concurrency tests below, so they faithfully simulate concurrent real
    requests rather than independent, context-less threads."""

    ctx = contextvars.copy_context()
    thread = threading.Thread(target=lambda: ctx.run(target, *args))
    thread.start()
    return thread


def _install_fake_bge_m3_hybrid_model(monkeypatch, *, init_delay: float = 0.0, encode_delay: float = 0.0) -> None:
    clear_bge_m3_hybrid_shared_model_cache()
    _FakeBGEM3FlagModel.init_calls = []
    _FakeBGEM3FlagModel.encode_calls = []
    _FakeBGEM3FlagModel.max_concurrent_encode_calls = 0
    _FakeBGEM3FlagModel._active_encode_calls = 0
    _FakeBGEM3FlagModel.init_delay_seconds = init_delay
    _FakeBGEM3FlagModel.encode_delay_seconds = encode_delay
    monkeypatch.setattr(
        "app.modules.embeddings.providers.bge_m3_hybrid._import_bge_m3_flag_model_class",
        lambda: _FakeBGEM3FlagModel,
    )
    monkeypatch.setattr(
        "app.modules.embeddings.providers.bge_m3_hybrid.resolve_bge_m3_model_load_path",
        lambda repo_id, **kwargs: (repo_id, False),
    )
    monkeypatch.setattr(
        "app.modules.embeddings.providers.bge_m3_hybrid.resolve_local_snapshot_path",
        lambda repo_id, **kwargs: f"/cache/{repo_id}/5617a9f61b028005a4858fdac845db406aefb181",
    )


def test_importing_app_main_enables_the_shared_model_cache_process_wide():
    """The fix is wired in `app/main.py` as plain top-level module code
    (not inside `async def lifespan`) specifically so the ContextVar is
    already `True` in the ambient context before uvicorn's event loop - and
    therefore every per-request asyncio Task it later spawns - exists.
    `tests/conftest.py` already imports `app.main` (required for the
    `client` fixture), so by the time any test runs, this must already be
    enabled."""

    import app.main  # noqa: F401  (import side effect under test)

    assert _shared_model_cache_enabled.get() is True


def test_build_embedding_provider_reuses_shared_model_across_separate_adapter_instances(monkeypatch):
    """Simulates the real bug: two separate per-request calls into
    `build_embedding_provider` (the exact factory used by
    `rag_retrieval/service.py::_build_provider`), each constructing its own
    fresh `BgeM3HybridEmbeddingAdapter`. Before the fix, this reloaded the
    ~2GB model from scratch on every call. With the shared cache enabled
    (as it now always is once `app.main` has been imported), the second
    adapter must reuse the exact same underlying model object, and the
    fake model loader must only ever be invoked once."""

    _install_fake_bge_m3_hybrid_model(monkeypatch)
    original_embedding_provider = settings.embedding_provider
    settings.embedding_provider = "sentence_transformers"
    try:
        assert _shared_model_cache_enabled.get() is True

        first_adapter = build_embedding_provider(model_code=BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)
        second_adapter = build_embedding_provider(model_code=BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)

        assert isinstance(first_adapter, BgeM3HybridEmbeddingAdapter)
        assert isinstance(second_adapter, BgeM3HybridEmbeddingAdapter)
        assert first_adapter is not second_adapter  # genuinely separate per-call instances
        # Task 65.11.3A: both providers must be cache-free, so the encode
        # counts below measure the model, never live Redis contents.
        assert isinstance(first_adapter._hybrid_provider._embedding_cache, NullEmbeddingCache)
        assert isinstance(second_adapter._hybrid_provider._embedding_cache, NullEmbeddingCache)

        first_adapter.embed_query("first request query", BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)
        second_adapter.embed_query("second request query", BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)

        assert len(_FakeBGEM3FlagModel.init_calls) == 1
        assert len(_FakeBGEM3FlagModel.encode_calls) == 2

        first_model = first_adapter._hybrid_provider._models[BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE]
        second_model = second_adapter._hybrid_provider._models[BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE]
        assert first_model is second_model
    finally:
        settings.embedding_provider = original_embedding_provider
        clear_bge_m3_hybrid_shared_model_cache()


def test_concurrent_requests_load_the_shared_model_exactly_once(monkeypatch):
    """Reproduces the concurrency conditions behind the real
    `NotImplementedError: Cannot copy out of meta tensor` failures observed
    in production: many "requests" racing to obtain the model at once. The
    fake model's constructor sleeps briefly to widen the race window (the
    real `flag_model_class(...)` call takes long enough in production for
    concurrent requests to overlap). Regardless of how many threads race,
    the existing double-checked-locking in `_get_or_load_model` (guarded by
    the module-level `_shared_models_lock`) must ensure the underlying
    loader is invoked exactly once."""

    _install_fake_bge_m3_hybrid_model(monkeypatch, init_delay=0.05)
    original_embedding_provider = settings.embedding_provider
    settings.embedding_provider = "sentence_transformers"
    try:
        assert _shared_model_cache_enabled.get() is True

        results: list[object] = [None] * 12
        errors: list[BaseException] = []

        def _simulate_one_request(index: int) -> None:
            try:
                adapter = build_embedding_provider(model_code=BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)
                adapter.embed_query(f"concurrent query {index}", BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)
                results[index] = adapter._hybrid_provider._models[BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE]
            except BaseException as exc:  # noqa: BLE001 - surfaced via `errors` for the assertion below
                errors.append(exc)

        threads = [_start_thread_with_copied_context(_simulate_one_request, i) for i in range(12)]
        for thread in threads:
            thread.join(timeout=10)

        assert not errors, f"concurrent requests raised: {errors}"
        assert len(_FakeBGEM3FlagModel.init_calls) == 1
        assert all(result is results[0] for result in results)
    finally:
        settings.embedding_provider = original_embedding_provider
        clear_bge_m3_hybrid_shared_model_cache()


def test_concurrent_encode_calls_on_a_shared_model_are_serialized(monkeypatch):
    """`FlagEmbedding`'s `AbsEmbedder.encode_single_device()` calls
    `self.model.to(device)` / `self.model.float()` on *every* `.encode()`
    call, not just once at load time (verified by reading the installed
    package source) - a real, mutating operation on the shared
    `nn.Module`'s parameter tree. Once a model instance is shared across
    concurrent requests, two overlapping `.encode()` calls on it are not
    provably safe. This proves the per-shared-model encode lock added
    alongside the caching fix actually serializes concurrent `.encode()`
    invocations: with several threads calling `encode()` concurrently on
    the same shared model and each call sleeping briefly, at most one
    encode call must ever be in flight at a time."""

    _install_fake_bge_m3_hybrid_model(monkeypatch, encode_delay=0.05)
    original_embedding_provider = settings.embedding_provider
    settings.embedding_provider = "sentence_transformers"
    try:
        # Prime the shared cache once, sequentially, so every thread below
        # is guaranteed to hit the "already loaded" branch and go straight
        # to a genuinely concurrent encode() call.
        priming_adapter = build_embedding_provider(model_code=BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)
        # Task 65.11.3A: a cache hit here would skip the fake model
        # entirely and silently invalidate the encode-count assertions.
        assert isinstance(priming_adapter._hybrid_provider._embedding_cache, NullEmbeddingCache)
        priming_adapter.embed_query("priming query", BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)
        assert len(_FakeBGEM3FlagModel.init_calls) == 1
        _FakeBGEM3FlagModel.encode_calls = []
        _FakeBGEM3FlagModel.max_concurrent_encode_calls = 0

        errors: list[BaseException] = []

        def _simulate_one_request(index: int) -> None:
            try:
                adapter = build_embedding_provider(model_code=BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)
                adapter.embed_query(f"concurrent encode query {index}", BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)
            except BaseException as exc:  # noqa: BLE001
                errors.append(exc)

        threads = [_start_thread_with_copied_context(_simulate_one_request, i) for i in range(8)]
        for thread in threads:
            thread.join(timeout=10)

        assert not errors, f"concurrent encode calls raised: {errors}"
        assert len(_FakeBGEM3FlagModel.init_calls) == 1  # still exactly one load
        assert len(_FakeBGEM3FlagModel.encode_calls) == 8  # every request's encode still ran
        assert _FakeBGEM3FlagModel.max_concurrent_encode_calls == 1
    finally:
        settings.embedding_provider = original_embedding_provider
        clear_bge_m3_hybrid_shared_model_cache()


def test_unshared_provider_instance_never_takes_an_encode_lock(monkeypatch):
    """When the shared cache is disabled (the ContextVar is False), each
    `BgeM3HybridEmbeddingProvider` instance owns a private model that
    nothing else touches concurrently - no encode lock should be attached,
    confirming the guard is scoped precisely to shared instances rather
    than blanket-applied everywhere."""

    _install_fake_bge_m3_hybrid_model(monkeypatch)
    token = _shared_model_cache_enabled.set(False)
    try:
        provider = BgeM3HybridEmbeddingProvider()
        provider.encode_query("unshared query", BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)
        assert provider._model_encode_locks[BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE] is None
    finally:
        _shared_model_cache_enabled.reset(token)
        clear_bge_m3_hybrid_shared_model_cache()


def test_shared_model_tests_never_depend_on_or_mutate_the_live_embedding_cache(
    monkeypatch,
    embedding_cache_guard,
):
    """Task 65.11.3A regression coverage for the isolation itself.

    Proves, without contacting Redis (which the guard forbids outright),
    that: the runtime configuration this deployment actually runs with
    (`embedding_cache_enabled=True`, `embedding_cache_provider="redis"`)
    cannot re-enable a live cache for this file; every provider built here
    receives a `NullEmbeddingCache`; no Redis client factory is ever
    invoked; a repeated identical round produces identical fake-model
    encode counts (against a live cache the second round would be a
    guaranteed hit, i.e. 0 encode calls); pre-existing cache contents can
    never be read back; and nothing this file does can create an
    `eternal_world:embedding_cache:*` entry or refresh an existing TTL."""

    # (1) The live runtime values, asserted explicitly rather than
    # inherited from the ambient environment, so this holds in every
    # deployment - including the one where the cache is genuinely on.
    monkeypatch.setattr(settings, "embedding_cache_enabled", True)
    monkeypatch.setattr(settings, "embedding_cache_provider", "redis")
    assert settings.embedding_cache_enabled is True
    assert settings.embedding_cache_provider == "redis"

    _install_fake_bge_m3_hybrid_model(monkeypatch)
    original_embedding_provider = settings.embedding_provider
    settings.embedding_provider = "sentence_transformers"
    try:
        def _run_one_round() -> int:
            adapter = build_embedding_provider(model_code=BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)
            # (2) the provider instance received the null cache.
            assert isinstance(adapter._hybrid_provider._embedding_cache, NullEmbeddingCache)
            adapter.embed_query("isolation probe query", BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)
            return len(_FakeBGEM3FlagModel.encode_calls)

        first_round_encode_calls = _run_one_round()
        _FakeBGEM3FlagModel.encode_calls = []
        second_round_encode_calls = _run_one_round()

        # (4)+(5) identical counts across repeated rounds with the exact
        # same query text: a live cache would have served round two.
        assert first_round_encode_calls == 1
        assert second_round_encode_calls == 1

        # (3) no Redis client factory and no Redis-backed cache class was
        # constructed at any point.
        assert embedding_cache_guard.redis_access_attempts == []
        embedding_cache_guard.assert_only_null_caches_were_injected(minimum_expected=2)

        probe_adapter = build_embedding_provider(model_code=BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)
        probe_provider = probe_adapter._hybrid_provider
        injected_cache = probe_provider._embedding_cache
        assert type(injected_cache) is NullEmbeddingCache

        cache_context = probe_provider._get_cache_context(BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE)
        cache_key = build_cache_key(
            key_prefix=settings.embedding_cache_key_prefix,
            provider_code=cache_context.provider_code,
            provider_model_name=cache_context.provider_model_name,
            snapshot_revision=cache_context.snapshot_revision,
            mode=cache_context.mode,
            input_type="query",
            dimension=cache_context.dimension,
            text="isolation probe query",
        )
        assert cache_key.startswith(f"{settings.embedding_cache_key_prefix}:embedding_cache:v1:")

        # (5) whatever the live namespace already holds for this key is
        # unreadable from here - the injected cache always misses.
        assert injected_cache.get(cache_key) is None

        # (6)+(7) a write attempt neither creates an entry nor refreshes
        # any TTL: the null cache stores nothing and there is no Redis
        # client behind it to reach.
        payload = build_cached_embedding_payload(
            provider_code=cache_context.provider_code,
            provider_model_name=cache_context.provider_model_name,
            snapshot_revision=cache_context.snapshot_revision,
            mode=cache_context.mode,
            input_type="query",
            dimension=cache_context.dimension,
            dense_vector=[1.0] * cache_context.dimension,
            sparse_vector={"stub": 1.0},
            text="isolation probe query",
        )
        assert injected_cache.set(cache_key, payload, settings.embedding_cache_ttl_seconds) is None
        assert injected_cache.get(cache_key) is None
        assert embedding_cache_guard.redis_was_never_accessed
    finally:
        settings.embedding_provider = original_embedding_provider
        clear_bge_m3_hybrid_shared_model_cache()


def test_any_attempt_to_reach_real_redis_from_this_file_fails_immediately(embedding_cache_guard):
    """Proves the Redis-access guard is live rather than vacuous: the real
    client factory raises the moment it is touched, so a future edit that
    reintroduces a live-Redis dependency in this file cannot silently make
    these shared-model tests environment-dependent again."""

    from app.cache.redis_client import get_redis_client

    with pytest.raises(AssertionError, match=REDIS_ACCESS_FORBIDDEN_MESSAGE):
        get_redis_client()

    assert embedding_cache_guard.redis_access_attempts == [
        "app.cache.redis_client.get_redis_client"
    ]
    # Deliberate probe - clear it so the fixture's teardown assertion (the
    # real safety net for every other test in this file) stays meaningful.
    embedding_cache_guard.redis_access_attempts.clear()
