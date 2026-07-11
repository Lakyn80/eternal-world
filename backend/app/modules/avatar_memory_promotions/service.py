from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.db.models import AvatarMemoryPromotion, ConversationMemoryCandidate
from app.modules.avatar_memory_promotions import repository
from app.modules.avatar_memory_promotions.schemas import (
    AvatarMemoryPromotionCreate,
    AvatarMemoryPromotionStatus,
)
from app.modules.memory_profiles import repository as memory_profiles_repository


class AvatarMemoryPromotionNotFoundError(Exception):
    pass


class AvatarMemoryPromotionInvalidTransitionError(Exception):
    pass


class AvatarMemoryPromotionCandidateStateError(Exception):
    pass


class AvatarMemoryPromotionProfileNotFoundError(Exception):
    pass


@dataclass(frozen=True)
class AvatarMemoryPromotionCreateOutcome:
    promotion: AvatarMemoryPromotion
    created: bool


def _validate_owned_profile(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int | None,
) -> None:
    if profile_id is None:
        return
    profile = memory_profiles_repository.get_memory_profile_for_user(
        db,
        user_id=owner_user_id,
        profile_id=profile_id,
    )
    if profile is None:
        raise AvatarMemoryPromotionProfileNotFoundError("Memory profile not found")


def create_or_get_promotion_for_candidate(
    db: Session,
    *,
    candidate: ConversationMemoryCandidate,
) -> AvatarMemoryPromotionCreateOutcome:
    if candidate.status != "approved":
        raise AvatarMemoryPromotionCandidateStateError(
            "Only approved memory candidates can create promotions."
        )

    existing_promotion = repository.get_avatar_memory_promotion_by_candidate_id(
        db,
        candidate_id=candidate.id,
    )
    if existing_promotion is not None:
        return AvatarMemoryPromotionCreateOutcome(
            promotion=existing_promotion,
            created=False,
        )

    _validate_owned_profile(
        db,
        owner_user_id=candidate.owner_user_id,
        profile_id=candidate.profile_id,
    )
    payload = AvatarMemoryPromotionCreate(
        owner_user_id=candidate.owner_user_id,
        candidate_id=candidate.id,
        avatar_id=candidate.avatar_id,
        profile_id=candidate.profile_id,
        approved_memory_text=candidate.proposed_memory_text,
        normalized_memory_text=candidate.proposed_memory_text,
        language=candidate.language,
        trace_id=candidate.trace_id,
        source_candidate_status_snapshot=candidate.status,
        review_note_snapshot=candidate.review_note,
    )
    promotion = repository.create_avatar_memory_promotion(
        db,
        candidate_id=payload.candidate_id,
        owner_user_id=payload.owner_user_id,
        avatar_id=payload.avatar_id,
        profile_id=payload.profile_id,
        source_type=payload.source_type.value,
        promotion_status=payload.promotion_status.value,
        approved_memory_text=payload.approved_memory_text,
        normalized_memory_text=payload.normalized_memory_text,
        language=payload.language,
        trace_id=payload.trace_id,
        source_candidate_status_snapshot=payload.source_candidate_status_snapshot,
        review_note_snapshot=payload.review_note_snapshot,
    )
    db.flush()
    return AvatarMemoryPromotionCreateOutcome(
        promotion=promotion,
        created=True,
    )


def list_promotions(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int | None = None,
    avatar_id: str | None = None,
) -> list[AvatarMemoryPromotion]:
    _validate_owned_profile(
        db,
        owner_user_id=owner_user_id,
        profile_id=profile_id,
    )
    return repository.list_avatar_memory_promotions(
        db,
        owner_user_id=owner_user_id,
        profile_id=profile_id,
        avatar_id=avatar_id,
    )


def get_promotion(
    db: Session,
    *,
    owner_user_id: int,
    promotion_id: int,
    for_update: bool = False,
) -> AvatarMemoryPromotion:
    promotion = repository.get_avatar_memory_promotion_for_owner(
        db,
        owner_user_id=owner_user_id,
        promotion_id=promotion_id,
        for_update=for_update,
    )
    if promotion is None:
        raise AvatarMemoryPromotionNotFoundError("Avatar memory promotion not found")
    return promotion


def cancel_promotion(
    db: Session,
    *,
    owner_user_id: int,
    promotion_id: int,
) -> AvatarMemoryPromotion:
    promotion = get_promotion(
        db,
        owner_user_id=owner_user_id,
        promotion_id=promotion_id,
        for_update=True,
    )
    if promotion.promotion_status != AvatarMemoryPromotionStatus.PENDING_INDEX.value:
        raise AvatarMemoryPromotionInvalidTransitionError(
            f"Cannot cancel promotion from `{promotion.promotion_status}`."
        )
    promotion.promotion_status = AvatarMemoryPromotionStatus.CANCELLED.value
    promotion.cancelled_at = datetime.now(timezone.utc)
    promotion.failure_reason = None
    db.commit()
    db.refresh(promotion)
    return promotion
