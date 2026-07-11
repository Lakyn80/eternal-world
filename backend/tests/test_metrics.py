from __future__ import annotations

from types import SimpleNamespace

from prometheus_client.parser import text_string_to_metric_families

from app.main import app
from app.modules.auth.schemas import RegisterRequest
from app.modules.auth.service import register_user
from app.modules.memory_profiles.schemas import MemoryProfileCreate
from app.modules.memory_profiles.service import create_memory_profile
from app.modules.rag_evaluation.brain_eval_e2e_bootstrap import (
    FAMILY_AVATAR_RU_E2E_EMAIL,
    FAMILY_AVATAR_RU_E2E_PASSWORD,
    FAMILY_AVATAR_RU_E2E_PROFILE_NAME,
)
from app.modules.rag_retrieval.schemas import RagRetrievalResponseRead, RagRetrievalResultRead


DEMO_COLLECTION_NAME = "eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu"


def _get_test_db_session():
    testing_session_local = app.state.testing_session_local
    return testing_session_local()


def _create_demo_profile():
    db = _get_test_db_session()
    try:
        user = register_user(
            db,
            RegisterRequest(
                email=FAMILY_AVATAR_RU_E2E_EMAIL,
                password=FAMILY_AVATAR_RU_E2E_PASSWORD,
                full_name="Metrics Demo Test User",
            ),
        )
        profile = create_memory_profile(
            db,
            current_user=user,
            payload=MemoryProfileCreate(
                name=FAMILY_AVATAR_RU_E2E_PROFILE_NAME,
                biography="Тестовый профиль для metrics.",
                personality="Спокойная и точная.",
            ),
        )
        return user, profile
    finally:
        db.close()


def _build_retrieval_response(profile_id: int, query: str) -> RagRetrievalResponseRead:
    return RagRetrievalResponseRead(
        profile_id=profile_id,
        query=query,
        model_code="bge_m3_dense_sparse",
        results=[
            RagRetrievalResultRead(
                chunk_id=27618,
                source_id=7,
                source_title="Family Novak RU E2E Corpus",
                embedding_id=43591,
                score=0.99,
                text="В детстве Ева жила с родителями в домике со сливовым садом у Попице.",
                chunk_index=0,
                language="ru",
                source_type="manual_text",
                validation_status="valid",
                text_hash="hash-27618",
                qdrant_collection=DEMO_COLLECTION_NAME,
                payload_metadata={},
            )
        ],
    )


def _metrics_text(client) -> str:
    response = client.get("/metrics")
    assert response.status_code == 200
    return response.text


def _sample_value(metrics_text: str, metric_name: str, labels: dict[str, str]) -> float:
    for family in text_string_to_metric_families(metrics_text):
        for sample in family.samples:
            if sample.name != metric_name:
                continue
            if all(sample.labels.get(key) == value for key, value in labels.items()):
                return float(sample.value)
    return 0.0


def test_metrics_endpoint_exists(client):
    body = _metrics_text(client)

    assert "http_requests_total" in body
    assert "fa_chat_requests_total" in body
    assert "rag_retrieval_duration_seconds" in body
    assert "brain_answer_duration_seconds" in body
    assert "embedding_cache_hits_total" in body
    assert "memory_promotion_created_total" in body
    assert "memory_promotion_status_total" in body


def test_fa_chat_metrics_increment_for_successful_request(client, monkeypatch):
    _user, profile = _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile: SimpleNamespace(
            collection_name=DEMO_COLLECTION_NAME,
            retrieval_mode="bge_m3_dense_sparse",
            top_k=5,
            source_id=7,
            point_count=20,
        ),
    )
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.retrieve_profile_rag",
        lambda db, *, current_user, profile_id, payload: _build_retrieval_response(profile_id, payload.query),
    )
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.get_agent_orchestrator",
        lambda: SimpleNamespace(
            generate_chat_response=lambda request: SimpleNamespace(
                text="В детстве я жила у Попице. [rag:27618]",
                provider_name="mock-brain",
                metadata={
                    "grounding_status": "grounded",
                    "output_guard_applied": False,
                    "output_guard_reason": None,
                    "output_guard_lack_of_evidence": False,
                },
            )
        ),
    )

    before_metrics = _metrics_text(client)
    before_requests = _sample_value(
        before_metrics,
        "fa_chat_requests_total",
        {
            "outcome": "success",
            "retrieval_used": "true",
            "guard_applied": "false",
            "guard_reason": "none",
            "debug": "false",
        },
    )

    response = client.post(
        "/api/demo/fa-chat/message",
        headers={"X-Request-ID": "metrics-trace-1"},
        json={"profile_id": profile.id, "message": "Где ты жила в детстве?"},
    )

    assert response.status_code == 200

    after_metrics = _metrics_text(client)
    after_requests = _sample_value(
        after_metrics,
        "fa_chat_requests_total",
        {
            "outcome": "success",
            "retrieval_used": "true",
            "guard_applied": "false",
            "guard_reason": "none",
            "debug": "false",
        },
    )
    retrieval_histogram_count = _sample_value(
        after_metrics,
        "rag_retrieval_duration_seconds_count",
        {"retrieval_mode": "bge_m3_dense_sparse", "top_k": "5"},
    )
    chunks_histogram_count = _sample_value(
        after_metrics,
        "rag_retrieved_chunks_count_count",
        {"retrieval_mode": "bge_m3_dense_sparse", "top_k": "5"},
    )

    assert after_requests == before_requests + 1
    assert retrieval_histogram_count >= 1
    assert chunks_histogram_count >= 1
    assert "Где ты жила в детстве?" not in after_metrics
    assert "metrics-trace-1" not in after_metrics
    assert DEMO_COLLECTION_NAME not in after_metrics


def test_fa_chat_lack_of_evidence_metric_increments(client, monkeypatch):
    _user, profile = _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile: SimpleNamespace(
            collection_name=DEMO_COLLECTION_NAME,
            retrieval_mode="bge_m3_dense_sparse",
            top_k=5,
            source_id=7,
            point_count=20,
        ),
    )
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.retrieve_profile_rag",
        lambda db, *, current_user, profile_id, payload: _build_retrieval_response(profile_id, payload.query),
    )
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.get_agent_orchestrator",
        lambda: SimpleNamespace(
            generate_chat_response=lambda request: SimpleNamespace(
                text="В сохранённых воспоминаниях этого нет.",
                provider_name="mock-brain",
                metadata={
                    "grounding_status": "no_evidence",
                    "output_guard_applied": False,
                    "output_guard_reason": None,
                    "output_guard_lack_of_evidence": True,
                },
            )
        ),
    )

    before_metrics = _metrics_text(client)
    before_lack = _sample_value(
        before_metrics,
        "fa_chat_lack_of_evidence_total",
        {"debug": "true"},
    )

    response = client.post(
        "/api/demo/fa-chat/message",
        json={"profile_id": profile.id, "message": "Была ли ты в Париже?", "debug": True},
    )

    assert response.status_code == 200

    after_metrics = _metrics_text(client)
    after_lack = _sample_value(
        after_metrics,
        "fa_chat_lack_of_evidence_total",
        {"debug": "true"},
    )

    assert after_lack == before_lack + 1


def test_fa_chat_guard_metric_increments(client, monkeypatch):
    _user, profile = _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile: SimpleNamespace(
            collection_name=DEMO_COLLECTION_NAME,
            retrieval_mode="bge_m3_dense_sparse",
            top_k=5,
            source_id=7,
            point_count=20,
        ),
    )
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.retrieve_profile_rag",
        lambda db, *, current_user, profile_id, payload: _build_retrieval_response(profile_id, payload.query),
    )
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.get_agent_orchestrator",
        lambda: SimpleNamespace(
            generate_chat_response=lambda request: SimpleNamespace(
                text="В сохранённых воспоминаниях этого нет.",
                provider_name="mock-brain",
                metadata={
                    "grounding_status": "grounded",
                    "output_guard_applied": True,
                    "output_guard_reason": "forbidden_claim_in_lack_case",
                    "output_guard_lack_of_evidence": False,
                },
            )
        ),
    )

    before_metrics = _metrics_text(client)
    before_guard = _sample_value(
        before_metrics,
        "fa_chat_guard_applied_total",
        {"guard_reason": "forbidden_claim_in_lack_case", "debug": "false"},
    )

    response = client.post(
        "/api/demo/fa-chat/message",
        json={"profile_id": profile.id, "message": "Как звали твоего брата?"},
    )

    assert response.status_code == 200

    after_metrics = _metrics_text(client)
    after_guard = _sample_value(
        after_metrics,
        "fa_chat_guard_applied_total",
        {"guard_reason": "forbidden_claim_in_lack_case", "debug": "false"},
    )

    assert after_guard == before_guard + 1


def test_memory_review_and_promotion_metrics_increment(client, monkeypatch):
    _user, profile = _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile: SimpleNamespace(
            collection_name=DEMO_COLLECTION_NAME,
            retrieval_mode="bge_m3_dense_sparse",
            top_k=5,
            source_id=7,
            point_count=20,
        ),
    )
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.retrieve_profile_rag",
        lambda db, *, current_user, profile_id, payload: RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code="bge_m3_dense_sparse",
            results=[],
        ),
    )
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.get_agent_orchestrator",
        lambda: SimpleNamespace(
            generate_chat_response=lambda request: SimpleNamespace(
                text="Я не помню этого по тем воспоминаниям, которые у меня сейчас есть.",
                provider_name="mock-brain",
                metadata={
                    "grounding_status": "no_evidence",
                    "output_guard_applied": False,
                    "output_guard_reason": None,
                    "output_guard_lack_of_evidence": True,
                    "persona_applied": True,
                },
            )
        ),
    )

    before_metrics = _metrics_text(client)
    before_reviewed = _sample_value(
        before_metrics,
        "memory_candidate_reviewed_total",
        {"status": "approved"},
    )
    before_promotions_created = _sample_value(
        before_metrics,
        "memory_promotion_created_total",
        {},
    )
    before_promotion_status = _sample_value(
        before_metrics,
        "memory_promotion_status_total",
        {"status": "pending_index"},
    )

    create_response = client.post(
        "/api/demo/fa-chat/message",
        json={
            "profile_id": profile.id,
            "message": "Ты помнишь, как я выиграл чемпионат мира по плаванию?",
        },
    )
    candidate_id = create_response.json()["memory_candidate"]["candidate_id"]
    approve_response = client.post(
        f"/api/demo/fa-chat/memory-candidates/{candidate_id}/approve?profile_id={profile.id}",
        json={"review_note": "Подтверждено"},
    )

    assert approve_response.status_code == 200

    after_metrics = _metrics_text(client)
    after_reviewed = _sample_value(
        after_metrics,
        "memory_candidate_reviewed_total",
        {"status": "approved"},
    )
    after_promotions_created = _sample_value(
        after_metrics,
        "memory_promotion_created_total",
        {},
    )
    after_promotion_status = _sample_value(
        after_metrics,
        "memory_promotion_status_total",
        {"status": "pending_index"},
    )

    assert after_reviewed == before_reviewed + 1
    assert after_promotions_created == before_promotions_created + 1
    assert after_promotion_status == before_promotion_status + 1
    assert "Ты помнишь, как я выиграл чемпионат мира по плаванию?" not in after_metrics
    forbidden_labels = {"candidate_id", "promotion_id", "trace_id"}
    for family in text_string_to_metric_families(after_metrics):
        for sample in family.samples:
            assert forbidden_labels.isdisjoint(sample.labels.keys())
