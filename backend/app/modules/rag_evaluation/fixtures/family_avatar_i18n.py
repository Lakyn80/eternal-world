from __future__ import annotations

import re

from app.modules.rag_evaluation.fixtures.family_avatar_i18n_specs import (
    FAMILY_AVATAR_I18N_SPECS,
    FamilyAvatarCaseSpec,
    SPEC_LOCALES,
)
from app.modules.rag_evaluation.fixtures.family_novak_locale import (
    FamilyAvatarLocale,
    SUPPORTED_FAMILY_AVATAR_LOCALES,
    get_memory_setup_by_fact_id,
    get_profile,
    get_rag_setup_by_fact_id,
    validate_locale_facts,
)
from app.modules.rag_evaluation.schemas import RagEvaluationCase

_CYRILLIC_PATTERN = re.compile(r"[\u0400-\u04FF]")

_LATIN_TO_CYRILLIC_MARKER_MAP: dict[str, str] = {
    "Popice": "Попиц",
    "Mikulov": "Микулов",
    "Brno": "Брно",
    "Brn": "Брн",
    "Lidick": "Лидиц",
    "Líšeň": "Лишн",
    "Líšn": "Лишн",
    "Lisen": "Лишн",
    "Pálava": "Палав",
    "Pálav": "Палав",
    "Pavlov": "Павлов",
    "Pavlem": "Павлом",
    "Pavel": "Павел",
    "Pavla": "Павла",
    "Václav": "Вацлав",
    "Vaclav": "Вацлав",
    "svatého": "святого",
    "Tereza": "Тереза",
    "Terez": "Терез",
    "Martin": "Мартин",
    "Klára": "Клара",
    "Klár": "Клар",
    "Eva": "Ева",
    "Petr": "Петр",
    "Jan": "Ян",
    "František": "Франтишек",
    "Ludm": "Людм",
    "Horákov": "Гораков",
    "Horakov": "Гораков",
    "Novotn": "Новотн",
    "Řečkovice": "Ржечковиц",
    "Řečkovic": "Ржечковиц",
    "Bohunice": "Богуниц",
    "Bohunic": "Богуниц",
    "Kuřim": "Куржим",
    "Dívčí": "Дивч",
    "Dívč": "Дивч",
    "Vídeň": "Вен",
    "Viden": "Вен",
    "Vienna": "Вене",
    "Praze": "Праге",
    "Prague": "Праге",
    "Paris": "Париж",
    "Balaton": "Балатон",
    "Vietnam": "Вьетнам",
    "Italy": "Итали",
    "Azor": "Азор",
    "literatur": "литерат",
    "kytar": "гитар",
    "knih": "книг",
    "book": "книг",
    "books": "книг",
    "sadem": "сад",
    "meruňky": "абрик",
    "šál": "шал",
    "třeš": "вишн",
    "zdravotn": "медсест",
    "flét": "флейт",
    "Nesem": "Несем",
    "noviny": "новин",
    "Mách": "Мах",
    "jezer": "озер",
    "únava": "устал",
    "Uhersk": "Угерск",
    "Pod hvězdami": "Под звёздами",
}


def _resolve_ru_text(value: str) -> str:
    if not value or value.isdigit() or _CYRILLIC_PATTERN.search(value):
        if not value or value.isdigit():
            return value
        resolved = value
        for latin in sorted(_LATIN_TO_CYRILLIC_MARKER_MAP, key=len, reverse=True):
            if latin in resolved:
                resolved = resolved.replace(latin, _LATIN_TO_CYRILLIC_MARKER_MAP[latin])
        return resolved

    if value in _LATIN_TO_CYRILLIC_MARKER_MAP:
        return _LATIN_TO_CYRILLIC_MARKER_MAP[value]

    resolved = value
    for latin in sorted(_LATIN_TO_CYRILLIC_MARKER_MAP, key=len, reverse=True):
        if latin in resolved:
            resolved = resolved.replace(latin, _LATIN_TO_CYRILLIC_MARKER_MAP[latin])
    return resolved


def _resolve_expected_markers(spec: FamilyAvatarCaseSpec, locale: FamilyAvatarLocale) -> list[str]:
    markers = list(spec.markers[locale])
    if locale != "ru":
        return markers
    return [_resolve_ru_text(marker) for marker in markers]


def _resolve_forbidden_claims(spec: FamilyAvatarCaseSpec, locale: FamilyAvatarLocale) -> list[str]:
    forbidden = list(spec.forbidden.get(locale, []))
    if locale != "ru":
        return forbidden
    return [_resolve_ru_text(claim) for claim in forbidden]


def _build_case_from_spec(
    spec: FamilyAvatarCaseSpec,
    locale: FamilyAvatarLocale,
) -> RagEvaluationCase:
    profile = get_profile(locale)
    user_query = spec.queries[locale]
    reference_queries = dict(spec.queries)
    if locale == "ru":
        user_query = _resolve_ru_text(user_query)
        reference_queries["ru"] = user_query
    expected_markers = _resolve_expected_markers(spec, locale)
    forbidden_claims = _resolve_forbidden_claims(spec, locale)

    if spec.kind == "memory":
        assert spec.fact_id is not None
        return RagEvaluationCase(
            case_id=spec.case_id,
            title=spec.title,
            profile=profile,
            memory_evidence_items=[get_memory_setup_by_fact_id(spec.fact_id, locale)],
            user_query=user_query,
            reference_queries=reference_queries,
            expected_behavior="grounded_answer",
            expected_evidence_markers=expected_markers,
            forbidden_claims=forbidden_claims,
            minimum_required_evidence_count=1,
        )

    if spec.kind == "rag":
        assert spec.fact_id is not None
        return RagEvaluationCase(
            case_id=spec.case_id,
            title=spec.title,
            profile=profile,
            retrieved_evidence_items=[get_rag_setup_by_fact_id(spec.fact_id, locale)],
            user_query=user_query,
            reference_queries=reference_queries,
            expected_behavior="grounded_answer",
            expected_evidence_markers=expected_markers,
            forbidden_claims=forbidden_claims,
            minimum_required_evidence_count=1,
        )

    if spec.kind == "lack":
        return RagEvaluationCase(
            case_id=spec.case_id,
            title=spec.title,
            profile=profile,
            user_query=user_query,
            reference_queries=reference_queries,
            expected_behavior="lack_of_evidence",
            expected_evidence_markers=expected_markers,
            forbidden_claims=forbidden_claims,
            should_require_lack_of_evidence=True,
        )

    recent_history = []
    if spec.recent_history is not None:
        recent_history = spec.recent_history[locale]

    memory_items = []
    if spec.memory_fact_id is not None:
        memory_items = [get_memory_setup_by_fact_id(spec.memory_fact_id, locale)]

    rag_items = []
    if spec.rag_fact_id is not None:
        rag_items = [get_rag_setup_by_fact_id(spec.rag_fact_id, locale)]

    return RagEvaluationCase(
        case_id=spec.case_id,
        title=spec.title,
        profile=profile,
        recent_history=recent_history,
        memory_evidence_items=memory_items,
        retrieved_evidence_items=rag_items,
        user_query=user_query,
        reference_queries=reference_queries,
        expected_behavior="grounded_answer",
        expected_evidence_markers=expected_markers,
        forbidden_claims=forbidden_claims,
        minimum_required_evidence_count=1,
    )


def build_family_avatar_cases(locale: FamilyAvatarLocale) -> tuple[RagEvaluationCase, ...]:
    if locale not in SUPPORTED_FAMILY_AVATAR_LOCALES:
        raise ValueError(f"Unsupported locale: {locale}")

    validate_locale_facts(locale)

    for spec in FAMILY_AVATAR_I18N_SPECS:
        missing_locales = set(SPEC_LOCALES) - set(spec.queries)
        if missing_locales:
            raise ValueError(f"Spec {spec.case_id} missing queries for: {missing_locales}")
        if locale not in spec.queries:
            raise ValueError(f"Spec {spec.case_id} missing query for locale {locale}")

    return tuple(_build_case_from_spec(spec, locale) for spec in FAMILY_AVATAR_I18N_SPECS)


FAMILY_AVATAR_CS_EVALUATION_CASES = build_family_avatar_cases("cs")
FAMILY_AVATAR_RU_EVALUATION_CASES = build_family_avatar_cases("ru")
FAMILY_AVATAR_EN_EVALUATION_CASES = build_family_avatar_cases("en")
FAMILY_AVATAR_ES_EVALUATION_CASES = build_family_avatar_cases("es")
FAMILY_AVATAR_FR_EVALUATION_CASES = build_family_avatar_cases("fr")

assert len(FAMILY_AVATAR_CS_EVALUATION_CASES) == 57
assert len(FAMILY_AVATAR_RU_EVALUATION_CASES) == 57
assert len(FAMILY_AVATAR_EN_EVALUATION_CASES) == 57
assert len(FAMILY_AVATAR_ES_EVALUATION_CASES) == 57
assert len(FAMILY_AVATAR_FR_EVALUATION_CASES) == 57

FAMILY_AVATAR_I18N_CASES_BY_LOCALE: dict[FamilyAvatarLocale, tuple[RagEvaluationCase, ...]] = {
    "cs": FAMILY_AVATAR_CS_EVALUATION_CASES,
    "ru": FAMILY_AVATAR_RU_EVALUATION_CASES,
    "en": FAMILY_AVATAR_EN_EVALUATION_CASES,
    "es": FAMILY_AVATAR_ES_EVALUATION_CASES,
    "fr": FAMILY_AVATAR_FR_EVALUATION_CASES,
}
