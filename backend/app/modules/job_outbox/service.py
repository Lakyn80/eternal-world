"""Transactional outbox for the async job platform (Task 65.9, Part E).

Closes exactly the gap Part E asks about: without this module, a domain
transaction (e.g. "candidate approved -> promotion pending_index") could
commit successfully, immediately followed by a broker-publish failure
(Redis briefly unreachable, network blip) - leaving the promotion stuck
`pending_index` forever with no queued Celery task and no automatic way
back. With this module: the `BackgroundJob` row and its `JobOutboxEvent`
row are written in the *same* transaction as the domain change (the
caller's own commit covers all three), so a broker failure only ever
leaves a `pending` outbox row - never a lost job. `dispatch_pending_
outbox_events` (invoked by the maintenance Celery task on a schedule, and
safe to invoke from any number of concurrent dispatcher replicas) sweeps
those rows and republishes them.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Protocol

from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.db.models import BackgroundJob
from app.modules.job_outbox import repository
from app.modules.job_tracking.enums import BackgroundJobStatus


logger = get_logger("job_outbox")

#: Bounded exponential backoff for a failed *publish attempt* (broker
#: unreachable) - distinct from, and never counted against, the job's own
#: `attempt_count`/provider-recovery counters (Part M: "Do not count
#: normal infrastructure retries as provider-recovery attempts").
_PUBLISH_BACKOFF_BASE_SECONDS = 5
_PUBLISH_BACKOFF_CAP_SECONDS = 300


class TaskSender(Protocol):
    def __call__(self, *, task_name: str, args: list[object], queue: str) -> str: ...


def _default_task_sender(*, task_name: str, args: list[object], queue: str) -> str:
    #: Imported lazily so this module never forces a Celery app import at
    #: FastAPI startup time purely for type-checking purposes, and so unit
    #: tests can inject a fake sender without needing a running broker.
    from app.worker.celery_app import celery_app

    async_result = celery_app.send_task(task_name, args=args, queue=queue)
    return async_result.id


@dataclass(frozen=True)
class OutboxDispatchSummary:
    scanned: int
    published: int
    failed: int


def enqueue_job_with_outbox(
    db: Session,
    *,
    job: BackgroundJob,
    task_name: str,
    queue: str,
    sender: TaskSender | None = None,
) -> BackgroundJob:
    """Create the outbox row for `job` and best-effort publish it
    immediately so the common case (broker healthy) still gets near-
    instant dispatch latency. On a publish failure the outbox row is left
    `pending` for the maintenance dispatcher - the job itself simply stays
    `pending`, never lost.

    Idempotent: if `job` already has an outbox row (e.g. `create_job`
    returned an existing job reused via its idempotency key), no second
    row is created - this call becomes a safe no-op redispatch attempt,
    which is itself a no-op if that row is already `published` (Part F:
    "repeated ... outbox publishing ... must not create duplicate ...
    active jobs")."""

    if repository.get_outbox_event_for_job(db, job_id=job.id) is None:
        repository.create_outbox_event(
            db,
            job_id=job.id,
            task_name=task_name,
            queue=queue,
            task_args={"job_id": job.id},
        )
        job.queue = queue
        db.commit()
        db.refresh(job)

    _dispatch_one(db, job_id=job.id, sender=sender)
    db.refresh(job)
    return job


def _mark_job_queued(db: Session, *, job_id: int, celery_task_id: str) -> None:
    job = db.get(BackgroundJob, job_id)
    if job is None:
        return
    if job.status == BackgroundJobStatus.PENDING.value:
        job.status = BackgroundJobStatus.QUEUED.value
    job.celery_task_id = celery_task_id
    job.queued_at = job.queued_at or datetime.now(timezone.utc)
    db.commit()


def _dispatch_one(
    db: Session,
    *,
    job_id: int,
    sender: TaskSender | None = None,
) -> bool:
    outbox_event = repository.get_outbox_event_for_job(db, job_id=job_id)
    if outbox_event is None or outbox_event.status != "pending":
        return outbox_event is not None and outbox_event.status == "published"

    active_sender = sender or _default_task_sender
    task_args = outbox_event.task_args or {}
    job_id_arg = task_args.get("job_id", job_id)
    try:
        celery_task_id = active_sender(
            task_name=outbox_event.task_name,
            args=[job_id_arg],
            queue=outbox_event.queue,
        )
    except Exception as exc:
        attempts_so_far = outbox_event.attempts
        backoff_seconds = min(
            _PUBLISH_BACKOFF_CAP_SECONDS,
            _PUBLISH_BACKOFF_BASE_SECONDS * (2**attempts_so_far),
        )
        repository.mark_publish_failed(
            db,
            outbox_event=outbox_event,
            error_class_name=exc.__class__.__name__,
            next_attempt_at=datetime.now(timezone.utc) + timedelta(seconds=backoff_seconds),
        )
        db.commit()
        log_event(
            logger,
            logging.WARNING,
            "job_outbox_publish_failed",
            job_id=job_id,
            task_name=outbox_event.task_name,
            queue=outbox_event.queue,
            attempts=outbox_event.attempts,
            error_type=exc.__class__.__name__,
        )
        return False

    repository.mark_published(db, outbox_event=outbox_event)
    db.commit()
    _mark_job_queued(db, job_id=job_id, celery_task_id=celery_task_id)
    log_event(
        logger,
        logging.INFO,
        "job_outbox_published",
        job_id=job_id,
        task_name=outbox_event.task_name,
        queue=outbox_event.queue,
    )
    return True


def redispatch_job(
    db: Session,
    *,
    job_id: int,
    sender: TaskSender | None = None,
) -> bool:
    """Re-arm and immediately attempt to redispatch an existing job's
    outbox row - used by bounded provider self-healing (Part M) and
    stale-job recovery (Part P), both of which reuse the *same* job row
    rather than creating a new one."""

    repository.reset_to_pending(db, job_id=job_id)
    db.commit()
    return _dispatch_one(db, job_id=job_id, sender=sender)


def dispatch_pending_outbox_events(
    db: Session,
    *,
    batch_size: int,
    sender: TaskSender | None = None,
) -> OutboxDispatchSummary:
    """The maintenance sweep (Part E.6). Safe to run from any number of
    concurrent dispatcher replicas: `list_pending_outbox_events` row-locks
    each candidate row, so two dispatchers racing on the same row simply
    serialize rather than double-publish; a row already flipped to
    `published` by another replica by the time this one gets the lock is
    a no-op here (`_dispatch_one` re-checks `status == "pending"`)."""

    outbox_events = repository.list_pending_outbox_events(db, limit=batch_size)
    published = 0
    failed = 0
    for outbox_event in outbox_events:
        if _dispatch_one(db, job_id=outbox_event.job_id, sender=sender):
            published += 1
        else:
            failed += 1
    return OutboxDispatchSummary(scanned=len(outbox_events), published=published, failed=failed)
