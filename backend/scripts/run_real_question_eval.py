from __future__ import annotations

import argparse
import json
import os
import sys

from app.core.config import BACKEND_DIR
from app.db.session import SessionLocal
from app.modules.real_question_eval import (
    REAL_QUESTION_EVAL_EMAIL,
    REAL_QUESTION_EVAL_PROFILE_NAME,
    RealQuestionEvalConfig,
    run_real_question_eval,
)


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
    return parser


def _print_text_result(result) -> None:
    print(f"REAL QUESTION EVAL RESULT: {'PASS' if result.passed else 'FAIL'}")
    print()
    print(f"dataset: {result.dataset_name} ({result.dataset_id})")
    print(f"overall_winner: {result.overall_winner_model_code}")
    print(f"used_fake_models: {str(result.used_fake_models).lower()}")
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
    env_flag = os.getenv("REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS", "").strip().lower()
    use_real_local_models = args.use_real_local_models or env_flag in {"1", "true", "yes", "on"}
    config = RealQuestionEvalConfig(
        email=args.email,
        profile_name=args.profile_name,
        artifact_dir=args.artifact_dir,
        use_real_local_models=use_real_local_models,
    )

    db = SessionLocal()
    try:
        result = run_real_question_eval(db, config)
    finally:
        db.close()

    if args.json_output:
        print(json.dumps(result.model_dump(mode="json"), indent=2, sort_keys=True))
    else:
        _print_text_result(result)

    return 0 if result.passed else 1


if __name__ == "__main__":
    sys.exit(main())
