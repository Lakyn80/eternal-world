from __future__ import annotations

import re


_PARAGRAPH_SPLIT_PATTERN = re.compile(r"\n\s*\n")
_SENTENCE_SPLIT_PATTERN = re.compile(r"(?<=[.!?])\s+")


def _pack(units: list[str], *, max_chars: int) -> list[str]:
    packed: list[str] = []
    current = ""
    for unit in units:
        candidate = f"{current} {unit}".strip() if current else unit
        if len(candidate) > max_chars and current:
            packed.append(current)
            current = unit
        else:
            current = candidate
    if current:
        packed.append(current)
    return packed


def chunk_biography_text(text: str, *, max_chars: int = 1200) -> list[str]:
    """Deterministic paragraph-based chunking: same input text always
    produces the same ordered list of chunks. Paragraphs (blank-line
    separated) are greedily packed up to `max_chars`; a single paragraph
    longer than `max_chars` is first split on sentence boundaries so no
    chunk silently grows unbounded."""

    normalized = text.strip()
    if not normalized:
        return []

    paragraphs = [p.strip() for p in _PARAGRAPH_SPLIT_PATTERN.split(normalized) if p.strip()]
    if not paragraphs:
        paragraphs = [normalized]

    units: list[str] = []
    for paragraph in paragraphs:
        if len(paragraph) > max_chars:
            sentences = [s.strip() for s in _SENTENCE_SPLIT_PATTERN.split(paragraph) if s.strip()]
            units.extend(sentences or [paragraph])
        else:
            units.append(paragraph)

    return _pack(units, max_chars=max_chars) or [normalized]
