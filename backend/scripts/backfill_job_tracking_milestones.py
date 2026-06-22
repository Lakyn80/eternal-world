from __future__ import annotations

import argparse

from app.db.session import SessionLocal
from app.modules.job_tracking.service import backfill_known_milestones


def main() -> None:
    parser = argparse.ArgumentParser(description="Backfill historical job-tracking milestones.")
    parser.add_argument("--owner-user-id", type=int, required=True)
    parser.add_argument("--profile-id", type=int, required=False)
    args = parser.parse_args()

    db = SessionLocal()
    try:
        summary = backfill_known_milestones(
            db,
            owner_user_id=args.owner_user_id,
            profile_id=args.profile_id,
        )
    finally:
        db.close()

    print(
        {
            "created_count": summary.created_count,
            "skipped_count": summary.skipped_count,
            "created_job_ids": summary.created_job_ids,
        }
    )


if __name__ == "__main__":
    main()
