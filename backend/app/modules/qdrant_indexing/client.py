from __future__ import annotations

from typing import Any

import httpx

from app.core.config import settings
from app.modules.qdrant_indexing.exceptions import QdrantClientError, QdrantCollectionConfigurationError


DISTANCE_METRIC = "Cosine"


def _extract_vector_size(collection_payload: dict[str, Any]) -> int | None:
    result = collection_payload.get("result")
    if not isinstance(result, dict):
        return None

    config = result.get("config")
    if not isinstance(config, dict):
        return None

    params = config.get("params")
    if not isinstance(params, dict):
        return None

    vectors = params.get("vectors")
    if isinstance(vectors, dict):
        if "size" in vectors:
            size = vectors.get("size")
            return int(size) if isinstance(size, (int, float)) else None

        for key in ("default", ""):
            candidate = vectors.get(key)
            if isinstance(candidate, dict) and "size" in candidate:
                size = candidate.get("size")
                return int(size) if isinstance(size, (int, float)) else None

    return None


class QdrantRestClient:
    def __init__(self, *, base_url: str, timeout_seconds: float) -> None:
        self._base_url = base_url.rstrip("/")
        self._timeout_seconds = timeout_seconds

    def _request(self, method: str, path: str, **kwargs) -> httpx.Response:
        try:
            with httpx.Client(base_url=self._base_url, timeout=self._timeout_seconds) as client:
                response = client.request(method, path, **kwargs)
                return response
        except httpx.HTTPError as exc:
            raise QdrantClientError("Qdrant request failed") from exc

    def delete_collection(self, *, collection_name: str) -> bool:
        response = self._request("DELETE", f"/collections/{collection_name}")
        if response.status_code == 404:
            return False
        if response.is_error:
            raise QdrantClientError("Qdrant collection deletion failed")
        return True

    def get_collection_vector_size(self, *, collection_name: str) -> int | None:
        response = self._request("GET", f"/collections/{collection_name}")
        if response.status_code == 404:
            return None
        if response.is_error:
            raise QdrantClientError("Qdrant collection check failed")
        return _extract_vector_size(response.json())

    def count_points(
        self,
        *,
        collection_name: str,
        search_filter: dict[str, object] | None = None,
        exact: bool = True,
    ) -> int:
        request_body: dict[str, object] = {"exact": exact}
        if search_filter is not None:
            request_body["filter"] = search_filter

        response = self._request(
            "POST",
            f"/collections/{collection_name}/points/count",
            json=request_body,
        )
        if response.status_code == 404:
            return 0
        if response.is_error:
            raise QdrantClientError("Qdrant point count failed")

        response_payload = response.json()
        result = response_payload.get("result")
        if not isinstance(result, dict):
            return 0

        count = result.get("count")
        if isinstance(count, bool):
            return 0
        if isinstance(count, int):
            return count
        if isinstance(count, float):
            return int(count)
        return 0

    def scroll_points(
        self,
        *,
        collection_name: str,
        limit: int,
        search_filter: dict[str, object] | None = None,
        with_payload: bool = True,
        with_vector: bool = False,
    ) -> list[dict[str, object]]:
        request_body: dict[str, object] = {
            "limit": limit,
            "with_payload": with_payload,
            "with_vector": with_vector,
        }
        if search_filter is not None:
            request_body["filter"] = search_filter

        response = self._request(
            "POST",
            f"/collections/{collection_name}/points/scroll",
            json=request_body,
        )
        if response.status_code == 404:
            return []
        if response.is_error:
            raise QdrantClientError("Qdrant point scroll failed")

        response_payload = response.json()
        result = response_payload.get("result")
        if not isinstance(result, dict):
            return []

        points = result.get("points")
        if not isinstance(points, list):
            return []

        normalized_points: list[dict[str, object]] = []
        for item in points:
            if isinstance(item, dict):
                normalized_points.append(item)
        return normalized_points

    def ensure_collection(self, *, collection_name: str, vector_size: int) -> None:
        response = self._request("GET", f"/collections/{collection_name}")

        if response.status_code == 404:
            self._create_collection(collection_name=collection_name, vector_size=vector_size)
            return

        if response.is_error:
            raise QdrantClientError("Qdrant collection check failed")

        existing_vector_size = _extract_vector_size(response.json())
        if existing_vector_size is None:
            raise QdrantCollectionConfigurationError("Qdrant collection metadata is invalid")

        if existing_vector_size != vector_size:
            raise QdrantCollectionConfigurationError("Qdrant collection is incompatible with embedding dimension")

    def _create_collection(self, *, collection_name: str, vector_size: int) -> None:
        response = self._request(
            "PUT",
            f"/collections/{collection_name}",
            json={
                "vectors": {
                    "size": vector_size,
                    "distance": DISTANCE_METRIC,
                }
            },
        )
        if response.is_error:
            raise QdrantClientError("Qdrant collection creation failed")

    def upsert_point(
        self,
        *,
        collection_name: str,
        point_id: str,
        vector: list[float],
        payload: dict[str, object],
    ) -> None:
        response = self._request(
            "PUT",
            f"/collections/{collection_name}/points",
            params={"wait": "true"},
            json={
                "points": [
                    {
                        "id": point_id,
                        "vector": vector,
                        "payload": payload,
                    }
                ]
            },
        )
        if response.is_error:
            raise QdrantClientError("Qdrant point upsert failed")

    def get_point(
        self,
        *,
        collection_name: str,
        point_id: str,
        with_vector: bool = False,
    ) -> dict[str, object] | None:
        response = self._request(
            "GET",
            f"/collections/{collection_name}/points/{point_id}",
            params={"with_payload": "true", "with_vector": str(with_vector).lower()},
        )
        if response.status_code == 404:
            return None
        if response.is_error:
            raise QdrantClientError("Qdrant point lookup failed")
        result = response.json().get("result")
        return result if isinstance(result, dict) else None

    def delete_point(self, *, collection_name: str, point_id: str) -> None:
        response = self._request(
            "POST",
            f"/collections/{collection_name}/points/delete",
            params={"wait": "true"},
            json={"points": [point_id]},
        )
        if response.is_error:
            raise QdrantClientError("Qdrant point deletion failed")

    def search_points(
        self,
        *,
        collection_name: str,
        vector: list[float],
        limit: int,
        search_filter: dict[str, object] | None = None,
        score_threshold: float | None = None,
    ) -> list[dict[str, object]]:
        request_body: dict[str, object] = {
            "vector": vector,
            "limit": limit,
            "with_payload": True,
        }
        if search_filter is not None:
            request_body["filter"] = search_filter
        if score_threshold is not None:
            request_body["score_threshold"] = score_threshold

        response = self._request(
            "POST",
            f"/collections/{collection_name}/points/search",
            json=request_body,
        )

        if response.status_code == 404:
            return []

        if response.is_error:
            raise QdrantClientError("Qdrant point search failed")

        response_payload = response.json()
        result = response_payload.get("result")
        if not isinstance(result, list):
            return []

        normalized_results: list[dict[str, object]] = []
        for item in result:
            if isinstance(item, dict):
                normalized_results.append(item)

        return normalized_results


def build_qdrant_client() -> QdrantRestClient:
    return QdrantRestClient(
        base_url=settings.qdrant_url,
        timeout_seconds=settings.qdrant_timeout_seconds,
    )
