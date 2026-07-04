from __future__ import annotations

from collections.abc import Mapping, Sequence

from rag_eval.metrics.evaluator import evaluate_case_results
from rag_eval.metrics.metrics import build_aggregate_metrics, summarize_metric_reasons
from rag_eval.metrics.schemas import (
    RagQualityCaseEvaluation,
    RagQualityCaseResultsInput,
    RagQualityConfigEvaluation,
    RagQualityDatasetEvaluation,
    RagQualityEvalDataset,
    RagQualityRetrievalConfigCandidate,
    RagQualityRetrievalResultItem,
    RagQualityRunResult,
    RagQualitySelectionResult,
)
from rag_eval.metrics.selectors import select_best_config


class RagQualityService:
    def evaluate_case_results(
        self,
        *,
        case,
        case_results: RagQualityCaseResultsInput | None,
        config_id: str | None = None,
    ) -> RagQualityCaseEvaluation:
        return evaluate_case_results(
            case=case,
            case_results=case_results,
            config_id=config_id,
        )

    def evaluate_config_results(
        self,
        *,
        dataset: RagQualityEvalDataset,
        candidate: RagQualityRetrievalConfigCandidate,
        case_results_inputs: Sequence[RagQualityCaseResultsInput],
    ) -> RagQualityConfigEvaluation:
        case_results_by_case_id = {
            item.case_id: item
            for item in case_results_inputs
            if item.config_id == candidate.config_id
        }
        case_evaluations = [
            self.evaluate_case_results(
                case=case,
                case_results=case_results_by_case_id.get(case.case_id),
                config_id=candidate.config_id,
            )
            for case in dataset.cases
        ]
        metrics = build_aggregate_metrics(case_evaluations)
        passed_case_count = sum(1 for item in case_evaluations if item.passed)
        failed_case_count = len(case_evaluations) - passed_case_count

        warnings: list[str] = []
        if any(item.input_missing for item in case_evaluations):
            warnings.append("One or more dataset cases were missing retrieval inputs.")
        if metrics.forbidden_marker_rate > 0:
            warnings.append("Forbidden markers were detected in at least one evaluated result set.")
        if metrics.average_latency_ms is None:
            warnings.append("Average latency could not be computed because latency values were not provided.")
        if metrics.cost_estimate_total is None:
            warnings.append("Cost estimate total could not be computed because cost values were not provided.")

        return RagQualityConfigEvaluation(
            config_id=candidate.config_id,
            model_code=candidate.model_code,
            collection_name=candidate.collection_name,
            retrieval_mode=candidate.retrieval_mode,
            passed_case_count=passed_case_count,
            failed_case_count=failed_case_count,
            metrics=metrics,
            case_evaluations=case_evaluations,
            reasons=summarize_metric_reasons(metrics),
            warnings=warnings,
            metadata=dict(candidate.metadata),
        )

    def evaluate_dataset_results(
        self,
        *,
        dataset: RagQualityEvalDataset,
        candidates: Sequence[RagQualityRetrievalConfigCandidate],
        case_results_inputs: Sequence[RagQualityCaseResultsInput],
    ) -> RagQualityDatasetEvaluation:
        config_evaluations = [
            self.evaluate_config_results(
                dataset=dataset,
                candidate=candidate,
                case_results_inputs=case_results_inputs,
            )
            for candidate in candidates
        ]

        warnings: list[str] = []
        if not dataset.cases:
            warnings.append("Dataset contains no evaluation cases.")
        if not candidates:
            warnings.append("No retrieval config candidates were provided.")

        return RagQualityDatasetEvaluation(
            dataset_id=dataset.dataset_id,
            dataset_name=dataset.name,
            total_cases=len(dataset.cases),
            config_evaluations=config_evaluations,
            warnings=warnings,
        )

    def select_best_config(
        self,
        *,
        config_evaluations: Sequence[RagQualityConfigEvaluation],
        max_average_latency_ms: float | None = None,
        max_cost_estimate_total: float | None = None,
    ) -> RagQualitySelectionResult:
        return select_best_config(
            config_evaluations,
            max_average_latency_ms=max_average_latency_ms,
            max_cost_estimate_total=max_cost_estimate_total,
        )

    def run_quality_evaluation(
        self,
        *,
        dataset: RagQualityEvalDataset,
        candidates: Sequence[RagQualityRetrievalConfigCandidate],
        case_results_inputs: Sequence[RagQualityCaseResultsInput],
        max_average_latency_ms: float | None = None,
        max_cost_estimate_total: float | None = None,
    ) -> RagQualityRunResult:
        dataset_evaluation = self.evaluate_dataset_results(
            dataset=dataset,
            candidates=candidates,
            case_results_inputs=case_results_inputs,
        )
        selection = self.select_best_config(
            config_evaluations=dataset_evaluation.config_evaluations,
            max_average_latency_ms=max_average_latency_ms,
            max_cost_estimate_total=max_cost_estimate_total,
        )
        return RagQualityRunResult(
            dataset_evaluation=dataset_evaluation,
            selection=selection,
        )

    def adapt_rag_retrieval_response(
        self,
        *,
        case_id: str,
        candidate: RagQualityRetrievalConfigCandidate,
        retrieval_response,
        latency_ms: float | None = None,
        cost_estimate: float | None = None,
        metadata: Mapping[str, object] | None = None,
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
            cost_estimate=cost_estimate,
            metadata=dict(metadata or {}),
        )
