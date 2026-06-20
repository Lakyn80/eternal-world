class QdrantIndexingError(Exception):
    pass


class RagVectorIndexEmbeddingNotFoundError(QdrantIndexingError):
    pass


class RagVectorIndexSourceNotFoundError(QdrantIndexingError):
    pass


class RagVectorIndexNotFoundError(QdrantIndexingError):
    pass


class RagVectorIndexEmbeddingNotReadyError(QdrantIndexingError):
    pass


class QdrantIndexingDisabledError(QdrantIndexingError):
    pass


class QdrantCollectionConfigurationError(QdrantIndexingError):
    pass


class QdrantClientError(QdrantIndexingError):
    pass
