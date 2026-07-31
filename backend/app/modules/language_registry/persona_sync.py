"""Helpers that bind memorial canonical language to avatar persona (Task 65.13.1)."""

from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.db.models import MemoryProfile
from app.modules.avatar_persona import settings_repository
from app.modules.avatar_persona.settings_schemas import (
    DEFAULT_VOICE_MODE,
    DEFAULT_VOICE_STYLE,
)
from app.modules.language_registry import (
    LanguageCode,
    assert_canonical_memorial_language,
    default_supported_chat_languages,
    is_chat_input_language,
)


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def sync_persona_languages_to_canonical(
    db: Session,
    *,
    profile: MemoryProfile,
) -> None:
    """Keep persona ``primary_language`` as a derived mirror of memorial canonical."""

    canonical = assert_canonical_memorial_language(profile.canonical_language)
    supported_default = default_supported_chat_languages(primary=canonical)
    row = settings_repository.get_settings_by_profile_id(db, profile_id=profile.id)
    if row is None:
        settings_repository.create_settings(
            db,
            profile_id=profile.id,
            voice_mode=DEFAULT_VOICE_MODE,
            voice_style=DEFAULT_VOICE_STYLE,
            personality_traits=[],
            primary_language=canonical,
            supported_languages=list(supported_default),
            remembered_age=None,
            communication_profile="",
        )
        return

    row.primary_language = canonical
    existing: list[str] = []
    if isinstance(row.supported_languages, list):
        existing = [code for code in row.supported_languages if isinstance(code, str)]

    merged: list[LanguageCode] = [canonical]
    for code in existing:
        if code in merged:
            continue
        if is_chat_input_language(code):
            merged.append(code)  # type: ignore[arg-type]
    for code in supported_default:
        if code not in merged:
            merged.append(code)
    row.supported_languages = merged
    db.flush()
