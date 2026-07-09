from __future__ import annotations

from types import SimpleNamespace

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
from app.modules.demo_fa_chat.service import (
    DEMO_FA_CHAT_NOT_INITIALIZED_DETAIL,
    DemoFaChatInitializationError,
)
from app.modules.rag_retrieval.schemas import RagRetrievalResponseRead, RagRetrievalResultRead


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
                full_name="FA Demo Test User",
            ),
        )
        profile = create_memory_profile(
            db,
            current_user=user,
            payload=MemoryProfileCreate(
                name=FAMILY_AVATAR_RU_E2E_PROFILE_NAME,
                biography="Тестовый профиль для демо-чата.",
                personality="Тёплая и фактическая.",
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
                qdrant_collection="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
                payload_metadata={},
            )
        ],
    )


def test_demo_fa_chat_empty_message_returns_400(client):
    response = client.post(
        "/api/demo/fa-chat/message",
        json={"message": "   "},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Сообщение не должно быть пустым."


def test_demo_fa_chat_too_long_message_returns_400(client):
    response = client.post(
        "/api/demo/fa-chat/message",
        json={"message": "а" * 4001},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Сообщение слишком длинное для демо-чата."


def test_demo_fa_chat_returns_profile_unavailable_when_default_profile_missing(client):
    response = client.post(
        "/api/demo/fa-chat/message",
        json={"message": "Где Павел жил в детстве?"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Тестовый профиль аватара сейчас недоступен."


def test_demo_fa_chat_valid_message_returns_answer_with_default_profile_and_trace(client, monkeypatch):
    _user, profile = _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile: SimpleNamespace(
            collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
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
                text="В детстве я жила с родителями у Попице. [rag:27618]",
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

    response = client.post(
        "/api/demo/fa-chat/message",
        headers={"X-Request-ID": "demo-trace-1"},
        json={"message": "Где ты жила в детстве?"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["answer"] == "В детстве я жила с родителями у Попице. [rag:27618]"
    assert body["trace_id"] == "demo-trace-1"
    assert body["guard_applied"] is False
    assert body["guard_reason"] is None
    assert body["retrieval_used"] is True
    assert body["lack_of_evidence"] is False
    assert body["evidence"] == []
    assert profile.id > 0


def test_demo_fa_chat_debug_true_includes_evidence_preview(client, monkeypatch):
    _user, profile = _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile: SimpleNamespace(
            collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
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
                text="В детстве я жила с родителями у Попице. [rag:27618]",
                provider_name="mock-brain",
                metadata={
                    "grounding_status": "grounded",
                    "output_guard_applied": True,
                    "output_guard_reason": "demo_reason",
                    "output_guard_lack_of_evidence": False,
                },
            )
        ),
    )

    response = client.post(
        "/api/demo/fa-chat/message",
        json={
            "profile_id": profile.id,
            "message": "Где ты жила в детстве?",
            "debug": True,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["guard_applied"] is True
    assert body["guard_reason"] == "demo_reason"
    assert len(body["evidence"]) == 1
    assert body["evidence"][0]["chunk_id"] == "27618"
    assert "Попице" in body["evidence"][0]["text_preview"]


def test_demo_fa_chat_returns_safe_error_when_demo_runtime_is_not_initialized(client, monkeypatch):
    _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda *args, **kwargs: (_ for _ in ()).throw(
            DemoFaChatInitializationError(DEMO_FA_CHAT_NOT_INITIALIZED_DETAIL)
        ),
    )

    response = client.post(
        "/api/demo/fa-chat/message",
        json={"message": "Где ты жила в детстве?"},
    )

    assert response.status_code == 503
    assert response.json()["detail"] == DEMO_FA_CHAT_NOT_INITIALIZED_DETAIL


def test_demo_fa_chat_internal_errors_return_safe_russian_response(client, monkeypatch):
    _user, profile = _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile: SimpleNamespace(
            collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
            retrieval_mode="bge_m3_dense_sparse",
            top_k=5,
            source_id=7,
            point_count=20,
        ),
    )
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.retrieve_profile_rag",
        lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("boom")),
    )

    response = client.post(
        "/api/demo/fa-chat/message",
        json={"profile_id": profile.id, "message": "Где ты жила в детстве?"},
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "Не удалось получить ответ аватара. Попробуйте ещё раз."
