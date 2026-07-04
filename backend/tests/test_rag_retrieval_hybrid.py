from __future__ import annotations

from app.modules.rag_retrieval.hybrid import (
    BGE_M3_DENSE_SPARSE_MODEL_CODE,
    HybridRetrievalCandidate,
    build_deterministic_sparse_vector,
    compute_sparse_overlap_score,
    rank_fused_hybrid_candidates,
)


def test_rank_fused_hybrid_candidates_prefers_sparse_match_over_dense_only_leader():
    query_sparse = {"lantern": 1.0, "archive": 0.8}
    wrong_dense_leader = HybridRetrievalCandidate(
        embedding_id=1,
        chunk_id=10,
        dense_score=0.95,
        sparse_vector={"noise": 0.1},
        payload_metadata={"embedding_id": 1},
    )
    sparse_match = HybridRetrievalCandidate(
        embedding_id=2,
        chunk_id=11,
        dense_score=0.70,
        sparse_vector={"lantern": 1.0, "archive": 0.9},
        payload_metadata={"embedding_id": 2},
    )
    weak_candidate = HybridRetrievalCandidate(
        embedding_id=3,
        chunk_id=12,
        dense_score=0.40,
        sparse_vector={"other": 0.2},
        payload_metadata={"embedding_id": 3},
    )

    ranked = rank_fused_hybrid_candidates(
        query_sparse_vector=query_sparse,
        candidates=[wrong_dense_leader, sparse_match, weak_candidate],
        top_k=1,
    )

    assert len(ranked) == 1
    assert ranked[0].embedding_id == 2


def test_build_deterministic_sparse_vector_is_stable_for_same_input():
    first = build_deterministic_sparse_vector(
        text="Lantern archive cart",
        model_code=BGE_M3_DENSE_SPARSE_MODEL_CODE,
    )
    second = build_deterministic_sparse_vector(
        text="Lantern archive cart",
        model_code=BGE_M3_DENSE_SPARSE_MODEL_CODE,
    )

    assert first == second
    assert compute_sparse_overlap_score(first, first) > 0
