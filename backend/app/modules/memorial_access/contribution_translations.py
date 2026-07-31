"""Memorial contribution translation helpers (Task 65.13.3).

Preserves exact original ``memory_text`` / ``source_language``. Derived
canonical and viewer texts live in ``MemoryContentTranslation`` rows with
``entity_type=memorial_contribution`` — never mixed into RAG indexing here.
"""

from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.db.models import MemorialContribution, MemoryContentTranslation, MemoryProfile, User
from app.modules.content_translation.enums import CURRENT_USABLE_TRANSLATION_STATUSES
from app.modules.content_translation.repository import get_current
from app.modules.content_translation.schemas import TranslationFieldRequest
from app.modules.content_translation.service import translate_content_field
from app.modules.language_registry import assert_translation_language, normalize_language_code
from app.modules.provider_usage.context import AiCallContext
from app.modules.provider_usage.enums import AiFeature, ExecutionSource


FIELD_MEMORY_TEXT = "memory_text"
ENTITY_MEMORIAL_CONTRIBUTION = "memorial_contribution"


@dataclass(frozen=True, slots=True)
class ContributionLocalizedViews:
    source_language: str
    memory_text: str
    canonical_language: str
    canonical_text: str | None
    canonical_translation_status: str
    display_language: str
    display_text: str | None
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


def ensure_contribution_translation(
    db: Session,
    *,
    contribution: MemorialContribution,
    target_language: str,
    actor: User,
) -> MemoryContentTranslation:
    """Translate (or identity-skip) contribution text into ``target_language``."""

    target = assert_translation_language(target_language)
    source = assert_translation_language(contribution.source_language)
    return translate_content_field(
        db,
        TranslationFieldRequest(
            profile_id=contribution.profile_id,
            entity_type=ENTITY_MEMORIAL_CONTRIBUTION,
            entity_id=str(contribution.id),
            field_name=FIELD_MEMORY_TEXT,
            source_language=source,
            target_language=target,
            source_text=contribution.memory_text,
        ),
        call_context=_call_context(user=actor, profile_id=contribution.profile_id),
    )


def ensure_canonical_and_author_display(
    db: Session,
    *,
    contribution: MemorialContribution,
    profile: MemoryProfile,
    author: User,
) -> None:
    """On submit: ensure canonical translation (+ author UI lang when distinct)."""

    ensure_contribution_translation(
        db,
        contribution=contribution,
        target_language=profile.canonical_language,
        actor=author,
    )
    author_ui = normalize_language_code(author.preferred_ui_language)
    if author_ui and author_ui not in {contribution.source_language, profile.canonical_language}:
        ensure_contribution_translation(
            db,
            contribution=contribution,
            target_language=author_ui,
            actor=author,
        )


def _usable_text(row: MemoryContentTranslation | None) -> tuple[str | None, str]:
    if row is None:
        return None, "missing"
    status = row.translation_status
    if status in CURRENT_USABLE_TRANSLATION_STATUSES and row.translated_text:
        return row.translated_text, status
    return None, status


def resolve_contribution_localized_views(
    db: Session,
    *,
    contribution: MemorialContribution,
    profile: MemoryProfile,
    viewer: User,
    for_review: bool,
    ensure_missing: bool = True,
) -> ContributionLocalizedViews:
    """Resolve original / canonical / viewer display texts for API responses.

    Review surfaces prefer canonical text and ignore the reviewer's temporary
    UI language for the body. Viewer/list surfaces prefer the viewer's
    ``preferred_ui_language`` when a usable translation exists.
    """

    canonical_lang = assert_translation_language(profile.canonical_language)
    source_lang = assert_translation_language(contribution.source_language)

    canonical_row = get_current(
        db,
        entity_type=ENTITY_MEMORIAL_CONTRIBUTION,
        entity_id=str(contribution.id),
        field_name=FIELD_MEMORY_TEXT,
        target_language=canonical_lang,
    )
    if ensure_missing and canonical_row is None:
        canonical_row = ensure_contribution_translation(
            db,
            contribution=contribution,
            target_language=canonical_lang,
            actor=viewer,
        )
        db.flush()

    canonical_text, canonical_status = _usable_text(canonical_row)
    if canonical_text is None and source_lang == canonical_lang:
        canonical_text = contribution.memory_text
        canonical_status = "identity"

    display_lang = normalize_language_code(viewer.preferred_ui_language) or source_lang
    if for_review:
        # Owner/trusted_reviewer review body is always canonical-facing.
        return ContributionLocalizedViews(
            source_language=source_lang,
            memory_text=contribution.memory_text,
            canonical_language=canonical_lang,
            canonical_text=canonical_text,
            canonical_translation_status=canonical_status,
            display_language=canonical_lang,
            display_text=canonical_text,
            display_translation_status=canonical_status,
        )

    if display_lang == source_lang:
        return ContributionLocalizedViews(
            source_language=source_lang,
            memory_text=contribution.memory_text,
            canonical_language=canonical_lang,
            canonical_text=canonical_text,
            canonical_translation_status=canonical_status,
            display_language=display_lang,
            display_text=contribution.memory_text,
            display_translation_status="identity",
        )

    display_row = get_current(
        db,
        entity_type=ENTITY_MEMORIAL_CONTRIBUTION,
        entity_id=str(contribution.id),
        field_name=FIELD_MEMORY_TEXT,
        target_language=display_lang,
    )
    if ensure_missing and display_row is None:
        display_row = ensure_contribution_translation(
            db,
            contribution=contribution,
            target_language=display_lang,
            actor=viewer,
        )
        db.flush()

    display_text, display_status = _usable_text(display_row)
    if display_text is None:
        # Safe fallback: original source, never invent text.
        display_text = contribution.memory_text
        display_lang = source_lang
        display_status = "fallback_original"

    return ContributionLocalizedViews(
        source_language=source_lang,
        memory_text=contribution.memory_text,
        canonical_language=canonical_lang,
        canonical_text=canonical_text,
        canonical_translation_status=canonical_status,
        display_language=display_lang,
        display_text=display_text,
        display_translation_status=display_status,
    )
