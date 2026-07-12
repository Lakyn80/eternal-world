from __future__ import annotations

from time import perf_counter

from app.core.config import settings
from app.core.metrics import observe_brain_answer_error, observe_brain_answer_success
from app.modules.ai_agents.brain.output_guard import (
    apply_brain_output_guard,
    strip_internal_evidence_citations,
)
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
        started_at = perf_counter()
        prompt_messages = build_brain_prompt_messages(request)
        provider_request = BrainAgentRequest(
            profile=request.profile,
            avatar_persona=request.avatar_persona,
            user_message=request.user_message,
            recent_history=request.recent_history,
            grounded_context=request.grounded_context,
            output_guard_context=request.output_guard_context,
            system_prompt=prompt_messages.system_prompt,
            user_prompt=prompt_messages.user_prompt,
            prompt=prompt_messages.combined_prompt,
        )
        try:
            provider_response = self.provider.generate_response(provider_request)
        except Exception:
            observe_brain_answer_error(
                provider=settings.ai_brain_provider,
                model=settings.ai_brain_model,
            )
            raise
        guard_result = apply_brain_output_guard(
            answer_text=provider_response.text,
            user_message=request.user_message,
            response_metadata=provider_response.metadata,
            guard_context=request.output_guard_context,
        )
        answer_text = guard_result.answer_text
        avatar_style_guard_applied = False
        avatar_style_guard_reason = None
        if request.avatar_persona is not None:
            sanitized_answer_text = strip_internal_evidence_citations(answer_text)
            avatar_style_guard_applied = sanitized_answer_text != answer_text
            if avatar_style_guard_applied:
                answer_text = sanitized_answer_text
                avatar_style_guard_reason = "avatar_internal_citation_removed"
        observe_brain_answer_success(
            provider=settings.ai_brain_provider,
            model=settings.ai_brain_model,
            duration_seconds=perf_counter() - started_at,
        )
        return BrainAgentResponse(
            text=answer_text,
            provider_name=provider_response.provider_name,
            metadata={
                **provider_response.metadata,
                "persona_applied": request.avatar_persona is not None,
                "avatar_persona_id": (
                    request.avatar_persona.avatar_id
                    if request.avatar_persona is not None
                    else None
                ),
                "output_guard_applied": guard_result.guard_applied or avatar_style_guard_applied,
                "output_guard_reason": guard_result.reason or avatar_style_guard_reason,
                "output_guard_detected_unsupported_terms": list(guard_result.detected_unsupported_terms),
                "output_guard_lack_of_evidence": guard_result.lack_of_evidence,
            },
        )


def get_brain_service() -> BrainAgentService:
    return BrainAgentService(provider=build_brain_provider())
