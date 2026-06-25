from __future__ import annotations

from dataclasses import dataclass


LOCAL_PROVIDER_TYPE = "local"
EXTERNAL_PROVIDER_TYPE = "external"
MOCK_PROVIDER_TYPE = "mock"
MULTILINGUAL_LANGUAGE = "multilingual"
DEFAULT_EMBEDDING_MODEL_CODE = "multilingual_e5_small"


@dataclass(frozen=True)
class EmbeddingModelDefinition:
    code: str
    display_name: str
    provider_type: str
    dimension: int
    languages: tuple[str, ...]
    max_input_tokens: int
    normalized_vectors: bool
    supports_batching: bool
    enabled: bool
    is_default: bool
    recommended_for: str
    notes: str


EMBEDDING_MODEL_DEFINITIONS: tuple[EmbeddingModelDefinition, ...] = (
    EmbeddingModelDefinition(
        code="multilingual_e5_small",
        display_name="Multilingual E5 Small",
        provider_type=LOCAL_PROVIDER_TYPE,
        dimension=384,
        languages=("ru", "cs", "en", MULTILINGUAL_LANGUAGE),
        max_input_tokens=512,
        normalized_vectors=True,
        supports_batching=True,
        enabled=True,
        is_default=True,
        recommended_for="cheap/default/local MVP",
        notes="Stable local-first default for future chunk embeddings and retrieval baselines.",
    ),
    EmbeddingModelDefinition(
        code="bge_m3",
        display_name="BGE M3",
        provider_type=LOCAL_PROVIDER_TYPE,
        dimension=1024,
        languages=("ru", "cs", "en", MULTILINGUAL_LANGUAGE),
        max_input_tokens=8192,
        normalized_vectors=True,
        supports_batching=True,
        enabled=True,
        is_default=False,
        recommended_for="high-quality multilingual retrieval",
        notes="Reserved for higher-quality multilingual retrieval experiments once real embedding execution is enabled.",
    ),
    EmbeddingModelDefinition(
        code="paraphrase_multilingual_mpnet_base_v2",
        display_name="Paraphrase Multilingual MPNet Base v2",
        provider_type=LOCAL_PROVIDER_TYPE,
        dimension=768,
        languages=("ru", "cs", "en", MULTILINGUAL_LANGUAGE),
        max_input_tokens=512,
        normalized_vectors=True,
        supports_batching=True,
        enabled=True,
        is_default=False,
        recommended_for="third multilingual retrieval baseline",
        notes="Dense-only SentenceTransformers adapter reserved for future three-model multilingual retrieval evaluation.",
    ),
    EmbeddingModelDefinition(
        code="jina_embeddings_v3",
        display_name="Jina Embeddings v3",
        provider_type=EXTERNAL_PROVIDER_TYPE,
        dimension=1024,
        languages=("ru", "cs", "en", MULTILINGUAL_LANGUAGE),
        max_input_tokens=8192,
        normalized_vectors=True,
        supports_batching=True,
        enabled=False,
        is_default=False,
        recommended_for="external high-quality multilingual retrieval",
        notes="Known external candidate kept disabled until external embedding calls are explicitly enabled in a later slice.",
    ),
    EmbeddingModelDefinition(
        code="mock_embedding",
        display_name="Mock Embedding",
        provider_type=MOCK_PROVIDER_TYPE,
        dimension=8,
        languages=("test",),
        max_input_tokens=32,
        normalized_vectors=False,
        supports_batching=True,
        enabled=True,
        is_default=False,
        recommended_for="tests only",
        notes="Deterministic lightweight test profile for registry and future embedding pipeline tests.",
    ),
)


def _validate_registry_invariants() -> None:
    normalized_codes = [model.code.strip().lower() for model in EMBEDDING_MODEL_DEFINITIONS]
    if len(normalized_codes) != len(set(normalized_codes)):
        raise RuntimeError("Embedding model registry contains duplicate model codes.")

    default_models = [model for model in EMBEDDING_MODEL_DEFINITIONS if model.is_default]
    if len(default_models) != 1:
        raise RuntimeError("Embedding model registry must contain exactly one default model.")

    if not default_models[0].enabled:
        raise RuntimeError("Default embedding model must be enabled.")


def normalize_embedding_model_code(model_code: str) -> str:
    return model_code.strip().lower()


def list_embedding_model_definitions() -> tuple[EmbeddingModelDefinition, ...]:
    _validate_registry_invariants()
    return EMBEDDING_MODEL_DEFINITIONS


def get_embedding_model_definition(model_code: str) -> EmbeddingModelDefinition | None:
    normalized_model_code = normalize_embedding_model_code(model_code)
    for model_definition in list_embedding_model_definitions():
        if model_definition.code == normalized_model_code:
            return model_definition

    return None


def get_default_embedding_model_definition() -> EmbeddingModelDefinition:
    for model_definition in list_embedding_model_definitions():
        if model_definition.is_default:
            return model_definition

    raise RuntimeError("Default embedding model is not configured.")
