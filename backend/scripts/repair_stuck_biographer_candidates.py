"""Task 65.7C (Part E) - idempotent repair for AI Biographer candidates
whose oldest pending mandatory clarification has been genuinely abandoned
(see `app.modules.avatar_biographer.repair` for the full contract and
`PROJECT_PROGRESS.md`'s Task 65.7C entry for why this exists and why it
never runs automatically). Never approves, never indexes, never modifies
the biography, never calls a provider, never prints candidate content -
only safe metadata (candidate ID, profile ID, status transition, counts).

Safe by default: with no flags, this ALWAYS runs in dry-run mode (lists
matching candidates, changes nothing). Real repair requires the explicit
`--apply` flag - there is no way to accidentally mutate data by running
this script with no arguments.

Usage (inside the backend container):

    python scripts/repair_stuck_biographer_candidates.py
    python scripts/repair_stuck_biographer_candidates.py --profile-id 42
    python scripts/repair_stuck_biographer_candidates.py --min-age-hours 48
    python scripts/repair_stuck_biographer_candidates.py --apply
    python scripts/repair_stuck_biographer_candidates.py --apply --limit 20
"""

from __future__ import annotations

import argparse
import json

from app.db.session import SessionLocal
from app.modules.avatar_biographer.repair import (
    find_stuck_biographer_candidates,
    repair_stuck_biographer_candidates,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Repair AI Biographer candidates whose oldest pending mandatory "
            "clarification has been genuinely abandoned. Dry-run by default; "
            "pass --apply to actually repair."
        )
    )
    parser.add_argument("--profile-id", type=int, default=None, help="Limit to a single memorial profile ID.")
    parser.add_argument(
        "--min-age-hours",
        type=int,
        default=None,
        help="Override the configured minimum pending-clarification age (hours) before a candidate is considered stuck.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of candidates a single --apply run will repair (bounded batch size).",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually repair matching candidates. Without this flag, the script only lists what it would do.",
    )
    return parser


def main() -> int:
    args = _build_parser().parse_args()
    db = SessionLocal()
    try:
        if not args.apply:
            candidates = find_stuck_biographer_candidates(
                db, profile_id=args.profile_id, min_age_hours=args.min_age_hours
            )
            if args.limit is not None:
                candidates = candidates[: args.limit]
            result = [
                {
                    "candidate_id": candidate.id,
                    "profile_id": candidate.profile_id,
                    "enrichment_status": candidate.enrichment_status,
                    "unresolved_clarification_count": candidate.unresolved_clarification_count,
                }
                for candidate in candidates
            ]
            print(json.dumps({"dry_run": True, "matched_count": len(result), "candidates": result}, indent=2))
            return 0

        repaired = repair_stuck_biographer_candidates(
            db,
            profile_id=args.profile_id,
            min_age_hours=args.min_age_hours,
            limit=args.limit,
        )
        result = [
            {
                "candidate_id": item.candidate_id,
                "profile_id": item.profile_id,
                "previous_enrichment_status": item.previous_enrichment_status,
                "new_enrichment_status": item.new_enrichment_status,
                "cancelled_clarification_count": item.cancelled_clarification_count,
            }
            for item in repaired
        ]
        print(json.dumps({"dry_run": False, "repaired_count": len(result), "candidates": result}, indent=2))
        return 0
    finally:
        db.close()


if __name__ == "__main__":
    raise SystemExit(main())
