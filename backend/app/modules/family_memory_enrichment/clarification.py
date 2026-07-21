from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass

from app.modules.family_memory_enrichment.enums import MemoryType


BEDTIME_SONG_PATTERN = re.compile(
    r"(?=.*\bмне\b)(?=.*(?:пел[аи]?|напевал[аи]?|спел[аи]?))"
    r"(?=.*(?:песн\w*|колыбельн\w*))(?=.*(?:перед\s+сном|на\s+ночь))",
    re.IGNORECASE,
)
QUOTED_TEXT_PATTERN = re.compile(r"[«\"]([^»\"]{1,300})[»\"]")


@dataclass(frozen=True)
class ClarificationSpec:
    key: str
    question_text: str
    required: bool


BEDTIME_SONG_QUESTIONS = (
    ClarificationSpec("song_title", "А ты помнишь, какую песню я тебе пела?", True),
    ClarificationSpec("place", "Где это обычно происходило?", True),
    ClarificationSpec(
        "approximate_period",
        "Когда это было — примерно в каком возрасте, году или периоде?",
        True,
    ),
)

#: AI Biographer "childhood" topic clarification bank (Task 65.2). Reuses the
#: same generic "place"/"approximate_period" keys as `BEDTIME_SONG_QUESTIONS`
#: (both already handled generically by `extract_answer_details`'s bottom-of-
#: function natural-language fallback, and both already have generic-enough
#: Czech localizations below) rather than inventing a second key namespace.
CHILDHOOD_MEMORY_QUESTIONS = (
    ClarificationSpec("place", "Где именно это происходило?", True),
    ClarificationSpec(
        "approximate_period",
        "Когда это было — примерно в каком возрасте, году или периоде?",
        True,
    ),
)

#: Static Czech localization for the fixed clarification question templates
#: above (Task 64.5.1, Part E.17). These are deterministic UI-adjacent
#: templates, not dynamic user content, so they are localized directly
#: rather than through the content_translation backend service. The
#: canonical persisted ``question_text`` column remains Russian for
#: backward compatibility; ``localize_question_text`` produces a
#: display-only Czech projection for the Czech chat/review UI while both
#: locales continue to refer to the exact same clarification record
#: (same ``question_key``, same row, same required/status fields).
BEDTIME_SONG_QUESTIONS_TEXT_CS = {
    "song_title": "A pamatuješ si, jakou písničku jsem ti zpívala?",
    "place": "Kde se to obvykle odehrávalo?",
    "approximate_period": "Kdy to bylo — přibližně v jakém věku, roce nebo období?",
}


def localize_question_text(*, question_key: str, source_text: str, locale: str) -> str:
    """Return a Czech display projection of a clarification question, or the
    original (Russian) source text for any other locale/unknown key."""
    if locale != "cs":
        return source_text
    return BEDTIME_SONG_QUESTIONS_TEXT_CS.get(question_key, source_text)


def normalize_text(value: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", value).split()).strip()


def classify_memory_type(text: str) -> MemoryType:
    return (
        MemoryType.BEDTIME_SONG
        if BEDTIME_SONG_PATTERN.search(normalize_text(text))
        else MemoryType.GENERAL
    )


def initial_structured_details(text: str) -> dict[str, str]:
    return {"what_happened": normalize_text(text)}


def collect_detail_values(contributions: list) -> dict[str, list[tuple[str, str, str]]]:
    values: dict[str, list[tuple[str, str, str]]] = {}
    for contribution in contributions:
        details = contribution.structured_details or {}
        if not isinstance(details, dict):
            continue
        for key, raw_value in details.items():
            if not isinstance(raw_value, str):
                continue
            value = normalize_text(raw_value)
            if not value:
                continue
            entry = (
                contribution.relationship_to_owner or "",
                contribution.actor_role,
                value,
            )
            bucket = values.setdefault(key, [])
            if entry not in bucket:
                bucket.append(entry)
    return values


def latest_details(contributions: list) -> dict[str, str]:
    resolved: dict[str, str] = {}
    for contribution in contributions:
        details = contribution.structured_details or {}
        if not isinstance(details, dict):
            continue
        for key, raw_value in details.items():
            if isinstance(raw_value, str) and normalize_text(raw_value):
                resolved[key] = normalize_text(raw_value)
    return resolved


def required_question_specs(memory_type: str) -> tuple[ClarificationSpec, ...]:
    if memory_type == MemoryType.BEDTIME_SONG.value:
        return BEDTIME_SONG_QUESTIONS
    if memory_type == MemoryType.CHILDHOOD_MEMORY.value:
        return CHILDHOOD_MEMORY_QUESTIONS
    return ()


def missing_required_keys(*, memory_type: str, contributions: list) -> list[str]:
    details = latest_details(contributions)
    return [
        spec.key
        for spec in required_question_specs(memory_type)
        if spec.required and not details.get(spec.key)
    ]


def next_question_spec(*, memory_type: str, contributions: list) -> ClarificationSpec | None:
    missing = set(missing_required_keys(memory_type=memory_type, contributions=contributions))
    for spec in required_question_specs(memory_type):
        if spec.key in missing:
            return spec
    return None


def extract_answer_details(*, question_key: str, answer_text: str) -> dict[str, str]:
    normalized = normalize_text(answer_text)
    lowered = normalized.casefold().replace("ё", "е")
    details: dict[str, str] = {}
    if question_key == "song_title":
        quoted = QUOTED_TEXT_PATTERN.search(normalized)
        details["song_title"] = normalize_text(quoted.group(1) if quoted else normalized)
    elif question_key == "place":
        details["place"] = normalized
    elif question_key == "approximate_period":
        details["approximate_period"] = normalized
    elif question_key.startswith("owner_request_"):
        details["additional_notes"] = normalized

    # A natural context answer often supplies place and period together.
    if any(token in lowered for token in ("деревн", "дома", "квартир", "дач")):
        details.setdefault("place", normalized)
    if any(token in lowered for token in ("летом", "зимой", "осенью", "весной", "каникул", "год", "детств")):
        details.setdefault("approximate_period", normalized)
    if any(token in lowered for token in ("часто", "каждый", "обычно", "однажды", "иногда")):
        details.setdefault("frequency", normalized)
    return details
