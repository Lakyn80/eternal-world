from __future__ import annotations

import pytest

from scripts.prefetch_embedding_model import (
    PREFETCH_DEPENDENCY_REPOS_BY_PROVIDER,
    PrefetchTarget,
    prefetch_provider_assets,
    resolve_prefetch_target,
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


def test_resolve_prefetch_target_rejects_unsupported_provider():
    with pytest.raises(ValueError, match="Unsupported provider for prefetch"):
        resolve_prefetch_target("multilingual_e5_base")


def test_prefetch_provider_assets_downloads_only_expected_repos_without_real_network():
    download_calls: list[dict[str, object]] = []

    def fake_snapshot_download(**kwargs):
        download_calls.append(dict(kwargs))
        repo_id = str(kwargs["repo_id"])
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
        "jinaai/xlm-roberta-flash-implementation",
    ]
    for call in download_calls:
        assert call["local_files_only"] is False
        assert call["max_workers"] == 4


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
