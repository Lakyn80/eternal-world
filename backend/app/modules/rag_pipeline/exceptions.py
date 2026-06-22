from __future__ import annotations


class RagPipelineError(Exception):
    """Base exception for tracked RAG pipeline orchestration failures."""


class RagPipelineJobNotFoundError(RagPipelineError):
    """Raised when a referenced BackgroundJob cannot be resolved."""


class RagPipelineSourceNotFoundError(RagPipelineError):
    """Raised when a referenced RagSource cannot be resolved for the job owner."""


class RagPipelineUserNotFoundError(RagPipelineError):
    """Raised when the BackgroundJob owner cannot be resolved."""
