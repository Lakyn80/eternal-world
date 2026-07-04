"""Example custom adapter for client projects.

Copy this module into your project, implement the four RagEvalBackend methods,
then reference it from rag_eval.yaml:

backend: custom
adapter:
  module: my_project.rag_eval_adapter
  class: MyProjectRagEvalBackend
  kwargs:
    database_url: ${DATABASE_URL}
    qdrant_url: ${QDRANT_URL}
"""

from __future__ import annotations

from rag_eval.adapters.base import RagEvalBackend, RagEvalChunk, RagEvalRetrievalResponse, RagEvalRetrievalResult
from rag_eval.config import BenchmarkConfig


class MyProjectRagEvalBackend(RagEvalBackend):
    def __init__(self, *, config: BenchmarkConfig, database_url: str, qdrant_url: str) -> None:
        self._config = config
        self._database_url = database_url
        self._qdrant_url = qdrant_url

    def get_source_chunks(self, *, source_id: int) -> list[RagEvalChunk]:
        raise NotImplementedError("Load chunks from your DB and map chunk_metadata.source_document_id.")

    def embed_source(self, *, source_id: int, model_code: str) -> None:
        raise NotImplementedError("Embed all chunks for source_id using your embedding pipeline.")

    def index_source(
        self,
        *,
        source_id: int,
        model_code: str,
        collection_name: str,
    ) -> None:
        raise NotImplementedError("Upsert embeddings for source_id into your Qdrant collection.")

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
        raise NotImplementedError("Search Qdrant and return ranked chunk texts.")
        return RagEvalRetrievalResponse(results=[])
