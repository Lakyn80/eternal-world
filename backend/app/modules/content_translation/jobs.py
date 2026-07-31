"""Background job / outbox contract for content translation (Task 65.13.2).

Routes LLM translation work onto the ``ai_generation`` queue so it never
shares the embedding-worker backpressure path. Callers persist the domain
request fields in ``BackgroundJob.input_payload``; the worker rehydrates a
``TranslationFieldRequest`` and invokes the existing sync translation path
with the configured (typically mock-in-tests) provider.
"""

from __future__ import annotations

from typing import Any

from sqlalchemy.orm import Session

from app.db.models import BackgroundJob, MemoryContentTranslation
from app.modules.content_translation.schemas import TranslationFieldRequest
from app.modules.content_translation.service import translate_content_field
from app.modules.job_outbox.service import TaskSender, enqueue_job_with_outbox
from app.modules.job_tracking.enums import BackgroundJobType
from app.modules.job_tracking.service import create_job
from app.modules.provider_usage.context import AiCallContext, development_test_context
from app.worker.celery_app import AI_GENERATION_QUEUE


CONTENT_TRANSLATION_TASK_NAME = "app.worker.tasks.run_content_translation_job"
CONTENT_TRANSLATION_WORKFLOW = "content_translation"


def enqueue_content_translation_job(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int,
    request: TranslationFieldRequest,
    sender: TaskSender | None = None,
) -> BackgroundJob:
    """Create an idempotent content-translation job and publish via outbox."""

    if request.profile_id is not None and int(request.profile_id) != int(profile_id):
        raise ValueError("translation request profile_id does not match job profile_id")

    idempotency_key = (
        f"{CONTENT_TRANSLATION_WORKFLOW}:"
        f"{profile_id}:{request.entity_type}:{request.entity_id}:"
        f"{request.field_name}:{request.target_language}"
    )
    payload: dict[str, Any] = {
        "workflow": CONTENT_TRANSLATION_WORKFLOW,
        "profile_id": profile_id,
        "candidate_id": request.candidate_id,
        "contribution_id": request.contribution_id,
        "clarification_id": request.clarification_id,
        "entity_type": str(request.entity_type),
        "entity_id": request.entity_id,
        "field_name": request.field_name,
        "source_language": str(request.source_language),
        "target_language": str(request.target_language),
        "source_text": request.source_text,
    }
    background_job = create_job(
        db,
        owner_user_id=owner_user_id,
        profile_id=profile_id,
        job_type=BackgroundJobType.CONTENT_TRANSLATION,
        input_payload=payload,
        queue=AI_GENERATION_QUEUE,
        idempotency_key=idempotency_key,
    )
    return enqueue_job_with_outbox(
        db,
        job=background_job,
        task_name=CONTENT_TRANSLATION_TASK_NAME,
        queue=AI_GENERATION_QUEUE,
        sender=sender,
    )


def process_content_translation_job(
    db: Session,
    *,
    job: BackgroundJob,
    call_context: AiCallContext | None = None,
) -> MemoryContentTranslation:
    """Execute one queued translation job against the sync translation path."""

    payload = job.input_payload or {}
    request = TranslationFieldRequest(
        profile_id=payload.get("profile_id") or job.profile_id,
        candidate_id=payload.get("candidate_id"),
        contribution_id=payload.get("contribution_id"),
        clarification_id=payload.get("clarification_id"),
        entity_type=payload["entity_type"],
        entity_id=str(payload["entity_id"]),
        field_name=str(payload["field_name"]),
        source_language=payload["source_language"],
        target_language=payload["target_language"],
        source_text=str(payload["source_text"]),
    )
    context = call_context or development_test_context(
        trace_id=f"content-translation-job-{job.id}"
    )
    return translate_content_field(db, request, call_context=context)
