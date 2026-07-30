"""Lightweight chat message language detection for persona response selection.

Deterministic heuristics only — no model download, no network. Used so
authenticated chat can answer in the user's language instead of always
forcing ``primary_language``.
"""

from __future__ import annotations

import re

# Czech-specific letters (beyond shared Latin diacritics with Slovak/etc.).
_CZECH_CHARS = set("ěščřžýáíéůúďťňóĚŠČŘŽÝÁÍÉŮÚĎŤŇÓ")
_GERMAN_CHARS = set("äöüßÄÖÜ")
_CYRILLIC_RE = re.compile(r"[\u0400-\u04FF]")
_LATIN_LETTER_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿĀ-ž]")


def detect_message_language(text: str) -> str | None:
    """Return ``cs`` / ``en`` / ``ru`` / ``de`` when confident, else ``None``.

    Priority: Cyrillic → ``ru``; Czech diacritics → ``cs``; German diacritics →
    ``de``; otherwise Latin letters → ``en``. Empty / emoji-only → ``None``.
    """

    if not isinstance(text, str):
        return None
    sample = text.strip()
    if not sample:
        return None

    if _CYRILLIC_RE.search(sample):
        return "ru"

    czech_hits = sum(1 for ch in sample if ch in _CZECH_CHARS)
    if czech_hits > 0:
        return "cs"

    german_hits = sum(1 for ch in sample if ch in _GERMAN_CHARS)
    if german_hits > 0:
        return "de"

    if _LATIN_LETTER_RE.search(sample):
        return "en"

    return None
