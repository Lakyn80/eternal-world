from __future__ import annotations


class RagEvaluationError(Exception):
    """Base exception for RAG evaluation harness failures."""


class RagEvaluationCaseExecutionError(RagEvaluationError):
    """Raised when an evaluation case cannot produce a valid agent response."""
