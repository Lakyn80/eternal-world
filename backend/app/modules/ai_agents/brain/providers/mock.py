from __future__ import annotations

import re

from app.modules.ai_agents.schemas import BrainAgentRequest, BrainAgentResponse


FACTUAL_QUERY_PATTERN = re.compile(
    r"\b(what|when|where|who|which|tell me|do you remember|remember|about|why|how)\b",
    re.IGNORECASE,
)


class MockBrainAgentProvider:
    provider_name = "mock"

    def generate_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
        history_count = len(request.recent_history)
        grounded_context = request.grounded_context
        memory_evidence_items = grounded_context.evidence_items if grounded_context is not None else []
        rag_evidence_items = grounded_context.retrieved_evidence_items if grounded_context is not None else []
        has_grounded_evidence = bool(memory_evidence_items or rag_evidence_items)

        if not has_grounded_evidence and FACTUAL_QUERY_PATTERN.search(request.user_message):
            return BrainAgentResponse(
                text=(
                    f"{request.profile.name} mock reply: "
                    "That information is not available in the stored memories/context."
                ),
                provider_name=self.provider_name,
                metadata={
                    "agent": "brain",
                    "history_count": history_count,
                    "grounding_status": "no_evidence",
                },
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
                "grounding_status": "grounded" if has_grounded_evidence else "general",
            },
        )
