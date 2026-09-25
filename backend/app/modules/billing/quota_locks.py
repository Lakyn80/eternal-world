"""Transaction-scoped billing quota locks (Phase 6B).

Uses ``SELECT ... FOR UPDATE`` on the owning ``users`` row so concurrent
quota-consuming creates for the same account serialize across API workers
until commit/rollback. Different users lock different rows and do not block
each other.

PostgreSQL honors the lock; SQLite test dialects ignore ``FOR UPDATE``
(same pattern as job_outbox). Concurrency correctness is covered by
PostgreSQL-backed tests.
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import User


def lock_user_row_for_billing_quota(db: Session, *, user_id: int) -> User:
    """Acquire a transaction-scoped exclusive lock on the billing user row.

    Must be called inside the same DB transaction that then counts usage,
    enforces the plan limit, and inserts the quota-consuming row.
    """

    statement = select(User).where(User.id == user_id).with_for_update()
    user = db.scalar(statement)
    if user is None:
        raise ValueError(f"Cannot lock billing quota for unknown user_id={user_id}")
    return user
