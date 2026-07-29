"""Task 65.11.1 - Redis embedding cache activation.

The fan-out fix and the Redis cache are BOTH required and neither replaces
the other: batching fixes the cold request (one model invocation instead of
16), the Redis cache fixes the repeated request (zero model invocations for
already-seen query texts).

Fake-safe by construction: a `FakeBgeM3Model` counts `.encode()` calls and a
`FakeRedis` dict-backed client records every `set(..., ex=...)`. Nothing here
loads real BGE-M3 weights, connects to the live Redis server, or writes to
live Qdrant/PostgreSQL.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from app.core.config import settings
from app.modules.embeddings import embedding_cache as embedding_cache_module
from app.modules.embeddings.embedding_cache import (
    NullEmbeddingCache,
    RedisEmbeddingCache,
    build_cache_key,
    build_embedding_cache,
)
from app.modules.embeddings.providers import bge_m3_hybrid as bge_m3_hybrid_module
from app.modules.embeddings.providers.bge_m3_hybrid import BgeM3HybridEmbeddingProvider


PROVIDER_CODE = "bge_m3_dense_sparse"
EXPECTED_TTL_SECONDS = 604800

#: The backend container mounts only `./backend` at `/app`, so the repo-root
#: compose files are not readable from inside it. The compose assertions
#: below therefore resolve the repo root defensively and skip (never silently
#: pass) when it is not reachable - they are meant to be run from the host
#: checkout, e.g. `python -m pytest backend/tests/test_task_65_11_1_embedding_cache_activation.py`.
_COMPOSE_ROOT_CANDIDATES = (
    Path(__file__).resolve().parents[2],
    Path(__file__).resolve().parents[1],
    Path("/repo"),
)


def _resolve_compose_path(compose_file: str) -> Path:
    for root in _COMPOSE_ROOT_CANDIDATES:
        candidate = root / compose_file
        if candidate.is_file():
            return candidate
    pytest.skip(
        f"{compose_file} is not reachable from this process "
        "(the backend container mounts only ./backend); run this test from the host checkout"
    )

TOPIC_QUERY_TEXTS = [
    "Kde jste prožil/a dětství a na co si z té doby nejvíc vzpomínáte?",
    "Povězte mi něco o vaší rodině - kdo ve vašem životě hrál nejdůležitější roli?",
    "Jaké bylo vaše vzdělání a je na něj nějaká vzpomínka, která vám utkvěla?",
    "Čím jste se v životě živil/a a co vás na té práci nejvíc bavilo?",
    "Kdo byli lidé, na kterých vám v životě nejvíc záleželo?",
    "Je nějaké místo, které pro vás bylo obzvlášť důležité?",
    "Měla vaše rodina nějaké tradice nebo zvyky, na které rádi vzpomínáte?",
    "Co je pro vás v životě nejdůležitější a co byste chtěl/a předat dalším generacím?",
]


class FakeBgeM3Model:
    """Stands in for the real 2GB `BGEM3FlagModel` - counts invocations."""

    def __init__(self) -> None:
        self.encode_calls = 0
        self.encoded_batches: list[list[str]] = []

    def encode(self, texts, batch_size=None, max_length=None, return_dense=True, return_sparse=True, return_colbert_vecs=False):
        self.encode_calls += 1
        self.encoded_batches.append(list(texts))
        return {
            "dense_vecs": [[0.01 * (index + 1)] * 1024 for index in range(len(texts))],
            "lexical_weights": [{"tok": 1.0 + index} for index in range(len(texts))],
        }


class FakeRedis:
    def __init__(self, *, fail: bool = False) -> None:
        self.store: dict[str, str] = {}
        self.set_calls: list[tuple[str, int | None]] = []
        self.get_calls: list[str] = []
        self.fail = fail

    def get(self, key: str):
        self.get_calls.append(key)
        if self.fail:
            raise RuntimeError("redis unavailable")
        return self.store.get(key)

    def set(self, key: str, value: str, ex: int | None = None):
        self.set_calls.append((key, ex))
        if self.fail:
            raise RuntimeError("redis unavailable")
        self.store[key] = value


def _build_provider(monkeypatch, *, redis_client=None, snapshot_revision: str = "rev-a"):
    """Provider with a fake model and a fully controlled embedding cache."""

    model = FakeBgeM3Model()
    monkeypatch.setattr(
        bge_m3_hybrid_module,
        "resolve_local_snapshot_path",
        lambda name, cache_dir=None: f"/models/snapshots/{snapshot_revision}",
    )

    provider = BgeM3HybridEmbeddingProvider(device="cpu", cache_dir=None)
    provider._models[PROVIDER_CODE] = model
    provider._model_encode_locks[PROVIDER_CODE] = None
    if redis_client is not None:
        provider._embedding_cache = RedisEmbeddingCache(redis_client)
    else:
        provider._embedding_cache = NullEmbeddingCache()
    return provider, model


# --- 1/2/3/4: miss, write, hit, partial hit -------------------------------


def test_cache_disabled_performs_one_batch_model_call(monkeypatch):
    monkeypatch.setattr(settings, "embedding_cache_enabled", False)
    provider, model = _build_provider(monkeypatch)

    encoded = provider.encode_queries(TOPIC_QUERY_TEXTS, PROVIDER_CODE)

    assert model.encode_calls == 1
    assert model.encoded_batches == [TOPIC_QUERY_TEXTS]
    assert len(encoded.dense_vectors) == 8
    assert provider.last_cache_summary.cache_enabled is False


def test_cold_request_misses_eight_encodes_once_and_writes_eight(monkeypatch):
    monkeypatch.setattr(settings, "embedding_cache_enabled", True)
    monkeypatch.setattr(settings, "embedding_cache_ttl_seconds", EXPECTED_TTL_SECONDS)
    redis_client = FakeRedis()
    provider, model = _build_provider(monkeypatch, redis_client=redis_client)

    provider.encode_queries(TOPIC_QUERY_TEXTS, PROVIDER_CODE)

    summary = provider.last_cache_summary
    assert summary.hits == 0
    assert summary.misses == 8
    assert summary.writes == 8
    assert model.encode_calls == 1
    assert model.encoded_batches == [TOPIC_QUERY_TEXTS]
    assert len(redis_client.set_calls) == 8


def test_warm_repeated_request_hits_eight_and_performs_zero_model_calls(monkeypatch):
    monkeypatch.setattr(settings, "embedding_cache_enabled", True)
    monkeypatch.setattr(settings, "embedding_cache_ttl_seconds", EXPECTED_TTL_SECONDS)
    redis_client = FakeRedis()

    cold_provider, cold_model = _build_provider(monkeypatch, redis_client=redis_client)
    cold = cold_provider.encode_queries(TOPIC_QUERY_TEXTS, PROVIDER_CODE)
    assert cold_model.encode_calls == 1

    warm_provider, warm_model = _build_provider(monkeypatch, redis_client=redis_client)
    warm = warm_provider.encode_queries(TOPIC_QUERY_TEXTS, PROVIDER_CODE)

    assert warm_model.encode_calls == 0
    summary = warm_provider.last_cache_summary
    assert summary.hits == 8
    assert summary.misses == 0
    # Same vectors, same topic->vector mapping.
    assert warm.dense_vectors == cold.dense_vectors
    assert warm.sparse_vectors == cold.sparse_vectors


def test_partial_cache_hit_encodes_only_the_misses_in_one_batch(monkeypatch):
    monkeypatch.setattr(settings, "embedding_cache_enabled", True)
    monkeypatch.setattr(settings, "embedding_cache_ttl_seconds", EXPECTED_TTL_SECONDS)
    redis_client = FakeRedis()

    warm_provider, _warm_model = _build_provider(monkeypatch, redis_client=redis_client)
    warm_provider.encode_queries(TOPIC_QUERY_TEXTS[:5], PROVIDER_CODE)

    provider, model = _build_provider(monkeypatch, redis_client=redis_client)
    provider.encode_queries(TOPIC_QUERY_TEXTS, PROVIDER_CODE)

    summary = provider.last_cache_summary
    assert summary.hits == 5
    assert summary.misses == 3
    # One model call regardless of miss count; only the misses are encoded.
    assert model.encode_calls == 1
    assert model.encoded_batches == [TOPIC_QUERY_TEXTS[5:]]


# --- 5/6: query/passage and model-revision isolation ----------------------


def test_cached_passage_embedding_never_satisfies_a_query_request(monkeypatch):
    monkeypatch.setattr(settings, "embedding_cache_enabled", True)
    monkeypatch.setattr(settings, "embedding_cache_ttl_seconds", EXPECTED_TTL_SECONDS)
    redis_client = FakeRedis()

    passage_provider, passage_model = _build_provider(monkeypatch, redis_client=redis_client)
    passage_provider.encode_passages(TOPIC_QUERY_TEXTS[:1], PROVIDER_CODE)
    assert passage_model.encode_calls == 1

    query_provider, query_model = _build_provider(monkeypatch, redis_client=redis_client)
    query_provider.encode_queries(TOPIC_QUERY_TEXTS[:1], PROVIDER_CODE)

    assert query_model.encode_calls == 1, "a passage embedding must not satisfy a query request"
    assert query_provider.last_cache_summary.hits == 0
    assert query_provider.last_cache_summary.input_type == "query"


def test_changing_model_snapshot_revision_creates_misses_not_stale_hits(monkeypatch):
    monkeypatch.setattr(settings, "embedding_cache_enabled", True)
    monkeypatch.setattr(settings, "embedding_cache_ttl_seconds", EXPECTED_TTL_SECONDS)
    redis_client = FakeRedis()

    old_provider, _old_model = _build_provider(
        monkeypatch, redis_client=redis_client, snapshot_revision="rev-a"
    )
    old_provider.encode_queries(TOPIC_QUERY_TEXTS[:2], PROVIDER_CODE)

    new_provider, new_model = _build_provider(
        monkeypatch, redis_client=redis_client, snapshot_revision="rev-b"
    )
    new_provider.encode_queries(TOPIC_QUERY_TEXTS[:2], PROVIDER_CODE)

    assert new_model.encode_calls == 1
    assert new_provider.last_cache_summary.hits == 0
    assert new_provider.last_cache_summary.misses == 2


def test_cache_key_isolates_every_required_dimension_and_hides_raw_text():
    base = dict(
        key_prefix="eternal_world",
        provider_code=PROVIDER_CODE,
        provider_model_name="BAAI/bge-m3",
        snapshot_revision="rev-a",
        mode="dense_sparse",
        input_type="query",
        dimension=1024,
        text=TOPIC_QUERY_TEXTS[0],
    )
    baseline = build_cache_key(**base)

    for field, changed_value in (
        ("provider_code", "bge_m3_dense_sparse_multivector"),
        ("provider_model_name", "BAAI/bge-m3-other"),
        ("snapshot_revision", "rev-b"),
        ("mode", "dense_sparse_multivector"),
        ("input_type", "passage"),
        ("dimension", 768),
        ("text", TOPIC_QUERY_TEXTS[1]),
    ):
        assert build_cache_key(**{**base, field: changed_value}) != baseline, field

    # Raw query text is never part of the key - only a SHA-256 hash.
    assert TOPIC_QUERY_TEXTS[0] not in baseline
    assert "sha256:" in baseline
    assert baseline.startswith("eternal_world:embedding_cache:")


# --- 7: Redis unavailable -------------------------------------------------


def test_redis_failure_degrades_to_one_batch_model_call_without_leaking_text(monkeypatch, capsys):
    monkeypatch.setattr(settings, "embedding_cache_enabled", True)
    monkeypatch.setattr(settings, "embedding_cache_ttl_seconds", EXPECTED_TTL_SECONDS)
    redis_client = FakeRedis(fail=True)
    provider, model = _build_provider(monkeypatch, redis_client=redis_client)

    encoded = provider.encode_queries(TOPIC_QUERY_TEXTS, PROVIDER_CODE)

    # The request succeeds: a cache outage must never fail an embedding.
    assert len(encoded.dense_vectors) == 8
    assert model.encode_calls == 1
    summary = provider.last_cache_summary
    assert summary.errors > 0

    logged = capsys.readouterr().out
    for text in TOPIC_QUERY_TEXTS:
        assert text not in logged


def test_redis_client_construction_failure_falls_back_to_null_cache(monkeypatch):
    monkeypatch.setattr(settings, "embedding_cache_enabled", True)
    monkeypatch.setattr(settings, "embedding_cache_provider", "redis")

    def _broken_factory():
        raise RuntimeError("redis connection refused")

    cache = build_embedding_cache(redis_client_factory=_broken_factory)
    assert isinstance(cache, NullEmbeddingCache)


def test_cache_disabled_setting_returns_null_cache(monkeypatch):
    monkeypatch.setattr(settings, "embedding_cache_enabled", False)
    assert isinstance(build_embedding_cache(), NullEmbeddingCache)


# --- 8: TTL ---------------------------------------------------------------


def test_redis_set_uses_the_configured_expiry(monkeypatch):
    monkeypatch.setattr(settings, "embedding_cache_enabled", True)
    monkeypatch.setattr(settings, "embedding_cache_ttl_seconds", EXPECTED_TTL_SECONDS)
    redis_client = FakeRedis()
    provider, _model = _build_provider(monkeypatch, redis_client=redis_client)

    provider.encode_queries(TOPIC_QUERY_TEXTS[:3], PROVIDER_CODE)

    assert len(redis_client.set_calls) == 3
    for _key, expiry in redis_client.set_calls:
        assert expiry == EXPECTED_TTL_SECONDS


@pytest.mark.parametrize("compose_file", ["docker-compose.yml", "docker-compose.prod.yml"])
def test_configured_runtime_never_uses_a_non_expiring_embedding_cache(compose_file):
    """No service may enable the cache without a finite TTL, and the
    maintenance worker (mock provider only) must never enable it at all."""

    compose = yaml.safe_load(_resolve_compose_path(compose_file).read_text(encoding="utf-8"))
    services = compose["services"]

    enabled_services = []
    for name, service in services.items():
        environment = service.get("environment") or {}
        if str(environment.get("EMBEDDING_CACHE_ENABLED", "")).lower() != "true":
            continue
        enabled_services.append(name)
        assert environment.get("EMBEDDING_CACHE_PROVIDER") == "redis", name
        assert int(environment["EMBEDDING_CACHE_TTL_SECONDS"]) == EXPECTED_TTL_SECONDS, name
        assert int(environment["EMBEDDING_CACHE_TTL_SECONDS"]) > 0, name
        assert environment.get("EMBEDDING_CACHE_KEY_PREFIX") == "eternal_world", name

    assert "backend" in enabled_services
    assert "embedding_worker" in enabled_services
    assert "maintenance_worker" not in enabled_services


def test_zero_ttl_is_the_unconfigured_default_and_is_never_used_at_runtime():
    """The `Settings` default stays 0 (explicitly opt-in), so every runtime
    that enables the cache must supply a real TTL - which the compose files
    above are asserted to do."""

    from app.core.config import Settings

    assert Settings.model_fields["embedding_cache_ttl_seconds"].default == 0
    assert Settings.model_fields["embedding_cache_enabled"].default is False


# --- 9: warm AI Biographer request end to end -----------------------------


def _install_cached_bge_m3_query_encoder(monkeypatch, redis_client: FakeRedis) -> FakeBgeM3Model:
    """Route the Biographer's batch query encode through the REAL
    `default_encode_hybrid_query_vectors_batch` -> `BgeM3HybridEmbeddingProvider`
    -> embedding-cache code path, with a fake model and a fake Redis.

    Nothing real is loaded: `FakeBgeM3Model` replaces the 2GB
    `BGEM3FlagModel`, and `FakeRedis` replaces the live server.
    """

    from app.modules.rag_retrieval import hybrid as hybrid_module

    model = FakeBgeM3Model()
    monkeypatch.setattr(hybrid_module, "_can_use_real_bge_m3_hybrid_provider", lambda: True)
    monkeypatch.setattr(
        bge_m3_hybrid_module,
        "resolve_local_snapshot_path",
        lambda name, cache_dir=None: "/models/snapshots/rev-a",
    )

    real_provider_class = BgeM3HybridEmbeddingProvider

    def _build_fake_backed_provider(*, device="cpu", cache_dir=None):
        provider = real_provider_class(device=device, cache_dir=cache_dir)
        provider._models[PROVIDER_CODE] = model
        provider._model_encode_locks[PROVIDER_CODE] = None
        provider._embedding_cache = RedisEmbeddingCache(redis_client)
        return provider

    monkeypatch.setattr(
        bge_m3_hybrid_module, "BgeM3HybridEmbeddingProvider", _build_fake_backed_provider
    )
    return model


def test_warm_biographer_request_hits_cache_eight_times_and_invokes_no_model(client, monkeypatch):
    from tests.test_task_65_11_1_biographer_query_batch import (
        FakeQdrantClient,
        RetrievalCallCounters,
        create_memorial_with_indexed_biography,
        request_next_question,
    )
    from app.modules.avatar_biographer import topics as topic_catalog
    from app.modules.rag_retrieval import service as rag_service

    monkeypatch.setattr(settings, "embedding_cache_enabled", True)
    monkeypatch.setattr(settings, "embedding_cache_ttl_seconds", EXPECTED_TTL_SECONDS)
    redis_client = FakeRedis()
    counters = RetrievalCallCounters()
    monkeypatch.setattr(rag_service, "build_qdrant_client", lambda: FakeQdrantClient(counters))

    model = _install_cached_bge_m3_query_encoder(monkeypatch, redis_client)

    _token, profile_id = create_memorial_with_indexed_biography(client, "cache-warm@example.com")

    cold = request_next_question(profile_id, locale="cs")
    assert cold is not None
    assert len(topic_catalog.BIOGRAPHER_TOPICS) == 8
    assert model.encode_calls == 1, "cold request: exactly one batch model invocation"
    assert model.encoded_batches[0] == [
        topic.questions["cs"] for topic in topic_catalog.BIOGRAPHER_TOPICS
    ]
    assert len(redis_client.set_calls) == 8
    assert counters.qdrant_batch_search_calls == 1

    # A second memorial re-uses the SAME eight topic query texts, so the warm
    # request must be a pure cache read: zero model invocations, and Qdrant
    # retrieval still runs on the cached vectors.
    _token2, profile_id2 = create_memorial_with_indexed_biography(client, "cache-warm2@example.com")
    warm = request_next_question(profile_id2, locale="cs")

    assert warm is not None
    assert model.encode_calls == 1, "warm request must invoke the model zero additional times"
    assert counters.qdrant_batch_search_calls == 2
    assert counters.scalar_query_encode_calls == 0
    # Topic-selection semantics unchanged: no evidence -> first catalog topic.
    assert warm.topic == cold.topic == topic_catalog.BIOGRAPHER_TOPICS[0].key


def test_redis_cache_set_without_ttl_is_only_reachable_when_ttl_is_zero():
    redis_client = FakeRedis()
    cache = RedisEmbeddingCache(redis_client)
    payload = embedding_cache_module.build_cached_embedding_payload(
        provider_code=PROVIDER_CODE,
        provider_model_name="BAAI/bge-m3",
        snapshot_revision="rev-a",
        mode="dense_sparse",
        input_type="query",
        dimension=2,
        dense_vector=[0.1, 0.2],
        sparse_vector={"tok": 1.0},
        text="text",
    )

    cache.set("k1", payload, EXPECTED_TTL_SECONDS)
    cache.set("k2", payload, 0)

    assert redis_client.set_calls == [("k1", EXPECTED_TTL_SECONDS), ("k2", None)]
