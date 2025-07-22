from __future__ import annotations

import base64
from pathlib import Path

from fastapi.testclient import TestClient
from docx import Document

from protocol_to_crf_generator.api.main import app


def _create_docx(path: Path) -> None:
    doc = Document()
    doc.add_paragraph("Screening visit with ECG assessment")
    doc.save(str(path))


def test_health() -> None:
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_ingest(tmp_path: Path) -> None:
    file_path = tmp_path / "sample.docx"
    _create_docx(file_path)
    payload = {
        "filename": file_path.name,
        "content": base64.b64encode(file_path.read_bytes()).decode(),
    }
    client = TestClient(app)
    resp = client.post("/ingest", json=payload)
    assert resp.status_code == 202
    body = resp.json()
    assert "job_id" in body
    assert body["state"] == "queued"
