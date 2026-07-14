"""Add Czech/Russian bilingual content translation table.

Task 64.5.1 - Czech/Russian Bilingual Test UI and Memory Synchronization.

This migration only creates new persistence for the new bilingual
translation layer. It does not touch any existing Russian data: no
existing row's ``language``/text columns are modified, and no network
translation call is made here (translation always happens through the
backend ``content_translation`` service at request time, never inside a
migration). Existing Russian-origin candidates/contributions have no
Czech source and therefore get no rows in this new table - they are
simply out of scope for the translation layer, not backfilled with
synthetic data.

Revision ID: 20260713_0019
Revises: 20260711_0018
Create Date: 2026-07-13 12:00:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260713_0019"
down_revision = "20260711_0018"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "memory_content_translations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("candidate_id", sa.Integer(), nullable=True),
        sa.Column("contribution_id", sa.Integer(), nullable=True),
        sa.Column("clarification_id", sa.Integer(), nullable=True),
        sa.Column("entity_type", sa.String(length=32), nullable=False),
        sa.Column("entity_id", sa.String(length=64), nullable=False),
        sa.Column("field_name", sa.String(length=64), nullable=False),
        sa.Column("source_language", sa.String(length=8), nullable=False),
        sa.Column("target_language", sa.String(length=8), nullable=False),
        sa.Column("source_text", sa.Text(), nullable=False),
        sa.Column("translated_text", sa.Text(), nullable=True),
        sa.Column("source_hash", sa.String(length=64), nullable=False),
        sa.Column(
            "translation_status",
            sa.String(length=32),
            server_default=sa.text("'pending'"),
            nullable=False,
        ),
        sa.Column("translation_provider", sa.String(length=64), nullable=True),
        sa.Column("translation_model", sa.String(length=120), nullable=True),
        sa.Column(
            "translation_version",
            sa.Integer(),
            server_default=sa.text("1"),
            nullable=False,
        ),
        sa.Column("translated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("reviewed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("reviewed_by", sa.String(length=120), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.CheckConstraint(
            "entity_type IN ('memory_candidate', 'family_memory_contribution', "
            "'clarification_question', 'fa_chat_turn')",
            name=op.f("ck_memory_content_translations_memory_content_translations_entity_type"),
        ),
        sa.CheckConstraint(
            "source_language IN ('cs', 'ru')",
            name=op.f("ck_memory_content_translations_memory_content_translations_source_language"),
        ),
        sa.CheckConstraint(
            "target_language IN ('cs', 'ru')",
            name=op.f("ck_memory_content_translations_memory_content_translations_target_language"),
        ),
        sa.CheckConstraint(
            "translation_status IN ('pending', 'translated', 'failed', 'stale', 'human_reviewed')",
            name=op.f("ck_memory_content_translations_memory_content_translations_status"),
        ),
        sa.CheckConstraint(
            "translation_version >= 1",
            name=op.f("ck_memory_content_translations_memory_content_translations_version_positive"),
        ),
        sa.ForeignKeyConstraint(
            ["candidate_id"],
            ["conversation_memory_candidates.id"],
            name=op.f("fk_memory_content_translations_candidate_id_conversation_memory_candidates"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["contribution_id"],
            ["family_memory_contributions.id"],
            name=op.f("fk_memory_content_translations_contribution_id_family_memory_contributions"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["clarification_id"],
            ["memory_clarification_questions.id"],
            name=op.f("fk_memory_content_translations_clarification_id_memory_clarification_questions"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_memory_content_translations")),
    )
    for column in ("candidate_id", "contribution_id", "clarification_id"):
        op.create_index(
            op.f(f"ix_memory_content_translations_{column}"),
            "memory_content_translations",
            [column],
            unique=False,
        )
    op.create_index(
        "ix_mct_entity_field_target_unique",
        "memory_content_translations",
        ["entity_type", "entity_id", "field_name", "target_language"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("ix_mct_entity_field_target_unique", table_name="memory_content_translations")
    for column in reversed(("candidate_id", "contribution_id", "clarification_id")):
        op.drop_index(
            op.f(f"ix_memory_content_translations_{column}"),
            table_name="memory_content_translations",
        )
    op.drop_table("memory_content_translations")
