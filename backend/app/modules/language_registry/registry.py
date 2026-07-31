"""Typed language capability registry for Eternal World.

Capabilities are independent: a language may be usable for chat input without
having a full UI localization, and must never appear as a silent persona-only
exception.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Literal


LanguageCode = Literal["cs", "en", "ru", "de"]
CanonicalLanguageSource = Literal[
    "existing_profile",
    "avatar_persona",
    "creator_preference",
    "reliable_content_metadata",
    "application_fallback",
    "manual_review_required",
]

CANONICAL_LANGUAGE_SOURCES: Final[frozenset[str]] = frozenset(
    {
        "existing_profile",
        "avatar_persona",
        "creator_preference",
        "reliable_content_metadata",
        "application_fallback",
        "manual_review_required",
    }
)

DEFAULT_UI_LANGUAGE: Final[LanguageCode] = "en"
#: Auditable fallback when no reliable memorial-language evidence exists.
#: Never assign silently — always persist ``canonical_language_source``.
APPLICATION_FALLBACK_CANONICAL_LANGUAGE: Final[LanguageCode] = "cs"


@dataclass(frozen=True, slots=True)
class LanguageCapabilities:
    code: LanguageCode
    #: Full authenticated workspace / marketing UI strings exist.
    ui_localization: bool
    #: Allowed as immutable memorial canonical language.
    canonical_memorial: bool
    #: Allowed as translation source/target in the content-translation layer.
    translation: bool
    #: Allowed as chat user-message / response language.
    chat_input: bool
    #: Display-only aliases (never persisted as canonical codes).
    aliases: tuple[str, ...] = ()


_REGISTRY: Final[dict[str, LanguageCapabilities]] = {
    "cs": LanguageCapabilities(
        code="cs",
        ui_localization=True,
        canonical_memorial=True,
        translation=True,
        chat_input=True,
        aliases=("cs-CZ",),
    ),
    "en": LanguageCapabilities(
        code="en",
        ui_localization=True,
        canonical_memorial=True,
        translation=True,
        chat_input=True,
        aliases=("en-US",),
    ),
    "ru": LanguageCapabilities(
        code="ru",
        ui_localization=True,
        canonical_memorial=True,
        translation=True,
        chat_input=True,
        aliases=("ru-RU",),
    ),
    "de": LanguageCapabilities(
        code="de",
        ui_localization=False,
        canonical_memorial=False,
        translation=True,
        chat_input=True,
        aliases=("de-DE",),
    ),
}

_ALIAS_TO_CODE: Final[dict[str, LanguageCode]] = {
    alias.lower(): caps.code
    for caps in _REGISTRY.values()
    for alias in caps.aliases
}
for _code in _REGISTRY:
    _ALIAS_TO_CODE[_code] = _code  # type: ignore[index]


def get_language(code: str) -> LanguageCapabilities | None:
    normalized = normalize_language_code(code)
    if normalized is None:
        return None
    return _REGISTRY.get(normalized)


def normalize_language_code(value: str | None) -> LanguageCode | None:
    if value is None:
        return None
    raw = value.strip().lower().replace("_", "-")
    if not raw:
        return None
    if raw in _REGISTRY:
        return raw  # type: ignore[return-value]
    if raw in _ALIAS_TO_CODE:
        return _ALIAS_TO_CODE[raw]
    primary = raw.split("-", 1)[0]
    if primary in _REGISTRY:
        return primary  # type: ignore[return-value]
    return None


def ui_languages() -> tuple[LanguageCode, ...]:
    return tuple(c.code for c in _REGISTRY.values() if c.ui_localization)


def canonical_memorial_languages() -> tuple[LanguageCode, ...]:
    return tuple(c.code for c in _REGISTRY.values() if c.canonical_memorial)


def translation_languages() -> tuple[LanguageCode, ...]:
    return tuple(c.code for c in _REGISTRY.values() if c.translation)


def chat_input_languages() -> tuple[LanguageCode, ...]:
    return tuple(c.code for c in _REGISTRY.values() if c.chat_input)


def default_supported_chat_languages(*, primary: LanguageCode) -> list[LanguageCode]:
    """Default persona ``supported_languages`` for a memorial with ``primary``.

    Uses the product UI language set (cs/en/ru) as the default chat set.
    Additional chat-input languages such as ``de`` remain selectable via
    detection without forcing them into every new persona row.
    """

    ordered: list[LanguageCode] = [primary]
    for code in ui_languages():
        if code not in ordered and is_chat_input_language(code):
            ordered.append(code)
    return ordered


def is_ui_language(code: str | None) -> bool:
    caps = get_language(code) if code else None
    return caps is not None and caps.ui_localization


def is_canonical_memorial_language(code: str | None) -> bool:
    caps = get_language(code) if code else None
    return caps is not None and caps.canonical_memorial


def is_translation_language(code: str | None) -> bool:
    caps = get_language(code) if code else None
    return caps is not None and caps.translation


def is_chat_input_language(code: str | None) -> bool:
    caps = get_language(code) if code else None
    return caps is not None and caps.chat_input


def assert_ui_language(code: str) -> LanguageCode:
    normalized = normalize_language_code(code)
    if normalized is None or not is_ui_language(normalized):
        raise ValueError("unsupported UI language")
    return normalized


def assert_canonical_memorial_language(code: str) -> LanguageCode:
    normalized = normalize_language_code(code)
    if normalized is None or not is_canonical_memorial_language(normalized):
        raise ValueError("unsupported canonical memorial language")
    return normalized


def assert_translation_language(code: str) -> LanguageCode:
    normalized = normalize_language_code(code)
    if normalized is None or not is_translation_language(normalized):
        raise ValueError("unsupported translation language")
    return normalized
