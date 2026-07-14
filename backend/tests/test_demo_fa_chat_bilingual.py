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
CZECH_ANSWER = "V dětství jsem žila s rodiči u Popice."
RUSSIAN_QUESTION = "Где ты жила в детстве?"
RUSSIAN_ANSWER = "В детстве я жила с родителями у Попице."


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


class RecordingChatTranslationProvider:
    """Fails the test loudly if the chat path ever calls it.

    Task 64.5.2 replaces the Task 64.5.1 double-translation FA chat design
    (Czech -> Russian query translation -> Russian Brain call -> Russian ->
    Czech answer translation) with direct-locale Brain answers: BGE-M3
    multilingual retrieval runs directly on the original-locale text, and
    the Brain is told ``response_language`` and answers in that language
    itself. This provider stands in for ``build_content_translation_provider``
    so any accidental ``translate()`` call made from the chat request/
    response path would be recorded and caught immediately by the
    ``.calls == []`` assertions below. The *other*, unrelated content-
    translation path (stored memory-content translations for contributor
    claims/clarifications/finalized text/corrections) is untouched by this
    task and is exercised by ``test_content_translation.py`` and
    ``test_bilingual_family_memory.py``, not here.
    """

    provider_name = "recording"

    def __init__(self):
        self.calls: list[tuple[str, str, str]] = []

    def translate(self, *, source_text, source_language, target_language):
        self.calls.append((source_text, source_language, target_language))
        from app.modules.content_translation.provider import ContentTranslationProviderResponse
        from app.modules.content_translation.schemas import ProviderTranslationResult

        return ContentTranslationProviderResponse(
            result=ProviderTranslationResult(translated_text=f"[{target_language}] {source_text}"),
            provider_name=self.provider_name,
            model="recording",
            latency_ms=1,
        )


def _patch_chat_runtime(monkeypatch, *, recorded_queries: list[str], recorded_requests: list):
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

    def fake_generate_chat_response(request):
        recorded_requests.append(request)
        # Stand-in "Brain": answers directly in whatever response_language
        # it was told, exactly the behavior prompt_builder's RESPONSE
        # LANGUAGE directive is meant to elicit from the real provider.
        answer = CZECH_ANSWER if request.response_language == "cs" else RUSSIAN_ANSWER
        return SimpleNamespace(
            text=answer,
            provider_name="mock-brain",
            metadata={
                "grounding_status": "grounded",
                "output_guard_applied": False,
                "output_guard_reason": None,
                "output_guard_lack_of_evidence": False,
            },
        )

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.get_agent_orchestrator",
        lambda: SimpleNamespace(generate_chat_response=fake_generate_chat_response),
    )


def test_czech_locale_direct_answer_no_translation_calls(client, monkeypatch):
    _user, profile = _create_demo_profile()
    recorded_queries: list[str] = []
    recorded_requests: list = []
    _patch_chat_runtime(monkeypatch, recorded_queries=recorded_queries, recorded_requests=recorded_requests)
    recording_provider = RecordingChatTranslationProvider()
    monkeypatch.setattr(
        "app.modules.content_translation.service.build_content_translation_provider",
        lambda *, provider_name=None, provider_settings=None: recording_provider,
    )

    response = client.post(
        "/api/demo/fa-chat/message",
        headers={"X-Request-ID": "cs-trace-1"},
        json={"message": CZECH_QUESTION, "locale": "cs"},
    )

    assert response.status_code == 200
    body = response.json()
    # The Brain answered directly in Czech - there is no answer-translation
    # call, so the response is exactly whatever the Brain returned.
    assert body["answer"] == CZECH_ANSWER
    assert body["locale"] == "cs"
    assert body["trace_id"] == "cs-trace-1"
    assert "[rag:" not in body["answer"]
    assert "[memory:" not in body["answer"]
    # Retrieval ran on the exact original Czech text - no query-translation
    # call; BGE-M3 multilingual retrieval is used directly on Czech.
    assert recorded_queries == [CZECH_QUESTION]
    # The Brain received the untranslated Czech user_message plus an
    # explicit response_language telling it to answer in Czech - this is
    # the only mechanism providing bilingual behavior now.
    assert len(recorded_requests) == 1
    assert recorded_requests[0].user_message == CZECH_QUESTION
    assert recorded_requests[0].response_language == "cs"
    # Hard acceptance criterion: zero translation-provider calls anywhere in
    # the chat request/response path for the Czech locale.
    assert recording_provider.calls == []


def test_russian_locale_direct_answer_unchanged(client, monkeypatch):
    _user, profile = _create_demo_profile()
    recorded_queries: list[str] = []
    recorded_requests: list = []
    _patch_chat_runtime(monkeypatch, recorded_queries=recorded_queries, recorded_requests=recorded_requests)
    recording_provider = RecordingChatTranslationProvider()
    monkeypatch.setattr(
        "app.modules.content_translation.service.build_content_translation_provider",
        lambda *, provider_name=None, provider_settings=None: recording_provider,
    )

    response = client.post(
        "/api/demo/fa-chat/message",
        headers={"X-Request-ID": "ru-trace-1"},
        json={"message": RUSSIAN_QUESTION},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["answer"] == RUSSIAN_ANSWER
    assert body["locale"] == "ru"
    assert recorded_queries == [RUSSIAN_QUESTION]
    assert len(recorded_requests) == 1
    assert recorded_requests[0].user_message == RUSSIAN_QUESTION
    assert recorded_requests[0].response_language == "ru"
    # Hard acceptance criterion: zero translation-provider calls for the
    # Russian locale (default) turn - unchanged from before this task.
    assert recording_provider.calls == []


def test_only_one_brain_call_per_chat_turn_for_either_locale(client, monkeypatch):
    """Hard acceptance criterion: exactly 1 Brain call, 0 translation calls,
    for both locales - no separate query-translation or answer-translation
    call is ever issued."""
    _user, profile = _create_demo_profile()
    recorded_requests: list = []
    _patch_chat_runtime(monkeypatch, recorded_queries=[], recorded_requests=recorded_requests)
    recording_provider = RecordingChatTranslationProvider()
    monkeypatch.setattr(
        "app.modules.content_translation.service.build_content_translation_provider",
        lambda *, provider_name=None, provider_settings=None: recording_provider,
    )

    for message, locale in ((CZECH_QUESTION, "cs"), (RUSSIAN_QUESTION, "ru")):
        response = client.post(
            "/api/demo/fa-chat/message",
            json={"message": message, "locale": locale},
        )
        assert response.status_code == 200

    assert len(recorded_requests) == 2
    assert recording_provider.calls == []
