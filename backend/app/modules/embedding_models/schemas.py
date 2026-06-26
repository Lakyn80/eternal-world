from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class EmbeddingModelRead(BaseModel):
    code: str
    display_name: str
    provider_type: str
    dimension: int
    languages: list[str]
    max_input_tokens: int
    normalized_vectors: bool
    supports_batching: bool
    enabled: bool
    is_default: bool
    recommended_for: str
    provider_model_name: str | None
    runtime_adapter: str
    manual_only_real_eval: bool
    high_resource: bool
    real_benchmark_only: bool
    ci_safe_real_inference: bool
    supports_task_adapters: bool
    supports_long_context: bool
    planning_tags: list[str]
    supported_retrieval_modes: list[str]
    notes: str


def build_embedding_model_read(model_definition: Any) -> EmbeddingModelRead:
    return EmbeddingModelRead(
        code=model_definition.code,
        display_name=model_definition.display_name,
        provider_type=model_definition.provider_type,
        dimension=model_definition.dimension,
        languages=list(model_definition.languages),
        max_input_tokens=model_definition.max_input_tokens,
        normalized_vectors=model_definition.normalized_vectors,
        supports_batching=model_definition.supports_batching,
        enabled=model_definition.enabled,
        is_default=model_definition.is_default,
        recommended_for=model_definition.recommended_for,
        provider_model_name=model_definition.provider_model_name,
        runtime_adapter=model_definition.runtime_adapter,
        manual_only_real_eval=model_definition.manual_only_real_eval,
        high_resource=model_definition.high_resource,
        real_benchmark_only=model_definition.real_benchmark_only,
        ci_safe_real_inference=model_definition.ci_safe_real_inference,
        supports_task_adapters=model_definition.supports_task_adapters,
        supports_long_context=model_definition.supports_long_context,
        planning_tags=list(model_definition.planning_tags),
        supported_retrieval_modes=list(model_definition.supported_retrieval_modes),
        notes=model_definition.notes,
    )
