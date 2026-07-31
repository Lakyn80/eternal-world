"""Task 65.13.1 - User UI language + immutable memorial canonical language.

Revision ID: 20260731_0030
Revises: 20260729_0028
Create Date: 2026-07-31

Adds:

- ``users.preferred_ui_language`` (mutable account UI chrome language)
- ``memory_profiles.canonical_language`` / ``canonical_language_source`` /
  ``canonical_language_locked_at`` (immutable memorial language)

Backfill is provenance-aware (never a silent Czech assignment):

1. persona ``primary_language`` in {cs,en,ru} → source ``avatar_persona``
2. persona primary is chat-only / non-canonical (e.g. ``de``) →
   application fallback language with source ``manual_review_required``
3. no persona row → application fallback language with source
   ``application_fallback``

Persona ``primary_language`` is then reconciled to the memorial canonical
language. Does not revive quarantined biographer migration ``20260731_0029``.
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260731_0030"
down_revision = "20260729_0028"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "preferred_ui_language",
            sa.String(length=8),
            server_default="en",
            nullable=False,
        ),
    )
    op.create_check_constraint(
        "users_preferred_ui_language",
        "users",
        "preferred_ui_language IN ('cs', 'en', 'ru')",
    )

    op.add_column(
        "memory_profiles",
        sa.Column("canonical_language", sa.String(length=8), nullable=True),
    )
    op.add_column(
        "memory_profiles",
        sa.Column("canonical_language_source", sa.String(length=64), nullable=True),
    )
    op.add_column(
        "memory_profiles",
        sa.Column(
            "canonical_language_locked_at",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
    )

    # Provenance-aware backfill (aggregate SQL only — no private text).
    op.execute(
        """
        UPDATE memory_profiles AS mp
        SET
            canonical_language = aps.primary_language,
            canonical_language_source = 'avatar_persona',
            canonical_language_locked_at = mp.created_at
        FROM avatar_persona_settings AS aps
        WHERE aps.profile_id = mp.id
          AND mp.canonical_language IS NULL
          AND aps.primary_language IN ('cs', 'en', 'ru')
        """
    )
    op.execute(
        """
        UPDATE memory_profiles AS mp
        SET
            canonical_language = 'cs',
            canonical_language_source = 'manual_review_required',
            canonical_language_locked_at = mp.created_at
        FROM avatar_persona_settings AS aps
        WHERE aps.profile_id = mp.id
          AND mp.canonical_language IS NULL
          AND aps.primary_language IS NOT NULL
          AND aps.primary_language NOT IN ('cs', 'en', 'ru')
        """
    )
    op.execute(
        """
        UPDATE memory_profiles
        SET
            canonical_language = 'cs',
            canonical_language_source = 'application_fallback',
            canonical_language_locked_at = created_at
        WHERE canonical_language IS NULL
        """
    )

    op.alter_column(
        "memory_profiles",
        "canonical_language",
        existing_type=sa.String(length=8),
        nullable=False,
        server_default="cs",
    )
    op.alter_column(
        "memory_profiles",
        "canonical_language_source",
        existing_type=sa.String(length=64),
        nullable=False,
        server_default="application_fallback",
    )
    op.alter_column(
        "memory_profiles",
        "canonical_language_locked_at",
        existing_type=sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.text("now()"),
    )
    op.create_check_constraint(
        "memory_profiles_canonical_language",
        "memory_profiles",
        "canonical_language IN ('cs', 'en', 'ru')",
    )
    op.create_check_constraint(
        "memory_profiles_canonical_language_source",
        "memory_profiles",
        "canonical_language_source IN ("
        "'existing_profile', 'avatar_persona', 'creator_preference', "
        "'reliable_content_metadata', 'application_fallback', 'manual_review_required'"
        ")",
    )

    # Reconcile persona primary_language to memorial canonical (derived mirror).
    op.execute(
        """
        UPDATE avatar_persona_settings AS aps
        SET primary_language = mp.canonical_language
        FROM memory_profiles AS mp
        WHERE aps.profile_id = mp.id
          AND aps.primary_language IS DISTINCT FROM mp.canonical_language
        """
    )


def downgrade() -> None:
    op.drop_constraint(
        "memory_profiles_canonical_language_source",
        "memory_profiles",
        type_="check",
    )
    op.drop_constraint(
        "memory_profiles_canonical_language",
        "memory_profiles",
        type_="check",
    )
    op.drop_column("memory_profiles", "canonical_language_locked_at")
    op.drop_column("memory_profiles", "canonical_language_source")
    op.drop_column("memory_profiles", "canonical_language")

    op.drop_constraint("users_preferred_ui_language", "users", type_="check")
    op.drop_column("users", "preferred_ui_language")
