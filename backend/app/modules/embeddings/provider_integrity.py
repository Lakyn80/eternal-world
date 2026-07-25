"""Embedding provider integrity probe (Task 65.9, Part K).

Built directly from a real production incident (documented in
PROJECT_PROGRESS.md, Task 65.9): `BAAI/bge-m3` reported "load success" on
every call, yet the loaded model's parameters were stuck on the PyTorch
`meta` device, so every real `encode()` call raised
`NotImplementedError: Cannot copy out of meta tensor; no data!`. A plain
"load returned without raising" check would have kept declaring this
provider healthy forever.

This module never uses real user memory content for probing - only the
fixed, harmless `PROVIDER_INTEGRITY_PROBE_TEXT` constant below - and never
logs embedding values or user text.
"""

from __future__ import annotations

import math

from app.modules.embeddings.providers.base import BaseEmbeddingProvider, EmbeddingVector


#: Fixed, harmless internal probe string (Part K: "Use a fixed harmless
#: internal probe string. Never use user content for the health probe.").
#: Deliberately not private/sensitive and not derived from any real
#: memorial content.
PROVIDER_INTEGRITY_PROBE_TEXT = "eternal-world-embedding-provider-integrity-probe"

_META_DEVICE_SIGNATURES = (
    "meta tensor",
    "cannot copy out of meta",
    "no data!",
    "is_meta",
)


class ProviderIntegrityError(Exception):
    """Raised when the provider integrity probe detects the model is
    unusable (meta-device parameters, invalid probe output, or a runtime
    exception carrying a known meta-device corruption signature). Always
    treated as `provider_corrupt` by the bounded self-healing layer -
    never conflated with an ordinary validation/domain error."""

    def __init__(self, message: str, *, reason_code: str) -> None:
        super().__init__(message)
        self.reason_code = reason_code


def looks_like_meta_device_corruption(exc: BaseException) -> bool:
    """Best-effort detection of the exact incident signature from a
    caught exception (which may have already been wrapped, e.g. by
    `BgeM3HybridProviderError`, losing the original exception type but
    typically preserving `__cause__`)."""

    haystack_parts = [str(exc)]
    cause = getattr(exc, "__cause__", None)
    if cause is not None:
        haystack_parts.append(str(cause))
    haystack = " ".join(haystack_parts).lower()
    return any(signature in haystack for signature in _META_DEVICE_SIGNATURES)


def _find_underlying_torch_modules(model: object) -> list[object]:
    """Best-effort traversal to find `torch.nn.Module` instances backing a
    `FlagEmbedding` BGE-M3 model object, so parameters/buffers can be
    inspected directly for `is_meta` (Part K items 1-2). Purely
    defense-in-depth: the primary, always-available detection path is the
    probe-embedding output check below, which does not depend on
    FlagEmbedding's internal attribute layout staying stable."""

    try:
        import torch
    except ImportError:  # pragma: no cover - torch is a hard runtime dependency in real deployments
        return []

    candidates: list[object] = []
    seen_ids: set[int] = set()
    for attribute_path in ("model", "model.model", "colbert_linear", "sparse_linear"):
        target = model
        for attribute_name in attribute_path.split("."):
            target = getattr(target, attribute_name, None)
            if target is None:
                break
        if target is None or id(target) in seen_ids:
            continue
        if isinstance(target, torch.nn.Module):
            candidates.append(target)
            seen_ids.add(id(target))
    return candidates


def check_provider_parameters_not_meta(model: object) -> None:
    """Part K items 1-2: parameters/buffers with `is_meta = True`. Skips
    silently (does not raise) if no inspectable `torch.nn.Module` is found
    - the output-based checks below remain the authoritative signal."""

    for module in _find_underlying_torch_modules(model):
        for parameter in module.parameters():
            if getattr(parameter, "is_meta", False):
                raise ProviderIntegrityError(
                    "Embedding model parameters are on the meta device",
                    reason_code="meta_parameter",
                )
        for buffer in module.buffers():
            if getattr(buffer, "is_meta", False):
                raise ProviderIntegrityError(
                    "Embedding model buffers are on the meta device",
                    reason_code="meta_buffer",
                )


def validate_embedding_output(vector: EmbeddingVector, *, expected_dimension: int | None = None) -> None:
    """Part K items 4-9: empty output, wrong vector count/dimensionality,
    NaN, infinite, or structurally invalid output."""

    if vector is None:
        raise ProviderIntegrityError("Embedding output is empty", reason_code="empty_output")
    values = vector.values
    if not isinstance(values, list) or not values:
        raise ProviderIntegrityError("Embedding output is empty", reason_code="empty_output")
    if len(values) != vector.dimension:
        raise ProviderIntegrityError(
            "Embedding output vector count does not match its declared dimension",
            reason_code="wrong_vector_count",
        )
    if expected_dimension is not None and vector.dimension != expected_dimension:
        raise ProviderIntegrityError(
            "Embedding output dimensionality is incorrect",
            reason_code="wrong_dimension",
        )
    for value in values:
        if not isinstance(value, (int, float)):
            raise ProviderIntegrityError(
                "Embedding output contains a non-numeric value",
                reason_code="invalid_structure",
            )
        if math.isnan(value):
            raise ProviderIntegrityError("Embedding output contains NaN", reason_code="nan_value")
        if math.isinf(value):
            raise ProviderIntegrityError(
                "Embedding output contains an infinite value", reason_code="infinite_value"
            )


def run_provider_integrity_probe(
    provider: BaseEmbeddingProvider,
    *,
    model_code: str,
    expected_dimension: int | None = None,
) -> EmbeddingVector:
    """The full integrity probe (Part K). Run after initial load, after a
    reload, and after any provider-corruption exception - never before
    every ordinary job (that would make every embed call pay for a second
    full model invocation)."""

    try:
        vector = provider.embed_passage(PROVIDER_INTEGRITY_PROBE_TEXT, model_code)
    except ProviderIntegrityError:
        raise
    except Exception as exc:
        if looks_like_meta_device_corruption(exc):
            raise ProviderIntegrityError(
                "Embedding provider probe failed with a meta-device corruption signature",
                reason_code="probe_raised_meta_device_error",
            ) from exc
        raise ProviderIntegrityError(
            "Embedding provider probe raised an unexpected error",
            reason_code="probe_raised_unexpected_error",
        ) from exc

    validate_embedding_output(vector, expected_dimension=expected_dimension)
    return vector
