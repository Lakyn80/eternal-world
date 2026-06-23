from __future__ import annotations

from app.modules.ai_agents.schemas import BrainAgentRequest, BrainAgentResponse
from app.modules.ai_agents.brain.providers.grounding import (
    build_lack_of_evidence_response,
    resolve_grounding_status,
    should_return_lack_of_evidence_response,
)


class MockBrainAgentProvider:
    provider_name = "mock"

    def generate_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
        history_count = len(request.recent_history)

        if should_return_lack_of_evidence_response(request):
            return build_lack_of_evidence_response(
                request,
                provider_name=self.provider_name,
                text_prefix=f"{request.profile.name} mock reply: ",
                metadata={"history_count": history_count},
            )

        response_text = (
            f"{request.profile.name} mock reply: I heard '{request.user_message}'. "
            f"Recent messages considered: {history_count}."
        )
        return BrainAgentResponse(
            text=response_text,
            provider_name=self.provider_name,
            metadata={
                "agent": "brain",
                "history_count": history_count,
                "grounding_status": resolve_grounding_status(request),
            },
        )
