from __future__ import annotations

from app.modules.rag_evaluation.schemas import (
    RagEvaluationCase,
    RagEvaluationMemoryEvidenceSetup,
    RagEvaluationProfileSetup,
    RagEvaluationRetrievedEvidenceSetup,
)


FOUNDATION_RAG_EVALUATION_CASES: tuple[RagEvaluationCase, ...] = (
    RagEvaluationCase(
        case_id="grounded-context-available",
        title="Grounded answer when verified evidence exists",
        profile=RagEvaluationProfileSetup(
            profile_id=1,
            name="Alya",
            biography="A careful family historian.",
            personality="Warm and factual.",
        ),
        memory_evidence_items=[
            RagEvaluationMemoryEvidenceSetup(
                source_id=101,
                title="Wedding memory",
                content_preview="Alya remembered the family wedding in Brno in 1986.",
                memory_type="text",
                selection_reason="eval_fixture_memory",
                occurred_year=1986,
            )
        ],
        retrieved_evidence_items=[
            RagEvaluationRetrievedEvidenceSetup(
                chunk_id=501,
                source_id=201,
                embedding_id=301,
                text_hash="eval-rag-hash-501",
                content_preview="The archival note says the wedding ceremony took place in Brno.",
                source_document_type="document_text",
                validation_status="valid",
            )
        ],
        user_query="Where did the wedding happen?",
        expected_behavior="grounded_answer",
        minimum_required_evidence_count=1,
    ),
    RagEvaluationCase(
        case_id="lack-of-evidence-required",
        title="Lack-of-evidence answer when no stored evidence exists",
        profile=RagEvaluationProfileSetup(
            profile_id=2,
            name="Marek",
            biography="A profile with no verified supporting evidence yet.",
        ),
        user_query="Where was I born?",
        expected_behavior="lack_of_evidence",
        should_require_lack_of_evidence=True,
    ),
)
