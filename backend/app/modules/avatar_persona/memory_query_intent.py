from __future__ import annotations

from enum import Enum


class MemoryQueryIntent(str, Enum):
    DIRECT_FACTUAL_MEMORY = "direct_factual_memory"
    CORRECTED_MEMORY_FACT = "corrected_memory_fact"
    CORRECTION_HISTORY = "correction_history"
    MULTIPLE_PERSPECTIVE_QUESTION = "multiple_perspective_question"
    UNKNOWN_OR_AMBIGUOUS = "unknown_or_ambiguous"


# Generic linguistic markers that signal the user is asking about an ongoing
# disagreement or "what would you say if we remember it differently" — as
# opposed to a question about a resolved correction. This mirrors the
# disagreement-question detection already used by the Task 64.4.1
# intent-gated evidence filter (app.modules.ai_agents.brain.context); kept
# here too since query-intent classification is a distinct concern (it
# drives retrieval query expansion, not evidence filtering) and this module
# must not depend on the Brain-layer module to avoid a layering inversion.
_PERSPECTIVE_QUESTION_MARKERS = (
    "по-разному",
    "по разному",
    "различ",
    "каждый по-своему",
    "каждый по своему",
    "кто из нас прав",
    "что ты скажешь если",
    "что скажешь если",
)

# Generic markers that signal the user is asking about a past correction —
# i.e. "what is the current, corrected fact" — not any specific memory or
# fact. This must never contain a specific song title, case ID, or dataset
# question so it generalizes to any corrected memory.
_CORRECTION_QUESTION_MARKERS = (
    "исправил",
    "исправила",
    "поправил",
    "поправила",
    "скорректировал",
    "скорректировала",
    "что было на самом деле",
    "что оказалось правильным",
    "какая была правильная версия",
    "какую версию подтвердил",
    "какую версию подтвердила",
)


def _normalize(user_message: str) -> str:
    return " ".join(user_message.casefold().split())


def classify_memory_query_intent(user_message: str) -> MemoryQueryIntent:
    """Deterministically classify what kind of memory question this is.

    Purely marker-based (no LLM call, no external dependency), so it is safe
    to run on every turn and always falls back to DIRECT_FACTUAL_MEMORY when
    nothing matches — an ordinary factual question is retrieved exactly as
    before with no behavior change.
    """
    normalized = _normalize(user_message)
    if not normalized:
        return MemoryQueryIntent.UNKNOWN_OR_AMBIGUOUS
    if any(marker in normalized for marker in _PERSPECTIVE_QUESTION_MARKERS):
        return MemoryQueryIntent.MULTIPLE_PERSPECTIVE_QUESTION
    if any(marker in normalized for marker in _CORRECTION_QUESTION_MARKERS):
        return MemoryQueryIntent.CORRECTED_MEMORY_FACT
    return MemoryQueryIntent.DIRECT_FACTUAL_MEMORY


# Identifies the exact deterministic rule that produced a normalized
# retrieval query, for safe (non-content) trace metadata.
CORRECTED_MEMORY_EXPANSION_RULE_ID = "corrected_memory_intent_expansion_v1"

# Generic, fact-agnostic phrases appended to the retrieval query for
# corrected-memory intent. These describe the *kind* of memory being sought
# (a finalized, owner-corrected version), never a specific fact, title, or
# the expected answer — so this does not leak dataset knowledge into
# retrieval and generalizes to any corrected memory.
_CORRECTED_MEMORY_QUERY_EXPANSION_TERMS = (
    "финальная подтверждённая версия воспоминания",
    "исправление владельца",
    "что было на самом деле",
)

_INTENTS_REQUIRING_CORRECTED_MEMORY_EXPANSION = frozenset(
    {
        MemoryQueryIntent.CORRECTED_MEMORY_FACT,
        MemoryQueryIntent.CORRECTION_HISTORY,
    }
)


def build_expanded_retrieval_query(
    user_message: str,
    intent: MemoryQueryIntent,
) -> str | None:
    """Build a separate, retrieval-only query representation for corrected-
    memory intent. Returns None when no expansion applies (the caller must
    then retrieve using only the original query, unchanged).

    The user-visible question is never modified — this expanded string is
    used only as an additional retrieval probe, never shown to the user or
    passed to the Brain as the conversation message.
    """
    if intent not in _INTENTS_REQUIRING_CORRECTED_MEMORY_EXPANSION:
        return None
    normalized_message = _normalize(user_message)
    if not normalized_message:
        return None
    return " ".join((normalized_message, *_CORRECTED_MEMORY_QUERY_EXPANSION_TERMS))
