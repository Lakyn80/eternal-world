from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models import BackgroundJob, User
from app.modules.embeddings.exceptions import RagEmbeddingGenerationError, RagEmbeddingModelUnavailableError
from app.modules.embeddings.service import embed_source_chunks
from app.modules.job_tracking.enums import BackgroundJobType
from app.modules.job_tracking.service import (
    append_job_event,
    create_job,
    mark_failed,
    mark_running,
    mark_succeeded,
    update_progress,
)
from app.modules.qdrant_indexing.exceptions import (
    QdrantCollectionConfigurationError,
    QdrantIndexingDisabledError,
    RagVectorIndexEmbeddingNotReadyError,
)
from app.modules.qdrant_indexing.service import index_source_embeddings
from app.modules.rag_chunks import repository as rag_chunks_repository
from app.modules.rag_chunks.schemas import RagSourceChunkingSummaryRead
from app.modules.rag_chunks.service import RagChunkingFailedError, chunk_rag_source
from app.modules.rag_pipeline.exceptions import (
    RagPipelineJobNotFoundError,
    RagPipelineSourceNotFoundError,
    RagPipelineUserNotFoundError,
)
from app.modules.rag_pipeline.schemas import RagSourceProcessRequest
from app.modules.rag_sources.service import RagSourceNotFoundError, get_rag_source


PIPELINE_PROGRESS_TOTAL = 4
STEP_SOURCE_VALIDATION = "source_validation"
STEP_CHUNKING = "chunking"
STEP_EMBEDDING_GENERATION = "embedding_generation"
STEP_QDRANT_INDEXING = "qdrant_indexing"


def _get_background_job_or_raise(db: Session, *, job_id: int) -> BackgroundJob:
    background_job = db.get(BackgroundJob, job_id)
    if background_job is None:
        raise RagPipelineJobNotFoundError("Background job not found")

    return background_job


def _get_job_owner_or_raise(db: Session, *, owner_user_id: int) -> User:
    owner = db.get(User, owner_user_id)
    if owner is None:
        raise RagPipelineUserNotFoundError("Job owner not found")

    return owner


def _get_job_source_or_raise(
    db: Session,
    *,
    owner: User,
    source_id: int,
):
    try:
        return get_rag_source(
            db,
            current_user=owner,
            source_id=source_id,
        )
    except RagSourceNotFoundError as exc:
        raise RagPipelineSourceNotFoundError("RAG source not found") from exc


def _build_qdrant_collection_name(model_code: str | None) -> str | None:
    if model_code is None:
        return None

    return f"{settings.qdrant_collection_name}__{model_code}"


def _build_result_payload(
    *,
    source_id: int,
    profile_id: int,
    chunk_count: int,
    valid_count: int,
    warning_count: int,
    invalid_count: int,
    embedded_count: int,
    embedding_skipped_count: int,
    embedding_failed_count: int,
    indexed_count: int,
    indexing_skipped_count: int,
    indexing_failed_count: int,
    model_code: str | None,
) -> dict[str, object]:
    return {
        "source_id": source_id,
        "profile_id": profile_id,
        "chunks_total": chunk_count,
        "chunks_valid": valid_count,
        "chunks_warning": warning_count,
        "chunks_invalid": invalid_count,
        "embeddings_total": embedded_count + embedding_skipped_count + embedding_failed_count,
        "embeddings_created": embedded_count,
        "embeddings_skipped": embedding_skipped_count,
        "embeddings_failed": embedding_failed_count,
        "indexed_total": indexed_count + indexing_skipped_count + indexing_failed_count,
        "embeddings_indexed": indexed_count,
        "indexing_skipped": indexing_skipped_count,
        "indexing_failed": indexing_failed_count,
        "model_code": model_code,
        "qdrant_collection": _build_qdrant_collection_name(model_code),
        "completed_at": datetime.now(timezone.utc).isoformat(),
    }


def _build_error_payload(
    *,
    code: str,
    message: str,
    step: str,
    details: dict[str, object] | None = None,
) -> dict[str, object]:
    payload: dict[str, object] = {
        "code": code,
        "message": message,
        "step": step,
    }
    if details:
        payload["details"] = details

    return payload


def _summarize_existing_chunks(
    db: Session,
    *,
    owner: User,
    rag_source,
) -> RagSourceChunkingSummaryRead | None:
    existing_chunks = rag_chunks_repository.list_chunks_for_source(
        db,
        owner_user_id=owner.id,
        source_id=rag_source.id,
    )
    if not existing_chunks:
        return None

    valid_count = sum(1 for chunk in existing_chunks if chunk.validation_status == "valid")
    warning_count = sum(1 for chunk in existing_chunks if chunk.validation_status == "warning")
    invalid_count = sum(1 for chunk in existing_chunks if chunk.validation_status == "invalid")
    source_validation_errors: list[str] = []
    for chunk in existing_chunks:
        if chunk.validation_errors:
            source_validation_errors.extend(chunk.validation_errors)

    return RagSourceChunkingSummaryRead(
        source_id=rag_source.id,
        profile_id=rag_source.profile_id,
        owner_user_id=owner.id,
        source_status=rag_source.status,
        chunk_count=len(existing_chunks),
        valid_count=valid_count,
        warning_count=warning_count,
        invalid_count=invalid_count,
        source_validation_errors=source_validation_errors,
        processing_error=rag_source.processing_error,
        normalized_text_updated=False,
    )


def _map_pipeline_exception(
    exc: Exception,
) -> tuple[str, str, str]:
    if isinstance(exc, RagPipelineSourceNotFoundError):
        return ("rag_source_not_found", "RAG source not found", STEP_SOURCE_VALIDATION)
    if isinstance(exc, RagChunkingFailedError):
        return ("rag_chunking_failed", "Chunking failed", STEP_CHUNKING)
    if isinstance(exc, RagEmbeddingModelUnavailableError):
        return ("embedding_model_unavailable", "Embedding model not available", STEP_EMBEDDING_GENERATION)
    if isinstance(exc, RagEmbeddingGenerationError):
        return ("embedding_generation_failed", "Embedding generation failed", STEP_EMBEDDING_GENERATION)
    if isinstance(exc, QdrantIndexingDisabledError):
        return ("qdrant_indexing_disabled", "Qdrant indexing is disabled", STEP_QDRANT_INDEXING)
    if isinstance(exc, RagVectorIndexEmbeddingNotReadyError):
        return ("rag_embedding_not_ready", "RAG embedding is not ready for indexing", STEP_QDRANT_INDEXING)
    if isinstance(exc, QdrantCollectionConfigurationError):
        return (
            "qdrant_collection_configuration_error",
            "Qdrant collection configuration is invalid",
            STEP_QDRANT_INDEXING,
        )

    return ("rag_source_processing_failed", "RAG source processing failed", "unknown")


def enqueue_rag_source_processing(
    db: Session,
    *,
    current_user: User,
    source_id: int,
    payload: RagSourceProcessRequest | None = None,
):
    rag_source = get_rag_source(
        db,
        current_user=current_user,
        source_id=source_id,
    )
    request_payload = payload or RagSourceProcessRequest()
    #: Task 65.9.1 (Part I) - this document-processing/embedding pipeline
    #: (chunk -> embed -> Qdrant index, routed to the `embedding` queue -
    #: see `app.worker.celery_app.task_routes`) is exactly the kind of
    #: heavy entry point Part I requires backpressure on; Task 65.9 only
    #: wired the centralized per-user/per-profile/global limits into the
    #: two candidate/contribution indexing paths, leaving this endpoint
    #: (already existing, already routed to `embedding`) as an unintended
    #: gap. `queue="embedding"` + a deterministic `idempotency_key` bring it
    #: under the same `_enforce_heavy_job_backpressure` check as the other
    #: heavy endpoints, and additionally make a duplicate "process" click
    #: for the same source+model converge on the same active job instead of
    #: creating a second one.
    idempotency_key = f"rag_source_processing:{rag_source.id}:{request_payload.model_code or 'default'}:process"
    background_job = create_job(
        db,
        owner_user_id=current_user.id,
        profile_id=rag_source.profile_id,
        job_type=BackgroundJobType.RAG_SOURCE_INGESTION,
        input_payload={
            "source_id": rag_source.id,
            "profile_id": rag_source.profile_id,
            "model_code": request_payload.model_code,
            "pipeline": [
                STEP_CHUNKING,
                STEP_EMBEDDING_GENERATION,
                STEP_QDRANT_INDEXING,
            ],
        },
        progress_current=0,
        progress_total=PIPELINE_PROGRESS_TOTAL,
        queue="embedding",
        idempotency_key=idempotency_key,
    )

    #: Task 65.9.1 (Part I) - migrated from an unconditional `.delay()`
    #: call to the transactional-outbox dispatch path (Task 65.9's own
    #: `enqueue_job_with_outbox`, already used by the candidate/contribution/
    #: biography indexing endpoints) for two reasons: (1) a broker publish
    #: failure right after `create_job` committed must not silently lose
    #: this job the way a bare `.delay()` would; (2) when `create_job`
    #: above returns a *reused* job (idempotency hit on the same
    #: source+model), `enqueue_job_with_outbox` is itself idempotent
    #: (`_dispatch_one` is a no-op once the existing outbox row is already
    #: `published`), so a duplicate "process" click can never double-dispatch
    #: the same job id to Celery.
    from app.modules.job_outbox.service import enqueue_job_with_outbox

    return enqueue_job_with_outbox(
        db,
        job=background_job,
        task_name="app.worker.tasks.run_rag_source_processing_job",
        queue="embedding",
    )


def process_rag_source_job(
    db: Session,
    *,
    job_id: int,
    celery_task_id: str | None = None,
) -> dict[str, object]:
    background_job = _get_background_job_or_raise(db, job_id=job_id)
    input_payload = background_job.input_payload or {}
    source_id = input_payload.get("source_id")
    model_code = input_payload.get("model_code")

    try:
        mark_running(
            db,
            job_id=job_id,
            celery_task_id=celery_task_id,
        )
        append_job_event(
            db,
            job_id=job_id,
            stage=STEP_SOURCE_VALIDATION,
            status="running",
            details={"source_id": source_id, "model_code": model_code},
        )

        if not isinstance(source_id, int):
            raise RagPipelineSourceNotFoundError("RAG source not found")
        if model_code is not None and not isinstance(model_code, str):
            model_code = None

        owner = _get_job_owner_or_raise(
            db,
            owner_user_id=background_job.owner_user_id,
        )
        rag_source = _get_job_source_or_raise(
            db,
            owner=owner,
            source_id=source_id,
        )
        update_progress(
            db,
            job_id=job_id,
            progress_current=1,
            progress_total=PIPELINE_PROGRESS_TOTAL,
        )

        chunk_summary = _summarize_existing_chunks(
            db,
            owner=owner,
            rag_source=rag_source,
        )
        if chunk_summary is None:
            chunk_summary = chunk_rag_source(
                db,
                current_user=owner,
                source_id=rag_source.id,
            )
        append_job_event(
            db,
            job_id=job_id,
            stage=STEP_CHUNKING,
            status="ok",
            details={
                "chunk_count": chunk_summary.chunk_count,
                "valid_count": chunk_summary.valid_count,
                "warning_count": chunk_summary.warning_count,
                "invalid_count": chunk_summary.invalid_count,
            },
        )
        update_progress(
            db,
            job_id=job_id,
            progress_current=2,
            progress_total=PIPELINE_PROGRESS_TOTAL,
        )

        embedding_summary = embed_source_chunks(
            db,
            current_user=owner,
            source_id=rag_source.id,
            model_code=model_code,
        )
        append_job_event(
            db,
            job_id=job_id,
            stage=STEP_EMBEDDING_GENERATION,
            status="ok",
            details={
                "model_code": embedding_summary.model_code,
                "embedded_count": embedding_summary.embedded_count,
                "skipped_count": embedding_summary.skipped_count,
                "failed_count": embedding_summary.failed_count,
            },
        )
        update_progress(
            db,
            job_id=job_id,
            progress_current=3,
            progress_total=PIPELINE_PROGRESS_TOTAL,
        )

        indexing_summary = index_source_embeddings(
            db,
            current_user=owner,
            source_id=rag_source.id,
            model_code=embedding_summary.model_code,
        )
        append_job_event(
            db,
            job_id=job_id,
            stage=STEP_QDRANT_INDEXING,
            status="ok",
            details={
                "model_code": embedding_summary.model_code,
                "indexed_count": indexing_summary.indexed_count,
                "skipped_count": indexing_summary.skipped_count,
                "failed_count": indexing_summary.failed_count,
            },
        )
        update_progress(
            db,
            job_id=job_id,
            progress_current=4,
            progress_total=PIPELINE_PROGRESS_TOTAL,
        )

        result_payload = _build_result_payload(
            source_id=rag_source.id,
            profile_id=rag_source.profile_id,
            chunk_count=chunk_summary.chunk_count,
            valid_count=chunk_summary.valid_count,
            warning_count=chunk_summary.warning_count,
            invalid_count=chunk_summary.invalid_count,
            embedded_count=embedding_summary.embedded_count,
            embedding_skipped_count=embedding_summary.skipped_count,
            embedding_failed_count=embedding_summary.failed_count,
            indexed_count=indexing_summary.indexed_count,
            indexing_skipped_count=indexing_summary.skipped_count,
            indexing_failed_count=indexing_summary.failed_count,
            model_code=embedding_summary.model_code,
        )
        mark_succeeded(
            db,
            job_id=job_id,
            result_payload=result_payload,
        )
        append_job_event(
            db,
            job_id=job_id,
            stage="job_completed",
            status="succeeded",
            details={"result_summary": result_payload},
        )
        return {
            "job_id": job_id,
            "status": "succeeded",
            "result_payload": result_payload,
        }
    except Exception as exc:
        error_code, error_message, error_step = _map_pipeline_exception(
            exc,
        )
        error_payload = _build_error_payload(
            code=error_code,
            message=error_message,
            step=error_step,
            details={
                "job_id": job_id,
                "source_id": source_id,
                "exception_type": exc.__class__.__name__,
            },
        )
        append_job_event(
            db,
            job_id=job_id,
            stage=error_step or "job_failed",
            status="failed",
            details=error_payload,
        )
        mark_failed(
            db,
            job_id=job_id,
            error_message=error_message,
            error_payload=error_payload,
        )
        raise
