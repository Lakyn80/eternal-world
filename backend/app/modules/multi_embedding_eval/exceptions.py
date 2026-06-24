from __future__ import annotations


class MultiEmbeddingEvalError(Exception):
    pass


class MultiEmbeddingEvalJobNotFoundError(MultiEmbeddingEvalError):
    pass


class MultiEmbeddingEvalUserNotFoundError(MultiEmbeddingEvalError):
    pass


class MultiEmbeddingEvalSourceNotFoundError(MultiEmbeddingEvalError):
    pass


class MultiEmbeddingEvalAllCandidatesFailedError(MultiEmbeddingEvalError):
    pass
