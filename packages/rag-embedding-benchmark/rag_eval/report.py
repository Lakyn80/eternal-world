from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def write_ranking_artifacts(
    *,
    ranking_payload: dict[str, Any],
    json_path: Path,
    markdown_path: Path,
) -> None:
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(ranking_payload, indent=2), encoding="utf-8")
    markdown_path.write_text(render_ranking_markdown(ranking_payload), encoding="utf-8")


def render_ranking_markdown(ranking_payload: dict[str, Any]) -> str:
    lines = [
        "# RAG Embedding Benchmark Report",
        "",
        f"- Run ID: `{ranking_payload.get('run_id', 'unknown')}`",
        f"- Dataset: `{ranking_payload.get('dataset_id', 'unknown')}`",
        f"- Preflight issues: `{ranking_payload.get('preflight_issue_count', 0)}`",
        "",
    ]

    winner = ranking_payload.get("winner")
    if winner:
        lines.extend(
            [
                "## Winner",
                "",
                f"- Model: `{winner.get('model_code')}`",
                f"- Config: `{winner.get('config_id')}`",
                f"- Collection: `{winner.get('collection_name')}`",
                "",
            ]
        )
        metrics = winner.get("metrics") or {}
        if metrics:
            lines.extend(
                [
                    "### Metrics",
                    "",
                    f"- hit_rate: `{metrics.get('hit_rate')}`",
                    f"- evidence_marker_coverage: `{metrics.get('evidence_marker_coverage')}`",
                    f"- recall_at_k: `{metrics.get('recall_at_k')}`",
                    f"- mrr: `{metrics.get('mrr')}`",
                    f"- forbidden_marker_rate: `{metrics.get('forbidden_marker_rate')}`",
                    "",
                ]
            )

    ranking = ranking_payload.get("ranking") or []
    if ranking:
        lines.extend(["## Ranking", ""])
        for index, item in enumerate(ranking, start=1):
            metrics = item.get("metrics") or {}
            lines.append(
                f"{index}. `{item.get('model_code')}` "
                f"(hit_rate={metrics.get('hit_rate')}, "
                f"coverage={metrics.get('evidence_marker_coverage')}, "
                f"forbidden_rate={metrics.get('forbidden_marker_rate')})"
            )
        lines.append("")

    failed_models = ranking_payload.get("failed_models") or []
    if failed_models:
        lines.extend(["## Failed Models", ""])
        for item in failed_models:
            lines.append(f"- `{item.get('model_code')}` [{item.get('status')}]: {item.get('error')}")
        lines.append("")

    return "\n".join(lines)
