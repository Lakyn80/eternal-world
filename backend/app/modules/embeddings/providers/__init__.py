from __future__ import annotations

from app.core.config import settings
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

    if (
        normalized_model_code in {
            "multilingual_e5_small",
            "bge_m3",
            "paraphrase_multilingual_mpnet_base_v2",
        }
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
