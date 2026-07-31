"""Task 65.13.4 - biographer_question / biographer_answer translation entities.

Revision ID: 20260731_0033
Revises: 20260731_0032
Create Date: 2026-07-31

Extend ``memory_content_translations.entity_type`` for Biographer display
and answer canonicalization. Pending-question identity remains one row per
profile (no per-locale pending index).
"""

from __future__ import annotations

from alembic import op


revision = "20260731_0033"
down_revision = "20260731_0032"
branch_labels = None
depends_on = None


def upgrade() -> None:
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
        "'clarification_question', 'fa_chat_turn', 'memorial_contribution', "
        "'biographer_question', 'biographer_answer'"
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
        "'clarification_question', 'fa_chat_turn', 'memorial_contribution'"
        ")",
    )
