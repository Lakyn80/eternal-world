from __future__ import annotations

from celery.utils.log import get_task_logger

from app.db.session import SessionLocal
from app.modules.job_tracking.service import append_job_event, mark_failed, mark_running, mark_succeeded, update_progress
from app.modules.multi_embedding_eval.service import process_multi_embedding_eval_job
from app.modules.rag_pipeline.service import process_rag_source_job
from app.worker.celery_app import celery_app


logger = get_task_logger(__name__)


def get_session_factory():
    return SessionLocal


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
