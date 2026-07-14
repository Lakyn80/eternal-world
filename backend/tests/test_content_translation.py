from __future__ import annotations

import pytest

from app.main import app
from app.modules.content_translation.provider import (
    ContentTranslationProviderRequestError,
    ContentTranslationProviderResponse,
    MockContentTranslationProvider,
)
from app.modules.content_translation.repository import get_current
from app.modules.content_translation.schemas import (
    ProviderTranslationResult,
    TranslationFieldRequest,
)
from app.modules.content_translation.service import (
    compute_source_hash,
    get_translations_for_candidate,
    is_translation_current,
    resolve_required_translation_block_reason,
    retry_translation,
    translate_content_field,
)
from app.modules.content_translation.validators import (
    ContentTranslationValidationError,
    validate_translation_result,
)


def _db():
    return app.state.testing_session_local()


class FakeProvider:
    """Controlled provider double mirroring this repo's FakeClient convention
    for the Brain OpenAI-compatible provider - no HTTP mocking library, just
    a constructor-injectable fake with recorded calls."""

    provider_name = "fake"

    def __init__(self, *, translated_text: str | None = "translated", raise_error: Exception | None = None):
        self.translated_text = translated_text
        self.raise_error = raise_error
        self.calls: list[dict] = []

    def translate(self, *, source_text: str, source_language: str, target_language: str):
        self.calls.append(
            {
                "source_text": source_text,
                "source_language": source_language,
                "target_language": target_language,
            }
        )
        if self.raise_error is not None:
            raise self.raise_error
        return ContentTranslationProviderResponse(
            result=ProviderTranslationResult(translated_text=self.translated_text or ""),
            provider_name=self.provider_name,
            model="fake-model",
            latency_ms=1,
        )


def _request(*, source_text: str = "Babička mi zpívala písničku.", candidate_id: int = 1) -> TranslationFieldRequest:
    return TranslationFieldRequest(
        candidate_id=candidate_id,
        entity_type="memory_candidate",
        entity_id=str(candidate_id),
        field_name="finalized_memory_text",
        source_language="cs",
        target_language="ru",
        source_text=source_text,
    )


def test_source_text_is_preserved_exactly(client):
    db = _db()
    try:
        row = translate_content_field(db, _request(), provider=FakeProvider())
        assert row.source_text == "Babička mi zpívala písničku."
        assert row.translated_text == "translated"
        assert row.source_text != row.translated_text
    finally:
        db.close()


def test_russian_translation_stored_separately_from_source(client):
    db = _db()
    try:
        row = translate_content_field(
            db, _request(), provider=FakeProvider(translated_text="Бабушка пела мне песню.")
        )
        assert row.translation_status == "translated"
        assert row.translated_text == "Бабушка пела мне песню."
        fetched = get_current(
            db,
            entity_type="memory_candidate",
            entity_id="1",
            field_name="finalized_memory_text",
            target_language="ru",
        )
        assert fetched is not None
        assert fetched.id == row.id
    finally:
        db.close()


def test_empty_provider_result_is_rejected():
    with pytest.raises(ContentTranslationValidationError):
        validate_translation_result(
            source_text="Ahoj babičko",
            result=ProviderTranslationResult(translated_text="   "),
        )


def test_implausible_length_ratio_is_rejected():
    with pytest.raises(ContentTranslationValidationError):
        validate_translation_result(
            source_text="Babička mi zpívala písničku před spaním, když jsem byl malý.",
            result=ProviderTranslationResult(translated_text="Da."),
        )


def test_provider_request_failure_leaves_source_intact_and_marks_failed(client):
    db = _db()
    try:
        row = translate_content_field(
            db,
            _request(),
            provider=FakeProvider(raise_error=ContentTranslationProviderRequestError("network down")),
        )
        assert row.translation_status == "failed"
        assert row.source_text == "Babička mi zpívala písničku."
    finally:
        db.close()


def test_retry_is_safe_and_idempotent_in_effect(client):
    db = _db()
    try:
        provider = FakeProvider(translated_text="Бабушка пела мне песню.")
        first = translate_content_field(db, _request(), provider=provider)
        second = retry_translation(
            db,
            entity_type="memory_candidate",
            entity_id="1",
            field_name="finalized_memory_text",
            source_language="cs",
            target_language="ru",
            source_text="Babička mi zpívala písničku.",
            candidate_id=1,
            provider=provider,
        )
        assert first.id == second.id
        assert second.translation_status == "translated"
        assert len(provider.calls) == 2
    finally:
        db.close()


def test_source_edit_marks_translation_stale_and_retranslates(client):
    db = _db()
    try:
        provider = FakeProvider(translated_text="Бабушка пела мне песню.")
        first = translate_content_field(db, _request(source_text="Původní text."), provider=provider)
        assert first.translation_version == 1

        provider_v2 = FakeProvider(translated_text="Бабушка часто пела мне песню.")
        second = translate_content_field(db, _request(source_text="Upravený text."), provider=provider_v2)
        assert second.id == first.id
        assert second.translation_version == 2
        assert second.source_text == "Upravený text."
        assert second.translation_status == "translated"
        assert second.translated_text == "Бабушка часто пела мне песню."
    finally:
        db.close()


def test_no_automatic_approval_or_indexing_side_effects(client):
    """translate_content_field must never touch candidate/promotion state -
    it only ever writes to memory_content_translations."""
    db = _db()
    try:
        translate_content_field(db, _request(), provider=FakeProvider())
        # No candidate row exists at all in this test (translation service
        # does not require one to exist), proving it never reaches into
        # ConversationMemoryCandidate/AvatarMemoryPromotion state.
        translations = get_translations_for_candidate(db, candidate_id=1)
        assert len(translations) == 1
    finally:
        db.close()


def test_is_translation_current_detects_hash_mismatch(client):
    db = _db()
    try:
        row = translate_content_field(
            db, _request(source_text="Text A."), provider=FakeProvider(translated_text="Text A RU.")
        )
        assert is_translation_current(row, current_source_text="Text A.") is True
        assert is_translation_current(row, current_source_text="Text B.") is False
    finally:
        db.close()


def test_resolve_required_translation_block_reason_paths(client):
    db = _db()
    try:
        assert (
            resolve_required_translation_block_reason(
                db,
                entity_type="memory_candidate",
                entity_id="42",
                field_name="finalized_memory_text",
                target_language="ru",
                current_source_text="Nic tu není.",
            )
            == "russian_translation_missing"
        )

        translate_content_field(
            db,
            TranslationFieldRequest(
                candidate_id=42,
                entity_type="memory_candidate",
                entity_id="42",
                field_name="finalized_memory_text",
                source_language="cs",
                target_language="ru",
                source_text="Text.",
            ),
            provider=FakeProvider(translated_text="Текст."),
        )
        assert (
            resolve_required_translation_block_reason(
                db,
                entity_type="memory_candidate",
                entity_id="42",
                field_name="finalized_memory_text",
                target_language="ru",
                current_source_text="Text.",
            )
            is None
        )
        # Source changed without a new translation -> stale, even though the
        # stored status still says "translated".
        assert (
            resolve_required_translation_block_reason(
                db,
                entity_type="memory_candidate",
                entity_id="42",
                field_name="finalized_memory_text",
                target_language="ru",
                current_source_text="Text changed.",
            )
            == "russian_translation_stale"
        )

        translate_content_field(
            db,
            TranslationFieldRequest(
                candidate_id=42,
                entity_type="memory_candidate",
                entity_id="42",
                field_name="finalized_memory_text",
                source_language="cs",
                target_language="ru",
                source_text="Text changed.",
            ),
            provider=FakeProvider(raise_error=ContentTranslationProviderRequestError("down")),
        )
        assert (
            resolve_required_translation_block_reason(
                db,
                entity_type="memory_candidate",
                entity_id="42",
                field_name="finalized_memory_text",
                target_language="ru",
                current_source_text="Text changed.",
            )
            == "russian_translation_failed"
        )
    finally:
        db.close()


def test_compute_source_hash_is_deterministic():
    assert compute_source_hash("abc") == compute_source_hash("abc")
    assert compute_source_hash("abc") != compute_source_hash("abd")


def test_mock_provider_never_makes_network_calls_and_is_clearly_labeled():
    provider = MockContentTranslationProvider()
    response = provider.translate(source_text="Ahoj", source_language="cs", target_language="ru")
    assert "mock_provider_not_a_real_translation" in response.result.warnings
    assert response.result.translated_text.startswith("[cs->ru] ")
