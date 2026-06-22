from __future__ import annotations


def rank_retrieval_results(
    results: list[dict[str, object]],
    *,
    limit: int,
    score_threshold: float | None = None,
) -> list[dict[str, object]]:
    ranked_results: list[dict[str, object]] = []
    for result in results:
        score = result.get("score")
        if not isinstance(score, (int, float)):
            continue

        normalized_score = float(score)
        if score_threshold is not None and normalized_score < score_threshold:
            continue

        ranked_results.append(
            {
                **result,
                "score": normalized_score,
            }
        )

    ranked_results.sort(
        key=lambda item: (
            float(item["score"]),
            int(item.get("chunk_id", 0)),
            int(item.get("embedding_id", 0)),
        ),
        reverse=True,
    )
    return ranked_results[:limit]
