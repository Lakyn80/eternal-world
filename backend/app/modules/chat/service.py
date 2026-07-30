from __future__ import annotations

import logging

from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logging import get_logger, get_request_id, log_event
from app.core.metrics import observe_chat_operation
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
from app.modules.avatar_persona.settings_service import (
    build_avatar_persona_section,
    resolve_avatar_persona,
    select_response_language,
)
from app.db.models import ChatMessage, MemoryProfile, User
from app.modules.ai_agents import get_agent_orchestrator
from app.modules.ai_agents.schemas import (
    ChatHistoryEntry,
    MemoryProfileContext,
    OrchestratorChatRequest,
)
from app.modules.chat import active_session, redis_snapshot, repository
from app.modules.chat.redis_snapshot import ChatSnapshot, SnapshotMessage
from app.modules.chat.schemas import ChatActiveRead, ChatMessageCreate, ChatMessageRead, ChatSendResponse
from app.modules.memories import repository as memories_repository
from app.modules.memorial_access.capabilities import MemorialCapability, resolve_authorized_profile
from app.modules.memorial_access.service import MemorialForbiddenError, MemorialNotFoundError
from app.modules.provider_usage.context import AiCallContext
from app.modules.provider_usage.enums import AiFeature, AiStepType, ExecutionSource
from app.modules.provider_usage.service import run_instrumented_single_attempt_action
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


def _build_history_entry(message: ChatMessage) -> ChatHistoryEntry:
    return ChatHistoryEntry(
        role=message.role,
        content=message.content,
        created_at=message.created_at,
    )


def _build_message_read(message: ChatMessage) -> ChatMessageRead:
    return ChatMessageRead(
        id=message.id,
        profile_id=message.memory_profile_id,
        role=message.role,
        content=message.content,
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
    retrieved_evidence_items = _retrieve_rag_evidence_safely(
        db,
        current_user=current_user,
        profile_id=profile_id,
        user_message=payload.message,
    )
    grounded_context = build_grounded_context(
        profile=profile,
        memories=profile_memories,
        user_message=payload.message,
        retrieved_evidence_items=retrieved_evidence_items,
    )

    active = active_session.get_or_create_active_session(db, user_id=current_user.id, profile_id=profile_id)
    conversation_id = active.conversation_id

    user_message = repository.create_chat_message(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
        role="user",
        content=payload.message,
        message_metadata={"source": "chat_api", "conversation_id": conversation_id},
    )
    db.flush()

    orchestrator = get_agent_orchestrator()
    # Task 65.12: resolve canonical persona once per chat request and reuse
    # the typed result for prompt section + language selection (no N+1).
    resolved_persona = resolve_avatar_persona(db, profile=profile)
    persona_section = (
        build_avatar_persona_section(resolved_persona) if resolved_persona.configured else None
    )
    # Preserve pre-65.12 language behavior when persona settings were never saved:
    # ``response_language=None`` keeps "match the user message" instructions.
    response_language = (
        select_response_language(
            resolved_persona,
            detected_language=None,
            explicit_supported_language=None,
        )
        if resolved_persona.configured
        else None
    )
    ai_call_context = AiCallContext(
        feature=AiFeature.BRAIN_CHAT_RESPONSE,
        execution_source=ExecutionSource.FASTAPI,
        trace_id=get_request_id(),
        user_id=current_user.id,
        memorial_id=profile_id,
        message_id=user_message.id,
    )
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
                user_message=payload.message,
                recent_history=[
                    _build_history_entry(message) for message in recent_history
                ],
                grounded_context=grounded_context,
                response_language=response_language,
            )
        ),
        extract_token_usage=_extract_brain_token_usage,
    )

    assistant_message = repository.create_chat_message(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
        role="assistant",
        content=orchestrator_response.text,
        message_metadata={
            "reply_to_message_id": user_message.id,
            "provider_name": orchestrator_response.provider_name,
            "ai_action_id": ai_action.id,
            "conversation_id": conversation_id,
            **orchestrator_response.metadata,
        },
    )
    db.commit()
    db.refresh(assistant_message)
    db.refresh(user_message)

    for message in (user_message, assistant_message):
        redis_snapshot.append_message(
            user_id=current_user.id,
            profile_id=profile_id,
            conversation_id=conversation_id,
            message=SnapshotMessage(
                id=message.id,
                role=message.role,
                content=message.content,
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
    )

    return ChatSendResponse(
        message_id=assistant_message.id,
        profile_id=profile_id,
        conversation_id=conversation_id,
        user_message=user_message.content,
        ai_response_text=assistant_message.content,
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
    _get_authorized_profile_or_raise(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )
    messages = repository.list_chat_messages_for_profile(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
    )
    return [_build_message_read(message) for message in messages]


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

    _get_authorized_profile_or_raise(db, current_user=current_user, profile_id=profile_id)
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
            ChatMessageRead(id=m.id, profile_id=profile_id, role=m.role, content=m.content, created_at=m.created_at)
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
    rebuilt = ChatSnapshot(
        conversation_id=active.conversation_id,
        profile_id=profile_id,
        locale=None,
        messages=[
            SnapshotMessage(id=m.id, role=m.role, content=m.content, created_at=m.created_at.isoformat())
            for m in db_messages
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
        messages=[_build_message_read(m) for m in db_messages],
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
