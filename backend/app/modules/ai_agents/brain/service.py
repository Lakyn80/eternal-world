from __future__ import annotations

from time import perf_counter

from app.core.config import settings
from app.core.metrics import observe_brain_answer_error, observe_brain_answer_success
from app.modules.ai_agents.brain.output_guard import (
    apply_brain_output_guard,
    sanitize_user_visible_answer,
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
            response_language=request.response_language,
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
        # Internal evidence-citation markers ([rag:...]/[memory:...]) must
        # never reach a real user's screen, on ANY route - not just the demo
        # persona chat. This used to be gated on `avatar_persona is not
        # None`, which authenticated `/api/chat` never sets, so citations
        # leaked into every real user's answer whenever grounded evidence
        # was cited. Sanitization now always runs; `persona_applied` below
        # remains a separate, unrelated concept (whether persona styling was
        # used), unaffected by this fix.
        citation_result = sanitize_user_visible_answer(answer_text)
        answer_text = citation_result.answer_text
        citation_guard_reason = (
            "avatar_internal_citation_removed" if citation_result.guard_applied else None
        )
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
                "output_guard_applied": guard_result.guard_applied or citation_result.guard_applied,
                "output_guard_reason": guard_result.reason or citation_guard_reason,
                "output_guard_detected_unsupported_terms": list(guard_result.detected_unsupported_terms),
                "output_guard_lack_of_evidence": guard_result.lack_of_evidence,
                "removed_internal_citation_count": citation_result.removed_internal_citation_count,
            },
        )


def get_brain_service() -> BrainAgentService:
    return BrainAgentService(provider=build_brain_provider())
