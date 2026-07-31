"""Authorization helpers for content-translation human overrides (Task 65.13.2).

Machine translation enqueue may be triggered by system workflows. Human
override / review of a translated field is restricted to memorial members
with the review capability (owner and trusted_reviewer).
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.db.models import MemorialMembership, MemoryProfile, User
from app.modules.memorial_access.capabilities import (
    MemorialCapability,
    resolve_authorized_profile,
)


def assert_can_review_content_translation(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
) -> tuple[MemoryProfile, MemorialMembership]:
    """Require owner/trusted_reviewer-equivalent review capability."""

    return resolve_authorized_profile(
        db,
        current_user=current_user,
        profile_id=profile_id,
        capability=MemorialCapability.REVIEW_CONTRIBUTION,
    )
