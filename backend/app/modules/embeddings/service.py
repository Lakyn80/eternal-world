from __future__ import annotations

from sqlalchemy.orm import Session

from app.db.models import RagChunk, RagEmbedding, User
from app.modules.embedding_models.exceptions import EmbeddingModelNotFoundError
from app.modules.embedding_models.service import get_default_embedding_model, get_embedding_model
from app.modules.embeddings import repository
from app.modules.embeddings.exceptions import (
    RagEmbeddingChunkNotFoundError,
    RagEmbeddingGenerationError,
    RagEmbeddingModelUnavailableError,
    RagEmbeddingNotFoundError,
    RagEmbeddingSourceNotFoundError,
)
from app.modules.embeddings.providers.base import EmbeddingVector
from app.modules.embeddings.providers.mock import MockEmbeddingProvider
from app.modules.embeddings.schemas import RagSourceEmbeddingSummaryRead
from app.modules.rag_chunks import repository as rag_chunks_repository
from app.modules.rag_chunks.service import RagChunkNotFoundError, get_rag_chunk
from app.modules.rag_sources.service import RagSourceNotFoundError, get_rag_source


EMBEDDED_STATUS = "embedded"
FAILED_STATUS = "failed"
INVALID_CHUNK_STATUS = "invalid"
SAFE_EMBEDDING_FAILURE_MESSAGE = "Embedding generation failed"


def _get_owned_chunk_or_raise(
    db: Session,
    *,
    current_user: User,
    chunk_id: int,
) -> RagChunk:
    try:
        return get_rag_chunk(
            db,
            current_user=current_user,
            chunk_id=chunk_id,
        )
    except RagChunkNotFoundError as exc:
        raise RagEmbeddingChunkNotFoundError("RAG chunk not found") from exc


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
        raise RagEmbeddingSourceNotFoundError("RAG source not found") from exc


def _resolve_model(model_code: str | None):
    try:
        model = get_default_embedding_model() if model_code is None else get_embedding_model(model_code)
    except EmbeddingModelNotFoundError as exc:
        raise RagEmbeddingModelUnavailableError("Embedding model not found") from exc

    if not model.enabled:
        raise RagEmbeddingModelUnavailableError("Embedding model not available")

    return model


def _build_provider():
    return MockEmbeddingProvider()


def _build_embedding_metadata(
    *,
    chunk: RagChunk,
    model,
    embedding_vector: EmbeddingVector,
) -> dict[str, object]:
    return {
        "provider_type": model.provider_type,
        "normalized_vectors": model.normalized_vectors,
        "supports_batching": model.supports_batching,
        "input_char_count": chunk.char_count,
        "input_sentence_count": chunk.sentence_count,
        "chunk_validation_status": chunk.validation_status,
        **embedding_vector.metadata,
    }


def _upsert_embedding_record(
    db: Session,
    *,
    chunk: RagChunk,
    model,
    vector: list[float] | None,
    status: str,
    error_message: str | None,
    embedding_metadata: dict[str, object] | None,
) -> RagEmbedding:
    rag_embedding = repository.get_embedding_for_chunk_and_model(
        db,
        chunk_id=chunk.id,
        model_code=model.code,
    )
    if rag_embedding is None:
        return repository.create_rag_embedding(
            db,
            owner_user_id=chunk.owner_user_id,
            profile_id=chunk.profile_id,
            source_id=chunk.source_id,
            chunk_id=chunk.id,
            model_code=model.code,
            vector=vector,
            vector_dimension=model.dimension,
            text_hash=chunk.text_hash,
            status=status,
            error_message=error_message,
            embedding_metadata=embedding_metadata,
        )

    rag_embedding.owner_user_id = chunk.owner_user_id
    rag_embedding.profile_id = chunk.profile_id
    rag_embedding.source_id = chunk.source_id
    rag_embedding.chunk_id = chunk.id
    rag_embedding.model_code = model.code
    rag_embedding.vector = vector
    rag_embedding.vector_dimension = model.dimension
    rag_embedding.text_hash = chunk.text_hash
    rag_embedding.status = status
    rag_embedding.error_message = error_message
    rag_embedding.embedding_metadata = embedding_metadata
    return rag_embedding


def embed_rag_chunk(
    db: Session,
    *,
    current_user: User,
    chunk_id: int,
    model_code: str | None = None,
) -> RagEmbedding:
    chunk = _get_owned_chunk_or_raise(
        db,
        current_user=current_user,
        chunk_id=chunk_id,
    )
    model = _resolve_model(model_code)
    provider = _build_provider()

    try:
        embedding_vector = provider.embed_text(chunk.chunk_text, model.code)
        if embedding_vector.dimension != model.dimension or len(embedding_vector.values) != model.dimension:
            raise RagEmbeddingGenerationError(SAFE_EMBEDDING_FAILURE_MESSAGE)

        rag_embedding = _upsert_embedding_record(
            db,
            chunk=chunk,
            model=model,
            vector=embedding_vector.values,
            status=EMBEDDED_STATUS,
            error_message=None,
            embedding_metadata=_build_embedding_metadata(
                chunk=chunk,
                model=model,
                embedding_vector=embedding_vector,
            ),
        )
        db.commit()
        db.refresh(rag_embedding)
        return rag_embedding
    except RagEmbeddingGenerationError:
        db.rollback()
        rag_embedding = _upsert_embedding_record(
            db,
            chunk=chunk,
            model=model,
            vector=None,
            status=FAILED_STATUS,
            error_message=SAFE_EMBEDDING_FAILURE_MESSAGE,
            embedding_metadata={
                "provider_type": model.provider_type,
                "chunk_validation_status": chunk.validation_status,
            },
        )
        db.commit()
        db.refresh(rag_embedding)
        raise
    except Exception as exc:
        db.rollback()
        rag_embedding = _upsert_embedding_record(
            db,
            chunk=chunk,
            model=model,
            vector=None,
            status=FAILED_STATUS,
            error_message=SAFE_EMBEDDING_FAILURE_MESSAGE,
            embedding_metadata={
                "provider_type": model.provider_type,
                "chunk_validation_status": chunk.validation_status,
            },
        )
        db.commit()
        db.refresh(rag_embedding)
        raise RagEmbeddingGenerationError(SAFE_EMBEDDING_FAILURE_MESSAGE) from exc


def embed_source_chunks(
    db: Session,
    *,
    current_user: User,
    source_id: int,
    model_code: str | None = None,
) -> RagSourceEmbeddingSummaryRead:
    source = _get_owned_source_or_raise(
        db,
        current_user=current_user,
        source_id=source_id,
    )
    model = _resolve_model(model_code)
    chunks = rag_chunks_repository.list_chunks_for_source(
        db,
        owner_user_id=current_user.id,
        source_id=source.id,
    )

    embedded_count = 0
    skipped_count = 0
    failed_count = 0

    for chunk in chunks:
        if chunk.validation_status == INVALID_CHUNK_STATUS:
            skipped_count += 1
            continue

        try:
            embed_rag_chunk(
                db,
                current_user=current_user,
                chunk_id=chunk.id,
                model_code=model.code,
            )
            embedded_count += 1
        except RagEmbeddingGenerationError:
            failed_count += 1

    return RagSourceEmbeddingSummaryRead(
        source_id=source.id,
        model_code=model.code,
        total_chunks=len(chunks),
        embedded_count=embedded_count,
        skipped_count=skipped_count,
        failed_count=failed_count,
    )


def list_rag_embeddings_for_chunk(
    db: Session,
    *,
    current_user: User,
    chunk_id: int,
) -> list[RagEmbedding]:
    _get_owned_chunk_or_raise(
        db,
        current_user=current_user,
        chunk_id=chunk_id,
    )
    return repository.list_embeddings_for_chunk_for_user(
        db,
        owner_user_id=current_user.id,
        chunk_id=chunk_id,
    )


def get_rag_embedding(
    db: Session,
    *,
    current_user: User,
    embedding_id: int,
) -> RagEmbedding:
    rag_embedding = repository.get_embedding_for_user(
        db,
        owner_user_id=current_user.id,
        embedding_id=embedding_id,
    )
    if rag_embedding is None:
        raise RagEmbeddingNotFoundError("RAG embedding not found")

    return rag_embedding
