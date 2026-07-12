from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DASHBOARD_PATH = (
    REPO_ROOT / "monitoring" / "grafana" / "dashboards" / "fa_chat_observability.json"
)
DATASOURCE_PATH = (
    REPO_ROOT
    / "monitoring"
    / "grafana"
    / "provisioning"
    / "datasources"
    / "prometheus.yml"
)
EXPECTED_PROMETHEUS_DATASOURCE = {
    "type": "prometheus",
    "uid": "eternal-world-prometheus",
}


def _load_dashboard() -> dict:
    return json.loads(DASHBOARD_PATH.read_text(encoding="utf-8"))


def _walk_panels(panels: list[dict]):
    for panel in panels:
        yield panel
        nested = panel.get("panels")
        if isinstance(nested, list):
            yield from _walk_panels(nested)


def test_dashboard_identity_and_json_contract_are_stable() -> None:
    dashboard = _load_dashboard()

    assert dashboard["id"] is None
    assert dashboard["uid"] == "eternal-world-fa-chat"
    assert dashboard["title"] == "Eternal World — FA Chat Observability"
    assert isinstance(dashboard.get("panels"), list)
    assert dashboard["panels"]


def test_every_prometheus_panel_uses_the_eternal_world_datasource_uid() -> None:
    dashboard = _load_dashboard()
    panel_ids: list[int] = []

    for panel in _walk_panels(dashboard["panels"]):
        panel_id = panel.get("id")
        if panel_id is not None:
            panel_ids.append(panel_id)

        if panel.get("type") != "row":
            assert panel.get("datasource") == EXPECTED_PROMETHEUS_DATASOURCE

        target_ref_ids: list[str] = []
        for target in panel.get("targets", []):
            datasource = target.get("datasource")
            if datasource is not None:
                assert datasource == EXPECTED_PROMETHEUS_DATASOURCE
            if target.get("refId") is not None:
                target_ref_ids.append(target["refId"])
        assert len(target_ref_ids) == len(set(target_ref_ids))

    assert len(panel_ids) == len(set(panel_ids))


def test_only_builtin_grafana_annotations_are_exempt_from_prometheus_uid() -> None:
    dashboard = _load_dashboard()
    annotations = dashboard.get("annotations", {}).get("list", [])

    for annotation in annotations:
        datasource = annotation.get("datasource")
        assert datasource in (
            EXPECTED_PROMETHEUS_DATASOURCE,
            {"type": "grafana", "uid": "-- Grafana --"},
        )

    serialized = DASHBOARD_PATH.read_text(encoding="utf-8")
    assert '"datasource": "Prometheus"' not in serialized
    assert '"uid": "prometheus"' not in serialized


def test_standalone_grafana_provisions_the_same_stable_datasource_uid() -> None:
    datasource = DATASOURCE_PATH.read_text(encoding="utf-8")
    assert "name: Eternal World Prometheus" in datasource
    assert "uid: eternal-world-prometheus" in datasource
    assert "url: http://prometheus:9090" in datasource
    assert "isDefault: true" in datasource

    compose = (REPO_ROOT / "docker-compose.yml").read_text(encoding="utf-8")
    assert "profiles:" in compose
    assert "- standalone-grafana" in compose
    assert '"3001:3000"' in compose
