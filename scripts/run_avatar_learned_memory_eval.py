from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
BACKEND_ROOT = REPO_ROOT / "backend"
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.db.session import SessionLocal  # noqa: E402
from app.modules.avatar_quality_evaluation.runner import run_avatar_quality_evaluation  # noqa: E402
from app.modules.avatar_quality_evaluation.schemas import AvatarEvalRunConfig  # noqa: E402


DEFAULT_DATASET = (
    BACKEND_ROOT
    / "app"
    / "modules"
    / "avatar_quality_evaluation"
    / "datasets"
    / "learned_memory_answer_eval_v1.jsonl"
)
DEFAULT_OUTPUT_DIR = (
    BACKEND_ROOT
    / "artifacts"
    / "avatar_quality_eval"
    / "runs"
    / "learned_memory_baseline"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the Task 64.4 learned-memory answer evaluation against the real FA chat path.",
    )
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--repeat-count", type=int, default=3)
    parser.add_argument("--profile-id", type=int, default=None)
    parser.add_argument("--run-label", default="baseline")
    parser.add_argument("--allow-overwrite", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = AvatarEvalRunConfig(
        dataset_path=args.dataset,
        output_dir=args.output_dir,
        repeat_count=args.repeat_count,
        profile_id=args.profile_id,
        run_label=args.run_label,
        allow_overwrite=args.allow_overwrite,
    )
    db = SessionLocal()
    try:
        result = run_avatar_quality_evaluation(db=db, config=config, write_artifacts=True)
    finally:
        db.close()

    print(
        json.dumps(
            {
                "run_id": result.manifest.run_id,
                "run_label": result.manifest.run_label,
                "evaluated_case_count": result.summary.evaluated_case_count,
                "total_runs": result.summary.total_runs,
                "passed_case_count": result.summary.passed_case_count,
                "failed_case_count": result.summary.failed_case_count,
                "artifact_paths": result.artifact_paths,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
