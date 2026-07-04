from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from rag_eval.adapters.factory import build_backend
from rag_eval.config import load_benchmark_config
from rag_eval.runner import run_benchmark, validate_benchmark


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare embedding models for RAG retrieval quality.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="Validate dataset schema and corpus alignment.")
    validate_parser.add_argument("--config", required=True, type=Path)

    run_parser = subparsers.add_parser("run", help="Run the embedding benchmark.")
    run_parser.add_argument("--config", required=True, type=Path)
    run_parser.add_argument("--backend-root", type=Path, default=None)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    config = load_benchmark_config(args.config)
    backend = build_backend(config, backend_root=str(args.backend_root) if getattr(args, "backend_root", None) else None)

    if args.command == "validate":
        validation = validate_benchmark(config=config, backend=backend)
        print(
            json.dumps(
                {
                    "passed": validation.passed,
                    "issue_count": validation.issue_count,
                    "issues": [
                        {
                            "question_id": issue.question_id,
                            "issue_code": issue.issue_code,
                            "marker": issue.marker,
                            "detail": issue.detail,
                        }
                        for issue in validation.issues
                    ],
                },
                indent=2,
            )
        )
        return 0 if validation.passed else 1

    if args.command == "run":
        result = run_benchmark(config=config, backend=backend)
        print(
            json.dumps(
                {
                    "run_id": result.run_id,
                    "dataset_id": result.dataset_id,
                    "winner_model_code": result.winner_model_code,
                    "winner_config_id": result.winner_config_id,
                    "failed_models": [
                        {"model_code": item.model_code, "status": item.status, "error": item.error}
                        for item in result.failed_models
                    ],
                    "artifact_paths": result.artifact_paths,
                },
                indent=2,
            )
        )
        return 0

    parser.error(f"Unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    sys.exit(main())
