from __future__ import annotations

from pathlib import Path
import json

from jsonschema import validate

from protocol_to_crf_generator.validation import (
    VALIDATION_LOG_SCHEMA,
    write_validation_report,
)


def test_validation_report_files_and_schema(tmp_path: Path) -> None:
    json_path, md_path = write_validation_report(
        "CRF1", ["Missing field A", "Bad format"], tmp_path
    )

    assert json_path.exists()
    assert md_path.exists()

    data = json.loads(json_path.read_text(encoding="utf-8"))
    validate(instance=data, schema=VALIDATION_LOG_SCHEMA)

    md_text = md_path.read_text(encoding="utf-8")
    assert "Validation Report for CRF1" in md_text
    assert "1. Missing field A" in md_text
    assert "2. Bad format" in md_text
