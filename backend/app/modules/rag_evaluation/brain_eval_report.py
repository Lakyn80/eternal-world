from __future__ import annotations

import json
from pathlib import Path

from app.modules.rag_evaluation.schemas import BrainRagEvalRunResult


def build_brain_rag_eval_markdown(result: BrainRagEvalRunResult) -> str:
    lines = [
        "# Brain RAG Evaluation Report",
        "",
        f"- Run ID: `{result.run_id}`",
        f"- Provider: `{result.provider_name}`",
        f"- Model: `{result.model or 'unknown'}`",
        f"- Case set: `{result.case_set}`",
        f"- Overall: `{'PASS' if result.passed else 'FAIL'}`",
        f"- Passed cases: `{result.suite_result.passed_cases}/{result.suite_result.total_cases}`",
        "",
        "## Case Results",
        "",
    ]

    for index, case_result in enumerate(result.suite_result.results, start=1):
        status = "PASS" if case_result.passed else "FAIL"
        lines.extend(
            [
                f"{index}. `{case_result.case_id}` — **{status}**",
                f"   - Title: {case_result.title}",
                f"   - Question: {case_result.user_query}",
            ]
        )
        if case_result.reference_queries:
            for locale in ("cs", "en", "ru", "es", "fr"):
                parallel_query = case_result.reference_queries.get(locale)
                if parallel_query and parallel_query != case_result.user_query:
                    lines.append(f"   - Question ({locale}): {parallel_query}")
        lines.extend(
            [
                f"   - Expected: `{case_result.expected_behavior}`",
                f"   - Actual: `{case_result.actual_behavior}`",
                f"   - Answer: {case_result.answer_text}",
            ]
        )
        if case_result.reasons:
            lines.append(f"   - Reasons: {'; '.join(case_result.reasons)}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _format_parallel_questions(case_result) -> list[str]:
    reference_queries = dict(case_result.reference_queries or {})
    if not reference_queries:
        return [f"**Q:** {case_result.user_query}"]

    locale_order = ("ru", "cs", "en", "es", "fr")
    lines: list[str] = []
    seen: set[str] = set()
    for locale in locale_order:
        query = reference_queries.get(locale)
        if not query or query in seen:
            continue
        seen.add(query)
        lines.append(f"**Q ({locale.upper()}):** {query}")

    for locale, query in sorted(reference_queries.items()):
        if query in seen:
            continue
        seen.add(query)
        lines.append(f"**Q ({locale.upper()}):** {query}")

    return lines or [f"**Q:** {case_result.user_query}"]


def build_brain_rag_eval_qa_markdown(result: BrainRagEvalRunResult) -> str:
    lines = [
        "# Brain RAG Evaluation Q&A",
        "",
        f"- Run ID: `{result.run_id}`",
        f"- Case set: `{result.case_set}`",
        f"- Passed: `{result.suite_result.passed_cases}/{result.suite_result.total_cases}`",
        "",
    ]

    for index, case_result in enumerate(result.suite_result.results, start=1):
        status = "PASS" if case_result.passed else "FAIL"
        lines.extend(
            [
                f"## {index}. `{case_result.case_id}` — {status}",
                "",
                *_format_parallel_questions(case_result),
                "",
                f"**A:** {case_result.answer_text}",
                "",
                "---",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def write_brain_rag_eval_artifacts(
    *,
    result: BrainRagEvalRunResult,
    artifact_dir: Path,
) -> dict[str, str]:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    run_dir = artifact_dir / "runs" / result.run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    result_json_path = run_dir / "brain_rag_eval_result.json"
    report_md_path = run_dir / "report.md"
    qa_report_md_path = run_dir / "qa_report.md"
    latest_result_json_path = artifact_dir / "brain_rag_eval_result.json"
    latest_report_md_path = artifact_dir / "report.md"
    latest_qa_report_md_path = artifact_dir / "qa_report.md"

    payload = result.model_dump(mode="json")
    result_json_text = json.dumps(payload, indent=2, ensure_ascii=False)
    report_md_text = build_brain_rag_eval_markdown(result)
    qa_report_md_text = build_brain_rag_eval_qa_markdown(result)

    result_json_path.write_text(result_json_text, encoding="utf-8")
    report_md_path.write_text(report_md_text, encoding="utf-8")
    qa_report_md_path.write_text(qa_report_md_text, encoding="utf-8")
    latest_result_json_path.write_text(result_json_text, encoding="utf-8")
    latest_report_md_path.write_text(report_md_text, encoding="utf-8")
    latest_qa_report_md_path.write_text(qa_report_md_text, encoding="utf-8")

    return {
        "run_result_json": str(result_json_path),
        "run_report_md": str(report_md_path),
        "run_qa_report_md": str(qa_report_md_path),
        "latest_result_json": str(latest_result_json_path),
        "latest_report_md": str(latest_report_md_path),
        "latest_qa_report_md": str(latest_qa_report_md_path),
    }
