"""Add memory profile main photo media reference.

Revision ID: 20260617_0006
Revises: 20260617_0005
Create Date: 2026-06-17 15:10:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260617_0006"
down_revision = "20260617_0005"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "memory_profiles",
        sa.Column("main_photo_media_id", sa.Integer(), nullable=True),
    )
    op.create_index(
        op.f("ix_memory_profiles_main_photo_media_id"),
        "memory_profiles",
        ["main_photo_media_id"],
        unique=False,
    )
    op.create_foreign_key(
        op.f("fk_memory_profiles_main_photo_media_id_media_assets"),
        "memory_profiles",
        "media_assets",
        ["main_photo_media_id"],
        ["id"],
        ondelete="SET NULL",
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("fk_memory_profiles_main_photo_media_id_media_assets"),
        "memory_profiles",
        type_="foreignkey",
    )
    op.drop_index(op.f("ix_memory_profiles_main_photo_media_id"), table_name="memory_profiles")
    op.drop_column("memory_profiles", "main_photo_media_id")
