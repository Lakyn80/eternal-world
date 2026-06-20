from __future__ import annotations


class EmbeddingModelError(Exception):
    """Base embedding-model registry exception."""


class EmbeddingModelNotFoundError(EmbeddingModelError):
    """Raised when an unknown embedding model code is requested."""
