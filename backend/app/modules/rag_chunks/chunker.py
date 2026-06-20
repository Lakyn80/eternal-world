from __future__ import annotations

import re
from dataclasses import dataclass


TARGET_CHUNK_SIZE = 1100
MAX_CHUNK_SIZE = 1800
MIN_USEFUL_CHUNK_SIZE = 80
SENTENCE_OVERLAP = 1
SENTENCE_ENDINGS = ".!?…"
ABBREVIATIONS = {
    "mr.",
    "mrs.",
    "ms.",
    "dr.",
    "prof.",
    "jr.",
    "sr.",
    "vs.",
    "etc.",
    "e.g.",
    "i.e.",
    "st.",
    "no.",
    "str.",
    "např.",
    "tj.",
    "atd.",
    "atp.",
    "obr.",
    "č.",
    "г.",
    "ул.",
    "стр.",
    "т.д.",
    "т.п.",
    "т.е.",
    "напр.",
}


@dataclass(frozen=True)
class ChunkCandidate:
    chunk_text: str
    sentence_count: int
    chunk_metadata: dict[str, object]


def normalize_source_text(text: str) -> str:
    normalized_newlines = text.replace("\r\n", "\n").replace("\r", "\n")
    paragraph_candidates = re.split(r"\n\s*\n+", normalized_newlines)
    normalized_paragraphs = []
    for paragraph in paragraph_candidates:
        compact_paragraph = re.sub(r"[^\S\n]+", " ", paragraph)
        compact_paragraph = re.sub(r"\s*\n\s*", " ", compact_paragraph).strip()
        if compact_paragraph:
            normalized_paragraphs.append(compact_paragraph)

    return "\n\n".join(normalized_paragraphs)


def _looks_like_abbreviation(text: str, dot_index: int) -> bool:
    start_index = text.rfind(" ", 0, dot_index) + 1
    token = text[start_index : dot_index + 1].lower()
    return token in ABBREVIATIONS


def split_paragraph_into_sentences(paragraph: str) -> list[str]:
    stripped_paragraph = paragraph.strip()
    if not stripped_paragraph:
        return []

    sentences: list[str] = []
    sentence_start = 0
    index = 0
    paragraph_length = len(stripped_paragraph)

    while index < paragraph_length:
        char = stripped_paragraph[index]
        is_boundary = False

        if char in "!?…":
            is_boundary = True
        elif char == "." and not _looks_like_abbreviation(stripped_paragraph, index):
            next_index = index + 1
            while next_index < paragraph_length and stripped_paragraph[next_index].isspace():
                next_index += 1
            if next_index >= paragraph_length:
                is_boundary = True
            elif stripped_paragraph[next_index].isupper() or stripped_paragraph[next_index].isdigit():
                is_boundary = True
            elif stripped_paragraph[next_index] in "\"'“”«»([":
                is_boundary = True

        if is_boundary:
            sentence = stripped_paragraph[sentence_start : index + 1].strip()
            if sentence:
                sentences.append(sentence)
            next_start = index + 1
            while next_start < paragraph_length and stripped_paragraph[next_start].isspace():
                next_start += 1
            sentence_start = next_start
            index = next_start
            continue

        index += 1

    trailing_text = stripped_paragraph[sentence_start:].strip()
    if trailing_text:
        sentences.append(trailing_text)

    return sentences or [stripped_paragraph]


def _hard_split_sentence(sentence: str, *, max_chunk_size: int) -> list[str]:
    remaining_text = sentence.strip()
    if not remaining_text:
        return []

    parts: list[str] = []
    while len(remaining_text) > max_chunk_size:
        split_at = remaining_text.rfind(" ", 0, max_chunk_size + 1)
        if split_at < MIN_USEFUL_CHUNK_SIZE:
            split_at = max_chunk_size
        part = remaining_text[:split_at].strip()
        if part:
            parts.append(part)
        remaining_text = remaining_text[split_at:].strip()

    if remaining_text:
        parts.append(remaining_text)

    return parts


def _build_chunk_text(sentences: list[str]) -> str:
    return " ".join(sentence.strip() for sentence in sentences if sentence.strip()).strip()


def build_chunk_candidates(
    text: str,
    *,
    target_chunk_size: int = TARGET_CHUNK_SIZE,
    max_chunk_size: int = MAX_CHUNK_SIZE,
    min_useful_chunk_size: int = MIN_USEFUL_CHUNK_SIZE,
    sentence_overlap: int = SENTENCE_OVERLAP,
) -> list[ChunkCandidate]:
    normalized_text = normalize_source_text(text)
    if not normalized_text:
        return []

    paragraphs = normalized_text.split("\n\n")
    sentence_entries: list[tuple[str, bool]] = []
    for paragraph in paragraphs:
        paragraph_sentences = split_paragraph_into_sentences(paragraph)
        for sentence in paragraph_sentences:
            if len(sentence) > max_chunk_size:
                for part in _hard_split_sentence(sentence, max_chunk_size=max_chunk_size):
                    sentence_entries.append((part, True))
            else:
                sentence_entries.append((sentence, False))

    if not sentence_entries:
        return []

    chunks: list[ChunkCandidate] = []
    current_sentences: list[str] = []
    current_hard_split = False
    overlap_from_previous = False

    def flush_current_chunk() -> None:
        nonlocal current_sentences, current_hard_split, overlap_from_previous
        chunk_text = _build_chunk_text(current_sentences)
        if chunk_text:
            chunks.append(
                ChunkCandidate(
                    chunk_text=chunk_text,
                    sentence_count=len(current_sentences),
                    chunk_metadata={
                        "hard_split_fallback": current_hard_split,
                        "overlap_from_previous": overlap_from_previous,
                    },
                )
            )
        current_sentences = []
        current_hard_split = False
        overlap_from_previous = False

    for sentence, hard_split_fallback in sentence_entries:
        if not current_sentences:
            current_sentences = [sentence]
            current_hard_split = hard_split_fallback
            overlap_from_previous = False
            continue

        candidate_text = _build_chunk_text([*current_sentences, sentence])
        if len(candidate_text) <= target_chunk_size or (
            len(_build_chunk_text(current_sentences)) < min_useful_chunk_size
            and len(candidate_text) <= max_chunk_size
        ):
            current_sentences.append(sentence)
            current_hard_split = current_hard_split or hard_split_fallback
            continue

        previous_sentences = list(current_sentences)
        flush_current_chunk()

        overlap_sentences = previous_sentences[-sentence_overlap:] if sentence_overlap > 0 else []
        seeded_sentences = list(overlap_sentences)
        if seeded_sentences:
            overlap_text = _build_chunk_text([*seeded_sentences, sentence])
            if overlap_text != sentence and len(overlap_text) <= max_chunk_size:
                current_sentences = [*seeded_sentences, sentence]
                current_hard_split = hard_split_fallback
                overlap_from_previous = True
            else:
                current_sentences = [sentence]
                current_hard_split = hard_split_fallback
                overlap_from_previous = False
        else:
            current_sentences = [sentence]
            current_hard_split = hard_split_fallback
            overlap_from_previous = False

    flush_current_chunk()

    if len(chunks) >= 2 and len(chunks[-1].chunk_text) < min_useful_chunk_size:
        merged_text = f"{chunks[-2].chunk_text} {chunks[-1].chunk_text}".strip()
        if len(merged_text) <= max_chunk_size:
            merged_chunk = ChunkCandidate(
                chunk_text=merged_text,
                sentence_count=chunks[-2].sentence_count + chunks[-1].sentence_count,
                chunk_metadata={
                    "hard_split_fallback": bool(
                        chunks[-2].chunk_metadata.get("hard_split_fallback")
                        or chunks[-1].chunk_metadata.get("hard_split_fallback")
                    ),
                    "overlap_from_previous": bool(chunks[-2].chunk_metadata.get("overlap_from_previous")),
                    "merged_small_tail": True,
                },
            )
            chunks = [*chunks[:-2], merged_chunk]

    return chunks
