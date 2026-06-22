from __future__ import annotations

from celery import Celery

from app.core.config import settings


celery_app = Celery(
    "eternal_world",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
)

celery_app.conf.update(
    task_always_eager=settings.celery_task_always_eager,
    task_eager_propagates=settings.celery_task_eager_propagates,
    task_track_started=True,
    timezone="UTC",
)

celery_app.autodiscover_tasks(["app.worker"])
