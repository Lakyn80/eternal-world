from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field, field_validator, model_validator


DEFAULT_MODEL_CODES = (
    "bge_m3",
    "multilingual_e5_large",
    "multilingual_e5_base",
    "multilingual_e5_small",
    "paraphrase_multilingual_mpnet_base_v2",
    "qwen3_embedding_0_6b",
    "jina_embeddings_v3",
)

OPTIONAL_HIGH_RAM_MODEL_CODES = (
    "qwen3_embedding_4b",
    "qwen3_embedding_8b",
)


class BenchmarkModelsConfig(BaseModel):
    default: list[str] = Field(default_factory=lambda: list(DEFAULT_MODEL_CODES))
    optional_high_ram: list[str] = Field(default_factory=lambda: list(OPTIONAL_HIGH_RAM_MODEL_CODES))
    include_optional: bool = False

    @field_validator("default", "optional_high_ram")
    @classmethod
    def normalize_model_codes(cls, value: list[str]) -> list[str]:
        normalized: list[str] = []
        seen: set[str] = set()
        for item in value:
            normalized_item = item.strip().lower()
            if not normalized_item or normalized_item in seen:
                continue
            seen.add(normalized_item)
            normalized.append(normalized_item)
        return normalized


class SqlQdrantColumnMapping(BaseModel):
    id: str = "id"
    source_id: str = "source_id"
    chunk_text: str = "chunk_text"
    chunk_metadata: str = "chunk_metadata"
    validation_status: str = "validation_status"


class SqlQdrantConfig(BaseModel):
    chunks_table: str = "rag_chunks"
    columns: SqlQdrantColumnMapping = Field(default_factory=SqlQdrantColumnMapping)
    invalid_statuses: list[str] = Field(default_factory=lambda: ["invalid"])


class CustomAdapterConfig(BaseModel):
    module: str = Field(min_length=1)
    class_name: str = Field(alias="class", min_length=1)
    kwargs: dict[str, Any] = Field(default_factory=dict)

    model_config = {"populate_by_name": True}


class BenchmarkConfig(BaseModel):
    device: str = "cpu"
    artifact_dir: Path = Field(default=Path("./rag_eval_out"))
    backend: str = "sql_qdrant"
    database_url: str | None = None
    qdrant_url: str | None = None
    collection_prefix: str = "rag_eval"
    source_id: int = Field(ge=1)
    profile_id: int = Field(default=1, ge=1)
    user_email: str = "demo.real.question.eval@example.test"
    dataset: Path
    models: BenchmarkModelsConfig = Field(default_factory=BenchmarkModelsConfig)
    top_k: int = Field(default=5, ge=1, le=100)
    score_threshold: float | None = None
    max_average_latency_ms: float | None = None
    max_cost_estimate_total: float | None = None
    sql_qdrant: SqlQdrantConfig | None = None
    adapter: CustomAdapterConfig | None = None

    @field_validator("device", "backend", "collection_prefix", "user_email")
    @classmethod
    def normalize_text(cls, value: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise ValueError("Field must not be empty")
        return normalized

    @field_validator("dataset", "artifact_dir")
    @classmethod
    def normalize_path(cls, value: Path) -> Path:
        return Path(value).expanduser()

    @model_validator(mode="after")
    def validate_backend_requirements(self) -> "BenchmarkConfig":
        if self.backend == "sql_qdrant":
            if not self.database_url:
                raise ValueError("sql_qdrant backend requires database_url.")
            if not self.qdrant_url:
                raise ValueError("sql_qdrant backend requires qdrant_url.")
        if self.backend == "custom" and self.adapter is None:
            raise ValueError("custom backend requires adapter.module and adapter.class.")
        return self

    def resolved_model_codes(self) -> list[str]:
        model_codes = list(self.models.default)
        if self.models.include_optional:
            model_codes.extend(self.models.optional_high_ram)
        return model_codes

    def apply_runtime_env(self) -> None:
        os.environ.setdefault("SENTENCE_TRANSFORMERS_DEVICE", self.device)


def _expand_env(value: Any) -> Any:
    if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
        env_name = value[2:-1]
        return os.environ.get(env_name)
    if isinstance(value, dict):
        return {key: _expand_env(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_expand_env(item) for item in value]
    return value


def load_benchmark_config(config_path: Path) -> BenchmarkConfig:
    resolved_path = config_path.expanduser().resolve()
    if not resolved_path.exists():
        raise FileNotFoundError(f"Config file not found: {resolved_path}")

    payload = yaml.safe_load(resolved_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Benchmark config must be a YAML mapping.")

    expanded_payload = _expand_env(payload)
    config = BenchmarkConfig.model_validate(expanded_payload)
    if config.dataset and not config.dataset.is_absolute():
        config = config.model_copy(update={"dataset": (resolved_path.parent / config.dataset).resolve()})
    if config.artifact_dir and not config.artifact_dir.is_absolute():
        config = config.model_copy(update={"artifact_dir": (resolved_path.parent / config.artifact_dir).resolve()})
    if config.sql_qdrant is None and config.backend == "sql_qdrant":
        config = config.model_copy(update={"sql_qdrant": SqlQdrantConfig()})
    return config
