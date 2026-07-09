from __future__ import annotations

from collections.abc import Callable, Sequence

from app.modules.ai_agents.brain.context import BrainGroundedContext, BrainMemoryEvidence, BrainProfileContext, BrainRagEvidence
from app.modules.ai_agents.brain.output_guard import BrainOutputGuardContext
from app.modules.ai_agents.brain.service import BrainAgentService, get_brain_service
from app.modules.ai_agents.schemas import BrainAgentResponse, MemoryProfileContext, OrchestratorChatRequest
from app.modules.rag_evaluation.evaluator import evaluate_answer_against_case
from app.modules.rag_evaluation.exceptions import RagEvaluationCaseExecutionError
from app.modules.rag_evaluation.schemas import (
    RagEvaluationCase,
    RagEvaluationCaseResult,
    RagEvaluationMemoryEvidenceSetup,
    RagEvaluationProfileSetup,
    RagEvaluationRetrievedEvidenceSetup,
    RagEvaluationSuiteResult,
)


RagEvaluationAnswerGenerator = Callable[[RagEvaluationCase, OrchestratorChatRequest], BrainAgentResponse]


def _build_profile_context(profile: RagEvaluationProfileSetup) -> BrainProfileContext:
    return BrainProfileContext(
        profile_id=profile.profile_id,
        name=profile.name,
        birth_date=profile.birth_date,
        death_date=profile.death_date,
        biography=profile.biography,
        personality=profile.personality,
        catchphrases=profile.catchphrases,
    )


def _build_memory_profile(profile: RagEvaluationProfileSetup) -> MemoryProfileContext:
    return MemoryProfileContext(
        id=profile.profile_id,
        name=profile.name,
        birth_date=profile.birth_date,
        death_date=profile.death_date,
        biography=profile.biography,
        personality=profile.personality,
        catchphrases=profile.catchphrases,
        is_public=False,
    )


def _build_memory_evidence(
    items: Sequence[RagEvaluationMemoryEvidenceSetup],
) -> list[BrainMemoryEvidence]:
    return [
        BrainMemoryEvidence(
            source_id=item.source_id,
            title=item.title,
            memory_type=item.memory_type,
            occurred_at=item.occurred_at,
            occurred_year=item.occurred_year,
            content_preview=item.content_preview,
            selection_reason=item.selection_reason,
        )
        for item in items
    ]


def _build_retrieved_evidence(
    items: Sequence[RagEvaluationRetrievedEvidenceSetup],
) -> list[BrainRagEvidence]:
    return [
        BrainRagEvidence(
            chunk_id=item.chunk_id,
            source_id=item.source_id,
            embedding_id=item.embedding_id,
            score=item.score,
            language=item.language,
            source_document_type=item.source_document_type,
            validation_status=item.validation_status,
            text_hash=item.text_hash,
            content_preview=item.content_preview,
        )
        for item in items
    ]


class RagEvaluationService:
    def __init__(self, brain_service: BrainAgentService | None = None) -> None:
        self.brain_service = brain_service or get_brain_service()

    def build_chat_request(self, case: RagEvaluationCase) -> OrchestratorChatRequest:
        grounded_context = BrainGroundedContext(
            profile_context=_build_profile_context(case.profile),
            evidence_items=_build_memory_evidence(case.memory_evidence_items),
            retrieved_evidence_items=_build_retrieved_evidence(case.retrieved_evidence_items),
        )
        return OrchestratorChatRequest(
            profile=_build_memory_profile(case.profile),
            user_message=case.user_query,
            recent_history=case.recent_history,
            grounded_context=grounded_context,
            output_guard_context=BrainOutputGuardContext(
                expected_behavior=case.expected_behavior,
                forbidden_claims=tuple(case.forbidden_claims),
                should_require_lack_of_evidence=case.should_require_lack_of_evidence,
            ),
        )

    def run_eval_case(
        self,
        case: RagEvaluationCase,
        *,
        answer_generator: RagEvaluationAnswerGenerator | None = None,
    ) -> RagEvaluationCaseResult:
        request = self.build_chat_request(case)
        response = (
            answer_generator(case, request)
            if answer_generator is not None
            else self.brain_service.generate_chat_response(request)
        )
        if not isinstance(response, BrainAgentResponse):
            raise RagEvaluationCaseExecutionError("Evaluation answer generator returned an invalid response")

        grounded_context = request.grounded_context
        evidence_count = 0
        if grounded_context is not None:
            evidence_count = len(grounded_context.evidence_items) + len(grounded_context.retrieved_evidence_items)

        return evaluate_answer_against_case(
            case=case,
            answer_text=response.text,
            provider_name=response.provider_name,
            response_metadata=response.metadata,
            evidence_count=evidence_count,
        )

    def run_eval_suite(
        self,
        cases: Sequence[RagEvaluationCase],
        *,
        answer_generator: RagEvaluationAnswerGenerator | None = None,
    ) -> RagEvaluationSuiteResult:
        results = [
            self.run_eval_case(case, answer_generator=answer_generator)
            for case in cases
        ]
        passed_cases = sum(1 for result in results if result.passed)
        failed_cases = len(results) - passed_cases
        return RagEvaluationSuiteResult(
            total_cases=len(results),
            passed_cases=passed_cases,
            failed_cases=failed_cases,
            results=results,
        )
