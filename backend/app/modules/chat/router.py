from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.chat.schemas import ChatMessageCreate, ChatMessageRead, ChatSendResponse
from app.modules.chat.service import (
    ChatForbiddenError,
    ChatProfileNotFoundError,
    list_chat_messages,
    send_chat_message,
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
    },
)
def send_message(
    profile_id: ProfileIdPath,
    payload: ChatMessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ChatSendResponse:
    try:
        return send_chat_message(
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
