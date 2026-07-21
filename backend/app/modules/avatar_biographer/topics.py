"""Bounded AI Biographer topic/question catalog (Task 65.2).

Deliberately a small, fixed, human-curated catalog rather than an
LLM-generated open-ended question stream: the roadmap requires "one
question at a time" over a "bounded topic/progress model", not unlimited
random questions, and a fixed catalog is directly unit-testable without a
model call (matching the existing `family_memory_enrichment.clarification`
fixed-catalog pattern for clarification questions). Each topic maps to a
`family_memory_enrichment.enums.MemoryType` value that decides whether the
resulting candidate ever asks a required clarification question - only
`childhood` does today (reusing the `CHILDHOOD_MEMORY_QUESTIONS` bank),
every other topic uses `general` (no required clarification), which is a
valid, deliberately minimal choice, not a placeholder bug.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BiographerTopic:
    key: str
    memory_type: str
    questions: dict[str, str]


#: Order matters: topics are offered in this fixed sequence, once per
#: memorial (see `avatar_biographer.service.get_next_question`).
BIOGRAPHER_TOPICS: tuple[BiographerTopic, ...] = (
    BiographerTopic(
        key="childhood",
        memory_type="childhood_memory",
        questions={
            "cs": "Kde jste prožil/a dětství a na co si z té doby nejvíc vzpomínáte?",
            "ru": "Где вы провели детство и что вам больше всего запомнилось из того времени?",
        },
    ),
    BiographerTopic(
        key="family",
        memory_type="general",
        questions={
            "cs": "Povězte mi něco o vaší rodině - kdo ve vašem životě hrál nejdůležitější roli?",
            "ru": "Расскажите немного о вашей семье - кто сыграл самую важную роль в вашей жизни?",
        },
    ),
    BiographerTopic(
        key="education",
        memory_type="general",
        questions={
            "cs": "Jaké bylo vaše vzdělání a je na něj nějaká vzpomínka, která vám utkvěla?",
            "ru": "Каким было ваше образование и есть ли воспоминание о нём, которое вам запомнилось?",
        },
    ),
    BiographerTopic(
        key="work",
        memory_type="general",
        questions={
            "cs": "Čím jste se v životě živil/a a co vás na té práci nejvíc bavilo?",
            "ru": "Чем вы занимались по работе и что вам в этом больше всего нравилось?",
        },
    ),
    BiographerTopic(
        key="relationships",
        memory_type="general",
        questions={
            "cs": "Kdo byli lidé, na kterých vám v životě nejvíc záleželo?",
            "ru": "Кто были люди, которые значили для вас больше всего в жизни?",
        },
    ),
    BiographerTopic(
        key="places",
        memory_type="general",
        questions={
            "cs": "Je nějaké místo, které pro vás bylo obzvlášť důležité?",
            "ru": "Есть ли место, которое было для вас особенно важным?",
        },
    ),
    BiographerTopic(
        key="traditions",
        memory_type="general",
        questions={
            "cs": "Měla vaše rodina nějaké tradice nebo zvyky, na které rádi vzpomínáte?",
            "ru": "Были ли у вашей семьи традиции или обычаи, которые вам приятно вспоминать?",
        },
    ),
    BiographerTopic(
        key="values",
        memory_type="general",
        questions={
            "cs": "Co je pro vás v životě nejdůležitější a co byste chtěl/a předat dalším generacím?",
            "ru": "Что для вас важнее всего в жизни и что вы хотели бы передать следующим поколениям?",
        },
    ),
)

_TOPICS_BY_KEY: dict[str, BiographerTopic] = {topic.key: topic for topic in BIOGRAPHER_TOPICS}


def get_topic(key: str) -> BiographerTopic | None:
    return _TOPICS_BY_KEY.get(key)


def question_text_for(topic: BiographerTopic, *, locale: str) -> str:
    return topic.questions.get(locale, topic.questions["ru"])


def next_unused_topic(*, used_topic_keys: set[str]) -> BiographerTopic | None:
    for topic in BIOGRAPHER_TOPICS:
        if topic.key not in used_topic_keys:
            return topic
    return None
