from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import ConversationMemoryCandidate


def create_conversation_memory_candidate(
    db: Session,
    *,
    owner_user_id: int,
    avatar_id: str,
    profile_id: int | None,
    conversation_id: str | None,
    trace_id: str | None,
    source: str,
    status: str,
    confidence: str,
    user_message_excerpt: str,
    proposed_memory_text: str,
    reason: str,
    language: str | None,
    memory_type: str,
    enrichment_status: str,
    finalized_memory_text: str | None,
    privacy_scope: str,
    dispute_status: str,
    unresolved_clarification_count: int,
    workflow_version: int,
) -> ConversationMemoryCandidate:
    candidate = ConversationMemoryCandidate(
        owner_user_id=owner_user_id,
        avatar_id=avatar_id,
        profile_id=profile_id,
        conversation_id=conversation_id,
        trace_id=trace_id,
        source=source,
        status=status,
        confidence=confidence,
        user_message_excerpt=user_message_excerpt,
        proposed_memory_text=proposed_memory_text,
        reason=reason,
        language=language,
        memory_type=memory_type,
        enrichment_status=enrichment_status,
        finalized_memory_text=finalized_memory_text,
        privacy_scope=privacy_scope,
        dispute_status=dispute_status,
        unresolved_clarification_count=unresolved_clarification_count,
        workflow_version=workflow_version,
    )
    db.add(candidate)
    return candidate


def list_conversation_memory_candidates(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int | None = None,
    avatar_id: str | None = None,
) -> list[ConversationMemoryCandidate]:
    statement = select(ConversationMemoryCandidate).where(
        ConversationMemoryCandidate.owner_user_id == owner_user_id,
    )
    if profile_id is not None:
        statement = statement.where(ConversationMemoryCandidate.profile_id == profile_id)
    if avatar_id is not None:
        statement = statement.where(ConversationMemoryCandidate.avatar_id == avatar_id)

    statement = statement.order_by(
        ConversationMemoryCandidate.created_at.desc(),
        ConversationMemoryCandidate.id.desc(),
    )
    return list(db.scalars(statement))


def get_conversation_memory_candidate_for_owner(
    db: Session,
    *,
    owner_user_id: int,
    candidate_id: int,
) -> ConversationMemoryCandidate | None:
    statement = select(ConversationMemoryCandidate).where(
        ConversationMemoryCandidate.id == candidate_id,
        ConversationMemoryCandidate.owner_user_id == owner_user_id,
    )
    return db.scalar(statement)
