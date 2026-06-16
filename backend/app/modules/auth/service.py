from __future__ import annotations

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.db.models import User
from app.modules.auth.schemas import LoginRequest, RegisterRequest, TokenResponse
from app.modules.users import repository as users_repository


class DuplicateEmailError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


def register_user(db: Session, payload: RegisterRequest) -> User:
    normalized_email = payload.email.strip().lower()

    if users_repository.get_user_by_email(db, normalized_email) is not None:
        raise DuplicateEmailError("A user with this email already exists")

    user = users_repository.create_user(
        db,
        email=normalized_email,
        username=users_repository.build_unique_username(db, normalized_email),
        full_name=payload.full_name,
        hashed_password=hash_password(payload.password),
    )

    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        if users_repository.get_user_by_email(db, normalized_email) is not None:
            raise DuplicateEmailError("A user with this email already exists") from exc
        raise

    db.refresh(user)
    return user


def login_user(db: Session, payload: LoginRequest) -> TokenResponse:
    normalized_email = payload.email.strip().lower()
    user = users_repository.get_user_by_email(db, normalized_email)

    if user is None or not user.is_active:
        raise InvalidCredentialsError("Invalid email or password")

    if not verify_password(payload.password, user.hashed_password):
        raise InvalidCredentialsError("Invalid email or password")

    access_token = create_access_token(
        subject=str(user.id),
        extra_claims={"email": user.email},
    )
    return TokenResponse(access_token=access_token)
