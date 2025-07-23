from __future__ import annotations

import sqlite3
from pathlib import Path
from importlib import reload

from fastapi.testclient import TestClient
import pytest

import protocol_to_crf_generator.api.main as main
from protocol_to_crf_generator.api import health as health_module
from protocol_to_crf_generator.persistence import storage
from protocol_to_crf_generator.audit import logging as audit_logging


def test_healthz_endpoint() -> None:
    client = TestClient(main.app)
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ready_endpoint_ok(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(audit_logging, "DB_PATH", tmp_path / "audit.sqlite")
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path / "data")
    storage.DATA_DIR.mkdir()
    reload(health_module)
    main.app.include_router(health_module.router)

    client = TestClient(main.app)
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_ready_endpoint_failure(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path / "data-missing")

    def failing_connect(*_: object, **__: object) -> sqlite3.Connection:
        raise sqlite3.OperationalError("fail")

    monkeypatch.setattr(sqlite3, "connect", failing_connect)
    reload(health_module)
    main.app.include_router(health_module.router)

    client = TestClient(main.app)
    response = client.get("/ready")
    assert response.status_code == 503
