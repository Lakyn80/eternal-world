from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.metrics import build_metrics_response, set_memory_promotions_current
from app.db.models import AvatarMemoryPromotion
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
    return build_metrics_response()
