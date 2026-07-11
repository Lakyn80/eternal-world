from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import AvatarMemoryPromotion


def create_avatar_memory_promotion(
    db: Session,
    *,
    candidate_id: int,
    owner_user_id: int,
    avatar_id: str,
    profile_id: int | None,
    source_type: str,
    promotion_status: str,
    approved_memory_text: str,
    normalized_memory_text: str,
    language: str | None,
    trace_id: str | None,
    source_candidate_status_snapshot: str,
    review_note_snapshot: str | None,
) -> AvatarMemoryPromotion:
    promotion = AvatarMemoryPromotion(
        candidate_id=candidate_id,
        owner_user_id=owner_user_id,
        avatar_id=avatar_id,
        profile_id=profile_id,
        source_type=source_type,
        promotion_status=promotion_status,
        approved_memory_text=approved_memory_text,
        normalized_memory_text=normalized_memory_text,
        language=language,
        trace_id=trace_id,
        source_candidate_status_snapshot=source_candidate_status_snapshot,
        review_note_snapshot=review_note_snapshot,
    )
    db.add(promotion)
    return promotion


def get_avatar_memory_promotion_by_candidate_id(
    db: Session,
    *,
    candidate_id: int,
) -> AvatarMemoryPromotion | None:
    statement = select(AvatarMemoryPromotion).where(AvatarMemoryPromotion.candidate_id == candidate_id)
    return db.scalar(statement)


def list_avatar_memory_promotions(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int | None = None,
    avatar_id: str | None = None,
) -> list[AvatarMemoryPromotion]:
    statement = select(AvatarMemoryPromotion).where(
        AvatarMemoryPromotion.owner_user_id == owner_user_id,
    )
    if profile_id is not None:
        statement = statement.where(AvatarMemoryPromotion.profile_id == profile_id)
    if avatar_id is not None:
        statement = statement.where(AvatarMemoryPromotion.avatar_id == avatar_id)

    statement = statement.order_by(
        AvatarMemoryPromotion.created_at.desc(),
        AvatarMemoryPromotion.id.desc(),
    )
    return list(db.scalars(statement))


def get_avatar_memory_promotion_for_owner(
    db: Session,
    *,
    owner_user_id: int,
    promotion_id: int,
) -> AvatarMemoryPromotion | None:
    statement = select(AvatarMemoryPromotion).where(
        AvatarMemoryPromotion.id == promotion_id,
        AvatarMemoryPromotion.owner_user_id == owner_user_id,
    )
    return db.scalar(statement)
