"""Bilingual (Czech/Russian) retrieval + direct-locale Brain evaluation.

Task 64.5.2 replaced the double-translation FA chat design (Task 64.5.1,
Part E.22-23) with a direct-locale architecture: BGE-M3 multilingual
retrieval runs directly on the original text the user typed (no query
translation), and the Brain is told an explicit ``response_language`` and
answers in that language itself (no answer translation). This module
exercises that architecture, once in Czech and once with an equivalent
Russian control question, across five question categories, through the
real ``run_demo_fa_chat_message`` service function with a scripted
(non-LLM) retrieval + Brain double so the outcome is deterministic and
fast. It is not exhaustive (see PROJECT_PROGRESS.md's Known Limitations
for this task) but directly demonstrates, for every category and both
locales:

- Retrieval receives the ORIGINAL, untranslated locale text - no
  query-translation call.
- The Brain receives ``response_language`` matching the active locale and
  the original (untranslated) ``user_message`` - no answer-translation call.
- Zero translation-provider calls anywhere in the chat request/response path.

It also records (not fixes) the documented Russian-keyword-heuristic
limitation: a Czech corrected-memory question is not detected as
corrected-memory intent by ``classify_memory_query_intent`` (it falls back
to an ordinary direct factual question, so no expanded two-query retrieval
probe is issued), while the Russian-equivalent phrasing correctly triggers
the ``CORRECTED_MEMORY_FACT`` expansion path.
"""

from __future__ import annotations

from dataclasses import dataclass
from types import SimpleNamespace

import pytest

from app.main import app
from app.modules.auth.schemas import RegisterRequest
from app.modules.auth.service import register_user
from app.modules.avatar_persona import build_expanded_retrieval_query, classify_memory_query_intent
from app.modules.avatar_persona.memory_query_intent import MemoryQueryIntent
from app.modules.memory_profiles.schemas import MemoryProfileCreate
from app.modules.memory_profiles.service import create_memory_profile
from app.modules.rag_evaluation.brain_eval_e2e_bootstrap import (
    FAMILY_AVATAR_RU_E2E_EMAIL,
    FAMILY_AVATAR_RU_E2E_PASSWORD,
    FAMILY_AVATAR_RU_E2E_PROFILE_NAME,
)
from app.modules.rag_retrieval.schemas import RagRetrievalResponseRead, RagRetrievalResultRead


def _create_demo_profile():
    db = app.state.testing_session_local()
    try:
        user = register_user(
            db,
            RegisterRequest(
                email=FAMILY_AVATAR_RU_E2E_EMAIL,
                password=FAMILY_AVATAR_RU_E2E_PASSWORD,
                full_name="FA Demo Bilingual Eval User",
            ),
        )
        profile = create_memory_profile(
            db,
            current_user=user,
            payload=MemoryProfileCreate(
                name=FAMILY_AVATAR_RU_E2E_PROFILE_NAME,
                biography="Test profile for bilingual retrieval evaluation.",
                personality="Warm and factual.",
            ),
        )
        return user, profile
    finally:
        db.close()


def _grounded_result(chunk_id: int, text: str) -> RagRetrievalResultRead:
    return RagRetrievalResultRead(
        chunk_id=chunk_id,
        source_id=7,
        source_title="Family Novak RU E2E Corpus",
        embedding_id=chunk_id + 10000,
        score=0.95,
        text=text,
        chunk_index=0,
        language="ru",
        source_type="manual_text",
        validation_status="valid",
        text_hash=f"hash-{chunk_id}",
        qdrant_collection="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
        payload_metadata={},
    )


@dataclass(frozen=True)
class Scenario:
    key: str
    locale: str
    message: str
    retrieval_results: tuple
    brain_answer: str


SCENARIOS = (
    Scenario(
        key="direct_factual",
        locale="cs",
        message="Kde jsi žila v dětství?",
        retrieval_results=(_grounded_result(1, "В детстве Ева жила с родителями у Попице."),),
        brain_answer="V dětství jsem žila s rodiči u Popice.",
    ),
    Scenario(
        key="direct_factual",
        locale="ru",
        message="Где ты жила в детстве?",
        retrieval_results=(_grounded_result(1, "В детстве Ева жила с родителями у Попице."),),
        brain_answer="В детстве я жила с родителями у Попице.",
    ),
    Scenario(
        key="corrected_memory",
        locale="cs",
        message="Jak to bylo doopravdy s tou písničkou před spaním?",
        retrieval_results=(_grounded_result(2, "Бабушка пела 'Спят усталые игрушки' перед сном."),),
        brain_answer="Doopravdy jsem ti zpívala „Spí unavené hračky“.",
    ),
    Scenario(
        key="corrected_memory",
        locale="ru",
        message="Что было на самом деле с той колыбельной?",
        retrieval_results=(_grounded_result(2, "Бабушка пела 'Спят усталые игрушки' перед сном."),),
        brain_answer="На самом деле я пела «Спят усталые игрушки».",
    ),
    Scenario(
        key="lack_of_evidence",
        locale="cs",
        message="Jaké boty jsi nosila na svatbě?",
        retrieval_results=(),
        brain_answer="Na to bohužel nemám vzpomínku.",
    ),
    Scenario(
        key="lack_of_evidence",
        locale="ru",
        message="Какую обувь ты носила на свадьбе?",
        retrieval_results=(),
        brain_answer="К сожалению, я этого не помню.",
    ),
    Scenario(
        key="multiple_perspective",
        locale="cs",
        message="Každý si tu historku pamatuje jinak, co na to říkáš?",
        retrieval_results=(
            _grounded_result(3, "Мама помнит одно, тётя помнит другое: 'версия А' против 'версия Б'."),
        ),
        brain_answer="Každý si to pamatuje trochu jinak, přesný detail už nevím jistě.",
    ),
    Scenario(
        key="multiple_perspective",
        locale="ru",
        message="Каждый по-своему помнит эту историю, что ты скажешь?",
        retrieval_results=(
            _grounded_result(3, "Мама помнит одно, тётя помнит другое: 'версия А' против 'версия Б'."),
        ),
        brain_answer="Каждый помнит немного по-своему, точная деталь мне не до конца ясна.",
    ),
    Scenario(
        key="emotional",
        locale="cs",
        message="Jak se cítíš, když vzpomínáš na dětství?",
        retrieval_results=(_grounded_result(4, "Ева вспоминала детство с теплом и грустью."),),
        brain_answer="Vzpomínám na to s teplem a trochou smutku.",
    ),
    Scenario(
        key="emotional",
        locale="ru",
        message="Что ты чувствуешь, вспоминая детство?",
        retrieval_results=(_grounded_result(4, "Ева вспоминала детство с теплом и грустью."),),
        brain_answer="Вспоминаю об этом с теплом и лёгкой грустью.",
    ),
)


class RecordingChatTranslationProvider:
    """Records every translate() call so a test can assert there were none."""

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


@pytest.mark.parametrize("scenario", SCENARIOS, ids=[f"{s.key}__{s.locale}" for s in SCENARIOS])
def test_bilingual_retrieval_and_direct_locale_brain_answer(client, monkeypatch, scenario):
    _create_demo_profile()

    recorded_queries: list[str] = []
    recorded_requests: list = []

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service._resolve_demo_runtime",
        # Task 65.3 stale-fixture fix: the real `_resolve_demo_runtime` has
        # taken a `locale: str = "ru"` keyword argument since Task 64.5.2
        # (`demo_fa_chat/service.py` calls it with `locale=locale` at its
        # real call site), but this fixture was never updated to accept it,
        # so every parametrized case in this module failed with
        # `TypeError: <lambda>() got an unexpected keyword argument 'locale'`
        # before the actual retrieval/Brain assertions ever ran - a stale
        # test double, not a retrieval regression. `locale` is accepted and
        # ignored here since this fixture's returned runtime is identical
        # for every locale in this test's scenarios.
        lambda db, *, resolved_profile, locale="ru": SimpleNamespace(
            collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
            retrieval_mode="bge_m3_dense_sparse",
            top_k=5,
            source_id=7,
            point_count=20,
        ),
    )

    def fake_retrieve(db, *, current_user, profile_id, payload):
        recorded_queries.append(payload.query)
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code="bge_m3_dense_sparse",
            results=list(scenario.retrieval_results),
        )

    monkeypatch.setattr("app.modules.demo_fa_chat.service.retrieve_profile_rag", fake_retrieve)

    def fake_generate_chat_response(request):
        recorded_requests.append(request)
        return SimpleNamespace(
            text=scenario.brain_answer,
            provider_name="mock-brain",
            metadata={
                "grounding_status": "grounded" if scenario.retrieval_results else "no_evidence",
                "output_guard_applied": False,
                "output_guard_reason": None,
                "output_guard_lack_of_evidence": not bool(scenario.retrieval_results),
            },
        )

    monkeypatch.setattr(
        "app.modules.demo_fa_chat.service.get_agent_orchestrator",
        lambda: SimpleNamespace(generate_chat_response=fake_generate_chat_response),
    )

    recording_provider = RecordingChatTranslationProvider()
    monkeypatch.setattr(
        "app.modules.content_translation.service.build_content_translation_provider",
        lambda *, provider_name=None, provider_settings=None: recording_provider,
    )

    response = client.post(
        "/api/demo/fa-chat/message",
        json={"message": scenario.message, "locale": scenario.locale},
    )

    assert response.status_code == 200
    body = response.json()

    # Hard acceptance criteria, verified for every category/locale combination:
    assert body["answer"] == scenario.brain_answer
    assert body["locale"] == scenario.locale
    # No query-translation call, ever - the primary retrieval query is always
    # the exact original-locale text. (A corrected-memory-intent turn may
    # issue one *additional* same-language expansion-query retrieval probe
    # derived from that same text, unrelated to translation - see
    # build_expanded_retrieval_query - which is why >1 query can appear here.)
    assert recorded_queries[0] == scenario.message
    assert len(recorded_requests) == 1  # exactly one Brain call
    assert recorded_requests[0].user_message == scenario.message  # Brain sees the original text
    assert recorded_requests[0].response_language == scenario.locale
    assert recording_provider.calls == []  # zero translation-provider calls

    if scenario.key == "lack_of_evidence":
        assert body["lack_of_evidence"] is True


def test_known_limitation_czech_corrected_memory_intent_not_detected():
    """Documents (does not fix) the accepted v1 tradeoff described in
    PROJECT_PROGRESS.md's Known Limitations for this task: intent-
    classification keyword heuristics are Russian-tuned and, after Task
    64.5.2 removed the query-translation indirection, are now evaluated
    directly against whatever raw locale text the user typed. A Czech
    corrected-memory question is misclassified as an ordinary direct
    factual question - no expanded two-query retrieval probe is issued -
    while the Russian-equivalent phrasing correctly triggers the
    CORRECTED_MEMORY_FACT expansion path."""
    czech_question = "Jak to bylo doopravdy s tou písničkou před spaním?"
    russian_question = "Что было на самом деле с той колыбельной?"

    czech_intent = classify_memory_query_intent(czech_question)
    russian_intent = classify_memory_query_intent(russian_question)

    assert czech_intent == MemoryQueryIntent.DIRECT_FACTUAL_MEMORY
    assert build_expanded_retrieval_query(czech_question, czech_intent) is None

    assert russian_intent == MemoryQueryIntent.CORRECTED_MEMORY_FACT
    assert build_expanded_retrieval_query(russian_question, russian_intent) is not None
