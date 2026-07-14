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
from app.modules.rag_retrieval.schemas import RagRetrievalResponseRead, RagRetrievalResultRead


CZECH_QUESTION = "Kde jsi žila v dětství?"
RUSSIAN_TRANSLATION_OF_QUESTION = "Где ты жила в детстве?"
RUSSIAN_ANSWER = "В детстве я жила с родителями у Попице."
CZECH_TRANSLATION_OF_ANSWER = "V dětství jsem žila s rodiči u Popice."


def _create_demo_profile():
    db = app.state.testing_session_local()
    try:
        user = register_user(
            db,
            RegisterRequest(
                email=FAMILY_AVATAR_RU_E2E_EMAIL,
                password=FAMILY_AVATAR_RU_E2E_PASSWORD,
                full_name="FA Demo Bilingual Test User",
            ),
        )
        profile = create_memory_profile(
            db,
            current_user=user,
            payload=MemoryProfileCreate(
                name=FAMILY_AVATAR_RU_E2E_PROFILE_NAME,
                biography="Test profile for bilingual demo chat.",
                personality="Warm and factual.",
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


class ScriptedChatTranslationProvider:
    provider_name = "scripted"

    def __init__(self):
        self.calls: list[tuple[str, str, str]] = []

    def translate(self, *, source_text, source_language, target_language):
        self.calls.append((source_text, source_language, target_language))
        from app.modules.content_translation.provider import ContentTranslationProviderResponse
        from app.modules.content_translation.schemas import ProviderTranslationResult

        if source_language == "cs" and target_language == "ru":
            translated = RUSSIAN_TRANSLATION_OF_QUESTION
        elif source_language == "ru" and target_language == "cs":
            translated = CZECH_TRANSLATION_OF_ANSWER
        else:
            translated = f"[{target_language}] {source_text}"
        return ContentTranslationProviderResponse(
            result=ProviderTranslationResult(translated_text=translated),
            provider_name=self.provider_name,
            model="scripted",
            latency_ms=1,
        )


def _patch_chat_runtime(monkeypatch, *, recorded_queries: list[str]):
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

    def fake_retrieve(db, *, current_user, profile_id, payload):
        recorded_queries.append(payload.query)
        return _build_retrieval_response(profile_id, payload.query)

    monkeypatch.setattr("app.modules.demo_fa_chat.service.retrieve_profile_rag", fake_retrieve)
    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.get_agent_orchestrator",
        lambda: SimpleNamespace(
            generate_chat_response=lambda request: SimpleNamespace(
                text=RUSSIAN_ANSWER,
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


def test_czech_locale_question_is_translated_for_retrieval_and_answer_translated_back(client, monkeypatch):
    _user, profile = _create_demo_profile()
    recorded_queries: list[str] = []
    _patch_chat_runtime(monkeypatch, recorded_queries=recorded_queries)
    scripted_provider = ScriptedChatTranslationProvider()
    monkeypatch.setattr(
        "app.modules.content_translation.service.build_content_translation_provider",
        lambda *, provider_name=None, provider_settings=None: scripted_provider,
    )

    response = client.post(
        "/api/demo/fa-chat/message",
        headers={"X-Request-ID": "cs-trace-1"},
        json={"message": CZECH_QUESTION, "locale": "cs"},
    )

    assert response.status_code == 200
    body = response.json()
    # The Czech-visible answer is the backend-translated Czech text, never
    # the raw Russian Brain answer.
    assert body["answer"] == CZECH_TRANSLATION_OF_ANSWER
    assert body["locale"] == "cs"
    assert body["trace_id"] == "cs-trace-1"
    # Internal technical markers never leak to the user-visible answer.
    assert "[rag:" not in body["answer"]
    assert "[memory:" not in body["answer"]
    # Retrieval/Brain ran on the Russian translation, not the raw Czech text -
    # proving the existing Russian pipeline is unchanged and still receives
    # Russian input for a Czech-locale turn.
    assert recorded_queries[0] == RUSSIAN_TRANSLATION_OF_QUESTION
    assert scripted_provider.calls[0] == (CZECH_QUESTION, "cs", "ru")
    assert scripted_provider.calls[1] == (RUSSIAN_ANSWER, "ru", "cs")


def test_russian_locale_default_behavior_is_unchanged(client, monkeypatch):
    _user, profile = _create_demo_profile()
    recorded_queries: list[str] = []
    _patch_chat_runtime(monkeypatch, recorded_queries=recorded_queries)
    scripted_provider = ScriptedChatTranslationProvider()
    monkeypatch.setattr(
        "app.modules.content_translation.service.build_content_translation_provider",
        lambda *, provider_name=None, provider_settings=None: scripted_provider,
    )

    response = client.post(
        "/api/demo/fa-chat/message",
        headers={"X-Request-ID": "ru-trace-1"},
        json={"message": "Где ты жила в детстве?"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["answer"] == RUSSIAN_ANSWER
    assert body["locale"] == "ru"
    # No translation call is ever made for a Russian-locale (default) turn.
    assert scripted_provider.calls == []
    assert recorded_queries[0] == "Где ты жила в детстве?"
