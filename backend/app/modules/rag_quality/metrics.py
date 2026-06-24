from __future__ import annotations

from collections.abc import Iterable, Sequence

from app.modules.rag_quality.schemas import RagQualityAggregateMetrics, RagQualityCaseEvaluation


def normalize_text(value: str) -> str:
    return " ".join(value.lower().split())


def marker_present(text: str, marker: str) -> bool:
    return normalize_text(marker) in normalize_text(text)


def average(values: Sequence[float]) -> float | None:
    if not values:
        return None

    return sum(values) / len(values)


def hit_rate(case_evaluations: Sequence[RagQualityCaseEvaluation]) -> float:
    if not case_evaluations:
        return 0

    return sum(1 for item in case_evaluations if item.hit) / len(case_evaluations)


def recall_at_k(case_evaluations: Sequence[RagQualityCaseEvaluation]) -> float:
    values = [item.recall_at_k for item in case_evaluations if item.recall_at_k is not None]
    if not values:
        return 0

    return sum(values) / len(values)


def mean_reciprocal_rank(case_evaluations: Sequence[RagQualityCaseEvaluation]) -> float:
    values = [item.reciprocal_rank for item in case_evaluations if item.reciprocal_rank is not None]
    if not values:
        return 0

    return sum(values) / len(values)


def forbidden_marker_rate(case_evaluations: Sequence[RagQualityCaseEvaluation]) -> float:
    if not case_evaluations:
        return 0

    total_forbidden_rate = sum(item.forbidden_marker_rate for item in case_evaluations)
    return total_forbidden_rate / len(case_evaluations)


def evidence_marker_coverage(case_evaluations: Sequence[RagQualityCaseEvaluation]) -> float:
    values = [
        item.evidence_marker_coverage
        for item in case_evaluations
        if item.evidence_marker_coverage is not None
    ]
    if not values:
        return 0

    return sum(values) / len(values)


def missing_expected_marker_count(case_evaluations: Sequence[RagQualityCaseEvaluation]) -> int:
    return sum(len(item.missing_expected_markers) for item in case_evaluations)


def false_positive_count(case_evaluations: Sequence[RagQualityCaseEvaluation]) -> int:
    return sum(item.false_positive_count for item in case_evaluations)


def average_latency_ms(case_evaluations: Sequence[RagQualityCaseEvaluation]) -> float | None:
    latency_values = [item.latency_ms for item in case_evaluations if item.latency_ms is not None]
    return average(latency_values)


def cost_estimate_total(case_evaluations: Sequence[RagQualityCaseEvaluation]) -> float | None:
    cost_values = [item.cost_estimate for item in case_evaluations if item.cost_estimate is not None]
    if not cost_values:
        return None

    return sum(cost_values)


def build_aggregate_metrics(
    case_evaluations: Sequence[RagQualityCaseEvaluation],
) -> RagQualityAggregateMetrics:
    return RagQualityAggregateMetrics(
        hit_rate=hit_rate(case_evaluations),
        recall_at_k=recall_at_k(case_evaluations),
        mrr=mean_reciprocal_rank(case_evaluations),
        forbidden_marker_rate=forbidden_marker_rate(case_evaluations),
        average_latency_ms=average_latency_ms(case_evaluations),
        cost_estimate_total=cost_estimate_total(case_evaluations),
        evidence_marker_coverage=evidence_marker_coverage(case_evaluations),
        missing_expected_marker_count=missing_expected_marker_count(case_evaluations),
        false_positive_count=false_positive_count(case_evaluations),
    )


def summarize_metric_reasons(metrics: RagQualityAggregateMetrics) -> list[str]:
    reasons = [
        f"hit_rate={metrics.hit_rate:.3f}",
        f"evidence_marker_coverage={metrics.evidence_marker_coverage:.3f}",
        f"recall_at_k={metrics.recall_at_k:.3f}",
        f"mrr={metrics.mrr:.3f}",
        f"forbidden_marker_rate={metrics.forbidden_marker_rate:.3f}",
        f"missing_expected_marker_count={metrics.missing_expected_marker_count}",
        f"false_positive_count={metrics.false_positive_count}",
    ]
    if metrics.average_latency_ms is not None:
        reasons.append(f"average_latency_ms={metrics.average_latency_ms:.3f}")
    if metrics.cost_estimate_total is not None:
        reasons.append(f"cost_estimate_total={metrics.cost_estimate_total:.6f}")

    return reasons
