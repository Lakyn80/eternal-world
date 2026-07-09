from __future__ import annotations

from app.modules.ai_agents.brain.output_guard import apply_brain_output_guard
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
            output_guard_context=request.output_guard_context,
            system_prompt=prompt_messages.system_prompt,
            user_prompt=prompt_messages.user_prompt,
            prompt=prompt_messages.combined_prompt,
        )
        provider_response = self.provider.generate_response(provider_request)
        guard_result = apply_brain_output_guard(
            answer_text=provider_response.text,
            user_message=request.user_message,
            response_metadata=provider_response.metadata,
            guard_context=request.output_guard_context,
        )
        return BrainAgentResponse(
            text=guard_result.answer_text,
            provider_name=provider_response.provider_name,
            metadata={
                **provider_response.metadata,
                "output_guard_applied": guard_result.guard_applied,
                "output_guard_reason": guard_result.reason,
                "output_guard_detected_unsupported_terms": list(guard_result.detected_unsupported_terms),
                "output_guard_lack_of_evidence": guard_result.lack_of_evidence,
            },
        )


def get_brain_service() -> BrainAgentService:
    return BrainAgentService(provider=build_brain_provider())
