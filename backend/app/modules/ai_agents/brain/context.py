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
    # Populated only for owner-approved learned memories indexed through the
    # explicit avatar-memory-promotion pipeline (Task 64.2). These fields let
    # the prompt distinguish a verified, first-person learned memory from an
    # ordinary archival document chunk, and let it order conflicting learned
    # memories about the same topic by recency. They are None for regular
    # archival RAG chunks.
    memory_status: str | None = None
    memory_provenance: str | None = None
    promotion_id: int | None = None
    candidate_id: int | None = None
    indexed_at: str | None = None


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


_LEARNED_MEMORY_SOURCE_TYPE = "conversation_candidate"
_LEARNED_MEMORY_VERIFIED_STATUS = "verified"


def _coerce_int(value: object) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str) and value.strip().isdigit():
        return int(value)
    return None


def _coerce_str(value: object) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def build_rag_evidence_items(results: list) -> list[BrainRagEvidence]:
    rag_evidence_items: list[BrainRagEvidence] = []
    for result in results:
        payload_metadata: dict = getattr(result, "payload_metadata", None) or {}
        is_learned_memory = result.source_type == _LEARNED_MEMORY_SOURCE_TYPE
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
                memory_status=_coerce_str(payload_metadata.get("memory_status")) if is_learned_memory else None,
                memory_provenance=_coerce_str(payload_metadata.get("provenance")) if is_learned_memory else None,
                promotion_id=_coerce_int(payload_metadata.get("promotion_id")) if is_learned_memory else None,
                candidate_id=_coerce_int(payload_metadata.get("candidate_id")) if is_learned_memory else None,
                indexed_at=_coerce_str(payload_metadata.get("indexed_at")) if is_learned_memory else None,
            )
        )

    return rag_evidence_items


# A verified learned memory is "dispute-shaped" when its own text attributes
# two or more distinct quoted alternatives (e.g. two candidate song titles) —
# a content-agnostic structural signal, not tied to any specific fact.
_QUOTE_CHARACTERS = "«»\"'"
_DISPUTE_QUOTE_PATTERN_MIN_COUNT = 2

# Generic Russian phrasing that signals the user is asking about a
# disagreement, differing recollections, or "what would you say if we
# remember it differently" — as opposed to an ordinary direct factual
# question or a question about a past correction (a past correction expects
# the single settled answer, not a live disagreement; see prompt_builder's
# LEARNED MEMORY rules). This list is about question *shape*, not about any
# specific fact, so it generalizes across profiles and topics.
_DISAGREEMENT_QUESTION_MARKERS = (
    "по-разному",
    "по разному",
    "различ",
    "каждый по-своему",
    "каждый по своему",
    "кто из нас прав",
    "что ты скажешь если",
    "что скажешь если",
)


def _is_dispute_shaped_learned_memory(result) -> bool:
    if getattr(result, "source_type", None) != _LEARNED_MEMORY_SOURCE_TYPE:
        return False
    payload_metadata: dict = getattr(result, "payload_metadata", None) or {}
    if payload_metadata.get("memory_status") != _LEARNED_MEMORY_VERIFIED_STATUS:
        return False
    text = getattr(result, "text", "") or ""
    quote_count = sum(text.count(char) for char in _QUOTE_CHARACTERS)
    # Each quoted phrase contributes an opening and closing character, so two
    # distinct quoted alternatives show up as at least four quote characters.
    return quote_count >= _DISPUTE_QUOTE_PATTERN_MIN_COUNT * 2


def _question_asks_about_disagreement(user_message: str) -> bool:
    normalized_message = " ".join(user_message.casefold().split())
    return any(marker in normalized_message for marker in _DISAGREEMENT_QUESTION_MARKERS)


# Bounded evidence count used for corrected-memory-intent turns once a
# verified learned memory has been floated to the front — small enough to
# meaningfully cut dilution from unrelated archival items, large enough to
# still give the Brain real context. Not a change to the profile's
# configured top_k; only the count of items forwarded into the prompt for
# this one intent path.
CORRECTED_MEMORY_EVIDENCE_CAP = 3


def _is_verified_learned_memory_result(result) -> bool:
    payload_metadata: dict = getattr(result, "payload_metadata", None) or {}
    return (
        getattr(result, "source_type", None) == _LEARNED_MEMORY_SOURCE_TYPE
        and payload_metadata.get("memory_status") == _LEARNED_MEMORY_VERIFIED_STATUS
    )


def prioritize_corrected_memory_evidence(results: list, *, limit: int = CORRECTED_MEMORY_EVIDENCE_CAP) -> list:
    """Deterministically float verified learned-memory items to the front of
    an already-retrieved, already-filtered evidence list and cap the total
    count sent to the Brain.

    Scoped to corrected-memory-intent turns (see
    app.modules.demo_fa_chat.service). This does not change retrieval
    scoring — it only reorders and trims the candidate pool the Brain
    receives, addressing measured cases where a correctly retrieved and
    correctly tagged verified item was inconsistently used by the Brain when
    outnumbered by several unrelated archival items in the same evidence
    block (see Task 64.4.2 diagnostics).
    """
    verified_first = [result for result in results if _is_verified_learned_memory_result(result)]
    rest = [result for result in results if not _is_verified_learned_memory_result(result)]
    return [*verified_first, *rest][:limit]


def filter_learned_memory_results_by_question_intent(results: list, *, user_message: str) -> list:
    """Drop dispute-shaped verified learned memories unless the current
    question is itself asking about a disagreement.

    `results` is the raw retrieval result list (duck-typed: each item needs
    `.source_type`, `.text`, and `.payload_metadata`, e.g. RagRetrievalResultRead).
    This is a downstream evidence-packaging decision over items Qdrant already
    returned for this turn — it does not change retrieval, ranking, or top_k.
    Without it, a verified memory that records "person A remembers X, person B
    remembers Y" would be shown to the Brain (and could leak into the answer)
    even for an unrelated plain factual question that should get a single
    confident answer from a different verified item. Applying the filter once,
    upstream of both the Brain prompt and the debug evidence list, keeps what
    the Brain sees and what is shown to the caller consistent.
    """
    if _question_asks_about_disagreement(user_message):
        return results
    return [result for result in results if not _is_dispute_shaped_learned_memory(result)]
