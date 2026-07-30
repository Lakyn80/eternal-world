from app.db.models import RagEmbedding
from app.db.session import get_db
from app.main import app
from app.modules.ai_agents.brain.providers.mock import MockBrainAgentProvider
from app.modules.ai_agents.brain.service import BrainAgentService
from app.modules.ai_agents.schemas import BrainAgentResponse
from app.modules.rag_evaluation.cases import (
    ALL_RAG_EVALUATION_CASES,
    ETERNAL_WORLD_RAG_EVALUATION_CASES,
    FAMILY_AVATAR_EVALUATION_CASES,
    FOUNDATION_RAG_EVALUATION_CASES,
)
from app.modules.rag_evaluation.evaluator import (
    detect_actual_behavior,
    evaluate_answer_against_case,
    _missing_expected_markers,
)
from app.modules.rag_evaluation.service import RagEvaluationService
from app.modules.rag_evaluation.schemas import (
    RagEvaluationCase,
    RagEvaluationMemoryEvidenceSetup,
    RagEvaluationProfileSetup,
    RagEvaluationRetrievedEvidenceSetup,
)


def _get_test_db_session():
    override = app.dependency_overrides[get_db]
    session_generator = override()
    db = next(session_generator)
    return db, session_generator


def _build_grounded_case() -> RagEvaluationCase:
    return RagEvaluationCase(
        case_id="grounded-pass",
        title="Grounded answer includes expected evidence markers",
        profile=RagEvaluationProfileSetup(
            profile_id=1,
            name="Eva",
            biography="A retired teacher from Brno.",
        ),
        memory_evidence_items=[
            RagEvaluationMemoryEvidenceSetup(
                source_id=10,
                title="Childhood home",
                content_preview="Eva grew up in Brno near the old station.",
                memory_type="text",
                selection_reason="eval_fixture_memory",
                occurred_year=1974,
            )
        ],
        retrieved_evidence_items=[
            RagEvaluationRetrievedEvidenceSetup(
                chunk_id=20,
                source_id=30,
                embedding_id=40,
                text_hash="hash-20",
                content_preview="An archival page states Eva later worked as a literature teacher.",
                source_document_type="biography",
                validation_status="valid",
            )
        ],
        user_query="Tell me about where I grew up and what I did for work.",
        expected_behavior="grounded_answer",
        expected_evidence_markers=["Brno", "literature teacher"],
        minimum_required_evidence_count=2,
    )


def test_eval_case_with_evidence_passes_when_answer_uses_evidence():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    case = _build_grounded_case()
    answer_text = "You grew up in Brno and later worked as a literature teacher."

    result = service.run_eval_case(
        case,
        answer_generator=lambda case, request: BrainAgentResponse(
            text=answer_text,
            provider_name="mock-eval",
            metadata={"grounding_status": "grounded"},
        ),
    )

    assert result.passed is True
    assert result.actual_behavior == "grounded_answer"
    assert result.evidence_count == 2
    assert result.user_query == case.user_query
    assert result.answer_text == answer_text
    assert result.missing_expected_markers == []
    assert result.forbidden_claims_found == []


def test_eval_case_fails_when_expected_evidence_marker_is_missing():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    case = _build_grounded_case()

    result = service.run_eval_case(
        case,
        answer_generator=lambda case, request: BrainAgentResponse(
            text="You grew up in Brno.",
            provider_name="mock-eval",
            metadata={"grounding_status": "grounded"},
        ),
    )

    assert result.passed is False
    assert result.missing_expected_markers == ["literature teacher"]
    assert any("missing expected evidence markers" in reason.lower() for reason in result.reasons)


def test_eval_case_fails_when_forbidden_unsupported_claim_appears():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    case = _build_grounded_case().model_copy(update={"forbidden_claims": ["moved to Paris"]})

    result = service.run_eval_case(
        case,
        answer_generator=lambda case, request: BrainAgentResponse(
            text="You grew up in Brno, worked as a literature teacher, and later moved to Paris.",
            provider_name="mock-eval",
            metadata={"grounding_status": "grounded"},
        ),
    )

    assert result.passed is False
    assert result.forbidden_claims_found == ["moved to Paris"]
    assert any("forbidden unsupported claims" in reason.lower() for reason in result.reasons)


def test_lack_of_evidence_eval_passes_with_mock_brain_provider():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    case = FOUNDATION_RAG_EVALUATION_CASES[1]

    result = service.run_eval_case(case)

    assert result.passed is True
    assert result.actual_behavior == "lack_of_evidence"
    assert result.provider_name == "mock"
    assert "i don't remember that" in result.answer_preview.lower()


def test_lack_of_evidence_eval_fails_when_answer_invents_unsupported_facts():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    case = FOUNDATION_RAG_EVALUATION_CASES[1].model_copy(update={"forbidden_claims": ["born in Paris"]})

    result = service.run_eval_case(
        case,
        answer_generator=lambda case, request: BrainAgentResponse(
            text="You were born in Paris in 1942.",
            provider_name="mock-eval",
            metadata={"grounding_status": "grounded"},
        ),
    )

    assert result.passed is False
    assert result.actual_behavior == "grounded_answer"
    assert result.forbidden_claims_found == ["born in Paris"]
    assert any("lack-of-evidence" in reason.lower() for reason in result.reasons)


def test_rag_evaluation_harness_does_not_call_real_external_ai_apis(monkeypatch):
    from app.modules.ai_agents.brain.providers import openai_compatible

    def fail_http_client(*args, **kwargs):
        raise AssertionError("External AI HTTP client should not be created for RAG evaluation tests")

    monkeypatch.setattr(openai_compatible.httpx, "Client", fail_http_client)
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))

    result = service.run_eval_case(FOUNDATION_RAG_EVALUATION_CASES[1])

    assert result.passed is True
    assert result.provider_name == "mock"


def test_rag_evaluation_harness_does_not_create_stored_query_embeddings(client):
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    db, session_generator = _get_test_db_session()
    embeddings_before = db.query(RagEmbedding).count()

    try:
        result = service.run_eval_case(FOUNDATION_RAG_EVALUATION_CASES[1])
        embeddings_after = db.query(RagEmbedding).count()
    finally:
        session_generator.close()

    assert result.passed is True
    assert embeddings_before == 0
    assert embeddings_after == 0


def test_run_eval_suite_returns_summary_counts():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    grounded_case = _build_grounded_case()
    no_evidence_case = FOUNDATION_RAG_EVALUATION_CASES[1]

    def answer_generator(case, request):
        if case.case_id == grounded_case.case_id:
            return BrainAgentResponse(
                text="You grew up in Brno and later worked as a literature teacher.",
                provider_name="mock-eval",
                metadata={"grounding_status": "grounded"},
            )
        return BrainAgentResponse(
            text="You were born in Paris.",
            provider_name="mock-eval",
            metadata={"grounding_status": "grounded"},
        )

    suite_result = service.run_eval_suite(
        [grounded_case, no_evidence_case],
        answer_generator=answer_generator,
    )

    assert suite_result.total_cases == 2
    assert suite_result.passed_cases == 1
    assert suite_result.failed_cases == 1
    assert [result.case_id for result in suite_result.results] == [
        grounded_case.case_id,
        no_evidence_case.case_id,
    ]


def test_eternal_world_eval_cases_pass_with_grounded_mock_brain():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    legacy_cases = (
        *FOUNDATION_RAG_EVALUATION_CASES,
        *ETERNAL_WORLD_RAG_EVALUATION_CASES,
    )

    suite_result = service.run_eval_suite(legacy_cases)

    assert suite_result.total_cases == len(legacy_cases)
    assert suite_result.failed_cases == 0
    assert suite_result.passed_cases == suite_result.total_cases


def _family_avatar_mock_answer_generator(
    case: RagEvaluationCase,
    request,
) -> BrainAgentResponse:
    if case.expected_behavior == "lack_of_evidence":
        return BrainAgentResponse(
            text="Na to bohužel nemám vzpomínku.",
            provider_name="mock-eval",
            metadata={"grounding_status": "no_evidence"},
        )

    cited_parts: list[str] = []
    for evidence_item in case.memory_evidence_items:
        cited_parts.append(
            f"[memory:{evidence_item.source_id}] {evidence_item.content_preview}"
        )
    for evidence_item in case.retrieved_evidence_items:
        cited_parts.append(
            f"[rag:{evidence_item.chunk_id}] {evidence_item.content_preview}"
        )
    marker_text = " ".join(case.expected_evidence_markers)
    return BrainAgentResponse(
        text=" ".join([*cited_parts, marker_text]),
        provider_name="mock-eval",
        metadata={"grounding_status": "grounded"},
    )


def test_family_avatar_eval_cases_pass_with_marker_aware_mock_brain():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))

    suite_result = service.run_eval_suite(
        FAMILY_AVATAR_EVALUATION_CASES,
        answer_generator=_family_avatar_mock_answer_generator,
    )

    assert suite_result.total_cases == len(FAMILY_AVATAR_EVALUATION_CASES)
    assert suite_result.failed_cases == 0
    assert suite_result.passed_cases == suite_result.total_cases


def test_human_czech_lack_of_evidence_markers_are_detected():
    behavior = detect_actual_behavior(
        answer_text="Tam jsem nebyla a o tom bohužel nevím.",
        response_metadata={"grounding_status": "no_evidence"},
    )
    assert behavior == "lack_of_evidence"


def test_foundation_grounded_case_passes_with_mock_brain_using_evidence_citations():
    service = RagEvaluationService(brain_service=BrainAgentService(MockBrainAgentProvider()))
    case = FOUNDATION_RAG_EVALUATION_CASES[0]

    result = service.run_eval_case(case)

    assert result.passed is True
    assert result.actual_behavior == "grounded_answer"
    assert "Brno" in result.answer_preview
    # Internal [memory:]/[rag:] citations are stripped before user-visible text.
    assert "[rag:501]" not in result.answer_preview
    assert "[memory:101]" not in result.answer_preview


def test_eternal_world_eval_case_count_is_at_least_eight():
    assert len(ETERNAL_WORLD_RAG_EVALUATION_CASES) >= 7
    assert len(FAMILY_AVATAR_EVALUATION_CASES) >= 25
    assert len(ALL_RAG_EVALUATION_CASES) >= 60


def test_hedged_but_substantively_grounded_answer_counts_as_grounded():
    combined_case = next(
        case
        for case in ETERNAL_WORLD_RAG_EVALUATION_CASES
        if case.case_id == "combined-memory-and-rag-grounding"
    )
    deepseek_style_answer = (
        "Based on the available evidence, Eva worked as a literature teacher in Brno. "
        "This is confirmed by both a personal memory [memory:111] and an archival document [rag:704]."
    )

    result = evaluate_answer_against_case(
        case=combined_case,
        answer_text=deepseek_style_answer,
        provider_name="openai_compatible",
        response_metadata={"grounding_status": "grounded"},
        evidence_count=2,
    )

    assert result.passed is True
    assert result.actual_behavior == "grounded_answer"


def test_uncertainty_phrase_without_markers_or_citations_stays_partial():
    combined_case = next(
        case
        for case in ETERNAL_WORLD_RAG_EVALUATION_CASES
        if case.case_id == "combined-memory-and-rag-grounding"
    )
    uncertain_answer = "Based on the available evidence, I am not sure about her work."

    behavior = detect_actual_behavior(
        answer_text=uncertain_answer,
        response_metadata={"grounding_status": "grounded"},
        expected_evidence_markers=combined_case.expected_evidence_markers,
    )

    assert behavior == "partial_answer_with_uncertainty"

    result = evaluate_answer_against_case(
        case=combined_case,
        answer_text=uncertain_answer,
        provider_name="openai_compatible",
        response_metadata={"grounding_status": "grounded"},
        evidence_count=2,
    )

    assert result.passed is False
    assert result.actual_behavior == "partial_answer_with_uncertainty"


def _build_lack_case(**updates) -> RagEvaluationCase:
    case = next(
        case for case in FAMILY_AVATAR_EVALUATION_CASES if case.case_id == "family-lack-paris-1968"
    )
    return case.model_copy(update=updates)


def test_czech_morphology_marker_matching_accepts_inflected_forms():
    audit_cases = [
        (
            "pero, učitelk",
            "Ano, dostala jsem pero s nápisem Děkujeme paní učitelce. [memory:1031]",
        ),
        (
            "Pavel, 1981",
            "Stavební plán nesl razítko projektanta Pavla Nováka ze dne 12. května 1981. [rag:2009]",
        ),
        (
            "únava, tlak",
            "V květnu 2018 jsem měla pobyt na interně kvůli únavě a nízkému tlaku. [rag:2011]",
        ),
        (
            "trpěliv, kroužek",
            "Byla popisována jako trpělivá vedoucí čtenářského kroužku. [rag:2013]",
        ),
    ]
    for markers, answer_text in audit_cases:
        missing = _missing_expected_markers(
            answer_text=answer_text,
            expected_evidence_markers=markers.split(", "),
        )
        assert missing == [], answer_text


def test_english_marker_aliases_accept_czech_equivalents_for_vienna_trip():
    missing = _missing_expected_markers(
        answer_text=(
            "Ano, v roce 1985 jsem jela autobusem do Vídně na výstavě knih. [memory:1016]"
        ),
        expected_evidence_markers=["Vienna", "book"],
    )
    assert missing == []


def test_lack_denial_with_question_echo_does_not_trigger_forbidden_claim():
    case = _build_lack_case()
    answer_text = (
        "Milá otázko, ale na to bohužel nemám vzpomínku. "
        "V uložených vzpomínkách ani v dostupných materiálech o Paříži v roce 1968 nic není."
    )

    result = evaluate_answer_against_case(
        case=case,
        answer_text=answer_text,
        provider_name="mock-eval",
        response_metadata={"grounding_status": "no_evidence"},
        evidence_count=0,
    )

    assert result.actual_behavior == "lack_of_evidence"
    assert result.forbidden_claims_found == []
    assert result.passed is True


def test_lack_denial_echo_patterns_from_audit_cases_pass_evaluator():
    audit_answers = {
        "family-lack-dog-azor": (
            "Milý příteli, na to bohužel nemám vzpomínku. "
            "V uložených vzpomínkách o prvním psovi ani o Azorovi nic není."
        ),
        "family-lack-vietnam": (
            "Na to bohužel nemám vzpomínku. "
            "O Pavlově službě ve Vietnamu mi nejsou známy žádné podrobnosti."
        ),
        "family-lack-famous-actor": (
            "Milá otázko, ale bohužel na to nemám vzpomínku. "
            "V uložených vzpomínkách nemám žádnou zmínku o setkání se slavným hercem v Brně."
        ),
    }
    for case_id, answer_text in audit_answers.items():
        case = next(item for item in FAMILY_AVATAR_EVALUATION_CASES if item.case_id == case_id)
        result = evaluate_answer_against_case(
            case=case,
            answer_text=answer_text,
            provider_name="mock-eval",
            response_metadata={"grounding_status": "no_evidence"},
            evidence_count=0,
        )
        assert result.forbidden_claims_found == [], case_id
        assert result.passed is True, case_id


def test_affirmative_unsupported_claim_still_fails_in_lack_case():
    case = next(
        item for item in FAMILY_AVATAR_EVALUATION_CASES if item.case_id == "family-lack-dog-azor"
    )

    result = evaluate_answer_against_case(
        case=case,
        answer_text="Ano, můj první pes se jmenoval Azor a byl to kříženec.",
        provider_name="mock-eval",
        response_metadata={"grounding_status": "grounded"},
        evidence_count=0,
    )

    assert result.passed is False
    assert "Azor" in result.forbidden_claims_found


def test_nevybavuji_is_detected_as_lack_of_evidence():
    behavior = detect_actual_behavior(
        answer_text=(
            "Milá vzpomínko, ale bohužel na plavání v moři u Itálie si "
            "v uložených vzpomínkách nevybavuji."
        ),
        response_metadata={"grounding_status": "general"},
    )
    assert behavior == "lack_of_evidence"

    case = next(
        item for item in FAMILY_AVATAR_EVALUATION_CASES if item.case_id == "family-lack-italy-sea"
    )
    result = evaluate_answer_against_case(
        case=case,
        answer_text=(
            "Milá vzpomínko, ale bohužel na plavání v moři u Itálie si "
            "v uložených vzpomínkách nevybavuji."
        ),
        provider_name="mock-eval",
        response_metadata={"grounding_status": "general"},
        evidence_count=0,
    )
    assert result.actual_behavior == "lack_of_evidence"
    assert result.forbidden_claims_found == []
    assert result.passed is True


def test_zero_evidence_grounded_biography_assertion_fails_lack_case():
    case = next(
        item for item in FAMILY_AVATAR_EVALUATION_CASES if item.case_id == "family-lack-prague-birth"
    )

    result = evaluate_answer_against_case(
        case=case,
        answer_text="Kdepak, narodila jsem se v Brně. Celý život jsem byla Moravanka.",
        provider_name="mock-eval",
        response_metadata={"grounding_status": "general"},
        evidence_count=0,
    )

    assert result.passed is False
    assert result.actual_behavior == "grounded_answer"
    assert any("lack-of-evidence" in reason.lower() for reason in result.reasons)


def test_mixed_lack_preface_with_grounded_citation_counts_as_grounded():
    case = next(
        item for item in FAMILY_AVATAR_EVALUATION_CASES if item.case_id == "family-rag-diploma"
    )
    answer_text = (
        "To v uložených vzpomínkách nemám. Z dostupných materiálů vím, že diplom z pedagogické "
        "fakulty jsem získala v červnu 1972 s tématem venkovské školní knihovny [rag:2002]."
    )

    result = evaluate_answer_against_case(
        case=case,
        answer_text=answer_text,
        provider_name="mock-eval",
        response_metadata={"grounding_status": "grounded"},
        evidence_count=1,
    )

    assert result.actual_behavior == "grounded_answer"
    assert result.passed is True


def test_grounded_marker_can_be_satisfied_from_user_query_context():
    missing = _missing_expected_markers(
        answer_text="Pod hvězdami. [rag:2005]",
        expected_evidence_markers=["Pod hvězdami", "kroužek"],
        user_query="Jak se jmenoval tvůj čtenářský kroužek?",
    )
    assert missing == []


def test_shorter_lack_phrases_are_detected():
    for answer_text in (
        "To bohužel v uložených vzpomínkách nemám.",
        "Omlouvám se, ale v uložených vzpomínkách ani dokumentech nemám žádné informace o tom. Tuto zkušenost nemám.",
    ):
        behavior = detect_actual_behavior(
            answer_text=answer_text,
            response_metadata={"grounding_status": "general"},
        )
        assert behavior == "lack_of_evidence", answer_text


def test_real_russian_lack_denials_with_citations_count_as_lack_for_lack_cases():
    audit_answers = {
        "family-lack-paris-1968": (
            "Нет, в 1968 году я не была в Париже. "
            "Весь тот год я провела за учёбой в Брно и на практике в Моравии [rag:27636]."
        ),
        "family-lack-prague-birth": (
            "Нет, я родилась в Брно, в доме с красной крышей на улице Вевери. [rag:27634]"
        ),
        "family-lack-english-paris": (
            "К сожалению, я не была в Париже. "
            "Самая дальняя моя поездка за границу вела в Будапешт в 1994 году [rag:27627]."
        ),
    }
    for case_id, answer_text in audit_answers.items():
        case = next(item for item in FAMILY_AVATAR_EVALUATION_CASES if item.case_id == case_id)
        result = evaluate_answer_against_case(
            case=case,
            answer_text=answer_text,
            provider_name="mock-eval",
            response_metadata={"grounding_status": "grounded"},
            evidence_count=1,
        )
        assert result.actual_behavior == "lack_of_evidence", case_id
        assert result.forbidden_claims_found == [], case_id
        assert result.passed is True, case_id


def test_real_garage_lack_answer_still_fails_when_it_repeats_forbidden_details():
    base_case = next(
        item
        for item in FAMILY_AVATAR_EVALUATION_CASES
        if item.case_id == "family-lack-corpus-only-frantisek-garage"
    )
    case = base_case.model_copy(
        update={
            "user_query": "Какие часы отец Франтишек чинил в гараже?",
            "forbidden_claims": ["часы", "гараж", "луп"],
        }
    )
    answer_text = (
        "Дорогой мой, в сохранённых воспоминаниях не указано, какие именно часы чинил отец "
        "Франтишек в гараже. Помню только, что я держала ему лупу, когда мне было семь лет, "
        "но марку или тип часов — увы, не запомнила. [rag:27618]"
    )

    result = evaluate_answer_against_case(
        case=case,
        answer_text=answer_text,
        provider_name="mock-eval",
        response_metadata={"grounding_status": "grounded"},
        evidence_count=1,
    )

    assert result.passed is False
    assert "часы" in result.forbidden_claims_found
    assert "гараж" in result.forbidden_claims_found


def test_real_machovo_answer_passes_when_fact_is_extracted_from_a_lower_ranked_chunk():
    base_case = next(
        item for item in FAMILY_AVATAR_EVALUATION_CASES if item.case_id == "family-rag-machovo"
    )
    case = base_case.model_copy(update={"expected_evidence_markers": ["Мах", "озер"]})
    answer_text = (
        "Семейный архив хранит письмо, где Мартин описывает первый совместный отпуск с детьми "
        "у озера Маха. [rag:27633]"
    )

    result = evaluate_answer_against_case(
        case=case,
        answer_text=answer_text,
        provider_name="mock-eval",
        response_metadata={"grounding_status": "grounded"},
        evidence_count=5,
    )

    assert result.actual_behavior == "grounded_answer"
    assert result.missing_expected_markers == []
    assert result.passed is True


def test_real_machovo_over_refusal_still_fails_on_missing_markers():
    base_case = next(
        item for item in FAMILY_AVATAR_EVALUATION_CASES if item.case_id == "family-rag-machovo"
    )
    case = base_case.model_copy(update={"expected_evidence_markers": ["Мах", "озер"]})
    answer_text = "Извините, я не могу найти эту информацию в сохранённых воспоминаниях."

    result = evaluate_answer_against_case(
        case=case,
        answer_text=answer_text,
        provider_name="mock-eval",
        response_metadata={"grounding_status": "grounded"},
        evidence_count=5,
    )

    assert result.passed is False
    assert result.missing_expected_markers == ["Мах", "озер"]


def test_rag_evaluation_service_guard_sanitizes_forbidden_detail_in_lack_case():
    class StubLeakProvider:
        def generate_response(self, request) -> BrainAgentResponse:
            return BrainAgentResponse(
                text=(
                    "Дорогой мой, в сохранённых воспоминаниях не указано, какие именно часы чинил отец "
                    "Франтишек в гараже. Помню только, что я держала ему лупу, когда мне было семь лет. "
                    "[rag:27618]"
                ),
                provider_name="stub-eval",
                metadata={"grounding_status": "grounded"},
            )

    case = next(
        item
        for item in FAMILY_AVATAR_EVALUATION_CASES
        if item.case_id == "family-lack-corpus-only-frantisek-garage"
    ).model_copy(update={"forbidden_claims": ["часы", "гараж", "луп"]})
    service = RagEvaluationService(brain_service=BrainAgentService(StubLeakProvider()))

    result = service.run_eval_case(case)

    assert result.passed is True
    assert result.actual_behavior == "lack_of_evidence"
    assert result.forbidden_claims_found == []
    assert result.response_metadata["output_guard_applied"] is True
    assert result.response_metadata["output_guard_reason"] == "forbidden_claim_in_lack_case"
