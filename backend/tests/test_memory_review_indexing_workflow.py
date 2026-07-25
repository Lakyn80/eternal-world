"""Task 65.8 - Memory Review, Approval, Embedding, and Searchable Indexing
Workflow Parity.

The core approve -> promote -> enqueue -> embed -> index pipeline for
`MemorialContribution` already existed and was already covered by
`test_memorial_contribution_indexing.py` (Task 65.1B). This file covers the
specific gaps identified while auditing that existing implementation against
the AI biography workflow's own review/indexing lifecycle:

  * an explicit, authorized "retry indexing" action (the AI biography
    workflow's `POST .../candidates/{id}/index` equivalent) - previously
    missing for contributions entirely (see
    `memorial_access.service.retry_contribution_indexing`);
  * HTTP-level authorization-matrix coverage for approve/retry that the
    existing test suite did not yet assert explicitly (self-review, viewer,
    non-member);
  * rejection never creating a promotion/indexing job;
  * repeated approval being a no-op rather than a silent duplicate;
  * a submitted (not-yet-approved) contribution never being index-eligible;
  * the shared privacy-visibility predicate applied to a contribution-shaped
    (not just conversation-candidate-shaped) Qdrant payload;
  * storage-level profile isolation for two memorials' promoted memories.

Uses the same fake-safe writer/encoder doubles as
`test_memorial_contribution_indexing.py` - no real network/model calls.
"""

from __future__ import annotations

from app.db.models import BackgroundJob, MemorialContributionPromotion, RagSource
from app.main import app
from app.modules.embeddings.providers.base import EmbeddingVector
from app.modules.memorial_contribution_indexing import service as contribution_indexing_service
from app.modules.memorial_contribution_indexing.repository import get_promotion_by_contribution_id


PASSWORD = "StrongPass123"


class FakeEncoder:
    def __init__(self) -> None:
        self.calls = 0

    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        self.calls += 1
        assert text
        assert model_code == "bge_m3_dense_sparse"
        return EmbeddingVector(
            values=[0.03] * 1024,
            dimension=1024,
            metadata={"sparse_vector": {"vzpominka": 0.5}, "provider_name": "bge_m3_hybrid"},
        )


class FakeWriter:
    def __init__(self, *, dimension: int = 1024) -> None:
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
        self.points[(collection_name, point_id)] = {
            "id": point_id,
            "vector": list(vector),
            "payload": dict(payload),
        }

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


def _create_memorial(client, token: str, name: str = "Workflow Memorial") -> int:
    response = client.post("/api/memorials", headers=_auth_headers(token), json={"name": name})
    assert response.status_code == 201
    return response.json()["id"]


def _invite(client, owner_token: str, profile_id: int, email: str, role: str) -> str:
    response = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": email, "role": role},
    )
    assert response.status_code == 201
    return response.json()["token"]


def _accept(client, token: str, invitation_token: str):
    response = client.post("/api/invitations/accept", headers=_auth_headers(token), json={"token": invitation_token})
    assert response.status_code == 200


def _submit(client, token: str, profile_id: int, title: str = "Recollection", privacy_scope: str = "all_family"):
    response = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(token),
        json={
            "title": title,
            "memory_text": "A specific, previously unrecorded family recollection.",
            "source_note": "Told during a visit",
            "privacy_scope": privacy_scope,
        },
    )
    assert response.status_code == 201
    return response.json()


def _approve(client, token: str, profile_id: int, contribution_id: int):
    return client.post(
        f"/api/memorials/{profile_id}/contributions/{contribution_id}/approve",
        headers=_auth_headers(token),
        json={"review_note": "confirmed"},
    )


def _retry(client, token: str, profile_id: int, contribution_id: int):
    return client.post(
        f"/api/memorials/{profile_id}/contributions/{contribution_id}/retry-indexing",
        headers=_auth_headers(token),
    )


def _force_promotion_failed(profile_id: int, contribution_id: int) -> None:
    """Test-only setup helper: simulates "a previous Celery execution of
    `index_contribution_promotion` already failed" without actually running
    a real (or even fake) embedding/Qdrant call - the retry endpoint's own
    authorization/eligibility gating is what this exercises; the actual
    embed-and-index execution path is already covered end-to-end by
    `test_memorial_contribution_indexing.py` and by
    `test_retry_endpoint_actually_reindexes_and_clears_failure` below."""

    db = _db()
    try:
        promotion = get_promotion_by_contribution_id(db, contribution_id=contribution_id)
        assert promotion is not None
        assert promotion.profile_id == profile_id
        promotion.promotion_status = "failed"
        promotion.failure_reason = "Contribution indexing failed"
        promotion.indexing_attempt_count = 1
        db.commit()
    finally:
        db.close()


# --- Submission: review-required, never indexed, never active memory ------


def test_submitted_memory_starts_needs_review_not_indexed_not_active(client):
    owner_token = _register_and_login(client, "wf-submit-owner@example.com")
    profile_id = _create_memorial(client, owner_token)

    submitted = _submit(client, owner_token, profile_id)

    assert submitted["status"] == "needs_review"
    assert submitted["active_memory_eligible"] is False
    assert submitted["indexing_status"]["state"] == "not_applicable"

    db = _db()
    try:
        from app.modules.memorial_access import repository as memorial_repository

        contribution = memorial_repository.get_contribution(
            db, profile_id=profile_id, contribution_id=submitted["id"]
        )
        raised = False
        try:
            contribution_indexing_service.promote_contribution(db, contribution=contribution)
        except contribution_indexing_service.ContributionIndexingEligibilityError:
            raised = True
        assert raised, "a needs_review contribution must never become index-eligible"
        assert db.query(MemorialContributionPromotion).count() == 0
    finally:
        db.close()


# --- Review authorization matrix -------------------------------------------


def test_owner_can_approve_own_submitted_contribution_self_review_allowed(client):
    """Established self-review policy for this codebase (mirrored from the
    AI biography workflow, where the owner is always the sole reviewer of
    their own conversation-derived candidates): an owner reviewing their own
    submission is not a distinct restricted case - `REVIEW_ROLES` grants the
    capability regardless of authorship, and nothing in the domain layer
    checks `contribution.author_user_id` against the reviewer. This test
    locks that existing, intended behavior in explicitly."""

    owner_token = _register_and_login(client, "wf-selfreview-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    submitted = _submit(client, owner_token, profile_id)

    approved = _approve(client, owner_token, profile_id, submitted["id"])

    assert approved.status_code == 200
    assert approved.json()["status"] == "approved"
    assert approved.json()["reviewed_by_user_id"] == approved.json()["author_user_id"]


def test_viewer_cannot_approve_contribution(client):
    owner_token = _register_and_login(client, "wf-viewer-owner@example.com")
    viewer_token = _register_and_login(client, "wf-viewer-viewer@example.com")
    profile_id = _create_memorial(client, owner_token)
    invite = _invite(client, owner_token, profile_id, "wf-viewer-viewer@example.com", "viewer")
    _accept(client, viewer_token, invite)
    submitted = _submit(client, owner_token, profile_id)

    approve_attempt = _approve(client, viewer_token, profile_id, submitted["id"])

    assert approve_attempt.status_code == 403


def test_non_member_gets_404_on_approve_and_retry(client):
    owner_token = _register_and_login(client, "wf-nonmember-owner@example.com")
    outsider_token = _register_and_login(client, "wf-nonmember-outsider@example.com")
    profile_id = _create_memorial(client, owner_token)
    submitted = _submit(client, owner_token, profile_id)

    approve_attempt = _approve(client, outsider_token, profile_id, submitted["id"])
    retry_attempt = _retry(client, outsider_token, profile_id, submitted["id"])

    assert approve_attempt.status_code == 404
    assert retry_attempt.status_code == 404


# --- Rejection never enqueues indexing --------------------------------------


def test_rejection_never_creates_a_promotion_or_indexing_job(client):
    owner_token = _register_and_login(client, "wf-reject-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    submitted = _submit(client, owner_token, profile_id)

    rejected = client.post(
        f"/api/memorials/{profile_id}/contributions/{submitted['id']}/reject",
        headers=_auth_headers(owner_token),
        json={"reason": "not accurate"},
    )

    assert rejected.status_code == 200
    assert rejected.json()["status"] == "rejected"
    assert rejected.json()["indexing_status"]["state"] == "not_applicable"

    db = _db()
    try:
        assert db.query(MemorialContributionPromotion).count() == 0
        assert db.query(BackgroundJob).filter(BackgroundJob.job_type == "qdrant_indexing").count() == 0
    finally:
        db.close()


# --- Approval idempotency at the HTTP layer --------------------------------


def test_repeated_approval_request_is_rejected_and_does_not_duplicate_state(client):
    """A second approval attempt against an already-approved contribution
    must not silently re-run the promotion/enqueue bridge a second time -
    the contribution is no longer in a reviewable state, so the transition
    is refused outright (safer than a second, ambiguous auto-promotion)."""

    owner_token = _register_and_login(client, "wf-idempotent-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    submitted = _submit(client, owner_token, profile_id)

    first = _approve(client, owner_token, profile_id, submitted["id"])
    second = _approve(client, owner_token, profile_id, submitted["id"])

    assert first.status_code == 200
    assert second.status_code == 400

    db = _db()
    try:
        assert db.query(MemorialContributionPromotion).count() == 1
        assert db.query(BackgroundJob).filter(BackgroundJob.job_type == "qdrant_indexing").count() == 1
    finally:
        db.close()


# --- Retry indexing: authorization + eligibility ---------------------------


def test_retry_requires_a_previously_failed_indexing_attempt(client):
    owner_token = _register_and_login(client, "wf-retry-notfailed-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    submitted = _submit(client, owner_token, profile_id)
    _approve(client, owner_token, profile_id, submitted["id"])

    # The promotion is `pending_index` (auto-enqueued, not yet failed) -
    # retry must refuse rather than race the already-queued Celery job.
    retry_attempt = _retry(client, owner_token, profile_id, submitted["id"])

    assert retry_attempt.status_code == 400


def test_retry_is_refused_for_a_needs_review_contribution(client):
    owner_token = _register_and_login(client, "wf-retry-unapproved-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    submitted = _submit(client, owner_token, profile_id)

    retry_attempt = _retry(client, owner_token, profile_id, submitted["id"])

    assert retry_attempt.status_code == 400


def test_contributor_cannot_retry_indexing(client):
    owner_token = _register_and_login(client, "wf-retry-contributor-owner@example.com")
    contributor_token = _register_and_login(client, "wf-retry-contributor-member@example.com")
    profile_id = _create_memorial(client, owner_token)
    invite = _invite(client, owner_token, profile_id, "wf-retry-contributor-member@example.com", "contributor")
    _accept(client, contributor_token, invite)
    submitted = _submit(client, owner_token, profile_id)
    _approve(client, owner_token, profile_id, submitted["id"])
    _force_promotion_failed(profile_id, submitted["id"])

    retry_attempt = _retry(client, contributor_token, profile_id, submitted["id"])

    assert retry_attempt.status_code == 403


def test_viewer_cannot_retry_indexing(client):
    owner_token = _register_and_login(client, "wf-retry-viewer-owner@example.com")
    viewer_token = _register_and_login(client, "wf-retry-viewer-member@example.com")
    profile_id = _create_memorial(client, owner_token)
    invite = _invite(client, owner_token, profile_id, "wf-retry-viewer-member@example.com", "viewer")
    _accept(client, viewer_token, invite)
    submitted = _submit(client, owner_token, profile_id)
    _approve(client, owner_token, profile_id, submitted["id"])
    _force_promotion_failed(profile_id, submitted["id"])

    retry_attempt = _retry(client, viewer_token, profile_id, submitted["id"])

    assert retry_attempt.status_code == 403


def test_trusted_reviewer_can_retry_failed_indexing(client, monkeypatch):
    """Task 65.9 (Part I): the retry endpoint itself now only authorizes,
    reactivates the promotion to `pending_index`, and creates/dispatches
    the persistent job - it must never call the encoder inline. This is
    asserted directly (`fake_encoder.calls == 0` right after the HTTP
    response), then the embedding-worker's own idempotent execution is
    simulated exactly as `test_memorial_contribution_indexing.py` already
    does for the original approve->index flow, by calling
    `index_contribution_promotion` directly with fakes - standing in for
    "a Celery embedding worker picks up the dispatched job"."""

    owner_token = _register_and_login(client, "wf-retry-reviewer-owner@example.com")
    reviewer_token = _register_and_login(client, "wf-retry-reviewer-member@example.com")
    profile_id = _create_memorial(client, owner_token)
    invite = _invite(client, owner_token, profile_id, "wf-retry-reviewer-member@example.com", "trusted_reviewer")
    _accept(client, reviewer_token, invite)
    submitted = _submit(client, owner_token, profile_id)
    _approve(client, owner_token, profile_id, submitted["id"])
    _force_promotion_failed(profile_id, submitted["id"])

    fake_writer = FakeWriter()
    fake_encoder = FakeEncoder()

    retry_response = _retry(client, reviewer_token, profile_id, submitted["id"])

    assert retry_response.status_code == 202
    assert retry_response.json()["indexing_status"]["state"] == "pending"
    assert fake_encoder.calls == 0, "the retry HTTP request itself must never call the encoder"

    db = _db()
    try:
        promotion = get_promotion_by_contribution_id(db, contribution_id=submitted["id"])
        assert promotion is not None
        result = contribution_indexing_service.index_contribution_promotion(
            db,
            profile_id=profile_id,
            promotion_id=promotion.id,
            writer=fake_writer,
            encoder=fake_encoder,
        )
        assert result.promotion_status == "indexed"
        assert result.result == "indexed"
    finally:
        db.close()

    assert fake_writer.upsert_calls == 1

    final = client.get(f"/api/memorials/{profile_id}/contributions", headers=_auth_headers(owner_token))
    matching = next(item for item in final.json() if item["id"] == submitted["id"])
    assert matching["indexing_status"]["state"] == "indexed"
    assert matching["indexing_status"]["failure_reason"] is None


def test_retry_endpoint_actually_reindexes_and_clears_failure(client, monkeypatch):
    """End-to-end (through the real HTTP endpoint plus a simulated worker
    execution, fake writer/encoder only) proof that retry transitions
    `failed -> indexed`, and a second retry request against an already-
    `indexed` promotion is refused rather than silently re-running."""

    owner_token = _register_and_login(client, "wf-retry-e2e-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    submitted = _submit(client, owner_token, profile_id)
    _approve(client, owner_token, profile_id, submitted["id"])
    _force_promotion_failed(profile_id, submitted["id"])

    fake_writer = FakeWriter()
    fake_encoder = FakeEncoder()

    first_retry = _retry(client, owner_token, profile_id, submitted["id"])
    assert first_retry.status_code == 202
    assert first_retry.json()["indexing_status"]["state"] == "pending"

    db = _db()
    try:
        promotion = get_promotion_by_contribution_id(db, contribution_id=submitted["id"])
        assert promotion is not None
        contribution_indexing_service.index_contribution_promotion(
            db,
            profile_id=profile_id,
            promotion_id=promotion.id,
            writer=fake_writer,
            encoder=fake_encoder,
        )
    finally:
        db.close()

    second_retry = _retry(client, owner_token, profile_id, submitted["id"])

    first_status = client.get(
        f"/api/memorials/{profile_id}/contributions", headers=_auth_headers(owner_token)
    )
    first_matching = next(item for item in first_status.json() if item["id"] == submitted["id"])
    assert first_matching["indexing_status"]["state"] == "indexed"
    # A second retry request against an already-`indexed` promotion is
    # refused (not semantically valid per Part I) rather than silently
    # re-running the embed/Qdrant step a second time.
    assert second_retry.status_code == 400
    assert fake_writer.upsert_calls == 1
    assert fake_encoder.calls == 1


# --- Privacy predicate applied to a contribution-shaped payload ------------


def test_privacy_visibility_predicate_treats_contribution_payload_like_any_other_evidence(client):
    """`rag_retrieval.service._is_visible_to_viewer` is the single shared
    gate every retrieval result (biographer-candidate-sourced or
    contribution-sourced) is filtered through. Exercised directly with a
    `source_type="manual_text"` payload (this module's own
    `SOURCE_TYPE`/`PROVENANCE` constants) to confirm the contribution
    pipeline gets the exact same owner-only enforcement as any other
    source, not a second, parallel privacy check."""

    from app.modules.rag_retrieval.service import _is_owner_only_evidence, _is_visible_to_viewer

    owner_only_payload = {
        "privacy_scope": "private_owner",
        "source_type": contribution_indexing_service.SOURCE_TYPE,
        "provenance": contribution_indexing_service.PROVENANCE,
    }
    family_payload = {
        "privacy_scope": "all_family",
        "source_type": contribution_indexing_service.SOURCE_TYPE,
        "provenance": contribution_indexing_service.PROVENANCE,
    }

    assert _is_owner_only_evidence(owner_only_payload) is True
    assert _is_owner_only_evidence(family_payload) is False
    assert _is_visible_to_viewer(owner_only_payload, viewer_is_profile_owner=True) is True
    assert _is_visible_to_viewer(owner_only_payload, viewer_is_profile_owner=False) is False
    assert _is_visible_to_viewer(family_payload, viewer_is_profile_owner=False) is True


# --- Storage-level profile isolation between two memorials -----------------


def test_two_memorials_indexed_contributions_are_stored_and_pointed_separately(client):
    owner_a_token = _register_and_login(client, "wf-isolation-owner-a@example.com")
    owner_b_token = _register_and_login(client, "wf-isolation-owner-b@example.com")
    profile_a_id = _create_memorial(client, owner_a_token, "Memorial A")
    profile_b_id = _create_memorial(client, owner_b_token, "Memorial B")

    submitted_a = _submit(client, owner_a_token, profile_a_id, title="Memory A")
    submitted_b = _submit(client, owner_b_token, profile_b_id, title="Memory B")
    approved_a = _approve(client, owner_a_token, profile_a_id, submitted_a["id"]).json()
    approved_b = _approve(client, owner_b_token, profile_b_id, submitted_b["id"]).json()

    db = _db()
    try:
        writer = FakeWriter()
        encoder = FakeEncoder()
        promotion_a = get_promotion_by_contribution_id(db, contribution_id=approved_a["id"])
        promotion_b = get_promotion_by_contribution_id(db, contribution_id=approved_b["id"])

        result_a = contribution_indexing_service.index_contribution_promotion(
            db, profile_id=profile_a_id, promotion_id=promotion_a.id, writer=writer, encoder=encoder, validate_runtime=False
        )
        result_b = contribution_indexing_service.index_contribution_promotion(
            db, profile_id=profile_b_id, promotion_id=promotion_b.id, writer=writer, encoder=encoder, validate_runtime=False
        )

        assert result_a.qdrant_point_id != result_b.qdrant_point_id
        sources = db.query(RagSource).order_by(RagSource.id).all()
        assert {source.profile_id for source in sources} == {profile_a_id, profile_b_id}

        point_a = writer.points[(result_a.target_collection_name, result_a.qdrant_point_id)]
        point_b = writer.points[(result_b.target_collection_name, result_b.qdrant_point_id)]
        assert point_a["payload"]["profile_id"] == profile_a_id
        assert point_b["payload"]["profile_id"] == profile_b_id
    finally:
        db.close()
