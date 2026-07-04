from __future__ import annotations

import argparse
import json
import sys

from app.db.session import SessionLocal
from app.modules.production_hybrid_smoke import (
    PRODUCTION_HYBRID_SMOKE_EMAIL,
    PRODUCTION_HYBRID_SMOKE_PROFILE_NAME,
    ProductionHybridSmokeConfig,
    run_production_hybrid_smoke,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run production hybrid retrieval smoke for bge_m3_dense_sparse.",
    )
    parser.add_argument("--email", default=PRODUCTION_HYBRID_SMOKE_EMAIL)
    parser.add_argument("--profile-name", default=PRODUCTION_HYBRID_SMOKE_PROFILE_NAME)
    parser.add_argument("--model-code", default="bge_m3_dense_sparse")
    parser.add_argument("--json", action="store_true", dest="json_output")
    return parser


def _print_text_result(result) -> None:
    print(f"PRODUCTION HYBRID SMOKE RESULT: {'PASS' if result.passed else 'FAIL'}")
    print()
    for stage in result.stages:
        status = "PASS" if stage.passed else "FAIL"
        print(f"[{status}] {stage.name}")
        if stage.details:
            print(f"  details: {stage.details}")
        if stage.error:
            print(f"  error: {stage.error}")


def main() -> int:
    args = _build_parser().parse_args()
    config = ProductionHybridSmokeConfig(
        email=args.email,
        profile_name=args.profile_name,
        model_code=args.model_code,
    )

    db = SessionLocal()
    try:
        result = run_production_hybrid_smoke(db, config)
    finally:
        db.close()

    if args.json_output:
        print(json.dumps(result.model_dump(mode="json"), indent=2, sort_keys=True))
    else:
        _print_text_result(result)

    return 0 if result.passed else 1


if __name__ == "__main__":
    sys.exit(main())
