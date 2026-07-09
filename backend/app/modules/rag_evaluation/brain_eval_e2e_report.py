from __future__ import annotations

import json
from pathlib import Path

from app.modules.rag_evaluation.brain_eval_e2e_schemas import BrainRagEvalE2ERunResult


def build_brain_rag_eval_e2e_markdown(result: BrainRagEvalE2ERunResult) -> str:
    lines = [
        "# Brain RAG E2E Evaluation Report",
        "",
        f"- Run ID: `{result.run_id}`",
        f"- Case set: `{result.case_set}`",
        f"- Provider: `{result.provider_name}`",
        f"- Model: `{result.model or 'unknown'}`",
        f"- Profile ID: `{result.profile_id}`",
        f"- Embedding model: `{result.embedding_model_code}`",
        f"- Retrieval mode: `{result.retrieval_mode}`",
        f"- Qdrant collection: `{result.qdrant_collection}`",
        f"- top_k: `{result.top_k}`",
        f"- Embedding provider setting: `{result.embedding_diagnostics.embedding_provider_setting}`",
        f"- Indexing provider: `{result.embedding_diagnostics.resolved_indexing_provider_name}`",
        f"- Query provider: `{result.embedding_diagnostics.resolved_query_provider_name}`",
        f"- Mock indexing provider: `{result.embedding_diagnostics.is_mock_indexing_provider}`",
        f"- Mock query provider: `{result.embedding_diagnostics.is_mock_query_provider}`",
        f"- Indexing/query providers match: `{result.embedding_diagnostics.indexing_query_providers_match}`",
        f"- Provider model name: `{result.embedding_diagnostics.provider_model_name or 'unknown'}`",
        f"- Embedding dimension: `{result.embedding_diagnostics.embedding_dimension}`",
        f"- Collection vector size: `{result.embedding_diagnostics.collection_vector_size}`",
        f"- BGE-M3 snapshot cached: `{result.embedding_diagnostics.bge_m3_snapshot_cached}`",
        f"- BGE-M3 snapshot path: `{result.embedding_diagnostics.bge_m3_snapshot_path}`",
        f"- Hugging Face offline mode: `{result.embedding_diagnostics.huggingface_offline_mode}`",
        f"- Embedding runtime fingerprint: `{result.embedding_diagnostics.embedding_runtime_fingerprint}`",
        f"- Collection rebuilt: `{result.embedding_diagnostics.collection_rebuilt}`",
        f"- Overall: `{'PASS' if result.passed else 'FAIL'}`",
        f"- Passed cases: `{result.suite_result.passed_cases}/{result.suite_result.total_cases}`",
        f"- Retrieval failures: `{result.suite_result.retrieval_failures}`",
        f"- Answer generation failures: `{result.suite_result.answer_failures}`",
        "",
        "## Retrieval Diagnostics",
        "",
    ]

    for diagnostic in result.retrieval_diagnostics:
        lines.extend(
            [
                f"- `{diagnostic.case_id}`",
                f"  - Query: {diagnostic.user_query}",
                f"  - Expected fact: `{diagnostic.expected_fact_id}`",
                f"  - Expected chunk: `{diagnostic.expected_chunk_id}`",
                f"  - Expected chunk source: `{diagnostic.expected_chunk_source_title}`",
                f"  - Expected chunk index: `{diagnostic.expected_chunk_index}`",
                f"  - Expected chunk exists in Qdrant: `{diagnostic.expected_chunk_exists_in_qdrant}`",
                f"  - Expected chunk in top_k: `{diagnostic.expected_chunk_in_top_k}`",
                f"  - Expected chunk rank at top_k: `{diagnostic.expected_chunk_rank}`",
                f"  - Expected chunk rank at top_50: `{diagnostic.expected_chunk_rank_at_50}`",
                f"  - Position bucket: `{diagnostic.expected_chunk_position_bucket}`",
                f"  - In top_5/top_10/top_20/top_50: `{diagnostic.expected_chunk_in_top_5}` / `{diagnostic.expected_chunk_in_top_10}` / `{diagnostic.expected_chunk_in_top_20}` / `{diagnostic.expected_chunk_in_top_50}`",
                f"  - Top retrieved chunk IDs: `{diagnostic.retrieved_chunk_ids}`",
            ]
        )
        for chunk in diagnostic.retrieved_chunks:
            lines.append(
                f"    - #{chunk.rank} chunk `{chunk.chunk_id}` score `{chunk.score:.4f}` source `{chunk.source_title or 'unknown'}` chunk_index `{chunk.chunk_index}`"
            )

    lines.extend(["", "## top_k Diagnostics", ""])
    for diagnostic in result.top_k_diagnostics:
        lines.append(
            f"- top_k=`{diagnostic.top_k}` expected-chunk hits="
            f"`{diagnostic.expected_chunk_hits}/{diagnostic.expected_chunk_checks}`"
        )

    lines.extend(
        [
        "",
        "## Case Results",
        "",
    ]
    )

    for index, case_result in enumerate(result.suite_result.results, start=1):
        status = "PASS" if case_result.passed else "FAIL"
        lines.extend(
            [
                f"{index}. `{case_result.case_id}` — **{status}**",
                f"   - Title: {case_result.title}",
                f"   - Question: {case_result.user_query}",
                f"   - Expected: `{case_result.expected_behavior}`",
                f"   - Actual: `{case_result.actual_behavior}`",
            ]
        )
        if case_result.failure_class:
            lines.append(f"   - Failure class: `{case_result.failure_class}`")
        if case_result.expected_fact_id:
            lines.append(f"   - Expected fact: `{case_result.expected_fact_id}`")
        if case_result.expected_evidence_found is not None:
            lines.append(
                f"   - Expected evidence in context: `{case_result.expected_evidence_found}`"
            )
        if case_result.expected_markers:
            lines.append(
                f"   - Expected markers: {', '.join(case_result.expected_markers)}"
            )
        if case_result.missing_expected_markers:
            lines.append(
                f"   - Missing markers: {', '.join(case_result.missing_expected_markers)}"
            )
        if case_result.selected_memory_ids:
            lines.append(
                f"   - Selected memory IDs: {', '.join(str(item) for item in case_result.selected_memory_ids)}"
            )
        if case_result.retrieved_chunks:
            chunk_summary = ", ".join(
                f"{item.chunk_id}@{item.score:.4f}" for item in case_result.retrieved_chunks
            )
            lines.append(f"   - Retrieved chunks: {chunk_summary}")
            for item in case_result.retrieved_chunks:
                lines.append(
                    f"     - #{item.rank} chunk `{item.chunk_id}` score `{item.score:.4f}`: {item.text_preview}"
                )
        lines.extend(
            [
                f"   - Answer: {case_result.answer_text}",
            ]
        )
        if case_result.reasons:
            lines.append(f"   - Reasons: {'; '.join(case_result.reasons)}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_brain_rag_eval_e2e_artifacts(
    *,
    result: BrainRagEvalE2ERunResult,
    artifact_dir: Path,
) -> dict[str, str]:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    run_dir = artifact_dir / "runs" / result.run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    result_json_path = run_dir / "e2e_result.json"
    report_md_path = run_dir / "e2e_report.md"
    latest_result_json_path = artifact_dir / "e2e_result.json"
    latest_report_md_path = artifact_dir / "e2e_report.md"

    payload = result.model_dump(mode="json")
    result_json_text = json.dumps(payload, indent=2, ensure_ascii=False)
    report_md_text = build_brain_rag_eval_e2e_markdown(result)

    result_json_path.write_text(result_json_text, encoding="utf-8")
    report_md_path.write_text(report_md_text, encoding="utf-8")
    latest_result_json_path.write_text(result_json_text, encoding="utf-8")
    latest_report_md_path.write_text(report_md_text, encoding="utf-8")

    return {
        "run_e2e_result_json": str(result_json_path),
        "run_e2e_report_md": str(report_md_path),
        "latest_e2e_result_json": str(latest_result_json_path),
        "latest_e2e_report_md": str(latest_report_md_path),
    }
