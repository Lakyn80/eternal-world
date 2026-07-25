"""Task 65.9 (Part Z) - reproducible, fake-safe load-test harness.

Three profiles:

  smoke  - local, fake embedding provider/broker, small dataset, quick
           validation. Safe to run anytime, anywhere, including this dev
           container - fully hermetic (isolated in-memory SQLite database,
           no real Redis/Qdrant/BGE-M3/DeepSeek call, no shared dev data
           touched).
  scale  - configurable registered-user cardinality / API concurrency /
           approval-indexing burst / worker replicas, against a real
           isolated staging deployment. Not executed by this harness in
           this environment (no isolated staging environment was
           available this session) - use this script's own `--profile
           scale` flags as the exact prepared command once one exists.
  stress - deliberately exceeds expected capacity to verify backpressure
           and controlled degradation. Same "prepared, not executed here"
           status as `scale`.

Never claims a specific concurrent-user capacity - only reports what was
actually measured in the current run.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import dataclass, field
from statistics import mean
from unittest.mock import patch

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.base import Base
from app.db.session import get_db
from app.main import app
from app.modules.embeddings.providers.base import EmbeddingVector
from app.modules.rag_retrieval.service import _is_visible_to_viewer


PASSWORD = "StrongPass123"


class FakeLoadTestEncoder:
    def encode(self, *, text: str, model_code: str) -> EmbeddingVector:
        return EmbeddingVector(values=[0.01] * 1024, dimension=1024, metadata={"provider_name": "fake_load_test"})


class FakeLoadTestWriter:
    def __init__(self) -> None:
        self.points: dict[tuple[str, str], dict[str, object]] = {}
        self.upsert_calls = 0

    def collection_vector_size(self, *, collection_name: str) -> int | None:
        return 1024

    def get_point(self, *, collection_name: str, point_id: str) -> dict[str, object] | None:
        return self.points.get((collection_name, point_id))

    def upsert_point(self, *, collection_name: str, point_id: str, vector, payload) -> None:
        self.upsert_calls += 1
        self.points[(collection_name, point_id)] = {"vector": list(vector), "payload": dict(payload)}

    def delete_point(self, *, collection_name: str, point_id: str) -> None:
        self.points.pop((collection_name, point_id), None)


@dataclass
class LoadTestResult:
    profile: str
    users: int
    request_count: int = 0
    enqueue_latencies_ms: list[float] = field(default_factory=list)
    job_completion_latencies_ms: list[float] = field(default_factory=list)
    duplicate_qdrant_point_count: int = 0
    failed_job_count: int = 0
    retry_count: int = 0
    cross_profile_contamination_count: int = 0
    private_leak_count: int = 0
    total_duration_seconds: float = 0.0

    def percentile(self, values: list[float], pct: float) -> float:
        if not values:
            return 0.0
        ordered = sorted(values)
        index = min(len(ordered) - 1, int(round(pct / 100.0 * (len(ordered) - 1))))
        return ordered[index]

    def to_dict(self) -> dict[str, object]:
        return {
            "profile": self.profile,
            "users": self.users,
            "request_count": self.request_count,
            "enqueue_latency_p50_ms": round(self.percentile(self.enqueue_latencies_ms, 50), 3),
            "enqueue_latency_p95_ms": round(self.percentile(self.enqueue_latencies_ms, 95), 3),
            "enqueue_latency_p99_ms": round(self.percentile(self.enqueue_latencies_ms, 99), 3),
            "job_completion_latency_mean_ms": round(mean(self.job_completion_latencies_ms), 3)
            if self.job_completion_latencies_ms
            else 0.0,
            "duplicate_qdrant_point_count": self.duplicate_qdrant_point_count,
            "failed_job_count": self.failed_job_count,
            "retry_count": self.retry_count,
            "cross_profile_contamination_count": self.cross_profile_contamination_count,
            "private_leak_count": self.private_leak_count,
            "total_duration_seconds": round(self.total_duration_seconds, 3),
        }


def _build_hermetic_client():
    from fastapi.testclient import TestClient

    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = testing_session_local()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    app.state.testing_session_local = testing_session_local
    client = TestClient(app)
    return client, engine


def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def run_smoke(*, users: int) -> LoadTestResult:
    result = LoadTestResult(profile="smoke", users=users)
    started_at = time.perf_counter()

    client, engine = _build_hermetic_client()
    fake_sender_calls = {"n": 0}

    def fake_sender(**kwargs):
        fake_sender_calls["n"] += 1
        return f"fake-task-{fake_sender_calls['n']}"

    with patch(
        "app.modules.job_outbox.service._default_task_sender",
        side_effect=lambda **kwargs: fake_sender(**kwargs),
    ):
        promotion_ids: list[int] = []
        profile_ids: list[int] = []
        for index in range(users):
            email = f"load-smoke-user-{index}@example.com"
            client.post("/api/auth/register", json={"email": email, "password": PASSWORD, "full_name": "Load User"})
            login = client.post("/api/auth/login", json={"email": email, "password": PASSWORD})
            token = login.json()["access_token"]

            memorial = client.post("/api/memorials", headers=_auth_headers(token), json={"name": f"Memorial {index}"})
            profile_id = memorial.json()["id"]
            profile_ids.append(profile_id)

            submit_started = time.perf_counter()
            submitted = client.post(
                f"/api/memorials/{profile_id}/contributions",
                headers=_auth_headers(token),
                json={
                    "title": "Load test memory",
                    "memory_text": f"Synthetic load-test memory number {index}.",
                    "privacy_scope": "private_owner" if index % 5 == 0 else "all_family",
                },
            )
            contribution_id = submitted.json()["id"]

            approved = client.post(
                f"/api/memorials/{profile_id}/contributions/{contribution_id}/approve",
                headers=_auth_headers(token),
                json={},
            )
            enqueue_latency_ms = (time.perf_counter() - submit_started) * 1000
            result.enqueue_latencies_ms.append(enqueue_latency_ms)
            result.request_count += 3

            if approved.status_code != 200:
                result.failed_job_count += 1
                continue

            promotion_status = approved.json()["indexing_status"]["state"]
            if promotion_status != "pending":
                result.failed_job_count += 1

            db = app.state.testing_session_local()
            try:
                from app.modules.memorial_contribution_indexing.repository import get_promotion_by_contribution_id
                from app.modules.memorial_contribution_indexing.service import index_contribution_promotion

                promotion = get_promotion_by_contribution_id(db, contribution_id=contribution_id)
                promotion_ids.append(promotion.id)

                completion_started = time.perf_counter()
                writer = FakeLoadTestWriter()
                encoder = FakeLoadTestEncoder()
                indexing_result = index_contribution_promotion(
                    db, profile_id=profile_id, promotion_id=promotion.id, writer=writer, encoder=encoder
                )
                result.job_completion_latencies_ms.append((time.perf_counter() - completion_started) * 1000)
                if indexing_result.result not in ("indexed", "already_indexed"):
                    result.failed_job_count += 1

                # Duplicate-delivery / idempotency check: re-run the exact
                # same idempotent operation and confirm no second point.
                second_result = index_contribution_promotion(
                    db, profile_id=profile_id, promotion_id=promotion.id, writer=writer, encoder=encoder
                )
                if writer.upsert_calls != 1:
                    result.duplicate_qdrant_point_count += 1
                if second_result.result != "already_indexed":
                    result.retry_count += 1

                # Privacy invariant: private_owner content must not be
                # visible to a non-owner viewer.
                if index % 5 == 0:
                    payload_metadata = {"privacy_scope": "private_owner"}
                    if _is_visible_to_viewer(payload_metadata, viewer_is_profile_owner=False):
                        result.private_leak_count += 1
            finally:
                db.close()

        # Cross-profile contamination invariant: every promotion's stored
        # profile_id must match the memorial it was created under - no
        # promotion should ever resolve to a foreign profile.
        db = app.state.testing_session_local()
        try:
            from app.db.models import MemorialContributionPromotion

            for promotion_id, expected_profile_id in zip(promotion_ids, profile_ids):
                promotion_row = db.get(MemorialContributionPromotion, promotion_id)
                if promotion_row is None or promotion_row.profile_id != expected_profile_id:
                    result.cross_profile_contamination_count += 1
        finally:
            db.close()

    Base.metadata.drop_all(bind=engine)
    engine.dispose()
    app.dependency_overrides.clear()
    if hasattr(app.state, "testing_session_local"):
        delattr(app.state, "testing_session_local")

    result.total_duration_seconds = time.perf_counter() - started_at
    return result


def _print_scale_or_stress_not_run(*, profile: str, args: argparse.Namespace) -> None:
    print(f"LOAD TEST PROFILE '{profile}': NOT RUN in this environment.")
    print(
        "Reason: this profile requires a real, isolated staging deployment "
        "(separate database/broker/Qdrant from any shared dev environment) "
        "- none was available in this session."
    )
    print("Prepared exact command for when such an environment exists:")
    print(
        f"  docker compose -f docker-compose.prod.yml exec backend "
        f"python scripts/run_async_job_load_smoke.py --profile {profile} "
        f"--users {args.users} --api-concurrency {args.api_concurrency} "
        f"--worker-replicas {args.worker_replicas}"
    )
    print(
        "Do not claim a specific concurrent-user capacity from this "
        "harness unless it was actually run against real infrastructure "
        "and the result is reproduced here."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Task 65.9 async job platform load-test harness.")
    parser.add_argument("--profile", choices=["smoke", "scale", "stress"], default="smoke")
    parser.add_argument("--users", type=int, default=25)
    parser.add_argument("--api-concurrency", type=int, default=1)
    parser.add_argument("--worker-replicas", type=int, default=1)
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args()

    if args.profile != "smoke":
        _print_scale_or_stress_not_run(profile=args.profile, args=args)
        return 0

    result = run_smoke(users=args.users)
    payload = result.to_dict()

    if args.json_output:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(f"LOAD TEST SMOKE RESULT (users={args.users})")
        for key, value in payload.items():
            print(f"  {key}: {value}")

    invariant_failure = (
        payload["duplicate_qdrant_point_count"] > 0
        or payload["cross_profile_contamination_count"] > 0
        or payload["private_leak_count"] > 0
    )
    return 1 if invariant_failure else 0


if __name__ == "__main__":
    sys.exit(main())
