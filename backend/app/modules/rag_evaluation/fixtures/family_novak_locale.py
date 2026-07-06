from __future__ import annotations

from datetime import date
from typing import Literal

from app.modules.rag_evaluation.fixtures.family_novak import (
    _MEMORY_SOURCE_ID_START,
    _RAG_CHUNK_ID_START,
    _RAG_EMBEDDING_ID_START,
    _RAG_SOURCE_ID_START,
    get_fact_by_id,
)
from app.modules.rag_evaluation.fixtures.family_novak_facts import FAMILY_NOVAK_FACTS
from app.modules.rag_evaluation.fixtures.family_novak_facts_ru import FAMILY_NOVAK_FACTS_RU
from app.modules.rag_evaluation.fixtures.family_novak_ru import (
    EVA_NOVAK_PROFILE_RU,
    get_memory_setup_by_fact_id_ru,
    get_rag_setup_by_fact_id_ru,
    validate_unique_facts_ru,
)
from app.modules.rag_evaluation.fixtures.family_novak_translations import (
    FACT_TRANSLATIONS,
    PROFILE_TRANSLATIONS,
    TRANSLATION_LANGS,
    get_fact_text,
    get_memory_title,
)
from app.modules.rag_evaluation.schemas import (
    RagEvaluationMemoryEvidenceSetup,
    RagEvaluationProfileSetup,
    RagEvaluationRetrievedEvidenceSetup,
)

FamilyAvatarLocale = Literal["cs", "ru", "en", "es", "fr"]

SUPPORTED_FAMILY_AVATAR_LOCALES: tuple[FamilyAvatarLocale, ...] = ("cs", "ru", "en", "es", "fr")

_PROFILE_NAME_BY_LOCALE: dict[FamilyAvatarLocale, str] = {
    "cs": "Eva Nováková",
    "ru": "Ева Новакова",
    "en": "Eva Nováková",
    "es": "Eva Nováková",
    "fr": "Eva Nováková",
}

_CS_PROFILE = RagEvaluationProfileSetup(
    profile_id=100,
    name="Eva Nováková",
    birth_date=date(1948, 4, 22),
    death_date=date(2020, 10, 3),
    biography=(
        "Moravská učitelka literatury, matka Terezy a Martina, babička Kláry. "
        "Většinu života prožila v Brně a v Řečkovicích."
    ),
    personality="Teplá, trpělivá, věcná; mluví klidně a s respektem k faktům.",
    catchphrases="Kniha je spolehlivější společník.; Pojďme si to říct po pravdě.; To si nechám projít hlavou.",
)


def _memory_facts_cs() -> tuple:
    return tuple(fact for fact in FAMILY_NOVAK_FACTS if fact.source_type == "memory")


def _rag_facts_cs() -> tuple:
    return tuple(fact for fact in FAMILY_NOVAK_FACTS if fact.source_type == "rag")


def get_profile(locale: FamilyAvatarLocale) -> RagEvaluationProfileSetup:
    if locale == "cs":
        return _CS_PROFILE.model_copy(deep=True)
    if locale == "ru":
        return EVA_NOVAK_PROFILE_RU.model_copy(deep=True)

    profile_fields = PROFILE_TRANSLATIONS[locale]
    return RagEvaluationProfileSetup(
        profile_id=100,
        name=_PROFILE_NAME_BY_LOCALE[locale],
        birth_date=date(1948, 4, 22),
        death_date=date(2020, 10, 3),
        biography=profile_fields["biography"],
        personality=profile_fields["personality"],
        catchphrases=profile_fields["catchphrases"],
    )


def get_memory_setup_by_fact_id(
    fact_id: str,
    locale: FamilyAvatarLocale,
) -> RagEvaluationMemoryEvidenceSetup:
    if locale == "ru":
        return get_memory_setup_by_fact_id_ru(fact_id)

    memory_facts = _memory_facts_cs()
    for index, fact in enumerate(memory_facts):
        if fact.fact_id != fact_id:
            continue

        title = get_memory_title(fact_id, locale) or fact.memory_title or fact_id
        return RagEvaluationMemoryEvidenceSetup(
            source_id=_MEMORY_SOURCE_ID_START + index,
            title=title,
            content_preview=get_fact_text(fact_id, locale),
            memory_type="text",
            selection_reason=f"family_novak:{fact_id}",
            occurred_year=fact.occurred_year,
        )

    raise KeyError(f"Memory fact not found: {fact_id}")


def get_rag_setup_by_fact_id(
    fact_id: str,
    locale: FamilyAvatarLocale,
) -> RagEvaluationRetrievedEvidenceSetup:
    if locale == "ru":
        return get_rag_setup_by_fact_id_ru(fact_id)

    rag_facts = _rag_facts_cs()
    for index, fact in enumerate(rag_facts):
        if fact.fact_id != fact_id:
            continue

        return RagEvaluationRetrievedEvidenceSetup(
            chunk_id=_RAG_CHUNK_ID_START + index,
            source_id=_RAG_SOURCE_ID_START + index,
            embedding_id=_RAG_EMBEDDING_ID_START + index,
            text_hash=f"family-novak-{fact.fact_id}",
            content_preview=get_fact_text(fact_id, locale),
            source_document_type="biography",
            validation_status="valid",
            language=locale,
        )

    raise KeyError(f"RAG fact not found: {fact_id}")


def validate_locale_facts(locale: FamilyAvatarLocale) -> None:
    if locale == "cs":
        return

    if locale == "ru":
        validate_unique_facts_ru()
        if len(FAMILY_NOVAK_FACTS_RU) != 124:
            raise ValueError("Russian fact manifest must contain 124 facts")
        profile = get_profile("ru")
        if not profile.biography or not profile.personality or not profile.catchphrases:
            raise ValueError("Incomplete native Russian profile")
        return

    if locale not in TRANSLATION_LANGS:
        raise ValueError(f"Unsupported locale: {locale}")

    for fact_id in FACT_TRANSLATIONS:
        get_fact_by_id(fact_id)
        get_fact_text(fact_id, locale)
        fact = get_fact_by_id(fact_id)
        if fact.memory_title is not None:
            title = get_memory_title(fact_id, locale)
            if not title:
                raise ValueError(f"Missing memory title translation for {fact_id} ({locale})")

    profile = get_profile(locale)
    if not profile.biography or not profile.personality or not profile.catchphrases:
        raise ValueError(f"Incomplete profile translation for locale {locale}")
