"""Task 65.13.6 - canonical-only RAG indexing for memorial contributions."""

from __future__ import annotations

import pytest

from app.core.config import settings
from app.db.models import MemorialContribution, MemoryProfile
from app.main import app
from app.modules.content_translation import repository as ct_repo
from app.modules.memorial_contribution_indexing.service import (
    ContributionIndexingEligibilityError,
    resolve_indexable_contribution_text,
)


PASSWORD = "StrongPass123"


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


def _create_memorial(client, token: str, *, canonical_language: str = "cs") -> int:
    response = client.post(
        "/api/memorials",
        headers=_auth_headers(token),
        json={
            "name": "Canon RAG",
            "canonical_language": canonical_language,
            "confirm_canonical_language": True,
        },
    )
    assert response.status_code == 201
    return int(response.json()["id"])


def test_same_language_contribution_indexes_original(client):
    token = _register_and_login(client, "rag65-same@example.com")
    profile_id = _create_memorial(client, token, canonical_language="cs")
    original = "Babička pečla koláče každou neděli."

    submitted = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(token),
        json={
            "title": "Koláče",
            "memory_text": original,
            "source_language": "cs",
            "privacy_scope": "all_family",
        },
    )
    assert submitted.status_code == 201
    contribution_id = submitted.json()["id"]

    approved = client.post(
        f"/api/memorials/{profile_id}/contributions/{contribution_id}/approve",
        headers=_auth_headers(token),
        json={},
    )
    assert approved.status_code == 200

    db = app.state.testing_session_local()
    try:
        from app.modules.memorial_contribution_indexing import repository as idx_repo

        promotion = idx_repo.get_promotion_by_contribution_id(db, contribution_id=contribution_id)
        assert promotion is not None
        assert promotion.approved_memory_text == original
        assert promotion.language == "cs"
    finally:
        db.close()


def test_cross_language_contribution_indexes_canonical_only(client):
    token = _register_and_login(client, "rag65-cross@example.com")
    profile_id = _create_memorial(client, token, canonical_language="cs")
    original = "She always watered the roses on Sunday morning."

    submitted = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(token),
        json={
            "title": "Roses",
            "memory_text": original,
            "source_language": "en",
            "privacy_scope": "all_family",
        },
    )
    assert submitted.status_code == 201
    body = submitted.json()
    assert body["canonical_text"].startswith("[en->cs] ")

    approved = client.post(
        f"/api/memorials/{profile_id}/contributions/{body['id']}/approve",
        headers=_auth_headers(token),
        json={},
    )
    assert approved.status_code == 200

    db = app.state.testing_session_local()
    try:
        from app.modules.memorial_contribution_indexing import repository as idx_repo

        promotion = idx_repo.get_promotion_by_contribution_id(db, contribution_id=body["id"])
        assert promotion is not None
        assert promotion.approved_memory_text == body["canonical_text"]
        assert promotion.language == "cs"
        assert original not in {promotion.approved_memory_text}
        # Original remains durable on the contribution row.
        contribution = db.get(MemorialContribution, body["id"])
        assert contribution is not None
        assert contribution.memory_text == original
    finally:
        db.close()


def test_missing_canonical_translation_blocks_indexing(client, monkeypatch):
    token = _register_and_login(client, "rag65-block@example.com")
    profile_id = _create_memorial(client, token, canonical_language="cs")
    original = "Foreign memory without usable canonical."

    submitted = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(token),
        json={
            "title": "Blocked",
            "memory_text": original,
            "source_language": "en",
            "privacy_scope": "all_family",
        },
    )
    assert submitted.status_code == 201
    contribution_id = submitted.json()["id"]

    db = app.state.testing_session_local()
    try:
        # Force the canonical MCT row into failed state.
        row = ct_repo.get_current(
            db,
            entity_type="memorial_contribution",
            entity_id=str(contribution_id),
            field_name="memory_text",
            target_language="cs",
        )
        assert row is not None
        ct_repo.mark_failed(db, row)
        db.commit()

        contribution = db.get(MemorialContribution, contribution_id)
        assert contribution is not None
        profile = db.get(MemoryProfile, contribution.profile_id)
        assert profile is not None
        with pytest.raises(ContributionIndexingEligibilityError):
            resolve_indexable_contribution_text(
                db,
                contribution=contribution,
                profile=profile,
            )
    finally:
        db.close()


def test_legacy_flag_allows_original_indexing(client, monkeypatch):
    monkeypatch.setattr(settings, "canonical_only_rag_indexing", False)
    token = _register_and_login(client, "rag65-legacy@example.com")
    profile_id = _create_memorial(client, token, canonical_language="cs")
    original = "Legacy English indexing path."

    submitted = client.post(
        f"/api/memorials/{profile_id}/contributions",
        headers=_auth_headers(token),
        json={
            "title": "Legacy",
            "memory_text": original,
            "source_language": "en",
            "privacy_scope": "all_family",
        },
    )
    assert submitted.status_code == 201
    contribution_id = submitted.json()["id"]

    approved = client.post(
        f"/api/memorials/{profile_id}/contributions/{contribution_id}/approve",
        headers=_auth_headers(token),
        json={},
    )
    assert approved.status_code == 200

    db = app.state.testing_session_local()
    try:
        from app.modules.memorial_contribution_indexing import repository as idx_repo

        promotion = idx_repo.get_promotion_by_contribution_id(db, contribution_id=contribution_id)
        assert promotion is not None
        assert promotion.approved_memory_text == original
    finally:
        db.close()
