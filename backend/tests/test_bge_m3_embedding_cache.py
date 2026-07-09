from __future__ import annotations

from types import SimpleNamespace

from app.modules.embeddings.embedding_cache import (
    RedisEmbeddingCache,
    build_cache_key,
    build_cached_embedding_payload,
)
from app.modules.embeddings.providers.bge_m3_hybrid import BgeM3HybridEmbeddingProvider


class _FakeRedisClient:
    def __init__(self) -> None:
        self.storage: dict[str, str] = {}

    def get(self, key: str) -> str | None:
        return self.storage.get(key)

    def set(self, key: str, value: str, ex: int | None = None) -> bool:
        self.storage[key] = value
        return True


class _FakeBGEM3FlagModel:
    encode_calls: list[dict[str, object]] = []

    def __init__(self, model_name: str, **kwargs) -> None:
        self.model_name = model_name
        self.kwargs = dict(kwargs)

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
        materialized_texts = list(texts)
        self.__class__.encode_calls.append(
            {
                "texts": materialized_texts,
                "batch_size": batch_size,
                "max_length": max_length,
                "return_dense": return_dense,
                "return_sparse": return_sparse,
                "return_colbert_vecs": return_colbert_vecs,
            }
        )
        dense_vecs: list[list[float]] = []
        lexical_weights: list[dict[str, float]] = []
        for text in materialized_texts:
            normalized = " ".join(text.strip().split())
            score = float(sum(ord(character) for character in normalized) % 997)
            dense_vecs.append([score, score + 1.0])
            lexical_weights.append({normalized: score})
        return {
            "dense_vecs": dense_vecs,
            "lexical_weights": lexical_weights,
        }


def test_bge_m3_embedding_cache_preserves_order_and_only_encodes_unique_misses(monkeypatch):
    _FakeBGEM3FlagModel.encode_calls = []
    fake_redis_client = _FakeRedisClient()
    cache = RedisEmbeddingCache(fake_redis_client)

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
    monkeypatch.setattr(
        "app.modules.embeddings.providers.bge_m3_hybrid.build_embedding_cache",
        lambda: cache,
    )

    cached_text = "already cached"
    cached_key = build_cache_key(
        key_prefix="eternal_world",
        provider_code="bge_m3_dense_sparse",
        provider_model_name="BAAI/bge-m3",
        snapshot_revision="5617a9f61b028005a4858fdac845db406aefb181",
        mode="dense_sparse",
        input_type="query",
        dimension=1024,
        text=cached_text,
    )
    cached_payload = build_cached_embedding_payload(
        provider_code="bge_m3_dense_sparse",
        provider_model_name="BAAI/bge-m3",
        snapshot_revision="5617a9f61b028005a4858fdac845db406aefb181",
        mode="dense_sparse",
        input_type="query",
        dimension=1024,
        dense_vector=[11.0, 12.0],
        sparse_vector={"cached": 11.0},
        text=cached_text,
    )
    fake_redis_client.storage[cached_key] = cached_payload.to_json()

    provider = BgeM3HybridEmbeddingProvider()
    result = provider.encode_texts(
        [
            cached_text,
            "missing text",
            cached_text,
            " missing   text ",
        ],
        provider_code="bge_m3_dense_sparse",
        input_type="query",
    )

    assert len(_FakeBGEM3FlagModel.encode_calls) == 1
    assert _FakeBGEM3FlagModel.encode_calls[0]["texts"] == ["missing text"]
    assert result.dense_vectors == [
        [11.0, 12.0],
        result.dense_vectors[1],
        [11.0, 12.0],
        result.dense_vectors[1],
    ]
    assert result.sparse_vectors == [
        {"cached": 11.0},
        result.sparse_vectors[1],
        {"cached": 11.0},
        result.sparse_vectors[1],
    ]


def test_bge_m3_embedding_cache_writes_missing_payloads_for_roundtrip_hits(monkeypatch):
    _FakeBGEM3FlagModel.encode_calls = []
    fake_redis_client = _FakeRedisClient()
    cache = RedisEmbeddingCache(fake_redis_client)

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
    monkeypatch.setattr(
        "app.modules.embeddings.providers.bge_m3_hybrid.build_embedding_cache",
        lambda: cache,
    )

    provider = BgeM3HybridEmbeddingProvider()
    first_result = provider.encode_texts(
        ["new text"],
        provider_code="bge_m3_dense_sparse",
        input_type="passage",
    )
    second_result = provider.encode_texts(
        [" new   text "],
        provider_code="bge_m3_dense_sparse",
        input_type="passage",
    )

    assert len(_FakeBGEM3FlagModel.encode_calls) == 1
    assert first_result.dense_vectors == second_result.dense_vectors
    assert first_result.sparse_vectors == second_result.sparse_vectors
