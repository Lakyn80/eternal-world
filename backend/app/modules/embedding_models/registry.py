from __future__ import annotations

from dataclasses import dataclass


LOCAL_PROVIDER_TYPE = "local"
EXTERNAL_PROVIDER_TYPE = "external"
MOCK_PROVIDER_TYPE = "mock"
MULTILINGUAL_LANGUAGE = "multilingual"
DEFAULT_EMBEDDING_MODEL_CODE = "multilingual_e5_small"
SENTENCE_TRANSFORMERS_ADAPTER = "sentence_transformers"
BGE_M3_HYBRID_ADAPTER = "bge_m3_hybrid"
PLANNED_MANUAL_ONLY_ADAPTER = "planned_manual_only"

BGE_M3_DENSE_RETRIEVAL_MODE = "bge_m3_dense"
BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE = "bge_m3_dense_sparse"
BGE_M3_DENSE_SPARSE_MULTIVECTOR_RETRIEVAL_MODE = "bge_m3_dense_sparse_multivector"
BGE_M3_FUTURE_RETRIEVAL_MODES = (
    BGE_M3_DENSE_RETRIEVAL_MODE,
    BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE,
    BGE_M3_DENSE_SPARSE_MULTIVECTOR_RETRIEVAL_MODE,
)


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
    provider_model_name: str | None
    runtime_adapter: str
    manual_only_real_eval: bool
    high_resource: bool
    real_benchmark_only: bool
    ci_safe_real_inference: bool
    supports_task_adapters: bool
    supports_long_context: bool
    planning_tags: tuple[str, ...]
    supported_retrieval_modes: tuple[str, ...]
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
        provider_model_name="intfloat/multilingual-e5-small",
        runtime_adapter=SENTENCE_TRANSFORMERS_ADAPTER,
        manual_only_real_eval=False,
        high_resource=False,
        real_benchmark_only=False,
        ci_safe_real_inference=True,
        supports_task_adapters=False,
        supports_long_context=False,
        planning_tags=("dense_only", "baseline", "ci_safe_fake"),
        supported_retrieval_modes=("dense",),
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
        provider_model_name="BAAI/bge-m3",
        runtime_adapter=SENTENCE_TRANSFORMERS_ADAPTER,
        manual_only_real_eval=True,
        high_resource=True,
        real_benchmark_only=False,
        ci_safe_real_inference=False,
        supports_task_adapters=False,
        supports_long_context=True,
        planning_tags=("dense_only_current", "hybrid_future", "manual_only_real_eval"),
        supported_retrieval_modes=BGE_M3_FUTURE_RETRIEVAL_MODES,
        notes="Reserved for higher-quality multilingual retrieval experiments once real embedding execution is enabled.",
    ),
    EmbeddingModelDefinition(
        code="bge_m3_dense_sparse",
        display_name="BGE M3 Dense + Sparse",
        provider_type=LOCAL_PROVIDER_TYPE,
        dimension=1024,
        languages=("ru", "cs", "en", MULTILINGUAL_LANGUAGE),
        max_input_tokens=8192,
        normalized_vectors=True,
        supports_batching=True,
        enabled=True,
        is_default=False,
        recommended_for="production hybrid multilingual retrieval",
        provider_model_name="BAAI/bge-m3",
        runtime_adapter=BGE_M3_HYBRID_ADAPTER,
        manual_only_real_eval=False,
        high_resource=True,
        real_benchmark_only=False,
        ci_safe_real_inference=False,
        supports_task_adapters=False,
        supports_long_context=True,
        planning_tags=("bge_m3", "dense_sparse", "production_hybrid"),
        supported_retrieval_modes=(BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE,),
        notes=(
            "Production BGE-M3 dense+sparse hybrid retrieval. Dense vectors are indexed in Qdrant and "
            "sparse lexical weights are stored in point payload for deterministic fusion at query time."
        ),
    ),
    EmbeddingModelDefinition(
        code="bge_m3_dense_sparse_multivector",
        display_name="BGE M3 Dense + Sparse + Multivector",
        provider_type=LOCAL_PROVIDER_TYPE,
        dimension=1024,
        languages=("ru", "cs", "en", MULTILINGUAL_LANGUAGE),
        max_input_tokens=8192,
        normalized_vectors=True,
        supports_batching=True,
        enabled=False,
        is_default=False,
        recommended_for="manual benchmark batch for full BGE-M3 dense+sparse+multivector retrieval",
        provider_model_name="BAAI/bge-m3",
        runtime_adapter=PLANNED_MANUAL_ONLY_ADAPTER,
        manual_only_real_eval=True,
        high_resource=True,
        real_benchmark_only=True,
        ci_safe_real_inference=False,
        supports_task_adapters=False,
        supports_long_context=True,
        planning_tags=("bge_m3", "dense_sparse_multivector", "manual_only_real_eval", "batch_d"),
        supported_retrieval_modes=(BGE_M3_DENSE_SPARSE_MULTIVECTOR_RETRIEVAL_MODE,),
        notes=(
            "Manual-only full-hybrid benchmark target for local Batch D evaluation. "
            "Uses dense embeddings, sparse lexical weights, and late-interaction multivector reranking "
            "in a local manual reranking path; it is intentionally disabled outside guarded benchmark execution."
        ),
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
        provider_model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
        runtime_adapter=SENTENCE_TRANSFORMERS_ADAPTER,
        manual_only_real_eval=False,
        high_resource=False,
        real_benchmark_only=False,
        ci_safe_real_inference=True,
        supports_task_adapters=False,
        supports_long_context=False,
        planning_tags=("dense_only", "baseline", "ci_safe_fake"),
        supported_retrieval_modes=("dense",),
        notes="Dense-only SentenceTransformers adapter reserved for future three-model multilingual retrieval evaluation.",
    ),
    EmbeddingModelDefinition(
        code="multilingual_e5_base",
        display_name="Multilingual E5 Base",
        provider_type=LOCAL_PROVIDER_TYPE,
        dimension=768,
        languages=("ru", "cs", "en", MULTILINGUAL_LANGUAGE),
        max_input_tokens=512,
        normalized_vectors=True,
        supports_batching=True,
        enabled=True,
        is_default=False,
        recommended_for="fourth multilingual retrieval baseline",
        provider_model_name="intfloat/multilingual-e5-base",
        runtime_adapter=SENTENCE_TRANSFORMERS_ADAPTER,
        manual_only_real_eval=False,
        high_resource=False,
        real_benchmark_only=False,
        ci_safe_real_inference=True,
        supports_task_adapters=False,
        supports_long_context=False,
        planning_tags=("dense_only", "baseline", "ci_safe_fake"),
        supported_retrieval_modes=("dense",),
        notes="Dense-only SentenceTransformers adapter reserved for future incremental multilingual retrieval evaluation against the historical E5-small baseline.",
    ),
    EmbeddingModelDefinition(
        code="multilingual_e5_large",
        display_name="Multilingual E5 Large",
        provider_type=LOCAL_PROVIDER_TYPE,
        dimension=1024,
        languages=("ru", "cs", "en", MULTILINGUAL_LANGUAGE),
        max_input_tokens=512,
        normalized_vectors=True,
        supports_batching=True,
        enabled=True,
        is_default=False,
        recommended_for="next larger dense multilingual benchmark candidate",
        provider_model_name="intfloat/multilingual-e5-large",
        runtime_adapter=SENTENCE_TRANSFORMERS_ADAPTER,
        manual_only_real_eval=True,
        high_resource=True,
        real_benchmark_only=False,
        ci_safe_real_inference=False,
        supports_task_adapters=False,
        supports_long_context=False,
        planning_tags=("dense_only", "benchmark_batch_a", "manual_only_real_eval"),
        supported_retrieval_modes=("dense",),
        notes="Full-version benchmark candidate added as a lazy-loaded SentenceTransformers adapter; real inference stays manual-only.",
    ),
    EmbeddingModelDefinition(
        code="qwen3_embedding_0_6b",
        display_name="Qwen3 Embedding 0.6B",
        provider_type=LOCAL_PROVIDER_TYPE,
        dimension=1024,
        languages=("ru", "cs", "en", MULTILINGUAL_LANGUAGE),
        max_input_tokens=32768,
        normalized_vectors=True,
        supports_batching=True,
        enabled=False,
        is_default=False,
        recommended_for="manual benchmark batch for compact Qwen embedding baseline",
        provider_model_name="Qwen/Qwen3-Embedding-0.6B",
        runtime_adapter=SENTENCE_TRANSFORMERS_ADAPTER,
        manual_only_real_eval=True,
        high_resource=True,
        real_benchmark_only=True,
        ci_safe_real_inference=False,
        supports_task_adapters=False,
        supports_long_context=True,
        planning_tags=("qwen3", "manual_only_real_eval", "high_resource", "not_ci_safe"),
        supported_retrieval_modes=("dense",),
        notes=(
            "Qwen3 0.6B benchmark was attempted but not completed in this local Docker runtime; "
            "keep the adapter available, but treat it as manual-only and not verified in this environment."
        ),
    ),
    EmbeddingModelDefinition(
        code="qwen3_embedding_4b",
        display_name="Qwen3 Embedding 4B",
        provider_type=LOCAL_PROVIDER_TYPE,
        dimension=2560,
        languages=("ru", "cs", "en", MULTILINGUAL_LANGUAGE),
        max_input_tokens=32768,
        normalized_vectors=True,
        supports_batching=True,
        enabled=False,
        is_default=False,
        recommended_for="manual benchmark batch for stronger Qwen embedding baseline",
        provider_model_name="Qwen/Qwen3-Embedding-4B",
        runtime_adapter=SENTENCE_TRANSFORMERS_ADAPTER,
        manual_only_real_eval=True,
        high_resource=True,
        real_benchmark_only=True,
        ci_safe_real_inference=False,
        supports_task_adapters=False,
        supports_long_context=True,
        planning_tags=("qwen3", "manual_only_real_eval", "high_resource", "benchmark_batch_e"),
        supported_retrieval_modes=("dense",),
        notes=(
            "Qwen3 4B manual-only real benchmark provider for optional Batch E; "
            "plain-text SentenceTransformers encoding without provider-specific retrieval instructions."
        ),
    ),
    EmbeddingModelDefinition(
        code="qwen3_embedding_8b",
        display_name="Qwen3 Embedding 8B",
        provider_type=LOCAL_PROVIDER_TYPE,
        dimension=4096,
        languages=("ru", "cs", "en", MULTILINGUAL_LANGUAGE),
        max_input_tokens=40960,
        normalized_vectors=True,
        supports_batching=True,
        enabled=False,
        is_default=False,
        recommended_for="manual benchmark batch for largest Qwen embedding baseline",
        provider_model_name="Qwen/Qwen3-Embedding-8B",
        runtime_adapter=SENTENCE_TRANSFORMERS_ADAPTER,
        manual_only_real_eval=True,
        high_resource=True,
        real_benchmark_only=True,
        ci_safe_real_inference=False,
        supports_task_adapters=False,
        supports_long_context=True,
        planning_tags=("qwen3", "manual_only_real_eval", "high_resource", "benchmark_batch_f"),
        supported_retrieval_modes=("dense",),
        notes=(
            "Qwen3 8B manual-only real benchmark provider for optional Batch F; "
            "plain-text SentenceTransformers encoding without provider-specific retrieval instructions."
        ),
    ),
    EmbeddingModelDefinition(
        code="jina_embeddings_v3",
        display_name="Jina Embeddings v3",
        provider_type=LOCAL_PROVIDER_TYPE,
        dimension=1024,
        languages=("ru", "cs", "en", MULTILINGUAL_LANGUAGE),
        max_input_tokens=8192,
        normalized_vectors=True,
        supports_batching=True,
        enabled=False,
        is_default=False,
        recommended_for="manual benchmark batch for long-context multilingual retrieval",
        provider_model_name="jinaai/jina-embeddings-v3",
        runtime_adapter=SENTENCE_TRANSFORMERS_ADAPTER,
        manual_only_real_eval=True,
        high_resource=True,
        real_benchmark_only=True,
        ci_safe_real_inference=False,
        supports_task_adapters=True,
        supports_long_context=True,
        planning_tags=("manual_only_real_eval", "long_context", "task_adapters", "not_ci_safe"),
        supported_retrieval_modes=("dense",),
        notes="Manual-only Jina Embeddings v3 foundation for later benchmark batches; keep disabled to avoid accidental API or local runtime usage.",
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
        provider_model_name=None,
        runtime_adapter="mock",
        manual_only_real_eval=False,
        high_resource=False,
        real_benchmark_only=False,
        ci_safe_real_inference=True,
        supports_task_adapters=False,
        supports_long_context=False,
        planning_tags=("tests_only",),
        supported_retrieval_modes=("dense",),
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
