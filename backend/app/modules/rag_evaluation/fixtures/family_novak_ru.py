from __future__ import annotations

import re
from datetime import date

from app.modules.rag_evaluation.fixtures.family_novak import (
    _MEMORY_SOURCE_ID_START,
    _RAG_CHUNK_ID_START,
    _RAG_EMBEDDING_ID_START,
    _RAG_SOURCE_ID_START,
)
from app.modules.rag_evaluation.fixtures.family_novak_facts import FamilyNovakFact, SECTION_ORDER
from app.modules.rag_evaluation.fixtures.family_novak_facts_ru import (
    FAMILY_NOVAK_FACTS_RU,
    SECTION_NARRATIVES_RU,
    SECTION_TITLES_RU,
)
from app.modules.rag_evaluation.schemas import (
    RagEvaluationMemoryEvidenceSetup,
    RagEvaluationProfileSetup,
    RagEvaluationRetrievedEvidenceSetup,
)

EVA_NOVAK_PROFILE_RU = RagEvaluationProfileSetup(
    profile_id=100,
    name="Ева Новакова",
    birth_date=date(1948, 4, 22),
    death_date=date(2020, 10, 3),
    biography=(
        "Моравская учительница литературы, мать Терезы и Мартина, бабушка Клары. "
        "Большую часть жизни прожила в Брно и в Ржечковице."
    ),
    personality="Тёплая, терпеливая, деловая; говорит спокойно и с уважением к фактам.",
    catchphrases=(
        "Книга — надёжнее спутник, чем большинство людей.; "
        "Давайте скажем друг другу правду.; "
        "Мне нужно это обдумать."
    ),
)

_WORD_PATTERN = re.compile(r"\w+", re.UNICODE)


def _normalize_for_overlap(value: str) -> str:
    return " ".join(_WORD_PATTERN.findall(value.lower()))


def _word_count(value: str) -> int:
    return len(_WORD_PATTERN.findall(value))


def build_corpus_text_ru() -> str:
    sections: list[str] = []
    for section_key in SECTION_ORDER:
        section_facts = [fact for fact in FAMILY_NOVAK_FACTS_RU if fact.section == section_key]
        if not section_facts:
            continue

        title = SECTION_TITLES_RU.get(section_key, section_key)
        section_parts = [SECTION_NARRATIVES_RU[section_key], *[fact.text for fact in section_facts]]
        sections.append(f"## {title}\n\n" + "\n\n".join(section_parts))

    return "\n\n".join(sections)


def validate_unique_facts_ru(*, min_word_count: int = 2780) -> None:
    fact_texts = [fact.text for fact in FAMILY_NOVAK_FACTS_RU]
    normalized_facts = [_normalize_for_overlap(text) for text in fact_texts]

    if len(set(normalized_facts)) != len(normalized_facts):
        raise ValueError("Duplicate normalized fact text detected in Russian family Novak corpus")

    for left_index, left_text in enumerate(normalized_facts):
        left_tokens = set(left_text.split())
        for right_index in range(left_index + 1, len(normalized_facts)):
            right_tokens = set(normalized_facts[right_index].split())
            overlap = left_tokens & right_tokens
            if len(overlap) >= 8:
                raise ValueError(
                    "Facts share too many tokens: "
                    f"{FAMILY_NOVAK_FACTS_RU[left_index].fact_id} vs "
                    f"{FAMILY_NOVAK_FACTS_RU[right_index].fact_id}"
                )

    narrative_texts = [SECTION_NARRATIVES_RU[section_key] for section_key in SECTION_ORDER]
    normalized_narratives = [_normalize_for_overlap(text) for text in narrative_texts]
    if len(set(normalized_narratives)) != len(normalized_narratives):
        raise ValueError("Duplicate section narratives detected in Russian family Novak corpus")

    total_words = _word_count(build_corpus_text_ru())
    if total_words < min_word_count:
        raise ValueError(
            f"Russian family Novak corpus is below minimum word count ({total_words} < {min_word_count})"
        )


def _memory_facts_ru() -> tuple[FamilyNovakFact, ...]:
    return tuple(fact for fact in FAMILY_NOVAK_FACTS_RU if fact.source_type == "memory")


def _rag_facts_ru() -> tuple[FamilyNovakFact, ...]:
    return tuple(fact for fact in FAMILY_NOVAK_FACTS_RU if fact.source_type == "rag")


def build_memory_setups_ru() -> tuple[RagEvaluationMemoryEvidenceSetup, ...]:
    memory_facts = _memory_facts_ru()
    setups: list[RagEvaluationMemoryEvidenceSetup] = []
    for index, fact in enumerate(memory_facts):
        setups.append(
            RagEvaluationMemoryEvidenceSetup(
                source_id=_MEMORY_SOURCE_ID_START + index,
                title=fact.memory_title or fact.fact_id,
                content_preview=fact.text,
                memory_type="text",
                selection_reason=f"family_novak:{fact.fact_id}",
                occurred_year=fact.occurred_year,
            )
        )
    return tuple(setups)


def build_rag_chunk_setups_ru() -> tuple[RagEvaluationRetrievedEvidenceSetup, ...]:
    rag_facts = _rag_facts_ru()
    setups: list[RagEvaluationRetrievedEvidenceSetup] = []
    for index, fact in enumerate(rag_facts):
        setups.append(
            RagEvaluationRetrievedEvidenceSetup(
                chunk_id=_RAG_CHUNK_ID_START + index,
                source_id=_RAG_SOURCE_ID_START + index,
                embedding_id=_RAG_EMBEDDING_ID_START + index,
                text_hash=f"family-novak-ru-{fact.fact_id}",
                content_preview=fact.text,
                source_document_type="biography",
                validation_status="valid",
                language="ru",
            )
        )
    return tuple(setups)


def get_memory_setup_by_fact_id_ru(fact_id: str) -> RagEvaluationMemoryEvidenceSetup:
    for setup in build_memory_setups_ru():
        if setup.selection_reason == f"family_novak:{fact_id}":
            return setup
    raise KeyError(f"Memory fact not found: {fact_id}")


def get_rag_setup_by_fact_id_ru(fact_id: str) -> RagEvaluationRetrievedEvidenceSetup:
    rag_facts = _rag_facts_ru()
    for index, fact in enumerate(rag_facts):
        if fact.fact_id == fact_id:
            return build_rag_chunk_setups_ru()[index]
    raise KeyError(f"RAG fact not found: {fact_id}")


def get_fact_by_id_ru(fact_id: str) -> FamilyNovakFact:
    for fact in FAMILY_NOVAK_FACTS_RU:
        if fact.fact_id == fact_id:
            return fact
    raise KeyError(f"Fact not found: {fact_id}")
