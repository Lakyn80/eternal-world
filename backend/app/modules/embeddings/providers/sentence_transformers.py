from __future__ import annotations

import sys
from contextlib import contextmanager
from contextvars import ContextVar
from importlib import import_module
from pathlib import Path
from threading import Lock
from time import perf_counter
from typing import Any

from app.modules.embedding_models.registry import SENTENCE_TRANSFORMERS_ADAPTER
from app.modules.embedding_models.service import get_embedding_model
from app.modules.embeddings.providers.base import BaseEmbeddingProvider, EmbeddingVector


SENTENCE_TRANSFORMERS_PROVIDER_NAME = "sentence_transformers"
E5_SMALL_MODEL_NAME = "intfloat/multilingual-e5-small"
E5_BASE_MODEL_NAME = "intfloat/multilingual-e5-base"
E5_LARGE_MODEL_NAME = "intfloat/multilingual-e5-large"
BGE_M3_MODEL_NAME = "BAAI/bge-m3"
PARAPHRASE_MULTILINGUAL_MPNET_BASE_V2_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
QWEN3_EMBEDDING_0_6B_MODEL_NAME = "Qwen/Qwen3-Embedding-0.6B"
QWEN3_EMBEDDING_4B_MODEL_NAME = "Qwen/Qwen3-Embedding-4B"
QWEN3_EMBEDDING_8B_MODEL_NAME = "Qwen/Qwen3-Embedding-8B"
JINA_EMBEDDINGS_V3_MODEL_NAME = "jinaai/jina-embeddings-v3"
E5_PREFIXED_MODEL_CODES = {
    "multilingual_e5_small",
    "multilingual_e5_base",
    "multilingual_e5_large",
}
PLAIN_TEXT_MODEL_CODES = {
    "bge_m3",
    "paraphrase_multilingual_mpnet_base_v2",
    "qwen3_embedding_0_6b",
    "qwen3_embedding_4b",
    "qwen3_embedding_8b",
    "jina_embeddings_v3",
}
QUERY_PREFIX = "query: "
PASSAGE_PREFIX = "passage: "
SAFE_PROVIDER_FAILURE_MESSAGE = "SentenceTransformers embedding generation failed"

try:
    import resource
except ImportError:  # pragma: no cover - resource is unavailable on some local test hosts.
    resource = None


class SentenceTransformersProviderError(Exception):
    pass


_shared_model_cache_enabled: ContextVar[bool] = ContextVar(
    "sentence_transformers_shared_model_cache_enabled",
    default=False,
)
_shared_models: dict[tuple[object, ...], Any] = {}
_shared_models_lock = Lock()


def _emit_sentence_transformers_log(message: str) -> None:
    print(f"[sentence_transformers] {message}", flush=True)


def _get_process_rss_mb() -> float | None:
    if resource is None:
        return None

    rss_value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss_value <= 0:
        return None

    if sys.platform == "darwin":
        return round(rss_value / (1024 * 1024), 2)

    return round(rss_value / 1024, 2)


def _emit_sentence_transformers_memory_log(*, stage: str, model_code: str, model_name: str) -> None:
    rss_mb = _get_process_rss_mb()
    if rss_mb is None:
        return

    _emit_sentence_transformers_log(
        f"memory stage={stage} model_code={model_code} model_name={model_name} rss_mb={rss_mb}"
    )


@contextmanager
def enable_sentence_transformers_shared_model_cache(*, clear_on_exit: bool = False):
    token = _shared_model_cache_enabled.set(True)
    try:
        yield
    finally:
        _shared_model_cache_enabled.reset(token)
        if clear_on_exit:
            clear_sentence_transformers_shared_model_cache()


def clear_sentence_transformers_shared_model_cache() -> None:
    with _shared_models_lock:
        _shared_models.clear()


class SentenceTransformersEmbeddingProvider(BaseEmbeddingProvider):
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

    def embed_text(self, text: str, model_code: str) -> EmbeddingVector:
        return self.embed_passage(text, model_code)

    def embed_batch(self, texts: list[str], model_code: str) -> list[EmbeddingVector]:
        prepared_texts = [
            self._prepare_text(text, model_code=model_code, input_type="passage")
            for text in texts
        ]
        return self._encode(
            prepared_texts,
            model_code=model_code,
            input_type="passage",
        )

    def embed_query(self, text: str, model_code: str) -> EmbeddingVector:
        return self._encode(
            [self._prepare_text(text, model_code=model_code, input_type="query")],
            model_code=model_code,
            input_type="query",
        )[0]

    def embed_passage(self, text: str, model_code: str) -> EmbeddingVector:
        return self._encode(
            [self._prepare_text(text, model_code=model_code, input_type="passage")],
            model_code=model_code,
            input_type="passage",
        )[0]

    def _prepare_text(
        self,
        text: str,
        *,
        model_code: str,
        input_type: str,
    ) -> str:
        normalized_text = self._normalize_text(text)
        normalized_model_code = model_code.strip().lower()
        if normalized_model_code in E5_PREFIXED_MODEL_CODES:
            if input_type == "query":
                return f"{QUERY_PREFIX}{normalized_text}"
            return f"{PASSAGE_PREFIX}{normalized_text}"
        if normalized_model_code in PLAIN_TEXT_MODEL_CODES:
            return normalized_text

        raise SentenceTransformersProviderError(
            "SentenceTransformers model input format is not configured"
        )

    def _normalize_text(self, text: str) -> str:
        normalized_text = " ".join(text.split())
        if not normalized_text:
            raise SentenceTransformersProviderError("Embedding input text must not be empty")

        return normalized_text

    def _get_or_load_model(self, model_code: str):
        normalized_model_code = model_code.strip().lower()
        if normalized_model_code in self._models:
            _emit_sentence_transformers_log(f"cache hit scope=provider model_code={normalized_model_code}")
            return self._models[normalized_model_code]

        with self._lock:
            if normalized_model_code in self._models:
                _emit_sentence_transformers_log(f"cache hit scope=provider model_code={normalized_model_code}")
                return self._models[normalized_model_code]

            sentence_transformer_class = self._load_sentence_transformer_class()
            model_name = self._resolve_model_name(normalized_model_code)
            model_init_kwargs = self._build_model_init_kwargs(normalized_model_code)
            cache_key = self._build_shared_model_cache_key(
                model_code=normalized_model_code,
                model_name=model_name,
                model_init_kwargs=model_init_kwargs,
            )

            if _shared_model_cache_enabled.get():
                with _shared_models_lock:
                    shared_model = _shared_models.get(cache_key)
                    if shared_model is not None:
                        self._models[normalized_model_code] = shared_model
                        _emit_sentence_transformers_log(
                            "cache hit scope=shared "
                            f"model_code={normalized_model_code} model_name={model_name} device={self.device}"
                        )
                        return shared_model

                    model = self._load_model_instance(
                        sentence_transformer_class=sentence_transformer_class,
                        model_code=normalized_model_code,
                        model_name=model_name,
                        model_init_kwargs=model_init_kwargs,
                    )
                    _shared_models[cache_key] = model
            else:
                model = self._load_model_instance(
                    sentence_transformer_class=sentence_transformer_class,
                    model_code=normalized_model_code,
                    model_name=model_name,
                    model_init_kwargs=model_init_kwargs,
                )

            self._models[normalized_model_code] = model
            return model

    def _load_sentence_transformer_class(self):
        try:
            module = import_module("sentence_transformers")
            return getattr(module, "SentenceTransformer")
        except ModuleNotFoundError as exc:
            raise SentenceTransformersProviderError(
                "SentenceTransformers dependency is not installed"
            ) from exc
        except AttributeError as exc:
            raise SentenceTransformersProviderError(
                "SentenceTransformers dependency is invalid"
            ) from exc

    def _resolve_model_name(self, model_code: str) -> str:
        model_definition = get_embedding_model(model_code)
        if (
            model_definition.runtime_adapter != SENTENCE_TRANSFORMERS_ADAPTER
            or model_definition.provider_model_name is None
        ):
            raise SentenceTransformersProviderError("SentenceTransformers model is not configured")

        return model_definition.provider_model_name

    def _encode(
        self,
        texts: list[str],
        *,
        model_code: str,
        input_type: str,
    ) -> list[EmbeddingVector]:
        if not texts:
            return []

        model_definition = get_embedding_model(model_code)
        model = self._get_or_load_model(model_definition.code)
        _emit_sentence_transformers_log(
            "encode start "
            f"model_code={model_definition.code} input_type={input_type} batch_size={len(texts)}"
        )
        started_at = perf_counter()
        try:
            raw_vectors = model.encode(
                texts,
                convert_to_numpy=True,
                normalize_embeddings=model_definition.normalized_vectors,
                show_progress_bar=False,
            )
        except Exception as exc:
            _emit_sentence_transformers_log(
                "encode failed "
                f"model_code={model_definition.code} input_type={input_type} "
                f"batch_size={len(texts)} error={exc.__class__.__name__}: {exc}"
            )
            raise SentenceTransformersProviderError(SAFE_PROVIDER_FAILURE_MESSAGE) from exc
        _emit_sentence_transformers_log(
            "encode done "
            f"model_code={model_definition.code} input_type={input_type} "
            f"batch_size={len(texts)} duration_ms={round((perf_counter() - started_at) * 1000, 2)}"
        )

        vectors = self._coerce_vectors(raw_vectors)
        embedding_vectors: list[EmbeddingVector] = []
        for prepared_text, values in zip(texts, vectors, strict=True):
            if len(values) != model_definition.dimension:
                raise SentenceTransformersProviderError(
                    "SentenceTransformers embedding dimension is invalid"
                )
            input_prefix = self._resolve_input_prefix(
                model_code=model_definition.code,
                input_type=input_type,
            )

            embedding_vectors.append(
                EmbeddingVector(
                    values=[float(value) for value in values],
                    dimension=len(values),
                    metadata={
                        "provider_name": SENTENCE_TRANSFORMERS_PROVIDER_NAME,
                        "provider_model_name": self._resolve_model_name(model_definition.code),
                        "input_type": input_type,
                        "input_prefix": input_prefix,
                        "prepared_text_char_count": len(prepared_text),
                        "normalized_vectors": model_definition.normalized_vectors,
                        "supports_batching": model_definition.supports_batching,
                        "device": self.device,
                    },
                )
            )

        return embedding_vectors

    def _coerce_vectors(self, raw_vectors: Any) -> list[list[float]]:
        if hasattr(raw_vectors, "tolist"):
            raw_vectors = raw_vectors.tolist()

        if isinstance(raw_vectors, list) and raw_vectors and isinstance(raw_vectors[0], (int, float)):
            return [[float(value) for value in raw_vectors]]

        if isinstance(raw_vectors, list):
            return [
                [float(value) for value in vector]
                for vector in raw_vectors
            ]

        raise SentenceTransformersProviderError(
            "SentenceTransformers embedding output is invalid"
        )

    def _resolve_input_prefix(
        self,
        *,
        model_code: str,
        input_type: str,
    ) -> str | None:
        normalized_model_code = model_code.strip().lower()
        if normalized_model_code in E5_PREFIXED_MODEL_CODES:
            return QUERY_PREFIX.strip() if input_type == "query" else PASSAGE_PREFIX.strip()
        if normalized_model_code in PLAIN_TEXT_MODEL_CODES:
            return None

        raise SentenceTransformersProviderError(
            "SentenceTransformers model input format is not configured"
        )

    def _build_model_init_kwargs(self, model_code: str) -> dict[str, object]:
        if model_code == "jina_embeddings_v3":
            return {"trust_remote_code": True}

        return {}

    def _build_shared_model_cache_key(
        self,
        *,
        model_code: str,
        model_name: str,
        model_init_kwargs: dict[str, object],
    ) -> tuple[object, ...]:
        frozen_kwargs = tuple(
            sorted((key, repr(value)) for key, value in model_init_kwargs.items())
        )
        return (
            SENTENCE_TRANSFORMERS_PROVIDER_NAME,
            model_code,
            model_name,
            self.device,
            self.cache_dir,
            frozen_kwargs,
        )

    def _load_model_instance(
        self,
        *,
        sentence_transformer_class,
        model_code: str,
        model_name: str,
        model_init_kwargs: dict[str, object],
    ):
        _emit_sentence_transformers_memory_log(
            stage="before_model_load",
            model_code=model_code,
            model_name=model_name,
        )
        _emit_sentence_transformers_log(
            f"load start model_code={model_code} model_name={model_name} device={self.device}"
        )
        try:
            model = sentence_transformer_class(
                model_name,
                device=self.device,
                cache_folder=self.cache_dir,
                **model_init_kwargs,
            )
        except Exception as exc:
            _emit_sentence_transformers_log(
                "load failed "
                f"model_code={model_code} model_name={model_name} "
                f"error={exc.__class__.__name__}: {exc}"
            )
            raise

        _emit_sentence_transformers_memory_log(
            stage="after_model_load",
            model_code=model_code,
            model_name=model_name,
        )
        _emit_sentence_transformers_log(
            f"load success model_code={model_code} model_name={model_name} device={self.device}"
        )
        return model
