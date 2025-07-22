from __future__ import annotations

import sqlite3
from pathlib import Path

from protocol_to_crf_generator.audit.logging import configure_logging


def test_audit_log_entry(tmp_path: Path) -> None:
    db_file = tmp_path / "audit.sqlite"
    logger = configure_logging(db_file)
    logger.error("failure", extra={"trace_id": "t123"})

    conn = sqlite3.connect(db_file)
    row = conn.execute("SELECT level, trace_id, message FROM AuditLog").fetchone()
    conn.close()

    assert row == ("ERROR", "t123", "failure")
