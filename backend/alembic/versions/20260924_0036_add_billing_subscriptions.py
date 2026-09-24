"""Phase 6A - billing_subscriptions: one current subscription row per user.

Revision ID: 20260924_0036
Revises: 20260923_0035
Create Date: 2026-09-24

## Model choice

One row per ``user_id`` (unique). Payment-provider webhooks (future) upsert
this current state; subscription history can be added later via a separate
events table without changing entitlement consumers.

Users without a row automatically resolve to the free plan - no backfill.
"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op


revision = "20260924_0036"
down_revision = "20260923_0035"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "billing_subscriptions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("plan_code", sa.String(length=32), nullable=False),
        sa.Column("status", sa.String(length=32), nullable=False),
        sa.Column("current_period_start", sa.DateTime(timezone=True), nullable=True),
        sa.Column("current_period_end", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "cancel_at_period_end",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
        sa.Column("provider", sa.String(length=64), nullable=True),
        sa.Column("provider_customer_id", sa.String(length=255), nullable=True),
        sa.Column("provider_subscription_id", sa.String(length=255), nullable=True),
        sa.Column("provider_price_id", sa.String(length=255), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.CheckConstraint(
            "status IN ('active', 'trialing', 'past_due', 'canceled', 'expired')",
            name="ck_billing_subscriptions_billing_subscriptions_status",
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", name="uq_billing_subscriptions_user_id"),
    )
    op.create_index("ix_billing_subscriptions_status", "billing_subscriptions", ["status"])
    op.create_index(
        "ix_billing_subscriptions_provider_subscription_id",
        "billing_subscriptions",
        ["provider_subscription_id"],
    )


def downgrade() -> None:
    op.drop_index(
        "ix_billing_subscriptions_provider_subscription_id",
        table_name="billing_subscriptions",
    )
    op.drop_index("ix_billing_subscriptions_status", table_name="billing_subscriptions")
    op.drop_table("billing_subscriptions")
