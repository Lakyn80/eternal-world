from __future__ import annotations

from sqlalchemy.orm import Session

from app.db.models import AvatarPersonaSettings


def get_settings_by_profile_id(db: Session, *, profile_id: int) -> AvatarPersonaSettings | None:
    return (
        db.query(AvatarPersonaSettings)
        .filter(AvatarPersonaSettings.profile_id == profile_id)
        .one_or_none()
    )


def create_settings(
    db: Session,
    *,
    profile_id: int,
    voice_mode: str,
    voice_style: str,
    personality_traits: list[str],
    primary_language: str,
    supported_languages: list[str],
    remembered_age: int | None,
    communication_profile: str,
) -> AvatarPersonaSettings:
    row = AvatarPersonaSettings(
        profile_id=profile_id,
        voice_mode=voice_mode,
        voice_style=voice_style,
        personality_traits=list(personality_traits),
        primary_language=primary_language,
        supported_languages=list(supported_languages),
        remembered_age=remembered_age,
        communication_profile=communication_profile,
    )
    db.add(row)
    db.flush()
    return row
