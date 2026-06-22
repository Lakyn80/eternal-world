from __future__ import annotations

import argparse
import json
import sys

from app.db.session import SessionLocal
from app.modules.demo_smoke import DEMO_EMAIL, DEMO_PROFILE_NAME, DemoSmokeConfig, run_demo_smoke


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the backend E2E demo smoke flow.")
    parser.add_argument("--email", default=DEMO_EMAIL)
    parser.add_argument("--profile-name", default=DEMO_PROFILE_NAME)
    parser.add_argument("--json", action="store_true", dest="json_output")
    parser.add_argument("--timeout-seconds", type=float, default=120.0)
    parser.add_argument("--poll-interval-seconds", type=float, default=2.0)
    return parser


def _print_text_result(result) -> None:
    print(f"E2E DEMO SMOKE RESULT: {'PASS' if result.passed else 'FAIL'}")
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
    config = DemoSmokeConfig(
        email=args.email,
        profile_name=args.profile_name,
        timeout_seconds=args.timeout_seconds,
        poll_interval_seconds=args.poll_interval_seconds,
    )

    db = SessionLocal()
    try:
        result = run_demo_smoke(db, config)
    finally:
        db.close()

    if args.json_output:
        print(json.dumps(result.model_dump(mode="json"), indent=2, sort_keys=True))
    else:
        _print_text_result(result)

    return 0 if result.passed else 1


if __name__ == "__main__":
    sys.exit(main())
