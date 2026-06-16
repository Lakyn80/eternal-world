"""Drop legacy memory profile columns.

Revision ID: 20260616_0004
Revises: 20260616_0003
Create Date: 2026-06-16 14:35:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260616_0004"
down_revision = "20260616_0003"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column("memory_profiles", "preferences")
    op.drop_column("memory_profiles", "long_term_summary")
    op.drop_column("memory_profiles", "persona_summary")
    op.drop_column("memory_profiles", "display_name")


def downgrade() -> None:
    op.add_column(
        "memory_profiles",
        sa.Column(
            "display_name",
            sa.String(length=120),
            nullable=True,
        ),
    )
    op.add_column(
        "memory_profiles",
        sa.Column("persona_summary", sa.Text(), nullable=True),
    )
    op.add_column(
        "memory_profiles",
        sa.Column("long_term_summary", sa.Text(), nullable=True),
    )
    op.add_column(
        "memory_profiles",
        sa.Column(
            "preferences",
            sa.JSON(),
            nullable=False,
            server_default=sa.text("'{}'::json"),
        ),
    )

    op.execute(
        """
        UPDATE memory_profiles
        SET
            display_name = name,
            persona_summary = personality,
            long_term_summary = biography
        """
    )
    op.alter_column("memory_profiles", "display_name", nullable=False)
    op.alter_column("memory_profiles", "preferences", server_default=None)
