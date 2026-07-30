"""Add context-aware AI Biographer provenance, postpone state, and concurrency guard.

Task 65.6 - Context-Aware AI Biographer, Coverage Tracking, and
Duplicate-Question Prevention. Purely additive/relaxing, no data loss:

- Drops `uq_biographer_questions_profile_topic`: the previous design asked
  each topic at most once, ever, for a memorial. The context-aware
  Biographer can legitimately revisit a topic later with a deeper question
  once new evidence exists, so "one row per (profile, topic)" is replaced by
  a plain non-unique index for query performance.
- Adds a partial unique index enforcing "at most one pending question per
  profile" at the database level, closing a real race window: the previous
  code only checked for an existing pending row in application logic
  (read-then-maybe-insert, no row lock), so two concurrent
  `GET next-question` requests could both create a question.
- Widens the `status` check constraint to add `'postponed'` (a distinct
  "ask me again later" state, alongside the existing `'skipped'` / "never
  ask this again").
- Adds nullable provenance columns (generation_mode/provider/model/
  ai_action_id/context_source_count/context_chunk_count/question_intent/
  validation_result/fallback_used) so a generated question's origin can be
  audited without storing any private prompt/answer/source text.

Revision ID: 20260722_0025
Revises: 20260721_0024
Create Date: 2026-07-22 12:00:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260722_0025"
down_revision = "20260721_0024"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint(
        "uq_biographer_questions_profile_topic",
        "biographer_questions",
        type_="unique",
    )
    op.create_index(
        "ix_biographer_questions_profile_topic",
        "biographer_questions",
        ["profile_id", "topic"],
    )
    op.create_index(
        "uq_biographer_questions_profile_pending",
        "biographer_questions",
        ["profile_id"],
        unique=True,
        postgresql_where=sa.text("status = 'pending'"),
    )

    op.drop_constraint("biographer_questions_status", "biographer_questions", type_="check")
    op.create_check_constraint(
        "biographer_questions_status",
        "biographer_questions",
        "status IN ('pending', 'answered', 'skipped', 'postponed')",
    )

    op.add_column(
        "biographer_questions",
        sa.Column("postponed_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "biographer_questions",
        sa.Column(
            "generation_mode",
            sa.String(length=32),
            server_default=sa.text("'deterministic_fallback'"),
            nullable=False,
        ),
    )
    op.add_column(
        "biographer_questions",
        sa.Column("provider", sa.String(length=64), nullable=True),
    )
    op.add_column(
        "biographer_questions",
        sa.Column("model", sa.String(length=128), nullable=True),
    )
    op.add_column(
        "biographer_questions",
        sa.Column("ai_action_id", sa.Integer(), nullable=True),
    )
    op.add_column(
        "biographer_questions",
        sa.Column("context_source_count", sa.Integer(), nullable=True),
    )
    op.add_column(
        "biographer_questions",
        sa.Column("context_chunk_count", sa.Integer(), nullable=True),
    )
    op.add_column(
        "biographer_questions",
        sa.Column("question_intent", sa.String(length=32), nullable=True),
    )
    op.add_column(
        "biographer_questions",
        sa.Column("validation_result", sa.String(length=32), nullable=True),
    )
    op.add_column(
        "biographer_questions",
        sa.Column(
            "fallback_used",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
    )
    op.create_foreign_key(
        "fk_biographer_questions_ai_action_id_ai_actions",
        "biographer_questions",
        "ai_actions",
        ["ai_action_id"],
        ["id"],
        ondelete="SET NULL",
    )


def downgrade() -> None:
    op.drop_constraint(
        "fk_biographer_questions_ai_action_id_ai_actions",
        "biographer_questions",
        type_="foreignkey",
    )
    op.drop_column("biographer_questions", "fallback_used")
    op.drop_column("biographer_questions", "validation_result")
    op.drop_column("biographer_questions", "question_intent")
    op.drop_column("biographer_questions", "context_chunk_count")
    op.drop_column("biographer_questions", "context_source_count")
    op.drop_column("biographer_questions", "ai_action_id")
    op.drop_column("biographer_questions", "model")
    op.drop_column("biographer_questions", "provider")
    op.drop_column("biographer_questions", "generation_mode")
    op.drop_column("biographer_questions", "postponed_at")

    op.drop_constraint("biographer_questions_status", "biographer_questions", type_="check")
    op.create_check_constraint(
        "biographer_questions_status",
        "biographer_questions",
        "status IN ('pending', 'answered', 'skipped')",
    )

    op.drop_index("uq_biographer_questions_profile_pending", table_name="biographer_questions")
    op.drop_index("ix_biographer_questions_profile_topic", table_name="biographer_questions")
    op.create_unique_constraint(
        "uq_biographer_questions_profile_topic",
        "biographer_questions",
        ["profile_id", "topic"],
    )
