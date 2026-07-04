from __future__ import annotations

from collections.abc import Sequence

from rag_eval.metrics.schemas import (
    RagQualityAggregateMetrics,
    RagQualityConfigEvaluation,
    RagQualityConfigScore,
    RagQualitySelectionResult,
)


def _is_acceptable(value: float | None, threshold: float | None) -> bool:
    if threshold is None or value is None:
        return True

    return value <= threshold


def _ranking_tuple(
    config_evaluation: RagQualityConfigEvaluation,
    *,
    max_average_latency_ms: float | None,
    max_cost_estimate_total: float | None,
) -> tuple[float, float, float, float, int, int, float, float]:
    metrics = config_evaluation.metrics
    acceptable_latency = _is_acceptable(metrics.average_latency_ms, max_average_latency_ms)
    acceptable_cost = _is_acceptable(metrics.cost_estimate_total, max_cost_estimate_total)
    latency_score = -metrics.average_latency_ms if metrics.average_latency_ms is not None else 0
    cost_score = -metrics.cost_estimate_total if metrics.cost_estimate_total is not None else 0

    return (
        metrics.hit_rate,
        metrics.evidence_marker_coverage,
        metrics.recall_at_k,
        metrics.mrr,
        int(acceptable_latency),
        int(acceptable_cost),
        latency_score,
        cost_score,
    )


def _build_score(
    config_evaluation: RagQualityConfigEvaluation,
    *,
    max_average_latency_ms: float | None,
    max_cost_estimate_total: float | None,
) -> RagQualityConfigScore:
    metrics = config_evaluation.metrics
    acceptable_latency = _is_acceptable(metrics.average_latency_ms, max_average_latency_ms)
    acceptable_cost = _is_acceptable(metrics.cost_estimate_total, max_cost_estimate_total)

    reasons = [
        f"hit_rate={metrics.hit_rate:.3f}",
        f"evidence_marker_coverage={metrics.evidence_marker_coverage:.3f}",
        f"recall_at_k={metrics.recall_at_k:.3f}",
        f"mrr={metrics.mrr:.3f}",
        f"forbidden_marker_rate={metrics.forbidden_marker_rate:.3f}",
    ]
    warnings = list(config_evaluation.warnings)
    if not acceptable_latency:
        warnings.append("Average latency exceeds the acceptable threshold.")
    if not acceptable_cost:
        warnings.append("Total cost estimate exceeds the acceptable threshold.")

    return RagQualityConfigScore(
        config_id=config_evaluation.config_id,
        model_code=config_evaluation.model_code,
        collection_name=config_evaluation.collection_name,
        metrics=metrics,
        acceptable_latency=acceptable_latency,
        acceptable_cost=acceptable_cost,
        ranking_factors={
            "hit_rate": metrics.hit_rate,
            "evidence_marker_coverage": metrics.evidence_marker_coverage,
            "recall_at_k": metrics.recall_at_k,
            "mrr": metrics.mrr,
            "forbidden_marker_rate": metrics.forbidden_marker_rate,
            "acceptable_latency": acceptable_latency,
            "acceptable_cost": acceptable_cost,
            "average_latency_ms": metrics.average_latency_ms,
            "cost_estimate_total": metrics.cost_estimate_total,
        },
        reasons=reasons,
        warnings=warnings,
    )


def _is_quality_competitive(
    contender: RagQualityConfigEvaluation,
    reference: RagQualityConfigEvaluation,
    *,
    quality_tolerance: float,
) -> bool:
    contender_metrics = contender.metrics
    reference_metrics = reference.metrics
    return (
        contender_metrics.hit_rate + quality_tolerance >= reference_metrics.hit_rate
        and contender_metrics.evidence_marker_coverage + quality_tolerance
        >= reference_metrics.evidence_marker_coverage
        and contender_metrics.recall_at_k + quality_tolerance >= reference_metrics.recall_at_k
    )


def select_best_config(
    config_evaluations: Sequence[RagQualityConfigEvaluation],
    *,
    max_average_latency_ms: float | None = None,
    max_cost_estimate_total: float | None = None,
    quality_tolerance: float = 0.05,
    forbidden_rate_safety_delta: float = 0.10,
) -> RagQualitySelectionResult:
    if not config_evaluations:
        return RagQualitySelectionResult(
            warnings=["No config evaluations were provided for selection."],
        )

    sorted_candidates = sorted(
        config_evaluations,
        key=lambda item: (
            _ranking_tuple(
                item,
                max_average_latency_ms=max_average_latency_ms,
                max_cost_estimate_total=max_cost_estimate_total,
            ),
            -item.metrics.forbidden_marker_rate,
        ),
        reverse=True,
    )
    provisional_best = sorted_candidates[0]
    selected_candidate = provisional_best
    reasons = [
        "Selection order: hit_rate/evidence marker coverage, recall_at_k, MRR, safety, latency, cost."
    ]
    warnings: list[str] = []

    safer_competitors = [
        item
        for item in sorted_candidates[1:]
        if _is_quality_competitive(
            item,
            provisional_best,
            quality_tolerance=quality_tolerance,
        )
        and item.metrics.forbidden_marker_rate + forbidden_rate_safety_delta
        <= provisional_best.metrics.forbidden_marker_rate
    ]
    if safer_competitors:
        selected_candidate = max(
            safer_competitors,
            key=lambda item: _ranking_tuple(
                item,
                max_average_latency_ms=max_average_latency_ms,
                max_cost_estimate_total=max_cost_estimate_total,
            ),
        )
        reasons.append(
            "Applied safety override because a near-equal quality config had a materially lower forbidden marker rate."
        )

    if selected_candidate.metrics.forbidden_marker_rate > 0:
        warnings.append("Selected config still has a non-zero forbidden marker rate.")

    all_scores = [
        _build_score(
            item,
            max_average_latency_ms=max_average_latency_ms,
            max_cost_estimate_total=max_cost_estimate_total,
        )
        for item in sorted_candidates
    ]

    return RagQualitySelectionResult(
        best_config_id=selected_candidate.config_id,
        best_model_code=selected_candidate.model_code,
        best_collection_name=selected_candidate.collection_name,
        selected_metrics=selected_candidate.metrics,
        all_config_scores=all_scores,
        reasons=reasons,
        warnings=warnings,
    )
