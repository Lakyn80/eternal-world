"""Central language capability registry (Task 65.13.1).

Product code must import capability sets from here instead of maintaining
ad-hoc allowlists (persona-only ``de``, scattered cs/en/ru tuples, etc.).
"""

from __future__ import annotations

from app.modules.language_registry.registry import (
    CANONICAL_LANGUAGE_SOURCES,
    CanonicalLanguageSource,
    LanguageCapabilities,
    LanguageCode,
    APPLICATION_FALLBACK_CANONICAL_LANGUAGE,
    DEFAULT_UI_LANGUAGE,
    assert_canonical_memorial_language,
    assert_ui_language,
    canonical_memorial_languages,
    chat_input_languages,
    default_supported_chat_languages,
    get_language,
    is_canonical_memorial_language,
    is_chat_input_language,
    is_translation_language,
    is_ui_language,
    normalize_language_code,
    translation_languages,
    ui_languages,
)

__all__ = [
    "APPLICATION_FALLBACK_CANONICAL_LANGUAGE",
    "CANONICAL_LANGUAGE_SOURCES",
    "CanonicalLanguageSource",
    "DEFAULT_UI_LANGUAGE",
    "LanguageCapabilities",
    "LanguageCode",
    "assert_canonical_memorial_language",
    "assert_ui_language",
    "canonical_memorial_languages",
    "chat_input_languages",
    "default_supported_chat_languages",
    "get_language",
    "is_canonical_memorial_language",
    "is_chat_input_language",
    "is_translation_language",
    "is_ui_language",
    "normalize_language_code",
    "translation_languages",
    "ui_languages",
]
