"""Task 65.6.1 (Part H) - idempotent reconciliation for approved candidates
missing a promotion, an indexing enqueue, or otherwise stuck in
`pending_index`/`failed`. Never touches a candidate that is not
`status == "approved"`, never creates a second promotion for a candidate
that already has one, never re-indexes an already-`indexed` promotion,
never cancels/rejects/archives anything.

Usage (inside the backend container):

    python scripts/reconcile_avatar_memory_promotions.py --dry-run
    python scripts/reconcile_avatar_memory_promotions.py --profile-id 15
    python scripts/reconcile_avatar_memory_promotions.py
"""

from __future__ import annotations

import argparse
import json

from app.db.session import SessionLocal
from app.modules.avatar_memory_promotions.reconciliation import reconcile_candidate_promotions


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Repair approved candidates missing a promotion or indexing enqueue "
            "in the avatar-memory-promotion pipeline."
        )
    )
    parser.add_argument("--profile-id", type=int, default=None, help="Limit to a single memorial profile ID.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would be repaired without writing/enqueuing anything.",
    )
    return parser


def main() -> int:
    args = _build_parser().parse_args()
    db = SessionLocal()
    try:
        result = reconcile_candidate_promotions(db, profile_id=args.profile_id, dry_run=args.dry_run)
        payload = {
            "dry_run": args.dry_run,
            "profile_id": args.profile_id,
            "scanned": result.scanned,
            "already_complete": result.already_complete,
            "promoted": result.promoted,
            "indexing_enqueued": result.indexing_enqueued,
            "failed": result.failed,
            "skipped": result.skipped,
            "outcomes": [
                {
                    "candidate_id": outcome.candidate_id,
                    "profile_id": outcome.profile_id,
                    "action": outcome.action,
                    "promotion_id": outcome.promotion_id,
                    "promotion_status": outcome.promotion_status,
                    "detail": outcome.detail,
                }
                for outcome in result.outcomes
            ],
        }
        print(json.dumps(payload, indent=2))
        return 0
    finally:
        db.close()


if __name__ == "__main__":
    raise SystemExit(main())
