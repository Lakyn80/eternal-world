from __future__ import annotations

import httpx
import pytest
from pydantic import SecretStr

from app.core.config import Settings
from app.modules.ai_agents.brain.providers.openai_compatible import (
    OpenAICompatibleBrainAgentProvider,
)
from app.modules.ai_agents.brain.service import BrainAgentService
from app.modules.rag_evaluation.brain_eval_report import (
    build_brain_rag_eval_markdown,
    build_brain_rag_eval_qa_markdown,
    write_brain_rag_eval_artifacts,
)
from app.modules.rag_evaluation.brain_eval_runner import (
    build_brain_rag_eval_provider,
    preflight_brain_rag_eval,
    resolve_brain_rag_eval_cases,
    run_brain_rag_eval,
)
from app.modules.rag_evaluation.cases import (
    ALL_RAG_EVALUATION_CASES,
    FOUNDATION_RAG_EVALUATION_CASES,
)
from app.modules.rag_evaluation.exceptions import BrainRagEvalConfigurationError
from app.modules.rag_evaluation.schemas import BrainRagEvalConfig


def _openai_compatible_settings(**overrides) -> Settings:
    base = {
        "ai_brain_provider": "openai_compatible",
        "ai_brain_model": "deepseek-chat",
        "ai_brain_api_key": SecretStr("test-api-key"),
        "ai_brain_base_url": "https://api.deepseek.com/v1",
    }
    base.update(overrides)
    return Settings(**base)


class FakeResponse:
    def __init__(self, *, json_data: dict | None = None, status_code: int = 200) -> None:
        self._json_data = json_data if json_data is not None else {}
        self.status_code = status_code

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            request = httpx.Request("POST", "https://example.test/v1/chat/completions")
            response = httpx.Response(self.status_code, request=request)
            raise httpx.HTTPStatusError(
                f"HTTP {self.status_code}",
                request=request,
                response=response,
            )

    def json(self):
        return self._json_data


class FakeHttpClient:
    def __init__(self, *, response_text: str) -> None:
        self.response_text = response_text
        self.calls: list[dict] = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        return None

    def post(self, url, headers=None, json=None):
        self.calls.append({"url": url, "headers": headers, "json": json})
        return FakeResponse(
            json_data={
                "model": "deepseek-chat",
                "choices": [{"message": {"content": self.response_text}}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
            }
        )


def test_resolve_brain_rag_eval_cases_returns_expected_sets():
    assert len(resolve_brain_rag_eval_cases("foundation")) == len(FOUNDATION_RAG_EVALUATION_CASES)
    assert len(resolve_brain_rag_eval_cases("all")) == len(ALL_RAG_EVALUATION_CASES)


def test_preflight_brain_rag_eval_fails_without_api_key():
    config = BrainRagEvalConfig(case_set="foundation")
    provider_settings = _openai_compatible_settings(ai_brain_api_key=None)

    result = preflight_brain_rag_eval(config, provider_settings=provider_settings)

    assert result.passed is False
    assert any("AI_BRAIN_API_KEY" in issue for issue in result.issues)


def test_preflight_brain_rag_eval_fails_for_mock_provider():
    config = BrainRagEvalConfig(provider_name="mock")
    provider_settings = Settings(ai_brain_provider="mock")

    result = preflight_brain_rag_eval(config, provider_settings=provider_settings)

    assert result.passed is False
    assert any("Supported values" in issue for issue in result.issues)


def test_preflight_brain_rag_eval_passes_with_valid_openai_compatible_config():
    config = BrainRagEvalConfig(case_set="foundation")
    provider_settings = _openai_compatible_settings()

    result = preflight_brain_rag_eval(config, provider_settings=provider_settings)

    assert result.passed is True
    assert result.case_count == len(FOUNDATION_RAG_EVALUATION_CASES)
    assert result.model == "deepseek-chat"


def test_run_brain_rag_eval_raises_when_preflight_fails():
    config = BrainRagEvalConfig(case_set="foundation")
    provider_settings = _openai_compatible_settings(ai_brain_api_key=None)

    with pytest.raises(BrainRagEvalConfigurationError, match="preflight failed"):
        run_brain_rag_eval(config, provider_settings=provider_settings)


def test_run_brain_rag_eval_uses_openai_compatible_provider_with_mocked_http():
    grounded_case = FOUNDATION_RAG_EVALUATION_CASES[0]
    lack_of_evidence_case = FOUNDATION_RAG_EVALUATION_CASES[1]
    response_queue = [
        (
            "The wedding ceremony took place in Brno according to the archival note "
            "and wedding memory evidence."
        ),
    ]
    clients: list[FakeHttpClient] = []

    def http_client_factory(_timeout_seconds: float):
        response_text = response_queue.pop(0) if response_queue else "unexpected call"
        client = FakeHttpClient(response_text=response_text)
        clients.append(client)
        return client

    provider = OpenAICompatibleBrainAgentProvider(
        model="deepseek-chat",
        api_key="test-api-key",
        base_url="https://api.deepseek.com/v1",
        timeout_seconds=5,
        http_client_factory=http_client_factory,
    )
    brain_service = BrainAgentService(provider=provider)
    config = BrainRagEvalConfig(
        case_set="foundation",
        write_artifacts=False,
        artifact_dir=None,
    )

    result = run_brain_rag_eval(
        config,
        provider_settings=_openai_compatible_settings(),
        brain_service=brain_service,
        cases=[grounded_case, lack_of_evidence_case],
    )

    assert result.passed is True
    assert result.provider_name == "openai_compatible"
    assert result.suite_result.failed_cases == 0
    assert len(clients) == 1
    messages = clients[0].calls[0]["json"]["messages"]
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
    assert "EVIDENCE HIERARCHY (strict)" in messages[0]["content"]
    assert "B2. Retrieved archival RAG evidence:" in messages[1]["content"]


def test_resolve_brain_rag_eval_cases_family_avatar():
    cases = resolve_brain_rag_eval_cases("family_avatar")
    assert len(cases) >= 25
    assert cases[0].case_id.startswith("family-")


def test_build_brain_rag_eval_provider_rejects_unsupported_provider():
    with pytest.raises(BrainRagEvalConfigurationError, match="does not support provider"):
        build_brain_rag_eval_provider(provider_name="mock")


def test_brain_rag_eval_qa_markdown_contains_question_and_full_answer():
    config = BrainRagEvalConfig(
        case_set="foundation",
        write_artifacts=False,
        artifact_dir=None,
    )
    result = run_brain_rag_eval(
        config,
        provider_settings=_openai_compatible_settings(),
        brain_service=BrainAgentService(
            provider=OpenAICompatibleBrainAgentProvider(
                model="deepseek-chat",
                api_key="test-api-key",
                base_url="https://api.deepseek.com/v1",
                timeout_seconds=5,
                http_client_factory=lambda _timeout: FakeHttpClient(
                    response_text="The wedding ceremony took place in Brno."
                ),
            )
        ),
        cases=[FOUNDATION_RAG_EVALUATION_CASES[0]],
    )

    qa_markdown = build_brain_rag_eval_qa_markdown(result)
    case_result = result.suite_result.results[0]

    assert "**Q:**" in qa_markdown
    assert case_result.user_query in qa_markdown
    assert case_result.answer_text in qa_markdown
    assert "Brain RAG Evaluation Q&A" in qa_markdown


def test_write_brain_rag_eval_artifacts_creates_json_and_markdown(tmp_path):
    config = BrainRagEvalConfig(
        case_set="foundation",
        artifact_dir=tmp_path,
        write_artifacts=True,
    )
    provider_settings = _openai_compatible_settings()
    result = run_brain_rag_eval(
        config,
        provider_settings=provider_settings,
        brain_service=BrainAgentService(
            provider=OpenAICompatibleBrainAgentProvider(
                model="deepseek-chat",
                api_key="test-api-key",
                base_url="https://api.deepseek.com/v1",
                timeout_seconds=5,
                http_client_factory=lambda _timeout: FakeHttpClient(
                    response_text="The wedding ceremony took place in Brno."
                ),
            )
        ),
        cases=[FOUNDATION_RAG_EVALUATION_CASES[0]],
    )

    artifact_paths = write_brain_rag_eval_artifacts(result=result, artifact_dir=tmp_path)

    assert (tmp_path / "brain_rag_eval_result.json").exists()
    assert (tmp_path / "report.md").exists()
    assert (tmp_path / "qa_report.md").exists()
    assert (tmp_path / "runs" / result.run_id / "brain_rag_eval_result.json").exists()
    assert (tmp_path / "runs" / result.run_id / "qa_report.md").exists()
    markdown = build_brain_rag_eval_markdown(result)
    assert "Brain RAG Evaluation Report" in markdown
    assert "**Q:**" not in markdown
    assert "Question:" in markdown
    assert result.suite_result.results[0].user_query
    assert result.suite_result.results[0].answer_text
    assert artifact_paths["latest_qa_report_md"].endswith("qa_report.md")
    assert artifact_paths["latest_result_json"].endswith("brain_rag_eval_result.json")
