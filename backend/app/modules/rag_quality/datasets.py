from __future__ import annotations

from app.modules.rag_quality.cases import UNIVERSAL_RAG_QUALITY_FOUNDATION_CASES
from app.modules.rag_quality.schemas import RagQualityEvalDataset


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
