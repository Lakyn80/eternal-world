"""Task 65.11.1 - AI Biographer RAG fan-out elimination + batched topic query
embeddings.

Fake-safe by construction: every test in this module replaces the BGE-M3
query-encoding seam (`rag_retrieval.hybrid.default_encode_hybrid_query_vectors`
/ `..._batch`) and the Qdrant client factory
(`rag_retrieval.service.build_qdrant_client`) with explicit, counting fakes.
Nothing here imports or initializes real BGE-M3 weights, contacts a real
Qdrant server, touches the live PostgreSQL/Redis instances, or makes a
DeepSeek request (the session-wide `conftest` guards force
`ai_brain_provider="mock"` and hard-fail any real paid-provider HTTP call).

The structural defect this module locks down: before Task 65.11.1 one
"generate a new question" request built a `TopicContextPackage` for all 8
catalog topics, each of which called the public `retrieve_profile_rag()`
twice (`source_type="biography"` and `source_type="conversation_candidate"`)
- 8 x 2 = 16 sequential query-embedding model invocations per HTTP request.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import pytest

from app.core.config import settings
from app.db.models import (
    BiographerQuestion,
    MemoryProfile,
    RagChunk,
    RagEmbedding,
    RagSource,
    User,
)
from app.main import app
from app.modules.avatar_biographer import coverage as coverage_module
from app.modules.avatar_biographer import repository as biographer_repository
from app.modules.avatar_biographer import service as biographer_service
from app.modules.avatar_biographer import topics as topic_catalog
from app.modules.avatar_biographer.context_package import (
    _BATCH_RETRIEVAL_LIMIT,
    _CONTEXT_CHUNK_LIMIT,
    _VERIFIED_SOURCE_TYPES,
)
from app.modules.avatar_biographer.provider import BiographerProviderResponse
from app.modules.avatar_biographer.schemas import ProviderQuestionResult
from app.modules.biography_ingestion.service import index_biography
from app.modules.embeddings.providers.base import EmbeddingVector
from app.modules.rag_retrieval import hybrid as hybrid_module
from app.modules.rag_retrieval import service as rag_service
from app.modules.rag_retrieval.hybrid import HybridQueryVectors


PASSWORD = "StrongPass123"

#: Deterministic stand-in for the real 1024-dim BGE-M3 dense vector - the
#: dimension must match `embedding_models.registry`'s `bge_m3_dense_sparse`
#: definition or `rag_retrieval` rejects the query before searching.
_DENSE_DIMENSION = 1024


class FakeEncoder:
    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        return EmbeddingVector(values=[0.01] * _DENSE_DIMENSION, dimension=_DENSE_DIMENSION, metadata={})


class FakeWriter:
    def __init__(self) -> None:
        self.points: dict[tuple[str, str], dict[str, object]] = {}

    def collection_vector_size(self, *, collection_name: str) -> int | None:
        return _DENSE_DIMENSION

    def get_point(self, *, collection_name: str, point_id: str) -> dict[str, object] | None:
        return self.points.get((collection_name, point_id))

    def upsert_point(self, *, collection_name: str, point_id: str, vector, payload) -> None:
        self.points[(collection_name, point_id)] = {"vector": list(vector), "payload": dict(payload)}

    def delete_point(self, *, collection_name: str, point_id: str) -> None:
        self.points.pop((collection_name, point_id), None)


@dataclass
class RetrievalCallCounters:
    """Explicit structural call counters - the performance proof for this
    task is deterministic invocation counting, never wall-clock timing."""

    scalar_query_encode_calls: int = 0
    batch_query_encode_calls: int = 0
    encoded_query_texts: list[str] = field(default_factory=list)
    batch_input_types: list[str] = field(default_factory=list)
    passage_encode_calls: int = 0
    qdrant_search_calls: int = 0
    qdrant_batch_search_calls: int = 0
    qdrant_search_filters: list[dict] = field(default_factory=list)


def _fake_dense_vector(text: str) -> list[float]:
    seed = (abs(hash(text)) % 97) / 1000.0
    return [round(0.01 + seed, 6)] * _DENSE_DIMENSION


def _fake_query_vectors(text: str) -> HybridQueryVectors:
    return HybridQueryVectors(
        dense_vector=_fake_dense_vector(text),
        sparse_vector={"tok": 1.0},
    )


class FakeQdrantClient:
    """Counts every Qdrant round trip and returns caller-supplied points.

    `points_by_query_text` is keyed by the topic query text so a test can
    give different topics different amounts of evidence deterministically.
    """

    def __init__(
        self,
        counters: RetrievalCallCounters,
        *,
        points_by_query_text: dict[str, list[dict[str, object]]] | None = None,
        fail: bool = False,
    ) -> None:
        self._counters = counters
        self._points_by_query_text = points_by_query_text or {}
        self._fail = fail
        self._vector_to_query_text = {
            tuple(_fake_dense_vector(text)): text for text in self._points_by_query_text
        }

    def _lookup(self, vector: list[float]) -> list[dict[str, object]]:
        query_text = self._vector_to_query_text.get(tuple(vector))
        if query_text is None:
            return []
        return [dict(point) for point in self._points_by_query_text[query_text]]

    def search_points(self, *, collection_name, vector, limit, search_filter=None, score_threshold=None):
        self._counters.qdrant_search_calls += 1
        self._counters.qdrant_search_filters.append(dict(search_filter or {}))
        if self._fail:
            raise RuntimeError("qdrant unavailable")
        return self._lookup(list(vector))[:limit]

    def search_points_batch(self, *, collection_name, searches):
        self._counters.qdrant_batch_search_calls += 1
        if self._fail:
            raise RuntimeError("qdrant unavailable")
        results: list[list[dict[str, object]]] = []
        for search in searches:
            self._counters.qdrant_search_filters.append(dict(search.get("filter") or {}))
            results.append(self._lookup(list(search["vector"]))[: int(search["limit"])])
        return results


def install_fake_retrieval_stack(
    monkeypatch,
    *,
    points_by_query_text: dict[str, list[dict[str, object]]] | None = None,
    qdrant_fails: bool = False,
    batch_encode_fails: bool = False,
) -> RetrievalCallCounters:
    counters = RetrievalCallCounters()

    def _fake_scalar_encode(query: str, model_code: str) -> HybridQueryVectors:
        counters.scalar_query_encode_calls += 1
        counters.encoded_query_texts.append(query)
        return _fake_query_vectors(query)

    def _fake_batch_encode(queries, model_code: str, *, input_type: str = "query"):
        counters.batch_query_encode_calls += 1
        counters.batch_input_types.append(input_type)
        if input_type != "query":  # pragma: no cover - defensive
            counters.passage_encode_calls += 1
        counters.encoded_query_texts.extend(list(queries))
        if batch_encode_fails:
            raise RuntimeError("batch query embedding failed")
        return [_fake_query_vectors(query) for query in queries]

    monkeypatch.setattr(hybrid_module, "default_encode_hybrid_query_vectors", _fake_scalar_encode)
    monkeypatch.setattr(
        hybrid_module,
        "default_encode_hybrid_query_vectors_batch",
        _fake_batch_encode,
        raising=False,
    )

    fake_client = FakeQdrantClient(
        counters,
        points_by_query_text=points_by_query_text,
        fail=qdrant_fails,
    )
    monkeypatch.setattr(rag_service, "build_qdrant_client", lambda: fake_client)
    return counters


def _db():
    return app.state.testing_session_local()


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _register_and_login(client, email: str) -> str:
    client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": email})
    response = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
    assert response.status_code == 200
    return response.json()["access_token"]


def create_memorial_with_indexed_biography(client, email: str) -> tuple[str, int]:
    token = _register_and_login(client, email)
    created = client.post("/api/memorials", headers=_auth_headers(token), json={"name": "Batch Memorial", "canonical_language": "cs", "confirm_canonical_language": True})
    assert created.status_code == 201
    profile_id = created.json()["id"]

    patch = client.patch(
        f"/api/memorials/{profile_id}/biography",
        headers=_auth_headers(token),
        json={"biography": "Zivotopisny text pro davkovy dotaz."},
    )
    assert patch.status_code == 200
    start = client.post(f"/api/memorials/{profile_id}/biography/ingest", headers=_auth_headers(token))
    assert start.status_code == 202

    db = _db()
    try:
        result = index_biography(
            db,
            profile_id=profile_id,
            writer=FakeWriter(),
            encoder=FakeEncoder(),
            validate_runtime=False,
        )
        assert result.status == "indexed"
    finally:
        db.close()
    return token, profile_id


def request_next_question(profile_id: int, *, locale: str = "cs"):
    """Calls the service entry point directly against the isolated SQLite
    test database - identical code path to the HTTP route, without needing a
    second authenticated round trip per assertion."""

    db = _db()
    try:
        profile = db.get(MemoryProfile, profile_id)
        user = db.get(User, profile.user_id)
        return biographer_service.get_next_question(
            db,
            profile=profile,
            current_user=user,
            locale=locale,
        )
    finally:
        db.close()


def count_questions(profile_id: int) -> int:
    db = _db()
    try:
        return (
            db.query(BiographerQuestion)
            .filter(BiographerQuestion.profile_id == profile_id)
            .count()
        )
    finally:
        db.close()


# --- Phase 1: one batch query embedding per new-question request -----------


def test_new_question_request_performs_exactly_one_batched_query_embedding(client, monkeypatch):
    """RED-first regression for the exact defect: before Task 65.11.1 this
    asserted 0 batch calls / 16 scalar calls."""

    counters = install_fake_retrieval_stack(monkeypatch)
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-owner1@example.com")

    question = request_next_question(profile_id)

    assert question is not None
    assert counters.scalar_query_encode_calls == 0, (
        "AI Biographer must not perform per-topic/per-source scalar query embedding fan-out"
    )
    assert counters.batch_query_encode_calls == 1
    assert len(counters.encoded_query_texts) == len(topic_catalog.BIOGRAPHER_TOPICS) == 8
    assert counters.passage_encode_calls == 0


def test_topic_query_batch_preserves_catalog_order_and_locale(client, monkeypatch):
    counters = install_fake_retrieval_stack(monkeypatch)
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-owner2@example.com")

    request_next_question(profile_id, locale="cs")

    expected = [topic.questions["cs"] for topic in topic_catalog.BIOGRAPHER_TOPICS]
    assert counters.encoded_query_texts == expected


def test_topic_query_batch_uses_query_semantics_not_passage_semantics(client, monkeypatch):
    counters = install_fake_retrieval_stack(monkeypatch)
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-owner3@example.com")

    request_next_question(profile_id)

    assert counters.batch_input_types == ["query"]
    assert counters.passage_encode_calls == 0


def test_no_sixteen_scalar_query_embedding_regression(client, monkeypatch):
    """Explicit invariant guard (Task 65.11.1 acceptance item 12)."""

    counters = install_fake_retrieval_stack(monkeypatch)
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-owner4@example.com")

    request_next_question(profile_id)

    topic_count = len(topic_catalog.BIOGRAPHER_TOPICS)
    source_type_count = 2
    assert counters.scalar_query_encode_calls != topic_count * source_type_count, (
        "AI Biographer must not perform per-topic/per-source scalar query embedding fan-out "
        f"({topic_count} topics x {source_type_count} source types = "
        f"{topic_count * source_type_count} scalar query embeddings)"
    )
    assert counters.scalar_query_encode_calls == 0
    assert counters.batch_query_encode_calls == 1


# --- Phase 2: batched coverage retrieval ----------------------------------


def test_coverage_retrieval_issues_one_qdrant_batch_request(client, monkeypatch):
    counters = install_fake_retrieval_stack(monkeypatch)
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-owner5@example.com")

    request_next_question(profile_id)

    assert counters.qdrant_batch_search_calls == 1
    assert counters.qdrant_search_calls == 0


def test_batch_filter_scopes_owner_profile_and_both_verified_source_types(client, monkeypatch):
    counters = install_fake_retrieval_stack(monkeypatch)
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-owner6@example.com")

    request_next_question(profile_id)

    assert counters.qdrant_search_filters, "no Qdrant filter was captured"
    for search_filter in counters.qdrant_search_filters:
        must = search_filter["must"]
        keys = {condition["key"] for condition in must}
        assert "owner_user_id" in keys
        assert "profile_id" in keys
        profile_condition = next(c for c in must if c["key"] == "profile_id")
        assert profile_condition["match"]["value"] == profile_id
        source_condition = next(c for c in must if c["key"] == "source_type")
        assert sorted(source_condition["match"]["any"]) == ["biography", "conversation_candidate"]


# --- Phases 3/4: pending fast path and idempotency ------------------------


def test_pending_question_fast_path_performs_zero_retrieval(client, monkeypatch):
    counters = install_fake_retrieval_stack(monkeypatch)
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-owner7@example.com")

    first = request_next_question(profile_id)
    assert first is not None

    before_batch = counters.batch_query_encode_calls
    before_qdrant = counters.qdrant_batch_search_calls
    second = request_next_question(profile_id)

    assert second is not None
    assert second.id == first.id
    assert counters.batch_query_encode_calls == before_batch
    assert counters.qdrant_batch_search_calls == before_qdrant
    assert counters.scalar_query_encode_calls == 0
    assert count_questions(profile_id) == 1


def test_repeated_request_is_idempotent_and_creates_no_duplicate_row(client, monkeypatch):
    counters = install_fake_retrieval_stack(monkeypatch)
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-owner8@example.com")

    first = request_next_question(profile_id)
    third = request_next_question(profile_id)
    fourth = request_next_question(profile_id)

    assert first.id == third.id == fourth.id
    assert count_questions(profile_id) == 1
    assert counters.batch_query_encode_calls == 1
    assert counters.qdrant_batch_search_calls == 1


@pytest.mark.parametrize("locale", ["cs", "ru"])
def test_locale_specific_topic_queries_are_batched_in_catalog_order(client, monkeypatch, locale):
    counters = install_fake_retrieval_stack(monkeypatch)
    _token, profile_id = create_memorial_with_indexed_biography(
        client, f"batch-locale-{locale}@example.com"
    )

    request_next_question(profile_id, locale=locale)

    expected = [topic.questions[locale] for topic in topic_catalog.BIOGRAPHER_TOPICS]
    assert counters.encoded_query_texts == expected
    assert counters.batch_query_encode_calls == 1


def test_unknown_locale_falls_back_to_the_russian_catalog_text(client, monkeypatch):
    """Fallback locale behaviour is unchanged from Task 65.6."""

    counters = install_fake_retrieval_stack(monkeypatch)
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-locale-xx@example.com")

    request_next_question(profile_id, locale="de")

    expected = [topic.questions["ru"] for topic in topic_catalog.BIOGRAPHER_TOPICS]
    assert counters.encoded_query_texts == expected


# --- Real evidence fixtures: verified source types, isolation, coverage ---


def seed_evidence(
    *,
    profile_id: int,
    source_type: str,
    texts: list[str],
    title: str,
    language: str = "cs",
) -> list[tuple[int, int]]:
    """Insert real `RagSource`/`RagChunk`/`RagEmbedding` rows for a profile.

    Retrieval hydration (`rag_retrieval.repository.list_retrieval_evidence_for_embeddings`)
    reads these rows - it is the layer that actually enforces owner/profile
    scoping and the "verified/indexed only" rule - so seeding them is what
    makes the isolation assertions below meaningful rather than cosmetic.
    Returns `(embedding_id, chunk_id)` pairs, ready to be handed back as fake
    Qdrant point payloads.
    """

    db = _db()
    try:
        profile = db.get(MemoryProfile, profile_id)
        source = RagSource(
            owner_user_id=profile.user_id,
            profile_id=profile_id,
            source_type=source_type,
            title=title,
            raw_text="\n".join(texts),
            language=language,
            status="embedded",
        )
        db.add(source)
        db.flush()

        pairs: list[tuple[int, int]] = []
        for index, text in enumerate(texts):
            chunk = RagChunk(
                owner_user_id=profile.user_id,
                profile_id=profile_id,
                source_id=source.id,
                chunk_index=index,
                chunk_text=text,
                text_hash=f"hash-{source_type}-{profile_id}-{index}-{abs(hash(text)) % 10**8}",
                token_estimate=len(text) // 4,
                char_count=len(text),
                sentence_count=1,
                language=language,
                validation_status="valid",
            )
            db.add(chunk)
            db.flush()
            embedding = RagEmbedding(
                owner_user_id=profile.user_id,
                profile_id=profile_id,
                source_id=source.id,
                chunk_id=chunk.id,
                model_code="bge_m3_dense_sparse",
                vector=None,
                vector_dimension=_DENSE_DIMENSION,
                text_hash=chunk.text_hash,
                status="embedded",
            )
            db.add(embedding)
            db.flush()
            pairs.append((embedding.id, chunk.id))
        db.commit()
        return pairs
    finally:
        db.close()


def qdrant_points(pairs: list[tuple[int, int]], *, base_score: float = 0.9) -> list[dict[str, object]]:
    return [
        {
            "score": round(base_score - (index * 0.01), 4),
            "payload": {"embedding_id": embedding_id, "chunk_id": chunk_id},
        }
        for index, (embedding_id, chunk_id) in enumerate(pairs)
    ]


def points_for_topic(topic_key: str, points: list[dict[str, object]], *, locale: str = "cs"):
    topic = topic_catalog.get_topic(topic_key)
    return {topic.questions[locale]: points}


def test_only_the_two_verified_source_types_reach_the_biographer_context(client, monkeypatch):
    """Both verified source types are included, and nothing else may be."""

    assert _VERIFIED_SOURCE_TYPES == ("biography", "conversation_candidate")

    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-sources@example.com")
    biography_pairs = seed_evidence(
        profile_id=profile_id,
        source_type="biography",
        texts=["Dětství na vesnici u řeky."],
        title="Biography evidence",
    )
    # `manual_text` is a perfectly real RagSource type that must NEVER enter
    # the Biographer context package, even if Qdrant were to return its point.
    manual_pairs = seed_evidence(
        profile_id=profile_id,
        source_type="manual_text",
        texts=["Poznamka, ktera do biografa nepatri."],
        title="Manual note",
    )

    points_by_query_text = points_for_topic(
        "childhood", qdrant_points(biography_pairs + manual_pairs)
    )
    # Every other topic gets rich evidence so `childhood` (one verified
    # chunk -> `basic`) is the selected topic and its prompt is the one under
    # inspection.
    for topic in topic_catalog.BIOGRAPHER_TOPICS:
        if topic.key == "childhood":
            continue
        pairs = seed_evidence(
            profile_id=profile_id,
            source_type="biography",
            texts=[f"{topic.key}: bohaty kontext {index}." for index in range(4)],
            title=f"{topic.key} evidence",
        )
        points_by_query_text.update(points_for_topic(topic.key, qdrant_points(pairs)))

    counters = install_fake_retrieval_stack(
        monkeypatch,
        points_by_query_text=points_by_query_text,
    )

    captured = _capture_generation_prompts(monkeypatch)
    question = request_next_question(profile_id)

    assert question is not None
    assert question.topic == "childhood"
    assert counters.batch_query_encode_calls == 1
    prompt = "\n".join(captured["user_prompts"])
    assert "Dětství na vesnici u řeky." in prompt
    assert "Poznamka, ktera do biografa nepatri." not in prompt


def test_batch_search_filter_expresses_both_verified_source_types_in_one_condition():
    """Unit-level guard on the combined verified-source filter itself."""

    from app.modules.rag_retrieval.batch_query import _build_batch_search_filter

    search_filter = _build_batch_search_filter(
        owner_user_id=7,
        profile_id=42,
        language=None,
        source_types=_VERIFIED_SOURCE_TYPES,
    )
    must = search_filter["must"]
    assert {"key": "owner_user_id", "match": {"value": 7}} in must
    assert {"key": "profile_id", "match": {"value": 42}} in must
    assert {
        "key": "source_type",
        "match": {"any": ["biography", "conversation_candidate"]},
    } in must
    # Exactly one source_type condition - never a second, narrower query.
    assert sum(1 for condition in must if condition["key"] == "source_type") == 1


def test_evidence_from_another_profile_and_owner_never_enters_coverage(client, monkeypatch):
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-isolation-a@example.com")
    _other_token, other_profile_id = create_memorial_with_indexed_biography(
        client, "batch-isolation-b@example.com"
    )
    foreign_pairs = seed_evidence(
        profile_id=other_profile_id,
        source_type="biography",
        texts=[
            "Cizi memorial: prvni tajemstvi.",
            "Cizi memorial: druhe tajemstvi.",
            "Cizi memorial: treti tajemstvi.",
            "Cizi memorial: ctvrte tajemstvi.",
        ],
        title="Foreign biography",
    )

    # Worst case: Qdrant itself (wrongly) hands back the other memorial's
    # points. Owner/profile scoping in the SQL hydration must still drop them,
    # so they can neither influence coverage nor reach the prompt.
    counters = install_fake_retrieval_stack(
        monkeypatch,
        points_by_query_text=points_for_topic("childhood", qdrant_points(foreign_pairs)),
    )
    captured = _capture_generation_prompts(monkeypatch)

    question = request_next_question(profile_id)

    assert question is not None
    prompt = "\n".join(captured["user_prompts"])
    assert "Cizi memorial" not in prompt
    # Zero verified chunks for every topic -> the first catalog topic wins.
    assert question.topic == topic_catalog.BIOGRAPHER_TOPICS[0].key
    for search_filter in counters.qdrant_search_filters:
        profile_condition = next(c for c in search_filter["must"] if c["key"] == "profile_id")
        assert profile_condition["match"]["value"] == profile_id


def _capture_generation_prompts(monkeypatch) -> dict[str, list[str]]:
    """Capture the exact prompts handed to the (mock) question provider."""

    captured: dict[str, list[str]] = {"user_prompts": [], "system_prompts": []}

    class _CapturingProvider:
        provider_name = "mock"
        model = "mock"

        def generate_question(self, *, system_prompt: str, user_prompt: str) -> BiographerProviderResponse:
            captured["system_prompts"].append(system_prompt)
            captured["user_prompts"].append(user_prompt)
            return BiographerProviderResponse(
                result=ProviderQuestionResult(
                    question="Jaká konkrétní vzpomínka se vám k tomu pojí nejsilněji?",
                    known_information_used=True,
                    question_intent="specific_memory",
                    confidence="high",
                ),
                provider_name="mock",
                model="mock",
                latency_ms=0,
            )

    import app.modules.avatar_biographer.question_generation as question_generation_module

    monkeypatch.setattr(
        question_generation_module,
        "build_biographer_question_provider",
        lambda: _CapturingProvider(),
    )
    return captured


def test_education_is_selected_and_receives_only_its_own_excerpts(client, monkeypatch):
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-education@example.com")

    points_by_query_text: dict[str, list[dict[str, object]]] = {}
    for topic in topic_catalog.BIOGRAPHER_TOPICS:
        if topic.key == "education":
            continue
        pairs = seed_evidence(
            profile_id=profile_id,
            source_type="biography",
            texts=[f"{topic.key}: bohaty kontext {index}." for index in range(4)],
            title=f"{topic.key} evidence",
        )
        points_by_query_text.update(points_for_topic(topic.key, qdrant_points(pairs)))

    education_pairs = seed_evidence(
        profile_id=profile_id,
        source_type="biography",
        texts=["education: vyucil jsem se ve strojirne."],
        title="education evidence",
    )
    points_by_query_text.update(points_for_topic("education", qdrant_points(education_pairs)))

    counters = install_fake_retrieval_stack(monkeypatch, points_by_query_text=points_by_query_text)
    captured = _capture_generation_prompts(monkeypatch)

    question = request_next_question(profile_id)

    # Every topic except `education` is `rich` (4 verified chunks each);
    # `education` is `basic` (1 chunk), which outranks `rich` in
    # `_SELECTABLE_STATES_PRIORITY`.
    assert question is not None
    assert question.topic == "education"

    prompt = "\n".join(captured["user_prompts"])
    assert "education: vyucil jsem se ve strojirne." in prompt
    for other_topic in ("childhood", "family", "work", "values"):
        assert f"{other_topic}: bohaty kontext 0." not in prompt

    # The selected topic's query vectors are NOT encoded a second time.
    assert counters.batch_query_encode_calls == 1
    assert counters.scalar_query_encode_calls == 0
    assert counters.qdrant_batch_search_calls == 1


# --- Coverage parity against the existing deterministic contract ----------


def test_coverage_parity_with_the_existing_topic_selection_contract(client, monkeypatch):
    """The optimization must not change which topic is selected.

    Deterministic per-topic chunk counts (zero / one basic / four rich) plus
    the existing question-history states (answered / skipped / postponed) are
    fed through BOTH the optimized service path and the untouched
    `coverage.build_topic_coverage_map` + `coverage.select_next_topic`
    contract; the two must agree.
    """

    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-parity@example.com")

    chunk_counts = {
        "childhood": 4,
        "family": 4,
        "education": 4,
        "work": 1,
        "relationships": 0,
        "places": 4,
        "traditions": 4,
        "values": 4,
    }
    points_by_query_text: dict[str, list[dict[str, object]]] = {}
    for topic_key, chunk_count in chunk_counts.items():
        if chunk_count == 0:
            continue
        pairs = seed_evidence(
            profile_id=profile_id,
            source_type="biography",
            texts=[f"{topic_key}: chunk {index}." for index in range(chunk_count)],
            title=f"{topic_key} evidence",
        )
        points_by_query_text.update(points_for_topic(topic_key, qdrant_points(pairs)))

    # Question history: answered / skipped / postponed, plus an unresolved
    # candidate blocking one topic entirely.
    db = _db()
    try:
        for topic_key, status in (
            ("childhood", "answered"),
            ("family", "skipped"),
            ("education", "postponed"),
            ("relationships", "answered"),
        ):
            db.add(
                BiographerQuestion(
                    profile_id=profile_id,
                    topic=topic_key,
                    locale="cs",
                    question_text=f"Historicka otazka pro {topic_key}?",
                    status=status,
                )
            )
        db.commit()
    finally:
        db.close()

    install_fake_retrieval_stack(monkeypatch, points_by_query_text=points_by_query_text)
    _capture_generation_prompts(monkeypatch)

    question = request_next_question(profile_id)

    db = _db()
    try:
        all_questions = biographer_repository.list_questions_for_profile(db, profile_id=profile_id)
        pending_topics = {q.topic for q in all_questions if q.status == "pending"}
        history = [q for q in all_questions if q.status != "pending"]
        expected_coverages = coverage_module.build_topic_coverage_map(
            all_questions=history,
            verified_chunk_counts_by_topic={
                key: min(value, _CONTEXT_CHUNK_LIMIT) for key, value in chunk_counts.items()
            },
            unresolved_candidate_topic_keys=set(),
        )
        expected = coverage_module.select_next_topic(
            expected_coverages, total_questions_asked=len(history)
        )
    finally:
        db.close()

    assert question is not None
    assert expected is not None
    assert question.topic == expected.topic.key
    assert pending_topics == {expected.topic.key}


def test_pending_question_blocks_its_topic_and_returns_it_unchanged(client, monkeypatch):
    counters = install_fake_retrieval_stack(monkeypatch)
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-pending@example.com")

    first = request_next_question(profile_id)
    assert first is not None
    assert first.status == "pending"

    resumed = request_next_question(profile_id)
    assert resumed.id == first.id
    assert resumed.topic == first.topic
    assert counters.batch_query_encode_calls == 1


# --- Degraded retrieval ---------------------------------------------------


def test_batch_query_embedding_failure_degrades_to_deterministic_fallback(client, monkeypatch):
    counters = install_fake_retrieval_stack(monkeypatch, batch_encode_fails=True)
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-degraded1@example.com")

    import app.modules.avatar_biographer.question_generation as question_generation_module

    def _explode():
        raise AssertionError("provider must never be constructed when retrieval is unavailable")

    monkeypatch.setattr(question_generation_module, "build_biographer_question_provider", _explode)

    question = request_next_question(profile_id)

    assert question is not None
    assert question.generation_mode == "deterministic_fallback"
    assert question.question_text == topic_catalog.BIOGRAPHER_TOPICS[0].questions["cs"]
    # No private content and no leaked internal exception reached the caller.
    assert "batch query embedding failed" not in question.question_text
    assert counters.qdrant_batch_search_calls == 0


def test_qdrant_batch_failure_degrades_to_deterministic_fallback(client, monkeypatch):
    counters = install_fake_retrieval_stack(monkeypatch, qdrant_fails=True)
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-degraded2@example.com")

    import app.modules.avatar_biographer.question_generation as question_generation_module

    def _explode():
        raise AssertionError("provider must never be constructed when retrieval is unavailable")

    monkeypatch.setattr(question_generation_module, "build_biographer_question_provider", _explode)

    question = request_next_question(profile_id)

    assert question is not None
    assert question.generation_mode == "deterministic_fallback"
    assert counters.batch_query_encode_calls == 1
    assert counters.qdrant_batch_search_calls == 1


def test_selected_topic_hydration_failure_degrades_safely(client, monkeypatch):
    install_fake_retrieval_stack(monkeypatch)
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-degraded3@example.com")

    from app.modules.avatar_biographer import context_package as context_package_module

    def _broken_hydrate(self, topic):
        raise RuntimeError("private hydration detail 12345 must not leak")

    monkeypatch.setattr(
        context_package_module.BiographerTopicContextBatch,
        "hydrate_context_package",
        _broken_hydrate,
    )

    question = request_next_question(profile_id)

    assert question is not None
    assert question.generation_mode == "deterministic_fallback"
    assert "12345" not in question.question_text


# --- Cache independence ---------------------------------------------------


def test_model_invocation_count_stays_one_with_embedding_cache_disabled(client, monkeypatch):
    monkeypatch.setattr(settings, "embedding_cache_enabled", False)
    counters = install_fake_retrieval_stack(monkeypatch)
    _token, profile_id = create_memorial_with_indexed_biography(client, "batch-nocache@example.com")

    request_next_question(profile_id)

    assert settings.embedding_cache_enabled is False
    assert counters.batch_query_encode_calls == 1
    assert counters.scalar_query_encode_calls == 0
    assert len(counters.encoded_query_texts) == 8


# --- Structural bounds ----------------------------------------------------


def test_batch_retrieval_limit_preserves_the_previous_two_source_type_bound(client):
    assert _CONTEXT_CHUNK_LIMIT == 5
    assert _BATCH_RETRIEVAL_LIMIT == _CONTEXT_CHUNK_LIMIT * len(_VERIFIED_SOURCE_TYPES)
