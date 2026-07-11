from __future__ import annotations

from typing import Protocol

from app.core.config import settings
from app.modules.qdrant_indexing.client import QdrantRestClient, build_qdrant_client


class AvatarMemoryQdrantWriter(Protocol):
    def collection_vector_size(self, *, collection_name: str) -> int | None: ...

    def get_point(self, *, collection_name: str, point_id: str) -> dict[str, object] | None: ...

    def upsert_point(
        self,
        *,
        collection_name: str,
        point_id: str,
        vector: list[float],
        payload: dict[str, object],
    ) -> None: ...

    def delete_point(self, *, collection_name: str, point_id: str) -> None: ...


class DefaultAvatarMemoryQdrantWriter:
    def __init__(self, *, qdrant_url: str | None = None) -> None:
        self._client = (
            QdrantRestClient(base_url=qdrant_url, timeout_seconds=settings.qdrant_timeout_seconds)
            if qdrant_url is not None
            else build_qdrant_client()
        )

    def collection_vector_size(self, *, collection_name: str) -> int | None:
        return self._client.get_collection_vector_size(collection_name=collection_name)

    def get_point(self, *, collection_name: str, point_id: str) -> dict[str, object] | None:
        return self._client.get_point(collection_name=collection_name, point_id=point_id)

    def upsert_point(
        self,
        *,
        collection_name: str,
        point_id: str,
        vector: list[float],
        payload: dict[str, object],
    ) -> None:
        self._client.upsert_point(
            collection_name=collection_name,
            point_id=point_id,
            vector=vector,
            payload=payload,
        )

    def delete_point(self, *, collection_name: str, point_id: str) -> None:
        self._client.delete_point(collection_name=collection_name, point_id=point_id)
