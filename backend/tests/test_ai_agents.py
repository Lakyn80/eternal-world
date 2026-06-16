from app.modules.ai_agents.brain.provider import MockBrainAgentProvider
from app.modules.ai_agents.orchestrator import AgentOrchestrator
from app.modules.ai_agents.schemas import (
    BrainAgentRequest,
    BrainAgentResponse,
    MemoryProfileContext,
    OrchestratorChatRequest,
)


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
