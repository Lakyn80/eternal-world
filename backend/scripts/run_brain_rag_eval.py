from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from app.db.session import SessionLocal
from app.modules.rag_evaluation.brain_eval_e2e_runner import run_brain_rag_eval_e2e
from app.modules.rag_evaluation.brain_eval_runner import (
    preflight_brain_rag_eval,
    run_brain_rag_eval,
)
from app.modules.rag_evaluation.exceptions import BrainRagEvalConfigurationError, RagEvaluationError
from app.modules.rag_evaluation.schemas import BrainRagEvalCaseSet, BrainRagEvalConfig

DEFAULT_ARTIFACT_DIR = Path("artifacts/brain_rag_eval")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Run Brain Agent RAG Q&A evaluation against the configured "
            "openai_compatible provider (Task 61)."
        ),
    )
    parser.add_argument(
        "--case-set",
        choices=(
            "foundation",
            "eternal_world",
            "family_avatar",
            "family_avatar_cs",
            "family_avatar_ru",
            "family_avatar_ru_e2e",
            "family_avatar_en",
            "family_avatar_es",
            "family_avatar_fr",
            "all",
        ),
        default="foundation",
        help="Evaluation case set to run (default: foundation).",
    )
    parser.add_argument(
        "--artifact-dir",
        type=Path,
        default=DEFAULT_ARTIFACT_DIR,
        help=f"Directory for JSON/Markdown artifacts (default: {DEFAULT_ARTIFACT_DIR}).",
    )
    parser.add_argument(
        "--no-artifacts",
        action="store_true",
        help="Skip writing artifact files.",
    )
    parser.add_argument(
        "--preflight",
        action="store_true",
        help="Validate configuration and case set without calling the Brain provider.",
    )
    parser.add_argument(
        "--real-retrieval",
        action="store_true",
        help=(
            "Run through real Qdrant retrieval instead of injected fixture evidence. "
            "Requires prefetched BAAI/bge-m3 cache; for offline runs set "
            "HF_HUB_OFFLINE=1 and TRANSFORMERS_OFFLINE=1."
        ),
    )
    parser.add_argument(
        "--allow-mock-embeddings",
        action="store_true",
        help="Allow real-retrieval E2E to run with mock embedding providers (diagnostics only).",
    )
    parser.add_argument("--json", action="store_true", dest="json_output")
    return parser


def _print_text_preflight(result) -> None:
    status = "PASS" if result.passed else "FAIL"
    print(f"BRAIN RAG EVAL PREFLIGHT: {status}")
    print(f"provider: {result.provider_name}")
    print(f"model: {result.model or 'unknown'}")
    print(f"case_set: {result.case_set}")
    print(f"case_count: {result.case_count}")
    for issue in result.issues:
        print(f"issue: {issue}")


def _print_text_result(result) -> None:
    print(f"BRAIN RAG EVAL RESULT: {'PASS' if result.passed else 'FAIL'}")
    print(f"run_id: {result.run_id}")
    print(f"provider: {result.provider_name}")
    print(f"model: {result.model or 'unknown'}")
    print(f"case_set: {result.case_set}")
    print(
        f"passed_cases: {result.suite_result.passed_cases}/"
        f"{result.suite_result.total_cases}"
    )
    print()
    for case_result in result.suite_result.results:
        status = "PASS" if case_result.passed else "FAIL"
        print(f"[{status}] {case_result.case_id}")
        print(f"  expected: {case_result.expected_behavior}")
        print(f"  actual: {case_result.actual_behavior}")
        if case_result.reasons:
            print(f"  reasons: {'; '.join(case_result.reasons)}")
    if result.artifact_paths:
        print()
        print("artifacts:")
        for key, path in sorted(result.artifact_paths.items()):
            print(f"  {key}: {path}")


def _print_text_e2e_result(result) -> None:
    print(f"BRAIN RAG E2E RESULT: {'PASS' if result.passed else 'FAIL'}")
    print(f"run_id: {result.run_id}")
    print(f"provider: {result.provider_name}")
    print(f"model: {result.model or 'unknown'}")
    print(f"case_set: {result.case_set}")
    print(f"profile_id: {result.profile_id}")
    print(f"embedding_model: {result.embedding_model_code}")
    print(f"retrieval_mode: {result.retrieval_mode}")
    print(f"qdrant_collection: {result.qdrant_collection}")
    print(f"top_k: {result.top_k}")
    print(f"embedding_provider: {result.embedding_diagnostics.embedding_provider_setting}")
    print(f"indexing_provider: {result.embedding_diagnostics.resolved_indexing_provider_name}")
    print(f"query_provider: {result.embedding_diagnostics.resolved_query_provider_name}")
    print(f"mock_indexing_provider: {result.embedding_diagnostics.is_mock_indexing_provider}")
    print(f"mock_query_provider: {result.embedding_diagnostics.is_mock_query_provider}")
    print(f"embedding_dimension: {result.embedding_diagnostics.embedding_dimension}")
    print(f"collection_vector_size: {result.embedding_diagnostics.collection_vector_size}")
    print(f"collection_rebuilt: {result.embedding_diagnostics.collection_rebuilt}")
    print(f"bge_m3_snapshot_cached: {result.embedding_diagnostics.bge_m3_snapshot_cached}")
    print(f"bge_m3_snapshot_path: {result.embedding_diagnostics.bge_m3_snapshot_path}")
    print(
        f"passed_cases: {result.suite_result.passed_cases}/"
        f"{result.suite_result.total_cases}"
    )
    print(f"retrieval_failures: {result.suite_result.retrieval_failures}")
    print(f"answer_failures: {result.suite_result.answer_failures}")
    print()
    print("retrieval_diagnostics:")
    for diagnostic in result.retrieval_diagnostics:
        print(
            f"  - {diagnostic.case_id}: qdrant_exists={diagnostic.expected_chunk_exists_in_qdrant} "
            f"bucket={diagnostic.expected_chunk_position_bucket} "
            f"top5={diagnostic.expected_chunk_in_top_5} "
            f"top10={diagnostic.expected_chunk_in_top_10} "
            f"top20={diagnostic.expected_chunk_in_top_20} "
            f"top50={diagnostic.expected_chunk_in_top_50} "
            f"rank_top50={diagnostic.expected_chunk_rank_at_50} "
            f"retrieved={diagnostic.retrieved_chunk_ids}"
        )
    print("top_k_diagnostics:")
    for diagnostic in result.top_k_diagnostics:
        print(
            f"  - top_k={diagnostic.top_k}: "
            f"{diagnostic.expected_chunk_hits}/{diagnostic.expected_chunk_checks}"
        )
    print()
    for case_result in result.suite_result.results:
        status = "PASS" if case_result.passed else "FAIL"
        print(f"[{status}] {case_result.case_id}")
        print(f"  expected: {case_result.expected_behavior}")
        print(f"  actual: {case_result.actual_behavior}")
        if case_result.failure_class:
            print(f"  failure_class: {case_result.failure_class}")
        if case_result.retrieved_chunks:
            chunk_ids = ", ".join(
                f"{item.chunk_id}({item.score:.3f})" for item in case_result.retrieved_chunks
            )
            print(f"  retrieved_chunks: {chunk_ids}")
        if case_result.reasons:
            print(f"  reasons: {'; '.join(case_result.reasons)}")
    if result.artifact_paths:
        print()
        print("artifacts:")
        for key, path in sorted(result.artifact_paths.items()):
            print(f"  {key}: {path}")


def main() -> int:
    args = _build_parser().parse_args()
    case_set: BrainRagEvalCaseSet = args.case_set
    real_retrieval = args.real_retrieval or case_set == "family_avatar_ru_e2e"
    config = BrainRagEvalConfig(
        case_set=case_set,
        artifact_dir=args.artifact_dir,
        write_artifacts=not args.no_artifacts,
        real_retrieval=real_retrieval,
        allow_mock_embeddings=args.allow_mock_embeddings,
    )

    try:
        if args.preflight:
            preflight_result = preflight_brain_rag_eval(config)
            if args.json_output:
                print(json.dumps(preflight_result.model_dump(mode="json"), indent=2, sort_keys=True))
            else:
                _print_text_preflight(preflight_result)
            return 0 if preflight_result.passed else 1

        if real_retrieval:
            db = SessionLocal()
            try:
                result = run_brain_rag_eval_e2e(db, config)
            finally:
                db.close()
            if args.json_output:
                print(json.dumps(result.model_dump(mode="json"), indent=2, sort_keys=True))
            else:
                _print_text_e2e_result(result)
            return 0 if result.passed else 1

        result = run_brain_rag_eval(config)
    except (BrainRagEvalConfigurationError, RagEvaluationError) as exc:
        print(f"BRAIN RAG EVAL ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json_output:
        print(json.dumps(result.model_dump(mode="json"), indent=2, sort_keys=True))
    else:
        _print_text_result(result)

    return 0 if result.passed else 1


if __name__ == "__main__":
    sys.exit(main())
