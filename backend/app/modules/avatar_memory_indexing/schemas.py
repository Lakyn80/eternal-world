from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class AvatarMemoryIndexingRead(BaseModel):
    promotion_id: int
    promotion_status: str
    indexed_at: datetime | None
    target_collection_name: str | None
    qdrant_point_id: str | None
    searchable_as_fact: bool
    result: str
    #: Task 65.9 (Part C/D) - present when this reflects an async job that
    #: was just created/reused rather than a synchronously-completed
    #: result. `None` for the legacy direct-call path (still used by
    #: internal scripts/tests that call `index_promotion` directly).
    job_id: int | None = None


class AvatarMemoryIndexingPreview(BaseModel):
    promotion_id: int
    candidate_id: int
    avatar_id: str
    profile_id: int
    target_collection_name: str
    qdrant_point_id: str
    model_code: str
    text_length: int
    eligible: bool = True


class AvatarMemoryIndexingBatchSummary(BaseModel):
    eligible: int = 0
    indexed: int = 0
    failed: int = 0
    skipped: int = 0
    already_indexed: int = 0
    items: list[dict[str, object]]
