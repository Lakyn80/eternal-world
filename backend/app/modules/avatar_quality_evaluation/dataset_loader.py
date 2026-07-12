from __future__ import annotations

import json
from pathlib import Path

from app.modules.avatar_quality_evaluation.schemas import AvatarEvalCase, AvatarEvalCategory


REQUIRED_AVATAR_EVAL_CATEGORIES: frozenset[AvatarEvalCategory] = frozenset(
    {
        "original_seeded_memory",
        "learned_indexed_memory",
        "owner_corrected_memory",
        "multiple_perspectives",
        "pending_unindexed_memory",
        "rejected_memory",
        "private_memory_blocked",
        "unknown_factual_question",
        "emotional_persona_question",
        "sensitive_subject",
        "repeat_answer_stability",
        "profile_isolation",
    }
)


class AvatarEvalDatasetError(ValueError):
    pass


def load_avatar_eval_dataset(path: Path) -> list[AvatarEvalCase]:
    if not path.exists():
        raise AvatarEvalDatasetError(f"Avatar eval dataset does not exist: {path}")
    if not path.is_file():
        raise AvatarEvalDatasetError(f"Avatar eval dataset path is not a file: {path}")

    cases: list[AvatarEvalCase] = []
    seen_ids: set[str] = set()
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        try:
            payload = json.loads(line)
            case = AvatarEvalCase.model_validate(payload)
        except Exception as exc:
            raise AvatarEvalDatasetError(
                f"Invalid avatar eval dataset row at line {line_number}: {exc}"
            ) from exc
        if case.id in seen_ids:
            raise AvatarEvalDatasetError(f"Duplicate avatar eval case id: {case.id}")
        seen_ids.add(case.id)
        cases.append(case)

    if not cases:
        raise AvatarEvalDatasetError("Avatar eval dataset must contain at least one case")

    present_categories = {case.category for case in cases}
    missing_categories = sorted(REQUIRED_AVATAR_EVAL_CATEGORIES - present_categories)
    if missing_categories:
        raise AvatarEvalDatasetError(
            "Avatar eval dataset is missing required categories: "
            + ", ".join(missing_categories)
        )

    return cases
