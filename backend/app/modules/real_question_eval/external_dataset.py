from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator

from app.modules.rag_quality.schemas import RagQualityEvalCase, RagQualityEvalDataset


SUPPORTED_EXTERNAL_EVAL_TEST_TYPES = (
    "short_fact",
    "page_level",
    "multi_document",
    "negative",
    "distractor",
)
SUPPORTED_EXTERNAL_EVAL_SOURCE_SCOPE_TYPES = (
    "document",
    "page",
    "multi_document",
    "collection",
)


class ExternalEvalDatasetError(ValueError):
    pass


class ExternalEvalSourceScope(BaseModel):
    scope_type: Literal["document", "page", "multi_document", "collection"]
    document_ids: list[str] = Field(default_factory=list)
    page_numbers: list[int] = Field(default_factory=list)
    section_ids: list[str] = Field(default_factory=list)
    notes: str | None = Field(default=None, max_length=500)

    @field_validator("document_ids", "section_ids")
    @classmethod
    def normalize_string_lists(cls, value: list[str]) -> list[str]:
        normalized_items: list[str] = []
        seen: set[str] = set()
        for item in value:
            normalized_item = " ".join(item.split())
            if not normalized_item:
                continue
            normalized_key = normalized_item.lower()
            if normalized_key in seen:
                continue
            seen.add(normalized_key)
            normalized_items.append(normalized_item)
        return normalized_items

    @field_validator("page_numbers")
    @classmethod
    def validate_page_numbers(cls, value: list[int]) -> list[int]:
        for item in value:
            if item <= 0:
                raise ValueError("page_numbers must contain only positive integers")
        return value

    @field_validator("notes")
    @classmethod
    def normalize_notes(cls, value: str | None) -> str | None:
        if value is None:
            return None
        normalized_value = " ".join(value.split())
        return normalized_value or None

    @model_validator(mode="after")
    def validate_scope_shape(self) -> "ExternalEvalSourceScope":
        if self.scope_type == "document" and not self.document_ids:
            raise ValueError("document scope requires at least one document_ids entry")
        if self.scope_type == "page":
            if not self.document_ids:
                raise ValueError("page scope requires at least one document_ids entry")
            if not self.page_numbers:
                raise ValueError("page scope requires at least one page_numbers entry")
        if self.scope_type == "multi_document" and len(self.document_ids) < 2:
            raise ValueError("multi_document scope requires at least two document_ids entries")
        return self


class ExternalEvalEvidenceRule(BaseModel):
    marker: str = Field(min_length=1, max_length=500)
    aliases: list[str] = Field(default_factory=list)

    @field_validator("marker")
    @classmethod
    def normalize_marker(cls, value: str) -> str:
        normalized_value = " ".join(value.split())
        if not normalized_value:
            raise ValueError("marker must not be empty")
        return normalized_value

    @field_validator("aliases")
    @classmethod
    def normalize_aliases(cls, value: list[str]) -> list[str]:
        normalized_items: list[str] = []
        seen: set[str] = set()
        for item in value:
            normalized_item = " ".join(item.split())
            if not normalized_item:
                continue
            normalized_key = normalized_item.lower()
            if normalized_key in seen:
                continue
            seen.add(normalized_key)
            normalized_items.append(normalized_item)
        return normalized_items


class ExternalEvalSourceDocument(BaseModel):
    document_id: str = Field(min_length=1, max_length=120)
    page_number: int | None = Field(default=None, ge=1)
    section_id: str | None = Field(default=None, max_length=120)
    content: str = Field(min_length=1, max_length=5000)

    @field_validator("document_id", "section_id", "content")
    @classmethod
    def normalize_text(cls, value: str | None) -> str | None:
        if value is None:
            return None
        normalized_value = " ".join(value.split())
        return normalized_value or None


class ExternalEvalDatasetCase(BaseModel):
    id: str = Field(min_length=1, max_length=120)
    question: str = Field(min_length=1, max_length=5000)
    expected_answer_type: str = Field(min_length=1, max_length=120)
    test_type: Literal["short_fact", "page_level", "multi_document", "negative", "distractor"]
    source_scope: ExternalEvalSourceScope
    required_evidence: list[ExternalEvalEvidenceRule] = Field(default_factory=list)
    forbidden_evidence: list[ExternalEvalEvidenceRule] = Field(default_factory=list)
    minimum_coverage: float = Field(default=1.0, ge=0, le=1)
    allow_partial: bool = False
    expected_citation_count_min: int = Field(default=0, ge=0)
    difficulty: str = Field(min_length=1, max_length=64)
    language: str = Field(min_length=1, max_length=32)
    expected_long_context: bool = False
    minimum_context_chars: int = Field(default=0, ge=0)

    @field_validator("id", "question", "expected_answer_type", "difficulty", "language")
    @classmethod
    def normalize_required_text(cls, value: str) -> str:
        normalized_value = " ".join(value.split())
        if not normalized_value:
            raise ValueError("Field must not be empty")
        return normalized_value

    @model_validator(mode="after")
    def validate_case_semantics(self) -> "ExternalEvalDatasetCase":
        if self.test_type == "negative" and self.required_evidence:
            raise ValueError("negative test_type must not define required_evidence")
        if self.test_type != "negative" and not self.required_evidence:
            raise ValueError(f"{self.test_type} test_type requires at least one required_evidence entry")
        return self

    def to_rag_quality_case(self) -> RagQualityEvalCase:
        expected_behavior = (
            "lack_of_evidence"
            if self.test_type == "negative"
            else "partial_answer_with_uncertainty"
            if self.allow_partial
            else "retrieval_only"
        )
        return RagQualityEvalCase(
            case_id=self.id,
            title=self.id.replace("-", " ").strip(),
            query=self.question,
            expected_markers=[item.marker for item in self.required_evidence],
            forbidden_markers=[item.marker for item in self.forbidden_evidence],
            required_evidence=[
                RagQualityEvalCase.EvidenceRule(marker=item.marker, aliases=list(item.aliases))
                for item in self.required_evidence
            ],
            forbidden_evidence=[
                RagQualityEvalCase.EvidenceRule(marker=item.marker, aliases=list(item.aliases))
                for item in self.forbidden_evidence
            ],
            expected_behavior=expected_behavior,
            minimum_relevant_results=self.expected_citation_count_min,
            expected_answer_type=self.expected_answer_type,
            test_type=self.test_type,
            source_scope=self.source_scope.model_dump(mode="json"),
            minimum_coverage=self.minimum_coverage,
            allow_partial=self.allow_partial,
            expected_citation_count_min=self.expected_citation_count_min,
            difficulty=self.difficulty,
            language=self.language,
            expected_long_context=self.expected_long_context,
            minimum_context_chars=self.minimum_context_chars,
            tags=[self.test_type, self.language],
            metadata={
                "external_dataset_case": True,
                "supported_test_types": list(SUPPORTED_EXTERNAL_EVAL_TEST_TYPES),
            },
        )


class ExternalEvalDataset(BaseModel):
    dataset_id: str = Field(min_length=1, max_length=120)
    name: str = Field(min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=2000)
    project_name: str | None = Field(default=None, max_length=120)
    cases: list[ExternalEvalDatasetCase] = Field(min_length=1)
    source_documents: list[ExternalEvalSourceDocument] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("dataset_id", "name", "description", "project_name")
    @classmethod
    def normalize_text(cls, value: str | None) -> str | None:
        if value is None:
            return None
        normalized_value = " ".join(value.split())
        return normalized_value or None

    def to_rag_quality_dataset(self) -> RagQualityEvalDataset:
        source_documents = self.resolve_source_documents()
        return RagQualityEvalDataset(
            dataset_id=self.dataset_id,
            name=self.name,
            description=self.description,
            project_name=self.project_name,
            cases=[case.to_rag_quality_case() for case in self.cases],
            metadata={
                **self.metadata,
                "external_dataset": True,
                "supported_test_types": list(SUPPORTED_EXTERNAL_EVAL_TEST_TYPES),
                "supported_source_scope_types": list(SUPPORTED_EXTERNAL_EVAL_SOURCE_SCOPE_TYPES),
                "source_documents": [item.model_dump(mode="json") for item in source_documents],
                "source_document_count": len(source_documents),
                "source_document_mode": "explicit" if self.source_documents else "synthesized",
            },
        )

    def resolve_source_documents(self) -> list[ExternalEvalSourceDocument]:
        if self.source_documents:
            return list(self.source_documents)
        return _synthesize_source_documents(self)


def _build_source_locator(
    *,
    document_id: str,
    page_number: int | None,
    section_id: str | None,
) -> str:
    parts = [f"document {document_id}"]
    if page_number is not None:
        parts.append(f"page {page_number}")
    if section_id is not None:
        parts.append(f"section {section_id}")
    return ", ".join(parts)


def _build_positive_source_content(
    *,
    case: ExternalEvalDatasetCase,
    document_id: str,
    page_number: int | None,
    section_id: str | None,
    evidence_rules: list[ExternalEvalEvidenceRule],
) -> str:
    locator = _build_source_locator(
        document_id=document_id,
        page_number=page_number,
        section_id=section_id,
    )
    evidence_phrases = ", ".join(rule.marker for rule in evidence_rules)
    return " ".join(
        [
            f"In {locator}, the verified archive note records {evidence_phrases}.",
            f"The validation question tied to this source asks: {case.question}",
            f"Canonical source scope reminder: {locator}; verified evidence: {evidence_phrases}.",
        ]
    )


def _build_forbidden_source_content(
    *,
    case: ExternalEvalDatasetCase,
    document_id: str,
    page_number: int | None,
    section_id: str | None,
    evidence_rules: list[ExternalEvalEvidenceRule],
) -> str:
    locator = _build_source_locator(
        document_id=document_id,
        page_number=page_number,
        section_id=section_id,
    )
    evidence_phrases = ", ".join(rule.marker for rule in evidence_rules)
    return " ".join(
        [
            f"A conflicting note in {locator} mentions {evidence_phrases} as a misleading archival rumor.",
            f"The same {locator} rumor is marked as different from the verified record for this source scope.",
            f"Conflict marker only: {evidence_phrases} remains archival noise rather than verified evidence.",
        ]
    )


def _append_document_content(
    documents: dict[tuple[str, int | None, str | None], list[str]],
    *,
    document_id: str,
    page_number: int | None,
    section_id: str | None,
    content: str,
) -> None:
    documents.setdefault((document_id, page_number, section_id), []).append(content)


def _synthesize_source_documents(dataset: ExternalEvalDataset) -> list[ExternalEvalSourceDocument]:
    documents: dict[tuple[str, int | None, str | None], list[str]] = {}

    for case in dataset.cases:
        source_scope = case.source_scope
        document_ids = list(source_scope.document_ids)
        page_number = source_scope.page_numbers[0] if source_scope.page_numbers else None
        section_id = source_scope.section_ids[0] if source_scope.section_ids else None

        if case.test_type == "negative":
            continue

        if not document_ids:
            document_ids = [f"{dataset.dataset_id}-{case.id}"]

        if case.test_type == "multi_document" and len(document_ids) >= 2:
            distributed_documents = document_ids[:]
            for index, evidence_rule in enumerate(case.required_evidence):
                original_document_id = distributed_documents[min(index, len(distributed_documents) - 1)]
                target_document_id = f"{original_document_id}::{case.id}::{index + 1}"
                _append_document_content(
                    documents,
                    document_id=target_document_id,
                    page_number=None,
                    section_id=None,
                    content=_build_positive_source_content(
                        case=case,
                        document_id=original_document_id,
                        page_number=None,
                        section_id=None,
                        evidence_rules=[evidence_rule],
                    ),
                )
        else:
            original_document_id = document_ids[0]
            target_document_id = f"{original_document_id}::{case.id}"
            _append_document_content(
                documents,
                document_id=target_document_id,
                page_number=page_number,
                section_id=section_id,
                content=_build_positive_source_content(
                    case=case,
                    document_id=original_document_id,
                    page_number=page_number,
                    section_id=section_id,
                    evidence_rules=list(case.required_evidence),
                ),
            )

        if case.forbidden_evidence:
            original_document_id = document_ids[0] if document_ids else f"{dataset.dataset_id}-{case.id}"
            distractor_document_id = (
                f"{original_document_id}::{case.id}::distractor"
                if document_ids
                else f"{dataset.dataset_id}-{case.id}::distractor"
            )
            _append_document_content(
                documents,
                document_id=distractor_document_id,
                page_number=page_number,
                section_id=section_id,
                content=_build_forbidden_source_content(
                    case=case,
                    document_id=original_document_id,
                    page_number=page_number,
                    section_id=section_id,
                    evidence_rules=list(case.forbidden_evidence),
                ),
            )

    ordered_documents = sorted(
        documents.items(),
        key=lambda item: ("::distractor" in item[0][0], item[0][0], item[0][1] or 0, item[0][2] or ""),
    )
    return [
        ExternalEvalSourceDocument(
            document_id=document_id,
            page_number=page_number,
            section_id=section_id,
            content=" ".join(parts),
        )
        for (document_id, page_number, section_id), parts in ordered_documents
    ]


def build_external_eval_source_text(source_documents: list[dict[str, Any]] | list[ExternalEvalSourceDocument]) -> str:
    normalized_documents: list[ExternalEvalSourceDocument] = []
    for item in source_documents:
        if isinstance(item, ExternalEvalSourceDocument):
            normalized_documents.append(item)
            continue
        if isinstance(item, dict):
            normalized_documents.append(ExternalEvalSourceDocument.model_validate(item))

    if not normalized_documents:
        return (
            "Validation archive placeholder. This corpus intentionally contains no matching evidence for the "
            "requested question set."
        )

    blocks: list[str] = []
    for document in normalized_documents:
        locator = _build_source_locator(
            document_id=document.document_id,
            page_number=document.page_number,
            section_id=document.section_id,
        )
        blocks.append(f"{locator}: {document.content}")
    return "\n\n".join(blocks)


def load_external_eval_dataset(dataset_path: str | Path) -> RagQualityEvalDataset:
    resolved_path = Path(dataset_path).expanduser().resolve()
    if not resolved_path.exists():
        raise ExternalEvalDatasetError(f"External eval dataset file not found: {resolved_path}")
    if resolved_path.suffix.lower() != ".json":
        raise ExternalEvalDatasetError(
            f"Unsupported external eval dataset format for {resolved_path.name}. Only JSON is supported."
        )

    try:
        payload = json.loads(resolved_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ExternalEvalDatasetError(
            f"External eval dataset JSON is invalid at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc

    try:
        dataset = ExternalEvalDataset.model_validate(payload)
    except ValidationError as exc:
        raise ExternalEvalDatasetError(
            "External eval dataset validation failed: "
            + "; ".join(
                f"{'.'.join(str(part) for part in error['loc'])}: {error['msg']}"
                for error in exc.errors()
            )
        ) from exc

    rag_quality_dataset = dataset.to_rag_quality_dataset()
    rag_quality_dataset.metadata["external_dataset_path"] = str(resolved_path)
    return rag_quality_dataset
