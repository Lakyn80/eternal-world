from __future__ import annotations

import httpx

from scripts.smoke_fa_chat_runtime import _configure_stdio_for_unicode, run_fa_chat_runtime_smoke


class _FakeResponse:
    def __init__(self, *, status_code: int, body: dict[str, object], headers: dict[str, str] | None = None):
        self.status_code = status_code
        self._body = body
        self.headers = headers or {}
        self.text = str(body)

    def json(self) -> dict[str, object]:
        return dict(self._body)


class _FakeClient:
    def __init__(self, response: _FakeResponse):
        self._response = response

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def post(self, url: str, json: dict[str, object]):
        return self._response


class _FakeStream:
    def __init__(self):
        self.calls: list[tuple[str, str]] = []

    def reconfigure(self, *, encoding: str, errors: str):
        self.calls.append((encoding, errors))


def test_configure_stdio_for_unicode_reconfigures_stdout_and_stderr(monkeypatch):
    fake_stdout = _FakeStream()
    fake_stderr = _FakeStream()
    monkeypatch.setattr("scripts.smoke_fa_chat_runtime.sys.stdout", fake_stdout)
    monkeypatch.setattr("scripts.smoke_fa_chat_runtime.sys.stderr", fake_stderr)

    _configure_stdio_for_unicode()

    assert fake_stdout.calls == [("utf-8", "replace")]
    assert fake_stderr.calls == [("utf-8", "replace")]


def test_run_fa_chat_runtime_smoke_passes_on_grounded_answer(monkeypatch):
    monkeypatch.setattr(
        httpx,
        "Client",
        lambda timeout: _FakeClient(
            _FakeResponse(
                status_code=200,
                body={
                    "answer": "В детстве я жила у Попице.",
                    "trace_id": "trace-1",
                    "retrieval_used": True,
                    "lack_of_evidence": False,
                    "guard_applied": False,
                },
            )
        ),
    )

    result = run_fa_chat_runtime_smoke(
        base_url="http://localhost:8033",
        message="Где ты жила в детстве?",
        expected_marker="Попице",
        timeout_seconds=30.0,
    )

    assert result.passed is True
    assert result.status_code == 200
    assert result.trace_id == "trace-1"


def test_run_fa_chat_runtime_smoke_surfaces_safe_error_detail(monkeypatch):
    monkeypatch.setattr(
        httpx,
        "Client",
        lambda timeout: _FakeClient(
            _FakeResponse(
                status_code=503,
                body={
                    "detail": (
                        "Демо временно недоступно: модель эмбеддингов BGE-M3 не инициализирована. "
                        "Запустите подготовку модели и повторите запрос."
                    )
                },
                headers={"x-request-id": "trace-503"},
            )
        ),
    )

    result = run_fa_chat_runtime_smoke(
        base_url="http://localhost:8033",
        message="Где ты жила в детстве?",
        expected_marker="Попице",
        timeout_seconds=30.0,
    )

    assert result.passed is False
    assert result.status_code == 503
    assert result.trace_id == "trace-503"
    assert "BGE-M3" in str(result.error_detail)
