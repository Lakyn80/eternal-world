from __future__ import annotations

from sqlalchemy.orm import Session

from app.db.models import RagChunk, User
from app.modules.rag_chunks.chunker import build_chunk_candidates, normalize_source_text
from app.modules.rag_chunks import repository
from app.modules.rag_chunks.schemas import RagSourceChunkingSummaryRead
from app.modules.rag_chunks.validation import validate_chunk_candidates
from app.modules.rag_sources.service import RagSourceNotFoundError, get_rag_source


CHUNKED_STATUS = "chunked"
FAILED_STATUS = "failed"
SAFE_CHUNKING_FAILURE_MESSAGE = "Chunking failed"


class RagChunkNotFoundError(Exception):
    pass


class RagChunkSourceNotFoundError(Exception):
    pass


class RagChunkingFailedError(Exception):
    pass


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
        raise RagChunkSourceNotFoundError("RAG source not found") from exc


def chunk_rag_source(
    db: Session,
    *,
    current_user: User,
    source_id: int,
) -> RagSourceChunkingSummaryRead:
    rag_source = _get_owned_source_or_raise(
        db,
        current_user=current_user,
        source_id=source_id,
    )
    source_text = rag_source.normalized_text or rag_source.raw_text
    normalized_text = normalize_source_text(source_text)

    try:
        chunk_candidates = build_chunk_candidates(normalized_text)
        if not chunk_candidates:
            raise RagChunkingFailedError(SAFE_CHUNKING_FAILURE_MESSAGE)

        validated_chunks, validation_summary = validate_chunk_candidates(
            chunk_candidates=chunk_candidates,
            owner_user_id=current_user.id,
            profile_id=rag_source.profile_id,
            source_id=rag_source.id,
            normalized_source_text=normalized_text,
        )

        normalized_text_updated = rag_source.normalized_text != normalized_text
        repository.delete_chunks_for_source(db, source_id=rag_source.id)
        for validated_chunk in validated_chunks:
            repository.create_rag_chunk(
                db,
                owner_user_id=current_user.id,
                profile_id=rag_source.profile_id,
                source_id=rag_source.id,
                chunk_index=validated_chunk.chunk_index,
                chunk_text=validated_chunk.chunk_text,
                text_hash=validated_chunk.text_hash,
                token_estimate=validated_chunk.token_estimate,
                char_count=validated_chunk.char_count,
                sentence_count=validated_chunk.sentence_count,
                language=rag_source.language,
                chunk_metadata=validated_chunk.chunk_metadata,
                validation_status=validated_chunk.validation_status,
                validation_errors=validated_chunk.validation_errors,
            )

        rag_source.normalized_text = normalized_text
        rag_source.status = CHUNKED_STATUS
        rag_source.processing_error = None
        db.commit()
        return RagSourceChunkingSummaryRead(
            source_id=rag_source.id,
            profile_id=rag_source.profile_id,
            owner_user_id=current_user.id,
            source_status=rag_source.status,
            chunk_count=validation_summary.chunk_count,
            valid_count=validation_summary.valid_count,
            warning_count=validation_summary.warning_count,
            invalid_count=validation_summary.invalid_count,
            source_validation_errors=validation_summary.source_validation_errors,
            processing_error=None,
            normalized_text_updated=normalized_text_updated,
        )
    except RagChunkingFailedError:
        db.rollback()
        rag_source.status = FAILED_STATUS
        rag_source.processing_error = SAFE_CHUNKING_FAILURE_MESSAGE
        db.commit()
        raise
    except Exception as exc:
        db.rollback()
        rag_source.status = FAILED_STATUS
        rag_source.processing_error = SAFE_CHUNKING_FAILURE_MESSAGE
        db.commit()
        raise RagChunkingFailedError(SAFE_CHUNKING_FAILURE_MESSAGE) from exc


def list_rag_chunks(
    db: Session,
    *,
    current_user: User,
    source_id: int,
) -> list[RagChunk]:
    _get_owned_source_or_raise(
        db,
        current_user=current_user,
        source_id=source_id,
    )
    return repository.list_chunks_for_source(
        db,
        owner_user_id=current_user.id,
        source_id=source_id,
    )


def get_rag_chunk(
    db: Session,
    *,
    current_user: User,
    chunk_id: int,
) -> RagChunk:
    rag_chunk = repository.get_chunk_for_user(
        db,
        owner_user_id=current_user.id,
        chunk_id=chunk_id,
    )
    if rag_chunk is None:
        raise RagChunkNotFoundError("RAG chunk not found")

    return rag_chunk
