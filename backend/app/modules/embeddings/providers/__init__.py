from __future__ import annotations

from app.core.config import settings
from app.modules.embedding_models.registry import (
    BGE_M3_HYBRID_ADAPTER,
    SENTENCE_TRANSFORMERS_ADAPTER,
    get_embedding_model_definition,
)
from app.modules.embeddings.providers.base import BaseEmbeddingProvider
from app.modules.embeddings.providers.mock import MockEmbeddingProvider
from app.modules.embeddings.providers.sentence_transformers import (
    SENTENCE_TRANSFORMERS_PROVIDER_NAME,
    SentenceTransformersEmbeddingProvider,
)


MOCK_PROVIDER_NAME = "mock"


def build_embedding_provider(*, model_code: str) -> BaseEmbeddingProvider:
    normalized_model_code = model_code.strip().lower()
    if normalized_model_code == "mock_embedding":
        return MockEmbeddingProvider()

    model_definition = get_embedding_model_definition(normalized_model_code)
    if (
        model_definition is not None
        and model_definition.runtime_adapter == BGE_M3_HYBRID_ADAPTER
    ):
        return MockEmbeddingProvider()

    if (
        model_definition is not None
        and model_definition.runtime_adapter == SENTENCE_TRANSFORMERS_ADAPTER
        and settings.embedding_provider == SENTENCE_TRANSFORMERS_PROVIDER_NAME
    ):
        return SentenceTransformersEmbeddingProvider(
            device=settings.sentence_transformers_device,
            cache_dir=settings.sentence_transformers_cache_dir,
        )

    return MockEmbeddingProvider()


__all__ = [
    "MOCK_PROVIDER_NAME",
    "SENTENCE_TRANSFORMERS_PROVIDER_NAME",
    "SentenceTransformersEmbeddingProvider",
    "build_embedding_provider",
]
