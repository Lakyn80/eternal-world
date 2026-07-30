"""Task 65.11.1 - the smallest internal retrieval primitive that answers
several *independent* semantic queries for one memorial in one query-embedding
model invocation and one Qdrant round trip.

Why this exists at all: the AI Biographer needs a verified-evidence chunk
count for every one of its 8 catalog topics before it can decide which topic
to ask about next. Expressing that through the public
`rag_retrieval.service.retrieve_profile_rag()` entry point meant 8 topics x 2
`source_type` values = 16 separate calls, each performing its own BGE-M3
query encode and its own Qdrant search inside a single HTTP request. This
module keeps every security-relevant rule of the public path byte-for-byte
identical - the same `resolve_authorized_profile` capability check, the same
`owner_user_id`/`profile_id` Qdrant filter, the same
`repository.list_retrieval_evidence_for_embeddings` SQL scoping (which is
what actually enforces "only indexed, verified evidence", including the
`promotion_status='indexed'` requirement for `conversation_candidate`), the
same `_is_visible_to_viewer` owner-only privacy check, and the same
`rank_retrieval_results` ordering - and changes only *how many* model/network
round trips are needed to get there.

Deliberately NOT a public API and deliberately not used by the Chat
retrieval path: `retrieve_profile_rag()` keeps its exact current behaviour
(Task 65.11.1 must not change public chat retrieval).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Sequence

from sqlalchemy.orm import Session

from app.db.models import User
from app.modules.active_retrieval_config.service import resolve_runtime_active_retrieval_config
from app.modules.qdrant_indexing.exceptions import QdrantCollectionConfigurationError
from app.modules.rag_retrieval import repository
from app.modules.rag_retrieval.hybrid import (
    HybridQueryVectors,
    HybridRetrievalCandidate,
    build_hybrid_candidate_pool_limit,
    encode_hybrid_query_vectors_batch,
    rank_fused_hybrid_candidates,
)
from app.modules.rag_retrieval.ranking import rank_retrieval_results
from app.modules.rag_retrieval.schemas import RagRetrievalResultRead


@dataclass(frozen=True)
class BatchQuerySpec:
    """One semantic query in the batch. `key` is a caller-owned, non-user
    -controlled label (the Biographer passes its fixed catalog topic key) used
    only to map results back - it never reaches Qdrant or any log line."""

    key: str
    query_text: str


@dataclass(frozen=True)
class BatchRetrievalOutcome:
    model_code: str
    #: Number of BGE-M3 (or fallback provider) query-embedding model
    #: invocations actually performed - the structural performance contract
    #: of this task asserts on this being exactly 1 per new-question request.
    model_invocation_count: int
    #: Number of Qdrant network round trips actually performed.
    qdrant_request_count: int
    encoded_query_count: int
    results_by_key: dict[str, list[RagRetrievalResultRead]] = field(default_factory=dict)

    def results_for(self, key: str) -> list[RagRetrievalResultRead]:
        return self.results_by_key.get(key, [])


def _build_batch_search_filter(
    *,
    owner_user_id: int,
    profile_id: int,
    language: str | None,
    source_types: Sequence[str],
) -> dict[str, object]:
    """Owner + profile isolation is mandatory and always `must`.

    The several verified `source_type` values are expressed as ONE `must`
    condition using Qdrant's `match: {"any": [...]}` (logically
    `source_type IN (...)`, still AND-ed with owner/profile) rather than as a
    `should` clause - a `should` would weaken the owner/profile constraint
    semantics and is not needed here.
    """

    must_filters: list[dict[str, object]] = [
        {"key": "owner_user_id", "match": {"value": owner_user_id}},
        {"key": "profile_id", "match": {"value": profile_id}},
    ]
    if language is not None:
        must_filters.append({"key": "language", "match": {"value": language}})

    normalized_source_types = [source_type for source_type in source_types if source_type]
    if len(normalized_source_types) == 1:
        must_filters.append({"key": "source_type", "match": {"value": normalized_source_types[0]}})
    elif normalized_source_types:
        must_filters.append({"key": "source_type", "match": {"any": list(normalized_source_types)}})

    return {"must": must_filters}


def _build_hybrid_candidates(raw_results: list[dict[str, object]]) -> list[HybridRetrievalCandidate]:
    from app.modules.rag_retrieval.service import _coerce_sparse_vector_payload

    candidates: list[HybridRetrievalCandidate] = []
    for item in raw_results:
        payload_metadata = item.get("payload")
        if not isinstance(payload_metadata, dict):
            continue

        embedding_id = payload_metadata.get("embedding_id")
        chunk_id = payload_metadata.get("chunk_id")
        if not isinstance(embedding_id, int) or not isinstance(chunk_id, int):
            continue

        candidates.append(
            HybridRetrievalCandidate(
                embedding_id=embedding_id,
                chunk_id=chunk_id,
                dense_score=float(item.get("score", 0.0)),
                sparse_vector=_coerce_sparse_vector_payload(payload_metadata),
                payload_metadata=payload_metadata,
            )
        )
    return candidates


def retrieve_profile_rag_query_batch(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    specs: Sequence[BatchQuerySpec],
    limit: int,
    source_types: Sequence[str],
    language: str | None = None,
    query_batch_encoder: Callable[..., list[HybridQueryVectors]] | None = None,
) -> BatchRetrievalOutcome:
    """Run every `spec` against the memorial's verified indexed evidence.

    Exactly one query-embedding model invocation (for all `specs` together)
    and exactly one Qdrant request (for all `specs` together) - never one per
    spec and never one per `source_type`.
    """

    # Imported lazily to avoid an import cycle: `service` imports nothing
    # from this module, but this module reuses `service`'s already-audited
    # authorization/model-resolution/visibility helpers rather than
    # re-implementing (and risking diverging from) them. The Qdrant client
    # factory is deliberately resolved through the `service` module object
    # (not re-imported here) so that `rag_retrieval.service.build_qdrant_client`
    # stays the single established test/injection seam for both the scalar
    # and the batch retrieval path.
    from app.modules.rag_retrieval import service as rag_retrieval_service
    from app.modules.rag_retrieval.service import (
        _ensure_retrieval_enabled,
        _is_visible_to_viewer,
        _resolve_authorized_profile,
        _resolve_model,
        _should_use_hybrid_dense_sparse_path,
        build_retrieval_collection_name,
    )

    spec_list = list(specs)
    if not spec_list:
        return BatchRetrievalOutcome(
            model_code="",
            model_invocation_count=0,
            qdrant_request_count=0,
            encoded_query_count=0,
            results_by_key={},
        )

    _ensure_retrieval_enabled()
    profile = _resolve_authorized_profile(db, current_user=current_user, profile_id=profile_id)
    owner_user_id = profile.user_id
    viewer_is_profile_owner = current_user.id == owner_user_id

    runtime_config = resolve_runtime_active_retrieval_config(
        db,
        current_user=current_user,
        profile_id=profile_id,
    )
    model = _resolve_model(runtime_config.model_code)
    qdrant_collection = build_retrieval_collection_name(
        model.code,
        collection_name=runtime_config.collection_name,
    )
    score_threshold = runtime_config.score_threshold

    # --- Phase 1: ONE query-batch model invocation ------------------------
    query_vectors = encode_hybrid_query_vectors_batch(
        [spec.query_text for spec in spec_list],
        model.code,
        query_batch_encoder=query_batch_encoder,
    )
    if len(query_vectors) != len(spec_list):
        raise QdrantCollectionConfigurationError("Query embedding batch size is invalid")
    for vectors in query_vectors:
        if len(vectors.dense_vector) != model.dimension:
            raise QdrantCollectionConfigurationError("Query embedding dimension is invalid")

    use_hybrid = _should_use_hybrid_dense_sparse_path(
        model_code=model.code,
        retrieval_mode=runtime_config.retrieval_mode,
    )
    candidate_limit = build_hybrid_candidate_pool_limit(top_k=limit) if use_hybrid else limit
    search_filter = _build_batch_search_filter(
        owner_user_id=owner_user_id,
        profile_id=profile_id,
        language=language,
        source_types=source_types,
    )

    # --- Phase 2: ONE Qdrant batch request for every topic vector ---------
    qdrant_client = rag_retrieval_service.build_qdrant_client()
    raw_result_batches = qdrant_client.search_points_batch(
        collection_name=qdrant_collection,
        searches=[
            {
                "vector": vectors.dense_vector,
                "limit": candidate_limit,
                "with_payload": True,
                "filter": search_filter,
                # The hybrid path fuses dense+sparse *after* retrieval, so a
                # dense-only score threshold must not pre-filter the pool -
                # identical to `_retrieve_hybrid_dense_sparse`.
                "score_threshold": None if use_hybrid else score_threshold,
            }
            for vectors in query_vectors
        ],
    )

    fused_by_key: dict[str, list] = {}
    all_embedding_ids: set[int] = set()
    for spec, vectors, raw_results in zip(spec_list, query_vectors, raw_result_batches, strict=True):
        candidates = _build_hybrid_candidates(list(raw_results))
        if not candidates:
            fused_by_key[spec.key] = []
            continue

        if use_hybrid:
            fused = rank_fused_hybrid_candidates(
                query_sparse_vector=vectors.sparse_vector,
                candidates=candidates,
                top_k=limit,
            )
        else:
            fused = [
                _DenseOnlyResult(
                    embedding_id=candidate.embedding_id,
                    chunk_id=candidate.chunk_id,
                    fused_score=candidate.dense_score,
                    payload_metadata=candidate.payload_metadata,
                )
                for candidate in sorted(
                    candidates,
                    key=lambda candidate: candidate.dense_score,
                    reverse=True,
                )[:limit]
            ]

        fused_by_key[spec.key] = fused
        all_embedding_ids.update(result.embedding_id for result in fused)

    # --- One SQL hydration for every topic's candidates at once -----------
    # `list_retrieval_evidence_for_embeddings` is what enforces "only
    # indexed, verified evidence" (owner/profile scoping on every joined
    # table plus the `promotion_status='indexed'` requirement for
    # `conversation_candidate` sources) - unchanged and reused verbatim.
    evidence_by_embedding_id = {}
    if all_embedding_ids:
        evidence_records = repository.list_retrieval_evidence_for_embeddings(
            db,
            owner_user_id=owner_user_id,
            profile_id=profile_id,
            embedding_ids=sorted(all_embedding_ids),
        )
        evidence_by_embedding_id = {record.embedding_id: record for record in evidence_records}

    allowed_source_types = {source_type for source_type in source_types if source_type}
    results_by_key: dict[str, list[RagRetrievalResultRead]] = {}
    for spec in spec_list:
        hydrated_results: list[dict[str, object]] = []
        for fused_result in fused_by_key.get(spec.key, []):
            evidence_record = evidence_by_embedding_id.get(fused_result.embedding_id)
            if evidence_record is None:
                continue
            if language is not None and evidence_record.language != language:
                continue
            if allowed_source_types and evidence_record.source_type not in allowed_source_types:
                continue
            if not _is_visible_to_viewer(
                fused_result.payload_metadata,
                viewer_is_profile_owner=viewer_is_profile_owner,
            ):
                continue

            hydrated_results.append(
                {
                    "chunk_id": evidence_record.chunk_id,
                    "source_id": evidence_record.source_id,
                    "source_title": evidence_record.source_title,
                    "embedding_id": evidence_record.embedding_id,
                    "score": fused_result.fused_score,
                    "text": evidence_record.chunk_text,
                    "chunk_index": evidence_record.chunk_index,
                    "language": evidence_record.language,
                    "source_type": evidence_record.source_type,
                    "validation_status": evidence_record.validation_status,
                    "text_hash": evidence_record.text_hash,
                    "qdrant_collection": qdrant_collection,
                    "payload_metadata": fused_result.payload_metadata,
                }
            )

        ranked_results = rank_retrieval_results(
            hydrated_results,
            limit=limit,
            score_threshold=score_threshold,
        )
        results_by_key[spec.key] = [RagRetrievalResultRead(**result) for result in ranked_results]

    return BatchRetrievalOutcome(
        model_code=model.code,
        model_invocation_count=1,
        qdrant_request_count=1,
        encoded_query_count=len(spec_list),
        results_by_key=results_by_key,
    )


@dataclass(frozen=True)
class _DenseOnlyResult:
    """Shape-compatible stand-in for `FusedHybridRetrievalResult` on the
    non-hybrid (plain dense) retrieval path."""

    embedding_id: int
    chunk_id: int
    fused_score: float
    payload_metadata: dict[str, object]
