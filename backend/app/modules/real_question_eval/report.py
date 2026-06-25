from __future__ import annotations

import json
import shutil
from pathlib import Path

from app.modules.real_question_eval.schemas import RealQuestionEvalArtifactPaths, RealQuestionEvalResult


TASK_NAME = "Task 32 Real Local Model Question Evaluation"


def build_real_question_eval_markdown(result: RealQuestionEvalResult) -> str:
    client_view = build_real_question_eval_client_view(result)
    developer_view = build_real_question_eval_developer_view(result)
    lines: list[str] = [
        "# Real Question Evaluation Report",
        "",
        "## Client Summary",
        f"- Source dataset: {client_view['source_dataset_note']}",
        f"- Real client/user data: {client_view['real_client_user_data']}",
        f"- Purpose: {client_view['purpose']}",
        "- Models compared:",
    ]
    for model_code in client_view["models_compared"]:
        lines.append(f"  - `{model_code}`")
    lines.extend(
        [
            f"- Recommended active model: `{client_view['recommended_active_model'] or 'none'}`",
            f"- Speed vs accuracy tradeoff: {client_view['speed_vs_accuracy_tradeoff']}",
            f"- Production recommendation: {client_view['production_recommendation']}",
            f"- Timestamp: {result.generated_at or 'unknown'}",
            f"- Run type: `{result.run_type or 'unknown'}`",
            "",
            "## Artifact Files",
            f"- Latest Markdown: `{result.artifact_paths.latest_markdown_report or 'n/a'}`",
            f"- Latest JSON: `{result.artifact_paths.latest_json_result or 'n/a'}`",
            f"- Archived Markdown: `{result.artifact_paths.archived_markdown_report or 'n/a'}`",
            f"- Archived JSON: `{result.artifact_paths.archived_json_result or 'n/a'}`",
            "",
            "## Client Question Breakdown",
        ]
    )

    for index, question_result in enumerate(client_view["questions"], start=1):
        lines.extend(
            [
                f"### Question {index} - {question_result['question_id']}",
                f"Question: {question_result['question']}",
                f"- Final evaluated answer: {question_result['final_evaluated_answer']}",
                f"- Correctness verdict: {question_result['correctness_verdict']}",
                f"- Evidence used: {question_result['evidence_used']}",
                f"- Model comparison: {question_result['model_comparison']}",
                f"- Winner: `{question_result['winner'] or 'none'}`",
                f"- Why it won: {question_result['reason']}",
                f"- What the losing model missed or got wrong: {question_result['losing_model_issue']}",
                f"- Distractors / false positives: {question_result['distractors_or_false_positives']}",
                "",
                "Expected evidence:",
            ]
        )
        for marker in question_result["expected_markers"]:
            lines.append(f"- {marker}")
        if question_result["expected_distractors"]:
            lines.append("")
            lines.append("Expected distractors:")
            for marker in question_result["expected_distractors"]:
                lines.append(f"- {marker}")
        lines.extend(["", "- Model verdicts:"])
        for model_result in question_result["model_summaries"]:
            lines.append(
                "  - "
                f"`{model_result['model_code']}`: verdict={model_result['verdict']} "
                f"coverage={model_result['evidence_coverage']} "
                f"matched={', '.join(model_result['matched_markers']) or 'none'} "
                f"missing={', '.join(model_result['missing_markers']) or 'none'} "
                f"distractors={', '.join(model_result['distractors']) or 'none'}"
            )
        lines.append("")

    lines.extend(
        [
            "## Aggregate Client Decision",
            f"- Recommended active model: `{client_view['recommended_active_model'] or 'none'}`",
            f"- Overall winner: `{client_view['overall_winner'] or 'none'}`",
            f"- Activation state: `{str(client_view['activated']).lower()}`",
            f"- Runtime retrieval verified: `{str(client_view['runtime_verified']).lower()}`",
            f"- Production recommendation: {client_view['production_recommendation']}",
            "",
            "## Developer Details",
            "",
        ]
    )

    for index, question_result in enumerate(developer_view["questions"], start=1):
        lines.extend(
            [
                f"### Question {index} - {question_result['question_id']}",
                f"Question: {question_result['question']}",
                "",
                "Expected evidence:",
            ]
        )
        for marker in question_result["expected_markers"]:
            lines.append(f"- {marker}")
        if question_result["expected_distractors"]:
            lines.append("")
            lines.append("Expected distractors:")
            for marker in question_result["expected_distractors"]:
                lines.append(f"- {marker}")
        lines.append("")

        for model_result in question_result["model_results"]:
            lines.extend(
                [
                    f"#### {model_result['model_code']}",
                    f"- Collection: `{model_result['collection_name']}`",
                    "- Top chunks:",
                ]
            )
            for chunk in model_result["top_chunks"]:
                lines.append(
                    f"  {chunk['rank']}. score={chunk['score']:.6f} chunk_id={chunk['chunk_id']} preview={chunk['preview']}"
                )
            if not model_result["top_chunks"]:
                lines.append("  1. No retrieved chunks.")
            lines.extend(
                [
                    f"- Matched markers: {', '.join(model_result['matched_markers']) or 'none'}",
                    f"- Missing markers: {', '.join(model_result['missing_markers']) or 'none'}",
                    f"- Distractors: {', '.join(model_result['distractors']) or 'none'}",
                    f"- Evidence coverage: {model_result['evidence_coverage'] if model_result['evidence_coverage'] is not None else 'n/a'}",
                    f"- First relevant rank: {model_result['first_relevant_rank'] if model_result['first_relevant_rank'] is not None else 'n/a'}",
                    f"- Answer summary: {model_result['answer_summary']}",
                    f"- Verdict: {model_result['verdict']}",
                    "",
                ]
            )

        lines.extend(
            [
                "- Winner:",
                f"  - `{question_result['winner'] or 'none'}`",
                f"  - {question_result['reason']}",
                "",
            ]
        )

    lines.extend(["### Aggregate Results", ""])
    for aggregate_result in developer_view["aggregate_results"]:
        lines.extend(
            [
                f"#### {aggregate_result['model_code']}",
                f"- Collection: `{aggregate_result['collection_name']}`",
                f"- Question wins: {aggregate_result['question_wins']}",
                f"- Passed questions: {aggregate_result['passed_questions']}",
                f"- Average evidence coverage: {aggregate_result['average_evidence_coverage']}",
                f"- Average first relevant rank: {aggregate_result['average_first_relevant_rank'] if aggregate_result['average_first_relevant_rank'] is not None else 'n/a'}",
                f"- Total matched markers: {aggregate_result['total_matched_markers']}",
                f"- Total missing markers: {aggregate_result['total_missing_markers']}",
                f"- Total false-positive markers: {aggregate_result['total_false_positive_markers']}",
                f"- Official metrics: {aggregate_result['official_metrics'] or {}}",
                "",
            ]
        )

    lines.extend(
            [
                "### Runtime Activation",
                f"- Selected config: {developer_view['selected_config'] or {}}",
                f"- Activated config: {developer_view['activated_config'] or {}}",
                f"- Runtime retrieval verification: {developer_view['runtime_retrieval_verification'] or {}}",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def build_real_question_eval_json_payload(result: RealQuestionEvalResult) -> dict[str, object]:
    client_view = build_real_question_eval_client_view(result)
    developer_view = build_real_question_eval_developer_view(result)
    return {
        "task": TASK_NAME,
        "run_id": result.run_id,
        "run_type": result.run_type,
        "timestamp": result.generated_at,
        "used_fake_models": result.used_fake_models,
        "status": "PASS" if result.passed else "FAIL",
        "artifact_paths": result.artifact_paths.model_dump(mode="json"),
        "client_view": client_view,
        "developer_view": developer_view,
    }


def build_real_question_eval_client_view(result: RealQuestionEvalResult) -> dict[str, object]:
    questions: list[dict[str, object]] = []
    for question_result in result.question_results:
        model_summaries = [
            {
                "model_code": model_result.model_code,
                "verdict": model_result.groundedness_verdict,
                "evidence_coverage": model_result.evidence_coverage,
                "matched_markers": list(model_result.matched_expected_markers),
                "missing_markers": list(model_result.missing_expected_markers),
                "distractors": list(model_result.false_positive_markers),
                "answer_summary": model_result.answer_summary,
            }
            for model_result in question_result.model_results
        ]
        winner_result = next(
            (item for item in question_result.model_results if item.model_code == question_result.winner_model_code),
            None,
        )
        losing_results = [
            item for item in question_result.model_results if item.model_code != question_result.winner_model_code
        ]
        losing_result = losing_results[0] if losing_results else None
        evidence_used = ", ".join(winner_result.matched_expected_markers) if winner_result and winner_result.matched_expected_markers else "none"
        losing_issues: list[str] = []
        if losing_result is not None:
            if losing_result.missing_expected_markers:
                losing_issues.append("missing " + ", ".join(losing_result.missing_expected_markers))
            if losing_result.false_positive_markers:
                losing_issues.append("distractors " + ", ".join(losing_result.false_positive_markers))
            if not losing_issues:
                losing_issues.append("lower retrieval score despite comparable evidence")
        questions.append(
            {
                "question_id": question_result.question_id,
                "question": question_result.question_text,
                "expected_markers": list(question_result.expected_markers),
                "expected_distractors": list(question_result.forbidden_markers),
                "winner": question_result.winner_model_code,
                "reason": question_result.winner_reason,
                "final_evaluated_answer": winner_result.answer_summary if winner_result is not None else "No winning answer summary available.",
                "correctness_verdict": winner_result.groundedness_verdict if winner_result is not None else "unknown",
                "evidence_used": evidence_used,
                "model_comparison": "; ".join(
                    f"{item['model_code']} -> verdict={item['verdict']} coverage={item['evidence_coverage']}"
                    for item in model_summaries
                ),
                "losing_model_issue": "; ".join(losing_issues),
                "distractors_or_false_positives": (
                    ", ".join(losing_result.false_positive_markers)
                    if losing_result is not None and losing_result.false_positive_markers
                    else "none"
                ),
                "model_summaries": model_summaries,
            }
        )

    recommended_active_model = result.overall_winner_model_code
    if result.used_fake_models:
        speed_vs_accuracy_tradeoff = (
            "Fake-mode evaluation is optimized for deterministic regression checks, not runtime speed measurements."
        )
        production_recommendation = (
            "Keep the fake-mode result for test coverage only; use the preserved latest real evaluation for production-facing model decisions."
        )
    else:
        speed_vs_accuracy_tradeoff = (
            "The winning model delivered stronger evidence quality, while the losing model can be faster or lighter but less reliable on grounded retrieval."
        )
        production_recommendation = (
            f"Use `{recommended_active_model}` as the active production retrieval model for this evaluation corpus."
            if recommended_active_model
            else "No production recommendation available."
        )

    return {
        "source_dataset_note": "deterministic fictional eval corpus",
        "real_client_user_data": "no",
        "purpose": "retrieval quality testing",
        "dataset": {
            "id": result.dataset_id,
            "name": result.dataset_name,
        },
        "models_compared": list(result.compared_models),
        "overall_winner": result.overall_winner_model_code,
        "recommended_active_model": recommended_active_model,
        "speed_vs_accuracy_tradeoff": speed_vs_accuracy_tradeoff,
        "production_recommendation": production_recommendation,
        "activated": result.activated,
        "runtime_verified": result.runtime_verified,
        "questions": questions,
    }


def build_real_question_eval_developer_view(result: RealQuestionEvalResult) -> dict[str, object]:
    return {
        "dataset": {
            "id": result.dataset_id,
            "name": result.dataset_name,
        },
        "models_compared": list(result.compared_models),
        "questions": [
            {
                "question_id": question_result.question_id,
                "question": question_result.question_text,
                "expected_markers": list(question_result.expected_markers),
                "expected_distractors": list(question_result.forbidden_markers),
                "winner": question_result.winner_model_code,
                "reason": question_result.winner_reason,
                "model_results": [
                    {
                        "model_code": model_result.model_code,
                        "collection_name": model_result.collection_name,
                        "top_chunks": [
                            {
                                "rank": chunk.rank,
                                "chunk_id": chunk.chunk_id,
                                "score": chunk.score,
                                "preview": chunk.preview,
                            }
                            for chunk in model_result.top_chunks
                        ],
                        "matched_markers": list(model_result.matched_expected_markers),
                        "missing_markers": list(model_result.missing_expected_markers),
                        "distractors": list(model_result.false_positive_markers),
                        "evidence_coverage": model_result.evidence_coverage,
                        "first_relevant_rank": model_result.first_relevant_rank,
                        "answer_summary": model_result.answer_summary,
                        "verdict": model_result.groundedness_verdict,
                    }
                    for model_result in question_result.model_results
                ],
            }
            for question_result in result.question_results
        ],
        "aggregate_results": [
            {
                "model_code": aggregate_result.model_code,
                "collection_name": aggregate_result.collection_name,
                "question_wins": aggregate_result.question_wins,
                "passed_questions": aggregate_result.passed_questions,
                "average_evidence_coverage": aggregate_result.average_evidence_coverage,
                "average_first_relevant_rank": aggregate_result.average_first_relevant_rank,
                "total_matched_markers": aggregate_result.total_matched_markers,
                "total_missing_markers": aggregate_result.total_missing_markers,
                "total_false_positive_markers": aggregate_result.total_false_positive_markers,
                "official_metrics": aggregate_result.official_metrics or {},
            }
            for aggregate_result in result.aggregate_results
        ],
        "selected_config": result.official_best_config or {},
        "activated_config": result.activated_config or {},
        "runtime_retrieval_verification": result.runtime_retrieval or {},
    }


def build_real_question_eval_run_id(*, generated_at: str | None) -> str:
    from datetime import datetime, timezone

    if generated_at:
        try:
            parsed = datetime.fromisoformat(generated_at.replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            parsed = parsed.astimezone(timezone.utc)
            return parsed.strftime("%Y%m%d_%H%M%SZ")
        except ValueError:
            pass

    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%SZ")


def _resolve_run_type(*, result: RealQuestionEvalResult) -> str:
    return "fake" if result.used_fake_models else "real"


def build_real_question_eval_artifact_paths(*, artifact_dir: Path, run_id: str) -> RealQuestionEvalArtifactPaths:
    raise NotImplementedError("Use build_real_question_eval_artifact_paths_for_result")


def build_real_question_eval_artifact_paths_for_result(
    *,
    artifact_dir: Path,
    run_id: str,
    result: RealQuestionEvalResult,
) -> RealQuestionEvalArtifactPaths:
    run_type = _resolve_run_type(result=result)
    latest_dir = artifact_dir / f"latest_{run_type}"
    archived_dir = artifact_dir / "runs" / f"{run_id}_{run_type}"
    return RealQuestionEvalArtifactPaths(
        latest_markdown_report=str(latest_dir / "real_question_eval_report.md"),
        latest_json_result=str(latest_dir / "real_question_eval_result.json"),
        archived_markdown_report=str(archived_dir / "real_question_eval_report.md"),
        archived_json_result=str(archived_dir / "real_question_eval_result.json"),
    )


def write_real_question_eval_artifacts(*, artifact_dir: Path, result: RealQuestionEvalResult) -> RealQuestionEvalArtifactPaths:
    run_id = result.run_id or build_real_question_eval_run_id(generated_at=result.generated_at)
    result.run_type = _resolve_run_type(result=result)
    artifact_paths = build_real_question_eval_artifact_paths_for_result(
        artifact_dir=artifact_dir,
        run_id=run_id,
        result=result,
    )
    result.run_id = run_id
    result.artifact_paths = artifact_paths
    result.markdown_report_path = artifact_paths.latest_markdown_report
    result.json_result_path = artifact_paths.latest_json_result

    latest_markdown_path = Path(artifact_paths.latest_markdown_report)
    latest_json_path = Path(artifact_paths.latest_json_result)
    archived_markdown_path = Path(artifact_paths.archived_markdown_report)
    archived_json_path = Path(artifact_paths.archived_json_result)

    latest_markdown_path.parent.mkdir(parents=True, exist_ok=True)
    archived_markdown_path.parent.mkdir(parents=True, exist_ok=True)

    markdown_content = build_real_question_eval_markdown(result)
    json_payload = build_real_question_eval_json_payload(result)
    json_content = json.dumps(json_payload, indent=2, ensure_ascii=False) + "\n"

    latest_markdown_path.write_text(markdown_content, encoding="utf-8")
    latest_json_path.write_text(json_content, encoding="utf-8")
    archived_markdown_path.write_text(markdown_content, encoding="utf-8")
    archived_json_path.write_text(json_content, encoding="utf-8")
    _ensure_other_latest_variant_preserved(artifact_dir=artifact_dir, current_run_type=result.run_type)

    return artifact_paths


def _ensure_other_latest_variant_preserved(*, artifact_dir: Path, current_run_type: str) -> None:
    other_run_type = "real" if current_run_type == "fake" else "fake"
    latest_dir = artifact_dir / f"latest_{other_run_type}"
    latest_markdown_path = latest_dir / "real_question_eval_report.md"
    latest_json_path = latest_dir / "real_question_eval_result.json"
    if latest_markdown_path.exists() and latest_json_path.exists():
        return

    source_pair = _find_latest_existing_run_pair(artifact_dir=artifact_dir, run_type=other_run_type)
    if source_pair is None:
        return

    source_markdown_path, source_json_path = source_pair
    latest_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source_markdown_path, latest_markdown_path)
    shutil.copyfile(source_json_path, latest_json_path)


def _find_latest_existing_run_pair(*, artifact_dir: Path, run_type: str) -> tuple[Path, Path] | None:
    runs_dir = artifact_dir / "runs"
    candidates: list[tuple[str, Path, Path]] = []
    if runs_dir.exists():
        for run_dir in runs_dir.iterdir():
            if not run_dir.is_dir():
                continue
            json_path = run_dir / "real_question_eval_result.json"
            markdown_path = run_dir / "real_question_eval_report.md"
            if not json_path.exists() or not markdown_path.exists():
                continue
            payload = _read_json_payload(json_path)
            payload_run_type = _extract_run_type_from_payload(payload)
            if payload_run_type != run_type:
                continue
            candidate_run_id = _extract_run_id_from_dir_name(run_dir.name, payload)
            candidates.append((candidate_run_id, markdown_path, json_path))

    if not candidates:
        return None

    candidates.sort(key=lambda item: item[0], reverse=True)
    _, markdown_path, json_path = candidates[0]
    return markdown_path, json_path


def _read_json_payload(json_path: Path) -> dict[str, object]:
    try:
        raw_payload = json.loads(json_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return raw_payload if isinstance(raw_payload, dict) else {}


def _extract_run_type_from_payload(payload: dict[str, object]) -> str | None:
    run_type = payload.get("run_type")
    if isinstance(run_type, str):
        return run_type
    used_fake_models = payload.get("used_fake_models")
    if isinstance(used_fake_models, bool):
        return "fake" if used_fake_models else "real"
    return None


def _extract_run_id_from_dir_name(dir_name: str, payload: dict[str, object]) -> str:
    for suffix in ("_real", "_fake"):
        if dir_name.endswith(suffix):
            return dir_name[: -len(suffix)]
    payload_run_id = payload.get("run_id")
    if isinstance(payload_run_id, str) and payload_run_id:
        return payload_run_id
    return dir_name
