from datetime import datetime
from pathlib import Path
import hashlib
import json

from protocol_to_crf_generator.models import protocol
from protocol_to_crf_generator.persistence import save_ir


def _sample_ir() -> protocol.StudyProtocolIR:
    return protocol.StudyProtocolIR(
        protocol_id="P1",
        protocol_title="Test",
        version="1.0",
        created_at=datetime(2025, 1, 1, 12, 0, 0),
        requirements=[
            protocol.DataCollectionRequirement(
                requirement_id="R1",
                visit_name="Screening",
                assessment_name="ECG",
                provenance=protocol.Provenance(
                    source_format="docx",
                    source_identifier="p.docx",
                ),
            )
        ],
    )


def test_save_ir(tmp_path: Path) -> None:
    ir = _sample_ir()
    path = save_ir(ir, tmp_path)
    assert path.exists()
    data = ir.model_dump() if hasattr(ir, "model_dump") else ir.dict()
    expected_json = json.dumps(
        data,
        default=lambda o: o.isoformat() if isinstance(o, datetime) else o,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
    assert path.read_text(encoding="utf-8") == expected_json
    manifest = (tmp_path / "manifest.csv").read_text(encoding="utf-8").splitlines()
    header, row = manifest
    assert header == "filename,sha256,timestamp"
    filename, digest, timestamp = row.split(",")
    assert filename == path.name
    assert digest == hashlib.sha256(expected_json.encode("utf-8")).hexdigest()
    assert timestamp
