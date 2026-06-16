from __future__ import annotations

from typing import Any

import httpx

from app.core.config import Settings, settings
from app.modules.ai_agents.schemas import BrainAgentRequest, BrainAgentResponse


class OpenAICompatibleBrainAgentProvider:
    provider_name = "openai_compatible"

    def __init__(
        self,
        *,
        model: str,
        api_key: str,
        base_url: str,
        timeout_seconds: float,
    ) -> None:
        self.model = model
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds

    @classmethod
    def from_settings(
        cls,
        provider_settings: Settings | None = None,
    ) -> "OpenAICompatibleBrainAgentProvider":
        from app.modules.ai_agents.brain.provider import BrainProviderConfigurationError

        resolved_settings = provider_settings or settings
        api_key_secret = resolved_settings.ai_brain_api_key
        api_key = api_key_secret.get_secret_value() if api_key_secret is not None else ""

        if not resolved_settings.ai_brain_model:
            raise BrainProviderConfigurationError(
                "AI_BRAIN_MODEL is required when AI_BRAIN_PROVIDER=openai_compatible"
            )

        if not api_key:
            raise BrainProviderConfigurationError(
                "AI_BRAIN_API_KEY is required when AI_BRAIN_PROVIDER=openai_compatible"
            )

        if not resolved_settings.ai_brain_base_url:
            raise BrainProviderConfigurationError(
                "AI_BRAIN_BASE_URL is required when AI_BRAIN_PROVIDER=openai_compatible"
            )

        return cls(
            model=resolved_settings.ai_brain_model,
            api_key=api_key,
            base_url=resolved_settings.ai_brain_base_url,
            timeout_seconds=resolved_settings.ai_brain_timeout_seconds,
        )

    def generate_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": request.prompt,
                }
            ],
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        with httpx.Client(timeout=self.timeout_seconds) as client:
            response = client.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
            )
            response.raise_for_status()
            data = response.json()

        response_text = self._extract_response_text(data)
        return BrainAgentResponse(
            text=response_text,
            provider_name=self.provider_name,
            metadata={
                "agent": "brain",
                "model": self.model,
                "provider_type": self.provider_name,
            },
        )

    def _extract_response_text(self, data: dict[str, Any]) -> str:
        from app.modules.ai_agents.brain.provider import BrainProviderResponseError

        choices = data.get("choices")
        if not isinstance(choices, list) or not choices:
            raise BrainProviderResponseError("OpenAI-compatible provider returned no choices")

        first_choice = choices[0]
        if not isinstance(first_choice, dict):
            raise BrainProviderResponseError("OpenAI-compatible provider returned an invalid choice")

        message = first_choice.get("message")
        if not isinstance(message, dict):
            raise BrainProviderResponseError(
                "OpenAI-compatible provider returned no message payload"
            )

        content = message.get("content")
        if not isinstance(content, str) or not content.strip():
            raise BrainProviderResponseError(
                "OpenAI-compatible provider returned empty content"
            )

        return content.strip()
