from __future__ import annotations

import re
import unicodedata
from datetime import date, datetime

from pydantic import BaseModel, Field

from app.core.config import settings


MAX_MEMORY_EVIDENCE_ITEMS = 10
MAX_CONTENT_PREVIEW_LENGTH = 240
MIN_UNICODE_TOKEN_LENGTH = 2
ABSOLUTE_FILESYSTEM_PATH_PATTERN = re.compile(r"([A-Za-z]:\\[^\s]+|/app/[^\s]+)")


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


class BrainRagEvidence(BaseModel):
    source_type: str = "rag_chunk"
    chunk_id: int
    source_id: int
    embedding_id: int
    score: float
    language: str | None = None
    source_document_type: str
    validation_status: str
    text_hash: str
    content_preview: str


class BrainGroundedContext(BaseModel):
    profile_context: BrainProfileContext
    evidence_items: list[BrainMemoryEvidence] = Field(default_factory=list)
    retrieved_evidence_items: list[BrainRagEvidence] = Field(default_factory=list)


def _sanitize_prompt_text(value: str | None) -> str | None:
    if value is None:
        return None

    normalized_value = " ".join(value.split())
    sanitized_value = ABSOLUTE_FILESYSTEM_PATH_PATTERN.sub("[path omitted]", normalized_value)
    return sanitized_value or None


def _build_content_preview(
    content: str | None,
    *,
    max_length: int = MAX_CONTENT_PREVIEW_LENGTH,
) -> str | None:
    sanitized_content = _sanitize_prompt_text(content)
    if sanitized_content is None:
        return None

    if len(sanitized_content) <= max_length:
        return sanitized_content

    return f"{sanitized_content[: max_length - 3].rstrip()}..."


def _build_memory_content_preview(content: str | None) -> str | None:
    return _build_content_preview(
        content,
        max_length=settings.ai_brain_memory_evidence_preview_length,
    )


def _build_rag_content_preview(content: str | None) -> str | None:
    return _build_content_preview(
        content,
        max_length=settings.ai_brain_rag_evidence_preview_length,
    )


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


def _normalize_unicode_text(value: str) -> str:
    return unicodedata.normalize("NFKC", value).casefold()


def _extract_unicode_tokens(
    text: str,
    *,
    min_length: int = MIN_UNICODE_TOKEN_LENGTH,
) -> set[str]:
    normalized_text = _normalize_unicode_text(text)
    tokens: list[str] = []
    current_token: list[str] = []

    for character in normalized_text:
        if unicodedata.category(character)[0] in {"L", "N"}:
            current_token.append(character)
            continue

        if len(current_token) >= min_length:
            tokens.append("".join(current_token))
        current_token = []

    if len(current_token) >= min_length:
        tokens.append("".join(current_token))

    return set(tokens)


def _extract_query_tokens(user_message: str) -> set[str]:
    return _extract_unicode_tokens(user_message)


def _build_memory_search_text(memory) -> str:
    searchable_chunks = [memory.title, memory.content]
    return " ".join(chunk for chunk in searchable_chunks if chunk)


def _count_keyword_overlap(user_message_tokens: set[str], memory) -> int:
    if not user_message_tokens:
        return 0

    memory_tokens = _extract_unicode_tokens(_build_memory_search_text(memory))
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
                content_preview=_build_memory_content_preview(memory.content),
                selection_reason=f"keyword_overlap:{overlap_count}",
            )
            for overlap_count, memory in selected_memories
        ]

    return []


def build_vector_retrieval_grounded_context(
    *,
    profile,
    retrieved_evidence_items: list[BrainRagEvidence] | None = None,
) -> BrainGroundedContext:
    return BrainGroundedContext(
        profile_context=build_brain_profile_context(profile),
        evidence_items=[],
        retrieved_evidence_items=retrieved_evidence_items or [],
    )


def build_grounded_context(
    *,
    profile,
    memories: list,
    user_message: str,
    retrieved_evidence_items: list[BrainRagEvidence] | None = None,
) -> BrainGroundedContext:
    return BrainGroundedContext(
        profile_context=build_brain_profile_context(profile),
        evidence_items=select_memory_evidence(
            memories=memories,
            user_message=user_message,
        ),
        retrieved_evidence_items=retrieved_evidence_items or [],
    )


def build_rag_evidence_items(results: list) -> list[BrainRagEvidence]:
    rag_evidence_items: list[BrainRagEvidence] = []
    for result in results:
        rag_evidence_items.append(
            BrainRagEvidence(
                chunk_id=result.chunk_id,
                source_id=result.source_id,
                embedding_id=result.embedding_id,
                score=float(result.score),
                language=result.language,
                source_document_type=result.source_type,
                validation_status=result.validation_status,
                text_hash=result.text_hash,
                content_preview=_build_rag_content_preview(result.text) or "",
            )
        )

    return rag_evidence_items
