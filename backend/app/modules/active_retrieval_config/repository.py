from __future__ import annotations

from sqlalchemy.orm import Session

from app.db.models import ActiveRetrievalConfig, BackgroundJob


def get_active_config_for_profile(
    db: Session,
    *,
    owner_user_id: int,
    profile_id: int,
) -> ActiveRetrievalConfig | None:
    return (
        db.query(ActiveRetrievalConfig)
        .filter(
            ActiveRetrievalConfig.owner_user_id == owner_user_id,
            ActiveRetrievalConfig.profile_id == profile_id,
            ActiveRetrievalConfig.is_active.is_(True),
        )
        .one_or_none()
    )


def get_background_job_for_owner(
    db: Session,
    *,
    owner_user_id: int,
    job_id: int,
) -> BackgroundJob | None:
    return (
        db.query(BackgroundJob)
        .filter(
            BackgroundJob.id == job_id,
            BackgroundJob.owner_user_id == owner_user_id,
        )
        .one_or_none()
    )
