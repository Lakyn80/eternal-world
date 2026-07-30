"""Task 65.9.1D (Docker Build Context Hygiene) - static, structured contract
test for the repository's `.dockerignore` files.

Deliberately does NOT implement a full Dockerignore-semantics parser (Docker
itself is the only authoritative implementation of that - see
`docker/docker-compose.yml` `build.context` values and the actual
`docker compose build` / `docker buildx build --check` runs recorded in
PROJECT_PROGRESS.md for the real validation). This file only checks two
narrow, high-value, easy-to-get-durably-wrong things at the *text* level:

1. Every Compose `build.context` that is actually declared in
   `docker-compose.yml` has an applicable `.dockerignore` file sitting at
   that exact context root (Docker only ever looks for `.dockerignore` at
   the context root, or a `<Dockerfile-name>.dockerignore` next to a
   specific Dockerfile - never at the repository root unless the context
   itself is the repository root, which it is not for this project).

2. Neither ignore file contains a bare, unqualified, whole-directory
   exclusion for one of the names this task's own specification calls out
   as unsafe blanket patterns (`app/`, `src/`, `backend/`, `frontend/`,
   `*.py`) - each of which would silently gut an entire build if ever
   added by a future careless edit.

This intentionally does NOT flag `tests/` or `scripts/` as forbidden lines,
even though the task specification lists `tests/`/`scripts/` among its
generic "don't do this by assumption" examples: this repository's
`backend/.dockerignore` and `frontend/.dockerignore` both contain a
deliberate, individually-justified `tests/` line (see the comments in
those files and PROJECT_PROGRESS.md, Task 65.9.1D) that was verified safe
via an isolated `docker build` reproduction - Docker's bare/no-slash
pattern matching is root-relative only (unlike `.gitignore`), the dev
service bind-mounts `./backend:/app` (or `./frontend:/app`) over whatever
the image contains at runtime, and the production Dockerfiles built from
these same contexts never execute a test suite. Re-litigating that
already-verified decision is out of scope for a lint-level contract test.

Run with the host Python interpreter from the repository root (same
convention as `test_task_65_9_1_compose_topology.py` in this directory):

    python -m pytest backend/tests_infra -q
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

yaml = pytest.importorskip("yaml", reason="PyYAML is required for the Docker ignore-file contract test")


REPO_ROOT = Path(__file__).resolve().parents[2]
DEV_COMPOSE_PATH = REPO_ROOT / "docker-compose.yml"
PROD_COMPOSE_PATH = REPO_ROOT / "docker-compose.prod.yml"

# Patterns that would each independently gut an entire build context if
# ever added as a bare, unqualified line. Deliberately narrower than the
# full list in the task specification - see module docstring for why
# `tests/`/`scripts/` are excluded from this particular automated check.
UNSAFE_BARE_PATTERNS = {
    "app",
    "app/",
    "src",
    "src/",
    "backend",
    "backend/",
    "frontend",
    "frontend/",
    "*.py",
}

# High-value categories that must be covered (as substrings of at least one
# non-comment line) for a context root to be considered hygienic. Kept
# deliberately short and specific to what was actually audited for this
# project, not a generic aspirational checklist.
REQUIRED_SUBSTRINGS_BY_CONTEXT = {
    "backend": (".env", "__pycache__", "artifacts/", ".git"),
    "frontend": (".env", "node_modules", ".git"),
}


def _load_compose(path: Path) -> dict[str, Any]:
    if not path.is_file():
        pytest.skip(f"{path} not reachable from this test run (see module docstring)")
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _declared_build_contexts(compose: dict[str, Any]) -> dict[str, str]:
    """Maps service name -> normalized (no leading `./`) build context path
    for every service that declares a `build.context` in the given, already
    -parsed Compose document. Services that only declare `image:` (no
    `build:` at all) are not build contexts and are correctly absent here."""

    services = compose.get("services")
    assert isinstance(services, dict), "Compose file has no top-level `services` mapping"
    contexts: dict[str, str] = {}
    for name, service in services.items():
        build = service.get("build") if isinstance(service, dict) else None
        if not isinstance(build, dict):
            continue
        context = build.get("context")
        assert context, f"service {name!r} declares `build:` but no `context:`"
        contexts[name] = context.removeprefix("./")
    return contexts


def _non_comment_lines(ignore_file: Path) -> list[str]:
    lines = []
    for raw_line in ignore_file.read_text(encoding="utf-8").splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        lines.append(stripped)
    return lines


def test_docker_compose_yml_declares_the_expected_build_contexts() -> None:
    """Baseline sanity check: this test's assumptions about which contexts
    exist must track reality, not the other way around."""

    compose = _load_compose(DEV_COMPOSE_PATH)
    contexts = _declared_build_contexts(compose)
    assert contexts, "docker-compose.yml must declare at least one build context"
    assert set(contexts.values()) == {"backend", "frontend"}, (
        "Task 65.9.1D audited exactly the `backend` and `frontend` build contexts - "
        f"a new/changed context ({contexts}) requires re-auditing before this test is updated"
    )


def test_docker_compose_prod_yml_uses_prebuilt_images_only() -> None:
    """`docker-compose.prod.yml` must keep using `image:` (pre-built, pushed
    to GHCR by .github/workflows/deploy-staging.yml) rather than a local
    `build:` context - if this ever changes, the production build-context
    hygiene story documented for Task 65.9.1D needs to be redone, not
    silently assumed to still hold."""

    compose = _load_compose(PROD_COMPOSE_PATH)
    contexts = _declared_build_contexts(compose)
    assert contexts == {}, (
        f"docker-compose.prod.yml now declares build context(s) {contexts} - "
        "Task 65.9.1D's audit assumed prod only consumes prebuilt images"
    )


@pytest.mark.parametrize("context_dir", ["backend", "frontend"])
def test_build_context_has_an_applicable_dockerignore(context_dir: str) -> None:
    ignore_path = REPO_ROOT / context_dir / ".dockerignore"
    assert ignore_path.is_file(), (
        f"{context_dir}/.dockerignore must exist at the build-context root - "
        "a repository-root .dockerignore would NOT apply here, since Docker "
        "only consults the ignore file located at (or Dockerfile-specific "
        f"within) the actual context root ({context_dir}/)"
    )


@pytest.mark.parametrize("context_dir", ["backend", "frontend"])
def test_dockerignore_covers_required_categories(context_dir: str) -> None:
    ignore_path = REPO_ROOT / context_dir / ".dockerignore"
    if not ignore_path.is_file():
        pytest.skip(f"{ignore_path} does not exist yet")
    text = ignore_path.read_text(encoding="utf-8")
    for required_substring in REQUIRED_SUBSTRINGS_BY_CONTEXT[context_dir]:
        assert required_substring in text, (
            f"{ignore_path} is missing an expected pattern covering {required_substring!r}"
        )


@pytest.mark.parametrize("context_dir", ["backend", "frontend"])
def test_dockerignore_has_no_unsafe_broad_exclusion(context_dir: str) -> None:
    ignore_path = REPO_ROOT / context_dir / ".dockerignore"
    if not ignore_path.is_file():
        pytest.skip(f"{ignore_path} does not exist yet")
    lines = set(_non_comment_lines(ignore_path))
    collisions = lines & UNSAFE_BARE_PATTERNS
    assert not collisions, (
        f"{ignore_path} contains unsafe blanket exclusion(s) {collisions} that "
        "would remove required application source from the build context"
    )


def test_dockerignore_files_do_not_exclude_dockerfiles_themselves() -> None:
    """A `.dockerignore` cannot exclude the Dockerfile Docker is about to
    read (Docker always reads the Dockerfile independently of the context
    filter), but a line like a bare `Dockerfile*` here would still be a
    sign of a copy-paste mistake worth catching early."""

    for context_dir in ("backend", "frontend"):
        ignore_path = REPO_ROOT / context_dir / ".dockerignore"
        if not ignore_path.is_file():
            continue
        lines = _non_comment_lines(ignore_path)
        for line in lines:
            assert not line.lower().startswith("dockerfile"), (
                f"{ignore_path} must not exclude Dockerfile* ({line!r})"
            )
