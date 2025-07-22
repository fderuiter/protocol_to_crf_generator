from __future__ import annotations

import logging
import sqlite3
from datetime import datetime
from pathlib import Path


AUDIT_DB = Path("audit_log.sqlite")


class SQLiteHandler(logging.Handler):
    """Logging handler that writes structured entries to SQLite."""

    def __init__(self, db_path: Path | str = AUDIT_DB) -> None:
        super().__init__()
        self.db_path = Path(db_path)
        self._ensure_table()

    def _ensure_table(self) -> None:
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "CREATE TABLE IF NOT EXISTS AuditLog (timestamp TEXT, level TEXT, trace_id TEXT, message TEXT)"
        )
        conn.commit()
        conn.close()

    def emit(self, record: logging.LogRecord) -> None:
        entry_time = datetime.utcfromtimestamp(record.created).isoformat()
        trace_id = getattr(record, "trace_id", "")
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO AuditLog (timestamp, level, trace_id, message) VALUES (?, ?, ?, ?)",
            (entry_time, record.levelname, trace_id, record.getMessage()),
        )
        conn.commit()
        conn.close()


def configure_logging(db_path: Path | str = AUDIT_DB) -> logging.Logger:
    """Return a logger configured to write JSON records to SQLite."""
    logger = logging.getLogger("audit")
    logger.setLevel(logging.INFO)
    if not any(isinstance(h, SQLiteHandler) for h in logger.handlers):
        logger.addHandler(SQLiteHandler(db_path))
    return logger


__all__ = ["configure_logging", "SQLiteHandler", "AUDIT_DB"]
