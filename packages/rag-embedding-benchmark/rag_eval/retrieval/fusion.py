from __future__ import annotations

from rag_eval.adapters.base import RagEvalRetrievalResponse, RagEvalRetrievalResult


def reciprocal_rank_fusion(
    ranked_lists: list[list[RagEvalRetrievalResult]],
    *,
    top_k: int,
    rrf_k: int = 60,
) -> RagEvalRetrievalResponse:
    """Fuse multiple ranked lists with RRF; never mixes raw dense/BM25 score scales."""
    fused_scores: dict[int, float] = {}
    result_by_chunk_id: dict[int, RagEvalRetrievalResult] = {}

    for ranked_results in ranked_lists:
        for rank, result in enumerate(ranked_results, start=1):
            if result.chunk_id is None:
                continue
            chunk_id = int(result.chunk_id)
            fused_scores[chunk_id] = fused_scores.get(chunk_id, 0.0) + (1.0 / (rrf_k + rank))
            result_by_chunk_id.setdefault(chunk_id, result)

    ordered_chunk_ids = sorted(
        fused_scores.keys(),
        key=lambda chunk_id: fused_scores[chunk_id],
        reverse=True,
    )

    fused_results: list[RagEvalRetrievalResult] = []
    for chunk_id in ordered_chunk_ids[:top_k]:
        base_result = result_by_chunk_id[chunk_id]
        fused_results.append(
            RagEvalRetrievalResult(
                chunk_id=base_result.chunk_id,
                source_id=base_result.source_id,
                score=fused_scores[chunk_id],
                text=base_result.text,
                embedding_id=base_result.embedding_id,
                language=base_result.language,
                source_type=base_result.source_type,
                validation_status=base_result.validation_status,
                text_hash=base_result.text_hash,
                qdrant_collection=base_result.qdrant_collection,
                payload_metadata={
                    **dict(base_result.payload_metadata),
                    "fusion": "rrf",
                    "rrf_k": rrf_k,
                },
            )
        )

    return RagEvalRetrievalResponse(results=fused_results)
