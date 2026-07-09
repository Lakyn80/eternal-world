from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any, Protocol

from app.core.config import settings


EMBEDDING_CACHE_SCHEMA_VERSION = "v1"


@dataclass(frozen=True)
class CachedEmbeddingPayload:
    cache_schema_version: str
    provider_code: str
    provider_model_name: str
    snapshot_revision: str
    mode: str
    input_type: str
    dimension: int
    dense_vector: list[float]
    sparse_vector: dict[str, float]
    text_hash: str
    created_at: str
    multivector: list[list[float]] | None = None

    def to_json(self) -> str:
        return json.dumps(
            {
                "cache_schema_version": self.cache_schema_version,
                "provider_code": self.provider_code,
                "provider_model_name": self.provider_model_name,
                "snapshot_revision": self.snapshot_revision,
                "mode": self.mode,
                "input_type": self.input_type,
                "dimension": self.dimension,
                "dense_vector": self.dense_vector,
                "sparse_vector": self.sparse_vector,
                "multivector": self.multivector,
                "text_hash": self.text_hash,
                "created_at": self.created_at,
            },
            ensure_ascii=False,
            separators=(",", ":"),
        )

    @classmethod
    def from_json(cls, raw_value: str) -> CachedEmbeddingPayload:
        payload = json.loads(raw_value)
        if not isinstance(payload, dict):
            raise ValueError("Embedding cache payload must be a JSON object")

        dense_vector = payload.get("dense_vector")
        sparse_vector = payload.get("sparse_vector")
        multivector = payload.get("multivector")
        if not isinstance(dense_vector, list) or not isinstance(sparse_vector, dict):
            raise ValueError("Embedding cache payload vectors are invalid")

        normalized_multivector: list[list[float]] | None = None
        if multivector is not None:
            if not isinstance(multivector, list):
                raise ValueError("Embedding cache multivector payload is invalid")
            normalized_multivector = [
                [float(value) for value in token_vector]
                for token_vector in multivector
            ]

        return cls(
            cache_schema_version=str(payload.get("cache_schema_version") or ""),
            provider_code=str(payload.get("provider_code") or ""),
            provider_model_name=str(payload.get("provider_model_name") or ""),
            snapshot_revision=str(payload.get("snapshot_revision") or ""),
            mode=str(payload.get("mode") or ""),
            input_type=str(payload.get("input_type") or ""),
            dimension=int(payload.get("dimension") or 0),
            dense_vector=[float(value) for value in dense_vector],
            sparse_vector={str(key): float(value) for key, value in sparse_vector.items()},
            multivector=normalized_multivector,
            text_hash=str(payload.get("text_hash") or ""),
            created_at=str(payload.get("created_at") or ""),
        )


class EmbeddingCacheProtocol(Protocol):
    def get(self, key: str) -> CachedEmbeddingPayload | None:
        ...

    def set(self, key: str, value: CachedEmbeddingPayload, ttl_seconds: int) -> None:
        ...


def _emit_embedding_cache_log(message: str) -> None:
    print(f"[embedding_cache] {message}", flush=True)


def _hash_prefix_from_cache_key(key: str) -> str:
    suffix = key.rsplit(":sha256:", 1)
    if len(suffix) != 2:
        return "unknown"
    return suffix[1][:8]


def _normalize_cache_text(text: str) -> str:
    return " ".join(text.strip().split())


def build_text_hash(text: str) -> str:
    normalized_text = _normalize_cache_text(text)
    digest = hashlib.sha256(normalized_text.encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def _sanitize_provider_model_name(provider_model_name: str) -> str:
    return provider_model_name.strip().replace("/", "-")


def build_cache_key(
    *,
    key_prefix: str,
    provider_code: str,
    provider_model_name: str,
    snapshot_revision: str,
    mode: str,
    input_type: str,
    dimension: int,
    text: str,
) -> str:
    return (
        f"{key_prefix}:embedding_cache:{EMBEDDING_CACHE_SCHEMA_VERSION}:"
        f"{provider_code}:{_sanitize_provider_model_name(provider_model_name)}:{snapshot_revision}:"
        f"mode={mode}:{input_type}:{dimension}:{build_text_hash(text)}"
    )


def build_cached_embedding_payload(
    *,
    provider_code: str,
    provider_model_name: str,
    snapshot_revision: str,
    mode: str,
    input_type: str,
    dimension: int,
    dense_vector: list[float],
    sparse_vector: dict[str, float],
    text: str,
    multivector: list[list[float]] | None = None,
) -> CachedEmbeddingPayload:
    return CachedEmbeddingPayload(
        cache_schema_version=EMBEDDING_CACHE_SCHEMA_VERSION,
        provider_code=provider_code,
        provider_model_name=provider_model_name,
        snapshot_revision=snapshot_revision,
        mode=mode,
        input_type=input_type,
        dimension=dimension,
        dense_vector=[float(value) for value in dense_vector],
        sparse_vector={str(key): float(value) for key, value in sparse_vector.items()},
        multivector=(
            [[float(value) for value in token_vector] for token_vector in multivector]
            if multivector is not None
            else None
        ),
        text_hash=build_text_hash(text),
        created_at=datetime.now(UTC).isoformat(),
    )


class NullEmbeddingCache:
    def get(self, key: str) -> CachedEmbeddingPayload | None:
        return None

    def set(self, key: str, value: CachedEmbeddingPayload, ttl_seconds: int) -> None:
        return None

    def consume_error_count(self) -> int:
        return 0


class RedisEmbeddingCache:
    def __init__(self, redis_client: Any) -> None:
        self._redis_client = redis_client
        self._error_count = 0

    def get(self, key: str) -> CachedEmbeddingPayload | None:
        try:
            raw_value = self._redis_client.get(key)
        except Exception as exc:
            self._error_count += 1
            _emit_embedding_cache_log(
                "redis_error "
                f"operation=get key_hash_prefix={_hash_prefix_from_cache_key(key)} "
                f"error={exc.__class__.__name__}: {exc}"
            )
            return None

        if raw_value is None:
            return None

        try:
            return CachedEmbeddingPayload.from_json(str(raw_value))
        except Exception as exc:
            self._error_count += 1
            _emit_embedding_cache_log(
                "redis_error "
                f"operation=deserialize key_hash_prefix={_hash_prefix_from_cache_key(key)} "
                f"error={exc.__class__.__name__}: {exc}"
            )
            return None

    def set(self, key: str, value: CachedEmbeddingPayload, ttl_seconds: int) -> None:
        try:
            if ttl_seconds > 0:
                self._redis_client.set(key, value.to_json(), ex=ttl_seconds)
            else:
                self._redis_client.set(key, value.to_json())
        except Exception as exc:
            self._error_count += 1
            _emit_embedding_cache_log(
                "redis_error "
                f"operation=set key_hash_prefix={_hash_prefix_from_cache_key(key)} "
                f"error={exc.__class__.__name__}: {exc}"
            )

    def consume_error_count(self) -> int:
        error_count = self._error_count
        self._error_count = 0
        return error_count


def build_embedding_cache(
    *,
    redis_client_factory: Any | None = None,
) -> EmbeddingCacheProtocol:
    if not settings.embedding_cache_enabled:
        return NullEmbeddingCache()
    if settings.embedding_cache_provider != "redis":
        return NullEmbeddingCache()

    try:
        if redis_client_factory is None:
            from app.cache.redis_client import get_redis_client

            redis_client = get_redis_client()
        else:
            redis_client = redis_client_factory()
    except Exception as exc:
        _emit_embedding_cache_log(
            f"build_fallback provider=redis error={exc.__class__.__name__}: {exc}"
        )
        return NullEmbeddingCache()

    return RedisEmbeddingCache(redis_client)
