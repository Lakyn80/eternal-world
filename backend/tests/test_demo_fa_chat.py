from __future__ import annotations

from types import SimpleNamespace

import pytest

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
    DEMO_FA_CHAT_EMBEDDING_UNAVAILABLE_DETAIL,
    DEMO_FA_CHAT_NOT_INITIALIZED_DETAIL,
    DemoFaChatInitializationError,
    _assert_embedding_runtime_ready,
)
from app.modules.embeddings.runtime import EmbeddingRuntimeDiagnostics
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
        lambda db, *, resolved_profile, locale="ru": SimpleNamespace(
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
    assert body["persona_applied"] is True
    assert body["guard_applied"] is False
    assert body["guard_reason"] is None
    assert body["retrieval_used"] is True
    assert body["lack_of_evidence"] is False
    assert body["memory_candidate"] is None
    assert body["emotion"]["primary"] == "warm_nostalgic"
    assert body["face_directives"]["expression"] == "gentle_smile"
    assert body["voice_directives"]["pace"] == "slow"
    assert body["evidence"] == []
    assert profile.id > 0


def test_demo_fa_chat_debug_true_includes_evidence_preview(client, monkeypatch):
    _user, profile = _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile, locale="ru": SimpleNamespace(
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
    assert body["persona_applied"] is True
    assert body["guard_applied"] is True
    assert body["guard_reason"] == "demo_reason"
    assert len(body["evidence"]) == 1
    assert body["evidence"][0]["chunk_id"] == "27618"
    assert "Попице" in body["evidence"][0]["text_preview"]


def test_demo_fa_chat_ordinary_question_issues_single_retrieval_call(client, monkeypatch):
    _user, profile = _create_demo_profile()
    call_count = {"n": 0}

    def fake_retrieve(db, *, current_user, profile_id, payload):
        call_count["n"] += 1
        return _build_retrieval_response(profile_id, payload.query)

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile, locale="ru": SimpleNamespace(
            collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
            retrieval_mode="bge_m3_dense_sparse",
            top_k=5,
            source_id=7,
            point_count=20,
        ),
    )
    monkeypatch.setattr("app.modules.demo_fa_chat.service.retrieve_profile_rag", fake_retrieve)
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
        json={"profile_id": profile.id, "message": "Где ты жила в детстве?"},
    )

    assert response.status_code == 200
    assert call_count["n"] == 1


def test_demo_fa_chat_corrected_memory_question_merges_two_retrieval_calls(client, monkeypatch):
    _user, profile = _create_demo_profile()
    seen_queries: list[str] = []

    verified_item = RagRetrievalResultRead(
        chunk_id=27640,
        source_id=10,
        source_title="Approved conversation memory",
        embedding_id=99999,
        score=0.4,
        text="По словам внука, бабушка часто пела ему песню «Спят усталые игрушки».",
        chunk_index=0,
        language="ru",
        source_type="conversation_candidate",
        validation_status="valid",
        text_hash="hash-27640",
        qdrant_collection="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
        payload_metadata={
            "memory_status": "verified",
            "provenance": "review_approved_conversation_candidate",
            "promotion_id": 5,
            "candidate_id": 14,
            "indexed_at": "2026-07-11T21:51:58.863798+00:00",
        },
    )
    archival_item = RagRetrievalResultRead(
        chunk_id=27618,
        source_id=7,
        source_title="Family Novak RU E2E Corpus",
        embedding_id=43591,
        score=0.99,
        text="Archival note unrelated to the song.",
        chunk_index=0,
        language="ru",
        source_type="manual_text",
        validation_status="valid",
        text_hash="hash-27618",
        qdrant_collection="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
        payload_metadata={},
    )

    def fake_retrieve(db, *, current_user, profile_id, payload):
        seen_queries.append(payload.query)
        # The verified item only surfaces on the expanded (second) query, to
        # prove the merge step actually combines both result sets.
        results = [archival_item, verified_item] if len(seen_queries) == 2 else [archival_item]
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code="bge_m3_dense_sparse",
            results=results,
        )

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile, locale="ru": SimpleNamespace(
            collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
            retrieval_mode="bge_m3_dense_sparse",
            top_k=5,
            source_id=7,
            point_count=20,
        ),
    )
    monkeypatch.setattr("app.modules.demo_fa_chat.service.retrieve_profile_rag", fake_retrieve)
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.get_agent_orchestrator",
        lambda: SimpleNamespace(
            generate_chat_response=lambda request: SimpleNamespace(
                text="Деточка, я пела тебе «Спят усталые игрушки». [rag:27640]",
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
        json={
            "profile_id": profile.id,
            "message": "Ты помнишь, какую песню я называл, а владелец потом исправил?",
            "debug": True,
        },
    )

    assert response.status_code == 200
    assert len(seen_queries) == 2
    assert seen_queries[0] == "Ты помнишь, какую песню я называл, а владелец потом исправил?"
    assert seen_queries[1] != seen_queries[0]
    # The expanded query must stay generic and must never contain the
    # dataset's expected answer.
    assert "спят усталые игрушки" not in seen_queries[1].casefold()
    body = response.json()
    evidence_chunk_ids = [item["chunk_id"] for item in body["evidence"]]
    assert "27640" in evidence_chunk_ids
    # The verified learned memory must be floated to the front despite its
    # lower raw score than the archival item.
    assert evidence_chunk_ids[0] == "27640"


def test_demo_fa_chat_creates_unverified_memory_candidate_for_new_personal_claim(client, monkeypatch):
    _user, profile = _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile, locale="ru": SimpleNamespace(
            collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
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
                text=(
                    "Я не помню этого по тем воспоминаниям, которые у меня сейчас есть. "
                    "Если хочешь, расскажи мне больше, и мы сможем сохранить это как новое воспоминание."
                ),
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

    response = client.post(
        "/api/demo/fa-chat/message",
        json={
            "profile_id": profile.id,
            "message": "Ты помнишь, как пела мне песню перед сном?",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["lack_of_evidence"] is True
    assert body["persona_applied"] is True
    assert body["memory_candidate_persisted"] is True
    assert body["memory_candidate"]["candidate_id"] is not None
    assert body["memory_candidate"]["status"] == "needs_review"
    assert body["memory_candidate"]["confidence"] == "unverified"
    assert body["memory_candidate"]["source"] == "conversation"
    assert "песню перед сном" in body["memory_candidate"]["proposed_memory_text"]
    assert body["emotion"]["primary"] == "warm_reflective"


def test_demo_fa_chat_candidate_persistence_failure_does_not_break_answer(client, monkeypatch):
    _user, profile = _create_demo_profile()
    logged_events: list[tuple[str, dict[str, object]]] = []

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile, locale="ru": SimpleNamespace(
            collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
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
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._persist_memory_candidate",
        lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("db write failed for candidate")),
    )
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.log_event",
        lambda logger, level, event, **fields: logged_events.append((event, fields)),
    )

    response = client.post(
        "/api/demo/fa-chat/message",
        headers={"X-Request-ID": "candidate-persist-fail-1"},
        json={
            "profile_id": profile.id,
            "message": "Ты помнишь, как пела мне песню перед сном?",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["memory_candidate"]["candidate_id"] is None
    assert body["memory_candidate"]["status"] == "needs_review"
    assert body["memory_candidate_persisted"] is False
    assert "песню перед сном" in body["memory_candidate"]["proposed_memory_text"]
    persist_failed_event = next(fields for event, fields in logged_events if event == "fa_demo_chat_memory_candidate_persist_failed")
    assert persist_failed_event["trace_id"] == "candidate-persist-fail-1"
    assert persist_failed_event["error_type"] == "RuntimeError"
    assert persist_failed_event["candidate_persisted"] is False
    assert "message" not in persist_failed_event
    assert "proposed_memory_text" not in persist_failed_event


def test_demo_fa_chat_memory_candidate_endpoints_cover_review_workflow(client, monkeypatch):
    _user, profile = _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile, locale="ru": SimpleNamespace(
            collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
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

    create_response = client.post(
        "/api/demo/fa-chat/message",
        json={
            "profile_id": profile.id,
            "message": "Ты помнишь, как пела мне песню перед сном?",
        },
    )
    assert create_response.status_code == 200
    candidate_id = create_response.json()["memory_candidate"]["candidate_id"]
    assert candidate_id is not None

    list_response = client.get(
        "/api/demo/fa-chat/memory-candidates",
        params={"profile_id": profile.id},
    )
    assert list_response.status_code == 200
    list_body = list_response.json()
    assert list_body["total"] == 1
    assert list_body["items"][0]["candidate_id"] == candidate_id
    assert list_body["items"][0]["status"] == "needs_review"

    get_response = client.get(
        f"/api/demo/fa-chat/memory-candidates/{candidate_id}",
        params={"profile_id": profile.id},
    )
    assert get_response.status_code == 200
    assert get_response.json()["candidate_id"] == candidate_id

    approve_response = client.post(
        f"/api/demo/fa-chat/memory-candidates/{candidate_id}/approve?profile_id={profile.id}",
        json={"review_note": "Подтверждено", "reviewed_by": _user.id},
    )
    assert approve_response.status_code == 200
    assert approve_response.json()["status"] == "approved"
    assert approve_response.json()["promotion_created"] is True
    assert approve_response.json()["promotion_id"] is not None
    assert approve_response.json()["promotion_status"] == "pending_index"
    assert approve_response.json()["searchable_as_fact"] is False

    invalid_transition_response = client.post(
        f"/api/demo/fa-chat/memory-candidates/{candidate_id}/archive?profile_id={profile.id}",
        json={"reviewed_by": _user.id},
    )
    assert invalid_transition_response.status_code == 409
    assert invalid_transition_response.json()["detail"] == "Недопустимое изменение статуса кандидата."

    missing_response = client.get(
        "/api/demo/fa-chat/memory-candidates/999",
        params={"profile_id": profile.id},
    )
    assert missing_response.status_code == 404
    assert missing_response.json()["detail"] == "Кандидат воспоминания не найден."


def test_demo_fa_chat_memory_candidate_reject_and_archive_endpoints(client, monkeypatch):
    _user, profile = _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile, locale="ru": SimpleNamespace(
            collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
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

    first_response = client.post(
        "/api/demo/fa-chat/message",
        json={
            "profile_id": profile.id,
            "message": "Ты помнишь, как пела мне колыбельную?",
        },
    )
    second_response = client.post(
        "/api/demo/fa-chat/message",
        json={
            "profile_id": profile.id,
            "message": "Ты помнишь, как мы вместе собирали яблоки?",
        },
    )
    first_candidate_id = first_response.json()["memory_candidate"]["candidate_id"]
    second_candidate_id = second_response.json()["memory_candidate"]["candidate_id"]

    reject_response = client.post(
        f"/api/demo/fa-chat/memory-candidates/{first_candidate_id}/reject?profile_id={profile.id}",
        json={
            "review_note": "Нужно больше контекста",
            "rejection_reason": "Нет подтверждения",
            "reviewed_by": _user.id,
        },
    )
    assert reject_response.status_code == 200
    assert reject_response.json()["status"] == "rejected"
    assert reject_response.json()["rejection_reason"] == "Нет подтверждения"

    archive_response = client.post(
        f"/api/demo/fa-chat/memory-candidates/{second_candidate_id}/archive?profile_id={profile.id}",
        json={"review_note": "Снято с рассмотрения", "reviewed_by": _user.id},
    )
    assert archive_response.status_code == 200
    assert archive_response.json()["status"] == "archived"
    assert archive_response.json()["rejection_reason"] is None


def test_demo_fa_chat_memory_promotion_endpoints_cover_cancel_workflow(client, monkeypatch):
    _user, profile = _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile, locale="ru": SimpleNamespace(
            collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
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
        json={"review_note": "Подтверждено", "reviewed_by": _user.id},
    )
    promotion_id = approve_response.json()["promotion_id"]

    list_response = client.get(
        "/api/demo/fa-chat/memory-promotions",
        params={"profile_id": profile.id},
    )
    assert list_response.status_code == 200
    assert list_response.json()["total"] == 1
    assert list_response.json()["items"][0]["promotion_id"] == promotion_id
    assert list_response.json()["items"][0]["promotion_status"] == "pending_index"
    assert list_response.json()["items"][0]["searchable_as_fact"] is False

    get_response = client.get(
        f"/api/demo/fa-chat/memory-promotions/{promotion_id}",
        params={"profile_id": profile.id},
    )
    assert get_response.status_code == 200
    assert get_response.json()["promotion_id"] == promotion_id
    assert get_response.json()["searchable_as_fact"] is False

    cancel_response = client.post(
        f"/api/demo/fa-chat/memory-promotions/{promotion_id}/cancel?profile_id={profile.id}",
    )
    assert cancel_response.status_code == 200
    assert cancel_response.json()["promotion_status"] == "cancelled"

    invalid_cancel_response = client.post(
        f"/api/demo/fa-chat/memory-promotions/{promotion_id}/cancel?profile_id={profile.id}",
    )
    assert invalid_cancel_response.status_code == 409
    assert invalid_cancel_response.json()["detail"] == "Недопустимое изменение статуса продвижения."

    missing_response = client.get(
        "/api/demo/fa-chat/memory-promotions/999",
        params={"profile_id": profile.id},
    )
    assert missing_response.status_code == 404
    assert missing_response.json()["detail"] == "Продвижение воспоминания не найдено."


def test_pending_index_promotion_is_not_used_as_factual_evidence(client, monkeypatch):
    _user, profile = _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile, locale="ru": SimpleNamespace(
            collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
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
                text=(
                    "Я не помню этого по тем воспоминаниям, которые у меня сейчас есть. "
                    "Если хочешь, расскажи мне больше, и мы сможем сохранить это как новое воспоминание."
                ),
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

    first_response = client.post(
        "/api/demo/fa-chat/message",
        json={
            "profile_id": profile.id,
            "message": "Ты помнишь, как я выиграл чемпионат мира по плаванию?",
        },
    )
    candidate_id = first_response.json()["memory_candidate"]["candidate_id"]
    approve_response = client.post(
        f"/api/demo/fa-chat/memory-candidates/{candidate_id}/approve?profile_id={profile.id}",
        json={"review_note": "Подтверждено", "reviewed_by": _user.id},
    )
    assert approve_response.status_code == 200
    assert approve_response.json()["promotion_status"] == "pending_index"
    assert approve_response.json()["searchable_as_fact"] is False

    second_response = client.post(
        "/api/demo/fa-chat/message",
        json={
            "profile_id": profile.id,
            "message": "Ты помнишь, как я выиграл чемпионат мира по плаванию?",
        },
    )

    assert second_response.status_code == 200
    assert second_response.json()["lack_of_evidence"] is True
    assert second_response.json()["memory_candidate"]["status"] == "needs_review"


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


def _build_embedding_runtime_diagnostics(
    *,
    model_code: str = "bge_m3_dense_sparse",
    bge_m3_snapshot_cached: bool = True,
    is_mock_query_provider: bool = False,
) -> EmbeddingRuntimeDiagnostics:
    return EmbeddingRuntimeDiagnostics(
        embedding_provider_setting="sentence_transformers",
        resolved_indexing_provider_name="bge_m3_hybrid",
        resolved_query_provider_name="mock" if is_mock_query_provider else "bge_m3_hybrid",
        is_mock_indexing_provider=False,
        is_mock_query_provider=is_mock_query_provider,
        indexing_query_providers_match=not is_mock_query_provider,
        model_code=model_code,
        model_display_name="BGE-M3 (dense+sparse)",
        provider_model_name="BAAI/bge-m3",
        embedding_dimension=1024,
        collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
        collection_vector_size=1024,
        flag_embedding_available=True,
        bge_m3_snapshot_cached=bge_m3_snapshot_cached,
        bge_m3_snapshot_path=(
            "/models/huggingface/hub/models--BAAI--bge-m3/snapshots/5617a9f"
            if bge_m3_snapshot_cached
            else None
        ),
        huggingface_offline_mode=True,
    )


def test_assert_embedding_runtime_ready_passes_when_snapshot_is_cached(monkeypatch):
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.resolve_embedding_runtime_diagnostics",
        lambda *, model_code, collection_name: _build_embedding_runtime_diagnostics(
            model_code=model_code,
        ),
    )

    _assert_embedding_runtime_ready(model_code="bge_m3_dense_sparse", collection_name="col")


def test_assert_embedding_runtime_ready_fails_clearly_when_snapshot_is_missing(monkeypatch):
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.resolve_embedding_runtime_diagnostics",
        lambda *, model_code, collection_name: _build_embedding_runtime_diagnostics(
            model_code=model_code,
            bge_m3_snapshot_cached=False,
        ),
    )

    with pytest.raises(DemoFaChatInitializationError) as exc_info:
        _assert_embedding_runtime_ready(model_code="bge_m3_dense_sparse", collection_name="col")

    assert str(exc_info.value) == DEMO_FA_CHAT_EMBEDDING_UNAVAILABLE_DETAIL


def test_assert_embedding_runtime_ready_fails_when_query_provider_is_mock(monkeypatch):
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.resolve_embedding_runtime_diagnostics",
        lambda *, model_code, collection_name: _build_embedding_runtime_diagnostics(
            model_code=model_code,
            is_mock_query_provider=True,
        ),
    )

    with pytest.raises(DemoFaChatInitializationError) as exc_info:
        _assert_embedding_runtime_ready(model_code="bge_m3_dense_sparse", collection_name="col")

    assert str(exc_info.value) == DEMO_FA_CHAT_EMBEDDING_UNAVAILABLE_DETAIL


def test_demo_fa_chat_returns_safe_503_when_embedding_runtime_is_unavailable(client, monkeypatch):
    _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda *args, **kwargs: (_ for _ in ()).throw(
            DemoFaChatInitializationError(DEMO_FA_CHAT_EMBEDDING_UNAVAILABLE_DETAIL)
        ),
    )

    response = client.post(
        "/api/demo/fa-chat/message",
        json={"message": "Где ты жила в детстве?"},
    )

    assert response.status_code == 503
    assert response.json()["detail"] == DEMO_FA_CHAT_EMBEDDING_UNAVAILABLE_DETAIL


def test_demo_fa_chat_internal_errors_return_safe_russian_response(client, monkeypatch):
    _user, profile = _create_demo_profile()

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        lambda db, *, resolved_profile, locale="ru": SimpleNamespace(
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
