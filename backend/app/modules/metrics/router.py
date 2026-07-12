from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.metrics import (
    build_metrics_response,
    set_memory_enrichment_current,
    set_memory_promotions_current,
)
from app.db.models import AvatarMemoryPromotion, ConversationMemoryCandidate
from app.db.session import get_db


router = APIRouter(tags=["metrics"])


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
    return build_metrics_response()
