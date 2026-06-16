from __future__ import annotations

from functools import lru_cache

from app.modules.ai_agents.brain.provider import MockBrainAgentProvider
from app.modules.ai_agents.brain.service import BrainAgentService
from app.modules.ai_agents.director.service import DirectorAgentService
from app.modules.ai_agents.face.service import FaceAgentService
from app.modules.ai_agents.schemas import (
    BrainAgentResponse,
    OrchestratorChatRequest,
    OrchestratorChatResponse,
)
from app.modules.ai_agents.voice.service import VoiceAgentService


class AgentOrchestrator:
    def __init__(
        self,
        *,
        brain_service: BrainAgentService | None = None,
        voice_service: VoiceAgentService | None = None,
        face_service: FaceAgentService | None = None,
        director_service: DirectorAgentService | None = None,
    ) -> None:
        self.brain_service = brain_service or BrainAgentService(
            provider=MockBrainAgentProvider()
        )
        self.voice_service = voice_service or VoiceAgentService()
        self.face_service = face_service or FaceAgentService()
        self.director_service = director_service or DirectorAgentService()

    def generate_chat_response(
        self,
        request: OrchestratorChatRequest,
    ) -> OrchestratorChatResponse:
        brain_response: BrainAgentResponse = self.brain_service.generate_chat_response(
            request
        )
        metadata = {
            "orchestrator_mode": "brain_only",
            **brain_response.metadata,
        }
        return OrchestratorChatResponse(
            text=brain_response.text,
            audio_url=None,
            video_url=None,
            provider_name=brain_response.provider_name,
            metadata=metadata,
        )


@lru_cache(maxsize=1)
def get_agent_orchestrator() -> AgentOrchestrator:
    return AgentOrchestrator()
