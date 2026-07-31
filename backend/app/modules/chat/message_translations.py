"""Chat message translation helpers (Task 65.13.5).

User ``ChatMessage.content`` stays the exact original. Derived canonical user
text and viewer display of assistant replies live in
``MemoryContentTranslation`` with ``entity_type=chat_message``.
Assistant ``content`` is stored already in memorial canonical language.
"""

from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.db.models import ChatMessage, MemoryContentTranslation, MemoryProfile, User
from app.modules.content_translation.enums import CURRENT_USABLE_TRANSLATION_STATUSES
from app.modules.content_translation.repository import get_current
from app.modules.content_translation.schemas import TranslationFieldRequest
from app.modules.content_translation.service import translate_content_field
from app.modules.language_registry import (
    assert_canonical_memorial_language,
    assert_translation_language,
    normalize_language_code,
)
from app.modules.provider_usage.context import AiCallContext
from app.modules.provider_usage.enums import AiFeature, ExecutionSource


ENTITY_CHAT_MESSAGE = "chat_message"
FIELD_CONTENT = "content"


@dataclass(frozen=True, slots=True)
class ChatMessageViews:
    original_text: str
    source_language: str | None
    canonical_language: str
    canonical_text: str | None
    canonical_translation_status: str
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


def _usable_text(row: MemoryContentTranslation | None) -> tuple[str | None, str]:
    if row is None:
        return None, "missing"
    if row.translation_status in CURRENT_USABLE_TRANSLATION_STATUSES and row.translated_text:
        return row.translated_text, row.translation_status
    return None, row.translation_status


def ensure_chat_message_translation(
    db: Session,
    *,
    profile_id: int,
    message_id: int,
    source_language: str,
    target_language: str,
    source_text: str,
    actor: User,
) -> MemoryContentTranslation:
    target = assert_translation_language(target_language)
    source = assert_translation_language(source_language)
    return translate_content_field(
        db,
        TranslationFieldRequest(
            profile_id=profile_id,
            entity_type=ENTITY_CHAT_MESSAGE,
            entity_id=str(message_id),
            field_name=FIELD_CONTENT,
            source_language=source,
            target_language=target,
            source_text=source_text,
        ),
        call_context=_call_context(user=actor, profile_id=profile_id),
    )


def ensure_user_canonical_translation(
    db: Session,
    *,
    profile: MemoryProfile,
    message: ChatMessage,
    source_language: str,
    actor: User,
) -> MemoryContentTranslation:
    """Translate (or identity-skip) the user original into memorial canonical."""

    return ensure_chat_message_translation(
        db,
        profile_id=profile.id,
        message_id=message.id,
        source_language=source_language,
        target_language=assert_canonical_memorial_language(profile.canonical_language),
        source_text=message.content,
        actor=actor,
    )


def ensure_assistant_display_translation(
    db: Session,
    *,
    profile: MemoryProfile,
    message: ChatMessage,
    display_language: str,
    actor: User,
) -> MemoryContentTranslation:
    """Translate canonical assistant text into the viewer display language."""

    return ensure_chat_message_translation(
        db,
        profile_id=profile.id,
        message_id=message.id,
        source_language=assert_canonical_memorial_language(profile.canonical_language),
        target_language=display_language,
        source_text=message.content,
        actor=actor,
    )


def resolve_user_canonical_text(
    db: Session,
    *,
    profile: MemoryProfile,
    message: ChatMessage,
    actor: User,
    ensure_missing: bool = True,
) -> tuple[str, str]:
    """Return ``(text_for_brain_or_rag, status)``.

    On missing/failed translation falls back to the durable original so chat
    never blocks on the translation provider.
    """

    canonical_lang = assert_canonical_memorial_language(profile.canonical_language)
    source_lang = normalize_language_code(message.source_language) or canonical_lang

    if source_lang == canonical_lang:
        return message.content, "identity"

    row = get_current(
        db,
        entity_type=ENTITY_CHAT_MESSAGE,
        entity_id=str(message.id),
        field_name=FIELD_CONTENT,
        target_language=canonical_lang,
    )
    if ensure_missing and row is None and message.source_language:
        row = ensure_user_canonical_translation(
            db,
            profile=profile,
            message=message,
            source_language=source_lang,
            actor=actor,
        )
        db.flush()

    text, status = _usable_text(row)
    if text is None:
        return message.content, "fallback_original"
    return text, status


def resolve_chat_message_views(
    db: Session,
    *,
    message: ChatMessage,
    profile: MemoryProfile,
    viewer: User,
    display_locale: str | None = None,
    ensure_missing: bool = True,
) -> ChatMessageViews:
    """Resolve original / canonical / display views for API responses."""

    canonical_lang = assert_canonical_memorial_language(profile.canonical_language)
    source_lang = normalize_language_code(message.source_language)

    display_lang = (
        normalize_language_code(display_locale)
        or normalize_language_code(viewer.preferred_ui_language)
        or canonical_lang
    )

    if message.role == "user":
        canonical_text, canonical_status = resolve_user_canonical_text(
            db,
            profile=profile,
            message=message,
            actor=viewer,
            ensure_missing=ensure_missing,
        )
        # User bubbles always show the durable original.
        return ChatMessageViews(
            original_text=message.content,
            source_language=source_lang,
            canonical_language=canonical_lang,
            canonical_text=canonical_text,
            canonical_translation_status=canonical_status,
            display_language=source_lang or canonical_lang,
            display_text=message.content,
            display_translation_status="identity",
        )

    # Assistant: content is memorial-canonical; display may differ.
    if display_lang == canonical_lang:
        return ChatMessageViews(
            original_text=message.content,
            source_language=None,
            canonical_language=canonical_lang,
            canonical_text=message.content,
            canonical_translation_status="identity",
            display_language=display_lang,
            display_text=message.content,
            display_translation_status="identity",
        )

    row = get_current(
        db,
        entity_type=ENTITY_CHAT_MESSAGE,
        entity_id=str(message.id),
        field_name=FIELD_CONTENT,
        target_language=display_lang,
    )
    if ensure_missing and row is None:
        row = ensure_assistant_display_translation(
            db,
            profile=profile,
            message=message,
            display_language=display_lang,
            actor=viewer,
        )
        db.flush()

    display_text, display_status = _usable_text(row)
    if display_text is None:
        return ChatMessageViews(
            original_text=message.content,
            source_language=None,
            canonical_language=canonical_lang,
            canonical_text=message.content,
            canonical_translation_status="identity",
            display_language=canonical_lang,
            display_text=message.content,
            display_translation_status="fallback_original",
        )

    return ChatMessageViews(
        original_text=message.content,
        source_language=None,
        canonical_language=canonical_lang,
        canonical_text=message.content,
        canonical_translation_status="identity",
        display_language=display_lang,
        display_text=display_text,
        display_translation_status=display_status,
    )
