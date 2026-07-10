from __future__ import annotations

from pathlib import Path

import pytest

from app.core.config import settings
from scripts.prefetch_embedding_model import (
    PREFETCH_DEPENDENCY_REPOS_BY_PROVIDER,
    PrefetchTarget,
    prefetch_provider_assets,
    resolve_prefetch_target,
)
from app.modules.embeddings.bge_m3_model_cache import (
    BGE_M3_MULTIVECTOR_EXTRA_PREFETCH_PATTERNS,
    BGE_M3_PREFETCH_ALLOW_PATTERNS,
)


@pytest.fixture(autouse=True)
def _treat_fake_snapshot_paths_as_complete(monkeypatch):
    monkeypatch.setattr(
        "scripts.prefetch_embedding_model.is_snapshot_weights_complete",
        lambda _path: True,
    )


def test_resolve_prefetch_target_for_jina_embeddings_v3():
    target = resolve_prefetch_target("jina_embeddings_v3")

    assert target == PrefetchTarget(
        provider_key="jina_embeddings_v3",
        primary_repo_id="jinaai/jina-embeddings-v3",
        dependency_repo_ids=PREFETCH_DEPENDENCY_REPOS_BY_PROVIDER["jina_embeddings_v3"],
    )


def test_resolve_prefetch_target_for_qwen3_embedding_0_6b():
    target = resolve_prefetch_target("qwen3_embedding_0_6b")

    assert target == PrefetchTarget(
        provider_key="qwen3_embedding_0_6b",
        primary_repo_id="Qwen/Qwen3-Embedding-0.6B",
        dependency_repo_ids=PREFETCH_DEPENDENCY_REPOS_BY_PROVIDER["qwen3_embedding_0_6b"],
    )


def test_resolve_prefetch_target_for_bge_m3_dense_sparse():
    target = resolve_prefetch_target("bge_m3_dense_sparse")

    assert target == PrefetchTarget(
        provider_key="bge_m3_dense_sparse",
        primary_repo_id="BAAI/bge-m3",
        dependency_repo_ids=PREFETCH_DEPENDENCY_REPOS_BY_PROVIDER["bge_m3_dense_sparse"],
    )


def test_resolve_prefetch_target_for_bge_m3_dense_sparse_multivector():
    target = resolve_prefetch_target("bge_m3_dense_sparse_multivector")

    assert target == PrefetchTarget(
        provider_key="bge_m3_dense_sparse_multivector",
        primary_repo_id="BAAI/bge-m3",
        dependency_repo_ids=PREFETCH_DEPENDENCY_REPOS_BY_PROVIDER["bge_m3_dense_sparse_multivector"],
    )


def test_resolve_prefetch_target_rejects_unsupported_provider():
    with pytest.raises(ValueError, match="Unsupported provider for prefetch"):
        resolve_prefetch_target("multilingual_e5_base")


def test_prefetch_provider_assets_downloads_only_expected_repos_without_real_network():
    download_calls: list[dict[str, object]] = []
    cached_repo_ids: set[str] = set()

    def fake_snapshot_download(**kwargs):
        download_calls.append(dict(kwargs))
        repo_id = str(kwargs["repo_id"])
        if kwargs["local_files_only"] is True and repo_id not in cached_repo_ids:
            cached_repo_ids.add(repo_id)
            raise FileNotFoundError(repo_id)
        return f"/fake-cache/{repo_id.replace('/', '--')}"

    prefetched_paths = prefetch_provider_assets(
        provider_key="jina_embeddings_v3",
        retries=2,
        retry_delay_seconds=0.0,
        snapshot_download_fn=fake_snapshot_download,
    )

    assert prefetched_paths == {
        "jinaai/jina-embeddings-v3": "/fake-cache/jinaai--jina-embeddings-v3",
        "jinaai/xlm-roberta-flash-implementation": "/fake-cache/jinaai--xlm-roberta-flash-implementation",
    }
    assert [call["repo_id"] for call in download_calls] == [
        "jinaai/jina-embeddings-v3",
        "jinaai/jina-embeddings-v3",
        "jinaai/xlm-roberta-flash-implementation",
        "jinaai/xlm-roberta-flash-implementation",
    ]
    for call in download_calls[1::2]:
        assert call["local_files_only"] is False
        assert call["max_workers"] == 1
        assert call["tqdm_class"] is not None


def test_prefetch_provider_assets_uses_bge_m3_allow_patterns_for_dense_sparse():
    download_calls: list[dict[str, object]] = []

    def fake_snapshot_download(**kwargs):
        download_calls.append(dict(kwargs))
        return "/fake-cache/BAAI--bge-m3"

    prefetch_provider_assets(
        provider_key="bge_m3_dense_sparse",
        retries=1,
        retry_delay_seconds=0.0,
        snapshot_download_fn=fake_snapshot_download,
    )

    assert download_calls[0]["allow_patterns"]
    assert "model.safetensors" in download_calls[0]["allow_patterns"]
    assert "colbert_linear.pt" not in download_calls[0]["allow_patterns"]


def test_prefetch_provider_assets_uses_bge_m3_allow_patterns_for_multivector():
    download_calls: list[dict[str, object]] = []

    def fake_snapshot_download(**kwargs):
        download_calls.append(dict(kwargs))
        return "/fake-cache/BAAI--bge-m3"

    prefetch_provider_assets(
        provider_key="bge_m3_dense_sparse_multivector",
        retries=1,
        retry_delay_seconds=0.0,
        snapshot_download_fn=fake_snapshot_download,
    )

    assert "colbert_linear.pt" in download_calls[0]["allow_patterns"]


def test_prefetch_provider_assets_supports_qwen3_embedding_0_6b_without_unrelated_repo_downloads():
    download_calls: list[dict[str, object]] = []

    def fake_snapshot_download(**kwargs):
        download_calls.append(dict(kwargs))
        repo_id = str(kwargs["repo_id"])
        return f"/fake-cache/{repo_id.replace('/', '--')}"

    prefetched_paths = prefetch_provider_assets(
        provider_key="qwen3_embedding_0_6b",
        retries=2,
        retry_delay_seconds=0.0,
        snapshot_download_fn=fake_snapshot_download,
    )

    assert prefetched_paths == {
        "Qwen/Qwen3-Embedding-0.6B": "/fake-cache/Qwen--Qwen3-Embedding-0.6B",
    }
    assert [call["repo_id"] for call in download_calls] == [
        "Qwen/Qwen3-Embedding-0.6B",
    ]


def test_prefetch_provider_assets_supports_bge_m3_dense_sparse_without_duplicate_dependency_downloads():
    download_calls: list[dict[str, object]] = []

    def fake_snapshot_download(**kwargs):
        download_calls.append(dict(kwargs))
        repo_id = str(kwargs["repo_id"])
        return f"/fake-cache/{repo_id.replace('/', '--')}"

    prefetched_paths = prefetch_provider_assets(
        provider_key="bge_m3_dense_sparse",
        retries=2,
        retry_delay_seconds=0.0,
        snapshot_download_fn=fake_snapshot_download,
    )

    assert prefetched_paths == {
        "BAAI/bge-m3": "/fake-cache/BAAI--bge-m3",
    }
    assert [call["repo_id"] for call in download_calls] == [
        "BAAI/bge-m3",
    ]


def test_prefetch_provider_assets_uses_cached_snapshot_before_attempting_remote_download():
    download_calls: list[dict[str, object]] = []

    def fake_snapshot_download(**kwargs):
        download_calls.append(dict(kwargs))
        if kwargs["local_files_only"] is True:
            return "/fake-cache/BAAI--bge-m3"
        raise AssertionError("Remote download should not run when the local cache is already populated")

    prefetched_paths = prefetch_provider_assets(
        provider_key="bge_m3_dense_sparse_multivector",
        retries=2,
        retry_delay_seconds=0.0,
        snapshot_download_fn=fake_snapshot_download,
    )

    assert prefetched_paths == {
        "BAAI/bge-m3": "/fake-cache/BAAI--bge-m3",
    }
    assert download_calls == [
        {
            "repo_id": "BAAI/bge-m3",
            "revision": None,
            "local_files_only": True,
            "allow_patterns": list(BGE_M3_PREFETCH_ALLOW_PATTERNS)
            + list(BGE_M3_MULTIVECTOR_EXTRA_PREFETCH_PATTERNS),
            "max_workers": 4,
            "tqdm_class": None,
        }
    ]


def test_prefetch_provider_assets_forwards_configured_cache_dir(monkeypatch, tmp_path):
    explicit_cache_dir = tmp_path / "hf-cache"
    monkeypatch.setattr(settings, "sentence_transformers_cache_dir", explicit_cache_dir)

    download_calls: list[dict[str, object]] = []

    def fake_snapshot_download(**kwargs):
        download_calls.append(dict(kwargs))
        return "/fake-cache/BAAI--bge-m3"

    prefetch_provider_assets(
        provider_key="bge_m3_dense_sparse",
        retries=1,
        retry_delay_seconds=0.0,
        snapshot_download_fn=fake_snapshot_download,
    )

    assert all(call["cache_dir"] == str(explicit_cache_dir) for call in download_calls)


def test_prefetch_provider_assets_forwards_configured_cache_dir_for_non_bge_m3_repos(
    monkeypatch, tmp_path
):
    explicit_cache_dir = tmp_path / "hf-cache"
    monkeypatch.setattr(settings, "sentence_transformers_cache_dir", explicit_cache_dir)

    download_calls: list[dict[str, object]] = []

    def fake_snapshot_download(**kwargs):
        download_calls.append(dict(kwargs))
        return f"/fake-cache/{str(kwargs['repo_id']).replace('/', '--')}"

    prefetch_provider_assets(
        provider_key="jina_embeddings_v3",
        retries=1,
        retry_delay_seconds=0.0,
        snapshot_download_fn=fake_snapshot_download,
    )

    assert all(call["cache_dir"] == str(explicit_cache_dir) for call in download_calls)


def test_prefetch_provider_assets_omits_cache_dir_when_not_configured():
    assert settings.sentence_transformers_cache_dir is None

    download_calls: list[dict[str, object]] = []

    def fake_snapshot_download(**kwargs):
        download_calls.append(dict(kwargs))
        return "/fake-cache/BAAI--bge-m3"

    prefetch_provider_assets(
        provider_key="bge_m3_dense_sparse",
        retries=1,
        retry_delay_seconds=0.0,
        snapshot_download_fn=fake_snapshot_download,
    )

    assert all("cache_dir" not in call for call in download_calls)
