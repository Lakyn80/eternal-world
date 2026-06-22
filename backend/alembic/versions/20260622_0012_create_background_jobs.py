"""Create background_jobs table.

Revision ID: 20260622_0012
Revises: 20260620_0011
Create Date: 2026-06-22 10:00:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260622_0012"
down_revision = "20260620_0011"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "background_jobs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("owner_user_id", sa.Integer(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=True),
        sa.Column("job_type", sa.String(length=64), nullable=False),
        sa.Column(
            "status",
            sa.String(length=16),
            server_default=sa.text("'queued'"),
            nullable=False,
        ),
        sa.Column("progress_current", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("progress_total", sa.Integer(), server_default=sa.text("0"), nullable=False),
        sa.Column("celery_task_id", sa.String(length=255), nullable=True),
        sa.Column("input_payload", sa.JSON(), nullable=False),
        sa.Column("result_payload", sa.JSON(), nullable=True),
        sa.Column("error_payload", sa.JSON(), nullable=True),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("finished_at", sa.DateTime(timezone=True), nullable=True),
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
            (
                "job_type IN ("
                "'smoke_test', 'system_milestone', 'rag_source_ingestion', 'rag_chunking', "
                "'embedding_generation', 'qdrant_indexing', 'rag_retrieval', "
                "'brain_agent_generation', 'media_processing', 'voice_generation', "
                "'video_generation'"
                ")"
            ),
            name=op.f("ck_background_jobs_background_jobs_job_type"),
        ),
        sa.CheckConstraint(
            "status IN ('queued', 'running', 'succeeded', 'failed', 'cancelled')",
            name=op.f("ck_background_jobs_background_jobs_status"),
        ),
        sa.ForeignKeyConstraint(
            ["owner_user_id"],
            ["users.id"],
            name=op.f("fk_background_jobs_owner_user_id_users"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["memory_profiles.id"],
            name=op.f("fk_background_jobs_profile_id_memory_profiles"),
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_background_jobs")),
    )
    op.create_index(op.f("ix_background_jobs_owner_user_id"), "background_jobs", ["owner_user_id"], unique=False)
    op.create_index(op.f("ix_background_jobs_profile_id"), "background_jobs", ["profile_id"], unique=False)
    op.create_index(op.f("ix_background_jobs_job_type"), "background_jobs", ["job_type"], unique=False)
    op.create_index(op.f("ix_background_jobs_status"), "background_jobs", ["status"], unique=False)
    op.create_index(op.f("ix_background_jobs_celery_task_id"), "background_jobs", ["celery_task_id"], unique=False)
    op.create_index("ix_background_jobs_created_at", "background_jobs", ["created_at"], unique=False)
    op.create_index(
        "ix_background_jobs_owner_user_id_profile_id",
        "background_jobs",
        ["owner_user_id", "profile_id"],
        unique=False,
    )
    op.create_index(
        "ix_background_jobs_owner_user_id_status",
        "background_jobs",
        ["owner_user_id", "status"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_background_jobs_owner_user_id_status", table_name="background_jobs")
    op.drop_index("ix_background_jobs_owner_user_id_profile_id", table_name="background_jobs")
    op.drop_index("ix_background_jobs_created_at", table_name="background_jobs")
    op.drop_index(op.f("ix_background_jobs_celery_task_id"), table_name="background_jobs")
    op.drop_index(op.f("ix_background_jobs_status"), table_name="background_jobs")
    op.drop_index(op.f("ix_background_jobs_job_type"), table_name="background_jobs")
    op.drop_index(op.f("ix_background_jobs_profile_id"), table_name="background_jobs")
    op.drop_index(op.f("ix_background_jobs_owner_user_id"), table_name="background_jobs")
    op.drop_table("background_jobs")
