from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.db.models import ConversationMemoryCandidate
from app.modules.avatar_memory_promotions import service as avatar_memory_promotions_service
from app.modules.conversation_memory_candidates import repository
from app.modules.conversation_memory_candidates.schemas import (
    MemoryCandidateCreate,
    MemoryCandidateRead,
    MemoryCandidateReviewUpdate,
    MemoryCandidateStatus,
    build_memory_candidate_read,
)
from app.modules.memory_profiles import repository as memory_profiles_repository


class ConversationMemoryCandidateNotFoundError(Exception):
    pass


class ConversationMemoryCandidateProfileNotFoundError(Exception):
    pass


class ConversationMemoryCandidateInvalidTransitionError(Exception):
    pass


@dataclass(frozen=True)
class CandidateApprovalResult:
    candidate: ConversationMemoryCandidate
    promotion: object
    promotion_created: bool


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
        raise ConversationMemoryCandidateProfileNotFoundError("Memory profile not found")


def create_candidate(
    db: Session,
    *,
    payload: MemoryCandidateCreate,
) -> ConversationMemoryCandidate:
    _validate_owned_profile(
        db,
        owner_user_id=payload.owner_user_id,
        profile_id=payload.profile_id,
    )
    candidate = repository.create_conversation_memory_candidate(
        db,
        owner_user_id=payload.owner_user_id,
        avatar_id=payload.avatar_id,
        profile_id=payload.profile_id,
        conversation_id=payload.conversation_id,
        trace_id=payload.trace_id,
        source=payload.source.value,
        status=payload.status.value,
        confidence=payload.confidence.value,
        user_message_excerpt=payload.user_message_excerpt,
        proposed_memory_text=payload.proposed_memory_text,
        reason=payload.reason,
        language=payload.language,
    )
    db.commit()
    db.refresh(candidate)
    return candidate


def list_candidates(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int | None = None,
    avatar_id: str | None = None,
) -> list[ConversationMemoryCandidate]:
    _validate_owned_profile(
        db,
        owner_user_id=owner_user_id,
        profile_id=profile_id,
    )
    return repository.list_conversation_memory_candidates(
        db,
        owner_user_id=owner_user_id,
        profile_id=profile_id,
        avatar_id=avatar_id,
    )


def get_candidate(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
) -> ConversationMemoryCandidate:
    candidate = repository.get_conversation_memory_candidate_for_owner(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate_id,
    )
    if candidate is None:
        raise ConversationMemoryCandidateNotFoundError("Memory candidate not found")
    return candidate


def _assert_transition_allowed(
    *,
    current_status: str,
    next_status: MemoryCandidateStatus,
) -> None:
    if current_status != MemoryCandidateStatus.NEEDS_REVIEW.value:
        raise ConversationMemoryCandidateInvalidTransitionError(
            f"Cannot change candidate from `{current_status}` to `{next_status.value}`."
        )


def _apply_review_state(
    candidate: ConversationMemoryCandidate,
    *,
    next_status: MemoryCandidateStatus,
    payload: MemoryCandidateReviewUpdate | None,
) -> None:
    _assert_transition_allowed(
        current_status=candidate.status,
        next_status=next_status,
    )

    review_payload = payload or MemoryCandidateReviewUpdate()
    candidate.status = next_status.value
    candidate.reviewed_at = datetime.now(timezone.utc)
    candidate.reviewed_by = review_payload.reviewed_by

    if next_status == MemoryCandidateStatus.REJECTED:
        candidate.review_note = review_payload.review_note
        candidate.rejection_reason = review_payload.rejection_reason
        return

    if review_payload.rejection_reason is not None:
        raise ConversationMemoryCandidateInvalidTransitionError(
            f"rejection_reason is not allowed when setting status `{next_status.value}`."
        )
    candidate.review_note = review_payload.review_note
    candidate.rejection_reason = None


def approve_candidate(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    payload: MemoryCandidateReviewUpdate | None = None,
) -> CandidateApprovalResult:
    candidate = get_candidate(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate_id,
    )
    _apply_review_state(
        candidate,
        next_status=MemoryCandidateStatus.APPROVED,
        payload=payload,
    )
    promotion_outcome = avatar_memory_promotions_service.create_or_get_promotion_for_candidate(
        db,
        candidate=candidate,
    )
    db.commit()
    db.refresh(candidate)
    db.refresh(promotion_outcome.promotion)
    return CandidateApprovalResult(
        candidate=candidate,
        promotion=promotion_outcome.promotion,
        promotion_created=promotion_outcome.created,
    )


def reject_candidate(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    payload: MemoryCandidateReviewUpdate | None = None,
) -> ConversationMemoryCandidate:
    candidate = get_candidate(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate_id,
    )
    _apply_review_state(
        candidate,
        next_status=MemoryCandidateStatus.REJECTED,
        payload=payload,
    )
    db.commit()
    db.refresh(candidate)
    return candidate


def archive_candidate(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
    payload: MemoryCandidateReviewUpdate | None = None,
) -> ConversationMemoryCandidate:
    candidate = get_candidate(
        db,
        owner_user_id=owner_user_id,
        candidate_id=candidate_id,
    )
    _apply_review_state(
        candidate,
        next_status=MemoryCandidateStatus.ARCHIVED,
        payload=payload,
    )
    db.commit()
    db.refresh(candidate)
    return candidate


def build_candidate_list_response(
    candidates: list[ConversationMemoryCandidate],
) -> list[MemoryCandidateRead]:
    return [build_memory_candidate_read(candidate) for candidate in candidates]
