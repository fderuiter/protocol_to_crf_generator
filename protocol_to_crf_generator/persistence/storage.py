"""Persistence layer for StudyProtocolIR objects."""

from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any

from protocol_to_crf_generator.models.protocol import StudyProtocolIR


DATA_DIR = Path("data")


def _to_canonical_json(data: Any) -> str:
    """Return canonical JSON per RFC 8785."""

    def default(obj: Any) -> Any:
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Type {type(obj)} not serializable")

    return json.dumps(
        data,
        default=default,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )


def save_ir(ir: StudyProtocolIR, directory: Path | None = None) -> Path:
    """Save the IR to disk and update the manifest.

    Parameters
    ----------
    ir:
        Instance to persist.
    directory:
        Optional base directory. Defaults to ``data``.

    Returns
    -------
    Path
        Path to the saved JSON file.
    """

    directory = directory or DATA_DIR
    directory.mkdir(parents=True, exist_ok=True)

    data = ir.model_dump() if hasattr(ir, "model_dump") else ir.dict()
    json_text = _to_canonical_json(data)

    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    filename = f"{ir.protocol_id}_{timestamp}.json"
    file_path = directory / filename
    file_path.write_text(json_text, encoding="utf-8")

    digest = hashlib.sha256(json_text.encode("utf-8")).hexdigest()

    manifest_path = directory / "manifest.csv"
    write_header = not manifest_path.exists()
    with manifest_path.open("a", newline="") as fh:
        writer = csv.writer(fh)
        if write_header:
            writer.writerow(["filename", "sha256", "timestamp"])
        writer.writerow([filename, digest, timestamp])

    return file_path


__all__ = ["save_ir"]
