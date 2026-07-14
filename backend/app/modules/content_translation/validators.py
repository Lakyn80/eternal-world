from __future__ import annotations

from app.modules.content_translation.schemas import ProviderTranslationResult


class ContentTranslationValidationError(Exception):
    """Raised when a provider's translation result fails safety validation.

    Never raised for stylistic reasons - only for results that would be
    unsafe to store as a translation (empty, absurdly short/long, or an
    exact untranslated echo when the languages differ).
    """


#: Outside this ratio (translated length / source length) the result is
#: rejected outright rather than silently accepted - a heuristic guard
#: against truncated or run-away generations, not a style check.
_MIN_LENGTH_RATIO = 0.15
_MAX_LENGTH_RATIO = 6.0


def validate_translation_result(
    *,
    source_text: str,
    result: ProviderTranslationResult,
) -> None:
    """Validate a provider translation result before it is persisted.

    Raises :class:`ContentTranslationValidationError` on any unsafe result.
    Does not attempt deep entity-level verification (that would require a
    second model call); this is a fast, deterministic safety net.
    """
    translated_text = (result.translated_text or "").strip()
    if not translated_text:
        raise ContentTranslationValidationError("Translated text must not be empty")

    source_length = len(source_text.strip())
    if source_length == 0:
        raise ContentTranslationValidationError("Source text must not be empty")

    ratio = len(translated_text) / source_length
    if ratio < _MIN_LENGTH_RATIO or ratio > _MAX_LENGTH_RATIO:
        raise ContentTranslationValidationError(
            "Translated text length is implausible relative to the source text"
        )
