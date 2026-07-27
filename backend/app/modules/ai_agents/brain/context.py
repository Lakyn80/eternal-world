from __future__ import annotations

import re
import unicodedata
from datetime import date, datetime

from pydantic import BaseModel, Field

from app.core.config import settings
from app.core.metrics import (
    observe_evidence_prioritization_dropped,
    observe_evidence_prioritization_pool,
    observe_evidence_prioritization_selected_item,
)


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


# Task 65.10 (Part D pipeline audit): every RagSource-backed indexing
# pipeline that stamps `payload_metadata["memory_status"] == "verified"` only
# after an explicit, server-controlled owner/family review-and-approval
# workflow (never from user-supplied input):
#   - "conversation_candidate": app.modules.avatar_memory_indexing, writing
#     from an approved AvatarMemoryPromotion (owner-confirmed conversation
#     candidate memory).
#   - "manual_text": app.modules.memorial_contribution_indexing, writing from
#     an approved+current MemorialContributionPromotion (family/owner
#     memorial contribution reviewed by the memorial owner).
#   - "biography": app.modules.biography_ingestion, writing from the
#     memorial owner's own confirmed profile biography text.
# A RagSource created directly through app.modules.rag_sources (document_text,
# letter, diary, chat_export, audio_transcript, video_transcript,
# timeline_memory, other) is embedded by the generic
# app.modules.qdrant_indexing pipeline, which never stamps `memory_status` at
# all - such evidence is correctly treated as ordinary archival material, not
# verified learned memory, regardless of this set. Adding a future verified
# pipeline means adding its source_type here once (and nowhere else) rather
# than growing a chain of per-call-site special cases.
VERIFIED_EVIDENCE_SOURCE_TYPES = frozenset({"conversation_candidate", "manual_text", "biography"})

# Retained for the content-shape "dispute detection" heuristic below, which is
# deliberately scoped to the conversation-candidate review workflow only (see
# `_is_dispute_shaped_learned_memory`) - not broadened by this task, since
# memorial-contribution and biography text are not produced through the same
# family-disagreement review flow and generalizing that heuristic to them is
# unproven and out of this task's scope.
_LEARNED_MEMORY_SOURCE_TYPE = "conversation_candidate"
_LEARNED_MEMORY_VERIFIED_STATUS = "verified"

# Task 65.10 (Part E/G): bounded, pipeline-neutral verification advantage
# added to an eligible item's raw relevance score before ranking. Small
# enough that a barely-relevant verified item cannot outrank a clearly more
# relevant item from any pipeline (verified or not) - it only breaks close
# ties and rewards a modest relevance gap, it never substitutes for
# relevance. Not a per-pipeline constant: it applies identically to every
# source_type in VERIFIED_EVIDENCE_SOURCE_TYPES.
VERIFIED_EVIDENCE_RELEVANCE_BOOST = 0.15


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
        # Task 65.10: populate the verified-memory provenance fields for
        # every recognized verified pipeline, not only conversation_candidate
        # - otherwise an approved memorial contribution or biography item
        # would reach the prompt builder with memory_status=None and be
        # mislabeled as an ordinary archival document (see prompt_builder's
        # `_is_verified_learned_memory`).
        is_learned_memory = result.source_type in VERIFIED_EVIDENCE_SOURCE_TYPES
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
    """True for evidence approved through ANY recognized verified pipeline
    (Task 65.10), not only conversation_candidate. Missing/unrecognized
    source_type or missing payload metadata safely resolves to False - it
    never makes an item appear more trusted than it is (Part G #8)."""
    payload_metadata: dict = getattr(result, "payload_metadata", None) or {}
    return (
        getattr(result, "source_type", None) in VERIFIED_EVIDENCE_SOURCE_TYPES
        and payload_metadata.get("memory_status") == _LEARNED_MEMORY_VERIFIED_STATUS
    )


def is_verified_evidence_result(result) -> bool:
    """Public, pipeline-neutral verified-evidence check (Task 65.10). Use
    this wherever calling code needs to know whether a retrieval result is
    recognized as verified evidence, instead of duplicating a
    `source_type == "conversation_candidate"` special case at each call
    site."""
    return _is_verified_learned_memory_result(result)


def _relevance_score(result) -> float:
    try:
        return float(getattr(result, "score", 0.0) or 0.0)
    except (TypeError, ValueError):
        return 0.0


def _dedup_key(result) -> tuple | None:
    """Identifies near-duplicate evidence that should not consume more than
    one context slot (Part E #6 / Part G #6).

    Two distinct signals, either sufficient on its own:
      * the exact same chunk text (`text_hash`) surfacing twice, e.g. via two
        separate retrieval queries that were merged upstream without a
        chunk_id-based dedup step (see app.modules.demo_fa_chat.service.
        `_merge_ranked_retrieval_results`, which only dedups by chunk_id).
      * the same canonical source-of-truth record (a candidate_id or
        promotion_id from payload_metadata) appearing as more than one
        chunk/embedding - defensive, since the current indexing pipelines
        (Task 64.5.1) already guarantee one point per approved memory, but
        ranking must not assume that invariant holds forever.
    Returns None when neither signal is available - such an item is never
    treated as a duplicate of anything.
    """
    payload_metadata: dict = getattr(result, "payload_metadata", None) or {}
    canonical_id = payload_metadata.get("candidate_id") or payload_metadata.get("promotion_id")
    if canonical_id is not None:
        return ("canonical", getattr(result, "source_type", None), canonical_id)
    text_hash = getattr(result, "text_hash", None)
    if text_hash:
        return ("text_hash", text_hash)
    return None


def _deduplicate_evidence(results: list) -> tuple[list, int]:
    """Keeps the highest-relevance item per `_dedup_key` group, preserving
    the original relative order of the survivors. Returns
    (deduplicated_results, dropped_count)."""
    best_by_key: dict[tuple, int] = {}
    for index, result in enumerate(results):
        key = _dedup_key(result)
        if key is None:
            continue
        current_best_index = best_by_key.get(key)
        if current_best_index is None or _relevance_score(result) > _relevance_score(results[current_best_index]):
            best_by_key[key] = index

    kept_indices: set[int] = set()
    for index, result in enumerate(results):
        key = _dedup_key(result)
        if key is None or best_by_key.get(key) == index:
            kept_indices.add(index)

    deduplicated = [result for index, result in enumerate(results) if index in kept_indices]
    return deduplicated, len(results) - len(deduplicated)


def prioritize_corrected_memory_evidence(
    results: list,
    *,
    limit: int = CORRECTED_MEMORY_EVIDENCE_CAP,
    corrected_memory_intent: bool = False,
) -> list:
    """Deterministically rank an already-retrieved, already-filtered evidence
    list and cap the total count sent to the Brain (Task 65.10).

    Cross-pipeline recognition (Part D/F): verification is recognized for
    ANY pipeline in `VERIFIED_EVIDENCE_SOURCE_TYPES` - not only
    conversation_candidate - so an approved memorial contribution or
    biography item is never invisible to this function the way it was
    before this task.

    Near-duplicate evidence (Part E #6 / Part G #6) is always collapsed to
    its single highest-scoring instance first, in both modes below, so it
    cannot consume more than one context slot.

    `corrected_memory_intent` selects between two deliberately different
    ranking modes, mirroring a distinction the roadmap itself already
    established (Task 64.4.1/64.4.2) between two different question shapes:

    * `corrected_memory_intent=False` (default - ordinary factual turns):
      bounded, relevance-driven mode. Each item's combined score is its raw
      retrieval relevance plus `VERIFIED_EVIDENCE_RELEVANCE_BOOST` when
      verified; items are sorted by combined score descending (stable
      tie-break on original position) and capped. Relevance remains the
      principal signal (Part E #3); verification is a small, bounded
      advantage, never an unconditional override (Part E #4, Part G #4-#5).
      This is the mode that fixes the Task 65.10 reported defect: an
      approved memorial-contribution memory (or biography memory) with
      genuinely higher relevance than a couple of unrelated
      conversation-candidate items must not be displaced by them merely
      because they happen to carry a recognized source_type.

    * `corrected_memory_intent=True` (turns the caller has already
      classified - via `app.modules.avatar_persona.memory_query_intent.
      classify_memory_query_intent` - as CORRECTED_MEMORY_FACT or
      CORRECTION_HISTORY): verified items are moved ahead of unverified
      items as a group (stable relevance order preserved within each
      group), matching the empirically-tuned Task 64.4.2 behavior for this
      narrow, explicitly-detected question shape ("what did I originally
      say, and what was it corrected to") - where an unrelated archival
      item scoring higher by raw vector similarity is reliably still the
      wrong answer, and the measured fix (65% -> 100% recall on 20 live
      samples) specifically relied on this stronger, group-level
      precedence. This mode is not a pipeline-specific special case: it
      applies identically to every pipeline in
      `VERIFIED_EVIDENCE_SOURCE_TYPES`, and the caller decides eligibility
      by explicit, generalizable question *intent*, never by which
      pipeline the evidence happens to come from.

    Does not change retrieval, scoring, or top_k itself - only deduplicates,
    reorders, and caps the already-retrieved, already-eligible candidate
    pool passed in.
    """
    deduplicated_results, duplicate_count = _deduplicate_evidence(results)
    for _ in range(duplicate_count):
        observe_evidence_prioritization_dropped(reason="duplicate")

    if corrected_memory_intent:
        verified_first = [result for result in deduplicated_results if _is_verified_learned_memory_result(result)]
        rest = [result for result in deduplicated_results if not _is_verified_learned_memory_result(result)]
        ordered = [*verified_first, *rest]
    else:
        scored = [
            (
                _relevance_score(result)
                + (VERIFIED_EVIDENCE_RELEVANCE_BOOST if _is_verified_learned_memory_result(result) else 0.0),
                index,
                result,
            )
            for index, result in enumerate(deduplicated_results)
        ]
        scored.sort(key=lambda item: (-item[0], item[1]))
        ordered = [result for _score, _index, result in scored]

    selected = ordered[:limit]
    dropped_by_cap = max(0, len(ordered) - len(selected))
    for _ in range(dropped_by_cap):
        observe_evidence_prioritization_dropped(reason="context_budget")

    observe_evidence_prioritization_pool(candidate_count=len(results), selected_count=len(selected))
    for result in selected:
        observe_evidence_prioritization_selected_item(
            verified=_is_verified_learned_memory_result(result),
            source_type=getattr(result, "source_type", None) or "other",
        )
    return selected


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
