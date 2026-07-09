from __future__ import annotations

import pytest

from app.core.config import settings
from app.modules.embeddings.providers import build_embedding_provider
from app.modules.embeddings.providers.bge_m3_hybrid import BgeM3HybridEmbeddingAdapter
from app.modules.embeddings.providers.mock import MockEmbeddingProvider
from app.modules.embeddings.providers.sentence_transformers import (
    SENTENCE_TRANSFORMERS_PROVIDER_NAME,
)
from app.modules.embeddings.runtime import assert_real_embedding_runtime_for_e2e
from app.modules.rag_evaluation.exceptions import BrainRagEvalConfigurationError
from app.modules.rag_evaluation.schemas import BrainRagEvalConfig
from app.modules.rag_evaluation.brain_eval_e2e_runner import run_brain_rag_eval_e2e


def test_bge_m3_dense_sparse_uses_mock_when_embedding_provider_is_mock(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", "mock")

    provider = build_embedding_provider(model_code="bge_m3_dense_sparse")

    assert isinstance(provider, MockEmbeddingProvider)


def test_bge_m3_dense_sparse_uses_hybrid_adapter_when_sentence_transformers_enabled(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", SENTENCE_TRANSFORMERS_PROVIDER_NAME)
    monkeypatch.setattr(
        "app.modules.embeddings.providers._can_use_real_bge_m3_hybrid_provider",
        lambda: True,
    )

    provider = build_embedding_provider(model_code="bge_m3_dense_sparse")

    assert isinstance(provider, BgeM3HybridEmbeddingAdapter)


def test_real_embedding_runtime_guard_rejects_mock_provider(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", "mock")
    monkeypatch.setattr(
        "app.modules.embeddings.runtime.resolve_local_snapshot_path",
        lambda *args, **kwargs: "/cache/BAAI--bge-m3",
    )

    with pytest.raises(RuntimeError, match="sentence_transformers"):
        assert_real_embedding_runtime_for_e2e(
            model_code="bge_m3_dense_sparse",
            collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse",
            allow_mock_embeddings=False,
        )


def test_real_embedding_runtime_guard_allows_mock_with_explicit_flag(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", "mock")

    diagnostics = assert_real_embedding_runtime_for_e2e(
        model_code="bge_m3_dense_sparse",
        collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse",
        allow_mock_embeddings=True,
    )

    assert diagnostics.is_mock_indexing_provider is True
    assert diagnostics.is_mock_query_provider is True


def test_real_embedding_runtime_guard_rejects_missing_bge_m3_cache(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", "sentence_transformers")
    monkeypatch.setattr(
        "app.modules.embeddings.providers._can_use_real_bge_m3_hybrid_provider",
        lambda: True,
    )
    monkeypatch.setattr(
        "app.modules.embeddings.runtime.resolve_local_snapshot_path",
        lambda *args, **kwargs: None,
    )

    with pytest.raises(RuntimeError, match="missing or incomplete"):
        assert_real_embedding_runtime_for_e2e(
            model_code="bge_m3_dense_sparse",
            collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse",
            allow_mock_embeddings=False,
        )


def test_run_brain_rag_eval_e2e_fails_fast_on_mock_embeddings(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", "mock")
    monkeypatch.setattr(
        "app.modules.rag_evaluation.brain_eval_e2e_runner.preflight_brain_rag_eval",
        lambda config, provider_settings=None: type(
            "Preflight",
            (),
            {"passed": True, "model": "deepseek-chat", "issues": []},
        )(),
    )
    monkeypatch.setattr(
        "app.modules.rag_evaluation.brain_eval_e2e_runner.resolve_brain_rag_eval_cases",
        lambda case_set: [object()],
    )

    config = BrainRagEvalConfig(
        case_set="family_avatar_ru",
        real_retrieval=True,
        write_artifacts=False,
        artifact_dir=None,
        allow_mock_embeddings=False,
    )

    with pytest.raises(BrainRagEvalConfigurationError, match="sentence_transformers"):
        run_brain_rag_eval_e2e(object(), config)
