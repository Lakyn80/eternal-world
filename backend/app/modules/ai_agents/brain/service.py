from __future__ import annotations

from app.modules.ai_agents.brain.provider import BrainAgentProvider, build_brain_provider
from app.modules.ai_agents.brain.prompt_builder import build_brain_prompt_messages
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
        prompt_messages = build_brain_prompt_messages(request)
        provider_request = BrainAgentRequest(
            profile=request.profile,
            user_message=request.user_message,
            recent_history=request.recent_history,
            grounded_context=request.grounded_context,
            system_prompt=prompt_messages.system_prompt,
            user_prompt=prompt_messages.user_prompt,
            prompt=prompt_messages.combined_prompt,
        )
        return self.provider.generate_response(provider_request)


def get_brain_service() -> BrainAgentService:
    return BrainAgentService(provider=build_brain_provider())
