from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.db.models import User
from app.modules.ai_agents import get_agent_orchestrator
from app.modules.ai_agents.brain.context import build_rag_evidence_items, build_vector_retrieval_grounded_context
from app.modules.ai_agents.schemas import MemoryProfileContext, OrchestratorChatRequest
from app.modules.embeddings.embedding_cache import build_text_hash
from app.modules.memory_profiles.repository import get_memory_profile_for_user, list_memory_profiles_for_user
from app.modules.rag_evaluation.brain_eval_e2e_bootstrap import (
    FAMILY_AVATAR_RU_E2E_EMAIL,
    FAMILY_AVATAR_RU_E2E_PROFILE_NAME,
)
from app.modules.rag_retrieval.schemas import RagRetrievalRequest, RagRetrievalResultRead
from app.modules.rag_retrieval.service import retrieve_profile_rag
from app.modules.users.repository import get_user_by_email

from .schemas import DemoFaChatEvidenceItem, DemoFaChatMessageResponse


DEMO_FA_CHAT_MESSAGE_MAX_LENGTH = 4000
DEMO_FA_CHAT_EVIDENCE_PREVIEW_LENGTH = 220
DEMO_FA_CHAT_PROFILE_UNAVAILABLE_DETAIL = "Тестовый профиль аватара сейчас недоступен."
DEMO_FA_CHAT_INTERNAL_ERROR_DETAIL = "Не удалось получить ответ аватара. Попробуйте ещё раз."

logger = get_logger("demo_fa_chat")


class DemoFaChatValidationError(Exception):
    pass


class DemoFaChatProfileUnavailableError(Exception):
    pass


@dataclass(frozen=True)
class DemoFaChatResolvedProfile:
    user: User
    profile: object


def _normalize_message_text(value: str) -> str:
    normalized_value = value.strip()
    if not normalized_value:
        raise DemoFaChatValidationError("Сообщение не должно быть пустым.")
    if len(normalized_value) > DEMO_FA_CHAT_MESSAGE_MAX_LENGTH:
        raise DemoFaChatValidationError("Сообщение слишком длинное для демо-чата.")
    return normalized_value


def _build_message_hash_prefix(message: str) -> str:
    return build_text_hash(message).split(":", 1)[1][:8]


def _build_profile_context(profile) -> MemoryProfileContext:
    return MemoryProfileContext(
        id=profile.id,
        name=profile.name,
        birth_date=profile.birth_date,
        death_date=profile.death_date,
        biography=profile.biography,
        personality=profile.personality,
        catchphrases=profile.catchphrases,
        is_public=profile.is_public,
    )


def _resolve_demo_profile(
    db: Session,
    *,
    profile_id: int | None,
) -> DemoFaChatResolvedProfile:
    user = get_user_by_email(db, FAMILY_AVATAR_RU_E2E_EMAIL)
    if user is None:
        raise DemoFaChatProfileUnavailableError(DEMO_FA_CHAT_PROFILE_UNAVAILABLE_DETAIL)

    if profile_id is not None:
        profile = get_memory_profile_for_user(
            db,
            user_id=user.id,
            profile_id=profile_id,
        )
    else:
        profiles = list_memory_profiles_for_user(db, user.id)
        profile = next(
            (item for item in profiles if item.name == FAMILY_AVATAR_RU_E2E_PROFILE_NAME),
            None,
        )

    if profile is None:
        raise DemoFaChatProfileUnavailableError(DEMO_FA_CHAT_PROFILE_UNAVAILABLE_DETAIL)

    return DemoFaChatResolvedProfile(user=user, profile=profile)


def _truncate_preview(text: str, *, limit: int = DEMO_FA_CHAT_EVIDENCE_PREVIEW_LENGTH) -> str:
    normalized_text = " ".join(text.split())
    if len(normalized_text) <= limit:
        return normalized_text
    return f"{normalized_text[: limit - 3].rstrip()}..."


def _build_evidence_items(
    results: list[RagRetrievalResultRead],
    *,
    debug: bool,
) -> list[DemoFaChatEvidenceItem]:
    if not debug:
        return []

    return [
        DemoFaChatEvidenceItem(
            chunk_id=str(result.chunk_id),
            source_id=result.source_id,
            source_title=result.source_title,
            score=float(result.score),
            text_preview=_truncate_preview(result.text),
        )
        for result in results
    ]


def run_demo_fa_chat_message(
    db: Session,
    *,
    profile_id: int | None,
    message: str,
    debug: bool,
    trace_id: str,
) -> DemoFaChatMessageResponse:
    normalized_message = _normalize_message_text(message)
    message_hash_prefix = _build_message_hash_prefix(normalized_message)
    resolved_profile = _resolve_demo_profile(db, profile_id=profile_id)
    log_event(
        logger,
        20,
        "fa_demo_chat_request",
        trace_id=trace_id,
        profile_id=resolved_profile.profile.id,
        message_length=len(normalized_message),
        message_hash_prefix=message_hash_prefix,
        debug=debug,
    )

    retrieval_response = retrieve_profile_rag(
        db,
        current_user=resolved_profile.user,
        profile_id=resolved_profile.profile.id,
        payload=RagRetrievalRequest(query=normalized_message),
    )
    retrieved_evidence_items = build_rag_evidence_items(retrieval_response.results)
    grounded_context = build_vector_retrieval_grounded_context(
        profile=resolved_profile.profile,
        retrieved_evidence_items=retrieved_evidence_items,
    )

    orchestrator = get_agent_orchestrator()
    orchestrator_response = orchestrator.generate_chat_response(
        OrchestratorChatRequest(
            profile=_build_profile_context(resolved_profile.profile),
            user_message=normalized_message,
            recent_history=[],
            grounded_context=grounded_context,
        )
    )
    metadata = dict(orchestrator_response.metadata)
    lack_of_evidence = bool(metadata.get("output_guard_lack_of_evidence")) or (
        str(metadata.get("grounding_status") or "").strip().lower() == "no_evidence"
    )

    log_event(
        logger,
        20,
        "fa_demo_chat_response",
        trace_id=trace_id,
        profile_id=resolved_profile.profile.id,
        retrieval_used=bool(retrieval_response.results),
        guard_applied=bool(metadata.get("output_guard_applied")),
        guard_reason=metadata.get("output_guard_reason"),
        lack_of_evidence=lack_of_evidence,
    )
    return DemoFaChatMessageResponse(
        answer=orchestrator_response.text,
        lack_of_evidence=lack_of_evidence,
        retrieval_used=bool(retrieval_response.results),
        guard_applied=bool(metadata.get("output_guard_applied")),
        guard_reason=(
            str(metadata.get("output_guard_reason"))
            if metadata.get("output_guard_reason") is not None
            else None
        ),
        trace_id=trace_id,
        evidence=_build_evidence_items(retrieval_response.results, debug=debug),
    )
