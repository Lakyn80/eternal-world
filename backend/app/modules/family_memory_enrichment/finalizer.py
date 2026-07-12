from __future__ import annotations

from dataclasses import dataclass

from app.modules.family_memory_enrichment.clarification import (
    collect_detail_values,
    latest_details,
    normalize_text,
)


@dataclass(frozen=True)
class FinalizedDraft:
    text: str
    has_conflict: bool


def _distinct_values(entries: list[tuple[str, str, str]]) -> list[str]:
    return list(dict.fromkeys(value for _relationship, _actor_role, value in entries))


def build_finalized_draft(*, candidate, contributions: list) -> FinalizedDraft:
    values = collect_detail_values(contributions)
    details = latest_details(contributions)
    conflicting_keys = [key for key, entries in values.items() if len(_distinct_values(entries)) > 1]

    if conflicting_keys:
        statements: list[str] = []
        for key in conflicting_keys:
            for relationship, actor_role, value in values[key]:
                if actor_role == "owner":
                    role_label = "Владелец аватара"
                elif relationship:
                    role_label = relationship[:1].upper() + relationship[1:]
                else:
                    role_label = "Член семьи"
                statements.append(f"{role_label} указывает: {value}.")
        statements.append("Различающиеся семейные точки зрения сохранены; точная деталь остаётся спорной.")
        return FinalizedDraft(text=normalize_text(" ".join(statements))[:500], has_conflict=True)

    if candidate.memory_type == "bedtime_song":
        song_title = details.get("song_title")
        place = details.get("place")
        period = details.get("approximate_period")
        frequency = details.get("frequency")
        if not song_title or not place or not period:
            raise ValueError("Required bedtime-song details are incomplete")
        text = f"По словам члена семьи, бабушка пела ему песню «{song_title}» перед сном."
        text += f" Это происходило {place}; период: {period}."
        if frequency:
            text += f" Частота по воспоминанию участника: {frequency}."
        if details.get("additional_notes"):
            text += f" Дополнительная деталь: {details['additional_notes']}."
        return FinalizedDraft(text=normalize_text(text)[:500], has_conflict=False)

    what_happened = details.get("what_happened") or candidate.proposed_memory_text
    additional_notes = details.get("additional_notes")
    text = f"По словам члена семьи, {what_happened}"
    if additional_notes:
        text += f" Дополнительная деталь: {additional_notes}."
    return FinalizedDraft(
        text=normalize_text(text)[:500],
        has_conflict=False,
    )
