from __future__ import annotations

import hashlib
import math
import re
from dataclasses import dataclass

from app.modules.rag_chunks.chunker import ChunkCandidate, MAX_CHUNK_SIZE


MID_SENTENCE_ENDING_PATTERN = re.compile(r"[.!?…][\"')\]»”]*$")
BROKEN_WORD_PATTERN = re.compile(r"[A-Za-zА-Яа-яЁёČčŠšŽžŘřĚěÝýÁáÍíÉéÚúŮůÓóÄäÖöÜüß]-$")


@dataclass(frozen=True)
class ValidatedChunk:
    chunk_index: int
    chunk_text: str
    text_hash: str
    token_estimate: int
    char_count: int
    sentence_count: int
    chunk_metadata: dict[str, object]
    validation_status: str
    validation_errors: list[str]


@dataclass(frozen=True)
class ChunkValidationSummary:
    chunk_count: int
    valid_count: int
    warning_count: int
    invalid_count: int
    source_validation_errors: list[str]


def estimate_token_count(text: str) -> int:
    word_count = len(text.split())
    return max(1, int(math.ceil(word_count * 1.3)))


def _classify_status(validation_errors: list[str]) -> str:
    if not validation_errors:
        return "valid"

    if any(
        error in {"empty_chunk", "duplicate_chunk_hash", "missing_owner_profile_source_ids"}
        for error in validation_errors
    ):
        return "invalid"

    return "warning"


def validate_chunk_candidates(
    *,
    chunk_candidates: list[ChunkCandidate],
    owner_user_id: int,
    profile_id: int,
    source_id: int,
    max_chunk_size: int = MAX_CHUNK_SIZE,
    normalized_source_text: str,
) -> tuple[list[ValidatedChunk], ChunkValidationSummary]:
    seen_hashes: set[str] = set()
    validated_chunks: list[ValidatedChunk] = []
    source_validation_errors: list[str] = []

    if not normalized_source_text.strip():
        source_validation_errors.append("normalized_source_text_empty")

    for chunk_index, chunk_candidate in enumerate(chunk_candidates):
        chunk_text = chunk_candidate.chunk_text.strip()
        validation_errors: list[str] = []
        text_hash = hashlib.sha256(chunk_text.encode("utf-8")).hexdigest()

        if not chunk_text:
            validation_errors.append("empty_chunk")

        if text_hash in seen_hashes:
            validation_errors.append("duplicate_chunk_hash")
        else:
            seen_hashes.add(text_hash)

        if len(chunk_text) > max_chunk_size and not bool(chunk_candidate.chunk_metadata.get("hard_split_fallback")):
            validation_errors.append("chunk_exceeds_max_size")

        if chunk_text and chunk_text[0].islower() and not bool(chunk_candidate.chunk_metadata.get("overlap_from_previous")):
            validation_errors.append("suspicious_mid_sentence_start")

        if chunk_text and not MID_SENTENCE_ENDING_PATTERN.search(chunk_text):
            validation_errors.append("suspicious_mid_sentence_end")

        if BROKEN_WORD_PATTERN.search(chunk_text):
            validation_errors.append("suspicious_broken_word_split")

        if not owner_user_id or not profile_id or not source_id:
            validation_errors.append("missing_owner_profile_source_ids")

        validated_chunks.append(
            ValidatedChunk(
                chunk_index=chunk_index,
                chunk_text=chunk_text,
                text_hash=text_hash,
                token_estimate=estimate_token_count(chunk_text),
                char_count=len(chunk_text),
                sentence_count=chunk_candidate.sentence_count,
                chunk_metadata=chunk_candidate.chunk_metadata,
                validation_status=_classify_status(validation_errors),
                validation_errors=validation_errors,
            )
        )

    if any(chunk.chunk_index != expected_index for expected_index, chunk in enumerate(validated_chunks)):
        source_validation_errors.append("chunk_index_sequence_invalid")

    if normalized_source_text and validated_chunks:
        unique_coverage_text = " ".join(dict.fromkeys(chunk.chunk_text for chunk in validated_chunks))
        if len(unique_coverage_text) < max(1, int(len(normalized_source_text) * 0.5)):
            source_validation_errors.append("source_text_coverage_low")

    valid_count = sum(1 for chunk in validated_chunks if chunk.validation_status == "valid")
    warning_count = sum(1 for chunk in validated_chunks if chunk.validation_status == "warning")
    invalid_count = sum(1 for chunk in validated_chunks if chunk.validation_status == "invalid")

    return validated_chunks, ChunkValidationSummary(
        chunk_count=len(validated_chunks),
        valid_count=valid_count,
        warning_count=warning_count,
        invalid_count=invalid_count,
        source_validation_errors=source_validation_errors,
    )
