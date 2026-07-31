from __future__ import annotations

import hashlib
from time import perf_counter

from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.core.metrics import (
    observe_content_translation_attempt,
    observe_content_translation_retry,
    set_content_translation_status_current,
)
from app.db.models import MemoryContentTranslation, User
from app.modules.content_translation import repository
from app.modules.content_translation.authorization import assert_can_review_content_translation
from app.modules.content_translation.provider import (
    ContentTranslationProvider,
    ContentTranslationProviderRequestError,
    ContentTranslationProviderResponseError,
    build_content_translation_provider,
)
from app.modules.content_translation.schemas import TranslationFieldRequest
from app.modules.content_translation.validators import (
    ContentTranslationValidationError,
    validate_translation_result,
)
from app.modules.language_registry import assert_translation_language, normalize_language_code
from app.modules.provider_usage.context import AiCallContext
from app.modules.provider_usage.enums import AiStepType
from app.modules.provider_usage.service import (
    AuditFinalizationError,
    AuditPersistenceError,
    run_instrumented_single_attempt_action,
)
from app.modules.provider_usage.usage import normalize_openai_compatible_usage


logger = get_logger("content_translation")


def compute_source_hash(source_text: str) -> str:
    return hashlib.sha256(source_text.encode("utf-8")).hexdigest()


def _normalize_request_languages(request: TranslationFieldRequest) -> tuple[str, str]:
    source = assert_translation_language(str(request.source_language))
    target = assert_translation_language(str(request.target_language))
    return source, target


def translate_content_field(
    db: Session,
    request: TranslationFieldRequest,
    *,
    call_context: AiCallContext,
    provider: ContentTranslationProvider | None = None,
) -> MemoryContentTranslation:
    """Translate one field and persist the resulting state.

    Never raises on provider failure - a failed translation is recorded as
    ``translation_status=failed`` and returned normally, so a caller
    persisting a Czech contribution/candidate can never have that write
    rolled back by a translation-provider outage. Never approves memory,
    never writes to Qdrant, and never overwrites ``source_text`` with the
    translated text.

    When ``source_language == target_language``, no provider is called; an
    identity translation is persisted (Task 65.13.2).

    ``call_context`` (Task 66.1) attributes this exact provider call to a
    durable ``AiAction``/token/cost record via the shared instrumentation
    wrapper - every caller must build one explicitly (feature/execution
    source/user or memorial identity where known) rather than relying on a
    default, since translation calls happen from several different features
    (dynamic chat translation, memory candidate/contribution finalization).
    """
    source_language, target_language = _normalize_request_languages(request)
    source_hash = compute_source_hash(request.source_text)
    row = repository.start_pending_attempt(
        db,
        profile_id=request.profile_id,
        candidate_id=request.candidate_id,
        contribution_id=request.contribution_id,
        clarification_id=request.clarification_id,
        entity_type=str(request.entity_type),
        entity_id=request.entity_id,
        field_name=request.field_name,
        source_language=source_language,
        target_language=target_language,
        source_text=request.source_text,
        source_hash=source_hash,
    )

    if source_language == target_language:
        repository.mark_identity_translation(db, row, source_text=request.source_text)
        set_content_translation_status_current(counts_by_status=repository.count_by_status(db))
        observe_content_translation_attempt(
            source_language=source_language,
            target_language=target_language,
            result="success",
            duration_seconds=0.0,
        )
        log_event(
            logger,
            20,
            "content_translation_identity_skipped",
            profile_id=request.profile_id,
            entity_type=str(request.entity_type),
            field_name=request.field_name,
            source_language=source_language,
            target_language=target_language,
            translation_version=row.translation_version,
        )
        return row

    active_provider = provider or build_content_translation_provider()
    started_at = perf_counter()

    def _translate_and_validate():
        response = active_provider.translate(
            source_text=request.source_text,
            source_language=source_language,
            target_language=target_language,
        )
        validate_translation_result(source_text=request.source_text, result=response.result)
        return response

    try:
        response, _ai_action = run_instrumented_single_attempt_action(
            db,
            context=call_context,
            step_type=AiStepType.PROVIDER_TRANSLATION,
            provider=active_provider.provider_name,
            model=getattr(active_provider, "model", "mock"),
            operation=_translate_and_validate,
            extract_token_usage=lambda resp: normalize_openai_compatible_usage(
                raw_response={"id": resp.provider_request_id, "usage": resp.usage}
            ),
        )
    except (
        ContentTranslationProviderRequestError,
        ContentTranslationProviderResponseError,
        ContentTranslationValidationError,
        AuditPersistenceError,
        AuditFinalizationError,
    ) as exc:
        repository.mark_failed(db, row)
        set_content_translation_status_current(counts_by_status=repository.count_by_status(db))
        observe_content_translation_attempt(
            source_language=source_language,
            target_language=target_language,
            result="failed",
            duration_seconds=perf_counter() - started_at,
        )
        log_event(
            logger,
            30,
            "content_translation_failed",
            profile_id=request.profile_id,
            candidate_id=request.candidate_id,
            entity_type=str(request.entity_type),
            field_name=request.field_name,
            source_language=source_language,
            target_language=target_language,
            error_type=exc.__class__.__name__,
        )
        return row

    repository.mark_translated(
        db,
        row,
        translated_text=response.result.translated_text,
        provider=response.provider_name,
        model=response.model,
    )
    set_content_translation_status_current(counts_by_status=repository.count_by_status(db))
    observe_content_translation_attempt(
        source_language=source_language,
        target_language=target_language,
        result="success",
        duration_seconds=perf_counter() - started_at,
    )
    log_event(
        logger,
        20,
        "content_translation_succeeded",
        profile_id=request.profile_id,
        candidate_id=request.candidate_id,
        entity_type=str(request.entity_type),
        field_name=request.field_name,
        source_language=source_language,
        target_language=target_language,
        translation_version=row.translation_version,
    )
    return row


def retry_translation(
    db: Session,
    *,
    entity_type: str,
    entity_id: str,
    field_name: str,
    source_language: str,
    target_language: str,
    source_text: str,
    candidate_id: int | None,
    call_context: AiCallContext,
    contribution_id: int | None = None,
    clarification_id: int | None = None,
    profile_id: int | None = None,
    provider: ContentTranslationProvider | None = None,
) -> MemoryContentTranslation:
    """Explicit, idempotent-in-effect retry of a translation.

    Always re-attempts the provider call for the *current* source text (it
    never approves or indexes memory). Safe to call repeatedly.
    """
    result = translate_content_field(
        db,
        TranslationFieldRequest(
            profile_id=profile_id,
            candidate_id=candidate_id,
            contribution_id=contribution_id,
            clarification_id=clarification_id,
            entity_type=entity_type,
            entity_id=entity_id,
            field_name=field_name,
            source_language=source_language,
            target_language=target_language,
            source_text=source_text,
        ),
        call_context=call_context,
        provider=provider,
    )
    observe_content_translation_retry(
        result="success" if result.translation_status in {"translated", "human_reviewed"} else "failed"
    )
    return result


def apply_human_translation_override(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    entity_type: str,
    entity_id: str,
    field_name: str,
    target_language: str,
    translated_text: str,
) -> MemoryContentTranslation:
    """Authorize + persist a human override of the current translation row."""

    assert_can_review_content_translation(db, current_user=current_user, profile_id=profile_id)
    normalized_target = assert_translation_language(target_language)
    cleaned = translated_text.strip()
    if not cleaned:
        raise ValueError("translated_text must not be empty")
    row = repository.get_current(
        db,
        entity_type=entity_type,
        entity_id=entity_id,
        field_name=field_name,
        target_language=normalized_target,
    )
    if row is None:
        raise ValueError("translation row not found")
    if row.profile_id is not None and int(row.profile_id) != int(profile_id):
        raise ValueError("translation row profile mismatch")
    return repository.apply_human_override(
        db,
        row,
        translated_text=cleaned,
        reviewed_by=f"user:{current_user.id}",
    )


def mark_translation_human_reviewed(
    db: Session,
    *,
    current_user: User,
    profile_id: int,
    entity_type: str,
    entity_id: str,
    field_name: str,
    target_language: str,
) -> MemoryContentTranslation:
    """Authorize + mark an existing translation as human-reviewed."""

    assert_can_review_content_translation(db, current_user=current_user, profile_id=profile_id)
    normalized_target = assert_translation_language(target_language)
    row = repository.get_current(
        db,
        entity_type=entity_type,
        entity_id=entity_id,
        field_name=field_name,
        target_language=normalized_target,
    )
    if row is None:
        raise ValueError("translation row not found")
    if row.profile_id is not None and int(row.profile_id) != int(profile_id):
        raise ValueError("translation row profile mismatch")
    return repository.mark_human_reviewed(db, row, reviewed_by=f"user:{current_user.id}")


def get_translations_for_candidate(db: Session, *, candidate_id: int) -> list[MemoryContentTranslation]:
    return repository.list_for_candidate(db, candidate_id=candidate_id)


def get_translations_for_profile(db: Session, *, profile_id: int) -> list[MemoryContentTranslation]:
    return repository.list_for_profile(db, profile_id=profile_id)


def resolve_required_translation_block_reason(
    db: Session,
    *,
    entity_type: str,
    entity_id: str,
    field_name: str,
    target_language: str,
    current_source_text: str,
) -> str | None:
    """Return a stable block-reason code, or ``None`` if the translation is usable.

    Reasons: ``russian_translation_missing`` (no successful translation
    exists yet - includes ``pending``/never attempted), ``russian_translation_failed``
    (last attempt failed and the source has not changed since), or
    ``russian_translation_stale`` (a translation exists but the source text
    has since changed). Named with an ``ru`` prefix because Russian is the
    only currently-required target language for indexing eligibility; the
    function itself is generic over ``target_language``.
    """
    normalized_target = normalize_language_code(target_language) or target_language
    row = repository.get_current(
        db,
        entity_type=entity_type,
        entity_id=entity_id,
        field_name=field_name,
        target_language=normalized_target,
    )
    language_names = {"ru": "russian", "cs": "czech", "en": "english", "de": "german"}
    prefix = f"{language_names.get(normalized_target, normalized_target)}_translation"
    if row is None:
        return f"{prefix}_missing"
    current_hash = compute_source_hash(current_source_text)
    if row.source_hash != current_hash:
        return f"{prefix}_stale"
    if row.translation_status == "failed":
        return f"{prefix}_failed"
    if row.translation_status not in {"translated", "human_reviewed"}:
        return f"{prefix}_missing"
    return None


def is_translation_current(row: MemoryContentTranslation | None, *, current_source_text: str) -> bool:
    """Whether ``row`` reflects a successful translation of the *current* source text.

    Staleness is derived from a hash comparison against the live source
    text rather than trusted solely from the stored status, so a source
    edit that bypassed the translation service (or a status left over from
    a previous version) is still correctly detected as stale.
    """
    if row is None:
        return False
    if row.translation_status not in {"translated", "human_reviewed"}:
        return False
    return row.source_hash == compute_source_hash(current_source_text)
