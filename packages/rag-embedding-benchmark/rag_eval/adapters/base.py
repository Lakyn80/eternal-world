from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable


@dataclass(frozen=True)
class RagEvalChunk:
    chunk_id: int
    chunk_text: str
    source_id: int | None = None
    chunk_metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RagEvalRetrievalResult:
    chunk_id: int | None
    source_id: int | None
    score: float
    text: str
    embedding_id: int | None = None
    language: str | None = None
    source_type: str | None = None
    validation_status: str | None = None
    text_hash: str | None = None
    qdrant_collection: str | None = None
    payload_metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RagEvalRetrievalResponse:
    results: list[RagEvalRetrievalResult] = field(default_factory=list)


@runtime_checkable
class RagEvalBackend(Protocol):
    def get_source_chunks(self, *, source_id: int) -> list[RagEvalChunk]:
        ...

    def embed_source(self, *, source_id: int, model_code: str) -> None:
        ...

    def index_source(
        self,
        *,
        source_id: int,
        model_code: str,
        collection_name: str,
    ) -> None:
        ...

    def retrieve(
        self,
        *,
        profile_id: int,
        source_id: int,
        query: str,
        model_code: str,
        collection_name: str,
        top_k: int,
        score_threshold: float | None = None,
    ) -> RagEvalRetrievalResponse:
        ...
