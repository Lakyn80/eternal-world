from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

from sqlalchemy.orm import Session

from app.core.logging import get_logger, log_event
from app.core.metrics import (
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
from app.modules.ai_agents.brain.context import build_rag_evidence_items, build_vector_retrieval_grounded_context
from app.modules.ai_agents.schemas import MemoryProfileContext, OrchestratorChatRequest
from app.modules.avatar_persona import (
    build_memory_candidate,
    derive_avatar_response_directives,
    load_demo_avatar_persona,
)
from app.modules.avatar_memory_promotions import service as avatar_memory_promotions_service
from app.modules.avatar_memory_indexing import service as avatar_memory_indexing_service
from app.modules.avatar_memory_promotions.schemas import build_avatar_memory_promotion_read
from app.modules.conversation_memory_candidates import service as conversation_memory_candidates_service
from app.modules.conversation_memory_candidates.schemas import (
    MemoryCandidateCreate,
    MemoryCandidateReviewUpdate,
    MemoryCandidateStatus,
)
from app.modules.family_memory_enrichment import service as family_memory_enrichment_service
from app.modules.family_memory_enrichment.enums import EnrichmentStatus, PrivacyScope
from app.modules.family_memory_enrichment.schemas import (
    CandidateEnrichmentRead,
    ClarificationAnswerRequest,
    DemoFamilyActorContext,
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
    DemoFaChatMemoryCandidateReviewResponse,
    DemoFaChatMessageResponse,
)


DEMO_FA_CHAT_MESSAGE_MAX_LENGTH = 4000
DEMO_FA_CHAT_EVIDENCE_PREVIEW_LENGTH = 220
DEMO_FA_CHAT_PROFILE_UNAVAILABLE_DETAIL = "Тестовый профиль аватара сейчас недоступен."
DEMO_FA_CHAT_NOT_INITIALIZED_DETAIL = (
    "Демо-профиль ещё не инициализирован. Пожалуйста, запустите подготовку тестовой памяти."
)
DEMO_FA_CHAT_EMBEDDING_UNAVAILABLE_DETAIL = (
    "Демо временно недоступно: модель эмбеддингов BGE-M3 не инициализирована. "
    "Запустите подготовку модели и повторите запрос."
)
DEMO_FA_CHAT_INTERNAL_ERROR_DETAIL = "Не удалось получить ответ аватара. Попробуйте ещё раз."

logger = get_logger("demo_fa_chat")


class DemoFaChatValidationError(Exception):
    pass


class DemoFaChatProfileUnavailableError(Exception):
    pass


class DemoFaChatInitializationError(Exception):
    pass


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


def _normalize_message_text(value: str) -> str:
    normalized_value = value.strip()
    if not normalized_value:
        raise DemoFaChatValidationError("Сообщение не должно быть пустым.")
    if len(normalized_value) > DEMO_FA_CHAT_MESSAGE_MAX_LENGTH:
        raise DemoFaChatValidationError("Сообщение слишком длинное для демо-чата.")
    return normalized_value


def _build_message_hash_prefix(message: str) -> str:
    return build_text_hash(message).split(":", 1)[1][:8]


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
) -> DemoFaChatResolvedProfile:
    user = get_user_by_email(db, FAMILY_AVATAR_RU_E2E_EMAIL)
    if user is None:
        raise DemoFaChatProfileUnavailableError(DEMO_FA_CHAT_PROFILE_UNAVAILABLE_DETAIL)

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
        raise DemoFaChatProfileUnavailableError(DEMO_FA_CHAT_PROFILE_UNAVAILABLE_DETAIL)

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


def _assert_embedding_runtime_ready(*, model_code: str, collection_name: str) -> None:
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
        raise DemoFaChatInitializationError(DEMO_FA_CHAT_EMBEDDING_UNAVAILABLE_DETAIL)


def _resolve_demo_runtime(
    db: Session,
    *,
    resolved_profile: DemoFaChatResolvedProfile,
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
        raise DemoFaChatInitializationError(DEMO_FA_CHAT_NOT_INITIALIZED_DETAIL) from exc

    if (
        active_config.model_code != recommendation.model_code
        or active_config.collection_name != expected_collection_name
        or active_config.retrieval_mode != recommendation.retrieval_mode
    ):
        raise DemoFaChatInitializationError(DEMO_FA_CHAT_NOT_INITIALIZED_DETAIL)

    _assert_embedding_runtime_ready(
        model_code=active_config.model_code,
        collection_name=active_config.collection_name,
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
        raise DemoFaChatInitializationError(DEMO_FA_CHAT_NOT_INITIALIZED_DETAIL)

    qdrant_point_count = build_qdrant_client().count_points(
        collection_name=active_config.collection_name,
        search_filter=_build_qdrant_demo_source_filter(
            owner_user_id=resolved_profile.user.id,
            profile_id=resolved_profile.profile.id,
            source_id=source.id,
        ),
    )
    if qdrant_point_count <= 0:
        raise DemoFaChatInitializationError(DEMO_FA_CHAT_NOT_INITIALIZED_DETAIL)

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
):
    resolved_profile = _resolve_demo_profile(db, profile_id=profile_id)
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
):
    resolved_profile = _resolve_demo_profile(db, profile_id=profile_id)
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
):
    resolved_profile = _resolve_demo_profile(db, profile_id=profile_id)
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
):
    resolved_profile = _resolve_demo_profile(db, profile_id=profile_id)
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
):
    promotion = get_demo_memory_promotion(
        db,
        profile_id=profile_id,
        promotion_id=promotion_id,
        allow_enriched_internal=True,
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
):
    promotion = get_demo_memory_promotion(
        db,
        profile_id=profile_id,
        promotion_id=promotion_id,
        allow_enriched_internal=True,
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
) -> DemoFaChatMessageResponse:
    normalized_message = _normalize_message_text(message)
    message_hash_prefix = _build_message_hash_prefix(normalized_message)
    resolved_profile = _resolve_demo_profile(db, profile_id=profile_id)
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
        next_question = enrichment.next_clarification_question
        return DemoFaChatMessageResponse(
            answer=(
                next_question.question_text
                if next_question is not None
                else "Спасибо. Черновик воспоминания готов к проверке владельцем аватара."
            ),
            lack_of_evidence=False,
            retrieval_used=False,
            persona_applied=False,
            guard_applied=False,
            trace_id=trace_id,
            memory_candidate=None,
            memory_candidate_persisted=True,
            active_memory_candidate_id=enrichment.candidate_id,
            enrichment_status=enrichment.enrichment_status,
            next_clarification_question=next_question,
            evidence=[],
        )
    resolved_runtime = _resolve_demo_runtime(
        db,
        resolved_profile=resolved_profile,
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

    retrieval_started_at = perf_counter()
    try:
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
    retrieved_evidence_items = build_rag_evidence_items(retrieval_response.results)
    grounded_context = build_vector_retrieval_grounded_context(
        profile=resolved_profile.profile,
        retrieved_evidence_items=retrieved_evidence_items,
    )

    orchestrator = get_agent_orchestrator()
    orchestrator_response = orchestrator.generate_chat_response(
        OrchestratorChatRequest(
            profile=_build_profile_context(resolved_profile.profile),
            avatar_persona=avatar_persona,
            user_message=normalized_message,
            recent_history=[],
            grounded_context=grounded_context,
        )
    )
    metadata = dict(orchestrator_response.metadata)
    persona_applied = bool(metadata.get("persona_applied", True))
    lack_of_evidence = bool(metadata.get("output_guard_lack_of_evidence")) or (
        str(metadata.get("grounding_status") or "").strip().lower() == "no_evidence"
    )
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
                language=avatar_persona.language,
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
    if candidate_enrichment is not None:
        if candidate_enrichment.next_clarification_question is not None:
            response_answer = candidate_enrichment.next_clarification_question.question_text
        elif candidate_enrichment.enrichment_status == EnrichmentStatus.READY_FOR_OWNER_REVIEW:
            response_answer = "Спасибо. Черновик воспоминания готов к проверке владельцем аватара."
    return DemoFaChatMessageResponse(
        answer=response_answer,
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
        next_clarification_question=(
            candidate_enrichment.next_clarification_question
            if candidate_enrichment is not None
            else None
        ),
        emotion=response_directives.emotion,
        face_directives=response_directives.face_directives,
        voice_directives=response_directives.voice_directives,
        evidence=_build_evidence_items(retrieval_response.results, debug=debug),
    )
