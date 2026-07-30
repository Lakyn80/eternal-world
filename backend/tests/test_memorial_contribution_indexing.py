"""Task 65.1B - contribution-to-canonical-memory indexing bridge.

Uses fake-safe writer/encoder doubles (no real Qdrant network calls, no
model downloads), mirroring the established pattern in
`test_avatar_memory_indexing.py`.
"""

from __future__ import annotations

from app.db.models import MemorialContributionPromotion, RagChunk, RagEmbedding, RagSource, RagVectorIndex
from app.main import app
from app.modules.embeddings.providers.base import EmbeddingVector
from app.modules.memorial_contribution_indexing.repository import get_promotion_by_contribution_id
from app.modules.memorial_contribution_indexing.service import (
    ContributionIndexingEligibilityError,
    build_deterministic_point_id,
    index_contribution_promotion,
    promote_contribution,
    retire_contribution_promotion,
)


PASSWORD = "StrongPass123"


class FakeEncoder:
    def __init__(self) -> None:
        self.calls = 0

    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        self.calls += 1
        assert text
        assert model_code == "bge_m3_dense_sparse"
        return EmbeddingVector(
            values=[0.02] * 1024,
            dimension=1024,
            metadata={"sparse_vector": {"vzpominka": 0.7}, "provider_name": "bge_m3_hybrid"},
        )


class FakeWriter:
    def __init__(self, *, fail_upsert: bool = False, dimension: int | None = 1024) -> None:
        self.fail_upsert = fail_upsert
        self.dimension = dimension
        self.points: dict[tuple[str, str], dict[str, object]] = {}
        self.upsert_calls = 0
        self.delete_calls = 0
        self.ensure_calls: list[tuple[str, int]] = []

    def collection_vector_size(self, *, collection_name: str) -> int | None:
        del collection_name
        return self.dimension

    def ensure_collection(self, *, collection_name: str, vector_size: int) -> None:
        self.ensure_calls.append((collection_name, vector_size))
        self.dimension = vector_size

    def get_point(self, *, collection_name: str, point_id: str) -> dict[str, object] | None:
        return self.points.get((collection_name, point_id))

    def upsert_point(self, *, collection_name: str, point_id: str, vector, payload) -> None:
        self.upsert_calls += 1
        if self.fail_upsert:
            raise RuntimeError("qdrant unavailable")
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


def _create_memorial(client, token: str, name: str = "Bridge Memorial") -> int:
    response = client.post("/api/memorials", headers=_auth_headers(token), json={"name": name})
    assert response.status_code == 201
    return response.json()["id"]


def _submit_and_approve_contribution(client, owner_token: str, profile_id: int, title: str = "Zpěv"):
    submit = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(owner_token),
        json={
            "title": title,
            "memory_text": "Babička zpívala ukolébavku každý večer před spaním.",
            "privacy_scope": "all_family",
        },
    )
    assert submit.status_code == 201
    approve = client.post(
        f"/api/memorials/{profile_id}/contributions/{submit.json()['id']}/approve",
        headers=_auth_headers(owner_token),
        json={"review_note": "confirmed"},
    )
    assert approve.status_code == 200
    return approve.json()


def test_approval_creates_pending_index_promotion_and_reports_pending_status(client):
    owner_token = _register_and_login(client, "bridge-owner@example.com")
    profile_id = _create_memorial(client, owner_token)

    approved = _submit_and_approve_contribution(client, owner_token, profile_id)

    # The heavy embedding/Qdrant step is enqueued on the Celery worker
    # rather than run inline inside the approval request (no blocking model
    # load in the HTTP path) - the API response must accurately report
    # "pending", never claim the contribution is already searchable.
    assert approved["indexing_status"]["state"] == "pending"
    assert approved["active_memory_eligible"] is True

    db = _db()
    try:
        from app.db.models import BackgroundJob

        jobs = db.query(BackgroundJob).filter(BackgroundJob.job_type == "qdrant_indexing").all()
        assert len(jobs) == 1
        assert jobs[0].input_payload["contribution_id"] == approved["id"]
        assert jobs[0].celery_task_id is not None
    finally:
        db.close()


def test_promote_contribution_is_idempotent_get_or_create(client):
    owner_token = _register_and_login(client, "bridge-idem-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    # Approval already promotes the contribution once automatically (see
    # `memorial_access.service._promote_and_enqueue_indexing_safely`) -
    # repeated *manual* calls below must still be pure get-or-create and
    # never create a second row for the same contribution.
    approved = _submit_and_approve_contribution(client, owner_token, profile_id)

    db = _db()
    try:
        from app.modules.memorial_access import repository as memorial_repository

        contribution = memorial_repository.get_contribution(
            db, profile_id=profile_id, contribution_id=approved["id"]
        )
        first = promote_contribution(db, contribution=contribution)
        second = promote_contribution(db, contribution=contribution)

        assert first.created is False
        assert second.created is False
        assert first.promotion.id == second.promotion.id
        assert db.query(MemorialContributionPromotion).count() == 1
    finally:
        db.close()


def test_only_approved_current_contribution_can_be_promoted(client):
    owner_token = _register_and_login(client, "bridge-eligibility-owner@example.com")
    contributor_token = _register_and_login(client, "bridge-eligibility-contributor@example.com")
    profile_id = _create_memorial(client, owner_token)
    invite = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": "bridge-eligibility-contributor@example.com", "role": "contributor"},
    )
    client.post(
        "/api/invitations/accept",
        headers=_auth_headers(contributor_token),
        json={"token": invite.json()["token"]},
    )
    pending = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(contributor_token),
        json={"title": "Pending", "memory_text": "Not yet reviewed.", "privacy_scope": "all_family"},
    )
    assert pending.status_code == 201

    db = _db()
    try:
        from app.modules.memorial_access import repository as memorial_repository

        contribution = memorial_repository.get_contribution(
            db, profile_id=profile_id, contribution_id=pending.json()["id"]
        )
        raised = False
        try:
            promote_contribution(db, contribution=contribution)
        except ContributionIndexingEligibilityError:
            raised = True
        assert raised, "needs_review contribution must never be promoted for indexing"
        assert db.query(MemorialContributionPromotion).count() == 0
    finally:
        db.close()


def test_index_contribution_promotion_writes_scoped_evidence_and_qdrant_payload(client):
    owner_token = _register_and_login(client, "bridge-index-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    approved = _submit_and_approve_contribution(client, owner_token, profile_id)

    db = _db()
    try:
        promotion = get_promotion_by_contribution_id(db, contribution_id=approved["id"])
        assert promotion is not None
        writer = FakeWriter()
        encoder = FakeEncoder()

        result = index_contribution_promotion(
            db,
            profile_id=profile_id,
            promotion_id=promotion.id,
            writer=writer,
            encoder=encoder,
            validate_runtime=False,
        )

        assert result.promotion_status == "indexed"
        assert result.searchable_as_fact is True
        assert result.qdrant_point_id == build_deterministic_point_id(promotion=promotion)
        assert writer.upsert_calls == 1
        assert db.query(RagSource).count() == 1
        assert db.query(RagChunk).count() == 1
        assert db.query(RagEmbedding).count() == 1
        assert db.query(RagVectorIndex).count() == 1

        source = db.query(RagSource).one()
        embedding = db.query(RagEmbedding).one()
        # The evidence must be scoped to the memorial's owner and profile,
        # never to whichever member happened to review it.
        assert source.owner_user_id == embedding.owner_user_id
        assert source.profile_id == profile_id

        point = next(iter(writer.points.values()))
        payload = point["payload"]
        assert payload["profile_id"] == profile_id
        assert payload["contribution_id"] == approved["id"]
        assert payload["memory_status"] == "verified"
    finally:
        db.close()


def test_repeated_indexing_trigger_does_not_duplicate_points_or_rows(client):
    owner_token = _register_and_login(client, "bridge-retry-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    approved = _submit_and_approve_contribution(client, owner_token, profile_id)

    db = _db()
    try:
        promotion = get_promotion_by_contribution_id(db, contribution_id=approved["id"])
        writer = FakeWriter()
        encoder = FakeEncoder()

        first = index_contribution_promotion(
            db, profile_id=profile_id, promotion_id=promotion.id, writer=writer, encoder=encoder, validate_runtime=False
        )
        second = index_contribution_promotion(
            db, profile_id=profile_id, promotion_id=promotion.id, writer=writer, encoder=encoder, validate_runtime=False
        )

        assert first.result == "indexed"
        assert second.result == "already_indexed"
        assert writer.upsert_calls == 1
        assert encoder.calls == 1
        assert db.query(RagSource).count() == 1
        assert db.query(RagChunk).count() == 1
        assert db.query(RagEmbedding).count() == 1
        assert db.query(RagVectorIndex).count() == 1
    finally:
        db.close()


def test_indexing_failure_is_recorded_and_safely_retryable(client):
    owner_token = _register_and_login(client, "bridge-fail-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    approved = _submit_and_approve_contribution(client, owner_token, profile_id)

    db = _db()
    try:
        promotion = get_promotion_by_contribution_id(db, contribution_id=approved["id"])
        failing_writer = FakeWriter(fail_upsert=True)
        encoder = FakeEncoder()

        raised = False
        try:
            index_contribution_promotion(
                db,
                profile_id=profile_id,
                promotion_id=promotion.id,
                writer=failing_writer,
                encoder=encoder,
                validate_runtime=False,
            )
        except Exception:
            raised = True
        assert raised

        db.refresh(promotion)
        assert promotion.promotion_status == "failed"
        assert promotion.failure_reason is not None
        assert promotion.indexing_attempt_count == 1

        working_writer = FakeWriter()
        retry_result = index_contribution_promotion(
            db,
            profile_id=profile_id,
            promotion_id=promotion.id,
            writer=working_writer,
            encoder=encoder,
            validate_runtime=False,
        )
        assert retry_result.promotion_status == "indexed"
        db.refresh(promotion)
        assert promotion.failure_reason is None
    finally:
        db.close()


def test_approving_a_superseding_contribution_calls_the_retire_bridge_for_the_old_one(client, monkeypatch):
    """Verifies the *wiring* in `memorial_access.service.approve_contribution`
    - that superseding an approved contribution calls the retire bridge for
    the contribution it replaces - without depending on a real Qdrant
    collection existing in this environment. `retire_contribution_promotion`
    itself (the actual Qdrant-point deletion logic) is already covered
    deterministically with a fake writer in
    `test_retire_contribution_promotion_deletes_the_qdrant_point` above.
    """

    from app.modules.memorial_access import service as memorial_access_service

    owner_token = _register_and_login(client, "bridge-supersede-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    old_approved = _submit_and_approve_contribution(client, owner_token, profile_id, "Old version")

    retire_calls: list[int] = []
    original_retire = memorial_access_service.contribution_indexing_service.retire_contribution_promotion

    def _recording_retire(db, *, contribution):
        retire_calls.append(contribution.id)
        return original_retire(db, contribution=contribution)

    monkeypatch.setattr(
        memorial_access_service.contribution_indexing_service,
        "retire_contribution_promotion",
        _recording_retire,
    )

    new_submit = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(owner_token),
        json={"title": "New version", "memory_text": "Opravena verze vzpomínky.", "privacy_scope": "all_family"},
    )
    new_approve = client.post(
        f"/api/memorials/{profile_id}/contributions/{new_submit.json()['id']}/approve",
        headers=_auth_headers(owner_token),
        json={"review_note": "corrected", "supersedes_contribution_id": old_approved["id"]},
    )

    assert new_approve.status_code == 200
    assert new_approve.json()["supersedes_contribution_id"] == old_approved["id"]
    assert retire_calls == [old_approved["id"]]


def test_retire_contribution_promotion_deletes_the_qdrant_point(client):
    owner_token = _register_and_login(client, "bridge-retire-owner@example.com")
    profile_id = _create_memorial(client, owner_token)
    approved = _submit_and_approve_contribution(client, owner_token, profile_id)

    db = _db()
    try:
        promotion = get_promotion_by_contribution_id(db, contribution_id=approved["id"])
        writer = FakeWriter()
        encoder = FakeEncoder()
        index_contribution_promotion(
            db, profile_id=profile_id, promotion_id=promotion.id, writer=writer, encoder=encoder, validate_runtime=False
        )
        db.refresh(promotion)
        point_key = (promotion.target_collection_name, promotion.qdrant_point_id)
        assert point_key in writer.points

        from app.modules.memorial_access import repository as memorial_repository

        contribution = memorial_repository.get_contribution(
            db, profile_id=profile_id, contribution_id=approved["id"]
        )
        retire_contribution_promotion(db, contribution=contribution, writer=writer)

        assert point_key not in writer.points
        assert writer.delete_calls == 1
        db.refresh(promotion)
        assert promotion.promotion_status == "retired"

        # Idempotent: retiring an already-retired promotion is a safe no-op.
        retire_contribution_promotion(db, contribution=contribution, writer=writer)
        assert writer.delete_calls == 1
    finally:
        db.close()
