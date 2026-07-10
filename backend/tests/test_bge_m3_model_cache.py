from __future__ import annotations

import pytest

from app.core.config import Settings
from app.modules.embeddings.bge_m3_model_cache import (
    describe_cache_dir,
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


def test_resolve_local_snapshot_path_checks_only_local_files_for_bge_m3(monkeypatch, tmp_path):
    snapshot_dir = tmp_path / "snapshot"
    snapshot_dir.mkdir()
    (snapshot_dir / "model.safetensors").write_text("fake", encoding="utf-8")
    captured_kwargs: dict[str, object] = {}

    def fake_snapshot_download(**kwargs):
        captured_kwargs.update(kwargs)
        return str(snapshot_dir)

    monkeypatch.setattr(
        "app.modules.embeddings.bge_m3_model_cache._import_snapshot_download",
        lambda: fake_snapshot_download,
    )

    resolved = resolve_local_snapshot_path("BAAI/bge-m3", cache_dir="/models/huggingface")

    assert resolved == str(snapshot_dir)
    assert captured_kwargs["local_files_only"] is True
    assert captured_kwargs["cache_dir"] == "/models/huggingface"


def test_describe_cache_dir_reports_explicit_path():
    assert describe_cache_dir("/models/huggingface") == "/models/huggingface"


def test_describe_cache_dir_warns_about_unstable_default_when_unset():
    description = describe_cache_dir(None)
    assert "default" in description.lower()
    assert "not backed by a stable volume" in description.lower()


def test_resolve_bge_m3_model_load_path_failure_message_includes_resolved_cache_dir(monkeypatch):
    monkeypatch.setattr(
        "app.modules.embeddings.bge_m3_model_cache.resolve_local_snapshot_path",
        lambda repo_id, **kwargs: None,
    )
    monkeypatch.setenv("HF_HUB_OFFLINE", "1")
    monkeypatch.setenv("TRANSFORMERS_OFFLINE", "1")

    with pytest.raises(RuntimeError, match=r"cache_dir=/models/huggingface"):
        resolve_bge_m3_model_load_path("BAAI/bge-m3", cache_dir="/models/huggingface")


def test_config_resolves_explicit_bge_m3_local_snapshot_path(monkeypatch, tmp_path):
    explicit_cache_dir = tmp_path / "hf-cache"
    monkeypatch.setenv("SENTENCE_TRANSFORMERS_CACHE_DIR", str(explicit_cache_dir))

    config = Settings(_env_file=None)

    assert config.sentence_transformers_cache_dir == explicit_cache_dir

    captured_cache_dir: dict[str, object] = {}

    def fake_snapshot_download(**kwargs):
        captured_cache_dir["cache_dir"] = kwargs.get("cache_dir")
        raise FileNotFoundError("missing")

    monkeypatch.setattr(
        "app.modules.embeddings.bge_m3_model_cache._import_snapshot_download",
        lambda: fake_snapshot_download,
    )

    resolve_local_snapshot_path("BAAI/bge-m3", cache_dir=config.sentence_transformers_cache_dir)

    assert captured_cache_dir["cache_dir"] == str(explicit_cache_dir)
