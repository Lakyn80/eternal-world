from __future__ import annotations

from app.modules.rag_evaluation.brain_eval_e2e_bootstrap import (
    _source_needs_embedding_pipeline,
    build_family_avatar_ru_e2e_collection_name,
)


def test_build_family_avatar_ru_e2e_collection_name_uses_dedicated_suffix():
    collection_name = build_family_avatar_ru_e2e_collection_name(
        base_collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse"
    )

    assert collection_name == (
        "eternal_world_rag_chunks__bge_m3_dense_sparse"
        "__family_novak_ru_e2e_v3_bge_m3_real_cpu"
    )


def test_source_needs_embedding_pipeline_when_embeddings_are_missing():
    assert _source_needs_embedding_pipeline(
        stored_hash="abc",
        corpus_hash="abc",
        stored_fingerprint="fingerprint",
        embedding_runtime_fingerprint="fingerprint",
        chunk_count=20,
        embedding_count=0,
        qdrant_point_count=20,
    )


def test_source_needs_embedding_pipeline_when_qdrant_points_are_missing():
    assert _source_needs_embedding_pipeline(
        stored_hash="abc",
        corpus_hash="abc",
        stored_fingerprint="fingerprint",
        embedding_runtime_fingerprint="fingerprint",
        chunk_count=20,
        embedding_count=20,
        qdrant_point_count=0,
    )


def test_source_does_not_need_pipeline_when_counts_and_fingerprint_match():
    assert _source_needs_embedding_pipeline(
        stored_hash="abc",
        corpus_hash="abc",
        stored_fingerprint="fingerprint",
        embedding_runtime_fingerprint="fingerprint",
        chunk_count=20,
        embedding_count=20,
        qdrant_point_count=20,
    ) is False
