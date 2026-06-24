"""Create active_retrieval_configs table.

Revision ID: 20260624_0013
Revises: 20260622_0012
Create Date: 2026-06-24 11:00:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260624_0013"
down_revision = "20260622_0012"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "active_retrieval_configs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("owner_user_id", sa.Integer(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.Column("model_code", sa.String(length=120), nullable=False),
        sa.Column("collection_name", sa.String(length=200), nullable=False),
        sa.Column("top_k", sa.Integer(), nullable=False),
        sa.Column("score_threshold", sa.Float(), nullable=True),
        sa.Column(
            "retrieval_mode",
            sa.String(length=64),
            server_default=sa.text("'hybrid'"),
            nullable=False,
        ),
        sa.Column("source_eval_job_id", sa.Integer(), nullable=True),
        sa.Column("source_eval_dataset_id", sa.String(length=120), nullable=True),
        sa.Column("selected_metrics", sa.JSON(), nullable=True),
        sa.Column("all_config_scores", sa.JSON(), nullable=True),
        sa.Column("selection_reason", sa.Text(), nullable=True),
        sa.Column("warnings", sa.JSON(), nullable=True),
        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default=sa.text("true"),
            nullable=False,
        ),
        sa.Column(
            "selected_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
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
            "top_k BETWEEN 1 AND 100",
            name=op.f("ck_active_retrieval_configs_active_retrieval_configs_top_k"),
        ),
        sa.ForeignKeyConstraint(
            ["owner_user_id"],
            ["users.id"],
            name=op.f("fk_active_retrieval_configs_owner_user_id_users"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["memory_profiles.id"],
            name=op.f("fk_active_retrieval_configs_profile_id_memory_profiles"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["source_eval_job_id"],
            ["background_jobs.id"],
            name=op.f("fk_active_retrieval_configs_source_eval_job_id_background_jobs"),
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_active_retrieval_configs")),
        sa.UniqueConstraint("profile_id", name=op.f("uq_active_retrieval_configs_profile_id")),
    )
    op.create_index(
        op.f("ix_active_retrieval_configs_owner_user_id"),
        "active_retrieval_configs",
        ["owner_user_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_active_retrieval_configs_profile_id"),
        "active_retrieval_configs",
        ["profile_id"],
        unique=False,
    )
    op.create_index(
        "ix_active_retrieval_configs_created_at",
        "active_retrieval_configs",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        "ix_active_retrieval_configs_owner_user_id_profile_id",
        "active_retrieval_configs",
        ["owner_user_id", "profile_id"],
        unique=False,
    )
    op.create_index(
        "ix_active_retrieval_configs_profile_id_is_active",
        "active_retrieval_configs",
        ["profile_id", "is_active"],
        unique=False,
    )
    op.create_index(
        "ix_active_retrieval_configs_source_eval_job_id",
        "active_retrieval_configs",
        ["source_eval_job_id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_active_retrieval_configs_source_eval_job_id", table_name="active_retrieval_configs")
    op.drop_index("ix_active_retrieval_configs_profile_id_is_active", table_name="active_retrieval_configs")
    op.drop_index("ix_active_retrieval_configs_owner_user_id_profile_id", table_name="active_retrieval_configs")
    op.drop_index("ix_active_retrieval_configs_created_at", table_name="active_retrieval_configs")
    op.drop_index(op.f("ix_active_retrieval_configs_profile_id"), table_name="active_retrieval_configs")
    op.drop_index(op.f("ix_active_retrieval_configs_owner_user_id"), table_name="active_retrieval_configs")
    op.drop_table("active_retrieval_configs")
