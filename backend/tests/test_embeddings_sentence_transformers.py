from __future__ import annotations

import socket
from types import SimpleNamespace

import pytest

from app.core.config import settings
from app.modules.embeddings.providers import build_embedding_provider
from app.modules.embeddings.providers.mock import MockEmbeddingProvider
from app.modules.embeddings.providers.sentence_transformers import (
    SENTENCE_TRANSFORMERS_PROVIDER_NAME,
    SentenceTransformersEmbeddingProvider,
    SentenceTransformersProviderError,
)


class FakeSentenceTransformer:
    init_calls: list[dict[str, object]] = []
    encode_calls: list[dict[str, object]] = []

    def __init__(self, model_name: str, *, device: str = "cpu", cache_folder: str | None = None):
        self.model_name = model_name
        self.device = device
        self.cache_folder = cache_folder
        self.__class__.init_calls.append(
            {
                "model_name": model_name,
                "device": device,
                "cache_folder": cache_folder,
            }
        )

    def encode(
        self,
        texts,
        *,
        convert_to_numpy: bool = True,
        normalize_embeddings: bool = False,
        show_progress_bar: bool = False,
    ):
        materialized_texts = list(texts)
        self.__class__.encode_calls.append(
            {
                "texts": materialized_texts,
                "convert_to_numpy": convert_to_numpy,
                "normalize_embeddings": normalize_embeddings,
                "show_progress_bar": show_progress_bar,
                "model_name": self.model_name,
            }
        )
        dimension = 384 if self.model_name == "intfloat/multilingual-e5-small" else 1024
        return [
            [round((index + 1) / 1000, 6) for index in range(dimension)]
            for _ in materialized_texts
        ]


def _install_fake_sentence_transformers(monkeypatch, fake_class=FakeSentenceTransformer):
    fake_class.init_calls = []
    fake_class.encode_calls = []
    monkeypatch.setattr(
        "app.modules.embeddings.providers.sentence_transformers.import_module",
        lambda module_name: SimpleNamespace(SentenceTransformer=fake_class),
    )


def test_mock_embedding_provider_remains_default_for_tests_and_dev(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", "mock")

    provider = build_embedding_provider(model_code="multilingual_e5_small")

    assert isinstance(provider, MockEmbeddingProvider)


def test_multilingual_e5_small_provider_can_be_resolved_when_enabled(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", SENTENCE_TRANSFORMERS_PROVIDER_NAME)

    provider = build_embedding_provider(model_code="multilingual_e5_small")

    assert isinstance(provider, SentenceTransformersEmbeddingProvider)


def test_bge_m3_provider_can_be_resolved_when_enabled(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", SENTENCE_TRANSFORMERS_PROVIDER_NAME)

    provider = build_embedding_provider(model_code="bge_m3")

    assert isinstance(provider, SentenceTransformersEmbeddingProvider)


def test_sentence_transformers_provider_lazy_loads_model_only_when_used(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", SENTENCE_TRANSFORMERS_PROVIDER_NAME)
    import_calls: list[str] = []

    def fake_import_module(module_name: str):
        import_calls.append(module_name)
        return SimpleNamespace(SentenceTransformer=FakeSentenceTransformer)

    FakeSentenceTransformer.init_calls = []
    FakeSentenceTransformer.encode_calls = []
    monkeypatch.setattr(
        "app.modules.embeddings.providers.sentence_transformers.import_module",
        fake_import_module,
    )
    provider = SentenceTransformersEmbeddingProvider()

    assert import_calls == []
    assert FakeSentenceTransformer.init_calls == []

    result = provider.embed_query("Where is Prague?", "multilingual_e5_small")

    assert result.dimension == 384
    assert import_calls == ["sentence_transformers"]
    assert len(FakeSentenceTransformer.init_calls) == 1


def test_bge_m3_provider_lazy_loads_model_only_when_used(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", SENTENCE_TRANSFORMERS_PROVIDER_NAME)
    import_calls: list[str] = []

    def fake_import_module(module_name: str):
        import_calls.append(module_name)
        return SimpleNamespace(SentenceTransformer=FakeSentenceTransformer)

    FakeSentenceTransformer.init_calls = []
    FakeSentenceTransformer.encode_calls = []
    monkeypatch.setattr(
        "app.modules.embeddings.providers.sentence_transformers.import_module",
        fake_import_module,
    )
    provider = SentenceTransformersEmbeddingProvider()

    assert import_calls == []
    assert FakeSentenceTransformer.init_calls == []

    result = provider.embed_query("Where is Brno?", "bge_m3")

    assert result.dimension == 1024
    assert import_calls == ["sentence_transformers"]
    assert len(FakeSentenceTransformer.init_calls) == 1
    assert FakeSentenceTransformer.init_calls[0]["model_name"] == "BAAI/bge-m3"


def test_provider_formats_query_and_passage_text_with_e5_prefixes(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", SENTENCE_TRANSFORMERS_PROVIDER_NAME)
    _install_fake_sentence_transformers(monkeypatch)
    provider = SentenceTransformersEmbeddingProvider()

    provider.embed_query("What happened in Brno?", "multilingual_e5_small")
    provider.embed_passage("Brno station archive note.", "multilingual_e5_small")

    assert FakeSentenceTransformer.encode_calls[0]["texts"] == ["query: What happened in Brno?"]
    assert FakeSentenceTransformer.encode_calls[1]["texts"] == ["passage: Brno station archive note."]


def test_provider_formats_bge_m3_query_and_passage_text_without_prefixes(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", SENTENCE_TRANSFORMERS_PROVIDER_NAME)
    _install_fake_sentence_transformers(monkeypatch)
    provider = SentenceTransformersEmbeddingProvider()

    provider.embed_query("What happened in Brno?", "bge_m3")
    provider.embed_passage("Brno station archive note.", "bge_m3")

    assert FakeSentenceTransformer.encode_calls[0]["texts"] == ["What happened in Brno?"]
    assert FakeSentenceTransformer.encode_calls[1]["texts"] == ["Brno station archive note."]


def test_provider_returns_vector_list_with_registry_dimension(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", SENTENCE_TRANSFORMERS_PROVIDER_NAME)
    _install_fake_sentence_transformers(monkeypatch)
    provider = SentenceTransformersEmbeddingProvider()

    result = provider.embed_passage("Deterministic archive sentence.", "multilingual_e5_small")

    assert result.dimension == 384
    assert len(result.values) == 384
    assert result.metadata["provider_name"] == "sentence_transformers"


def test_bge_m3_provider_returns_vector_list_with_registry_dimension(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", SENTENCE_TRANSFORMERS_PROVIDER_NAME)
    _install_fake_sentence_transformers(monkeypatch)
    provider = SentenceTransformersEmbeddingProvider()

    result = provider.embed_passage("Deterministic archive sentence.", "bge_m3")

    assert result.dimension == 1024
    assert len(result.values) == 1024
    assert result.metadata["provider_name"] == "sentence_transformers"
    assert result.metadata["input_prefix"] is None


def test_provider_rejects_empty_input_text(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", SENTENCE_TRANSFORMERS_PROVIDER_NAME)
    _install_fake_sentence_transformers(monkeypatch)
    provider = SentenceTransformersEmbeddingProvider()

    with pytest.raises(SentenceTransformersProviderError, match="must not be empty"):
        provider.embed_passage("   ", "multilingual_e5_small")


def test_provider_returns_safe_error_when_inference_fails(monkeypatch):
    class FailingSentenceTransformer(FakeSentenceTransformer):
        def encode(self, texts, **kwargs):
            raise RuntimeError("model exploded")

    monkeypatch.setattr(settings, "embedding_provider", SENTENCE_TRANSFORMERS_PROVIDER_NAME)
    _install_fake_sentence_transformers(monkeypatch, fake_class=FailingSentenceTransformer)
    provider = SentenceTransformersEmbeddingProvider()

    with pytest.raises(SentenceTransformersProviderError, match="embedding generation failed"):
        provider.embed_query("safe query", "multilingual_e5_small")


def test_provider_does_not_require_network_in_tests(monkeypatch):
    monkeypatch.setattr(settings, "embedding_provider", SENTENCE_TRANSFORMERS_PROVIDER_NAME)
    _install_fake_sentence_transformers(monkeypatch)

    def fail_network(*args, **kwargs):
        raise AssertionError("SentenceTransformers provider tests must not require network access")

    monkeypatch.setattr(socket, "create_connection", fail_network)
    provider = SentenceTransformersEmbeddingProvider()
    result = provider.embed_query("network-free query", "multilingual_e5_small")

    assert result.dimension == 384
