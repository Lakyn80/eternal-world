import pytest

from app.core.config import Settings, settings
from app.db.models import RagEmbedding
from app.db.session import get_db
from app.core.logging import REDACTED_VALUE, sanitize_log_data
from app.main import app
from app.modules.ai_agents.brain.context import (
    CORRECTED_MEMORY_EVIDENCE_CAP,
    MAX_MEMORY_EVIDENCE_ITEMS,
    is_verified_evidence_result,
    prioritize_corrected_memory_evidence,
)
from app.modules.ai_agents.brain.output_guard import (
    BrainOutputGuardContext,
    apply_brain_output_guard,
    strip_internal_evidence_citations,
)
from app.modules.ai_agents.brain.prompt_builder import build_brain_prompt_messages
from app.modules.ai_agents.brain.provider import (
    BrainProviderConfigurationError,
    MockBrainAgentProvider,
    build_brain_provider,
)
from app.modules.ai_agents.orchestrator import AgentOrchestrator, get_agent_orchestrator
from app.modules.ai_agents.brain.service import BrainAgentService
from app.modules.ai_agents.schemas import (
    BrainAgentRequest,
    BrainAgentResponse,
    MemoryProfileContext,
    OrchestratorChatRequest,
)
from app.modules.avatar_persona import load_demo_avatar_persona
from app.modules.rag_retrieval.schemas import RagRetrievalResponseRead, RagRetrievalResultRead


@pytest.fixture(autouse=True)
def clear_orchestrator_cache():
    get_agent_orchestrator.cache_clear()
    yield
    get_agent_orchestrator.cache_clear()


def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "AI Test User",
        },
    )
    login_response = client.post(
        "/api/auth/login",
        json={"email": email, "password": password},
    )
    return login_response.json()["access_token"]


def _create_profile(client, token: str, name: str = "AI Profile") -> int:
    response = client.post(
        "/api/memory-profiles",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": name},
    )
    return response.json()["id"]


def _create_memory(
    client,
    token: str,
    profile_id: int,
    *,
    title: str,
    content: str | None = None,
    memory_type: str = "text",
    occurred_at: str | None = None,
    occurred_year: int | None = None,
):
    payload = {
        "title": title,
        "content": content,
        "memory_type": memory_type,
    }
    if occurred_at is not None:
        payload["occurred_at"] = occurred_at
    if occurred_year is not None:
        payload["occurred_year"] = occurred_year

    response = client.post(
        f"/api/memory-profiles/{profile_id}/memories",
        headers={"Authorization": f"Bearer {token}"},
        json=payload,
    )
    return response


def _capture_prompt(monkeypatch):
    captured: dict[str, str] = {}
    monkeypatch.setattr(settings, "ai_brain_provider", "mock")
    get_agent_orchestrator.cache_clear()

    def capture_generate_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
        captured["prompt"] = request.prompt
        return BrainAgentResponse(
            text=(
                f"{request.profile.name} mock reply: I heard '{request.user_message}'. "
                f"Recent messages considered: {len(request.recent_history)}."
            ),
            provider_name="mock",
            metadata={
                "agent": "brain",
                "history_count": len(request.recent_history),
            },
        )

    monkeypatch.setattr(MockBrainAgentProvider, "generate_response", capture_generate_response)
    return captured


class CitationStubProvider:
    def generate_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
        return BrainAgentResponse(
            text="Деточка, я жила у Попице. [rag:27618]",
            provider_name="citation-stub",
            metadata={"grounding_status": "grounded"},
        )


def _get_test_db_session():
    override = app.dependency_overrides[get_db]
    session_generator = override()
    db = next(session_generator)
    return db, session_generator


def test_default_brain_provider_is_mock(monkeypatch):
    # Task 65.3 stabilization: `_env_file=None` only disables reading from a
    # `.env` FILE - it does not stop pydantic-settings from reading real OS
    # process environment variables. This dev container legitimately runs
    # with `AI_BRAIN_PROVIDER=openai_compatible` set as a real environment
    # variable (for live smoke tests elsewhere), which silently overrode the
    # field default here and made this test fail in this environment only.
    # Explicitly clearing the relevant vars proves the code's actual default
    # rather than whatever happens to be configured on the host running the
    # test.
    for env_var in ("AI_BRAIN_PROVIDER", "AI_BRAIN_MODEL", "AI_BRAIN_API_KEY", "AI_BRAIN_BASE_URL"):
        monkeypatch.delenv(env_var, raising=False)
    default_settings = Settings(_env_file=None)

    provider = build_brain_provider(provider_settings=default_settings)

    assert default_settings.ai_brain_provider == "mock"
    assert isinstance(provider, MockBrainAgentProvider)


def test_brain_agent_mock_provider_is_deterministic():
    provider = MockBrainAgentProvider()
    request = BrainAgentRequest(
        profile=MemoryProfileContext(id=1, name="Ada"),
        user_message="Hello",
        recent_history=[],
        system_prompt="System prompt",
        user_prompt="User prompt",
        prompt="System prompt\n\n---\n\nUser prompt",
    )

    first_response = provider.generate_response(request)
    second_response = provider.generate_response(request)

    assert first_response.text == second_response.text
    assert first_response.provider_name == second_response.provider_name


def test_provider_factory_selects_mock():
    provider = build_brain_provider(
        provider_name="mock",
        provider_settings=Settings(_env_file=None),
    )

    assert isinstance(provider, MockBrainAgentProvider)


def test_provider_factory_rejects_unknown_provider():
    with pytest.raises(BrainProviderConfigurationError) as exc_info:
        build_brain_provider(
            provider_name="unknown-provider",
            provider_settings=Settings(_env_file=None),
        )

    assert "Unsupported AI_BRAIN_PROVIDER" in str(exc_info.value)


def test_openai_compatible_provider_requires_api_key_when_selected(monkeypatch):
    # Task 65.3 stabilization: this container has a real `AI_BRAIN_API_KEY`
    # set as an OS environment variable; since only `ai_brain_provider`/
    # `ai_brain_model` were overridden explicitly, the api key field fell
    # through to that real value and the expected error never raised.
    monkeypatch.delenv("AI_BRAIN_API_KEY", raising=False)
    selected_settings = Settings(
        _env_file=None,
        ai_brain_provider="openai_compatible",
        ai_brain_model="test-model",
    )

    with pytest.raises(BrainProviderConfigurationError) as exc_info:
        build_brain_provider(provider_settings=selected_settings)

    assert "AI_BRAIN_API_KEY is required" in str(exc_info.value)


def test_openai_compatible_provider_does_not_run_in_normal_tests_unless_explicitly_mocked(
    client,
    monkeypatch,
):
    from app.modules.ai_agents.brain.providers import openai_compatible

    def fail_http_client(*args, **kwargs):
        raise AssertionError("OpenAI-compatible HTTP client should not be created for mock tests")

    monkeypatch.setattr(settings, "ai_brain_provider", "mock")
    monkeypatch.setattr(openai_compatible.httpx, "Client", fail_http_client)
    get_agent_orchestrator.cache_clear()

    token = _register_and_login(client, "ai-mock-chat@example.com")
    profile_id = _create_profile(client, token, name="AI Mock Profile")
    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Hello provider"},
    )

    assert response.status_code == 200
    assert response.json()["ai_response_text"] == (
        "AI Mock Profile mock reply: I heard 'Hello provider'. "
        "Recent messages considered: 0."
    )


def test_sensitive_ai_config_values_are_not_exposed_in_logs_or_api_responses(
    client,
    monkeypatch,
):
    sanitized = sanitize_log_data(
        {
            "ai_brain_api_key": "super-secret-key",
            "ai_brain_provider": "openai_compatible",
        }
    )
    assert sanitized["ai_brain_api_key"] == REDACTED_VALUE
    assert sanitized["ai_brain_provider"] == "openai_compatible"

    monkeypatch.setattr(settings, "ai_brain_provider", "openai_compatible")
    monkeypatch.setattr(settings, "ai_brain_model", "test-model")
    monkeypatch.setattr(settings, "ai_brain_api_key", None)
    get_agent_orchestrator.cache_clear()

    token = _register_and_login(client, "ai-safe-error@example.com")
    profile_id = _create_profile(client, token, name="AI Safe Error Profile")
    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Trigger provider config"},
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "Internal server error"
    assert "AI_BRAIN_API_KEY" not in response.text
    assert "super-secret-key" not in response.text


def test_agent_orchestrator_calls_brain_only_for_current_slice():
    class StubBrainService:
        def __init__(self) -> None:
            self.called = False

        def generate_chat_response(self, request):
            self.called = True
            return BrainAgentResponse(
                text="brain-only-response",
                provider_name="stub-brain",
            )

    class FailVoiceService:
        def generate_audio(self, text: str) -> str:
            raise AssertionError("Voice agent should not be called")

    class FailFaceService:
        def generate_video(self, text: str, audio_url: str | None = None) -> str:
            raise AssertionError("Face agent should not be called")

    class FailDirectorService:
        def prepare_scene(self) -> None:
            raise AssertionError("Director agent should not be called")

    brain_service = StubBrainService()
    orchestrator = AgentOrchestrator(
        brain_service=brain_service,
        voice_service=FailVoiceService(),
        face_service=FailFaceService(),
        director_service=FailDirectorService(),
    )

    response = orchestrator.generate_chat_response(
        OrchestratorChatRequest(
            profile=MemoryProfileContext(id=1, name="Ada"),
            user_message="Hello",
            recent_history=[],
        )
    )

    assert brain_service.called is True
    assert response.text == "brain-only-response"
    assert response.audio_url is None
    assert response.video_url is None


def test_chat_response_generation_still_works_with_no_memories(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    token = _register_and_login(client, "ai-no-memories@example.com")
    profile_id = _create_profile(client, token, name="No Memory Profile")

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Hello there"},
    )

    assert response.status_code == 200
    assert response.json()["ai_response_text"] == (
        "No Memory Profile mock reply: I heard 'Hello there'. "
        "Recent messages considered: 0."
    )
    assert "- None available." in captured["prompt"]


def test_generated_brain_prompt_includes_profile_context(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    token = _register_and_login(client, "ai-profile-context@example.com")
    profile_id = _create_profile(client, token, name="Grounded Ada")
    client.patch(
        f"/api/memory-profiles/{profile_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "biography": "Pioneer of analytical engines",
            "personality": "Warm and curious",
            "catchphrases": "Let's think carefully",
        },
    )

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Tell me about yourself"},
    )

    assert response.status_code == 200
    prompt = captured["prompt"]
    assert "SYSTEM — Eternal World Brain Agent (Production v2)" in prompt
    assert "- Name: Grounded Ada" in prompt
    assert "- Biography summary: Pioneer of analytical engines" in prompt
    assert "- Personality style: Warm and curious" in prompt
    assert "- Catchphrases style: Let's think carefully" in prompt


def test_generated_brain_prompt_includes_selected_memory_evidence_when_memories_exist(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    token = _register_and_login(client, "ai-memory-evidence@example.com")
    profile_id = _create_profile(client, token, name="Evidence Profile")
    create_response = _create_memory(
        client,
        token,
        profile_id,
        title="Paris Trip",
        content="We visited Paris in the spring and walked near the Seine.",
        occurred_year=2015,
    )
    assert create_response.status_code == 201

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Do you remember Paris?"},
    )

    assert response.status_code == 200
    prompt = captured["prompt"]
    assert "B1. Timeline memory evidence:" in prompt
    assert "[memory:" in prompt
    assert "Paris Trip" in prompt
    assert "visited Paris in the spring" in prompt


def test_factual_grounding_instructions_are_present_in_prompt(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    token = _register_and_login(client, "ai-grounding-rules@example.com")
    profile_id = _create_profile(client, token)

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "What happened in my life?"},
    )

    assert response.status_code == 200
    prompt = captured["prompt"]
    assert "EVIDENCE HIERARCHY (strict)" in prompt
    assert "Answer factual questions ONLY from B1, B2, and explicit profile fields above." in prompt
    assert "Do not guess, fill gaps, or use world knowledge to invent personal history." in prompt
    assert "the information is not available in the stored memories/context." in prompt
    assert "correcting the premise with a related denial or substitute fact." in prompt
    assert "\"I never lived in Paris.\", \"I had no sister.\", \"Pavel was never in Vietnam.\"" in prompt
    assert "answer ONLY with lack-of-evidence wording and stop after" in prompt
    assert "Do not add a contrasting true fact, corrective denial, or extra archival detail" in prompt
    assert "Na to bohužel nemám vzpomínku." in prompt
    assert "cite inline: [memory:id] or [rag:chunk_id]" in prompt
    assert "Respond in the same language as the user's current message" in prompt
    assert "B1. Timeline memory evidence:" in prompt
    assert "check EVERY item in B1 and B2 individually, not only" in prompt
    assert "even when other provided" in prompt
    assert "evidence items are about unrelated facts or state that different things did not happen." in prompt
    assert "does not state the exact specific" in prompt
    assert "do not restate the general event as a partial or consolation answer either." in prompt
    assert "without repeating the surrounding general facts from that evidence item." in prompt


def test_brain_prompt_separates_memory_and_rag_evidence_sections(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    token = _register_and_login(client, "ai-evidence-sections@example.com")
    profile_id = _create_profile(client, token, name="Section Profile")
    assert _create_memory(
        client,
        token,
        profile_id,
        title="Family Dinner",
        content="We shared soup at the old station in Brno.",
        occurred_year=1990,
    ).status_code == 201

    def fake_retrieval_response(db, *, current_user, profile_id, payload):
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code="bge_m3_dense_sparse",
            results=[
                RagRetrievalResultRead(
                    chunk_id=88,
                    source_id=44,
                    embedding_id=22,
                    score=0.95,
                    text="The archival note confirms the station dinner tradition in Brno.",
                    chunk_index=0,
                    language="en",
                    source_type="document_text",
                    validation_status="valid",
                    text_hash="hash-88",
                    qdrant_collection="eternal_world_rag_chunks__bge_m3_dense_sparse",
                    payload_metadata={},
                )
            ],
        )

    monkeypatch.setattr("app.modules.chat.service.retrieve_profile_rag", fake_retrieval_response)

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Tell me about Brno"},
    )

    assert response.status_code == 200
    prompt = captured["prompt"]
    assert "B1. Timeline memory evidence:" in prompt
    assert "B2. Retrieved archival RAG evidence:" in prompt
    assert "[memory:" in prompt
    assert "[rag:88]" in prompt
    assert prompt.index("B1.") < prompt.index("B2.")


def test_rag_evidence_preview_uses_longer_excerpt_limit(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    token = _register_and_login(client, "ai-rag-excerpt@example.com")
    profile_id = _create_profile(client, token, name="RAG Excerpt Profile")
    long_rag_text = "A" * 400 + " unique-marker-tail"

    def fake_retrieval_response(db, *, current_user, profile_id, payload):
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code="bge_m3_dense_sparse",
            results=[
                RagRetrievalResultRead(
                    chunk_id=99,
                    source_id=55,
                    embedding_id=33,
                    score=0.91,
                    text=long_rag_text,
                    chunk_index=0,
                    language="en",
                    source_type="document_text",
                    validation_status="valid",
                    text_hash="hash-99",
                    qdrant_collection="eternal_world_rag_chunks__bge_m3_dense_sparse",
                    payload_metadata={},
                )
            ],
        )

    monkeypatch.setattr("app.modules.chat.service.retrieve_profile_rag", fake_retrieval_response)

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Tell me about the archive"},
    )

    assert response.status_code == 200
    prompt = captured["prompt"]
    assert "unique-marker-tail" in prompt
    assert "Excerpt:" in prompt


def _rag_result(
    *,
    chunk_id: int,
    score: float,
    source_type: str = "document_text",
    memory_status: str | None = None,
    text_hash: str | None = None,
    candidate_id: int | None = None,
    promotion_id: int | None = None,
    text: str = "text",
) -> RagRetrievalResultRead:
    payload_metadata: dict = {}
    if memory_status:
        payload_metadata["memory_status"] = memory_status
    if candidate_id is not None:
        payload_metadata["candidate_id"] = candidate_id
    if promotion_id is not None:
        payload_metadata["promotion_id"] = promotion_id
    return RagRetrievalResultRead(
        chunk_id=chunk_id,
        source_id=chunk_id,
        embedding_id=chunk_id,
        score=score,
        text=text,
        chunk_index=0,
        language="ru",
        source_type=source_type,
        validation_status="valid",
        text_hash=text_hash or f"hash-{chunk_id}",
        qdrant_collection="eternal_world_rag_chunks__bge_m3_dense_sparse",
        payload_metadata=payload_metadata,
    )


# --- Task 65.10: cross-pipeline verified evidence prioritization ------------
#
# Replaces the old "conversation_candidate always floats to front"
# unconditional-partition tests below with a bounded, pipeline-neutral
# contract: verification (recognized from ANY of VERIFIED_EVIDENCE_SOURCE_
# TYPES - conversation_candidate, manual_text, biography) adds a small,
# bounded relevance boost (VERIFIED_EVIDENCE_RELEVANCE_BOOST); it never
# unconditionally overrides a significantly higher-relevance item from any
# pipeline. See `app.modules.ai_agents.brain.context.
# prioritize_corrected_memory_evidence` for the full rationale.


def test_prioritize_corrected_memory_evidence_caps_at_configured_limit():
    results = [
        _rag_result(chunk_id=i, score=1.0 - i * 0.1, source_type="manual_text") for i in range(6)
    ]

    prioritized = prioritize_corrected_memory_evidence(results)

    assert len(prioritized) == CORRECTED_MEMORY_EVIDENCE_CAP


def test_prioritize_corrected_memory_evidence_is_a_noop_without_verified_items():
    results = [
        _rag_result(chunk_id=1, score=1.0, source_type="manual_text"),
        _rag_result(chunk_id=2, score=0.9, source_type="manual_text"),
    ]

    prioritized = prioritize_corrected_memory_evidence(results, limit=5)

    assert [item.chunk_id for item in prioritized] == [1, 2]


def test_prioritize_corrected_memory_evidence_gives_verified_item_bounded_boost():
    """A verified item gets a small boost that can break a close relevance
    gap (Part E #4: "may receive a bounded verification benefit") without
    ever becoming an unconditional front-of-queue rule."""
    results = [
        _rag_result(chunk_id=1, score=0.50, source_type="document_text"),
        _rag_result(chunk_id=2, score=0.40, source_type="conversation_candidate", memory_status="verified"),
    ]

    prioritized = prioritize_corrected_memory_evidence(results, limit=2)

    # 0.40 + 0.15 boost = 0.55 > 0.50: the close gap is broken in favor of
    # the verified item.
    assert [item.chunk_id for item in prioritized] == [2, 1]


def test_prioritize_corrected_memory_evidence_does_not_let_low_relevance_verified_item_override_much_higher_relevance():
    """Task 65.10 Part G #4 / rule 9: source type (verification) alone must
    never override a significantly higher semantic relevance score from any
    pipeline. Directly covers required Part J test #4 ("stronger relevance
    beats weaker relevance across pipelines") and #17 ("no pipeline receives
    unconditional priority")."""
    results = [
        _rag_result(chunk_id=1, score=0.90, source_type="document_text"),
        _rag_result(chunk_id=2, score=0.30, source_type="conversation_candidate", memory_status="verified"),
    ]

    prioritized = prioritize_corrected_memory_evidence(results, limit=2)

    # 0.30 + 0.15 boost = 0.45, still far below 0.90 - relevance wins.
    assert [item.chunk_id for item in prioritized] == [1, 2]


def test_prioritize_corrected_memory_evidence_corrected_memory_intent_mode_still_floats_verified_group():
    """Task 65.10: `corrected_memory_intent=True` (the mode the caller must
    only request after classifying the turn as CORRECTED_MEMORY_FACT /
    CORRECTION_HISTORY via `classify_memory_query_intent`) preserves the
    empirically-tuned Task 64.4.2 behavior - a verified item still leads
    even against a much higher-scoring unrelated archival item - for this
    narrow, explicitly-detected question shape. This is intent-gated, not a
    pipeline special case: it is not the default behavior for ordinary
    questions (see the bounded-boost tests above)."""
    results = [
        _rag_result(chunk_id=1, score=0.97, source_type="document_text"),
        _rag_result(chunk_id=2, score=0.42, source_type="conversation_candidate", memory_status="verified"),
    ]

    prioritized = prioritize_corrected_memory_evidence(results, limit=2, corrected_memory_intent=True)

    assert [item.chunk_id for item in prioritized] == [2, 1]


def test_prioritize_corrected_memory_evidence_recognizes_all_audited_verified_pipelines():
    """Part J test #1/#2/#18: approved memorial contribution (manual_text),
    approved chat-learned memory (conversation_candidate), and approved
    biography evidence must all be recognized as verified and compete on
    relevance, none privileged over another merely by pipeline identity."""
    manual_text_item = _rag_result(chunk_id=1, score=0.60, source_type="manual_text", memory_status="verified")
    conversation_item = _rag_result(
        chunk_id=2, score=0.62, source_type="conversation_candidate", memory_status="verified"
    )
    biography_item = _rag_result(chunk_id=3, score=0.58, source_type="biography", memory_status="verified")

    assert is_verified_evidence_result(manual_text_item)
    assert is_verified_evidence_result(conversation_item)
    assert is_verified_evidence_result(biography_item)

    prioritized = prioritize_corrected_memory_evidence(
        [manual_text_item, conversation_item, biography_item], limit=3
    )

    # All three are equally verified (same boost) - plain relevance order
    # decides among them, exactly matching pipeline neutrality (Part E #5).
    assert [item.chunk_id for item in prioritized] == [2, 1, 3]


def test_prioritize_corrected_memory_evidence_birthday_regression():
    """Task 65.10 primary regression test (Part J).

    Reproduces the reported defect with synthetic evidence (not the user's
    real production memory, per Part J): a highly relevant approved
    memorial-contribution memory (~0.829, the reported "18. narozeniny
    brestek" birthday memory's real observed score) must survive the
    final context cap of 3 ahead of two less-relevant verified
    conversation-candidate items, and source pipeline alone must not decide
    the outcome.
    """
    less_relevant_verified_chat_a = _rag_result(
        chunk_id=101, score=0.42, source_type="conversation_candidate", memory_status="verified", candidate_id=195
    )
    less_relevant_verified_chat_b = _rag_result(
        chunk_id=102, score=0.36, source_type="conversation_candidate", memory_status="verified", candidate_id=192
    )
    another_relevant_eligible_memory = _rag_result(chunk_id=103, score=0.50, source_type="biography", memory_status="verified")
    another_eligible_memory = _rag_result(chunk_id=104, score=0.41, source_type="biography", memory_status="verified")
    birthday_memory = _rag_result(
        chunk_id=105,
        score=0.829,
        source_type="manual_text",
        memory_status="verified",
        promotion_id=2,
    )

    candidates = [
        less_relevant_verified_chat_a,
        less_relevant_verified_chat_b,
        another_relevant_eligible_memory,
        another_eligible_memory,
        birthday_memory,
    ]

    prioritized = prioritize_corrected_memory_evidence(candidates, limit=CORRECTED_MEMORY_EVIDENCE_CAP)
    selected_chunk_ids = [item.chunk_id for item in prioritized]

    assert len(prioritized) == 3
    assert 105 in selected_chunk_ids, "the highly relevant birthday memory must be included"
    assert selected_chunk_ids[0] == 105, "the highest-relevance item must rank first"
    # The least relevant items are dropped - pipeline identity alone does
    # not save them, and does not exclude the manual_text item either.
    assert 102 not in selected_chunk_ids


def test_prioritize_corrected_memory_evidence_deduplicates_same_canonical_memory():
    """Part E #6 / Part G #6 / Part J #14: near-duplicate evidence (the same
    canonical candidate/promotion surfacing as more than one chunk) must not
    consume more than one context slot."""
    duplicate_low = _rag_result(
        chunk_id=1, score=0.40, source_type="conversation_candidate", memory_status="verified", candidate_id=50
    )
    duplicate_high = _rag_result(
        chunk_id=2, score=0.55, source_type="conversation_candidate", memory_status="verified", candidate_id=50
    )
    distinct_item = _rag_result(chunk_id=3, score=0.45, source_type="manual_text", memory_status="verified")

    prioritized = prioritize_corrected_memory_evidence(
        [duplicate_low, duplicate_high, distinct_item], limit=3
    )

    selected_chunk_ids = [item.chunk_id for item in prioritized]
    assert 1 not in selected_chunk_ids, "the lower-scoring duplicate must be dropped"
    assert selected_chunk_ids.count(2) == 1
    assert 3 in selected_chunk_ids
    assert len(prioritized) == 2, "the duplicate pair must only consume one context slot"


def test_prioritize_corrected_memory_evidence_deduplicates_same_text_hash():
    duplicate_a = _rag_result(chunk_id=1, score=0.30, source_type="document_text", text_hash="shared-hash")
    duplicate_b = _rag_result(chunk_id=2, score=0.60, source_type="document_text", text_hash="shared-hash")

    prioritized = prioritize_corrected_memory_evidence([duplicate_a, duplicate_b], limit=5)

    assert [item.chunk_id for item in prioritized] == [2]


def test_prioritize_corrected_memory_evidence_is_deterministic_for_equal_scores():
    """Part J test #3/#7 in Part G: ordering must be stable for identical
    inputs - equal combined scores keep original relative order."""
    results = [
        _rag_result(chunk_id=1, score=0.5, source_type="document_text"),
        _rag_result(chunk_id=2, score=0.5, source_type="document_text"),
        _rag_result(chunk_id=3, score=0.5, source_type="document_text"),
    ]

    first_run = prioritize_corrected_memory_evidence(results, limit=3)
    second_run = prioritize_corrected_memory_evidence(results, limit=3)

    assert [item.chunk_id for item in first_run] == [1, 2, 3]
    assert [item.chunk_id for item in first_run] == [item.chunk_id for item in second_run]


def test_prioritize_corrected_memory_evidence_missing_metadata_fails_safely():
    """Part G #8: missing optional metadata must fail safely and must never
    make an item appear more trusted than it is."""
    no_payload_metadata = RagRetrievalResultRead(
        chunk_id=1,
        source_id=1,
        embedding_id=1,
        score=0.9,
        text="text",
        chunk_index=0,
        language=None,
        source_type="conversation_candidate",
        validation_status="valid",
        text_hash="hash-1",
        qdrant_collection="eternal_world_rag_chunks__bge_m3_dense_sparse",
        payload_metadata={},
    )
    unrecognized_source_type_but_marked_verified = _rag_result(
        chunk_id=2, score=0.1, source_type="other", memory_status="verified"
    )

    assert is_verified_evidence_result(no_payload_metadata) is False
    assert is_verified_evidence_result(unrecognized_source_type_but_marked_verified) is False

    prioritized = prioritize_corrected_memory_evidence(
        [no_payload_metadata, unrecognized_source_type_but_marked_verified], limit=2
    )
    # Neither item gets a verification boost - plain relevance order holds.
    assert [item.chunk_id for item in prioritized] == [1, 2]


def test_build_rag_evidence_items_populates_provenance_for_memorial_contribution():
    """Part C/D fix: an approved memorial contribution (manual_text) must
    get its memory_status/provenance/promotion_id populated into
    BrainRagEvidence exactly like a conversation-candidate item, not only
    conversation_candidate (this was the second half of the reported prompt-
    labeling defect, in `build_rag_evidence_items`)."""
    from app.modules.ai_agents.brain.context import build_rag_evidence_items

    manual_text_item = _rag_result(
        chunk_id=42,
        score=0.83,
        source_type="manual_text",
        memory_status="verified",
        promotion_id=2,
    )

    evidence_items = build_rag_evidence_items([manual_text_item])

    assert evidence_items[0].memory_status == "verified"
    assert evidence_items[0].promotion_id == 2


def test_verified_learned_memory_is_tagged_with_equal_authority_in_prompt(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    token = _register_and_login(client, "ai-learned-memory-tag@example.com")
    profile_id = _create_profile(client, token, name="Learned Memory Profile")

    def fake_retrieval_response(db, *, current_user, profile_id, payload):
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code="bge_m3_dense_sparse",
            results=[
                RagRetrievalResultRead(
                    chunk_id=201,
                    source_id=101,
                    embedding_id=301,
                    score=0.42,
                    text="По словам внука, бабушка пела ему песню перед сном.",
                    chunk_index=0,
                    language="ru",
                    source_type="conversation_candidate",
                    validation_status="valid",
                    text_hash="hash-201",
                    qdrant_collection="eternal_world_rag_chunks__bge_m3_dense_sparse",
                    payload_metadata={
                        "memory_status": "verified",
                        "provenance": "review_approved_conversation_candidate",
                        "promotion_id": 5,
                        "candidate_id": 14,
                        "indexed_at": "2026-07-11T21:51:58.863798+00:00",
                    },
                ),
                RagRetrievalResultRead(
                    chunk_id=202,
                    source_id=102,
                    embedding_id=302,
                    # Task 65.10: a moderate gap (not the old 0.97), so the
                    # bounded verification boost (0.15) genuinely breaks the
                    # tie in the verified item's favor (0.42+0.15=0.57>0.50)
                    # instead of relying on an unconditional priority rule.
                    # See test_prioritize_corrected_memory_evidence_does_not_
                    # let_low_relevance_verified_item_override_much_higher_
                    # relevance for the case where the gap is too large.
                    score=0.50,
                    text="Archival note about an unrelated household topic.",
                    chunk_index=0,
                    language="ru",
                    source_type="document_text",
                    validation_status="valid",
                    text_hash="hash-202",
                    qdrant_collection="eternal_world_rag_chunks__bge_m3_dense_sparse",
                    payload_metadata={},
                ),
            ],
        )

    monkeypatch.setattr("app.modules.chat.service.retrieve_profile_rag", fake_retrieval_response)

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Tell me about the song"},
    )

    assert response.status_code == 200
    prompt = captured["prompt"]
    assert "LEARNED MEMORY (learned_memory_answer_policy_v3_1)" in prompt
    assert "[rag:201] VERIFIED LEARNED MEMORY (owner-approved, first-person, equal authority to B1)" in prompt
    assert "promotion_id=5, candidate_id=14" in prompt
    assert "[rag:202] ARCHIVAL DOCUMENT" in prompt
    # A moderately higher retrieval score on the unrelated archival item must
    # not be the only signal in the prompt distinguishing the two evidence
    # kinds - the bounded verification boost still lets the verified item
    # lead when the gap is close.
    assert "VERIFIED LEARNED MEMORY" in prompt.split("[rag:202]")[0]


def test_archival_evidence_is_not_tagged_as_learned_memory(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    token = _register_and_login(client, "ai-archival-not-learned@example.com")
    profile_id = _create_profile(client, token, name="Archival Only Profile")

    def fake_retrieval_response(db, *, current_user, profile_id, payload):
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code="bge_m3_dense_sparse",
            results=[
                RagRetrievalResultRead(
                    chunk_id=301,
                    source_id=111,
                    embedding_id=401,
                    score=0.5,
                    text="Household chronicle entry from the archive.",
                    chunk_index=0,
                    language="ru",
                    source_type="document_text",
                    validation_status="valid",
                    text_hash="hash-301",
                    qdrant_collection="eternal_world_rag_chunks__bge_m3_dense_sparse",
                    payload_metadata={},
                )
            ],
        )

    monkeypatch.setattr("app.modules.chat.service.retrieve_profile_rag", fake_retrieval_response)

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Tell me about the archive"},
    )

    assert response.status_code == 200
    prompt = captured["prompt"]
    assert "[rag:301] ARCHIVAL DOCUMENT" in prompt
    assert "[rag:301] VERIFIED LEARNED MEMORY" not in prompt
    assert "Provenance: promotion_id=" not in prompt


def test_approved_memorial_contribution_survives_end_to_end_chat_prompt(client, monkeypatch):
    """Task 65.10 end-to-end regression (Part J test #20 / Part C #6):
    reproduces the reported defect shape through the real chat evidence path
    (`app.modules.chat.service._retrieve_rag_evidence_safely`, the same
    filter -> prioritize -> build_rag_evidence_items chain used in
    production) with synthetic evidence modeled on the real observed
    scores, and asserts the highly relevant approved memorial-contribution
    memory is both selected AND correctly tagged VERIFIED LEARNED MEMORY in
    the final prompt sent toward the provider - not silently dropped by the
    cap, and not mislabeled as an ordinary archival document."""
    captured = _capture_prompt(monkeypatch)
    token = _register_and_login(client, "ai-memorial-contribution-survives@example.com")
    profile_id = _create_profile(client, token, name="Memorial Contribution Profile")

    def fake_retrieval_response(db, *, current_user, profile_id, payload):
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code="bge_m3_dense_sparse",
            results=[
                RagRetrievalResultRead(
                    chunk_id=401,
                    source_id=201,
                    embedding_id=501,
                    score=0.829,
                    text="Oslavil jsem 18. narozeniny s rodinou u breste ku.",
                    chunk_index=0,
                    language="cs",
                    source_type="manual_text",
                    validation_status="valid",
                    text_hash="hash-401",
                    qdrant_collection="eternal_world_rag_chunks__bge_m3_dense_sparse",
                    payload_metadata={
                        "memory_status": "verified",
                        "provenance": "review_approved_memorial_contribution",
                        "promotion_id": 2,
                        "indexed_at": "2026-07-23T20:02:06.661536+00:00",
                    },
                ),
                RagRetrievalResultRead(
                    chunk_id=402,
                    source_id=202,
                    embedding_id=502,
                    score=0.42,
                    text="По словам внука, бабушка вспоминала о своём детстве.",
                    chunk_index=0,
                    language="ru",
                    source_type="conversation_candidate",
                    validation_status="valid",
                    text_hash="hash-402",
                    qdrant_collection="eternal_world_rag_chunks__bge_m3_dense_sparse",
                    payload_metadata={
                        "memory_status": "verified",
                        "provenance": "review_approved_conversation_candidate",
                        "promotion_id": 15,
                        "candidate_id": 195,
                        "indexed_at": "2026-07-24T15:12:19.920244+00:00",
                    },
                ),
                RagRetrievalResultRead(
                    chunk_id=403,
                    source_id=203,
                    embedding_id=503,
                    score=0.36,
                    text="По словам внука, бабушка вспоминала о бабушке.",
                    chunk_index=0,
                    language="ru",
                    source_type="conversation_candidate",
                    validation_status="valid",
                    text_hash="hash-403",
                    qdrant_collection="eternal_world_rag_chunks__bge_m3_dense_sparse",
                    payload_metadata={
                        "memory_status": "verified",
                        "provenance": "review_approved_conversation_candidate",
                        "promotion_id": 13,
                        "candidate_id": 192,
                        "indexed_at": "2026-07-23T15:39:32.713568+00:00",
                    },
                ),
            ],
        )

    monkeypatch.setattr("app.modules.chat.service.retrieve_profile_rag", fake_retrieval_response)

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "jak jsi slavil 18. narozeniny?"},
    )

    assert response.status_code == 200
    prompt = captured["prompt"]
    assert "[rag:401] VERIFIED LEARNED MEMORY (owner-approved, first-person, equal authority to B1)" in prompt
    assert "promotion_id=2" in prompt
    # It must lead the evidence block, not merely be present anywhere in it.
    assert prompt.index("[rag:401]") < prompt.index("[rag:402]")


def test_only_selected_profiles_memories_are_included(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    monkeypatch.setattr(
        "app.modules.billing.service.get_effective_plan_code_for_user",
        lambda current_user: "basic",
    )
    token = _register_and_login(client, "ai-selected-profile@example.com")
    selected_profile_id = _create_profile(client, token, name="Selected Profile")
    other_profile_id = _create_profile(client, token, name="Other Profile")
    assert _create_memory(
        client,
        token,
        selected_profile_id,
        title="Selected Memory",
        content="This belongs to the selected profile.",
    ).status_code == 201
    assert _create_memory(
        client,
        token,
        other_profile_id,
        title="Other Memory",
        content="This belongs to another profile.",
    ).status_code == 201

    response = client.post(
        f"/api/chat/{selected_profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Tell me about this profile"},
    )

    assert response.status_code == 200
    prompt = captured["prompt"]
    assert "Selected Memory" in prompt
    assert "Other Memory" not in prompt


def test_another_users_memories_are_not_included(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    owner_token = _register_and_login(client, "ai-owner-memories@example.com")
    other_token = _register_and_login(client, "ai-other-memories@example.com")
    owner_profile_id = _create_profile(client, owner_token, name="Owner Profile")
    other_profile_id = _create_profile(client, other_token, name="Other User Profile")
    assert _create_memory(
        client,
        owner_token,
        owner_profile_id,
        title="Owner Memory",
        content="Owner evidence about the family house.",
    ).status_code == 201
    assert _create_memory(
        client,
        other_token,
        other_profile_id,
        title="Other User Memory",
        content="Other user evidence should stay private.",
    ).status_code == 201

    response = client.post(
        f"/api/chat/{owner_profile_id}/messages",
        headers={"Authorization": f"Bearer {owner_token}"},
        json={"message": "What do you know about the house?"},
    )

    assert response.status_code == 200
    prompt = captured["prompt"]
    assert "Owner Memory" in prompt
    assert "Other User Memory" not in prompt


def test_memory_evidence_count_is_capped_at_10(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    monkeypatch.setattr(
        "app.modules.billing.service.get_effective_plan_code_for_user",
        lambda current_user: "basic",
    )
    token = _register_and_login(client, "ai-memory-cap@example.com")
    profile_id = _create_profile(client, token, name="Cap Profile")

    for index in range(MAX_MEMORY_EVIDENCE_ITEMS + 2):
        response = _create_memory(
            client,
            token,
            profile_id,
            title=f"Shared keyword memory {index}",
            content=f"Shared keyword content {index}",
            occurred_year=2000 + index,
        )
        assert response.status_code == 201

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Tell me about shared keyword memories"},
    )

    assert response.status_code == 200
    assert captured["prompt"].count("- [memory:") == MAX_MEMORY_EVIDENCE_ITEMS


def test_unrelated_query_does_not_inject_timeline_memory_fallback(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    token = _register_and_login(client, "ai-fallback-order@example.com")
    profile_id = _create_profile(client, token, name="Fallback Order Profile")
    assert _create_memory(
        client,
        token,
        profile_id,
        title="Created Only",
        content="Old fallback memory",
    ).status_code == 201
    assert _create_memory(
        client,
        token,
        profile_id,
        title="Year Only",
        content="Second fallback memory",
        occurred_year=2010,
    ).status_code == 201
    assert _create_memory(
        client,
        token,
        profile_id,
        title="Occurred At",
        content="Newest fallback memory",
        occurred_at="2024-05-06T10:30:00Z",
    ).status_code == 201

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "zzqv unrelated tokens"},
    )

    assert response.status_code == 200
    prompt = captured["prompt"]
    assert "- [memory:" not in prompt
    assert "latest_timeline_fallback" not in prompt


def test_keyword_matching_memory_is_preferred_over_unrelated_latest_memory(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    token = _register_and_login(client, "ai-keyword-priority@example.com")
    profile_id = _create_profile(client, token, name="Keyword Profile")
    assert _create_memory(
        client,
        token,
        profile_id,
        title="Recent Dinner",
        content="We had soup yesterday.",
        occurred_at="2025-01-01T10:00:00Z",
    ).status_code == 201
    assert _create_memory(
        client,
        token,
        profile_id,
        title="Paris Journey",
        content="We visited Paris and saw the Eiffel Tower.",
        occurred_year=2018,
    ).status_code == 201

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Do you remember Paris?"},
    )

    assert response.status_code == 200
    prompt = captured["prompt"]
    assert "Paris Journey" in prompt
    assert "keyword_overlap:" in prompt
    assert "Recent Dinner" not in prompt


def test_prompt_does_not_include_absolute_local_file_paths(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    token = _register_and_login(client, "ai-path-safety@example.com")
    profile_id = _create_profile(client, token, name="Path Safety Profile")
    client.patch(
        f"/api/memory-profiles/{profile_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"biography": "Kept notes in C:\\private\\notes.txt and /app/media/secret.png"},
    )
    assert _create_memory(
        client,
        token,
        profile_id,
        title="Path Memory",
        content="Stored at C:\\archive\\memory.txt and mirrored in /app/media/clip.mp4",
    ).status_code == 201

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "What files do you remember?"},
    )

    assert response.status_code == 200
    prompt = captured["prompt"]
    assert "C:\\private\\notes.txt" not in prompt
    assert "C:\\archive\\memory.txt" not in prompt
    assert "/app/media/secret.png" not in prompt
    assert "/app/media/clip.mp4" not in prompt
    assert "[path omitted]" in prompt


def test_grounded_memory_context_makes_no_external_api_calls(client, monkeypatch):
    def fail_http_call(*args, **kwargs):
        raise AssertionError("No external HTTP call should be made for grounded memory context")

    monkeypatch.setattr(settings, "ai_brain_provider", "mock")
    monkeypatch.setattr("httpx.request", fail_http_call)
    monkeypatch.setattr("httpx.get", fail_http_call)
    monkeypatch.setattr("httpx.post", fail_http_call)
    get_agent_orchestrator.cache_clear()

    token = _register_and_login(client, "ai-no-http-grounded@example.com")
    profile_id = _create_profile(client, token, name="No HTTP Grounded Profile")
    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Hello grounded world"},
    )

    assert response.status_code == 200


def test_chat_flow_calls_retrieval_for_correct_owner_and_profile(client, monkeypatch):
    captured_call: dict[str, object] = {}
    token = _register_and_login(client, "ai-rag-call@example.com")
    profile_id = _create_profile(client, token, name="RAG Call Profile")

    def capture_retrieval_call(db, *, current_user, profile_id, payload):
        captured_call["owner_user_id"] = current_user.id
        captured_call["profile_id"] = profile_id
        captured_call["query"] = payload.query
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code="multilingual_e5_small",
            results=[],
        )

    monkeypatch.setattr("app.modules.chat.service.retrieve_profile_rag", capture_retrieval_call)

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "What do you know about Prague?"},
    )

    assert response.status_code == 200
    assert captured_call == {
        "owner_user_id": 1,
        "profile_id": profile_id,
        "query": "What do you know about Prague?",
    }


def test_retrieved_chunks_are_included_in_brain_grounded_context(client, monkeypatch):
    captured = _capture_prompt(monkeypatch)
    token = _register_and_login(client, "ai-rag-prompt@example.com")
    profile_id = _create_profile(client, token, name="RAG Prompt Profile")

    def fake_retrieval_response(db, *, current_user, profile_id, payload):
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code="multilingual_e5_small",
            results=[
                RagRetrievalResultRead(
                    chunk_id=77,
                    source_id=33,
                    embedding_id=15,
                    score=0.9123,
                    text="Verified archive note about a Prague spring visit.",
                    chunk_index=0,
                    language="en",
                    source_type="manual_text",
                    validation_status="valid",
                    text_hash="hash-123",
                    qdrant_collection="eternal_world_rag_chunks__multilingual_e5_small",
                    payload_metadata={
                        "owner_user_id": current_user.id,
                        "profile_id": profile_id,
                    },
                )
            ],
        )

    monkeypatch.setattr("app.modules.chat.service.retrieve_profile_rag", fake_retrieval_response)

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Tell me about Prague"},
    )

    assert response.status_code == 200
    prompt = captured["prompt"]
    assert "[rag:77]" in prompt
    assert "Verified archive note about a Prague spring visit." in prompt
    assert "embedding_id=15" in prompt
    assert "validation=valid" in prompt


def test_cross_user_profile_data_is_not_retrieved(client, monkeypatch):
    called = False
    owner_token = _register_and_login(client, "ai-rag-owner@example.com")
    other_token = _register_and_login(client, "ai-rag-other@example.com")
    profile_id = _create_profile(client, owner_token, name="Owner RAG Profile")

    def fail_if_called(*args, **kwargs):
        nonlocal called
        called = True
        raise AssertionError("Retrieval should not run for cross-user profile access")

    monkeypatch.setattr("app.modules.chat.service.retrieve_profile_rag", fail_if_called)

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {other_token}"},
        json={"message": "Unauthorized access"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Memory profile not found"
    assert called is False


def test_no_retrieval_results_return_safe_lack_of_evidence_answer(client, monkeypatch):
    token = _register_and_login(client, "ai-rag-no-evidence@example.com")
    profile_id = _create_profile(client, token, name="No Evidence RAG Profile")

    def no_results(db, *, current_user, profile_id, payload):
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code="multilingual_e5_small",
            results=[],
        )

    monkeypatch.setattr("app.modules.chat.service.retrieve_profile_rag", no_results)
    monkeypatch.setattr(settings, "ai_brain_provider", "mock")
    get_agent_orchestrator.cache_clear()

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "What happened in Prague?"},
    )

    assert response.status_code == 200
    assert response.json()["ai_response_text"] == (
        "No Evidence RAG Profile mock reply: "
        "That information is not available in the stored memories/context."
    )


def test_chat_flow_does_not_create_query_rag_embeddings(client, monkeypatch):
    token = _register_and_login(client, "ai-rag-no-persist@example.com")
    profile_id = _create_profile(client, token, name="No Persist RAG Profile")

    def no_results(db, *, current_user, profile_id, payload):
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code="multilingual_e5_small",
            results=[],
        )

    monkeypatch.setattr("app.modules.chat.service.retrieve_profile_rag", no_results)

    db, session_generator = _get_test_db_session()
    try:
        before_count = db.query(RagEmbedding).count()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "What happened in Prague?"},
    )

    db, session_generator = _get_test_db_session()
    try:
        after_count = db.query(RagEmbedding).count()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    assert response.status_code == 200
    assert before_count == after_count


def test_brain_agent_chat_flow_uses_rag_retrieval_service_not_qdrant_directly(client, monkeypatch):
    token = _register_and_login(client, "ai-rag-service-only@example.com")
    profile_id = _create_profile(client, token, name="Service Only Profile")

    def fake_retrieval_response(db, *, current_user, profile_id, payload):
        return RagRetrievalResponseRead(
            profile_id=profile_id,
            query=payload.query,
            model_code="multilingual_e5_small",
            results=[],
        )

    def fail_if_qdrant_called(*args, **kwargs):
        raise AssertionError("Chat flow should use rag_retrieval service abstraction, not call Qdrant directly")

    monkeypatch.setattr("app.modules.chat.service.retrieve_profile_rag", fake_retrieval_response)
    monkeypatch.setattr("app.modules.rag_retrieval.service.build_qdrant_client", fail_if_qdrant_called)

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "Tell me about Prague"},
    )

    assert response.status_code == 200


def test_output_guard_sanitizes_lack_answer_with_substitute_unsupported_detail():
    result = apply_brain_output_guard(
        answer_text=(
            "В сохранённых воспоминаниях не указано, какие именно часы чинил отец Франтишек в гараже. "
            "Помню только, что я держала ему лупу. [rag:27618]"
        ),
        user_message="Какие часы отец Франтишек чинил в гараже?",
        response_metadata={"grounding_status": "grounded"},
        guard_context=BrainOutputGuardContext(
            expected_behavior="lack_of_evidence",
            forbidden_claims=("часы", "гараж", "луп"),
        ),
    )

    assert result.guard_applied is True
    assert result.reason == "forbidden_claim_in_lack_case"
    assert result.answer_text == (
        "В сохранённых воспоминаниях этого нет, поэтому не хочу придумывать."
    )
    assert "луп" in result.detected_unsupported_terms
    assert "держала" not in result.answer_text


def test_output_guard_does_not_change_grounded_machovo_answer():
    answer_text = (
        "Семейный архив хранит письмо, где Мартин описывает первый совместный отпуск с детьми "
        "у озера Маха. [rag:27633]"
    )

    result = apply_brain_output_guard(
        answer_text=answer_text,
        user_message="Где был первый совместный отпуск с детьми?",
        response_metadata={"grounding_status": "grounded"},
    )

    assert result.guard_applied is False
    assert result.answer_text == answer_text


def test_output_guard_lack_flag_ignores_trailing_aside_after_real_answer():
    # Regression: a grounded answer that states the requested fact first and
    # only adds an honest aside about a separate, unconfirmed detail must not
    # be flagged lack_of_evidence=True just because "не помню" appears later
    # in the text — that flag feeds memory-candidate extraction and eval
    # scoring, and previously misfired on this exact pattern.
    result = apply_brain_output_guard(
        answer_text=(
            "Деточка, я пела тебе «Спят усталые игрушки» летом в деревне перед сном. "
            "Но я не помню, чтобы кто-то это потом исправлял."
        ),
        user_message="Ты помнишь, какую песню я называл, а владелец потом исправил?",
        response_metadata={"grounding_status": "grounded"},
    )

    assert result.lack_of_evidence is None
    assert result.guard_applied is False


def test_output_guard_lack_flag_still_true_when_answer_opens_with_refusal():
    result = apply_brain_output_guard(
        answer_text=(
            "Я не помню этого по тем воспоминаниям, которые у меня сейчас есть. "
            "Если хочешь, расскажи мне больше, и мы сможем сохранить это как новое воспоминание."
        ),
        user_message="Какую песню ты пела мне перед сном?",
        response_metadata={"grounding_status": "grounded"},
    )

    assert result.lack_of_evidence is True


def test_output_guard_lack_flag_detects_denial_after_a_warm_address():
    # Regression: DIRECT_LACK_DENIAL_PREFIXES ("я не была", "никогда не", ...)
    # previously only matched if the denial was the very first text in the
    # answer. Real answers almost always open with a warm address first
    # ("Деточка, ...", "Милая, ..."), so the strict prefix check never fired
    # in practice for a perfectly clear direct denial.
    result = apply_brain_output_guard(
        answer_text=(
            "Деточка, я не была в Париже в 1968 году. Весь тот год я провела за учёбой в "
            "Брно и на практике в Моравии. Так что, к сожалению, названия парижской улицы "
            "я назвать не могу."
        ),
        user_message="Как называлась улица, где ты жила в Париже в 1968 году?",
        response_metadata={"grounding_status": "grounded"},
    )

    assert result.lack_of_evidence is True


def test_output_guard_does_not_change_grounded_reckovice_cherry_answer():
    answer_text = (
        "В саду в Řečkovicích росла старая вишня, под которой мы летом пили лимонад. [rag:27624]"
    )

    result = apply_brain_output_guard(
        answer_text=answer_text,
        user_message="Что росло в саду в Řečkovicích?",
        response_metadata={"grounding_status": "grounded"},
    )

    assert result.guard_applied is False
    assert result.answer_text == answer_text


def test_strip_internal_evidence_citations_removes_memory_and_rag_labels():
    assert strip_internal_evidence_citations(
        "Да, я жила у Попице [rag:27618], а потом вспоминала семью [memory:7]."
    ) == "Да, я жила у Попице, а потом вспоминала семью."


def test_brain_service_removes_internal_citations_regardless_of_avatar_persona():
    """Task 65.3 regression: citation stripping used to be gated on
    `avatar_persona is not None`, which the real authenticated `/api/chat`
    endpoint never sets - every grounded authenticated answer leaked its
    `[rag:...]` marker verbatim. Sanitization must now apply identically
    whether or not a persona object is attached to the request."""

    service = BrainAgentService(provider=CitationStubProvider())

    generic_response = service.generate_chat_response(
        OrchestratorChatRequest(
            profile=MemoryProfileContext(id=1, name="Ева"),
            user_message="Где ты жила?",
            recent_history=[],
        )
    )
    avatar_response = service.generate_chat_response(
        OrchestratorChatRequest(
            profile=MemoryProfileContext(id=1, name="Ева"),
            avatar_persona=load_demo_avatar_persona(),
            user_message="Где ты жила?",
            recent_history=[],
        )
    )

    assert "[rag:27618]" not in generic_response.text
    assert generic_response.text == "Деточка, я жила у Попице."
    assert generic_response.metadata["output_guard_applied"] is True
    assert generic_response.metadata["output_guard_reason"] == "avatar_internal_citation_removed"
    assert generic_response.metadata["removed_internal_citation_count"] == 1
    assert generic_response.metadata["persona_applied"] is False

    assert "[rag:27618]" not in avatar_response.text
    assert avatar_response.text == "Деточка, я жила у Попице."
    assert avatar_response.metadata["output_guard_applied"] is True
    assert avatar_response.metadata["output_guard_reason"] == "avatar_internal_citation_removed"
    assert avatar_response.metadata["removed_internal_citation_count"] == 1
    assert avatar_response.metadata["persona_applied"] is True


def test_brain_service_answer_without_citations_is_unchanged():
    class NoCitationStubProvider:
        def generate_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
            return BrainAgentResponse(
                text="Деточка, я жила у Попице.",
                provider_name="no-citation-stub",
                metadata={"grounding_status": "grounded"},
            )

    service = BrainAgentService(provider=NoCitationStubProvider())
    response = service.generate_chat_response(
        OrchestratorChatRequest(
            profile=MemoryProfileContext(id=1, name="Ева"),
            user_message="Где ты жила?",
            recent_history=[],
        )
    )

    assert response.text == "Деточка, я жила у Попице."
    assert response.metadata["output_guard_applied"] is False
    assert response.metadata["removed_internal_citation_count"] == 0


def test_brain_service_preserves_legitimate_bracketed_text():
    class BracketStubProvider:
        def generate_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
            return BrainAgentResponse(
                text="Ahoj [poznámka] to je vše, co si pamatuji.",
                provider_name="bracket-stub",
                metadata={"grounding_status": "grounded"},
            )

    service = BrainAgentService(provider=BracketStubProvider())
    response = service.generate_chat_response(
        OrchestratorChatRequest(
            profile=MemoryProfileContext(id=1, name="Anna"),
            user_message="Co si pamatujete?",
            recent_history=[],
        )
    )

    assert response.text == "Ahoj [poznámka] to je vše, co si pamatuji."
    assert response.metadata["output_guard_applied"] is False
    assert response.metadata["removed_internal_citation_count"] == 0


def test_brain_service_removes_multiple_citations_in_different_positions():
    class MultiCitationStubProvider:
        def generate_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
            return BrainAgentResponse(
                text=(
                    "[rag:1] Vyrostla jsem na vesnici [memory:42], v malém domku.\n"
                    "[rag:abc-def]"
                ),
                provider_name="multi-citation-stub",
                metadata={"grounding_status": "grounded"},
            )

    service = BrainAgentService(provider=MultiCitationStubProvider())
    response = service.generate_chat_response(
        OrchestratorChatRequest(
            profile=MemoryProfileContext(id=1, name="Anna"),
            user_message="Kde jste vyrostla?",
            recent_history=[],
        )
    )

    assert "[rag:" not in response.text
    assert "[memory:" not in response.text
    assert response.metadata["removed_internal_citation_count"] == 3


def test_brain_service_guard_metadata_does_not_store_original_answer_text():
    class StubProvider:
        def generate_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
            return BrainAgentResponse(
                text=(
                    "В сохранённых воспоминаниях не указано, какие именно часы чинил отец Франтишек в гараже. "
                    "Помню только, что я держала ему лупу. [rag:27618]"
                ),
                provider_name="stub",
                metadata={"grounding_status": "grounded"},
            )

    service = BrainAgentService(provider=StubProvider())
    response = service.generate_chat_response(
        OrchestratorChatRequest(
            profile=MemoryProfileContext(id=1, name="Анна"),
            user_message="Какие часы отец Франтишек чинил в гараже?",
            recent_history=[],
            output_guard_context=BrainOutputGuardContext(
                expected_behavior="lack_of_evidence",
                forbidden_claims=("часы", "гараж", "луп"),
            ),
        )
    )

    assert response.metadata["output_guard_applied"] is True
    assert response.metadata["output_guard_reason"] == "forbidden_claim_in_lack_case"
    assert response.metadata["output_guard_detected_unsupported_terms"] == ["часы", "гараж", "луп"]
    assert "original_answer_text" not in response.metadata


def test_response_language_none_preserves_generic_language_matching_behavior():
    """Every caller that never sets response_language (the generic
    authenticated chat endpoint, the RAG eval harness) must get byte-for-byte
    the same prompt as before Task 64.5.2 - no RESPONSE LANGUAGE directive at
    all, just the pre-existing generic LANGUAGE section."""
    messages = build_brain_prompt_messages(
        OrchestratorChatRequest(
            profile=MemoryProfileContext(id=1, name="Eva"),
            user_message="Tell me about yourself",
            recent_history=[],
        )
    )
    assert "RESPONSE LANGUAGE" not in messages.system_prompt
    assert "LANGUAGE" in messages.system_prompt


def test_response_language_cs_adds_authoritative_czech_directive():
    """Task 64.5.2 direct-locale architecture: demo_fa_chat passes
    response_language="cs" so the Brain answers directly in Czech from
    whatever-language evidence it retrieved, with no separate translation
    call."""
    messages = build_brain_prompt_messages(
        OrchestratorChatRequest(
            profile=MemoryProfileContext(id=1, name="Babička"),
            user_message="Kde jsi žila v dětství?",
            recent_history=[],
            response_language="cs",
        )
    )
    assert "RESPONSE LANGUAGE" in messages.system_prompt
    assert "Czech" in messages.system_prompt
    assert "You MUST write your entire answer in natural, fluent Czech" in messages.system_prompt


def test_response_language_ru_adds_authoritative_russian_directive():
    messages = build_brain_prompt_messages(
        OrchestratorChatRequest(
            profile=MemoryProfileContext(id=1, name="Babička"),
            user_message="Где ты жила в детстве?",
            recent_history=[],
            response_language="ru",
        )
    )
    assert "RESPONSE LANGUAGE" in messages.system_prompt
    assert "You MUST write your entire answer in natural, fluent Russian" in messages.system_prompt


def test_brain_agent_request_carries_response_language_through_service():
    """response_language must survive from OrchestratorChatRequest into the
    BrainAgentRequest the provider layer/logs see, even though the actual
    instruction is already baked into system_prompt by prompt_builder."""

    class CapturingProvider:
        def __init__(self):
            self.captured_request: BrainAgentRequest | None = None

        def generate_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
            self.captured_request = request
            return BrainAgentResponse(text="Ahoj.", provider_name="stub")

    provider = CapturingProvider()
    service = BrainAgentService(provider=provider)
    service.generate_chat_response(
        OrchestratorChatRequest(
            profile=MemoryProfileContext(id=1, name="Babička"),
            user_message="Kde jsi žila v dětství?",
            recent_history=[],
            response_language="cs",
        )
    )

    assert provider.captured_request is not None
    assert provider.captured_request.response_language == "cs"
