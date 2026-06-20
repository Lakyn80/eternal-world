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
