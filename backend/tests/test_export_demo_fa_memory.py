from __future__ import annotations

from scripts.export_demo_fa_memory import (
    _build_json_payload,
    _derive_topics,
    _parse_sections,
    _resolve_output_dir,
    _select_questions,
)


def test_parse_sections_extracts_markdown_sections():
    sections = _parse_sections(
        "## Детство\nЖила у Попице.\n\n## Учёба\nУчилась в Брно.\n"
    )

    assert sections == [
        {"title": "Детство", "text": "Жила у Попице."},
        {"title": "Учёба", "text": "Училась в Брно."},
    ]


def test_derive_topics_detects_grounded_demo_topics():
    topics = _derive_topics(
        "В детстве Ева жила у Попице. После учёбы в Брно она преподавала литературу."
    )

    assert "детство" in topics
    assert "Попице" in topics
    assert "учёба" in topics


def test_select_questions_only_returns_questions_supported_by_source_text():
    questions = _select_questions(
        "В детстве Ева жила у Попице. Павел никогда не был во Вьетнаме."
    )

    assert {"question": "Где ты жила в детстве?", "expected_behavior": "answerable"} in questions
    assert {
        "question": "Был ли Павел во Вьетнаме?",
        "expected_behavior": "lack_of_evidence_or_negative",
    } in questions


def test_resolve_output_dir_keeps_backend_relative_paths_stable(monkeypatch, tmp_path):
    backend_dir = tmp_path / "backend"
    backend_dir.mkdir()
    monkeypatch.chdir(backend_dir)

    resolved = _resolve_output_dir("backend/artifacts/demo_exports")

    assert resolved == backend_dir / "artifacts" / "demo_exports"


def test_build_json_payload_includes_chunk_metadata():
    profile = type("Profile", (), {"id": 8, "name": "Eva Novakova"})()
    source = type(
        "Source",
        (),
        {
            "id": 7,
            "title": "Family Novak RU E2E Corpus",
            "raw_text": "В детстве Ева жила у Попице.",
        },
    )()
    active_config = type(
        "Config",
        (),
        {
            "collection_name": "eternal_world_rag_chunks__bge_m3_dense_sparse__family_novak_ru_e2e_v3_bge_m3_real_cpu",
            "retrieval_mode": "bge_m3_dense_sparse",
            "top_k": 5,
        },
    )()
    chunks = [
        type(
            "Chunk",
            (),
            {
                "id": 27618,
                "chunk_index": 0,
                "chunk_text": "В детстве Ева жила у Попице.",
                "text_hash": "hash-27618",
            },
        )()
    ]

    payload = _build_json_payload(
        profile=profile,
        source=source,
        active_config=active_config,
        chunks=chunks,
        topics=["детство", "Попице"],
        suggested_questions=[{"question": "Где ты жила в детстве?", "expected_behavior": "answerable"}],
    )

    assert payload["profile_id"] == 8
    assert payload["source_id"] == 7
    assert payload["chunk_count"] == 1
    assert payload["chunks"] == [
        {
            "chunk_id": "27618",
            "chunk_index": 0,
            "text": "В детстве Ева жила у Попице.",
            "text_hash": "hash-27618",
        }
    ]
