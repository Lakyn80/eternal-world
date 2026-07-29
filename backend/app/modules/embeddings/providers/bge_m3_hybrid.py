from __future__ import annotations

import sys
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass
from pathlib import Path
from threading import Lock
from time import perf_counter
from typing import Any

from app.core.config import settings
from app.core.metrics import observe_embedding_cache_summary
from app.modules.embedding_models.service import get_embedding_model
from app.modules.embeddings.bge_m3_model_cache import (
    BGE_M3_DEFAULT_REPO_ID,
    describe_cache_dir,
    is_huggingface_offline_mode,
    resolve_bge_m3_model_load_path,
    resolve_local_snapshot_path,
)
from app.modules.embeddings.embedding_cache import (
    CachedEmbeddingPayload,
    NullEmbeddingCache,
    build_cache_key,
    build_cached_embedding_payload,
    build_embedding_cache,
    build_text_hash,
)
from app.modules.embeddings.providers.base import BaseEmbeddingProvider, EmbeddingVector


BGE_M3_HYBRID_PROVIDER_NAME = "bge_m3_hybrid"
BGE_M3_SHARED_MODEL_FAMILY = "bge_m3_full_hybrid_runtime"
SAFE_BGE_M3_HYBRID_FAILURE_MESSAGE = "BGE-M3 hybrid embedding generation failed"

try:
    import resource
except ImportError:  # pragma: no cover - resource is unavailable on some local test hosts.
    resource = None


class BgeM3HybridProviderError(Exception):
    pass


@dataclass(frozen=True)
class _BgeM3CacheContext:
    provider_code: str
    provider_model_name: str
    snapshot_revision: str
    mode: str
    dimension: int


@dataclass(frozen=True)
class _PreparedCacheItem:
    index: int
    text: str
    cache_key: str
    text_hash: str


@dataclass(frozen=True)
class BgeM3HybridCacheSummary:
    provider_code: str
    provider_model_name: str
    snapshot_revision: str
    source: str
    device: str
    mode: str
    input_type: str
    batch_size: int
    unique_texts: int
    hits: int
    misses: int
    writes: int
    errors: int
    cache_enabled: bool
    text_hash_prefixes: tuple[str, ...]


class BgeM3HybridEmbeddings:
    def __init__(
        self,
        *,
        dense_vectors: list[list[float]],
        sparse_vectors: list[dict[str, float]],
        multivectors: list[list[list[float]]] | None,
    ) -> None:
        self.dense_vectors = dense_vectors
        self.sparse_vectors = sparse_vectors
        self.multivectors = multivectors


_shared_model_cache_enabled: ContextVar[bool] = ContextVar(
    "bge_m3_hybrid_shared_model_cache_enabled",
    default=False,
)
_shared_models: dict[tuple[object, ...], Any] = {}
_shared_models_lock = Lock()

#: Task 65.11: a per-shared-model encode lock, created alongside each entry
#: in `_shared_models`. This is *not* about protecting model loading (the
#: double-checked-locking around `_shared_models_lock` already handles
#: that) - it exists because `FlagEmbedding`'s
#: `AbsEmbedder.encode_single_device()` unconditionally calls
#: `self.model.to(device)` and `self.model.float()` on *every single*
#: `.encode()` call, not just once at load time (verified by reading the
#: installed `FlagEmbedding` package source, not assumed). Those two calls
#: mutate the shared `nn.Module`'s `_parameters`/`_buffers` trees in place
#: (`nn.Module._apply()` reassigns fresh `Parameter` wrappers even when the
#: device/dtype already match). Once a single model instance is shared
#: across concurrent requests (the fix below), two requests' encode calls
#: could otherwise race on that mutation while a third request's forward
#: pass is mid-read of the same parameter tree. Serializing `.encode()`
#: calls on a *shared* model instance is the smallest guard that removes
#: this hazard; unshared (per-request-private) model instances never take
#: this lock, since there is nothing else operating on their model
#: concurrently.
_shared_model_encode_locks: dict[tuple[object, ...], Lock] = {}


def _emit_bge_m3_hybrid_log(message: str) -> None:
    print(f"[bge_m3_hybrid] {message}", flush=True)


def _get_process_rss_mb() -> float | None:
    if resource is None:
        return None

    rss_value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss_value <= 0:
        return None

    if sys.platform == "darwin":
        return round(rss_value / (1024 * 1024), 2)

    return round(rss_value / 1024, 2)


def _emit_bge_m3_hybrid_memory_log(*, stage: str, provider_code: str, model_name: str) -> None:
    rss_mb = _get_process_rss_mb()
    if rss_mb is None:
        return

    _emit_bge_m3_hybrid_log(
        "memory "
        f"stage={stage} provider_code={provider_code} model_name={model_name} rss_mb={rss_mb}"
    )


@contextmanager
def enable_bge_m3_hybrid_shared_model_cache(*, clear_on_exit: bool = False):
    token = _shared_model_cache_enabled.set(True)
    try:
        yield
    finally:
        _shared_model_cache_enabled.reset(token)
        if clear_on_exit:
            clear_bge_m3_hybrid_shared_model_cache()


def clear_bge_m3_hybrid_shared_model_cache() -> None:
    with _shared_models_lock:
        _shared_models.clear()
        _shared_model_encode_locks.clear()


class BgeM3HybridEmbeddingProvider:
    def __init__(
        self,
        *,
        device: str = "cpu",
        cache_dir: Path | None = None,
    ) -> None:
        self.device = device
        self.cache_dir = str(cache_dir) if cache_dir is not None else None
        self._models: dict[str, Any] = {}
        self._model_encode_locks: dict[str, Lock | None] = {}
        self._cache_contexts: dict[str, _BgeM3CacheContext] = {}
        self._embedding_cache = build_embedding_cache()
        self._last_cache_summary: BgeM3HybridCacheSummary | None = None
        self._lock = Lock()

    @property
    def last_cache_summary(self) -> BgeM3HybridCacheSummary | None:
        return self._last_cache_summary

    def encode_query(self, text: str, provider_code: str) -> BgeM3HybridEmbeddings:
        return self.encode_texts([text], provider_code=provider_code, input_type="query")

    def encode_queries(self, texts: list[str], provider_code: str) -> BgeM3HybridEmbeddings:
        """Task 65.11.1 - N query texts, ONE model invocation.

        Query semantics (`input_type="query"`), never the passage-oriented
        `encode_passages()`: the embedding cache key, the cached payload's
        `input_type` guard and the (future) provider-side query/passage
        prefixing all depend on this distinction, so a cached passage
        embedding can never satisfy a query request and vice versa.
        Output order matches input order exactly.
        """

        return self.encode_texts(texts, provider_code=provider_code, input_type="query")

    def encode_passages(self, texts: list[str], provider_code: str) -> BgeM3HybridEmbeddings:
        return self.encode_texts(texts, provider_code=provider_code, input_type="passage")

    def encode_texts(
        self,
        texts: list[str],
        *,
        provider_code: str,
        input_type: str,
    ) -> BgeM3HybridEmbeddings:
        if not texts:
            return BgeM3HybridEmbeddings(dense_vectors=[], sparse_vectors=[], multivectors=None)

        normalized_provider_code = provider_code.strip().lower()
        model = self._get_or_load_model(normalized_provider_code)
        cache_context = self._get_cache_context(normalized_provider_code)
        return_colbert_vecs = normalized_provider_code == "bge_m3_dense_sparse_multivector"
        prepared_items: list[_PreparedCacheItem] = []
        unique_items_by_key: dict[str, _PreparedCacheItem] = {}
        for index, text in enumerate(texts):
            cache_key = build_cache_key(
                key_prefix=settings.embedding_cache_key_prefix,
                provider_code=cache_context.provider_code,
                provider_model_name=cache_context.provider_model_name,
                snapshot_revision=cache_context.snapshot_revision,
                mode=cache_context.mode,
                input_type=input_type,
                dimension=cache_context.dimension,
                text=text,
            )
            item = _PreparedCacheItem(
                index=index,
                text=text,
                cache_key=cache_key,
                text_hash=build_text_hash(text),
            )
            prepared_items.append(item)
            unique_items_by_key.setdefault(cache_key, item)

        cached_payloads_by_key: dict[str, CachedEmbeddingPayload] = {}
        cached_hit_keys: set[str] = set()
        missing_items: list[_PreparedCacheItem] = []
        for cache_key, item in unique_items_by_key.items():
            cached_payload = self._embedding_cache.get(cache_key)
            if cached_payload is None:
                missing_items.append(item)
                continue
            if not _cached_payload_matches_context(
                payload=cached_payload,
                cache_context=cache_context,
                input_type=input_type,
                expected_text_hash=item.text_hash,
                require_multivector=return_colbert_vecs,
            ):
                missing_items.append(item)
                continue
            cached_payloads_by_key[cache_key] = cached_payload
            cached_hit_keys.add(cache_key)

        if missing_items:
            raw_payloads = self._encode_missing_items(
                model=model,
                provider_code=normalized_provider_code,
                input_type=input_type,
                texts=[item.text for item in missing_items],
                return_colbert_vecs=return_colbert_vecs,
                encode_lock=self._model_encode_locks.get(normalized_provider_code),
            )
            for offset, item in enumerate(missing_items):
                payload = build_cached_embedding_payload(
                    provider_code=cache_context.provider_code,
                    provider_model_name=cache_context.provider_model_name,
                    snapshot_revision=cache_context.snapshot_revision,
                    mode=cache_context.mode,
                    input_type=input_type,
                    dimension=cache_context.dimension,
                    dense_vector=raw_payloads.dense_vectors[offset],
                    sparse_vector=raw_payloads.sparse_vectors[offset],
                    multivector=(
                        raw_payloads.multivectors[offset]
                        if raw_payloads.multivectors is not None
                        else None
                    ),
                    text=item.text,
                )
                cached_payloads_by_key[item.cache_key] = payload
                self._embedding_cache.set(
                    item.cache_key,
                    payload,
                    settings.embedding_cache_ttl_seconds,
                )

        dense_vectors: list[list[float]] = []
        sparse_vectors: list[dict[str, float]] = []
        multivectors: list[list[list[float]]] | None = [] if return_colbert_vecs else None
        for item in prepared_items:
            payload = cached_payloads_by_key.get(item.cache_key)
            if payload is None:
                raise BgeM3HybridProviderError("BGE-M3 cached embedding output is incomplete")
            dense_vectors.append(list(payload.dense_vector))
            sparse_vectors.append(dict(payload.sparse_vector))
            if multivectors is not None:
                if payload.multivector is None:
                    raise BgeM3HybridProviderError("BGE-M3 cached multivector output is invalid")
                multivectors.append([list(token_vector) for token_vector in payload.multivector])

        hit_count = sum(1 for item in prepared_items if item.cache_key in cached_hit_keys)
        error_count = self._consume_cache_error_count()
        self._last_cache_summary = BgeM3HybridCacheSummary(
            provider_code=normalized_provider_code,
            provider_model_name=cache_context.provider_model_name,
            snapshot_revision=cache_context.snapshot_revision,
            source="local_snapshot" if cache_context.snapshot_revision != "missing" else "missing",
            device=self.device,
            mode=cache_context.mode,
            input_type=input_type,
            batch_size=len(texts),
            unique_texts=len(unique_items_by_key),
            hits=hit_count,
            misses=len(missing_items),
            writes=len(missing_items),
            errors=error_count,
            cache_enabled=not isinstance(self._embedding_cache, NullEmbeddingCache),
            text_hash_prefixes=tuple(
                item.text_hash.split(":", 1)[1][:8]
                for item in unique_items_by_key.values()
            ),
        )
        _emit_bge_m3_hybrid_log(
            "cache summary "
            f"provider_code={normalized_provider_code} input_type={input_type} "
            f"mode={cache_context.mode} batch_size={len(texts)} unique_texts={len(unique_items_by_key)} "
            f"hits={hit_count} misses={len(missing_items)} writes={len(missing_items)} "
            f"errors={error_count}"
        )
        observe_embedding_cache_summary(
            provider_code=normalized_provider_code,
            input_type=input_type,
            mode=cache_context.mode,
            hits=hit_count,
            misses=len(missing_items),
            writes=len(missing_items),
            errors=error_count,
        )
        return BgeM3HybridEmbeddings(
            dense_vectors=dense_vectors,
            sparse_vectors=sparse_vectors,
            multivectors=multivectors,
        )

    def _get_cache_context(self, provider_code: str) -> _BgeM3CacheContext:
        existing_context = self._cache_contexts.get(provider_code)
        if existing_context is not None:
            return existing_context

        model_definition = get_embedding_model(provider_code)
        provider_model_name = model_definition.provider_model_name or BGE_M3_DEFAULT_REPO_ID
        snapshot_path = resolve_local_snapshot_path(
            provider_model_name,
            cache_dir=self.cache_dir,
        )
        snapshot_revision = _resolve_snapshot_revision(snapshot_path)
        cache_context = _BgeM3CacheContext(
            provider_code=provider_code,
            provider_model_name=provider_model_name,
            snapshot_revision=snapshot_revision,
            mode=_resolve_bge_m3_cache_mode(provider_code),
            dimension=model_definition.dimension,
        )
        self._cache_contexts[provider_code] = cache_context
        return cache_context

    def _encode_missing_items(
        self,
        *,
        model: Any,
        provider_code: str,
        input_type: str,
        texts: list[str],
        return_colbert_vecs: bool,
        encode_lock: Lock | None = None,
    ) -> BgeM3HybridEmbeddings:
        model_definition = get_embedding_model(provider_code)
        batch_size = max(1, min(8, len(texts)))

        _emit_bge_m3_hybrid_log(
            "dense encode start "
            f"provider_code={provider_code} input_type={input_type} batch_size={len(texts)}"
        )
        _emit_bge_m3_hybrid_log(
            "sparse encode start "
            f"provider_code={provider_code} input_type={input_type} batch_size={len(texts)}"
        )
        if return_colbert_vecs:
            _emit_bge_m3_hybrid_log(
                "multivector encode start "
                f"provider_code={provider_code} input_type={input_type} batch_size={len(texts)}"
            )

        started_at = perf_counter()
        try:
            if encode_lock is not None:
                # Serialize `.encode()` calls against a model instance that
                # is shared across concurrent requests (Task 65.11) - see
                # the module-level `_shared_model_encode_locks` docstring
                # for why this is required (FlagEmbedding mutates the
                # shared nn.Module's parameter tree on every encode call,
                # not just once at load time).
                with encode_lock:
                    raw_output = model.encode(
                        texts,
                        batch_size=batch_size,
                        max_length=model_definition.max_input_tokens,
                        return_dense=True,
                        return_sparse=True,
                        return_colbert_vecs=return_colbert_vecs,
                    )
            else:
                raw_output = model.encode(
                    texts,
                    batch_size=batch_size,
                    max_length=model_definition.max_input_tokens,
                    return_dense=True,
                    return_sparse=True,
                    return_colbert_vecs=return_colbert_vecs,
                )
        except Exception as exc:  # pragma: no cover - exercised through higher-level failure tests
            _emit_bge_m3_hybrid_log(
                "encode failed "
                f"provider_code={provider_code} input_type={input_type} "
                f"batch_size={len(texts)} error={exc.__class__.__name__}: {exc}"
            )
            raise BgeM3HybridProviderError(SAFE_BGE_M3_HYBRID_FAILURE_MESSAGE) from exc

        duration_ms = round((perf_counter() - started_at) * 1000, 2)
        _emit_bge_m3_hybrid_log(
            "dense encode done "
            f"provider_code={provider_code} input_type={input_type} "
            f"batch_size={len(texts)} duration_ms={duration_ms}"
        )
        _emit_bge_m3_hybrid_log(
            "sparse encode done "
            f"provider_code={provider_code} input_type={input_type} "
            f"batch_size={len(texts)} duration_ms={duration_ms}"
        )
        if return_colbert_vecs:
            _emit_bge_m3_hybrid_log(
                "multivector encode done "
                f"provider_code={provider_code} input_type={input_type} "
                f"batch_size={len(texts)} duration_ms={duration_ms}"
            )

        dense_vectors = _coerce_dense_vectors(raw_output.get("dense_vecs"))
        sparse_vectors = _coerce_sparse_vectors(raw_output.get("lexical_weights"))
        multivectors = (
            _coerce_multivectors(raw_output.get("colbert_vecs"))
            if return_colbert_vecs
            else None
        )
        if len(dense_vectors) != len(texts) or len(sparse_vectors) != len(texts):
            raise BgeM3HybridProviderError("BGE-M3 hybrid embedding output is invalid")
        if return_colbert_vecs and (multivectors is None or len(multivectors) != len(texts)):
            raise BgeM3HybridProviderError("BGE-M3 multivector output is invalid")

        return BgeM3HybridEmbeddings(
            dense_vectors=dense_vectors,
            sparse_vectors=sparse_vectors,
            multivectors=multivectors,
        )

    def _consume_cache_error_count(self) -> int:
        consume_error_count = getattr(self._embedding_cache, "consume_error_count", None)
        if callable(consume_error_count):
            return int(consume_error_count())
        return 0

    def _get_or_load_model(self, provider_code: str):
        if provider_code in self._models:
            _emit_bge_m3_hybrid_log(f"cache hit scope=provider provider_code={provider_code}")
            return self._models[provider_code]

        with self._lock:
            if provider_code in self._models:
                _emit_bge_m3_hybrid_log(f"cache hit scope=provider provider_code={provider_code}")
                return self._models[provider_code]

            model_definition = get_embedding_model(provider_code)
            model_name = model_definition.provider_model_name
            if model_name is None:
                raise BgeM3HybridProviderError("BGE-M3 hybrid model is not configured")

            model_init_kwargs = self._build_model_init_kwargs()
            cache_key = self._build_shared_model_cache_key(
                model_name=model_name,
                model_init_kwargs=model_init_kwargs,
            )
            flag_model_class = _import_bge_m3_flag_model_class()

            if _shared_model_cache_enabled.get():
                with _shared_models_lock:
                    shared_model = _shared_models.get(cache_key)
                    if shared_model is not None:
                        self._models[provider_code] = shared_model
                        self._model_encode_locks[provider_code] = _shared_model_encode_locks[cache_key]
                        _emit_bge_m3_hybrid_log(
                            "cache hit scope=shared "
                            f"provider_code={provider_code} model_name={model_name} device={self.device}"
                        )
                        return shared_model

                    model = self._load_model_instance(
                        flag_model_class=flag_model_class,
                        provider_code=provider_code,
                        model_name=model_name,
                        model_init_kwargs=model_init_kwargs,
                    )
                    _shared_models[cache_key] = model
                    _shared_model_encode_locks[cache_key] = Lock()
                    self._model_encode_locks[provider_code] = _shared_model_encode_locks[cache_key]
            else:
                model = self._load_model_instance(
                    flag_model_class=flag_model_class,
                    provider_code=provider_code,
                    model_name=model_name,
                    model_init_kwargs=model_init_kwargs,
                )
                self._model_encode_locks[provider_code] = None

            self._models[provider_code] = model
            return model

    def _build_model_init_kwargs(self) -> dict[str, object]:
        return {
            "use_fp16": False,
            "devices": self.device,
        }

    def _build_shared_model_cache_key(
        self,
        *,
        model_name: str,
        model_init_kwargs: dict[str, object],
    ) -> tuple[object, ...]:
        frozen_kwargs = tuple(sorted((key, repr(value)) for key, value in model_init_kwargs.items()))
        return (
            BGE_M3_HYBRID_PROVIDER_NAME,
            BGE_M3_SHARED_MODEL_FAMILY,
            model_name,
            self.device,
            self.cache_dir,
            frozen_kwargs,
        )

    def _load_model_instance(
        self,
        *,
        flag_model_class,
        provider_code: str,
        model_name: str,
        model_init_kwargs: dict[str, object],
    ):
        _emit_bge_m3_hybrid_memory_log(
            stage="before_model_load",
            provider_code=provider_code,
            model_name=model_name,
        )
        resolved_cache_dir = describe_cache_dir(self.cache_dir)
        offline_mode = is_huggingface_offline_mode()
        try:
            load_path, loaded_from_local_cache = resolve_bge_m3_model_load_path(
                model_name,
                cache_dir=self.cache_dir,
                allow_remote_download=False,
            )
        except RuntimeError as exc:
            _emit_bge_m3_hybrid_log(
                "load failed "
                f"provider_code={provider_code} model_name={model_name} "
                f"cache_dir={resolved_cache_dir} source=local_snapshot device={self.device} "
                f"snapshot_exists=false offline_hf_hub_env={offline_mode} "
                f"error={exc.__class__.__name__}: {exc}"
            )
            raise BgeM3HybridProviderError(str(exc)) from exc

        load_source = "local_snapshot" if loaded_from_local_cache else "remote_repo_id"
        _emit_bge_m3_hybrid_log(
            "load start "
            f"provider_code={provider_code} model_name={model_name} "
            f"load_path={load_path} source={load_source} device={self.device} "
            f"cache_dir={resolved_cache_dir} offline_hf_hub_env={offline_mode} "
            f"snapshot_exists=true"
        )
        try:
            model = flag_model_class(load_path, **model_init_kwargs)
        except Exception as exc:  # pragma: no cover - exercised through higher-level failure tests
            _emit_bge_m3_hybrid_log(
                "load failed "
                f"provider_code={provider_code} model_name={model_name} load_path={load_path} "
                f"error={exc.__class__.__name__}: {exc}"
            )
            raise BgeM3HybridProviderError("BGE-M3 hybrid model load failed") from exc

        _emit_bge_m3_hybrid_memory_log(
            stage="after_model_load",
            provider_code=provider_code,
            model_name=model_name,
        )
        _emit_bge_m3_hybrid_log(
            "load success "
            f"provider_code={provider_code} model_name={model_name} "
            f"load_path={load_path} source={load_source} device={self.device} "
            f"cache_dir={resolved_cache_dir} offline_hf_hub_env={offline_mode}"
        )
        return model


def _import_bge_m3_flag_model_class():
    try:
        from FlagEmbedding import BGEM3FlagModel
    except ModuleNotFoundError as exc:
        raise BgeM3HybridProviderError(
            "FlagEmbedding is not installed in this environment"
        ) from exc
    except ImportError as exc:  # pragma: no cover - defensive import wrapper
        raise BgeM3HybridProviderError("FlagEmbedding import failed") from exc

    return BGEM3FlagModel


def _resolve_snapshot_revision(snapshot_path: str | None) -> str:
    if not snapshot_path:
        return "missing"
    return snapshot_path.rstrip("/").split("/")[-1]


def _resolve_bge_m3_cache_mode(provider_code: str) -> str:
    if provider_code == "bge_m3_dense_sparse_multivector":
        return "dense_sparse_multivector"
    return "dense_sparse"


def _cached_payload_matches_context(
    *,
    payload: CachedEmbeddingPayload,
    cache_context: _BgeM3CacheContext,
    input_type: str,
    expected_text_hash: str,
    require_multivector: bool,
) -> bool:
    if payload.cache_schema_version != "v1":
        return False
    if payload.provider_code != cache_context.provider_code:
        return False
    if payload.provider_model_name != cache_context.provider_model_name:
        return False
    if payload.snapshot_revision != cache_context.snapshot_revision:
        return False
    if payload.mode != cache_context.mode:
        return False
    if payload.input_type != input_type:
        return False
    if payload.dimension != cache_context.dimension:
        return False
    if payload.text_hash != expected_text_hash:
        return False
    if require_multivector and payload.multivector is None:
        return False
    return True


def _coerce_dense_vectors(raw_dense_vectors: Any) -> list[list[float]]:
    if hasattr(raw_dense_vectors, "tolist"):
        raw_dense_vectors = raw_dense_vectors.tolist()

    if isinstance(raw_dense_vectors, list) and raw_dense_vectors and isinstance(raw_dense_vectors[0], (int, float)):
        return [[float(value) for value in raw_dense_vectors]]
    if isinstance(raw_dense_vectors, list):
        return [[float(value) for value in vector] for vector in raw_dense_vectors]

    raise BgeM3HybridProviderError("BGE-M3 dense vector output is invalid")


def _coerce_sparse_vectors(raw_sparse_vectors: Any) -> list[dict[str, float]]:
    if isinstance(raw_sparse_vectors, dict):
        raw_sparse_vectors = [raw_sparse_vectors]
    if not isinstance(raw_sparse_vectors, list):
        raise BgeM3HybridProviderError("BGE-M3 sparse vector output is invalid")

    normalized_vectors: list[dict[str, float]] = []
    for item in raw_sparse_vectors:
        if not isinstance(item, dict):
            raise BgeM3HybridProviderError("BGE-M3 sparse vector output is invalid")
        normalized_vectors.append(
            {
                str(key): float(value)
                for key, value in item.items()
                if float(value) != 0.0
            }
        )
    return normalized_vectors


def _coerce_multivectors(raw_multivectors: Any) -> list[list[list[float]]]:
    if hasattr(raw_multivectors, "tolist"):
        raw_multivectors = raw_multivectors.tolist()
    if not isinstance(raw_multivectors, list):
        raise BgeM3HybridProviderError("BGE-M3 multivector output is invalid")

    normalized_vectors: list[list[list[float]]] = []
    for item in raw_multivectors:
        if hasattr(item, "tolist"):
            item = item.tolist()
        if not isinstance(item, list):
            raise BgeM3HybridProviderError("BGE-M3 multivector output is invalid")
        normalized_vectors.append(
            [
                [float(value) for value in token_vector]
                for token_vector in item
            ]
        )
    return normalized_vectors


class BgeM3HybridEmbeddingAdapter(BaseEmbeddingProvider):
    def __init__(
        self,
        *,
        device: str = "cpu",
        cache_dir: Path | None = None,
    ) -> None:
        self._hybrid_provider = BgeM3HybridEmbeddingProvider(
            device=device,
            cache_dir=cache_dir,
        )

    def embed_text(self, text: str, model_code: str) -> EmbeddingVector:
        return self.embed_passage(text, model_code)

    def embed_passage(self, text: str, model_code: str) -> EmbeddingVector:
        encoded = self._hybrid_provider.encode_passages([text], model_code)
        return self._build_embedding_vector(encoded=encoded, model_code=model_code)

    def embed_query(self, text: str, model_code: str) -> EmbeddingVector:
        encoded = self._hybrid_provider.encode_query(text, model_code)
        return self._build_embedding_vector(encoded=encoded, model_code=model_code)

    def embed_batch(self, texts: list[str], model_code: str) -> list[EmbeddingVector]:
        encoded = self._hybrid_provider.encode_passages(texts, model_code)
        return self._split_encoded_batch(encoded=encoded, texts=texts, model_code=model_code)

    def embed_query_batch(self, texts: list[str], model_code: str) -> list[EmbeddingVector]:
        """Task 65.11.1 - query-semantics counterpart of `embed_batch()`.

        One model invocation for all `texts`; never routes through
        `encode_passages()`.
        """

        encoded = self._hybrid_provider.encode_queries(texts, model_code)
        return self._split_encoded_batch(encoded=encoded, texts=texts, model_code=model_code)

    def _split_encoded_batch(
        self,
        *,
        encoded: BgeM3HybridEmbeddings,
        texts: list[str],
        model_code: str,
    ) -> list[EmbeddingVector]:
        vectors: list[EmbeddingVector] = []
        for index, _text in enumerate(texts):
            vectors.append(
                self._build_embedding_vector(
                    encoded=BgeM3HybridEmbeddings(
                        dense_vectors=[encoded.dense_vectors[index]],
                        sparse_vectors=[encoded.sparse_vectors[index]],
                        multivectors=None,
                    ),
                    model_code=model_code,
                )
            )
        return vectors

    def _build_embedding_vector(
        self,
        *,
        encoded: BgeM3HybridEmbeddings,
        model_code: str,
    ) -> EmbeddingVector:
        if not encoded.dense_vectors:
            raise BgeM3HybridProviderError("BGE-M3 hybrid embedding output is empty")

        model = get_embedding_model(model_code)
        dense_vector = [float(value) for value in encoded.dense_vectors[0]]
        sparse_vector = encoded.sparse_vectors[0] if encoded.sparse_vectors else {}
        if len(dense_vector) != model.dimension:
            raise BgeM3HybridProviderError("BGE-M3 dense vector dimension is invalid")

        return EmbeddingVector(
            values=dense_vector,
            dimension=len(dense_vector),
            metadata={
                "provider_name": BGE_M3_HYBRID_PROVIDER_NAME,
                "normalized_vectors": model.normalized_vectors,
                "supports_batching": model.supports_batching,
                "sparse_vector": sparse_vector,
            },
        )
