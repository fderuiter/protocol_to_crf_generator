import json
import logging
import sqlite3
from pathlib import Path


DB_PATH = Path("audit_log.sqlite")


class SQLiteAuditHandler(logging.Handler):
    """Logging handler writing JSON records to SQLite."""

    def __init__(self, db_path: Path = DB_PATH) -> None:
        super().__init__()
        self.db_path = db_path
        self._ensure_table()

    def _ensure_table(self) -> None:
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS AuditLog (entry TEXT)")
        conn.commit()
        conn.close()

    def emit(self, record: logging.LogRecord) -> None:
        entry = json.dumps(
            {
                "level": record.levelname,
                "message": record.getMessage(),
                "trace_id": getattr(record, "trace_id", ""),
            }
        )
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("INSERT INTO AuditLog (entry) VALUES (?)", (entry,))
        conn.commit()
        conn.close()


def setup_audit_logger(db_path: Path | str | None = None) -> logging.Logger:
    """Configure and return the audit logger."""
    path = Path(db_path) if db_path is not None else DB_PATH
    logger = logging.getLogger("protocol_to_crf_generator.audit")
    logger.setLevel(logging.INFO)

    # remove existing handlers of this type
    for handler in list(logger.handlers):
        if isinstance(handler, SQLiteAuditHandler):
            logger.removeHandler(handler)

    logger.addHandler(SQLiteAuditHandler(path))
    return logger


__all__ = ["setup_audit_logger", "SQLiteAuditHandler"]
