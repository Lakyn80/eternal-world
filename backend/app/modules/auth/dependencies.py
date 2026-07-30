from __future__ import annotations

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logging import get_request_id
from app.db.models import User
from app.db.session import get_db
from app.modules.auth.browser_session import resolve_browser_session
from app.modules.auth.schemas import TokenPayload
from app.modules.users import repository as users_repository
from app.core.security import decode_access_token


bearer_scheme = HTTPBearer(auto_error=False)


def get_current_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> User:
    """Resolves the authenticated user from EITHER a bearer JWT (unchanged
    behavior - Swagger/API/PowerShell/internal clients) OR, when no bearer
    credentials were sent at all, a Redis-backed browser session cookie
    (Task 65.7 - both frontend applications). A bearer header, if present,
    is always tried first and exclusively - this preserves the exact prior
    behavior for every existing API caller; the cookie path is purely
    additive."""

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user_id: int | None = None

    if credentials is not None and credentials.scheme.lower() == "bearer":
        try:
            payload = decode_access_token(credentials.credentials)
            token_payload = TokenPayload.from_payload(payload)
            if token_payload.type != "access":
                raise credentials_exception
            user_id = int(token_payload.sub)
        except (jwt.PyJWTError, ValueError, TypeError):
            raise credentials_exception
    else:
        session_id = request.cookies.get(settings.browser_session_cookie_name)
        user_id = resolve_browser_session(session_id, trace_id=get_request_id())
        if user_id is None:
            raise credentials_exception

    user = users_repository.get_user_by_id(db, user_id)
    if user is None or not user.is_active:
        raise credentials_exception

    return user
