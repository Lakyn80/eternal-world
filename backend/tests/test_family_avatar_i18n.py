from app.modules.rag_evaluation.brain_eval_runner import resolve_brain_rag_eval_cases
from app.modules.rag_evaluation.fixtures.family_avatar_i18n import (
    FAMILY_AVATAR_I18N_CASES_BY_LOCALE,
    build_family_avatar_cases,
)
from app.modules.rag_evaluation.fixtures.family_novak_facts_ru import FAMILY_NOVAK_FACTS_RU
from app.modules.rag_evaluation.fixtures.family_novak_locale import validate_locale_facts


def test_all_locales_have_57_family_avatar_cases():
    for locale, cases in FAMILY_AVATAR_I18N_CASES_BY_LOCALE.items():
        assert len(cases) == 57, locale


def test_each_locale_case_has_parallel_reference_queries():
    for locale, cases in FAMILY_AVATAR_I18N_CASES_BY_LOCALE.items():
        for case in cases:
            assert case.reference_queries.get(locale) == case.user_query, case.case_id
            assert set(case.reference_queries) >= {"cs", "ru", "en", "es", "fr"}, case.case_id


def test_russian_cases_use_native_russian_evidence_text():
    ru_cases = build_family_avatar_cases("ru")
    sample = next(case for case in ru_cases if case.case_id == "family-popice-childhood")
    evidence_text = sample.memory_evidence_items[0].content_preview or ""
    assert "Попиц" in evidence_text
    assert any(ord(char) > 127 for char in evidence_text)
    assert sample.profile.name == "Ева Новакова"


def test_all_eval_facts_have_translations_for_supported_langs():
    validate_locale_facts("ru")
    validate_locale_facts("en")
    validate_locale_facts("es")
    validate_locale_facts("fr")
    assert len(FAMILY_NOVAK_FACTS_RU) == 124


def test_resolve_brain_rag_eval_cases_supports_multilingual_family_avatar_sets():
    assert len(resolve_brain_rag_eval_cases("family_avatar_ru")) == 57
    assert len(resolve_brain_rag_eval_cases("family_avatar_en")) == 57
    assert len(resolve_brain_rag_eval_cases("family_avatar_es")) == 57
    assert len(resolve_brain_rag_eval_cases("family_avatar_fr")) == 57
    assert len(resolve_brain_rag_eval_cases("family_avatar_cs")) == 57
