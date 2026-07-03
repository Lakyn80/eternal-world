from __future__ import annotations

import argparse
import json
import os
import sys

from app.core.config import BACKEND_DIR
from app.db.session import SessionLocal
from app.modules.real_question_eval import (
    REAL_QUESTION_EVAL_EMAIL,
    REAL_QUESTION_EVAL_FULL_VERSION_BATCH_A_BASELINE_PROVIDER,
    REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_BASELINE_PROVIDER,
    REAL_QUESTION_EVAL_FULL_VERSION_BATCH_C_BASELINE_PROVIDER,
    REAL_QUESTION_EVAL_FULL_VERSION_BATCH_D_BASELINE_PROVIDER,
    REAL_QUESTION_EVAL_HISTORICAL_PROVIDERS,
    REAL_QUESTION_EVAL_INCREMENTAL_NEW_PROVIDER_CODES,
    REAL_QUESTION_EVAL_PROFILE_NAME,
    RealQuestionEvalConfig,
    run_real_question_eval,
)


FAKE_EVAL_EXECUTION_MODE = "fake_eval"
REAL_EVAL_EXECUTION_MODE = "real_eval"
INCREMENTAL_REAL_EVAL_EXECUTION_MODE = "incremental_real_eval"
FULL_VERSION_BATCH_A_REAL_EVAL_EXECUTION_MODE = "full_version_batch_a_real_eval"
FULL_VERSION_BATCH_B_REAL_EVAL_EXECUTION_MODE = "full_version_batch_b_real_eval"
FULL_VERSION_BATCH_C_REAL_EVAL_EXECUTION_MODE = "full_version_batch_c_real_eval"
FULL_VERSION_BATCH_D_REAL_EVAL_EXECUTION_MODE = "full_version_batch_d_real_eval"
FULL_VERSION_BATCH_E_REAL_EVAL_EXECUTION_MODE = "full_version_batch_e_real_eval"
FULL_VERSION_BATCH_F_REAL_EVAL_EXECUTION_MODE = "full_version_batch_f_real_eval"


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the real question-based embedding evaluation flow.")
    parser.add_argument("--email", default=REAL_QUESTION_EVAL_EMAIL)
    parser.add_argument("--profile-name", default=REAL_QUESTION_EVAL_PROFILE_NAME)
    parser.add_argument(
        "--artifact-dir",
        default=str(BACKEND_DIR / "artifacts" / "real_question_eval"),
    )
    parser.add_argument("--dataset-file")
    parser.add_argument("--json", action="store_true", dest="json_output")
    parser.add_argument("--use-real-local-models", action="store_true")
    parser.add_argument("--incremental-real-providers")
    parser.add_argument("--full-version-batch-a-providers")
    parser.add_argument("--full-version-batch-b-providers")
    parser.add_argument("--full-version-batch-c-providers")
    parser.add_argument("--full-version-batch-d-providers")
    parser.add_argument("--full-version-batch-e-providers")
    parser.add_argument("--full-version-batch-f-providers")
    parser.add_argument("--rerun-attempted-full-version-batch-b", action="store_true")
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


def resolve_full_version_batch_a_providers(
    *,
    cli_use_real_local_models: bool,
    env_use_real_local_models: str | None,
    full_version_batch_a_providers_raw: str | None,
) -> list[str] | None:
    batch_a_providers = _parse_incremental_real_providers(full_version_batch_a_providers_raw)
    if batch_a_providers is None:
        return None

    if not cli_use_real_local_models or not _is_truthy_env_flag(env_use_real_local_models):
        raise ValueError(
            "Full-version Batch A is manual-only and requires BOTH --use-real-local-models "
            "and REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1."
        )
    if batch_a_providers != ["multilingual_e5_large"]:
        raise ValueError(
            "Full-version Batch A requires the explicit provider list: multilingual_e5_large."
        )

    return batch_a_providers


def resolve_full_version_batch_b_providers(
    *,
    cli_use_real_local_models: bool,
    env_use_real_local_models: str | None,
    full_version_batch_b_providers_raw: str | None,
    rerun_attempted_full_version_batch_b: bool = False,
) -> list[str] | None:
    batch_b_providers = _parse_incremental_real_providers(full_version_batch_b_providers_raw)
    if batch_b_providers is None:
        return None

    if not rerun_attempted_full_version_batch_b:
        raise ValueError(
            "Full-version Batch B is closed in this environment by default. "
            "Qwen3 0.6B was attempted but not completed and requires "
            "--rerun-attempted-full-version-batch-b for one explicit guarded rerun."
        )
    if not cli_use_real_local_models or not _is_truthy_env_flag(env_use_real_local_models):
        raise ValueError(
            "Full-version Batch B rerun is manual-only and requires BOTH --use-real-local-models "
            "and REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1."
        )
    if batch_b_providers != ["qwen3_embedding_0_6b"]:
        raise ValueError(
            "Full-version Batch B requires the explicit provider list: qwen3_embedding_0_6b."
        )

    return batch_b_providers


def resolve_full_version_batch_c_providers(
    *,
    cli_use_real_local_models: bool,
    env_use_real_local_models: str | None,
    full_version_batch_c_providers_raw: str | None,
) -> list[str] | None:
    batch_c_providers = _parse_incremental_real_providers(full_version_batch_c_providers_raw)
    if batch_c_providers is None:
        return None

    if not cli_use_real_local_models or not _is_truthy_env_flag(env_use_real_local_models):
        raise ValueError(
            "Full-version Batch C is manual-only and requires BOTH --use-real-local-models "
            "and REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1."
        )
    if batch_c_providers != ["jina_embeddings_v3"]:
        raise ValueError(
            "Full-version Batch C requires the explicit provider list: jina_embeddings_v3."
        )

    return batch_c_providers


def resolve_full_version_batch_d_providers(
    *,
    cli_use_real_local_models: bool,
    env_use_real_local_models: str | None,
    full_version_batch_d_providers_raw: str | None,
) -> list[str] | None:
    batch_d_providers = _parse_incremental_real_providers(full_version_batch_d_providers_raw)
    if batch_d_providers is None:
        return None

    if not cli_use_real_local_models or not _is_truthy_env_flag(env_use_real_local_models):
        raise ValueError(
            "Full-version Batch D is manual-only and requires BOTH --use-real-local-models "
            "and REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1."
        )
    if batch_d_providers != ["bge_m3_dense_sparse", "bge_m3_dense_sparse_multivector"]:
        raise ValueError(
            "Full-version Batch D requires the explicit provider list: "
            "bge_m3_dense_sparse,bge_m3_dense_sparse_multivector."
        )

    return batch_d_providers


def resolve_full_version_batch_e_providers(
    *,
    cli_use_real_local_models: bool,
    env_use_real_local_models: str | None,
    full_version_batch_e_providers_raw: str | None,
) -> list[str] | None:
    batch_e_providers = _parse_incremental_real_providers(full_version_batch_e_providers_raw)
    if batch_e_providers is None:
        return None

    if not cli_use_real_local_models or not _is_truthy_env_flag(env_use_real_local_models):
        raise ValueError(
            "Full-version Batch E is manual-only and requires BOTH --use-real-local-models "
            "and REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1."
        )
    if batch_e_providers != ["qwen3_embedding_4b"]:
        raise ValueError(
            "Full-version Batch E requires the explicit provider list: qwen3_embedding_4b."
        )

    return batch_e_providers


def resolve_full_version_batch_f_providers(
    *,
    cli_use_real_local_models: bool,
    env_use_real_local_models: str | None,
    full_version_batch_f_providers_raw: str | None,
) -> list[str] | None:
    batch_f_providers = _parse_incremental_real_providers(full_version_batch_f_providers_raw)
    if batch_f_providers is None:
        return None

    if not cli_use_real_local_models or not _is_truthy_env_flag(env_use_real_local_models):
        raise ValueError(
            "Full-version Batch F is manual-only and requires BOTH --use-real-local-models "
            "and REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1."
        )
    if batch_f_providers != ["qwen3_embedding_8b"]:
        raise ValueError(
            "Full-version Batch F requires the explicit provider list: qwen3_embedding_8b."
        )

    return batch_f_providers


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
    print(f"REAL QUESTION EVAL RESULT: {result.quality_status or ('PASS' if result.passed else 'FAIL')}")
    print()
    print(f"dataset: {result.dataset_name} ({result.dataset_id})")
    print(f"run_status: {result.run_status or 'unknown'}")
    print(f"quality_status: {result.quality_status or ('PASS' if result.passed else 'FAIL')}")
    if result.quality_gate is not None:
        print(
            "quality_gate: "
            f"{result.quality_gate.gate_name}>={result.quality_gate.threshold:.4f} "
            f"best={result.quality_gate.best_model_code or 'none'} "
            f"pass_rate={result.quality_gate.best_pass_rate:.4f}"
        )
    print(f"overall_winner: {result.overall_winner_model_code}")
    if result.overall_winner_reason:
        print(f"overall_winner_reason: {result.overall_winner_reason}")
    if result.preflight_validation is not None:
        print(
            "preflight_validation: "
            f"{'PASS' if result.preflight_validation.passed else 'FAIL'} "
            f"missing_marker_count={result.preflight_validation.missing_marker_count}"
        )
    print(f"execution_mode: {result.execution_mode}")
    print(f"used_fake_models: {str(result.used_fake_models).lower()}")
    if result.benchmark_batch_label:
        print(f"benchmark_batch_label: {result.benchmark_batch_label}")
    if result.baseline_provider_codes:
        print(f"baseline_provider_codes: {result.baseline_provider_codes}")
    if result.newly_evaluated_provider_codes:
        print(f"newly_evaluated_provider_codes: {result.newly_evaluated_provider_codes}")
    if result.excluded_provider_codes:
        print(f"excluded_provider_codes: {result.excluded_provider_codes}")
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
    print(f"latest_markdown_summary: {result.artifact_paths.latest_markdown_summary}")
    print(f"latest_json_summary: {result.artifact_paths.latest_json_summary}")
    print(f"archived_markdown_report: {result.artifact_paths.archived_markdown_report}")
    print(f"archived_json_result: {result.artifact_paths.archived_json_result}")
    print(f"archived_markdown_summary: {result.artifact_paths.archived_markdown_summary}")
    print(f"archived_json_summary: {result.artifact_paths.archived_json_summary}")
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
    print(f"status: {result.quality_status or ('PASS' if result.passed else 'FAIL')}")


def _run_with_config(*, args, config: RealQuestionEvalConfig, execution_mode: str) -> int:
    db = SessionLocal()
    try:
        result = run_real_question_eval(db, config)
    finally:
        db.close()

    result.execution_mode = execution_mode
    if execution_mode == FULL_VERSION_BATCH_D_REAL_EVAL_EXECUTION_MODE:
        result.baseline_provider_codes = [REAL_QUESTION_EVAL_FULL_VERSION_BATCH_D_BASELINE_PROVIDER]
        result.newly_evaluated_provider_codes = [
            "bge_m3_dense_sparse",
            "bge_m3_dense_sparse_multivector",
        ]
    if execution_mode == FULL_VERSION_BATCH_E_REAL_EVAL_EXECUTION_MODE:
        result.baseline_provider_codes = [REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_BASELINE_PROVIDER]
        result.newly_evaluated_provider_codes = ["qwen3_embedding_4b"]
    if execution_mode == FULL_VERSION_BATCH_F_REAL_EVAL_EXECUTION_MODE:
        result.baseline_provider_codes = [REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_BASELINE_PROVIDER]
        result.newly_evaluated_provider_codes = ["qwen3_embedding_8b"]
    if execution_mode == FULL_VERSION_BATCH_C_REAL_EVAL_EXECUTION_MODE:
        result.baseline_provider_codes = [REAL_QUESTION_EVAL_FULL_VERSION_BATCH_C_BASELINE_PROVIDER]
        result.newly_evaluated_provider_codes = ["jina_embeddings_v3"]
    if execution_mode == FULL_VERSION_BATCH_B_REAL_EVAL_EXECUTION_MODE:
        result.baseline_provider_codes = [REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_BASELINE_PROVIDER]
        result.newly_evaluated_provider_codes = ["qwen3_embedding_0_6b"]
    if execution_mode == FULL_VERSION_BATCH_A_REAL_EVAL_EXECUTION_MODE:
        result.baseline_provider_codes = [REAL_QUESTION_EVAL_FULL_VERSION_BATCH_A_BASELINE_PROVIDER]
        result.newly_evaluated_provider_codes = ["multilingual_e5_large"]

    if args.json_output:
        print(json.dumps(result.model_dump(mode="json"), indent=2, sort_keys=True))
    else:
        _print_text_result(result)

    return 0 if result.passed else 1


def main() -> int:
    args = _build_parser().parse_args()
    env_use_real_local_models = os.getenv("REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS")
    try:
        batch_a_providers = resolve_full_version_batch_a_providers(
            cli_use_real_local_models=args.use_real_local_models,
            env_use_real_local_models=env_use_real_local_models,
            full_version_batch_a_providers_raw=args.full_version_batch_a_providers,
        )
        batch_b_providers = resolve_full_version_batch_b_providers(
            cli_use_real_local_models=args.use_real_local_models,
            env_use_real_local_models=env_use_real_local_models,
            full_version_batch_b_providers_raw=args.full_version_batch_b_providers,
            rerun_attempted_full_version_batch_b=args.rerun_attempted_full_version_batch_b,
        )
        batch_c_providers = resolve_full_version_batch_c_providers(
            cli_use_real_local_models=args.use_real_local_models,
            env_use_real_local_models=env_use_real_local_models,
            full_version_batch_c_providers_raw=args.full_version_batch_c_providers,
        )
        batch_d_providers = resolve_full_version_batch_d_providers(
            cli_use_real_local_models=args.use_real_local_models,
            env_use_real_local_models=env_use_real_local_models,
            full_version_batch_d_providers_raw=args.full_version_batch_d_providers,
        )
        batch_e_providers = resolve_full_version_batch_e_providers(
            cli_use_real_local_models=args.use_real_local_models,
            env_use_real_local_models=env_use_real_local_models,
            full_version_batch_e_providers_raw=args.full_version_batch_e_providers,
        )
        batch_f_providers = resolve_full_version_batch_f_providers(
            cli_use_real_local_models=args.use_real_local_models,
            env_use_real_local_models=env_use_real_local_models,
            full_version_batch_f_providers_raw=args.full_version_batch_f_providers,
        )
        manual_batch_count = sum(
            provider_list is not None
            for provider_list in (
                batch_a_providers,
                batch_b_providers,
                batch_c_providers,
                batch_d_providers,
                batch_e_providers,
                batch_f_providers,
            )
        )
        if manual_batch_count > 1:
            raise ValueError("Choose exactly one manual full-version batch mode at a time.")
        if batch_f_providers is not None:
            execution_mode = FULL_VERSION_BATCH_F_REAL_EVAL_EXECUTION_MODE
            use_real_local_models = True
            incremental_real_providers = None
        elif batch_e_providers is not None:
            execution_mode = FULL_VERSION_BATCH_E_REAL_EVAL_EXECUTION_MODE
            use_real_local_models = True
            incremental_real_providers = None
        elif batch_d_providers is not None:
            execution_mode = FULL_VERSION_BATCH_D_REAL_EVAL_EXECUTION_MODE
            use_real_local_models = True
            incremental_real_providers = None
        elif batch_c_providers is not None:
            execution_mode = FULL_VERSION_BATCH_C_REAL_EVAL_EXECUTION_MODE
            use_real_local_models = True
            incremental_real_providers = None
        elif batch_b_providers is not None:
            execution_mode = FULL_VERSION_BATCH_B_REAL_EVAL_EXECUTION_MODE
            use_real_local_models = True
            incremental_real_providers = None
        elif batch_a_providers is not None:
            execution_mode = FULL_VERSION_BATCH_A_REAL_EVAL_EXECUTION_MODE
            use_real_local_models = True
            incremental_real_providers = None
        else:
            execution_mode, use_real_local_models, incremental_real_providers = resolve_real_question_eval_execution_mode(
                cli_use_real_local_models=args.use_real_local_models,
                env_use_real_local_models=env_use_real_local_models,
                incremental_real_providers_raw=args.incremental_real_providers,
            )
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    config = RealQuestionEvalConfig(
        email=args.email,
        profile_name=args.profile_name,
        artifact_dir=args.artifact_dir,
        dataset_path=args.dataset_file,
        use_real_local_models=use_real_local_models,
        candidate_model_codes=(
            batch_f_providers
            or batch_e_providers
            or batch_d_providers
            or batch_c_providers
            or batch_b_providers
            or batch_a_providers
            or incremental_real_providers
        ),
        run_type_override=(
            "full_version_batch_f"
            if execution_mode == FULL_VERSION_BATCH_F_REAL_EVAL_EXECUTION_MODE
            else "full_version_batch_e"
            if execution_mode == FULL_VERSION_BATCH_E_REAL_EVAL_EXECUTION_MODE
            else "full_version_batch_d"
            if execution_mode == FULL_VERSION_BATCH_D_REAL_EVAL_EXECUTION_MODE
            else "full_version_batch_c"
            if execution_mode == FULL_VERSION_BATCH_C_REAL_EVAL_EXECUTION_MODE
            else "full_version_batch_b"
            if execution_mode == FULL_VERSION_BATCH_B_REAL_EVAL_EXECUTION_MODE
            else "full_version_batch_a"
            if execution_mode == FULL_VERSION_BATCH_A_REAL_EVAL_EXECUTION_MODE
            else "incremental_real"
            if execution_mode == INCREMENTAL_REAL_EVAL_EXECUTION_MODE
            else None
        ),
        execution_mode_override=(
            execution_mode
            if execution_mode
            in {
                FULL_VERSION_BATCH_F_REAL_EVAL_EXECUTION_MODE,
                FULL_VERSION_BATCH_E_REAL_EVAL_EXECUTION_MODE,
                FULL_VERSION_BATCH_D_REAL_EVAL_EXECUTION_MODE,
                FULL_VERSION_BATCH_C_REAL_EVAL_EXECUTION_MODE,
                FULL_VERSION_BATCH_A_REAL_EVAL_EXECUTION_MODE,
                FULL_VERSION_BATCH_B_REAL_EVAL_EXECUTION_MODE,
                INCREMENTAL_REAL_EVAL_EXECUTION_MODE,
            }
            else None
        ),
        rerun_attempted_full_version_batch_b=args.rerun_attempted_full_version_batch_b,
    )
    return _run_with_config(
        args=args,
        config=config,
        execution_mode=execution_mode,
    )


if __name__ == "__main__":
    sys.exit(main())
