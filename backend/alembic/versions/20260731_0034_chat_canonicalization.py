"""Task 65.13.5 - chat message source language + chat_message MCT entity.

Revision ID: 20260731_0034
Revises: 20260731_0033
Create Date: 2026-07-31

- ``chat_messages.source_language`` stores the original user-message language
  (nullable; assistant rows remain null).
- MCT ``entity_type`` gains ``chat_message`` for user→canonical and
  assistant→viewer derived texts (Decision B).
"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op


revision = "20260731_0034"
down_revision = "20260731_0033"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "chat_messages",
        sa.Column("source_language", sa.String(length=8), nullable=True),
    )
    op.create_check_constraint(
        "chat_messages_source_language",
        "chat_messages",
        "source_language IS NULL OR source_language IN ('cs', 'ru', 'en', 'de')",
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
        "'clarification_question', 'fa_chat_turn', 'memorial_contribution', "
        "'biographer_question', 'biographer_answer', 'chat_message'"
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
        "'clarification_question', 'fa_chat_turn', 'memorial_contribution', "
        "'biographer_question', 'biographer_answer'"
        ")",
    )

    op.drop_constraint(
        "chat_messages_source_language",
        "chat_messages",
        type_="check",
    )
    op.drop_column("chat_messages", "source_language")
