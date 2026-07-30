from __future__ import annotations

from datetime import datetime, timezone
import importlib

import pytest

from app.core.metrics import MEMORY_PROMOTION_INDEX_STATUS_TOTAL, MEMORY_PROMOTION_STATUS_TOTAL
from app.db.models import AvatarMemoryPromotion, RagChunk, RagEmbedding, RagSource, RagVectorIndex
from app.main import app
from app.modules.auth.schemas import RegisterRequest
from app.modules.auth.service import register_user
from app.modules.avatar_memory_indexing.schemas import AvatarMemoryIndexingRead
from app.modules.avatar_memory_indexing.service import (
    AvatarMemoryIndexingConflictError,
    AvatarMemoryIndexingEligibilityError,
    AvatarMemoryIndexingExecutionError,
    build_deterministic_point_id,
    index_promotion,
)
from app.modules.avatar_memory_promotions.service import cancel_promotion
from app.modules.conversation_memory_candidates.schemas import (
    MemoryCandidateCreate,
    MemoryCandidateReviewUpdate,
)
from app.modules.conversation_memory_candidates.service import approve_candidate, create_candidate
from app.modules.embeddings.providers.base import EmbeddingVector
from app.modules.memory_profiles.schemas import MemoryProfileCreate
from app.modules.memory_profiles.service import create_memory_profile
from app.modules.rag_retrieval.repository import list_retrieval_evidence_for_embeddings
from scripts.index_approved_memory_promotions import run_indexing


class FakeEncoder:
    def __init__(self) -> None:
        self.calls = 0

    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        self.calls += 1
        assert text
        assert model_code == "bge_m3_dense_sparse"
        return EmbeddingVector(
            values=[0.01] * 1024,
            dimension=1024,
            metadata={"sparse_vector": {"плаванию": 0.8}, "provider_name": "bge_m3_hybrid"},
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


def _create_pending_promotion(*, approve: bool = True):
    db = _db()
    user = register_user(
        db,
        RegisterRequest(
            email="index-owner@example.com",
            password="StrongPass123",
            full_name="Index Owner",
        ),
    )
    profile = create_memory_profile(
        db,
        current_user=user,
        payload=MemoryProfileCreate(
            name="Index Profile",
            biography="Biography",
            personality="Careful",
        ),
    )
    candidate = create_candidate(
        db,
        payload=MemoryCandidateCreate(
            owner_user_id=user.id,
            avatar_id="eva_novakova_demo",
            profile_id=profile.id,
            trace_id="index-trace",
            user_message_excerpt="Я выиграл чемпионат мира по плаванию.",
            proposed_memory_text="Пользователь выиграл чемпионат мира по плаванию.",
            reason="Новый личный факт.",
            language="ru",
        ),
    )
    if approve:
        outcome = approve_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=MemoryCandidateReviewUpdate(reviewed_by=user.id, review_note="Проверено"),
        )
        promotion = outcome.promotion
    else:
        promotion = AvatarMemoryPromotion(
            candidate_id=candidate.id,
            owner_user_id=user.id,
            avatar_id=candidate.avatar_id,
            profile_id=profile.id,
            source_type="conversation_candidate",
            promotion_status="pending_index",
            approved_memory_text=candidate.proposed_memory_text,
            normalized_memory_text=candidate.proposed_memory_text,
            language="ru",
            source_candidate_status_snapshot="needs_review",
        )
        db.add(promotion)
        db.commit()
        db.refresh(promotion)
    return db, user, profile, candidate, promotion


def _index(db, user, promotion, writer, encoder):
    return index_promotion(
        db,
        owner_user_id=user.id,
        promotion_id=promotion.id,
        writer=writer,
        encoder=encoder,
        validate_runtime=False,
    )


def test_indexes_approved_pending_promotion_and_creates_searchable_evidence(client):
    db, user, profile, _candidate, promotion = _create_pending_promotion()
    writer = FakeWriter()
    encoder = FakeEncoder()
    try:
        assert db.query(RagSource).count() == 0
        assert db.query(RagChunk).count() == 0
        assert db.query(RagEmbedding).count() == 0

        result = _index(db, user, promotion, writer, encoder)

        assert result.promotion_status == "indexed"
        assert result.searchable_as_fact is True
        assert result.target_collection_name
        assert result.qdrant_point_id == build_deterministic_point_id(promotion=promotion)
        assert writer.upsert_calls == 1
        assert db.query(RagSource).count() == 1
        assert db.query(RagChunk).count() == 1
        assert db.query(RagEmbedding).count() == 1
        assert db.query(RagVectorIndex).count() == 1
        db.refresh(promotion)
        assert promotion.indexed_at is not None
        assert promotion.indexing_attempt_count == 1

        evidence = list_retrieval_evidence_for_embeddings(
            db,
            owner_user_id=user.id,
            profile_id=profile.id,
            embedding_ids=[promotion.rag_embedding_id],
        )
        assert len(evidence) == 1
        assert evidence[0].chunk_text == promotion.approved_memory_text
        assert evidence[0].source_type == "conversation_candidate"
        point = next(iter(writer.points.values()))
        payload = point["payload"]
        assert payload["promotion_id"] == promotion.id
        assert payload["memory_status"] == "verified"
        assert payload["provenance"] == "review_approved_conversation_candidate"
        assert "text" not in payload
        assert "raw_text" not in payload
    finally:
        db.close()


def test_rejects_needs_review_source_candidate(client):
    db, user, _profile, _candidate, promotion = _create_pending_promotion(approve=False)
    try:
        with pytest.raises(AvatarMemoryIndexingEligibilityError):
            _index(db, user, promotion, FakeWriter(), FakeEncoder())
        db.refresh(promotion)
        assert promotion.promotion_status == "pending_index"
        assert promotion.indexing_attempt_count == 0
    finally:
        db.close()


def test_rejects_cancelled_promotion(client):
    db, user, _profile, _candidate, promotion = _create_pending_promotion()
    try:
        cancel_promotion(db, owner_user_id=user.id, promotion_id=promotion.id)
        with pytest.raises(AvatarMemoryIndexingEligibilityError):
            _index(db, user, promotion, FakeWriter(), FakeEncoder())
        db.refresh(promotion)
        assert promotion.promotion_status == "cancelled"
    finally:
        db.close()


def test_exact_rerun_is_idempotent_and_does_not_duplicate(client):
    db, user, _profile, _candidate, promotion = _create_pending_promotion()
    writer = FakeWriter()
    encoder = FakeEncoder()
    try:
        before_index_events = MEMORY_PROMOTION_INDEX_STATUS_TOTAL.labels("indexed")._value.get()
        before_skipped_events = MEMORY_PROMOTION_INDEX_STATUS_TOTAL.labels("skipped")._value.get()
        before_status_events = MEMORY_PROMOTION_STATUS_TOTAL.labels("indexed")._value.get()
        first = _index(db, user, promotion, writer, encoder)
        after_first_index_events = MEMORY_PROMOTION_INDEX_STATUS_TOTAL.labels("indexed")._value.get()
        after_first_status_events = MEMORY_PROMOTION_STATUS_TOTAL.labels("indexed")._value.get()
        second = _index(db, user, promotion, writer, encoder)
        assert first.result == "indexed"
        assert second.result == "already_indexed"
        assert writer.upsert_calls == 1
        assert len(writer.points) == 1
        assert encoder.calls == 1
        assert db.query(RagSource).count() == 1
        assert db.query(RagEmbedding).count() == 1
        assert after_first_index_events == before_index_events + 1
        assert after_first_status_events == before_status_events + 1
        assert MEMORY_PROMOTION_INDEX_STATUS_TOTAL.labels("indexed")._value.get() == after_first_index_events
        assert MEMORY_PROMOTION_STATUS_TOTAL.labels("indexed")._value.get() == after_first_status_events
        assert MEMORY_PROMOTION_INDEX_STATUS_TOTAL.labels("skipped")._value.get() == before_skipped_events + 1
    finally:
        db.close()


def test_conflicting_deterministic_point_fails_without_overwrite(client):
    db, user, _profile, _candidate, promotion = _create_pending_promotion()
    writer = FakeWriter()
    encoder = FakeEncoder()
    try:
        _index(db, user, promotion, writer, encoder)
        point = next(iter(writer.points.values()))
        point["payload"]["text_hash"] = "conflict"
        with pytest.raises(AvatarMemoryIndexingConflictError):
            _index(db, user, promotion, writer, encoder)
        assert writer.upsert_calls == 1
        db.refresh(promotion)
        assert promotion.promotion_status == "failed"
        assert list_retrieval_evidence_for_embeddings(
            db,
            owner_user_id=user.id,
            profile_id=promotion.profile_id,
            embedding_ids=[promotion.rag_embedding_id],
        ) == []
    finally:
        db.close()


def test_failed_qdrant_write_marks_promotion_failed_safely(client):
    db, user, _profile, _candidate, promotion = _create_pending_promotion()
    writer = FakeWriter(fail_upsert=True)
    try:
        with pytest.raises(AvatarMemoryIndexingExecutionError):
            _index(db, user, promotion, writer, FakeEncoder())
        db.refresh(promotion)
        assert promotion.promotion_status == "failed"
        assert promotion.failed_at is not None
        assert promotion.indexed_at is None
        assert promotion.failure_reason == "Approved memory indexing failed"
        assert promotion.indexing_attempt_count == 1
        assert writer.points == {}
        assert db.query(RagSource).count() == 0
        assert db.query(RagChunk).count() == 0
        assert db.query(RagEmbedding).count() == 0
    finally:
        db.close()


def test_point_id_is_stable(client):
    db, _user, _profile, _candidate, promotion = _create_pending_promotion()
    try:
        first = build_deterministic_point_id(promotion=promotion)
        second = build_deterministic_point_id(promotion=promotion)
        assert first == second
    finally:
        db.close()


def test_existing_point_with_invalid_payload_is_not_overwritten(client):
    db, user, _profile, _candidate, promotion = _create_pending_promotion()
    writer = FakeWriter()
    encoder = FakeEncoder()
    try:
        _index(db, user, promotion, writer, encoder)
        point = next(iter(writer.points.values()))
        point["payload"] = None
        with pytest.raises(AvatarMemoryIndexingConflictError):
            _index(db, user, promotion, writer, encoder)
        assert writer.upsert_calls == 1
        db.refresh(promotion)
        assert promotion.promotion_status == "failed"
    finally:
        db.close()


def test_dry_run_summary_does_not_mutate_or_embed(client):
    db, _user, _profile, _candidate, promotion = _create_pending_promotion()
    writer = FakeWriter()
    encoder = FakeEncoder()
    try:
        summary = run_indexing(
            db,
            promotion_id=promotion.id,
            avatar_id=None,
            profile_id=None,
            limit=10,
            dry_run=True,
            writer=writer,
            encoder=encoder,
            validate_runtime=False,
        )
        assert summary["eligible"] == 1
        assert summary["indexed"] == 0
        assert writer.upsert_calls == 0
        assert encoder.calls == 0
        db.refresh(promotion)
        assert promotion.promotion_status == "pending_index"
        assert promotion.indexing_attempt_count == 0
        assert db.query(RagSource).count() == 0
    finally:
        db.close()


def test_cli_invalid_pending_candidate_is_skipped_not_eligible(client):
    db, _user, _profile, _candidate, promotion = _create_pending_promotion(approve=False)
    try:
        summary = run_indexing(
            db,
            promotion_id=promotion.id,
            avatar_id=None,
            profile_id=None,
            limit=10,
            dry_run=True,
            writer=FakeWriter(),
            encoder=FakeEncoder(),
            validate_runtime=False,
        )
        assert summary["eligible"] == 0
        assert summary["failed"] == 0
        assert summary["skipped"] == 1
    finally:
        db.close()


def test_cli_batch_limit_is_applied_to_pending_promotions_only(client):
    db, user, profile, _candidate, terminal_promotion = _create_pending_promotion()
    try:
        terminal_promotion.promotion_status = "indexed"
        terminal_promotion.indexed_at = datetime.now(timezone.utc)
        candidate = create_candidate(
            db,
            payload=MemoryCandidateCreate(
                owner_user_id=user.id,
                avatar_id="eva_novakova_demo",
                profile_id=profile.id,
                trace_id="index-trace-second",
                user_message_excerpt="Вторая семейная история.",
                proposed_memory_text="Пользователь рассказал вторую семейную историю.",
                reason="Новый семейный факт.",
                language="ru",
            ),
        )
        pending_promotion = approve_candidate(
            db,
            owner_user_id=user.id,
            candidate_id=candidate.id,
            payload=MemoryCandidateReviewUpdate(reviewed_by=user.id),
        ).promotion

        summary = run_indexing(
            db,
            promotion_id=None,
            avatar_id=None,
            profile_id=None,
            limit=1,
            dry_run=False,
            writer=FakeWriter(),
            encoder=FakeEncoder(),
            validate_runtime=False,
        )
        assert summary["eligible"] == 1
        assert summary["indexed"] == 1
        assert summary["already_indexed"] == 0
        db.refresh(pending_promotion)
        assert pending_promotion.promotion_status == "indexed"
    finally:
        db.close()


def test_script_execute_and_failure_summaries(client):
    db, _user, _profile, _candidate, promotion = _create_pending_promotion()
    try:
        success = run_indexing(
            db,
            promotion_id=promotion.id,
            avatar_id=None,
            profile_id=None,
            limit=10,
            dry_run=False,
            writer=FakeWriter(),
            encoder=FakeEncoder(),
            validate_runtime=False,
        )
        assert success["eligible"] == 1
        assert success["indexed"] == 1
    finally:
        db.close()

    # A fresh per-test database is supplied by the fixture, so create another pending row in this one.
    db = _db()
    try:
        # Execute mode verifies indexed rows and repairs a missing deterministic point.
        summary = run_indexing(
            db,
            promotion_id=promotion.id,
            avatar_id=None,
            profile_id=None,
            limit=10,
            dry_run=False,
            writer=FakeWriter(),
            encoder=FakeEncoder(),
            validate_runtime=False,
        )
        assert summary["indexed"] == 1
        stored = db.get(AvatarMemoryPromotion, promotion.id)
        stored.promotion_status = "pending_index"
        stored.indexed_at = None
        db.commit()
        failed = run_indexing(
            db,
            promotion_id=promotion.id,
            avatar_id=None,
            profile_id=None,
            limit=10,
            dry_run=False,
            writer=FakeWriter(fail_upsert=True),
            encoder=FakeEncoder(),
            validate_runtime=False,
        )
        assert failed["eligible"] == 1
        assert failed["failed"] == 1
    finally:
        db.close()


def test_index_api_success_not_found_invalid_status_and_idempotent_response(client, monkeypatch):
    router_module = importlib.import_module("app.modules.demo_fa_chat.router")
    now = datetime.now(timezone.utc)
    success = AvatarMemoryIndexingRead(
        promotion_id=1,
        promotion_status="indexed",
        indexed_at=now,
        target_collection_name="demo-memory",
        qdrant_point_id="point-1",
        searchable_as_fact=True,
        result="indexed",
    )
    monkeypatch.setattr(router_module, "index_demo_memory_promotion", lambda *_args, **_kwargs: success)
    response = client.post("/api/demo/fa-chat/memory-promotions/1/index")
    assert response.status_code == 200
    assert response.json()["searchable_as_fact"] is True

    from app.modules.avatar_memory_promotions.service import AvatarMemoryPromotionNotFoundError

    def not_found(*_args, **_kwargs):
        raise AvatarMemoryPromotionNotFoundError()

    monkeypatch.setattr(router_module, "index_demo_memory_promotion", not_found)
    assert client.post("/api/demo/fa-chat/memory-promotions/999/index").status_code == 404

    def invalid(*_args, **_kwargs):
        raise AvatarMemoryIndexingEligibilityError()

    monkeypatch.setattr(router_module, "index_demo_memory_promotion", invalid)
    assert client.post("/api/demo/fa-chat/memory-promotions/1/index").status_code == 409

    idempotent = success.model_copy(update={"result": "already_indexed"})
    monkeypatch.setattr(
        router_module,
        "index_demo_memory_promotion",
        lambda *_args, **_kwargs: idempotent,
    )
    assert client.post("/api/demo/fa-chat/memory-promotions/1/index").json()["result"] == "already_indexed"
