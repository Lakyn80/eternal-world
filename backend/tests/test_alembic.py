from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from alembic.config import Config
from alembic.script import ScriptDirectory


def test_alembic_configuration_loads_revision_history():
    """Task 65.7C (Part G): this test previously hardcoded a specific
    revision id (`20260722_0025`) as "the head". That assertion went stale
    the moment the very next migration (`20260723_0026`, Task 65.7) landed,
    and would go stale again with every future migration - a brittle,
    self-defeating check that a real reviewer would have to keep editing
    forever. It is replaced with three properties that stay true regardless
    of how many migrations are added later:

    1. Exactly one head exists (catches accidental branching - two
       migrations authored against the same `down_revision` - which a
       hardcoded-head assertion would NOT reliably catch either).
    2. The specific set of revisions this test has always enumerated, plus
       Task 65.7 (`20260723_0026`), Task 65.9 (`20260724_0027`), and
       Task 65.12 (`20260729_0028`), are present and reachable.
    3. The exact linear edges introduced by recent migration work are
       correct: `20260722_0025 -> 20260723_0026 -> 20260724_0027 -> 20260729_0028`.
    """

    backend_dir = Path(__file__).resolve().parents[1]
    config = Config(str(backend_dir / "alembic.ini"))
    config.set_main_option("script_location", str(backend_dir / "alembic"))

    script_directory = ScriptDirectory.from_config(config)
    revisions = list(script_directory.walk_revisions())
    revision_ids = {revision.revision for revision in revisions}
    revisions_by_id = {revision.revision: revision for revision in revisions}

    assert revisions

    heads = script_directory.get_heads()
    assert len(heads) == 1, f"expected exactly one Alembic head, found {heads}"
    assert script_directory.get_current_head() == heads[0]

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
        "20260624_0013",
        "20260704_0014",
        "20260711_0015",
        "20260711_0016",
        "20260711_0017",
        "20260711_0018",
        "20260713_0019",
        "20260715_0020",
        "20260716_0021",
        "20260719_0022",
        "20260721_0023",
        "20260721_0024",
        "20260722_0025",
        "20260723_0026",
        "20260724_0027",
        "20260729_0028",
        "20260731_0030",
        "20260731_0031",
    }.issubset(revision_ids)

    # Task 65.7 (chat active sessions), Task 65.9 (async job platform), and
    # Task 65.12 (avatar persona settings) must chain linearly onto each
    # other and onto the pre-existing head, never as a silent second branch.
    assert revisions_by_id["20260723_0026"].down_revision == "20260722_0025"
    assert revisions_by_id["20260724_0027"].down_revision == "20260723_0026"
    assert revisions_by_id["20260729_0028"].down_revision == "20260724_0027"
    assert revisions_by_id["20260731_0030"].down_revision == "20260729_0028"
    assert revisions_by_id["20260731_0031"].down_revision == "20260731_0030"
    assert heads[0] == "20260731_0031"


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
        backend_dir
        / "alembic"
        / "versions"
        / "20260731_0031_generalize_content_translation.py"
    )

    spec = spec_from_file_location("alembic_revision_20260731_0031", revision_path)
    assert spec is not None
    assert spec.loader is not None

    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    assert module.revision == "20260731_0031"
    assert module.down_revision == "20260731_0030"
