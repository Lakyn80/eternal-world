from __future__ import annotations

from rag_eval.adapters.base import RagEvalBackend, RagEvalChunk, RagEvalRetrievalResponse, RagEvalRetrievalResult
from rag_eval.config import BenchmarkRetrievalConfig
from rag_eval.metrics.metrics import marker_present
from rag_eval.retrieval.bm25 import Bm25IndexStore
from rag_eval.retrieval.fusion import reciprocal_rank_fusion


class MemoryRagEvalBackend(RagEvalBackend):
    """Deterministic in-memory backend for fast tests without DB or Qdrant."""

    def __init__(
        self,
        *,
        source_chunks: list[RagEvalChunk],
        profile_id: int = 1,
        retrieval_config: BenchmarkRetrievalConfig | None = None,
    ) -> None:
        from rag_eval.config import BenchmarkRetrievalConfig as DefaultRetrievalConfig

        self._source_chunks = list(source_chunks)
        self._profile_id = profile_id
        self._retrieval_config = retrieval_config or DefaultRetrievalConfig()
        self._indexed_collections: dict[tuple[int, str, str], list[tuple[RagEvalChunk, float]]] = {}
        self._bm25_store = Bm25IndexStore(retrieval_config=self._retrieval_config)

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

    def _retrieve_dense(
        self,
        *,
        source_id: int,
        query: str,
        model_code: str,
        collection_name: str,
        top_k: int,
        score_threshold: float | None,
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

    def _retrieve_bm25(
        self,
        *,
        source_id: int,
        query: str,
        collection_name: str,
        top_k: int,
    ) -> RagEvalRetrievalResponse:
        chunks = self.get_source_chunks(source_id=source_id)
        index = self._bm25_store.get_index(source_id=source_id, chunks=chunks)
        return index.retrieve(
            query=query,
            source_id=source_id,
            top_k=top_k,
            collection_name=collection_name,
        )

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
        retrieval_mode: str = "dense",
    ) -> RagEvalRetrievalResponse:
        if retrieval_mode == "bm25":
            return self._retrieve_bm25(
                source_id=source_id,
                query=query,
                collection_name=collection_name,
                top_k=top_k,
            )

        dense_response = self._retrieve_dense(
            source_id=source_id,
            query=query,
            model_code=model_code,
            collection_name=collection_name,
            top_k=top_k,
            score_threshold=score_threshold,
        )

        if retrieval_mode == "dense":
            return dense_response

        if retrieval_mode == "dense_plus_bm25":
            bm25_response = self._retrieve_bm25(
                source_id=source_id,
                query=query,
                collection_name=collection_name,
                top_k=top_k,
            )
            return reciprocal_rank_fusion(
                [dense_response.results, bm25_response.results],
                top_k=top_k,
                rrf_k=self._retrieval_config.rrf_k,
            )

        raise ValueError(f"Unsupported retrieval_mode: {retrieval_mode}")
