from __future__ import annotations

from sqlalchemy.orm import Session

from app.modules.ai_agents.brain.context import build_grounded_context, build_rag_evidence_items
from app.db.models import ChatMessage, User
from app.modules.ai_agents import get_agent_orchestrator
from app.modules.ai_agents.schemas import (
    ChatHistoryEntry,
    MemoryProfileContext,
    OrchestratorChatRequest,
)
from app.modules.chat import repository
from app.modules.chat.schemas import ChatMessageCreate, ChatMessageRead, ChatSendResponse
from app.modules.memories import repository as memories_repository
from app.modules.memory_profiles import repository as memory_profiles_repository
from app.modules.qdrant_indexing.exceptions import QdrantClientError, QdrantCollectionConfigurationError
from app.modules.rag_retrieval.exceptions import (
    RagRetrievalDisabledError,
    RagRetrievalModelUnavailableError,
    RagRetrievalProfileNotFoundError,
)
from app.modules.rag_retrieval.schemas import RagRetrievalRequest
from app.modules.rag_retrieval.service import retrieve_profile_rag


RECENT_HISTORY_LIMIT = 10


class ChatProfileNotFoundError(Exception):
    pass


def _get_owned_profile_or_raise(
    db: Session,
    *,
    user_id: int,
    profile_id: int,
):
    profile = memory_profiles_repository.get_memory_profile_for_user(
        db,
        user_id=user_id,
        profile_id=profile_id,
    )
    if profile is None:
        raise ChatProfileNotFoundError("Memory profile not found")

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

    return build_rag_evidence_items(retrieval_response.results)


def send_chat_message(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    payload: ChatMessageCreate,
) -> ChatSendResponse:
    profile = _get_owned_profile_or_raise(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
    )
    recent_history = repository.list_recent_chat_messages_for_profile(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
        limit=RECENT_HISTORY_LIMIT,
    )
    profile_memories = memories_repository.list_memories_for_profile(
        db,
        user_id=current_user.id,
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

    user_message = repository.create_chat_message(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
        role="user",
        content=payload.message,
        message_metadata={"source": "chat_api"},
    )
    db.flush()

    orchestrator = get_agent_orchestrator()
    orchestrator_response = orchestrator.generate_chat_response(
        OrchestratorChatRequest(
            profile=_build_profile_context(profile),
            user_message=payload.message,
            recent_history=[
                _build_history_entry(message) for message in recent_history
            ],
            grounded_context=grounded_context,
        )
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
            **orchestrator_response.metadata,
        },
    )
    db.commit()
    db.refresh(assistant_message)

    return ChatSendResponse(
        message_id=assistant_message.id,
        profile_id=profile_id,
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
    _get_owned_profile_or_raise(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
    )
    messages = repository.list_chat_messages_for_profile(
        db,
        user_id=current_user.id,
        profile_id=profile_id,
    )
    return [_build_message_read(message) for message in messages]
