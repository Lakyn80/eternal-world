from __future__ import annotations

import json
from pathlib import Path

from app.modules.avatar_quality_evaluation.schemas import (
    AvatarEvalCaseRunResult,
    AvatarEvalRunManifest,
    AvatarEvalRunResult,
    AvatarEvalSummary,
)


class AvatarEvalArtifactError(RuntimeError):
    pass


def _write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _write_jsonl(path: Path, results: list[AvatarEvalCaseRunResult]) -> None:
    lines = [
        result.model_dump_json(exclude_none=True)
        for result in results
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _failure_markdown(results: list[AvatarEvalCaseRunResult]) -> str:
    failed = [result for result in results if not result.passed]
    if not failed:
        return "# Avatar Answer Quality Failures\n\nNo failed cases.\n"

    lines = ["# Avatar Answer Quality Failures", ""]
    for result in failed:
        lines.extend(
            [
                f"## {result.case_id} / run {result.run_index}",
                "",
                f"- Category: `{result.category}`",
                f"- Trace ID: `{result.trace_id}`",
                f"- Failure types: {', '.join(result.failure_types) or 'none'}",
                f"- Likely layer: `{result.likely_layer}`",
                f"- Recommended fix layer: `{result.recommended_fix_layer}`",
                "",
                "Answer:",
                "",
                "```text",
                result.answer,
                "```",
                "",
                "Evidence summary:",
                "",
            ]
        )
        if result.evidence_summary:
            for evidence in result.evidence_summary:
                lines.append(
                    "- "
                    + ", ".join(
                        f"{key}={value}"
                        for key, value in evidence.items()
                        if value not in (None, {}, [])
                    )
                )
        else:
            lines.append("- No evidence returned.")
        lines.append("")
        lines.append("Dimension results:")
        lines.append("")
        for dimension in result.dimensions:
            status = "pass" if dimension.passed else "fail"
            details = "; ".join(dimension.details)
            lines.append(f"- `{dimension.name}`: {status} - {details}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _baseline_report_markdown(
    *,
    manifest: AvatarEvalRunManifest,
    summary: AvatarEvalSummary,
    results: list[AvatarEvalCaseRunResult],
) -> str:
    evidence_ignored = sum(
        1 for result in results if "evidence_present_but_ignored" in result.failure_types
    )
    unsupported = sum(1 for result in results if "unsupported_detail" in result.failure_types)
    over_refusal = sum(1 for result in results if "over_refusal" in result.failure_types)
    persona_failures = sum(
        1
        for result in results
        if {"persona_cold_or_technical", "persona_inconsistent"} & set(result.failure_types)
    )
    perspective_failures = sum(
        1 for result in results if "perspective_collapsed" in result.failure_types
    )
    stability_failures = (
        0 if summary.answer_stability_rate == 1.0 else 1
    )

    lines = [
        "# Task 64.4 Baseline Report",
        "",
        f"- Run ID: `{manifest.run_id}`",
        f"- Run label: `{manifest.run_label}`",
        f"- Dataset: `{manifest.dataset_path}`",
        f"- Repeat count: `{manifest.repeat_count}`",
        f"- Total cases: {summary.evaluated_case_count}",
        f"- Total runs: {summary.total_runs}",
        "",
        "## Gate Metrics",
        "",
        f"- Retrieval hit rate: {summary.retrieval_evidence_hit_rate:.3f}",
        f"- Evidence-present-but-ignored count: {evidence_ignored}",
        f"- Unsupported-detail count: {unsupported}",
        f"- Over-refusal count: {over_refusal}",
        f"- Persona failures: {persona_failures}",
        f"- Perspective failures: {perspective_failures}",
        f"- Stability failures: {stability_failures}",
        "",
        "## Per-Case Table",
        "",
        "| Case | Run | Category | Result | Failures |",
        "| --- | ---: | --- | --- | --- |",
    ]
    for result in results:
        status = "pass" if result.passed else "fail"
        failures = ", ".join(result.failure_types) or "none"
        lines.append(
            f"| `{result.case_id}` | {result.run_index} | `{result.category}` | {status} | {failures} |"
        )
    lines.extend(
        [
            "",
            "## Metric Definitions",
            "",
        ]
    )
    for name, definition in summary.metric_definitions.model_dump().items():
        lines.append(f"- `{name}`: {definition}")
    return "\n".join(lines).rstrip() + "\n"


def write_avatar_eval_artifacts(
    *,
    manifest: AvatarEvalRunManifest,
    summary: AvatarEvalSummary,
    results: list[AvatarEvalCaseRunResult],
    output_dir: Path,
    allow_overwrite: bool = False,
) -> dict[str, str]:
    if output_dir.exists() and any(output_dir.iterdir()) and not allow_overwrite:
        raise AvatarEvalArtifactError(
            f"Avatar eval output directory already exists and is not empty: {output_dir}"
        )
    output_dir.mkdir(parents=True, exist_ok=True)

    paths = {
        "results": output_dir / "results.jsonl",
        "summary": output_dir / "summary.json",
        "metrics": output_dir / "metrics.json",
        "failures": output_dir / "failures.md",
        "manifest": output_dir / "run_manifest.json",
        "baseline_report": output_dir / "baseline_report.md",
    }
    _write_jsonl(paths["results"], results)
    _write_json(paths["summary"], summary.model_dump(mode="json"))
    _write_json(
        paths["metrics"],
        {
            key: value
            for key, value in summary.model_dump(mode="json").items()
            if key not in {"metric_definitions", "failure_counts"}
        }
        | {"failure_counts": summary.failure_counts},
    )
    paths["failures"].write_text(_failure_markdown(results), encoding="utf-8")
    _write_json(paths["manifest"], manifest.model_dump(mode="json"))
    paths["baseline_report"].write_text(
        _baseline_report_markdown(manifest=manifest, summary=summary, results=results),
        encoding="utf-8",
    )
    return {key: str(path) for key, path in paths.items()}


def attach_artifacts(
    *,
    run_result: AvatarEvalRunResult,
    allow_overwrite: bool,
) -> AvatarEvalRunResult:
    artifact_paths = write_avatar_eval_artifacts(
        manifest=run_result.manifest,
        summary=run_result.summary,
        results=run_result.results,
        output_dir=Path(run_result.manifest.output_dir),
        allow_overwrite=allow_overwrite,
    )
    return run_result.model_copy(update={"artifact_paths": artifact_paths})
