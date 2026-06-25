from __future__ import annotations

import argparse
import json
import os
import sys

from app.core.config import BACKEND_DIR
from app.db.session import SessionLocal
from app.modules.real_question_eval import (
    REAL_QUESTION_EVAL_EMAIL,
    REAL_QUESTION_EVAL_HISTORICAL_PROVIDERS,
    REAL_QUESTION_EVAL_INCREMENTAL_NEW_PROVIDER_CODES,
    REAL_QUESTION_EVAL_PROFILE_NAME,
    RealQuestionEvalConfig,
    run_real_question_eval,
)


FAKE_EVAL_EXECUTION_MODE = "fake_eval"
REAL_EVAL_EXECUTION_MODE = "real_eval"
INCREMENTAL_REAL_EVAL_EXECUTION_MODE = "incremental_real_eval"


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the real question-based embedding evaluation flow.")
    parser.add_argument("--email", default=REAL_QUESTION_EVAL_EMAIL)
    parser.add_argument("--profile-name", default=REAL_QUESTION_EVAL_PROFILE_NAME)
    parser.add_argument(
        "--artifact-dir",
        default=str(BACKEND_DIR / "artifacts" / "real_question_eval"),
    )
    parser.add_argument("--json", action="store_true", dest="json_output")
    parser.add_argument("--use-real-local-models", action="store_true")
    parser.add_argument("--incremental-real-providers")
    return parser


def _is_truthy_env_flag(raw_value: str | None) -> bool:
    return (raw_value or "").strip().lower() in {"1", "true", "yes", "on"}


def _parse_incremental_real_providers(raw_value: str | None) -> list[str] | None:
    if raw_value is None:
        return None

    parsed_values = [
        item.strip().lower()
        for item in raw_value.split(",")
        if item.strip()
    ]
    if not parsed_values:
        raise ValueError("Incremental real evaluation requires a non-empty provider list.")

    deduplicated_values: list[str] = []
    seen: set[str] = set()
    for item in parsed_values:
        if item in seen:
            continue
        seen.add(item)
        deduplicated_values.append(item)

    return deduplicated_values


def resolve_real_question_eval_execution_mode(
    *,
    cli_use_real_local_models: bool,
    env_use_real_local_models: str | None,
    incremental_real_providers_raw: str | None = None,
) -> tuple[str, bool, list[str] | None]:
    env_enabled = _is_truthy_env_flag(env_use_real_local_models)
    incremental_real_providers = _parse_incremental_real_providers(incremental_real_providers_raw)
    if incremental_real_providers is not None:
        if not env_enabled:
            raise ValueError(
                "Incremental real evaluation requires REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1."
            )
        historical_overlap = [
            item for item in incremental_real_providers if item in REAL_QUESTION_EVAL_HISTORICAL_PROVIDERS
        ]
        if historical_overlap:
            raise ValueError(
                "Incremental real evaluation must not rerun historical providers: "
                + ", ".join(historical_overlap)
            )
        unsupported_providers = [
            item
            for item in incremental_real_providers
            if item not in REAL_QUESTION_EVAL_INCREMENTAL_NEW_PROVIDER_CODES
        ]
        if unsupported_providers:
            raise ValueError(
                "Incremental real evaluation only supports: "
                + ", ".join(REAL_QUESTION_EVAL_INCREMENTAL_NEW_PROVIDER_CODES)
                + ". Unsupported: "
                + ", ".join(unsupported_providers)
            )
        return INCREMENTAL_REAL_EVAL_EXECUTION_MODE, True, incremental_real_providers
    if cli_use_real_local_models and not env_enabled:
        raise ValueError(
            "Real-local evaluation is manual-only and requires BOTH --use-real-local-models "
            "and REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1."
        )
    if env_enabled and not cli_use_real_local_models:
        raise ValueError(
            "REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1 was set without --use-real-local-models. "
            "Real-local evaluation is manual-only and requires BOTH signals."
        )
    if cli_use_real_local_models and env_enabled:
        return REAL_EVAL_EXECUTION_MODE, True, None
    return FAKE_EVAL_EXECUTION_MODE, False, None


def _print_text_result(result) -> None:
    print(f"REAL QUESTION EVAL RESULT: {'PASS' if result.passed else 'FAIL'}")
    print()
    print(f"dataset: {result.dataset_name} ({result.dataset_id})")
    print(f"overall_winner: {result.overall_winner_model_code}")
    print(f"execution_mode: {result.execution_mode}")
    print(f"used_fake_models: {str(result.used_fake_models).lower()}")
    if result.historical_providers:
        print(f"historical_providers: {result.historical_providers}")
    if result.new_real_providers:
        print(f"new_real_providers: {result.new_real_providers}")
    if result.historical_overall_winner_model_code:
        print(f"historical_overall_winner: {result.historical_overall_winner_model_code}")
    if result.any_new_provider_beat_historical_winner is not None:
        print(
            "any_new_provider_beat_historical_winner: "
            f"{str(result.any_new_provider_beat_historical_winner).lower()}"
        )
    print(f"activated: {str(result.activated).lower()}")
    print(f"runtime_verified: {str(result.runtime_verified).lower()}")
    print(f"latest_markdown_report: {result.artifact_paths.latest_markdown_report}")
    print(f"latest_json_result: {result.artifact_paths.latest_json_result}")
    print(f"archived_markdown_report: {result.artifact_paths.archived_markdown_report}")
    print(f"archived_json_result: {result.artifact_paths.archived_json_result}")
    print()

    for question_result in result.question_results:
        print(f"question: {question_result.question_id}")
        print(f"winner: {question_result.winner_model_code}")
        print(f"reason: {question_result.winner_reason}")
        for model_result in question_result.model_results:
            print(
                "  "
                f"{model_result.model_code}: coverage={model_result.evidence_coverage} "
                f"matched={model_result.matched_expected_markers} "
                f"missing={model_result.missing_expected_markers} "
                f"distractors={model_result.false_positive_markers}"
            )
        print()

    if result.error:
        print(f"error: {result.error}")
    print(f"status: {'PASS' if result.passed else 'FAIL'}")


def main() -> int:
    args = _build_parser().parse_args()
    try:
        execution_mode, use_real_local_models, incremental_real_providers = resolve_real_question_eval_execution_mode(
            cli_use_real_local_models=args.use_real_local_models,
            env_use_real_local_models=os.getenv("REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS"),
            incremental_real_providers_raw=args.incremental_real_providers,
        )
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    config = RealQuestionEvalConfig(
        email=args.email,
        profile_name=args.profile_name,
        artifact_dir=args.artifact_dir,
        use_real_local_models=use_real_local_models,
        candidate_model_codes=incremental_real_providers,
        run_type_override="incremental_real" if execution_mode == INCREMENTAL_REAL_EVAL_EXECUTION_MODE else None,
        execution_mode_override=execution_mode if execution_mode == INCREMENTAL_REAL_EVAL_EXECUTION_MODE else None,
    )

    db = SessionLocal()
    try:
        result = run_real_question_eval(db, config)
    finally:
        db.close()

    result.execution_mode = execution_mode

    if args.json_output:
        print(json.dumps(result.model_dump(mode="json"), indent=2, sort_keys=True))
    else:
        _print_text_result(result)

    return 0 if result.passed else 1


if __name__ == "__main__":
    sys.exit(main())
