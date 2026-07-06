from __future__ import annotations

from pathlib import Path

import pytest

from app.modules.rag_evaluation.fixtures.family_avatar_cases import (
    FAMILY_AVATAR_EVALUATION_CASES,
)
from app.modules.rag_evaluation.fixtures.family_novak import (
    build_corpus_text,
    build_memory_setups,
    build_rag_chunk_setups,
    validate_unique_facts,
)


CORPUS_DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "app"
    / "modules"
    / "rag_evaluation"
    / "fixtures"
    / "data"
    / "family_novak_corpus.cs.txt"
)


def test_family_novak_corpus_meets_minimum_size_and_unique_facts():
    validate_unique_facts(min_word_count=2780)


def test_family_novak_corpus_file_matches_builder_output():
    expected_text = build_corpus_text()
    assert CORPUS_DATA_PATH.exists()
    assert CORPUS_DATA_PATH.read_text(encoding="utf-8") == expected_text


def test_family_avatar_case_count_and_sources():
    assert len(FAMILY_AVATAR_EVALUATION_CASES) >= 25
    assert len(build_memory_setups()) >= 25
    assert len(build_rag_chunk_setups()) >= 10


def test_family_avatar_memory_setups_map_to_known_facts():
    from app.modules.rag_evaluation.fixtures.family_novak_facts import FAMILY_NOVAK_FACTS

    known_fact_ids = {fact.fact_id for fact in FAMILY_NOVAK_FACTS}
    for memory in build_memory_setups():
        fact_id = memory.selection_reason.removeprefix("family_novak:")
        assert fact_id in known_fact_ids
