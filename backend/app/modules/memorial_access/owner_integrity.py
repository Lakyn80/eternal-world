"""Read-only Phase 5A memorial owner integrity checks.

Invariant split (Phase 5A):

* **DB:** at most one active owner membership per ``profile_id``
  (``uq_memorial_memberships_one_active_owner``).
* **Service (canonical create):** exactly one active owner whose
  ``user_id`` equals ``memory_profiles.user_id``
  (``memorial_access.service.create_memorial``).
* **Legacy compatibility:** profiles created via ``/api/memory-profiles``
  may temporarily have zero owner memberships until the creator hits a
  ``resolve_authorized_profile`` path, which self-heals one matching owner.

This module never mutates data. Use it for deploy preflight and ops audits.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

from sqlalchemy import text
from sqlalchemy.orm import Session


@dataclass(frozen=True)
class OwnerIntegrityFinding:
    code: str
    profile_id: int
    detail: str


@dataclass(frozen=True)
class OwnerIntegrityReport:
    profile_count: int
    findings: list[OwnerIntegrityFinding]

    @property
    def passed(self) -> bool:
        return not self.findings

    @property
    def zero_owner_count(self) -> int:
        return sum(1 for item in self.findings if item.code == "zero_active_owners")

    @property
    def multi_owner_count(self) -> int:
        return sum(1 for item in self.findings if item.code == "multiple_active_owners")

    @property
    def mismatch_count(self) -> int:
        return sum(1 for item in self.findings if item.code == "owner_profile_mismatch")

    def to_dict(self) -> dict:
        return {
            "passed": self.passed,
            "profile_count": self.profile_count,
            "zero_owner_count": self.zero_owner_count,
            "multiple_active_owners_count": self.multi_owner_count,
            "owner_profile_mismatch_count": self.mismatch_count,
            "findings": [asdict(item) for item in self.findings],
        }


def check_memorial_owner_integrity(db: Session) -> OwnerIntegrityReport:
    """Return all A/B/C owner integrity violations without writing."""

    profile_count = int(db.execute(text("SELECT COUNT(*) FROM memory_profiles")).scalar() or 0)
    findings: list[OwnerIntegrityFinding] = []

    zero_rows = db.execute(
        text(
            """
            SELECT mp.id AS profile_id, mp.name, mp.user_id AS profile_owner_user_id
            FROM memory_profiles mp
            LEFT JOIN memorial_memberships mm
              ON mm.profile_id = mp.id
             AND mm.role = 'owner'
             AND mm.status = 'active'
            GROUP BY mp.id, mp.name, mp.user_id
            HAVING COUNT(mm.id) = 0
            ORDER BY mp.id
            """
        )
    ).mappings().all()
    for row in zero_rows:
        findings.append(
            OwnerIntegrityFinding(
                code="zero_active_owners",
                profile_id=int(row["profile_id"]),
                detail=(
                    f"name={row['name']!r} profile_owner_user_id={row['profile_owner_user_id']} "
                    "(legacy-invalid until creator self-heal or explicit repair)"
                ),
            )
        )

    multi_rows = db.execute(
        text(
            """
            SELECT profile_id, COUNT(*) AS active_owner_count
            FROM memorial_memberships
            WHERE role = 'owner' AND status = 'active'
            GROUP BY profile_id
            HAVING COUNT(*) > 1
            ORDER BY profile_id
            """
        )
    ).mappings().all()
    for row in multi_rows:
        findings.append(
            OwnerIntegrityFinding(
                code="multiple_active_owners",
                profile_id=int(row["profile_id"]),
                detail=f"active_owner_count={row['active_owner_count']}",
            )
        )

    mismatch_rows = db.execute(
        text(
            """
            SELECT mp.id AS profile_id,
                   mp.user_id AS profile_owner_user_id,
                   mm.user_id AS membership_owner_user_id,
                   mm.id AS membership_id
            FROM memory_profiles mp
            JOIN memorial_memberships mm
              ON mm.profile_id = mp.id
             AND mm.role = 'owner'
             AND mm.status = 'active'
            WHERE mm.user_id <> mp.user_id
            ORDER BY mp.id
            """
        )
    ).mappings().all()
    for row in mismatch_rows:
        findings.append(
            OwnerIntegrityFinding(
                code="owner_profile_mismatch",
                profile_id=int(row["profile_id"]),
                detail=(
                    f"profile_owner_user_id={row['profile_owner_user_id']} "
                    f"membership_owner_user_id={row['membership_owner_user_id']} "
                    f"membership_id={row['membership_id']}"
                ),
            )
        )

    return OwnerIntegrityReport(profile_count=profile_count, findings=findings)
