"""Task 65.2 - AI Biographer question/answer/clarification loop, extended in
Task 65.6 to be context-aware (coverage tracking, duplicate-question
prevention, known-answer validation, deterministic fallback).

Reuses the fake-safe writer/encoder pattern to get a profile's biography
into `indexed` state (a precondition for Biographer eligibility) without any
real Qdrant/model calls, then exercises the authenticated HTTP surface.

Every test in this module stubs `avatar_biographer.service.build_topic_context_batch`
(see `_stub_context_retrieval` below) instead of relying on the real
`rag_retrieval`/Qdrant path: the `FakeWriter`/`FakeEncoder` bypass used to
put a biography into `indexed` state never actually writes to the real
Qdrant instance the RAG retrieval path would query, and that Qdrant
instance is a long-lived shared server (not reset per test run) - hitting
it for real here would be both slow and non-hermetic (behavior would depend
on whatever unrelated data the shared server happens to hold). Tests that
specifically exercise context-aware behavior override the stub per-topic via
`_patch_context_by_topic`.

Task 65.11.1 note: the stub seam moved from the old per-topic
`build_topic_context_package` to the batched `build_topic_context_batch`
(one query-embedding model invocation and one Qdrant request for the whole
8-topic catalog instead of 8 x 2 = 16 serial `retrieve_profile_rag()`
calls). The per-topic fixtures below are unchanged and are simply shaped
into that batch via `context_batch_from_packages`, so every coverage/
selection expectation in this file still asserts exactly the same contract
against exactly the same inputs. The structural call-count contract itself
is covered separately in
`test_task_65_11_1_biographer_query_batch.py`.
"""

from __future__ import annotations

import pytest
from sqlalchemy.exc import IntegrityError

from app.core.config import settings
from app.db.models import AiAction, BiographerQuestion, ConversationMemoryCandidate
from app.main import app
from app.modules.avatar_biographer import coverage, duplicate_prevention, repository
from app.modules.avatar_biographer import service as biographer_service
from app.modules.avatar_biographer import topics as topic_catalog
from app.modules.avatar_biographer.context_package import (
    TopicContextPackage,
    context_batch_from_packages,
    empty_context_batch,
    empty_context_package,
)
from app.modules.avatar_biographer.provider import (
    BiographerProviderRequestError,
    BiographerProviderResponse,
)
from app.modules.avatar_biographer.schemas import ProviderQuestionResult
from app.modules.avatar_memory_indexing.service import AvatarMemoryIndexingExecutionError, index_promotion
from app.modules.biography_ingestion.service import index_biography
from app.modules.embeddings.providers.base import EmbeddingVector
from app.modules.provider_usage.enums import AiFeature


PASSWORD = "StrongPass123"


@pytest.fixture(autouse=True)
def _force_mock_ai_brain_provider(monkeypatch):
    """This dev container's real environment sets `AI_BRAIN_PROVIDER=openai_compatible`
    with a real DeepSeek key (needed for live smoke testing) - `app.core.config.settings`
    is a process-level singleton that picks that up for every pytest run too,
    not just the running uvicorn server (the same mechanism already documented
    as a pre-existing `test_chat.py` flake). Without forcing this back to
    `mock` here, every un-monkeypatched `build_biographer_question_provider()`
    call in this file would silently place a real, billed DeepSeek call -
    violating the zero-paid-call requirement for automated tests."""

    monkeypatch.setattr(settings, "ai_brain_provider", "mock")


class FakeEncoder:
    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        return EmbeddingVector(values=[0.01] * 1024, dimension=1024, metadata={})


class FakeWriter:
    def __init__(self) -> None:
        self.points: dict[tuple[str, str], dict[str, object]] = {}

    def collection_vector_size(self, *, collection_name: str) -> int | None:
        return 1024

    def get_point(self, *, collection_name: str, point_id: str) -> dict[str, object] | None:
        return self.points.get((collection_name, point_id))

    def upsert_point(self, *, collection_name: str, point_id: str, vector, payload) -> None:
        self.points[(collection_name, point_id)] = {"vector": list(vector), "payload": dict(payload)}

    def delete_point(self, *, collection_name: str, point_id: str) -> None:
        self.points.pop((collection_name, point_id), None)


def _db():
    return app.state.testing_session_local()


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _register_and_login(client, email: str) -> str:
    client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": email})
    response = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    assert response.status_code == 200
    return response.json()["access_token"]


def _create_memorial(client, token: str, name: str = "Biographer Memorial") -> int:
    response = client.post("/api/memorials", headers=_auth_headers(token), json={"name": name})
    assert response.status_code == 201
    return response.json()["id"]


def _create_memorial_with_indexed_biography(client, email: str, biography: str = "Zivotopisny text.") -> tuple[str, int]:
    token = _register_and_login(client, email)
    profile_id = _create_memorial(client, token)
    patch = client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(token),
        json={"biography": biography},
    )
    assert patch.status_code == 200
    start = client.post(f"/api/memorials/{profile_id}/biography/ingest", headers=_auth_headers(token))
    assert start.status_code == 202

    db = _db()
    try:
        result = index_biography(db, profile_id=profile_id, writer=FakeWriter(), encoder=FakeEncoder(), validate_runtime=False)
        assert result.status == "indexed"
    finally:
        db.close()
    return token, profile_id


def _no_evidence_context(topic) -> TopicContextPackage:
    """Retrieval genuinely ran and found nothing yet for this topic -
    distinct from `empty_context_package` (retrieval unavailable/degraded,
    Part 11 of the task spec), which must skip generation entirely instead
    of still attempting one. This is the default stub used by every test
    below unless overridden, matching the previous (Task 65.2) behavior of
    always attempting a question even with no verified evidence yet."""

    return TopicContextPackage(
        topic_key=topic.key,
        retrieval_used=True,
        available_verified_sources=0,
        selected_source_count=0,
        selected_chunk_count=0,
        context_character_count=0,
        estimated_context_tokens=0,
        retrieval_duration_ms=1,
        chunk_excerpts=[],
    )


def _empty_context(db, *, current_user, profile_id, topics, locale):
    return context_batch_from_packages(
        {topic.key: _no_evidence_context(topic) for topic in topics},
        topics=topics,
        locale=locale,
    )


@pytest.fixture(autouse=True)
def _stub_context_retrieval(monkeypatch):
    monkeypatch.setattr(biographer_service, "build_topic_context_batch", _empty_context)


def _patch_context_by_topic(monkeypatch, overrides: dict[str, TopicContextPackage]) -> None:
    def _fake(db, *, current_user, profile_id, topics, locale):
        return context_batch_from_packages(
            {
                topic.key: overrides.get(topic.key, empty_context_package(topic))
                for topic in topics
            },
            topics=topics,
            locale=locale,
        )

    monkeypatch.setattr(biographer_service, "build_topic_context_batch", _fake)


def _rich_context(topic_key: str, excerpts: list[str]) -> TopicContextPackage:
    return TopicContextPackage(
        topic_key=topic_key,
        retrieval_used=True,
        available_verified_sources=1,
        selected_source_count=1,
        selected_chunk_count=len(excerpts),
        context_character_count=sum(len(e) for e in excerpts),
        estimated_context_tokens=sum(len(e) for e in excerpts) // 4,
        retrieval_duration_ms=5,
        chunk_excerpts=excerpts,
    )


def _all_topics_basic_except(monkeypatch, topic_key: str, excerpts: list[str]) -> None:
    """Gives every catalog topic exactly one generic `basic`-coverage chunk
    (so none of them out-rank each other as `not_started`), except
    `topic_key`, which gets the given excerpts (kept below the `rich`
    threshold so it stays selectable). Within a tied coverage band,
    selection falls back to fixed catalog order, so `topic_key` - being
    listed first for `"childhood"` - wins deterministically. This isolates
    "does generation/validation behave correctly for the topic under test"
    from "which topic does coverage pick", which is covered separately."""

    assert len(excerpts) < coverage.RICH_EVIDENCE_CHUNK_THRESHOLD
    overrides = {
        topic.key: _rich_context(topic.key, ["Obecný neutrální kontext."])
        for topic in topic_catalog.BIOGRAPHER_TOPICS
        if topic.key != topic_key
    }
    overrides[topic_key] = _rich_context(topic_key, excerpts)
    _patch_context_by_topic(monkeypatch, overrides)


def _patch_provider_responses(monkeypatch, responses: list[ProviderQuestionResult | Exception]) -> None:
    """Each call to the (mock) provider's `generate_question` pops the next
    scripted response/exception, in order."""

    remaining = list(responses)

    class _ScriptedProvider:
        provider_name = "mock"
        model = "mock"

        def generate_question(self, *, system_prompt: str, user_prompt: str) -> BiographerProviderResponse:
            item = remaining.pop(0)
            if isinstance(item, Exception):
                raise item
            return BiographerProviderResponse(result=item, provider_name="mock", model="mock", latency_ms=0)

    import app.modules.avatar_biographer.question_generation as question_generation_module

    monkeypatch.setattr(question_generation_module, "build_biographer_question_provider", lambda: _ScriptedProvider())


def test_eligibility_blocked_when_biography_missing(client):
    token = _register_and_login(client, "biographer-owner1@example.com")
    profile_id = _create_memorial(client, token)

    response = client.get(f"/api/memorials/{profile_id}/biographer/eligibility", headers=_auth_headers(token))
    assert response.status_code == 200
    body = response.json()
    assert body["eligible"] is False
    assert body["blocked_reason"] == "biography_missing"


def test_eligibility_blocked_when_biography_saved_but_not_indexed(client):
    token = _register_and_login(client, "biographer-owner2@example.com")
    profile_id = _create_memorial(client, token)
    client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(token),
        json={"biography": "Text bez indexace."},
    )

    response = client.get(f"/api/memorials/{profile_id}/biographer/eligibility", headers=_auth_headers(token))
    assert response.status_code == 200
    body = response.json()
    assert body["eligible"] is False
    assert body["blocked_reason"] == "biography_not_indexed"


def test_eligibility_blocked_while_indexing_in_progress(client):
    token = _register_and_login(client, "biographer-owner-ingesting@example.com")
    profile_id = _create_memorial(client, token)
    client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(token),
        json={"biography": "Text ke zpracovani."},
    )
    start = client.post(f"/api/memorials/{profile_id}/biography/ingest", headers=_auth_headers(token))
    assert start.status_code == 202

    response = client.get(f"/api/memorials/{profile_id}/biographer/eligibility", headers=_auth_headers(token))
    assert response.status_code == 200
    body = response.json()
    assert body["eligible"] is False
    assert body["blocked_reason"] == "indexing_in_progress"


def test_eligibility_blocked_when_biography_stale(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner-stale@example.com")
    edit = client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(token),
        json={"biography": "Upraveny text po indexaci."},
    )
    assert edit.status_code == 200

    response = client.get(f"/api/memorials/{profile_id}/biographer/eligibility", headers=_auth_headers(token))
    assert response.status_code == 200
    body = response.json()
    assert body["eligible"] is False
    assert body["blocked_reason"] == "biography_stale"

    blocked = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    )
    assert blocked.status_code == 400
    assert blocked.json()["detail"] == "biography_stale"


def test_eligible_once_biography_indexed(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner3@example.com")

    response = client.get(f"/api/memorials/{profile_id}/biographer/eligibility", headers=_auth_headers(token))
    assert response.status_code == 200
    assert response.json() == {"eligible": True, "blocked_reason": None}


def test_next_question_starts_with_childhood_topic(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner4@example.com")

    response = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    )
    assert response.status_code == 200
    body = response.json()
    assert body["topic"] == "childhood"
    assert body["locale"] == "cs"
    assert body["status"] == "pending"


def test_answering_childhood_question_creates_candidate_with_required_clarification(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner5@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    ).json()

    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Vyrostl jsem na malé vesnici s prarodiči."},
    )
    assert answer.status_code == 200
    body = answer.json()
    assert body["candidate_id"] is not None
    assert body["enrichment_status"] == "collecting_details"
    assert body["unresolved_clarification_count"] == 2  # place + approximate_period

    db = _db()
    try:
        from app.db.models import MemoryProfile

        profile = db.get(MemoryProfile, profile_id)
        candidate = db.get(ConversationMemoryCandidate, body["candidate_id"])
        assert candidate.workflow_version == 2
        assert candidate.memory_type == "childhood_memory"
        assert candidate.status == "needs_review"
        assert candidate.owner_user_id == profile.user_id
    finally:
        db.close()


def test_active_clarification_blocks_new_topic(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner6@example.com")
    childhood_question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    ).json()
    client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{childhood_question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Vyrostl jsem ve meste."},
    )

    # The candidate created above still has 2 unresolved required
    # clarifications - the eligibility gate must block offering a new topic
    # until they are answered, never silently skip ahead.
    eligibility = client.get(f"/api/memorials/{profile_id}/biographer/eligibility", headers=_auth_headers(token)).json()
    assert eligibility["eligible"] is False
    assert eligibility["blocked_reason"] == "active_clarification_exists"

    blocked = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    )
    assert blocked.status_code == 400


def test_answering_general_topic_question_has_no_required_clarification(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner6b@example.com")
    childhood_question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    ).json()
    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{childhood_question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Vyrostl jsem ve meste."},
    ).json()
    candidate_id = answer["candidate_id"]

    for answer_text in ["V malém bytě ve městě.", "Bylo mi asi šest let."]:
        resolve = client.post(
            f"/api/memorials/{profile_id}/candidates/{candidate_id}/clarifications/answer",
            headers=_auth_headers(token),
            json={"answer_text": answer_text},
        )
        assert resolve.status_code == 200
    assert resolve.json()["unresolved_clarification_count"] == 0
    assert resolve.json()["enrichment_status"] == "ready_for_owner_review"

    family_question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    )
    assert family_question.status_code == 200
    assert family_question.json()["topic"] == "family"

    family_answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{family_question.json()['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Moje maminka byla pro mě vždy nejdůležitější člověk."},
    )
    assert family_answer.status_code == 200
    body = family_answer.json()
    assert body["unresolved_clarification_count"] == 0
    assert body["enrichment_status"] == "ready_for_owner_review"

    db = _db()
    try:
        candidate = db.get(ConversationMemoryCandidate, body["candidate_id"])
        assert candidate.memory_type == "general"
    finally:
        db.close()


def test_skip_question_never_creates_a_candidate(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner7@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    ).json()

    response = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/skip",
        headers=_auth_headers(token),
    )
    assert response.status_code == 200
    assert response.json()["status"] == "skipped"
    assert response.json()["resulting_candidate_id"] is None

    db = _db()
    try:
        candidate_count = db.query(ConversationMemoryCandidate).filter(ConversationMemoryCandidate.profile_id == profile_id).count()
        assert candidate_count == 0
    finally:
        db.close()


def test_postpone_question_marks_status_and_never_creates_a_candidate(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner-postpone@example.com")
    question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    ).json()

    response = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/postpone",
        headers=_auth_headers(token),
    )
    assert response.status_code == 200
    assert response.json()["status"] == "postponed"
    assert response.json()["resulting_candidate_id"] is None

    # A second postpone attempt on the same (no longer pending) question is
    # a conflict, not a silent no-op.
    conflict = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/postpone",
        headers=_auth_headers(token),
    )
    assert conflict.status_code == 409


def test_topics_are_never_repeated_across_the_first_pass_through_the_catalog(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner8@example.com")
    seen_topics: set[str] = set()
    for _ in range(8):
        question = client.get(
            f"/api/memorials/{profile_id}/biographer/next-question",
            params={"locale": "ru"},
            headers=_auth_headers(token),
        ).json()
        assert question["topic"] not in seen_topics
        seen_topics.add(question["topic"])
        client.post(
            f"/api/memorials/{profile_id}/biographer/questions/{question['id']}/skip",
            headers=_auth_headers(token),
        )

    # Business rule: the Biographer must never present a permanent
    # "nothing left to ask" dead end - once every catalog topic has been
    # covered once, it keeps offering questions by revisiting the topic
    # asked longest ago instead of returning `None` (see
    # `avatar_biographer.coverage.select_next_topic`'s revisit tier).
    revisited = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "ru"},
        headers=_auth_headers(token),
    )
    assert revisited.status_code == 200
    revisited_body = revisited.json()
    assert revisited_body is not None
    assert revisited_body["topic"] in seen_topics


def test_foreign_user_cannot_reach_biographer_endpoints(client):
    _owner_token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner9@example.com")
    outsider_token = _register_and_login(client, "biographer-outsider9@example.com")

    response = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(outsider_token),
    )
    assert response.status_code == 404


def test_viewer_cannot_answer_biographer_questions(client):
    owner_token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-owner10@example.com")
    viewer_token = _register_and_login(client, "biographer-viewer10@example.com")
    invite = client.post(
        f"/api/memorials/{profile_id}/invitations",
        headers=_auth_headers(owner_token),
        json={"email": "biographer-viewer10@example.com", "role": "viewer"},
    )
    assert invite.status_code == 201
    client.post(
        "/api/invitations/accept",
        headers=_auth_headers(viewer_token),
        json={"token": invite.json()["token"]},
    )

    response = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(viewer_token),
    )
    assert response.status_code == 403


# --- Task 65.6: coverage, duplicate prevention, generation, provenance ----


def test_coverage_topic_with_rich_evidence_is_not_selected_before_untouched_topics(client, monkeypatch):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-coverage1@example.com")
    _patch_context_by_topic(
        monkeypatch,
        {
            "childhood": _rich_context(
                "childhood",
                [
                    "Dětství jsem prožil poblíž Uherského Hradiště.",
                    "Jezdil jsem na kole a hrál fotbal.",
                    "Chodil jsem do lesa s kamarády.",
                    "Rád jsem rozebíral staré přístroje.",
                ],
            )
        },
    )

    response = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    )
    assert response.status_code == 200
    # "childhood" already has rich verified evidence (>= RICH_EVIDENCE_CHUNK_THRESHOLD
    # chunks) while every other topic is untouched (`not_started`) - coverage
    # priority must offer a `not_started` topic first, proving topic
    # selection is not unconditionally childhood-first.
    assert response.json()["topic"] != "childhood"


def test_known_broad_question_rejected_when_evidence_already_covers_it():
    topic = topic_catalog.get_topic("childhood")
    broad_question_cs = topic.questions["cs"]
    result = duplicate_prevention.find_known_answer_violation(
        broad_question_cs,
        topic=topic,
        verified_chunk_count=4,
        known_information_used_reported_by_provider=False,
    )
    assert result.accepted is False
    assert result.reason == duplicate_prevention.RejectionReason.KNOWN_BROAD_FACT


def test_specific_followup_question_accepted_when_it_uses_known_context():
    topic = topic_catalog.get_topic("childhood")
    deep_question = "Který konkrétní přístroj jste jako dítě rozebral a co jste se při tom naučil?"
    result = duplicate_prevention.find_known_answer_violation(
        deep_question,
        topic=topic,
        verified_chunk_count=4,
        known_information_used_reported_by_provider=True,
    )
    assert result.accepted is True


def test_broad_question_still_allowed_when_nothing_is_known_yet():
    topic = topic_catalog.get_topic("childhood")
    result = duplicate_prevention.find_known_answer_violation(
        topic.questions["cs"], topic=topic, verified_chunk_count=0, known_information_used_reported_by_provider=False
    )
    assert result.accepted is True


def test_duplicate_question_text_rejected_regardless_of_case_and_punctuation():
    question = BiographerQuestion(
        id=1, profile_id=1, topic="family", locale="cs", status="answered",
        question_text="Kdo byl pro vás nejdůležitější?",
    )
    result = duplicate_prevention.find_duplicate_against_history(
        "kdo byl pro vás nejdůležitější???",
        topic_key="family",
        candidate_question_intent=None,
        previous_questions=[question],
    )
    assert result.accepted is False
    assert result.reason == duplicate_prevention.RejectionReason.EXACT_DUPLICATE


def test_generation_regenerates_once_then_falls_back_to_deterministic_question(client, monkeypatch):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-fallback1@example.com")
    _all_topics_basic_except(
        monkeypatch,
        "childhood",
        ["Dětství jsem prožil poblíž Uherského Hradiště.", "Jezdil jsem na kole.", "Hrál jsem fotbal."],
    )

    banned_question = ProviderQuestionResult(
        question=topic_catalog.get_topic("childhood").questions["cs"],
        known_information_used=False,
        question_intent="general_fact",
        confidence="low",
    )
    _patch_provider_responses(monkeypatch, [banned_question, banned_question])

    response = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    )
    assert response.status_code == 200
    body = response.json()
    assert body["topic"] == "childhood"
    assert body["generation_mode"] == "deterministic_fallback"
    assert body["fallback_used"] is True

    db = _db()
    try:
        question = db.get(BiographerQuestion, body["id"])
        assert question.validation_result == "fallback_used"
    finally:
        db.close()


def test_generation_accepts_second_attempt_after_first_rejection(client, monkeypatch):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-regenerate1@example.com")
    _all_topics_basic_except(
        monkeypatch,
        "childhood",
        ["Dětství jsem prožil poblíž Uherského Hradiště.", "Jezdil jsem na kole.", "Hrál jsem fotbal."],
    )

    banned_question = ProviderQuestionResult(
        question=topic_catalog.get_topic("childhood").questions["cs"],
        known_information_used=False,
        question_intent="general_fact",
        confidence="low",
    )
    good_question = ProviderQuestionResult(
        question="Který konkrétní přístroj jste jako dítě rozebral a co jste se při tom naučil?",
        known_information_used=True,
        question_intent="specific_memory",
        confidence="high",
    )
    _patch_provider_responses(monkeypatch, [banned_question, good_question])

    response = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    )
    assert response.status_code == 200
    body = response.json()
    assert body["generation_mode"] == "llm_generated"
    assert body["question_text"] == good_question.question

    db = _db()
    try:
        question = db.get(BiographerQuestion, body["id"])
        assert question.validation_result == "regenerated"
        assert question.question_intent == "specific_memory"
    finally:
        db.close()


def test_provider_failure_falls_back_to_deterministic_question(client, monkeypatch):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-providerdown@example.com")

    import app.modules.avatar_biographer.question_generation as question_generation_module

    class _FailingProvider:
        provider_name = "openai_compatible"
        model = "deepseek-chat"

        def generate_question(self, *, system_prompt: str, user_prompt: str):
            raise BiographerProviderRequestError("simulated network failure")

    monkeypatch.setattr(question_generation_module, "build_biographer_question_provider", lambda: _FailingProvider())
    _all_topics_basic_except(monkeypatch, "childhood", ["Dětství jsem prožil na vesnici."])

    response = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    )
    assert response.status_code == 200
    body = response.json()
    assert body["generation_mode"] == "deterministic_fallback"
    assert body["fallback_used"] is True


def test_successful_llm_generated_question_persists_ai_action(client):
    # Default autouse stub returns zero evidence for every topic, so the
    # (mock) provider's single canned response is accepted outright for the
    # very first-ever question (nothing to duplicate against yet).
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-aiaction1@example.com")

    response = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    )
    assert response.status_code == 200
    body = response.json()
    assert body["generation_mode"] == "llm_generated"

    db = _db()
    try:
        question = db.get(BiographerQuestion, body["id"])
        assert question.ai_action_id is not None
        action = db.get(AiAction, question.ai_action_id)
        assert action.feature == AiFeature.AVATAR_BIOGRAPHER_QUESTION.value
        assert action.status == "succeeded"
        assert action.provider_call_count == 1
    finally:
        db.close()


def test_retrieval_unavailable_falls_back_without_any_provider_call(client, monkeypatch):
    """Part 11/65 of the task spec: a degraded retrieval path (Qdrant down,
    embedding model unavailable, etc.) must fall back deterministically
    without ever attempting a paid provider call - proven here by
    monkeypatching the (mock) provider to explode if it is ever
    constructed at all."""

    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-retrievaldown@example.com")

    def _unavailable(db, *, current_user, profile_id, topics, locale):
        return empty_context_batch(topics, locale=locale)

    monkeypatch.setattr(biographer_service, "build_topic_context_batch", _unavailable)

    import app.modules.avatar_biographer.question_generation as question_generation_module

    def _explode():
        raise AssertionError("provider must never be constructed when retrieval is unavailable")

    monkeypatch.setattr(question_generation_module, "build_biographer_question_provider", _explode)

    response = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    )
    assert response.status_code == 200
    body = response.json()
    assert body["generation_mode"] == "deterministic_fallback"
    assert body["question_text"] == topic_catalog.get_topic("childhood").questions["cs"]

    db = _db()
    try:
        action_count = db.query(AiAction).filter(AiAction.feature == AiFeature.AVATAR_BIOGRAPHER_QUESTION.value).count()
        assert action_count == 0
    finally:
        db.close()


def test_partial_unique_index_prevents_two_pending_questions_for_same_profile(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-race1@example.com")
    db = _db()
    try:
        repository.create_question(db, profile_id=profile_id, topic="childhood", locale="cs", question_text="Q1")
        db.commit()
        with pytest.raises(IntegrityError):
            repository.create_question(db, profile_id=profile_id, topic="family", locale="cs", question_text="Q2")
    finally:
        db.rollback()
        db.close()


def test_concurrent_next_question_requests_reuse_the_winning_pending_question(client, monkeypatch):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biographer-race2@example.com")

    real_get_pending_question = repository.get_pending_question
    call_count = {"n": 0}

    def _racy_get_pending_question(db, *, profile_id):
        call_count["n"] += 1
        if call_count["n"] == 1:
            # Simulate another request winning the race right after this
            # request already decided there was no pending question.
            winner_db = _db()
            try:
                repository.create_question(
                    winner_db, profile_id=profile_id, topic="childhood", locale="cs", question_text="Winner question"
                )
                winner_db.commit()
            finally:
                winner_db.close()
            return None
        return real_get_pending_question(db, profile_id=profile_id)

    monkeypatch.setattr(repository, "get_pending_question", _racy_get_pending_question)

    response = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    )
    assert response.status_code == 200
    body = response.json()
    assert body["question_text"] == "Winner question"

    db = _db()
    try:
        pending_count = (
            db.query(BiographerQuestion)
            .filter(BiographerQuestion.profile_id == profile_id, BiographerQuestion.status == "pending")
            .count()
        )
        assert pending_count == 1
    finally:
        db.close()


def test_postpone_cooldown_pure_unit():
    childhood = topic_catalog.get_topic("childhood")
    postponed_question = BiographerQuestion(
        id=1, profile_id=1, topic="childhood", locale="cs", status="postponed",
    )
    coverage_row = coverage.evaluate_topic_coverage(
        topic=childhood,
        topic_questions=[postponed_question],
        verified_chunk_count=0,
        has_unresolved_candidate_for_topic=False,
        sequence_by_question_id={1: 0},
    )
    assert coverage_row.state == coverage.TopicCoverageState.POSTPONED

    not_yet_selectable = coverage.select_next_topic(
        [
            coverage_row,
            *(
                coverage.evaluate_topic_coverage(
                    topic=other,
                    topic_questions=[],
                    verified_chunk_count=0,
                    has_unresolved_candidate_for_topic=False,
                    sequence_by_question_id={},
                )
                for other in topic_catalog.BIOGRAPHER_TOPICS
                if other.key != "childhood"
            ),
        ],
        total_questions_asked=1,
    )
    # Every other topic is `not_started`, strictly higher priority than a
    # `postponed` topic regardless of cool-down - proves postponed topics
    # never jump the queue ahead of untouched ones.
    assert not_yet_selectable is not None
    assert not_yet_selectable.state == coverage.TopicCoverageState.NOT_STARTED


def test_normalize_question_text_ignores_whitespace_and_punctuation():
    a = duplicate_prevention.normalize_question_text("Kde jste  prožil dětství?!")
    b = duplicate_prevention.normalize_question_text("kde jste prožil dětství")
    assert a == b


# --- Task 65.10.5: continue the AI Biographer immediately after an indexed
# answer, instead of the resume endpoint reporting the completed candidate as
# `candidate_indexed` forever (even across a fresh page reload, since the
# "latest ever" Biographer-sourced candidate never stops being the latest
# once indexed). Covers the exact backend half of the bug: a terminal
# `indexed`/`failed` promotion outcome must never be reported as an ongoing
# block on new question generation. -----------------------------------------


def _answer_childhood_and_approve_for_indexing(client, token: str, profile_id: int) -> dict:
    """Drives the real HTTP flow up to (and including) owner approval, the
    same path a real Biographer interview takes: answer the first (always
    `childhood`) question, resolve its two mandatory clarifications, approve
    the resulting candidate. Returns everything a caller needs to then
    simulate the indexing job succeeding or failing directly via
    `index_promotion` (Task 65.6.1's own precedent for testing the indexing
    outcome without a real Qdrant/embedding call)."""

    childhood_question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    ).json()
    assert childhood_question["topic"] == "childhood"

    answer = client.post(
        f"/api/memorials/{profile_id}/biographer/questions/{childhood_question['id']}/answer",
        headers=_auth_headers(token),
        json={"locale": "cs", "answer_text": "Vyrostl jsem ve meste."},
    ).json()
    candidate_id = answer["candidate_id"]

    for answer_text in ["V malém bytě ve městě.", "Bylo mi asi šest let."]:
        resolve = client.post(
            f"/api/memorials/{profile_id}/candidates/{candidate_id}/clarifications/answer",
            headers=_auth_headers(token),
            json={"answer_text": answer_text},
        )
        assert resolve.status_code == 200
    assert resolve.json()["enrichment_status"] == "ready_for_owner_review"

    # Backend correctness requirement: a genuine owner-review-pending
    # candidate must still block exactly as before - the fix must not
    # weaken this real gate.
    resume_before_review = client.get(
        f"/api/memorials/{profile_id}/biographer/resume", headers=_auth_headers(token)
    ).json()
    assert resume_before_review["next_action"] == "candidate_ready_for_review"
    assert resume_before_review["active_question"] is None

    review = client.post(
        f"/api/memorials/{profile_id}/candidates/{candidate_id}/owner-review",
        headers=_auth_headers(token),
        json={"action": "confirm"},
    )
    assert review.status_code == 200
    body = review.json()
    assert body["promotion_status"] == "pending_index"

    # Backend correctness requirement: a real, not-yet-run indexing job must
    # still block exactly as before too.
    resume_pending_index = client.get(
        f"/api/memorials/{profile_id}/biographer/resume", headers=_auth_headers(token)
    ).json()
    assert resume_pending_index["next_action"] == "candidate_pending_index"

    db = _db()
    try:
        candidate = db.get(ConversationMemoryCandidate, candidate_id)
        owner_user_id = candidate.owner_user_id
    finally:
        db.close()

    return {
        "candidate_id": candidate_id,
        "promotion_id": body["promotion_id"],
        "owner_user_id": owner_user_id,
        "childhood_question_text": childhood_question["question_text"],
    }


def test_successfully_indexed_answer_is_no_longer_active_and_resume_advances_to_the_next_real_question(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biog-index-flow1@example.com")
    state = _answer_childhood_and_approve_for_indexing(client, token, profile_id)

    db = _db()
    try:
        result = index_promotion(
            db,
            owner_user_id=state["owner_user_id"],
            promotion_id=state["promotion_id"],
            writer=FakeWriter(),
            encoder=FakeEncoder(),
            validate_runtime=False,
        )
        assert result.result == "indexed"
    finally:
        db.close()

    # (1) The successfully indexed candidate is no longer returned as an
    # unresolved/active candidate blocking the interview, and (2) resume
    # returns `question_ready` immediately - not `candidate_indexed` forever,
    # and not a page-reload-proof dead end.
    resume_after_index = client.get(
        f"/api/memorials/{profile_id}/biographer/resume", headers=_auth_headers(token)
    ).json()
    assert resume_after_index["eligible"] is True
    assert resume_after_index["next_action"] == "question_ready"
    assert resume_after_index["promotion_status"] == "indexed"
    assert resume_after_index["candidate_id"] == state["candidate_id"]
    # No pending question exists yet - resume never generates one itself
    # (Task 65.7 D.25's own "never a side effect" contract), it only signals
    # that a fresh one may now be fetched.
    assert resume_after_index["active_question"] is None

    # (3) The completed (childhood) question is never selected again as the
    # "next" question - a real, different topic is offered.
    next_question = client.get(
        f"/api/memorials/{profile_id}/biographer/next-question",
        params={"locale": "cs"},
        headers=_auth_headers(token),
    ).json()
    assert next_question is not None
    assert next_question["status"] == "pending"
    assert next_question["question_text"] != state["childhood_question_text"]

    # (4) Repeated resume calls are idempotent - the same pending question is
    # returned, never a second one created.
    resume_again = client.get(
        f"/api/memorials/{profile_id}/biographer/resume", headers=_auth_headers(token)
    ).json()
    assert resume_again["next_action"] == "question_ready"
    assert resume_again["active_question"]["id"] == next_question["id"]

    db = _db()
    try:
        pending_count = (
            db.query(BiographerQuestion)
            .filter(BiographerQuestion.profile_id == profile_id, BiographerQuestion.status == "pending")
            .count()
        )
        assert pending_count == 1
    finally:
        db.close()


def test_failed_indexing_surfaces_as_candidate_indexing_failed_and_never_silently_advances(client):
    token, profile_id = _create_memorial_with_indexed_biography(client, "biog-index-flow2@example.com")
    state = _answer_childhood_and_approve_for_indexing(client, token, profile_id)

    class _FailingWriter:
        def collection_vector_size(self, *, collection_name: str) -> int | None:
            return 1024

        def get_point(self, *, collection_name: str, point_id: str) -> dict[str, object] | None:
            return None

        def upsert_point(self, *, collection_name: str, point_id: str, vector, payload) -> None:
            raise RuntimeError("qdrant temporarily unavailable")

        def delete_point(self, *, collection_name: str, point_id: str) -> None:
            pass

    db = _db()
    try:
        with pytest.raises(AvatarMemoryIndexingExecutionError):
            index_promotion(
                db,
                owner_user_id=state["owner_user_id"],
                promotion_id=state["promotion_id"],
                writer=_FailingWriter(),
                encoder=FakeEncoder(),
                validate_runtime=False,
            )
    finally:
        db.close()

    # (5) The pre-fix code fell straight through to `question_ready` here
    # (nothing in the resume decision tree recognized `failed`) - silently
    # treating a failed indexing job as though it had succeeded. It must now
    # be a distinct, explicit, blocking state instead.
    resume_after_failure = client.get(
        f"/api/memorials/{profile_id}/biographer/resume", headers=_auth_headers(token)
    ).json()
    assert resume_after_failure["eligible"] is True
    assert resume_after_failure["next_action"] == "candidate_indexing_failed"
    assert resume_after_failure["promotion_status"] == "failed"
    assert resume_after_failure["active_question"] is None

    # Idempotent: calling resume again keeps reporting the same blocked
    # state - it never "gives up" and advances to a new question on its own.
    resume_again = client.get(
        f"/api/memorials/{profile_id}/biographer/resume", headers=_auth_headers(token)
    ).json()
    assert resume_again["next_action"] == "candidate_indexing_failed"

    db = _db()
    try:
        pending_count = (
            db.query(BiographerQuestion)
            .filter(BiographerQuestion.profile_id == profile_id, BiographerQuestion.status == "pending")
            .count()
        )
        assert pending_count == 0
    finally:
        db.close()


def test_passive_resume_is_read_only_without_generation_rag_or_question_writes(client, monkeypatch):
    """Task 65.11.4 Part F: ordinary healthy resume is generation/retrieval-free.

    On a clean eligible profile (no stale-clarification repair needed), the
    resume endpoint must not call question generation, embeddings, Qdrant,
    create a BiographerQuestion, mutate candidates/jobs, or flush/commit.

    Note: a pre-existing Task 65.10.1 bounded self-repair may still commit
    when unresolved_clarification_count disagrees with real pending rows;
    that path is out of scope for this clean-path assertion and is not
    claimed to be impossible on every resume.
    """

    from app.modules.avatar_biographer import question_generation as question_generation_module
    from app.modules.avatar_biographer import resume as resume_module
    from app.modules.rag_retrieval import service as rag_service
    from sqlalchemy.orm import Session

    token, profile_id = _create_memorial_with_indexed_biography(
        client, "biographer-resume-readonly-65-11-4@example.com"
    )

    def _explode_provider():
        raise AssertionError("resume must never construct the question provider")

    def _explode_batch(*_args, **_kwargs):
        raise AssertionError("resume must never call topic-context / RAG batch retrieval")

    def _explode_create_question(*_args, **_kwargs):
        raise AssertionError("resume must never create a BiographerQuestion")

    def _explode_qdrant(*_args, **_kwargs):
        raise AssertionError("resume must never build a Qdrant client")

    monkeypatch.setattr(question_generation_module, "build_biographer_question_provider", _explode_provider)
    monkeypatch.setattr(biographer_service, "build_topic_context_batch", _explode_batch)
    monkeypatch.setattr(repository, "create_question", _explode_create_question)
    monkeypatch.setattr(rag_service, "build_qdrant_client", _explode_qdrant)

    commit_calls = {"count": 0}
    flush_calls = {"count": 0}
    original_commit = Session.commit
    original_flush = Session.flush

    def _counting_commit(self, *args, **kwargs):
        commit_calls["count"] += 1
        return original_commit(self, *args, **kwargs)

    def _counting_flush(self, *args, **kwargs):
        flush_calls["count"] += 1
        return original_flush(self, *args, **kwargs)

    monkeypatch.setattr(Session, "commit", _counting_commit)
    monkeypatch.setattr(Session, "flush", _counting_flush)

    db = _db()
    try:
        before_questions = db.query(BiographerQuestion).filter(BiographerQuestion.profile_id == profile_id).count()
        before_candidates = (
            db.query(ConversationMemoryCandidate).filter(ConversationMemoryCandidate.profile_id == profile_id).count()
        )
        before_actions = db.query(AiAction).filter(AiAction.memorial_id == profile_id).count()
    finally:
        db.close()

    # Reset counters after setup queries (which may flush/commit via fixtures).
    commit_calls["count"] = 0
    flush_calls["count"] = 0

    response = client.get(f"/api/memorials/{profile_id}/biographer/resume", headers=_auth_headers(token))
    assert response.status_code == 200
    body = response.json()
    assert body["eligible"] is True
    assert body["next_action"] == "question_ready"
    assert body["active_question"] is None

    db = _db()
    try:
        after_questions = db.query(BiographerQuestion).filter(BiographerQuestion.profile_id == profile_id).count()
        after_candidates = (
            db.query(ConversationMemoryCandidate).filter(ConversationMemoryCandidate.profile_id == profile_id).count()
        )
        after_actions = db.query(AiAction).filter(AiAction.memorial_id == profile_id).count()
    finally:
        db.close()

    assert after_questions == before_questions == 0
    assert after_candidates == before_candidates == 0
    assert after_actions == before_actions
    assert commit_calls["count"] == 0, "clean passive resume must not session.commit()"
    assert flush_calls["count"] == 0, "clean passive resume must not session.flush()"
    # Keep the public resume helper importable for static review of this contract.
    assert callable(resume_module.get_resume_state)
