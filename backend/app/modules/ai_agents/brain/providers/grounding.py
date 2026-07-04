from __future__ import annotations

import re
from typing import Any

from app.modules.ai_agents.schemas import BrainAgentRequest, BrainAgentResponse


FACTUAL_QUERY_PATTERN = re.compile(
    r"\b(what|when|where|who|which|tell me|do you remember|remember|about|why|how)\b",
    re.IGNORECASE,
)
LACK_OF_EVIDENCE_MESSAGE = "That information is not available in the stored memories/context."


def has_grounded_evidence(request: BrainAgentRequest) -> bool:
    grounded_context = request.grounded_context
    if grounded_context is None:
        return False

    return bool(
        grounded_context.evidence_items
        or grounded_context.retrieved_evidence_items
    )


def should_return_lack_of_evidence_response(request: BrainAgentRequest) -> bool:
    return not has_grounded_evidence(request) and bool(
        FACTUAL_QUERY_PATTERN.search(request.user_message)
    )


def resolve_grounding_status(request: BrainAgentRequest) -> str:
    if has_grounded_evidence(request):
        return "grounded"

    if should_return_lack_of_evidence_response(request):
        return "no_evidence"

    return "general"


def build_lack_of_evidence_response(
    request: BrainAgentRequest,
    *,
    provider_name: str,
    text_prefix: str = "",
    metadata: dict[str, Any] | None = None,
) -> BrainAgentResponse:
    response_metadata = {
        "agent": "brain",
        "grounding_status": "no_evidence",
        **(metadata or {}),
    }
    return BrainAgentResponse(
        text=f"{text_prefix}{LACK_OF_EVIDENCE_MESSAGE}",
        provider_name=provider_name,
        metadata=response_metadata,
    )


def build_grounded_mock_answer(request: BrainAgentRequest) -> str | None:
    grounded_context = request.grounded_context
    if grounded_context is None:
        return None

    cited_parts: list[str] = []
    for evidence_item in grounded_context.evidence_items:
        if evidence_item.content_preview:
            cited_parts.append(
                f"[memory:{evidence_item.source_id}] {evidence_item.content_preview}"
            )

    for evidence_item in grounded_context.retrieved_evidence_items:
        if evidence_item.content_preview:
            cited_parts.append(
                f"[rag:{evidence_item.chunk_id}] {evidence_item.content_preview}"
            )

    if not cited_parts:
        return None

    return f"{request.profile.name} mock reply: " + " ".join(cited_parts)
