from __future__ import annotations

from datetime import datetime, timezone
from time import perf_counter

from sqlalchemy.orm import Session

from app.db.models import BackgroundJob, User
from app.modules.embeddings.exceptions import (
    RagEmbeddingGenerationError,
    RagEmbeddingModelUnavailableError,
)
from app.modules.embeddings.service import embed_source_chunks
from app.modules.job_tracking.enums import BackgroundJobType
from app.modules.job_tracking.service import (
    attach_celery_task_id,
    create_job,
    mark_failed,
    mark_running,
    mark_succeeded,
    update_progress,
)
from app.modules.multi_embedding_eval.exceptions import (
    MultiEmbeddingEvalAllCandidatesFailedError,
    MultiEmbeddingEvalJobNotFoundError,
    MultiEmbeddingEvalSourceNotFoundError,
    MultiEmbeddingEvalUserNotFoundError,
)
from app.modules.multi_embedding_eval.schemas import (
    CandidateExecutionResult,
    CandidateExecutionWarning,
    MultiEmbeddingEvalCandidate,
    MultiEmbeddingEvalRequest,
    MultiEmbeddingEvalResult,
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
from app.modules.rag_quality.schemas import RagQualityCaseResultsInput
from app.modules.rag_quality.service import RagQualityService
from app.modules.rag_retrieval.exceptions import (
    RagRetrievalDisabledError,
    RagRetrievalModelUnavailableError,
    RagRetrievalProfileNotFoundError,
)
from app.modules.rag_retrieval.schemas import RagRetrievalRequest
from app.modules.rag_retrieval.service import retrieve_profile_rag_for_collection
from app.modules.rag_sources.schemas import READY_FOR_CLEANING_STATUS
from app.modules.rag_sources.service import RagSourceNotFoundError, get_rag_source


MAJOR_STEPS_PER_CANDIDATE = 4
STEP_SOURCE_VALIDATION = "source_validation"
STEP_CHUNK_PREPARATION = "chunk_preparation"
STEP_EMBEDDINGS_READY = "embeddings_ready"
STEP_QDRANT_INDEXED = "qdrant_indexed"
STEP_RETRIEVAL_RESULTS = "retrieval_results_collected"
STEP_RAG_QUALITY_EVALUATED = "rag_quality_evaluated"
WORKFLOW_NAME = "multi_embedding_eval"


def _emit_multi_embedding_eval_log(message: str) -> None:
    print(f"[multi_embedding_eval] {message}", flush=True)


def _get_background_job_or_raise(db: Session, *, job_id: int) -> BackgroundJob:
    background_job = db.get(BackgroundJob, job_id)
    if background_job is None:
        raise MultiEmbeddingEvalJobNotFoundError("Background job not found")

    return background_job


def _get_job_owner_or_raise(db: Session, *, owner_user_id: int) -> User:
    owner = db.get(User, owner_user_id)
    if owner is None:
        raise MultiEmbeddingEvalUserNotFoundError("Job owner not found")

    return owner


def _get_job_source_or_raise(db: Session, *, owner: User, source_id: int):
    try:
        return get_rag_source(
            db,
            current_user=owner,
            source_id=source_id,
        )
    except RagSourceNotFoundError as exc:
        raise MultiEmbeddingEvalSourceNotFoundError("RAG source not found") from exc


def _summarize_existing_chunks(
    db: Session,
    *,
    owner: User,
    rag_source,
) -> RagSourceChunkingSummaryRead | None:
    if getattr(rag_source, "status", None) == READY_FOR_CLEANING_STATUS:
        return None

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


def _candidate_warning(
    *,
    code: str,
    message: str,
    details: dict[str, object] | None = None,
) -> CandidateExecutionWarning:
    return CandidateExecutionWarning(
        code=code,
        message=message,
        details=dict(details or {}),
    )


def _build_error_payload(
    *,
    code: str,
    message: str,
    step: str,
    candidate_config_id: str | None = None,
    details: dict[str, object] | None = None,
) -> dict[str, object]:
    payload: dict[str, object] = {
        "code": code,
        "message": message,
        "step": step,
    }
    if candidate_config_id is not None:
        payload["candidate_config_id"] = candidate_config_id
    if details:
        payload["details"] = details

    return payload


def _map_candidate_exception(
    exc: Exception,
    *,
    candidate: MultiEmbeddingEvalCandidate,
    step: str,
) -> CandidateExecutionWarning:
    if isinstance(exc, RagEmbeddingModelUnavailableError):
        return _candidate_warning(
            code="embedding_model_unavailable",
            message="Embedding model not available",
            details={"step": step, "candidate_config_id": candidate.config_id},
        )
    if isinstance(exc, RagEmbeddingGenerationError):
        return _candidate_warning(
            code="embedding_generation_failed",
            message="Embedding generation failed",
            details={"step": step, "candidate_config_id": candidate.config_id},
        )
    if isinstance(exc, (QdrantCollectionConfigurationError, QdrantIndexingDisabledError, RagVectorIndexEmbeddingNotReadyError)):
        return _candidate_warning(
            code="qdrant_indexing_failed",
            message="Qdrant indexing failed for candidate",
            details={"step": step, "candidate_config_id": candidate.config_id},
        )
    if isinstance(exc, (RagRetrievalDisabledError, RagRetrievalModelUnavailableError, RagRetrievalProfileNotFoundError)):
        return _candidate_warning(
            code="retrieval_failed",
            message="RAG retrieval failed for candidate",
            details={"step": step, "candidate_config_id": candidate.config_id},
        )

    return _candidate_warning(
        code="candidate_execution_failed",
        message="Candidate execution failed",
        details={
            "step": step,
            "candidate_config_id": candidate.config_id,
            "exception_type": exc.__class__.__name__,
        },
    )


def _advance_candidate_to_retrieval_boundary(
    db: Session,
    *,
    job_id: int,
    candidate_index: int,
    total_candidates: int,
) -> None:
    update_progress(
        db,
        job_id=job_id,
        progress_current=((candidate_index + 1) * (MAJOR_STEPS_PER_CANDIDATE - 1)),
        progress_total=total_candidates * MAJOR_STEPS_PER_CANDIDATE,
    )


def _build_result_payload(
    *,
    source_id: int,
    profile_id: int,
    request_payload: MultiEmbeddingEvalRequest,
    candidate_execution_results: list[CandidateExecutionResult],
    run_result,
    warnings: list[CandidateExecutionWarning],
) -> MultiEmbeddingEvalResult:
    successful_candidates = [
        item.config_id for item in candidate_execution_results if item.status == "succeeded"
    ]
    failed_candidates = [
        item.config_id for item in candidate_execution_results if item.status == "failed"
    ]
    best_config = None
    if run_result.selection.best_config_id is not None:
        best_config = {
            "best_config_id": run_result.selection.best_config_id,
            "best_model_code": run_result.selection.best_model_code,
            "best_collection_name": run_result.selection.best_collection_name,
            "selected_metrics": (
                run_result.selection.selected_metrics.model_dump()
                if run_result.selection.selected_metrics is not None
                else None
            ),
        }

    return MultiEmbeddingEvalResult(
        source_id=source_id,
        profile_id=profile_id,
        dataset_id=request_payload.dataset.dataset_id,
        candidates_evaluated=successful_candidates,
        candidates_failed=failed_candidates,
        best_config=best_config,
        all_config_scores=run_result.selection.all_config_scores,
        warnings=warnings,
        candidate_execution_results=candidate_execution_results,
        dataset_evaluation=run_result.dataset_evaluation,
        completed_at=datetime.now(timezone.utc).isoformat(),
    )


def enqueue_multi_embedding_eval(
    db: Session,
    *,
    current_user: User,
    source_id: int,
    payload: MultiEmbeddingEvalRequest,
):
    rag_source = get_rag_source(
        db,
        current_user=current_user,
        source_id=source_id,
    )
    progress_total = len(payload.candidates) * MAJOR_STEPS_PER_CANDIDATE
    background_job = create_job(
        db,
        owner_user_id=current_user.id,
        profile_id=rag_source.profile_id,
        job_type=BackgroundJobType.RAG_RETRIEVAL,
        input_payload={
            "workflow": WORKFLOW_NAME,
            "source_id": rag_source.id,
            "profile_id": rag_source.profile_id,
            "dataset_id": payload.dataset.dataset_id,
            "request": payload.model_dump(),
        },
        progress_current=0,
        progress_total=progress_total,
    )

    from app.worker.tasks import run_multi_embedding_eval_job

    async_result = run_multi_embedding_eval_job.delay(background_job.id)
    return attach_celery_task_id(
        db,
        job_id=background_job.id,
        celery_task_id=async_result.id,
    )


def process_multi_embedding_eval_job(
    db: Session,
    *,
    job_id: int,
    celery_task_id: str | None = None,
) -> dict[str, object]:
    background_job = _get_background_job_or_raise(db, job_id=job_id)
    input_payload = background_job.input_payload or {}
    source_id = input_payload.get("source_id")
    request_payload_raw = input_payload.get("request")

    try:
        mark_running(
            db,
            job_id=job_id,
            celery_task_id=celery_task_id,
        )

        if not isinstance(source_id, int):
            raise MultiEmbeddingEvalSourceNotFoundError("RAG source not found")
        if not isinstance(request_payload_raw, dict):
            raise ValueError("Multi-embedding evaluation request payload is invalid")

        request_payload = MultiEmbeddingEvalRequest.model_validate(request_payload_raw)
        total_candidates = len(request_payload.candidates)

        owner = _get_job_owner_or_raise(
            db,
            owner_user_id=background_job.owner_user_id,
        )
        rag_source = _get_job_source_or_raise(
            db,
            owner=owner,
            source_id=source_id,
        )

        chunk_summary = _summarize_existing_chunks(
            db,
            owner=owner,
            rag_source=rag_source,
        )
        chunks_reused = chunk_summary is not None
        if chunk_summary is None:
            chunk_summary = chunk_rag_source(
                db,
                current_user=owner,
                source_id=rag_source.id,
            )

        rag_quality_service = RagQualityService()
        case_results_inputs: list[RagQualityCaseResultsInput] = []
        successful_candidates = []
        candidate_execution_results: list[CandidateExecutionResult] = []
        aggregated_warnings: list[CandidateExecutionWarning] = []

        for index, candidate in enumerate(request_payload.candidates):
            quality_candidate = candidate.to_rag_quality_candidate()
            candidate_warnings: list[CandidateExecutionWarning] = []
            _emit_multi_embedding_eval_log(
                "candidate start "
                f"model_code={candidate.model_code} collection={candidate.collection_name}"
            )

            try:
                embedding_summary = embed_source_chunks(
                    db,
                    current_user=owner,
                    source_id=rag_source.id,
                    model_code=candidate.model_code,
                )
                update_progress(
                    db,
                    job_id=job_id,
                    progress_current=(index * MAJOR_STEPS_PER_CANDIDATE) + 1,
                    progress_total=total_candidates * MAJOR_STEPS_PER_CANDIDATE,
                )

                indexing_summary = index_source_embeddings(
                    db,
                    current_user=owner,
                    source_id=rag_source.id,
                    model_code=candidate.model_code,
                    collection_name=candidate.collection_name,
                )
                update_progress(
                    db,
                    job_id=job_id,
                    progress_current=(index * MAJOR_STEPS_PER_CANDIDATE) + 2,
                    progress_total=total_candidates * MAJOR_STEPS_PER_CANDIDATE,
                )

                for case in request_payload.dataset.cases:
                    started_at = perf_counter()
                    retrieval_response = retrieve_profile_rag_for_collection(
                        db,
                        current_user=owner,
                        profile_id=rag_source.profile_id,
                        payload=RagRetrievalRequest(
                            query=case.query,
                            model_code=candidate.model_code,
                            limit=candidate.top_k,
                            score_threshold=candidate.score_threshold,
                        ),
                        collection_name=candidate.collection_name,
                    )
                    latency_ms = round((perf_counter() - started_at) * 1000, 3)
                    case_results_inputs.append(
                        rag_quality_service.adapt_rag_retrieval_response(
                            case_id=case.case_id,
                            candidate=quality_candidate,
                            retrieval_response=retrieval_response,
                            latency_ms=latency_ms,
                            cost_estimate=None,
                            metadata={
                                "workflow": WORKFLOW_NAME,
                                "source_id": rag_source.id,
                            },
                        )
                    )
                update_progress(
                    db,
                    job_id=job_id,
                    progress_current=(index * MAJOR_STEPS_PER_CANDIDATE) + 3,
                    progress_total=total_candidates * MAJOR_STEPS_PER_CANDIDATE,
                )
                _emit_multi_embedding_eval_log(
                    "candidate succeeded "
                    f"model_code={candidate.model_code} retrieval_cases={len(request_payload.dataset.cases)}"
                )

                successful_candidates.append(quality_candidate)
                candidate_execution_results.append(
                    CandidateExecutionResult(
                        config_id=candidate.config_id,
                        model_code=candidate.model_code,
                        collection_name=candidate.collection_name,
                        status="succeeded",
                        chunks_reused=chunks_reused,
                        embedding_summary=embedding_summary.model_dump(),
                        indexing_summary=indexing_summary.model_dump(),
                        retrieval_case_count=len(request_payload.dataset.cases),
                        warnings=candidate_warnings,
                        metadata=dict(candidate.metadata),
                    )
                )
            except Exception as exc:
                _emit_multi_embedding_eval_log(
                    "candidate failed "
                    f"model_code={candidate.model_code} error={exc.__class__.__name__}: {exc}"
                )
                candidate_warning = _map_candidate_exception(
                    exc,
                    candidate=candidate,
                    step=(
                        STEP_EMBEDDINGS_READY
                        if not successful_candidates and not case_results_inputs
                        else STEP_RETRIEVAL_RESULTS
                    ),
                )
                candidate_warnings.append(candidate_warning)
                aggregated_warnings.append(candidate_warning)
                candidate_execution_results.append(
                    CandidateExecutionResult(
                        config_id=candidate.config_id,
                        model_code=candidate.model_code,
                        collection_name=candidate.collection_name,
                        status="failed",
                        chunks_reused=chunks_reused,
                        retrieval_case_count=0,
                        warnings=candidate_warnings,
                        metadata=dict(candidate.metadata),
                    )
                )
                _advance_candidate_to_retrieval_boundary(
                    db,
                    job_id=job_id,
                    candidate_index=index,
                    total_candidates=total_candidates,
                )

        if not successful_candidates:
            raise MultiEmbeddingEvalAllCandidatesFailedError(
                "All candidate configurations failed"
            )

        run_result = rag_quality_service.run_quality_evaluation(
            dataset=request_payload.dataset,
            candidates=successful_candidates,
            case_results_inputs=case_results_inputs,
            max_average_latency_ms=request_payload.max_average_latency_ms,
            max_cost_estimate_total=request_payload.max_cost_estimate_total,
        )
        update_progress(
            db,
            job_id=job_id,
            progress_current=total_candidates * MAJOR_STEPS_PER_CANDIDATE,
            progress_total=total_candidates * MAJOR_STEPS_PER_CANDIDATE,
        )

        for warning_message in run_result.selection.warnings:
            aggregated_warnings.append(
                _candidate_warning(
                    code="rag_quality_warning",
                    message=warning_message,
                )
            )
        for warning_message in run_result.dataset_evaluation.warnings:
            aggregated_warnings.append(
                _candidate_warning(
                    code="dataset_evaluation_warning",
                    message=warning_message,
                )
            )

        result_payload = _build_result_payload(
            source_id=rag_source.id,
            profile_id=rag_source.profile_id,
            request_payload=request_payload,
            candidate_execution_results=candidate_execution_results,
            run_result=run_result,
            warnings=aggregated_warnings,
        )
        serialized_payload = result_payload.model_dump()
        mark_succeeded(
            db,
            job_id=job_id,
            result_payload=serialized_payload,
        )
        return {
            "job_id": job_id,
            "status": "succeeded",
            "result_payload": serialized_payload,
        }
    except Exception as exc:
        if isinstance(exc, MultiEmbeddingEvalAllCandidatesFailedError):
            error_payload = _build_error_payload(
                code="multi_embedding_eval_all_candidates_failed",
                message="All candidate configurations failed",
                step=STEP_RAG_QUALITY_EVALUATED,
                details={
                    "job_id": job_id,
                    "source_id": source_id,
                    "exception_type": exc.__class__.__name__,
                },
            )
            update_progress(
                db,
                job_id=job_id,
                progress_current=background_job.progress_total,
                progress_total=background_job.progress_total,
            )
            mark_failed(
                db,
                job_id=job_id,
                error_message="All candidate configurations failed",
                error_payload=error_payload,
            )
            raise

        if isinstance(exc, MultiEmbeddingEvalSourceNotFoundError):
            code = "multi_embedding_eval_source_not_found"
            message = "RAG source not found"
            step = STEP_SOURCE_VALIDATION
        elif isinstance(exc, RagChunkingFailedError):
            code = "multi_embedding_eval_chunking_failed"
            message = "Chunking failed"
            step = STEP_CHUNK_PREPARATION
        else:
            code = "multi_embedding_eval_failed"
            message = "Multi-embedding evaluation failed"
            step = "unknown"

        error_payload = _build_error_payload(
            code=code,
            message=message,
            step=step,
            details={
                "job_id": job_id,
                "source_id": source_id,
                "exception_type": exc.__class__.__name__,
            },
        )
        mark_failed(
            db,
            job_id=job_id,
            error_message=message,
            error_payload=error_payload,
        )
        raise
