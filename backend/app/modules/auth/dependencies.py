from __future__ import annotations

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.schemas import TokenPayload
from app.modules.users import repository as users_repository
from app.core.security import decode_access_token


bearer_scheme = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if credentials is None or credentials.scheme.lower() != "bearer":
        raise credentials_exception

    try:
        payload = decode_access_token(credentials.credentials)
        token_payload = TokenPayload.from_payload(payload)
        if token_payload.type != "access":
            raise credentials_exception
        user_id = int(token_payload.sub)
    except (jwt.PyJWTError, ValueError, TypeError):
        raise credentials_exception

    user = users_repository.get_user_by_id(db, user_id)
    if user is None or not user.is_active:
        raise credentials_exception

    return user
