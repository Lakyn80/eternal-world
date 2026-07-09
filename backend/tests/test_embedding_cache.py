from __future__ import annotations

from app.core.config import settings
from app.modules.embeddings.embedding_cache import (
    NullEmbeddingCache,
    RedisEmbeddingCache,
    build_cache_key,
    build_cached_embedding_payload,
    build_embedding_cache,
)


class _FakeRedisClient:
    def __init__(self) -> None:
        self.storage: dict[str, str] = {}
        self.get_calls: list[str] = []
        self.set_calls: list[dict[str, object]] = []
        self.fail_get = False
        self.fail_set = False

    def get(self, key: str) -> str | None:
        self.get_calls.append(key)
        if self.fail_get:
            raise RuntimeError("redis get unavailable")
        return self.storage.get(key)

    def set(self, key: str, value: str, ex: int | None = None) -> bool:
        self.set_calls.append({"key": key, "value": value, "ex": ex})
        if self.fail_set:
            raise RuntimeError("redis set unavailable")
        self.storage[key] = value
        return True


def test_build_cache_key_changes_with_revision_and_input_type_and_hides_raw_text():
    key_query = build_cache_key(
        key_prefix="eternal_world",
        provider_code="bge_m3_dense_sparse",
        provider_model_name="BAAI/bge-m3",
        snapshot_revision="revision-a",
        mode="dense_sparse",
        input_type="query",
        dimension=1024,
        text="  Mixed   Text  Example  ",
    )
    key_passage = build_cache_key(
        key_prefix="eternal_world",
        provider_code="bge_m3_dense_sparse",
        provider_model_name="BAAI/bge-m3",
        snapshot_revision="revision-a",
        mode="dense_sparse",
        input_type="passage",
        dimension=1024,
        text="Mixed Text Example",
    )
    key_new_revision = build_cache_key(
        key_prefix="eternal_world",
        provider_code="bge_m3_dense_sparse",
        provider_model_name="BAAI/bge-m3",
        snapshot_revision="revision-b",
        mode="dense_sparse",
        input_type="query",
        dimension=1024,
        text="Mixed Text Example",
    )

    assert "Mixed Text Example" not in key_query
    assert "BAAI-bge-m3" in key_query
    assert "mode=dense_sparse" in key_query
    assert key_query != key_passage
    assert key_query != key_new_revision


def test_redis_embedding_cache_roundtrip_returns_dense_and_sparse_payload():
    redis_client = _FakeRedisClient()
    cache = RedisEmbeddingCache(redis_client)
    cache_key = build_cache_key(
        key_prefix="eternal_world",
        provider_code="bge_m3_dense_sparse",
        provider_model_name="BAAI/bge-m3",
        snapshot_revision="5617a9f",
        mode="dense_sparse",
        input_type="query",
        dimension=1024,
        text="Where is Brno?",
    )
    payload = build_cached_embedding_payload(
        provider_code="bge_m3_dense_sparse",
        provider_model_name="BAAI/bge-m3",
        snapshot_revision="5617a9f",
        mode="dense_sparse",
        input_type="query",
        dimension=1024,
        dense_vector=[0.1, 0.2],
        sparse_vector={"brno": 1.0},
        text="Where is Brno?",
    )

    cache.set(cache_key, payload, ttl_seconds=300)
    restored_payload = cache.get(cache_key)

    assert restored_payload is not None
    assert restored_payload.provider_code == "bge_m3_dense_sparse"
    assert restored_payload.dense_vector == [0.1, 0.2]
    assert restored_payload.sparse_vector == {"brno": 1.0}
    assert redis_client.set_calls[0]["ex"] == 300


def test_redis_embedding_cache_falls_back_safely_on_get_set_and_deserialize_errors():
    redis_client = _FakeRedisClient()
    cache = RedisEmbeddingCache(redis_client)
    cache_key = build_cache_key(
        key_prefix="eternal_world",
        provider_code="bge_m3_dense_sparse",
        provider_model_name="BAAI/bge-m3",
        snapshot_revision="5617a9f",
        mode="dense_sparse",
        input_type="query",
        dimension=1024,
        text="Where is Prague?",
    )
    payload = build_cached_embedding_payload(
        provider_code="bge_m3_dense_sparse",
        provider_model_name="BAAI/bge-m3",
        snapshot_revision="5617a9f",
        mode="dense_sparse",
        input_type="query",
        dimension=1024,
        dense_vector=[0.1],
        sparse_vector={"prague": 1.0},
        text="Where is Prague?",
    )

    redis_client.fail_set = True
    cache.set(cache_key, payload, ttl_seconds=0)
    redis_client.fail_set = False

    redis_client.fail_get = True
    assert cache.get(cache_key) is None
    redis_client.fail_get = False

    redis_client.storage[cache_key] = "{bad-json"
    assert cache.get(cache_key) is None
    assert cache.consume_error_count() == 3


def test_build_embedding_cache_returns_null_cache_when_disabled_or_provider_factory_fails(monkeypatch):
    monkeypatch.setattr(settings, "embedding_cache_enabled", False)
    disabled_cache = build_embedding_cache()
    assert isinstance(disabled_cache, NullEmbeddingCache)

    monkeypatch.setattr(settings, "embedding_cache_enabled", True)
    monkeypatch.setattr(settings, "embedding_cache_provider", "redis")
    failed_cache = build_embedding_cache(redis_client_factory=lambda: (_ for _ in ()).throw(RuntimeError("boom")))

    assert isinstance(failed_cache, NullEmbeddingCache)
