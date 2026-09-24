"""Phase 6A market correction — persist purchase currency on subscriptions.

Revision ID: 20260924_0037
Revises: 20260924_0036
Create Date: 2026-09-24

Nullable ``currency`` records the ISO code used when a paid subscription
was purchased. Free / no-row users leave it null. Never backfilled from
UI locale.
"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op


revision = "20260924_0037"
down_revision = "20260924_0036"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "billing_subscriptions",
        sa.Column("currency", sa.String(length=3), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("billing_subscriptions", "currency")
