from __future__ import annotations

import json
from pathlib import Path

from scripts.print_real_question_eval_summary import (
    MISSING_MODEL_METRICS_WARNING,
    main,
    render_summary,
    summarize_artifact,
)


def _write_json(path: Path, payload: dict[str, object]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def _build_result_payload(
    *,
    run_id: str = "20260702_124856Z",
    dataset_id: str = "eternal-world-short-fact-v1",
    dataset_name: str = "Eternal World Short Fact Validation V1",
    status: str = "PASS",
    overall_winner: str = "multilingual_e5_small",
    total_questions: int = 12,
) -> dict[str, object]:
    return {
        "run_id": run_id,
        "status": status,
        "client_view": {
            "dataset": {
                "id": dataset_id,
                "name": dataset_name,
            },
            "overall_winner": overall_winner,
            "questions": [{} for _ in range(total_questions)],
        },
        "developer_view": {
            "dataset": {
                "id": dataset_id,
                "name": dataset_name,
            },
            "questions": [{} for _ in range(total_questions)],
            "aggregate_results": [
                {
                    "model_code": "multilingual_e5_small",
                    "passed_questions": total_questions,
                    "average_evidence_coverage": 1.0,
                    "total_missing_markers": 0,
                    "total_false_positive_markers": 0,
                    "official_metrics": {
                        "average_latency_ms": 12.3,
                        "evidence_marker_coverage": 1.0,
                        "missing_expected_marker_count": 0,
                        "false_positive_count": 0,
                    },
                },
                {
                    "model_code": "bge_m3",
                    "passed_questions": total_questions - 1,
                    "average_evidence_coverage": 0.9167,
                    "total_missing_markers": 1,
                    "total_false_positive_markers": 0,
                    "official_metrics": {
                        "average_latency_ms": 18.4,
                        "evidence_marker_coverage": 0.9167,
                        "missing_expected_marker_count": 1,
                        "false_positive_count": 0,
                    },
                },
            ],
        },
    }


def _build_summary_payload(
    *,
    run_id: str = "20260702_124856Z",
    dataset_id: str = "fixture-summary-dataset",
    dataset_name: str = "Fixture Summary Dataset",
    winner: str = "bge_m3",
) -> dict[str, object]:
    return {
        "run_id": run_id,
        "created_at": "2026-07-02T12:48:56Z",
        "run_mode": "fake_eval",
        "dataset_name": dataset_name,
        "dataset_id": dataset_id,
        "dataset_file": "app/modules/real_question_eval/datasets/eternal_world_short_fact_v1.json",
        "status": "PASS",
        "overall_winner": winner,
        "total_questions": 10,
        "models": ["bge_m3"],
        "model_results": [
            {
                "model": "bge_m3",
                "status": "PASS",
                "passed_questions": 9,
                "total_questions": 10,
                "evidence_coverage": 0.75,
                "missing_evidence": 2,
                "distractors": 1,
                "false_positives": 1,
                "latency_ms": 42.0,
                "average_latency_ms": 42.0,
                "is_winner": True,
            }
        ],
        "question_results": [
            {
                "question_id": "short-fact-1",
                "question": "Which seeds were under the porch bench?",
                "test_type": "short_fact",
                "model": "bge_m3",
                "status": "PASS",
                "evidence_coverage": 1.0,
                "missing_evidence": [],
                "forbidden_evidence_hits": [],
                "distractors": [],
                "latency_ms": None,
            }
        ],
    }


def test_print_summary_reads_latest_fake_summary_artifact(tmp_path, capsys) -> None:
    runs_dir = tmp_path / "artifacts" / "real_question_eval" / "runs"
    latest_fake_path = tmp_path / "artifacts" / "real_question_eval" / "latest_fake" / "real_question_eval_summary.json"
    _write_json(latest_fake_path, _build_summary_payload(dataset_name="Latest Fake Summary Dataset"))

    exit_code = main(["--latest-fake", "--runs-dir", str(runs_dir)])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "REAL QUESTION EVAL SUMMARY" in captured.out
    assert "DATASET: Latest Fake Summary Dataset" in captured.out
    assert "DATASET ID: fixture-summary-dataset" in captured.out
    assert "WINNER: bge_m3" in captured.out
    assert "bge_m3" in captured.out


def test_print_summary_reads_specific_run_dir(tmp_path, capsys) -> None:
    run_dir = tmp_path / "artifacts" / "real_question_eval" / "runs" / "20260702_124856Z_fake"
    artifact_path = _write_json(run_dir / "real_question_eval_summary.json", _build_summary_payload())

    exit_code = main(["--run-dir", str(run_dir)])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert f"ARTIFACT PATH: {artifact_path}" in captured.out
    assert "STATUS: PASS" in captured.out


def test_print_summary_reads_latest_archived_runs_in_desc_order(tmp_path, capsys) -> None:
    runs_dir = tmp_path / "artifacts" / "real_question_eval" / "runs"
    older_run_dir = runs_dir / "20260701_111111Z_fake"
    newer_run_dir = runs_dir / "20260702_222222Z_fake"
    _write_json(
        older_run_dir / "real_question_eval_summary.json",
        _build_summary_payload(run_id="20260701_111111Z", dataset_name="Older Dataset"),
    )
    _write_json(
        newer_run_dir / "real_question_eval_summary.json",
        _build_summary_payload(run_id="20260702_222222Z", dataset_name="Newer Dataset"),
    )

    exit_code = main(["--latest", "2", "--runs-dir", str(runs_dir)])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.index("DATASET: Newer Dataset") < captured.out.index("DATASET: Older Dataset")


def test_print_summary_prefers_summary_json_over_result_json(tmp_path, capsys) -> None:
    run_dir = tmp_path / "artifacts" / "real_question_eval" / "runs" / "20260702_124856Z_fake"
    _write_json(run_dir / "real_question_eval_result.json", _build_result_payload(dataset_name="Legacy Result Dataset"))
    _write_json(run_dir / "real_question_eval_summary.json", _build_summary_payload(dataset_name="Preferred Summary Dataset"))

    exit_code = main(["--run-dir", str(run_dir)])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "DATASET: Preferred Summary Dataset" in captured.out
    assert "Legacy Result Dataset" not in captured.out


def test_print_summary_falls_back_to_old_artifact_shape_when_summary_is_missing(tmp_path, capsys) -> None:
    run_dir = tmp_path / "artifacts" / "real_question_eval" / "runs" / "20260702_124856Z_fake"
    _write_json(run_dir / "real_question_eval_result.json", _build_result_payload())

    exit_code = main(["--run-dir", str(run_dir)])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "DATASET: Eternal World Short Fact Validation V1" in captured.out
    assert "multilingual_e5_small" in captured.out
    assert "bge_m3" in captured.out


def test_print_summary_warns_when_per_model_metrics_are_missing(tmp_path, capsys) -> None:
    run_dir = tmp_path / "artifacts" / "real_question_eval" / "runs" / "20260702_124856Z_fake"
    _write_json(
        run_dir / "real_question_eval_result.json",
        {
            "run_id": "20260702_124856Z",
            "status": "PASS",
            "client_view": {
                "dataset": {"id": "eternal-world-negative-v1", "name": "Eternal World Negative Validation V1"},
                "overall_winner": "bge_m3",
            },
        },
    )

    exit_code = main(["--run-dir", str(run_dir)])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert f"WARNING: {MISSING_MODEL_METRICS_WARNING}" in captured.out


def test_print_summary_renders_table_from_summary_json_fixture(tmp_path) -> None:
    run_dir = tmp_path / "artifacts" / "real_question_eval" / "runs" / "20260702_124856Z_fake"
    artifact_path = _write_json(run_dir / "real_question_eval_summary.json", _build_summary_payload())

    summary = summarize_artifact(artifact_path)
    text = render_summary(summary)

    assert summary.warning is None
    assert "MODEL RESULTS" in text
    assert "bge_m3" in text
    assert "0.7500" in text
    assert "42.0" in text


def test_print_summary_does_not_crash_when_optional_metrics_are_missing(tmp_path) -> None:
    run_dir = tmp_path / "artifacts" / "real_question_eval" / "runs" / "20260702_124856Z_fake"
    artifact_path = _write_json(
        run_dir / "real_question_eval_summary.json",
        {
            "run_id": "20260702_124856Z",
            "dataset_name": "Optional Metrics Dataset",
            "dataset_id": "optional-metrics-dataset",
            "status": "PASS",
            "overall_winner": "bge_m3",
            "total_questions": 1,
            "model_results": [
                {
                    "model": "bge_m3",
                    "passed_questions": 1,
                    "total_questions": 1,
                    "evidence_coverage": 1.0,
                    "missing_evidence": 0,
                    "distractors": 0,
                }
            ],
            "question_results": [],
        },
    )

    text = render_summary(summarize_artifact(artifact_path))

    assert "Optional Metrics Dataset" in text
    assert "n/a" in text


def test_print_summary_unknown_shape_does_not_crash(tmp_path, capsys) -> None:
    run_dir = tmp_path / "artifacts" / "real_question_eval" / "runs" / "20260702_124856Z_fake"
    _write_json(run_dir / "real_question_eval_result.json", {"hello": "world"})

    exit_code = main(["--run-dir", str(run_dir)])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "DATASET: unknown" in captured.out
    assert f"WARNING: {MISSING_MODEL_METRICS_WARNING}" in captured.out
