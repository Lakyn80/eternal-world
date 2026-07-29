"""Bounded, privacy-safe verified-context retrieval for the Biographer topic
catalog (Task 65.6, made single-batch in Task 65.11.1).

Only two `source_type` values are ever queried: `"biography"` (the current
indexed biography) and `"conversation_candidate"` (previously approved,
explicitly indexed memories) - both are, by construction of
`avatar_memory_indexing`/`biography_ingestion`, always fully verified/indexed
content; nothing in `draft`/`needs_review`/`pending_index`/`rejected` state
ever has a Qdrant point to retrieve (see `rag_retrieval.service` audit notes).

Task 65.11.1 - why this module no longer calls `retrieve_profile_rag()`
-----------------------------------------------------------------------
The Task 65.6 implementation built one `TopicContextPackage` per catalog
topic by calling the public `retrieve_profile_rag()` twice per topic (once
per `source_type`). With 8 catalog topics that is 16 sequential calls per
"generate a new question" request, and every one of them performed its own
real BGE-M3 query encode (the 560M-parameter model, on CPU, inside one HTTP
request) plus its own Qdrant round trip. Task 65.11's shared model instance
removed the repeated 2GB model *loads* and the meta-tensor race, but the 16
serial encodes remained - and the new per-shared-model encode lock correctly
serializes them, so "run them concurrently" is not a fix.

The whole catalog is now served by exactly one query-embedding model
invocation (all 8 topic queries batched together, query semantics) and
exactly one Qdrant batch request (all 8 topic vectors, one combined
verified-source filter), via `rag_retrieval.batch_query`. Coverage
evaluation only ever needed a chunk *count* per topic; the prompt-ready
excerpt text is materialized for the one selected topic only.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from time import perf_counter

from sqlalchemy.orm import Session

from app.db.models import User
from app.modules.avatar_biographer.topics import BiographerTopic
from app.modules.rag_retrieval.batch_query import BatchQuerySpec, retrieve_profile_rag_query_batch
from app.modules.rag_retrieval.schemas import RagRetrievalResultRead

#: Small, bounded per-topic retrieval - never the whole biography, never the
#: global Chat top_k (that ranking/limit is explicitly out of scope here).
_CONTEXT_CHUNK_LIMIT = 5
_MAX_CHUNK_CHARS_IN_PROMPT = 320
#: Rough, deterministic estimate (no tokenizer call) for observability only.
_CHARS_PER_ESTIMATED_TOKEN = 4

_VERIFIED_SOURCE_TYPES = ("biography", "conversation_candidate")

#: Fused top-k requested per topic from the combined-source-type batch query.
#: Deliberately `_CONTEXT_CHUNK_LIMIT * len(_VERIFIED_SOURCE_TYPES)` so the
#: pre-bound candidate list this module reasons about
#: (`available_verified_sources`) keeps exactly the same size bound it had
#: when the two source types were queried separately at `_CONTEXT_CHUNK_LIMIT`
#: each; the prompt itself is still bounded to `_CONTEXT_CHUNK_LIMIT` chunks.
_BATCH_RETRIEVAL_LIMIT = _CONTEXT_CHUNK_LIMIT * len(_VERIFIED_SOURCE_TYPES)


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


@dataclass(frozen=True)
class TopicCoverageEvidence:
    """What coverage evaluation actually needs for ONE topic.

    Deliberately not a prompt-ready package: `build_topic_coverage_map` only
    compares `selected_chunk_count` against
    `RICH_EVIDENCE_CHUNK_THRESHOLD`/`BASIC_EVIDENCE_CHUNK_THRESHOLD`, and the
    per-topic metric only needs `selected_source_count`. `bounded_chunk_texts`
    carries the text the single batch query already returned so the *selected*
    topic can be hydrated without any further embedding or Qdrant work - it is
    never turned into prompt excerpts for a topic that is not selected.
    """

    topic_key: str
    retrieval_used: bool
    available_verified_sources: int
    selected_source_count: int
    selected_chunk_count: int
    retrieval_duration_ms: int
    bounded_chunk_texts: tuple[str, ...] = ()


@dataclass(frozen=True)
class BiographerTopicContextBatch:
    """Result of the single batched coverage retrieval for the whole catalog."""

    locale: str
    retrieval_used: bool
    #: Number of topic query texts handed to the model in one batch.
    topic_query_batch_size: int
    #: Query-embedding model invocations performed (contract: exactly 1).
    model_invocation_count: int
    #: Qdrant network round trips performed (contract: exactly 1).
    qdrant_request_count: int
    coverage_retrieval_duration_ms: int
    evidence_by_topic: dict[str, TopicCoverageEvidence] = field(default_factory=dict)

    def evidence_for(self, topic_key: str) -> TopicCoverageEvidence:
        existing = self.evidence_by_topic.get(topic_key)
        if existing is not None:
            return existing
        return TopicCoverageEvidence(
            topic_key=topic_key,
            retrieval_used=self.retrieval_used,
            available_verified_sources=0,
            selected_source_count=0,
            selected_chunk_count=0,
            retrieval_duration_ms=0,
        )

    def verified_chunk_counts_by_topic(self) -> dict[str, int]:
        return {key: evidence.selected_chunk_count for key, evidence in self.evidence_by_topic.items()}

    def hydrate_context_package(self, topic: BiographerTopic) -> TopicContextPackage:
        """Materialize the prompt-ready package for the SELECTED topic only.

        Pure, local shaping of text the single batch query already returned:
        no embedding call, no Qdrant call, no second per-source-type query.
        """

        evidence = self.evidence_for(topic.key)
        chunk_excerpts = [
            text[:_MAX_CHUNK_CHARS_IN_PROMPT].strip() for text in evidence.bounded_chunk_texts
        ]
        context_character_count = sum(len(excerpt) for excerpt in chunk_excerpts)
        return TopicContextPackage(
            topic_key=topic.key,
            retrieval_used=evidence.retrieval_used,
            available_verified_sources=evidence.available_verified_sources,
            selected_source_count=evidence.selected_source_count,
            selected_chunk_count=evidence.selected_chunk_count,
            context_character_count=context_character_count,
            estimated_context_tokens=context_character_count // _CHARS_PER_ESTIMATED_TOKEN,
            retrieval_duration_ms=evidence.retrieval_duration_ms,
            chunk_excerpts=chunk_excerpts,
        )


def topic_query_text(topic: BiographerTopic, *, locale: str) -> str:
    # The topic's own fixed fallback question is a good, human-curated
    # semantic query for "what does the memorial already say about this
    # topic" - reusing it avoids inventing a second query-generation step.
    return topic.questions.get(locale, topic.questions["ru"])


def build_topic_query_batch(
    topics: tuple[BiographerTopic, ...],
    *,
    locale: str,
) -> list[BatchQuerySpec]:
    """One semantic query text per catalog topic, in stable catalog order.

    Order is the contract: `topics[i]` <-> `specs[i]` <-> vector `i`, so the
    topic/vector mapping stays deterministic for every locale.
    """

    return [
        BatchQuerySpec(key=topic.key, query_text=topic_query_text(topic, locale=locale))
        for topic in topics
    ]


def _build_topic_evidence(
    *,
    topic_key: str,
    results: list[RagRetrievalResultRead],
    retrieval_duration_ms: int,
) -> TopicCoverageEvidence:
    bounded_results = results[:_CONTEXT_CHUNK_LIMIT]
    return TopicCoverageEvidence(
        topic_key=topic_key,
        retrieval_used=True,
        available_verified_sources=len({item.source_id for item in results}),
        selected_source_count=len({item.source_id for item in bounded_results}),
        selected_chunk_count=len(bounded_results),
        retrieval_duration_ms=retrieval_duration_ms,
        bounded_chunk_texts=tuple(item.text for item in bounded_results),
    )


def build_topic_context_batch(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    topics: tuple[BiographerTopic, ...],
    locale: str,
) -> BiographerTopicContextBatch:
    """Coverage evidence for EVERY catalog topic in one model invocation and
    one Qdrant request."""

    specs = build_topic_query_batch(topics, locale=locale)
    started_at = perf_counter()
    outcome = retrieve_profile_rag_query_batch(
        db,
        current_user=current_user,
        profile_id=profile_id,
        specs=specs,
        limit=_BATCH_RETRIEVAL_LIMIT,
        source_types=_VERIFIED_SOURCE_TYPES,
    )
    duration_ms = int((perf_counter() - started_at) * 1000)

    return BiographerTopicContextBatch(
        locale=locale,
        retrieval_used=True,
        topic_query_batch_size=len(specs),
        model_invocation_count=outcome.model_invocation_count,
        qdrant_request_count=outcome.qdrant_request_count,
        coverage_retrieval_duration_ms=duration_ms,
        evidence_by_topic={
            topic.key: _build_topic_evidence(
                topic_key=topic.key,
                results=outcome.results_for(topic.key),
                retrieval_duration_ms=duration_ms,
            )
            for topic in topics
        },
    )


def empty_context_batch(
    topics: tuple[BiographerTopic, ...],
    *,
    locale: str,
) -> BiographerTopicContextBatch:
    """Used when batched retrieval degrades safely (e.g. Qdrant unavailable or
    the batch query encode failed) - the caller must still be able to fall
    back to a deterministic question rather than returning a 500."""

    return BiographerTopicContextBatch(
        locale=locale,
        retrieval_used=False,
        topic_query_batch_size=0,
        model_invocation_count=0,
        qdrant_request_count=0,
        coverage_retrieval_duration_ms=0,
        evidence_by_topic={
            topic.key: TopicCoverageEvidence(
                topic_key=topic.key,
                retrieval_used=False,
                available_verified_sources=0,
                selected_source_count=0,
                selected_chunk_count=0,
                retrieval_duration_ms=0,
            )
            for topic in topics
        },
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


def context_batch_from_packages(
    packages: dict[str, TopicContextPackage],
    *,
    topics: tuple[BiographerTopic, ...],
    locale: str,
) -> BiographerTopicContextBatch:
    """Build a batch result from already-shaped per-topic packages.

    The only production-code use is symmetry with `empty_context_batch`; its
    real purpose is to let fake-safe tests express "these are the per-topic
    coverage fixtures" without needing a real embedding provider or Qdrant
    server, while still exercising the exact same coverage/selection/hydration
    code path the real batch takes.
    """

    return BiographerTopicContextBatch(
        locale=locale,
        retrieval_used=any(package.retrieval_used for package in packages.values()),
        topic_query_batch_size=len(topics),
        model_invocation_count=1,
        qdrant_request_count=1,
        coverage_retrieval_duration_ms=0,
        evidence_by_topic={
            topic.key: _evidence_from_package(topic.key, packages.get(topic.key))
            for topic in topics
        },
    )


def _evidence_from_package(
    topic_key: str,
    package: TopicContextPackage | None,
) -> TopicCoverageEvidence:
    if package is None:
        return TopicCoverageEvidence(
            topic_key=topic_key,
            retrieval_used=False,
            available_verified_sources=0,
            selected_source_count=0,
            selected_chunk_count=0,
            retrieval_duration_ms=0,
        )
    return TopicCoverageEvidence(
        topic_key=topic_key,
        retrieval_used=package.retrieval_used,
        available_verified_sources=package.available_verified_sources,
        selected_source_count=package.selected_source_count,
        selected_chunk_count=package.selected_chunk_count,
        retrieval_duration_ms=package.retrieval_duration_ms,
        bounded_chunk_texts=tuple(package.chunk_excerpts),
    )
