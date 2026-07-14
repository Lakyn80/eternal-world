from __future__ import annotations

import json
import re
from dataclasses import dataclass
from time import perf_counter
from typing import Any, Callable, Protocol

import httpx

from app.core.config import Settings, settings
from app.modules.content_translation.prompt import (
    build_translation_system_prompt,
    build_translation_user_prompt,
)
from app.modules.content_translation.schemas import ProviderTranslationResult


class ContentTranslationProviderConfigurationError(ValueError):
    pass


class ContentTranslationProviderRequestError(RuntimeError):
    pass


class ContentTranslationProviderResponseError(RuntimeError):
    pass


@dataclass(frozen=True)
class ContentTranslationProviderResponse:
    result: ProviderTranslationResult
    provider_name: str
    model: str
    latency_ms: int


class ContentTranslationProvider(Protocol):
    provider_name: str

    def translate(
        self,
        *,
        source_text: str,
        source_language: str,
        target_language: str,
    ) -> ContentTranslationProviderResponse: ...


class MockContentTranslationProvider:
    """Deterministic, network-free provider for local/dev/test use.

    This is NOT a real translation - it is the same kind of safe, explicit
    "mock" fallback already used for ``AI_BRAIN_PROVIDER=mock``. It exists so
    the bilingual workflow can be exercised end-to-end (statuses, staleness,
    eligibility gating, idempotency) without any network dependency or
    provider credentials. Tests that need to assert on real translation
    fidelity (name/date/song-title preservation) inject a fake provider with
    controlled output instead of relying on this passthrough behavior.
    """

    provider_name = "mock"

    def translate(
        self,
        *,
        source_text: str,
        source_language: str,
        target_language: str,
    ) -> ContentTranslationProviderResponse:
        marker = f"[{source_language}->{target_language}] "
        return ContentTranslationProviderResponse(
            result=ProviderTranslationResult(
                translated_text=f"{marker}{source_text}",
                preserved_entities=[],
                warnings=["mock_provider_not_a_real_translation"],
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
        raise ContentTranslationProviderResponseError(
            "Translation provider response did not contain a JSON object"
        )
    try:
        return json.loads(match.group(0))
    except ValueError as exc:
        raise ContentTranslationProviderResponseError(
            "Translation provider response was not valid JSON"
        ) from exc


class OpenAICompatibleContentTranslationProvider:
    """Reuses the same OpenAI-compatible wire format as the Brain agent.

    Deliberately mirrors
    ``app.modules.ai_agents.brain.providers.openai_compatible.OpenAICompatibleBrainAgentProvider``:
    a hand-rolled sync ``httpx.Client`` call against ``{base_url}/chat/completions``,
    no SDK, no retries beyond what the caller explicitly requests, and an
    injectable ``http_client_factory`` seam for tests (matching this repo's
    existing test convention - no HTTP-mocking library dependency).
    """

    provider_name = "openai_compatible"

    def __init__(
        self,
        *,
        model: str,
        api_key: str,
        base_url: str,
        timeout_seconds: float,
        temperature: float = 0.0,
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
    ) -> "OpenAICompatibleContentTranslationProvider":
        resolved_settings = provider_settings or settings
        api_key_secret = resolved_settings.content_translation_api_key
        api_key = api_key_secret.get_secret_value() if api_key_secret is not None else ""

        if not resolved_settings.content_translation_model:
            raise ContentTranslationProviderConfigurationError(
                "CONTENT_TRANSLATION_MODEL is required when "
                "CONTENT_TRANSLATION_PROVIDER=openai_compatible"
            )
        if not api_key:
            raise ContentTranslationProviderConfigurationError(
                "CONTENT_TRANSLATION_API_KEY is required when "
                "CONTENT_TRANSLATION_PROVIDER=openai_compatible"
            )
        if not resolved_settings.content_translation_base_url:
            raise ContentTranslationProviderConfigurationError(
                "CONTENT_TRANSLATION_BASE_URL is required when "
                "CONTENT_TRANSLATION_PROVIDER=openai_compatible"
            )

        return cls(
            model=resolved_settings.content_translation_model,
            api_key=api_key,
            base_url=resolved_settings.content_translation_base_url,
            timeout_seconds=resolved_settings.content_translation_timeout_seconds,
        )

    def _default_http_client_factory(self, timeout_seconds: float) -> httpx.Client:
        return httpx.Client(timeout=timeout_seconds)

    def _build_chat_completions_url(self) -> str:
        if self.base_url.endswith("/chat/completions"):
            return self.base_url
        return f"{self.base_url}/chat/completions"

    def translate(
        self,
        *,
        source_text: str,
        source_language: str,
        target_language: str,
    ) -> ContentTranslationProviderResponse:
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": build_translation_system_prompt(
                        source_language=source_language,
                        target_language=target_language,
                    ),
                },
                {
                    "role": "user",
                    "content": build_translation_user_prompt(source_text=source_text),
                },
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
                response = client.post(
                    self._build_chat_completions_url(),
                    headers=headers,
                    json=payload,
                )
                response.raise_for_status()
        except httpx.TimeoutException as exc:
            raise ContentTranslationProviderRequestError(
                "Content translation provider request timed out"
            ) from exc
        except httpx.NetworkError as exc:
            raise ContentTranslationProviderRequestError(
                "Content translation provider network request failed"
            ) from exc
        except httpx.HTTPStatusError as exc:
            status_code = exc.response.status_code if exc.response is not None else "unknown"
            raise ContentTranslationProviderRequestError(
                f"Content translation provider returned HTTP {status_code}"
            ) from exc
        except httpx.HTTPError as exc:
            raise ContentTranslationProviderRequestError(
                "Content translation provider request failed"
            ) from exc

        latency_ms = int((perf_counter() - started_at) * 1000)

        try:
            data = response.json()
        except ValueError as exc:
            raise ContentTranslationProviderResponseError(
                "Content translation provider returned invalid JSON"
            ) from exc

        try:
            choices = data["choices"]
            message_content = choices[0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise ContentTranslationProviderResponseError(
                "Content translation provider response is missing message content"
            ) from exc

        if isinstance(message_content, list):
            message_content = "".join(
                part.get("text", "")
                for part in message_content
                if isinstance(part, dict) and part.get("type") == "text"
            )
        if not isinstance(message_content, str) or not message_content.strip():
            raise ContentTranslationProviderResponseError(
                "Content translation provider returned empty content"
            )

        parsed = _extract_json_object(message_content)
        try:
            result = ProviderTranslationResult.model_validate(parsed)
        except Exception as exc:  # pydantic ValidationError
            raise ContentTranslationProviderResponseError(
                "Content translation provider response did not match the required schema"
            ) from exc

        return ContentTranslationProviderResponse(
            result=result,
            provider_name=self.provider_name,
            model=str(data.get("model") or self.model),
            latency_ms=latency_ms,
        )


def build_content_translation_provider(
    *,
    provider_name: str | None = None,
    provider_settings: Settings | None = None,
) -> ContentTranslationProvider:
    resolved_settings = provider_settings or settings
    normalized_provider_name = (
        provider_name or resolved_settings.content_translation_provider
    ).strip().lower()
    if normalized_provider_name == "mock":
        return MockContentTranslationProvider()
    if normalized_provider_name == "openai_compatible":
        return OpenAICompatibleContentTranslationProvider.from_settings(resolved_settings)
    raise ContentTranslationProviderConfigurationError(
        f"Unsupported CONTENT_TRANSLATION_PROVIDER `{normalized_provider_name}`"
    )
