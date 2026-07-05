from __future__ import annotations

import json
from typing import Any
from uuid import NAMESPACE_URL, uuid5

from rag_eval.adapters.base import RagEvalBackend, RagEvalChunk, RagEvalRetrievalResponse, RagEvalRetrievalResult
from rag_eval.config import BenchmarkConfig, SqlQdrantConfig
from rag_eval.models.registry import get_embedding_model_definition
from rag_eval.retrieval.bm25 import Bm25IndexStore
from rag_eval.retrieval.fusion import reciprocal_rank_fusion


class SqlQdrantRagEvalBackend(RagEvalBackend):
    """Generic Postgres chunks + SentenceTransformers + Qdrant adapter for external clients."""

    def __init__(self, *, config: BenchmarkConfig) -> None:
        if config.database_url is None:
            raise ValueError("sql_qdrant backend requires database_url.")
        if config.qdrant_url is None:
            raise ValueError("sql_qdrant backend requires qdrant_url.")

        self._config = config
        self._sql_config = config.sql_qdrant or SqlQdrantConfig()
        self._engine = None
        self._qdrant_client = None
        self._embedding_models: dict[str, Any] = {}
        self._chunk_cache: dict[int, RagEvalChunk] = {}
        self._bm25_store = Bm25IndexStore(retrieval_config=config.retrieval)

    def _get_engine(self):
        if self._engine is None:
            from sqlalchemy import create_engine

            self._engine = create_engine(self._config.database_url)
        return self._engine

    def _get_qdrant_client(self):
        if self._qdrant_client is None:
            from qdrant_client import QdrantClient

            self._qdrant_client = QdrantClient(
                url=self._config.qdrant_url,
                check_compatibility=False,
            )
        return self._qdrant_client

    def _search_points(
        self,
        *,
        collection_name: str,
        query_vector: list[float],
        top_k: int,
        score_threshold: float | None,
    ):
        client = self._get_qdrant_client()
        if hasattr(client, "query_points"):
            query_kwargs: dict[str, Any] = {
                "collection_name": collection_name,
                "query": query_vector,
                "limit": top_k,
            }
            if score_threshold is not None:
                query_kwargs["score_threshold"] = score_threshold
            response = client.query_points(**query_kwargs)
            return response.points

        return client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            limit=top_k,
            score_threshold=score_threshold,
        )

    def _get_embedding_model(self, model_code: str):
        if model_code in self._embedding_models:
            return self._embedding_models[model_code]

        model_definition = get_embedding_model_definition(model_code)
        if model_definition is None or model_definition.provider_model_name is None:
            raise ValueError(f"Embedding model is not configured for local inference: {model_code}")

        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer(model_definition.provider_model_name, device=self._config.device)
        self._embedding_models[model_code] = model
        return model

    def _encode_texts(self, *, model_code: str, texts: list[str]) -> list[list[float]]:
        model = self._get_embedding_model(model_code)
        vectors = model.encode(texts, normalize_embeddings=True, show_progress_bar=False)
        return [vector.tolist() for vector in vectors]

    def _encode_query(self, *, model_code: str, query: str) -> list[float]:
        return self._encode_texts(model_code=model_code, texts=[query])[0]

    def _point_id(self, *, collection_name: str, chunk_id: int) -> str:
        return str(uuid5(NAMESPACE_URL, f"{collection_name}:{chunk_id}"))

    def _load_rows(self, *, source_id: int) -> list[dict[str, Any]]:
        from sqlalchemy import text

        columns = self._sql_config.columns
        invalid_statuses = ", ".join(f"'{status}'" for status in self._sql_config.invalid_statuses)
        query = text(
            f"""
            SELECT
                {columns.id} AS chunk_id,
                {columns.source_id} AS source_id,
                {columns.chunk_text} AS chunk_text,
                {columns.chunk_metadata} AS chunk_metadata,
                {columns.validation_status} AS validation_status
            FROM {self._sql_config.chunks_table}
            WHERE {columns.source_id} = :source_id
              AND {columns.validation_status} NOT IN ({invalid_statuses})
            ORDER BY {columns.id}
            """
        )
        with self._get_engine().connect() as connection:
            rows = connection.execute(query, {"source_id": source_id}).mappings().all()

        normalized_rows: list[dict[str, Any]] = []
        for row in rows:
            metadata = row["chunk_metadata"]
            if isinstance(metadata, str):
                metadata = json.loads(metadata) if metadata else {}
            elif metadata is None:
                metadata = {}
            normalized_rows.append(
                {
                    "chunk_id": int(row["chunk_id"]),
                    "source_id": int(row["source_id"]) if row["source_id"] is not None else source_id,
                    "chunk_text": str(row["chunk_text"] or ""),
                    "chunk_metadata": dict(metadata),
                    "validation_status": str(row["validation_status"] or "valid"),
                }
            )
        return normalized_rows

    def get_source_chunks(self, *, source_id: int) -> list[RagEvalChunk]:
        chunks = [
            RagEvalChunk(
                chunk_id=row["chunk_id"],
                chunk_text=row["chunk_text"],
                source_id=row["source_id"],
                chunk_metadata=row["chunk_metadata"],
            )
            for row in self._load_rows(source_id=source_id)
        ]
        for chunk in chunks:
            self._chunk_cache[chunk.chunk_id] = chunk
        return chunks

    def embed_source(self, *, source_id: int, model_code: str) -> None:
        return None

    def index_source(
        self,
        *,
        source_id: int,
        model_code: str,
        collection_name: str,
    ) -> None:
        from qdrant_client.http import models as qmodels

        chunks = self.get_source_chunks(source_id=source_id)
        if not chunks:
            raise ValueError(f"No chunks found for source_id={source_id}.")

        model_definition = get_embedding_model_definition(model_code)
        if model_definition is None:
            raise ValueError(f"Unknown embedding model: {model_code}")

        vectors = self._encode_texts(model_code=model_code, texts=[chunk.chunk_text for chunk in chunks])
        client = self._get_qdrant_client()
        client.recreate_collection(
            collection_name=collection_name,
            vectors_config=qmodels.VectorParams(
                size=model_definition.dimension,
                distance=qmodels.Distance.COSINE,
            ),
        )

        points = [
            qmodels.PointStruct(
                id=self._point_id(collection_name=collection_name, chunk_id=chunk.chunk_id),
                vector=vector,
                payload={
                    "chunk_id": chunk.chunk_id,
                    "source_id": chunk.source_id,
                    "text": chunk.chunk_text,
                    "model_code": model_code,
                    "chunk_metadata": chunk.chunk_metadata,
                },
            )
            for chunk, vector in zip(chunks, vectors, strict=True)
        ]
        client.upsert(collection_name=collection_name, points=points)

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
        query_vector = self._encode_query(model_code=model_code, query=query)
        hits = self._search_points(
            collection_name=collection_name,
            query_vector=query_vector,
            top_k=top_k,
            score_threshold=score_threshold,
        )

        results: list[RagEvalRetrievalResult] = []
        for hit in hits:
            payload = hit.payload or {}
            chunk_id = payload.get("chunk_id")
            cached_chunk = self._chunk_cache.get(int(chunk_id)) if chunk_id is not None else None
            text = str(payload.get("text") or (cached_chunk.chunk_text if cached_chunk else ""))
            results.append(
                RagEvalRetrievalResult(
                    chunk_id=int(chunk_id) if chunk_id is not None else None,
                    source_id=int(payload.get("source_id") or source_id),
                    score=float(hit.score),
                    text=text,
                    qdrant_collection=collection_name,
                    payload_metadata=dict(payload.get("chunk_metadata") or {}),
                )
            )
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
                rrf_k=self._config.retrieval.rrf_k,
            )

        raise ValueError(f"Unsupported retrieval_mode: {retrieval_mode}")
