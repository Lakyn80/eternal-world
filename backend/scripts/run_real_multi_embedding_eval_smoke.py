from __future__ import annotations

import argparse
import json
import os
import sys

from app.db.session import SessionLocal
from app.modules.real_multi_embedding_eval_smoke import (
    RealMultiEmbeddingEvalSmokeConfig,
    SMOKE_EMAIL,
    SMOKE_PROFILE_NAME,
    run_real_multi_embedding_eval_smoke,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the real multi-embedding evaluation smoke flow.")
    parser.add_argument("--email", default=SMOKE_EMAIL)
    parser.add_argument("--profile-name", default=SMOKE_PROFILE_NAME)
    parser.add_argument("--json", action="store_true", dest="json_output")
    parser.add_argument("--use-real-local-models", action="store_true")
    return parser


def _print_text_result(result) -> None:
    print(f"REAL MULTI-EMBEDDING SMOKE RESULT: {'PASS' if result.passed else 'FAIL'}")
    print()
    for candidate in result.candidates:
        print(f"candidate: {candidate.candidate}")
        print(f"status: {candidate.status}")
        print(f"collection: {candidate.collection}")
        print(f"metrics: {candidate.metrics}")
        print()

    best_model_code = None
    if isinstance(result.best_config, dict):
        best_model_code = result.best_config.get("best_model_code")
    print(f"best_config: {best_model_code}")
    print(f"activated: {str(result.activated).lower()}")
    print(f"runtime_active_config: {result.runtime_active_config}")
    print(f"used_fake_models: {str(result.used_fake_models).lower()}")
    if result.runtime_retrieval is not None:
        print(f"runtime_retrieval: {result.runtime_retrieval}")
    if result.warnings:
        print(f"warnings: {result.warnings}")
    if result.error:
        print(f"error: {result.error}")
    print(f"status: {'PASS' if result.passed else 'FAIL'}")


def main() -> int:
    args = _build_parser().parse_args()
    env_flag = os.getenv("REAL_MULTI_EMBEDDING_SMOKE_USE_REAL_LOCAL_MODELS", "").strip().lower()
    use_real_local_models = args.use_real_local_models or env_flag in {"1", "true", "yes", "on"}
    config = RealMultiEmbeddingEvalSmokeConfig(
        email=args.email,
        profile_name=args.profile_name,
        use_real_local_models=use_real_local_models,
    )

    db = SessionLocal()
    try:
        result = run_real_multi_embedding_eval_smoke(db, config)
    finally:
        db.close()

    if args.json_output:
        print(json.dumps(result.model_dump(mode="json"), indent=2, sort_keys=True))
    else:
        _print_text_result(result)

    return 0 if result.passed else 1


if __name__ == "__main__":
    sys.exit(main())
