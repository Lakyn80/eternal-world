from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class EmbeddingVector:
    values: list[float]
    dimension: int
    metadata: dict[str, Any]


class BaseEmbeddingProvider(ABC):
    @abstractmethod
    def embed_text(self, text: str, model_code: str) -> EmbeddingVector:
        raise NotImplementedError

    @abstractmethod
    def embed_batch(self, texts: list[str], model_code: str) -> list[EmbeddingVector]:
        raise NotImplementedError

    def embed_query(self, text: str, model_code: str) -> EmbeddingVector:
        return self.embed_text(text, model_code)

    def embed_passage(self, text: str, model_code: str) -> EmbeddingVector:
        return self.embed_text(text, model_code)

    def embed_query_batch(self, texts: list[str], model_code: str) -> list[EmbeddingVector]:
        """Task 65.11.1 - deliberately a *separate* entry point from
        `embed_batch()`.

        `embed_batch()` is passage-oriented (see `BgeM3HybridEmbeddingAdapter`
        and the E5 `passage: ` prefixing in the SentenceTransformers
        provider); reusing it for queries would silently encode query text
        with passage semantics and degrade retrieval quality. This default
        implementation is correct but unbatched - providers that can encode
        several query texts in one model invocation must override it (the
        real BGE-M3 hybrid adapter does).
        """

        return [self.embed_query(text, model_code) for text in texts]
