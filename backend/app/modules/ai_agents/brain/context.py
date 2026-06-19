from __future__ import annotations

import re
from datetime import date, datetime

from pydantic import BaseModel, Field


MAX_MEMORY_EVIDENCE_ITEMS = 10
MAX_CONTENT_PREVIEW_LENGTH = 240
ABSOLUTE_FILESYSTEM_PATH_PATTERN = re.compile(r"([A-Za-z]:\\[^\s]+|/app/[^\s]+)")
QUERY_TOKEN_PATTERN = re.compile(r"[A-Za-z0-9]{2,}")


class BrainProfileContext(BaseModel):
    profile_id: int
    name: str
    birth_date: date | None = None
    death_date: date | None = None
    biography: str | None = None
    personality: str | None = None
    catchphrases: str | None = None


class BrainMemoryEvidence(BaseModel):
    source_type: str = "memory"
    source_id: int
    title: str
    memory_type: str
    occurred_at: datetime | None = None
    occurred_year: int | None = None
    content_preview: str | None = None
    selection_reason: str


class BrainGroundedContext(BaseModel):
    profile_context: BrainProfileContext
    evidence_items: list[BrainMemoryEvidence] = Field(default_factory=list)


def _sanitize_prompt_text(value: str | None) -> str | None:
    if value is None:
        return None

    normalized_value = " ".join(value.split())
    sanitized_value = ABSOLUTE_FILESYSTEM_PATH_PATTERN.sub("[path omitted]", normalized_value)
    return sanitized_value or None


def _build_content_preview(content: str | None) -> str | None:
    sanitized_content = _sanitize_prompt_text(content)
    if sanitized_content is None:
        return None

    if len(sanitized_content) <= MAX_CONTENT_PREVIEW_LENGTH:
        return sanitized_content

    return f"{sanitized_content[: MAX_CONTENT_PREVIEW_LENGTH - 3].rstrip()}..."


def build_brain_profile_context(profile) -> BrainProfileContext:
    return BrainProfileContext(
        profile_id=profile.id,
        name=_sanitize_prompt_text(profile.name) or "Unknown",
        birth_date=profile.birth_date,
        death_date=profile.death_date,
        biography=_sanitize_prompt_text(profile.biography),
        personality=_sanitize_prompt_text(profile.personality),
        catchphrases=_sanitize_prompt_text(profile.catchphrases),
    )


def _extract_query_tokens(user_message: str) -> set[str]:
    return {token.lower() for token in QUERY_TOKEN_PATTERN.findall(user_message)}


def _build_memory_search_text(memory) -> str:
    searchable_chunks = [memory.title, memory.content]
    return " ".join(chunk for chunk in searchable_chunks if chunk)


def _count_keyword_overlap(user_message_tokens: set[str], memory) -> int:
    if not user_message_tokens:
        return 0

    memory_tokens = {
        token.lower()
        for token in QUERY_TOKEN_PATTERN.findall(_build_memory_search_text(memory))
    }
    return len(user_message_tokens & memory_tokens)


def select_memory_evidence(
    *,
    memories: list,
    user_message: str,
    limit: int = MAX_MEMORY_EVIDENCE_ITEMS,
) -> list[BrainMemoryEvidence]:
    query_tokens = _extract_query_tokens(user_message)
    ranked_memories: list[tuple[int, object]] = []

    for memory in memories:
        overlap_count = _count_keyword_overlap(query_tokens, memory)
        if overlap_count > 0:
            ranked_memories.append((overlap_count, memory))

    if ranked_memories:
        ranked_memories.sort(key=lambda item: item[0], reverse=True)
        selected_memories = ranked_memories[:limit]
        return [
            BrainMemoryEvidence(
                source_id=memory.id,
                title=_sanitize_prompt_text(memory.title) or "Untitled memory",
                memory_type=memory.memory_type,
                occurred_at=memory.occurred_at,
                occurred_year=memory.occurred_year,
                content_preview=_build_content_preview(memory.content),
                selection_reason=f"keyword_overlap:{overlap_count}",
            )
            for overlap_count, memory in selected_memories
        ]

    fallback_memories = memories[:limit]
    return [
        BrainMemoryEvidence(
            source_id=memory.id,
            title=_sanitize_prompt_text(memory.title) or "Untitled memory",
            memory_type=memory.memory_type,
            occurred_at=memory.occurred_at,
            occurred_year=memory.occurred_year,
            content_preview=_build_content_preview(memory.content),
            selection_reason="latest_timeline_fallback",
        )
        for memory in fallback_memories
    ]


def build_grounded_context(
    *,
    profile,
    memories: list,
    user_message: str,
) -> BrainGroundedContext:
    return BrainGroundedContext(
        profile_context=build_brain_profile_context(profile),
        evidence_items=select_memory_evidence(
            memories=memories,
            user_message=user_message,
        ),
    )
