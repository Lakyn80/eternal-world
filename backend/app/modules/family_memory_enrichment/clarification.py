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
