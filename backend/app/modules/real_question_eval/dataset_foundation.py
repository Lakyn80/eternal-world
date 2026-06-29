from __future__ import annotations

from pathlib import Path

from app.modules.rag_quality.schemas import RagQualityEvalCase, RagQualityEvalDataset


REAL_QUESTION_EVAL_DATASET_ID = "real-question-eval-dataset"
REAL_QUESTION_EVAL_DATASET_NAME = "Real Question Evaluation Dataset"
EXTENDED_REAL_QUESTION_EVAL_DATASET_ID = "real-question-eval-extended-dataset-plan"
EXTENDED_REAL_QUESTION_EVAL_DATASET_NAME = "Real Question Evaluation Extended Dataset Plan"
EXTERNAL_EVAL_SAMPLE_DATASET_PATH = (
    Path(__file__).resolve().parent / "datasets" / "eternal_world_eval_dataset_sample.json"
)


def build_core_real_question_eval_cases() -> list[RagQualityEvalCase]:
    return [
        RagQualityEvalCase(
            case_id="question-sunflower-house",
            title="Village house flower evidence",
            query="What details show which flower was kept at the old village house and what part of the entrance is mentioned?",
            expected_markers=["sunflower seeds", "blue gate latch"],
            forbidden_markers=["rose market poster"],
            expected_behavior="retrieval_only",
            minimum_relevant_results=2,
            tags=["core", "task32", "english_query", "multi_evidence"],
        ),
        RagQualityEvalCase(
            case_id="question-winter-trip",
            title="Winter trip travel evidence",
            query="During the winter trip, what travel item was saved and what container kept everyone warm?",
            expected_markers=["overnight train ticket", "wooden thermos"],
            forbidden_markers=["summer bus timetable"],
            expected_behavior="retrieval_only",
            minimum_relevant_results=2,
            tags=["core", "task32", "english_query", "multi_evidence"],
        ),
        RagQualityEvalCase(
            case_id="question-grandmother-soup",
            title="Grandmother soup evidence",
            query="Which ingredients and cooking setup explain why grandmother's soup tasted smoky?",
            expected_markers=["dried mushrooms", "oak stove"],
            forbidden_markers=["vanilla jam"],
            expected_behavior="retrieval_only",
            minimum_relevant_results=2,
            tags=["core", "task32", "english_query", "distractor_heavy"],
        ),
    ]


def build_default_real_question_eval_dataset() -> RagQualityEvalDataset:
    return RagQualityEvalDataset(
        dataset_id=REAL_QUESTION_EVAL_DATASET_ID,
        name=REAL_QUESTION_EVAL_DATASET_NAME,
        description="Default deterministic fictional smoke/regression dataset for real question evaluation.",
        project_name="Eternal World / Vechniy Mir",
        cases=build_core_real_question_eval_cases(),
        metadata={
            "default_smoke_dataset": True,
            "external_dataset_supported": True,
        },
    )


def build_extended_real_question_eval_dataset() -> RagQualityEvalDataset:
    planned_cases = [
        RagQualityEvalCase(
            case_id="planned-short-factual-lookup",
            title="Planned short factual lookup",
            query="Which station lantern color was recorded in the archive note?",
            expected_markers=["amber lantern"],
            forbidden_markers=["silver whistle"],
            expected_behavior="retrieval_only",
            minimum_relevant_results=1,
            tags=["planned", "short_factual_lookup", "english_query"],
            metadata={"planned_only": True, "category": "short factual lookup"},
        ),
        RagQualityEvalCase(
            case_id="planned-distractor-heavy-czech",
            title="Planned Czech distractor-heavy question",
            query="Ktery predmet zustal v zasuvce a ktera poznamka byla jen matouci plakat?",
            expected_markers=["mosazny klic"],
            forbidden_markers=["cerveny jarmarecni plakat"],
            expected_behavior="retrieval_only",
            minimum_relevant_results=1,
            tags=["planned", "czech_query", "distractor_heavy"],
            metadata={"planned_only": True, "category": "Czech query"},
        ),
        RagQualityEvalCase(
            case_id="planned-russian-conflict",
            title="Planned Russian similar-document conflict question",
            query="Kakaya zapis podtverzhdaet pravilnuyu datu otpravleniya, a kakaya pohozhaya zapis yavlyaetsya konfliktnoy?",
            expected_markers=["pravilnaya data otpravleniya"],
            forbidden_markers=["staryi chernovik daty"],
            expected_behavior="retrieval_only",
            minimum_relevant_results=1,
            tags=["planned", "russian_query", "similar_document_conflict"],
            metadata={"planned_only": True, "category": "Russian query"},
        ),
        RagQualityEvalCase(
            case_id="planned-answer-not-available",
            title="Planned answer-not-available question",
            query="What was the exact serial number of the missing brass compass?",
            expected_markers=[],
            forbidden_markers=["invented serial number"],
            expected_behavior="lack_of_evidence",
            minimum_relevant_results=0,
            tags=["planned", "answer_not_available", "english_query"],
            metadata={"planned_only": True, "category": "answer-not-available question"},
        ),
        RagQualityEvalCase(
            case_id="planned-long-context-distant-evidence",
            title="Planned long-context distant evidence question",
            query="Which two distant archive details together explain why the river meeting was delayed?",
            expected_markers=["flooded footbridge", "late telegraph reply"],
            forbidden_markers=["harvest parade rumor"],
            expected_behavior="retrieval_only",
            minimum_relevant_results=2,
            tags=["planned", "long_context", "distant_evidence", "multi_evidence"],
            metadata={"planned_only": True, "category": "long-context / distant evidence question"},
        ),
    ]

    return RagQualityEvalDataset(
        dataset_id=EXTENDED_REAL_QUESTION_EVAL_DATASET_ID,
        name=EXTENDED_REAL_QUESTION_EVAL_DATASET_NAME,
        description="Planning-only extended dataset foundation for the future full-version embedding benchmark. Not connected to default real eval runs.",
        project_name="Eternal World / Vechniy Mir",
        cases=[*build_core_real_question_eval_cases(), *planned_cases],
        metadata={
            "planned_categories": [
                "short factual lookup",
                "multi-evidence question",
                "distractor-heavy question",
                "Czech query",
                "Russian query",
                "English query",
                "answer-not-available question",
                "similar-document conflict question",
                "long-context / distant evidence question",
            ],
            "manual_only_real_benchmark": True,
            "connected_to_default_real_runs": False,
        },
    )
