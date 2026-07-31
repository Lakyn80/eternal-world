"""Task 65.13.3 - memorial contribution source language + viewer translations.

Revision ID: 20260731_0032
Revises: 20260731_0031
Create Date: 2026-07-31

- ``memorial_contributions.source_language`` (exact original language; text
  column unchanged).
- ``memorial_invitations.preferred_locale_hint`` (optional UI locale for invitee).
- Extend ``memory_content_translations.entity_type`` with
  ``memorial_contribution``.
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260731_0032"
down_revision = "20260731_0031"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "memorial_contributions",
        sa.Column("source_language", sa.String(length=8), nullable=True),
    )
    op.execute(
        """
        UPDATE memorial_contributions AS mc
        SET source_language = mp.canonical_language
        FROM memory_profiles AS mp
        WHERE mc.profile_id = mp.id
          AND mc.source_language IS NULL
        """
    )
    op.execute(
        """
        UPDATE memorial_contributions
        SET source_language = 'cs'
        WHERE source_language IS NULL
        """
    )
    op.alter_column("memorial_contributions", "source_language", nullable=False)
    op.create_check_constraint(
        "memorial_contributions_source_language",
        "memorial_contributions",
        "source_language IN ('cs', 'ru', 'en', 'de')",
    )

    op.add_column(
        "memorial_invitations",
        sa.Column("preferred_locale_hint", sa.String(length=8), nullable=True),
    )
    op.create_check_constraint(
        "memorial_invitations_preferred_locale_hint",
        "memorial_invitations",
        "preferred_locale_hint IS NULL OR preferred_locale_hint IN ('cs', 'en', 'ru')",
    )

    op.drop_constraint(
        "memory_content_translations_entity_type",
        "memory_content_translations",
        type_="check",
    )
    op.create_check_constraint(
        "memory_content_translations_entity_type",
        "memory_content_translations",
        "entity_type IN ("
        "'memory_candidate', 'family_memory_contribution', "
        "'clarification_question', 'fa_chat_turn', 'memorial_contribution'"
        ")",
    )


def downgrade() -> None:
    op.drop_constraint(
        "memory_content_translations_entity_type",
        "memory_content_translations",
        type_="check",
    )
    op.create_check_constraint(
        "memory_content_translations_entity_type",
        "memory_content_translations",
        "entity_type IN ("
        "'memory_candidate', 'family_memory_contribution', "
        "'clarification_question', 'fa_chat_turn'"
        ")",
    )

    op.drop_constraint(
        "memorial_invitations_preferred_locale_hint",
        "memorial_invitations",
        type_="check",
    )
    op.drop_column("memorial_invitations", "preferred_locale_hint")

    op.drop_constraint(
        "memorial_contributions_source_language",
        "memorial_contributions",
        type_="check",
    )
    op.drop_column("memorial_contributions", "source_language")
