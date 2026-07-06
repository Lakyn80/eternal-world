from __future__ import annotations

from app.modules.rag_evaluation.fixtures.family_avatar_cases import (
    FAMILY_AVATAR_EVALUATION_CASES,
)
from app.modules.rag_evaluation.fixtures.family_avatar_i18n import (
    FAMILY_AVATAR_CS_EVALUATION_CASES,
    FAMILY_AVATAR_EN_EVALUATION_CASES,
    FAMILY_AVATAR_ES_EVALUATION_CASES,
    FAMILY_AVATAR_FR_EVALUATION_CASES,
    FAMILY_AVATAR_I18N_CASES_BY_LOCALE,
    FAMILY_AVATAR_RU_EVALUATION_CASES,
)
from app.modules.rag_evaluation.schemas import (
    RagEvaluationCase,
    RagEvaluationMemoryEvidenceSetup,
    RagEvaluationProfileSetup,
    RagEvaluationRetrievedEvidenceSetup,
)


FOUNDATION_RAG_EVALUATION_CASES: tuple[RagEvaluationCase, ...] = (
    RagEvaluationCase(
        case_id="grounded-context-available",
        title="Grounded answer when verified evidence exists",
        profile=RagEvaluationProfileSetup(
            profile_id=1,
            name="Alya",
            biography="A careful family historian.",
            personality="Warm and factual.",
        ),
        memory_evidence_items=[
            RagEvaluationMemoryEvidenceSetup(
                source_id=101,
                title="Wedding memory",
                content_preview="Alya remembered the family wedding in Brno in 1986.",
                memory_type="text",
                selection_reason="eval_fixture_memory",
                occurred_year=1986,
            )
        ],
        retrieved_evidence_items=[
            RagEvaluationRetrievedEvidenceSetup(
                chunk_id=501,
                source_id=201,
                embedding_id=301,
                text_hash="eval-rag-hash-501",
                content_preview="The archival note says the wedding ceremony took place in Brno.",
                source_document_type="document_text",
                validation_status="valid",
            )
        ],
        user_query="Where did the wedding happen?",
        expected_behavior="grounded_answer",
        expected_evidence_markers=["Brno"],
        forbidden_claims=["Paris"],
        minimum_required_evidence_count=1,
    ),
    RagEvaluationCase(
        case_id="lack-of-evidence-required",
        title="Lack-of-evidence answer when no stored evidence exists",
        profile=RagEvaluationProfileSetup(
            profile_id=2,
            name="Marek",
            biography="A profile with no verified supporting evidence yet.",
        ),
        user_query="Where was I born?",
        expected_behavior="lack_of_evidence",
        should_require_lack_of_evidence=True,
        forbidden_claims=["born in Paris"],
    ),
)


ETERNAL_WORLD_RAG_EVALUATION_CASES: tuple[RagEvaluationCase, ...] = (
    RagEvaluationCase(
        case_id="production-hybrid-lantern-archive",
        title="Production hybrid smoke grounded answer for lantern archive",
        profile=RagEvaluationProfileSetup(
            profile_id=10,
            name="Production Hybrid Smoke Profile",
            biography="Fictional profile for hybrid retrieval smoke checks.",
        ),
        retrieved_evidence_items=[
            RagEvaluationRetrievedEvidenceSetup(
                chunk_id=701,
                source_id=601,
                embedding_id=801,
                text_hash="hybrid-smoke-lantern",
                content_preview=(
                    "The lantern archive stayed tied to the cedar drawer in Prague "
                    "during every winter trip."
                ),
                source_document_type="document_text",
                validation_status="valid",
            )
        ],
        user_query="Which lantern archive stayed tied to the cedar drawer in Prague?",
        expected_behavior="grounded_answer",
        expected_evidence_markers=["lantern archive", "Prague"],
        forbidden_claims=["favorite car", "Berlin"],
        minimum_required_evidence_count=1,
    ),
    RagEvaluationCase(
        case_id="demo-smoke-sunflower",
        title="Demo smoke grounded answer for sunflower memory",
        profile=RagEvaluationProfileSetup(
            profile_id=11,
            name="Demo Grandfather",
            biography="Fictional person used only for backend smoke testing.",
        ),
        retrieved_evidence_items=[
            RagEvaluationRetrievedEvidenceSetup(
                chunk_id=702,
                source_id=602,
                embedding_id=802,
                text_hash="demo-smoke-sunflower",
                content_preview="His favorite flower was sunflower.",
                source_document_type="document_text",
                validation_status="valid",
            )
        ],
        user_query="What flower did he like? Was it sunflower?",
        expected_behavior="grounded_answer",
        expected_evidence_markers=["sunflower"],
        forbidden_claims=["rose", "tulip"],
        minimum_required_evidence_count=1,
    ),
    RagEvaluationCase(
        case_id="rag-only-archival-note",
        title="Grounded answer from RAG evidence without timeline memories",
        profile=RagEvaluationProfileSetup(
            profile_id=12,
            name="Archival Profile",
            biography="Profile with document-only evidence.",
        ),
        retrieved_evidence_items=[
            RagEvaluationRetrievedEvidenceSetup(
                chunk_id=703,
                source_id=603,
                embedding_id=803,
                text_hash="rag-only-brass-tag",
                content_preview="The brass tag remained on the archive cart for deterministic checks.",
                source_document_type="document_text",
                validation_status="valid",
            )
        ],
        user_query="What remained on the archive cart?",
        expected_behavior="grounded_answer",
        expected_evidence_markers=["brass tag"],
        forbidden_claims=["silver tag"],
        minimum_required_evidence_count=1,
    ),
    RagEvaluationCase(
        case_id="memory-only-timeline-recollection",
        title="Grounded answer from timeline memory without RAG chunks",
        profile=RagEvaluationProfileSetup(
            profile_id=13,
            name="Timeline Profile",
            biography="Profile with curated timeline memories only.",
        ),
        memory_evidence_items=[
            RagEvaluationMemoryEvidenceSetup(
                source_id=110,
                title="Station dinner",
                content_preview="We shared soup at the old station in Brno after the choir eve.",
                memory_type="text",
                selection_reason="eval_fixture_memory",
                occurred_year=1990,
            )
        ],
        user_query="Do you remember the station dinner in Brno?",
        expected_behavior="grounded_answer",
        expected_evidence_markers=["Brno", "station"],
        forbidden_claims=["Vienna"],
        minimum_required_evidence_count=1,
    ),
    RagEvaluationCase(
        case_id="combined-memory-and-rag-grounding",
        title="Grounded answer when both memory and RAG evidence support the fact",
        profile=RagEvaluationProfileSetup(
            profile_id=14,
            name="Combined Evidence Profile",
            biography="Family historian with both memories and archival notes.",
        ),
        memory_evidence_items=[
            RagEvaluationMemoryEvidenceSetup(
                source_id=111,
                title="Teacher years",
                content_preview="Eva later worked as a literature teacher in Brno.",
                memory_type="text",
                selection_reason="eval_fixture_memory",
                occurred_year=1995,
            )
        ],
        retrieved_evidence_items=[
            RagEvaluationRetrievedEvidenceSetup(
                chunk_id=704,
                source_id=604,
                embedding_id=804,
                text_hash="combined-teacher-brno",
                content_preview="An archival page states Eva worked as a literature teacher in Brno.",
                source_document_type="biography",
                validation_status="valid",
            )
        ],
        user_query="Tell me about Eva's work in Brno.",
        expected_behavior="grounded_answer",
        expected_evidence_markers=["literature teacher", "Brno"],
        forbidden_claims=["Paris", "engineer"],
        minimum_required_evidence_count=2,
    ),
    RagEvaluationCase(
        case_id="czech-language-wedding-query",
        title="Grounded answer for Czech-language user query",
        profile=RagEvaluationProfileSetup(
            profile_id=15,
            name="Alya",
            biography="Rodinná historička z Brna.",
        ),
        retrieved_evidence_items=[
            RagEvaluationRetrievedEvidenceSetup(
                chunk_id=705,
                source_id=605,
                embedding_id=805,
                text_hash="czech-wedding-brno",
                content_preview="Archivní poznámka uvádí, že svatební obřad proběhl v Brně.",
                source_document_type="document_text",
                validation_status="valid",
                language="cs",
            )
        ],
        user_query="Kde proběhla svatba?",
        expected_behavior="grounded_answer",
        expected_evidence_markers=["Brn"],
        forbidden_claims=["Praze", "Paříži"],
        minimum_required_evidence_count=1,
    ),
    RagEvaluationCase(
        case_id="lack-of-evidence-with-forbidden-invention",
        title="Lack-of-evidence must not invent unsupported birthplace",
        profile=RagEvaluationProfileSetup(
            profile_id=16,
            name="Empty Evidence Profile",
            biography="No verified supporting evidence yet.",
        ),
        user_query="Where was I born?",
        expected_behavior="lack_of_evidence",
        should_require_lack_of_evidence=True,
        forbidden_claims=["born in Brno", "born in Prague"],
    ),
)


ALL_RAG_EVALUATION_CASES: tuple[RagEvaluationCase, ...] = (
    *FOUNDATION_RAG_EVALUATION_CASES,
    *ETERNAL_WORLD_RAG_EVALUATION_CASES,
    *FAMILY_AVATAR_EVALUATION_CASES,
)
