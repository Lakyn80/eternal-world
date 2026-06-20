from __future__ import annotations

import hashlib
import math

from app.modules.embedding_models.service import get_embedding_model
from app.modules.embeddings.providers.base import BaseEmbeddingProvider, EmbeddingVector


class MockEmbeddingProvider(BaseEmbeddingProvider):
    def embed_text(self, text: str, model_code: str) -> EmbeddingVector:
        model = get_embedding_model(model_code)
        values = _build_deterministic_vector(
            text=text,
            model_code=model.code,
            dimension=model.dimension,
            normalized_vectors=model.normalized_vectors,
        )
        return EmbeddingVector(
            values=values,
            dimension=len(values),
            metadata={
                "provider_name": "mock",
                "normalized_vectors": model.normalized_vectors,
                "supports_batching": model.supports_batching,
            },
        )

    def embed_batch(self, texts: list[str], model_code: str) -> list[EmbeddingVector]:
        return [self.embed_text(text, model_code) for text in texts]


def _build_deterministic_vector(
    *,
    text: str,
    model_code: str,
    dimension: int,
    normalized_vectors: bool,
) -> list[float]:
    values: list[float] = []
    seed_prefix = f"{model_code}:{text}".encode("utf-8")
    counter = 0
    while len(values) < dimension:
        digest = hashlib.sha256(seed_prefix + counter.to_bytes(4, byteorder="big", signed=False)).digest()
        for byte_value in digest:
            scaled_value = round((byte_value / 127.5) - 1.0, 6)
            values.append(scaled_value)
            if len(values) == dimension:
                break
        counter += 1

    if normalized_vectors:
        norm = math.sqrt(sum(value * value for value in values))
        if norm > 0:
            values = [round(value / norm, 6) for value in values]

    return values
