from __future__ import annotations

import pytest

from app.modules.embeddings.bge_m3_model_cache import (
    is_huggingface_offline_mode,
    resolve_bge_m3_model_load_path,
    resolve_local_snapshot_path,
)


def test_resolve_bge_m3_model_load_path_uses_local_snapshot_when_cached(monkeypatch):
    monkeypatch.setattr(
        "app.modules.embeddings.bge_m3_model_cache.resolve_local_snapshot_path",
        lambda repo_id, **kwargs: "/cache/BAAI--bge-m3",
    )

    load_path, loaded_from_local_cache = resolve_bge_m3_model_load_path("BAAI/bge-m3")

    assert load_path == "/cache/BAAI--bge-m3"
    assert loaded_from_local_cache is True


def test_resolve_bge_m3_model_load_path_fails_when_cache_missing_and_remote_disabled(monkeypatch):
    monkeypatch.setattr(
        "app.modules.embeddings.bge_m3_model_cache.resolve_local_snapshot_path",
        lambda repo_id, **kwargs: None,
    )
    monkeypatch.setenv("HF_HUB_OFFLINE", "0")

    with pytest.raises(RuntimeError, match="Prefetch first"):
        resolve_bge_m3_model_load_path("BAAI/bge-m3", allow_remote_download=False)


def test_resolve_bge_m3_model_load_path_fails_in_offline_mode_when_cache_missing(monkeypatch):
    monkeypatch.setattr(
        "app.modules.embeddings.bge_m3_model_cache.resolve_local_snapshot_path",
        lambda repo_id, **kwargs: None,
    )
    monkeypatch.setenv("HF_HUB_OFFLINE", "1")
    monkeypatch.setenv("TRANSFORMERS_OFFLINE", "1")

    with pytest.raises(RuntimeError, match="offline mode is enabled"):
        resolve_bge_m3_model_load_path("BAAI/bge-m3")


def test_is_huggingface_offline_mode_reads_env_flags(monkeypatch):
    monkeypatch.setenv("HF_HUB_OFFLINE", "1")
    monkeypatch.setenv("TRANSFORMERS_OFFLINE", "0")
    assert is_huggingface_offline_mode() is True

    monkeypatch.setenv("HF_HUB_OFFLINE", "0")
    monkeypatch.setenv("TRANSFORMERS_OFFLINE", "true")
    assert is_huggingface_offline_mode() is True


def test_resolve_local_snapshot_path_returns_none_when_weights_missing(monkeypatch, tmp_path):
    snapshot_dir = tmp_path / "snapshot"
    snapshot_dir.mkdir()
    (snapshot_dir / "config.json").write_text("{}", encoding="utf-8")

    def fake_snapshot_download(**kwargs):
        if kwargs["local_files_only"] is True:
            return str(snapshot_dir)
        return str(snapshot_dir)

    monkeypatch.setattr(
        "app.modules.embeddings.bge_m3_model_cache._import_snapshot_download",
        lambda: fake_snapshot_download,
    )

    assert resolve_local_snapshot_path("BAAI/bge-m3") is None


def test_resolve_local_snapshot_path_returns_path_when_weights_present(monkeypatch, tmp_path):
    snapshot_dir = tmp_path / "snapshot"
    snapshot_dir.mkdir()
    (snapshot_dir / "model.safetensors").write_text("fake", encoding="utf-8")

    def fake_snapshot_download(**kwargs):
        return str(snapshot_dir)

    monkeypatch.setattr(
        "app.modules.embeddings.bge_m3_model_cache._import_snapshot_download",
        lambda: fake_snapshot_download,
    )

    assert resolve_local_snapshot_path("BAAI/bge-m3") == str(snapshot_dir)


def test_resolve_local_snapshot_path_returns_none_when_cache_missing(monkeypatch):
    def fake_snapshot_download(**kwargs):
        if kwargs["local_files_only"] is True:
            raise FileNotFoundError("missing")
        return "/cache/BAAI--bge-m3"

    monkeypatch.setattr(
        "app.modules.embeddings.bge_m3_model_cache._import_snapshot_download",
        lambda: fake_snapshot_download,
    )

    assert resolve_local_snapshot_path("BAAI/bge-m3") is None
