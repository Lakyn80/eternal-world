"""Task 65.9.1 (Part D/E) - static, structured (never string-grep) Compose
contract test for worker queue isolation.

Deliberately has ZERO dependency on the FastAPI app, the database, Celery,
or any other backend module - it only parses the two repository-root
`docker-compose*.yml` files with PyYAML and asserts on the resulting data
structure. This is intentional: `docker-compose.yml`/`docker-compose.prod.yml`
live at the repository root and are NOT inside the `backend/` directory that
this dev stack bind-mounts into the `backend`/`celery_worker`/etc. containers
(they configure those containers - a file cannot usefully describe its own
container from inside it), so this file cannot be exercised via
`docker compose exec backend pytest ...` in this environment.

It also deliberately lives in `backend/tests_infra/` rather than
`backend/tests/`: the latter's `conftest.py` has an autouse fixture chain
that imports `app.core.config`/the full FastAPI app, which requires the
docker backend's installed dependencies (psycopg, etc.) that the *host*
Python interpreter does not have - and this file must run on the host,
since the compose YAML files it reads are not visible from inside the
backend container at all. Keeping it out of `backend/tests/` avoids that
conftest entirely. Run it with the host Python interpreter from the
repository root:

    python -m pytest backend/tests_infra -q

If the compose files are genuinely unreachable (e.g. a checkout that only
has the `backend/` subtree), every test here skips with a clear reason
rather than failing - a repo-layout limitation, not a topology defect.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

yaml = pytest.importorskip("yaml", reason="PyYAML is required for the Compose structural contract test")


REPO_ROOT = Path(__file__).resolve().parents[2]
DEV_COMPOSE_PATH = REPO_ROOT / "docker-compose.yml"
PROD_COMPOSE_PATH = REPO_ROOT / "docker-compose.prod.yml"

EXPECTED_GENERAL_WORKER_QUEUES = {"document_processing", "ai_generation", "media", "notifications"}
EXPECTED_EMBEDDING_QUEUES = {"embedding"}
EXPECTED_MAINTENANCE_QUEUES = {"maintenance"}


def _load_compose(path: Path) -> dict[str, Any]:
    if not path.is_file():
        pytest.skip(f"{path} not reachable from this test run (see module docstring)")
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _command_text(service: dict[str, Any]) -> str:
    """Normalizes a Compose `command` value (string, YAML block scalar, or
    list-of-args form) into one whitespace-joined string so `-Q` parsing
    below does not care which style a given service uses."""

    command = service.get("command")
    if command is None:
        return ""
    if isinstance(command, list):
        return " ".join(str(part) for part in command)
    return str(command)


def _queues_from_command(command_text: str) -> set[str] | None:
    """Extracts the comma-separated queue list following a `-Q` flag.
    Returns None if no `-Q` flag is present at all (i.e. an unrestricted
    worker that would subscribe to every declared queue)."""

    tokens = command_text.split()
    for index, token in enumerate(tokens):
        if token == "-Q" and index + 1 < len(tokens):
            return {queue.strip() for queue in tokens[index + 1].split(",") if queue.strip()}
        if token.startswith("-Q") and len(token) > 2:
            return {queue.strip() for queue in token[2:].split(",") if queue.strip()}
    return None


@pytest.mark.parametrize("compose_path", [DEV_COMPOSE_PATH, PROD_COMPOSE_PATH], ids=["dev", "prod"])
class TestWorkerQueueIsolation:
    def _services(self, compose_path: Path) -> dict[str, Any]:
        compose = _load_compose(compose_path)
        services = compose.get("services")
        assert isinstance(services, dict), f"{compose_path} has no top-level `services` mapping"
        return services

    def test_general_worker_has_explicit_restricted_queue_list(self, compose_path: Path) -> None:
        services = self._services(compose_path)
        assert "celery_worker" in services, "general celery_worker service must exist"
        queues = _queues_from_command(_command_text(services["celery_worker"]))
        assert queues is not None, "celery_worker must pass an explicit -Q flag (no unrestricted subscription)"
        assert queues == EXPECTED_GENERAL_WORKER_QUEUES
        assert "embedding" not in queues
        assert "maintenance" not in queues

    def test_embedding_worker_consumes_only_embedding(self, compose_path: Path) -> None:
        services = self._services(compose_path)
        assert "embedding_worker" in services, "dedicated embedding_worker service must exist"
        queues = _queues_from_command(_command_text(services["embedding_worker"]))
        assert queues == EXPECTED_EMBEDDING_QUEUES

    def test_maintenance_worker_consumes_only_maintenance(self, compose_path: Path) -> None:
        services = self._services(compose_path)
        assert "maintenance_worker" in services, "dedicated maintenance_worker service must exist"
        queues = _queues_from_command(_command_text(services["maintenance_worker"]))
        assert queues == EXPECTED_MAINTENANCE_QUEUES

    def test_no_worker_service_mounts_the_docker_socket(self, compose_path: Path) -> None:
        services = self._services(compose_path)
        for name in ("celery_worker", "embedding_worker", "maintenance_worker"):
            volumes = services[name].get("volumes") or []
            for volume in volumes:
                volume_text = volume if isinstance(volume, str) else str(volume)
                assert "docker.sock" not in volume_text, f"{name} must never mount the Docker socket"

    def test_no_worker_service_is_privileged(self, compose_path: Path) -> None:
        services = self._services(compose_path)
        for name in ("celery_worker", "embedding_worker", "maintenance_worker"):
            assert services[name].get("privileged") is not True, f"{name} must never run privileged"

    def test_no_worker_service_publishes_a_port(self, compose_path: Path) -> None:
        services = self._services(compose_path)
        for name in ("celery_worker", "embedding_worker", "maintenance_worker"):
            assert not services[name].get("ports"), f"{name} must never publish a port"

    def test_embedding_worker_uses_bounded_single_concurrency(self, compose_path: Path) -> None:
        services = self._services(compose_path)
        command_text = _command_text(services["embedding_worker"])
        assert "--concurrency=1" in command_text
        assert "--prefetch-multiplier=1" in command_text


def test_declared_queue_names_cover_every_worker_queue_list() -> None:
    """Cross-check against the celery_app source of truth (read directly
    from the file, not via `import app.worker.celery_app`, so this test
    still works even when the backend package itself is not importable
    from wherever this file is executed)."""

    celery_app_source = REPO_ROOT / "backend" / "app" / "worker" / "celery_app.py"
    if not celery_app_source.is_file():
        pytest.skip("backend/app/worker/celery_app.py not reachable from this test run")
    text = celery_app_source.read_text(encoding="utf-8")
    for queue_name in EXPECTED_GENERAL_WORKER_QUEUES | EXPECTED_EMBEDDING_QUEUES | EXPECTED_MAINTENANCE_QUEUES:
        assert f'"{queue_name}"' in text, f"queue {queue_name!r} must be declared in celery_app.py"
