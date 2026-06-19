"""Add timeline memory fields and media linkage.

Revision ID: 20260619_0007
Revises: 20260617_0006
Create Date: 2026-06-19 00:30:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260619_0007"
down_revision = "20260617_0006"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("memories", sa.Column("media_id", sa.Integer(), nullable=True))
    op.add_column("memories", sa.Column("title", sa.String(length=200), nullable=True))
    op.add_column("memories", sa.Column("occurred_at", sa.DateTime(timezone=True), nullable=True))
    op.add_column("memories", sa.Column("occurred_year", sa.Integer(), nullable=True))
    op.create_index(op.f("ix_memories_media_id"), "memories", ["media_id"], unique=False)
    op.create_foreign_key(
        op.f("fk_memories_media_id_media_assets"),
        "memories",
        "media_assets",
        ["media_id"],
        ["id"],
        ondelete="SET NULL",
    )

    op.execute(
        sa.text(
            """
            UPDATE memories
            SET title = COALESCE(NULLIF(BTRIM(content), ''), 'Untitled memory')
            WHERE title IS NULL
            """
        )
    )

    op.alter_column("memories", "title", existing_type=sa.String(length=200), nullable=False)
    op.alter_column("memories", "content", existing_type=sa.Text(), nullable=True)
    op.alter_column(
        "memories",
        "memory_type",
        existing_type=sa.String(length=32),
        server_default=sa.text("'text'"),
        existing_nullable=False,
    )

    with op.batch_alter_table("memories") as batch_op:
        batch_op.drop_constraint(op.f("ck_memories_memories_memory_type"), type_="check")
        batch_op.create_check_constraint(
            op.f("ck_memories_memories_memory_type"),
            "memory_type IN ('text', 'photo', 'audio', 'video')",
        )


def downgrade() -> None:
    with op.batch_alter_table("memories") as batch_op:
        batch_op.drop_constraint(op.f("ck_memories_memories_memory_type"), type_="check")
        batch_op.create_check_constraint(
            op.f("ck_memories_memories_memory_type"),
            "memory_type IN ('episodic', 'semantic', 'profile', 'system')",
        )

    op.alter_column(
        "memories",
        "memory_type",
        existing_type=sa.String(length=32),
        server_default=sa.text("'episodic'"),
        existing_nullable=False,
    )
    op.alter_column("memories", "content", existing_type=sa.Text(), nullable=False)

    op.drop_constraint(op.f("fk_memories_media_id_media_assets"), "memories", type_="foreignkey")
    op.drop_index(op.f("ix_memories_media_id"), table_name="memories")
    op.drop_column("memories", "occurred_year")
    op.drop_column("memories", "occurred_at")
    op.drop_column("memories", "title")
    op.drop_column("memories", "media_id")
