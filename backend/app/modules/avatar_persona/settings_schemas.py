"""Task 65.12 - persisted memorial avatar persona settings (canonical).

Distinct from the demo-only ``AvatarPersonaProfile`` / Eva fixture. This is
the profile-scoped source of truth for chat, voice adapters, and future
face/video channels.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator, model_validator


VoiceMode = Literal["original_recording", "warm_older", "younger_self"]
VoiceStyle = Literal["warm", "calm", "older", "energetic"]
PersonalityTrait = Literal["gentle", "funny", "thoughtful"]
PersonaLanguage = Literal["cs", "en", "de"]

ALLOWED_VOICE_MODES: frozenset[str] = frozenset(
    {"original_recording", "warm_older", "younger_self"}
)
ALLOWED_VOICE_STYLES: frozenset[str] = frozenset({"warm", "calm", "older", "energetic"})
ALLOWED_PERSONALITY_TRAITS: frozenset[str] = frozenset({"gentle", "funny", "thoughtful"})
ALLOWED_PERSONA_LANGUAGES: frozenset[str] = frozenset({"cs", "en", "de"})

MAX_PERSONALITY_TRAITS = 8
MAX_SUPPORTED_LANGUAGES = 8
MAX_COMMUNICATION_PROFILE_LENGTH = 4000
DEFAULT_PRIMARY_LANGUAGE: PersonaLanguage = "cs"
DEFAULT_VOICE_MODE: VoiceMode = "warm_older"
DEFAULT_VOICE_STYLE: VoiceStyle = "warm"


class AvatarPersonaSettingsRead(BaseModel):
    profile_id: int
    voice_mode: VoiceMode
    voice_style: VoiceStyle
    personality_traits: list[PersonalityTrait]
    primary_language: PersonaLanguage
    supported_languages: list[PersonaLanguage]
    remembered_age: int | None
    communication_profile: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    #: Honest provider capability flags for the current deployment (no TTS yet).
    original_recording_available: bool = False
    voice_provider_supports_style: bool = False
    voice_provider_supports_age: bool = False


class AvatarPersonaSettingsUpdate(BaseModel):
    """Partial update — only explicitly provided fields are applied."""

    voice_mode: VoiceMode | None = None
    voice_style: VoiceStyle | None = None
    personality_traits: list[PersonalityTrait] | None = None
    primary_language: PersonaLanguage | None = None
    supported_languages: list[PersonaLanguage] | None = None
    remembered_age: int | None = Field(default=None)
    #: Sentinel: if the key is present (including null/empty), apply it.
    communication_profile: str | None = None

    model_config = {"extra": "forbid"}

    @field_validator("remembered_age")
    @classmethod
    def _validate_age(cls, value: int | None) -> int | None:
        if value is None:
            return None
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError("remembered_age must be an integer or null")
        if value < 1 or value > 120:
            raise ValueError("remembered_age must be between 1 and 120")
        return value

    @field_validator("personality_traits")
    @classmethod
    def _validate_traits(cls, value: list[PersonalityTrait] | None) -> list[PersonalityTrait] | None:
        if value is None:
            return None
        if len(value) > MAX_PERSONALITY_TRAITS:
            raise ValueError(f"personality_traits may contain at most {MAX_PERSONALITY_TRAITS} items")
        seen: set[str] = set()
        normalized: list[PersonalityTrait] = []
        for trait in value:
            if trait not in ALLOWED_PERSONALITY_TRAITS:
                raise ValueError("unknown personality trait")
            if trait in seen:
                continue
            seen.add(trait)
            normalized.append(trait)
        return normalized

    @field_validator("supported_languages")
    @classmethod
    def _validate_languages(
        cls, value: list[PersonaLanguage] | None
    ) -> list[PersonaLanguage] | None:
        if value is None:
            return None
        if len(value) == 0:
            raise ValueError("supported_languages must not be empty")
        if len(value) > MAX_SUPPORTED_LANGUAGES:
            raise ValueError(f"supported_languages may contain at most {MAX_SUPPORTED_LANGUAGES} items")
        seen: set[str] = set()
        normalized: list[PersonaLanguage] = []
        for code in value:
            if code not in ALLOWED_PERSONA_LANGUAGES:
                raise ValueError("unknown language code")
            if code in seen:
                continue
            seen.add(code)
            normalized.append(code)
        return normalized

    @field_validator("communication_profile")
    @classmethod
    def _validate_communication_profile(cls, value: str | None) -> str | None:
        if value is None:
            return None
        if len(value) > MAX_COMMUNICATION_PROFILE_LENGTH:
            raise ValueError(
                f"communication_profile must be at most {MAX_COMMUNICATION_PROFILE_LENGTH} characters"
            )
        return value

    @model_validator(mode="after")
    def _primary_in_supported(self) -> AvatarPersonaSettingsUpdate:
        if self.supported_languages is not None and self.primary_language is not None:
            if self.primary_language not in self.supported_languages:
                raise ValueError("primary_language must be included in supported_languages")
        return self


class ResolvedAvatarPersona(BaseModel):
    """Typed persona object resolved once per request and reused by adapters."""

    profile_id: int
    voice_mode: VoiceMode
    voice_style: VoiceStyle
    personality_traits: list[PersonalityTrait]
    primary_language: PersonaLanguage
    supported_languages: list[PersonaLanguage]
    remembered_age: int | None
    communication_profile: str
    configured: bool


class VoicePersonaAdapterResult(BaseModel):
    """Honest mapping of canonical persona → current voice provider capabilities."""

    profile_id: int
    voice_mode: VoiceMode
    voice_style: VoiceStyle
    remembered_age: int | None
    personality_traits: list[PersonalityTrait]
    primary_language: PersonaLanguage
    supported_languages: list[PersonaLanguage]
    supported_fields: list[str]
    approximated_fields: list[str]
    unsupported_fields: list[str]
    #: Never includes communication_profile text — only whether a private
    #: description exists (for operator diagnostics).
    has_communication_profile: bool
