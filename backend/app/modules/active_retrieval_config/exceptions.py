from __future__ import annotations


class ActiveRetrievalConfigError(Exception):
    pass


class ActiveRetrievalConfigNotFoundError(ActiveRetrievalConfigError):
    pass


class ActiveRetrievalConfigProfileNotFoundError(ActiveRetrievalConfigError):
    pass


class ActiveRetrievalConfigJobNotFoundError(ActiveRetrievalConfigError):
    pass


class ActiveRetrievalConfigActivationError(ActiveRetrievalConfigError):
    pass
