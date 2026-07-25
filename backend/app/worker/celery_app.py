from __future__ import annotations

from celery import Celery
from kombu import Queue

from app.core.config import settings


celery_app = Celery(
    "eternal_world",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
)

#: Task 65.9 (Part G) - explicit queue topology. Only `embedding` and
#: `maintenance` are actually populated with real tasks today; the other
#: four are declared so the topology exists ahead of the product features
#: that will use them (no product behavior is implemented for them here -
#: Part G: "Do not implement product features that do not yet exist").
#: User-controlled input never selects a queue or raw task name - routing
#: below is a fixed, code-only mapping from task name to queue.
EMBEDDING_QUEUE = "embedding"
DOCUMENT_PROCESSING_QUEUE = "document_processing"
AI_GENERATION_QUEUE = "ai_generation"
MEDIA_QUEUE = "media"
NOTIFICATIONS_QUEUE = "notifications"
MAINTENANCE_QUEUE = "maintenance"

celery_app.conf.task_queues = (
    Queue(EMBEDDING_QUEUE),
    Queue(DOCUMENT_PROCESSING_QUEUE),
    Queue(AI_GENERATION_QUEUE),
    Queue(MEDIA_QUEUE),
    Queue(NOTIFICATIONS_QUEUE),
    Queue(MAINTENANCE_QUEUE),
)
celery_app.conf.task_default_queue = MAINTENANCE_QUEUE

#: Task routing is a fixed, explicit table keyed by the Celery task's own
#: registered name - never influenced by request/queue-message payload
#: content (Part G: "User-controlled input must never determine a raw
#: Celery task or queue name"). Embedding-heavy tasks (real BGE-M3
#: inference) route to `embedding`; lightweight maintenance/outbox-
#: dispatch tasks route to `maintenance`.
celery_app.conf.task_routes = {
    "app.worker.tasks.run_avatar_memory_indexing_job": {"queue": EMBEDDING_QUEUE},
    "app.worker.tasks.run_memorial_contribution_indexing_job": {"queue": EMBEDDING_QUEUE},
    "app.worker.tasks.run_biography_indexing_job": {"queue": EMBEDDING_QUEUE},
    "app.worker.tasks.run_rag_source_processing_job": {"queue": EMBEDDING_QUEUE},
    "app.worker.tasks.run_multi_embedding_eval_job": {"queue": EMBEDDING_QUEUE},
    "app.worker.tasks.run_outbox_dispatch_job": {"queue": MAINTENANCE_QUEUE},
    "app.worker.tasks.run_stale_job_recovery_job": {"queue": MAINTENANCE_QUEUE},
    "app.worker.tasks.run_job_smoke_test": {"queue": MAINTENANCE_QUEUE},
}

celery_app.conf.update(
    task_always_eager=settings.celery_task_always_eager,
    task_eager_propagates=settings.celery_task_eager_propagates,
    task_track_started=True,
    timezone="UTC",
    #: Task 65.9 (Part O) - reliability baseline. Safe globally because
    #: every real task this app registers is idempotent (deterministic
    #: Qdrant point ids, get-or-create evidence rows, idempotent outbox/
    #: job-status transitions) - late acknowledgement plus worker-lost
    #: rejection means a killed/recycled worker's in-flight task is
    #: redelivered rather than silently dropped, and redelivery converges
    #: safely instead of duplicating data.
    task_acks_late=True,
    task_reject_on_worker_lost=True,
    #: One task in flight per prefetch slot - avoids one worker process
    #: hoarding a burst of embedding jobs while sibling worker replicas
    #: sit idle (Part H: "Scale throughput by adding worker replicas, not
    #: by uncontrolled concurrency against one model object").
    worker_prefetch_multiplier=1,
    #: Broker-reconnect resilience (Part O) - a transient Redis restart/
    #: network blip must not permanently wedge a worker process.
    broker_connection_retry_on_startup=True,
    broker_connection_retry=True,
    broker_connection_max_retries=None,
    #: Bounded task time limits (Part O) - a single hung embedding call
    #: must not occupy a worker slot forever. Soft limit raises inside the
    #: task (caught as an ordinary exception by the existing try/except in
    #: each task body); the hard limit forcibly terminates the child
    #: process if the soft limit is somehow not honored.
    task_soft_time_limit=settings.celery_task_soft_time_limit_seconds,
    task_time_limit=settings.celery_task_time_limit_seconds,
)

#: Task 65.9 (Part E/P) - the maintenance worker's embedded beat schedule.
#: Both tasks are cheap, idempotent, and safe to run from multiple
#: scheduler/worker replicas (see `job_outbox.service.
#: dispatch_pending_outbox_events` and `app.worker.tasks.
#: run_stale_job_recovery_job`), so no distributed-lock/leader-election
#: mechanism is required here.
celery_app.conf.beat_schedule = {
    "dispatch-pending-outbox-events": {
        "task": "app.worker.tasks.run_outbox_dispatch_job",
        "schedule": 15.0,
        "options": {"queue": MAINTENANCE_QUEUE},
    },
    "recover-stale-jobs": {
        "task": "app.worker.tasks.run_stale_job_recovery_job",
        "schedule": 60.0,
        "options": {"queue": MAINTENANCE_QUEUE},
    },
}

celery_app.autodiscover_tasks(["app.worker"])
