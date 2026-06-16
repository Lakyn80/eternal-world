"""Create media assets table.

Revision ID: 20260617_0005
Revises: 20260616_0004
Create Date: 2026-06-17 10:00:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260617_0005"
down_revision = "20260616_0004"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "media_assets",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("owner_id", sa.Integer(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=True),
        sa.Column("media_type", sa.String(length=16), nullable=False),
        sa.Column("storage_provider", sa.String(length=32), nullable=False),
        sa.Column("storage_key", sa.String(length=255), nullable=False),
        sa.Column("original_filename", sa.String(length=255), nullable=False),
        sa.Column("mime_type", sa.String(length=255), nullable=False),
        sa.Column("size_bytes", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.CheckConstraint(
            "media_type IN ('image', 'audio', 'video')",
            name=op.f("ck_media_assets_media_assets_media_type"),
        ),
        sa.CheckConstraint(
            "size_bytes >= 0",
            name=op.f("ck_media_assets_media_assets_size_bytes_non_negative"),
        ),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["users.id"],
            name=op.f("fk_media_assets_owner_id_users"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["memory_profiles.id"],
            name=op.f("fk_media_assets_profile_id_memory_profiles"),
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_media_assets")),
    )
    op.create_index(op.f("ix_media_assets_owner_id"), "media_assets", ["owner_id"], unique=False)
    op.create_index(op.f("ix_media_assets_profile_id"), "media_assets", ["profile_id"], unique=False)
    op.create_index(op.f("ix_media_assets_storage_key"), "media_assets", ["storage_key"], unique=True)


def downgrade() -> None:
    op.drop_index(op.f("ix_media_assets_storage_key"), table_name="media_assets")
    op.drop_index(op.f("ix_media_assets_profile_id"), table_name="media_assets")
    op.drop_index(op.f("ix_media_assets_owner_id"), table_name="media_assets")
    op.drop_table("media_assets")
