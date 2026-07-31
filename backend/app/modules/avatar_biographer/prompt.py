"""Prompt construction for context-aware Biographer question generation
(Task 65.6). Mirrors `content_translation.prompt`'s structure - plain
string-building functions, no templating engine, JSON-only output contract.
"""

from __future__ import annotations

from app.modules.avatar_biographer.context_package import TopicContextPackage
from app.modules.avatar_biographer.topics import BiographerTopic
from app.db.models import BiographerQuestion

_LOCALE_NAMES = {
    "cs": "Czech (čeština)",
    "ru": "Russian (русский)",
    "en": "English",
}

_QUESTION_INTENTS = (
    "specific_memory",
    "specific_person",
    "specific_event",
    "sensory_detail",
    "impact",
    "general_fact",
)


def _locale_name(locale: str) -> str:
    return _LOCALE_NAMES.get(locale, locale)


def build_question_generation_system_prompt(*, locale: str) -> str:
    locale_name = _locale_name(locale)
    return (
        "You are the question-writing component of a digital memorial's AI Biographer. "
        "Your only job is to write exactly ONE short, warm, non-technical follow-up question "
        "that helps a family member add a genuinely new detail to a person's life story.\n\n"
        "Rules (follow all of them exactly):\n"
        "1. Write the question entirely in " + locale_name + ". Do not mix languages.\n"
        "2. Ask about exactly one coherent thing - never combine two questions.\n"
        "3. If KNOWN VERIFIED CONTEXT is provided below, do not ask something that context "
        "already clearly answers. Instead, ask for a more specific, concrete detail that "
        "builds on it (a particular object, person, moment, place, or feeling), or pivot to "
        "an adjacent unanswered detail for the same topic.\n"
        "4. You may reference a known verified fact as context for your question, but you must "
        "never invent, assume, or assert a new fact that is not present in the KNOWN VERIFIED "
        "CONTEXT (e.g. do not name a specific relative, object, or event unless it already "
        "appears in that context).\n"
        "5. Never repeat a question listed under PREVIOUS QUESTIONS or SKIPPED QUESTIONS below, "
        "even reworded - ask about something genuinely different.\n"
        "6. Avoid medical or legal diagnosis, coercive framing, or dramatizing traumatic topics.\n"
        "7. Keep the question short (roughly one sentence) and understandable to a "
        "non-technical person - never mention retrieval, chunks, embeddings, databases, or "
        "AI/model internals.\n"
        "8. Return ONLY a single JSON object matching exactly this schema, with no surrounding "
        "text or Markdown fences:\n"
        '{"question": "...", "known_information_used": true|false, '
        '"question_intent": "specific_memory|specific_person|specific_event|sensory_detail|'
        'impact|general_fact", "confidence": "high|medium|low"}\n'
        '"known_information_used" must be true only if your question directly builds on '
        "something stated in KNOWN VERIFIED CONTEXT."
    )


def _format_context_bullets(chunk_excerpts: list[str]) -> str:
    if not chunk_excerpts:
        return "(none - nothing verified is known yet about this topic)"
    return "\n".join(f"- {excerpt}" for excerpt in chunk_excerpts)


def _format_question_list(questions: list[str]) -> str:
    if not questions:
        return "(none)"
    return "\n".join(f"- {text}" for text in questions)


def build_question_generation_user_prompt(
    *,
    topic: BiographerTopic,
    context_package: TopicContextPackage,
    previous_questions_for_topic: list[BiographerQuestion],
    skipped_or_postponed_question_texts: list[str],
    rejected_question_text: str | None = None,
    rejection_reason: str | None = None,
) -> str:
    topic_label = topic.key.replace("_", " ")
    previous_texts = [question.question_text for question in previous_questions_for_topic]
    sections = [
        f"TOPIC: {topic_label}",
        "KNOWN VERIFIED CONTEXT (already established, do not re-ask this):",
        _format_context_bullets(context_package.chunk_excerpts),
        "PREVIOUS QUESTIONS ALREADY ASKED FOR THIS TOPIC:",
        _format_question_list(previous_texts),
        "SKIPPED OR POSTPONED QUESTIONS (do not repeat these either):",
        _format_question_list(skipped_or_postponed_question_texts),
    ]
    if rejected_question_text is not None:
        sections.append(
            "Your previous attempt was rejected and must not be repeated in any form:\n"
            f'- rejected question: "{rejected_question_text}"\n'
            f"- rejection reason: {rejection_reason}\n"
            "Write a genuinely different question this time."
        )
    sections.append(
        "Write exactly one new question about this topic that adds information not already "
        "covered above. Return only the JSON object described in the system prompt."
    )
    return "\n\n".join(sections)
