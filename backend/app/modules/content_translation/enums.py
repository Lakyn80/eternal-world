from __future__ import annotations

from enum import Enum


class SupportedContentLanguage(str, Enum):
    """Languages the content-translation layer supports.

    Capability source of truth is ``language_registry.translation_languages``.
    Keep this enum aligned with that registry (and DB check constraints).
    """

    CS = "cs"
    RU = "ru"
    EN = "en"
    DE = "de"


class TranslationStatus(str, Enum):
    PENDING = "pending"
    TRANSLATED = "translated"
    FAILED = "failed"
    STALE = "stale"
    HUMAN_REVIEWED = "human_reviewed"


#: Statuses under which a translation may be treated as currently usable
#: (eligible for promotion/indexing eligibility checks and for display as
#: the "current" translation in bilingual review UIs).
CURRENT_USABLE_TRANSLATION_STATUSES = frozenset(
    {TranslationStatus.TRANSLATED.value, TranslationStatus.HUMAN_REVIEWED.value}
)


class TranslatableEntityType(str, Enum):
    """What kind of row/field a ``MemoryContentTranslation`` row describes.

    Kept narrow and explicit (no generic polymorphic association) so every
    entity type has an unambiguous, documented meaning instead of an opaque
    string. ``entity_id`` is stored as a string because the underlying
    identifiers are heterogeneous (integer PKs for candidates/contributions,
    a ``trace_id`` string for ephemeral chat turns).
    """

    MEMORY_CANDIDATE = "memory_candidate"
    FAMILY_MEMORY_CONTRIBUTION = "family_memory_contribution"
    CLARIFICATION_QUESTION = "clarification_question"
    FA_CHAT_TURN = "fa_chat_turn"
    MEMORIAL_CONTRIBUTION = "memorial_contribution"
    BIOGRAPHER_QUESTION = "biographer_question"
    BIOGRAPHER_ANSWER = "biographer_answer"
    CHAT_MESSAGE = "chat_message"


class ContentTranslationProviderName(str, Enum):
    MOCK = "mock"
    OPENAI_COMPATIBLE = "openai_compatible"
