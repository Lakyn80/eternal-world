from __future__ import annotations

from typing import Protocol


class VoiceAgentProvider(Protocol):
    def generate_audio(self, text: str) -> str:
        ...
