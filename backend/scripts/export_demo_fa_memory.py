from __future__ import annotations

import argparse
import json
import os
from collections.abc import Iterable
from pathlib import Path

from sqlalchemy import create_engine, select
from sqlalchemy.engine import make_url
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.db.models import ActiveRetrievalConfig, MemoryProfile, RagChunk, RagSource


DEFAULT_MARKDOWN_FILENAME = "client_demo_family_avatar_memory_ru.md"
DEFAULT_JSON_FILENAME = "client_demo_family_avatar_memory_ru.json"

TOPIC_CANDIDATES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("детство", ("детств",)),
    ("Попице", ("Попице", "Попиц")),
    ("Микулов", ("Микулов",)),
    ("учёба", ("педагогический факультет", "диплом", "учёбы")),
    ("Павел", ("Павел",)),
    ("свадьба", ("Свадьба", "свадьбы")),
    ("дети", ("Тереза", "Мартин")),
    ("Клара", ("Клара", "Клар")),
    ("учительница литературы", ("литературу", "читательский кружок")),
    ("гитара", ("Гитар",)),
    ("сад", ("сад", "лаванд", "сушёные яблоки")),
    ("путешествия", ("Балатона", "Вену", "Будапешт", "Пьештянах")),
    ("дом", ("Дом в Ржечковицах", "дом в Ржечковицах")),
    ("Ржечковицы", ("Ржечковиц",)),
    ("семейные ритуалы", ("Каждое воскресенье", "колядку", "варенье")),
    ("здоровье", ("сердечный шум", "реабилитацию", "госпитализацию")),
    ("последние годы", ("Последние годы", "Завершение жизни")),
    ("личность", ("Личность", "книга — более надёжный спутник")),
    ("семья сегодня", ("Семья сегодня",)),
    ("факты, которых в памяти нет", ("Никогда не", "нет записи", "не помнила")),
)

QUESTION_CANDIDATES: tuple[dict[str, object], ...] = (
    {
        "question": "Где ты жила в детстве?",
        "expected_behavior": "answerable",
        "required_terms": ("Попице",),
    },
    {
        "question": "Чем ты помогала матери на рынке в Микулове?",
        "expected_behavior": "answerable",
        "required_terms": ("Микулове", "абрикосы"),
    },
    {
        "question": "Что чинил твой отец Франтишек в гараже?",
        "expected_behavior": "answerable",
        "required_terms": ("Франтишек", "часы"),
    },
    {
        "question": "Когда ты окончила начальную школу в Микулове?",
        "expected_behavior": "answerable",
        "required_terms": ("Микулове", "1962"),
    },
    {
        "question": "Когда ты получила диплом в Брно?",
        "expected_behavior": "answerable",
        "required_terms": ("диплом", "1972"),
    },
    {
        "question": "Как ты познакомилась с Павлом?",
        "expected_behavior": "answerable",
        "required_terms": ("Павлом", "Лидицкой"),
    },
    {
        "question": "Когда состоялась свадьба и где она прошла?",
        "expected_behavior": "answerable",
        "required_terms": ("16 сентября 1972", "часовне святого Вацлава"),
    },
    {
        "question": "Когда родилась Тереза?",
        "expected_behavior": "answerable",
        "required_terms": ("Тереза", "14 марта 1974"),
    },
    {
        "question": "Когда родилась внучка Клара?",
        "expected_behavior": "answerable",
        "required_terms": ("Клара", "2003"),
    },
    {
        "question": "Где ты преподавала литературу после назначения?",
        "expected_behavior": "answerable",
        "required_terms": ("преподавала литературу", "Лишни"),
    },
    {
        "question": "Когда ты ушла на пенсию?",
        "expected_behavior": "answerable",
        "required_terms": ("пенсию", "2000"),
    },
    {
        "question": "Когда ты купила гитару?",
        "expected_behavior": "answerable",
        "required_terms": ("Гитару", "1975"),
    },
    {
        "question": "Что было на строительном плане дома в Ржечковицах?",
        "expected_behavior": "answerable",
        "required_terms": ("Строительный план", "Павла Новака"),
    },
    {
        "question": "Какой семейный ритуал был у тебя по воскресеньям в девять часов?",
        "expected_behavior": "answerable",
        "required_terms": ("Каждое воскресенье", "девять часов"),
    },
    {
        "question": "Когда врач впервые диагностировал у тебя сердечный шум?",
        "expected_behavior": "answerable",
        "required_terms": ("сердечный шум", "2015"),
    },
    {
        "question": "Когда ты умерла и где это произошло?",
        "expected_behavior": "answerable",
        "required_terms": ("умерла", "3 октября 2020"),
    },
    {
        "question": "Была ли ты когда-нибудь в Париже?",
        "expected_behavior": "lack_of_evidence_or_negative",
        "required_terms": ("не была в Париже",),
    },
    {
        "question": "Был ли Павел во Вьетнаме?",
        "expected_behavior": "lack_of_evidence_or_negative",
        "required_terms": ("Павел никогда не был во Вьетнаме",),
    },
    {
        "question": "Был ли у вашей семьи пёс по имени Азор?",
        "expected_behavior": "lack_of_evidence_or_negative",
        "required_terms": ("собаки по имени Азор",),
    },
    {
        "question": "Был ли у тебя брат или сестра?",
        "expected_behavior": "lack_of_evidence_or_negative",
        "required_terms": ("не было брата или сестры",),
    },
    {
        "question": "Жила ли ты когда-нибудь в Лондоне?",
        "expected_behavior": "lack_of_evidence_or_negative",
        "required_terms": ("Никогда не посещала Париж и Лондон",),
    },
)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export the seeded Russian Family Avatar demo memory without modifying runtime data."
    )
    parser.add_argument("--profile-id", type=int, required=True)
    parser.add_argument("--source-id", type=int, required=True)
    parser.add_argument("--output-dir", type=str, default=None)
    return parser.parse_args()


def _resolve_output_dir(raw_output_dir: str | None) -> Path:
    backend_dir = Path(__file__).resolve().parents[1]
    if raw_output_dir is None:
        return backend_dir / "artifacts" / "demo_exports"

    output_dir = Path(raw_output_dir)
    if output_dir.is_absolute():
        return output_dir

    current_dir = Path.cwd().resolve()
    if current_dir.name == "backend" and output_dir.parts and output_dir.parts[0] == "backend":
        output_dir = Path(*output_dir.parts[1:])

    return (current_dir / output_dir).resolve()


def _build_session_factory() -> sessionmaker:
    database_url = settings.database_url
    parsed_url = make_url(database_url)

    if (
        parsed_url.host == "db"
        and os.name == "nt"
        and not Path("/.dockerenv").exists()
    ):
        database_url = parsed_url.set(host="localhost", port=5543).render_as_string(hide_password=False)

    engine = create_engine(
        database_url,
        pool_pre_ping=True,
        echo=False,
    )
    return sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
        expire_on_commit=False,
    )


def _load_profile_source_and_chunks(*, profile_id: int, source_id: int) -> tuple[MemoryProfile, RagSource, ActiveRetrievalConfig, list[RagChunk]]:
    session_factory = _build_session_factory()
    with session_factory() as db:
        profile = db.get(MemoryProfile, profile_id)
        if profile is None:
            raise RuntimeError(f"Memory profile {profile_id} was not found.")

        source = db.get(RagSource, source_id)
        if source is None:
            raise RuntimeError(f"RAG source {source_id} was not found.")
        if source.profile_id != profile_id:
            raise RuntimeError(
                f"RAG source {source_id} belongs to profile {source.profile_id}, not to requested profile {profile_id}."
            )

        active_config = db.scalar(
            select(ActiveRetrievalConfig).where(ActiveRetrievalConfig.profile_id == profile_id)
        )
        if active_config is None:
            raise RuntimeError(f"Active retrieval config for profile {profile_id} was not found.")

        chunks = list(
            db.scalars(
                select(RagChunk)
                .where(RagChunk.source_id == source_id, RagChunk.profile_id == profile_id)
                .order_by(RagChunk.chunk_index.asc(), RagChunk.id.asc())
            )
        )
        if not chunks:
            raise RuntimeError(f"No chunks were found for source {source_id}.")

        return profile, source, active_config, chunks


def _parse_sections(raw_text: str) -> list[dict[str, str]]:
    sections: list[dict[str, str]] = []
    current_title: str | None = None
    current_lines: list[str] = []

    for line in raw_text.splitlines():
        if line.startswith("## "):
            if current_title is not None:
                sections.append(
                    {
                        "title": current_title,
                        "text": "\n".join(current_lines).strip(),
                    }
                )
            current_title = line[3:].strip()
            current_lines = []
            continue
        current_lines.append(line)

    if current_title is not None:
        sections.append(
            {
                "title": current_title,
                "text": "\n".join(current_lines).strip(),
            }
        )

    return sections


def _derive_topics(raw_text: str) -> list[str]:
    topics: list[str] = []
    for label, terms in TOPIC_CANDIDATES:
        if any(term in raw_text for term in terms):
            topics.append(label)
    return topics


def _select_questions(raw_text: str) -> list[dict[str, str]]:
    selected_questions: list[dict[str, str]] = []
    for candidate in QUESTION_CANDIDATES:
        required_terms = tuple(str(term) for term in candidate["required_terms"])
        if all(term in raw_text for term in required_terms):
            selected_questions.append(
                {
                    "question": str(candidate["question"]),
                    "expected_behavior": str(candidate["expected_behavior"]),
                }
            )
    return selected_questions


def _build_markdown(
    *,
    profile: MemoryProfile,
    source: RagSource,
    active_config: ActiveRetrievalConfig,
    chunks: list[RagChunk],
    sections: list[dict[str, str]],
    topics: list[str],
    suggested_questions: list[dict[str, str]],
) -> str:
    answerable_questions = [
        item["question"] for item in suggested_questions if item["expected_behavior"] == "answerable"
    ]
    lack_questions = [
        item["question"]
        for item in suggested_questions
        if item["expected_behavior"] == "lack_of_evidence_or_negative"
    ]

    lines: list[str] = [
        "# Память тестового цифрового аватара",
        "",
        "Это демонстрационный аватар.",
        "Он отвечает только на основе подготовленных воспоминаний и архивных фрагментов.",
        "Если информации нет или в памяти есть явное отрицание, аватар должен сказать об этом честно и не придумывать детали.",
        "",
        f"- Профиль: `{profile.id}` — {profile.name}",
        f"- Источник: `{source.id}` — {source.title}",
        f"- Коллекция: `{active_config.collection_name}`",
        f"- Indexed chunks: `{len(chunks)}`",
        "",
        "## Что знает аватар",
        "",
        "Ниже приведён точный текст источника, который загружен для тестового RU-аватара:",
        "",
    ]

    for section in sections:
        lines.append(f"### {section['title']}")
        lines.append("")
        lines.append(section["text"])
        lines.append("")

    lines.extend(
        [
            "## Основные темы",
            "",
        ]
    )
    lines.extend([f"- {topic}" for topic in topics])
    lines.append("")
    lines.extend(
        [
            "## Примеры вопросов",
            "",
            "Вопросы, на которые аватар должен уметь ответить:",
            "",
        ]
    )
    lines.extend([f"- {question}" for question in answerable_questions])
    lines.append("")
    lines.extend(
        [
            "Вопросы, на которые аватар должен ответить отрицательно или сказать, что подтверждения нет:",
            "",
        ]
    )
    lines.extend([f"- {question}" for question in lack_questions])
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _build_json_payload(
    *,
    profile: MemoryProfile,
    source: RagSource,
    active_config: ActiveRetrievalConfig,
    chunks: Iterable[RagChunk],
    topics: list[str],
    suggested_questions: list[dict[str, str]],
) -> dict[str, object]:
    return {
        "profile_id": profile.id,
        "profile_name": profile.name,
        "source_id": source.id,
        "source_title": source.title,
        "collection_name": active_config.collection_name,
        "retrieval_mode": active_config.retrieval_mode,
        "top_k": active_config.top_k,
        "chunk_count": len(list(chunks)) if not isinstance(chunks, list) else len(chunks),
        "raw_text": source.raw_text,
        "topics": topics,
        "suggested_questions": suggested_questions,
        "chunks": [
            {
                "chunk_id": str(chunk.id),
                "chunk_index": chunk.chunk_index,
                "text": chunk.chunk_text,
                "text_hash": chunk.text_hash,
            }
            for chunk in chunks
        ],
    }


def main() -> None:
    args = _parse_args()
    output_dir = _resolve_output_dir(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    profile, source, active_config, chunks = _load_profile_source_and_chunks(
        profile_id=args.profile_id,
        source_id=args.source_id,
    )
    sections = _parse_sections(source.raw_text)
    topics = _derive_topics(source.raw_text)
    suggested_questions = _select_questions(source.raw_text)

    markdown_path = output_dir / DEFAULT_MARKDOWN_FILENAME
    json_path = output_dir / DEFAULT_JSON_FILENAME

    markdown_path.write_text(
        _build_markdown(
            profile=profile,
            source=source,
            active_config=active_config,
            chunks=chunks,
            sections=sections,
            topics=topics,
            suggested_questions=suggested_questions,
        ),
        encoding="utf-8",
    )
    json_path.write_text(
        json.dumps(
            _build_json_payload(
                profile=profile,
                source=source,
                active_config=active_config,
                chunks=chunks,
                topics=topics,
                suggested_questions=suggested_questions,
            ),
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"markdown_path={markdown_path}")
    print(f"json_path={json_path}")
    print(f"profile_id={profile.id}")
    print(f"source_id={source.id}")
    print(f"collection_name={active_config.collection_name}")
    print(f"chunk_count={len(chunks)}")


if __name__ == "__main__":
    main()
