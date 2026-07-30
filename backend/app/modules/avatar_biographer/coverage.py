"""Deterministic topic coverage evaluation and selection (Task 65.6).

Coverage is derived entirely from already-persisted rows (`BiographerQuestion`
history plus a verified-evidence chunk count per topic) - no new table, no
LLM call, per the roadmap's instruction to "prefer deriving coverage from
verified indexed source evidence... previous questions... skipped/postponed
questions... active candidate". An LLM later helps write one topic's
*question text*; which topic is next, and how covered it already is, stay
plain deterministic arithmetic so they remain unit-testable without a model
and cannot themselves hallucinate a wrong topic choice.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from app.db.models import BiographerQuestion
from app.modules.avatar_biographer.topics import BIOGRAPHER_TOPICS, BiographerTopic


class TopicCoverageState(str, Enum):
    NOT_STARTED = "not_started"
    WEAK = "weak"
    BASIC = "basic"
    RICH = "rich"
    SKIPPED = "skipped"
    POSTPONED = "postponed"
    EXHAUSTED = "exhausted"


#: A postponed topic becomes selectable again once at least this many
#: questions for *other* topics have since been asked - a small
#: deterministic cool-down (not a wall-clock timer) so it stays exercisable
#: in tests without sleeping.
POSTPONE_COOLDOWN_QUESTIONS = 2

#: A topic backed by this many or more verified retrieved chunks is
#: considered richly covered by the indexed biography/approved memories.
RICH_EVIDENCE_CHUNK_THRESHOLD = 4
BASIC_EVIDENCE_CHUNK_THRESHOLD = 1

#: Once a topic has been asked this many times, deprioritize it below every
#: not-yet-covered topic (see `_REVISIT_STATES_PRIORITY`) - prevents an
#: unbounded loop repeatedly asking about the same topic before every other
#: topic has had a turn, without ever making the topic permanently
#: unselectable.
MAX_QUESTIONS_PER_TOPIC = 3

_ACTIVE_CANDIDATE_STATUSES = frozenset({"needs_review"})


@dataclass(frozen=True)
class TopicCoverage:
    topic: BiographerTopic
    state: TopicCoverageState
    verified_chunk_count: int
    questions_asked: int
    questions_answered: int
    questions_skipped: int
    questions_postponed: int
    #: True when this exact topic currently has a pending question or an
    #: unresolved candidate tied to it - it must not be re-selected right
    #: now, independent of how much evidence already exists for it.
    blocked_from_selection: bool
    last_question_sequence: int | None


def _questions_by_topic(questions: list[BiographerQuestion]) -> dict[str, list[BiographerQuestion]]:
    by_topic: dict[str, list[BiographerQuestion]] = {}
    for question in questions:
        by_topic.setdefault(question.topic, []).append(question)
    return by_topic


def evaluate_topic_coverage(
    *,
    topic: BiographerTopic,
    topic_questions: list[BiographerQuestion],
    verified_chunk_count: int,
    has_unresolved_candidate_for_topic: bool,
    sequence_by_question_id: dict[int, int],
) -> TopicCoverage:
    questions_asked = len(topic_questions)
    questions_answered = sum(1 for q in topic_questions if q.status == "answered")
    questions_skipped = sum(1 for q in topic_questions if q.status == "skipped")
    questions_postponed = sum(1 for q in topic_questions if q.status == "postponed")
    has_pending = any(q.status == "pending" for q in topic_questions)
    last_sequence = max(
        (sequence_by_question_id[q.id] for q in topic_questions if q.id in sequence_by_question_id),
        default=None,
    )

    blocked_from_selection = has_pending or has_unresolved_candidate_for_topic

    if blocked_from_selection:
        state = TopicCoverageState.NOT_STARTED if questions_asked == 0 else TopicCoverageState.WEAK
        if verified_chunk_count >= RICH_EVIDENCE_CHUNK_THRESHOLD:
            state = TopicCoverageState.RICH
        elif verified_chunk_count >= BASIC_EVIDENCE_CHUNK_THRESHOLD:
            state = TopicCoverageState.BASIC
    elif questions_asked >= MAX_QUESTIONS_PER_TOPIC:
        state = TopicCoverageState.EXHAUSTED
    elif questions_skipped > 0 and questions_answered == 0 and questions_postponed == 0:
        state = TopicCoverageState.SKIPPED
    elif questions_postponed > 0 and questions_postponed >= questions_answered:
        state = TopicCoverageState.POSTPONED
    elif verified_chunk_count >= RICH_EVIDENCE_CHUNK_THRESHOLD:
        state = TopicCoverageState.RICH
    elif verified_chunk_count >= BASIC_EVIDENCE_CHUNK_THRESHOLD or questions_answered > 0:
        state = TopicCoverageState.BASIC
    elif questions_asked > 0:
        state = TopicCoverageState.WEAK
    else:
        state = TopicCoverageState.NOT_STARTED

    return TopicCoverage(
        topic=topic,
        state=state,
        verified_chunk_count=verified_chunk_count,
        questions_asked=questions_asked,
        questions_answered=questions_answered,
        questions_skipped=questions_skipped,
        questions_postponed=questions_postponed,
        blocked_from_selection=blocked_from_selection,
        last_question_sequence=last_sequence,
    )


def build_topic_coverage_map(
    *,
    all_questions: list[BiographerQuestion],
    verified_chunk_counts_by_topic: dict[str, int],
    unresolved_candidate_topic_keys: set[str],
) -> list[TopicCoverage]:
    """One `TopicCoverage` per catalog topic, in fixed catalog order.

    `all_questions` must be every `BiographerQuestion` row for the profile,
    ordered by `asked_at`/`id` ascending (used both to bucket per-topic
    history and to compute the postpone cool-down sequence number).
    """

    questions_by_topic = _questions_by_topic(all_questions)
    sequence_by_question_id = {question.id: index for index, question in enumerate(all_questions)}
    return [
        evaluate_topic_coverage(
            topic=topic,
            topic_questions=questions_by_topic.get(topic.key, []),
            verified_chunk_count=verified_chunk_counts_by_topic.get(topic.key, 0),
            has_unresolved_candidate_for_topic=topic.key in unresolved_candidate_topic_keys,
            sequence_by_question_id=sequence_by_question_id,
        )
        for topic in BIOGRAPHER_TOPICS
    ]


def _postpone_cooldown_elapsed(coverage: TopicCoverage, *, total_questions_asked: int) -> bool:
    if coverage.last_question_sequence is None:
        return True
    questions_since = total_questions_asked - 1 - coverage.last_question_sequence
    return questions_since >= POSTPONE_COOLDOWN_QUESTIONS


_SELECTABLE_STATES_PRIORITY = (
    TopicCoverageState.NOT_STARTED,
    TopicCoverageState.WEAK,
    TopicCoverageState.BASIC,
    TopicCoverageState.POSTPONED,
)

#: Business rule: the Biographer conversation must never present a
#: permanent "nothing left to ask" dead end - once every catalog topic has
#: reached one of these states, they become a last-resort tier instead of
#: making the topic forever unselectable. Without this, a biography whose
#: text already reads as covering most topics well (`rich` evidence found
#: on the very first evaluation, before the owner was ever asked about that
#: topic directly) reaches an all-topics-covered dead end after only one or
#: two real questions - the frontend then has no way to offer another
#: question at all. The same postpone cool-down (`_postpone_cooldown_elapsed`)
#: still applies, so a just-covered topic is not immediately re-asked.
_REVISIT_STATES_PRIORITY = (
    TopicCoverageState.RICH,
    TopicCoverageState.SKIPPED,
    TopicCoverageState.EXHAUSTED,
)


def select_next_topic(
    coverages: list[TopicCoverage],
    *,
    total_questions_asked: int,
) -> TopicCoverage | None:
    """Deterministic priority selection (Part D.15 of the task spec).

    1. never-started topics, 2. weak, 3. basic (a useful gap remains),
    4. postponed topics whose cool-down has elapsed. Order within a
    priority band follows the fixed catalog order - "childhood-first" no
    longer holds structurally, since any topic (not only `childhood`) can
    occupy the highest-priority band depending on what has actually been
    covered so far.

    If none of the above are selectable, every topic has been richly
    covered, skipped, or exhausted - fall back to revisiting the one that
    has gone longest without a question (never-asked-directly topics, i.e.
    `last_question_sequence is None`, come first) once its cool-down has
    elapsed, rather than returning `None`. Topics currently
    `blocked_from_selection` are never offered by either tier. `None` is
    only ever returned when literally every topic is blocked - the caller
    (`avatar_biographer.service.get_next_question`) turns that into an
    explicit `candidate_waiting_for_review` block, never a bare "done".
    """

    for state in _SELECTABLE_STATES_PRIORITY:
        for coverage in coverages:
            if coverage.blocked_from_selection or coverage.state != state:
                continue
            if state == TopicCoverageState.POSTPONED and not _postpone_cooldown_elapsed(
                coverage, total_questions_asked=total_questions_asked
            ):
                continue
            return coverage

    revisit_candidates = [
        coverage
        for coverage in coverages
        if not coverage.blocked_from_selection and coverage.state in _REVISIT_STATES_PRIORITY
    ]
    if not revisit_candidates:
        return None
    ready = [
        coverage
        for coverage in revisit_candidates
        if _postpone_cooldown_elapsed(coverage, total_questions_asked=total_questions_asked)
    ]
    pool = ready or revisit_candidates
    return min(
        pool,
        key=lambda coverage: (
            -1 if coverage.last_question_sequence is None else coverage.last_question_sequence
        ),
    )
