from __future__ import annotations

import sqlite3

from fastapi import APIRouter, HTTPException, status

from protocol_to_crf_generator.audit import logging as audit_logging
from protocol_to_crf_generator.persistence import storage

router = APIRouter()


@router.get("/healthz")
def healthz() -> dict[str, str]:
    """Return basic liveness status."""

    return {"status": "ok"}


@router.get("/ready")
def ready() -> dict[str, str]:
    """Check service readiness by verifying dependencies."""

    try:
        conn = sqlite3.connect(audit_logging.DB_PATH)
        conn.execute("SELECT 1")
        conn.close()
    except sqlite3.Error as exc:  # pragma: no cover - exceptional path
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database unreachable",
        ) from exc

    if not storage.DATA_DIR.exists():
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Data directory missing",
        )

    return {"status": "ready"}


__all__ = ["router"]
