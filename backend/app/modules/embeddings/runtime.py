from __future__ import annotations

from dataclasses import dataclass

from app.core.config import settings
from app.modules.embedding_models.registry import BGE_M3_HYBRID_ADAPTER
from app.modules.embedding_models.service import get_embedding_model
from app.modules.embeddings.providers import MOCK_PROVIDER_NAME, build_embedding_provider
from app.modules.embeddings.bge_m3_model_cache import (
    BGE_M3_DEFAULT_REPO_ID,
    is_huggingface_offline_mode,
    resolve_local_snapshot_path,
)
from app.modules.embeddings.providers.bge_m3_hybrid import (
    BGE_M3_HYBRID_PROVIDER_NAME,
    BgeM3HybridEmbeddingAdapter,
)
from app.modules.embeddings.providers.mock import MockEmbeddingProvider
from app.modules.qdrant_indexing.client import build_qdrant_client


@dataclass(frozen=True)
class EmbeddingRuntimeDiagnostics:
    embedding_provider_setting: str
    resolved_indexing_provider_name: str
    resolved_query_provider_name: str
    is_mock_indexing_provider: bool
    is_mock_query_provider: bool
    indexing_query_providers_match: bool
    model_code: str
    model_display_name: str
    provider_model_name: str | None
    embedding_dimension: int
    collection_name: str
    collection_vector_size: int | None
    flag_embedding_available: bool
    bge_m3_snapshot_cached: bool = False
    bge_m3_snapshot_path: str | None = None
    huggingface_offline_mode: bool = False


def _flag_embedding_available() -> bool:
    try:
        import FlagEmbedding  # noqa: F401
    except ImportError:
        return False
    return True


def _resolve_runtime_adapter_name(*, model_code: str) -> str:
    provider = build_embedding_provider(model_code=model_code)
    if isinstance(provider, BgeM3HybridEmbeddingAdapter):
        return BGE_M3_HYBRID_PROVIDER_NAME
    if isinstance(provider, MockEmbeddingProvider):
        return MOCK_PROVIDER_NAME
    return provider.__class__.__name__


def _resolve_query_provider_name(*, model_code: str) -> str:
    model = get_embedding_model(model_code)
    if model.runtime_adapter == BGE_M3_HYBRID_ADAPTER:
        if (
            settings.embedding_provider == "sentence_transformers"
            and _flag_embedding_available()
        ):
            return BGE_M3_HYBRID_PROVIDER_NAME
        return MOCK_PROVIDER_NAME

    indexing_provider_name = _resolve_runtime_adapter_name(model_code=model_code)
    return indexing_provider_name


def build_embedding_runtime_fingerprint(*, model_code: str) -> str:
    model = get_embedding_model(model_code)
    indexing_provider_name = _resolve_runtime_adapter_name(model_code=model_code)
    query_provider_name = _resolve_query_provider_name(model_code=model_code)
    fingerprint = (
        f"{settings.embedding_provider}:{model_code}:"
        f"index={indexing_provider_name}:query={query_provider_name}"
    )
    if model.provider_model_name:
        fingerprint += f":provider_model={model.provider_model_name}"

    if model.runtime_adapter == BGE_M3_HYBRID_ADAPTER:
        snapshot_path = resolve_local_snapshot_path(
            model.provider_model_name or BGE_M3_DEFAULT_REPO_ID,
            cache_dir=settings.sentence_transformers_cache_dir,
        )
        snapshot_revision = None
        if snapshot_path:
            snapshot_revision = snapshot_path.rstrip("/").split("/")[-1]
        fingerprint += f":snapshot={snapshot_revision or 'missing'}"

    return fingerprint


def resolve_embedding_runtime_diagnostics(
    *,
    model_code: str,
    collection_name: str,
) -> EmbeddingRuntimeDiagnostics:
    model = get_embedding_model(model_code)
    indexing_provider_name = _resolve_runtime_adapter_name(model_code=model_code)
    query_provider_name = _resolve_query_provider_name(model_code=model_code)
    collection_vector_size: int | None = None
    try:
        qdrant_client = build_qdrant_client()
        collection_vector_size = qdrant_client.get_collection_vector_size(
            collection_name=collection_name
        )
    except Exception:
        collection_vector_size = None

    bge_m3_snapshot_path: str | None = None
    bge_m3_snapshot_cached = False
    if model.runtime_adapter == BGE_M3_HYBRID_ADAPTER:
        repo_id = model.provider_model_name or BGE_M3_DEFAULT_REPO_ID
        bge_m3_snapshot_path = resolve_local_snapshot_path(
            repo_id,
            cache_dir=settings.sentence_transformers_cache_dir,
        )
        bge_m3_snapshot_cached = bge_m3_snapshot_path is not None

    return EmbeddingRuntimeDiagnostics(
        embedding_provider_setting=settings.embedding_provider,
        resolved_indexing_provider_name=indexing_provider_name,
        resolved_query_provider_name=query_provider_name,
        is_mock_indexing_provider=indexing_provider_name == MOCK_PROVIDER_NAME,
        is_mock_query_provider=query_provider_name == MOCK_PROVIDER_NAME,
        indexing_query_providers_match=indexing_provider_name == query_provider_name,
        model_code=model.code,
        model_display_name=model.display_name,
        provider_model_name=model.provider_model_name,
        embedding_dimension=model.dimension,
        collection_name=collection_name,
        collection_vector_size=collection_vector_size,
        flag_embedding_available=_flag_embedding_available(),
        bge_m3_snapshot_cached=bge_m3_snapshot_cached,
        bge_m3_snapshot_path=bge_m3_snapshot_path,
        huggingface_offline_mode=is_huggingface_offline_mode(),
    )


def assert_real_embedding_runtime_for_e2e(
    *,
    model_code: str,
    collection_name: str,
    allow_mock_embeddings: bool = False,
) -> EmbeddingRuntimeDiagnostics:
    diagnostics = resolve_embedding_runtime_diagnostics(
        model_code=model_code,
        collection_name=collection_name,
    )
    if allow_mock_embeddings:
        return diagnostics

    issues: list[str] = []
    if diagnostics.embedding_provider_setting != "sentence_transformers":
        issues.append(
            "EMBEDDING_PROVIDER must be sentence_transformers for real-retrieval E2E "
            f"(current: {diagnostics.embedding_provider_setting})."
        )
    if diagnostics.is_mock_indexing_provider:
        issues.append(
            "Indexing embedding provider resolves to mock for "
            f"{diagnostics.model_code}."
        )
    if diagnostics.is_mock_query_provider:
        issues.append(
            "Query embedding provider resolves to mock for "
            f"{diagnostics.model_code}."
        )
    if not diagnostics.indexing_query_providers_match:
        issues.append(
            "Indexing and query embedding providers do not match: "
            f"{diagnostics.resolved_indexing_provider_name} vs "
            f"{diagnostics.resolved_query_provider_name}."
        )
    if not diagnostics.flag_embedding_available:
        issues.append("FlagEmbedding is not available in the runtime environment.")
    if diagnostics.model_code.startswith("bge_m3") and not diagnostics.bge_m3_snapshot_cached:
        issues.append(
            "BGE-M3 Hugging Face snapshot is missing or incomplete (model weights not cached). "
            "Re-run prefetch: docker compose exec backend python scripts/prefetch_embedding_model.py "
            "--provider bge_m3_dense_sparse"
        )
    if (
        diagnostics.collection_vector_size is not None
        and diagnostics.collection_vector_size != diagnostics.embedding_dimension
    ):
        issues.append(
            "Qdrant collection vector size "
            f"{diagnostics.collection_vector_size} does not match model dimension "
            f"{diagnostics.embedding_dimension}."
        )

    if issues:
        raise RuntimeError(
            "Real-retrieval E2E requires real embedding runtime. "
            + " ".join(issues)
            + " Pass --allow-mock-embeddings only for explicit mock diagnostics."
        )

    return diagnostics
