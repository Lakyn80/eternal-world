import httpx

from app.db.models import RagSource
from app.db.session import get_db
from app.main import app
from app.modules.rag_chunks.chunker import build_chunk_candidates, split_paragraph_into_sentences
from app.modules.rag_chunks.validation import validate_chunk_candidates


def _register_and_login(client, email: str) -> str:
    password = "StrongPass123"
    client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": password,
            "full_name": "RAG Chunk User",
        },
    )
    login_response = client.post(
        "/api/auth/login",
        json={"email": email, "password": password},
    )
    return login_response.json()["access_token"]


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _create_profile(client, token: str, name: str) -> int:
    response = client.post(
        "/api/memory-profiles",
        headers=_auth_headers(token),
        json={"name": name},
    )
    return response.json()["id"]


def _build_long_source(sentence_count: int = 28) -> str:
    return " ".join(
        f"This is sentence number {index} about a remembered family story that stays coherent and complete."
        for index in range(sentence_count)
    )


def _create_rag_source(client, token: str, profile_id: int, **overrides):
    payload = {
        "title": "Chunk Source",
        "raw_text": _build_long_source(),
        "source_type": "manual_text",
        "language": "en",
    }
    payload.update(overrides)
    return client.post(
        f"/api/memory-profiles/{profile_id}/rag-sources",
        headers=_auth_headers(token),
        json=payload,
    )


def _chunk_source(client, token: str, source_id: int):
    return client.post(
        f"/api/rag-sources/{source_id}/chunk",
        headers=_auth_headers(token),
    )


def _list_chunks(client, token: str, source_id: int):
    return client.get(
        f"/api/rag-sources/{source_id}/chunks",
        headers=_auth_headers(token),
    )


def _get_test_db_session():
    override = app.dependency_overrides[get_db]
    session_generator = override()
    db = next(session_generator)
    return db, session_generator


def test_authenticated_user_can_chunk_own_source(client):
    token = _register_and_login(client, "rag-chunk-own@example.com")
    profile_id = _create_profile(client, token, "Chunk Own Profile")
    source_response = _create_rag_source(client, token, profile_id)
    source_id = source_response.json()["id"]

    response = _chunk_source(client, token, source_id)

    assert response.status_code == 200
    body = response.json()
    assert body["source_id"] == source_id
    assert body["source_status"] == "chunked"
    assert body["chunk_count"] >= 1
    assert body["processing_error"] is None


def test_unauthenticated_user_cannot_chunk_source(client):
    token = _register_and_login(client, "rag-chunk-unauth@example.com")
    profile_id = _create_profile(client, token, "Chunk Unauth Profile")
    source_response = _create_rag_source(client, token, profile_id)
    source_id = source_response.json()["id"]

    client.cookies.clear()
    response = client.post(f"/api/rag-sources/{source_id}/chunk")

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


def test_user_cannot_chunk_another_users_source(client):
    owner_token = _register_and_login(client, "rag-chunk-owner@example.com")
    other_token = _register_and_login(client, "rag-chunk-other@example.com")
    profile_id = _create_profile(client, owner_token, "Owner Chunk Profile")
    source_response = _create_rag_source(client, owner_token, profile_id)
    source_id = source_response.json()["id"]

    response = _chunk_source(client, other_token, source_id)

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG source not found"


def test_chunking_creates_ordered_chunks_with_zero_based_indexes(client):
    token = _register_and_login(client, "rag-chunk-order@example.com")
    profile_id = _create_profile(client, token, "Chunk Order Profile")
    source_response = _create_rag_source(client, token, profile_id, raw_text=_build_long_source(40))
    source_id = source_response.json()["id"]

    chunk_response = _chunk_source(client, token, source_id)
    list_response = _list_chunks(client, token, source_id)

    assert chunk_response.status_code == 200
    assert list_response.status_code == 200
    chunk_indexes = [chunk["chunk_index"] for chunk in list_response.json()]
    assert chunk_indexes == list(range(len(chunk_indexes)))


def test_chunking_replaces_previous_chunks_for_same_source(client):
    token = _register_and_login(client, "rag-chunk-replace@example.com")
    profile_id = _create_profile(client, token, "Chunk Replace Profile")
    source_response = _create_rag_source(client, token, profile_id, raw_text=_build_long_source(42))
    source_id = source_response.json()["id"]

    first_chunk_response = _chunk_source(client, token, source_id)
    first_chunks = _list_chunks(client, token, source_id).json()
    update_response = client.patch(
        f"/api/rag-sources/{source_id}",
        headers=_auth_headers(token),
        json={"raw_text": _build_long_source(4)},
    )
    second_chunk_response = _chunk_source(client, token, source_id)
    second_chunks = _list_chunks(client, token, source_id).json()

    assert first_chunk_response.status_code == 200
    assert update_response.status_code == 200
    assert second_chunk_response.status_code == 200
    assert len(first_chunks) > len(second_chunks)
    assert [chunk["chunk_index"] for chunk in second_chunks] == list(range(len(second_chunks)))


def test_list_chunks_returns_only_owned_source_chunks(client):
    first_token = _register_and_login(client, "rag-chunk-list-first@example.com")
    second_token = _register_and_login(client, "rag-chunk-list-second@example.com")
    first_profile_id = _create_profile(client, first_token, "First Chunk List Profile")
    second_profile_id = _create_profile(client, second_token, "Second Chunk List Profile")
    first_source_id = _create_rag_source(client, first_token, first_profile_id).json()["id"]
    second_source_id = _create_rag_source(client, second_token, second_profile_id).json()["id"]
    assert _chunk_source(client, first_token, first_source_id).status_code == 200
    assert _chunk_source(client, second_token, second_source_id).status_code == 200

    response = _list_chunks(client, first_token, first_source_id)

    assert response.status_code == 200
    body = response.json()
    assert body
    assert all(chunk["source_id"] == first_source_id for chunk in body)
    assert all(chunk["source_id"] != second_source_id for chunk in body)


def test_user_cannot_list_chunks_for_another_users_source(client):
    owner_token = _register_and_login(client, "rag-chunk-list-owner@example.com")
    other_token = _register_and_login(client, "rag-chunk-list-other@example.com")
    profile_id = _create_profile(client, owner_token, "Owner Chunk List Profile")
    source_id = _create_rag_source(client, owner_token, profile_id).json()["id"]
    assert _chunk_source(client, owner_token, source_id).status_code == 200

    response = _list_chunks(client, other_token, source_id)

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG source not found"


def test_user_can_read_own_chunk(client):
    token = _register_and_login(client, "rag-chunk-read-own@example.com")
    profile_id = _create_profile(client, token, "Chunk Read Own Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]
    assert _chunk_source(client, token, source_id).status_code == 200
    chunk_id = _list_chunks(client, token, source_id).json()[0]["id"]

    response = client.get(
        f"/api/rag-chunks/{chunk_id}",
        headers=_auth_headers(token),
    )

    assert response.status_code == 200
    assert response.json()["id"] == chunk_id
    assert response.json()["source_id"] == source_id


def test_user_cannot_read_another_users_chunk(client):
    owner_token = _register_and_login(client, "rag-chunk-read-owner@example.com")
    other_token = _register_and_login(client, "rag-chunk-read-other@example.com")
    profile_id = _create_profile(client, owner_token, "Chunk Read Owner Profile")
    source_id = _create_rag_source(client, owner_token, profile_id).json()["id"]
    assert _chunk_source(client, owner_token, source_id).status_code == 200
    chunk_id = _list_chunks(client, owner_token, source_id).json()[0]["id"]

    response = client.get(
        f"/api/rag-chunks/{chunk_id}",
        headers=_auth_headers(other_token),
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "RAG chunk not found"


def test_chunker_preserves_sentence_boundaries_on_normal_text():
    text = (
        "Prvni veta zustava cela a uzavrena. "
        "Druha veta navazuje bez rozbiti slov nebo interpunkce. "
        "Third sentence also stays intact for deterministic chunking."
    )

    chunks = build_chunk_candidates(
        text,
        target_chunk_size=70,
        max_chunk_size=140,
        min_useful_chunk_size=0,
        sentence_overlap=0,
    )

    assert len(chunks) >= 2
    assert all(chunk.chunk_text[-1] in ".!?…" for chunk in chunks)
    assert "Prvni veta zustava cela a uzavrena." in chunks[0].chunk_text


def test_chunker_preserves_russian_czech_and_english_punctuation_endings():
    sentences = split_paragraph_into_sentences(
        "Ahoj svete. Jak se mas? Привет мир! English sentence ends cleanly…"
    )

    assert sentences == [
        "Ahoj svete.",
        "Jak se mas?",
        "Привет мир!",
        "English sentence ends cleanly…",
    ]


def test_chunker_does_not_create_empty_chunks():
    chunks = build_chunk_candidates("\n\n First sentence. \n\n Second sentence. \n\n")

    assert chunks
    assert all(chunk.chunk_text.strip() for chunk in chunks)


def test_duplicate_chunks_are_detected_by_hash_validation():
    chunk_candidates = build_chunk_candidates(
        "Repeated sentence. Repeated sentence.",
        target_chunk_size=20,
        max_chunk_size=40,
        sentence_overlap=0,
    )
    validated_chunks, _ = validate_chunk_candidates(
        chunk_candidates=chunk_candidates + [chunk_candidates[0]],
        owner_user_id=1,
        profile_id=1,
        source_id=1,
        normalized_source_text="Repeated sentence. Repeated sentence.",
    )

    assert validated_chunks[-1].validation_status == "invalid"
    assert "duplicate_chunk_hash" in validated_chunks[-1].validation_errors


def test_validation_flags_suspicious_mid_sentence_starts_and_ends():
    chunk_candidates = build_chunk_candidates(
        "valid first sentence. lowercase continuation without ending",
        target_chunk_size=40,
        max_chunk_size=80,
        sentence_overlap=0,
    )
    validated_chunks, _ = validate_chunk_candidates(
        chunk_candidates=chunk_candidates,
        owner_user_id=1,
        profile_id=1,
        source_id=1,
        normalized_source_text="valid first sentence. lowercase continuation without ending",
    )

    warning_chunks = [chunk for chunk in validated_chunks if chunk.validation_status == "warning"]

    assert warning_chunks
    assert any("suspicious_mid_sentence_start" in chunk.validation_errors for chunk in warning_chunks)
    assert any("suspicious_mid_sentence_end" in chunk.validation_errors for chunk in warning_chunks)


def test_very_long_sentence_fallback_does_not_crash():
    very_long_sentence = ("word " * 500).strip() + "."

    chunks = build_chunk_candidates(
        very_long_sentence,
        target_chunk_size=300,
        max_chunk_size=500,
        sentence_overlap=0,
    )

    assert len(chunks) >= 2
    assert all(chunk.chunk_text for chunk in chunks)


def test_source_status_becomes_chunked_after_success(client):
    token = _register_and_login(client, "rag-chunk-status@example.com")
    profile_id = _create_profile(client, token, "Chunk Status Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    response = _chunk_source(client, token, source_id)

    assert response.status_code == 200
    assert response.json()["source_status"] == "chunked"

    db, session_generator = _get_test_db_session()
    try:
        rag_source = db.get(RagSource, source_id)
        assert rag_source is not None
        assert rag_source.status == "chunked"
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass


def test_source_processing_error_is_cleared_after_success(client):
    token = _register_and_login(client, "rag-chunk-clear-error@example.com")
    profile_id = _create_profile(client, token, "Chunk Clear Error Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    db, session_generator = _get_test_db_session()
    try:
        rag_source = db.get(RagSource, source_id)
        assert rag_source is not None
        rag_source.status = "failed"
        rag_source.processing_error = "old failure"
        db.commit()
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass

    response = _chunk_source(client, token, source_id)

    assert response.status_code == 200
    assert response.json()["processing_error"] is None

    db, session_generator = _get_test_db_session()
    try:
        rag_source = db.get(RagSource, source_id)
        assert rag_source is not None
        assert rag_source.processing_error is None
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass


def test_failure_path_sets_source_status_to_failed_with_safe_error(client, monkeypatch):
    token = _register_and_login(client, "rag-chunk-failure@example.com")
    profile_id = _create_profile(client, token, "Chunk Failure Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    def fail_chunk_build(*args, **kwargs):
        raise RuntimeError("unexpected chunker failure")

    monkeypatch.setattr("app.modules.rag_chunks.service.build_chunk_candidates", fail_chunk_build)

    response = _chunk_source(client, token, source_id)

    assert response.status_code == 500
    assert response.json()["detail"] == "Chunking failed"

    db, session_generator = _get_test_db_session()
    try:
        rag_source = db.get(RagSource, source_id)
        assert rag_source is not None
        assert rag_source.status == "failed"
        assert rag_source.processing_error == "Chunking failed"
    finally:
        try:
            next(session_generator)
        except StopIteration:
            pass


def test_no_external_api_calls_are_made_for_chunking_foundation(client, monkeypatch):
    def fail_http_call(*args, **kwargs):
        raise AssertionError("No external HTTP call should be made for rag chunking foundation")

    monkeypatch.setattr(httpx, "request", fail_http_call)
    monkeypatch.setattr(httpx, "get", fail_http_call)
    monkeypatch.setattr(httpx, "post", fail_http_call)

    token = _register_and_login(client, "rag-chunk-no-http@example.com")
    profile_id = _create_profile(client, token, "Chunk No HTTP Profile")
    source_id = _create_rag_source(client, token, profile_id).json()["id"]

    chunk_response = _chunk_source(client, token, source_id)
    list_response = _list_chunks(client, token, source_id)
    chunk_id = list_response.json()[0]["id"]
    get_response = client.get(
        f"/api/rag-chunks/{chunk_id}",
        headers=_auth_headers(token),
    )

    assert chunk_response.status_code == 200
    assert list_response.status_code == 200
    assert get_response.status_code == 200
