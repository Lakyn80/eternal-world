from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import RagChunk, RagSource, User
from app.modules.qdrant_indexing.client import build_qdrant_client
from app.modules.rag_evaluation.brain_eval_e2e_bootstrap import (
    FamilyAvatarRuE2EBootstrapResult,
)
from app.modules.rag_evaluation.brain_eval_e2e_schemas import (
    BrainEvalE2ECaseResult,
    BrainEvalE2ERetrievalDiagnostic,
    BrainEvalRetrievedChunkRecord,
)
from app.modules.rag_evaluation.fixtures.family_avatar_i18n_specs import (
    FAMILY_AVATAR_I18N_SPECS,
    FamilyAvatarCaseSpec,
)
from app.modules.rag_retrieval.schemas import RagRetrievalRequest
from app.modules.rag_retrieval.service import retrieve_profile_rag_for_collection


SPECS_BY_CASE_ID: dict[str, FamilyAvatarCaseSpec] = {
    spec.case_id: spec for spec in FAMILY_AVATAR_I18N_SPECS
}

DIAGNOSTIC_SEARCH_LIMIT = 50
DIAGNOSTIC_REPORTED_RESULTS = 10


@dataclass(frozen=True)
class E2ETopKDiagnosticSummary:
    top_k: int
    expected_chunk_hits: int
    expected_chunk_checks: int


@dataclass(frozen=True)
class ChunkContext:
    chunk_id: int
    source_id: int
    source_title: str
    chunk_index: int
    text_preview: str


def _resolve_expected_chunk_id(
    *,
    spec: FamilyAvatarCaseSpec | None,
    bootstrap: FamilyAvatarRuE2EBootstrapResult,
) -> int | None:
    if spec is None or spec.kind == "lack":
        return None
    if spec.kind in {"memory", "rag"} and spec.fact_id is not None:
        return bootstrap.chunk_ids_by_fact_id.get(spec.fact_id)
    for fact_id in (spec.memory_fact_id, spec.rag_fact_id):
        if fact_id is None:
            continue
        chunk_id = bootstrap.chunk_ids_by_fact_id.get(fact_id)
        if chunk_id is not None:
            return chunk_id
    return None


def _build_qdrant_expected_chunk_filter(
    *,
    owner_user_id: int,
    profile_id: int,
    chunk_id: int,
) -> dict[str, object]:
    return {
        "must": [
            {"key": "owner_user_id", "match": {"value": owner_user_id}},
            {"key": "profile_id", "match": {"value": profile_id}},
            {"key": "chunk_id", "match": {"value": chunk_id}},
        ]
    }


def _load_chunk_context(
    *,
    db: Session,
    owner_user_id: int,
    profile_id: int,
    chunk_id: int | None,
) -> ChunkContext | None:
    if chunk_id is None:
        return None

    statement = (
        select(RagChunk, RagSource)
        .join(RagSource, RagChunk.source_id == RagSource.id)
        .where(
            RagChunk.id == chunk_id,
            RagChunk.owner_user_id == owner_user_id,
            RagChunk.profile_id == profile_id,
            RagSource.owner_user_id == owner_user_id,
            RagSource.profile_id == profile_id,
        )
    )
    row = db.execute(statement).first()
    if row is None:
        return None

    rag_chunk, rag_source = row
    return ChunkContext(
        chunk_id=rag_chunk.id,
        source_id=rag_source.id,
        source_title=rag_source.title,
        chunk_index=rag_chunk.chunk_index,
        text_preview=rag_chunk.chunk_text[:240],
    )


def _build_diagnostic_request(
    *,
    query: str,
    model_code: str,
    top_k: int,
) -> RagRetrievalRequest:
    return RagRetrievalRequest.model_construct(
        query=query,
        model_code=model_code,
        limit=top_k,
        score_threshold=None,
        language=None,
        source_type=None,
        _fields_set={"query", "model_code", "limit"},
    )


def _bucket_for_rank(rank: int | None) -> str:
    if rank is None:
        return "not_found"
    if rank <= 5:
        return "top_5"
    if rank <= 10:
        return "top_10"
    if rank <= 20:
        return "top_20"
    if rank <= 50:
        return "top_50"
    return "not_found"


def _expected_chunk_present(
    *,
    owner_user_id: int,
    profile_id: int,
    chunk_id: int | None,
    collection_name: str,
) -> bool | None:
    if chunk_id is None:
        return None

    qdrant_client = build_qdrant_client()
    point_count = qdrant_client.count_points(
        collection_name=collection_name,
        search_filter=_build_qdrant_expected_chunk_filter(
            owner_user_id=owner_user_id,
            profile_id=profile_id,
            chunk_id=chunk_id,
        ),
    )
    return point_count > 0


def run_e2e_retrieval_diagnostics(
    *,
    db: Session,
    user: User,
    bootstrap: FamilyAvatarRuE2EBootstrapResult,
    case_results: list[BrainEvalE2ECaseResult],
    top_k: int,
    diagnostic_search_limit: int = DIAGNOSTIC_SEARCH_LIMIT,
) -> list[BrainEvalE2ERetrievalDiagnostic]:
    diagnostics: list[BrainEvalE2ERetrievalDiagnostic] = []

    retrieval_failures = [
        case_result
        for case_result in case_results
        if case_result.failure_class == "RETRIEVAL_MISSING_EVIDENCE"
    ]

    for case_result in retrieval_failures:
        spec = SPECS_BY_CASE_ID.get(case_result.case_id)
        expected_chunk_id = _resolve_expected_chunk_id(spec=spec, bootstrap=bootstrap)
        query = case_result.user_query
        diagnostic_response = retrieve_profile_rag_for_collection(
            db,
            current_user=user,
            profile_id=bootstrap.profile_id,
            payload=_build_diagnostic_request(
                query=query,
                model_code=bootstrap.model_code,
                top_k=diagnostic_search_limit,
            ),
            collection_name=bootstrap.collection_name,
            retrieval_mode=bootstrap.retrieval_mode,
        )
        retrieved_chunk_ids = [result.chunk_id for result in diagnostic_response.results]
        expected_chunk_rank_at_50 = None
        if expected_chunk_id is not None and expected_chunk_id in retrieved_chunk_ids:
            expected_chunk_rank_at_50 = retrieved_chunk_ids.index(expected_chunk_id) + 1

        expected_chunk_context = _load_chunk_context(
            db=db,
            owner_user_id=user.id,
            profile_id=bootstrap.profile_id,
            chunk_id=expected_chunk_id,
        )
        diagnostics.append(
            BrainEvalE2ERetrievalDiagnostic(
                case_id=case_result.case_id,
                user_query=query,
                expected_fact_id=case_result.expected_fact_id,
                expected_chunk_id=expected_chunk_id,
                expected_chunk_source_id=(
                    expected_chunk_context.source_id if expected_chunk_context is not None else None
                ),
                expected_chunk_source_title=(
                    expected_chunk_context.source_title if expected_chunk_context is not None else None
                ),
                expected_chunk_index=(
                    expected_chunk_context.chunk_index if expected_chunk_context is not None else None
                ),
                expected_chunk_exists_in_qdrant=_expected_chunk_present(
                    owner_user_id=user.id,
                    profile_id=bootstrap.profile_id,
                    chunk_id=expected_chunk_id,
                    collection_name=bootstrap.collection_name,
                ),
                expected_chunk_in_top_k=(
                    expected_chunk_rank_at_50 is not None and expected_chunk_rank_at_50 <= top_k
                )
                if expected_chunk_id is not None
                else None,
                expected_chunk_rank=(
                    expected_chunk_rank_at_50 if expected_chunk_rank_at_50 is not None and expected_chunk_rank_at_50 <= top_k else None
                ),
                expected_chunk_in_top_5=(
                    expected_chunk_rank_at_50 is not None and expected_chunk_rank_at_50 <= 5
                )
                if expected_chunk_id is not None
                else None,
                expected_chunk_in_top_10=(
                    expected_chunk_rank_at_50 is not None and expected_chunk_rank_at_50 <= 10
                )
                if expected_chunk_id is not None
                else None,
                expected_chunk_in_top_20=(
                    expected_chunk_rank_at_50 is not None and expected_chunk_rank_at_50 <= 20
                )
                if expected_chunk_id is not None
                else None,
                expected_chunk_in_top_50=(
                    expected_chunk_rank_at_50 is not None and expected_chunk_rank_at_50 <= diagnostic_search_limit
                )
                if expected_chunk_id is not None
                else None,
                expected_chunk_rank_at_50=expected_chunk_rank_at_50,
                diagnostic_search_limit=diagnostic_search_limit,
                expected_chunk_position_bucket=_bucket_for_rank(expected_chunk_rank_at_50),
                retrieved_chunk_ids=[
                    result.chunk_id
                    for result in diagnostic_response.results[:DIAGNOSTIC_REPORTED_RESULTS]
                ],
                retrieved_chunks=[
                    BrainEvalRetrievedChunkRecord(
                        rank=index,
                        chunk_id=result.chunk_id,
                        embedding_id=result.embedding_id,
                        source_id=result.source_id,
                        source_title=result.source_title,
                        chunk_index=result.chunk_index,
                        score=float(result.score),
                        text_preview=result.text[:240],
                    )
                    for index, result in enumerate(
                        diagnostic_response.results[:DIAGNOSTIC_REPORTED_RESULTS],
                        start=1,
                    )
                ],
                top_k=top_k,
            )
        )

    return diagnostics


def run_e2e_top_k_diagnostics(
    *,
    db: Session,
    user: User,
    bootstrap: FamilyAvatarRuE2EBootstrapResult,
    top_k_values: tuple[int, ...] = (5, 10, 20),
) -> list[E2ETopKDiagnosticSummary]:
    grounded_specs = [
        spec
        for spec in FAMILY_AVATAR_I18N_SPECS
        if spec.kind != "lack"
    ]
    summaries: list[E2ETopKDiagnosticSummary] = []

    for top_k in top_k_values:
        hits = 0
        checks = 0
        for spec in grounded_specs:
            expected_chunk_id = _resolve_expected_chunk_id(spec=spec, bootstrap=bootstrap)
            if expected_chunk_id is None:
                continue
            checks += 1
            query = spec.queries["ru"]
            retrieval_response = retrieve_profile_rag_for_collection(
                db,
                current_user=user,
                profile_id=bootstrap.profile_id,
                payload=_build_diagnostic_request(
                    query=query,
                    model_code=bootstrap.model_code,
                    top_k=top_k,
                ),
                collection_name=bootstrap.collection_name,
                retrieval_mode=bootstrap.retrieval_mode,
            )
            retrieved_chunk_ids = [result.chunk_id for result in retrieval_response.results]
            if expected_chunk_id in retrieved_chunk_ids:
                hits += 1
        summaries.append(
            E2ETopKDiagnosticSummary(
                top_k=top_k,
                expected_chunk_hits=hits,
                expected_chunk_checks=checks,
            )
        )

    return summaries
