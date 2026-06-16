from __future__ import annotations

from app.modules.ai_agents.brain.provider import BrainAgentProvider, build_brain_provider
from app.modules.ai_agents.brain.prompt_builder import build_brain_prompt
from app.modules.ai_agents.schemas import (
    BrainAgentRequest,
    BrainAgentResponse,
    OrchestratorChatRequest,
)


class BrainAgentService:
    def __init__(self, provider: BrainAgentProvider) -> None:
        self.provider = provider

    def generate_chat_response(
        self,
        request: OrchestratorChatRequest,
    ) -> BrainAgentResponse:
        prompt = build_brain_prompt(request)
        provider_request = BrainAgentRequest(
            profile=request.profile,
            user_message=request.user_message,
            recent_history=request.recent_history,
            prompt=prompt,
        )
        return self.provider.generate_response(provider_request)


def get_brain_service() -> BrainAgentService:
    return BrainAgentService(provider=build_brain_provider())
