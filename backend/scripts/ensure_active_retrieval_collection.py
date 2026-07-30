"""Ensure the active memory-retrieval Qdrant collection exists.

Idempotent. Safe for local Docker and staging deploy so biography /
avatar-memory / contribution indexing does not skip with
\"Target memory collection does not exist\" on a fresh Qdrant volume.

Uses the production-recommended collection (no per-user DB lookup) so the
script can run during deploy bootstrap without a memorial owner context.
"""

from __future__ import annotations

import argparse
import sys

from app.modules.active_retrieval_config.service import (
    get_production_recommended_active_retrieval_config,
)
from app.modules.avatar_memory_indexing.qdrant_writer import DefaultAvatarMemoryQdrantWriter
from app.modules.embedding_models.service import get_embedding_model
from app.modules.qdrant_indexing.memory_collection import resolve_or_create_collection_dimension


def _emit(message: str) -> None:
    print(f"[ensure_active_retrieval_collection] {message}", flush=True)


def _build_parser() -> argparse.ArgumentParser:
    return argparse.ArgumentParser(
        description="Ensure the production-recommended retrieval Qdrant collection exists."
    )


def ensure_active_retrieval_collection() -> int:
    runtime = get_production_recommended_active_retrieval_config()
    model = get_embedding_model(runtime.model_code)
    collection_name = runtime.collection_name
    model_code = runtime.model_code
    vector_size = model.dimension

    writer = DefaultAvatarMemoryQdrantWriter()
    existing = writer.collection_vector_size(collection_name=collection_name)
    if existing is not None:
        _emit(
            f"already present collection={collection_name} model={model_code} "
            f"dimension={existing}"
        )
        if existing != vector_size:
            _emit(
                f"ERROR incompatible dimension existing={existing} expected={vector_size}"
            )
            return 1
        return 0

    dimension = resolve_or_create_collection_dimension(
        writer,
        collection_name=collection_name,
        vector_size=vector_size,
    )
    if dimension is None:
        _emit(f"ERROR failed to create collection={collection_name}")
        return 1

    _emit(
        f"created collection={collection_name} model={model_code} dimension={dimension}"
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    _build_parser().parse_args(argv)
    return ensure_active_retrieval_collection()


if __name__ == "__main__":
    sys.exit(main())
