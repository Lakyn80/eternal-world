from __future__ import annotations

import importlib
from typing import Any

from rag_eval.adapters.base import RagEvalBackend
from rag_eval.adapters.eternal_world import EternalWorldRagEvalBackend
from rag_eval.adapters.sql_qdrant import SqlQdrantRagEvalBackend
from rag_eval.config import BenchmarkConfig


def _load_custom_backend(*, config: BenchmarkConfig) -> RagEvalBackend:
    if config.adapter is None:
        raise ValueError("backend=custom requires adapter.module and adapter.class in config.")

    module = importlib.import_module(config.adapter.module)
    adapter_class = getattr(module, config.adapter.class_name)
    kwargs: dict[str, Any] = dict(config.adapter.kwargs)
    kwargs.setdefault("config", config)
    return adapter_class(**kwargs)


def build_backend(config: BenchmarkConfig, *, backend_root: str | None = None) -> RagEvalBackend:
    if config.backend == "memory":
        raise ValueError("Memory backend must be constructed directly in tests.")
    if config.backend == "eternal_world":
        return EternalWorldRagEvalBackend(config=config, backend_root=backend_root)
    if config.backend == "sql_qdrant":
        return SqlQdrantRagEvalBackend(config=config)
    if config.backend == "custom":
        return _load_custom_backend(config=config)
    raise ValueError(
        f"Unsupported backend: {config.backend}. "
        "Use eternal_world, sql_qdrant, or custom."
    )
