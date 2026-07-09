from __future__ import annotations

from pydantic import BaseModel


class DemoFaChatMessageRequest(BaseModel):
    profile_id: int | None = None
    message: str
    debug: bool | None = None


class DemoFaChatEvidenceItem(BaseModel):
    chunk_id: str
    source_id: int | None = None
    source_title: str | None = None
    score: float | None = None
    text_preview: str | None = None


class DemoFaChatMessageResponse(BaseModel):
    answer: str
    lack_of_evidence: bool
    retrieval_used: bool
    guard_applied: bool
    guard_reason: str | None = None
    trace_id: str
    evidence: list[DemoFaChatEvidenceItem]


class DemoFaChatErrorResponse(BaseModel):
    detail: str
    trace_id: str | None = None
