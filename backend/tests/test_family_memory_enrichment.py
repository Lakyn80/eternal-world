from __future__ import annotations

import pytest
from pydantic import ValidationError

from app.main import app
from app.modules.auth.schemas import RegisterRequest
from app.modules.auth.service import register_user
from app.modules.conversation_memory_candidates.schemas import MemoryCandidateCreate
from app.modules.conversation_memory_candidates.service import create_candidate
from app.modules.family_memory_enrichment.schemas import (
    ClarificationAnswerRequest,
    ClarificationSkipRequest,
    DemoFamilyActorContext,
    FamilyMemoryContributionCreate,
    OwnerReviewRequest,
    PersonalMemoryDetails,
)
from app.modules.family_memory_enrichment.service import (
    FamilyMemoryAuthorizationError,
    FamilyMemoryInvalidTransitionError,
    add_contribution,
    answer_next_clarification,
    initialize_candidate,
    list_contributions,
    owner_review,
    skip_clarification,
)
from app.modules.family_memory_enrichment import repository as enrichment_repository
from app.modules.family_memory_enrichment.eligibility import (
    FamilyMemoryEligibilityError,
    get_promotion_block_reason,
)
from app.modules.avatar_memory_indexing.service import (
    AvatarMemoryIndexingEligibilityError,
    index_promotion,
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
                full_name="Family workflow owner",
            ),
        )
        profile = create_memory_profile(
            db,
            current_user=user,
            payload=MemoryProfileCreate(
                name=FAMILY_AVATAR_RU_E2E_PROFILE_NAME,
                biography="Family workflow test profile",
                personality="Warm and factual",
            ),
        )
        return user, profile
    finally:
        db.close()


def _create_enrichment_candidate(*, owner_user_id: int, profile_id: int):
    db = _db()
    try:
        return create_candidate(
            db,
            payload=MemoryCandidateCreate(
                owner_user_id=owner_user_id,
                avatar_id="eva_novakova_demo",
                profile_id=profile_id,
                trace_id="family-enrichment-test",
                user_message_excerpt="Бабушка пела мне колыбельную перед сном.",
                proposed_memory_text="Бабушка пела колыбельную перед сном.",
                reason="A family member introduced a possible personal memory.",
                language="ru",
                enrichment_status="draft",
                finalized_memory_text=None,
                privacy_scope="private_owner",
                workflow_version=2,
            ),
        )
    finally:
        db.close()


def test_bedtime_song_enrichment_is_one_question_at_a_time_and_owner_gated(client):
    user, profile = _create_scope()
    candidate = _create_enrichment_candidate(owner_user_id=user.id, profile_id=profile.id)
    contributor = DemoFamilyActorContext(
        actor_id="family-anna",
        actor_role="contributor",
        relationship_to_owner="granddaughter",
    )
    db = _db()
    try:
        enrichment = initialize_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            actor=contributor,
            initial_text="Бабушка пела мне колыбельную перед сном.",
            trace_id="family-enrichment-test",
        )
        assert enrichment.memory_type == "bedtime_song"
        assert enrichment.enrichment_status == "collecting_details"
        assert enrichment.unresolved_clarification_count == 3
        assert enrichment.next_clarification_question.question_key == "song_title"

        for answer, expected_next in (
            ("«Спи, моя радость, усни»", "place"),
            ("Дома в детской комнате", "approximate_period"),
            ("Летом, когда мне было около шести лет", None),
        ):
            enrichment = answer_next_clarification(
                db,
                owner_user_id=user.id,
                candidate_id=candidate.id,
                payload=ClarificationAnswerRequest(
                    actor_id=contributor.actor_id,
                    actor_role=contributor.actor_role,
                    relationship_to_owner=contributor.relationship_to_owner,
                    answer_text=answer,
                    trace_id="family-enrichment-test",
                ),
            )
            if expected_next is None:
                assert enrichment.next_clarification_question is None
            else:
                assert enrichment.next_clarification_question.question_key == expected_next

        assert enrichment.enrichment_status == "ready_for_owner_review"
        assert enrichment.unresolved_clarification_count == 0
        assert "Спи, моя радость, усни" in enrichment.finalized_memory_text

        legacy_bypass = client.post(
            f"/api/demo/fa-chat/memory-candidates/{candidate.id}/approve",
            json={"review_note": "bypass attempt", "reviewed_by": user.id},
        )
        assert legacy_bypass.status_code == 403

        reviewed = owner_review(
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
        assert reviewed.review_status == "approved"
        assert reviewed.promotion_created is True
        assert reviewed.promotion_status == "pending_index"
        assert reviewed.searchable_as_fact is False
        assert reviewed.explicit_indexing_required is True
        assert len(
            list_contributions(
                db,
                owner_user_id=user.id,
                candidate_id=candidate.id,
                actor=DemoFamilyActorContext(
                    actor_id="demo-owner-eva",
                    actor_role="owner",
                ),
            )
        ) == 5
    finally:
        db.close()


def test_conflicting_contributions_preserve_attributed_perspectives(client):
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
            initial_text="Мы вместе собирали яблоки в саду.",
        )
        enrichment = add_contribution(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=FamilyMemoryContributionCreate(
                actor_id="demo-owner-eva",
                actor_role="owner",
                contribution_type="owner_correction",
                contribution_text="Это были груши, а не яблоки.",
                structured_details=PersonalMemoryDetails(
                    what_happened="Мы вместе собирали груши в саду."
                ),
            ),
        )
        assert enrichment.dispute_status == "disputed"
        assert "Член семьи указывает" in enrichment.finalized_memory_text
        assert "Владелец аватара указывает" in enrichment.finalized_memory_text
        history = list_contributions(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            actor=DemoFamilyActorContext(actor_id="demo-owner-eva", actor_role="owner"),
        )
        assert history[0].contribution_text == "Мы вместе собирали яблоки в саду."
        assert history[1].contribution_text == "Это были груши, а не яблоки."

        with pytest.raises(FamilyMemoryInvalidTransitionError):
            owner_review(
                db,
                owner_user_id=user.id,
                candidate_id=candidate.id,
                payload=OwnerReviewRequest(
                    actor_id="demo-owner-eva",
                    actor_role="owner",
                    action="confirm",
                    privacy_scope="all_family",
                ),
            )
        db.rollback()

        reviewed = owner_review(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=OwnerReviewRequest(
                actor_id="demo-owner-eva",
                actor_role="owner",
                action="approve_multiple_perspectives",
                privacy_scope="all_family",
            ),
        )
        assert reviewed.dispute_status == "resolved"
        assert reviewed.review_status == "approved"
        assert reviewed.promotion_status == "pending_index"
    finally:
        db.close()


def test_private_candidate_is_visible_to_its_contributor_but_not_an_unrelated_actor(client):
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

    own_response = client.get(
        f"/api/demo/fa-chat/memory-candidates/{candidate.id}/enrichment",
        params={"actor_id": "family-anna", "actor_role": "contributor"},
    )
    assert own_response.status_code == 200

    unrelated_response = client.get(
        f"/api/demo/fa-chat/memory-candidates/{candidate.id}/enrichment",
        params={"actor_id": "family-boris", "actor_role": "contributor"},
    )
    assert unrelated_response.status_code == 404


def test_chat_active_candidate_answers_without_rag_runtime(client):
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

    response = client.post(
        "/api/demo/fa-chat/message",
        json={
            "profile_id": profile.id,
            "message": "«Спи, моя радость, усни»",
            "active_memory_candidate_id": candidate.id,
            "actor_id": "family-anna",
            "actor_role": "contributor",
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["retrieval_used"] is False
    assert body["active_memory_candidate_id"] == candidate.id
    assert body["next_clarification_question"]["question_key"] == "place"


def test_family_enrichment_metrics_are_low_cardinality_and_include_durable_state(client):
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

    metrics = client.get("/metrics")
    assert metrics.status_code == 200
    text = metrics.text
    assert 'memory_contribution_created_total{role="contributor"}' in text
    assert 'memory_clarification_total{status="pending"}' in text
    assert 'memory_enrichment_current{status="collecting_details"} 1.0' in text
    assert "family-anna" not in text
    assert "family-enrichment-test" not in text


def test_contribution_actor_and_privacy_input_limits_are_strict():
    with pytest.raises(ValidationError):
        DemoFamilyActorContext(actor_id="family-anna", actor_role="administrator")
    with pytest.raises(ValidationError):
        FamilyMemoryContributionCreate(
            actor_id="family-anna",
            actor_role="contributor",
            contribution_text="x" * 1001,
        )
    with pytest.raises(ValidationError):
        OwnerReviewRequest(
            actor_id="demo-owner-eva",
            actor_role="owner",
            action="confirm",
            privacy_scope="everyone",
        )


def test_owner_edit_reject_request_more_dispute_and_optional_skip(client):
    user, profile = _create_scope()
    db = _db()
    try:
        def new_general(text: str):
            candidate = _create_enrichment_candidate(owner_user_id=user.id, profile_id=profile.id)
            enrichment = initialize_candidate(
                db,
                owner_user_id=user.id,
                candidate_id=candidate.id,
                actor=DemoFamilyActorContext(actor_id="family-anna", actor_role="contributor"),
                initial_text=text,
            )
            return candidate, enrichment

        edited_candidate, _ = new_general("Мы вместе собирали яблоки в саду.")
        with pytest.raises(FamilyMemoryAuthorizationError):
            owner_review(
                db,
                owner_user_id=user.id,
                candidate_id=edited_candidate.id,
                payload=OwnerReviewRequest(
                    actor_id="family-anna",
                    actor_role="contributor",
                    action="confirm",
                ),
            )
        edited = owner_review(
            db,
            owner_user_id=user.id,
            candidate_id=edited_candidate.id,
            payload=OwnerReviewRequest(
                actor_id="demo-owner-eva",
                actor_role="owner",
                action="edit_and_confirm",
                finalized_memory_text="По словам владельца, семья вместе собирала яблоки в саду.",
                privacy_scope="all_family",
            ),
        )
        assert edited.review_status == "approved"
        assert edited.dispute_status == "resolved"

        rejected_candidate, _ = new_general("Мы вместе гуляли у реки.")
        rejected = owner_review(
            db,
            owner_user_id=user.id,
            candidate_id=rejected_candidate.id,
            payload=OwnerReviewRequest(
                actor_id="demo-owner-eva",
                actor_role="owner",
                action="reject",
                rejection_reason="Владелец не подтвердил эпизод.",
            ),
        )
        assert rejected.review_status == "rejected"
        assert rejected.promotion_id is None

        details_candidate, _ = new_general("Мы вместе готовили пирог.")
        collecting = owner_review(
            db,
            owner_user_id=user.id,
            candidate_id=details_candidate.id,
            payload=OwnerReviewRequest(
                actor_id="demo-owner-eva",
                actor_role="owner",
                action="request_more_details",
                review_note="Какой это был праздник?",
            ),
        )
        assert collecting.enrichment_status == "collecting_details"
        assert collecting.next_clarification_question.required is True
        answered = answer_next_clarification(
            db,
            owner_user_id=user.id,
            candidate_id=details_candidate.id,
            payload=ClarificationAnswerRequest(
                actor_id="family-anna",
                actor_role="contributor",
                answer_text="Это было на семейный Новый год.",
            ),
        )
        assert answered.enrichment_status == "ready_for_owner_review"
        assert "семейный Новый год" in answered.finalized_memory_text

        optional = enrichment_repository.create_clarification(
            db,
            candidate_id=details_candidate.id,
            question_key="optional_emotion",
            question_text="Какие чувства остались?",
            language="ru",
            status="pending",
            required=False,
        )
        db.commit()
        skipped = skip_clarification(
            db,
            owner_user_id=user.id,
            candidate_id=details_candidate.id,
            clarification_id=optional.id,
            payload=ClarificationSkipRequest(
                actor_id="family-anna",
                actor_role="contributor",
            ),
        )
        assert skipped.enrichment_status == "ready_for_owner_review"

        disputed_candidate, _ = new_general("Мы встречались у старого дома.")
        disputed = owner_review(
            db,
            owner_user_id=user.id,
            candidate_id=disputed_candidate.id,
            payload=OwnerReviewRequest(
                actor_id="demo-owner-eva",
                actor_role="owner",
                action="mark_disputed",
                review_note="Место требует проверки.",
            ),
        )
        assert disputed.dispute_status == "disputed"
        assert disputed.review_status == "needs_review"
        assert disputed.promotion_id is None
    finally:
        db.close()


def test_promotion_and_indexing_revalidate_enrichment_and_privacy(client):
    user, profile = _create_scope()
    db = _db()
    try:
        private_candidate = _create_enrichment_candidate(
            owner_user_id=user.id,
            profile_id=profile.id,
        )
        initialize_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=private_candidate.id,
            actor=DemoFamilyActorContext(actor_id="family-anna", actor_role="contributor"),
            initial_text="Мы вместе собирали яблоки в саду.",
        )
        private_approval = owner_review(
            db,
            owner_user_id=user.id,
            candidate_id=private_candidate.id,
            payload=OwnerReviewRequest(
                actor_id="demo-owner-eva",
                actor_role="owner",
                action="confirm",
                privacy_scope="private_owner",
            ),
        )
        assert private_approval.review_status == "approved"
        assert private_approval.promotion_id is None

        selected = _create_enrichment_candidate(owner_user_id=user.id, profile_id=profile.id)
        initialize_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=selected.id,
            actor=DemoFamilyActorContext(actor_id="family-anna", actor_role="contributor"),
            initial_text="Мы вместе гуляли у реки.",
        )
        selected_row = enrichment_repository.get_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=selected.id,
            for_update=True,
        )
        selected_row.status = "approved"
        selected_row.owner_review_actor_role = "owner"
        selected_row.privacy_scope = "selected_family"
        db.commit()
        from app.modules.avatar_memory_promotions.service import create_or_get_promotion_for_candidate

        with pytest.raises(FamilyMemoryEligibilityError) as selected_error:
            create_or_get_promotion_for_candidate(db, candidate=selected_row)
        assert selected_error.value.reason == "privacy_scope"

        index_candidate = _create_enrichment_candidate(owner_user_id=user.id, profile_id=profile.id)
        initialize_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=index_candidate.id,
            actor=DemoFamilyActorContext(actor_id="family-anna", actor_role="contributor"),
            initial_text="Мы вместе читали семейную книгу.",
        )
        approved = owner_review(
            db,
            owner_user_id=user.id,
            candidate_id=index_candidate.id,
            payload=OwnerReviewRequest(
                actor_id="demo-owner-eva",
                actor_role="owner",
                action="confirm",
                privacy_scope="all_family",
            ),
        )
        row = enrichment_repository.get_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=index_candidate.id,
            for_update=True,
        )
        row.enrichment_status = "collecting_details"
        row.unresolved_clarification_count = 1
        db.commit()
        with pytest.raises(AvatarMemoryIndexingEligibilityError):
            index_promotion(
                db,
                owner_user_id=user.id,
                promotion_id=approved.promotion_id,
            )
    finally:
        db.close()


@pytest.mark.parametrize(
    ("status", "enrichment_status", "unresolved", "dispute", "expected"),
    (
        ("needs_review", "ready_for_owner_review", 0, "none", "not_approved"),
        ("approved", "draft", 0, "none", "incomplete"),
        ("approved", "collecting_details", 1, "none", "collecting_details"),
        ("approved", "ready_for_owner_review", 1, "none", "unresolved_clarification"),
        ("rejected", "ready_for_owner_review", 0, "none", "not_approved"),
        ("approved", "ready_for_owner_review", 0, "disputed", "disputed"),
    ),
)
def test_promotion_policy_blocks_unsafe_candidate_states(
    client,
    status,
    enrichment_status,
    unresolved,
    dispute,
    expected,
):
    user, profile = _create_scope()
    candidate = _create_enrichment_candidate(owner_user_id=user.id, profile_id=profile.id)
    db = _db()
    try:
        row = enrichment_repository.get_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            for_update=True,
        )
        row.status = status
        row.enrichment_status = enrichment_status
        row.finalized_memory_text = "Атрибутированный финальный текст."
        row.unresolved_clarification_count = unresolved
        row.dispute_status = dispute
        row.privacy_scope = "all_family"
        row.owner_review_actor_role = "owner"
        db.flush()
        assert get_promotion_block_reason(db, candidate=row) == expected
    finally:
        db.rollback()
        db.close()
