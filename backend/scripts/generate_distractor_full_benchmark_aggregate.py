from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from app.core.config import BACKEND_DIR
from app.modules.embedding_models.registry import EMBEDDING_MODEL_DEFINITIONS, LOCAL_PROVIDER_TYPE
from app.modules.real_question_eval.service import (
    REAL_QUESTION_EVAL_FULL_VERSION_BATCH_A_NEW_PROVIDER_CODES,
    REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_NEW_PROVIDER_CODES,
    REAL_QUESTION_EVAL_FULL_VERSION_BATCH_C_NEW_PROVIDER_CODES,
    REAL_QUESTION_EVAL_FULL_VERSION_BATCH_D_NEW_PROVIDER_CODES,
    REAL_QUESTION_EVAL_FULL_VERSION_BATCH_E_NEW_PROVIDER_CODES,
    REAL_QUESTION_EVAL_FULL_VERSION_BATCH_F_NEW_PROVIDER_CODES,
    REAL_QUESTION_EVAL_INCREMENTAL_NEW_PROVIDER_CODES,
    REAL_QUESTION_EVAL_HISTORICAL_PROVIDERS,
)

ARTIFACT_ROOT = BACKEND_DIR / "artifacts" / "real_question_eval" / "eternal_world_distractor_full_benchmark"
AGGREGATE_JSON = ARTIFACT_ROOT / "real_question_eval_distractor_full_benchmark_aggregate.json"
AGGREGATE_MD = ARTIFACT_ROOT / "real_question_eval_distractor_full_benchmark_aggregate.md"

STAGE_MODELS: dict[str, tuple[str, ...]] = {
    "latest_incremental_new_providers": (
        *REAL_QUESTION_EVAL_HISTORICAL_PROVIDERS,
        *REAL_QUESTION_EVAL_INCREMENTAL_NEW_PROVIDER_CODES,
    ),
    "latest_full_version_batch_a": REAL_QUESTION_EVAL_FULL_VERSION_BATCH_A_NEW_PROVIDER_CODES,
    "latest_full_version_batch_b": REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_NEW_PROVIDER_CODES,
    "latest_full_version_batch_b_attempted": REAL_QUESTION_EVAL_FULL_VERSION_BATCH_B_NEW_PROVIDER_CODES,
    "latest_full_version_batch_c": REAL_QUESTION_EVAL_FULL_VERSION_BATCH_C_NEW_PROVIDER_CODES,
    "latest_full_version_batch_d": REAL_QUESTION_EVAL_FULL_VERSION_BATCH_D_NEW_PROVIDER_CODES,
    "latest_full_version_batch_e": REAL_QUESTION_EVAL_FULL_VERSION_BATCH_E_NEW_PROVIDER_CODES,
    "latest_full_version_batch_f": REAL_QUESTION_EVAL_FULL_VERSION_BATCH_F_NEW_PROVIDER_CODES,
}

EXCLUDED_FROM_BATCHES = ("mock_embedding",)

FAILED_RUN_LOG_PATTERNS: dict[str, str] = {
    "qwen3_embedding_4b": "batch_e_qwen3_embedding_4b.log",
    "qwen3_embedding_8b": "batch_f_qwen3_embedding_8b.log",
}


def _load_summary(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _extract_model_rows(summary: dict, *, models: tuple[str, ...], source_artifact: str) -> list[dict]:
    rows: list[dict] = []
    for item in summary.get("model_results") or []:
        model = str(item.get("model") or "")
        if model not in models:
            continue
        rows.append(
            {
                "model": model,
                "status": "AVAILABLE",
                "source_artifact": source_artifact,
                "passed_questions": int(item.get("passed_questions") or 0),
                "total_questions": int(item.get("total_questions") or 0),
                "pass_rate": float(item.get("pass_rate") or 0.0),
                "evidence_coverage": float(item.get("evidence_coverage") or 0.0),
                "missing_evidence": int(item.get("missing_evidence") or 0),
                "distractors": int(item.get("distractors") or 0),
                "latency_ms": float(item.get("latency_ms") or item.get("average_latency_ms") or 0.0),
            }
        )
    return rows


def _inventory_artifacts() -> list[dict]:
    inventory: list[dict] = []
    for path in sorted(ARTIFACT_ROOT.rglob("*")):
        if path.is_dir():
            inventory.append({"path": str(path.relative_to(BACKEND_DIR)).replace("\\", "/"), "kind": "directory", "size_bytes": None})
            continue
        inventory.append(
            {
                "path": str(path.relative_to(BACKEND_DIR)).replace("\\", "/"),
                "kind": "file",
                "size_bytes": path.stat().st_size,
            }
        )
    return inventory


def _registry_real_local_models() -> list[str]:
    return [
        model.code
        for model in EMBEDDING_MODEL_DEFINITIONS
        if model.provider_type == LOCAL_PROVIDER_TYPE and model.code != "mock_embedding"
    ]


def _classify_failed_log_excerpt(log_text: str) -> tuple[str, str]:
    lowered = log_text.lower()
    if "outofmemory" in lowered or "oom" in lowered or "cuda out of memory" in lowered:
        return "OOM", "Log contains out-of-memory evidence."
    if "modulenotfounderror" in lowered or "importerror" in lowered:
        return "dependency error", "Log contains import/module dependency failure."
    if "validationerror" in lowered or "valueerror" in lowered:
        return "unsupported config", "Log contains configuration/validation failure."
    if "traceback" in lowered:
        return "FAILED", "Log contains a Python traceback."
    return "FAILED", "Run log exists but no artifact summary was written."


def _failed_run_from_log(*, model_code: str, log_path: Path) -> dict | None:
    if not log_path.exists():
        return None
    log_text = log_path.read_text(encoding="utf-8", errors="replace")
    if "exit_code: 0" in log_text[-2000:] or "REAL QUESTION EVAL RESULT: PASS" in log_text:
        return None
    status, reason_hint = _classify_failed_log_excerpt(log_text)
    traceback_excerpt = ""
    if "Traceback" in log_text:
        traceback_excerpt = log_text.split("Traceback")[-1].strip()[:500]
    return {
        "stage": f"full_version_batch_{'e' if model_code == 'qwen3_embedding_4b' else 'f'}",
        "models": [model_code],
        "status": status,
        "reason": (
            f"{reason_hint} See log `{log_path.relative_to(BACKEND_DIR).as_posix()}`."
            + (f" Traceback excerpt: {traceback_excerpt}" if traceback_excerpt else "")
        ),
    }


def build_aggregate() -> dict:
    ranking_by_model: dict[str, dict] = {}
    completed_stages: list[dict] = []
    missing_or_skipped: list[dict] = []
    run_logs: list[dict] = []

    logs_dir = ARTIFACT_ROOT / "run_logs"
    if logs_dir.exists():
        for log_path in sorted(logs_dir.glob("*.log")):
            run_logs.append({"path": str(log_path.relative_to(BACKEND_DIR)).replace("\\", "/"), "size_bytes": log_path.stat().st_size})

    for stage_dir_name, stage_models in STAGE_MODELS.items():
        stage_dir = ARTIFACT_ROOT / stage_dir_name
        summary_path = stage_dir / "real_question_eval_summary.json"
        summary = _load_summary(summary_path)
        if summary is None:
            if stage_dir_name == "latest_full_version_batch_b_attempted":
                continue
            if stage_dir_name.startswith("latest_full_version_batch_"):
                batch_key = stage_dir_name.removeprefix("latest_")
                missing_or_skipped.append(
                    {
                        "stage": batch_key,
                        "models": list(stage_models),
                        "status": "MISSING",
                        "reason": f"No {summary_path} artifact exists under the benchmark artifact dir.",
                    }
                )
            continue

        completed_stages.append(
            {
                "stage": stage_dir_name.removeprefix("latest_"),
                "status": "COMPLETED",
                "artifact_dir": str(stage_dir.relative_to(BACKEND_DIR)).replace("\\", "/"),
                "run_id": summary.get("run_id"),
                "quality_status": summary.get("quality_status"),
                "winner": summary.get("overall_winner"),
            }
        )
        source_artifact = str(summary_path.relative_to(BACKEND_DIR)).replace("\\", "/")
        for row in _extract_model_rows(summary, models=stage_models, source_artifact=source_artifact):
            ranking_by_model[row["model"]] = row

    incremental_summary_path = ARTIFACT_ROOT / "latest_incremental_new_providers" / "real_question_eval_summary.json"
    base_summary_path = ARTIFACT_ROOT / "latest_real" / "real_question_eval_summary.json"
    incremental_summary = _load_summary(incremental_summary_path)
    base_summary = _load_summary(base_summary_path)
    if base_summary is not None:
        completed_stages.insert(
            0,
            {
                "stage": "base_real_eval",
                "status": "COMPLETED",
                "artifact_dir": str((ARTIFACT_ROOT / "latest_real").relative_to(BACKEND_DIR)).replace("\\", "/"),
                "run_id": base_summary.get("run_id"),
                "quality_status": base_summary.get("quality_status"),
                "winner": base_summary.get("overall_winner"),
            },
        )

    for model_code in EXCLUDED_FROM_BATCHES:
        if model_code in ranking_by_model:
            continue
        missing_or_skipped.append(
            {
                "stage": "excluded_config",
                "models": [model_code],
                "status": "SKIPPED",
                "reason": "Mock embedding is a test/dev provider and is not a real local model benchmark candidate.",
            }
        )

    for model_code, log_name in FAILED_RUN_LOG_PATTERNS.items():
        if model_code in ranking_by_model:
            continue
        failed_entry = _failed_run_from_log(
            model_code=model_code,
            log_path=ARTIFACT_ROOT / "run_logs" / log_name,
        )
        if failed_entry is not None:
            missing_or_skipped = [
                item
                for item in missing_or_skipped
                if model_code not in item.get("models", [])
            ]
            missing_or_skipped.append(failed_entry)
            continue
        if any(model_code in item.get("models", []) for item in missing_or_skipped):
            continue
        batch_suffix = "e" if model_code == "qwen3_embedding_4b" else "f"
        missing_or_skipped.append(
            {
                "stage": f"full_version_batch_{batch_suffix}",
                "models": [model_code],
                "status": "MISSING",
                "reason": (
                    f"No `{ARTIFACT_ROOT / f'latest_full_version_batch_{batch_suffix}' / 'real_question_eval_summary.json'}` "
                    "artifact exists under the benchmark artifact dir."
                ),
            }
        )

    ranking = sorted(
        ranking_by_model.values(),
        key=lambda item: (-item["pass_rate"], -item["passed_questions"], -item["evidence_coverage"]),
    )
    for index, item in enumerate(ranking, start=1):
        item["rank"] = index

    registry_models = _registry_real_local_models()
    accounted = set(ranking_by_model) | {item for group in missing_or_skipped for item in group.get("models", [])}
    unaccounted = [model for model in registry_models if model not in accounted]

    best_model = ranking[0] if ranking else None
    worst_model = ranking[-1] if ranking else None
    full_complete = (
        not any(item["status"] == "MISSING" for item in missing_or_skipped)
        and not unaccounted
    )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "artifact_root": str(ARTIFACT_ROOT.relative_to(BACKEND_DIR)).replace("\\", "/"),
        "dataset_name": (incremental_summary or base_summary or {}).get("dataset_name", "Eternal World Distractor Validation V1"),
        "dataset_id": (incremental_summary or base_summary or {}).get("dataset_id", "eternal-world-distractor-v1"),
        "available_source_summary": str(incremental_summary_path.relative_to(BACKEND_DIR)).replace("\\", "/")
        if incremental_summary_path.exists()
        else None,
        "base_source_summary": str(base_summary_path.relative_to(BACKEND_DIR)).replace("\\", "/")
        if base_summary_path.exists()
        else None,
        "completed_stages": completed_stages,
        "ranking": ranking,
        "best_model": best_model,
        "worst_model": worst_model,
        "missing_or_skipped_configs": missing_or_skipped,
        "unaccounted_registry_models": unaccounted,
        "run_logs": run_logs,
        "acceptance": {
            "available_results_gate": "PASS"
            if best_model is not None and best_model["pass_rate"] >= 0.8
            else "FAIL",
            "available_results_verdict": (
                f"Best available model {best_model['model']} passed "
                f"{best_model['passed_questions']}/{best_model['total_questions']} "
                f"({best_model['pass_rate']:.4f})."
                if best_model
                else "No completed model results are available."
            ),
            "full_benchmark_completion": "COMPLETE" if full_complete and not unaccounted else "INCOMPLETE",
            "full_benchmark_verdict": (
                "All repository-supported real local providers are accounted for."
                if full_complete and not unaccounted
                else "One or more benchmark stages are still missing or unaccounted."
            ),
        },
        "artifact_inventory": _inventory_artifacts(),
        "not_rerun_statement": "Existing completed base/incremental artifacts were preserved; only missing batch stages were executed in this pass.",
    }


def _render_markdown(payload: dict) -> str:
    lines = [
        "# Eternal World Distractor Real Eval Aggregate Report",
        "",
        f"Generated at: `{payload['generated_at']}`",
        f"Artifact root: `{payload['artifact_root']}`",
        f"Dataset: `{payload['dataset_name']}` (`{payload['dataset_id']}`)",
        "",
        "## Completed Stages",
    ]
    for stage in payload["completed_stages"]:
        lines.append(
            f"- `{stage['stage']}`: {stage['status']} | run `{stage.get('run_id')}` | "
            f"quality `{stage.get('quality_status')}` | winner `{stage.get('winner')}` | "
            f"artifact `{stage['artifact_dir']}`"
        )
    lines.extend(["", "## Final Ranking From Available Results", "| rank | model | passed | total | pass_rate | coverage | missing | distractors | latency_ms |", "|---:|---|---:|---:|---:|---:|---:|---:|---:|"])
    for item in payload["ranking"]:
        lines.append(
            f"| {item['rank']} | `{item['model']}` | {item['passed_questions']} | {item['total_questions']} | "
            f"{item['pass_rate']:.4f} | {item['evidence_coverage']:.4f} | {item['missing_evidence']} | "
            f"{item['distractors']} | {item['latency_ms']:.1f} |"
        )
    lines.extend(
        [
            "",
            "## Acceptance Verdict",
            f"- Available-results gate: `{payload['acceptance']['available_results_gate']}`",
            f"- {payload['acceptance']['available_results_verdict']}",
            f"- Full benchmark completion: `{payload['acceptance']['full_benchmark_completion']}`",
            f"- {payload['acceptance']['full_benchmark_verdict']}",
            "",
            "## Missing Or Skipped Configs",
        ]
    )
    for item in payload["missing_or_skipped_configs"]:
        lines.append(
            f"- `{item['stage']}` / `{', '.join(item['models'])}`: {item['status']} - {item['reason']}"
        )
    if payload["unaccounted_registry_models"]:
        lines.extend(["", "## Unaccounted Registry Models", ""])
        for model in payload["unaccounted_registry_models"]:
            lines.append(f"- `{model}`")
    if payload["run_logs"]:
        lines.extend(["", "## Run Logs", ""])
        for item in payload["run_logs"]:
            lines.append(f"- `{item['path']}` ({item['size_bytes']} bytes)")
    lines.extend(["", "## Notes", f"- {payload['not_rerun_statement']}", ""])
    return "\n".join(lines)


def main() -> None:
    payload = build_aggregate()
    AGGREGATE_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    AGGREGATE_MD.write_text(_render_markdown(payload), encoding="utf-8")
    print(f"Wrote {AGGREGATE_JSON}")
    print(f"Wrote {AGGREGATE_MD}")
    print(f"Ranking models: {len(payload['ranking'])}")
    print(f"Full benchmark completion: {payload['acceptance']['full_benchmark_completion']}")


if __name__ == "__main__":
    main()
