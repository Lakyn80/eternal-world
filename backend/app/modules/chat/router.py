from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.chat.http_errors import CHAT_ADMISSION_HTTP_ERRORS, raise_chat_admission_http
from app.modules.chat.schemas import ChatActiveRead, ChatMessageCreate, ChatMessageRead, ChatSendResponse
from app.modules.chat.service import (
    ChatForbiddenError,
    ChatProfileNotFoundError,
    get_active_chat,
    list_chat_messages,
    reset_chat,
    send_chat_message_async,
)


router = APIRouter(prefix="/api/chat", tags=["chat"])
ProfileIdPath = Annotated[int, Path(gt=0)]


@router.post(
    "/{profile_id}/messages",
    response_model=ChatSendResponse,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
        status.HTTP_429_TOO_MANY_REQUESTS: {"model": ErrorResponse},
        status.HTTP_503_SERVICE_UNAVAILABLE: {"model": ErrorResponse},
    },
)
async def send_message(
    profile_id: ProfileIdPath,
    payload: ChatMessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ChatSendResponse:
    """Task 65.13.12: async chat send — Brain wait is non-blocking on the event loop."""

    try:
        return await send_chat_message_async(
            db,
            current_user=current_user,
            profile_id=profile_id,
            payload=payload,
        )
    except ChatProfileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except ChatForbiddenError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(exc),
        ) from exc
    except CHAT_ADMISSION_HTTP_ERRORS as exc:
        raise_chat_admission_http(exc)


@router.get(
    "/{profile_id}/active",
    response_model=ChatActiveRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_active_chat_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ChatActiveRead:
    """Task 65.7 (Part E.35): restores the active conversation transcript -
    Redis fast-path, Postgres fallback/rebuild on a cache miss."""

    try:
        return get_active_chat(db, current_user=current_user, profile_id=profile_id)
    except ChatProfileNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ChatForbiddenError as exc:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc


@router.post(
    "/{profile_id}/reset",
    response_model=ChatActiveRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def reset_chat_endpoint(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ChatActiveRead:
    """Task 65.7 (Part E.34): "Obnovit chat" - starts a brand-new empty
    active conversation. Prior messages are preserved (never deleted),
    just no longer part of the active conversation."""

    try:
        return reset_chat(db, current_user=current_user, profile_id=profile_id)
    except ChatProfileNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ChatForbiddenError as exc:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc


@router.get(
    "/{profile_id}/messages",
    response_model=list[ChatMessageRead],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_messages(
    profile_id: ProfileIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[ChatMessageRead]:
    try:
        return list_chat_messages(
            db,
            current_user=current_user,
            profile_id=profile_id,
        )
    except ChatProfileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except ChatForbiddenError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(exc),
        ) from exc
