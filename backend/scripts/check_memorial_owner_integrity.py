"""Read-only Phase 5A preflight: memorial active-owner integrity.

Exit codes:
  0 — no findings (or only --allow-zero-owner findings when that flag is set)
  1 — integrity findings present
  2 — unexpected error

Does not mutate data.
"""

from __future__ import annotations

import argparse
import json
import sys

from app.db.session import SessionLocal
from app.modules.memorial_access.owner_integrity import check_memorial_owner_integrity


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON instead of text lines.",
    )
    parser.add_argument(
        "--allow-zero-owner",
        action="store_true",
        help=(
            "Treat zero-active-owner findings as non-fatal (legacy "
            "/api/memory-profiles rows that self-heal on first capability access). "
            "Multiple owners and owner/profile mismatches always fail."
        ),
    )
    args = parser.parse_args(argv)

    db = SessionLocal()
    try:
        report = check_memorial_owner_integrity(db)
    except Exception as exc:  # noqa: BLE001 - ops script must exit cleanly
        print(f"[check_memorial_owner_integrity] ERROR {exc}", flush=True)
        return 2
    finally:
        db.close()

    blocking = [
        item
        for item in report.findings
        if not (args.allow_zero_owner and item.code == "zero_active_owners")
    ]
    passed = not blocking

    if args.json:
        payload = report.to_dict()
        payload["passed"] = passed
        payload["allow_zero_owner"] = args.allow_zero_owner
        payload["blocking_findings"] = [
            {"code": item.code, "profile_id": item.profile_id, "detail": item.detail} for item in blocking
        ]
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(
            f"[check_memorial_owner_integrity] profiles={report.profile_count} "
            f"zero={report.zero_owner_count} multi={report.multi_owner_count} "
            f"mismatch={report.mismatch_count} passed={passed}",
            flush=True,
        )
        for item in report.findings:
            fatal = item in blocking
            print(
                f"  [{'FAIL' if fatal else 'WARN'}] {item.code} profile_id={item.profile_id} {item.detail}",
                flush=True,
            )

    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
