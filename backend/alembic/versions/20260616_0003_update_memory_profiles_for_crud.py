"""Update memory profiles for CRUD support.

Revision ID: 20260616_0003
Revises: 20260616_0002
Create Date: 2026-06-16 14:10:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260616_0003"
down_revision = "20260616_0002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("memory_profiles", sa.Column("name", sa.String(length=120), nullable=True))
    op.add_column("memory_profiles", sa.Column("birth_date", sa.Date(), nullable=True))
    op.add_column("memory_profiles", sa.Column("death_date", sa.Date(), nullable=True))
    op.add_column("memory_profiles", sa.Column("biography", sa.Text(), nullable=True))
    op.add_column("memory_profiles", sa.Column("personality", sa.Text(), nullable=True))
    op.add_column("memory_profiles", sa.Column("catchphrases", sa.Text(), nullable=True))
    op.add_column(
        "memory_profiles",
        sa.Column("is_public", sa.Boolean(), nullable=False, server_default=sa.text("false")),
    )

    op.execute(
        """
        UPDATE memory_profiles
        SET
            name = display_name,
            biography = long_term_summary,
            personality = persona_summary
        """
    )
    op.alter_column("memory_profiles", "name", nullable=False)
    op.drop_index(op.f("ix_memory_profiles_user_id"), table_name="memory_profiles")
    op.create_index(op.f("ix_memory_profiles_user_id"), "memory_profiles", ["user_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_memory_profiles_user_id"), table_name="memory_profiles")
    op.create_index(op.f("ix_memory_profiles_user_id"), "memory_profiles", ["user_id"], unique=True)
    op.drop_column("memory_profiles", "is_public")
    op.drop_column("memory_profiles", "catchphrases")
    op.drop_column("memory_profiles", "personality")
    op.drop_column("memory_profiles", "biography")
    op.drop_column("memory_profiles", "death_date")
    op.drop_column("memory_profiles", "birth_date")
    op.drop_column("memory_profiles", "name")
