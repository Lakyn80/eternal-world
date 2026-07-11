from __future__ import annotations

import pytest

from app.main import app
from app.modules.auth.schemas import RegisterRequest
from app.modules.auth.service import register_user
from app.modules.avatar_memory_promotions.service import (
    AvatarMemoryPromotionCandidateStateError,
    AvatarMemoryPromotionInvalidTransitionError,
    AvatarMemoryPromotionNotFoundError,
    cancel_promotion,
    create_or_get_promotion_for_candidate,
    get_promotion,
    list_promotions,
)
from app.modules.conversation_memory_candidates.schemas import MemoryCandidateReviewUpdate
from app.modules.conversation_memory_candidates.service import (
    approve_candidate,
    archive_candidate,
    create_candidate,
    reject_candidate,
)
from app.modules.memory_profiles.schemas import MemoryProfileCreate
from app.modules.memory_profiles.service import create_memory_profile


def _get_test_db_session():
    testing_session_local = app.state.testing_session_local
    return testing_session_local()


def _create_user_with_profile():
    db = _get_test_db_session()
    try:
        user = register_user(
            db,
            RegisterRequest(
                email="promotion-owner@example.com",
                password="StrongPass123",
                full_name="Promotion Owner",
            ),
        )
        profile = create_memory_profile(
            db,
            current_user=user,
            payload=MemoryProfileCreate(
                name="Promotion Profile",
                biography="Promotion profile biography",
                personality="Careful and factual",
            ),
        )
        return user, profile
    finally:
        db.close()


def _build_candidate_payload(*, owner_user_id: int, profile_id: int, excerpt: str = "Ты пела мне песню."):
    from app.modules.conversation_memory_candidates.schemas import MemoryCandidateCreate

    return MemoryCandidateCreate(
        owner_user_id=owner_user_id,
        avatar_id="eva_novakova_demo",
        profile_id=profile_id,
        trace_id="promotion-trace-1",
        user_message_excerpt=excerpt,
        proposed_memory_text="Пользователь утверждает, что бабушка пела ему песню перед сном.",
        reason="User introduced a possible personal memory not found in current evidence.",
        language="ru",
    )


def test_approve_candidate_creates_pending_index_promotion(client):
    user, profile = _create_user_with_profile()
    db = _get_test_db_session()
    try:
        candidate = create_candidate(
            db,
            payload=_build_candidate_payload(owner_user_id=user.id, profile_id=profile.id),
        )

        approval = approve_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=MemoryCandidateReviewUpdate(review_note="Подтверждено", reviewed_by=user.id),
        )

        assert approval.candidate.status == "approved"
        assert approval.promotion_created is True
        assert approval.promotion.candidate_id == candidate.id
        assert approval.promotion.promotion_status == "pending_index"
        assert approval.promotion.approved_memory_text == candidate.proposed_memory_text
    finally:
        db.close()


def test_promotion_service_does_not_duplicate_for_same_candidate(client):
    user, profile = _create_user_with_profile()
    db = _get_test_db_session()
    try:
        candidate = create_candidate(
            db,
            payload=_build_candidate_payload(owner_user_id=user.id, profile_id=profile.id),
        )
        approval = approve_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=MemoryCandidateReviewUpdate(reviewed_by=user.id),
        )

        second_outcome = create_or_get_promotion_for_candidate(
            db,
            candidate=approval.candidate,
        )

        assert second_outcome.created is False
        assert second_outcome.promotion.id == approval.promotion.id
        assert len(list_promotions(db, owner_user_id=user.id, profile_id=profile.id)) == 1
    finally:
        db.close()


def test_rejected_candidate_cannot_create_promotion(client):
    user, profile = _create_user_with_profile()
    db = _get_test_db_session()
    try:
        candidate = create_candidate(
            db,
            payload=_build_candidate_payload(owner_user_id=user.id, profile_id=profile.id),
        )
        rejected = reject_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=MemoryCandidateReviewUpdate(reviewed_by=user.id, rejection_reason="Нет источника"),
        )

        with pytest.raises(AvatarMemoryPromotionCandidateStateError):
            create_or_get_promotion_for_candidate(db, candidate=rejected)
    finally:
        db.close()


def test_archived_candidate_cannot_create_promotion(client):
    user, profile = _create_user_with_profile()
    db = _get_test_db_session()
    try:
        candidate = create_candidate(
            db,
            payload=_build_candidate_payload(owner_user_id=user.id, profile_id=profile.id),
        )
        archived = archive_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=MemoryCandidateReviewUpdate(reviewed_by=user.id),
        )

        with pytest.raises(AvatarMemoryPromotionCandidateStateError):
            create_or_get_promotion_for_candidate(db, candidate=archived)
    finally:
        db.close()


def test_pending_index_promotion_can_be_cancelled(client):
    user, profile = _create_user_with_profile()
    db = _get_test_db_session()
    try:
        candidate = create_candidate(
            db,
            payload=_build_candidate_payload(owner_user_id=user.id, profile_id=profile.id),
        )
        approval = approve_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=MemoryCandidateReviewUpdate(reviewed_by=user.id),
        )

        cancelled = cancel_promotion(
            db,
            owner_user_id=user.id,
            promotion_id=approval.promotion.id,
        )

        assert cancelled.promotion_status == "cancelled"
        assert cancelled.cancelled_at is not None
        assert cancelled.indexed_at is None
    finally:
        db.close()


def test_cancel_invalid_transition_is_rejected(client):
    user, profile = _create_user_with_profile()
    db = _get_test_db_session()
    try:
        candidate = create_candidate(
            db,
            payload=_build_candidate_payload(owner_user_id=user.id, profile_id=profile.id),
        )
        approval = approve_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=MemoryCandidateReviewUpdate(reviewed_by=user.id),
        )
        cancel_promotion(
            db,
            owner_user_id=user.id,
            promotion_id=approval.promotion.id,
        )

        with pytest.raises(AvatarMemoryPromotionInvalidTransitionError):
            cancel_promotion(
                db,
                owner_user_id=user.id,
                promotion_id=approval.promotion.id,
            )
    finally:
        db.close()


def test_get_promotion_not_found_raises_error(client):
    user, _profile = _create_user_with_profile()
    db = _get_test_db_session()
    try:
        with pytest.raises(AvatarMemoryPromotionNotFoundError):
            get_promotion(
                db,
                owner_user_id=user.id,
                promotion_id=999,
            )
    finally:
        db.close()
