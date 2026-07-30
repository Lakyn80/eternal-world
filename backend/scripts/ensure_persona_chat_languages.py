"""Ensure every memorial persona can answer in production chat locales.

Idempotent. Merges cs/en/ru into supported_languages without removing
existing entries (e.g. de). Does not change primary_language.
"""

from __future__ import annotations

import sys

from app.db.models import AvatarPersonaSettings
from app.db.session import SessionLocal
from app.modules.avatar_persona.settings_schemas import (
    ALLOWED_PERSONA_LANGUAGES,
    DEFAULT_SUPPORTED_LANGUAGES,
)


def _emit(message: str) -> None:
    print(f"[ensure_persona_chat_languages] {message}", flush=True)


def ensure_persona_chat_languages() -> int:
    db = SessionLocal()
    updated = 0
    try:
        rows = db.query(AvatarPersonaSettings).all()
        for row in rows:
            current = row.supported_languages if isinstance(row.supported_languages, list) else []
            merged: list[str] = []
            seen: set[str] = set()
            for code in [*current, *DEFAULT_SUPPORTED_LANGUAGES]:
                if not isinstance(code, str) or code not in ALLOWED_PERSONA_LANGUAGES or code in seen:
                    continue
                seen.add(code)
                merged.append(code)
            if not merged:
                merged = list(DEFAULT_SUPPORTED_LANGUAGES)
            if merged == current:
                continue
            row.supported_languages = merged
            updated += 1
        db.commit()
    except Exception as exc:  # noqa: BLE001 - ops script must exit non-zero cleanly
        db.rollback()
        _emit(f"ERROR {exc}")
        return 1
    finally:
        db.close()

    _emit(f"updated_rows={updated}")
    return 0


def main() -> int:
    return ensure_persona_chat_languages()


if __name__ == "__main__":
    sys.exit(main())
