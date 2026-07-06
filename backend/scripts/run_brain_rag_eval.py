from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from app.modules.rag_evaluation.brain_eval_runner import (
    preflight_brain_rag_eval,
    run_brain_rag_eval,
)
from app.modules.rag_evaluation.exceptions import BrainRagEvalConfigurationError, RagEvaluationError
from app.modules.rag_evaluation.schemas import BrainRagEvalCaseSet, BrainRagEvalConfig

DEFAULT_ARTIFACT_DIR = Path("artifacts/brain_rag_eval")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Run Brain Agent RAG Q&A evaluation against the configured "
            "openai_compatible provider (Task 61)."
        ),
    )
    parser.add_argument(
        "--case-set",
        choices=(
            "foundation",
            "eternal_world",
            "family_avatar",
            "family_avatar_cs",
            "family_avatar_ru",
            "family_avatar_en",
            "family_avatar_es",
            "family_avatar_fr",
            "all",
        ),
        default="foundation",
        help="Evaluation case set to run (default: foundation).",
    )
    parser.add_argument(
        "--artifact-dir",
        type=Path,
        default=DEFAULT_ARTIFACT_DIR,
        help=f"Directory for JSON/Markdown artifacts (default: {DEFAULT_ARTIFACT_DIR}).",
    )
    parser.add_argument(
        "--no-artifacts",
        action="store_true",
        help="Skip writing artifact files.",
    )
    parser.add_argument(
        "--preflight",
        action="store_true",
        help="Validate configuration and case set without calling the Brain provider.",
    )
    parser.add_argument("--json", action="store_true", dest="json_output")
    return parser


def _print_text_preflight(result) -> None:
    status = "PASS" if result.passed else "FAIL"
    print(f"BRAIN RAG EVAL PREFLIGHT: {status}")
    print(f"provider: {result.provider_name}")
    print(f"model: {result.model or 'unknown'}")
    print(f"case_set: {result.case_set}")
    print(f"case_count: {result.case_count}")
    for issue in result.issues:
        print(f"issue: {issue}")


def _print_text_result(result) -> None:
    print(f"BRAIN RAG EVAL RESULT: {'PASS' if result.passed else 'FAIL'}")
    print(f"run_id: {result.run_id}")
    print(f"provider: {result.provider_name}")
    print(f"model: {result.model or 'unknown'}")
    print(f"case_set: {result.case_set}")
    print(
        f"passed_cases: {result.suite_result.passed_cases}/"
        f"{result.suite_result.total_cases}"
    )
    print()
    for case_result in result.suite_result.results:
        status = "PASS" if case_result.passed else "FAIL"
        print(f"[{status}] {case_result.case_id}")
        print(f"  expected: {case_result.expected_behavior}")
        print(f"  actual: {case_result.actual_behavior}")
        if case_result.reasons:
            print(f"  reasons: {'; '.join(case_result.reasons)}")
    if result.artifact_paths:
        print()
        print("artifacts:")
        for key, path in sorted(result.artifact_paths.items()):
            print(f"  {key}: {path}")


def main() -> int:
    args = _build_parser().parse_args()
    case_set: BrainRagEvalCaseSet = args.case_set
    config = BrainRagEvalConfig(
        case_set=case_set,
        artifact_dir=args.artifact_dir,
        write_artifacts=not args.no_artifacts,
    )

    try:
        if args.preflight:
            preflight_result = preflight_brain_rag_eval(config)
            if args.json_output:
                print(json.dumps(preflight_result.model_dump(mode="json"), indent=2, sort_keys=True))
            else:
                _print_text_preflight(preflight_result)
            return 0 if preflight_result.passed else 1

        result = run_brain_rag_eval(config)
    except (BrainRagEvalConfigurationError, RagEvaluationError) as exc:
        print(f"BRAIN RAG EVAL ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json_output:
        print(json.dumps(result.model_dump(mode="json"), indent=2, sort_keys=True))
    else:
        _print_text_result(result)

    return 0 if result.passed else 1


if __name__ == "__main__":
    sys.exit(main())
