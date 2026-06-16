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

    assert revisions
    assert revisions[0].revision == "20260616_0001"


def test_alembic_revision_module_imports():
    backend_dir = Path(__file__).resolve().parents[1]
    revision_path = (
        backend_dir / "alembic" / "versions" / "20260616_0001_create_core_tables.py"
    )

    spec = spec_from_file_location("alembic_revision_20260616_0001", revision_path)
    assert spec is not None
    assert spec.loader is not None

    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    assert module.revision == "20260616_0001"
