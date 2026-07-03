from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence


BACKEND_DIR = Path(__file__).resolve().parents[1]
DEFAULT_ARTIFACT_ROOT = BACKEND_DIR / "artifacts" / "real_question_eval"
DEFAULT_RUNS_DIR = DEFAULT_ARTIFACT_ROOT / "runs"
SUMMARY_FILE_NAME = "real_question_eval_summary.json"
SUMMARY_MARKDOWN_FILE_NAME = "real_question_eval_summary.md"
FULL_RESULTS_FILE_NAME = "real_question_eval_full_results.json"
FULL_RESULTS_MARKDOWN_FILE_NAME = "real_question_eval_full_results.md"
LEGACY_SUMMARY_FILE_NAME = "summary.json"
RESULT_FILE_NAME = "real_question_eval_result.json"
SEPARATOR = "=" * 80
MISSING_MODEL_METRICS_WARNING = "Per-model compact metrics are not present in this artifact."


@dataclass(frozen=True)
class CompactModelResult:
    model: str
    passed_questions: int | None
    total_questions: int | None
    evidence_coverage: float | None
    missing_evidence: int | None
    distractors: int | None
    latency_ms: float | None


@dataclass(frozen=True)
class CompactRunSummary:
    run_id: str
    dataset_name: str | None
    dataset_id: str | None
    run_status: str | None
    quality_status: str | None
    quality_gate: dict[str, Any]
    overall_winner: str | None
    overall_winner_reason: str | None
    preflight_validation: dict[str, Any]
    model_results: list[CompactModelResult]
    artifact_path: Path
    warning: str | None = None


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Print compact summaries for real question eval artifacts.")
    parser.add_argument(
        "--runs-dir",
        default=str(DEFAULT_RUNS_DIR),
        help="Directory that contains archived real question eval run folders.",
    )
    parser.add_argument(
        "--show-full-paths",
        action="store_true",
        help="Print summary and full-results artifact paths for each run.",
    )
    target_group = parser.add_mutually_exclusive_group(required=True)
    target_group.add_argument("--latest", type=int, help="Print the latest N archived run summaries.")
    target_group.add_argument(
        "--latest-fake",
        action="store_true",
        help="Print the latest fake artifact summary from latest_fake.",
    )
    target_group.add_argument("--run-dir", help="Print the summary for one specific archived run directory.")
    return parser


def _read_json_payload(path: Path) -> dict[str, Any]:
    try:
        raw_payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return raw_payload if isinstance(raw_payload, dict) else {}


def _coerce_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _coerce_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _extract_string(value: Any) -> str | None:
    if isinstance(value, str):
        stripped = value.strip()
        return stripped or None
    if value is None:
        return None
    return str(value)


def _extract_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return None


def _extract_float(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


def _first_non_none(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _resolve_dataset_name(payload: dict[str, Any]) -> str | None:
    client_dataset = _coerce_dict(_coerce_dict(payload.get("client_view")).get("dataset"))
    developer_dataset = _coerce_dict(_coerce_dict(payload.get("developer_view")).get("dataset"))
    return _first_non_none(
        _extract_string(payload.get("dataset_name")),
        _extract_string(_coerce_dict(payload.get("dataset")).get("name")),
        _extract_string(client_dataset.get("name")),
        _extract_string(developer_dataset.get("name")),
    )


def _resolve_dataset_id(payload: dict[str, Any]) -> str | None:
    client_dataset = _coerce_dict(_coerce_dict(payload.get("client_view")).get("dataset"))
    developer_dataset = _coerce_dict(_coerce_dict(payload.get("developer_view")).get("dataset"))
    return _first_non_none(
        _extract_string(payload.get("dataset_id")),
        _extract_string(_coerce_dict(payload.get("dataset")).get("id")),
        _extract_string(client_dataset.get("id")),
        _extract_string(developer_dataset.get("id")),
    )


def _resolve_run_status(payload: dict[str, Any]) -> str | None:
    client_view = _coerce_dict(payload.get("client_view"))
    developer_view = _coerce_dict(payload.get("developer_view"))
    return _first_non_none(
        _extract_string(payload.get("run_status")),
        _extract_string(client_view.get("run_status")),
        _extract_string(developer_view.get("run_status")),
        "FAILED" if payload.get("error") else None,
    )


def _resolve_quality_status(payload: dict[str, Any]) -> str | None:
    client_view = _coerce_dict(payload.get("client_view"))
    developer_view = _coerce_dict(payload.get("developer_view"))
    status = _first_non_none(
        _extract_string(payload.get("quality_status")),
        _extract_string(client_view.get("quality_status")),
        _extract_string(developer_view.get("quality_status")),
        _extract_string(payload.get("status")),
    )
    if status is not None:
        return status
    passed = payload.get("passed")
    if isinstance(passed, bool):
        return "PASS" if passed else "FAIL"
    return None


def _resolve_overall_winner(payload: dict[str, Any]) -> str | None:
    client_view = _coerce_dict(payload.get("client_view"))
    return _first_non_none(
        _extract_string(payload.get("overall_winner")),
        _extract_string(payload.get("overall_winner_model_code")),
        _extract_string(client_view.get("overall_winner")),
        _extract_string(_coerce_dict(payload.get("selected_config")).get("best_model_code")),
        _extract_string(_coerce_dict(_coerce_dict(payload.get("developer_view")).get("selected_config")).get("best_model_code")),
    )


def _resolve_overall_winner_reason(payload: dict[str, Any]) -> str | None:
    client_view = _coerce_dict(payload.get("client_view"))
    developer_view = _coerce_dict(payload.get("developer_view"))
    return _first_non_none(
        _extract_string(payload.get("overall_winner_reason")),
        _extract_string(client_view.get("overall_winner_reason")),
        _extract_string(developer_view.get("overall_winner_reason")),
    )


def _resolve_quality_gate(payload: dict[str, Any]) -> dict[str, Any]:
    client_view = _coerce_dict(payload.get("client_view"))
    developer_view = _coerce_dict(payload.get("developer_view"))
    return _first_non_none(
        _coerce_dict(payload.get("quality_gate")),
        _coerce_dict(client_view.get("quality_gate")),
        _coerce_dict(developer_view.get("quality_gate")),
        {},
    )


def _resolve_preflight_validation(payload: dict[str, Any]) -> dict[str, Any]:
    client_view = _coerce_dict(payload.get("client_view"))
    developer_view = _coerce_dict(payload.get("developer_view"))
    return _first_non_none(
        _coerce_dict(payload.get("preflight_validation")),
        _coerce_dict(client_view.get("preflight_validation")),
        _coerce_dict(developer_view.get("preflight_validation")),
        {},
    )


def _resolve_total_questions(payload: dict[str, Any]) -> int | None:
    direct_total = _extract_int(payload.get("total_questions"))
    if direct_total is not None:
        return direct_total

    developer_questions = _coerce_list(_coerce_dict(payload.get("developer_view")).get("questions"))
    if developer_questions:
        return len(developer_questions)

    client_questions = _coerce_list(_coerce_dict(payload.get("client_view")).get("questions"))
    if client_questions:
        return len(client_questions)

    return None


def _extract_official_metrics(item: dict[str, Any]) -> dict[str, Any]:
    return _coerce_dict(item.get("official_metrics"))


def _build_model_result_from_summary_item(item: dict[str, Any], *, default_total_questions: int | None) -> CompactModelResult | None:
    official_metrics = _extract_official_metrics(item)
    model = _first_non_none(
        _extract_string(item.get("model")),
        _extract_string(item.get("provider")),
        _extract_string(item.get("model_code")),
        _extract_string(item.get("provider_code")),
    )
    if model is None:
        return None

    return CompactModelResult(
        model=model,
        passed_questions=_extract_int(item.get("passed_questions")),
        total_questions=_first_non_none(
            _extract_int(item.get("total_questions")),
            default_total_questions,
        ),
        evidence_coverage=_first_non_none(
            _extract_float(item.get("evidence_coverage")),
            _extract_float(item.get("average_evidence_coverage")),
            _extract_float(official_metrics.get("evidence_marker_coverage")),
        ),
        missing_evidence=_first_non_none(
            _extract_int(item.get("missing_evidence")),
            _extract_int(item.get("total_missing_markers")),
            _extract_int(official_metrics.get("missing_expected_marker_count")),
        ),
        distractors=_first_non_none(
            _extract_int(item.get("distractors")),
            _extract_int(item.get("false_positives")),
            _extract_int(item.get("false_positive_count")),
            _extract_int(item.get("total_false_positive_markers")),
            _extract_int(official_metrics.get("false_positive_count")),
        ),
        latency_ms=_first_non_none(
            _extract_float(item.get("latency_ms")),
            _extract_float(item.get("average_latency_ms")),
            _extract_float(official_metrics.get("average_latency_ms")),
        ),
    )


def _extract_model_results(payload: dict[str, Any], *, default_total_questions: int | None) -> list[CompactModelResult]:
    candidate_lists = [
        _coerce_list(payload.get("model_results")),
        _coerce_list(payload.get("aggregate_results")),
        _coerce_list(_coerce_dict(payload.get("developer_view")).get("aggregate_results")),
    ]
    for candidate_list in candidate_lists:
        parsed_results = [
            parsed
            for parsed in (
                _build_model_result_from_summary_item(_coerce_dict(item), default_total_questions=default_total_questions)
                for item in candidate_list
            )
            if parsed is not None
        ]
        if parsed_results:
            return parsed_results
    return []


def _resolve_run_id(payload: dict[str, Any], *, artifact_path: Path) -> str:
    run_id = _extract_string(payload.get("run_id"))
    if run_id is not None:
        return run_id

    parent_name = artifact_path.parent.name
    if artifact_path.name in {SUMMARY_FILE_NAME, LEGACY_SUMMARY_FILE_NAME} and parent_name == "latest_fake":
        return "latest_fake"
    if artifact_path.name == RESULT_FILE_NAME and parent_name == "latest_fake":
        return "latest_fake"
    return parent_name


def summarize_artifact(artifact_path: Path) -> CompactRunSummary:
    payload = _read_json_payload(artifact_path)
    total_questions = _resolve_total_questions(payload)
    model_results = _extract_model_results(payload, default_total_questions=total_questions)
    warning = None if model_results else MISSING_MODEL_METRICS_WARNING
    return CompactRunSummary(
        run_id=_resolve_run_id(payload, artifact_path=artifact_path),
        dataset_name=_resolve_dataset_name(payload),
        dataset_id=_resolve_dataset_id(payload),
        run_status=_resolve_run_status(payload),
        quality_status=_resolve_quality_status(payload),
        quality_gate=_resolve_quality_gate(payload),
        overall_winner=_resolve_overall_winner(payload),
        overall_winner_reason=_resolve_overall_winner_reason(payload),
        preflight_validation=_resolve_preflight_validation(payload),
        model_results=model_results,
        artifact_path=artifact_path,
        warning=warning,
    )


def _format_float(value: float | None, *, decimals: int) -> str:
    if value is None:
        return "n/a"
    return f"{value:.{decimals}f}"


def _format_int(value: int | None) -> str:
    if value is None:
        return "n/a"
    return str(value)


def _format_quality_gate(gate: dict[str, Any]) -> str:
    if not gate:
        return "n/a"
    gate_name = _extract_string(gate.get("gate_name")) or "unknown"
    threshold = _extract_float(gate.get("threshold"))
    best_model_code = _extract_string(gate.get("best_model_code")) or "none"
    best_passed_questions = _extract_int(gate.get("best_passed_questions"))
    total_questions = _extract_int(gate.get("total_questions"))
    best_pass_rate = _extract_float(gate.get("best_pass_rate"))
    threshold_text = _format_float(threshold, decimals=4)
    pass_rate_text = _format_float(best_pass_rate, decimals=4)
    counts_text = (
        f"{_format_int(best_passed_questions)}/{_format_int(total_questions)}"
        if best_passed_questions is not None or total_questions is not None
        else "n/a"
    )
    return f"{gate_name} >= {threshold_text} (best={best_model_code} {counts_text}, pass_rate={pass_rate_text})"


def _format_preflight_validation(preflight_validation: dict[str, Any]) -> str:
    if not preflight_validation:
        return "n/a"
    passed = preflight_validation.get("passed")
    status = "PASS" if passed is True else "FAIL" if passed is False else "unknown"
    missing_marker_count = _extract_int(preflight_validation.get("missing_marker_count"))
    source_document_count = _extract_int(preflight_validation.get("source_document_count"))
    source_chunk_count = _extract_int(preflight_validation.get("source_chunk_count"))
    return (
        f"{status} "
        f"(missing_markers={_format_int(missing_marker_count)}, "
        f"source_documents={_format_int(source_document_count)}, "
        f"source_chunks={_format_int(source_chunk_count)})"
    )


def _format_related_artifact_paths(artifact_path: Path) -> list[str]:
    artifact_dir = artifact_path.parent
    return [
        f"SUMMARY MARKDOWN: {artifact_dir / SUMMARY_MARKDOWN_FILE_NAME}",
        f"SUMMARY JSON: {artifact_dir / SUMMARY_FILE_NAME}",
        f"FULL RESULTS MARKDOWN: {artifact_dir / FULL_RESULTS_MARKDOWN_FILE_NAME}",
        f"FULL RESULTS JSON: {artifact_dir / FULL_RESULTS_FILE_NAME}",
    ]


def render_summary(summary: CompactRunSummary, *, show_full_paths: bool = False) -> str:
    lines = [
        "REAL QUESTION EVAL SUMMARY",
        SEPARATOR,
        f"RUN: {summary.run_id}",
        f"DATASET: {summary.dataset_name or 'unknown'}",
    ]
    if summary.dataset_id is not None:
        lines.append(f"DATASET ID: {summary.dataset_id}")
    lines.extend(
        [
            f"RUN STATUS: {summary.run_status or 'unknown'}",
            f"QUALITY STATUS: {summary.quality_status or 'unknown'}",
            f"QUALITY GATE: {_format_quality_gate(summary.quality_gate)}",
            f"WINNER: {summary.overall_winner or 'unknown'}",
            f"WINNER REASON: {summary.overall_winner_reason or 'n/a'}",
            f"PREFLIGHT: {_format_preflight_validation(summary.preflight_validation)}",
            f"ARTIFACT PATH: {summary.artifact_path}",
        ]
    )
    if show_full_paths:
        lines.extend(["", "ARTIFACT FILES", *_format_related_artifact_paths(summary.artifact_path)])
    if summary.warning is not None:
        lines.extend(["", f"WARNING: {summary.warning}", SEPARATOR])
        return "\n".join(lines)

    header = ["model", "passed", "total", "coverage", "missing", "distractors", "latency_ms"]
    rows = [
        [
            item.model,
            _format_int(item.passed_questions),
            _format_int(item.total_questions),
            _format_float(item.evidence_coverage, decimals=4),
            _format_int(item.missing_evidence),
            _format_int(item.distractors),
            _format_float(item.latency_ms, decimals=1),
        ]
        for item in summary.model_results
    ]
    widths = [len(column) for column in header]
    for row in rows:
        for index, cell in enumerate(row):
            widths[index] = max(widths[index], len(cell))

    lines.extend(["", "MODEL RESULTS"])
    lines.append("  ".join(column.ljust(widths[index]) for index, column in enumerate(header)))
    for row in rows:
        lines.append("  ".join(cell.ljust(widths[index]) for index, cell in enumerate(row)))
    lines.append(SEPARATOR)
    return "\n".join(lines)


def _resolve_latest_fake_artifact_path(*, runs_dir: Path) -> Path:
    artifact_root = runs_dir.parent
    latest_fake_dir = artifact_root / "latest_fake"
    return _resolve_artifact_path_in_dir(latest_fake_dir)


def _resolve_artifact_path_in_dir(directory: Path) -> Path:
    summary_path = directory / SUMMARY_FILE_NAME
    if summary_path.exists():
        return summary_path
    legacy_summary_path = directory / LEGACY_SUMMARY_FILE_NAME
    if legacy_summary_path.exists():
        return legacy_summary_path
    result_path = directory / RESULT_FILE_NAME
    if result_path.exists():
        return result_path
    raise FileNotFoundError(
        f"No {SUMMARY_FILE_NAME}, {LEGACY_SUMMARY_FILE_NAME}, or {RESULT_FILE_NAME} found in {directory}"
    )


def _resolve_latest_run_artifact_paths(*, runs_dir: Path, limit: int) -> list[Path]:
    if limit <= 0:
        raise ValueError("--latest must be greater than zero.")
    if not runs_dir.exists():
        raise FileNotFoundError(f"Runs directory does not exist: {runs_dir}")

    candidates: list[tuple[str, Path]] = []
    for run_dir in runs_dir.iterdir():
        if not run_dir.is_dir():
            continue
        try:
            artifact_path = _resolve_artifact_path_in_dir(run_dir)
        except FileNotFoundError:
            continue
        candidates.append((run_dir.name, artifact_path))

    candidates.sort(key=lambda item: item[0], reverse=True)
    return [artifact_path for _, artifact_path in candidates[:limit]]


def resolve_target_artifact_paths(args: argparse.Namespace) -> list[Path]:
    runs_dir = Path(args.runs_dir).resolve()
    if args.latest_fake:
        return [_resolve_latest_fake_artifact_path(runs_dir=runs_dir)]
    if args.run_dir:
        return [_resolve_artifact_path_in_dir(Path(args.run_dir).resolve())]
    return _resolve_latest_run_artifact_paths(runs_dir=runs_dir, limit=args.latest)


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        artifact_paths = resolve_target_artifact_paths(args)
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    output_blocks = [
        render_summary(summarize_artifact(path), show_full_paths=bool(args.show_full_paths))
        for path in artifact_paths
    ]
    print("\n\n".join(output_blocks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
