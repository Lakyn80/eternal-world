from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass

from app.modules.embedding_models.service import get_embedding_model
from app.modules.embeddings.embedding_cache import build_text_hash
from app.modules.embeddings.providers.bge_m3_hybrid import (
    BgeM3HybridCacheSummary,
    BgeM3HybridEmbeddingProvider,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run a repeat-query smoke to verify Redis embedding cache hits for BGE-M3.",
    )
    parser.add_argument("--provider", default="bge_m3_dense_sparse")
    parser.add_argument("--query", required=True)
    parser.add_argument("--repeat", type=int, default=3)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--json", action="store_true", dest="json_output")
    return parser


@dataclass(frozen=True)
class SmokeIterationResult:
    iteration: int
    hits: int
    misses: int
    writes: int
    errors: int
    cache_enabled: bool
    text_hash_prefixes: tuple[str, ...]
    embedding_dimension: int
    stable_dense_vector: bool


@dataclass(frozen=True)
class EmbeddingCacheSmokeResult:
    provider_code: str
    provider_model_name: str
    source: str
    device: str
    cache_enabled: bool
    repeat: int
    hits: int
    misses: int
    writes: int
    errors: int
    text_hash_prefix: str
    embedding_dimension: int
    repeated_call_hit: bool
    vectors_stable: bool
    iterations: tuple[SmokeIterationResult, ...]

    @property
    def passed(self) -> bool:
        if not self.cache_enabled:
            return False
        if self.repeat > 1 and not self.repeated_call_hit:
            return False
        return self.errors == 0 and self.vectors_stable


def _build_text_hash_prefix(text: str) -> str:
    return build_text_hash(text).split(":", 1)[1][:8]


def _coerce_cache_summary(summary: BgeM3HybridCacheSummary | None) -> BgeM3HybridCacheSummary:
    if summary is None:
        raise RuntimeError("BGE-M3 cache summary is missing after encode call")
    return summary


def run_embedding_cache_smoke(
    *,
    provider_code: str,
    query: str,
    repeat: int,
    device: str = "cpu",
) -> EmbeddingCacheSmokeResult:
    if repeat < 2:
        raise ValueError("repeat must be at least 2")

    provider = BgeM3HybridEmbeddingProvider(device=device)
    model_definition = get_embedding_model(provider_code)
    baseline_dense_vector: list[float] | None = None
    iterations: list[SmokeIterationResult] = []
    total_hits = 0
    total_misses = 0
    total_writes = 0
    total_errors = 0
    provider_model_name = model_definition.provider_model_name or "unknown"
    source = "missing"
    cache_enabled = False

    for iteration_index in range(repeat):
        encoded = provider.encode_query(query, provider_code)
        summary = _coerce_cache_summary(provider.last_cache_summary)
        dense_vector = list(encoded.dense_vectors[0])
        stable_dense_vector = baseline_dense_vector is None or baseline_dense_vector == dense_vector
        if baseline_dense_vector is None:
            baseline_dense_vector = dense_vector

        provider_model_name = summary.provider_model_name
        source = summary.source
        cache_enabled = summary.cache_enabled
        total_hits += summary.hits
        total_misses += summary.misses
        total_writes += summary.writes
        total_errors += summary.errors
        iterations.append(
            SmokeIterationResult(
                iteration=iteration_index + 1,
                hits=summary.hits,
                misses=summary.misses,
                writes=summary.writes,
                errors=summary.errors,
                cache_enabled=summary.cache_enabled,
                text_hash_prefixes=summary.text_hash_prefixes,
                embedding_dimension=len(dense_vector),
                stable_dense_vector=stable_dense_vector,
            )
        )

    repeated_call_hit = any(
        iteration.hits > 0 and iteration.misses == 0
        for iteration in iterations[1:]
    )
    vectors_stable = all(iteration.stable_dense_vector for iteration in iterations)
    return EmbeddingCacheSmokeResult(
        provider_code=provider_code,
        provider_model_name=provider_model_name,
        source=source,
        device=device,
        cache_enabled=cache_enabled,
        repeat=repeat,
        hits=total_hits,
        misses=total_misses,
        writes=total_writes,
        errors=total_errors,
        text_hash_prefix=_build_text_hash_prefix(query),
        embedding_dimension=len(baseline_dense_vector or []),
        repeated_call_hit=repeated_call_hit,
        vectors_stable=vectors_stable,
        iterations=tuple(iterations),
    )


def _result_to_json_ready(result: EmbeddingCacheSmokeResult) -> dict[str, object]:
    payload = asdict(result)
    payload["iterations"] = [asdict(iteration) for iteration in result.iterations]
    payload["passed"] = result.passed
    return payload


def _print_text_result(result: EmbeddingCacheSmokeResult) -> None:
    print(f"EMBEDDING CACHE SMOKE RESULT: {'PASS' if result.passed else 'FAIL'}")
    print(
        "summary "
        f"provider_code={result.provider_code} "
        f"provider_model_name={result.provider_model_name} "
        f"source={result.source} device={result.device} "
        f"cache_enabled={str(result.cache_enabled).lower()} repeat={result.repeat} "
        f"hits={result.hits} misses={result.misses} writes={result.writes} errors={result.errors} "
        f"text_hash_prefix={result.text_hash_prefix} "
        f"embedding_dimension={result.embedding_dimension} "
        f"repeated_call_hit={str(result.repeated_call_hit).lower()} "
        f"vectors_stable={str(result.vectors_stable).lower()}"
    )
    for iteration in result.iterations:
        print(
            "iteration "
            f"index={iteration.iteration} hits={iteration.hits} misses={iteration.misses} "
            f"writes={iteration.writes} errors={iteration.errors} "
            f"cache_enabled={str(iteration.cache_enabled).lower()} "
            f"text_hash_prefixes={','.join(iteration.text_hash_prefixes)} "
            f"embedding_dimension={iteration.embedding_dimension} "
            f"stable_dense_vector={str(iteration.stable_dense_vector).lower()}"
        )


def main() -> int:
    args = _build_parser().parse_args()
    try:
        result = run_embedding_cache_smoke(
            provider_code=args.provider,
            query=args.query,
            repeat=args.repeat,
            device=args.device,
        )
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.json_output:
        print(json.dumps(_result_to_json_ready(result), ensure_ascii=False, indent=2, sort_keys=True))
    else:
        _print_text_result(result)

    return 0 if result.passed else 1


if __name__ == "__main__":
    sys.exit(main())
