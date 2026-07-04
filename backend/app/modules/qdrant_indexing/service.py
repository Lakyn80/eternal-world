from __future__ import annotations

from datetime import datetime, timezone
from uuid import NAMESPACE_URL, uuid5

from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models import RagEmbedding, RagVectorIndex, User
from app.modules.qdrant_indexing import repository
from app.modules.qdrant_indexing.client import build_qdrant_client
from app.modules.qdrant_indexing.exceptions import (
    QdrantCollectionConfigurationError,
    QdrantIndexingDisabledError,
    RagVectorIndexEmbeddingNotFoundError,
    RagVectorIndexEmbeddingNotReadyError,
    RagVectorIndexNotFoundError,
    RagVectorIndexSourceNotFoundError,
)
from app.modules.qdrant_indexing.schemas import RagSourceIndexingSummaryRead
from app.modules.rag_retrieval.hybrid import (
    SPARSE_VECTOR_PAYLOAD_KEY,
    is_bge_m3_dense_sparse_model,
    resolve_passage_sparse_vector,
)
from app.modules.rag_sources.service import RagSourceNotFoundError, get_rag_source


INDEXED_STATUS = "indexed"
FAILED_STATUS = "failed"


def _ensure_indexing_enabled() -> None:
    if not settings.qdrant_indexing_enabled:
        raise QdrantIndexingDisabledError("Qdrant indexing is disabled")


def _get_owned_embedding_or_raise(
    db: Session,
    *,
    current_user: User,
    embedding_id: int,
) -> RagEmbedding:
    rag_embedding = repository.get_embedding_for_indexing_for_user(
        db,
        owner_user_id=current_user.id,
        embedding_id=embedding_id,
    )
    if rag_embedding is None:
        raise RagVectorIndexEmbeddingNotFoundError("RAG embedding not found")

    return rag_embedding


def _get_owned_source_or_raise(
    db: Session,
    *,
    current_user: User,
    source_id: int,
):
    try:
        return get_rag_source(
            db,
            current_user=current_user,
            source_id=source_id,
        )
    except RagSourceNotFoundError as exc:
        raise RagVectorIndexSourceNotFoundError("RAG source not found") from exc


def build_qdrant_collection_name(
    model_code: str,
    *,
    collection_name: str | None = None,
) -> str:
    if collection_name is not None:
        return collection_name

    return f"{settings.qdrant_collection_name}__{model_code}"


def _build_point_id(*, collection_name: str, embedding_id: int) -> str:
    return str(uuid5(NAMESPACE_URL, f"{collection_name}:{embedding_id}"))


def _build_qdrant_payload(
    *,
    rag_embedding: RagEmbedding,
    indexed_at: datetime,
    sparse_vector: dict[str, float] | None = None,
) -> dict[str, object]:
    payload = {
        "owner_user_id": rag_embedding.owner_user_id,
        "profile_id": rag_embedding.profile_id,
        "source_id": rag_embedding.source_id,
        "chunk_id": rag_embedding.chunk_id,
        "embedding_id": rag_embedding.id,
        "model_code": rag_embedding.model_code,
        "text_hash": rag_embedding.text_hash,
        "language": rag_embedding.chunk.language,
        "validation_status": rag_embedding.chunk.validation_status,
        "source_type": rag_embedding.source.source_type,
        "chunk_index": rag_embedding.chunk.chunk_index,
        "indexed_at": indexed_at.isoformat(),
    }
    if sparse_vector:
        payload[SPARSE_VECTOR_PAYLOAD_KEY] = sparse_vector

    return payload


def _upsert_vector_index_record(
    db: Session,
    *,
    rag_embedding: RagEmbedding,
    qdrant_collection: str,
    qdrant_point_id: str,
    status: str,
    error_message: str | None,
    indexed_at: datetime | None,
) -> RagVectorIndex:
    rag_vector_index = repository.get_vector_index_for_embedding_and_collection(
        db,
        embedding_id=rag_embedding.id,
        qdrant_collection=qdrant_collection,
    )
    if rag_vector_index is None:
        return repository.create_rag_vector_index(
            db,
            owner_user_id=rag_embedding.owner_user_id,
            profile_id=rag_embedding.profile_id,
            source_id=rag_embedding.source_id,
            chunk_id=rag_embedding.chunk_id,
            embedding_id=rag_embedding.id,
            model_code=rag_embedding.model_code,
            qdrant_collection=qdrant_collection,
            qdrant_point_id=qdrant_point_id,
            status=status,
            error_message=error_message,
            indexed_at=indexed_at,
        )

    rag_vector_index.owner_user_id = rag_embedding.owner_user_id
    rag_vector_index.profile_id = rag_embedding.profile_id
    rag_vector_index.source_id = rag_embedding.source_id
    rag_vector_index.chunk_id = rag_embedding.chunk_id
    rag_vector_index.embedding_id = rag_embedding.id
    rag_vector_index.model_code = rag_embedding.model_code
    rag_vector_index.qdrant_collection = qdrant_collection
    rag_vector_index.qdrant_point_id = qdrant_point_id
    rag_vector_index.status = status
    rag_vector_index.error_message = error_message
    rag_vector_index.indexed_at = indexed_at
    return rag_vector_index


def _index_embedding_record(
    db: Session,
    *,
    rag_embedding: RagEmbedding,
    collection_name: str | None = None,
) -> RagVectorIndex:
    _ensure_indexing_enabled()

    if rag_embedding.status != "embedded" or not rag_embedding.vector:
        raise RagVectorIndexEmbeddingNotReadyError("RAG embedding is not ready for indexing")

    if len(rag_embedding.vector) != rag_embedding.vector_dimension:
        raise QdrantCollectionConfigurationError("Embedding vector dimension is invalid")

    qdrant_collection = build_qdrant_collection_name(
        rag_embedding.model_code,
        collection_name=collection_name,
    )
    qdrant_point_id = _build_point_id(
        collection_name=qdrant_collection,
        embedding_id=rag_embedding.id,
    )
    indexed_at = datetime.now(timezone.utc)
    qdrant_client = build_qdrant_client()
    sparse_vector = None
    if is_bge_m3_dense_sparse_model(rag_embedding.model_code):
        sparse_vector = resolve_passage_sparse_vector(
            chunk_text=rag_embedding.chunk.chunk_text,
            model_code=rag_embedding.model_code,
            embedding_metadata=rag_embedding.embedding_metadata,
        )

    try:
        qdrant_client.ensure_collection(
            collection_name=qdrant_collection,
            vector_size=rag_embedding.vector_dimension,
        )
        qdrant_client.upsert_point(
            collection_name=qdrant_collection,
            point_id=qdrant_point_id,
            vector=rag_embedding.vector,
            payload=_build_qdrant_payload(
                rag_embedding=rag_embedding,
                indexed_at=indexed_at,
                sparse_vector=sparse_vector,
            ),
        )
        rag_vector_index = _upsert_vector_index_record(
            db,
            rag_embedding=rag_embedding,
            qdrant_collection=qdrant_collection,
            qdrant_point_id=qdrant_point_id,
            status=INDEXED_STATUS,
            error_message=None,
            indexed_at=indexed_at,
        )
        db.commit()
        db.refresh(rag_vector_index)
        return rag_vector_index
    except Exception as exc:
        db.rollback()
        rag_vector_index = _upsert_vector_index_record(
            db,
            rag_embedding=rag_embedding,
            qdrant_collection=qdrant_collection,
            qdrant_point_id=qdrant_point_id,
            status=FAILED_STATUS,
            error_message=str(exc),
            indexed_at=None,
        )
        db.commit()
        db.refresh(rag_vector_index)
        raise


def index_rag_embedding(
    db: Session,
    *,
    current_user: User,
    embedding_id: int,
    collection_name: str | None = None,
) -> RagVectorIndex:
    rag_embedding = _get_owned_embedding_or_raise(
        db,
        current_user=current_user,
        embedding_id=embedding_id,
    )
    return _index_embedding_record(
        db,
        rag_embedding=rag_embedding,
        collection_name=collection_name,
    )


def index_source_embeddings(
    db: Session,
    *,
    current_user: User,
    source_id: int,
    model_code: str | None = None,
    collection_name: str | None = None,
) -> RagSourceIndexingSummaryRead:
    _ensure_indexing_enabled()
    source = _get_owned_source_or_raise(
        db,
        current_user=current_user,
        source_id=source_id,
    )
    rag_embeddings = repository.list_source_embeddings_for_user(
        db,
        owner_user_id=current_user.id,
        source_id=source.id,
        model_code=model_code,
    )

    indexed_count = 0
    skipped_count = 0
    failed_count = 0

    for rag_embedding in rag_embeddings:
        if rag_embedding.status != "embedded" or not rag_embedding.vector:
            skipped_count += 1
            continue

        try:
            _index_embedding_record(
                db,
                rag_embedding=rag_embedding,
                collection_name=collection_name,
            )
            indexed_count += 1
        except (
            QdrantCollectionConfigurationError,
            QdrantIndexingDisabledError,
            RagVectorIndexEmbeddingNotReadyError,
        ):
            failed_count += 1
        except Exception:
            failed_count += 1

    return RagSourceIndexingSummaryRead(
        source_id=source.id,
        model_code=model_code,
        total_embeddings=len(rag_embeddings),
        indexed_count=indexed_count,
        skipped_count=skipped_count,
        failed_count=failed_count,
    )


def get_rag_vector_index(
    db: Session,
    *,
    current_user: User,
    embedding_id: int,
) -> RagVectorIndex:
    _get_owned_embedding_or_raise(
        db,
        current_user=current_user,
        embedding_id=embedding_id,
    )
    rag_vector_index = repository.get_vector_index_for_user_by_embedding(
        db,
        owner_user_id=current_user.id,
        embedding_id=embedding_id,
    )
    if rag_vector_index is None:
        raise RagVectorIndexNotFoundError("RAG vector index not found")

    return rag_vector_index
