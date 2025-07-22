import json
import sqlite3
from pathlib import Path

import pytest  # type: ignore
from fastapi.testclient import TestClient

from protocol_to_crf_generator.api import main
from protocol_to_crf_generator.audit import setup_audit_logger


def test_error_written_to_audit_log(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    db_path = tmp_path / "audit.sqlite"
    logger = setup_audit_logger(db_path)
    main.audit_logger = logger

    client = TestClient(main.app)
    response = client.post("/ingest", json={"filename": "bad.docx", "content": "!!!"})
    assert response.status_code == 400

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT entry FROM AuditLog")
    rows = [json.loads(row[0]) for row in cur.fetchall()]
    conn.close()

    error_rows = [r for r in rows if r["level"] == "ERROR"]
    assert error_rows
    assert error_rows[0]["trace_id"]
