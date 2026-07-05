from app.db.models import RagEmbedding
from app.db.session import get_db
from app.main import app
from app.modules.ai_agents.brain.providers.mock import MockBrainAgentProvider
from app.modules.ai_agents.brain.service import BrainAgentService
from app.modules.ai_agents.schemas import BrainAgentResponse
from app.modules.rag_evaluation.cases import (
    ALL_RAG_EVALUATION_CASES,
    ETERNAL_WORLD_RAG_EVALUATION_CASES,
    FOUNDATION_RAG_EVALUATION_CASES,
)
from app.modules.rag_evaluation.evaluator import detect_actual_behavior, evaluate_answer_against_case
from app.modules.rag_evaluation.service import RagEvaluationService
from app.modules.rag_evaluation.schemas import (
    RagEvaluationCase,
    RagEvaluationMemoryEvidenceSetup,
    RagEvaluationProfileSetup,
    RagEvaluationRetrievedEvidenceSetup,
)


def _get_test_db_session():
    override = app.dependency_overrides[get_db]
    session_generator = override()
    db = next(session_generator)
    return db, session_generator


def _build_grounded_case() -> RagEvaluationCase:
    return RagEvaluationCase(
        case_id="grounded-pass",
        title="Grounded answer includes expected evidence markers",
        profile=RagEvaluationProfileSetup(
            profile_id=1,
            name="Eva",
            biography="A retired teacher from Brno.",
        ),
        memory_evidence_items=[
            RagEvaluationMemoryEvidenceSetup(
                source_id=10,
                title="Childhood home",
                content_preview="Eva grew up in Brno near the old station.",
                memory_type="text",
                selection_reason="eval_fixture_memory",
                occurred_year=1974,
            )
        ],
        retrieved_evidence_items=[
            RagEvaluationRetrievedEvidenceSetup(
                chunk_id=20,
                source_id=30,
                embedding_id=40,
                text_hash="hash-20",
                content_preview="An archival page states Eva later worked as a literature teacher.",
                source_document_type="biography",
                validation_status="valid",
            )
        ],
        user_query="Tell me about where I grew up and what I did for work.",
        expected_behavior="grounded_answer",
        expected_evidence_markers=["Brno", "literature teacher"],
        minimum_required_evidence_count=2,
    )


def test_eval_case_with_evidence_passes_when_answer_uses_evidence():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    case = _build_grounded_case()

    result = service.run_eval_case(
        case,
        answer_generator=lambda case, request: BrainAgentResponse(
            text="You grew up in Brno and later worked as a literature teacher.",
            provider_name="mock-eval",
            metadata={"grounding_status": "grounded"},
        ),
    )

    assert result.passed is True
    assert result.actual_behavior == "grounded_answer"
    assert result.evidence_count == 2
    assert result.missing_expected_markers == []
    assert result.forbidden_claims_found == []


def test_eval_case_fails_when_expected_evidence_marker_is_missing():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    case = _build_grounded_case()

    result = service.run_eval_case(
        case,
        answer_generator=lambda case, request: BrainAgentResponse(
            text="You grew up in Brno.",
            provider_name="mock-eval",
            metadata={"grounding_status": "grounded"},
        ),
    )

    assert result.passed is False
    assert result.missing_expected_markers == ["literature teacher"]
    assert any("missing expected evidence markers" in reason.lower() for reason in result.reasons)


def test_eval_case_fails_when_forbidden_unsupported_claim_appears():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    case = _build_grounded_case().model_copy(update={"forbidden_claims": ["moved to Paris"]})

    result = service.run_eval_case(
        case,
        answer_generator=lambda case, request: BrainAgentResponse(
            text="You grew up in Brno, worked as a literature teacher, and later moved to Paris.",
            provider_name="mock-eval",
            metadata={"grounding_status": "grounded"},
        ),
    )

    assert result.passed is False
    assert result.forbidden_claims_found == ["moved to Paris"]
    assert any("forbidden unsupported claims" in reason.lower() for reason in result.reasons)


def test_lack_of_evidence_eval_passes_with_mock_brain_provider():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    case = FOUNDATION_RAG_EVALUATION_CASES[1]

    result = service.run_eval_case(case)

    assert result.passed is True
    assert result.actual_behavior == "lack_of_evidence"
    assert result.provider_name == "mock"
    assert "not available in the stored memories/context" in result.answer_preview.lower()


def test_lack_of_evidence_eval_fails_when_answer_invents_unsupported_facts():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    case = FOUNDATION_RAG_EVALUATION_CASES[1].model_copy(update={"forbidden_claims": ["born in Paris"]})

    result = service.run_eval_case(
        case,
        answer_generator=lambda case, request: BrainAgentResponse(
            text="You were born in Paris in 1942.",
            provider_name="mock-eval",
            metadata={"grounding_status": "grounded"},
        ),
    )

    assert result.passed is False
    assert result.actual_behavior == "grounded_answer"
    assert result.forbidden_claims_found == ["born in Paris"]
    assert any("lack-of-evidence" in reason.lower() for reason in result.reasons)


def test_rag_evaluation_harness_does_not_call_real_external_ai_apis(monkeypatch):
    from app.modules.ai_agents.brain.providers import openai_compatible

    def fail_http_client(*args, **kwargs):
        raise AssertionError("External AI HTTP client should not be created for RAG evaluation tests")

    monkeypatch.setattr(openai_compatible.httpx, "Client", fail_http_client)
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))

    result = service.run_eval_case(FOUNDATION_RAG_EVALUATION_CASES[1])

    assert result.passed is True
    assert result.provider_name == "mock"


def test_rag_evaluation_harness_does_not_create_stored_query_embeddings(client):
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    db, session_generator = _get_test_db_session()
    embeddings_before = db.query(RagEmbedding).count()

    try:
        result = service.run_eval_case(FOUNDATION_RAG_EVALUATION_CASES[1])
        embeddings_after = db.query(RagEmbedding).count()
    finally:
        session_generator.close()

    assert result.passed is True
    assert embeddings_before == 0
    assert embeddings_after == 0


def test_run_eval_suite_returns_summary_counts():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    grounded_case = _build_grounded_case()
    no_evidence_case = FOUNDATION_RAG_EVALUATION_CASES[1]

    def answer_generator(case, request):
        if case.case_id == grounded_case.case_id:
            return BrainAgentResponse(
                text="You grew up in Brno and later worked as a literature teacher.",
                provider_name="mock-eval",
                metadata={"grounding_status": "grounded"},
            )
        return BrainAgentResponse(
            text="You were born in Paris.",
            provider_name="mock-eval",
            metadata={"grounding_status": "grounded"},
        )

    suite_result = service.run_eval_suite(
        [grounded_case, no_evidence_case],
        answer_generator=answer_generator,
    )

    assert suite_result.total_cases == 2
    assert suite_result.passed_cases == 1
    assert suite_result.failed_cases == 1
    assert [result.case_id for result in suite_result.results] == [
        grounded_case.case_id,
        no_evidence_case.case_id,
    ]


def test_eternal_world_eval_cases_pass_with_grounded_mock_brain():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))

    suite_result = service.run_eval_suite(ALL_RAG_EVALUATION_CASES)

    assert suite_result.total_cases == len(ALL_RAG_EVALUATION_CASES)
    assert suite_result.failed_cases == 0
    assert suite_result.passed_cases == suite_result.total_cases


def test_foundation_grounded_case_passes_with_mock_brain_using_evidence_citations():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    case = FOUNDATION_RAG_EVALUATION_CASES[0]

    result = service.run_eval_case(case)

    assert result.passed is True
    assert result.actual_behavior == "grounded_answer"
    assert "Brno" in result.answer_preview
    assert "[rag:501]" in result.answer_preview or "[memory:101]" in result.answer_preview


def test_eternal_world_eval_case_count_is_at_least_eight():
    assert len(ETERNAL_WORLD_RAG_EVALUATION_CASES) >= 7
    assert len(ALL_RAG_EVALUATION_CASES) >= 9


def test_hedged_but_substantively_grounded_answer_counts_as_grounded():
    combined_case = next(
        case
        for case in ETERNAL_WORLD_RAG_EVALUATION_CASES
        if case.case_id == "combined-memory-and-rag-grounding"
    )
    deepseek_style_answer = (
        "Based on the available evidence, Eva worked as a literature teacher in Brno. "
        "This is confirmed by both a personal memory [memory:111] and an archival document [rag:704]."
    )

    result = evaluate_answer_against_case(
        case=combined_case,
        answer_text=deepseek_style_answer,
        provider_name="openai_compatible",
        response_metadata={"grounding_status": "grounded"},
        evidence_count=2,
    )

    assert result.passed is True
    assert result.actual_behavior == "grounded_answer"


def test_uncertainty_phrase_without_markers_or_citations_stays_partial():
    combined_case = next(
        case
        for case in ETERNAL_WORLD_RAG_EVALUATION_CASES
        if case.case_id == "combined-memory-and-rag-grounding"
    )
    uncertain_answer = "Based on the available evidence, I am not sure about her work."

    behavior = detect_actual_behavior(
        answer_text=uncertain_answer,
        response_metadata={"grounding_status": "grounded"},
        expected_evidence_markers=combined_case.expected_evidence_markers,
    )

    assert behavior == "partial_answer_with_uncertainty"

    result = evaluate_answer_against_case(
        case=combined_case,
        answer_text=uncertain_answer,
        provider_name="openai_compatible",
        response_metadata={"grounding_status": "grounded"},
        evidence_count=2,
    )

    assert result.passed is False
    assert result.actual_behavior == "partial_answer_with_uncertainty"
