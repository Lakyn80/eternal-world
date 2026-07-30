from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class ContributionIndexingStatusRead(BaseModel):
    """Backend-derived indexing state for one contribution, safe to expose
    directly on `ContributionRead` - the frontend must never infer
    "searchable" purely from `contribution.status`."""

    state: str
    indexed_at: datetime | None = None
    attempt_count: int = 0
    failure_reason: str | None = None
    #: Task 65.9.1 (Part F) - the active background job id backing a
    #: `pending` state, when one currently exists, so the frontend can poll
    #: `GET /api/jobs/{job_id}` for the full lifecycle instead of only
    #: reloading the whole contribution list. Always `None` for every other
    #: state (indexed/failed/retired/not_applicable have no active job).
    job_id: int | None = None


class ContributionIndexingRead(BaseModel):
    promotion_id: int
    contribution_id: int
    promotion_status: str
    indexed_at: datetime | None
    target_collection_name: str | None
    qdrant_point_id: str | None
    searchable_as_fact: bool
    result: str
