from __future__ import annotations


class RagEmbeddingError(Exception):
    """Base embeddings-domain exception."""


class RagEmbeddingNotFoundError(RagEmbeddingError):
    """Raised when the requested embedding does not exist for the current user."""


class RagEmbeddingChunkNotFoundError(RagEmbeddingError):
    """Raised when the requested chunk does not exist for the current user."""


class RagEmbeddingSourceNotFoundError(RagEmbeddingError):
    """Raised when the requested source does not exist for the current user."""


class RagEmbeddingModelUnavailableError(RagEmbeddingError):
    """Raised when the requested embedding model is unavailable for generation."""


class RagEmbeddingGenerationError(RagEmbeddingError):
    """Raised when embedding generation fails."""
