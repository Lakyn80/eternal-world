from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from alembic.config import Config
from alembic.script import ScriptDirectory


def test_alembic_configuration_loads_revision_history():
    backend_dir = Path(__file__).resolve().parents[1]
    config = Config(str(backend_dir / "alembic.ini"))
    config.set_main_option("script_location", str(backend_dir / "alembic"))

    script_directory = ScriptDirectory.from_config(config)
    revisions = list(script_directory.walk_revisions())
    revision_ids = {revision.revision for revision in revisions}

    assert revisions
    assert script_directory.get_current_head() == "20260622_0012"
    assert {
        "20260616_0001",
        "20260616_0002",
        "20260616_0003",
        "20260616_0004",
        "20260617_0005",
        "20260617_0006",
        "20260619_0007",
        "20260620_0008",
        "20260620_0009",
        "20260620_0010",
        "20260620_0011",
        "20260622_0012",
    }.issubset(revision_ids)


def test_alembic_revision_module_imports():
    backend_dir = Path(__file__).resolve().parents[1]
    revision_path = (
        backend_dir / "alembic" / "versions" / "20260620_0008_create_rag_sources.py"
    )

    spec = spec_from_file_location("alembic_revision_20260620_0008", revision_path)
    assert spec is not None
    assert spec.loader is not None

    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    assert module.revision == "20260620_0008"


def test_latest_alembic_revision_module_imports():
    backend_dir = Path(__file__).resolve().parents[1]
    revision_path = (
        backend_dir / "alembic" / "versions" / "20260620_0009_create_rag_chunks.py"
    )

    spec = spec_from_file_location("alembic_revision_20260620_0009", revision_path)
    assert spec is not None
    assert spec.loader is not None

    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    assert module.revision == "20260620_0009"


def test_current_alembic_revision_module_imports():
    backend_dir = Path(__file__).resolve().parents[1]
    revision_path = (
        backend_dir / "alembic" / "versions" / "20260622_0012_create_background_jobs.py"
    )

    spec = spec_from_file_location("alembic_revision_20260622_0012", revision_path)
    assert spec is not None
    assert spec.loader is not None

    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    assert module.revision == "20260622_0012"
