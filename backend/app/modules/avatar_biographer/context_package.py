"""Bounded, privacy-safe verified-context retrieval for one Biographer topic
(Task 65.6).

Reuses the existing `rag_retrieval` service exactly as-is (same BGE-M3
embeddings, same Qdrant collections, same profile/owner scoping, same
ranking) - this module adds no new retrieval implementation, it only builds
one topic-scoped query and shapes the result into a small package the
question-generation prompt can consume. Only two `source_type` values are
ever queried: `"biography"` (the current indexed biography) and
`"conversation_candidate"` (previously approved, explicitly indexed
memories) - both are, by construction of `avatar_memory_indexing`/
`biography_ingestion`, always fully verified/indexed content; nothing in
`draft`/`needs_review`/`pending_index`/`rejected` state ever has a Qdrant
point to retrieve (see `rag_retrieval.service` audit notes).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from time import perf_counter

from sqlalchemy.orm import Session

from app.db.models import User
from app.modules.avatar_biographer.topics import BiographerTopic
from app.modules.rag_retrieval.schemas import RagRetrievalRequest, RagRetrievalResultRead
from app.modules.rag_retrieval.service import retrieve_profile_rag

#: Small, bounded per-topic retrieval - never the whole biography, never the
#: global Chat top_k (that ranking/limit is explicitly out of scope here).
_CONTEXT_CHUNK_LIMIT = 5
_MAX_CHUNK_CHARS_IN_PROMPT = 320
#: Rough, deterministic estimate (no tokenizer call) for observability only.
_CHARS_PER_ESTIMATED_TOKEN = 4

_VERIFIED_SOURCE_TYPES = ("biography", "conversation_candidate")


@dataclass(frozen=True)
class TopicContextPackage:
    topic_key: str
    retrieval_used: bool
    available_verified_sources: int
    selected_source_count: int
    selected_chunk_count: int
    context_character_count: int
    estimated_context_tokens: int
    retrieval_duration_ms: int
    #: Short, bounded chunk excerpts used only to build the provider prompt -
    #: never logged and never persisted verbatim (see `avatar_biographer.service`).
    chunk_excerpts: list[str] = field(default_factory=list)


def _topic_query_text(topic: BiographerTopic, *, locale: str) -> str:
    # The topic's own fixed fallback question is a good, human-curated
    # semantic query for "what does the memorial already say about this
    # topic" - reusing it avoids inventing a second query-generation step.
    return topic.questions.get(locale, topic.questions["ru"])


def build_topic_context_package(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    topic: BiographerTopic,
    locale: str,
) -> TopicContextPackage:
    query_text = _topic_query_text(topic, locale=locale)
    started_at = perf_counter()
    results: list[RagRetrievalResultRead] = []
    for source_type in _VERIFIED_SOURCE_TYPES:
        response = retrieve_profile_rag(
            db,
            current_user=current_user,
            profile_id=profile_id,
            payload=RagRetrievalRequest(
                query=query_text,
                limit=_CONTEXT_CHUNK_LIMIT,
                source_type=source_type,
            ),
        )
        results.extend(response.results)

    duration_ms = int((perf_counter() - started_at) * 1000)
    results.sort(key=lambda item: item.score, reverse=True)
    bounded_results = results[:_CONTEXT_CHUNK_LIMIT]

    distinct_source_ids = {item.source_id for item in results}
    chunk_excerpts = [item.text[:_MAX_CHUNK_CHARS_IN_PROMPT].strip() for item in bounded_results]
    context_character_count = sum(len(excerpt) for excerpt in chunk_excerpts)

    return TopicContextPackage(
        topic_key=topic.key,
        retrieval_used=True,
        available_verified_sources=len(distinct_source_ids),
        selected_source_count=len({item.source_id for item in bounded_results}),
        selected_chunk_count=len(bounded_results),
        context_character_count=context_character_count,
        estimated_context_tokens=context_character_count // _CHARS_PER_ESTIMATED_TOKEN,
        retrieval_duration_ms=duration_ms,
        chunk_excerpts=chunk_excerpts,
    )


def empty_context_package(topic: BiographerTopic) -> TopicContextPackage:
    """Used when retrieval degrades safely (e.g. Qdrant unavailable) - the
    caller must still be able to fall back to a deterministic question."""

    return TopicContextPackage(
        topic_key=topic.key,
        retrieval_used=False,
        available_verified_sources=0,
        selected_source_count=0,
        selected_chunk_count=0,
        context_character_count=0,
        estimated_context_tokens=0,
        retrieval_duration_ms=0,
        chunk_excerpts=[],
    )
