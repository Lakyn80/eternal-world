from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from rag_eval.config import BenchmarkConfig
from rag_eval.datasets.loader import ExternalEvalDataset
from rag_eval.datasets.validate import build_collection_name
from rag_eval.retrieval.bm25 import BM25_MODEL_CODE


RetrievalMode = Literal["dense", "bm25", "dense_plus_bm25"]


@dataclass(frozen=True)
class RetrievalCandidateSpec:
    config_id: str
    model_code: str
    collection_name: str
    retrieval_mode: RetrievalMode


def expand_retrieval_candidates(
    *,
    config: BenchmarkConfig,
    dataset: ExternalEvalDataset,
) -> list[RetrievalCandidateSpec]:
    modes = config.retrieval.resolved_modes()
    model_codes = config.resolved_model_codes()
    candidates: list[RetrievalCandidateSpec] = []
    bm25_added = False

    for mode in modes:
        if mode == "bm25":
            if bm25_added:
                continue
            candidates.append(
                RetrievalCandidateSpec(
                    config_id=f"{BM25_MODEL_CODE}__bm25",
                    model_code=BM25_MODEL_CODE,
                    collection_name=build_collection_name(
                        collection_prefix=config.collection_prefix,
                        model_code=BM25_MODEL_CODE,
                        dataset=dataset,
                    ),
                    retrieval_mode="bm25",
                )
            )
            bm25_added = True
            continue

        for model_code in model_codes:
            if mode == "dense":
                candidates.append(
                    RetrievalCandidateSpec(
                        config_id=f"{model_code}__dense",
                        model_code=model_code,
                        collection_name=build_collection_name(
                            collection_prefix=config.collection_prefix,
                            model_code=model_code,
                            dataset=dataset,
                        ),
                        retrieval_mode="dense",
                    )
                )
            elif mode == "dense_plus_bm25":
                candidates.append(
                    RetrievalCandidateSpec(
                        config_id=f"{model_code}__dense_plus_bm25",
                        model_code=model_code,
                        collection_name=build_collection_name(
                            collection_prefix=config.collection_prefix,
                            model_code=model_code,
                            dataset=dataset,
                        ),
                        retrieval_mode="dense_plus_bm25",
                    )
                )

    return candidates
