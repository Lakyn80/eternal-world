"""Unit tests for auto-creating the active memory Qdrant collection."""

from __future__ import annotations

from app.modules.qdrant_indexing.memory_collection import resolve_or_create_collection_dimension


class RecordingWriter:
    def __init__(self, *, initial_size: int | None = None, create_fails: bool = False) -> None:
        self._size = initial_size
        self.create_fails = create_fails
        self.ensure_calls: list[tuple[str, int]] = []

    def collection_vector_size(self, *, collection_name: str) -> int | None:
        del collection_name
        return self._size

    def ensure_collection(self, *, collection_name: str, vector_size: int) -> None:
        self.ensure_calls.append((collection_name, vector_size))
        if self.create_fails:
            return
        self._size = vector_size


def test_resolve_or_create_returns_existing_without_ensure():
    writer = RecordingWriter(initial_size=1024)

    dimension = resolve_or_create_collection_dimension(
        writer,
        collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse",
        vector_size=1024,
    )

    assert dimension == 1024
    assert writer.ensure_calls == []


def test_resolve_or_create_creates_missing_collection():
    writer = RecordingWriter(initial_size=None)

    dimension = resolve_or_create_collection_dimension(
        writer,
        collection_name="eternal_world_rag_chunks__bge_m3_dense_sparse",
        vector_size=1024,
    )

    assert dimension == 1024
    assert writer.ensure_calls == [
        ("eternal_world_rag_chunks__bge_m3_dense_sparse", 1024),
    ]


def test_resolve_or_create_returns_none_when_create_does_not_materialize():
    writer = RecordingWriter(initial_size=None, create_fails=True)

    dimension = resolve_or_create_collection_dimension(
        writer,
        collection_name="missing",
        vector_size=1024,
    )

    assert dimension is None
    assert writer.ensure_calls == [("missing", 1024)]
