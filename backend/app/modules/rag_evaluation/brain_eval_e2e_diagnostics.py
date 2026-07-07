from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.modules.rag_evaluation.brain_eval_e2e_bootstrap import FamilyAvatarRuE2EBootstrapResult
from app.modules.rag_evaluation.brain_eval_e2e_schemas import BrainEvalE2ERetrievalDiagnostic
from app.modules.rag_evaluation.fixtures.family_avatar_i18n_specs import (
    FAMILY_AVATAR_I18N_SPECS,
    FamilyAvatarCaseSpec,
)
from app.modules.rag_retrieval.schemas import RagRetrievalRequest
from app.modules.rag_retrieval.service import retrieve_profile_rag
from app.db.models import User


E2E_DIAGNOSTIC_CASE_IDS = (
    "family-popice-childhood",
    "family-rag-house-plan",
    "family-lack-paris-1968",
)

SPECS_BY_CASE_ID: dict[str, FamilyAvatarCaseSpec] = {
    spec.case_id: spec for spec in FAMILY_AVATAR_I18N_SPECS
}


@dataclass(frozen=True)
class E2ETopKDiagnosticSummary:
    top_k: int
    expected_chunk_hits: int
    expected_chunk_checks: int


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


def run_e2e_retrieval_diagnostics(
    *,
    db: Session,
    user: User,
    bootstrap: FamilyAvatarRuE2EBootstrapResult,
    top_k: int,
) -> list[BrainEvalE2ERetrievalDiagnostic]:
    diagnostics: list[BrainEvalE2ERetrievalDiagnostic] = []

    for case_id in E2E_DIAGNOSTIC_CASE_IDS:
        spec = SPECS_BY_CASE_ID.get(case_id)
        if spec is None:
            continue

        query = spec.queries["ru"]
        retrieval_response = retrieve_profile_rag(
            db,
            current_user=user,
            profile_id=bootstrap.profile_id,
            payload=RagRetrievalRequest(query=query, limit=top_k),
        )
        retrieved_chunk_ids = [result.chunk_id for result in retrieval_response.results]
        expected_chunk_id = _resolve_expected_chunk_id(spec=spec, bootstrap=bootstrap)
        expected_chunk_rank = None
        if expected_chunk_id is not None and expected_chunk_id in retrieved_chunk_ids:
            expected_chunk_rank = retrieved_chunk_ids.index(expected_chunk_id) + 1

        diagnostics.append(
            BrainEvalE2ERetrievalDiagnostic(
                case_id=case_id,
                user_query=query,
                expected_fact_id=spec.fact_id or spec.memory_fact_id or spec.rag_fact_id,
                expected_chunk_id=expected_chunk_id,
                expected_chunk_in_top_k=(
                    expected_chunk_id in retrieved_chunk_ids
                    if expected_chunk_id is not None
                    else None
                ),
                expected_chunk_rank=expected_chunk_rank,
                retrieved_chunk_ids=retrieved_chunk_ids,
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
            retrieval_response = retrieve_profile_rag(
                db,
                current_user=user,
                profile_id=bootstrap.profile_id,
                payload=RagRetrievalRequest(query=query, limit=top_k),
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
