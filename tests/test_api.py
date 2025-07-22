from __future__ import annotations

import base64
from pathlib import Path

from fastapi.testclient import TestClient
from docx import Document
import pytest  # type: ignore

from protocol_to_crf_generator.api.main import app
from protocol_to_crf_generator.persistence import storage


def _create_docx(path: Path) -> None:
    doc = Document()
    doc.add_paragraph("Protocol Title")
    doc.save(str(path))


def test_health_endpoint() -> None:
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ingest_endpoint(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    file_path = tmp_path / "sample.docx"
    _create_docx(file_path)
    content = base64.b64encode(file_path.read_bytes()).decode()

    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)

    client = TestClient(app)
    response = client.post(
        "/ingest",
        json={"filename": "sample.docx", "content": content},
    )

    assert response.status_code == 202
    data = response.json()
    assert data["state"] == "accepted"
    assert data["job_id"]
    # ensure IR was written
    assert any(p.suffix == ".json" for p in tmp_path.iterdir())
