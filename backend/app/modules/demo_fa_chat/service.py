from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.core.metrics import (
    observe_avatar_corrected_memory_resolution,
    observe_avatar_memory_query_intent,
    observe_memory_candidate_created,
    observe_memory_candidate_reviewed,
    observe_memory_promotion_created,
    observe_memory_promotion_status,
    observe_rag_retrieval_error,
    observe_rag_retrieval_success,
)
from app.db.models import User
from app.modules.active_retrieval_config.exceptions import ActiveRetrievalConfigNotFoundError
from app.modules.active_retrieval_config.service import (
    get_active_retrieval_config,
    get_production_recommended_active_retrieval_config,
)
from app.modules.ai_agents import get_agent_orchestrator
from app.modules.ai_agents.brain.context import (
    CORRECTED_MEMORY_EVIDENCE_CAP,
    build_rag_evidence_items,
    build_vector_retrieval_grounded_context,
    filter_learned_memory_results_by_question_intent,
    prioritize_corrected_memory_evidence,
)
from app.modules.ai_agents.schemas import MemoryProfileContext, OrchestratorChatRequest
from app.core.config import settings as app_settings
from app.modules.provider_usage import service as provider_usage_service
from app.modules.provider_usage.context import AiCallContext
from app.modules.provider_usage.enums import AiFeature, AiStepType, ExecutionSource
from app.modules.provider_usage.service import run_instrumented_single_attempt_action
from app.modules.provider_usage.usage import normalize_openai_compatible_usage
from app.modules.avatar_persona import (
    CORRECTED_MEMORY_EXPANSION_RULE_ID,
    build_expanded_retrieval_query,
    build_memory_candidate,
    classify_memory_query_intent,
    derive_avatar_response_directives,
    load_demo_avatar_persona,
)
from app.modules.avatar_memory_promotions import service as avatar_memory_promotions_service
from app.modules.avatar_memory_indexing import service as avatar_memory_indexing_service
from app.modules.avatar_memory_promotions.schemas import build_avatar_memory_promotion_read
from app.modules.content_translation import repository as content_translation_repository
from app.modules.content_translation import service as content_translation_service
from app.modules.content_translation.schemas import MemoryContentTranslationRead, TranslationFieldRequest
from app.modules.conversation_memory_candidates import service as conversation_memory_candidates_service
from app.modules.conversation_memory_candidates.schemas import (
    MemoryCandidateCreate,
    MemoryCandidateRead,
    MemoryCandidateReviewUpdate,
    MemoryCandidateStatus,
    build_memory_candidate_read,
)
from app.modules.family_memory_enrichment import service as family_memory_enrichment_service
from app.modules.family_memory_enrichment import eligibility as family_memory_eligibility
from app.modules.family_memory_enrichment.clarification import localize_question_text
from app.modules.family_memory_enrichment.enums import EnrichmentStatus, PrivacyScope
from app.modules.family_memory_enrichment.schemas import (
    CandidateEnrichmentRead,
    ClarificationAnswerRequest,
    ClarificationQuestionRead,
    DemoFamilyActorContext,
    FamilyMemoryContributionRead,
)
from app.modules.embeddings.embedding_cache import build_text_hash
from app.modules.embeddings.runtime import resolve_embedding_runtime_diagnostics
from app.modules.memory_profiles.repository import get_memory_profile_for_user, list_memory_profiles_for_user
from app.modules.qdrant_indexing.client import build_qdrant_client
from app.modules.rag_evaluation.brain_eval_e2e_bootstrap import (
    FAMILY_AVATAR_RU_E2E_EMAIL,
    FAMILY_AVATAR_RU_E2E_PROFILE_NAME,
    FAMILY_AVATAR_RU_E2E_SOURCE_KEY,
    FAMILY_AVATAR_RU_E2E_SOURCE_TITLE,
    build_family_avatar_ru_e2e_collection_name,
)
from app.modules.rag_retrieval.schemas import RagRetrievalRequest, RagRetrievalResultRead
from app.modules.rag_retrieval.service import retrieve_profile_rag
from app.modules.rag_sources.repository import list_rag_sources_for_profile
from app.modules.users.repository import get_user_by_email

from .schemas import (
    DemoFaChatEvidenceItem,
    DemoFaChatMemoryCandidate,
    DemoFaChatMemoryCandidateReviewDetail,
    DemoFaChatMemoryCandidateReviewResponse,
    DemoFaChatMemoryCandidateSummary,
    DemoFaChatMessageResponse,
)


DEMO_FA_CHAT_MESSAGE_MAX_LENGTH = 4000
DEMO_FA_CHAT_EVIDENCE_PREVIEW_LENGTH = 220
SUPPORTED_REVIEW_CONTENT_LANGUAGES = frozenset({"cs", "ru", "en"})


def _localized_detail(locale: str, *, cs: str, ru: str, en: str | None = None) -> str:
    """Pick the right-language detail while keeping Russian as the default."""
    if locale == "cs":
        return cs
    if locale == "en" and en is not None:
        return en
    return ru


def _review_ready_message(locale: str) -> str:
    if locale == "cs":
        return "Děkuji. Návrh vzpomínky je připraven ke kontrole vlastníkem avatara."
    if locale == "en":
        return "Thank you. The memory draft is ready for the avatar owner's review."
    return "Спасибо. Черновик воспоминания готов к проверке владельцем аватара."


def _normalize_review_content_language(language: str | None) -> str | None:
    normalized_language = (language or "").strip().lower()
    if normalized_language in SUPPORTED_REVIEW_CONTENT_LANGUAGES:
        return normalized_language
    return None


def _localize_review_text(
    db: Session,
    *,
    candidate_id: int,
    entity_type: str,
    entity_id: str,
    field_name: str,
    source_language: str | None,
    requested_locale: str,
    source_text: str | None,
    contribution_id: int | None = None,
    clarification_id: int | None = None,
) -> str | None:
    if source_text is None:
        return None

    normalized_source_language = _normalize_review_content_language(source_language)
    normalized_target_language = _normalize_review_content_language(requested_locale)
    if normalized_source_language is None or normalized_target_language is None:
        return source_text
    if normalized_source_language == normalized_target_language:
        return source_text

    current_source_text = source_text.strip()
    if not current_source_text:
        return source_text

    current_row = content_translation_repository.get_current(
        db,
        entity_type=entity_type,
        entity_id=entity_id,
        field_name=field_name,
        target_language=normalized_target_language,
    )
    if content_translation_service.is_translation_current(
        current_row, current_source_text=current_source_text
    ):
        translated_text = (current_row.translated_text or "").strip() if current_row is not None else ""
        if translated_text:
            provider_usage_service.record_translation_cache_hit(
                source_locale=normalized_source_language,
                target_locale=normalized_target_language,
                entity_type=entity_type,
                field_name=field_name,
            )
            return current_row.translated_text

    provider_usage_service.record_translation_cache_miss(
        source_locale=normalized_source_language,
        target_locale=normalized_target_language,
        entity_type=entity_type,
        field_name=field_name,
    )
    try:
        row = content_translation_service.translate_content_field(
            db,
            TranslationFieldRequest(
                candidate_id=candidate_id,
                contribution_id=contribution_id,
                clarification_id=clarification_id,
                entity_type=entity_type,
                entity_id=entity_id,
                field_name=field_name,
                source_language=normalized_source_language,
                target_language=normalized_target_language,
                source_text=current_source_text,
            ),
            call_context=AiCallContext(
                feature=AiFeature.DYNAMIC_MEMORY_TRANSLATION,
                execution_source=ExecutionSource.FASTAPI,
                requested_locale=normalized_target_language,
                resolved_locale=normalized_target_language,
            ),
        )
        db.commit()
    except Exception as exc:
        db.rollback()
        log_event(
            logger,
            30,
            "review_content_localization_failed",
            candidate_id=candidate_id,
            entity_type=entity_type,
            entity_id=entity_id,
            field_name=field_name,
            source_language=normalized_source_language,
            target_language=normalized_target_language,
            error_type=exc.__class__.__name__,
        )
        return source_text

    translated_text = (row.translated_text or "").strip()
    if (
        translated_text
        and content_translation_service.is_translation_current(
            row, current_source_text=current_source_text
        )
    ):
        return row.translated_text
    return source_text


def _localize_candidate_review_read(
    db: Session,
    *,
    candidate: MemoryCandidateRead,
    locale: str,
) -> MemoryCandidateRead:
    source_language = candidate.language
    updates: dict[str, str | None] = {}
    for field_name in (
        "user_message_excerpt",
        "proposed_memory_text",
        "reason",
        "finalized_memory_text",
        "review_note",
        "rejection_reason",
    ):
        localized_value = _localize_review_text(
            db,
            candidate_id=candidate.candidate_id,
            entity_type="memory_candidate",
            entity_id=str(candidate.candidate_id),
            field_name=field_name,
            source_language=source_language,
            requested_locale=locale,
            source_text=getattr(candidate, field_name),
        )
        if localized_value != getattr(candidate, field_name):
            updates[field_name] = localized_value
    return candidate.model_copy(update=updates) if updates else candidate


def _localize_enrichment_read(
    db: Session,
    *,
    candidate_id: int,
    candidate_language: str | None,
    enrichment: CandidateEnrichmentRead | None,
    locale: str,
) -> CandidateEnrichmentRead | None:
    if enrichment is None:
        return None

    updates: dict[str, object] = {}
    localized_finalized_memory_text = _localize_review_text(
        db,
        candidate_id=candidate_id,
        entity_type="memory_candidate",
        entity_id=str(candidate_id),
        field_name="finalized_memory_text",
        source_language=candidate_language,
        requested_locale=locale,
        source_text=enrichment.finalized_memory_text,
    )
    if localized_finalized_memory_text != enrichment.finalized_memory_text:
        updates["finalized_memory_text"] = localized_finalized_memory_text

    if enrichment.next_clarification_question is not None:
        localized_next_question = _localize_clarification_read(
            db,
            candidate_id=candidate_id,
            candidate_language=candidate_language,
            clarification=enrichment.next_clarification_question,
            locale=locale,
        )
        if localized_next_question != enrichment.next_clarification_question:
            updates["next_clarification_question"] = localized_next_question

    return enrichment.model_copy(update=updates) if updates else enrichment


def _localize_contribution_read(
    db: Session,
    *,
    candidate_id: int,
    candidate_language: str | None,
    contribution: FamilyMemoryContributionRead,
    locale: str,
) -> FamilyMemoryContributionRead:
    localized_text = _localize_review_text(
        db,
        candidate_id=candidate_id,
        contribution_id=contribution.contribution_id,
        entity_type="family_memory_contribution",
        entity_id=str(contribution.contribution_id),
        field_name="contribution_text",
        source_language=contribution.language or candidate_language,
        requested_locale=locale,
        source_text=contribution.contribution_text,
    )
    if localized_text == contribution.contribution_text:
        return contribution
    return contribution.model_copy(update={"contribution_text": localized_text})


def _localize_clarification_read(
    db: Session,
    *,
    candidate_id: int,
    candidate_language: str | None,
    clarification: ClarificationQuestionRead,
    locale: str,
) -> ClarificationQuestionRead:
    localized_text = _localize_review_text(
        db,
        candidate_id=candidate_id,
        clarification_id=clarification.clarification_id,
        entity_type="clarification_question",
        entity_id=str(clarification.clarification_id),
        field_name="question_text",
        source_language=clarification.language or candidate_language,
        requested_locale=locale,
        source_text=clarification.question_text,
    )
    if localized_text == clarification.question_text:
        return clarification
    return clarification.model_copy(update={"question_text": localized_text})


def demo_fa_chat_profile_unavailable_detail(locale: str = "ru") -> str:
    return _localized_detail(
        locale,
        cs="Testovací profil avatara momentálně není dostupný.",
        ru="Тестовый профиль аватара сейчас недоступен.",
        en="The demo avatar profile is currently unavailable.",
    )


def demo_fa_chat_not_initialized_detail(locale: str = "ru") -> str:
    return _localized_detail(
        locale,
        cs="Demo profil zatím není inicializován. Spusťte prosím přípravu testové paměti.",
        ru="Демо-профиль ещё не инициализирован. Пожалуйста, запустите подготовку тестовой памяти.",
        en="The demo profile is not initialized yet. Run the demo memory preparation first.",
    )


def demo_fa_chat_embedding_unavailable_detail(locale: str = "ru") -> str:
    return _localized_detail(
        locale,
        cs=(
            "Demo je dočasně nedostupné: model embeddingů BGE-M3 není inicializován. "
            "Spusťte přípravu modelu a zkuste to znovu."
        ),
        ru=(
            "Демо временно недоступно: модель эмбеддингов BGE-M3 не инициализирована. "
            "Запустите подготовку модели и повторите запрос."
        ),
        en=(
            "The demo is temporarily unavailable: the BGE-M3 embeddings model is not initialized. "
            "Run the model preparation and try again."
        ),
    )


def demo_fa_chat_internal_error_detail(locale: str = "ru") -> str:
    return _localized_detail(
        locale,
        cs="Nepodařilo se získat odpověď avatara. Zkuste to prosím znovu.",
        ru="Не удалось получить ответ аватара. Попробуйте ещё раз.",
        en="The avatar response could not be generated. Please try again.",
    )


# Backward-compatible module-level aliases (Russian default) for any caller
# that still imports the old constant names directly.
DEMO_FA_CHAT_PROFILE_UNAVAILABLE_DETAIL = demo_fa_chat_profile_unavailable_detail()
DEMO_FA_CHAT_NOT_INITIALIZED_DETAIL = demo_fa_chat_not_initialized_detail()
DEMO_FA_CHAT_EMBEDDING_UNAVAILABLE_DETAIL = demo_fa_chat_embedding_unavailable_detail()
DEMO_FA_CHAT_INTERNAL_ERROR_DETAIL = demo_fa_chat_internal_error_detail()

logger = get_logger("demo_fa_chat")


class DemoFaChatValidationError(Exception):
    pass


class DemoFaChatProfileUnavailableError(Exception):
    pass


class DemoFaChatInitializationError(Exception):
    pass


def _localize_clarification_question_for_locale(
    question: ClarificationQuestionRead | None,
    *,
    locale: str,
) -> ClarificationQuestionRead | None:
    """Display-only Czech projection of a clarification question (Part E.17).

    Both locales still refer to the exact same clarification record
    (``clarification_id``/``question_key`` unchanged) - only the rendered
    ``question_text`` differs.
    """
    if question is None or locale != "cs":
        return question
    return question.model_copy(
        update={
            "question_text": localize_question_text(
                question_key=question.question_key,
                source_text=question.question_text,
                locale=locale,
            )
        }
    )


@dataclass(frozen=True)
class DemoFaChatResolvedProfile:
    user: User
    profile: object


@dataclass(frozen=True)
class DemoFaChatResolvedRuntime:
    collection_name: str
    retrieval_mode: str
    top_k: int
    source_id: int
    point_count: int


def _normalize_message_text(value: str, *, locale: str = "ru") -> str:
    normalized_value = value.strip()
    if not normalized_value:
        raise DemoFaChatValidationError(
            _localized_detail(
                locale,
                cs="Zpráva nesmí být prázdná.",
                ru="Сообщение не должно быть пустым.",
                en="The message must not be empty.",
            )
        )
    if len(normalized_value) > DEMO_FA_CHAT_MESSAGE_MAX_LENGTH:
        raise DemoFaChatValidationError(
            _localized_detail(
                locale,
                cs="Zpráva je pro demo-chat příliš dlouhá.",
                ru="Сообщение слишком длинное для демо-чата.",
                en="The message is too long for the demo chat.",
            )
        )
    return normalized_value


def _build_message_hash_prefix(message: str) -> str:
    return build_text_hash(message).split(":", 1)[1][:8]


# How many extra candidates (beyond the profile's normal top_k) to over-fetch
# for corrected-memory-intent turns only, so the dispute-shaped-evidence
# filter has room to drop a filtered item without shrinking the final
# evidence set below what an ordinary turn would receive. Bounded and small
# on purpose — this is a pool-then-filter-then-truncate pattern scoped to one
# intent path, not a change to the profile's configured top_k.
_CORRECTED_MEMORY_CANDIDATE_POOL_OVERFETCH = 5


def _merge_ranked_retrieval_results(
    *,
    primary: list[RagRetrievalResultRead],
    secondary: list[RagRetrievalResultRead],
    limit: int,
) -> list[RagRetrievalResultRead]:
    """Deterministically merge two ranked retrieval result lists.

    Deduplicates by chunk_id (keeping the higher of the two scores when a
    chunk appears in both), then re-sorts by score and truncates to `limit`
    — the same top_k the profile's active retrieval config already uses, so
    the Brain never receives more evidence than an ordinary single-query
    turn would. This is a downstream merge over two already-independently
    profile/avatar/privacy-filtered result sets; it does not change how
    either individual retrieval call itself scores or filters candidates.
    """
    merged_by_chunk_id: dict[int, RagRetrievalResultRead] = {}
    for result in (*primary, *secondary):
        existing = merged_by_chunk_id.get(result.chunk_id)
        if existing is None or result.score > existing.score:
            merged_by_chunk_id[result.chunk_id] = result
    ranked = sorted(merged_by_chunk_id.values(), key=lambda item: item.score, reverse=True)
    return ranked[:limit]


def _build_expected_demo_collection_name() -> str:
    recommendation = get_production_recommended_active_retrieval_config()
    return build_family_avatar_ru_e2e_collection_name(
        base_collection_name=recommendation.collection_name,
    )


def _build_profile_context(profile) -> MemoryProfileContext:
    return MemoryProfileContext(
        id=profile.id,
        name=profile.name,
        birth_date=profile.birth_date,
        death_date=profile.death_date,
        biography=profile.biography,
        personality=profile.personality,
        catchphrases=profile.catchphrases,
        is_public=profile.is_public,
    )


def _resolve_demo_avatar_persona():
    return load_demo_avatar_persona()


def _resolve_demo_profile(
    db: Session,
    *,
    profile_id: int | None,
    locale: str = "ru",
) -> DemoFaChatResolvedProfile:
    user = get_user_by_email(db, FAMILY_AVATAR_RU_E2E_EMAIL)
    if user is None:
        raise DemoFaChatProfileUnavailableError(demo_fa_chat_profile_unavailable_detail(locale))

    if profile_id is not None:
        profile = get_memory_profile_for_user(
            db,
            user_id=user.id,
            profile_id=profile_id,
        )
    else:
        profiles = list_memory_profiles_for_user(db, user.id)
        profile = next(
            (item for item in profiles if item.name == FAMILY_AVATAR_RU_E2E_PROFILE_NAME),
            None,
        )

    if profile is None:
        raise DemoFaChatProfileUnavailableError(demo_fa_chat_profile_unavailable_detail(locale))

    return DemoFaChatResolvedProfile(user=user, profile=profile)


def _build_qdrant_demo_source_filter(
    *,
    owner_user_id: int,
    profile_id: int,
    source_id: int,
) -> dict[str, object]:
    return {
        "must": [
            {"key": "owner_user_id", "match": {"value": owner_user_id}},
            {"key": "profile_id", "match": {"value": profile_id}},
            {"key": "source_id", "match": {"value": source_id}},
        ]
    }


def _assert_embedding_runtime_ready(*, model_code: str, collection_name: str, locale: str = "ru") -> None:
    diagnostics = resolve_embedding_runtime_diagnostics(
        model_code=model_code,
        collection_name=collection_name,
    )
    is_bge_m3_model = diagnostics.model_code.startswith("bge_m3")
    snapshot_missing = is_bge_m3_model and not diagnostics.bge_m3_snapshot_cached
    if snapshot_missing or diagnostics.is_mock_query_provider:
        log_event(
            logger,
            40,
            "fa_demo_chat_embedding_unavailable",
            model_code=diagnostics.model_code,
            embedding_provider_setting=diagnostics.embedding_provider_setting,
            is_mock_query_provider=diagnostics.is_mock_query_provider,
            bge_m3_snapshot_cached=diagnostics.bge_m3_snapshot_cached,
            bge_m3_snapshot_path=diagnostics.bge_m3_snapshot_path,
            huggingface_offline_mode=diagnostics.huggingface_offline_mode,
        )
        raise DemoFaChatInitializationError(demo_fa_chat_embedding_unavailable_detail(locale))


def _resolve_demo_runtime(
    db: Session,
    *,
    resolved_profile: DemoFaChatResolvedProfile,
    locale: str = "ru",
) -> DemoFaChatResolvedRuntime:
    expected_collection_name = _build_expected_demo_collection_name()
    recommendation = get_production_recommended_active_retrieval_config()
    try:
        active_config = get_active_retrieval_config(
            db,
            current_user=resolved_profile.user,
            profile_id=resolved_profile.profile.id,
        )
    except ActiveRetrievalConfigNotFoundError as exc:
        raise DemoFaChatInitializationError(demo_fa_chat_not_initialized_detail(locale)) from exc

    if (
        active_config.model_code != recommendation.model_code
        or active_config.collection_name != expected_collection_name
        or active_config.retrieval_mode != recommendation.retrieval_mode
    ):
        raise DemoFaChatInitializationError(demo_fa_chat_not_initialized_detail(locale))

    _assert_embedding_runtime_ready(
        model_code=active_config.model_code,
        collection_name=active_config.collection_name,
        locale=locale,
    )

    sources = list_rag_sources_for_profile(
        db,
        owner_user_id=resolved_profile.user.id,
        profile_id=resolved_profile.profile.id,
    )
    source = next(
        (
            item
            for item in sources
            if item.title == FAMILY_AVATAR_RU_E2E_SOURCE_TITLE
            and isinstance(item.source_metadata, dict)
            and item.source_metadata.get("family_avatar_ru_e2e_key") == FAMILY_AVATAR_RU_E2E_SOURCE_KEY
        ),
        None,
    )
    if source is None:
        raise DemoFaChatInitializationError(demo_fa_chat_not_initialized_detail(locale))

    qdrant_point_count = build_qdrant_client().count_points(
        collection_name=active_config.collection_name,
        search_filter=_build_qdrant_demo_source_filter(
            owner_user_id=resolved_profile.user.id,
            profile_id=resolved_profile.profile.id,
            source_id=source.id,
        ),
    )
    if qdrant_point_count <= 0:
        raise DemoFaChatInitializationError(demo_fa_chat_not_initialized_detail(locale))

    return DemoFaChatResolvedRuntime(
        collection_name=active_config.collection_name,
        retrieval_mode=active_config.retrieval_mode,
        top_k=active_config.top_k,
        source_id=source.id,
        point_count=qdrant_point_count,
    )


def _truncate_preview(text: str, *, limit: int = DEMO_FA_CHAT_EVIDENCE_PREVIEW_LENGTH) -> str:
    normalized_text = " ".join(text.split())
    if len(normalized_text) <= limit:
        return normalized_text
    return f"{normalized_text[: limit - 3].rstrip()}..."


def _build_evidence_items(
    results: list[RagRetrievalResultRead],
    *,
    debug: bool,
) -> list[DemoFaChatEvidenceItem]:
    if not debug:
        return []

    safe_payload_keys = {
        "avatar_id",
        "candidate_id",
        "chunk_source_id",
        "indexed_at",
        "memory_status",
        "promotion_id",
        "provenance",
        "source_type",
    }

    return [
        DemoFaChatEvidenceItem(
            chunk_id=str(result.chunk_id),
            source_id=result.source_id,
            source_title=result.source_title,
            score=float(result.score),
            text_preview=_truncate_preview(result.text),
            payload_metadata={
                key: value
                for key, value in result.payload_metadata.items()
                if key in safe_payload_keys
            },
        )
        for result in results
    ]


def _build_demo_memory_candidate(
    *,
    extracted_candidate,
    persisted_candidate,
    enrichment: CandidateEnrichmentRead | None,
) -> DemoFaChatMemoryCandidate:
    return DemoFaChatMemoryCandidate(
        candidate_id=persisted_candidate.id if persisted_candidate is not None else None,
        status=MemoryCandidateStatus.NEEDS_REVIEW,
        confidence="unverified",
        source="conversation",
        proposed_memory_text=extracted_candidate.proposed_memory_text,
        user_message_excerpt=extracted_candidate.user_message_excerpt,
        reason=extracted_candidate.reason,
        memory_type=enrichment.memory_type if enrichment is not None else None,
        enrichment_status=enrichment.enrichment_status if enrichment is not None else None,
        privacy_scope=enrichment.privacy_scope if enrichment is not None else None,
        dispute_status=enrichment.dispute_status if enrichment is not None else None,
        unresolved_clarification_count=(
            enrichment.unresolved_clarification_count if enrichment is not None else None
        ),
    )


def _persist_memory_candidate(
    db: Session,
    *,
    owner_user_id: int,
    avatar_id: str,
    profile_id: int,
    trace_id: str,
    language: str,
    extracted_candidate,
    enrichment_enabled: bool = False,
):
    payload = MemoryCandidateCreate(
        owner_user_id=owner_user_id,
        avatar_id=avatar_id,
        profile_id=profile_id,
        conversation_id=None,
        trace_id=trace_id,
        user_message_excerpt=extracted_candidate.user_message_excerpt,
        proposed_memory_text=extracted_candidate.proposed_memory_text,
        reason=extracted_candidate.reason,
        language=language,
        enrichment_status=(
            EnrichmentStatus.DRAFT
            if enrichment_enabled
            else EnrichmentStatus.READY_FOR_OWNER_REVIEW
        ),
        finalized_memory_text=(
            None if enrichment_enabled else extracted_candidate.proposed_memory_text
        ),
        privacy_scope=(
            PrivacyScope.PRIVATE_OWNER if enrichment_enabled else PrivacyScope.PUBLIC_LEGACY
        ),
        workflow_version=2 if enrichment_enabled else 1,
    )
    return conversation_memory_candidates_service.create_candidate(
        db,
        payload=payload,
        commit=not enrichment_enabled,
    )


def list_demo_memory_candidates(
    db: Session,
    *,
    profile_id: int | None,
    actor: DemoFamilyActorContext | None = None,
    locale: str = "ru",
):
    resolved_profile = _resolve_demo_profile(db, profile_id=profile_id, locale=locale)
    avatar_persona = _resolve_demo_avatar_persona()
    candidates = conversation_memory_candidates_service.list_candidates(
        db,
        owner_user_id=resolved_profile.user.id,
        profile_id=resolved_profile.profile.id,
        avatar_id=avatar_persona.avatar_id,
    )
    visible = []
    for candidate in candidates:
        if candidate.workflow_version < 2:
            visible.append(candidate)
            continue
        if actor is None:
            continue
        try:
            family_memory_enrichment_service.get_candidate_enrichment(
                db,
                owner_user_id=resolved_profile.user.id,
                candidate_id=candidate.id,
                actor=actor,
            )
        except family_memory_enrichment_service.FamilyMemoryNotFoundError:
            continue
        visible.append(candidate)
    return visible


def get_demo_memory_candidate(
    db: Session,
    *,
    profile_id: int | None,
    candidate_id: int,
    actor: DemoFamilyActorContext | None = None,
    allow_enriched_internal: bool = False,
    locale: str = "ru",
):
    resolved_profile = _resolve_demo_profile(db, profile_id=profile_id, locale=locale)
    candidate = conversation_memory_candidates_service.get_candidate(
        db,
        owner_user_id=resolved_profile.user.id,
        candidate_id=candidate_id,
    )
    if candidate.profile_id != resolved_profile.profile.id:
        raise conversation_memory_candidates_service.ConversationMemoryCandidateNotFoundError(
            "Memory candidate not found"
        )
    if candidate.workflow_version >= 2 and not allow_enriched_internal:
        if actor is None:
            raise family_memory_enrichment_service.FamilyMemoryNotFoundError(
                "Family memory candidate not found"
            )
        family_memory_enrichment_service.get_candidate_enrichment(
            db,
            owner_user_id=resolved_profile.user.id,
            candidate_id=candidate.id,
            actor=actor,
        )
    return candidate


def list_demo_memory_candidate_summaries(
    db: Session,
    *,
    profile_id: int | None,
    actor: DemoFamilyActorContext | None = None,
    locale: str = "ru",
) -> list[DemoFaChatMemoryCandidateSummary]:
    """Review-inbox card projection (Task 64.5). Reuses existing visibility and
    contribution-privacy rules; adds no new business logic."""
    resolved_profile = _resolve_demo_profile(db, profile_id=profile_id, locale=locale)
    candidates = list_demo_memory_candidates(db, profile_id=profile_id, actor=actor, locale=locale)
    summaries: list[DemoFaChatMemoryCandidateSummary] = []
    for candidate in candidates:
        promotion = candidate.avatar_memory_promotion
        contributor_actor_id = None
        contributor_actor_role = None
        contributor_relationship_to_owner = None
        if candidate.workflow_version >= 2 and actor is not None:
            visible_contributions = family_memory_enrichment_service.list_contributions(
                db,
                owner_user_id=resolved_profile.user.id,
                candidate_id=candidate.id,
                actor=actor,
            )
            earliest = next(
                (item for item in visible_contributions if item.contribution_type == "initial_claim"),
                visible_contributions[0] if visible_contributions else None,
            )
            if earliest is not None:
                contributor_actor_id = earliest.actor_id
                contributor_actor_role = earliest.actor_role
                contributor_relationship_to_owner = earliest.relationship_to_owner
        localized_finalized_memory_text = _localize_review_text(
            db,
            candidate_id=candidate.id,
            entity_type="memory_candidate",
            entity_id=str(candidate.id),
            field_name="finalized_memory_text",
            source_language=candidate.language,
            requested_locale=locale,
            source_text=candidate.finalized_memory_text,
        )
        localized_user_message_excerpt = candidate.user_message_excerpt
        if not (localized_finalized_memory_text or "").strip():
            localized_user_message_excerpt = (
                _localize_review_text(
                    db,
                    candidate_id=candidate.id,
                    entity_type="memory_candidate",
                    entity_id=str(candidate.id),
                    field_name="user_message_excerpt",
                    source_language=candidate.language,
                    requested_locale=locale,
                    source_text=candidate.user_message_excerpt,
                )
                or candidate.user_message_excerpt
            )
        summaries.append(
            DemoFaChatMemoryCandidateSummary(
                candidate_id=candidate.id,
                status=candidate.status,
                workflow_version=candidate.workflow_version,
                memory_type=candidate.memory_type,
                enrichment_status=candidate.enrichment_status,
                privacy_scope=candidate.privacy_scope,
                dispute_status=candidate.dispute_status,
                unresolved_clarification_count=candidate.unresolved_clarification_count,
                finalized_memory_text=localized_finalized_memory_text,
                user_message_excerpt=localized_user_message_excerpt,
                created_at=candidate.created_at,
                updated_at=candidate.updated_at,
                contributor_actor_id=contributor_actor_id,
                contributor_actor_role=contributor_actor_role,
                contributor_relationship_to_owner=contributor_relationship_to_owner,
                promotion_id=promotion.id if promotion is not None else None,
                promotion_status=promotion.promotion_status if promotion is not None else None,
                searchable_as_fact=bool(promotion and promotion.promotion_status == "indexed"),
            )
        )
    return summaries


def get_demo_memory_candidate_review_detail(
    db: Session,
    *,
    profile_id: int | None,
    candidate_id: int,
    actor: DemoFamilyActorContext | None = None,
    locale: str = "ru",
) -> DemoFaChatMemoryCandidateReviewDetail:
    """Aggregated review-detail read model (Task 64.5, Part M.32).

    Combines existing reads (candidate / enrichment / contributions /
    clarifications / promotion) and previews which owner-review / indexing
    actions are currently available, purely by projecting already-computed
    backend state. It does not re-implement or replace the real transition
    checks in ``family_memory_enrichment.service.owner_review`` or
    ``avatar_memory_indexing.service.index_promotion`` - those remain the
    sole source of truth and are re-validated independently on every call.
    """
    resolved_profile = _resolve_demo_profile(db, profile_id=profile_id, locale=locale)
    candidate = get_demo_memory_candidate(
        db,
        profile_id=profile_id,
        candidate_id=candidate_id,
        actor=actor,
    )
    candidate_read = _localize_candidate_review_read(
        db,
        candidate=build_memory_candidate_read(candidate),
        locale=locale,
    )

    enrichment = None
    contributions = []
    clarifications = []
    if candidate.workflow_version >= 2:
        enrichment = family_memory_enrichment_service.get_candidate_enrichment(
            db,
            owner_user_id=resolved_profile.user.id,
            candidate_id=candidate.id,
            actor=actor,
        )
        contributions = family_memory_enrichment_service.list_contributions(
            db,
            owner_user_id=resolved_profile.user.id,
            candidate_id=candidate.id,
            actor=actor,
        )
        clarifications = family_memory_enrichment_service.list_clarifications(
            db,
            owner_user_id=resolved_profile.user.id,
            candidate_id=candidate.id,
            actor=actor,
        )
        enrichment = _localize_enrichment_read(
            db,
            candidate_id=candidate.id,
            candidate_language=candidate.language,
            enrichment=enrichment,
            locale=locale,
        )
        contributions = [
            _localize_contribution_read(
                db,
                candidate_id=candidate.id,
                candidate_language=candidate.language,
                contribution=item,
                locale=locale,
            )
            for item in contributions
        ]
        clarifications = [
            _localize_clarification_read(
                db,
                candidate_id=candidate.id,
                candidate_language=candidate.language,
                clarification=item,
                locale=locale,
            )
            for item in clarifications
        ]

    promotion_row = candidate.avatar_memory_promotion
    promotion = build_avatar_memory_promotion_read(promotion_row) if promotion_row is not None else None

    is_owner_actor = actor is not None and family_memory_enrichment_service.is_demo_owner(actor)
    is_legacy = candidate.workflow_version < 2
    is_needs_review = candidate.status == "needs_review"
    enrichment_status = enrichment.enrichment_status.value if enrichment else candidate.enrichment_status
    dispute_status = enrichment.dispute_status.value if enrichment else candidate.dispute_status
    unresolved_count = enrichment.unresolved_clarification_count if enrichment else candidate.unresolved_clarification_count
    ready_for_owner_review = enrichment_status == "ready_for_owner_review" and unresolved_count == 0
    privacy_scope_value = enrichment.privacy_scope.value if enrichment else candidate.privacy_scope
    promotion_status_value = promotion.promotion_status.value if promotion else None

    can_confirm = (
        not is_legacy
        and is_owner_actor
        and is_needs_review
        and ready_for_owner_review
        and dispute_status != "disputed"
    )
    can_edit_and_confirm = not is_legacy and is_owner_actor and is_needs_review and ready_for_owner_review
    can_reject = not is_legacy and is_owner_actor and is_needs_review
    can_request_more_details = not is_legacy and is_owner_actor and is_needs_review
    can_mark_disputed = not is_legacy and is_owner_actor and is_needs_review
    can_approve_multiple_perspectives = (
        not is_legacy
        and is_owner_actor
        and is_needs_review
        and ready_for_owner_review
        and dispute_status == "disputed"
    )
    can_index = is_owner_actor and promotion_status_value == "pending_index"

    blocked_reasons: list[str] = []
    if is_legacy:
        blocked_reasons.append("legacy_workflow_not_supported_in_review_ui")
    if not is_owner_actor:
        blocked_reasons.append("actor_is_not_owner")
    if not is_legacy and not is_needs_review:
        blocked_reasons.append("candidate_review_already_terminal")
    if not is_legacy and is_needs_review and not ready_for_owner_review:
        blocked_reasons.append(
            "collecting_details" if enrichment_status == "collecting_details" else "not_ready_for_review"
        )
    if not is_legacy and dispute_status == "disputed":
        blocked_reasons.append("disputed")
    if promotion_status_value is None:
        blocked_reasons.append("not_promoted_yet")
    elif promotion_status_value != "pending_index":
        blocked_reasons.append(f"promotion_status_{promotion_status_value}")
    if privacy_scope_value not in {"all_family", "public_legacy"}:
        blocked_reasons.append("privacy_scope_not_indexable")

    translation_block_reason = family_memory_eligibility.get_finalized_memory_translation_block_reason(
        db, candidate=candidate
    )
    if translation_block_reason is not None:
        can_index = False
        blocked_reasons.append(translation_block_reason)

    translations = [
        MemoryContentTranslationRead.model_validate(row)
        for row in content_translation_service.get_translations_for_candidate(db, candidate_id=candidate.id)
    ]

    return DemoFaChatMemoryCandidateReviewDetail(
        candidate=candidate_read,
        enrichment=enrichment,
        contributions=contributions,
        clarifications=clarifications,
        promotion=promotion,
        is_owner_actor=is_owner_actor,
        can_confirm=can_confirm,
        can_edit_and_confirm=can_edit_and_confirm,
        can_reject=can_reject,
        can_request_more_details=can_request_more_details,
        can_mark_disputed=can_mark_disputed,
        can_approve_multiple_perspectives=can_approve_multiple_perspectives,
        can_index=can_index,
        blocked_reasons=blocked_reasons,
        requested_locale=locale if locale in {"cs", "ru", "en"} else "ru",
        source_language=candidate.language,
        translations=translations,
        translation_block_reason=translation_block_reason,
    )


def list_demo_memory_candidate_translations(
    db: Session,
    *,
    profile_id: int | None,
    candidate_id: int,
    actor: DemoFamilyActorContext | None = None,
) -> list[MemoryContentTranslationRead]:
    candidate = get_demo_memory_candidate(db, profile_id=profile_id, candidate_id=candidate_id, actor=actor)
    return [
        MemoryContentTranslationRead.model_validate(row)
        for row in content_translation_service.get_translations_for_candidate(db, candidate_id=candidate.id)
    ]


def retry_demo_memory_candidate_translation(
    db: Session,
    *,
    profile_id: int | None,
    candidate_id: int,
    target_language: str,
    actor: DemoFamilyActorContext | None = None,
) -> MemoryContentTranslationRead:
    """Explicit, owner-only retry of the candidate's finalized-memory translation.

    Idempotent in effect: re-running it when the source has not changed
    since the last successful translation simply reproduces the same
    current state (see content_translation.service.translate_content_field).
    Never approves the candidate and never triggers indexing.
    """
    if actor is None or not family_memory_enrichment_service.is_demo_owner(actor):
        raise family_memory_enrichment_service.FamilyMemoryAuthorizationError(
            "Only the avatar owner can retry a memory translation"
        )
    candidate = get_demo_memory_candidate(
        db, profile_id=profile_id, candidate_id=candidate_id, actor=actor, allow_enriched_internal=True
    )
    finalized_text = (candidate.finalized_memory_text or "").strip()
    if not finalized_text:
        raise DemoFaChatValidationError("Candidate has no finalized memory text to translate yet.")
    row = content_translation_service.retry_translation(
        db,
        entity_type="memory_candidate",
        entity_id=str(candidate.id),
        field_name=family_memory_eligibility.FINALIZED_MEMORY_FIELD_NAME,
        source_language=candidate.language or "cs",
        target_language=target_language,
        source_text=finalized_text,
        candidate_id=candidate.id,
        call_context=AiCallContext(
            feature=AiFeature.DYNAMIC_MEMORY_TRANSLATION,
            execution_source=ExecutionSource.FASTAPI,
            requested_locale=target_language,
            resolved_locale=target_language,
            memorial_id=profile_id,
        ),
    )
    return MemoryContentTranslationRead.model_validate(row)


def approve_demo_memory_candidate(
    db: Session,
    *,
    profile_id: int | None,
    candidate_id: int,
    payload: MemoryCandidateReviewUpdate | None,
):
    candidate = get_demo_memory_candidate(
        db,
        profile_id=profile_id,
        candidate_id=candidate_id,
        allow_enriched_internal=True,
    )
    if candidate.workflow_version >= 2:
        raise family_memory_enrichment_service.FamilyMemoryAuthorizationError(
            "Enriched candidates require the explicit owner-review endpoint"
        )
    approval_result = conversation_memory_candidates_service.approve_candidate(
        db,
        owner_user_id=candidate.owner_user_id,
        candidate_id=candidate.id,
        payload=payload,
    )
    observe_memory_candidate_reviewed(status=approval_result.candidate.status)
    if approval_result.promotion_created:
        observe_memory_promotion_created()
    observe_memory_promotion_status(status=approval_result.promotion.promotion_status)
    return approval_result


def reject_demo_memory_candidate(
    db: Session,
    *,
    profile_id: int | None,
    candidate_id: int,
    payload: MemoryCandidateReviewUpdate | None,
):
    candidate = get_demo_memory_candidate(
        db,
        profile_id=profile_id,
        candidate_id=candidate_id,
        allow_enriched_internal=True,
    )
    if candidate.workflow_version >= 2:
        raise family_memory_enrichment_service.FamilyMemoryAuthorizationError(
            "Enriched candidates require the explicit owner-review endpoint"
        )
    rejected_candidate = conversation_memory_candidates_service.reject_candidate(
        db,
        owner_user_id=candidate.owner_user_id,
        candidate_id=candidate.id,
        payload=payload,
    )
    observe_memory_candidate_reviewed(status=rejected_candidate.status)
    return rejected_candidate


def archive_demo_memory_candidate(
    db: Session,
    *,
    profile_id: int | None,
    candidate_id: int,
    payload: MemoryCandidateReviewUpdate | None,
):
    candidate = get_demo_memory_candidate(
        db,
        profile_id=profile_id,
        candidate_id=candidate_id,
        allow_enriched_internal=True,
    )
    if candidate.workflow_version >= 2:
        raise family_memory_enrichment_service.FamilyMemoryAuthorizationError(
            "Enriched candidates require the explicit owner-review endpoint"
        )
    archived_candidate = conversation_memory_candidates_service.archive_candidate(
        db,
        owner_user_id=candidate.owner_user_id,
        candidate_id=candidate.id,
        payload=payload,
    )
    observe_memory_candidate_reviewed(status=archived_candidate.status)
    return archived_candidate


def list_demo_memory_promotions(
    db: Session,
    *,
    profile_id: int | None,
    actor: DemoFamilyActorContext | None = None,
    locale: str = "ru",
):
    resolved_profile = _resolve_demo_profile(db, profile_id=profile_id, locale=locale)
    avatar_persona = _resolve_demo_avatar_persona()
    promotions = avatar_memory_promotions_service.list_promotions(
        db,
        owner_user_id=resolved_profile.user.id,
        profile_id=resolved_profile.profile.id,
        avatar_id=avatar_persona.avatar_id,
    )
    visible = []
    for promotion in promotions:
        if promotion.candidate.workflow_version < 2:
            visible.append(promotion)
            continue
        if actor is None:
            continue
        try:
            family_memory_enrichment_service.get_candidate_enrichment(
                db,
                owner_user_id=resolved_profile.user.id,
                candidate_id=promotion.candidate_id,
                actor=actor,
            )
        except family_memory_enrichment_service.FamilyMemoryNotFoundError:
            continue
        visible.append(promotion)
    return visible


def get_demo_memory_promotion(
    db: Session,
    *,
    profile_id: int | None,
    promotion_id: int,
    actor: DemoFamilyActorContext | None = None,
    allow_enriched_internal: bool = False,
    locale: str = "ru",
):
    resolved_profile = _resolve_demo_profile(db, profile_id=profile_id, locale=locale)
    avatar_persona = _resolve_demo_avatar_persona()
    promotion = avatar_memory_promotions_service.get_promotion(
        db,
        owner_user_id=resolved_profile.user.id,
        promotion_id=promotion_id,
    )
    if (
        promotion.profile_id != resolved_profile.profile.id
        or promotion.avatar_id != avatar_persona.avatar_id
    ):
        raise avatar_memory_promotions_service.AvatarMemoryPromotionNotFoundError(
            "Avatar memory promotion not found"
        )
    if promotion.candidate.workflow_version >= 2 and not allow_enriched_internal:
        if actor is None:
            raise family_memory_enrichment_service.FamilyMemoryNotFoundError(
                "Family memory promotion not found"
            )
        family_memory_enrichment_service.get_candidate_enrichment(
            db,
            owner_user_id=resolved_profile.user.id,
            candidate_id=promotion.candidate_id,
            actor=actor,
        )
    return promotion


def cancel_demo_memory_promotion(
    db: Session,
    *,
    profile_id: int | None,
    promotion_id: int,
    actor: DemoFamilyActorContext | None = None,
    locale: str = "ru",
):
    promotion = get_demo_memory_promotion(
        db,
        profile_id=profile_id,
        promotion_id=promotion_id,
        allow_enriched_internal=True,
        locale=locale,
    )
    if promotion.candidate.workflow_version >= 2:
        if actor is None or not family_memory_enrichment_service.is_demo_owner(actor):
            raise family_memory_enrichment_service.FamilyMemoryAuthorizationError(
                "Only the avatar owner can cancel an enriched memory promotion"
            )
    cancelled_promotion = avatar_memory_promotions_service.cancel_promotion(
        db,
        owner_user_id=promotion.owner_user_id,
        promotion_id=promotion.id,
    )
    observe_memory_promotion_status(status=cancelled_promotion.promotion_status)
    return cancelled_promotion


def index_demo_memory_promotion(
    db: Session,
    *,
    profile_id: int | None,
    promotion_id: int,
    actor: DemoFamilyActorContext | None = None,
    locale: str = "ru",
):
    promotion = get_demo_memory_promotion(
        db,
        profile_id=profile_id,
        promotion_id=promotion_id,
        allow_enriched_internal=True,
        locale=locale,
    )
    if promotion.candidate.workflow_version >= 2:
        if actor is None or not family_memory_enrichment_service.is_demo_owner(actor):
            raise family_memory_enrichment_service.FamilyMemoryAuthorizationError(
                "Only the avatar owner can index an enriched memory promotion"
            )
    return avatar_memory_indexing_service.index_promotion(
        db,
        owner_user_id=promotion.owner_user_id,
        promotion_id=promotion.id,
    )


def build_demo_memory_candidate_review_response(
    approval_result: conversation_memory_candidates_service.CandidateApprovalResult,
) -> DemoFaChatMemoryCandidateReviewResponse:
    promotion = build_avatar_memory_promotion_read(approval_result.promotion)
    return DemoFaChatMemoryCandidateReviewResponse(
        candidate_id=approval_result.candidate.id,
        owner_user_id=approval_result.candidate.owner_user_id,
        avatar_id=approval_result.candidate.avatar_id,
        profile_id=approval_result.candidate.profile_id,
        conversation_id=approval_result.candidate.conversation_id,
        trace_id=approval_result.candidate.trace_id,
        source=approval_result.candidate.source,
        status=approval_result.candidate.status,
        confidence=approval_result.candidate.confidence,
        user_message_excerpt=approval_result.candidate.user_message_excerpt,
        proposed_memory_text=approval_result.candidate.proposed_memory_text,
        reason=approval_result.candidate.reason,
        language=approval_result.candidate.language,
        created_at=approval_result.candidate.created_at,
        updated_at=approval_result.candidate.updated_at,
        reviewed_at=approval_result.candidate.reviewed_at,
        reviewed_by=approval_result.candidate.reviewed_by,
        review_note=approval_result.candidate.review_note,
        rejection_reason=approval_result.candidate.rejection_reason,
        memory_type=approval_result.candidate.memory_type,
        enrichment_status=approval_result.candidate.enrichment_status,
        finalized_memory_text=approval_result.candidate.finalized_memory_text,
        privacy_scope=approval_result.candidate.privacy_scope,
        dispute_status=approval_result.candidate.dispute_status,
        finalized_at=approval_result.candidate.finalized_at,
        finalized_by=approval_result.candidate.finalized_by,
        owner_reviewed_at=approval_result.candidate.owner_reviewed_at,
        owner_reviewed_by=approval_result.candidate.owner_reviewed_by,
        owner_review_actor_role=approval_result.candidate.owner_review_actor_role,
        unresolved_clarification_count=approval_result.candidate.unresolved_clarification_count,
        version=approval_result.candidate.version,
        workflow_version=approval_result.candidate.workflow_version,
        promotion_created=approval_result.promotion_created,
        promotion_id=promotion.promotion_id,
        promotion_status=promotion.promotion_status,
        searchable_as_fact=promotion.searchable_as_fact,
    )


def run_demo_fa_chat_message(
    db: Session,
    *,
    profile_id: int | None,
    message: str,
    debug: bool,
    trace_id: str,
    active_memory_candidate_id: int | None = None,
    actor_id: str | None = None,
    actor_role: str | None = None,
    relationship_to_owner: str | None = None,
    locale: str = "ru",
) -> DemoFaChatMessageResponse:
    """Run one FA-chat turn.

    Direct-locale bilingual architecture (Task 64.5.2, replacing the
    double-translation design from Task 64.5.1 Part E.22-23):
    ``normalized_message`` (the exact text the user typed, in whatever
    locale) is used, completely unmodified, for BGE-M3 retrieval, memory-
    query-intent classification, expanded-query building, and the Brain
    call - there is no query-translation call for either locale.
    ``response_language`` (equal to ``locale``) is passed to the Brain so it
    answers directly in natural Czech or Russian from whichever-language
    evidence BGE-M3's multilingual retrieval returns; there is no separate
    answer-translation call either. Total AI calls per chat turn: exactly
    one (the Brain), for both locales - see prompt_builder's
    ``RESPONSE LANGUAGE`` directive for how the Brain is instructed.

    Known limitation: ``classify_memory_query_intent``/``build_memory_candidate``
    (and their expansion-query sibling) are Russian-keyword-tuned heuristics.
    They now run directly against ``normalized_message`` for both locales
    (no more routing through a Russian translation), so on raw Czech text
    they may be less accurate at detecting corrected-memory/dispute intent
    and new-memory-candidate creation than on Russian text - see the
    "Known Limitations" note in PROJECT_PROGRESS.md for this task.
    """
    normalized_message = _normalize_message_text(message, locale=locale)
    message_hash_prefix = _build_message_hash_prefix(normalized_message)
    resolved_profile = _resolve_demo_profile(db, profile_id=profile_id, locale=locale)
    avatar_persona = _resolve_demo_avatar_persona()
    actor = (
        DemoFamilyActorContext(
            actor_id=actor_id,
            actor_role=actor_role,
            relationship_to_owner=relationship_to_owner,
        )
        if actor_id is not None and actor_role is not None
        else None
    )
    if active_memory_candidate_id is not None:
        if actor is None:
            raise DemoFaChatValidationError(
                "Для продолжения уточнения нужен явный контекст участника семьи."
            )
        candidate = family_memory_enrichment_service.repository.get_candidate(
            db,
            owner_user_id=resolved_profile.user.id,
            candidate_id=active_memory_candidate_id,
        )
        if (
            candidate is None
            or candidate.profile_id != resolved_profile.profile.id
            or candidate.avatar_id != avatar_persona.avatar_id
        ):
            raise family_memory_enrichment_service.FamilyMemoryNotFoundError(
                "Family memory candidate not found"
            )
        enrichment = family_memory_enrichment_service.answer_next_clarification(
            db,
            owner_user_id=resolved_profile.user.id,
            candidate_id=active_memory_candidate_id,
            payload=ClarificationAnswerRequest(
                actor_id=actor.actor_id,
                actor_role=actor.actor_role,
                relationship_to_owner=actor.relationship_to_owner,
                answer_text=normalized_message,
                trace_id=trace_id,
            ),
        )
        localized_next_question = _localize_clarification_question_for_locale(
            enrichment.next_clarification_question, locale=locale
        )
        draft_ready_message = _review_ready_message(locale)
        return DemoFaChatMessageResponse(
            answer=(
                localized_next_question.question_text
                if localized_next_question is not None
                else draft_ready_message
            ),
            locale=locale,
            lack_of_evidence=False,
            retrieval_used=False,
            persona_applied=False,
            guard_applied=False,
            trace_id=trace_id,
            memory_candidate=None,
            memory_candidate_persisted=True,
            active_memory_candidate_id=enrichment.candidate_id,
            enrichment_status=enrichment.enrichment_status,
            next_clarification_question=localized_next_question,
            evidence=[],
        )
    resolved_runtime = _resolve_demo_runtime(
        db,
        resolved_profile=resolved_profile,
        locale=locale,
    )
    log_event(
        logger,
        20,
        "fa_demo_chat_request",
        trace_id=trace_id,
        profile_id=resolved_profile.profile.id,
        collection_name=resolved_runtime.collection_name,
        retrieval_mode=resolved_runtime.retrieval_mode,
        retrieval_top_k=resolved_runtime.top_k,
        source_id=resolved_runtime.source_id,
        qdrant_point_count=resolved_runtime.point_count,
        message_length=len(normalized_message),
        message_hash_prefix=message_hash_prefix,
        debug=debug,
    )

    memory_query_intent = classify_memory_query_intent(normalized_message)
    observe_avatar_memory_query_intent(intent=memory_query_intent.value)
    expanded_retrieval_query = build_expanded_retrieval_query(normalized_message, memory_query_intent)

    retrieval_started_at = perf_counter()
    try:
        if expanded_retrieval_query is not None:
            # Corrected-memory intent: issue one additional, generic,
            # fact-agnostic retrieval probe (the original query above is
            # always issued too, unchanged) and merge deterministically. A
            # small, bounded candidate pool is over-fetched from both
            # queries — rather than the profile's normal top_k — so that
            # the dispute-shaped-evidence filter (applied below, same as
            # for ordinary turns) can drop an item that would be excluded
            # from the Brain's evidence anyway *before* truncating to the
            # real top_k, instead of after. Without this, a dispute-shaped
            # item could occupy one of only top_k raw slots purely to be
            # discarded downstream, crowding out a legitimate item that
            # would otherwise have ranked just below it. This only changes
            # retrieval for turns classified as corrected-memory intent in
            # the avatar learned-memory demo path; ordinary questions take
            # the single-query, unmodified-top_k branch below.
            pool_limit = resolved_runtime.top_k + _CORRECTED_MEMORY_CANDIDATE_POOL_OVERFETCH
            retrieval_response = retrieve_profile_rag(
                db,
                current_user=resolved_profile.user,
                profile_id=resolved_profile.profile.id,
                payload=RagRetrievalRequest(query=normalized_message, limit=pool_limit),
            )
            expansion_response = retrieve_profile_rag(
                db,
                current_user=resolved_profile.user,
                profile_id=resolved_profile.profile.id,
                payload=RagRetrievalRequest(query=expanded_retrieval_query, limit=pool_limit),
            )
            merged_pool = _merge_ranked_retrieval_results(
                primary=retrieval_response.results,
                secondary=expansion_response.results,
                limit=pool_limit,
            )
            filtered_pool = filter_learned_memory_results_by_question_intent(
                merged_pool,
                user_message=normalized_message,
            )
            # Deterministically float a verified learned memory to the front
            # and cap the evidence count for this intent path — reduces
            # dilution by unrelated archival items instead of relying only
            # on prompt wording to hold the Brain's attention (see
            # prioritize_corrected_memory_evidence docstring).
            prioritized_results = prioritize_corrected_memory_evidence(
                filtered_pool,
                limit=min(resolved_runtime.top_k, CORRECTED_MEMORY_EVIDENCE_CAP),
            )
            retrieval_response = retrieval_response.model_copy(update={"results": prioritized_results})
            observe_avatar_corrected_memory_resolution(
                resolved=any(
                    result.source_type == "conversation_candidate"
                    and (result.payload_metadata or {}).get("memory_status") == "verified"
                    for result in prioritized_results
                )
            )
        else:
            retrieval_response = retrieve_profile_rag(
                db,
                current_user=resolved_profile.user,
                profile_id=resolved_profile.profile.id,
                payload=RagRetrievalRequest(query=normalized_message),
            )
    except Exception:
        observe_rag_retrieval_error(
            retrieval_mode=resolved_runtime.retrieval_mode,
            top_k=resolved_runtime.top_k,
        )
        raise

    observe_rag_retrieval_success(
        retrieval_mode=resolved_runtime.retrieval_mode,
        top_k=resolved_runtime.top_k,
        duration_seconds=perf_counter() - retrieval_started_at,
        retrieved_chunk_count=len(retrieval_response.results),
    )
    log_event(
        logger,
        20,
        "fa_demo_chat_memory_query_intent",
        trace_id=trace_id,
        profile_id=resolved_profile.profile.id,
        memory_query_intent=memory_query_intent.value,
        normalization_applied=expanded_retrieval_query is not None,
        normalized_query_hash=(
            build_text_hash(expanded_retrieval_query).split(":", 1)[1][:8]
            if expanded_retrieval_query is not None
            else None
        ),
        normalization_rule_id=(
            CORRECTED_MEMORY_EXPANSION_RULE_ID if expanded_retrieval_query is not None else None
        ),
    )
    log_event(
        logger,
        20,
        "fa_demo_chat_retrieval",
        trace_id=trace_id,
        profile_id=resolved_profile.profile.id,
        collection_name=(
            retrieval_response.results[0].qdrant_collection
            if retrieval_response.results
            else resolved_runtime.collection_name
        ),
        retrieval_top_k=resolved_runtime.top_k,
        retrieved_chunk_count=len(retrieval_response.results),
        top_chunk_ids=[str(result.chunk_id) for result in retrieval_response.results[:5]],
        top_source_titles=[result.source_title for result in retrieval_response.results[:3] if result.source_title],
        top_text_hash_prefixes=[result.text_hash[:12] for result in retrieval_response.results[:5]],
    )
    evidence_source_results = filter_learned_memory_results_by_question_intent(
        retrieval_response.results,
        user_message=normalized_message,
    )
    retrieved_evidence_items = build_rag_evidence_items(evidence_source_results)
    grounded_context = build_vector_retrieval_grounded_context(
        profile=resolved_profile.profile,
        retrieved_evidence_items=retrieved_evidence_items,
    )

    orchestrator = get_agent_orchestrator()
    ai_call_context = AiCallContext(
        feature=AiFeature.BRAIN_CHAT_RESPONSE,
        execution_source=ExecutionSource.FASTAPI,
        trace_id=trace_id,
        requested_locale=locale,
        resolved_locale=locale,
        memorial_id=resolved_profile.profile.id,
    )
    orchestrator_response, _ai_action = run_instrumented_single_attempt_action(
        db,
        context=ai_call_context,
        step_type=AiStepType.PROVIDER_GENERATION,
        provider=app_settings.ai_brain_provider,
        model=app_settings.ai_brain_model,
        operation=lambda: orchestrator.generate_chat_response(
            OrchestratorChatRequest(
                profile=_build_profile_context(resolved_profile.profile),
                avatar_persona=avatar_persona,
                user_message=normalized_message,
                recent_history=[],
                grounded_context=grounded_context,
                # Direct-locale architecture (Task 64.5.2): the Brain receives the
                # ORIGINAL untranslated user_message above plus this explicit
                # response_language, and answers directly in that language - no
                # separate query-translation or answer-translation call. See
                # prompt_builder._build_response_language_directive.
                response_language=locale,
            )
        ),
        extract_token_usage=lambda resp: normalize_openai_compatible_usage(
            raw_response={
                "id": (resp.metadata or {}).get("provider_request_id"),
                "usage": (resp.metadata or {}).get("usage"),
            }
        ),
    )
    metadata = dict(orchestrator_response.metadata)
    persona_applied = bool(metadata.get("persona_applied", True))
    lack_of_evidence = bool(metadata.get("output_guard_lack_of_evidence")) or (
        str(metadata.get("grounding_status") or "").strip().lower() == "no_evidence"
    )
    # Known limitation (Task 64.5.2): these detection/classification
    # heuristics (avatar_persona.build_memory_candidate /
    # classify_memory_query_intent / build_expanded_retrieval_query above)
    # are Russian-keyword-tuned. They now run directly against
    # normalized_message for BOTH locales (no more indirection through a
    # Russian translation) - on raw Czech text they may be less accurate at
    # detecting corrected-memory/dispute intent or a new memory candidate
    # than on Russian text. This is an accepted v1 tradeoff to keep the
    # architecture to exactly one AI call per chat turn; a narrow
    # Czech-keyword extension is a documented follow-up if evaluation shows
    # it is needed (see PROJECT_PROGRESS.md Known Limitations).
    extracted_memory_candidate = build_memory_candidate(
        user_message=normalized_message,
        lack_of_evidence=lack_of_evidence,
    )
    persisted_memory_candidate = None
    candidate_enrichment: CandidateEnrichmentRead | None = None
    memory_candidate_persisted: bool | None = None
    if extracted_memory_candidate is not None:
        try:
            persisted_memory_candidate = _persist_memory_candidate(
                db,
                owner_user_id=resolved_profile.user.id,
                avatar_id=avatar_persona.avatar_id,
                profile_id=resolved_profile.profile.id,
                trace_id=trace_id,
                # The candidate's source language must reflect the language the
                # user actually typed in (locale), not the persona's own
                # response language, so the bilingual translation gate above
                # (family_memory_enrichment.eligibility) is triggered correctly
                # for Czech-origin chat-created candidates.
                language=locale,
                extracted_candidate=extracted_memory_candidate,
                enrichment_enabled=actor is not None,
            )
            if actor is not None:
                candidate_enrichment = family_memory_enrichment_service.initialize_candidate(
                    db,
                    owner_user_id=resolved_profile.user.id,
                    candidate_id=persisted_memory_candidate.id,
                    actor=actor,
                    initial_text=normalized_message,
                    trace_id=trace_id,
                    classification_hint_text=normalized_message,
                )
            memory_candidate_persisted = True
        except Exception as exc:
            db.rollback()
            persisted_memory_candidate = None
            candidate_enrichment = None
            memory_candidate_persisted = False
            log_event(
                logger,
                40,
                "fa_demo_chat_memory_candidate_persist_failed",
                trace_id=trace_id,
                avatar_id=avatar_persona.avatar_id,
                profile_id=resolved_profile.profile.id,
                candidate_created=True,
                candidate_persisted=False,
                candidate_status=MemoryCandidateStatus.NEEDS_REVIEW.value,
                error_type=exc.__class__.__name__,
            )
        observe_memory_candidate_created(
            persisted=bool(memory_candidate_persisted),
            status=MemoryCandidateStatus.NEEDS_REVIEW.value,
        )
    response_directives = derive_avatar_response_directives(
        persona=avatar_persona,
        user_message=normalized_message,
        lack_of_evidence=lack_of_evidence,
    )

    log_event(
        logger,
        20,
        "fa_demo_chat_response",
        trace_id=trace_id,
        profile_id=resolved_profile.profile.id,
        retrieval_used=bool(retrieval_response.results),
        persona_applied=persona_applied,
        guard_applied=bool(metadata.get("output_guard_applied")),
        guard_reason=metadata.get("output_guard_reason"),
        lack_of_evidence=lack_of_evidence,
        memory_candidate_created=extracted_memory_candidate is not None,
        memory_candidate_persisted=memory_candidate_persisted,
        candidate_id=persisted_memory_candidate.id if persisted_memory_candidate is not None else None,
        candidate_status=(
            persisted_memory_candidate.status
            if persisted_memory_candidate is not None
            else (
                MemoryCandidateStatus.NEEDS_REVIEW.value
                if extracted_memory_candidate is not None
                else None
            )
        ),
        emotion_primary=response_directives.emotion.primary,
    )
    response_answer = orchestrator_response.text
    localized_next_question_for_response = _localize_clarification_question_for_locale(
        candidate_enrichment.next_clarification_question if candidate_enrichment is not None else None,
        locale=locale,
    )
    if candidate_enrichment is not None:
        if localized_next_question_for_response is not None:
            response_answer = localized_next_question_for_response.question_text
        elif candidate_enrichment.enrichment_status == EnrichmentStatus.READY_FOR_OWNER_REVIEW:
            response_answer = _review_ready_message(locale)
    # Ordinary grounded/lack-of-evidence answer: orchestrator_response.text is
    # final as-is. The Brain answered directly in `locale` (via
    # response_language above) - there is no separate answer-translation call
    # for either locale (Task 64.5.2, replacing the Task 64.5.1 double-
    # translation design).
    return DemoFaChatMessageResponse(
        answer=response_answer,
        locale=locale,
        lack_of_evidence=lack_of_evidence,
        retrieval_used=bool(retrieval_response.results),
        persona_applied=persona_applied,
        guard_applied=bool(metadata.get("output_guard_applied")),
        guard_reason=(
            str(metadata.get("output_guard_reason"))
            if metadata.get("output_guard_reason") is not None
            else None
        ),
        trace_id=trace_id,
        memory_candidate=(
            _build_demo_memory_candidate(
                extracted_candidate=extracted_memory_candidate,
                persisted_candidate=persisted_memory_candidate,
                enrichment=candidate_enrichment,
            )
            if extracted_memory_candidate is not None
            else None
        ),
        memory_candidate_persisted=memory_candidate_persisted,
        active_memory_candidate_id=(
            candidate_enrichment.candidate_id if candidate_enrichment is not None else None
        ),
        enrichment_status=(
            candidate_enrichment.enrichment_status if candidate_enrichment is not None else None
        ),
        next_clarification_question=localized_next_question_for_response,
        emotion=response_directives.emotion,
        face_directives=response_directives.face_directives,
        voice_directives=response_directives.voice_directives,
        evidence=_build_evidence_items(evidence_source_results, debug=debug),
    )
