from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.avatar_persona import settings_repository
from app.modules.avatar_persona.settings_schemas import (
    AvatarPersonaSettingsRead,
    AvatarPersonaSettingsUpdate,
)
from app.modules.avatar_persona.settings_service import (
    AvatarPersonaValidationError,
    apply_settings_update,
    resolve_avatar_persona,
    settings_to_read,
)
from app.modules.memorial_access.capabilities import MemorialCapability, resolve_authorized_profile
from app.modules.memorial_access.service import MemorialForbiddenError, MemorialNotFoundError


router = APIRouter(tags=["avatar-persona"])
ProfileIdPath = Annotated[int, Path(gt=0)]


def _raise_access(exc: Exception) -> None:
    if isinstance(exc, MemorialNotFoundError):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    if isinstance(exc, MemorialForbiddenError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc
    raise exc


@router.get(
    "/api/memorials/{profile_id}/avatar-persona",
    response_model=AvatarPersonaSettingsRead,
)
def get_avatar_persona_settings(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> AvatarPersonaSettingsRead:
    """Owner-only read of canonical persona settings (defaults when unset)."""

    try:
        profile, _membership = resolve_authorized_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
            capability=MemorialCapability.MANAGE_MEMORIAL,
        )
    except (MemorialNotFoundError, MemorialForbiddenError) as exc:
        _raise_access(exc)

    resolved = resolve_avatar_persona(db, profile=profile)
    row = settings_repository.get_settings_by_profile_id(db, profile_id=profile.id)
    return settings_to_read(
        resolved,
        created_at=row.created_at if row is not None else None,
        updated_at=row.updated_at if row is not None else None,
    )


@router.patch(
    "/api/memorials/{profile_id}/avatar-persona",
    response_model=AvatarPersonaSettingsRead,
)
def patch_avatar_persona_settings(
    profile_id: ProfileIdPath,
    payload: AvatarPersonaSettingsUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> AvatarPersonaSettingsRead:
    """Owner-only partial update of canonical persona settings."""

    try:
        profile, _membership = resolve_authorized_profile(
            db,
            current_user=current_user,
            profile_id=profile_id,
            capability=MemorialCapability.MANAGE_MEMORIAL,
        )
    except (MemorialNotFoundError, MemorialForbiddenError) as exc:
        _raise_access(exc)

    fields_set = payload.model_fields_set
    try:
        if "primary_language" in fields_set and "supported_languages" not in fields_set:
            current = resolve_avatar_persona(db, profile=profile)
            if payload.primary_language is not None and payload.primary_language not in current.supported_languages:
                raise AvatarPersonaValidationError(
                    "primary_language must be included in supported_languages"
                )
        if "supported_languages" in fields_set and "primary_language" not in fields_set:
            current = resolve_avatar_persona(db, profile=profile)
            if (
                payload.supported_languages is not None
                and current.primary_language not in payload.supported_languages
            ):
                raise AvatarPersonaValidationError(
                    "supported_languages must include the current primary_language"
                )
        resolved = apply_settings_update(
            db,
            profile=profile,
            payload=payload,
            fields_set=fields_set,
        )
    except AvatarPersonaValidationError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    row = settings_repository.get_settings_by_profile_id(db, profile_id=profile.id)
    return settings_to_read(
        resolved,
        created_at=row.created_at if row is not None else None,
        updated_at=row.updated_at if row is not None else None,
    )
