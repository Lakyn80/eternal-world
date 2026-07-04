from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

from app.db.session import SessionLocal
from app.modules.real_question_eval.schemas import RealQuestionEvalConfig
from app.modules.real_question_eval.service import RealQuestionEvalRunner


SAMPLE_DATASET = Path("app/modules/real_question_eval/datasets/eternal_world_eval_dataset_sample.json")
PACKAGE_ROOT = Path("/packages/rag-embedding-benchmark")
if not PACKAGE_ROOT.exists():
    PACKAGE_ROOT = Path(__file__).resolve().parents[2] / "packages" / "rag-embedding-benchmark"


def _resolve_database_url() -> str:
    import os

    return os.environ.get(
        "DATABASE_URL",
        "postgresql+psycopg://eternal_user:eternal_password@db:5432/eternal_world",
    )


def _resolve_qdrant_url() -> str:
    import os

    return os.environ.get("QDRANT_URL", "http://qdrant:6333")


def prepare_smoke_corpus() -> tuple[int, int]:
    db = SessionLocal()
    try:
        runner = RealQuestionEvalRunner(
            db,
            RealQuestionEvalConfig(
                dataset_path=SAMPLE_DATASET,
                write_artifacts=False,
            ),
        )
        user = runner.ensure_user()
        profile = runner.ensure_profile(user)
        source = runner.ensure_source(user, profile)
        runner.prepare_eval_source_chunks(user=user, source=source)
        db.commit()
        return source.id, profile.id
    finally:
        db.close()


def write_smoke_config(*, source_id: int, profile_id: int, config_path: Path) -> None:
    dataset_path = Path("/app") / SAMPLE_DATASET
    if not dataset_path.exists():
        dataset_path = (Path(__file__).resolve().parent.parent / SAMPLE_DATASET).resolve()

    smoke_config = {
        "device": "cpu",
        "artifact_dir": "/app/artifacts/rag_eval_smoke",
        "backend": "sql_qdrant",
        "database_url": _resolve_database_url(),
        "qdrant_url": _resolve_qdrant_url(),
        "collection_prefix": "rag_eval_smoke",
        "source_id": source_id,
        "profile_id": profile_id,
        "dataset": str(dataset_path),
        "top_k": 5,
        "models": {
            "default": ["multilingual_e5_small", "paraphrase_multilingual_mpnet_base_v2"],
            "include_optional": False,
        },
        "sql_qdrant": {
            "chunks_table": "rag_chunks",
            "columns": {
                "id": "id",
                "source_id": "source_id",
                "chunk_text": "chunk_text",
                "chunk_metadata": "chunk_metadata",
                "validation_status": "validation_status",
            },
            "invalid_statuses": ["invalid"],
        },
    }
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(yaml.safe_dump(smoke_config, sort_keys=False), encoding="utf-8")


def install_rag_eval_package() -> None:
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-q",
            "-e",
            f"{PACKAGE_ROOT}[sql-qdrant]",
        ]
    )


def run_rag_eval_command(*, command: str, config_path: Path) -> int:
    completed = subprocess.run(["rag-eval", command, "--config", str(config_path)], check=False)
    return completed.returncode


def main() -> int:
    print("Preparing smoke eval corpus...")
    source_id, profile_id = prepare_smoke_corpus()
    print(f"Using source_id={source_id}, profile_id={profile_id}")

    config_path = Path("/app/artifacts/rag_eval_smoke_config.yaml")
    write_smoke_config(source_id=source_id, profile_id=profile_id, config_path=config_path)
    print(f"Wrote smoke config: {config_path}")

    print("Installing rag-embedding-benchmark package...")
    install_rag_eval_package()

    print("Running rag-eval validate...")
    validate_exit_code = run_rag_eval_command(command="validate", config_path=config_path)
    if validate_exit_code != 0:
        print("rag-eval validate failed")
        return validate_exit_code

    print("Running rag-eval run...")
    run_exit_code = run_rag_eval_command(command="run", config_path=config_path)
    if run_exit_code != 0:
        print("rag-eval run failed")
        return run_exit_code

    ranking_path = Path("/app/artifacts/rag_eval_smoke/ranking.json")
    ranking_payload = json.loads(ranking_path.read_text(encoding="utf-8"))
    winner = ranking_payload.get("winner") or {}
    if not winner.get("model_code"):
        failed_models = ranking_payload.get("failed_models") or []
        print(f"Smoke test failed: no winner selected. failed_models={failed_models}")
        return 1

    print(f"Smoke test passed. Winner: {winner['model_code']}")
    print(f"Ranking artifact: {ranking_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
