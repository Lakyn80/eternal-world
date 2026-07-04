from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from rag_eval.adapters.base import RagEvalBackend, RagEvalChunk
from rag_eval.datasets.loader import ExternalEvalDataset, ExternalEvalSourceDocument, load_external_eval_dataset
from rag_eval.metrics.metrics import marker_present


@dataclass
class PreflightIssue:
    question_id: str
    issue_code: str
    detail: str
    marker: str | None = None


@dataclass
class PreflightValidation:
    passed: bool
    issue_count: int
    issues: list[PreflightIssue] = field(default_factory=list)


def _matches_source_scope(document: ExternalEvalSourceDocument, *, source_scope: dict[str, Any]) -> bool:
    scope_type = source_scope.get("scope_type")
    document_ids = [str(item) for item in source_scope.get("document_ids") or []]
    page_numbers = [int(item) for item in source_scope.get("page_numbers") or []]
    section_ids = [str(item) for item in source_scope.get("section_ids") or []]

    if scope_type == "collection":
        return True
    if document_ids and not any(document.document_id.startswith(document_id) for document_id in document_ids):
        return False
    if scope_type == "page" and page_numbers and document.page_number not in page_numbers:
        return False
    if section_ids and document.section_id not in section_ids:
        return False
    return True


def validate_dataset_schema(dataset_path: Path) -> ExternalEvalDataset:
    load_external_eval_dataset(dataset_path)
    payload = json.loads(dataset_path.read_text(encoding="utf-8"))
    dataset = ExternalEvalDataset.model_validate(payload)
    if not dataset.cases:
        raise ValueError("Dataset must contain at least one case.")
    return dataset


def validate_dataset_against_chunks(
    *,
    dataset: ExternalEvalDataset,
    source_chunks: list[RagEvalChunk],
) -> PreflightValidation:
    source_documents = dataset.resolve_source_documents()
    chunk_texts_by_document_id: dict[str, list[str]] = defaultdict(list)
    for chunk in source_chunks:
        source_document_id = chunk.chunk_metadata.get("source_document_id")
        if source_document_id is not None:
            chunk_texts_by_document_id[str(source_document_id)].append(chunk.chunk_text)

    issues: list[PreflightIssue] = []
    rag_quality_dataset = dataset.to_rag_quality_dataset()

    for case in rag_quality_dataset.cases:
        source_scope = case.source_scope or {}
        scoped_documents = [
            document for document in source_documents if _matches_source_scope(document, source_scope=source_scope)
        ]
        scoped_document_text = " ".join(document.content for document in scoped_documents)
        scoped_chunk_text = " ".join(
            " ".join(chunk_texts_by_document_id.get(document.document_id, []))
            for document in scoped_documents
            if document.document_id in chunk_texts_by_document_id
        )

        required_rules = case.required_evidence
        forbidden_rules = case.forbidden_evidence

        if required_rules and not scoped_chunk_text.strip():
            issues.append(
                PreflightIssue(
                    question_id=case.case_id,
                    issue_code="missing_scoped_source_chunks",
                    detail="No scoped source chunks were materialized for a case that requires evidence.",
                )
            )

        if case.test_type == "page_level" and len(scoped_document_text) < int(case.minimum_context_chars or 0):
            issues.append(
                PreflightIssue(
                    question_id=case.case_id,
                    issue_code="page_context_too_short",
                    detail=(
                        f"Scoped source text has {len(scoped_document_text)} chars but requires "
                        f"{int(case.minimum_context_chars or 0)}."
                    ),
                )
            )

        if case.test_type == "multi_document":
            matched_base_documents = {
                document_id
                for document_id in source_scope.get("document_ids") or []
                if any(document.document_id.startswith(str(document_id)) for document in scoped_documents)
            }
            if len(matched_base_documents) < 2:
                issues.append(
                    PreflightIssue(
                        question_id=case.case_id,
                        issue_code="multi_document_scope_incomplete",
                        detail=(
                            f"Expected at least 2 source documents but found {len(matched_base_documents)} "
                            f"for scope {list(source_scope.get('document_ids') or [])}."
                        ),
                    )
                )

        if case.expected_behavior == "lack_of_evidence" and case.required_evidence:
            issues.append(
                PreflightIssue(
                    question_id=case.case_id,
                    issue_code="negative_case_has_required_evidence",
                    detail="Negative cases must not define required_evidence.",
                )
            )

        for evidence_rule in required_rules:
            candidates = [evidence_rule.marker, *evidence_rule.aliases]
            if not any(marker_present(scoped_document_text, candidate) for candidate in candidates):
                issues.append(
                    PreflightIssue(
                        question_id=case.case_id,
                        issue_code="missing_required_marker_in_source_documents",
                        marker=evidence_rule.marker,
                        detail=(
                            f"Required evidence marker '{evidence_rule.marker}' is missing from scoped source documents."
                        ),
                    )
                )
            if scoped_chunk_text.strip() and not any(
                marker_present(scoped_chunk_text, candidate) for candidate in candidates
            ):
                issues.append(
                    PreflightIssue(
                        question_id=case.case_id,
                        issue_code="missing_required_marker_in_source_chunks",
                        marker=evidence_rule.marker,
                        detail=(
                            f"Required evidence marker '{evidence_rule.marker}' is missing from scoped source chunks."
                        ),
                    )
                )

        if case.test_type == "distractor":
            for evidence_rule in forbidden_rules:
                candidates = [evidence_rule.marker, *evidence_rule.aliases]
                if not any(marker_present(scoped_document_text, candidate) for candidate in candidates):
                    issues.append(
                        PreflightIssue(
                            question_id=case.case_id,
                            issue_code="missing_forbidden_distractor_marker",
                            marker=evidence_rule.marker,
                            detail=(
                                f"Distractor evidence marker '{evidence_rule.marker}' is missing from the scoped source corpus."
                            ),
                        )
                    )

    return PreflightValidation(
        passed=not issues,
        issue_count=len(issues),
        issues=issues,
    )


def build_collection_name(*, collection_prefix: str, model_code: str, dataset: ExternalEvalDataset) -> str:
    dataset_slug = re.sub(r"[^a-z0-9]+", "_", dataset.dataset_id.lower()).strip("_") or "external_dataset"
    dataset_slug = dataset_slug[:40]
    from hashlib import sha1

    from rag_eval.datasets.loader import build_external_eval_source_text

    source_signature = sha1(
        build_external_eval_source_text(dataset.resolve_source_documents()).encode("utf-8")
    ).hexdigest()[:10]
    return f"{collection_prefix}__{model_code}__rag_eval__{dataset_slug}__{source_signature}"[:200]
