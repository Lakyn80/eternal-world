from __future__ import annotations

from collections.abc import Sequence
from datetime import UTC, datetime

from app.core.config import Settings, settings
from app.modules.ai_agents.brain.provider import (
    BrainAgentProvider,
    BrainProviderConfigurationError,
    build_brain_provider,
)
from app.modules.ai_agents.brain.service import BrainAgentService
from app.modules.rag_evaluation.brain_eval_report import write_brain_rag_eval_artifacts
from app.modules.rag_evaluation.cases import (
    ALL_RAG_EVALUATION_CASES,
    ETERNAL_WORLD_RAG_EVALUATION_CASES,
    FAMILY_AVATAR_CS_EVALUATION_CASES,
    FAMILY_AVATAR_EN_EVALUATION_CASES,
    FAMILY_AVATAR_ES_EVALUATION_CASES,
    FAMILY_AVATAR_EVALUATION_CASES,
    FAMILY_AVATAR_FR_EVALUATION_CASES,
    FAMILY_AVATAR_RU_EVALUATION_CASES,
    FOUNDATION_RAG_EVALUATION_CASES,
)
from app.modules.rag_evaluation.exceptions import BrainRagEvalConfigurationError
from app.modules.rag_evaluation.schemas import (
    BrainRagEvalCaseSet,
    BrainRagEvalConfig,
    BrainRagEvalPreflightResult,
    BrainRagEvalRunResult,
    RagEvaluationCase,
)
from app.modules.rag_evaluation.service import RagEvaluationService


SUPPORTED_BRAIN_RAG_EVAL_PROVIDERS = frozenset({"openai_compatible"})


def resolve_brain_rag_eval_cases(case_set: BrainRagEvalCaseSet) -> tuple[RagEvaluationCase, ...]:
    if case_set == "foundation":
        return FOUNDATION_RAG_EVALUATION_CASES
    if case_set == "eternal_world":
        return ETERNAL_WORLD_RAG_EVALUATION_CASES
    if case_set == "family_avatar":
        return FAMILY_AVATAR_EVALUATION_CASES
    if case_set == "family_avatar_cs":
        return FAMILY_AVATAR_CS_EVALUATION_CASES
    if case_set == "family_avatar_ru":
        return FAMILY_AVATAR_RU_EVALUATION_CASES
    if case_set == "family_avatar_en":
        return FAMILY_AVATAR_EN_EVALUATION_CASES
    if case_set == "family_avatar_es":
        return FAMILY_AVATAR_ES_EVALUATION_CASES
    if case_set == "family_avatar_fr":
        return FAMILY_AVATAR_FR_EVALUATION_CASES
    if case_set == "all":
        return ALL_RAG_EVALUATION_CASES

    raise BrainRagEvalConfigurationError(f"Unsupported Brain RAG eval case set: {case_set}")


def _validate_provider_configuration(
    *,
    provider_name: str,
    provider_settings: Settings,
) -> tuple[list[str], str | None]:
    issues: list[str] = []
    model: str | None = None

    if provider_name not in SUPPORTED_BRAIN_RAG_EVAL_PROVIDERS:
        issues.append(
            "Brain RAG eval requires a real Brain provider. "
            f"Supported values: {', '.join(sorted(SUPPORTED_BRAIN_RAG_EVAL_PROVIDERS))}."
        )
        return issues, model

    if provider_name == "openai_compatible":
        if not provider_settings.ai_brain_model:
            issues.append("AI_BRAIN_MODEL is required for openai_compatible Brain RAG eval.")
        else:
            model = provider_settings.ai_brain_model

        api_key_secret = provider_settings.ai_brain_api_key
        api_key = api_key_secret.get_secret_value() if api_key_secret is not None else ""
        if not api_key:
            issues.append("AI_BRAIN_API_KEY is required for openai_compatible Brain RAG eval.")

        if not provider_settings.ai_brain_base_url:
            issues.append("AI_BRAIN_BASE_URL is required for openai_compatible Brain RAG eval.")

    return issues, model


def build_brain_rag_eval_provider(
    *,
    provider_name: str,
    provider_settings: Settings | None = None,
) -> BrainAgentProvider:
    resolved_settings = provider_settings or settings
    normalized_provider_name = provider_name.strip().lower()

    if normalized_provider_name not in SUPPORTED_BRAIN_RAG_EVAL_PROVIDERS:
        raise BrainRagEvalConfigurationError(
            "Brain RAG eval does not support provider "
            f"'{normalized_provider_name}'. "
            f"Allowed: {', '.join(sorted(SUPPORTED_BRAIN_RAG_EVAL_PROVIDERS))}."
        )

    try:
        return build_brain_provider(
            provider_name=normalized_provider_name,
            provider_settings=resolved_settings,
        )
    except BrainProviderConfigurationError as exc:
        raise BrainRagEvalConfigurationError(str(exc)) from exc


def preflight_brain_rag_eval(
    config: BrainRagEvalConfig,
    *,
    provider_settings: Settings | None = None,
) -> BrainRagEvalPreflightResult:
    resolved_settings = provider_settings or settings
    cases = resolve_brain_rag_eval_cases(config.case_set)
    issues, model = _validate_provider_configuration(
        provider_name=config.provider_name,
        provider_settings=resolved_settings,
    )

    if not cases:
        issues.append("Selected case set is empty.")

    return BrainRagEvalPreflightResult(
        passed=not issues,
        provider_name=config.provider_name,
        model=model,
        case_set=config.case_set,
        case_count=len(cases),
        issues=issues,
    )


def run_brain_rag_eval(
    config: BrainRagEvalConfig,
    *,
    provider_settings: Settings | None = None,
    brain_service: BrainAgentService | None = None,
    cases: Sequence[RagEvaluationCase] | None = None,
) -> BrainRagEvalRunResult:
    preflight = preflight_brain_rag_eval(config, provider_settings=provider_settings)
    if not preflight.passed:
        raise BrainRagEvalConfigurationError(
            "Brain RAG eval preflight failed: " + "; ".join(preflight.issues)
        )

    resolved_cases = tuple(cases) if cases is not None else resolve_brain_rag_eval_cases(config.case_set)
    if not resolved_cases:
        raise BrainRagEvalConfigurationError("Brain RAG eval requires at least one case.")

    if brain_service is None:
        provider = build_brain_rag_eval_provider(
            provider_name=config.provider_name,
            provider_settings=provider_settings,
        )
        brain_service = BrainAgentService(provider=provider)

    evaluation_service = RagEvaluationService(brain_service=brain_service)
    suite_result = evaluation_service.run_eval_suite(resolved_cases)

    run_id = datetime.now(UTC).strftime("%Y%m%d_%H%M%SZ")
    passed = suite_result.failed_cases == 0
    result = BrainRagEvalRunResult(
        run_id=run_id,
        passed=passed,
        case_set=config.case_set,
        provider_name=config.provider_name,
        model=preflight.model,
        suite_result=suite_result,
    )

    if config.write_artifacts and config.artifact_dir is not None:
        result.artifact_paths = write_brain_rag_eval_artifacts(
            result=result,
            artifact_dir=config.artifact_dir,
        )

    return result
