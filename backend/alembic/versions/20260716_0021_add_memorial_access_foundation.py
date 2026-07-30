"""Add memorial access, invitations, and contribution review foundation.

Task 65 - Accounts, Memorial Access, and Contribution Review Foundation.

Revision ID: 20260716_0021
Revises: 20260715_0020
Create Date: 2026-07-16 20:45:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "20260716_0021"
down_revision = "20260715_0020"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "memorial_memberships",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("role", sa.String(length=32), nullable=False),
        sa.Column("status", sa.String(length=32), server_default=sa.text("'active'"), nullable=False),
        sa.Column("created_by_user_id", sa.Integer(), nullable=True),
        sa.Column("revoked_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("revoked_by_user_id", sa.Integer(), nullable=True),
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
            "role IN ('owner', 'trusted_reviewer', 'contributor', 'viewer')",
            name=op.f("ck_memorial_memberships_memorial_memberships_role"),
        ),
        sa.CheckConstraint(
            "status IN ('active', 'revoked')",
            name=op.f("ck_memorial_memberships_memorial_memberships_status"),
        ),
        sa.ForeignKeyConstraint(
            ["created_by_user_id"],
            ["users.id"],
            name=op.f("fk_memorial_memberships_created_by_user_id_users"),
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["memory_profiles.id"],
            name=op.f("fk_memorial_memberships_profile_id_memory_profiles"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["revoked_by_user_id"],
            ["users.id"],
            name=op.f("fk_memorial_memberships_revoked_by_user_id_users"),
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("fk_memorial_memberships_user_id_users"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_memorial_memberships")),
        sa.UniqueConstraint("profile_id", "user_id", name="uq_memorial_memberships_profile_user"),
    )
    for column in ("profile_id", "user_id", "role", "status", "created_by_user_id", "revoked_by_user_id"):
        op.create_index(op.f(f"ix_memorial_memberships_{column}"), "memorial_memberships", [column])
    op.create_index("ix_memorial_memberships_profile_role", "memorial_memberships", ["profile_id", "role"])
    op.create_index("ix_memorial_memberships_user_status", "memorial_memberships", ["user_id", "status"])

    op.create_table(
        "memorial_invitations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("role", sa.String(length=32), nullable=False),
        sa.Column("token_hash", sa.String(length=64), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("accepted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("accepted_by_user_id", sa.Integer(), nullable=True),
        sa.Column("revoked_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_user_id", sa.Integer(), nullable=True),
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
            "role IN ('trusted_reviewer', 'contributor', 'viewer')",
            name=op.f("ck_memorial_invitations_memorial_invitations_role"),
        ),
        sa.ForeignKeyConstraint(
            ["accepted_by_user_id"],
            ["users.id"],
            name=op.f("fk_memorial_invitations_accepted_by_user_id_users"),
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["created_by_user_id"],
            ["users.id"],
            name=op.f("fk_memorial_invitations_created_by_user_id_users"),
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["memory_profiles.id"],
            name=op.f("fk_memorial_invitations_profile_id_memory_profiles"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_memorial_invitations")),
        sa.UniqueConstraint("token_hash", name=op.f("uq_memorial_invitations_token_hash")),
    )
    for column in (
        "profile_id",
        "email",
        "role",
        "token_hash",
        "expires_at",
        "accepted_at",
        "accepted_by_user_id",
        "revoked_at",
        "created_by_user_id",
    ):
        op.create_index(op.f(f"ix_memorial_invitations_{column}"), "memorial_invitations", [column])
    op.create_index("ix_memorial_invitations_profile_email", "memorial_invitations", ["profile_id", "email"])
    op.create_index(
        "ix_memorial_invitations_profile_status",
        "memorial_invitations",
        ["profile_id", "accepted_at", "revoked_at"],
    )

    op.create_table(
        "memorial_contributions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.Column("author_user_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("memory_text", sa.Text(), nullable=False),
        sa.Column("source_note", sa.String(length=500), nullable=True),
        sa.Column(
            "privacy_scope",
            sa.String(length=32),
            server_default=sa.text("'private_owner'"),
            nullable=False,
        ),
        sa.Column(
            "status",
            sa.String(length=32),
            server_default=sa.text("'needs_review'"),
            nullable=False,
        ),
        sa.Column("is_current", sa.Boolean(), server_default=sa.text("false"), nullable=False),
        sa.Column("supersedes_contribution_id", sa.Integer(), nullable=True),
        sa.Column("reviewed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("reviewed_by_user_id", sa.Integer(), nullable=True),
        sa.Column("review_note", sa.String(length=500), nullable=True),
        sa.Column("rejection_reason", sa.String(length=500), nullable=True),
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
            "status IN ('draft', 'needs_review', 'approved', 'rejected', 'archived', 'superseded')",
            name=op.f("ck_memorial_contributions_memorial_contributions_status"),
        ),
        sa.CheckConstraint(
            "privacy_scope IN ('private_owner', 'selected_family', 'all_family', 'public_legacy')",
            name=op.f("ck_memorial_contributions_memorial_contributions_privacy_scope"),
        ),
        sa.ForeignKeyConstraint(
            ["author_user_id"],
            ["users.id"],
            name=op.f("fk_memorial_contributions_author_user_id_users"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["memory_profiles.id"],
            name=op.f("fk_memorial_contributions_profile_id_memory_profiles"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["reviewed_by_user_id"],
            ["users.id"],
            name=op.f("fk_memorial_contributions_reviewed_by_user_id_users"),
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["supersedes_contribution_id"],
            ["memorial_contributions.id"],
            name=op.f("fk_memorial_contributions_supersedes_contribution_id_memorial_contributions"),
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_memorial_contributions")),
    )
    for column in (
        "profile_id",
        "author_user_id",
        "status",
        "is_current",
        "supersedes_contribution_id",
        "reviewed_by_user_id",
    ):
        op.create_index(op.f(f"ix_memorial_contributions_{column}"), "memorial_contributions", [column])
    op.create_index("ix_memorial_contributions_profile_status", "memorial_contributions", ["profile_id", "status"])
    op.create_index("ix_memorial_contributions_profile_current", "memorial_contributions", ["profile_id", "is_current"])
    op.create_index("ix_memorial_contributions_author_status", "memorial_contributions", ["author_user_id", "status"])
    op.create_index("ix_memorial_contributions_created_at", "memorial_contributions", ["created_at"])

    op.execute(
        "INSERT INTO memorial_memberships (profile_id, user_id, role, status, created_by_user_id, created_at, updated_at) "
        "SELECT id, user_id, 'owner', 'active', user_id, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP "
        "FROM memory_profiles"
    )


def downgrade() -> None:
    for name in (
        "ix_memorial_contributions_created_at",
        "ix_memorial_contributions_author_status",
        "ix_memorial_contributions_profile_current",
        "ix_memorial_contributions_profile_status",
    ):
        op.drop_index(name, table_name="memorial_contributions")
    for column in reversed(
        ("profile_id", "author_user_id", "status", "is_current", "supersedes_contribution_id", "reviewed_by_user_id")
    ):
        op.drop_index(op.f(f"ix_memorial_contributions_{column}"), table_name="memorial_contributions")
    op.drop_table("memorial_contributions")

    op.drop_index("ix_memorial_invitations_profile_status", table_name="memorial_invitations")
    op.drop_index("ix_memorial_invitations_profile_email", table_name="memorial_invitations")
    for column in reversed(
        (
            "profile_id",
            "email",
            "role",
            "token_hash",
            "expires_at",
            "accepted_at",
            "accepted_by_user_id",
            "revoked_at",
            "created_by_user_id",
        )
    ):
        op.drop_index(op.f(f"ix_memorial_invitations_{column}"), table_name="memorial_invitations")
    op.drop_table("memorial_invitations")

    op.drop_index("ix_memorial_memberships_user_status", table_name="memorial_memberships")
    op.drop_index("ix_memorial_memberships_profile_role", table_name="memorial_memberships")
    for column in reversed(("profile_id", "user_id", "role", "status", "created_by_user_id", "revoked_by_user_id")):
        op.drop_index(op.f(f"ix_memorial_memberships_{column}"), table_name="memorial_memberships")
    op.drop_table("memorial_memberships")

