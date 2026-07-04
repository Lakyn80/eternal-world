from __future__ import annotations

from rag_eval.metrics.cases import UNIVERSAL_RAG_QUALITY_FOUNDATION_CASES
from rag_eval.metrics.schemas import RagQualityEvalDataset


UNIVERSAL_RAG_QUALITY_FOUNDATION_DATASET = RagQualityEvalDataset(
    dataset_id="universal-rag-quality-foundation",
    name="Universal RAG Quality Foundation Dataset",
    description=(
        "A small reusable dataset demonstrating positive retrieval and lack-of-evidence"
        " quality checks without depending on Eternal World database entities."
    ),
    cases=list(UNIVERSAL_RAG_QUALITY_FOUNDATION_CASES),
    metadata={"scope": "foundation"},
)
