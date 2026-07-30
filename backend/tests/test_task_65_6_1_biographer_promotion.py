"""Task 65.6.1 - approved Biographer candidate promotion, biography
projection, indexing, and chat recall.

Covers the generic lifecycle bug: an approved AI-Biographer candidate
(always `privacy_scope=private_owner`, `workflow_version=2`) used to be
silently excluded from `family_memory_enrichment.eligibility.
INDEXABLE_PRIVACY_SCOPES`, so `owner_review`'s confirm/edit_and_confirm/
approve_multiple_perspectives branch never created a promotion, never
enqueued indexing, and left no failure state at all - approved in the UI,
invisible to Biography and chat forever. These tests cover the fix (Parts
C/D/E/F/G/H/I/J/L of the task spec) without hardcoding any candidate id,
account, or memorial-specific text.
"""

from __future__ import annotations

from app.db.models import AvatarMemoryPromotion, ConversationMemoryCandidate
from app.main import app
from app.modules.avatar_memory_indexing.service import (
    AvatarMemoryIndexingExecutionError,
    index_promotion,
)
from app.modules.avatar_memory_promotions import repository as promotion_repository
from app.modules.avatar_memory_promotions.reconciliation import (
    find_approved_candidates_for_reconciliation,
    reconcile_candidate_promotions,
)
from app.modules.avatar_memory_promotions.service import (
    AvatarMemoryPromotionCreateOutcome,
    create_or_get_promotion_for_candidate,
)
from app.modules.embeddings.providers.base import EmbeddingVector
from app.modules.family_memory_enrichment.eligibility import (
    BROAD_VISIBILITY_PRIVACY_SCOPES,
    INDEXABLE_PRIVACY_SCOPES,
    get_promotion_block_reason,
)


PASSWORD = "StrongPass123"


class FakeEncoder:
    def __init__(self, *, dimension: int = 1024) -> None:
        self.dimension = dimension
        self.calls = 0

    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        self.calls += 1
        return EmbeddingVector(values=[0.01] * self.dimension, dimension=self.dimension, metadata={})


class FakeWriter:
    def __init__(self, *, fail_upsert: bool = False, dimension: int = 1024) -> None:
        self.fail_upsert = fail_upsert
        self.dimension = dimension
        self.points: dict[tuple[str, str], dict[str, object]] = {}
        self.upsert_calls = 0
        self.delete_calls = 0

    def collection_vector_size(self, *, collection_name: str) -> int | None:
        return self.dimension

    def get_point(self, *, collection_name: str, point_id: str) -> dict[str, object] | None:
        return self.points.get((collection_name, point_id))

    def upsert_point(self, *, collection_name: str, point_id: str, vector, payload) -> None:
        self.upsert_calls += 1
        if self.fail_upsert:
            raise RuntimeError("qdrant temporarily unavailable")
        self.points[(collection_name, point_id)] = {"vector": list(vector), "payload": dict(payload)}

    def delete_point(self, *, collection_name: str, point_id: str) -> None:
        self.delete_calls += 1
        self.points.pop((collection_name, point_id), None)


def _db():
    return app.state.testing_session_local()


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _register_and_login(client, email: str) -> str:
    client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": email})
    response = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    assert response.status_code == 200
    return response.json()["access_token"]


def _create_memorial(client, token: str, name: str = "Biographer Promotion Memorial") -> int:
    response = client.post("/api/memorials", headers=_auth_headers(token), json={"name": name})
    assert response.status_code == 201
    return response.json()["id"]


def _create_ready_for_review_candidate(*, owner_user_id: int, profile_id: int, text: str) -> int:
    """Builds a `ConversationMemoryCandidate` row with the exact shape a
    real AI-Biographer candidate has once the owner reaches the review step
    (`source="conversation"`, `workflow_version=2`, `avatar_id=str(profile_
    id)`, `privacy_scope=private_owner` - all `avatar_biographer.service.
    answer_question`'s real defaults - `enrichment_status=
    ready_for_owner_review`, no unresolved clarification).

    Deliberately bypasses the real `/biographer/next-question` HTTP flow:
    that endpoint performs a real BGE-M3 retrieval-augmented question
    generation call even with the AI provider mocked (Task 65.6/65.7
    territory, irrelevant to this task), which makes it far slower than a
    direct DB build without changing anything this test suite actually
    needs to verify - the approval/promotion/indexing/biography/retrieval
    behavior under test starts from exactly this candidate shape either
    way."""

    from app.modules.conversation_memory_candidates.schemas import MemoryCandidateCreate
    from app.modules.conversation_memory_candidates.service import create_candidate

    db = _db()
    try:
        candidate = create_candidate(
            db,
            payload=MemoryCandidateCreate(
                owner_user_id=owner_user_id,
                avatar_id=str(profile_id),
                profile_id=profile_id,
                trace_id="biog-promo-test-trace",
                user_message_excerpt=text,
                proposed_memory_text=text,
                reason="AI Biographer topic: childhood",
                # Russian, not Czech: a Czech-origin candidate additionally
                # requires a current Russian translation before it is
                # promotion-eligible (`family_memory_enrichment.eligibility.
                # get_finalized_memory_translation_block_reason`) - a real,
                # separate concern this test file is not about. Real
                # Biographer candidates are `cs` or `ru` depending on the
                # memorial's chosen locale; both are equally realistic.
                language="ru",
                enrichment_status="ready_for_owner_review",
                finalized_memory_text=text,
                privacy_scope="private_owner",
                workflow_version=2,
            ),
        )
        return candidate.id
    finally:
        db.close()


def _get_profile_owner_user_id(profile_id: int) -> int:
    from app.db.models import MemoryProfile

    db = _db()
    try:
        return db.get(MemoryProfile, profile_id).user_id
    finally:
        db.close()


def _get_candidate(candidate_id: int) -> ConversationMemoryCandidate:
    db = _db()
    try:
        return db.get(ConversationMemoryCandidate, candidate_id)
    finally:
        db.close()


def _get_promotion_for_candidate(candidate_id: int) -> AvatarMemoryPromotion | None:
    db = _db()
    try:
        return promotion_repository.get_avatar_memory_promotion_by_candidate_id(db, candidate_id=candidate_id)
    finally:
        db.close()


# --- Root cause: private_owner is eligible for promotion, but only visible to the owner --


def test_private_owner_scope_is_indexable_but_not_broadly_visible():
    """The exact split that fixes Task 65.6.1 without reintroducing a
    visibility regression: `private_owner` must be promotion-eligible, but
    must NOT be part of the separate "broadly visible to any contributor/
    trusted_reviewer" set."""

    assert "private_owner" in INDEXABLE_PRIVACY_SCOPES
    assert "private_owner" not in BROAD_VISIBILITY_PRIVACY_SCOPES
    assert BROAD_VISIBILITY_PRIVACY_SCOPES == frozenset({"all_family", "public_legacy"})


def test_owner_review_confirm_without_privacy_override_creates_one_promotion_for_private_owner_candidate(client):
    """Reproduces the exact real-world bug: the owner confirms a Biographer
    candidate WITHOUT overriding `privacy_scope` (it stays the Biographer
    default, `private_owner`). Before the fix this silently produced no
    promotion at all - `body["promotion_id"]` was `None` and no exception
    was ever raised."""

    token = _register_and_login(client, "biog-promo-owner1@example.com")
    profile_id = _create_memorial(client, token)
    candidate_id = _create_ready_for_review_candidate(
        owner_user_id=_get_profile_owner_user_id(profile_id),
        profile_id=profile_id,
        text="Moje rodina byla vždy velmi důležitá.",
    )

    review = client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/owner-review",
        headers=_auth_headers(token),
        json={"action": "confirm"},
    )
    assert review.status_code == 200
    body = review.json()
    assert body["review_status"] == "approved"
    assert body["privacy_scope"] == "private_owner"
    assert body["promotion_id"] is not None
    assert body["promotion_status"] == "pending_index"

    db = _db()
    try:
        promotions = db.query(AvatarMemoryPromotion).filter(AvatarMemoryPromotion.candidate_id == candidate_id).all()
        assert len(promotions) == 1
        assert promotions[0].promotion_status == "pending_index"
    finally:
        db.close()


def test_rejected_candidate_is_never_promoted(client):
    token = _register_and_login(client, "biog-promo-owner2@example.com")
    profile_id = _create_memorial(client, token)
    candidate_id = _create_ready_for_review_candidate(
        owner_user_id=_get_profile_owner_user_id(profile_id),
        profile_id=profile_id,
        text="Rodina byla důležitá, ale toto se nakonec zamítne.",
    )

    review = client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/owner-review",
        headers=_auth_headers(token),
        json={"action": "reject", "rejection_reason": "Not accurate"},
    )
    assert review.status_code == 200
    assert review.json()["review_status"] == "rejected"
    assert _get_promotion_for_candidate(candidate_id) is None

    db = _db()
    try:
        candidate = db.get(ConversationMemoryCandidate, candidate_id)
        assert get_promotion_block_reason(db, candidate=candidate) == "not_approved"
    finally:
        db.close()


def test_repeated_promotion_creation_is_idempotent(client):
    """Calling `create_or_get_promotion_for_candidate` twice for the same
    already-approved candidate must return the same row, never a second
    one - covers repeated-approval and repeated-promotion-retry
    idempotency together (Task 65.6.1 Part L items 4/5)."""

    db = _db()
    try:
        from app.modules.auth.schemas import RegisterRequest
        from app.modules.auth.service import register_user
        from app.modules.conversation_memory_candidates.schemas import MemoryCandidateCreate
        from app.modules.conversation_memory_candidates.service import create_candidate
        from app.modules.memory_profiles.schemas import MemoryProfileCreate
        from app.modules.memory_profiles.service import create_memory_profile

        user = register_user(
            db, RegisterRequest(email="biog-promo-idem@example.com", password=PASSWORD, full_name="Idem Owner")
        )
        profile = create_memory_profile(
            db, current_user=user, payload=MemoryProfileCreate(name="Idem Profile", biography="Bio", personality="Warm")
        )
        candidate = create_candidate(
            db,
            payload=MemoryCandidateCreate(
                owner_user_id=user.id,
                avatar_id=str(profile.id),
                profile_id=profile.id,
                trace_id="idem-trace",
                user_message_excerpt="Rodina byla důležitá.",
                proposed_memory_text="Rodina byla důležitá.",
                reason="AI Biographer topic: family",
                language="ru",
                enrichment_status="ready_for_owner_review",
                finalized_memory_text="Rodina byla důležitá.",
                privacy_scope="private_owner",
                workflow_version=2,
            ),
        )
        candidate.status = "approved"
        candidate.owner_review_actor_role = "owner"
        db.commit()
        db.refresh(candidate)

        first = create_or_get_promotion_for_candidate(db, candidate=candidate)
        second = create_or_get_promotion_for_candidate(db, candidate=candidate)

        assert isinstance(first, AvatarMemoryPromotionCreateOutcome)
        assert first.created is True
        assert second.created is False
        assert first.promotion.id == second.promotion.id
        assert (
            db.query(AvatarMemoryPromotion).filter(AvatarMemoryPromotion.candidate_id == candidate.id).count() == 1
        )
    finally:
        db.close()


# --- Indexing: idempotent retry, retry-from-failed, Qdrant provenance ------


def test_indexing_is_idempotent_on_repeated_call(client):
    token = _register_and_login(client, "biog-promo-owner3@example.com")
    profile_id = _create_memorial(client, token)
    candidate_id = _create_ready_for_review_candidate(
        owner_user_id=_get_profile_owner_user_id(profile_id),
        profile_id=profile_id,
        text="Rodina se scházela každou neděli k obědu.",
    )
    review = client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/owner-review",
        headers=_auth_headers(token),
        json={"action": "confirm"},
    )
    promotion_id = review.json()["promotion_id"]
    owner_user_id = _get_candidate(candidate_id).owner_user_id

    writer = FakeWriter()
    db = _db()
    try:
        first = index_promotion(
            db, owner_user_id=owner_user_id, promotion_id=promotion_id, writer=writer, encoder=FakeEncoder(), validate_runtime=False
        )
        assert first.result == "indexed"
        assert writer.upsert_calls == 1

        second = index_promotion(
            db, owner_user_id=owner_user_id, promotion_id=promotion_id, writer=writer, encoder=FakeEncoder(), validate_runtime=False
        )
        assert second.result == "already_indexed"
        assert writer.upsert_calls == 1  # no duplicate point written
        assert len(writer.points) == 1
    finally:
        db.close()


def test_indexed_qdrant_payload_includes_profile_and_biographer_provenance(client):
    token = _register_and_login(client, "biog-promo-owner4@example.com")
    profile_id = _create_memorial(client, token)
    candidate_id = _create_ready_for_review_candidate(
        owner_user_id=_get_profile_owner_user_id(profile_id),
        profile_id=profile_id,
        text="Dědeček nás učil hrát šachy.",
    )
    review = client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/owner-review",
        headers=_auth_headers(token),
        json={"action": "confirm"},
    )
    promotion_id = review.json()["promotion_id"]
    owner_user_id = _get_candidate(candidate_id).owner_user_id

    writer = FakeWriter()
    db = _db()
    try:
        result = index_promotion(
            db, owner_user_id=owner_user_id, promotion_id=promotion_id, writer=writer, encoder=FakeEncoder(), validate_runtime=False
        )
        assert result.result == "indexed"
        [point] = writer.points.values()
        payload = point["payload"]
        assert payload["profile_id"] == profile_id
        assert payload["candidate_id"] == candidate_id
        assert payload["promotion_id"] == promotion_id
        assert payload["source_type"] == "conversation_candidate"
        assert payload["memory_status"] == "verified"
        assert payload["privacy_scope"] == "private_owner"
        assert payload["workflow_version"] == 2
    finally:
        db.close()


def test_failed_indexing_is_recorded_and_retryable(client):
    """Task 65.6.1 fix: `failed` used to be excluded from the retryable
    promotion-status set in `avatar_memory_indexing.service.index_promotion`
    - a transient Qdrant failure left the promotion permanently stuck."""

    token = _register_and_login(client, "biog-promo-owner5@example.com")
    profile_id = _create_memorial(client, token)
    candidate_id = _create_ready_for_review_candidate(
        owner_user_id=_get_profile_owner_user_id(profile_id),
        profile_id=profile_id,
        text="Babička vařila nejlepší svíčkovou.",
    )
    review = client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/owner-review",
        headers=_auth_headers(token),
        json={"action": "confirm"},
    )
    promotion_id = review.json()["promotion_id"]
    owner_user_id = _get_candidate(candidate_id).owner_user_id

    failing_writer = FakeWriter(fail_upsert=True)
    db = _db()
    try:
        try:
            index_promotion(
                db,
                owner_user_id=owner_user_id,
                promotion_id=promotion_id,
                writer=failing_writer,
                encoder=FakeEncoder(),
                validate_runtime=False,
            )
            raise AssertionError("expected AvatarMemoryIndexingExecutionError")
        except AvatarMemoryIndexingExecutionError:
            pass

        promotion = db.get(AvatarMemoryPromotion, promotion_id)
        assert promotion.promotion_status == "failed"
        assert promotion.failure_reason
    finally:
        db.close()

    working_writer = FakeWriter()
    db = _db()
    try:
        retried = index_promotion(
            db,
            owner_user_id=owner_user_id,
            promotion_id=promotion_id,
            writer=working_writer,
            encoder=FakeEncoder(),
            validate_runtime=False,
        )
        assert retried.result == "indexed"
        assert retried.promotion_status == "indexed"
    finally:
        db.close()


# --- Biography projection ---------------------------------------------------


def test_biography_endpoint_returns_the_promoted_memory_for_the_owner(client):
    token = _register_and_login(client, "biog-promo-owner6@example.com")
    profile_id = _create_memorial(client, token)
    candidate_id = _create_ready_for_review_candidate(
        owner_user_id=_get_profile_owner_user_id(profile_id),
        profile_id=profile_id,
        text="Rodinné vzpomínky na chalupu u lesa.",
    )
    review = client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/owner-review",
        headers=_auth_headers(token),
        json={"action": "confirm"},
    )
    promotion_id = review.json()["promotion_id"]

    entries_before = client.get(
        f"/api/memorials/{profile_id}/biography/memory-entries", headers=_auth_headers(token)
    )
    assert entries_before.status_code == 200
    [entry] = entries_before.json()
    assert entry["promotion_id"] == promotion_id
    assert entry["candidate_id"] == candidate_id
    assert entry["searchable_as_fact"] is False

    owner_user_id = _get_candidate(candidate_id).owner_user_id
    db = _db()
    try:
        index_promotion(
            db, owner_user_id=owner_user_id, promotion_id=promotion_id, writer=FakeWriter(), encoder=FakeEncoder(), validate_runtime=False
        )
    finally:
        db.close()

    entries_after = client.get(
        f"/api/memorials/{profile_id}/biography/memory-entries", headers=_auth_headers(token)
    ).json()
    assert len(entries_after) == 1
    assert entries_after[0]["searchable_as_fact"] is True


def test_biography_endpoint_does_not_leak_private_owner_entry_to_a_non_owner_member(client):
    owner_token = _register_and_login(client, "biog-promo-owner7@example.com")
    contributor_token = _register_and_login(client, "biog-promo-contrib7@example.com")
    profile_id = _create_memorial(client, owner_token)
    candidate_id = _create_ready_for_review_candidate(
        owner_user_id=_get_profile_owner_user_id(profile_id),
        profile_id=profile_id,
        text="Toto je soukromá vzpomínka jen pro vlastníka.",
    )
    client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/owner-review",
        headers=_auth_headers(owner_token),
        json={"action": "confirm"},
    )

    invite = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": "biog-promo-contrib7@example.com", "role": "contributor"},
    )
    client.post(
        "/api/invitations/accept",
        headers=_auth_headers(contributor_token),
        json={"token": invite.json()["token"]},
    )

    owner_view = client.get(
        f"/api/memorials/{profile_id}/biography/memory-entries", headers=_auth_headers(owner_token)
    ).json()
    assert len(owner_view) == 1

    contributor_view = client.get(
        f"/api/memorials/{profile_id}/biography/memory-entries", headers=_auth_headers(contributor_token)
    ).json()
    assert contributor_view == []


# --- Reconciliation ----------------------------------------------------------


def _create_approved_private_owner_candidate_missing_promotion(*, email: str) -> tuple[int, int, int]:
    """Directly builds the exact stuck state the real "Lukas Krumpach 3"
    candidate was found in: `status=approved`, `enrichment_status=
    ready_for_owner_review`, `privacy_scope=private_owner`,
    `owner_review_actor_role=owner`, and NO `AvatarMemoryPromotion` row at
    all - simulating a candidate approved before this task's eligibility
    fix existed. Returns (owner_user_id, profile_id, candidate_id)."""

    db = _db()
    try:
        from app.modules.auth.schemas import RegisterRequest
        from app.modules.auth.service import register_user
        from app.modules.conversation_memory_candidates.schemas import MemoryCandidateCreate
        from app.modules.conversation_memory_candidates.service import create_candidate
        from app.modules.memory_profiles.schemas import MemoryProfileCreate
        from app.modules.memory_profiles.service import create_memory_profile

        user = register_user(db, RegisterRequest(email=email, password=PASSWORD, full_name="Reconcile Owner"))
        profile = create_memory_profile(
            db, current_user=user, payload=MemoryProfileCreate(name="Reconcile Profile", biography="Bio", personality="Warm")
        )
        candidate = create_candidate(
            db,
            payload=MemoryCandidateCreate(
                owner_user_id=user.id,
                avatar_id=str(profile.id),
                profile_id=profile.id,
                trace_id="reconcile-trace",
                user_message_excerpt="Approved memory missing its promotion.",
                proposed_memory_text="Approved memory missing its promotion.",
                reason="AI Biographer topic: childhood",
                language="ru",
                enrichment_status="ready_for_owner_review",
                finalized_memory_text="Approved memory missing its promotion.",
                privacy_scope="private_owner",
                workflow_version=2,
            ),
        )
        candidate.status = "approved"
        candidate.owner_review_actor_role = "owner"
        db.commit()
        return user.id, profile.id, candidate.id
    finally:
        db.close()


def test_reconciliation_finds_and_repairs_a_missing_promotion(client):
    owner_user_id, profile_id, candidate_id = _create_approved_private_owner_candidate_missing_promotion(
        email="biog-promo-reconcile1@example.com"
    )
    assert _get_promotion_for_candidate(candidate_id) is None

    db = _db()
    try:
        scanned = find_approved_candidates_for_reconciliation(db, profile_id=profile_id)
        assert [c.id for c in scanned] == [candidate_id]
    finally:
        db.close()

    db = _db()
    try:
        result = reconcile_candidate_promotions(db, profile_id=profile_id)
        assert result.scanned == 1
        assert result.promoted == 1
        assert result.already_complete == 0
        assert result.failed == 0
    finally:
        db.close()

    promotion = _get_promotion_for_candidate(candidate_id)
    assert promotion is not None
    assert promotion.owner_user_id == owner_user_id
    assert promotion.promotion_status in {"pending_index", "indexed"}


def test_reconciliation_dry_run_never_writes_anything(client):
    _owner_user_id, profile_id, candidate_id = _create_approved_private_owner_candidate_missing_promotion(
        email="biog-promo-reconcile2@example.com"
    )

    db = _db()
    try:
        result = reconcile_candidate_promotions(db, profile_id=profile_id, dry_run=True)
        assert result.promoted == 1
    finally:
        db.close()

    assert _get_promotion_for_candidate(candidate_id) is None


def test_reconciliation_is_idempotent_and_never_duplicates_the_promotion(client):
    _owner_user_id, profile_id, candidate_id = _create_approved_private_owner_candidate_missing_promotion(
        email="biog-promo-reconcile3@example.com"
    )

    db = _db()
    try:
        first = reconcile_candidate_promotions(db, profile_id=profile_id)
        assert first.promoted == 1
    finally:
        db.close()

    db = _db()
    try:
        second = reconcile_candidate_promotions(db, profile_id=profile_id)
        assert second.promoted == 0
        assert second.already_complete + second.indexing_enqueued + second.skipped == 1
    finally:
        db.close()

    db = _db()
    try:
        count = (
            db.query(AvatarMemoryPromotion)
            .filter(AvatarMemoryPromotion.candidate_id == candidate_id)
            .count()
        )
        assert count == 1
    finally:
        db.close()


def test_reconciliation_never_touches_a_rejected_candidate(client):
    db = _db()
    try:
        from app.modules.auth.schemas import RegisterRequest
        from app.modules.auth.service import register_user
        from app.modules.conversation_memory_candidates.schemas import MemoryCandidateCreate
        from app.modules.conversation_memory_candidates.service import create_candidate
        from app.modules.memory_profiles.schemas import MemoryProfileCreate
        from app.modules.memory_profiles.service import create_memory_profile

        user = register_user(
            db, RegisterRequest(email="biog-promo-reconcile4@example.com", password=PASSWORD, full_name="Owner")
        )
        profile = create_memory_profile(
            db, current_user=user, payload=MemoryProfileCreate(name="Profile", biography="Bio", personality="Warm")
        )
        candidate = create_candidate(
            db,
            payload=MemoryCandidateCreate(
                owner_user_id=user.id,
                avatar_id=str(profile.id),
                profile_id=profile.id,
                trace_id="reconcile-rejected",
                user_message_excerpt="Rejected memory.",
                proposed_memory_text="Rejected memory.",
                reason="AI Biographer topic: childhood",
                language="ru",
                enrichment_status="ready_for_owner_review",
                finalized_memory_text="Rejected memory.",
                privacy_scope="private_owner",
                workflow_version=2,
            ),
        )
        candidate.status = "rejected"
        db.commit()
        profile_id = profile.id
    finally:
        db.close()

    db = _db()
    try:
        assert find_approved_candidates_for_reconciliation(db, profile_id=profile_id) == []
        result = reconcile_candidate_promotions(db, profile_id=profile_id)
        assert result.scanned == 0
    finally:
        db.close()


# --- Chat retrieval: privacy enforcement + corrected-memory priority -------


def test_retrieval_visibility_predicate_hides_private_owner_evidence_from_non_owner_viewer():
    """Direct unit test of `rag_retrieval.service._is_visible_to_viewer` /
    `_is_owner_only_evidence` - the exact predicate every retrieval result
    is filtered through (both the dense and hybrid dense+sparse paths in
    `rag_retrieval.service`). Exercised directly, rather than through the
    full HTTP + real-embedding-provider stack, to test the actual
    decision logic deterministically without depending on this
    environment's default embedding provider/model configuration."""

    from app.modules.rag_retrieval.service import _is_owner_only_evidence, _is_visible_to_viewer

    private_owner_payload = {"privacy_scope": "private_owner", "source_type": "conversation_candidate"}
    all_family_payload = {"privacy_scope": "all_family", "source_type": "conversation_candidate"}
    no_scope_payload = {"source_type": "biography"}

    assert _is_owner_only_evidence(private_owner_payload) is True
    assert _is_owner_only_evidence(all_family_payload) is False
    assert _is_owner_only_evidence(no_scope_payload) is False

    assert _is_visible_to_viewer(private_owner_payload, viewer_is_profile_owner=True) is True
    assert _is_visible_to_viewer(private_owner_payload, viewer_is_profile_owner=False) is False
    assert _is_visible_to_viewer(all_family_payload, viewer_is_profile_owner=False) is True
    assert _is_visible_to_viewer(no_scope_payload, viewer_is_profile_owner=False) is True


def test_chat_evidence_prioritizes_verified_promoted_memory_over_generic_evidence(client, monkeypatch):
    """Task 65.6.1 (Part F/I) + Task 65.10 (Part E/G): the authenticated chat
    path must correctly thread the same bounded, relevance-driven
    verified-evidence boost (`VERIFIED_EVIDENCE_RELEVANCE_BOOST = 0.15`,
    see `app.modules.ai_agents.brain.context.
    prioritize_corrected_memory_evidence`) through
    `chat.service._retrieve_rag_evidence_safely` that the unit tests in
    `test_ai_agents.py` cover directly on `prioritize_corrected_memory_
    evidence`. An approved, verified (`memory_status=verified`,
    `source_type=conversation_candidate`) memory whose relevance gap to a
    generic archival item is within the bounded boost must be floated ahead
    of it - but (per Task 65.10) verification is never an unconditional
    override of a *substantially* more relevant generic item on an ordinary
    factual question (this scenario's Czech question classifies as
    `DIRECT_FACTUAL_MEMORY`, not `CORRECTED_MEMORY_FACT`/
    `CORRECTION_HISTORY`, so only the bounded-boost mode applies here, not
    the group-level verified-first mode). Does not change retrieval,
    ranking, or top_k itself."""

    from app.modules.chat import service as chat_service
    from app.modules.rag_retrieval.schemas import RagRetrievalResponseRead, RagRetrievalResultRead

    generic_result = RagRetrievalResultRead(
        chunk_id=1,
        source_id=1,
        source_title="Generic biography",
        embedding_id=1,
        score=0.50,
        text="Generic older statement about the same subject.",
        chunk_index=0,
        language="cs",
        source_type="biography",
        validation_status="valid",
        text_hash="hash1",
        qdrant_collection="col",
        payload_metadata={"source_type": "biography"},
    )
    verified_result = RagRetrievalResultRead(
        chunk_id=2,
        source_id=2,
        source_title="Approved conversation memory",
        embedding_id=2,
        score=0.40,
        text="Approved, more specific corrected memory.",
        chunk_index=0,
        language="cs",
        source_type="conversation_candidate",
        validation_status="valid",
        text_hash="hash2",
        qdrant_collection="col",
        payload_metadata={
            "source_type": "conversation_candidate",
            "memory_status": "verified",
            "promotion_id": 9,
            "candidate_id": 9,
        },
    )

    def fake_retrieve_profile_rag(db, *, current_user, profile_id, payload):
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code="mock",
            results=[generic_result, verified_result],
        )

    monkeypatch.setattr(chat_service, "retrieve_profile_rag", fake_retrieve_profile_rag)

    db = _db()
    try:
        from app.db.models import User

        fake_user = User(id=1, email="chat-priority@example.com", hashed_password="x", full_name="X")
        evidence_items = chat_service._retrieve_rag_evidence_safely(
            db, current_user=fake_user, profile_id=1, user_message="Kde jsi strávil dětství?"
        )
    finally:
        db.close()

    # Bounded-boost math (Task 65.10): verified score 0.40 + boost 0.15 =
    # 0.55, which beats the generic item's 0.50 - a close relevance gap the
    # boost is meant to break - without the generic item being anywhere
    # near as relevant as the birthday-regression scenario in
    # `test_ai_agents.py` (where a 0.90+ generic item correctly keeps
    # ranking first despite a verified competitor).
    assert len(evidence_items) == 2
    assert evidence_items[0].candidate_id == 9
    assert evidence_items[0].memory_status == "verified"
    assert evidence_items[1].source_document_type == "biography"
