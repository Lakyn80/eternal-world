from __future__ import annotations

from app.modules.embedding_models.exceptions import EmbeddingModelNotFoundError
from app.modules.embedding_models.registry import (
    DEFAULT_EMBEDDING_MODEL_CODE,
    MULTILINGUAL_LANGUAGE,
    get_default_embedding_model_definition,
    get_embedding_model_definition,
    list_embedding_model_definitions,
    normalize_embedding_model_code,
)
from app.modules.embedding_models.schemas import EmbeddingModelRead, build_embedding_model_read


def list_embedding_models(include_disabled: bool = False) -> list[EmbeddingModelRead]:
    embedding_models = []
    for model_definition in list_embedding_model_definitions():
        if not include_disabled and not model_definition.enabled:
            continue
        embedding_models.append(build_embedding_model_read(model_definition))

    return embedding_models


def get_enabled_embedding_models() -> list[EmbeddingModelRead]:
    return list_embedding_models(include_disabled=False)


def validate_embedding_model_code(model_code: str) -> str:
    normalized_model_code = normalize_embedding_model_code(model_code)
    if get_embedding_model_definition(normalized_model_code) is None:
        raise EmbeddingModelNotFoundError("Embedding model not found")

    return normalized_model_code


def get_embedding_model(model_code: str) -> EmbeddingModelRead:
    normalized_model_code = validate_embedding_model_code(model_code)
    model_definition = get_embedding_model_definition(normalized_model_code)
    if model_definition is None:
        raise EmbeddingModelNotFoundError("Embedding model not found")

    return build_embedding_model_read(model_definition)


def get_default_embedding_model() -> EmbeddingModelRead:
    default_model_definition = get_default_embedding_model_definition()
    return build_embedding_model_read(default_model_definition)


def get_candidate_models_for_language(language: str) -> list[EmbeddingModelRead]:
    normalized_language = language.strip().lower()
    if "-" in normalized_language:
        normalized_language = normalized_language.split("-", maxsplit=1)[0]
    if "_" in normalized_language:
        normalized_language = normalized_language.split("_", maxsplit=1)[0]

    candidate_models: list[EmbeddingModelRead] = []
    for model_definition in list_embedding_model_definitions():
        if not model_definition.enabled:
            continue

        language_set = set(model_definition.languages)
        if normalized_language and normalized_language in language_set:
            candidate_models.append(build_embedding_model_read(model_definition))
            continue

        if MULTILINGUAL_LANGUAGE in language_set:
            candidate_models.append(build_embedding_model_read(model_definition))

    if candidate_models:
        return candidate_models

    default_model = get_default_embedding_model()
    if default_model.enabled and default_model.code == DEFAULT_EMBEDDING_MODEL_CODE:
        return [default_model]

    return []
