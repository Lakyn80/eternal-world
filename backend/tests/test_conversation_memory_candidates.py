from __future__ import annotations

import pytest

from app.main import app
from app.modules.auth.schemas import RegisterRequest
from app.modules.auth.service import register_user
from app.modules.conversation_memory_candidates.schemas import (
    MEMORY_CANDIDATE_EXCERPT_MAX_LENGTH,
    MemoryCandidateCreate,
    MemoryCandidateReviewUpdate,
)
from app.modules.conversation_memory_candidates.service import (
    ConversationMemoryCandidateInvalidTransitionError,
    ConversationMemoryCandidateNotFoundError,
    create_candidate,
    get_candidate,
    list_candidates,
    reject_candidate,
    approve_candidate,
    archive_candidate,
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
                email="memory-candidate-owner@example.com",
                password="StrongPass123",
                full_name="Memory Candidate Owner",
            ),
        )
        profile = create_memory_profile(
            db,
            current_user=user,
            payload=MemoryProfileCreate(
                name="Candidate Profile",
                biography="Candidate profile biography",
                personality="Calm and careful",
            ),
        )
        return user, profile
    finally:
        db.close()


def _build_candidate_payload(*, owner_user_id: int, profile_id: int, excerpt: str = "Ты пела мне песню.") -> MemoryCandidateCreate:
    return MemoryCandidateCreate(
        owner_user_id=owner_user_id,
        avatar_id="eva_novakova_demo",
        profile_id=profile_id,
        trace_id="candidate-trace-1",
        user_message_excerpt=excerpt,
        proposed_memory_text="Пользователь утверждает, что бабушка пела ему песню перед сном.",
        reason="User introduced a possible personal memory not found in current evidence.",
        language="ru",
    )


def test_create_and_get_conversation_memory_candidate(client):
    user, profile = _create_user_with_profile()
    db = _get_test_db_session()
    try:
        candidate = create_candidate(
            db,
            payload=_build_candidate_payload(owner_user_id=user.id, profile_id=profile.id),
        )

        fetched = get_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
        )

        assert fetched.id == candidate.id
        assert fetched.status == "needs_review"
        assert fetched.confidence == "unverified"
        assert fetched.profile_id == profile.id
    finally:
        db.close()


def test_list_conversation_memory_candidates_returns_newest_first(client):
    user, profile = _create_user_with_profile()
    db = _get_test_db_session()
    try:
        first = create_candidate(
            db,
            payload=_build_candidate_payload(
                owner_user_id=user.id,
                profile_id=profile.id,
                excerpt="Первый возможный эпизод.",
            ),
        )
        second = create_candidate(
            db,
            payload=_build_candidate_payload(
                owner_user_id=user.id,
                profile_id=profile.id,
                excerpt="Второй возможный эпизод.",
            ),
        )

        items = list_candidates(
            db,
            owner_user_id=user.id,
            profile_id=profile.id,
            avatar_id="eva_novakova_demo",
        )

        assert [item.id for item in items] == [second.id, first.id]
    finally:
        db.close()


def test_candidate_excerpt_is_safely_truncated():
    payload = _build_candidate_payload(
        owner_user_id=1,
        profile_id=1,
        excerpt="длинный " * 40,
    )

    assert len(payload.user_message_excerpt) == MEMORY_CANDIDATE_EXCERPT_MAX_LENGTH
    assert payload.user_message_excerpt.endswith("...")


def test_approve_candidate_updates_review_fields(client):
    user, profile = _create_user_with_profile()
    db = _get_test_db_session()
    try:
        candidate = create_candidate(
            db,
            payload=_build_candidate_payload(owner_user_id=user.id, profile_id=profile.id),
        )

        approved = approve_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=MemoryCandidateReviewUpdate(review_note="Подтверждено семьей", reviewed_by=user.id),
        )

        assert approved.status == "approved"
        assert approved.review_note == "Подтверждено семьей"
        assert approved.reviewed_by == user.id
        assert approved.reviewed_at is not None
        assert approved.rejection_reason is None
    finally:
        db.close()


def test_reject_candidate_updates_rejection_reason(client):
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
            payload=MemoryCandidateReviewUpdate(
                review_note="Нужно больше подтверждений",
                rejection_reason="Нет подтверждающего источника",
                reviewed_by=user.id,
            ),
        )

        assert rejected.status == "rejected"
        assert rejected.review_note == "Нужно больше подтверждений"
        assert rejected.rejection_reason == "Нет подтверждающего источника"
    finally:
        db.close()


def test_archive_candidate_updates_status_without_rejection_reason(client):
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
            payload=MemoryCandidateReviewUpdate(review_note="Архивировано", reviewed_by=user.id),
        )

        assert archived.status == "archived"
        assert archived.review_note == "Архивировано"
        assert archived.rejection_reason is None
    finally:
        db.close()


def test_invalid_transition_is_rejected(client):
    user, profile = _create_user_with_profile()
    db = _get_test_db_session()
    try:
        candidate = create_candidate(
            db,
            payload=_build_candidate_payload(owner_user_id=user.id, profile_id=profile.id),
        )
        approve_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=MemoryCandidateReviewUpdate(reviewed_by=user.id),
        )

        with pytest.raises(ConversationMemoryCandidateInvalidTransitionError):
            archive_candidate(
                db,
                owner_user_id=user.id,
                candidate_id=candidate.id,
                payload=MemoryCandidateReviewUpdate(reviewed_by=user.id),
            )
    finally:
        db.close()


def test_candidate_not_found_raises_service_error(client):
    user, _profile = _create_user_with_profile()
    db = _get_test_db_session()
    try:
        with pytest.raises(ConversationMemoryCandidateNotFoundError):
            get_candidate(
                db,
                owner_user_id=user.id,
                candidate_id=999,
            )
    finally:
        db.close()
