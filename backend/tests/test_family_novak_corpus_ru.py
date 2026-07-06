from __future__ import annotations

import re
from pathlib import Path

from app.modules.rag_evaluation.fixtures.family_avatar_i18n import (
    FAMILY_AVATAR_RU_EVALUATION_CASES,
)
from app.modules.rag_evaluation.fixtures.family_novak_facts_ru import FAMILY_NOVAK_FACTS_RU
from app.modules.rag_evaluation.fixtures.family_novak_ru import (
    build_corpus_text_ru,
    validate_unique_facts_ru,
)

CORPUS_DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "app"
    / "modules"
    / "rag_evaluation"
    / "fixtures"
    / "data"
    / "family_novak_corpus.ru.txt"
)

_CYRILLIC_PATTERN = re.compile(r"[\u0400-\u04FF]")
_LATIN_PATTERN = re.compile(r"[A-Za-z]")


def test_family_novak_ru_corpus_meets_minimum_size_and_unique_facts():
    validate_unique_facts_ru(min_word_count=2780)


def test_family_novak_ru_corpus_file_matches_builder_output():
    expected_text = build_corpus_text_ru()
    assert CORPUS_DATA_PATH.exists()
    assert CORPUS_DATA_PATH.read_text(encoding="utf-8") == expected_text


def test_family_novak_ru_facts_are_primarily_cyrillic():
    cyrillic_facts = sum(1 for fact in FAMILY_NOVAK_FACTS_RU if _CYRILLIC_PATTERN.search(fact.text))
    assert cyrillic_facts == len(FAMILY_NOVAK_FACTS_RU)


def test_family_avatar_ru_cases_use_cyrillic_evidence_and_queries():
    for case in FAMILY_AVATAR_RU_EVALUATION_CASES:
        assert _CYRILLIC_PATTERN.search(case.user_query), case.case_id
        for marker in case.expected_evidence_markers:
            if marker:
                assert _CYRILLIC_PATTERN.search(marker) or marker.isdigit(), case.case_id
        for item in case.memory_evidence_items:
            assert _CYRILLIC_PATTERN.search(item.content_preview or ""), case.case_id
        for item in case.retrieved_evidence_items:
            assert item.language == "ru"
            assert _CYRILLIC_PATTERN.search(item.content_preview), case.case_id
