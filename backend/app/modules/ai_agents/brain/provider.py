from __future__ import annotations

from typing import Protocol

from app.core.config import Settings, settings
from app.modules.ai_agents.schemas import BrainAgentRequest, BrainAgentResponse
from app.modules.ai_agents.brain.providers import (
    MockBrainAgentProvider,
    OpenAICompatibleBrainAgentProvider,
)


class BrainAgentProvider(Protocol):
    def generate_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
        ...


class BrainProviderConfigurationError(ValueError):
    pass


class BrainProviderResponseError(RuntimeError):
    pass


class BrainProviderRequestError(RuntimeError):
    pass


def build_brain_provider(
    *,
    provider_name: str | None = None,
    provider_settings: Settings | None = None,
) -> BrainAgentProvider:
    resolved_settings = provider_settings or settings
    normalized_provider_name = (provider_name or resolved_settings.ai_brain_provider).strip().lower()

    if normalized_provider_name == "mock":
        return MockBrainAgentProvider()

    if normalized_provider_name == "openai_compatible":
        return OpenAICompatibleBrainAgentProvider.from_settings(resolved_settings)

    raise BrainProviderConfigurationError(
        "Unsupported AI_BRAIN_PROVIDER: "
        f"{normalized_provider_name}. Allowed values: mock, openai_compatible"
    )
