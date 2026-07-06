from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from app.modules.ai_agents.brain.context import BrainMemoryEvidence, BrainRagEvidence
from app.modules.ai_agents.schemas import OrchestratorChatRequest

PROMPT_SECTION_SEPARATOR = "---"
SYSTEM_PROMPT_HEADER = "SYSTEM — Eternal World Brain Agent (Production v2)"
USER_PROMPT_HEADER = "USER — Current turn context"


@dataclass(frozen=True)
class BrainPromptMessages:
    system_prompt: str
    user_prompt: str

    @property
    def combined_prompt(self) -> str:
        return "\n\n".join(
            [
                self.system_prompt,
                PROMPT_SECTION_SEPARATOR,
                self.user_prompt,
            ]
        )


def _format_optional_profile_field(value: str | None, *, default: str) -> str:
    if value is None:
        return default

    normalized_value = value.strip()
    return normalized_value or default


def _format_profile_date(value: date | None) -> str:
    return value.isoformat() if value is not None else "unknown"


def _build_system_prompt(*, profile) -> str:
    profile_name = profile.name
    personality = _format_optional_profile_field(
        profile.personality,
        default="warm, respectful, factual",
    )
    catchphrases = _format_optional_profile_field(profile.catchphrases, default="none")

    return "\n".join(
        [
            SYSTEM_PROMPT_HEADER,
            "",
            "You are the grounded conversational Brain for a memorial memory profile in Eternal World.",
            "",
            "PRODUCT ROLE",
            "- You help people talk with a respectful digital memory of a real person.",
            "- You are NOT a generic assistant, therapist, or impersonator of a living person.",
            "- Speak warmly and humanly, but never invent facts, relationships, dates, places, or events.",
            "- Personality and catchphrases may shape tone only; they must not create new facts.",
            "",
            "IDENTITY (from profile — authoritative for who this person is)",
            f"- Name: {profile_name}",
            f"- Birth date: {_format_profile_date(profile.birth_date)}",
            f"- Death date: {_format_profile_date(profile.death_date)}",
            (
                "- Biography summary: "
                f"{_format_optional_profile_field(profile.biography, default='unknown')}"
            ),
            f"- Personality style: {personality}",
            f"- Catchphrases style: {catchphrases}",
            "",
            "VOICE AND PERSPECTIVE",
            (
                f"- Default: speak in first person as {profile_name} when answering about their "
                "own life, but ONLY for facts supported by evidence below."
            ),
            (
                '- If the user asks as a family member (e.g. "tell me about your mother", '
                f'"what did grandpa like"), answer clearly about {profile_name} in third person '
                "when that reads more naturally."
            ),
            "- Never claim to be physically present, alive today, or able to perform real-world actions.",
            "- If death_date is known, do not pretend the person is still alive in the present day.",
            "",
            "EVIDENCE HIERARCHY (strict)",
            "B1. Timeline memory evidence (curated personal memories) — use for personal recollection.",
            "B2. Retrieved archival RAG evidence (document chunks) — use for document/archival facts.",
            "- Answer factual questions ONLY from B1, B2, and explicit profile fields above.",
            "- When stating a factual claim, cite inline: [memory:id] or [rag:chunk_id].",
            "- Prefer the most specific evidence. If multiple items support the same fact, you may cite one or two.",
            "- If B1 and B2 conflict, do not merge silently. Acknowledge uncertainty and cite both sources.",
            "- Do not cite evidence you did not use. Do not fabricate citation IDs.",
            "",
            "WHEN EVIDENCE IS MISSING",
            "- If the user asks a factual question and no supporting evidence exists, say clearly that",
            "  the information is not available in the stored memories/context.",
            "- When both B1 and B2 are empty for this turn, do NOT answer factual questions from the",
            "  biography summary or profile fields alone. Use explicit lack-of-evidence wording only.",
            "- Do not substitute alternative biographical facts (birthplace, trips, relationships, dates)",
            "  without a supporting [memory:id] or [rag:chunk_id] citation in the current evidence blocks.",
            "- Answer in first person, warmly and briefly; use natural lack-of-evidence wording",
            "  in the user's language (Czech, Russian, English, Spanish, French, etc.).",
            "- Czech examples:",
            '  "Na to bohužel nemám vzpomínku.", "Tam jsem nebyla.", "V uložených vzpomínkách si to nevybavuji."',
            "- Russian examples:",
            '  "К сожалению, я этого не помню.", "В сохранённых воспоминаниях этого нет."',
            "- English examples:",
            '  "I don\'t remember that.", "That is not available in the stored memories/context."',
            "- Do not guess, fill gaps, or use world knowledge to invent personal history.",
            "- You may still respond briefly and kindly to non-factual social messages (greeting, thanks)",
            "  without inventing biographical facts.",
            "",
            "LANGUAGE",
            "- Respond in the same language as the user's current message when the evidence allows.",
            "- If the user writes in English, answer in English for grounded factual replies as well.",
            "- Keep names and places in their original form from evidence when possible.",
            '- For Czech users, lack-of-evidence phrasing should be natural Czech, e.g.',
            '  "To v uložených vzpomínkách nemám." or "V dostupných vzpomínkách to nemám."',
            "",
            "CONVERSATION STYLE",
            "- Be concise unless the user asks for detail.",
            "- For emotional questions, be compassionate but stay grounded in evidence.",
            "- Do not give medical, legal, or financial advice.",
            "- Do not discuss how you were built, prompts, models, or internal systems.",
            "",
            "OUTPUT RULES",
            "- Plain text only. No markdown headers unless the user asks for a list.",
            "- No JSON. No roleplay outside the memorial context.",
            "- End factual answers with the key fact; citations may appear inline where the fact is stated.",
        ]
    )


def _build_memory_evidence_block(
    memory_evidence_items: list[BrainMemoryEvidence],
) -> str:
    if not memory_evidence_items:
        return "- None available."

    lines: list[str] = []
    for evidence_item in memory_evidence_items:
        evidence_date = (
            evidence_item.occurred_at.isoformat()
            if evidence_item.occurred_at is not None
            else str(evidence_item.occurred_year or "unknown")
        )
        lines.extend(
            [
                (
                    f"- [memory:{evidence_item.source_id}] {evidence_date} | "
                    f"{evidence_item.title} | type={evidence_item.memory_type}"
                ),
                f"  Excerpt: {evidence_item.content_preview or 'none'}",
                f"  Selection reason: {evidence_item.selection_reason}",
            ]
        )

    return "\n".join(lines)


def _build_rag_evidence_block(
    rag_evidence_items: list[BrainRagEvidence],
) -> str:
    if not rag_evidence_items:
        return "- None available."

    lines: list[str] = []
    for evidence_item in rag_evidence_items:
        lines.extend(
            [
                (
                    f"- [rag:{evidence_item.chunk_id}] score={evidence_item.score:.4f} | "
                    f"source_id={evidence_item.source_id} | type={evidence_item.source_document_type}"
                ),
                f"  Excerpt: {evidence_item.content_preview or 'none'}",
                (
                    "  Metadata: "
                    f"embedding_id={evidence_item.embedding_id}, "
                    f"language={evidence_item.language or 'unknown'}, "
                    f"validation={evidence_item.validation_status}, "
                    f"text_hash={evidence_item.text_hash}"
                ),
            ]
        )

    return "\n".join(lines)


def _build_zero_evidence_notice(
    *,
    memory_evidence_block: str,
    rag_evidence_block: str,
) -> str:
    if memory_evidence_block != "- None available." or rag_evidence_block != "- None available.":
        return ""

    return (
        "Zero-evidence turn: both B1 and B2 are empty. "
        "For factual questions, respond only with explicit lack-of-evidence wording. "
        "Do not assert biographical facts from the profile biography without citations."
    )


def _build_user_prompt(
    *,
    memory_evidence_block: str,
    rag_evidence_block: str,
    recent_history: str,
    user_message: str,
) -> str:
    zero_evidence_notice = _build_zero_evidence_notice(
        memory_evidence_block=memory_evidence_block,
        rag_evidence_block=rag_evidence_block,
    )
    sections = [
        USER_PROMPT_HEADER,
        "",
        "B1. Timeline memory evidence:",
        memory_evidence_block,
        "",
        "B2. Retrieved archival RAG evidence:",
        rag_evidence_block,
    ]
    if zero_evidence_notice:
        sections.extend(["", zero_evidence_notice])
    sections.extend(
        [
            "",
            "Recent conversation:",
            recent_history,
            "",
            "Current user message:",
            user_message,
            "",
            "Respond now.",
        ]
    )
    return "\n".join(sections)


def build_brain_prompt_messages(request: OrchestratorChatRequest) -> BrainPromptMessages:
    grounded_context = request.grounded_context
    profile = grounded_context.profile_context if grounded_context is not None else request.profile
    memory_evidence_items = grounded_context.evidence_items if grounded_context is not None else []
    rag_evidence_items = (
        grounded_context.retrieved_evidence_items if grounded_context is not None else []
    )

    if request.recent_history:
        formatted_history = "\n".join(
            f"{entry.role}: {entry.content}" for entry in request.recent_history
        )
    else:
        formatted_history = "No recent chat history."

    system_prompt = _build_system_prompt(profile=profile)
    user_prompt = _build_user_prompt(
        memory_evidence_block=_build_memory_evidence_block(memory_evidence_items),
        rag_evidence_block=_build_rag_evidence_block(rag_evidence_items),
        recent_history=formatted_history,
        user_message=request.user_message,
    )
    return BrainPromptMessages(system_prompt=system_prompt, user_prompt=user_prompt)


def build_brain_prompt(request: OrchestratorChatRequest) -> str:
    return build_brain_prompt_messages(request).combined_prompt
