import time

from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.metrics import (
    build_metrics_response,
    set_memory_enrichment_current,
    set_memory_promotions_current,
)
from app.db.models import AvatarMemoryPromotion, ConversationMemoryCandidate
from app.db.session import get_db
from app.modules.job_tracking.service import refresh_async_queue_metrics


router = APIRouter(tags=["metrics"])

#: Task 65.13.11 — Prometheus scrapes the backend process, while the Beat
#: refresh historically ran only inside maintenance_worker. Debounced
#: refresh on scrape keeps async_queue_* gauges fresh in this process.
_last_async_queue_metrics_refresh_at = 0.0


def _maybe_refresh_async_queue_metrics(db: Session) -> None:
    global _last_async_queue_metrics_refresh_at
    min_interval = float(settings.metrics_async_queue_refresh_min_interval_seconds)
    now = time.monotonic()
    if min_interval > 0 and (now - _last_async_queue_metrics_refresh_at) < min_interval:
        return
    refresh_async_queue_metrics(db)
    _last_async_queue_metrics_refresh_at = now


@router.get("/metrics")
def metrics(db: Session = Depends(get_db)) -> object:
    rows = db.execute(
        select(
            AvatarMemoryPromotion.promotion_status,
            func.count(AvatarMemoryPromotion.id),
        ).group_by(AvatarMemoryPromotion.promotion_status)
    ).all()
    set_memory_promotions_current(
        counts_by_status={status: int(count) for status, count in rows}
    )
    enrichment_rows = db.execute(
        select(
            ConversationMemoryCandidate.enrichment_status,
            func.count(ConversationMemoryCandidate.id),
        )
        .where(ConversationMemoryCandidate.workflow_version >= 2)
        .group_by(ConversationMemoryCandidate.enrichment_status)
    ).all()
    dispute_rows = db.execute(
        select(
            ConversationMemoryCandidate.dispute_status,
            func.count(ConversationMemoryCandidate.id),
        )
        .where(ConversationMemoryCandidate.workflow_version >= 2)
        .group_by(ConversationMemoryCandidate.dispute_status)
    ).all()
    set_memory_enrichment_current(
        counts_by_status={status: int(count) for status, count in enrichment_rows},
        disputes_by_status={status: int(count) for status, count in dispute_rows},
    )
    _maybe_refresh_async_queue_metrics(db)
    return build_metrics_response()
