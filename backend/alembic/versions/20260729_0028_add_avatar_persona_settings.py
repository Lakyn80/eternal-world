"""Add avatar_persona_settings one-to-one table (Task 65.12).

Revision ID: 20260729_0028
Revises: 20260724_0027
Create Date: 2026-07-29

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260729_0028"
down_revision = "20260724_0027"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "avatar_persona_settings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.Column("voice_mode", sa.String(length=32), server_default="warm_older", nullable=False),
        sa.Column("voice_style", sa.String(length=32), server_default="warm", nullable=False),
        sa.Column("personality_traits", sa.JSON(), server_default=sa.text("'[]'"), nullable=False),
        sa.Column("primary_language", sa.String(length=8), server_default="cs", nullable=False),
        sa.Column("supported_languages", sa.JSON(), server_default=sa.text("'[\"cs\"]'"), nullable=False),
        sa.Column("remembered_age", sa.Integer(), nullable=True),
        sa.Column("communication_profile", sa.Text(), server_default="", nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.CheckConstraint(
            "voice_mode IN ('original_recording', 'warm_older', 'younger_self')",
            name="ck_avatar_persona_settings_avatar_persona_settings_voice_mode",
        ),
        sa.CheckConstraint(
            "voice_style IN ('warm', 'calm', 'older', 'energetic')",
            name="ck_avatar_persona_settings_avatar_persona_settings_voice_style",
        ),
        sa.CheckConstraint(
            "remembered_age IS NULL OR (remembered_age >= 1 AND remembered_age <= 120)",
            name="ck_avatar_persona_settings_avatar_persona_settings_remembered_age",
        ),
        sa.ForeignKeyConstraint(["profile_id"], ["memory_profiles.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("profile_id", name="uq_avatar_persona_settings_profile_id"),
    )
    op.create_index("ix_avatar_persona_settings_profile_id", "avatar_persona_settings", ["profile_id"])


def downgrade() -> None:
    op.drop_index("ix_avatar_persona_settings_profile_id", table_name="avatar_persona_settings")
    op.drop_table("avatar_persona_settings")
