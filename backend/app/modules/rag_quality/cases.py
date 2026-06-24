from __future__ import annotations

from app.modules.rag_quality.schemas import RagQualityEvalCase


UNIVERSAL_RAG_QUALITY_FOUNDATION_CASES: tuple[RagQualityEvalCase, ...] = (
    RagQualityEvalCase(
        case_id="retrieval-grounded-fact",
        title="Retrieved evidence includes the expected grounded fact",
        query="What city was mentioned in the family archive?",
        expected_markers=["Brno"],
        expected_behavior="retrieval_only",
        minimum_relevant_results=1,
        tags=["grounded", "evidence"],
        metadata={"project_type": "generic_rag"},
    ),
    RagQualityEvalCase(
        case_id="retrieval-no-evidence",
        title="No unsupported evidence should be returned for unknown facts",
        query="What was the secret code word?",
        forbidden_markers=["secret code word"],
        expected_behavior="lack_of_evidence",
        tags=["safety", "lack_of_evidence"],
    ),
)
