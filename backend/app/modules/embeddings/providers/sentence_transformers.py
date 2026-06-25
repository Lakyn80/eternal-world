from __future__ import annotations

from importlib import import_module
from pathlib import Path
from threading import Lock
from typing import Any

from app.modules.embedding_models.service import get_embedding_model
from app.modules.embeddings.providers.base import BaseEmbeddingProvider, EmbeddingVector


SENTENCE_TRANSFORMERS_PROVIDER_NAME = "sentence_transformers"
E5_SMALL_MODEL_NAME = "intfloat/multilingual-e5-small"
BGE_M3_MODEL_NAME = "BAAI/bge-m3"
QUERY_PREFIX = "query: "
PASSAGE_PREFIX = "passage: "
SAFE_PROVIDER_FAILURE_MESSAGE = "SentenceTransformers embedding generation failed"


class SentenceTransformersProviderError(Exception):
    pass


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
        if normalized_model_code == "multilingual_e5_small":
            if input_type == "query":
                return f"{QUERY_PREFIX}{normalized_text}"
            return f"{PASSAGE_PREFIX}{normalized_text}"
        if normalized_model_code == "bge_m3":
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
            return self._models[normalized_model_code]

        with self._lock:
            if normalized_model_code in self._models:
                return self._models[normalized_model_code]

            sentence_transformer_class = self._load_sentence_transformer_class()
            model_name = self._resolve_model_name(normalized_model_code)
            model = sentence_transformer_class(
                model_name,
                device=self.device,
                cache_folder=self.cache_dir,
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
        if model_code == "multilingual_e5_small":
            return E5_SMALL_MODEL_NAME
        if model_code == "bge_m3":
            return BGE_M3_MODEL_NAME

        raise SentenceTransformersProviderError("SentenceTransformers model is not configured")

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
        try:
            raw_vectors = model.encode(
                texts,
                convert_to_numpy=True,
                normalize_embeddings=model_definition.normalized_vectors,
                show_progress_bar=False,
            )
        except Exception as exc:
            raise SentenceTransformersProviderError(SAFE_PROVIDER_FAILURE_MESSAGE) from exc

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
        if normalized_model_code == "multilingual_e5_small":
            return QUERY_PREFIX.strip() if input_type == "query" else PASSAGE_PREFIX.strip()
        if normalized_model_code == "bge_m3":
            return None

        raise SentenceTransformersProviderError(
            "SentenceTransformers model input format is not configured"
        )
