from __future__ import annotations

from pathlib import Path

import pytest

from app.modules.real_question_eval import (
    EXTERNAL_EVAL_SAMPLE_DATASET_PATH,
    RealQuestionEvalConfig,
    RealQuestionEvalRunner,
    SUPPORTED_EXTERNAL_EVAL_SOURCE_SCOPE_TYPES,
    SUPPORTED_EXTERNAL_EVAL_TEST_TYPES,
    load_external_eval_dataset,
)


def test_sample_external_eval_dataset_exists_and_loads():
    assert EXTERNAL_EVAL_SAMPLE_DATASET_PATH.exists()

    dataset = load_external_eval_dataset(EXTERNAL_EVAL_SAMPLE_DATASET_PATH)

    assert dataset.dataset_id == "eternal-world-external-eval-sample"
    assert len(dataset.cases) == 5
    assert dataset.metadata["external_dataset"] is True
    assert dataset.metadata["supported_test_types"] == list(SUPPORTED_EXTERNAL_EVAL_TEST_TYPES)
    assert dataset.metadata["supported_source_scope_types"] == list(SUPPORTED_EXTERNAL_EVAL_SOURCE_SCOPE_TYPES)
    assert dataset.metadata["external_dataset_path"] == str(EXTERNAL_EVAL_SAMPLE_DATASET_PATH.resolve())


def test_external_eval_dataset_required_evidence_aliases_parse_correctly():
    dataset = load_external_eval_dataset(EXTERNAL_EVAL_SAMPLE_DATASET_PATH)
    short_fact_case = next(case for case in dataset.cases if case.case_id == "short-fact-sunflower-house")

    assert short_fact_case.required_evidence[0].marker == "sunflower seeds"
    assert short_fact_case.required_evidence[0].aliases == [
        "paper envelope of sunflower seeds",
        "sunflower seed envelope",
    ]


def test_external_eval_dataset_forbidden_evidence_parses_correctly():
    dataset = load_external_eval_dataset(EXTERNAL_EVAL_SAMPLE_DATASET_PATH)
    distractor_case = next(case for case in dataset.cases if case.case_id == "distractor-grandmother-soup")

    assert distractor_case.forbidden_evidence[0].marker == "vanilla jam"
    assert distractor_case.forbidden_evidence[0].aliases == ["jam for beach travelers"]


def test_external_eval_dataset_page_level_fields_parse_correctly():
    dataset = load_external_eval_dataset(EXTERNAL_EVAL_SAMPLE_DATASET_PATH)
    page_case = next(case for case in dataset.cases if case.case_id == "page-level-gate-latch")

    assert page_case.test_type == "page_level"
    assert page_case.source_scope["scope_type"] == "page"
    assert page_case.source_scope["document_ids"] == ["village-house-archive"]
    assert page_case.source_scope["page_numbers"] == [2]
    assert page_case.source_scope["section_ids"] == ["gate-section"]


def test_external_eval_dataset_multi_document_scope_parses_correctly():
    dataset = load_external_eval_dataset(EXTERNAL_EVAL_SAMPLE_DATASET_PATH)
    multi_document_case = next(case for case in dataset.cases if case.case_id == "multi-document-winter-trip")

    assert multi_document_case.test_type == "multi_document"
    assert multi_document_case.source_scope["scope_type"] == "multi_document"
    assert multi_document_case.source_scope["document_ids"] == [
        "winter-ticket-archive",
        "winter-thermos-archive",
    ]


def test_external_eval_dataset_negative_case_parses_correctly():
    dataset = load_external_eval_dataset(EXTERNAL_EVAL_SAMPLE_DATASET_PATH)
    negative_case = next(case for case in dataset.cases if case.case_id == "negative-missing-compass")

    assert negative_case.test_type == "negative"
    assert negative_case.expected_behavior == "lack_of_evidence"
    assert negative_case.required_evidence == []
    assert negative_case.forbidden_evidence[0].marker == "invented serial number"


def test_external_eval_dataset_distractor_case_parses_correctly():
    dataset = load_external_eval_dataset(EXTERNAL_EVAL_SAMPLE_DATASET_PATH)
    distractor_case = next(case for case in dataset.cases if case.case_id == "distractor-grandmother-soup")

    assert distractor_case.test_type == "distractor"
    assert distractor_case.expected_long_context is True
    assert distractor_case.minimum_context_chars == 60
    assert distractor_case.minimum_coverage == 1.0


def test_external_eval_dataset_loader_rejects_invalid_dataset_with_clear_error(tmp_path):
    invalid_dataset_path = tmp_path / "invalid_eval_dataset.json"
    invalid_dataset_path.write_text(
        """
{
  "dataset_id": "invalid-external-dataset",
  "name": "Invalid External Dataset",
  "cases": [
    {
      "id": "bad-case",
      "question": "What is wrong here?",
      "expected_answer_type": "short_fact",
      "test_type": "not_supported",
      "source_scope": {
        "scope_type": "page",
        "document_ids": []
      },
      "required_evidence": [],
      "forbidden_evidence": [],
      "minimum_coverage": 1.0,
      "allow_partial": false,
      "expected_citation_count_min": 1,
      "difficulty": "easy",
      "language": "en",
      "expected_long_context": false,
      "minimum_context_chars": 0
    }
  ]
}
""".strip(),
        encoding="utf-8",
    )

    with pytest.raises(ValueError) as exc_info:
        load_external_eval_dataset(invalid_dataset_path)

    error_message = str(exc_info.value)
    assert "External eval dataset validation failed:" in error_message
    assert "cases.0.test_type" in error_message or "cases.0.source_scope" in error_message


def test_real_question_eval_runner_build_request_can_use_external_dataset_path():
    runner = RealQuestionEvalRunner(
        db=None,
        config=RealQuestionEvalConfig(dataset_path=EXTERNAL_EVAL_SAMPLE_DATASET_PATH),
    )

    request = runner.build_request()

    assert request.dataset.dataset_id == "eternal-world-external-eval-sample"
    assert len(request.dataset.cases) == 5
    assert request.dataset.metadata["external_dataset"] is True
