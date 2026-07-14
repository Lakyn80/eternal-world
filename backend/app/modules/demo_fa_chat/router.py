from __future__ import annotations

import logging as std_logging
from time import perf_counter
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query, Request, status
from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.core.metrics import observe_fa_chat_error, observe_fa_chat_success
from app.db.session import get_db
from app.modules.avatar_memory_promotions.schemas import (
    AvatarMemoryPromotionRead,
    build_avatar_memory_promotion_read,
)
from app.modules.avatar_memory_promotions.service import (
    AvatarMemoryPromotionInvalidTransitionError,
    AvatarMemoryPromotionNotFoundError,
)
from app.modules.avatar_memory_indexing.schemas import AvatarMemoryIndexingRead
from app.modules.avatar_memory_indexing.service import (
    AvatarMemoryIndexingConflictError,
    AvatarMemoryIndexingEligibilityError,
    AvatarMemoryIndexingExecutionError,
    AvatarMemoryIndexingNotFoundError,
)
from app.modules.conversation_memory_candidates.schemas import (
    MemoryCandidateListResponse,
    MemoryCandidateRead,
    MemoryCandidateReviewUpdate,
    build_memory_candidate_read,
)

from .schemas import (
    DemoFaChatErrorResponse,
    DemoFaChatMemoryCandidateReviewDetail,
    DemoFaChatMemoryCandidateReviewResponse,
    DemoFaChatMemoryCandidateSummaryListResponse,
    DemoFaChatMemoryPromotionListResponse,
    DemoFaChatMessageRequest,
    DemoFaChatMessageResponse,
    DemoFaChatTranslationListResponse,
)
from app.modules.content_translation.schemas import MemoryContentTranslationRead
from .service import (
    DEMO_FA_CHAT_INTERNAL_ERROR_DETAIL,
    DemoFaChatInitializationError,
    DemoFaChatProfileUnavailableError,
    DemoFaChatValidationError,
    approve_demo_memory_candidate,
    archive_demo_memory_candidate,
    build_demo_memory_candidate_review_response,
    cancel_demo_memory_promotion,
    get_demo_memory_candidate,
    get_demo_memory_candidate_review_detail,
    get_demo_memory_promotion,
    index_demo_memory_promotion,
    list_demo_memory_candidate_summaries,
    list_demo_memory_candidate_translations,
    list_demo_memory_candidates,
    list_demo_memory_promotions,
    reject_demo_memory_candidate,
    retry_demo_memory_candidate_translation,
    run_demo_fa_chat_message,
)
from app.modules.conversation_memory_candidates.service import (
    ConversationMemoryCandidateInvalidTransitionError,
    ConversationMemoryCandidateNotFoundError,
)
from app.modules.family_memory_enrichment.service import (
    FamilyMemoryAuthorizationError,
    FamilyMemoryInvalidTransitionError,
    FamilyMemoryNotFoundError,
    validate_demo_actor,
)
from app.modules.family_memory_enrichment.enums import FamilyMemoryActorRole
from app.modules.family_memory_enrichment.schemas import DemoFamilyActorContext


router = APIRouter(prefix="/api/demo/fa-chat", tags=["demo-fa-chat"])
logger = get_logger("demo_fa_chat_router")
CandidateIdPath = Annotated[int, Path(gt=0)]

def _detail(locale: str, *, cs: str, ru: str) -> str:
    """Pick the right-language error detail. Defaults to ``ru`` for any
    ``locale`` other than ``"cs"``, matching this demo's original Russian-only
    behavior for any caller that doesn't pass a locale."""
    return cs if locale == "cs" else ru


def _validate_locale_param(locale: str) -> str:
    if locale not in {"cs", "ru"}:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Unsupported locale. Supported values: cs, ru.",
        )
    return locale


def _candidate_not_found_detail(locale: str) -> str:
    return _detail(locale, cs="Kandidát vzpomínky nebyl nalezen.", ru="Кандидат воспоминания не найден.")


def _candidate_invalid_transition_detail(locale: str) -> str:
    return _detail(
        locale,
        cs="Nepřípustná změna stavu kandidáta.",
        ru="Недопустимое изменение статуса кандидата.",
    )


def _promotion_not_found_detail(locale: str) -> str:
    return _detail(locale, cs="Postoupení vzpomínky nebylo nalezeno.", ru="Продвижение воспоминания не найдено.")


def _promotion_invalid_transition_detail(locale: str) -> str:
    return _detail(
        locale,
        cs="Nepřípustná změna stavu postoupení.",
        ru="Недопустимое изменение статуса продвижения.",
    )


def _promotion_indexing_failed_detail(locale: str) -> str:
    return _detail(
        locale,
        cs="Indexace potvrzené vzpomínky se nezdařila.",
        ru="Индексация подтвержденного воспоминания не выполнена.",
    )


# Backward-compatible Russian-default module-level aliases, for any caller
# that still imports the old constant names directly.
CANDIDATE_NOT_FOUND_DETAIL = _candidate_not_found_detail("ru")
CANDIDATE_INVALID_TRANSITION_DETAIL = _candidate_invalid_transition_detail("ru")
PROMOTION_NOT_FOUND_DETAIL = _promotion_not_found_detail("ru")
PROMOTION_INVALID_TRANSITION_DETAIL = _promotion_invalid_transition_detail("ru")
PROMOTION_INDEXING_FAILED_DETAIL = _promotion_indexing_failed_detail("ru")


def _optional_actor_context(
    *,
    actor_id: str | None,
    actor_role: FamilyMemoryActorRole | None,
    relationship_to_owner: str | None,
    locale: str = "ru",
) -> DemoFamilyActorContext | None:
    if actor_id is None and actor_role is None and relationship_to_owner is None:
        return None
    if actor_id is None or actor_role is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="actor_id and actor_role must be provided together",
        )
    actor = DemoFamilyActorContext(
        actor_id=actor_id,
        actor_role=actor_role,
        relationship_to_owner=relationship_to_owner,
    )
    try:
        validate_demo_actor(actor)
    except FamilyMemoryAuthorizationError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=_detail(
                locale,
                cs="Zadaný kontext rodinného účastníka je neplatný.",
                ru="Указанный контекст участника семьи недопустим.",
            ),
        ) from exc
    return actor


@router.post(
    "/message",
    response_model=DemoFaChatMessageResponse,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": DemoFaChatErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
        status.HTTP_503_SERVICE_UNAVAILABLE: {"model": DemoFaChatErrorResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": DemoFaChatErrorResponse},
    },
)
def send_demo_fa_chat_message(
    payload: DemoFaChatMessageRequest,
    request: Request,
    db: Session = Depends(get_db),
) -> DemoFaChatMessageResponse:
    trace_id = getattr(request.state, "request_id", None) or "unknown"
    started_at = perf_counter()
    debug_enabled = bool(payload.debug)
    try:
        response = run_demo_fa_chat_message(
            db,
            profile_id=payload.profile_id,
            message=payload.message,
            debug=debug_enabled,
            trace_id=trace_id,
            active_memory_candidate_id=payload.active_memory_candidate_id,
            actor_id=payload.actor_id,
            actor_role=payload.actor_role.value if payload.actor_role is not None else None,
            relationship_to_owner=payload.relationship_to_owner,
            locale=payload.locale,
        )
        observe_fa_chat_success(
            duration_seconds=perf_counter() - started_at,
            retrieval_used=response.retrieval_used,
            guard_applied=response.guard_applied,
            guard_reason=response.guard_reason,
            lack_of_evidence=response.lack_of_evidence,
            debug=debug_enabled,
        )
        return response
    except DemoFaChatValidationError as exc:
        observe_fa_chat_error(
            outcome="validation_error",
            debug=debug_enabled,
            duration_seconds=perf_counter() - started_at,
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
    except DemoFaChatProfileUnavailableError as exc:
        observe_fa_chat_error(
            outcome="profile_unavailable",
            debug=debug_enabled,
            duration_seconds=perf_counter() - started_at,
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except DemoFaChatInitializationError as exc:
        observe_fa_chat_error(
            outcome="not_initialized",
            debug=debug_enabled,
            duration_seconds=perf_counter() - started_at,
        )
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc
    except FamilyMemoryAuthorizationError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=_detail(
                payload.locale,
                cs="Rodinný účastník nemá oprávnění provést tuto akci.",
                ru="Участник семьи не имеет права выполнять это действие.",
            ),
        ) from exc
    except FamilyMemoryNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=_detail(
                payload.locale,
                cs="Kandidát rodinné vzpomínky nebyl nalezen.",
                ru="Кандидат семейного воспоминания не найден.",
            ),
        ) from exc
    except FamilyMemoryInvalidTransitionError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=_detail(
                payload.locale,
                cs="Pro kandidáta není žádná čekající doplňující otázka.",
                ru="Для кандидата нет ожидающего уточняющего вопроса.",
            ),
        ) from exc
    except HTTPException:
        raise
    except Exception as exc:
        observe_fa_chat_error(
            outcome="internal_error",
            debug=debug_enabled,
            duration_seconds=perf_counter() - started_at,
        )
        log_event(
            logger,
            std_logging.ERROR,
            "fa_demo_chat_failed",
            trace_id=trace_id,
            profile_id=payload.profile_id,
            error_type=exc.__class__.__name__,
            error_summary=str(exc)[:200],
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=_detail(
                payload.locale,
                cs="Nepodařilo se získat odpověď avatara. Zkuste to prosím znovu.",
                ru=DEMO_FA_CHAT_INTERNAL_ERROR_DETAIL,
            ),
        ) from exc


@router.get(
    "/memory-candidates",
    response_model=MemoryCandidateListResponse,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
    },
)
def list_demo_memory_candidates_endpoint(
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    locale: str = Query(default="ru"),
    db: Session = Depends(get_db),
) -> MemoryCandidateListResponse:
    locale = _validate_locale_param(locale)
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
            locale=locale,
        )
        candidates = list_demo_memory_candidates(
            db,
            profile_id=profile_id,
            actor=actor,
            locale=locale,
        )
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    items = [build_memory_candidate_read(candidate) for candidate in candidates]
    return MemoryCandidateListResponse(items=items, total=len(items))


@router.get(
    "/memory-candidates/review-summary",
    response_model=DemoFaChatMemoryCandidateSummaryListResponse,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
    },
)
def list_demo_memory_candidate_summaries_endpoint(
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    locale: str = Query(default="ru"),
    db: Session = Depends(get_db),
) -> DemoFaChatMemoryCandidateSummaryListResponse:
    """Review-inbox card list (Task 64.5). Must be registered before the
    ``{candidate_id}`` path so the literal ``review-summary`` segment is not
    swallowed by the int path parameter."""
    locale = _validate_locale_param(locale)
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
            locale=locale,
        )
        items = list_demo_memory_candidate_summaries(db, profile_id=profile_id, actor=actor, locale=locale)
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return DemoFaChatMemoryCandidateSummaryListResponse(items=items, total=len(items))


@router.get(
    "/memory-candidates/{candidate_id}",
    response_model=MemoryCandidateRead,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
    },
)
def get_demo_memory_candidate_endpoint(
    candidate_id: CandidateIdPath,
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    locale: str = Query(default="ru"),
    db: Session = Depends(get_db),
) -> MemoryCandidateRead:
    locale = _validate_locale_param(locale)
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
            locale=locale,
        )
        candidate = get_demo_memory_candidate(
            db,
            profile_id=profile_id,
            candidate_id=candidate_id,
            actor=actor,
            locale=locale,
        )
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except ConversationMemoryCandidateNotFoundError as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_candidate_not_found",
            profile_id=profile_id,
            candidate_id=candidate_id,
            error_type=exc.__class__.__name__,
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=_candidate_not_found_detail(locale),
        ) from exc
    except FamilyMemoryNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=_candidate_not_found_detail(locale),
        ) from exc

    return build_memory_candidate_read(candidate)


@router.get(
    "/memory-candidates/{candidate_id}/review-detail",
    response_model=DemoFaChatMemoryCandidateReviewDetail,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
    },
)
def get_demo_memory_candidate_review_detail_endpoint(
    candidate_id: CandidateIdPath,
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    locale: str = Query(default="ru"),
    db: Session = Depends(get_db),
) -> DemoFaChatMemoryCandidateReviewDetail:
    locale = _validate_locale_param(locale)
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
            locale=locale,
        )
        return get_demo_memory_candidate_review_detail(
            db,
            profile_id=profile_id,
            candidate_id=candidate_id,
            actor=actor,
            locale=locale,
        )
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except ConversationMemoryCandidateNotFoundError as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_candidate_not_found",
            profile_id=profile_id,
            candidate_id=candidate_id,
            action="review-detail",
            error_type=exc.__class__.__name__,
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=_candidate_not_found_detail(locale),
        ) from exc
    except FamilyMemoryNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=_candidate_not_found_detail(locale),
        ) from exc


@router.get(
    "/memory-candidates/{candidate_id}/translations",
    response_model=DemoFaChatTranslationListResponse,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
    },
)
def list_demo_memory_candidate_translations_endpoint(
    candidate_id: CandidateIdPath,
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    locale: str = Query(default="ru"),
    db: Session = Depends(get_db),
) -> DemoFaChatTranslationListResponse:
    locale = _validate_locale_param(locale)
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
            locale=locale,
        )
        items = list_demo_memory_candidate_translations(
            db,
            profile_id=profile_id,
            candidate_id=candidate_id,
            actor=actor,
        )
    except (DemoFaChatProfileUnavailableError, ConversationMemoryCandidateNotFoundError, FamilyMemoryNotFoundError) as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=_candidate_not_found_detail(locale),
        ) from exc
    return DemoFaChatTranslationListResponse(items=items, total=len(items))


@router.post(
    "/memory-candidates/{candidate_id}/translations/{target_language}/retry",
    response_model=MemoryContentTranslationRead,
    responses={
        status.HTTP_403_FORBIDDEN: {"model": DemoFaChatErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": DemoFaChatErrorResponse},
    },
)
def retry_demo_memory_candidate_translation_endpoint(
    candidate_id: CandidateIdPath,
    target_language: str,
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    locale: str = Query(default="ru"),
    db: Session = Depends(get_db),
) -> MemoryContentTranslationRead:
    """Explicit owner-only translation retry (Part G.29). Never approves or
    indexes the candidate; safe to call repeatedly."""
    locale = _validate_locale_param(locale)
    if target_language not in {"cs", "ru"}:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Unsupported target language. Supported values: cs, ru.",
        )
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
            locale=locale,
        )
        return retry_demo_memory_candidate_translation(
            db,
            profile_id=profile_id,
            candidate_id=candidate_id,
            target_language=target_language,
            actor=actor,
        )
    except (DemoFaChatProfileUnavailableError, ConversationMemoryCandidateNotFoundError, FamilyMemoryNotFoundError) as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=_candidate_not_found_detail(locale),
        ) from exc
    except FamilyMemoryAuthorizationError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=_detail(
                locale,
                cs="Pouze vlastník avatara může znovu spustit překlad vzpomínky.",
                ru="Только владелец аватара может повторить перевод воспоминания.",
            ),
        ) from exc
    except DemoFaChatValidationError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc


def _review_demo_memory_candidate(
    *,
    db: Session,
    profile_id: int | None,
    candidate_id: int,
    payload: MemoryCandidateReviewUpdate | None,
    action: str,
    locale: str = "ru",
 ) -> MemoryCandidateRead | DemoFaChatMemoryCandidateReviewResponse:
    action_map = {
        "approve": approve_demo_memory_candidate,
        "reject": reject_demo_memory_candidate,
        "archive": archive_demo_memory_candidate,
    }
    handler = action_map[action]
    try:
        candidate = handler(
            db,
            profile_id=profile_id,
            candidate_id=candidate_id,
            payload=payload,
        )
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except ConversationMemoryCandidateNotFoundError as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_candidate_not_found",
            profile_id=profile_id,
            candidate_id=candidate_id,
            action=action,
            error_type=exc.__class__.__name__,
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=_candidate_not_found_detail(locale),
        ) from exc
    except ConversationMemoryCandidateInvalidTransitionError as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_candidate_invalid_transition",
            profile_id=profile_id,
            candidate_id=candidate_id,
            action=action,
            error_type=exc.__class__.__name__,
            error_summary=str(exc)[:200],
        )
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=_candidate_invalid_transition_detail(locale),
        ) from exc
    except FamilyMemoryAuthorizationError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=_detail(
                locale,
                cs="Pro obohacenou vzpomínku je vyžadována výslovná kontrola vlastníkem.",
                ru="Для обогащённого воспоминания требуется явная проверка владельцем.",
            ),
        ) from exc

    if action == "approve":
        return build_demo_memory_candidate_review_response(candidate)
    return build_memory_candidate_read(candidate)


@router.post(
    "/memory-candidates/{candidate_id}/approve",
    response_model=DemoFaChatMemoryCandidateReviewResponse,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
        status.HTTP_409_CONFLICT: {"model": DemoFaChatErrorResponse},
    },
)
def approve_demo_memory_candidate_endpoint(
    candidate_id: CandidateIdPath,
    payload: MemoryCandidateReviewUpdate | None = None,
    profile_id: int | None = None,
    locale: str = Query(default="ru"),
    db: Session = Depends(get_db),
) -> DemoFaChatMemoryCandidateReviewResponse:
    return _review_demo_memory_candidate(
        db=db,
        profile_id=profile_id,
        candidate_id=candidate_id,
        payload=payload,
        action="approve",
        locale=_validate_locale_param(locale),
    )


@router.get(
    "/memory-promotions",
    response_model=DemoFaChatMemoryPromotionListResponse,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
    },
)
def list_demo_memory_promotions_endpoint(
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    locale: str = Query(default="ru"),
    db: Session = Depends(get_db),
) -> DemoFaChatMemoryPromotionListResponse:
    locale = _validate_locale_param(locale)
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
            locale=locale,
        )
        promotions = list_demo_memory_promotions(
            db,
            profile_id=profile_id,
            actor=actor,
            locale=locale,
        )
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    items = [build_avatar_memory_promotion_read(promotion) for promotion in promotions]
    return DemoFaChatMemoryPromotionListResponse(items=items, total=len(items))


@router.get(
    "/memory-promotions/{promotion_id}",
    response_model=AvatarMemoryPromotionRead,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
    },
)
def get_demo_memory_promotion_endpoint(
    promotion_id: CandidateIdPath,
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    locale: str = Query(default="ru"),
    db: Session = Depends(get_db),
) -> AvatarMemoryPromotionRead:
    locale = _validate_locale_param(locale)
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
            locale=locale,
        )
        promotion = get_demo_memory_promotion(
            db,
            profile_id=profile_id,
            promotion_id=promotion_id,
            actor=actor,
            locale=locale,
        )
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except AvatarMemoryPromotionNotFoundError as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_promotion_not_found",
            profile_id=profile_id,
            promotion_id=promotion_id,
            error_type=exc.__class__.__name__,
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=_promotion_not_found_detail(locale),
        ) from exc
    except FamilyMemoryNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=_promotion_not_found_detail(locale),
        ) from exc

    return build_avatar_memory_promotion_read(promotion)


@router.post(
    "/memory-promotions/{promotion_id}/cancel",
    response_model=AvatarMemoryPromotionRead,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
        status.HTTP_409_CONFLICT: {"model": DemoFaChatErrorResponse},
    },
)
def cancel_demo_memory_promotion_endpoint(
    promotion_id: CandidateIdPath,
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    locale: str = Query(default="ru"),
    db: Session = Depends(get_db),
) -> AvatarMemoryPromotionRead:
    locale = _validate_locale_param(locale)
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
            locale=locale,
        )
        promotion = cancel_demo_memory_promotion(
            db,
            profile_id=profile_id,
            promotion_id=promotion_id,
            actor=actor,
            locale=locale,
        )
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except AvatarMemoryPromotionNotFoundError as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_promotion_not_found",
            profile_id=profile_id,
            promotion_id=promotion_id,
            action="cancel",
            error_type=exc.__class__.__name__,
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=_promotion_not_found_detail(locale),
        ) from exc
    except AvatarMemoryPromotionInvalidTransitionError as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_promotion_invalid_transition",
            profile_id=profile_id,
            promotion_id=promotion_id,
            action="cancel",
            error_type=exc.__class__.__name__,
            error_summary=str(exc)[:200],
        )
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=_promotion_invalid_transition_detail(locale),
        ) from exc
    except FamilyMemoryAuthorizationError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=_detail(
                locale,
                cs="Pouze vlastník avatara může zrušit postoupení vzpomínky.",
                ru="Только владелец аватара может отменить продвижение воспоминания.",
            ),
        ) from exc

    return build_avatar_memory_promotion_read(promotion)


@router.post(
    "/memory-promotions/{promotion_id}/index",
    response_model=AvatarMemoryIndexingRead,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
        status.HTTP_409_CONFLICT: {"model": DemoFaChatErrorResponse},
        status.HTTP_503_SERVICE_UNAVAILABLE: {"model": DemoFaChatErrorResponse},
    },
)
def index_demo_memory_promotion_endpoint(
    promotion_id: CandidateIdPath,
    profile_id: int | None = None,
    actor_id: str | None = Query(default=None, min_length=1, max_length=120),
    actor_role: FamilyMemoryActorRole | None = Query(default=None),
    relationship_to_owner: str | None = Query(default=None, max_length=120),
    locale: str = Query(default="ru"),
    db: Session = Depends(get_db),
) -> AvatarMemoryIndexingRead:
    locale = _validate_locale_param(locale)
    try:
        actor = _optional_actor_context(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
            locale=locale,
        )
        return index_demo_memory_promotion(
            db,
            profile_id=profile_id,
            promotion_id=promotion_id,
            actor=actor,
            locale=locale,
        )
    except (AvatarMemoryPromotionNotFoundError, AvatarMemoryIndexingNotFoundError) as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_promotion_not_found",
            profile_id=profile_id,
            promotion_id=promotion_id,
            action="index",
            error_type=exc.__class__.__name__,
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=_promotion_not_found_detail(locale),
        ) from exc
    except DemoFaChatProfileUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except (AvatarMemoryIndexingEligibilityError, AvatarMemoryIndexingConflictError) as exc:
        log_event(
            logger,
            std_logging.INFO,
            "fa_demo_chat_memory_promotion_index_rejected",
            profile_id=profile_id,
            promotion_id=promotion_id,
            action="index",
            error_type=exc.__class__.__name__,
        )
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=_promotion_invalid_transition_detail(locale),
        ) from exc
    except AvatarMemoryIndexingExecutionError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=_promotion_indexing_failed_detail(locale),
        ) from exc
    except FamilyMemoryAuthorizationError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=_detail(
                locale,
                cs="Pouze vlastník avatara může vzpomínku indexovat.",
                ru="Только владелец аватара может индексировать воспоминание.",
            ),
        ) from exc


@router.post(
    "/memory-candidates/{candidate_id}/reject",
    response_model=MemoryCandidateRead,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
        status.HTTP_409_CONFLICT: {"model": DemoFaChatErrorResponse},
    },
)
def reject_demo_memory_candidate_endpoint(
    candidate_id: CandidateIdPath,
    payload: MemoryCandidateReviewUpdate | None = None,
    profile_id: int | None = None,
    locale: str = Query(default="ru"),
    db: Session = Depends(get_db),
) -> MemoryCandidateRead:
    return _review_demo_memory_candidate(
        db=db,
        profile_id=profile_id,
        candidate_id=candidate_id,
        payload=payload,
        action="reject",
        locale=_validate_locale_param(locale),
    )


@router.post(
    "/memory-candidates/{candidate_id}/archive",
    response_model=MemoryCandidateRead,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": DemoFaChatErrorResponse},
        status.HTTP_409_CONFLICT: {"model": DemoFaChatErrorResponse},
    },
)
def archive_demo_memory_candidate_endpoint(
    candidate_id: CandidateIdPath,
    payload: MemoryCandidateReviewUpdate | None = None,
    profile_id: int | None = None,
    locale: str = Query(default="ru"),
    db: Session = Depends(get_db),
) -> MemoryCandidateRead:
    return _review_demo_memory_candidate(
        db=db,
        profile_id=profile_id,
        candidate_id=candidate_id,
        payload=payload,
        action="archive",
        locale=_validate_locale_param(locale),
    )
