from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, File, Form, HTTPException, Path, Response, UploadFile, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models import User
from app.db.session import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.schemas import ErrorResponse
from app.modules.media.schemas import MediaAssetRead, MediaUploadRequest
from app.modules.media.service import (
    MediaAssetNotFoundError,
    MediaProfileNotFoundError,
    MediaTooLargeError,
    UnsupportedMediaTypeError,
    create_media_asset,
    delete_media_asset,
    get_media_asset,
    list_media_assets,
)


router = APIRouter(prefix="/api/media", tags=["media"])
MediaIdPath = Annotated[int, Path(gt=0)]


@router.post(
    "/upload",
    response_model=MediaAssetRead,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
        status.HTTP_413_REQUEST_ENTITY_TOO_LARGE: {"model": ErrorResponse},
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE: {"model": ErrorResponse},
    },
)
async def upload_media_endpoint(
    file: UploadFile = File(...),
    profile_id: int | None = Form(default=None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MediaAssetRead:
    payload = MediaUploadRequest(profile_id=profile_id)
    file_content = await file.read(settings.media_max_file_size_bytes + 1)

    try:
        return create_media_asset(
            db,
            current_user=current_user,
            payload=payload,
            original_filename=file.filename,
            mime_type=file.content_type,
            content=file_content,
        )
    except UnsupportedMediaTypeError as exc:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=str(exc),
        ) from exc
    except MediaTooLargeError as exc:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=str(exc),
        ) from exc
    except MediaProfileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.get(
    "",
    response_model=list[MediaAssetRead],
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse}},
)
def list_media_endpoint(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[MediaAssetRead]:
    return list_media_assets(db, current_user=current_user)


@router.get(
    "/{media_id}",
    response_model=MediaAssetRead,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def get_media_endpoint(
    media_id: MediaIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MediaAssetRead:
    try:
        return get_media_asset(
            db,
            current_user=current_user,
            media_id=media_id,
        )
    except MediaAssetNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.delete(
    "/{media_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)
def delete_media_endpoint(
    media_id: MediaIdPath,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Response:
    try:
        delete_media_asset(
            db,
            current_user=current_user,
            media_id=media_id,
        )
    except MediaAssetNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return Response(status_code=status.HTTP_204_NO_CONTENT)
