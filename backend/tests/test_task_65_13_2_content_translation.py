"""Task 65.13.2 - generalize content translation domain (Decision B)."""

from __future__ import annotations

import pytest

from app.main import app
from app.modules.content_translation.jobs import (
    CONTENT_TRANSLATION_TASK_NAME,
    enqueue_content_translation_job,
    process_content_translation_job,
)
from app.modules.content_translation.provider import ContentTranslationProviderResponse
from app.modules.content_translation.repository import get_current
from app.modules.content_translation.schemas import (
    ProviderTranslationResult,
    TranslationFieldRequest,
)
from app.modules.content_translation.service import (
    apply_human_translation_override,
    mark_translation_human_reviewed,
    translate_content_field,
)
from app.modules.job_tracking.enums import BackgroundJobType
from app.modules.language_registry import assert_translation_language, translation_languages
from app.modules.memorial_access.service import MemorialForbiddenError, MemorialNotFoundError
from app.modules.provider_usage.context import development_test_context
from app.worker.celery_app import AI_GENERATION_QUEUE


PASSWORD = "StrongPass123"


def _db():
    return app.state.testing_session_local()


def _ctx():
    return development_test_context(trace_id="test-task-65-13-2")


class FakeProvider:
    provider_name = "fake"

    def __init__(self, *, translated_text: str = "translated"):
        self.translated_text = translated_text
        self.calls: list[dict] = []
        self.model = "fake-model"

    def translate(self, *, source_text: str, source_language: str, target_language: str):
        self.calls.append(
            {
                "source_text": source_text,
                "source_language": source_language,
                "target_language": target_language,
            }
        )
        return ContentTranslationProviderResponse(
            result=ProviderTranslationResult(translated_text=self.translated_text),
            provider_name=self.provider_name,
            model=self.model,
            latency_ms=1,
        )


def _register_and_login(client, email: str) -> str:
    client.post(
        "/api/auth/register",
        json={"email": email, "password": PASSWORD, "full_name": email.split("@")[0]},
    )
    response = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    assert response.status_code == 200
    return response.json()["access_token"]


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _create_memorial(client, token: str, *, name: str = "Marie") -> int:
    created = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={
            "name": name,
            "canonical_language": "cs",
            "confirm_canonical_language": True,
        },
    )
    assert created.status_code == 201
    return int(created.json()["id"])


def _request(
    *,
    profile_id: int | None = None,
    source_language: str = "cs",
    target_language: str = "ru",
    source_text: str = "Babička mi zpívala písničku.",
    entity_id: str = "42",
) -> TranslationFieldRequest:
    return TranslationFieldRequest(
        profile_id=profile_id,
        candidate_id=None,
        entity_type="fa_chat_turn",
        entity_id=entity_id,
        field_name="message_text",
        source_language=source_language,
        target_language=target_language,
        source_text=source_text,
    )


def test_translation_languages_include_de_via_registry():
    assert "de" in translation_languages()
    assert assert_translation_language("de") == "de"
    assert assert_translation_language("DE-de") == "de"
    with pytest.raises(ValueError):
        assert_translation_language("fr")


def test_same_language_skips_provider(client):
    db = _db()
    provider = FakeProvider()
    try:
        row = translate_content_field(
            db,
            _request(source_language="cs", target_language="cs", entity_id="same-lang-1"),
            call_context=_ctx(),
            provider=provider,
        )
        assert row.translation_status == "translated"
        assert row.translated_text == "Babička mi zpívala písničku."
        assert row.translation_provider == "identity"
        assert provider.calls == []
    finally:
        db.close()


def test_german_target_language_is_persisted(client):
    db = _db()
    provider = FakeProvider(translated_text="Oma hat mir ein Lied gesungen.")
    try:
        row = translate_content_field(
            db,
            _request(target_language="de", entity_id="de-target-1"),
            call_context=_ctx(),
            provider=provider,
        )
        assert row.target_language == "de"
        assert row.translation_status == "translated"
        assert row.translated_text == "Oma hat mir ein Lied gesungen."
        assert row.profile_id is None
        fetched = get_current(
            db,
            entity_type="fa_chat_turn",
            entity_id="de-target-1",
            field_name="message_text",
            target_language="de",
        )
        assert fetched is not None
        assert fetched.id == row.id
    finally:
        db.close()


def test_multi_target_dedup_unique_per_target(client):
    db = _db()
    provider = FakeProvider()
    try:
        first = translate_content_field(
            db,
            _request(target_language="ru", entity_id="multi-1"),
            call_context=_ctx(),
            provider=provider,
        )
        second = translate_content_field(
            db,
            _request(target_language="en", entity_id="multi-1"),
            call_context=_ctx(),
            provider=FakeProvider(translated_text="Grandma sang me a song."),
        )
        assert first.id != second.id
        assert first.target_language == "ru"
        assert second.target_language == "en"
        again = translate_content_field(
            db,
            _request(target_language="ru", entity_id="multi-1"),
            call_context=_ctx(),
            provider=FakeProvider(translated_text="again"),
        )
        assert again.id == first.id
        assert again.translated_text == "again"
    finally:
        db.close()


def test_human_override_requires_review_capability(client):
    owner_token = _register_and_login(client, "ct-owner@example.com")
    profile_id = _create_memorial(client, owner_token, name="Override Memorial")
    stranger_token = _register_and_login(client, "ct-stranger@example.com")

    db = _db()
    try:
        from app.db.models import User

        owner = db.query(User).filter(User.email == "ct-owner@example.com").one()
        stranger = db.query(User).filter(User.email == "ct-stranger@example.com").one()

        translate_content_field(
            db,
            _request(profile_id=profile_id, entity_id=f"override-{profile_id}"),
            call_context=_ctx(),
            provider=FakeProvider(translated_text="machine"),
        )
        db.commit()

        with pytest.raises((MemorialForbiddenError, MemorialNotFoundError)):
            apply_human_translation_override(
                db,
                current_user=stranger,
                profile_id=profile_id,
                entity_type="fa_chat_turn",
                entity_id=f"override-{profile_id}",
                field_name="message_text",
                target_language="ru",
                translated_text="human text",
            )

        overridden = apply_human_translation_override(
            db,
            current_user=owner,
            profile_id=profile_id,
            entity_type="fa_chat_turn",
            entity_id=f"override-{profile_id}",
            field_name="message_text",
            target_language="ru",
            translated_text="human text",
        )
        assert overridden.translation_status == "human_reviewed"
        assert overridden.translated_text == "human text"
        assert overridden.reviewed_by == f"user:{owner.id}"
        assert overridden.source_text == "Babička mi zpívala písničku."

        reviewed = mark_translation_human_reviewed(
            db,
            current_user=owner,
            profile_id=profile_id,
            entity_type="fa_chat_turn",
            entity_id=f"override-{profile_id}",
            field_name="message_text",
            target_language="ru",
        )
        assert reviewed.translation_status == "human_reviewed"
    finally:
        db.close()


def test_content_translation_job_outbox_contract(client):
    owner_token = _register_and_login(client, "ct-job@example.com")
    profile_id = _create_memorial(client, owner_token, name="Job Memorial")

    db = _db()
    published: list[dict] = []

    def fake_sender(*, task_name: str, args: list[object], queue: str) -> str:
        published.append({"task_name": task_name, "args": args, "queue": queue})
        return "fake-celery-id"

    try:
        from app.db.models import User

        owner = db.query(User).filter(User.email == "ct-job@example.com").one()
        request = _request(profile_id=profile_id, entity_id=f"job-{profile_id}", target_language="en")
        job = enqueue_content_translation_job(
            db,
            owner_user_id=owner.id,
            profile_id=profile_id,
            request=request,
            sender=fake_sender,
        )
        assert job.job_type == BackgroundJobType.CONTENT_TRANSLATION.value
        assert job.profile_id == profile_id
        assert job.queue == AI_GENERATION_QUEUE
        assert published
        assert published[0]["task_name"] == CONTENT_TRANSLATION_TASK_NAME
        assert published[0]["queue"] == AI_GENERATION_QUEUE

        again = enqueue_content_translation_job(
            db,
            owner_user_id=owner.id,
            profile_id=profile_id,
            request=request,
            sender=fake_sender,
        )
        assert again.id == job.id

        row = process_content_translation_job(db, job=job)
        assert row.translation_status in {"translated", "failed"}
        assert row.target_language == "en"
        assert row.profile_id == profile_id
    finally:
        db.close()
