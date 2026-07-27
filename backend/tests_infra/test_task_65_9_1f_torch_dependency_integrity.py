"""Task 65.9.1F (Backend Dependency Integrity Repair) - static, structured
contract test for the CPU-only PyTorch dependency pin introduced by this
task.

Context: prior to this task, `backend/Dockerfile` and
`backend/Dockerfile.ai-base` each ran an *unpinned* `pip install
--index-url https://download.pytorch.org/whl/cpu torch` - no version pin,
no hash, duplicated verbatim in two Dockerfiles. Investigating the
reported "Expected SHA256 .../Received SHA256 ..." symptom (Part C) found
that pip's hash-checking mode was never enabled by anything in this repo
or the `python:3.12-slim` base image (no `--require-hashes`, no `--hash`
in any requirements file, no `PIP_REQUIRE_HASHES`/other `PIP_*` env var,
no global/site/user `pip.conf` - all verified directly via `python -m pip
config debug`/`list -v` inside a disposable container from the same base
image, and via a full reproduction of the prior literal Dockerfile RUN
command, which completed with zero hash errors). The actual mechanism
that CAN produce that exact error message is pip's own automatic,
always-on verification of a downloaded distribution against the hash the
package index publishes in its own simple-repository metadata - which
fires independently of any project file.

This task's required two-independent-download provenance check (Part D)
then reproduced a genuine, live mismatch: two back-to-back `pip download
--no-cache-dir` runs of the exact same wheel (same URL, same official
index) returned different content - one matched the index's own declared
hash (`4ca4a9394b0c771238a4f73590fdbbc4debad85ed0fa63d026ae1b085da7d6e2`),
the other did not (rejected by pip's own check before use). Per this
task's explicit safety rule, that means a hash must NOT be inserted
anywhere this session - see `backend/requirements-torch-cpu.txt`'s module
comment and PROJECT_PROGRESS.md (Task 65.9.1F) for the full trace.

What this test suite asserts is therefore deliberately scoped to what
*is* safely true today: an exact, explicit CPU-only version pin,
centralized in one file both Dockerfiles consume (no more duplicated,
independently-drifting ad-hoc install lines), no CUDA reference anywhere,
and no conflicting `torch` declaration elsewhere. It does NOT assert that
a hash is present (there deliberately isn't one yet - see above) and does
NOT download the ~192MB wheel (or any dependency wheel) - every assertion
here is a static parse of the lock file and the two Dockerfiles. Run with
the host Python interpreter:

    python -m pytest backend/tests_infra -q
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[2]
BACKEND_DIR = REPO_ROOT / "backend"
TORCH_LOCK_PATH = BACKEND_DIR / "requirements-torch-cpu.txt"
DEV_DOCKERFILE_PATH = BACKEND_DIR / "Dockerfile"
AI_BASE_DOCKERFILE_PATH = BACKEND_DIR / "Dockerfile.ai-base"
PROD_DOCKERFILE_PATH = BACKEND_DIR / "Dockerfile.prod"
OTHER_REQUIREMENTS_PATHS = (
    BACKEND_DIR / "requirements.txt",
    BACKEND_DIR / "requirements.runtime.txt",
    BACKEND_DIR / "requirements.ai-base.txt",
)
GITIGNORE_PATH = REPO_ROOT / ".gitignore"
DOCKERIGNORE_PATH = BACKEND_DIR / ".dockerignore"
CELERYBEAT_SCHEDULE_PATH = BACKEND_DIR / "celerybeat-schedule"

# Official PyTorch CPU wheel index this project is pinned to - never a
# third-party mirror, never a CUDA index (Part D/Part E of Task 65.9.1F).
EXPECTED_TORCH_INDEX_URL = "https://download.pytorch.org/whl/cpu"

# Substrings that would indicate a CUDA build/index ever crept back in.
FORBIDDEN_CUDA_MARKERS = ("+cu1", "+cu2", "cu118", "cu121", "cu124", "cu126", "nvidia-")


def _read(path: Path) -> str:
    if not path.is_file():
        pytest.skip(f"{path} not reachable from this test run")
    return path.read_text(encoding="utf-8")


def _non_comment_lines(text: str) -> list[str]:
    lines = []
    for raw_line in text.splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        lines.append(stripped)
    return lines


def test_torch_cpu_lock_file_exists() -> None:
    assert TORCH_LOCK_PATH.is_file(), (
        "Task 65.9.1F introduces backend/requirements-torch-cpu.txt as the single "
        "source of truth for the pinned CPU Torch dependency"
    )


def test_torch_cpu_lock_uses_official_cpu_index_only() -> None:
    text = _read(TORCH_LOCK_PATH)
    assert EXPECTED_TORCH_INDEX_URL in text, (
        f"{TORCH_LOCK_PATH} must declare the official PyTorch CPU index ({EXPECTED_TORCH_INDEX_URL})"
    )
    # No other --index-url/--extra-index-url pointing anywhere else - a
    # third-party mirror would defeat the entire provenance investigation.
    index_lines = [
        line
        for line in _non_comment_lines(text)
        if line.startswith("--index-url") or line.startswith("--extra-index-url")
    ]
    assert index_lines, f"{TORCH_LOCK_PATH} must explicitly declare an --index-url"
    for line in index_lines:
        assert EXPECTED_TORCH_INDEX_URL in line, f"unexpected non-official index declared: {line!r}"


def test_torch_is_exactly_pinned_to_a_cpu_build() -> None:
    text = _read(TORCH_LOCK_PATH)
    match = re.search(r"^torch==([^\s;]+)", text, flags=re.MULTILINE)
    assert match, f"{TORCH_LOCK_PATH} must pin an exact `torch==<version>` requirement (no range, no bare 'torch')"
    version = match.group(1)
    assert version.endswith("+cpu"), (
        f"torch must be pinned to an explicit CPU build (version was {version!r}, expected a '+cpu' suffix)"
    )
    for marker in FORBIDDEN_CUDA_MARKERS:
        assert marker not in version, f"torch version {version!r} must never reference a CUDA build ({marker!r})"


def test_torch_cpu_lock_has_no_cuda_markers_anywhere() -> None:
    text = _read(TORCH_LOCK_PATH)
    lowered = text.lower()
    for marker in FORBIDDEN_CUDA_MARKERS:
        assert marker not in lowered, f"{TORCH_LOCK_PATH} must never reference a CUDA marker ({marker!r})"


def test_torch_cpu_lock_documents_why_no_hash_is_present_yet() -> None:
    """Task 65.9.1F's Part D provenance check found a genuine, reproducible
    hash mismatch between two independent downloads of the same official
    wheel - per the task's explicit safety rule, no hash may be inserted
    until that is resolved. This must stay documented in the lock file
    itself (not just in PROJECT_PROGRESS.md prose) so a future edit to
    this file does not silently drop the reason and add an unverified
    hash. If a future task DOES add a verified hash, it should also
    remove/replace this documentation - this test only guards against the
    hash appearing with no explanation at all."""

    text = _read(TORCH_LOCK_PATH)
    has_hash = "--hash=sha256:" in text
    if has_hash:
        pytest.skip(
            "requirements-torch-cpu.txt now carries a hash - presumably a later task "
            "completed the provenance re-check; this test's guard no longer applies"
        )
    assert "mismatch" in text.lower() or "provenance" in text.lower(), (
        f"{TORCH_LOCK_PATH} has no hash - it must document why (see Task 65.9.1F's Part D finding)"
    )


@pytest.mark.parametrize("dockerfile_path", [DEV_DOCKERFILE_PATH, AI_BASE_DOCKERFILE_PATH], ids=["dev", "ai-base"])
def test_dockerfile_installs_the_shared_torch_lock_file(dockerfile_path: Path) -> None:
    text = _read(dockerfile_path)
    assert "requirements-torch-cpu.txt" in text, (
        f"{dockerfile_path} must install the shared requirements-torch-cpu.txt "
        "rather than its own ad-hoc, independently-drifting torch install"
    )


@pytest.mark.parametrize("dockerfile_path", [DEV_DOCKERFILE_PATH, AI_BASE_DOCKERFILE_PATH], ids=["dev", "ai-base"])
def test_dockerfile_has_no_unpinned_bare_torch_install(dockerfile_path: Path) -> None:
    """The historical defect: `pip install ... torch` with no version pin,
    resolved fresh (and potentially differently) on every build. Assert
    this exact pattern is gone - every remaining torch-related install
    line must go through the shared lock file."""

    text = _read(dockerfile_path)
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#") or "pip install" not in stripped:
            continue
        if re.search(r"\btorch\b", stripped) and "requirements-torch-cpu.txt" not in stripped:
            pytest.fail(f"{dockerfile_path} still has an ad-hoc torch install outside the lock file: {stripped!r}")


@pytest.mark.parametrize("dockerfile_path", [DEV_DOCKERFILE_PATH, AI_BASE_DOCKERFILE_PATH], ids=["dev", "ai-base"])
def test_dockerfile_does_not_falsely_claim_hash_verification(dockerfile_path: Path) -> None:
    """`--require-hashes` must never appear for a lock file that has no
    hashes - that would fail every build outright (or, worse, mislead a
    reader into believing hash verification is active when it is not)."""

    text = _read(dockerfile_path)
    lock_text = _read(TORCH_LOCK_PATH)
    if "--hash=sha256:" in lock_text:
        pytest.skip("torch lock file now carries hashes - --require-hashes would be expected/appropriate")
    for line in text.splitlines():
        if "requirements-torch-cpu.txt" in line:
            assert "--require-hashes" not in line, (
                f"{dockerfile_path} claims --require-hashes for a lock file with no hashes present: {line!r}"
            )


def test_dockerfile_prod_does_not_install_torch_directly() -> None:
    """Dockerfile.prod builds FROM the prebuilt python-ai-base image (which
    itself is built from Dockerfile.ai-base), so it must never re-declare
    its own torch install - that would be a second, driftable source of
    truth for the same dependency."""

    if not PROD_DOCKERFILE_PATH.is_file():
        pytest.skip(f"{PROD_DOCKERFILE_PATH} not reachable from this test run")
    text = PROD_DOCKERFILE_PATH.read_text(encoding="utf-8")
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if "pip install" in stripped and re.search(r"\btorch\b", stripped):
            pytest.fail(f"{PROD_DOCKERFILE_PATH} must not install torch directly: {stripped!r}")


def test_no_other_requirements_file_redeclares_torch() -> None:
    """A second, conflicting `torch` line in any of the plain requirements
    files would silently reintroduce version drift between build stages."""

    for path in OTHER_REQUIREMENTS_PATHS:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for line in _non_comment_lines(text):
            assert not re.match(r"^torch\b", line), (
                f"{path} must not declare its own `torch` requirement - "
                "requirements-torch-cpu.txt is the single source of truth"
            )


# ---------------------------------------------------------------------------
# Task 65.9.1F.2 - Celery Beat runtime-artifact hygiene.
#
# `backend/celerybeat-schedule` is a GNU dbm/ndbm database that the
# maintenance_worker's `celery beat` process writes to at runtime (its own
# schedule bookkeeping) - it is generated state, not application source, and
# must never be tracked by Git or shipped inside a Docker build context. The
# tests below assert the narrow, exact ignore rules added to the repo-root
# `.gitignore` and `backend/.dockerignore` are present, and that the file is
# not (and never becomes) tracked - they do not read or print the file's
# contents, and they do not require the runtime file to exist on disk (a
# fresh checkout with no maintenance_worker run yet has no such file).
# ---------------------------------------------------------------------------


def test_gitignore_covers_celerybeat_schedule_exactly() -> None:
    text = _read(GITIGNORE_PATH)
    lines = {line.strip() for line in text.splitlines()}
    assert "backend/celerybeat-schedule" in lines, (
        f"{GITIGNORE_PATH} must ignore the exact path backend/celerybeat-schedule"
    )
    assert "backend/celerybeat-schedule.*" in lines, (
        f"{GITIGNORE_PATH} must ignore backend/celerybeat-schedule's sibling shelve/dbm "
        "suffix files (e.g. .db/.dat/.dir/.bak) with an exact, narrow pattern"
    )
    # Guard against a future edit widening this to something that could
    # shadow real source files under backend/ (e.g. `backend/*` or a bare
    # `*schedule*`).
    forbidden = ("backend/*", "*schedule*", "*.db")
    for pattern in forbidden:
        assert pattern not in lines, (
            f"{GITIGNORE_PATH} must not use the overly broad pattern {pattern!r} - "
            "only the exact celerybeat-schedule paths are permitted"
        )


def test_dockerignore_covers_celerybeat_schedule_exactly() -> None:
    text = _read(DOCKERIGNORE_PATH)
    lines = {line.strip() for line in text.splitlines()}
    assert "celerybeat-schedule" in lines, (
        f"{DOCKERIGNORE_PATH} must exclude the context-relative celerybeat-schedule file "
        "from the backend Docker build context"
    )
    assert "celerybeat-schedule.*" in lines, (
        f"{DOCKERIGNORE_PATH} must exclude celerybeat-schedule's sibling shelve/dbm suffix "
        "files with an exact, narrow pattern"
    )
    forbidden = ("backend/*", "*schedule*", "*.db")
    for pattern in forbidden:
        assert pattern not in lines, (
            f"{DOCKERIGNORE_PATH} must not use the overly broad pattern {pattern!r} - "
            "only the exact celerybeat-schedule paths are permitted"
        )


def test_celerybeat_schedule_is_not_git_tracked() -> None:
    """Regardless of whether the runtime file currently exists on this
    machine, it must never be a tracked path in the repository."""

    result = subprocess.run(
        ["git", "ls-files", "--", "backend/celerybeat-schedule"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, f"git ls-files failed: {result.stderr}"
    assert result.stdout.strip() == "", (
        "backend/celerybeat-schedule must never be tracked by Git - it is Celery Beat "
        "runtime state, not application source"
    )


def test_celerybeat_schedule_is_ignored_when_present() -> None:
    """If the runtime file happens to exist on this machine (as it will on
    any host that has run the maintenance_worker's `celery beat` process
    locally), `git check-ignore` must positively match it against the new
    rule. This test does not create the file and does not read its
    contents - it only skips if the file is absent (e.g. a fresh CI
    checkout that never ran Celery Beat)."""

    if not CELERYBEAT_SCHEDULE_PATH.exists():
        pytest.skip("backend/celerybeat-schedule not present on this machine - nothing to verify")
    result = subprocess.run(
        ["git", "check-ignore", "-v", "--", "backend/celerybeat-schedule"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, (
        f"git check-ignore must match backend/celerybeat-schedule (rc={result.returncode}): "
        f"{result.stdout!r} {result.stderr!r}"
    )
    assert ".gitignore" in result.stdout, (
        f"expected the match to come from .gitignore, got: {result.stdout!r}"
    )
