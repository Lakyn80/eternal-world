from __future__ import annotations

from contextlib import contextmanager

from rag_eval.adapters.base import RagEvalBackend, RagEvalChunk, RagEvalRetrievalResponse, RagEvalRetrievalResult
from rag_eval.config import BenchmarkConfig
from rag_eval.retrieval.bm25 import Bm25IndexStore
from rag_eval.retrieval.fusion import reciprocal_rank_fusion


class EternalWorldRagEvalBackend(RagEvalBackend):
    """Adapter that delegates to the Eternal World backend application stack."""

    def __init__(
        self,
        *,
        config: BenchmarkConfig,
        backend_root: str | None = None,
    ) -> None:
        self._config = config
        self._backend_root = backend_root
        self._session = None
        self._user = None
        self._bm25_store = Bm25IndexStore(retrieval_config=config.retrieval)

    @contextmanager
    def session(self):
        db = self._open_session()
        try:
            yield db
        finally:
            db.close()

    def _ensure_backend_imports(self):
        import sys
        from pathlib import Path

        if self._backend_root:
            backend_path = Path(self._backend_root).resolve()
        else:
            backend_path = Path(__file__).resolve().parents[4] / "backend"
        backend_str = str(backend_path)
        if backend_str not in sys.path:
            sys.path.insert(0, backend_str)

    def _open_session(self):
        self._ensure_backend_imports()
        from app.db.session import SessionLocal

        return SessionLocal()

    def _resolve_user(self, db):
        if self._user is not None:
            return self._user
        from app.modules.users.repository import get_user_by_email

        user = get_user_by_email(db, email=self._config.user_email)
        if user is None:
            raise ValueError(f"User not found for email: {self._config.user_email}")
        self._user = user
        return user

    def get_source_chunks(self, *, source_id: int) -> list[RagEvalChunk]:
        with self.session() as db:
            user = self._resolve_user(db)
            from app.modules.rag_chunks.service import list_rag_chunks

            chunks = list_rag_chunks(db, current_user=user, source_id=source_id)
            return [
                RagEvalChunk(
                    chunk_id=chunk.id,
                    chunk_text=str(chunk.chunk_text or ""),
                    source_id=chunk.source_id,
                    chunk_metadata=dict(chunk.chunk_metadata or {}),
                )
                for chunk in chunks
                if chunk.validation_status != "invalid"
            ]

    def embed_source(self, *, source_id: int, model_code: str) -> None:
        with self.session() as db:
            user = self._resolve_user(db)
            from app.modules.embeddings.service import embed_source_chunks

            embed_source_chunks(
                db,
                current_user=user,
                source_id=source_id,
                model_code=model_code,
            )

    def index_source(
        self,
        *,
        source_id: int,
        model_code: str,
        collection_name: str,
    ) -> None:
        with self.session() as db:
            user = self._resolve_user(db)
            from app.modules.qdrant_indexing.service import index_source_embeddings

            index_source_embeddings(
                db,
                current_user=user,
                source_id=source_id,
                model_code=model_code,
                collection_name=collection_name,
            )

    def _retrieve_dense(
        self,
        *,
        profile_id: int,
        source_id: int,
        query: str,
        model_code: str,
        collection_name: str,
        top_k: int,
        score_threshold: float | None,
    ) -> RagEvalRetrievalResponse:
        with self.session() as db:
            user = self._resolve_user(db)
            from app.modules.rag_retrieval.schemas import RagRetrievalRequest
            from app.modules.rag_retrieval.service import retrieve_profile_rag_for_collection

            retrieval_response = retrieve_profile_rag_for_collection(
                db,
                current_user=user,
                profile_id=profile_id,
                payload=RagRetrievalRequest(
                    query=query,
                    model_code=model_code,
                    limit=top_k,
                    score_threshold=score_threshold,
                ),
                collection_name=collection_name,
            )
            return RagEvalRetrievalResponse(
                results=[
                    RagEvalRetrievalResult(
                        chunk_id=result.chunk_id,
                        source_id=result.source_id,
                        score=result.score,
                        text=result.text,
                        embedding_id=result.embedding_id,
                        language=result.language,
                        source_type=result.source_type,
                        validation_status=result.validation_status,
                        text_hash=result.text_hash,
                        qdrant_collection=result.qdrant_collection,
                        payload_metadata=dict(result.payload_metadata or {}),
                    )
                    for result in retrieval_response.results
                ]
            )

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
            profile_id=profile_id,
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
                rrf_k=self._config.retrieval.rrf_k,
            )

        raise ValueError(f"Unsupported retrieval_mode: {retrieval_mode}")


__all__ = ["EternalWorldRagEvalBackend"]
