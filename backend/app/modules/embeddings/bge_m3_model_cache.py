from __future__ import annotations

import os
from pathlib import Path


BGE_M3_DEFAULT_REPO_ID = "BAAI/bge-m3"
BGE_M3_PREFETCH_ALLOW_PATTERNS = (
    "config.json",
    "tokenizer.json",
    "tokenizer_config.json",
    "special_tokens_map.json",
    "sentencepiece.bpe.model",
    "modules.json",
    "config_sentence_transformers.json",
    "sentence_bert_config.json",
    "sparse_linear.pt",
    "model.safetensors",
    "model.safetensors.index.json",
    "pytorch_model.bin",
    "pytorch_model.bin.index.json",
    "1_Pooling/*",
)
BGE_M3_MULTIVECTOR_EXTRA_PREFETCH_PATTERNS = ("colbert_linear.pt",)
BGE_M3_WEIGHT_FILENAMES = (
    "model.safetensors",
    "pytorch_model.bin",
)
BGE_M3_WEIGHT_INDEX_FILENAMES = (
    "model.safetensors.index.json",
    "pytorch_model.bin.index.json",
)
PREFETCH_CLI_HINT = (
    "docker compose exec backend python scripts/prefetch_embedding_model.py "
    "--provider bge_m3_dense_sparse"
)


def build_bge_m3_snapshot_download_kwargs(
    *,
    local_files_only: bool,
    include_multivector_assets: bool = False,
    cache_dir: str | Path | None = None,
) -> dict[str, object]:
    allow_patterns = list(BGE_M3_PREFETCH_ALLOW_PATTERNS)
    if include_multivector_assets:
        allow_patterns.extend(BGE_M3_MULTIVECTOR_EXTRA_PREFETCH_PATTERNS)

    kwargs: dict[str, object] = {
        "repo_id": BGE_M3_DEFAULT_REPO_ID,
        "revision": None,
        "local_files_only": local_files_only,
        "allow_patterns": allow_patterns,
        "max_workers": 4,
    }
    if cache_dir is not None:
        kwargs["cache_dir"] = str(cache_dir)
    return kwargs


def is_snapshot_weights_complete(snapshot_path: str | Path) -> bool:
    path = Path(snapshot_path)
    if not path.is_dir():
        return False

    if any((path / filename).exists() for filename in BGE_M3_WEIGHT_FILENAMES):
        return True

    return any((path / filename).exists() for filename in BGE_M3_WEIGHT_INDEX_FILENAMES)


def is_huggingface_offline_mode() -> bool:
    offline_flags = (
        os.getenv("HF_HUB_OFFLINE", ""),
        os.getenv("TRANSFORMERS_OFFLINE", ""),
    )
    return any(value.strip().lower() in {"1", "true", "yes", "on"} for value in offline_flags)


def _import_snapshot_download():
    try:
        from huggingface_hub import snapshot_download
    except ModuleNotFoundError as exc:
        raise RuntimeError("huggingface_hub is not installed in this environment") from exc

    return snapshot_download


def resolve_local_snapshot_path(
    repo_id: str,
    *,
    cache_dir: str | Path | None = None,
    include_multivector_assets: bool = False,
) -> str | None:
    snapshot_download = _import_snapshot_download()
    if repo_id == BGE_M3_DEFAULT_REPO_ID:
        kwargs = build_bge_m3_snapshot_download_kwargs(
            local_files_only=True,
            include_multivector_assets=include_multivector_assets,
            cache_dir=cache_dir,
        )
        kwargs["tqdm_class"] = None
    else:
        kwargs = {
            "repo_id": repo_id,
            "revision": None,
            "local_files_only": True,
            "max_workers": 1,
            "tqdm_class": None,
        }
        if cache_dir is not None:
            kwargs["cache_dir"] = str(cache_dir)

    try:
        snapshot_path = snapshot_download(**kwargs)
    except Exception:
        return None

    if not is_snapshot_weights_complete(snapshot_path):
        return None

    return snapshot_path


def describe_cache_dir(cache_dir: str | Path | None) -> str:
    if cache_dir is not None:
        return str(cache_dir)
    return "<default Hugging Face cache: ~/.cache/huggingface/hub (not backed by a stable volume)>"


def assert_local_snapshot_available(
    repo_id: str,
    *,
    cache_dir: str | Path | None = None,
) -> str:
    snapshot_path = resolve_local_snapshot_path(repo_id, cache_dir=cache_dir)
    resolved_cache_dir = describe_cache_dir(cache_dir)
    if snapshot_path is None:
        raise RuntimeError(
            f"BGE-M3 Hugging Face snapshot is not fully cached for `{repo_id}` "
            f"under cache_dir={resolved_cache_dir}. "
            f"Prefetch first: {PREFETCH_CLI_HINT}"
        )
    if not is_snapshot_weights_complete(snapshot_path):
        raise RuntimeError(
            f"BGE-M3 Hugging Face snapshot is incomplete for `{repo_id}` at path={snapshot_path} "
            f"(missing model weights). Re-run prefetch: {PREFETCH_CLI_HINT}"
        )
    return snapshot_path


def resolve_bge_m3_model_load_path(
    repo_id: str,
    *,
    cache_dir: str | Path | None = None,
    allow_remote_download: bool = False,
) -> tuple[str, bool]:
    snapshot_path = resolve_local_snapshot_path(repo_id, cache_dir=cache_dir)
    if snapshot_path is not None:
        return snapshot_path, True

    resolved_cache_dir = describe_cache_dir(cache_dir)
    if is_huggingface_offline_mode():
        raise RuntimeError(
            f"BGE-M3 snapshot cache is missing for `{repo_id}` under cache_dir={resolved_cache_dir} "
            "while offline mode is enabled. "
            f"Prefetch first: {PREFETCH_CLI_HINT}"
        )

    if allow_remote_download:
        return repo_id, False

    raise RuntimeError(
        f"BGE-M3 snapshot cache is missing for `{repo_id}` under cache_dir={resolved_cache_dir}. "
        f"Prefetch first: {PREFETCH_CLI_HINT} "
        "Remote download during embedding is disabled to avoid blocking E2E runs."
    )
