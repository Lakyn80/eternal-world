from __future__ import annotations

import argparse
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from app.core.config import settings
from app.modules.embeddings.bge_m3_model_cache import (
    BGE_M3_DEFAULT_REPO_ID,
    build_bge_m3_snapshot_download_kwargs,
    is_snapshot_weights_complete,
)
from app.modules.embedding_models.service import get_embedding_model


SUPPORTED_PREFETCH_PROVIDER_KEYS = (
    "bge_m3_dense_sparse",
    "bge_m3_dense_sparse_multivector",
    "jina_embeddings_v3",
    "qwen3_embedding_0_6b",
)
PREFETCH_DEPENDENCY_REPOS_BY_PROVIDER: dict[str, tuple[str, ...]] = {
    "bge_m3_dense_sparse": (),
    "bge_m3_dense_sparse_multivector": (),
    "jina_embeddings_v3": ("jinaai/xlm-roberta-flash-implementation",),
    "qwen3_embedding_0_6b": (),
}


@dataclass(frozen=True)
class PrefetchTarget:
    provider_key: str
    primary_repo_id: str
    dependency_repo_ids: tuple[str, ...]


def _build_prefetch_tqdm_class():
    from tqdm import tqdm

    class PrefetchTqdm(tqdm):
        def __init__(self, *args, **kwargs):
            kwargs.setdefault("mininterval", 15.0)
            super().__init__(*args, **kwargs)
            self._last_logged_at = 0.0

        def update(self, n=1):
            result = super().update(n)
            now = time.monotonic()
            if self.total and (now - self._last_logged_at >= 15.0 or self.n >= self.total):
                self._last_logged_at = now
                pct = (100.0 * self.n) / self.total
                _emit_prefetch_log(
                    f"download {self.desc or 'file'}: {self.n}/{self.total} ({pct:.1f}%)"
                )
            return result

    return PrefetchTqdm


PrefetchTqdm = _build_prefetch_tqdm_class()


def _emit_prefetch_log(message: str) -> None:
    print(f"[prefetch_embedding_model] {message}", flush=True)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Prefetch Hugging Face model assets into the backend cache.")
    parser.add_argument("--provider", required=True)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--retry-delay-seconds", type=float, default=3.0)
    return parser


def resolve_prefetch_target(provider_key: str) -> PrefetchTarget:
    normalized_provider_key = provider_key.strip().lower()
    if normalized_provider_key not in SUPPORTED_PREFETCH_PROVIDER_KEYS:
        raise ValueError(
            "Unsupported provider for prefetch. Supported providers: "
            + ", ".join(SUPPORTED_PREFETCH_PROVIDER_KEYS)
        )

    model_definition = get_embedding_model(normalized_provider_key)
    if model_definition.provider_model_name is None:
        raise ValueError(f"Provider `{normalized_provider_key}` does not define a Hugging Face model id.")

    return PrefetchTarget(
        provider_key=normalized_provider_key,
        primary_repo_id=model_definition.provider_model_name,
        dependency_repo_ids=PREFETCH_DEPENDENCY_REPOS_BY_PROVIDER.get(normalized_provider_key, ()),
    )


def _import_snapshot_download():
    try:
        from huggingface_hub import snapshot_download
    except ModuleNotFoundError as exc:
        raise RuntimeError("huggingface_hub is not installed in this environment") from exc

    return snapshot_download


def _log_cache_environment() -> None:
    if settings.sentence_transformers_cache_dir is not None:
        _emit_prefetch_log(
            f"SENTENCE_TRANSFORMERS_CACHE_DIR={settings.sentence_transformers_cache_dir}"
        )
    else:
        _emit_prefetch_log(
            "SENTENCE_TRANSFORMERS_CACHE_DIR is unset; falling back to the default "
            "Hugging Face cache location, which does not survive a container recreate "
            "unless a volume is mounted there."
        )
    for env_name in (
        "HF_HOME",
        "HUGGINGFACE_HUB_CACHE",
        "TRANSFORMERS_CACHE",
        "SENTENCE_TRANSFORMERS_HOME",
        "HF_HUB_OFFLINE",
        "TRANSFORMERS_OFFLINE",
    ):
        value = os.getenv(env_name)
        if value:
            _emit_prefetch_log(f"{env_name}={value}")


def _resolve_hf_cache_dir() -> Path | None:
    if settings.sentence_transformers_cache_dir is not None:
        return Path(settings.sentence_transformers_cache_dir)
    for env_name in ("HUGGINGFACE_HUB_CACHE", "HF_HOME"):
        value = os.getenv(env_name)
        if value:
            return Path(value)
    return None


def _log_incomplete_downloads() -> None:
    cache_root = _resolve_hf_cache_dir()
    if cache_root is None:
        cache_root = Path.home() / ".cache" / "huggingface" / "hub"

    incomplete_files = sorted(cache_root.glob("**/*.incomplete"))
    if not incomplete_files:
        return

    for incomplete_path in incomplete_files:
        size_mb = incomplete_path.stat().st_size / (1024 * 1024)
        _emit_prefetch_log(
            f"resuming incomplete download path={incomplete_path} downloaded_so_far={size_mb:.1f}MB"
        )


def _build_snapshot_download_kwargs(
    *,
    repo_id: str,
    provider_key: str,
    local_files_only: bool,
) -> dict[str, object]:
    cache_dir = settings.sentence_transformers_cache_dir
    if repo_id == BGE_M3_DEFAULT_REPO_ID:
        kwargs = build_bge_m3_snapshot_download_kwargs(
            local_files_only=local_files_only,
            include_multivector_assets=provider_key == "bge_m3_dense_sparse_multivector",
            cache_dir=cache_dir,
        )
        if not local_files_only:
            kwargs["tqdm_class"] = PrefetchTqdm
        else:
            kwargs["tqdm_class"] = None
        return kwargs

    kwargs = {
        "repo_id": repo_id,
        "revision": None,
        "local_files_only": local_files_only,
        "max_workers": 1,
        "tqdm_class": None if local_files_only else PrefetchTqdm,
    }
    if cache_dir is not None:
        kwargs["cache_dir"] = str(cache_dir)
    return kwargs


def _prefetch_repo(
    *,
    repo_id: str,
    provider_key: str,
    snapshot_download_fn,
    retries: int,
    retry_delay_seconds: float,
) -> str:
    cached_snapshot_path: str | None = None
    try:
        snapshot_path = snapshot_download_fn(
            **_build_snapshot_download_kwargs(
                repo_id=repo_id,
                provider_key=provider_key,
                local_files_only=True,
            )
        )
        if is_snapshot_weights_complete(snapshot_path):
            cached_snapshot_path = snapshot_path
        else:
            _emit_prefetch_log(
                f"prefetch cache incomplete repo_id={repo_id} snapshot_path={snapshot_path}"
            )
    except Exception:
        cached_snapshot_path = None

    if cached_snapshot_path is not None:
        _emit_prefetch_log(
            f"prefetch cache hit repo_id={repo_id} snapshot_path={cached_snapshot_path}"
        )
        return cached_snapshot_path

    last_error: Exception | None = None
    attempts = max(1, retries)
    for attempt in range(1, attempts + 1):
        _emit_prefetch_log(f"prefetch start repo_id={repo_id} attempt={attempt}/{attempts}")
        if repo_id == BGE_M3_DEFAULT_REPO_ID:
            _emit_prefetch_log(
                "downloading only embedding runtime files (skipping onnx and other optional assets)"
            )
        _log_incomplete_downloads()
        try:
            snapshot_path = snapshot_download_fn(
                **_build_snapshot_download_kwargs(
                    repo_id=repo_id,
                    provider_key=provider_key,
                    local_files_only=False,
                )
            )
        except Exception as exc:
            last_error = exc
            _emit_prefetch_log(
                f"prefetch failed repo_id={repo_id} error={exc.__class__.__name__}: {exc}"
            )
            if attempt >= attempts:
                break
            time.sleep(max(0.0, retry_delay_seconds))
            continue

        _emit_prefetch_log(f"prefetch complete repo_id={repo_id} snapshot_path={snapshot_path}")
        if not is_snapshot_weights_complete(snapshot_path):
            raise RuntimeError(
                f"Prefetch finished but model weights are still missing for `{repo_id}`."
            )
        return snapshot_path

    assert last_error is not None
    raise RuntimeError(
        f"Failed to prefetch repo `{repo_id}` after {attempts} attempts: "
        f"{last_error.__class__.__name__}: {last_error}"
    ) from last_error


def prefetch_provider_assets(
    *,
    provider_key: str,
    retries: int = 3,
    retry_delay_seconds: float = 3.0,
    snapshot_download_fn=None,
) -> dict[str, str]:
    target = resolve_prefetch_target(provider_key)
    _log_cache_environment()
    download_fn = snapshot_download_fn or _import_snapshot_download()
    prefetched_paths: dict[str, str] = {}

    prefetched_paths[target.primary_repo_id] = _prefetch_repo(
        repo_id=target.primary_repo_id,
        provider_key=target.provider_key,
        snapshot_download_fn=download_fn,
        retries=retries,
        retry_delay_seconds=retry_delay_seconds,
    )
    for dependency_repo_id in target.dependency_repo_ids:
        prefetched_paths[dependency_repo_id] = _prefetch_repo(
            repo_id=dependency_repo_id,
            provider_key=target.provider_key,
            snapshot_download_fn=download_fn,
            retries=retries,
            retry_delay_seconds=retry_delay_seconds,
        )

    return prefetched_paths


def main() -> int:
    args = _build_parser().parse_args()
    try:
        prefetched_paths = prefetch_provider_assets(
            provider_key=args.provider,
            retries=args.retries,
            retry_delay_seconds=args.retry_delay_seconds,
        )
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    for repo_id, snapshot_path in prefetched_paths.items():
        print(f"{repo_id} -> {snapshot_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
