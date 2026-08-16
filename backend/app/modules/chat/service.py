from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logging import get_logger, get_request_id, log_event
from app.core.metrics import (
    observe_chat_async_cancellation,
    observe_chat_operation,
)
from app.modules.ai_agents.brain.context import (
    build_grounded_context,
    build_rag_evidence_items,
    filter_learned_memory_results_by_question_intent,
    prioritize_corrected_memory_evidence,
)
from app.modules.avatar_persona.memory_query_intent import (
    MemoryQueryIntent,
    classify_memory_query_intent,
)
from app.modules.avatar_persona.language_detection import detect_message_language
from app.modules.avatar_persona.settings_service import (
    build_avatar_persona_section,
    resolve_avatar_persona,
)
from app.db.models import ChatMessage, MemoryProfile, User
from app.modules.ai_agents import get_agent_orchestrator
from app.modules.ai_agents.schemas import (
    ChatHistoryEntry,
    MemoryProfileContext,
    OrchestratorChatRequest,
    OrchestratorChatResponse,
)
from app.modules.billing.service import get_effective_plan_definition_for_user
from app.modules.chat import active_session, redis_snapshot, repository
from app.modules.chat.admission import (
    async_brain_chat_admission,
    async_user_chat_admission,
    brain_chat_admission,
    map_brain_provider_error,
    resolve_user_chat_rate_limit,
    user_chat_admission,
)
from app.modules.chat.message_translations import (
    ensure_assistant_display_translation,
    ensure_user_canonical_translation,
    resolve_chat_message_views,
    resolve_user_canonical_text,
)
from app.modules.chat.redis_snapshot import ChatSnapshot, SnapshotMessage
from app.modules.chat.schemas import ChatActiveRead, ChatMessageCreate, ChatMessageRead, ChatSendResponse
from app.modules.language_registry import (
    assert_canonical_memorial_language,
    is_translation_language,
    normalize_language_code,
)
from app.modules.memories import repository as memories_repository
from app.modules.memorial_access.capabilities import MemorialCapability, resolve_authorized_profile
from app.modules.memorial_access.service import MemorialForbiddenError, MemorialNotFoundError
from app.modules.provider_usage.context import AiCallContext
from app.modules.provider_usage.enums import AiFeature, AiStepType, ExecutionSource
from app.modules.provider_usage.service import (
    run_instrumented_single_attempt_action,
    run_instrumented_single_attempt_action_async,
)
from app.modules.provider_usage.usage import normalize_openai_compatible_usage
from app.modules.qdrant_indexing.exceptions import QdrantClientError, QdrantCollectionConfigurationError
from app.modules.rag_retrieval.exceptions import (
    RagRetrievalDisabledError,
    RagRetrievalModelUnavailableError,
    RagRetrievalProfileNotFoundError,
)
from app.modules.rag_retrieval.schemas import RagRetrievalRequest
from app.modules.rag_retrieval.service import retrieve_profile_rag


def _extract_brain_token_usage(orchestrator_response):
    metadata = orchestrator_response.metadata or {}
    return normalize_openai_compatible_usage(
        raw_response={
            "id": metadata.get("provider_request_id"),
            "usage": metadata.get("usage"),
        }
    )


RECENT_HISTORY_LIMIT = 10
_logger = get_logger("chat")


class ChatProfileNotFoundError(Exception):
    pass


class ChatForbiddenError(Exception):
    pass


def _get_authorized_profile_or_raise(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
) -> MemoryProfile:
    """Resolve `profile_id` for `current_user`, requiring chat_with_avatar.

    Every active member (owner/trusted_reviewer/contributor/viewer) may chat
    with the avatar; a non-member gets a safe 404, a member without the
    capability gets a 403. Membership is re-read from the database on every
    call - the caller's asserted role is never trusted.
    """

    try:
        profile, _membership = resolve_authorized_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
            capability=MemorialCapability.CHAT_WITH_AVATAR,
        )
    except MemorialNotFoundError as exc:
        raise ChatProfileNotFoundError("Memory profile not found") from exc
    except MemorialForbiddenError as exc:
        raise ChatForbiddenError("Insufficient memorial permissions") from exc
    return profile


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


def _resolve_user_source_language(
    *,
    message: str,
    locale: str | None,
    preferred_ui_language: str | None,
    canonical_language: str,
) -> str:
    """Pick durable source language for a user turn.

    Precedence: detected message language → request locale → account UI →
    memorial canonical (last resort so MCT always has a valid source).
    """

    detected = detect_message_language(message)
    if detected and is_translation_language(detected):
        return detected
    if locale and is_translation_language(locale):
        return normalize_language_code(locale) or canonical_language
    preferred = normalize_language_code(preferred_ui_language)
    if preferred and is_translation_language(preferred):
        return preferred
    return canonical_language


def _resolve_display_language(
    *,
    source_language: str,
    locale: str | None,
    preferred_ui_language: str | None,
    canonical_language: str,
) -> str:
    """Viewer language for assistant display translation.

    Precedence: explicit request locale → account UI language → detected
    message language → memorial canonical.
    """

    if locale and is_translation_language(locale):
        return normalize_language_code(locale) or canonical_language
    preferred = normalize_language_code(preferred_ui_language)
    if preferred and is_translation_language(preferred):
        return preferred
    if source_language and is_translation_language(source_language):
        return source_language
    return canonical_language


def _build_history_entry(
    db: Session,
    *,
    message: ChatMessage,
    profile: MemoryProfile,
    actor: User,
) -> ChatHistoryEntry:
    """Brain history stays memorial-canonical when translations are usable."""

    if message.role == "user":
        content, _status = resolve_user_canonical_text(
            db,
            profile=profile,
            message=message,
            actor=actor,
            ensure_missing=True,
        )
    else:
        content = message.content
    return ChatHistoryEntry(
        role=message.role,
        content=content,
        created_at=message.created_at,
    )


def _build_message_read(
    db: Session,
    *,
    message: ChatMessage,
    profile: MemoryProfile,
    viewer: User,
    display_locale: str | None = None,
    ensure_missing: bool = True,
) -> ChatMessageRead:
    views = resolve_chat_message_views(
        db,
        message=message,
        profile=profile,
        viewer=viewer,
        display_locale=display_locale,
        ensure_missing=ensure_missing,
    )
    return ChatMessageRead(
        id=message.id,
        profile_id=message.memory_profile_id,
        role=message.role,
        content=views.display_text,
        source_language=views.source_language,
        display_language=views.display_language,
        display_translation_status=views.display_translation_status,
        created_at=message.created_at,
    )


def _retrieve_rag_evidence_safely(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    user_message: str,
):
    try:
        retrieval_response = retrieve_profile_rag(
            db,
            current_user=current_user,
            profile_id=profile_id,
            payload=RagRetrievalRequest(
                query=user_message,
            ),
        )
    except (
        RagRetrievalDisabledError,
        RagRetrievalModelUnavailableError,
        RagRetrievalProfileNotFoundError,
        QdrantClientError,
        QdrantCollectionConfigurationError,
        Exception,
    ):
        return []

    # Task 65.6.1 (Part F/I): the authenticated chat path retrieves the same
    # top-k pool the demo learned-memory path does, but was missing the
    # demo path's evidence-ordering step (`app.modules.demo_fa_chat.
    # service`) - so an owner-approved, verified learned memory that WAS
    # correctly retrieved could still be outranked in the prompt by several
    # unrelated/older archival chunks, purely by raw vector score. Reusing
    # these two existing, already-tested functions unchanged (never
    # re-implemented here) reorders and caps the already-retrieved,
    # already-top_k'd pool - it does not change retrieval, ranking, or
    # top_k itself (see their own docstrings in `ai_agents.brain.context`).
    filtered_results = filter_learned_memory_results_by_question_intent(
        retrieval_response.results,
        user_message=user_message,
    )
    # Task 65.10: the authenticated chat path previously applied the
    # corrected-memory-intent evidence ordering (verified items floated
    # unconditionally to the front, as a group) to EVERY turn, regardless of
    # question shape - unlike the demo path, which only ever applies it
    # behind an explicit intent classification. That mismatch is why a
    # highly relevant, approved memorial-contribution memory could be
    # displaced by less-relevant conversation-candidate items on an
    # ordinary factual question (the reported "18. narozeniny" defect).
    # Classifying intent here and only requesting the stronger
    # verified-first mode for turns actually classified as a corrected-
    # memory question restores relevance-driven ranking for ordinary
    # questions while preserving the empirically-tuned Task 64.4.2 behavior
    # for the question shape it was built for.
    memory_query_intent = classify_memory_query_intent(user_message)
    corrected_memory_intent = memory_query_intent in (
        MemoryQueryIntent.CORRECTED_MEMORY_FACT,
        MemoryQueryIntent.CORRECTION_HISTORY,
    )
    prioritized_results = prioritize_corrected_memory_evidence(
        filtered_results,
        corrected_memory_intent=corrected_memory_intent,
    )
    log_event(
        _logger,
        logging.DEBUG,
        "chat_rag_evidence_prioritized",
        trace_id=get_request_id(),
        profile_id=profile_id,
        memory_query_intent=memory_query_intent.value,
        corrected_memory_intent=corrected_memory_intent,
        retrieved_count=len(retrieval_response.results),
        filtered_count=len(filtered_results),
        selected_count=len(prioritized_results),
        selected_chunk_ids=[result.chunk_id for result in prioritized_results],
    )
    return build_rag_evidence_items(prioritized_results)


@dataclass(frozen=True)
class _AsyncChatPrep:
    """Pure data handed across the await boundary (no ORM Session/objects)."""

    user_id: int
    profile_id: int
    conversation_id: str
    user_message_id: int
    user_message_content: str
    brain_user_message: str
    user_canonical_status: str
    canonical_language: str
    source_language: str
    display_language: str
    orchestrator_request: OrchestratorChatRequest
    ai_call_context: AiCallContext


async def send_chat_message_async(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    payload: ChatMessageCreate,
) -> ChatSendResponse:
    """Authenticated chat send with true-async Brain wait (Task 65.13.12).

    Redis admission is bridged off the event loop. SQLAlchemy/RAG stay on the
    request Session (same task; never shared across threads). The Session is
    idle only during the awaited Brain provider call — not AsyncSession.
    """

    plan = get_effective_plan_definition_for_user(current_user)
    rate_limit = resolve_user_chat_rate_limit(
        allow_unlimited_chat=plan.limits.allow_unlimited_chat
    )
    async with async_user_chat_admission(
        user_id=current_user.id,
        rate_limit_per_minute=rate_limit,
    ):
        return await _send_chat_message_admitted_async(
            db,
            current_user=current_user,
            profile_id=profile_id,
            payload=payload,
        )


async def _send_chat_message_admitted_async(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    payload: ChatMessageCreate,
) -> ChatSendResponse:
    prep = _prepare_chat_for_async_brain(
        db,
        current_user=current_user,
        profile_id=profile_id,
        payload=payload,
        trace_id=get_request_id(),
    )
    orchestrator = get_agent_orchestrator()
    try:
        async with async_brain_chat_admission():
            orchestrator_response, ai_action = await run_instrumented_single_attempt_action_async(
                db,
                context=prep.ai_call_context,
                step_type=AiStepType.PROVIDER_GENERATION,
                provider=settings.ai_brain_provider,
                model=settings.ai_brain_model,
                operation=lambda: orchestrator.generate_chat_response_async(
                    prep.orchestrator_request
                ),
                extract_token_usage=_extract_brain_token_usage,
            )
    except asyncio.CancelledError:
        observe_chat_async_cancellation()
        raise
    except Exception as exc:
        mapped = map_brain_provider_error(exc)
        if mapped is not None:
            raise mapped from exc
        raise

    return _finalize_chat_after_async_brain(
        db,
        prep=prep,
        orchestrator_response=orchestrator_response,
        ai_action_id=ai_action.id,
    )


def _prepare_chat_for_async_brain(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    payload: ChatMessageCreate,
    trace_id: str | None,
) -> _AsyncChatPrep:
    profile = _get_authorized_profile_or_raise(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )
    canonical_language = assert_canonical_memorial_language(profile.canonical_language)
    source_language = _resolve_user_source_language(
        message=payload.message,
        locale=payload.locale,
        preferred_ui_language=current_user.preferred_ui_language,
        canonical_language=canonical_language,
    )
    display_language = _resolve_display_language(
        source_language=source_language,
        locale=payload.locale,
        preferred_ui_language=current_user.preferred_ui_language,
        canonical_language=canonical_language,
    )
    recent_history = repository.list_recent_chat_messages_for_profile(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
        limit=RECENT_HISTORY_LIMIT,
    )
    profile_memories = memories_repository.list_memories_for_profile(
        db,
        user_id=profile.user_id,
        profile_id=profile_id,
    )
    active = active_session.get_or_create_active_session(
        db, user_id=current_user.id, profile_id=profile_id
    )
    conversation_id = active.conversation_id
    user_message = repository.create_chat_message(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
        role="user",
        content=payload.message,
        source_language=source_language,
        message_metadata={"source": "chat_api", "conversation_id": conversation_id},
    )
    db.flush()
    ensure_user_canonical_translation(
        db,
        profile=profile,
        message=user_message,
        source_language=source_language,
        actor=current_user,
    )
    db.flush()
    brain_user_message, user_canonical_status = resolve_user_canonical_text(
        db,
        profile=profile,
        message=user_message,
        actor=current_user,
        ensure_missing=False,
    )
    retrieved_evidence_items = _retrieve_rag_evidence_safely(
        db,
        current_user=current_user,
        profile_id=profile_id,
        user_message=brain_user_message,
    )
    grounded_context = build_grounded_context(
        profile=profile,
        memories=profile_memories,
        user_message=brain_user_message,
        retrieved_evidence_items=retrieved_evidence_items,
    )
    resolved_persona = resolve_avatar_persona(db, profile=profile)
    persona_section = (
        build_avatar_persona_section(resolved_persona) if resolved_persona.configured else None
    )
    history_entries = [
        _build_history_entry(
            db,
            message=message,
            profile=profile,
            actor=current_user,
        )
        for message in recent_history
    ]
    # Persist the user turn before awaiting Brain so a cancelled provider wait
    # does not lose the durable original message.
    db.commit()
    return _AsyncChatPrep(
        user_id=current_user.id,
        profile_id=profile_id,
        conversation_id=conversation_id,
        user_message_id=user_message.id,
        user_message_content=user_message.content,
        brain_user_message=brain_user_message,
        user_canonical_status=user_canonical_status,
        canonical_language=canonical_language,
        source_language=source_language,
        display_language=display_language,
        orchestrator_request=OrchestratorChatRequest(
            profile=_build_profile_context(profile),
            avatar_persona_section=persona_section,
            user_message=brain_user_message,
            recent_history=history_entries,
            grounded_context=grounded_context,
            response_language=canonical_language,
        ),
        ai_call_context=AiCallContext(
            feature=AiFeature.BRAIN_CHAT_RESPONSE,
            execution_source=ExecutionSource.FASTAPI,
            trace_id=trace_id,
            user_id=current_user.id,
            memorial_id=profile_id,
            message_id=user_message.id,
        ),
    )


def _finalize_chat_after_async_brain(
    db: Session,
    *,
    prep: _AsyncChatPrep,
    orchestrator_response: OrchestratorChatResponse,
    ai_action_id: int,
) -> ChatSendResponse:
    user = db.get(User, prep.user_id)
    profile = db.get(MemoryProfile, prep.profile_id)
    user_message = db.get(ChatMessage, prep.user_message_id)
    if user is None or profile is None or user_message is None:
        raise ChatProfileNotFoundError("Memory profile not found")

    assistant_message = repository.create_chat_message(
        db,
        user_id=prep.user_id,
        profile_id=prep.profile_id,
        role="assistant",
        content=orchestrator_response.text,
        source_language=None,
        message_metadata={
            "reply_to_message_id": user_message.id,
            "provider_name": orchestrator_response.provider_name,
            "ai_action_id": ai_action_id,
            "conversation_id": prep.conversation_id,
            "canonical_language": prep.canonical_language,
            "user_canonical_status": prep.user_canonical_status,
            "display_language": prep.display_language,
            **orchestrator_response.metadata,
        },
    )
    db.flush()
    display_row = ensure_assistant_display_translation(
        db,
        profile=profile,
        message=assistant_message,
        display_language=prep.display_language,
        actor=user,
    )
    db.flush()
    assistant_views = resolve_chat_message_views(
        db,
        message=assistant_message,
        profile=profile,
        viewer=user,
        display_locale=prep.display_language,
        ensure_missing=False,
    )
    metadata = dict(assistant_message.message_metadata or {})
    metadata["display_translation_status"] = assistant_views.display_translation_status
    metadata["display_translation_provider"] = getattr(display_row, "translation_provider", None)
    assistant_message.message_metadata = metadata
    db.commit()
    db.refresh(assistant_message)
    db.refresh(user_message)

    snapshot_assistant_content = assistant_views.display_text
    for message, snapshot_content in (
        (user_message, user_message.content),
        (assistant_message, snapshot_assistant_content),
    ):
        redis_snapshot.append_message(
            user_id=prep.user_id,
            profile_id=prep.profile_id,
            conversation_id=prep.conversation_id,
            message=SnapshotMessage(
                id=message.id,
                role=message.role,
                content=snapshot_content,
                created_at=message.created_at.isoformat(),
            ),
        )
    observe_chat_operation(operation="send", result="success")
    log_event(
        _logger,
        logging.INFO,
        "chat_active_loaded",
        profile_id=prep.profile_id,
        conversation_id=prep.conversation_id,
        message_count=2,
        canonical_language=prep.canonical_language,
        source_language=prep.source_language,
        display_language=assistant_views.display_language,
        user_canonical_status=prep.user_canonical_status,
        display_translation_status=assistant_views.display_translation_status,
    )
    return ChatSendResponse(
        message_id=assistant_message.id,
        profile_id=prep.profile_id,
        conversation_id=prep.conversation_id,
        user_message=user_message.content,
        user_message_language=prep.source_language,
        ai_response_text=assistant_views.display_text,
        ai_response_language=assistant_views.display_language,
        ai_response_translation_status=assistant_views.display_translation_status,
        audio_url=orchestrator_response.audio_url,
        video_url=orchestrator_response.video_url,
        created_at=assistant_message.created_at,
    )


def send_chat_message(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    payload: ChatMessageCreate,
) -> ChatSendResponse:
    profile = _get_authorized_profile_or_raise(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )
    plan = get_effective_plan_definition_for_user(current_user)
    rate_limit = resolve_user_chat_rate_limit(
        allow_unlimited_chat=plan.limits.allow_unlimited_chat
    )

    with user_chat_admission(user_id=current_user.id, rate_limit_per_minute=rate_limit):
        return _send_chat_message_admitted(
            db,
            current_user=current_user,
            profile=profile,
            profile_id=profile_id,
            payload=payload,
        )


def _send_chat_message_admitted(
    db: Session,
    *,
    current_user: User,
    profile: MemoryProfile,
    profile_id: int,
    payload: ChatMessageCreate,
) -> ChatSendResponse:
    canonical_language = assert_canonical_memorial_language(profile.canonical_language)
    source_language = _resolve_user_source_language(
        message=payload.message,
        locale=payload.locale,
        preferred_ui_language=current_user.preferred_ui_language,
        canonical_language=canonical_language,
    )
    display_language = _resolve_display_language(
        source_language=source_language,
        locale=payload.locale,
        preferred_ui_language=current_user.preferred_ui_language,
        canonical_language=canonical_language,
    )

    # Each member's conversation with the avatar is their own, so chat
    # history stays scoped by (current_user.id, profile_id). Canonical
    # memories, however, belong to the memorial itself (profile.user_id),
    # not to whichever member is currently chatting - a contributor/viewer
    # must see the same grounded memory context an owner would, not an
    # empty one because the rows were authored by a different account.
    recent_history = repository.list_recent_chat_messages_for_profile(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
        limit=RECENT_HISTORY_LIMIT,
    )
    profile_memories = memories_repository.list_memories_for_profile(
        db,
        user_id=profile.user_id,
        profile_id=profile_id,
    )

    active = active_session.get_or_create_active_session(db, user_id=current_user.id, profile_id=profile_id)
    conversation_id = active.conversation_id

    # Persist the durable original first so translation failure never loses it.
    user_message = repository.create_chat_message(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
        role="user",
        content=payload.message,
        source_language=source_language,
        message_metadata={"source": "chat_api", "conversation_id": conversation_id},
    )
    db.flush()

    ensure_user_canonical_translation(
        db,
        profile=profile,
        message=user_message,
        source_language=source_language,
        actor=current_user,
    )
    db.flush()
    brain_user_message, user_canonical_status = resolve_user_canonical_text(
        db,
        profile=profile,
        message=user_message,
        actor=current_user,
        ensure_missing=False,
    )

    retrieved_evidence_items = _retrieve_rag_evidence_safely(
        db,
        current_user=current_user,
        profile_id=profile_id,
        user_message=brain_user_message,
    )
    grounded_context = build_grounded_context(
        profile=profile,
        memories=profile_memories,
        user_message=brain_user_message,
        retrieved_evidence_items=retrieved_evidence_items,
    )

    orchestrator = get_agent_orchestrator()
    # Task 65.12: resolve canonical persona once per chat request and reuse
    # the typed result for the prompt section (no N+1).
    resolved_persona = resolve_avatar_persona(db, profile=profile)
    persona_section = (
        build_avatar_persona_section(resolved_persona) if resolved_persona.configured else None
    )
    # Task 65.13.5: Brain always generates in memorial canonical language.
    # Viewer language is applied only as a post-generation display translation.
    response_language = canonical_language
    ai_call_context = AiCallContext(
        feature=AiFeature.BRAIN_CHAT_RESPONSE,
        execution_source=ExecutionSource.FASTAPI,
        trace_id=get_request_id(),
        user_id=current_user.id,
        memorial_id=profile_id,
        message_id=user_message.id,
    )
    try:
        with brain_chat_admission():
            orchestrator_response, ai_action = run_instrumented_single_attempt_action(
                db,
                context=ai_call_context,
                step_type=AiStepType.PROVIDER_GENERATION,
                provider=settings.ai_brain_provider,
                model=settings.ai_brain_model,
                operation=lambda: orchestrator.generate_chat_response(
                    OrchestratorChatRequest(
                        profile=_build_profile_context(profile),
                        avatar_persona_section=persona_section,
                        user_message=brain_user_message,
                        recent_history=[
                            _build_history_entry(
                                db,
                                message=message,
                                profile=profile,
                                actor=current_user,
                            )
                            for message in recent_history
                        ],
                        grounded_context=grounded_context,
                        response_language=response_language,
                    )
                ),
                extract_token_usage=_extract_brain_token_usage,
            )
    except Exception as exc:
        mapped = map_brain_provider_error(exc)
        if mapped is not None:
            raise mapped from exc
        raise

    assistant_message = repository.create_chat_message(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
        role="assistant",
        content=orchestrator_response.text,
        source_language=None,
        message_metadata={
            "reply_to_message_id": user_message.id,
            "provider_name": orchestrator_response.provider_name,
            "ai_action_id": ai_action.id,
            "conversation_id": conversation_id,
            "canonical_language": canonical_language,
            "user_canonical_status": user_canonical_status,
            "display_language": display_language,
            **orchestrator_response.metadata,
        },
    )
    db.flush()

    display_row = ensure_assistant_display_translation(
        db,
        profile=profile,
        message=assistant_message,
        display_language=display_language,
        actor=current_user,
    )
    db.flush()
    assistant_views = resolve_chat_message_views(
        db,
        message=assistant_message,
        profile=profile,
        viewer=current_user,
        display_locale=display_language,
        ensure_missing=False,
    )
    # Keep metadata diagnosable without blocking on translation.
    metadata = dict(assistant_message.message_metadata or {})
    metadata["display_translation_status"] = assistant_views.display_translation_status
    metadata["display_translation_provider"] = getattr(display_row, "translation_provider", None)
    assistant_message.message_metadata = metadata

    db.commit()
    db.refresh(assistant_message)
    db.refresh(user_message)

    snapshot_assistant_content = assistant_views.display_text
    for message, snapshot_content in (
        (user_message, user_message.content),
        (assistant_message, snapshot_assistant_content),
    ):
        redis_snapshot.append_message(
            user_id=current_user.id,
            profile_id=profile_id,
            conversation_id=conversation_id,
            message=SnapshotMessage(
                id=message.id,
                role=message.role,
                content=snapshot_content,
                created_at=message.created_at.isoformat(),
            ),
        )
    observe_chat_operation(operation="send", result="success")
    log_event(
        _logger,
        logging.INFO,
        "chat_active_loaded",
        profile_id=profile_id,
        conversation_id=conversation_id,
        message_count=2,
        canonical_language=canonical_language,
        source_language=source_language,
        display_language=assistant_views.display_language,
        user_canonical_status=user_canonical_status,
        display_translation_status=assistant_views.display_translation_status,
    )

    return ChatSendResponse(
        message_id=assistant_message.id,
        profile_id=profile_id,
        conversation_id=conversation_id,
        user_message=user_message.content,
        user_message_language=source_language,
        ai_response_text=assistant_views.display_text,
        ai_response_language=assistant_views.display_language,
        ai_response_translation_status=assistant_views.display_translation_status,
        audio_url=orchestrator_response.audio_url,
        video_url=orchestrator_response.video_url,
        created_at=assistant_message.created_at,
    )


def list_chat_messages(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
) -> list[ChatMessageRead]:
    profile = _get_authorized_profile_or_raise(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )
    messages = repository.list_chat_messages_for_profile(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
    )
    return [
        _build_message_read(
            db,
            message=message,
            profile=profile,
            viewer=current_user,
            ensure_missing=True,
        )
        for message in messages
    ]


def _messages_for_conversation(
    db: Session, *, user_id: int, profile_id: int, conversation_id: str
) -> list[ChatMessage]:
    all_messages = repository.list_chat_messages_for_profile(db, user_id=user_id, profile_id=profile_id)
    return [
        message
        for message in all_messages
        if isinstance(message.message_metadata, dict)
        and message.message_metadata.get("conversation_id") == conversation_id
    ]


def get_active_chat(db: Session, *, current_user: User, profile_id: int) -> ChatActiveRead:
    """Restores the active conversation's transcript (Part E.30/33): tries
    the Redis fast-path snapshot first; on a miss or mismatch (different
    `conversation_id`, e.g. after a Redis restart), rebuilds it from the
    durable Postgres record and re-writes the Redis snapshot so the next
    restore is fast again. Never silently loses messages - a genuinely
    empty conversation (brand new, or just reset) returns an empty list,
    not an error."""

    profile = _get_authorized_profile_or_raise(db, current_user=current_user, profile_id=profile_id)
    active = active_session.get_or_create_active_session(db, user_id=current_user.id, profile_id=profile_id)

    snapshot = redis_snapshot.read_snapshot(user_id=current_user.id, profile_id=profile_id)
    if snapshot is not None and snapshot.conversation_id == active.conversation_id:
        log_event(
            _logger,
            logging.INFO,
            "chat_redis_snapshot_restored",
            profile_id=profile_id,
            conversation_id=active.conversation_id,
            message_count=len(snapshot.messages),
        )
        messages = [
            ChatMessageRead(
                id=m.id,
                profile_id=profile_id,
                role=m.role,
                content=m.content,
                created_at=m.created_at,
            )
            for m in snapshot.messages
        ]
        return ChatActiveRead(
            profile_id=profile_id,
            conversation_id=active.conversation_id,
            messages=messages,
            restored_from="redis",
        )

    db_messages = _messages_for_conversation(
        db, user_id=current_user.id, profile_id=profile_id, conversation_id=active.conversation_id
    )
    read_messages = [
        _build_message_read(
            db,
            message=m,
            profile=profile,
            viewer=current_user,
            ensure_missing=True,
        )
        for m in db_messages
    ]
    rebuilt = ChatSnapshot(
        conversation_id=active.conversation_id,
        profile_id=profile_id,
        locale=None,
        messages=[
            SnapshotMessage(
                id=m.id,
                role=m.role,
                content=read.content,
                created_at=m.created_at.isoformat(),
            )
            for m, read in zip(db_messages, read_messages, strict=True)
        ],
    )
    redis_snapshot.write_snapshot(user_id=current_user.id, profile_id=profile_id, snapshot=rebuilt)
    log_event(
        _logger,
        logging.INFO,
        "chat_redis_snapshot_rebuilt",
        profile_id=profile_id,
        conversation_id=active.conversation_id,
        message_count=len(db_messages),
    )
    observe_chat_operation(operation="restore", result="success")
    return ChatActiveRead(
        profile_id=profile_id,
        conversation_id=active.conversation_id,
        messages=read_messages,
        restored_from="database" if db_messages else "empty",
    )


def reset_chat(db: Session, *, current_user: User, profile_id: int) -> ChatActiveRead:
    """Chat reset (Part E.34): rotates the active-session pointer to a
    brand-new `conversation_id` and clears the Redis snapshot. Prior
    messages are never deleted - they simply stop being part of the active
    conversation (still reachable via `GET .../messages`' full history if
    ever needed). Returns the new, empty active conversation."""

    _get_authorized_profile_or_raise(db, current_user=current_user, profile_id=profile_id)
    log_event(_logger, logging.INFO, "chat_reset_started", profile_id=profile_id)
    try:
        new_session = active_session.rotate_active_session(db, user_id=current_user.id, profile_id=profile_id)
        db.commit()
        db.refresh(new_session)
        redis_snapshot.delete_snapshot(user_id=current_user.id, profile_id=profile_id)
    except Exception:
        db.rollback()
        log_event(_logger, logging.ERROR, "chat_reset_failed", profile_id=profile_id)
        observe_chat_operation(operation="reset", result="error")
        raise
    log_event(
        _logger, logging.INFO, "chat_reset_succeeded", profile_id=profile_id, conversation_id=new_session.conversation_id
    )
    observe_chat_operation(operation="reset", result="success")
    return ChatActiveRead(
        profile_id=profile_id,
        conversation_id=new_session.conversation_id,
        messages=[],
        restored_from="empty",
    )
