from __future__ import annotations

from app.modules.ai_agents.schemas import BrainAgentRequest, BrainAgentResponse


class MockBrainAgentProvider:
    provider_name = "mock"

    def generate_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
        history_count = len(request.recent_history)
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
            },
        )
