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
        notes=model_definition.notes,
    )
