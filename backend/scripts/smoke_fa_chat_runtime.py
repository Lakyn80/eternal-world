from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass

import httpx


DEFAULT_BASE_URL = "http://localhost:8033"
DEFAULT_MESSAGE = "Где ты жила в детстве?"
DEFAULT_EXPECTED_MARKER = "Попице"
DEFAULT_TIMEOUT_SECONDS = 60.0


def _configure_stdio_for_unicode() -> None:
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="replace")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Cold-start runtime smoke check for the live FA demo chat endpoint. "
            "Verifies the backend can serve a real grounded answer end to end "
            "(profile resolution, BGE-M3 query embedding, Qdrant retrieval, Brain "
            "answer generation) after a container recreate, instead of failing "
            "with a cold BGE-M3 runtime/cache error."
        ),
    )
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--message", default=DEFAULT_MESSAGE)
    parser.add_argument("--expected-marker", default=DEFAULT_EXPECTED_MARKER)
    parser.add_argument("--timeout-seconds", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--json", action="store_true", dest="json_output")
    return parser


@dataclass(frozen=True)
class FaChatRuntimeSmokeResult:
    base_url: str
    status_code: int
    trace_id: str | None
    retrieval_used: bool | None
    lack_of_evidence: bool | None
    guard_applied: bool | None
    answer_contains_expected_marker: bool
    error_detail: str | None

    @property
    def passed(self) -> bool:
        if self.status_code != 200:
            return False
        if not self.retrieval_used:
            return False
        if self.lack_of_evidence:
            return False
        return self.answer_contains_expected_marker


def run_fa_chat_runtime_smoke(
    *,
    base_url: str,
    message: str,
    expected_marker: str,
    timeout_seconds: float,
) -> FaChatRuntimeSmokeResult:
    url = f"{base_url.rstrip('/')}/api/demo/fa-chat/message"
    with httpx.Client(timeout=timeout_seconds) as http_client:
        response = http_client.post(url, json={"message": message, "debug": True})

    if response.status_code != 200:
        error_detail: str | None = None
        try:
            error_detail = str(response.json().get("detail"))
        except Exception:  # noqa: BLE001 - best-effort error surface for the smoke report
            error_detail = response.text[:300]
        return FaChatRuntimeSmokeResult(
            base_url=base_url,
            status_code=response.status_code,
            trace_id=response.headers.get("x-request-id"),
            retrieval_used=None,
            lack_of_evidence=None,
            guard_applied=None,
            answer_contains_expected_marker=False,
            error_detail=error_detail,
        )

    body = response.json()
    answer = str(body.get("answer") or "")
    return FaChatRuntimeSmokeResult(
        base_url=base_url,
        status_code=response.status_code,
        trace_id=body.get("trace_id"),
        retrieval_used=bool(body.get("retrieval_used")),
        lack_of_evidence=bool(body.get("lack_of_evidence")),
        guard_applied=bool(body.get("guard_applied")),
        answer_contains_expected_marker=expected_marker in answer,
        error_detail=None,
    )


def _print_text_result(result: FaChatRuntimeSmokeResult) -> None:
    print(f"FA CHAT RUNTIME SMOKE RESULT: {'PASS' if result.passed else 'FAIL'}")
    print(
        "summary "
        f"base_url={result.base_url} status_code={result.status_code} "
        f"trace_id={result.trace_id} retrieval_used={result.retrieval_used} "
        f"lack_of_evidence={result.lack_of_evidence} guard_applied={result.guard_applied} "
        f"answer_contains_expected_marker={result.answer_contains_expected_marker}"
    )
    if result.error_detail:
        print(f"error_detail={result.error_detail}")


def main() -> int:
    _configure_stdio_for_unicode()
    args = _build_parser().parse_args()
    try:
        result = run_fa_chat_runtime_smoke(
            base_url=args.base_url,
            message=args.message,
            expected_marker=args.expected_marker,
            timeout_seconds=args.timeout_seconds,
        )
    except httpx.HTTPError as exc:
        print(f"error: could not reach {args.base_url}: {exc}", file=sys.stderr)
        return 1

    if args.json_output:
        print(json.dumps({**asdict(result), "passed": result.passed}, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        _print_text_result(result)

    return 0 if result.passed else 1


if __name__ == "__main__":
    sys.exit(main())
