from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Callable, Protocol

from app.core.config import settings
from app.modules.embedding_models.registry import BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE

BGE_M3_DENSE_SPARSE_MODEL_CODE = BGE_M3_DENSE_SPARSE_RETRIEVAL_MODE
SPARSE_VECTOR_PAYLOAD_KEY = "sparse_vector"
HYBRID_DENSE_CANDIDATE_POOL_MULTIPLIER = 4
HYBRID_DENSE_CANDIDATE_POOL_MIN = 20

TOKEN_PATTERN = re.compile(r"[A-Za-z0-9]{2,}")


@dataclass(frozen=True)
class HybridQueryVectors:
    dense_vector: list[float]
    sparse_vector: dict[str, float]


@dataclass(frozen=True)
class HybridRetrievalCandidate:
    embedding_id: int
    chunk_id: int
    dense_score: float
    sparse_vector: dict[str, float]
    payload_metadata: dict[str, object]


@dataclass(frozen=True)
class FusedHybridRetrievalResult:
    embedding_id: int
    chunk_id: int
    fused_score: float
    dense_score: float
    sparse_score: float
    payload_metadata: dict[str, object]


class HybridQueryEncoder(Protocol):
    def __call__(self, query: str, model_code: str) -> HybridQueryVectors:
        raise NotImplementedError


def is_bge_m3_dense_sparse_model(model_code: str) -> bool:
    return model_code.strip().lower() == BGE_M3_DENSE_SPARSE_MODEL_CODE


def normalize_score_map(raw_scores: dict[int, float]) -> dict[int, float]:
    if not raw_scores:
        return {}

    score_values = list(raw_scores.values())
    min_score = min(score_values)
    max_score = max(score_values)
    if max_score == min_score:
        return {candidate_id: 1.0 for candidate_id in raw_scores}

    return {
        candidate_id: (score - min_score) / (max_score - min_score)
        for candidate_id, score in raw_scores.items()
    }


def dot_product(left: list[float], right: list[float]) -> float:
    return sum(left_item * right_item for left_item, right_item in zip(left, right, strict=True))


def compute_sparse_overlap_score(
    query_sparse_vector: dict[str, float],
    passage_sparse_vector: dict[str, float],
) -> float:
    if not query_sparse_vector or not passage_sparse_vector:
        return 0.0

    return sum(
        query_sparse_vector[token] * passage_sparse_vector[token]
        for token in query_sparse_vector.keys() & passage_sparse_vector.keys()
    )


def build_deterministic_sparse_vector(*, text: str, model_code: str) -> dict[str, float]:
    tokens = TOKEN_PATTERN.findall(text.lower())
    if not tokens:
        return {}

    sparse_vector: dict[str, float] = {}
    for token in dict.fromkeys(tokens):
        digest = hashlib.sha256(f"{model_code}:sparse:{token}".encode("utf-8")).digest()
        sparse_vector[token] = round((digest[0] / 255.0) + 0.1, 6)

    return sparse_vector


def resolve_passage_sparse_vector(
    *,
    chunk_text: str,
    model_code: str,
    embedding_metadata: dict[str, object] | None,
) -> dict[str, float]:
    if isinstance(embedding_metadata, dict):
        stored_sparse_vector = embedding_metadata.get("sparse_vector")
        if isinstance(stored_sparse_vector, dict):
            normalized_sparse_vector: dict[str, float] = {}
            for token, weight in stored_sparse_vector.items():
                if isinstance(token, str) and isinstance(weight, (int, float)):
                    normalized_sparse_vector[token] = float(weight)
            if normalized_sparse_vector:
                return normalized_sparse_vector

    return build_deterministic_sparse_vector(text=chunk_text, model_code=model_code)


def build_hybrid_candidate_pool_limit(*, top_k: int) -> int:
    return max(top_k * HYBRID_DENSE_CANDIDATE_POOL_MULTIPLIER, HYBRID_DENSE_CANDIDATE_POOL_MIN, top_k)


def rank_fused_hybrid_candidates(
    *,
    query_sparse_vector: dict[str, float],
    candidates: list[HybridRetrievalCandidate],
    top_k: int,
) -> list[FusedHybridRetrievalResult]:
    if not candidates:
        return []

    dense_scores = {candidate.embedding_id: candidate.dense_score for candidate in candidates}
    sparse_scores = {
        candidate.embedding_id: compute_sparse_overlap_score(
            query_sparse_vector,
            candidate.sparse_vector,
        )
        for candidate in candidates
    }
    normalized_dense_scores = normalize_score_map(dense_scores)
    normalized_sparse_scores = normalize_score_map(sparse_scores)
    fused_scores = {
        candidate.embedding_id: (
            normalized_dense_scores.get(candidate.embedding_id, 0.0)
            + normalized_sparse_scores.get(candidate.embedding_id, 0.0)
        )
        / 2.0
        for candidate in candidates
    }

    ranked_candidates = sorted(
        candidates,
        key=lambda candidate: (
            fused_scores.get(candidate.embedding_id, 0.0),
            dense_scores.get(candidate.embedding_id, 0.0),
            sparse_scores.get(candidate.embedding_id, 0.0),
        ),
        reverse=True,
    )[:top_k]

    return [
        FusedHybridRetrievalResult(
            embedding_id=candidate.embedding_id,
            chunk_id=candidate.chunk_id,
            fused_score=fused_scores.get(candidate.embedding_id, 0.0),
            dense_score=dense_scores.get(candidate.embedding_id, 0.0),
            sparse_score=sparse_scores.get(candidate.embedding_id, 0.0),
            payload_metadata={
                **candidate.payload_metadata,
                "hybrid_retrieval": True,
                "dense_score": round(dense_scores.get(candidate.embedding_id, 0.0), 6),
                "sparse_score": round(sparse_scores.get(candidate.embedding_id, 0.0), 6),
                "fused_score": round(fused_scores.get(candidate.embedding_id, 0.0), 6),
            },
        )
        for candidate in ranked_candidates
    ]


def _can_use_real_bge_m3_hybrid_provider() -> bool:
    if settings.embedding_provider != "sentence_transformers":
        return False

    try:
        import FlagEmbedding  # noqa: F401
    except ImportError:
        return False

    return True


def default_encode_hybrid_query_vectors(query: str, model_code: str) -> HybridQueryVectors:
    if _can_use_real_bge_m3_hybrid_provider():
        from app.modules.embeddings.providers.bge_m3_hybrid import BgeM3HybridEmbeddingProvider

        hybrid_provider = BgeM3HybridEmbeddingProvider(
            device=settings.sentence_transformers_device,
            cache_dir=settings.sentence_transformers_cache_dir,
        )
        encoded = hybrid_provider.encode_query(query, model_code)
        if not encoded.dense_vectors or not encoded.sparse_vectors:
            raise ValueError("Hybrid query encoding returned empty vectors")

        return HybridQueryVectors(
            dense_vector=list(encoded.dense_vectors[0]),
            sparse_vector=dict(encoded.sparse_vectors[0]),
        )

    from app.modules.embeddings.providers import build_embedding_provider

    dense_provider = build_embedding_provider(model_code=model_code)
    dense_embedding = dense_provider.embed_query(query, model_code)
    return HybridQueryVectors(
        dense_vector=list(dense_embedding.values),
        sparse_vector=build_deterministic_sparse_vector(text=query, model_code=model_code),
    )


def encode_hybrid_query_vectors(
    query: str,
    model_code: str,
    *,
    query_encoder: Callable[[str, str], HybridQueryVectors] | None = None,
) -> HybridQueryVectors:
    encoder = query_encoder or default_encode_hybrid_query_vectors
    return encoder(query, model_code)
