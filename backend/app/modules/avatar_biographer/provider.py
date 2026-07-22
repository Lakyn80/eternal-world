"""DeepSeek structured-output provider for Biographer question generation
(Task 65.6).

Deliberately reuses the exact same DeepSeek account/connection settings as
the Brain agent (`AI_BRAIN_*`) - this is the same provider, not a second
one, and `settings.ai_brain_provider` (`mock`/`openai_compatible`) already
controls mock-vs-real for every other AI call in this codebase, so the same
toggle is reused here rather than inventing a new one. Structurally mirrors
`content_translation.provider.OpenAICompatibleContentTranslationProvider`:
a hand-rolled sync `httpx.Client` call against the same
`{base_url}/chat/completions` endpoint, JSON-object extraction, and Pydantic
schema validation - no SDK, no second HTTP client implementation.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from time import perf_counter
from typing import Any, Callable, Protocol

import httpx

from app.core.config import Settings, settings
from app.modules.avatar_biographer.schemas import ProviderQuestionResult


class BiographerProviderConfigurationError(ValueError):
    pass


class BiographerProviderRequestError(RuntimeError):
    pass


class BiographerProviderResponseError(RuntimeError):
    pass


@dataclass(frozen=True)
class BiographerProviderResponse:
    result: ProviderQuestionResult
    provider_name: str
    model: str
    latency_ms: int
    #: Task 66.1 raw numeric usage fields only - never prompt/answer text.
    usage: dict[str, Any] | None = None
    provider_request_id: str | None = None


class BiographerQuestionProvider(Protocol):
    provider_name: str

    def generate_question(self, *, system_prompt: str, user_prompt: str) -> BiographerProviderResponse: ...


class MockBiographerQuestionProvider:
    """Deterministic, network-free provider for local/dev/test use - never a
    real question generation, matching the existing `AI_BRAIN_PROVIDER=mock`
    and `MockContentTranslationProvider` conventions."""

    provider_name = "mock"

    def generate_question(self, *, system_prompt: str, user_prompt: str) -> BiographerProviderResponse:
        return BiographerProviderResponse(
            result=ProviderQuestionResult(
                question="(mock) Tell me more about this period of life.",
                known_information_used=False,
                question_intent="general_fact",
                confidence="low",
            ),
            provider_name=self.provider_name,
            model="mock",
            latency_ms=0,
        )


_JSON_OBJECT_PATTERN = re.compile(r"\{.*\}", re.DOTALL)


def _extract_json_object(content: str) -> dict[str, Any]:
    stripped = content.strip()
    if stripped.startswith("```"):
        stripped = stripped.strip("`")
        first_newline = stripped.find("\n")
        if first_newline != -1:
            stripped = stripped[first_newline + 1 :]
    try:
        return json.loads(stripped)
    except ValueError:
        pass
    match = _JSON_OBJECT_PATTERN.search(stripped)
    if match is None:
        raise BiographerProviderResponseError("Biographer provider response did not contain a JSON object")
    try:
        return json.loads(match.group(0))
    except ValueError as exc:
        raise BiographerProviderResponseError("Biographer provider response was not valid JSON") from exc


class OpenAICompatibleBiographerQuestionProvider:
    provider_name = "openai_compatible"

    def __init__(
        self,
        *,
        model: str,
        api_key: str,
        base_url: str,
        timeout_seconds: float,
        temperature: float = 0.4,
        http_client_factory: Callable[[float], Any] | None = None,
    ) -> None:
        self.model = model
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds
        self.temperature = temperature
        self._http_client_factory = http_client_factory or self._default_http_client_factory

    @classmethod
    def from_settings(
        cls,
        provider_settings: Settings | None = None,
    ) -> "OpenAICompatibleBiographerQuestionProvider":
        resolved_settings = provider_settings or settings
        api_key_secret = resolved_settings.ai_brain_api_key
        api_key = api_key_secret.get_secret_value() if api_key_secret is not None else ""

        if not resolved_settings.ai_brain_model:
            raise BiographerProviderConfigurationError(
                "AI_BRAIN_MODEL is required when AI_BRAIN_PROVIDER=openai_compatible"
            )
        if not api_key:
            raise BiographerProviderConfigurationError(
                "AI_BRAIN_API_KEY is required when AI_BRAIN_PROVIDER=openai_compatible"
            )
        if not resolved_settings.ai_brain_base_url:
            raise BiographerProviderConfigurationError(
                "AI_BRAIN_BASE_URL is required when AI_BRAIN_PROVIDER=openai_compatible"
            )

        return cls(
            model=resolved_settings.ai_brain_model,
            api_key=api_key,
            base_url=resolved_settings.ai_brain_base_url,
            timeout_seconds=resolved_settings.ai_brain_timeout_seconds,
        )

    def _default_http_client_factory(self, timeout_seconds: float) -> httpx.Client:
        return httpx.Client(timeout=timeout_seconds)

    def _build_chat_completions_url(self) -> str:
        if self.base_url.endswith("/chat/completions"):
            return self.base_url
        return f"{self.base_url}/chat/completions"

    def generate_question(self, *, system_prompt: str, user_prompt: str) -> BiographerProviderResponse:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": self.temperature,
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        started_at = perf_counter()
        try:
            with self._http_client_factory(self.timeout_seconds) as client:
                response = client.post(self._build_chat_completions_url(), headers=headers, json=payload)
                response.raise_for_status()
        except httpx.TimeoutException as exc:
            raise BiographerProviderRequestError("Biographer provider request timed out") from exc
        except httpx.NetworkError as exc:
            raise BiographerProviderRequestError("Biographer provider network request failed") from exc
        except httpx.HTTPStatusError as exc:
            status_code = exc.response.status_code if exc.response is not None else "unknown"
            raise BiographerProviderRequestError(f"Biographer provider returned HTTP {status_code}") from exc
        except httpx.HTTPError as exc:
            raise BiographerProviderRequestError("Biographer provider request failed") from exc

        latency_ms = int((perf_counter() - started_at) * 1000)

        try:
            data = response.json()
        except ValueError as exc:
            raise BiographerProviderResponseError("Biographer provider returned invalid JSON") from exc

        try:
            choices = data["choices"]
            message_content = choices[0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise BiographerProviderResponseError("Biographer provider response is missing message content") from exc

        if isinstance(message_content, list):
            message_content = "".join(
                part.get("text", "") for part in message_content if isinstance(part, dict) and part.get("type") == "text"
            )
        if not isinstance(message_content, str) or not message_content.strip():
            raise BiographerProviderResponseError("Biographer provider returned empty content")

        parsed = _extract_json_object(message_content)
        try:
            result = ProviderQuestionResult.model_validate(parsed)
        except Exception as exc:  # pydantic ValidationError
            raise BiographerProviderResponseError(
                "Biographer provider response did not match the required schema"
            ) from exc

        return BiographerProviderResponse(
            result=result,
            provider_name=self.provider_name,
            model=str(data.get("model") or self.model),
            latency_ms=latency_ms,
            usage=self._extract_usage(data),
            provider_request_id=self._extract_provider_request_id(data),
        )

    def _extract_usage(self, data: dict[str, Any]) -> dict[str, Any] | None:
        usage = data.get("usage")
        if not isinstance(usage, dict):
            return None
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
        if isinstance(completion_details, dict) and isinstance(completion_details.get("reasoning_tokens"), int):
            usage_metadata["completion_tokens_details"] = {
                "reasoning_tokens": completion_details["reasoning_tokens"]
            }
        return usage_metadata or None

    def _extract_provider_request_id(self, data: dict[str, Any]) -> str | None:
        provider_request_id = data.get("id")
        if isinstance(provider_request_id, str) and provider_request_id.strip():
            return provider_request_id.strip()
        return None


def build_biographer_question_provider(
    *,
    provider_settings: Settings | None = None,
) -> BiographerQuestionProvider:
    resolved_settings = provider_settings or settings
    normalized_provider_name = (resolved_settings.ai_brain_provider or "mock").strip().lower()
    if normalized_provider_name == "mock":
        return MockBiographerQuestionProvider()
    if normalized_provider_name == "openai_compatible":
        return OpenAICompatibleBiographerQuestionProvider.from_settings(resolved_settings)
    raise BiographerProviderConfigurationError(f"Unsupported AI_BRAIN_PROVIDER `{normalized_provider_name}`")
