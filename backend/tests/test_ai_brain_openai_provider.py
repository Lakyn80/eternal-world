from __future__ import annotations

import httpx
import pytest
from pydantic import SecretStr

from app.core.config import Settings
from app.modules.ai_agents.brain.context import (
    BrainGroundedContext,
    BrainMemoryEvidence,
    BrainProfileContext,
    BrainRagEvidence,
)
from app.modules.ai_agents.brain.provider import (
    BrainProviderConfigurationError,
    BrainProviderRequestError,
    BrainProviderResponseError,
)
from app.modules.ai_agents.brain.providers.openai_compatible import (
    OpenAICompatibleBrainAgentProvider,
)
from app.modules.ai_agents.schemas import BrainAgentRequest, MemoryProfileContext


def _build_request(
    *,
    user_message: str = "Tell me about Prague",
    system_prompt: str = "System prompt from prompt builder",
    user_prompt: str = "User prompt from prompt builder",
    prompt: str | None = None,
    grounded_context: BrainGroundedContext | None = None,
) -> BrainAgentRequest:
    resolved_prompt = prompt if prompt is not None else f"{system_prompt}\n\n---\n\n{user_prompt}"
    return BrainAgentRequest(
        profile=MemoryProfileContext(id=1, name="Ada"),
        user_message=user_message,
        recent_history=[],
        grounded_context=grounded_context,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        prompt=resolved_prompt,
    )


def _grounded_context(*, has_memory_evidence: bool = False, has_rag_evidence: bool = False):
    evidence_items = []
    retrieved_evidence_items = []
    if has_memory_evidence:
        evidence_items.append(
            BrainMemoryEvidence(
                source_id=1,
                title="Verified Memory",
                memory_type="text",
                content_preview="Verified evidence",
                selection_reason="test",
            )
        )
    if has_rag_evidence:
        retrieved_evidence_items.append(
            BrainRagEvidence(
                chunk_id=10,
                source_id=20,
                embedding_id=30,
                score=0.91,
                source_document_type="manual_text",
                validation_status="valid",
                text_hash="hash-123",
                content_preview="Retrieved evidence",
            )
        )
    return BrainGroundedContext(
        profile_context=BrainProfileContext(profile_id=1, name="Ada"),
        evidence_items=evidence_items,
        retrieved_evidence_items=retrieved_evidence_items,
    )


class FakeResponse:
    def __init__(
        self,
        *,
        json_data=None,
        status_code: int = 200,
        raise_http_error: bool = False,
    ) -> None:
        self._json_data = json_data if json_data is not None else {}
        self.status_code = status_code
        self._raise_http_error = raise_http_error

    def raise_for_status(self) -> None:
        if not self._raise_http_error:
            return

        request = httpx.Request("POST", "https://example.test/v1/chat/completions")
        response = httpx.Response(self.status_code, request=request)
        raise httpx.HTTPStatusError(
            f"HTTP {self.status_code}",
            request=request,
            response=response,
        )

    def json(self):
        if isinstance(self._json_data, Exception):
            raise self._json_data

        return self._json_data


class FakeClient:
    def __init__(self, response=None, exception: Exception | None = None) -> None:
        self.response = response
        self.exception = exception
        self.calls: list[dict[str, object]] = []

    def __enter__(self) -> "FakeClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        return False

    def post(self, url: str, *, headers: dict[str, str], json: dict[str, object]):
        self.calls.append({"url": url, "headers": headers, "json": json})
        if self.exception is not None:
            raise self.exception

        return self.response


def test_from_settings_requires_model_for_openai_compatible_provider():
    selected_settings = Settings(
        _env_file=None,
        ai_brain_provider="openai_compatible",
        ai_brain_api_key=SecretStr("super-secret"),
    )

    with pytest.raises(BrainProviderConfigurationError) as exc_info:
        OpenAICompatibleBrainAgentProvider.from_settings(selected_settings)

    assert "AI_BRAIN_MODEL is required" in str(exc_info.value)


def test_from_settings_uses_configured_model_base_url_api_key_timeout_and_generation_options():
    selected_settings = Settings(
        _env_file=None,
        ai_brain_provider="openai_compatible",
        ai_brain_model="deepseek-chat",
        ai_brain_api_key=SecretStr("super-secret"),
        ai_brain_base_url="https://example.test/v1/",
        ai_brain_timeout_seconds=12.5,
        ai_brain_temperature=0.1,
        ai_brain_max_tokens=256,
    )

    provider = OpenAICompatibleBrainAgentProvider.from_settings(selected_settings)

    assert provider.model == "deepseek-chat"
    assert provider.base_url == "https://example.test/v1"
    assert provider.api_key == "super-secret"
    assert provider.timeout_seconds == 12.5
    assert provider.temperature == 0.1
    assert provider.max_tokens == 256


def test_build_request_uses_system_and_user_prompt_messages_and_normalized_chat_completions_url():
    provider = OpenAICompatibleBrainAgentProvider(
        model="brain-model",
        api_key="super-secret",
        base_url="https://example.test/v1/",
        timeout_seconds=5,
        temperature=0.2,
        max_tokens=128,
    )

    prepared_request = provider.build_request(
        _build_request(
            system_prompt="System prompt from prompt builder",
            user_prompt="User prompt from prompt builder",
        )
    )

    assert prepared_request.url == "https://example.test/v1/chat/completions"
    assert prepared_request.headers == {
        "Authorization": "Bearer super-secret",
        "Content-Type": "application/json",
    }
    assert prepared_request.payload == {
        "model": "brain-model",
        "messages": [
            {"role": "system", "content": "System prompt from prompt builder"},
            {"role": "user", "content": "User prompt from prompt builder"},
        ],
        "temperature": 0.2,
        "max_tokens": 128,
    }


def test_build_request_keeps_explicit_chat_completions_endpoint_unchanged():
    provider = OpenAICompatibleBrainAgentProvider(
        model="brain-model",
        api_key="super-secret",
        base_url="https://example.test/v1/chat/completions",
        timeout_seconds=5,
    )

    prepared_request = provider.build_request(_build_request())

    assert prepared_request.url == "https://example.test/v1/chat/completions"


def test_generate_response_returns_text_and_safe_metadata():
    fake_client = FakeClient(
        response=FakeResponse(
            json_data={
                "model": "brain-model-final",
                "choices": [
                    {
                        "message": {
                            "content": "Grounded answer from provider.",
                        }
                    }
                ],
                "usage": {
                    "prompt_tokens": 11,
                    "completion_tokens": 7,
                    "total_tokens": 18,
                    "ignored_field": "value",
                },
            }
        )
    )
    provider = OpenAICompatibleBrainAgentProvider(
        model="brain-model",
        api_key="super-secret",
        base_url="https://example.test/v1",
        timeout_seconds=5,
        http_client_factory=lambda timeout: fake_client,
    )

    response = provider.generate_response(
        _build_request(grounded_context=_grounded_context(has_memory_evidence=True))
    )

    assert response.text == "Grounded answer from provider."
    assert response.provider_name == "openai_compatible"
    assert response.metadata["agent"] == "brain"
    assert response.metadata["provider_type"] == "openai_compatible"
    assert response.metadata["model"] == "brain-model-final"
    assert response.metadata["grounding_status"] == "grounded"
    assert isinstance(response.metadata["latency_ms"], int)
    assert response.metadata["latency_ms"] >= 0
    assert response.metadata["usage"] == {
        "prompt_tokens": 11,
        "completion_tokens": 7,
        "total_tokens": 18,
    }
    assert "api_key" not in response.metadata
    assert fake_client.calls[0]["headers"]["Authorization"] == "Bearer super-secret"


def test_generate_response_supports_text_content_arrays():
    fake_client = FakeClient(
        response=FakeResponse(
            json_data={
                "choices": [
                    {
                        "message": {
                            "content": [
                                {"type": "text", "text": "First line."},
                                {"type": "text", "text": "Second line."},
                            ]
                        }
                    }
                ]
            }
        )
    )
    provider = OpenAICompatibleBrainAgentProvider(
        model="brain-model",
        api_key="super-secret",
        base_url="https://example.test/v1",
        timeout_seconds=5,
        http_client_factory=lambda timeout: fake_client,
    )

    response = provider.generate_response(
        _build_request(grounded_context=_grounded_context(has_rag_evidence=True))
    )

    assert response.text == "First line.\nSecond line."


def test_generate_response_returns_deterministic_lack_of_evidence_without_http_call():
    was_called = False

    def fail_if_called(timeout: float):
        nonlocal was_called
        was_called = True
        raise AssertionError("HTTP client should not be created without evidence for factual queries")

    provider = OpenAICompatibleBrainAgentProvider(
        model="brain-model",
        api_key="super-secret",
        base_url="https://example.test/v1",
        timeout_seconds=5,
        http_client_factory=fail_if_called,
    )

    response = provider.generate_response(
        _build_request(
            user_message="What happened in Prague?",
            grounded_context=_grounded_context(),
        )
    )

    assert was_called is False
    assert response.text == "I don't remember that."
    assert response.provider_name == "openai_compatible"
    assert response.metadata["grounding_status"] == "no_evidence"
    assert response.metadata["provider_type"] == "openai_compatible"
    assert response.metadata["model"] == "brain-model"
    assert response.metadata["latency_ms"] == 0


@pytest.mark.parametrize(
    ("exception", "expected_message"),
    [
        (
            httpx.ConnectTimeout("timed out"),
            "OpenAI-compatible provider request timed out",
        ),
        (
            httpx.ConnectError("network down"),
            "OpenAI-compatible provider network request failed",
        ),
    ],
)
def test_generate_response_raises_safe_request_errors_for_timeout_and_network_failures(
    exception: Exception,
    expected_message: str,
):
    fake_client = FakeClient(exception=exception)
    provider = OpenAICompatibleBrainAgentProvider(
        model="brain-model",
        api_key="super-secret",
        base_url="https://example.test/v1",
        timeout_seconds=5,
        http_client_factory=lambda timeout: fake_client,
    )

    with pytest.raises(BrainProviderRequestError) as exc_info:
        provider.generate_response(
            _build_request(grounded_context=_grounded_context(has_memory_evidence=True))
        )

    assert str(exc_info.value) == expected_message
    assert "super-secret" not in str(exc_info.value)


def test_generate_response_raises_safe_request_error_for_http_status_failures():
    fake_client = FakeClient(response=FakeResponse(status_code=429, raise_http_error=True))
    provider = OpenAICompatibleBrainAgentProvider(
        model="brain-model",
        api_key="super-secret",
        base_url="https://example.test/v1",
        timeout_seconds=5,
        http_client_factory=lambda timeout: fake_client,
    )

    with pytest.raises(BrainProviderRequestError) as exc_info:
        provider.generate_response(
            _build_request(grounded_context=_grounded_context(has_memory_evidence=True))
        )

    assert str(exc_info.value) == "OpenAI-compatible provider returned HTTP 429"
    assert "super-secret" not in str(exc_info.value)


def test_generate_response_rejects_invalid_json_response():
    fake_client = FakeClient(response=FakeResponse(json_data=ValueError("bad json")))
    provider = OpenAICompatibleBrainAgentProvider(
        model="brain-model",
        api_key="super-secret",
        base_url="https://example.test/v1",
        timeout_seconds=5,
        http_client_factory=lambda timeout: fake_client,
    )

    with pytest.raises(BrainProviderResponseError) as exc_info:
        provider.generate_response(
            _build_request(grounded_context=_grounded_context(has_memory_evidence=True))
        )

    assert str(exc_info.value) == "OpenAI-compatible provider returned invalid JSON"


def test_generate_response_rejects_invalid_response_shape():
    fake_client = FakeClient(response=FakeResponse(json_data={"choices": []}))
    provider = OpenAICompatibleBrainAgentProvider(
        model="brain-model",
        api_key="super-secret",
        base_url="https://example.test/v1",
        timeout_seconds=5,
        http_client_factory=lambda timeout: fake_client,
    )

    with pytest.raises(BrainProviderResponseError) as exc_info:
        provider.generate_response(
            _build_request(grounded_context=_grounded_context(has_memory_evidence=True))
        )

    assert str(exc_info.value) == "OpenAI-compatible provider returned no choices"
