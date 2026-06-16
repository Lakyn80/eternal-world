from __future__ import annotations

from typing import Protocol

from app.modules.ai_agents.schemas import BrainAgentRequest, BrainAgentResponse


class BrainAgentProvider(Protocol):
    def generate_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
        ...


class MockBrainAgentProvider:
    provider_name = "mock-brain-provider"

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
