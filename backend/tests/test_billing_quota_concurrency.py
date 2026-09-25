"""Phase 6B — PostgreSQL concurrency tests for billing quota locks.

Requires a real PostgreSQL URL (``settings.database_url``). Skips on SQLite.
"""

from __future__ import annotations

import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone

import pytest
from sqlalchemy import create_engine, delete, select
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings
from app.core.security import hash_password
from app.db.models import BillingSubscription, Memory, MemoryProfile, MemorialMembership, User
from app.modules.billing.exceptions import BillingLimitExceededError
from app.modules.billing.subscriptions import apply_subscription_state
from app.modules.memorial_access.schemas import MemorialCreate
from app.modules.memorial_access.service import create_memorial
from app.modules.memories.schemas import MemoryCreate
from app.modules.memories.service import create_memory
from app.modules.memory_profiles import repository as memory_profiles_repository
from app.modules.memory_profiles.schemas import MemoryProfileCreate
from app.modules.memory_profiles.service import create_memory_profile
from app.modules.memories import repository as memories_repository


pytestmark = pytest.mark.skipif(
    not str(settings.database_url).startswith("postgresql"),
    reason="Phase 6B concurrency tests require PostgreSQL FOR UPDATE semantics",
)


PASSWORD = "StrongPass123"


def _session_factory() -> tuple[sessionmaker, object]:
    engine = create_engine(settings.database_url, pool_pre_ping=True, pool_size=5, max_overflow=5)
    factory = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
    return factory, engine


def _unique_email(label: str) -> str:
    return f"quota-6b-{label}-{uuid.uuid4().hex[:12]}@example.com"


def _create_user(db: Session, *, email: str) -> User:
    username = f"u{uuid.uuid4().hex[:16]}"
    user = User(
        email=email,
        username=username,
        full_name="Quota Concurrency User",
        hashed_password=hash_password(PASSWORD),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def _cleanup_user(session_factory: sessionmaker, user_id: int) -> None:
    db = session_factory()
    try:
        db.execute(delete(Memory).where(Memory.user_id == user_id))
        profile_ids = list(
            db.scalars(select(MemoryProfile.id).where(MemoryProfile.user_id == user_id))
        )
        if profile_ids:
            db.execute(delete(MemorialMembership).where(MemorialMembership.profile_id.in_(profile_ids)))
        db.execute(delete(MemorialMembership).where(MemorialMembership.user_id == user_id))
        db.execute(delete(MemoryProfile).where(MemoryProfile.user_id == user_id))
        db.execute(delete(BillingSubscription).where(BillingSubscription.user_id == user_id))
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
    finally:
        db.close()


def _memorial_payload(name: str) -> MemorialCreate:
    return MemorialCreate(
        name=name,
        canonical_language="cs",
        confirm_canonical_language=True,
    )


def _profile_payload(name: str) -> MemoryProfileCreate:
    return MemoryProfileCreate(
        name=name,
        canonical_language="cs",
        confirm_canonical_language=True,
    )


def _run_concurrent(worker_count: int, worker):
    outcomes: list[object] = []
    with ThreadPoolExecutor(max_workers=worker_count) as pool:
        futures = [pool.submit(worker, index) for index in range(worker_count)]
        for future in as_completed(futures):
            outcomes.append(future.result())
    return outcomes


@pytest.fixture
def pg_sessions():
    factory, engine = _session_factory()
    created_user_ids: list[int] = []
    yield factory, created_user_ids
    for user_id in created_user_ids:
        _cleanup_user(factory, user_id)
    engine.dispose()


def test_free_profile_quota_two_concurrent_memorial_creates(pg_sessions):
    session_factory, created_user_ids = pg_sessions
    setup = session_factory()
    try:
        user = _create_user(setup, email=_unique_email("free-memorial"))
        created_user_ids.append(user.id)
        user_id = user.id
    finally:
        setup.close()

    def worker(index: int):
        db = session_factory()
        try:
            locked_user = db.get(User, user_id)
            assert locked_user is not None
            return create_memorial(
                db,
                current_user=locked_user,
                payload=_memorial_payload(f"Memorial {index}"),
            )
        except BillingLimitExceededError as exc:
            db.rollback()
            return exc
        finally:
            db.close()

    outcomes = _run_concurrent(2, worker)
    successes = [item for item in outcomes if not isinstance(item, BillingLimitExceededError)]
    failures = [item for item in outcomes if isinstance(item, BillingLimitExceededError)]
    assert len(successes) == 1
    assert len(failures) == 1
    assert failures[0].code == "profile_limit_exceeded"
    assert failures[0].error == "limit_exceeded"

    verify = session_factory()
    try:
        assert memory_profiles_repository.count_memory_profiles_for_user(verify, user_id) == 1
    finally:
        verify.close()


def test_cross_endpoint_profile_quota_shares_lock(pg_sessions):
    session_factory, created_user_ids = pg_sessions
    setup = session_factory()
    try:
        user = _create_user(setup, email=_unique_email("cross-endpoint"))
        created_user_ids.append(user.id)
        user_id = user.id
    finally:
        setup.close()

    def memorial_worker(_index: int):
        db = session_factory()
        try:
            locked_user = db.get(User, user_id)
            assert locked_user is not None
            return create_memorial(
                db,
                current_user=locked_user,
                payload=_memorial_payload("Via memorials"),
            )
        except BillingLimitExceededError as exc:
            db.rollback()
            return exc
        finally:
            db.close()

    def profile_worker(_index: int):
        db = session_factory()
        try:
            locked_user = db.get(User, user_id)
            assert locked_user is not None
            return create_memory_profile(
                db,
                current_user=locked_user,
                payload=_profile_payload("Via memory-profiles"),
            )
        except BillingLimitExceededError as exc:
            db.rollback()
            return exc
        finally:
            db.close()

    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(memorial_worker, 0), pool.submit(profile_worker, 1)]
        outcomes = [future.result() for future in as_completed(futures)]

    successes = [item for item in outcomes if not isinstance(item, BillingLimitExceededError)]
    failures = [item for item in outcomes if isinstance(item, BillingLimitExceededError)]
    assert len(successes) == 1
    assert len(failures) == 1
    assert failures[0].code == "profile_limit_exceeded"

    verify = session_factory()
    try:
        assert memory_profiles_repository.count_memory_profiles_for_user(verify, user_id) == 1
    finally:
        verify.close()


def test_basic_plan_profile_quota_two_concurrent_creates_at_limit(pg_sessions):
    session_factory, created_user_ids = pg_sessions
    setup = session_factory()
    try:
        user = _create_user(setup, email=_unique_email("basic-limit"))
        created_user_ids.append(user.id)
        user_id = user.id
        apply_subscription_state(
            setup,
            user_id=user_id,
            plan_code="basic",
            status="active",
            current_period_start=datetime.now(timezone.utc) - timedelta(days=1),
            current_period_end=datetime.now(timezone.utc) + timedelta(days=30),
        )
        for index in range(2):
            create_memorial(
                setup,
                current_user=setup.get(User, user_id),
                payload=_memorial_payload(f"Seed {index}"),
            )
    finally:
        setup.close()

    def worker(index: int):
        db = session_factory()
        try:
            locked_user = db.get(User, user_id)
            assert locked_user is not None
            return create_memorial(
                db,
                current_user=locked_user,
                payload=_memorial_payload(f"Race {index}"),
            )
        except BillingLimitExceededError as exc:
            db.rollback()
            return exc
        finally:
            db.close()

    outcomes = _run_concurrent(2, worker)
    successes = [item for item in outcomes if not isinstance(item, BillingLimitExceededError)]
    failures = [item for item in outcomes if isinstance(item, BillingLimitExceededError)]
    assert len(successes) == 1
    assert len(failures) == 1
    assert failures[0].code == "profile_limit_exceeded"

    verify = session_factory()
    try:
        assert memory_profiles_repository.count_memory_profiles_for_user(verify, user_id) == 3
    finally:
        verify.close()


def test_memory_quota_two_concurrent_creates_at_limit(pg_sessions):
    session_factory, created_user_ids = pg_sessions
    setup = session_factory()
    try:
        user = _create_user(setup, email=_unique_email("memory-limit"))
        created_user_ids.append(user.id)
        user_id = user.id
        profile, _membership = create_memorial(
            setup,
            current_user=user,
            payload=_memorial_payload("Memory host"),
        )
        profile_id = profile.id
        for index in range(9):
            create_memory(
                setup,
                current_user=setup.get(User, user_id),
                profile_id=profile_id,
                payload=MemoryCreate(title=f"Seed memory {index}", memory_type="text"),
            )
    finally:
        setup.close()

    def worker(index: int):
        db = session_factory()
        try:
            locked_user = db.get(User, user_id)
            assert locked_user is not None
            return create_memory(
                db,
                current_user=locked_user,
                profile_id=profile_id,
                payload=MemoryCreate(title=f"Race memory {index}", memory_type="text"),
            )
        except BillingLimitExceededError as exc:
            db.rollback()
            return exc
        finally:
            db.close()

    outcomes = _run_concurrent(2, worker)
    successes = [item for item in outcomes if not isinstance(item, BillingLimitExceededError)]
    failures = [item for item in outcomes if isinstance(item, BillingLimitExceededError)]
    assert len(successes) == 1
    assert len(failures) == 1
    assert failures[0].code == "memory_limit_exceeded"
    assert failures[0].error == "limit_exceeded"

    verify = session_factory()
    try:
        assert memories_repository.count_memories_for_user(verify, user_id) == 10
    finally:
        verify.close()


def test_premium_unlimited_profiles_allow_concurrent_creates(pg_sessions):
    session_factory, created_user_ids = pg_sessions
    setup = session_factory()
    try:
        user = _create_user(setup, email=_unique_email("premium-unlimited"))
        created_user_ids.append(user.id)
        user_id = user.id
        apply_subscription_state(
            setup,
            user_id=user_id,
            plan_code="premium",
            status="active",
            current_period_start=datetime.now(timezone.utc) - timedelta(days=1),
            current_period_end=datetime.now(timezone.utc) + timedelta(days=30),
        )
    finally:
        setup.close()

    def worker(index: int):
        db = session_factory()
        try:
            locked_user = db.get(User, user_id)
            assert locked_user is not None
            return create_memorial(
                db,
                current_user=locked_user,
                payload=_memorial_payload(f"Premium {index}"),
            )
        except BillingLimitExceededError as exc:
            db.rollback()
            return exc
        finally:
            db.close()

    outcomes = _run_concurrent(3, worker)
    assert all(not isinstance(item, BillingLimitExceededError) for item in outcomes)
    verify = session_factory()
    try:
        assert memory_profiles_repository.count_memory_profiles_for_user(verify, user_id) == 3
    finally:
        verify.close()


def test_different_users_do_not_block_each_other(pg_sessions):
    session_factory, created_user_ids = pg_sessions
    setup = session_factory()
    try:
        user_a = _create_user(setup, email=_unique_email("user-a"))
        user_b = _create_user(setup, email=_unique_email("user-b"))
        created_user_ids.extend([user_a.id, user_b.id])
        user_ids = [user_a.id, user_b.id]
    finally:
        setup.close()

    def worker(index: int):
        db = session_factory()
        try:
            locked_user = db.get(User, user_ids[index])
            assert locked_user is not None
            return create_memorial(
                db,
                current_user=locked_user,
                payload=_memorial_payload(f"User {index}"),
            )
        except BillingLimitExceededError as exc:
            db.rollback()
            return exc
        finally:
            db.close()

    outcomes = _run_concurrent(2, worker)
    assert all(not isinstance(item, BillingLimitExceededError) for item in outcomes)
    verify = session_factory()
    try:
        assert memory_profiles_repository.count_memory_profiles_for_user(verify, user_ids[0]) == 1
        assert memory_profiles_repository.count_memory_profiles_for_user(verify, user_ids[1]) == 1
    finally:
        verify.close()
