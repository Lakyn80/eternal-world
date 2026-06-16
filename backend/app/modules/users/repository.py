from __future__ import annotations

import re

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import User


USERNAME_MAX_LENGTH = 64
NON_USERNAME_CHARACTERS = re.compile(r"[^a-z0-9._-]+")


def get_user_by_email(db: Session, email: str) -> User | None:
    normalized_email = email.strip().lower()
    statement = select(User).where(User.email == normalized_email)
    return db.scalar(statement)


def get_user_by_id(db: Session, user_id: int) -> User | None:
    statement = select(User).where(User.id == user_id)
    return db.scalar(statement)


def get_user_by_username(db: Session, username: str) -> User | None:
    statement = select(User).where(User.username == username)
    return db.scalar(statement)


def build_unique_username(db: Session, email: str) -> str:
    local_part = email.split("@", maxsplit=1)[0].lower()
    normalized_base = NON_USERNAME_CHARACTERS.sub("-", local_part).strip("._-")
    base_username = (normalized_base or "user")[:USERNAME_MAX_LENGTH]

    candidate = base_username
    suffix = 1

    while get_user_by_username(db, candidate) is not None:
        suffix_token = f"-{suffix}"
        candidate = f"{base_username[:USERNAME_MAX_LENGTH - len(suffix_token)]}{suffix_token}"
        suffix += 1

    return candidate


def create_user(
    db: Session,
    *,
    email: str,
    username: str,
    hashed_password: str,
    full_name: str | None,
) -> User:
    user = User(
        email=email,
        username=username,
        full_name=full_name,
        hashed_password=hashed_password,
    )
    db.add(user)
    return user
