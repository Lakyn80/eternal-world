from __future__ import annotations

from rag_eval.adapters.base import RagEvalBackend, RagEvalChunk, RagEvalRetrievalResponse, RagEvalRetrievalResult
from rag_eval.metrics.metrics import marker_present


class MemoryRagEvalBackend(RagEvalBackend):
    """Deterministic in-memory backend for fast tests without DB or Qdrant."""

    def __init__(
        self,
        *,
        source_chunks: list[RagEvalChunk],
        profile_id: int = 1,
    ) -> None:
        self._source_chunks = list(source_chunks)
        self._profile_id = profile_id
        self._indexed_collections: dict[tuple[int, str, str], list[tuple[RagEvalChunk, float]]] = {}

    def get_source_chunks(self, *, source_id: int) -> list[RagEvalChunk]:
        return [chunk for chunk in self._source_chunks if chunk.source_id in {None, source_id}]

    def embed_source(self, *, source_id: int, model_code: str) -> None:
        return None

    def index_source(
        self,
        *,
        source_id: int,
        model_code: str,
        collection_name: str,
    ) -> None:
        chunks = self.get_source_chunks(source_id=source_id)
        indexed: list[tuple[RagEvalChunk, float]] = []
        for chunk in chunks:
            score_seed = sum(ord(character) for character in f"{model_code}:{chunk.chunk_id}")
            indexed.append((chunk, float(score_seed % 1000) / 1000.0))
        self._indexed_collections[(source_id, model_code, collection_name)] = indexed

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
        indexed = self._indexed_collections.get((source_id, model_code, collection_name), [])
        scored_results: list[tuple[RagEvalChunk, float]] = []
        for chunk, base_score in indexed:
            overlap = sum(1 for token in query.lower().split() if marker_present(chunk.chunk_text, token))
            score = base_score + overlap
            if score_threshold is not None and score < score_threshold:
                continue
            scored_results.append((chunk, score))

        scored_results.sort(key=lambda item: item[1], reverse=True)
        results = [
            RagEvalRetrievalResult(
                chunk_id=chunk.chunk_id,
                source_id=chunk.source_id,
                score=score,
                text=chunk.chunk_text,
                qdrant_collection=collection_name,
                payload_metadata=dict(chunk.chunk_metadata),
            )
            for chunk, score in scored_results[:top_k]
        ]
        return RagEvalRetrievalResponse(results=results)
