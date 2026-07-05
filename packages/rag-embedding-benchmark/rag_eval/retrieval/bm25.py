from __future__ import annotations

import re
from typing import TYPE_CHECKING

from rag_eval.adapters.base import RagEvalChunk, RagEvalRetrievalResponse, RagEvalRetrievalResult

if TYPE_CHECKING:
    from rag_eval.config import BenchmarkRetrievalConfig


BM25_MODEL_CODE = "bm25"

LEGAL_TOKEN_PATTERN = re.compile(
    r"[0-9]+/[0-9]+(?:\s*sb\.)?|§\s*[0-9]+(?:/[0-9]+)?|[a-zà-žá-úý-ýč-žš-ž0-9]+",
    re.UNICODE,
)


def require_bm25s():
    try:
        import bm25s
    except ImportError as exc:
        raise ImportError(
            "BM25 retrieval requires the optional 'bm25' extra. "
            "Install with: pip install 'rag-embedding-benchmark[bm25]'"
        ) from exc
    return bm25s


def tokenize_legal_text(text: str) -> list[str]:
    """Tokenize Czech/legal text while preserving section numbers and statute refs."""
    normalized_text = " ".join(text.split()).lower()
    tokens = LEGAL_TOKEN_PATTERN.findall(normalized_text)
    return [token for token in tokens if token.strip()]


def legal_text_to_bm25_input(text: str) -> str:
    tokens = tokenize_legal_text(text)
    return " ".join(tokens) if tokens else text.strip().lower()


class Bm25IndexStore:
    """Build BM25 indexes once per source_id and reuse for the benchmark run."""

    def __init__(self, *, retrieval_config: BenchmarkRetrievalConfig) -> None:
        self._retrieval_config = retrieval_config
        self._indexes: dict[int, Bm25ChunkIndex] = {}

    def get_index(self, *, source_id: int, chunks: list[RagEvalChunk]) -> Bm25ChunkIndex:
        if source_id not in self._indexes:
            self._indexes[source_id] = Bm25ChunkIndex(
                chunks=chunks,
                retrieval_config=self._retrieval_config,
            )
        return self._indexes[source_id]


class Bm25ChunkIndex:
    """In-memory BM25 index built from benchmark chunks."""

    def __init__(
        self,
        *,
        chunks: list[RagEvalChunk],
        retrieval_config: BenchmarkRetrievalConfig,
    ) -> None:
        bm25s = require_bm25s()

        self._chunks = list(chunks)
        self._retrieval_config = retrieval_config
        corpus = [legal_text_to_bm25_input(chunk.chunk_text) for chunk in self._chunks]
        corpus_tokens = bm25s.tokenize(corpus)
        self._retriever = bm25s.BM25(
            k1=retrieval_config.bm25_k1,
            b=retrieval_config.bm25_b,
        )
        self._retriever.index(corpus_tokens)

    def retrieve(
        self,
        *,
        query: str,
        source_id: int,
        top_k: int,
        collection_name: str,
    ) -> RagEvalRetrievalResponse:
        bm25s = require_bm25s()

        if not self._chunks:
            return RagEvalRetrievalResponse(results=[])

        query_tokens = bm25s.tokenize([legal_text_to_bm25_input(query)])
        doc_indices, scores = self._retriever.retrieve(
            query_tokens,
            k=min(top_k, len(self._chunks)),
        )

        results: list[RagEvalRetrievalResult] = []
        for rank in range(doc_indices.shape[1]):
            doc_index = int(doc_indices[0, rank])
            if doc_index < 0 or doc_index >= len(self._chunks):
                continue
            chunk = self._chunks[doc_index]
            results.append(
                RagEvalRetrievalResult(
                    chunk_id=chunk.chunk_id,
                    source_id=chunk.source_id or source_id,
                    score=float(scores[0, rank]),
                    text=chunk.chunk_text,
                    qdrant_collection=collection_name,
                    payload_metadata={
                        **dict(chunk.chunk_metadata),
                        "retrieval_mode": "bm25",
                    },
                )
            )

        return RagEvalRetrievalResponse(results=results)
