from __future__ import annotations

from collections.abc import Sequence
from datetime import UTC, datetime

from sqlalchemy.orm import Session

from app.core.config import Settings
from app.modules.ai_agents.brain.context import (
    build_rag_evidence_items,
    build_vector_retrieval_grounded_context,
)
from app.modules.ai_agents.brain.service import BrainAgentService
from app.modules.ai_agents.schemas import MemoryProfileContext, OrchestratorChatRequest
from app.modules.memory_profiles.repository import get_memory_profile_for_user
from app.modules.active_retrieval_config.service import (
    get_production_recommended_active_retrieval_config,
)
from app.modules.ai_agents.brain.output_guard import BrainOutputGuardContext
from app.modules.embeddings.runtime import (
    assert_real_embedding_runtime_for_e2e,
)
from app.modules.rag_evaluation.brain_eval_e2e_bootstrap import (
    FamilyAvatarRuE2EBootstrapResult,
    build_family_avatar_ru_e2e_collection_name,
    ensure_family_avatar_ru_e2e_bootstrap,
)
from app.modules.rag_evaluation.brain_eval_e2e_diagnostics import (
    run_e2e_retrieval_diagnostics,
    run_e2e_top_k_diagnostics,
)
from app.modules.rag_evaluation.brain_eval_e2e_report import write_brain_rag_eval_e2e_artifacts
from app.modules.rag_evaluation.brain_eval_e2e_schemas import (
    BrainEvalE2ECaseResult,
    BrainEvalE2EEmbeddingDiagnostics,
    BrainEvalE2ESuiteResult,
    BrainEvalE2EFailureClass,
    BrainEvalE2ETopKDiagnostic,
    BrainEvalRetrievedChunkRecord,
    BrainRagEvalE2ERunResult,
)
from app.modules.rag_evaluation.brain_eval_runner import (
    build_brain_rag_eval_provider,
    preflight_brain_rag_eval,
    resolve_brain_rag_eval_cases,
)
from app.modules.rag_evaluation.evaluator import evaluate_answer_against_case
from app.modules.rag_evaluation.exceptions import BrainRagEvalConfigurationError
from app.modules.rag_evaluation.fixtures.family_avatar_i18n_specs import (
    FAMILY_AVATAR_I18N_SPECS,
    FamilyAvatarCaseSpec,
)
from app.modules.rag_evaluation.schemas import BrainRagEvalConfig, RagEvaluationCase
from app.modules.rag_retrieval.schemas import RagRetrievalRequest
from app.modules.rag_retrieval.service import retrieve_profile_rag
from app.modules.users.repository import get_user_by_id


SPECS_BY_CASE_ID: dict[str, FamilyAvatarCaseSpec] = {
    spec.case_id: spec for spec in FAMILY_AVATAR_I18N_SPECS
}

SUPPORTED_E2E_CASE_SETS = frozenset({"family_avatar_ru", "family_avatar_ru_e2e"})


def _resolve_e2e_case_set(case_set: str) -> str:
    if case_set == "family_avatar_ru_e2e":
        return "family_avatar_ru"
    return case_set


def _build_profile_context(profile) -> MemoryProfileContext:
    return MemoryProfileContext(
        id=profile.id,
        name=profile.name,
        birth_date=profile.birth_date,
        death_date=profile.death_date,
        biography=profile.biography,
        personality=profile.personality,
        catchphrases=profile.catchphrases,
        is_public=profile.is_public,
    )


def _resolve_expected_fact_id(spec: FamilyAvatarCaseSpec | None) -> str | None:
    if spec is None:
        return None
    if spec.kind in {"memory", "rag"}:
        return spec.fact_id
    if spec.kind == "custom":
        return spec.memory_fact_id or spec.rag_fact_id
    return None


def _expected_evidence_in_context(
    *,
    spec: FamilyAvatarCaseSpec | None,
    bootstrap: FamilyAvatarRuE2EBootstrapResult,
    retrieved_chunk_ids: Sequence[int],
) -> bool | None:
    if spec is None or spec.kind == "lack":
        return None

    if spec.kind in {"memory", "rag"}:
        if spec.fact_id is None:
            return None
        expected_chunk_id = bootstrap.chunk_ids_by_fact_id.get(spec.fact_id)
        if expected_chunk_id is None:
            return False
        return expected_chunk_id in retrieved_chunk_ids

    checks: list[bool] = []
    for fact_id in (spec.memory_fact_id, spec.rag_fact_id):
        if fact_id is None:
            continue
        expected_chunk_id = bootstrap.chunk_ids_by_fact_id.get(fact_id)
        checks.append(
            expected_chunk_id is not None and expected_chunk_id in retrieved_chunk_ids
        )
    if not checks:
        return None
    return all(checks)


def _classify_e2e_failure(
    *,
    case: RagEvaluationCase,
    eval_passed: bool,
    expected_evidence_found: bool | None,
) -> BrainEvalE2EFailureClass | None:
    if eval_passed:
        return None

    if case.expected_behavior == "lack_of_evidence":
        return "ANSWER_GENERATION"

    if expected_evidence_found is False:
        return "RETRIEVAL_MISSING_EVIDENCE"

    return "ANSWER_GENERATION"


def _run_e2e_case(
    *,
    db: Session,
    case: RagEvaluationCase,
    bootstrap: FamilyAvatarRuE2EBootstrapResult,
    brain_service: BrainAgentService,
) -> BrainEvalE2ECaseResult:
    user = get_user_by_id(db, bootstrap.user_id)
    if user is None:
        raise BrainRagEvalConfigurationError("Family Avatar RU E2E user not found")

    profile = get_memory_profile_for_user(
        db,
        user_id=bootstrap.user_id,
        profile_id=bootstrap.profile_id,
    )
    if profile is None:
        raise BrainRagEvalConfigurationError("Family Avatar RU E2E profile not found")

    retrieval_response = retrieve_profile_rag(
        db,
        current_user=user,
        profile_id=bootstrap.profile_id,
        payload=RagRetrievalRequest(
            query=case.user_query,
            limit=bootstrap.top_k,
        ),
    )
    retrieved_evidence_items = build_rag_evidence_items(retrieval_response.results)
    grounded_context = build_vector_retrieval_grounded_context(
        profile=profile,
        retrieved_evidence_items=retrieved_evidence_items,
    )

    request = OrchestratorChatRequest(
        profile=_build_profile_context(profile),
        user_message=case.user_query,
        recent_history=case.recent_history,
        grounded_context=grounded_context,
        output_guard_context=BrainOutputGuardContext(
            expected_behavior=case.expected_behavior,
            forbidden_claims=tuple(case.forbidden_claims),
            should_require_lack_of_evidence=case.should_require_lack_of_evidence,
        ),
    )
    response = brain_service.generate_chat_response(request)

    evidence_count = len(grounded_context.evidence_items) + len(grounded_context.retrieved_evidence_items)
    eval_result = evaluate_answer_against_case(
        case=case,
        answer_text=response.text,
        provider_name=response.provider_name,
        response_metadata=response.metadata,
        evidence_count=evidence_count,
    )

    spec = SPECS_BY_CASE_ID.get(case.case_id)
    selected_memory_ids: list[int] = []
    retrieved_chunk_ids = [item.chunk_id for item in grounded_context.retrieved_evidence_items]
    expected_evidence_found = _expected_evidence_in_context(
        spec=spec,
        bootstrap=bootstrap,
        retrieved_chunk_ids=retrieved_chunk_ids,
    )
    failure_class = _classify_e2e_failure(
        case=case,
        eval_passed=eval_result.passed,
        expected_evidence_found=expected_evidence_found,
    )

    reasons = list(eval_result.reasons)
    if failure_class == "RETRIEVAL_MISSING_EVIDENCE":
        reasons.insert(0, "Expected evidence was not present in retrieved context (RETRIEVAL_MISSING_EVIDENCE)")
    elif failure_class == "ANSWER_GENERATION" and not reasons:
        reasons.append("Answer generation did not satisfy evaluator checks")

    retrieved_chunks = [
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
        for index, result in enumerate(retrieval_response.results, start=1)
    ]

    return BrainEvalE2ECaseResult(
        case_id=case.case_id,
        title=case.title,
        passed=eval_result.passed,
        expected_behavior=case.expected_behavior,
        actual_behavior=eval_result.actual_behavior,
        failure_class=failure_class,
        reasons=reasons,
        user_query=case.user_query,
        answer_text=eval_result.answer_text,
        answer_preview=eval_result.answer_preview,
        reference_queries=eval_result.reference_queries,
        expected_markers=list(case.expected_evidence_markers),
        missing_expected_markers=list(eval_result.missing_expected_markers),
        forbidden_claims_found=list(eval_result.forbidden_claims_found),
        expected_fact_id=_resolve_expected_fact_id(spec),
        expected_evidence_found=expected_evidence_found,
        selected_memory_ids=selected_memory_ids,
        retrieved_chunks=retrieved_chunks,
        evidence_count=evidence_count,
        provider_name=eval_result.provider_name,
        response_metadata=eval_result.response_metadata,
    )


def run_brain_rag_eval_e2e(
    db: Session,
    config: BrainRagEvalConfig,
    *,
    provider_settings: Settings | None = None,
    brain_service: BrainAgentService | None = None,
) -> BrainRagEvalE2ERunResult:
    if config.case_set not in SUPPORTED_E2E_CASE_SETS:
        raise BrainRagEvalConfigurationError(
            "Real-retrieval E2E mode supports only family_avatar_ru or family_avatar_ru_e2e case sets."
        )

    resolved_case_set = _resolve_e2e_case_set(config.case_set)
    preflight_config = config.model_copy(update={"case_set": resolved_case_set})
    preflight = preflight_brain_rag_eval(preflight_config, provider_settings=provider_settings)
    if not preflight.passed:
        raise BrainRagEvalConfigurationError(
            "Brain RAG E2E preflight failed: " + "; ".join(preflight.issues)
        )

    cases = resolve_brain_rag_eval_cases(resolved_case_set)
    if not cases:
        raise BrainRagEvalConfigurationError("Brain RAG E2E requires at least one case.")

    recommendation = get_production_recommended_active_retrieval_config()
    e2e_collection_name = build_family_avatar_ru_e2e_collection_name(
        base_collection_name=recommendation.collection_name,
    )
    try:
        runtime_diagnostics = assert_real_embedding_runtime_for_e2e(
            model_code=recommendation.model_code,
            collection_name=e2e_collection_name,
            allow_mock_embeddings=config.allow_mock_embeddings,
        )
    except RuntimeError as exc:
        raise BrainRagEvalConfigurationError(str(exc)) from exc

    bootstrap = ensure_family_avatar_ru_e2e_bootstrap(db)

    user = get_user_by_id(db, bootstrap.user_id)
    if user is None:
        raise BrainRagEvalConfigurationError("Family Avatar RU E2E user not found")
    embedding_diagnostics = BrainEvalE2EEmbeddingDiagnostics(
        embedding_provider_setting=runtime_diagnostics.embedding_provider_setting,
        resolved_indexing_provider_name=runtime_diagnostics.resolved_indexing_provider_name,
        resolved_query_provider_name=runtime_diagnostics.resolved_query_provider_name,
        is_mock_indexing_provider=runtime_diagnostics.is_mock_indexing_provider,
        is_mock_query_provider=runtime_diagnostics.is_mock_query_provider,
        indexing_query_providers_match=runtime_diagnostics.indexing_query_providers_match,
        model_code=runtime_diagnostics.model_code,
        model_display_name=runtime_diagnostics.model_display_name,
        provider_model_name=runtime_diagnostics.provider_model_name,
        embedding_dimension=runtime_diagnostics.embedding_dimension,
        collection_name=runtime_diagnostics.collection_name,
        collection_vector_size=runtime_diagnostics.collection_vector_size,
        flag_embedding_available=runtime_diagnostics.flag_embedding_available,
        bge_m3_snapshot_cached=runtime_diagnostics.bge_m3_snapshot_cached,
        bge_m3_snapshot_path=runtime_diagnostics.bge_m3_snapshot_path,
        huggingface_offline_mode=runtime_diagnostics.huggingface_offline_mode,
        embedding_runtime_fingerprint=bootstrap.embedding_runtime_fingerprint,
        collection_rebuilt=bootstrap.collection_rebuilt,
    )

    if brain_service is None:
        provider = build_brain_rag_eval_provider(
            provider_name=config.provider_name,
            provider_settings=provider_settings,
        )
        brain_service = BrainAgentService(provider=provider)

    results = [
        _run_e2e_case(
            db=db,
            case=case,
            bootstrap=bootstrap,
            brain_service=brain_service,
        )
        for case in cases
    ]

    passed_cases = sum(1 for result in results if result.passed)
    retrieval_failures = sum(
        1 for result in results if result.failure_class == "RETRIEVAL_MISSING_EVIDENCE"
    )
    answer_failures = sum(
        1 for result in results if result.failure_class == "ANSWER_GENERATION"
    )
    suite_result = BrainEvalE2ESuiteResult(
        total_cases=len(results),
        passed_cases=passed_cases,
        failed_cases=len(results) - passed_cases,
        retrieval_failures=retrieval_failures,
        answer_failures=answer_failures,
        results=results,
    )
    retrieval_diagnostics = run_e2e_retrieval_diagnostics(
        db=db,
        user=user,
        bootstrap=bootstrap,
        case_results=results,
        top_k=bootstrap.top_k,
    )
    top_k_diagnostics = [
        BrainEvalE2ETopKDiagnostic(
            top_k=summary.top_k,
            expected_chunk_hits=summary.expected_chunk_hits,
            expected_chunk_checks=summary.expected_chunk_checks,
        )
        for summary in run_e2e_top_k_diagnostics(
            db=db,
            user=user,
            bootstrap=bootstrap,
            top_k_values=(5, 10, 20),
        )
    ]

    run_id = datetime.now(UTC).strftime("%Y%m%d_%H%M%SZ")
    e2e_result = BrainRagEvalE2ERunResult(
        run_id=run_id,
        passed=suite_result.failed_cases == 0,
        case_set=config.case_set,
        provider_name=config.provider_name,
        model=preflight.model,
        profile_id=bootstrap.profile_id,
        top_k=bootstrap.top_k,
        embedding_model_code=bootstrap.model_code,
        qdrant_collection=bootstrap.collection_name,
        retrieval_mode=bootstrap.retrieval_mode,
        embedding_diagnostics=embedding_diagnostics,
        retrieval_diagnostics=retrieval_diagnostics,
        top_k_diagnostics=top_k_diagnostics,
        suite_result=suite_result,
    )

    if config.write_artifacts and config.artifact_dir is not None:
        e2e_result.artifact_paths = write_brain_rag_eval_e2e_artifacts(
            result=e2e_result,
            artifact_dir=config.artifact_dir,
        )

    return e2e_result
