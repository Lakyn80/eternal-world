from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logging import get_request_id
from app.db.models import User
from app.db.session import get_db
from app.modules.auth.browser_session import revoke_browser_session, rotate_browser_session
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse, LoginRequest, RegisterRequest, TokenResponse
from app.modules.auth.service import (
    DuplicateEmailError,
    InvalidCredentialsError,
    login_user,
    register_user,
)
from app.modules.users.schemas import UserRead


router = APIRouter(prefix="/api/auth", tags=["auth"])


def _set_session_cookie(response: Response, session_id: str) -> None:
    # Deliberately no `max_age`/`expires` - Part B.11: "no persistent
    # Expires/Max-Age browser lifetime". The cookie itself is a browser-
    # session-lifetime cookie; the *server-side* Redis record carries the
    # actual sliding inactivity TTL (`browser_session_ttl_seconds`).
    response.set_cookie(
        key=settings.browser_session_cookie_name,
        value=session_id,
        httponly=True,
        secure=settings.browser_session_cookie_secure,
        samesite="lax",
        path="/",
        domain=settings.browser_session_cookie_domain,
    )


def _clear_session_cookie(response: Response) -> None:
    response.delete_cookie(
        key=settings.browser_session_cookie_name,
        path="/",
        domain=settings.browser_session_cookie_domain,
    )


@router.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_409_CONFLICT: {"model": ErrorResponse}},
)
def register(payload: RegisterRequest, db: Session = Depends(get_db)) -> UserRead:
    try:
        user = register_user(db, payload)
    except DuplicateEmailError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc

    return UserRead.model_validate(user)


@router.post(
    "/login",
    response_model=TokenResponse,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse}},
)
def login(
    payload: LoginRequest, response: Response, request: Request, db: Session = Depends(get_db)
) -> TokenResponse:
    """Returns a bearer token (unchanged contract - Swagger/API/PowerShell
    clients) AND sets an HttpOnly Redis-backed browser session cookie
    (Task 65.7), so a browser client never needs to hold or replay the
    bearer token itself across navigation/remounts."""

    try:
        token_response, user = login_user(db, payload)
    except InvalidCredentialsError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc

    old_session_id = request.cookies.get(settings.browser_session_cookie_name)
    session_id = rotate_browser_session(old_session_id, user_id=user.id, trace_id=get_request_id())
    # Cookie is best-effort: bearer token remains the primary API contract.
    if session_id is not None:
        _set_session_cookie(response, session_id)
    return token_response


@router.get(
    "/me",
    response_model=UserRead,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse}},
)
def get_me(current_user: User = Depends(get_current_user)) -> UserRead:
    return UserRead.model_validate(current_user)


@router.get(
    "/session",
    response_model=UserRead,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse}},
)
def get_session(current_user: User = Depends(get_current_user)) -> UserRead:
    """Session-resume endpoint (Part B.12): identical resolution to `/me`
    (bearer OR cookie) - a distinct path purely so both frontend
    applications have an explicit, self-describing "am I logged in"
    endpoint to call on startup, independent of `/me`'s original bearer-
    only intent."""

    return UserRead.model_validate(current_user)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
def logout(response: Response, request: Request) -> None:
    """Revokes the browser session (if any) and clears the cookie. Never
    requires authentication to succeed - logging out an already-expired/
    missing session is a safe no-op, not an error."""

    session_id = request.cookies.get(settings.browser_session_cookie_name)
    revoke_browser_session(session_id, trace_id=get_request_id())
    _clear_session_cookie(response)
