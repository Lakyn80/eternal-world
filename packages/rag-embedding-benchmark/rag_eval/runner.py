from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from time import perf_counter
from typing import Any

from rag_eval.adapters.base import RagEvalBackend, RagEvalRetrievalResponse
from rag_eval.config import BenchmarkConfig
from rag_eval.datasets.loader import ExternalEvalDataset, load_external_eval_dataset
from rag_eval.datasets.validate import (
    PreflightValidation,
    validate_dataset_against_chunks,
    validate_dataset_schema,
)
from rag_eval.metrics.schemas import (
    RagQualityCaseResultsInput,
    RagQualityConfigEvaluation,
    RagQualityRetrievalConfigCandidate,
    RagQualityRetrievalResultItem,
    RagQualityRunResult,
)
from rag_eval.metrics.service import RagQualityService
from rag_eval.models.registry import get_embedding_model_definition
from rag_eval.report import write_ranking_artifacts
from rag_eval.retrieval.bm25 import BM25_MODEL_CODE
from rag_eval.retrieval.candidates import expand_retrieval_candidates


@dataclass
class ModelRunFailure:
    model_code: str
    status: str
    error: str
    config_id: str | None = None


@dataclass
class BenchmarkRunResult:
    run_id: str
    dataset_id: str
    winner_model_code: str | None
    winner_config_id: str | None
    quality_result: RagQualityRunResult | None
    failed_models: list[ModelRunFailure] = field(default_factory=list)
    preflight_validation: PreflightValidation | None = None
    artifact_paths: dict[str, str] = field(default_factory=dict)


def validate_benchmark(*, config: BenchmarkConfig, backend: RagEvalBackend) -> PreflightValidation:
    dataset = validate_dataset_schema(config.dataset)
    source_chunks = backend.get_source_chunks(source_id=config.source_id)
    return validate_dataset_against_chunks(dataset=dataset, source_chunks=source_chunks)


def run_benchmark(*, config: BenchmarkConfig, backend: RagEvalBackend) -> BenchmarkRunResult:
    config.apply_runtime_env()
    config.artifact_dir.mkdir(parents=True, exist_ok=True)

    dataset = validate_dataset_schema(config.dataset)
    rag_quality_dataset = load_external_eval_dataset(config.dataset)
    source_chunks = backend.get_source_chunks(source_id=config.source_id)
    preflight_validation = validate_dataset_against_chunks(dataset=dataset, source_chunks=source_chunks)
    if not preflight_validation.passed:
        raise ValueError(
            f"Dataset preflight failed with {preflight_validation.issue_count} issue(s): "
            f"{preflight_validation.issues[0].detail if preflight_validation.issues else 'unknown'}"
        )

    run_id = datetime.now(UTC).strftime("%Y%m%d_%H%M%SZ")
    rag_quality_service = RagQualityService()
    candidates: list[RagQualityRetrievalConfigCandidate] = []
    case_results_inputs: list[RagQualityCaseResultsInput] = []
    failed_models: list[ModelRunFailure] = []
    config_evaluations: list[RagQualityConfigEvaluation] = []
    candidate_specs = expand_retrieval_candidates(config=config, dataset=dataset)
    indexed_collections: set[tuple[str, str]] = set()

    for candidate_spec in candidate_specs:
        if candidate_spec.model_code != BM25_MODEL_CODE:
            model_definition = get_embedding_model_definition(candidate_spec.model_code)
            if model_definition is None:
                failed_models.append(
                    ModelRunFailure(
                        model_code=candidate_spec.model_code,
                        config_id=candidate_spec.config_id,
                        status="UNKNOWN_MODEL",
                        error=f"Unknown embedding model code: {candidate_spec.model_code}",
                    )
                )
                continue

        candidate = RagQualityRetrievalConfigCandidate(
            config_id=candidate_spec.config_id,
            model_code=candidate_spec.model_code,
            collection_name=candidate_spec.collection_name,
            top_k=config.top_k,
            score_threshold=config.score_threshold,
            retrieval_mode=candidate_spec.retrieval_mode,
            metadata=_candidate_metadata(config, candidate_spec.retrieval_mode),
        )

        try:
            if candidate_spec.retrieval_mode in {"dense", "dense_plus_bm25"}:
                index_key = (candidate_spec.model_code, candidate_spec.collection_name)
                if index_key not in indexed_collections:
                    backend.embed_source(
                        source_id=config.source_id,
                        model_code=candidate_spec.model_code,
                    )
                    backend.index_source(
                        source_id=config.source_id,
                        model_code=candidate_spec.model_code,
                        collection_name=candidate_spec.collection_name,
                    )
                    indexed_collections.add(index_key)

            model_case_inputs: list[RagQualityCaseResultsInput] = []
            for case in rag_quality_dataset.cases:
                started_at = perf_counter()
                retrieval_response = backend.retrieve(
                    profile_id=config.profile_id,
                    source_id=config.source_id,
                    query=case.query,
                    model_code=candidate_spec.model_code,
                    collection_name=candidate_spec.collection_name,
                    top_k=config.top_k,
                    score_threshold=config.score_threshold,
                    retrieval_mode=candidate_spec.retrieval_mode,
                )
                latency_ms = round((perf_counter() - started_at) * 1000, 3)
                model_case_inputs.append(
                    _adapt_retrieval_response(
                        case_id=case.case_id,
                        candidate=candidate,
                        retrieval_response=retrieval_response,
                        latency_ms=latency_ms,
                    )
                )

            case_results_inputs.extend(model_case_inputs)
            candidates.append(candidate)
            config_evaluations.append(
                rag_quality_service.evaluate_config_results(
                    dataset=rag_quality_dataset,
                    candidate=candidate,
                    case_results_inputs=model_case_inputs,
                )
            )
        except Exception as exc:
            failed_models.append(
                ModelRunFailure(
                    model_code=candidate_spec.model_code,
                    config_id=candidate_spec.config_id,
                    status=_classify_failure(exc),
                    error=str(exc),
                )
            )

    quality_result = None
    if config_evaluations:
        quality_result = rag_quality_service.run_quality_evaluation(
            dataset=rag_quality_dataset,
            candidates=candidates,
            case_results_inputs=case_results_inputs,
            max_average_latency_ms=config.max_average_latency_ms,
            max_cost_estimate_total=config.max_cost_estimate_total,
        )

    artifact_paths = write_benchmark_artifacts(
        artifact_dir=config.artifact_dir,
        run_id=run_id,
        dataset=dataset,
        quality_result=quality_result,
        failed_models=failed_models,
        preflight_validation=preflight_validation,
    )

    winner_model_code = None
    winner_config_id = None
    if quality_result is not None:
        winner_model_code = quality_result.selection.best_model_code
        winner_config_id = quality_result.selection.best_config_id

    return BenchmarkRunResult(
        run_id=run_id,
        dataset_id=dataset.dataset_id,
        winner_model_code=winner_model_code,
        winner_config_id=winner_config_id,
        quality_result=quality_result,
        failed_models=failed_models,
        preflight_validation=preflight_validation,
        artifact_paths=artifact_paths,
    )


def _candidate_metadata(config: BenchmarkConfig, retrieval_mode: str) -> dict[str, object]:
    metadata: dict[str, object] = {"device": config.device}
    if retrieval_mode == "dense_plus_bm25":
        metadata["fusion"] = config.retrieval.fusion
        metadata["rrf_k"] = config.retrieval.rrf_k
    return metadata


def _adapt_retrieval_response(
    *,
    case_id: str,
    candidate: RagQualityRetrievalConfigCandidate,
    retrieval_response: RagEvalRetrievalResponse,
    latency_ms: float,
) -> RagQualityCaseResultsInput:
    return RagQualityCaseResultsInput(
        config_id=candidate.config_id,
        case_id=case_id,
        results=[
            RagQualityRetrievalResultItem(
                chunk_id=result.chunk_id,
                source_id=result.source_id,
                score=result.score,
                text=result.text,
                rank=index + 1,
                metadata={
                    "embedding_id": result.embedding_id,
                    "language": result.language,
                    "source_type": result.source_type,
                    "validation_status": result.validation_status,
                    "text_hash": result.text_hash,
                    "qdrant_collection": result.qdrant_collection,
                    "payload_metadata": result.payload_metadata,
                },
            )
            for index, result in enumerate(retrieval_response.results)
        ],
        latency_ms=latency_ms,
    )


def _classify_failure(exc: Exception) -> str:
    message = str(exc).lower()
    if "out of memory" in message or "oom" in message or "killed" in message:
        return "OOM"
    return "FAILED"



def write_benchmark_artifacts(
    *,
    artifact_dir: Path,
    run_id: str,
    dataset: ExternalEvalDataset,
    quality_result: RagQualityRunResult | None,
    failed_models: list[ModelRunFailure],
    preflight_validation: PreflightValidation,
) -> dict[str, str]:
    run_dir = artifact_dir / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    ranking_payload: dict[str, Any] = {
        "run_id": run_id,
        "dataset_id": dataset.dataset_id,
        "dataset_name": dataset.name,
        "preflight_passed": preflight_validation.passed,
        "preflight_issue_count": preflight_validation.issue_count,
        "failed_models": [
            {
                "model_code": item.model_code,
                "config_id": item.config_id,
                "status": item.status,
                "error": item.error,
            }
            for item in failed_models
        ],
    }

    if quality_result is not None:
        selection = quality_result.selection
        ranking_payload.update(
            {
                "winner": {
                    "config_id": selection.best_config_id,
                    "model_code": selection.best_model_code,
                    "collection_name": selection.best_collection_name,
                    "metrics": selection.selected_metrics.model_dump(mode="json")
                    if selection.selected_metrics is not None
                    else None,
                },
                "ranking": [
                    {
                        "config_id": score.config_id,
                        "model_code": score.model_code,
                        "collection_name": score.collection_name,
                        "metrics": score.metrics.model_dump(mode="json"),
                        "reasons": score.reasons,
                    }
                    for score in selection.all_config_scores
                ],
            }
        )

    ranking_json_path = artifact_dir / "ranking.json"
    ranking_md_path = artifact_dir / "report.md"
    run_ranking_json_path = run_dir / "ranking.json"
    run_ranking_md_path = run_dir / "report.md"

    write_ranking_artifacts(
        ranking_payload=ranking_payload,
        json_path=ranking_json_path,
        markdown_path=ranking_md_path,
    )
    write_ranking_artifacts(
        ranking_payload=ranking_payload,
        json_path=run_ranking_json_path,
        markdown_path=run_ranking_md_path,
    )

    preflight_path = run_dir / "preflight.json"
    preflight_path.write_text(
        json.dumps(
            {
                "passed": preflight_validation.passed,
                "issue_count": preflight_validation.issue_count,
                "issues": [
                    {
                        "question_id": issue.question_id,
                        "issue_code": issue.issue_code,
                        "marker": issue.marker,
                        "detail": issue.detail,
                    }
                    for issue in preflight_validation.issues
                ],
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    return {
        "ranking_json": str(ranking_json_path),
        "report_md": str(ranking_md_path),
        "run_dir": str(run_dir),
        "preflight_json": str(preflight_path),
    }
