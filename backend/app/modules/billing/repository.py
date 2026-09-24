"""Persisted billing subscription repository (Phase 6A)."""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import BillingSubscription


def get_subscription_for_user(db: Session, *, user_id: int) -> BillingSubscription | None:
    statement = select(BillingSubscription).where(BillingSubscription.user_id == user_id)
    return db.scalar(statement)


def upsert_subscription(
    db: Session,
    *,
    user_id: int,
    plan_code: str,
    status: str,
    current_period_start: datetime | None = None,
    current_period_end: datetime | None = None,
    cancel_at_period_end: bool = False,
    provider: str | None = None,
    provider_customer_id: str | None = None,
    provider_subscription_id: str | None = None,
    provider_price_id: str | None = None,
    currency: str | None = None,
) -> BillingSubscription:
    """Create or replace the single current subscription row for ``user_id``."""

    row = get_subscription_for_user(db, user_id=user_id)
    if row is None:
        row = BillingSubscription(user_id=user_id)
        db.add(row)

    row.plan_code = plan_code
    row.status = status
    row.current_period_start = current_period_start
    row.current_period_end = current_period_end
    row.cancel_at_period_end = cancel_at_period_end
    row.provider = provider
    row.provider_customer_id = provider_customer_id
    row.provider_subscription_id = provider_subscription_id
    row.provider_price_id = provider_price_id
    row.currency = currency.strip().upper() if currency else None
    db.flush()
    return row
