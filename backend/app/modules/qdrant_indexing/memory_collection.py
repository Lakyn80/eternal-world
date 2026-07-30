"""Ensure the active memory-retrieval Qdrant collection exists.

Used by biography / avatar-memory / contribution indexing so a fresh Qdrant
(local or staging) does not skip jobs with "Target memory collection does
not exist".
"""

from __future__ import annotations

from typing import Protocol


class MemoryCollectionWriter(Protocol):
    def collection_vector_size(self, *, collection_name: str) -> int | None: ...

    def ensure_collection(self, *, collection_name: str, vector_size: int) -> None: ...


def resolve_or_create_collection_dimension(
    writer: MemoryCollectionWriter,
    *,
    collection_name: str,
    vector_size: int,
) -> int | None:
    """Return the collection dense vector size, creating the collection if missing.

    Returns ``None`` only when creation/re-read still cannot observe a size
    (caller maps that to its domain eligibility error).
    """

    existing = writer.collection_vector_size(collection_name=collection_name)
    if existing is not None:
        return existing

    writer.ensure_collection(collection_name=collection_name, vector_size=vector_size)
    return writer.collection_vector_size(collection_name=collection_name)
