from __future__ import annotations

import sys
from contextlib import contextmanager
from contextvars import ContextVar
from pathlib import Path
from threading import Lock
from time import perf_counter
from typing import Any

from app.modules.embedding_models.service import get_embedding_model


BGE_M3_HYBRID_PROVIDER_NAME = "bge_m3_hybrid"
BGE_M3_SHARED_MODEL_FAMILY = "bge_m3_full_hybrid_runtime"
SAFE_BGE_M3_HYBRID_FAILURE_MESSAGE = "BGE-M3 hybrid embedding generation failed"

try:
    import resource
except ImportError:  # pragma: no cover - resource is unavailable on some local test hosts.
    resource = None


class BgeM3HybridProviderError(Exception):
    pass


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
        self._lock = Lock()

    def encode_query(self, text: str, provider_code: str) -> BgeM3HybridEmbeddings:
        return self.encode_texts([text], provider_code=provider_code, input_type="query")

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
        model_definition = get_embedding_model(normalized_provider_code)
        return_colbert_vecs = normalized_provider_code == "bge_m3_dense_sparse_multivector"
        batch_size = max(1, min(8, len(texts)))

        _emit_bge_m3_hybrid_log(
            "dense encode start "
            f"provider_code={normalized_provider_code} input_type={input_type} batch_size={len(texts)}"
        )
        _emit_bge_m3_hybrid_log(
            "sparse encode start "
            f"provider_code={normalized_provider_code} input_type={input_type} batch_size={len(texts)}"
        )
        if return_colbert_vecs:
            _emit_bge_m3_hybrid_log(
                "multivector encode start "
                f"provider_code={normalized_provider_code} input_type={input_type} batch_size={len(texts)}"
            )

        started_at = perf_counter()
        try:
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
                f"provider_code={normalized_provider_code} input_type={input_type} "
                f"batch_size={len(texts)} error={exc.__class__.__name__}: {exc}"
            )
            raise BgeM3HybridProviderError(SAFE_BGE_M3_HYBRID_FAILURE_MESSAGE) from exc

        duration_ms = round((perf_counter() - started_at) * 1000, 2)
        _emit_bge_m3_hybrid_log(
            "dense encode done "
            f"provider_code={normalized_provider_code} input_type={input_type} "
            f"batch_size={len(texts)} duration_ms={duration_ms}"
        )
        _emit_bge_m3_hybrid_log(
            "sparse encode done "
            f"provider_code={normalized_provider_code} input_type={input_type} "
            f"batch_size={len(texts)} duration_ms={duration_ms}"
        )
        if return_colbert_vecs:
            _emit_bge_m3_hybrid_log(
                "multivector encode done "
                f"provider_code={normalized_provider_code} input_type={input_type} "
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
            else:
                model = self._load_model_instance(
                    flag_model_class=flag_model_class,
                    provider_code=provider_code,
                    model_name=model_name,
                    model_init_kwargs=model_init_kwargs,
                )

            self._models[provider_code] = model
            return model

    def _build_model_init_kwargs(self) -> dict[str, object]:
        return {"use_fp16": False}

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
        _emit_bge_m3_hybrid_log(
            f"load start provider_code={provider_code} model_name={model_name} device={self.device}"
        )
        try:
            model = flag_model_class(model_name, **model_init_kwargs)
        except Exception as exc:  # pragma: no cover - exercised through higher-level failure tests
            _emit_bge_m3_hybrid_log(
                "load failed "
                f"provider_code={provider_code} model_name={model_name} "
                f"error={exc.__class__.__name__}: {exc}"
            )
            raise BgeM3HybridProviderError("BGE-M3 hybrid model load failed") from exc

        _emit_bge_m3_hybrid_memory_log(
            stage="after_model_load",
            provider_code=provider_code,
            model_name=model_name,
        )
        _emit_bge_m3_hybrid_log(
            f"load success provider_code={provider_code} model_name={model_name} device={self.device}"
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

