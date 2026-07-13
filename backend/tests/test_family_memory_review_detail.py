from __future__ import annotations

import pytest

from app.main import app
from app.modules.auth.schemas import RegisterRequest
from app.modules.auth.service import register_user
from app.modules.conversation_memory_candidates.schemas import MemoryCandidateCreate
from app.modules.conversation_memory_candidates.service import create_candidate
from app.modules.family_memory_enrichment import repository as enrichment_repository
from app.modules.family_memory_enrichment.schemas import (
    ClarificationAnswerRequest,
    DemoFamilyActorContext,
    FamilyMemoryContributionCreate,
    OwnerReviewRequest,
    PersonalMemoryDetails,
)
from app.modules.family_memory_enrichment.service import (
    add_contribution,
    answer_next_clarification,
    initialize_candidate,
    owner_review,
)
from app.modules.memory_profiles.schemas import MemoryProfileCreate
from app.modules.memory_profiles.service import create_memory_profile
from app.modules.rag_evaluation.brain_eval_e2e_bootstrap import (
    FAMILY_AVATAR_RU_E2E_EMAIL,
    FAMILY_AVATAR_RU_E2E_PASSWORD,
    FAMILY_AVATAR_RU_E2E_PROFILE_NAME,
)


def _db():
    return app.state.testing_session_local()


def _create_scope():
    db = _db()
    try:
        user = register_user(
            db,
            RegisterRequest(
                email=FAMILY_AVATAR_RU_E2E_EMAIL,
                password=FAMILY_AVATAR_RU_E2E_PASSWORD,
                full_name="Family review detail owner",
            ),
        )
        profile = create_memory_profile(
            db,
            current_user=user,
            payload=MemoryProfileCreate(
                name=FAMILY_AVATAR_RU_E2E_PROFILE_NAME,
                biography="Family review detail test profile",
                personality="Warm and factual",
            ),
        )
        return user, profile
    finally:
        db.close()


def _create_enrichment_candidate(*, owner_user_id: int, profile_id: int, privacy_scope: str = "private_owner"):
    db = _db()
    try:
        return create_candidate(
            db,
            payload=MemoryCandidateCreate(
                owner_user_id=owner_user_id,
                avatar_id="eva_novakova_demo",
                profile_id=profile_id,
                trace_id="family-review-detail-test",
                user_message_excerpt="Бабушка пела мне колыбельную перед сном.",
                proposed_memory_text="Бабушка пела колыбельную перед сном.",
                reason="A family member introduced a possible personal memory.",
                language="ru",
                enrichment_status="draft",
                finalized_memory_text=None,
                privacy_scope=privacy_scope,
                workflow_version=2,
            ),
        )
    finally:
        db.close()


CONTRIBUTOR = {"actor_id": "family-anna", "actor_role": "contributor", "relationship_to_owner": "granddaughter"}
OWNER = {"actor_id": "demo-owner-eva", "actor_role": "owner"}


def test_review_summary_shows_contributor_and_hides_promotion_before_approval(client):
    user, profile = _create_scope()
    candidate = _create_enrichment_candidate(owner_user_id=user.id, profile_id=profile.id)
    db = _db()
    try:
        initialize_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            actor=DemoFamilyActorContext(
                actor_id=CONTRIBUTOR["actor_id"],
                actor_role=CONTRIBUTOR["actor_role"],
                relationship_to_owner=CONTRIBUTOR["relationship_to_owner"],
            ),
            initial_text="Бабушка пела мне колыбельную перед сном.",
        )
    finally:
        db.close()

    response = client.get(
        "/api/demo/fa-chat/memory-candidates/review-summary",
        params={"profile_id": profile.id, **OWNER},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 1
    item = body["items"][0]
    assert item["candidate_id"] == candidate.id
    assert item["contributor_actor_id"] == "family-anna"
    assert item["contributor_actor_role"] == "contributor"
    assert item["contributor_relationship_to_owner"] == "granddaughter"
    assert item["promotion_id"] is None
    assert item["searchable_as_fact"] is False


def test_review_summary_hides_private_candidate_from_unrelated_actor(client):
    user, profile = _create_scope()
    candidate = _create_enrichment_candidate(owner_user_id=user.id, profile_id=profile.id)
    db = _db()
    try:
        initialize_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            actor=DemoFamilyActorContext(actor_id="family-anna", actor_role="contributor"),
            initial_text="Мы вместе собирали яблоки в саду.",
        )
    finally:
        db.close()

    response = client.get(
        "/api/demo/fa-chat/memory-candidates/review-summary",
        params={
            "profile_id": profile.id,
            "actor_id": "family-unrelated",
            "actor_role": "contributor",
        },
    )
    assert response.status_code == 200
    assert response.json() == {"items": [], "total": 0}


def test_review_detail_blocks_owner_actions_while_collecting_details(client):
    user, profile = _create_scope()
    candidate = _create_enrichment_candidate(owner_user_id=user.id, profile_id=profile.id)
    db = _db()
    try:
        initialize_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            actor=DemoFamilyActorContext(actor_id="family-anna", actor_role="contributor"),
            initial_text="Бабушка пела мне колыбельную перед сном.",
        )
    finally:
        db.close()

    response = client.get(
        f"/api/demo/fa-chat/memory-candidates/{candidate.id}/review-detail",
        params={"profile_id": profile.id, **OWNER},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["enrichment"]["enrichment_status"] == "collecting_details"
    assert len(body["contributions"]) == 1
    assert len(body["clarifications"]) == 1
    assert body["clarifications"][0]["status"] == "pending"
    assert body["is_owner_actor"] is True
    assert body["can_confirm"] is False
    assert body["can_edit_and_confirm"] is False
    assert body["can_reject"] is True
    assert body["can_request_more_details"] is True
    assert body["can_mark_disputed"] is True
    assert body["can_approve_multiple_perspectives"] is False
    assert body["can_index"] is False
    assert "collecting_details" in body["blocked_reasons"]
    assert "not_promoted_yet" in body["blocked_reasons"]
    assert "privacy_scope_not_indexable" in body["blocked_reasons"]


def test_review_detail_contributor_actor_sees_no_owner_actions(client):
    user, profile = _create_scope()
    candidate = _create_enrichment_candidate(owner_user_id=user.id, profile_id=profile.id)
    db = _db()
    try:
        initialize_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            actor=DemoFamilyActorContext(actor_id="family-anna", actor_role="contributor"),
            initial_text="Бабушка пела мне колыбельную перед сном.",
        )
    finally:
        db.close()

    response = client.get(
        f"/api/demo/fa-chat/memory-candidates/{candidate.id}/review-detail",
        params={"profile_id": profile.id, "actor_id": "family-anna", "actor_role": "contributor"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["is_owner_actor"] is False
    for flag in (
        "can_confirm",
        "can_edit_and_confirm",
        "can_reject",
        "can_request_more_details",
        "can_mark_disputed",
        "can_approve_multiple_perspectives",
        "can_index",
    ):
        assert body[flag] is False
    assert "actor_is_not_owner" in body["blocked_reasons"]


def test_review_detail_ready_for_review_then_approval_creates_pending_index_promotion(client):
    user, profile = _create_scope()
    candidate = _create_enrichment_candidate(owner_user_id=user.id, profile_id=profile.id)
    contributor = DemoFamilyActorContext(actor_id="family-anna", actor_role="contributor")
    db = _db()
    try:
        initialize_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            actor=contributor,
            initial_text="Бабушка пела мне колыбельную перед сном.",
        )
        for answer in (
            "«Спи, моя радость, усни»",
            "Дома в детской комнате",
            "Летом, когда мне было около шести лет",
        ):
            answer_next_clarification(
                db,
                owner_user_id=user.id,
                candidate_id=candidate.id,
                payload=ClarificationAnswerRequest(
                    actor_id=contributor.actor_id,
                    actor_role=contributor.actor_role,
                    answer_text=answer,
                ),
            )
    finally:
        db.close()

    ready_response = client.get(
        f"/api/demo/fa-chat/memory-candidates/{candidate.id}/review-detail",
        params={"profile_id": profile.id, **OWNER},
    )
    ready_body = ready_response.json()
    assert ready_body["enrichment"]["enrichment_status"] == "ready_for_owner_review"
    assert ready_body["can_confirm"] is True
    assert ready_body["can_edit_and_confirm"] is True
    assert ready_body["can_approve_multiple_perspectives"] is False
    assert len(ready_body["clarifications"]) == 3
    assert all(item["status"] == "answered" for item in ready_body["clarifications"])

    db = _db()
    try:
        owner_review(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=OwnerReviewRequest(
                actor_id="demo-owner-eva",
                actor_role="owner",
                action="confirm",
                privacy_scope="all_family",
                review_note="Подтверждено владельцем",
            ),
        )
    finally:
        db.close()

    approved_response = client.get(
        f"/api/demo/fa-chat/memory-candidates/{candidate.id}/review-detail",
        params={"profile_id": profile.id, **OWNER},
    )
    approved_body = approved_response.json()
    assert approved_body["enrichment"]["review_status"] == "approved"
    assert approved_body["promotion"]["promotion_status"] == "pending_index"
    assert approved_body["promotion"]["searchable_as_fact"] is False
    assert approved_body["can_index"] is True
    assert approved_body["can_confirm"] is False
    assert "candidate_review_already_terminal" in approved_body["blocked_reasons"]

    # Simulate a completed indexing run without invoking real Qdrant/BGE-M3 infrastructure.
    db = _db()
    try:
        promotion_row = enrichment_repository.get_candidate(
            db, owner_user_id=user.id, candidate_id=candidate.id
        ).avatar_memory_promotion
        promotion_row.promotion_status = "indexed"
        db.commit()
    finally:
        db.close()

    indexed_response = client.get(
        f"/api/demo/fa-chat/memory-candidates/{candidate.id}/review-detail",
        params={"profile_id": profile.id, **OWNER},
    )
    indexed_body = indexed_response.json()
    assert indexed_body["promotion"]["promotion_status"] == "indexed"
    assert indexed_body["promotion"]["searchable_as_fact"] is True
    assert indexed_body["can_index"] is False
    assert "promotion_status_indexed" in indexed_body["blocked_reasons"]


def test_review_detail_disputed_candidate_allows_perspectives_not_plain_confirm(client):
    user, profile = _create_scope()
    candidate = _create_enrichment_candidate(owner_user_id=user.id, profile_id=profile.id)
    db = _db()
    try:
        initialize_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            actor=DemoFamilyActorContext(actor_id="family-anna", actor_role="contributor"),
            initial_text="Мы вместе собирали яблоки в саду.",
        )
        add_contribution(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=FamilyMemoryContributionCreate(
                actor_id="demo-owner-eva",
                actor_role="owner",
                contribution_type="owner_correction",
                contribution_text="Это были груши, а не яблоки.",
                structured_details=PersonalMemoryDetails(what_happened="Мы вместе собирали груши в саду."),
            ),
        )
    finally:
        db.close()

    response = client.get(
        f"/api/demo/fa-chat/memory-candidates/{candidate.id}/review-detail",
        params={"profile_id": profile.id, **OWNER},
    )
    body = response.json()
    assert body["enrichment"]["dispute_status"] == "disputed"
    assert body["can_confirm"] is False
    assert body["can_approve_multiple_perspectives"] is True
    assert "disputed" in body["blocked_reasons"]


def test_review_detail_returns_404_for_missing_candidate(client):
    user, profile = _create_scope()
    response = client.get(
        "/api/demo/fa-chat/memory-candidates/999999/review-detail",
        params={"profile_id": profile.id, **OWNER},
    )
    assert response.status_code == 404
    assert "detail" in response.json()


def test_clarifications_endpoint_returns_full_history_not_only_next(client):
    user, profile = _create_scope()
    candidate = _create_enrichment_candidate(owner_user_id=user.id, profile_id=profile.id)
    contributor = DemoFamilyActorContext(actor_id="family-anna", actor_role="contributor")
    db = _db()
    try:
        initialize_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            actor=contributor,
            initial_text="Бабушка пела мне колыбельную перед сном.",
        )
        answer_next_clarification(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=ClarificationAnswerRequest(
                actor_id=contributor.actor_id,
                actor_role=contributor.actor_role,
                answer_text="«Спи, моя радость, усни»",
            ),
        )
    finally:
        db.close()

    response = client.get(
        f"/api/demo/fa-chat/memory-candidates/{candidate.id}/clarifications",
        params={"actor_id": "family-anna", "actor_role": "contributor"},
    )
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 2
    statuses = {item["question_key"]: item["status"] for item in items}
    assert statuses["song_title"] == "answered"
    assert statuses["place"] == "pending"
