class RagRetrievalError(Exception):
    pass


class RagRetrievalProfileNotFoundError(RagRetrievalError):
    pass


class RagRetrievalForbiddenError(RagRetrievalError):
    pass


class RagRetrievalModelUnavailableError(RagRetrievalError):
    pass


class RagRetrievalDisabledError(RagRetrievalError):
    pass
