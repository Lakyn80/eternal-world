"""Orchestrates one context-aware Biographer question: build the bounded
context package, call the DeepSeek structured-output provider through the
Task 66.1 instrumentation, validate the result, allow at most one bounded
regeneration, and fall back to a deterministic contextual template if
generation cannot produce an accepted question (Task 65.6).
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.db.models import BiographerQuestion
from app.modules.avatar_biographer import duplicate_prevention, topics as topic_catalog
from app.modules.avatar_biographer.context_package import TopicContextPackage
from app.modules.avatar_biographer.provider import (
    BiographerProviderConfigurationError,
    BiographerProviderRequestError,
    BiographerProviderResponseError,
    BiographerQuestionProvider,
    build_biographer_question_provider,
)
from app.modules.avatar_biographer.prompt import (
    build_question_generation_system_prompt,
    build_question_generation_user_prompt,
)
from app.modules.avatar_biographer.schemas import ProviderQuestionResult
from app.modules.avatar_biographer.topics import BiographerTopic
from app.modules.provider_usage.context import AiCallContext
from app.modules.provider_usage.enums import AiFeature, AiStepType, ExecutionSource
from app.modules.provider_usage.service import (
    AuditFinalizationError,
    AuditPersistenceError,
    run_instrumented_single_attempt_action,
)
from app.modules.provider_usage.usage import normalize_openai_compatible_usage

_logger = get_logger("avatar_biographer")

#: Rotating deterministic fallback templates keyed by question intent. Used
#: only once LLM generation has genuinely failed/been rejected twice - never
#: the same generic broad question that caused the original defect.
_FALLBACK_TEMPLATES: tuple[tuple[str, dict[str, str]], ...] = (
    (
        "specific_person",
        {
            "cs": "Kdo byl v této části života pro vás nejdůležitější a proč?",
            "ru": "Кто был для вас самым важным человеком в этот период и почему?",
        },
    ),
    (
        "specific_event",
        {
            "cs": "Jaká jedna konkrétní událost z této doby vám nejvíc utkvěla v paměti?",
            "ru": "Какое одно конкретное событие того времени вам запомнилось больше всего?",
        },
    ),
    (
        "sensory_detail",
        {
            "cs": "Je nějaké místo, zvuk, vůně nebo předmět, který vám tuto dobu nejvíc připomíná?",
            "ru": "Есть ли место, звук, запах или предмет, который сильнее всего напоминает вам об этом времени?",
        },
    ),
    (
        "impact",
        {
            "cs": "Jak tato zkušenost ovlivnila vaše pozdější rozhodnutí?",
            "ru": "Как этот опыт повлиял на ваши решения в дальнейшем?",
        },
    ),
)


@dataclass(frozen=True)
class GeneratedQuestion:
    question_text: str
    generation_mode: str  # "llm_generated" | "deterministic_fallback"
    provider: str | None
    model: str | None
    ai_action_id: int | None
    question_intent: str | None
    validation_result: str  # "accepted" | "regenerated" | "fallback_used" | "generation_failed"
    fallback_used: bool


def _extract_token_usage(response) -> object:
    return normalize_openai_compatible_usage(
        raw_response={"id": response.provider_request_id, "usage": response.usage}
    )


def _call_provider(
    db: Session,
    *,
    provider: BiographerQuestionProvider,
    system_prompt: str,
    user_prompt: str,
    profile_id: int,
    user_id: int | None,
    trace_id: str | None,
    locale: str,
) -> tuple[ProviderQuestionResult, int, str, str] | None:
    context = AiCallContext(
        feature=AiFeature.AVATAR_BIOGRAPHER_QUESTION,
        execution_source=ExecutionSource.FASTAPI,
        trace_id=trace_id,
        requested_locale=locale,
        resolved_locale=locale,
        user_id=user_id,
        memorial_id=profile_id,
    )
    try:
        response, ai_action = run_instrumented_single_attempt_action(
            db,
            context=context,
            step_type=AiStepType.PROVIDER_STRUCTURED_OUTPUT,
            provider=provider.provider_name,
            model=getattr(provider, "model", provider.provider_name),
            operation=lambda: provider.generate_question(system_prompt=system_prompt, user_prompt=user_prompt),
            extract_token_usage=_extract_token_usage,
        )
    except (
        BiographerProviderRequestError,
        BiographerProviderResponseError,
        BiographerProviderConfigurationError,
        AuditPersistenceError,
        AuditFinalizationError,
    ) as exc:
        log_event(
            _logger,
            logging.WARNING,
            "biographer_question_generation_failed",
            profile_id=profile_id,
            trace_id=trace_id,
            error_type=type(exc).__name__,
        )
        return None
    return response.result, ai_action.id, response.provider_name, response.model


def _select_fallback_template(
    *, topic: BiographerTopic, locale: str, previous_questions_for_topic: list[BiographerQuestion]
) -> tuple[str, str]:
    index = len(previous_questions_for_topic) % len(_FALLBACK_TEMPLATES)
    intent, texts = _FALLBACK_TEMPLATES[index]
    return texts.get(locale, texts["ru"]), intent


def _build_fallback(
    *,
    topic: BiographerTopic,
    context_package: TopicContextPackage,
    locale: str,
    previous_questions_for_topic: list[BiographerQuestion],
    validation_result: str = "fallback_used",
) -> GeneratedQuestion:
    if context_package.selected_chunk_count == 0:
        # Nothing verified is known yet about this topic - the topic's own
        # human-curated starter question is still appropriate here.
        question_text = topic_catalog.question_text_for(topic, locale=locale)
        intent = "general_fact"
    else:
        question_text, intent = _select_fallback_template(
            topic=topic, locale=locale, previous_questions_for_topic=previous_questions_for_topic
        )
    return GeneratedQuestion(
        question_text=question_text,
        generation_mode="deterministic_fallback",
        provider=None,
        model=None,
        ai_action_id=None,
        question_intent=intent,
        validation_result=validation_result,
        fallback_used=True,
    )


def generate_question_for_topic(
    db: Session,
    *,
    topic: BiographerTopic,
    context_package: TopicContextPackage,
    locale: str,
    profile_id: int,
    user_id: int | None,
    trace_id: str | None,
    previous_questions_for_topic: list[BiographerQuestion],
    all_previous_questions: list[BiographerQuestion],
    skipped_or_postponed_texts: list[str],
) -> GeneratedQuestion:
    log_event(
        _logger,
        logging.INFO,
        "biographer_question_generation_started",
        profile_id=profile_id,
        trace_id=trace_id,
        topic=topic.key,
        locale=locale,
        retrieval_used=context_package.retrieval_used,
        selected_chunk_count=context_package.selected_chunk_count,
    )

    if not context_package.retrieval_used:
        return _build_fallback(
            topic=topic,
            context_package=context_package,
            locale=locale,
            previous_questions_for_topic=previous_questions_for_topic,
        )

    provider = build_biographer_question_provider()
    system_prompt = build_question_generation_system_prompt(locale=locale)

    def _attempt(rejected_text: str | None, rejected_reason: str | None):
        user_prompt = build_question_generation_user_prompt(
            topic=topic,
            context_package=context_package,
            previous_questions_for_topic=previous_questions_for_topic,
            skipped_or_postponed_question_texts=skipped_or_postponed_texts,
            rejected_question_text=rejected_text,
            rejection_reason=rejected_reason,
        )
        return _call_provider(
            db,
            provider=provider,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            profile_id=profile_id,
            user_id=user_id,
            trace_id=trace_id,
            locale=locale,
        )

    first_attempt = _attempt(None, None)
    if first_attempt is None:
        return _build_fallback(
            topic=topic,
            context_package=context_package,
            locale=locale,
            previous_questions_for_topic=previous_questions_for_topic,
        )

    result, ai_action_id, provider_name, model_name = first_attempt
    validation = _validate(
        result,
        topic=topic,
        context_package=context_package,
        all_previous_questions=all_previous_questions,
    )
    if validation.accepted:
        log_event(
            _logger,
            logging.INFO,
            "biographer_question_generation_succeeded",
            profile_id=profile_id,
            trace_id=trace_id,
            topic=topic.key,
            ai_action_id=ai_action_id,
        )
        return GeneratedQuestion(
            question_text=result.question,
            generation_mode="llm_generated",
            provider=provider_name,
            model=model_name,
            ai_action_id=ai_action_id,
            question_intent=result.question_intent,
            validation_result="accepted",
            fallback_used=False,
        )

    event_name = (
        "biographer_question_rejected_duplicate"
        if validation.reason
        in (
            duplicate_prevention.RejectionReason.EXACT_DUPLICATE,
            duplicate_prevention.RejectionReason.HIGH_LEXICAL_OVERLAP,
            duplicate_prevention.RejectionReason.SAME_TOPIC_INTENT,
        )
        else "biographer_question_rejected_known_answer"
    )
    log_event(
        _logger,
        logging.INFO,
        event_name,
        profile_id=profile_id,
        trace_id=trace_id,
        topic=topic.key,
        rejection_reason=validation.reason.value if validation.reason else None,
    )

    second_attempt = _attempt(result.question, validation.reason.value if validation.reason else None)
    if second_attempt is not None:
        result2, ai_action_id2, provider_name2, model_name2 = second_attempt
        validation2 = _validate(
            result2,
            topic=topic,
            context_package=context_package,
            all_previous_questions=all_previous_questions,
        )
        log_event(
            _logger,
            logging.INFO,
            "biographer_question_regenerated",
            profile_id=profile_id,
            trace_id=trace_id,
            topic=topic.key,
            accepted=validation2.accepted,
        )
        if validation2.accepted:
            return GeneratedQuestion(
                question_text=result2.question,
                generation_mode="llm_generated",
                provider=provider_name2,
                model=model_name2,
                ai_action_id=ai_action_id2,
                question_intent=result2.question_intent,
                validation_result="regenerated",
                fallback_used=False,
            )

    log_event(
        _logger,
        logging.INFO,
        "biographer_fallback_used",
        profile_id=profile_id,
        trace_id=trace_id,
        topic=topic.key,
    )
    return _build_fallback(
        topic=topic,
        context_package=context_package,
        locale=locale,
        previous_questions_for_topic=previous_questions_for_topic,
    )


def _validate(
    result: ProviderQuestionResult,
    *,
    topic: BiographerTopic,
    context_package: TopicContextPackage,
    all_previous_questions: list[BiographerQuestion],
) -> duplicate_prevention.ValidationResult:
    duplicate_check = duplicate_prevention.find_duplicate_against_history(
        result.question,
        topic_key=topic.key,
        candidate_question_intent=result.question_intent,
        previous_questions=all_previous_questions,
    )
    if not duplicate_check.accepted:
        return duplicate_check
    return duplicate_prevention.find_known_answer_violation(
        result.question,
        topic=topic,
        verified_chunk_count=context_package.selected_chunk_count,
        known_information_used_reported_by_provider=result.known_information_used,
    )
