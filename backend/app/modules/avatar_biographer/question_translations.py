"""Biographer question/answer translation helpers (Task 65.13.4).

Canonical question text is stored on ``BiographerQuestion.question_text`` in
the memorial ``canonical_language``. Viewer/UI locales get derived rows in
``MemoryContentTranslation`` — they never create a second pending question.
"""

from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.db.models import BiographerQuestion, MemoryContentTranslation, MemoryProfile, User
from app.modules.content_translation.enums import CURRENT_USABLE_TRANSLATION_STATUSES
from app.modules.content_translation.repository import get_current
from app.modules.content_translation.schemas import TranslationFieldRequest
from app.modules.content_translation.service import translate_content_field
from app.modules.language_registry import assert_translation_language, normalize_language_code
from app.modules.provider_usage.context import AiCallContext
from app.modules.provider_usage.enums import AiFeature, ExecutionSource


ENTITY_BIOGRAPHER_QUESTION = "biographer_question"
ENTITY_BIOGRAPHER_ANSWER = "biographer_answer"
FIELD_QUESTION_TEXT = "question_text"
FIELD_ANSWER_TEXT = "answer_text"


@dataclass(frozen=True, slots=True)
class BiographerQuestionViews:
    question_text: str
    canonical_language: str
    display_language: str
    display_text: str
    display_translation_status: str


def _call_context(*, user: User, profile_id: int) -> AiCallContext:
    return AiCallContext(
        feature=AiFeature.DYNAMIC_MEMORY_TRANSLATION,
        execution_source=ExecutionSource.FASTAPI,
        user_id=user.id,
        memorial_id=profile_id,
        requested_locale=normalize_language_code(user.preferred_ui_language),
        resolved_locale=normalize_language_code(user.preferred_ui_language),
    )


def ensure_biographer_question_translation(
    db: Session,
    *,
    question: BiographerQuestion,
    target_language: str,
    actor: User,
) -> MemoryContentTranslation:
    target = assert_translation_language(target_language)
    source = assert_translation_language(question.locale)
    return translate_content_field(
        db,
        TranslationFieldRequest(
            profile_id=question.profile_id,
            entity_type=ENTITY_BIOGRAPHER_QUESTION,
            entity_id=str(question.id),
            field_name=FIELD_QUESTION_TEXT,
            source_language=source,
            target_language=target,
            source_text=question.question_text,
        ),
        call_context=_call_context(user=actor, profile_id=question.profile_id),
    )


def ensure_biographer_answer_translation(
    db: Session,
    *,
    profile: MemoryProfile,
    candidate_id: int,
    source_language: str,
    answer_text: str,
    actor: User,
) -> MemoryContentTranslation:
    """Translate a biographer answer into the memorial canonical language."""

    target = assert_translation_language(profile.canonical_language)
    source = assert_translation_language(source_language)
    return translate_content_field(
        db,
        TranslationFieldRequest(
            profile_id=profile.id,
            entity_type=ENTITY_BIOGRAPHER_ANSWER,
            entity_id=str(candidate_id),
            field_name=FIELD_ANSWER_TEXT,
            source_language=source,
            target_language=target,
            source_text=answer_text,
        ),
        call_context=_call_context(user=actor, profile_id=profile.id),
    )


def _usable_text(row: MemoryContentTranslation | None) -> tuple[str | None, str]:
    if row is None:
        return None, "missing"
    if row.translation_status in CURRENT_USABLE_TRANSLATION_STATUSES and row.translated_text:
        return row.translated_text, row.translation_status
    return None, row.translation_status


def resolve_biographer_question_views(
    db: Session,
    *,
    question: BiographerQuestion,
    profile: MemoryProfile,
    viewer: User,
    display_locale: str | None,
    ensure_missing: bool = True,
) -> BiographerQuestionViews:
    canonical_lang = assert_translation_language(profile.canonical_language)
    display_lang = (
        normalize_language_code(display_locale)
        or normalize_language_code(viewer.preferred_ui_language)
        or canonical_lang
    )

    if display_lang == question.locale:
        return BiographerQuestionViews(
            question_text=question.question_text,
            canonical_language=canonical_lang,
            display_language=display_lang,
            display_text=question.question_text,
            display_translation_status="identity",
        )

    row = get_current(
        db,
        entity_type=ENTITY_BIOGRAPHER_QUESTION,
        entity_id=str(question.id),
        field_name=FIELD_QUESTION_TEXT,
        target_language=display_lang,
    )
    if ensure_missing and row is None:
        row = ensure_biographer_question_translation(
            db,
            question=question,
            target_language=display_lang,
            actor=viewer,
        )
        db.flush()

    display_text, status = _usable_text(row)
    if display_text is None:
        return BiographerQuestionViews(
            question_text=question.question_text,
            canonical_language=canonical_lang,
            display_language=question.locale,
            display_text=question.question_text,
            display_translation_status="fallback_original",
        )
    return BiographerQuestionViews(
        question_text=question.question_text,
        canonical_language=canonical_lang,
        display_language=display_lang,
        display_text=display_text,
        display_translation_status=status,
    )
