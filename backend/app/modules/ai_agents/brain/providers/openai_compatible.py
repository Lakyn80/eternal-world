from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter
from typing import Any, Callable

import httpx

from app.core.config import Settings, settings
from app.modules.ai_agents.brain.providers.grounding import (
    build_lack_of_evidence_response,
    resolve_grounding_status,
    should_return_lack_of_evidence_response,
)
from app.modules.ai_agents.schemas import BrainAgentRequest, BrainAgentResponse


@dataclass(frozen=True)
class OpenAICompatibleChatRequest:
    url: str
    headers: dict[str, str]
    payload: dict[str, Any]


class OpenAICompatibleBrainAgentProvider:
    provider_name = "openai_compatible"

    def __init__(
        self,
        *,
        model: str,
        api_key: str,
        base_url: str,
        timeout_seconds: float,
        temperature: float = 0.2,
        max_tokens: int | None = None,
        http_client_factory: Callable[[float], Any] | None = None,
    ) -> None:
        self.model = model
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds
        self.temperature = temperature
        self.max_tokens = max_tokens
        self._http_client_factory = http_client_factory or self._default_http_client_factory

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
            temperature=resolved_settings.ai_brain_temperature,
            max_tokens=resolved_settings.ai_brain_max_tokens,
        )

    def generate_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
        from app.modules.ai_agents.brain.provider import (
            BrainProviderRequestError,
            BrainProviderResponseError,
        )

        if should_return_lack_of_evidence_response(request):
            return build_lack_of_evidence_response(
                request,
                provider_name=self.provider_name,
                metadata={
                    "provider_type": self.provider_name,
                    "model": self.model,
                    "latency_ms": 0,
                },
            )

        prepared_request = self.build_request(request)
        started_at = perf_counter()

        try:
            with self._http_client_factory(self.timeout_seconds) as client:
                response = client.post(
                    prepared_request.url,
                    headers=prepared_request.headers,
                    json=prepared_request.payload,
                )
                response.raise_for_status()
        except httpx.TimeoutException as exc:
            raise BrainProviderRequestError(
                "OpenAI-compatible provider request timed out"
            ) from exc
        except httpx.NetworkError as exc:
            raise BrainProviderRequestError(
                "OpenAI-compatible provider network request failed"
            ) from exc
        except httpx.HTTPStatusError as exc:
            status_code = exc.response.status_code if exc.response is not None else "unknown"
            raise BrainProviderRequestError(
                f"OpenAI-compatible provider returned HTTP {status_code}"
            ) from exc
        except httpx.HTTPError as exc:
            raise BrainProviderRequestError(
                "OpenAI-compatible provider request failed"
            ) from exc

        latency_ms = int((perf_counter() - started_at) * 1000)

        try:
            data = response.json()
        except ValueError as exc:
            raise BrainProviderResponseError(
                "OpenAI-compatible provider returned invalid JSON"
            ) from exc

        response_text = self._extract_response_text(data)
        return BrainAgentResponse(
            text=response_text,
            provider_name=self.provider_name,
            metadata={
                "agent": "brain",
                "provider_type": self.provider_name,
                "model": self._extract_response_model(data),
                "grounding_status": resolve_grounding_status(request),
                "latency_ms": latency_ms,
                **self._extract_usage_metadata(data),
            },
        )

    def build_request(self, request: BrainAgentRequest) -> OpenAICompatibleChatRequest:
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": request.system_prompt,
                },
                {
                    "role": "user",
                    "content": request.user_prompt,
                },
            ],
            "temperature": self.temperature,
        }
        if self.max_tokens is not None:
            payload["max_tokens"] = self.max_tokens

        return OpenAICompatibleChatRequest(
            url=self._build_chat_completions_url(),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            payload=payload,
        )

    def _build_chat_completions_url(self) -> str:
        if self.base_url.endswith("/chat/completions"):
            return self.base_url

        return f"{self.base_url}/chat/completions"

    def _default_http_client_factory(self, timeout_seconds: float) -> httpx.Client:
        return httpx.Client(timeout=timeout_seconds)

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
        if isinstance(content, str) and content.strip():
            return content.strip()

        if isinstance(content, list):
            text_parts = []
            for item in content:
                if isinstance(item, dict) and item.get("type") == "text":
                    text_value = item.get("text")
                    if isinstance(text_value, str) and text_value.strip():
                        text_parts.append(text_value.strip())
            if text_parts:
                return "\n".join(text_parts)

        raise BrainProviderResponseError("OpenAI-compatible provider returned empty content")

    def _extract_response_model(self, data: dict[str, Any]) -> str:
        response_model = data.get("model")
        if isinstance(response_model, str) and response_model.strip():
            return response_model.strip()

        return self.model

    def _extract_usage_metadata(self, data: dict[str, Any]) -> dict[str, Any]:
        usage = data.get("usage")
        if not isinstance(usage, dict):
            return {}

        usage_metadata = {
            key: value
            for key in ("prompt_tokens", "completion_tokens", "total_tokens")
            if isinstance((value := usage.get(key)), int)
        }
        if not usage_metadata:
            return {}

        return {"usage": usage_metadata}
