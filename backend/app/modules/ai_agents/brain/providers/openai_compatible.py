from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter
from typing import Any, Callable, NoReturn

import httpx

from app.core.config import Settings, settings
from app.core.metrics import observe_brain_provider_await
from app.modules.ai_agents.brain.async_http import (
    build_brain_async_timeout,
    get_shared_brain_async_http_client,
)
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
        async_http_client: httpx.AsyncClient | None = None,
    ) -> None:
        self.model = model
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds
        self.temperature = temperature
        self.max_tokens = max_tokens
        self._http_client_factory = http_client_factory or self._default_http_client_factory
        self._async_http_client = async_http_client

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
        """Synchronous path for non-chat / legacy consumers (httpx.Client)."""

        if should_return_lack_of_evidence_response(request):
            return self._lack_of_evidence_response(request)

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
        except Exception as exc:
            self._raise_mapped_httpx_error(exc)

        return self._build_success_response(
            request,
            response=response,
            latency_ms=int((perf_counter() - started_at) * 1000),
        )

    async def generate_response_async(self, request: BrainAgentRequest) -> BrainAgentResponse:
        """True async path for chat: awaits httpx.AsyncClient network I/O."""

        if should_return_lack_of_evidence_response(request):
            return self._lack_of_evidence_response(request)

        prepared_request = self.build_request(request)
        started_at = perf_counter()
        client = self._async_http_client or await get_shared_brain_async_http_client(
            timeout_seconds=self.timeout_seconds,
        )
        request_timeout = build_brain_async_timeout(self.timeout_seconds)

        try:
            response = await client.post(
                prepared_request.url,
                headers=prepared_request.headers,
                json=prepared_request.payload,
                timeout=request_timeout,
            )
            response.raise_for_status()
        except Exception as exc:
            self._raise_mapped_httpx_error(exc)

        latency_ms = int((perf_counter() - started_at) * 1000)
        observe_brain_provider_await(
            provider=self.provider_name,
            duration_seconds=latency_ms / 1000.0,
        )
        return self._build_success_response(
            request,
            response=response,
            latency_ms=latency_ms,
        )

    def _lack_of_evidence_response(self, request: BrainAgentRequest) -> BrainAgentResponse:
        return build_lack_of_evidence_response(
            request,
            provider_name=self.provider_name,
            metadata={
                "provider_type": self.provider_name,
                "model": self.model,
                "latency_ms": 0,
            },
        )

    def _raise_mapped_httpx_error(self, exc: BaseException) -> NoReturn:
        from app.modules.ai_agents.brain.provider import BrainProviderRequestError

        if isinstance(exc, httpx.TimeoutException):
            raise BrainProviderRequestError(
                "OpenAI-compatible provider request timed out"
            ) from exc
        if isinstance(exc, httpx.NetworkError):
            raise BrainProviderRequestError(
                "OpenAI-compatible provider network request failed"
            ) from exc
        if isinstance(exc, httpx.HTTPStatusError):
            status_code = exc.response.status_code if exc.response is not None else "unknown"
            raise BrainProviderRequestError(
                f"OpenAI-compatible provider returned HTTP {status_code}"
            ) from exc
        if isinstance(exc, httpx.HTTPError):
            raise BrainProviderRequestError(
                "OpenAI-compatible provider request failed"
            ) from exc
        raise exc

    def _build_success_response(
        self,
        request: BrainAgentRequest,
        *,
        response: httpx.Response,
        latency_ms: int,
    ) -> BrainAgentResponse:
        from app.modules.ai_agents.brain.provider import BrainProviderResponseError

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
                **self._extract_provider_request_id_metadata(data),
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
        """Task 66.1: retains every numeric usage field DeepSeek actually
        returns (``prompt_tokens``, ``prompt_cache_hit_tokens``,
        ``prompt_cache_miss_tokens``, ``completion_tokens``, ``total_tokens``,
        and the nested ``completion_tokens_details.reasoning_tokens``) rather
        than only the three OpenAI-shaped fields previously kept - all of
        these are small non-negative token counts, never prompt/answer text,
        so retaining the full object here is safe. This is consumed by
        ``app.modules.provider_usage.usage.normalize_openai_compatible_usage``
        at the cost-accounting call site."""

        usage = data.get("usage")
        if not isinstance(usage, dict):
            return {}

        usage_metadata: dict[str, Any] = {
            key: value
            for key in (
                "prompt_tokens",
                "completion_tokens",
                "total_tokens",
                "prompt_cache_hit_tokens",
                "prompt_cache_miss_tokens",
            )
            if isinstance((value := usage.get(key)), int)
        }
        completion_details = usage.get("completion_tokens_details")
        if isinstance(completion_details, dict) and isinstance(
            completion_details.get("reasoning_tokens"), int
        ):
            usage_metadata["completion_tokens_details"] = {
                "reasoning_tokens": completion_details["reasoning_tokens"]
            }
        if not usage_metadata:
            return {}

        return {"usage": usage_metadata}

    def _extract_provider_request_id_metadata(self, data: dict[str, Any]) -> dict[str, Any]:
        provider_request_id = data.get("id")
        if isinstance(provider_request_id, str) and provider_request_id.strip():
            return {"provider_request_id": provider_request_id.strip()}
        return {}
