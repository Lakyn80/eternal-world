from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db.models import MemoryContentTranslation


def get_current(
    db: Session,
    *,
    entity_type: str,
    entity_id: str,
    field_name: str,
    target_language: str,
) -> MemoryContentTranslation | None:
    return db.scalar(
        select(MemoryContentTranslation).where(
            MemoryContentTranslation.entity_type == entity_type,
            MemoryContentTranslation.entity_id == entity_id,
            MemoryContentTranslation.field_name == field_name,
            MemoryContentTranslation.target_language == target_language,
        )
    )


def list_for_candidate(db: Session, *, candidate_id: int) -> list[MemoryContentTranslation]:
    return list(
        db.scalars(
            select(MemoryContentTranslation)
            .where(MemoryContentTranslation.candidate_id == candidate_id)
            .order_by(MemoryContentTranslation.id.asc())
        )
    )


def start_pending_attempt(
    db: Session,
    *,
    candidate_id: int | None,
    contribution_id: int | None,
    clarification_id: int | None,
    entity_type: str,
    entity_id: str,
    field_name: str,
    source_language: str,
    target_language: str,
    source_text: str,
    source_hash: str,
    profile_id: int | None = None,
) -> MemoryContentTranslation:
    """Create or update-in-place the current translation row for this field.

    If a row already exists and its ``source_hash`` differs from the new
    one, the previous state is marked ``stale`` first (in place - see the
    model docstring for why this table is not a full history table), then
    the row is updated to reflect the new source text with
    ``translation_status=pending`` and an incremented ``translation_version``.
    """
    existing = get_current(
        db,
        entity_type=entity_type,
        entity_id=entity_id,
        field_name=field_name,
        target_language=target_language,
    )
    if existing is None:
        row = MemoryContentTranslation(
            profile_id=profile_id,
            candidate_id=candidate_id,
            contribution_id=contribution_id,
            clarification_id=clarification_id,
            entity_type=entity_type,
            entity_id=entity_id,
            field_name=field_name,
            source_language=source_language,
            target_language=target_language,
            source_text=source_text,
            source_hash=source_hash,
            translation_status="pending",
            translation_version=1,
        )
        db.add(row)
        db.flush()
        return row

    source_changed = existing.source_hash != source_hash
    if source_changed:
        existing.translation_version += 1
        existing.translated_text = None
        existing.reviewed_at = None
        existing.reviewed_by = None
    if profile_id is not None:
        existing.profile_id = profile_id
    existing.source_text = source_text
    existing.source_hash = source_hash
    existing.source_language = source_language
    existing.translation_status = "pending"
    db.flush()
    return existing


def mark_translated(
    db: Session,
    row: MemoryContentTranslation,
    *,
    translated_text: str,
    provider: str,
    model: str,
) -> MemoryContentTranslation:
    row.translated_text = translated_text
    row.translation_status = "translated"
    row.translation_provider = provider
    row.translation_model = model
    row.translated_at = datetime.now(timezone.utc)
    db.flush()
    return row


def mark_failed(db: Session, row: MemoryContentTranslation) -> MemoryContentTranslation:
    row.translation_status = "failed"
    db.flush()
    return row


def mark_stale(db: Session, row: MemoryContentTranslation) -> MemoryContentTranslation:
    row.translation_status = "stale"
    db.flush()
    return row


def mark_identity_translation(
    db: Session,
    row: MemoryContentTranslation,
    *,
    source_text: str,
) -> MemoryContentTranslation:
    """Persist a same-language identity result without calling a provider."""

    row.translated_text = source_text
    row.translation_status = "translated"
    row.translation_provider = "identity"
    row.translation_model = "identity"
    row.translated_at = datetime.now(timezone.utc)
    db.flush()
    return row


def apply_human_override(
    db: Session,
    row: MemoryContentTranslation,
    *,
    translated_text: str,
    reviewed_by: str,
) -> MemoryContentTranslation:
    """Replace machine text with a human-reviewed override.

    Does not change ``source_text`` / ``source_hash``. Increments
    ``translation_version`` so consumers can detect the override.
    """

    row.translated_text = translated_text
    row.translation_status = "human_reviewed"
    row.translation_provider = row.translation_provider or "human"
    row.translation_model = row.translation_model or "human"
    row.translation_version += 1
    row.translated_at = datetime.now(timezone.utc)
    row.reviewed_at = datetime.now(timezone.utc)
    row.reviewed_by = reviewed_by
    db.flush()
    return row


def mark_human_reviewed(
    db: Session,
    row: MemoryContentTranslation,
    *,
    reviewed_by: str,
) -> MemoryContentTranslation:
    """Mark an existing usable translation as human-reviewed without edits."""

    if row.translated_text is None or not str(row.translated_text).strip():
        raise ValueError("cannot mark empty translation as human_reviewed")
    row.translation_status = "human_reviewed"
    row.reviewed_at = datetime.now(timezone.utc)
    row.reviewed_by = reviewed_by
    db.flush()
    return row


def list_for_profile(db: Session, *, profile_id: int) -> list[MemoryContentTranslation]:
    return list(
        db.scalars(
            select(MemoryContentTranslation)
            .where(MemoryContentTranslation.profile_id == profile_id)
            .order_by(MemoryContentTranslation.id.asc())
        )
    )


def count_by_status(db: Session) -> dict[str, int]:
    rows = db.execute(
        select(MemoryContentTranslation.translation_status, func.count(MemoryContentTranslation.id)).group_by(
            MemoryContentTranslation.translation_status
        )
    ).all()
    return {status: count for status, count in rows}
