from __future__ import annotations

from typing import Protocol


class FaceAgentProvider(Protocol):
    def generate_video(self, text: str, audio_url: str | None = None) -> str:
        ...
