import pytest

from app.core.config import Settings, settings
from app.db.models import RagEmbedding
from app.db.session import get_db
from app.core.logging import REDACTED_VALUE, sanitize_log_data
from app.main import app
from app.modules.ai_agents.brain.context import MAX_MEMORY_EVIDENCE_ITEMS
from app.modules.ai_agents.brain.provider import (
    BrainProviderConfigurationError,
    MockBrainAgentProvider,
    build_brain_provider,
)
from app.modules.ai_agents.orchestrator import AgentOrchestrator, get_agent_orchestrator
from app.modules.ai_agents.schemas import (
    BrainAgentRequest,
    BrainAgentResponse,
    MemoryProfileContext,
    OrchestratorChatRequest,
)
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


def _get_test_db_session():
    override = app.dependency_overrides[get_db]
    session_generator = override()
    db = next(session_generator)
    return db, session_generator


def test_default_brain_provider_is_mock():
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
        prompt="test-prompt",
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


def test_openai_compatible_provider_requires_api_key_when_selected():
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
    assert "No verified memory evidence is currently available" in captured["prompt"]


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
    assert "A. Avatar identity and style" in prompt
    assert "- Name: Grounded Ada" in prompt
    assert "- Biography: Pioneer of analytical engines" in prompt
    assert "- Personality style hint: Warm and curious" in prompt
    assert "- Catchphrases style hint: Let's think carefully" in prompt


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
    assert "B. Verified memory evidence" in prompt
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
    assert "C. Grounding instructions" in prompt
    assert "Answer factual questions only from the verified evidence" in prompt
    assert "Do not invent unknown facts, dates, places, people, relationships, or events." in prompt
    assert "it is not available in the stored memories/context" in prompt
    assert "cite the source inline using [memory:id] or [rag:chunk_id]" in prompt
    assert "Respond in the same language as the user's current message" in prompt
    assert "B1. Timeline memory evidence" in prompt or "No verified memory evidence" in prompt


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
    assert "B1. Timeline memory evidence" in prompt
    assert "B2. Retrieved archival RAG evidence" in prompt
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
            title=f"Memory {index}",
            content=f"Fallback content {index}",
            occurred_year=2000 + index,
        )
        assert response.status_code == 201

    response = client.post(
        f"/api/chat/{profile_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": "completely unrelated query"},
    )

    assert response.status_code == 200
    assert captured["prompt"].count("- [memory:") == MAX_MEMORY_EVIDENCE_ITEMS


def test_memory_evidence_is_deterministic_and_timeline_ordered_for_fallback(client, monkeypatch):
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
    assert prompt.index("Occurred At") < prompt.index("Year Only") < prompt.index("Created Only")
    assert "latest_timeline_fallback" in prompt


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
