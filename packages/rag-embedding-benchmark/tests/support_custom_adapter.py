from __future__ import annotations

from rag_eval.adapters.base import RagEvalBackend, RagEvalChunk, RagEvalRetrievalResponse


class SupportCustomAdapter(RagEvalBackend):
    def __init__(self, *, label: str = "support", config=None) -> None:
        self.label = label
        self.config = config

    def get_source_chunks(self, *, source_id: int) -> list[RagEvalChunk]:
        return []

    def embed_source(self, *, source_id: int, model_code: str) -> None:
        return None

    def index_source(
        self,
        *,
        source_id: int,
        model_code: str,
        collection_name: str,
    ) -> None:
        return None

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
        return RagEvalRetrievalResponse(results=[])
