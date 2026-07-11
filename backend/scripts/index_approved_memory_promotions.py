from __future__ import annotations

import argparse
import json
from collections.abc import Sequence

from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.modules.avatar_memory_indexing import repository
from app.modules.avatar_memory_indexing.qdrant_writer import DefaultAvatarMemoryQdrantWriter
from app.modules.avatar_memory_indexing.service import (
    AvatarMemoryIndexingConflictError,
    AvatarMemoryIndexingEligibilityError,
    AvatarMemoryIndexingExecutionError,
    AvatarMemoryIndexingNotFoundError,
    DefaultAvatarMemoryEmbeddingEncoder,
    index_promotion,
    preview_promotion_indexing,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Explicitly index approved pending avatar memory promotions."
    )
    parser.add_argument("--promotion-id", type=int)
    parser.add_argument("--avatar-id")
    parser.add_argument("--profile-id", type=int)
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--qdrant-url")
    return parser


def run_indexing(
    db: Session,
    *,
    promotion_id: int | None,
    avatar_id: str | None,
    profile_id: int | None,
    limit: int,
    dry_run: bool,
    writer=None,
    encoder=None,
    validate_runtime: bool = True,
) -> dict[str, object]:
    if limit < 1 or limit > 1000:
        raise ValueError("limit must be between 1 and 1000")
    selection_kwargs = {
        "promotion_id": promotion_id,
        "avatar_id": avatar_id,
        "profile_id": profile_id,
        "limit": limit,
    }
    selected = (
        repository.list_selected_promotions(db, **selection_kwargs)
        if promotion_id is not None
        else repository.list_promotions_for_indexing(db, **selection_kwargs)
    )
    summary: dict[str, object] = {
        "dry_run": dry_run,
        "eligible": 0,
        "indexed": 0,
        "failed": 0,
        "skipped": 0,
        "already_indexed": 0,
        "items": [],
    }
    items = summary["items"]
    assert isinstance(items, list)
    for promotion in selected:
        if promotion.promotion_status == "indexed" and dry_run:
            summary["already_indexed"] = int(summary["already_indexed"]) + 1
            items.append({"promotion_id": promotion.id, "result": "already_indexed"})
            continue
        if promotion.promotion_status not in {"pending_index", "indexed"}:
            summary["skipped"] = int(summary["skipped"]) + 1
            items.append(
                {
                    "promotion_id": promotion.id,
                    "result": "skipped",
                    "promotion_status": promotion.promotion_status,
                }
            )
            continue
        try:
            if dry_run:
                preview = preview_promotion_indexing(
                    db,
                    owner_user_id=promotion.owner_user_id,
                    promotion_id=promotion.id,
                    writer=writer,
                )
                summary["eligible"] = int(summary["eligible"]) + 1
                items.append({**preview.model_dump(mode="json"), "result": "eligible"})
            else:
                if promotion.promotion_status == "pending_index":
                    preview_promotion_indexing(
                        db,
                        owner_user_id=promotion.owner_user_id,
                        promotion_id=promotion.id,
                        writer=writer,
                    )
                    summary["eligible"] = int(summary["eligible"]) + 1
                outcome = index_promotion(
                    db,
                    owner_user_id=promotion.owner_user_id,
                    promotion_id=promotion.id,
                    writer=writer,
                    encoder=encoder,
                    validate_runtime=validate_runtime,
                )
                if outcome.result == "already_indexed":
                    summary["already_indexed"] = int(summary["already_indexed"]) + 1
                else:
                    summary["indexed"] = int(summary["indexed"]) + 1
                items.append(outcome.model_dump(mode="json"))
        except (AvatarMemoryIndexingNotFoundError, AvatarMemoryIndexingEligibilityError) as exc:
            summary["skipped"] = int(summary["skipped"]) + 1
            items.append(
                {
                    "promotion_id": promotion.id,
                    "result": "skipped",
                    "error_type": exc.__class__.__name__,
                }
            )
        except (AvatarMemoryIndexingConflictError, AvatarMemoryIndexingExecutionError) as exc:
            summary["failed"] = int(summary["failed"]) + 1
            items.append(
                {
                    "promotion_id": promotion.id,
                    "result": "failed",
                    "error_type": exc.__class__.__name__,
                }
            )
        except Exception as exc:
            summary["failed"] = int(summary["failed"]) + 1
            items.append(
                {
                    "promotion_id": promotion.id,
                    "result": "failed",
                    "error_type": exc.__class__.__name__,
                }
            )
    return summary


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    writer = DefaultAvatarMemoryQdrantWriter(qdrant_url=args.qdrant_url)
    encoder = None if args.dry_run else DefaultAvatarMemoryEmbeddingEncoder()
    db = SessionLocal()
    try:
        summary = run_indexing(
            db,
            promotion_id=args.promotion_id,
            avatar_id=args.avatar_id,
            profile_id=args.profile_id,
            limit=args.limit,
            dry_run=args.dry_run,
            writer=writer,
            encoder=encoder,
        )
    finally:
        db.close()
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 1 if int(summary["failed"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
