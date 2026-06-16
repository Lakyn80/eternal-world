import pytest

from app.core.config import Settings, settings
from app.core.logging import REDACTED_VALUE, sanitize_log_data
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
