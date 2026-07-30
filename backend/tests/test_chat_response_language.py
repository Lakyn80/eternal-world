"""Tests for chat message language detection and response-language selection."""

from __future__ import annotations

from app.modules.avatar_persona.language_detection import detect_message_language
from app.modules.avatar_persona.settings_schemas import ResolvedAvatarPersona
from app.modules.avatar_persona.settings_service import select_response_language


def test_detect_russian_cyrillic():
    assert detect_message_language("Привет, как дела?") == "ru"


def test_detect_czech_diacritics():
    assert detect_message_language("Ahoj, jak se máš?") == "cs"


def test_detect_english_latin():
    assert detect_message_language("Hello, how are you today?") == "en"


def test_detect_german_umlaut():
    assert detect_message_language("Guten Tag, wie geht es dir? Schön!") == "de"


def test_detect_empty_returns_none():
    assert detect_message_language("   ") is None
    assert detect_message_language("🙂🙂") is None


def _persona(*, supported: list[str], primary: str = "cs") -> ResolvedAvatarPersona:
    return ResolvedAvatarPersona(
        profile_id=1,
        voice_mode="warm_older",
        voice_style="warm",
        personality_traits=[],
        primary_language=primary,  # type: ignore[arg-type]
        supported_languages=supported,  # type: ignore[arg-type]
        remembered_age=None,
        communication_profile="",
        configured=True,
    )


def test_select_prefers_detected_english_over_czech_primary():
    persona = _persona(supported=["cs"], primary="cs")
    assert (
        select_response_language(
            persona,
            detected_language="en",
            fallback_to_primary=False,
        )
        == "en"
    )


def test_select_prefers_detected_russian_over_czech_primary():
    persona = _persona(supported=["cs", "en", "ru"], primary="cs")
    assert (
        select_response_language(
            persona,
            detected_language="ru",
            fallback_to_primary=False,
        )
        == "ru"
    )


def test_select_returns_none_when_undetected_without_primary_fallback():
    persona = _persona(supported=["cs"], primary="cs")
    assert (
        select_response_language(
            persona,
            detected_language=None,
            fallback_to_primary=False,
        )
        is None
    )
