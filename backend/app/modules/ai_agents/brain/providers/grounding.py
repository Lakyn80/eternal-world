from __future__ import annotations

import re
from typing import Any

from app.modules.ai_agents.schemas import BrainAgentRequest, BrainAgentResponse


FACTUAL_QUERY_PATTERN = re.compile(
    r"\b(what|when|where|who|which|tell me|do you remember|remember|about|why|how)\b",
    re.IGNORECASE,
)
_CYRILLIC_PATTERN = re.compile(r"[А-Яа-яЁё]")
_CZECH_HINT_PATTERN = re.compile(
    r"\b(co|kde|kdy|proč|jak|kdo|vzpomín|nevybav|nemám|nevím)\b",
    re.IGNORECASE,
)
_GERMAN_HINT_PATTERN = re.compile(
    r"(erinnere mich|erinnerst du|weiß ich nicht|weiss ich nicht|leider nicht)",
    re.IGNORECASE,
)
_SPANISH_HINT_PATTERN = re.compile(
    r"\b(dónde|donde|cuándo|cuando|quién|quien|recuerdas|recuerdo)\b",
    re.IGNORECASE,
)
_FRENCH_HINT_PATTERN = re.compile(
    r"(je ne me souviens|je ne me rappelle|où est|quand est|pourquoi)",
    re.IGNORECASE,
)

# Natural first-person defaults (never mention stored/indexed memories as a system).
LACK_OF_EVIDENCE_MESSAGES: dict[str, str] = {
    "en": "I don't remember that.",
    "cs": "Na to si bohužel nevzpomínám.",
    "ru": "К сожалению, я этого не помню.",
    "de": "Daran erinnere ich mich leider nicht.",
    "es": "No recuerdo eso.",
    "fr": "Je ne m'en souviens pas.",
}
# Backward-compatible alias used by older tests/imports.
LACK_OF_EVIDENCE_MESSAGE = LACK_OF_EVIDENCE_MESSAGES["en"]


def resolve_lack_of_evidence_message(
    *,
    response_language: str | None = None,
    user_message: str = "",
) -> str:
    """Pick a natural first-person lack-of-evidence line for the reply language."""

    code = (response_language or "").strip().lower()
    if code in LACK_OF_EVIDENCE_MESSAGES:
        return LACK_OF_EVIDENCE_MESSAGES[code]

    probe = user_message or ""
    if _CYRILLIC_PATTERN.search(probe):
        return LACK_OF_EVIDENCE_MESSAGES["ru"]
    if _CZECH_HINT_PATTERN.search(probe):
        return LACK_OF_EVIDENCE_MESSAGES["cs"]
    if _GERMAN_HINT_PATTERN.search(probe):
        return LACK_OF_EVIDENCE_MESSAGES["de"]
    if _SPANISH_HINT_PATTERN.search(probe):
        return LACK_OF_EVIDENCE_MESSAGES["es"]
    if _FRENCH_HINT_PATTERN.search(probe):
        return LACK_OF_EVIDENCE_MESSAGES["fr"]
    return LACK_OF_EVIDENCE_MESSAGES["en"]


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
    message = resolve_lack_of_evidence_message(
        response_language=request.response_language,
        user_message=request.user_message,
    )
    response_metadata = {
        "agent": "brain",
        "grounding_status": "no_evidence",
        **(metadata or {}),
    }
    return BrainAgentResponse(
        text=f"{text_prefix}{message}",
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
