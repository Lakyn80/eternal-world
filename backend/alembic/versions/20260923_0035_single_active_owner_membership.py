"""Phase 5A - enforce at most one active owner membership per memorial.

Revision ID: 20260923_0035
Revises: 20260731_0034
Create Date: 2026-09-23

Adds a partial unique index:

    UNIQUE(profile_id) WHERE role = 'owner' AND status = 'active'

## Invariant model (Phase 5A)

* **DB-enforced:** at most one active owner per memorial (this migration).
* **Service-enforced (canonical create):** exactly one active owner whose
  ``user_id`` equals ``memory_profiles.user_id`` via
  ``memorial_access.service.create_memorial``.
* **Not DB-enforced:** exactly-one / owner↔profile match. Zero-owner and
  mismatch rows are detected by the read-only preflight
  ``scripts/check_memorial_owner_integrity.py`` and must be repaired
  explicitly (or left for intentional creator self-heal on legacy
  ``/api/memory-profiles`` creates).

This upgrade **fails only** when multiple active owners exist. Zero-owner
and owner/profile-mismatch rows do **not** block the migration: failing on
zero-owner would incorrectly stop deploys that still contain legacy
memory-profile fixtures awaiting self-heal. This migration never mutates
or auto-repairs membership rows.
"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op


revision = "20260923_0035"
down_revision = "20260731_0034"
branch_labels = None
depends_on = None


def upgrade() -> None:
    conn = op.get_bind()
    duplicates = conn.execute(
        sa.text(
            """
            SELECT profile_id, COUNT(*) AS active_owner_count
            FROM memorial_memberships
            WHERE role = 'owner' AND status = 'active'
            GROUP BY profile_id
            HAVING COUNT(*) > 1
            ORDER BY profile_id
            """
        )
    ).mappings().all()
    if duplicates:
        detail = ", ".join(
            f"profile_id={row['profile_id']} count={row['active_owner_count']}" for row in duplicates
        )
        raise RuntimeError(
            "Cannot add uq_memorial_memberships_one_active_owner: "
            f"memorials with multiple active owners: {detail}"
        )

    op.create_index(
        "uq_memorial_memberships_one_active_owner",
        "memorial_memberships",
        ["profile_id"],
        unique=True,
        postgresql_where=sa.text("role = 'owner' AND status = 'active'"),
    )


def downgrade() -> None:
    op.drop_index(
        "uq_memorial_memberships_one_active_owner",
        table_name="memorial_memberships",
        postgresql_where=sa.text("role = 'owner' AND status = 'active'"),
    )
