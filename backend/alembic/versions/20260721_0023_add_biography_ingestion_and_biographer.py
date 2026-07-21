"""Add biography ingestion tracking and biographer_questions table.

Task 65.2 - AI Biographer & Living Memory Onboarding. Purely additive: adds
lifecycle-tracking columns to memory_profiles (biography_status/content
hash/active source/indexed_at/attempt count/failure reason) so the owner's
free-text biography field can be explicitly, idempotently ingested into the
existing RagSource -> RagChunk -> RagEmbedding -> Qdrant pipeline, and adds a
new biographer_questions table for the bounded AI Biographer topic/question
engine. Also widens the existing conversation_memory_candidates_memory_type
check constraint to add 'childhood_memory' (a new clarification-question
topic, reusing the existing bedtime_song-era 'place'/'approximate_period'
question keys) - no existing row's memory_type value is affected.

Revision ID: 20260721_0023
Revises: 20260719_0022
Create Date: 2026-07-21 12:00:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260721_0023"
down_revision = "20260719_0022"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "memory_profiles",
        sa.Column(
            "biography_status",
            sa.String(length=32),
            server_default=sa.text("'draft'"),
            nullable=False,
        ),
    )
    op.add_column(
        "memory_profiles",
        sa.Column("biography_content_hash", sa.String(length=64), nullable=True),
    )
    op.add_column(
        "memory_profiles",
        sa.Column("biography_source_id", sa.Integer(), nullable=True),
    )
    op.add_column(
        "memory_profiles",
        sa.Column("biography_indexed_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "memory_profiles",
        sa.Column(
            "biography_ingestion_attempt_count",
            sa.Integer(),
            server_default=sa.text("0"),
            nullable=False,
        ),
    )
    op.add_column(
        "memory_profiles",
        sa.Column("biography_ingestion_failure_reason", sa.String(length=500), nullable=True),
    )
    op.create_check_constraint(
        "memory_profiles_biography_status",
        "memory_profiles",
        "biography_status IN ('draft', 'ready_for_ingestion', 'ingesting', 'indexed', 'failed', 'stale')",
    )
    op.create_index(
        "ix_memory_profiles_biography_source_id",
        "memory_profiles",
        ["biography_source_id"],
    )
    op.create_foreign_key(
        "fk_memory_profiles_biography_source_id_rag_sources",
        "memory_profiles",
        "rag_sources",
        ["biography_source_id"],
        ["id"],
        ondelete="SET NULL",
    )

    op.drop_constraint(
        "conversation_memory_candidates_memory_type",
        "conversation_memory_candidates",
        type_="check",
    )
    op.create_check_constraint(
        "conversation_memory_candidates_memory_type",
        "conversation_memory_candidates",
        "memory_type IN ('general', 'bedtime_song', 'childhood_memory')",
    )

    op.create_table(
        "biographer_questions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.Column("topic", sa.String(length=64), nullable=False),
        sa.Column("locale", sa.String(length=8), nullable=False),
        sa.Column("question_text", sa.String(length=500), nullable=False),
        sa.Column(
            "status",
            sa.String(length=32),
            server_default=sa.text("'pending'"),
            nullable=False,
        ),
        sa.Column(
            "asked_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("answered_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("skipped_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("answered_by_user_id", sa.Integer(), nullable=True),
        sa.Column("resulting_candidate_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.CheckConstraint(
            "status IN ('pending', 'answered', 'skipped')",
            name="biographer_questions_status",
        ),
        sa.ForeignKeyConstraint(["profile_id"], ["memory_profiles.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["answered_by_user_id"], ["users.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(
            ["resulting_candidate_id"],
            ["conversation_memory_candidates.id"],
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("profile_id", "topic", name="uq_biographer_questions_profile_topic"),
    )
    op.create_index(
        "ix_biographer_questions_profile_status",
        "biographer_questions",
        ["profile_id", "status"],
    )
    op.create_index(
        "ix_biographer_questions_profile_id",
        "biographer_questions",
        ["profile_id"],
    )


def downgrade() -> None:
    op.drop_index("ix_biographer_questions_profile_id", table_name="biographer_questions")
    op.drop_index("ix_biographer_questions_profile_status", table_name="biographer_questions")
    op.drop_table("biographer_questions")

    op.drop_constraint(
        "conversation_memory_candidates_memory_type",
        "conversation_memory_candidates",
        type_="check",
    )
    op.create_check_constraint(
        "conversation_memory_candidates_memory_type",
        "conversation_memory_candidates",
        "memory_type IN ('general', 'bedtime_song')",
    )

    op.drop_constraint(
        "fk_memory_profiles_biography_source_id_rag_sources",
        "memory_profiles",
        type_="foreignkey",
    )
    op.drop_index("ix_memory_profiles_biography_source_id", table_name="memory_profiles")
    op.drop_constraint("memory_profiles_biography_status", "memory_profiles", type_="check")
    op.drop_column("memory_profiles", "biography_ingestion_failure_reason")
    op.drop_column("memory_profiles", "biography_ingestion_attempt_count")
    op.drop_column("memory_profiles", "biography_indexed_at")
    op.drop_column("memory_profiles", "biography_source_id")
    op.drop_column("memory_profiles", "biography_content_hash")
    op.drop_column("memory_profiles", "biography_status")
