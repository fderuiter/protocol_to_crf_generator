"""Generate validation reports in JSON and Markdown formats."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Iterable, Tuple

from protocol_to_crf_generator.persistence.storage import _to_canonical_json

# Default directory for validation reports
REPORT_DIR = Path("validation_reports")

# JSON schema for validation log
VALIDATION_LOG_SCHEMA: dict[str, object] = {
    "type": "object",
    "properties": {
        "crf_id": {"type": "string"},
        "generated_at": {"type": "string", "format": "date-time"},
        "issues": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"message": {"type": "string"}},
                "required": ["message"],
            },
        },
    },
    "required": ["crf_id", "generated_at", "issues"],
}


def write_validation_report(
    crf_id: str,
    issues: Iterable[str],
    directory: Path | None = None,
) -> Tuple[Path, Path]:
    """Write validation results to JSON and Markdown files.

    Parameters
    ----------
    crf_id:
        Identifier for the CRF being validated.
    issues:
        Iterable of validation issue messages.
    directory:
        Optional output directory. Defaults to ``validation_reports``.

    Returns
    -------
    Tuple[Path, Path]
        Paths to the JSON and Markdown report files respectively.
    """

    directory = directory or REPORT_DIR
    directory.mkdir(parents=True, exist_ok=True)

    issues_list = [{"message": msg} for msg in issues]
    data = {
        "crf_id": crf_id,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "issues": issues_list,
    }

    json_path = directory / f"{crf_id}_validation.json"
    json_path.write_text(_to_canonical_json(data), encoding="utf-8")

    md_lines = [f"# Validation Report for {crf_id}", ""]
    if issues_list:
        for idx, item in enumerate(issues_list, start=1):
            md_lines.append(f"{idx}. {item['message']}")
    else:
        md_lines.append("No issues found.")
    md_text = "\n".join(md_lines)

    md_path = directory / f"{crf_id}_validation.md"
    md_path.write_text(md_text, encoding="utf-8")

    return json_path, md_path


__all__ = ["write_validation_report", "VALIDATION_LOG_SCHEMA", "REPORT_DIR"]
