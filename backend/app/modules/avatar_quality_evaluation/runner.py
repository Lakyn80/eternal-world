from __future__ import annotations

from datetime import UTC, datetime
from time import perf_counter
from uuid import uuid4

from sqlalchemy.orm import Session

from app.core.metrics import (
    observe_avatar_eval_case,
    observe_avatar_eval_duration,
    observe_avatar_eval_failure,
    observe_avatar_eval_ratios,
    observe_avatar_eval_run,
)
from app.modules.avatar_quality_evaluation.dataset_loader import load_avatar_eval_dataset
from app.modules.avatar_quality_evaluation.evaluator import (
    build_avatar_eval_summary,
    evaluate_avatar_answer,
)
from app.modules.avatar_quality_evaluation.reporting import attach_artifacts
from app.modules.avatar_quality_evaluation.schemas import (
    AvatarEvalAnswerInput,
    AvatarEvalCase,
    AvatarEvalCaseRunResult,
    AvatarEvalEvidence,
    AvatarEvalRunConfig,
    AvatarEvalRunManifest,
    AvatarEvalRunResult,
)
from app.modules.demo_fa_chat.service import run_demo_fa_chat_message


def _case_repeat_count(*, case: AvatarEvalCase, default_repeat_count: int) -> int:
    return case.repeat_count or default_repeat_count


def _build_trace_id(*, run_id: str, case_id: str, run_index: int) -> str:
    safe_case_id = "".join(char if char.isalnum() or char in {"-", "_"} else "-" for char in case_id)
    return f"avatar-eval-{run_id}-{safe_case_id}-{run_index}"


def _coerce_evidence(response) -> list[AvatarEvalEvidence]:
    return [
        AvatarEvalEvidence.model_validate(item.model_dump())
        for item in response.evidence
    ]


def _run_case_once(
    *,
    db: Session,
    case: AvatarEvalCase,
    profile_id: int | None,
    run_id: str,
    run_index: int,
) -> AvatarEvalCaseRunResult:
    trace_id = _build_trace_id(run_id=run_id, case_id=case.id, run_index=run_index)
    started_at = perf_counter()
    try:
        response = run_demo_fa_chat_message(
            db,
            profile_id=profile_id,
            message=case.question,
            debug=True,
            trace_id=trace_id,
        )
        duration = perf_counter() - started_at
        answer_input = AvatarEvalAnswerInput(
            answer=response.answer,
            trace_id=response.trace_id,
            evidence=_coerce_evidence(response),
            lack_of_evidence=response.lack_of_evidence,
            persona_applied=response.persona_applied,
            guard_applied=response.guard_applied,
            guard_reason=response.guard_reason,
            duration_seconds=duration,
            candidate_provenance=(
                response.memory_candidate.model_dump(mode="json")
                if response.memory_candidate is not None
                else {}
            ),
        )
        return evaluate_avatar_answer(
            case=case,
            answer_input=answer_input,
            run_index=run_index,
        )
    except Exception as exc:
        duration = perf_counter() - started_at
        return AvatarEvalCaseRunResult(
            case_id=case.id,
            category=case.category,
            run_index=run_index,
            passed=False,
            answer="",
            trace_id=trace_id,
            evidence_summary=[],
            dimensions=[],
            failure_types=["runtime_failure"],
            likely_layer="runtime",
            recommended_fix_layer="runtime_configuration",
            duration_seconds=duration,
            evaluator_error=f"{exc.__class__.__name__}: {str(exc)[:240]}",
        )


def _record_prometheus_metrics(results: list[AvatarEvalCaseRunResult]) -> None:
    summary = build_avatar_eval_summary(results)
    observe_avatar_eval_run(result="passed" if summary.failed_case_count == 0 else "failed")
    observe_avatar_eval_ratios(
        persona_consistency=summary.persona_consistency_rate,
        unsupported_detail=summary.unsupported_detail_rate,
        over_refusal=summary.over_refusal_rate,
    )
    for result in results:
        observe_avatar_eval_case(
            category=result.category,
            result="passed" if result.passed else "failed",
        )
        observe_avatar_eval_duration(duration_seconds=result.duration_seconds)
        for failure_type in result.failure_types:
            observe_avatar_eval_failure(failure_type=failure_type)


def run_avatar_quality_evaluation(
    *,
    db: Session,
    config: AvatarEvalRunConfig,
    write_artifacts: bool = True,
) -> AvatarEvalRunResult:
    started_at = datetime.now(UTC)
    run_id = datetime.now(UTC).strftime("%Y%m%d_%H%M%SZ") + "_" + uuid4().hex[:8]
    cases = load_avatar_eval_dataset(config.dataset_path)
    results: list[AvatarEvalCaseRunResult] = []
    for case in cases:
        for run_index in range(1, _case_repeat_count(case=case, default_repeat_count=config.repeat_count) + 1):
            results.append(
                _run_case_once(
                    db=db,
                    case=case,
                    profile_id=config.profile_id,
                    run_id=run_id,
                    run_index=run_index,
                )
            )

    _record_prometheus_metrics(results)
    completed_at = datetime.now(UTC)
    manifest = AvatarEvalRunManifest(
        run_id=run_id,
        run_label=config.run_label,
        dataset_path=str(config.dataset_path),
        output_dir=str(config.output_dir),
        repeat_count=config.repeat_count,
        started_at=started_at,
        completed_at=completed_at,
        real_fa_chat_path=True,
    )
    run_result = AvatarEvalRunResult(
        manifest=manifest,
        summary=build_avatar_eval_summary(results),
        results=results,
    )
    if not write_artifacts:
        return run_result
    return attach_artifacts(run_result=run_result, allow_overwrite=config.allow_overwrite)
