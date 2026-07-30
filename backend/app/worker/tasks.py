from __future__ import annotations

from celery.utils.log import get_task_logger

from app.core.config import settings
from app.db.session import SessionLocal
from app.modules.avatar_memory_indexing.schemas import AvatarMemoryIndexingRead
from app.modules.avatar_memory_indexing.service import (
    AvatarMemoryIndexingEligibilityError,
    AvatarMemoryIndexingExecutionError,
    AvatarMemoryIndexingNotFoundError,
    DefaultAvatarMemoryEmbeddingEncoder,
    index_promotion,
)
from app.modules.biography_ingestion.service import (
    BiographyIngestionEligibilityError,
    BiographyIngestionExecutionError,
    BiographyIngestionNotFoundError,
    DefaultBiographyEmbeddingEncoder,
    index_biography,
)
from app.modules.embeddings.self_healing import ProviderRecoveryExhaustedError, SelfHealingEmbeddingEncoder
from app.modules.embeddings.worker_recycle import trigger_worker_recycle
from app.modules.job_outbox import service as job_outbox_service
from app.modules.job_tracking import repository as job_tracking_repository
from app.modules.job_tracking.service import (
    append_job_event,
    mark_failed,
    mark_running,
    mark_succeeded,
    refresh_async_queue_metrics,
    requeue_stale_job,
    touch_heartbeat,
    update_progress,
)
from app.modules.memorial_contribution_indexing.service import (
    ContributionIndexingEligibilityError,
    ContributionIndexingExecutionError,
    ContributionIndexingNotFoundError,
    DefaultContributionIndexingEmbeddingEncoder,
    index_contribution_promotion,
)
from app.modules.multi_embedding_eval.service import process_multi_embedding_eval_job
from app.modules.rag_pipeline.service import process_rag_source_job
from app.worker.celery_app import celery_app


logger = get_task_logger(__name__)


def get_session_factory():
    return SessionLocal


def _extract_recovery_exception(exc: BaseException) -> ProviderRecoveryExhaustedError | None:
    """Walks one level of exception chaining to find a
    `ProviderRecoveryExhaustedError` wrapped by a module-specific
    `*ExecutionError` (see `Default*EmbeddingEncoder.encode` in each
    indexing service module) without requiring those service modules to
    know anything about the job-platform recovery machinery."""

    cause = exc.__cause__
    if isinstance(cause, ProviderRecoveryExhaustedError):
        return cause
    return None


def _handle_provider_recovery_if_requested(
    db,
    *,
    job_id: int,
    exc: Exception,
    stage: str,
) -> bool:
    """Returns True if `exc` represents a bounded-recovery-in-progress
    outcome (Part M attempts 1-2 exhausted) that has already been safely
    persisted as `recovery_pending` by the self-healing encoder - in which
    case the task must redispatch the same job and (only on the dedicated
    embedding worker) recycle the process, and must NOT additionally call
    `mark_failed` (that would incorrectly turn a retryable, in-progress
    recovery into a terminal state). Returns False for every other
    exception, including a final (attempt-3) provider failure, which the
    caller handles via its normal `mark_failed` path."""

    recovery_exc = _extract_recovery_exception(exc)
    if recovery_exc is None or not recovery_exc.requires_fresh_process:
        return False

    append_job_event(
        db,
        job_id=job_id,
        stage=stage,
        status="recovery_pending",
        details={"reason": "provider_corrupt_fresh_process_required"},
    )
    job_outbox_service.redispatch_job(db, job_id=job_id)
    trigger_worker_recycle()
    return True


@celery_app.task(bind=True, name="app.worker.tasks.run_job_smoke_test")
def run_job_smoke_test(self, job_id: int) -> dict[str, object]:
    session_factory = get_session_factory()
    db = session_factory()
    try:
        mark_running(
            db,
            job_id=job_id,
            celery_task_id=self.request.id,
        )
        append_job_event(
            db,
            job_id=job_id,
            stage="smoke_test",
            status="running",
            details={"celery_task_id": self.request.id},
        )
        update_progress(
            db,
            job_id=job_id,
            progress_current=1,
            progress_total=3,
        )
        update_progress(
            db,
            job_id=job_id,
            progress_current=2,
            progress_total=3,
        )
        update_progress(
            db,
            job_id=job_id,
            progress_current=3,
            progress_total=3,
        )
        mark_succeeded(
            db,
            job_id=job_id,
            result_payload={
                "smoke_test": True,
                "message": "Celery smoke test completed successfully.",
            },
        )
        append_job_event(
            db,
            job_id=job_id,
            stage="smoke_test",
            status="succeeded",
            details={"progress_total": 3},
        )
        return {
            "job_id": job_id,
            "status": "succeeded",
        }
    except Exception as exc:
        logger.exception("celery_smoke_test_failed", extra={"job_id": job_id})
        append_job_event(
            db,
            job_id=job_id,
            stage="smoke_test",
            status="failed",
            details={"exception_type": exc.__class__.__name__},
        )
        mark_failed(
            db,
            job_id=job_id,
            error_message="Celery smoke test failed",
            error_payload={
                "code": "celery_smoke_test_failed",
                "message": "Celery smoke test failed",
                "details": {"job_id": job_id, "exception_type": exc.__class__.__name__},
            },
        )
        raise
    finally:
        db.close()


@celery_app.task(bind=True, name="app.worker.tasks.run_rag_source_processing_job")
def run_rag_source_processing_job(self, job_id: int) -> dict[str, object]:
    session_factory = get_session_factory()
    db = session_factory()
    try:
        return process_rag_source_job(
            db,
            job_id=job_id,
            celery_task_id=self.request.id,
        )
    except Exception:
        logger.exception("rag_source_processing_failed", extra={"job_id": job_id})
        raise
    finally:
        db.close()


@celery_app.task(bind=True, name="app.worker.tasks.run_multi_embedding_eval_job")
def run_multi_embedding_eval_job(self, job_id: int) -> dict[str, object]:
    session_factory = get_session_factory()
    db = session_factory()
    try:
        return process_multi_embedding_eval_job(
            db,
            job_id=job_id,
            celery_task_id=self.request.id,
        )
    except Exception:
        logger.exception("multi_embedding_eval_failed", extra={"job_id": job_id})
        raise
    finally:
        db.close()


@celery_app.task(bind=True, name="app.worker.tasks.run_memorial_contribution_indexing_job")
def run_memorial_contribution_indexing_job(self, job_id: int) -> dict[str, object]:
    """Runs the heavy embedding/Qdrant step of the Task 65.1B contribution
    indexing bridge outside the HTTP request that approved the contribution.
    Never raises out of this task for domain-level ineligibility/not-found -
    those are recorded as a failed job, not a Celery retry storm, since a
    contribution that was superseded/archived between enqueue and execution
    is an expected race, not an infrastructure failure.
    """

    session_factory = get_session_factory()
    db = session_factory()
    try:
        background_job = job_tracking_repository.get_background_job_by_id(db, job_id=job_id)
        if background_job is None:
            # Enqueued from an isolated test database that the worker does
            # not share - nothing to do, and nothing to alarm on.
            return {"job_id": job_id, "status": "skipped", "reason": "job_not_found"}

        promotion_id = (background_job.input_payload or {}).get("promotion_id")
        if not isinstance(promotion_id, int):
            mark_failed(
                db,
                job_id=job_id,
                error_message="Contribution indexing job payload is missing promotion_id",
            )
            return {"job_id": job_id, "status": "failed"}

        mark_running(db, job_id=job_id, celery_task_id=self.request.id)
        touch_heartbeat(db, job_id=job_id)
        append_job_event(db, job_id=job_id, stage="memorial_contribution_indexing", status="running")
        encoder = DefaultContributionIndexingEmbeddingEncoder(
            self_healing_encoder=SelfHealingEmbeddingEncoder(db=db, job_id=job_id)
        )
        try:
            result = index_contribution_promotion(
                db,
                profile_id=background_job.profile_id,
                promotion_id=promotion_id,
                encoder=encoder,
            )
        except (ContributionIndexingNotFoundError, ContributionIndexingEligibilityError) as exc:
            append_job_event(
                db,
                job_id=job_id,
                stage="memorial_contribution_indexing",
                status="skipped",
                details={"reason": str(exc)},
            )
            mark_succeeded(db, job_id=job_id, result_payload={"skipped": True, "reason": str(exc)})
            return {"job_id": job_id, "status": "skipped"}
        except ContributionIndexingExecutionError as exc:
            if _handle_provider_recovery_if_requested(
                db, job_id=job_id, exc=exc, stage="memorial_contribution_indexing"
            ):
                return {"job_id": job_id, "status": "recovery_pending"}
            logger.exception("memorial_contribution_indexing_job_failed", extra={"job_id": job_id})
            append_job_event(
                db,
                job_id=job_id,
                stage="memorial_contribution_indexing",
                status="failed",
                details={"exception_type": exc.__class__.__name__},
            )
            mark_failed(
                db,
                job_id=job_id,
                error_message="Contribution indexing failed",
                error_payload={"code": "memorial_contribution_indexing_failed"},
                safe_error_category=(
                    "provider_corrupt" if _extract_recovery_exception(exc) is not None else "unknown_internal_failure"
                ),
            )
            return {"job_id": job_id, "status": "failed"}
        except Exception as exc:
            logger.exception("memorial_contribution_indexing_job_failed", extra={"job_id": job_id})
            append_job_event(
                db,
                job_id=job_id,
                stage="memorial_contribution_indexing",
                status="failed",
                details={"exception_type": exc.__class__.__name__},
            )
            mark_failed(
                db,
                job_id=job_id,
                error_message="Contribution indexing failed",
                error_payload={"code": "memorial_contribution_indexing_failed"},
                safe_error_category="unknown_internal_failure",
            )
            return {"job_id": job_id, "status": "failed"}

        append_job_event(
            db,
            job_id=job_id,
            stage="memorial_contribution_indexing",
            status="succeeded",
            details={"result": result.result, "promotion_status": result.promotion_status},
        )
        mark_succeeded(
            db,
            job_id=job_id,
            result_payload={
                "promotion_id": result.promotion_id,
                "contribution_id": result.contribution_id,
                "promotion_status": result.promotion_status,
                "searchable_as_fact": result.searchable_as_fact,
            },
        )
        return {"job_id": job_id, "status": "succeeded"}
    finally:
        db.close()


@celery_app.task(bind=True, name="app.worker.tasks.run_avatar_memory_indexing_job")
def run_avatar_memory_indexing_job(self, job_id: int) -> dict[str, object]:
    """Runs the heavy embedding/Qdrant step of the Task 65.6.1 approved-
    candidate promotion/indexing bridge outside the HTTP request that
    approved the candidate. Domain-level ineligibility/not-found (e.g. a
    candidate that was superseded or the promotion cancelled between
    enqueue and execution) is recorded as a skipped job, not a Celery retry
    storm - mirrors `run_memorial_contribution_indexing_job` exactly."""

    session_factory = get_session_factory()
    db = session_factory()
    try:
        background_job = job_tracking_repository.get_background_job_by_id(db, job_id=job_id)
        if background_job is None:
            # Enqueued from an isolated test database that the worker does
            # not share - nothing to do, and nothing to alarm on.
            return {"job_id": job_id, "status": "skipped", "reason": "job_not_found"}

        promotion_id = (background_job.input_payload or {}).get("promotion_id")
        if not isinstance(promotion_id, int):
            mark_failed(
                db,
                job_id=job_id,
                error_message="Avatar memory indexing job payload is missing promotion_id",
            )
            return {"job_id": job_id, "status": "failed"}

        mark_running(db, job_id=job_id, celery_task_id=self.request.id)
        touch_heartbeat(db, job_id=job_id)
        append_job_event(db, job_id=job_id, stage="avatar_memory_indexing", status="running")
        encoder = DefaultAvatarMemoryEmbeddingEncoder(
            self_healing_encoder=SelfHealingEmbeddingEncoder(db=db, job_id=job_id)
        )
        try:
            result = index_promotion(
                db,
                owner_user_id=background_job.owner_user_id,
                promotion_id=promotion_id,
                encoder=encoder,
            )
        except (AvatarMemoryIndexingNotFoundError, AvatarMemoryIndexingEligibilityError) as exc:
            append_job_event(
                db,
                job_id=job_id,
                stage="avatar_memory_indexing",
                status="skipped",
                details={"reason": str(exc)},
            )
            mark_succeeded(db, job_id=job_id, result_payload={"skipped": True, "reason": str(exc)})
            return {"job_id": job_id, "status": "skipped"}
        except AvatarMemoryIndexingExecutionError as exc:
            if _handle_provider_recovery_if_requested(db, job_id=job_id, exc=exc, stage="avatar_memory_indexing"):
                return {"job_id": job_id, "status": "recovery_pending"}
            logger.exception("avatar_memory_indexing_job_failed", extra={"job_id": job_id})
            append_job_event(
                db,
                job_id=job_id,
                stage="avatar_memory_indexing",
                status="failed",
                details={"exception_type": exc.__class__.__name__},
            )
            mark_failed(
                db,
                job_id=job_id,
                error_message="Avatar memory indexing failed",
                error_payload={"code": "avatar_memory_indexing_failed"},
                safe_error_category=(
                    "provider_corrupt" if _extract_recovery_exception(exc) is not None else "unknown_internal_failure"
                ),
            )
            return {"job_id": job_id, "status": "failed"}
        except Exception as exc:
            logger.exception("avatar_memory_indexing_job_failed", extra={"job_id": job_id})
            append_job_event(
                db,
                job_id=job_id,
                stage="avatar_memory_indexing",
                status="failed",
                details={"exception_type": exc.__class__.__name__},
            )
            mark_failed(
                db,
                job_id=job_id,
                error_message="Avatar memory indexing failed",
                error_payload={"code": "avatar_memory_indexing_failed"},
                safe_error_category="unknown_internal_failure",
            )
            return {"job_id": job_id, "status": "failed"}

        append_job_event(
            db,
            job_id=job_id,
            stage="avatar_memory_indexing",
            status="succeeded",
            details={"result": result.result, "promotion_status": result.promotion_status},
        )
        mark_succeeded(
            db,
            job_id=job_id,
            result_payload={
                "promotion_id": result.promotion_id,
                "promotion_status": result.promotion_status,
                "searchable_as_fact": result.searchable_as_fact,
            },
        )
        return {"job_id": job_id, "status": "succeeded"}
    finally:
        db.close()


@celery_app.task(bind=True, name="app.worker.tasks.run_biography_indexing_job")
def run_biography_indexing_job(self, job_id: int) -> dict[str, object]:
    """Runs the heavy chunk/embed/Qdrant step of Task 65.2's initial-biography
    ingestion outside the HTTP request that started it. Domain-level
    ineligibility (e.g. the biography was cleared between enqueue and
    execution) is recorded as a failed job, not a Celery retry storm."""

    session_factory = get_session_factory()
    db = session_factory()
    try:
        background_job = job_tracking_repository.get_background_job_by_id(db, job_id=job_id)
        if background_job is None:
            return {"job_id": job_id, "status": "skipped", "reason": "job_not_found"}

        profile_id = background_job.profile_id
        if not isinstance(profile_id, int):
            mark_failed(
                db,
                job_id=job_id,
                error_message="Biography indexing job payload is missing profile_id",
            )
            return {"job_id": job_id, "status": "failed"}

        mark_running(db, job_id=job_id, celery_task_id=self.request.id)
        touch_heartbeat(db, job_id=job_id)
        append_job_event(db, job_id=job_id, stage="biography_indexing", status="running")
        encoder = DefaultBiographyEmbeddingEncoder(
            self_healing_encoder=SelfHealingEmbeddingEncoder(db=db, job_id=job_id)
        )
        try:
            result = index_biography(db, profile_id=profile_id, encoder=encoder)
        except (BiographyIngestionNotFoundError, BiographyIngestionEligibilityError) as exc:
            append_job_event(
                db,
                job_id=job_id,
                stage="biography_indexing",
                status="skipped",
                details={"reason": str(exc)},
            )
            mark_succeeded(db, job_id=job_id, result_payload={"skipped": True, "reason": str(exc)})
            return {"job_id": job_id, "status": "skipped"}
        except BiographyIngestionExecutionError as exc:
            if _handle_provider_recovery_if_requested(db, job_id=job_id, exc=exc, stage="biography_indexing"):
                return {"job_id": job_id, "status": "recovery_pending"}
            logger.exception("biography_indexing_job_failed", extra={"job_id": job_id})
            append_job_event(
                db,
                job_id=job_id,
                stage="biography_indexing",
                status="failed",
                details={"exception_type": exc.__class__.__name__},
            )
            mark_failed(
                db,
                job_id=job_id,
                error_message="Biography indexing failed",
                error_payload={"code": "biography_indexing_failed"},
                safe_error_category=(
                    "provider_corrupt" if _extract_recovery_exception(exc) is not None else "unknown_internal_failure"
                ),
            )
            return {"job_id": job_id, "status": "failed"}
        except Exception as exc:
            logger.exception("biography_indexing_job_failed", extra={"job_id": job_id})
            append_job_event(
                db,
                job_id=job_id,
                stage="biography_indexing",
                status="failed",
                details={"exception_type": exc.__class__.__name__},
            )
            mark_failed(
                db,
                job_id=job_id,
                error_message="Biography indexing failed",
                error_payload={"code": "biography_indexing_failed"},
                safe_error_category="unknown_internal_failure",
            )
            return {"job_id": job_id, "status": "failed"}

        append_job_event(
            db,
            job_id=job_id,
            stage="biography_indexing",
            status="succeeded",
            details={"status": result.status},
        )
        mark_succeeded(
            db,
            job_id=job_id,
            result_payload={
                "profile_id": result.profile_id,
                "status": result.status,
                "indexed_at": result.indexed_at.isoformat() if result.indexed_at else None,
            },
        )
        return {"job_id": job_id, "status": "succeeded"}
    finally:
        db.close()


@celery_app.task(name="app.worker.tasks.run_outbox_dispatch_job")
def run_outbox_dispatch_job() -> dict[str, object]:
    """Task 65.9 (Part E/G) - the maintenance sweep that republishes any
    transactional-outbox row still `pending` (a domain transaction
    committed but the initial best-effort broker publish failed, or has
    not been attempted yet). Safe to run from any number of concurrent
    maintenance-worker replicas/schedules - see
    `job_outbox.service.dispatch_pending_outbox_events`. Routed to the
    `maintenance` queue (never `embedding`) - this task never touches the
    embedding provider."""

    session_factory = get_session_factory()
    db = session_factory()
    try:
        summary = job_outbox_service.dispatch_pending_outbox_events(
            db,
            batch_size=settings.job_outbox_dispatch_batch_size,
        )
        return {
            "scanned": summary.scanned,
            "published": summary.published,
            "failed": summary.failed,
        }
    finally:
        db.close()


@celery_app.task(name="app.worker.tasks.run_stale_job_recovery_job")
def run_stale_job_recovery_job() -> dict[str, object]:
    """Task 65.9 (Part P) - the maintenance sweep that recovers jobs left
    `running`/`recovery_pending` by a worker that crashed (or was
    recycled) before it could reach a terminal state or update its own
    heartbeat. Safe under concurrent maintenance-worker replicas: each
    candidate job is re-checked for staleness (`requeue_stale_job`) before
    being touched, so a job already recovered/completed by another sweep
    is simply skipped, never resurrected or duplicated. Routed to the
    `maintenance` queue."""

    session_factory = get_session_factory()
    db = session_factory()
    try:
        stale_job_ids = job_tracking_repository.list_stale_processing_jobs(
            db,
            stale_before=_stale_before_cutoff(),
            limit=200,
        )
        requeued = 0
        permanently_failed = 0
        for stale_job in stale_job_ids:
            job_id = stale_job.id
            was_requeued = requeue_stale_job(db, job_id=job_id)
            if was_requeued:
                requeued += 1
                job_outbox_service.redispatch_job(db, job_id=job_id)
            else:
                refreshed = job_tracking_repository.get_background_job_by_id(db, job_id=job_id)
                if refreshed is not None and refreshed.status == "failed":
                    permanently_failed += 1
        return {
            "scanned": len(stale_job_ids),
            "requeued": requeued,
            "permanently_failed": permanently_failed,
        }
    finally:
        db.close()


@celery_app.task(name="app.worker.tasks.run_async_queue_metrics_refresh_job")
def run_async_queue_metrics_refresh_job() -> dict[str, object]:
    """Task 65.9.1 (Part H) - the maintenance sweep that recomputes the
    `async_queue_depth`/`async_oldest_job_age_seconds` gauges straight from
    PostgreSQL. Routed to the `maintenance` queue (never `embedding`) - this
    task never touches the embedding provider. Never raises: a database
    failure is recorded via a safe failure counter/log inside
    `refresh_async_queue_metrics` and reported here as `ok: False` rather
    than as a Celery task failure, so a transient DB blip cannot create a
    retry storm on a purely observational task."""

    session_factory = get_session_factory()
    db = session_factory()
    try:
        result = refresh_async_queue_metrics(db)
        return {
            "ok": result.ok,
            "queue_depths": result.queue_depths,
            "oldest_ages_seconds": result.oldest_ages_seconds,
        }
    finally:
        db.close()


def _stale_before_cutoff():
    from datetime import datetime, timedelta, timezone

    return datetime.now(timezone.utc) - timedelta(seconds=settings.job_stale_heartbeat_timeout_seconds)
