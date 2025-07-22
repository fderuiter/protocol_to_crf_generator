from __future__ import annotations

import base64
import tempfile
import uuid
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from protocol_to_crf_generator.ingestion.docx_importer import load_docx
from protocol_to_crf_generator.nlp.extract import extract_entities
from protocol_to_crf_generator.persistence.storage import save_ir
from protocol_to_crf_generator.models.protocol import (
    DataCollectionRequirement,
    Provenance,
    StudyProtocolIR,
)


class ProtocolInput(BaseModel):
    """Input payload for protocol ingestion."""

    filename: str
    content: str


class JobStatus(BaseModel):
    """Status information returned after job submission."""

    job_id: str
    state: str


app = FastAPI(title="Protocol to CRF Generator")


@app.post("/ingest", status_code=202, response_model=JobStatus)
def ingest(data: ProtocolInput) -> JobStatus:
    """Ingest a protocol document."""
    try:
        binary = base64.b64decode(data.content)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=400, detail="invalid content") from exc

    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / data.filename
        path.write_bytes(binary)
        text, _ = load_docx(path)

    prov = Provenance(source_format="docx", source_identifier=data.filename)
    entities = extract_entities(text, prov)
    requirements = [
        DataCollectionRequirement(
            requirement_id=str(i),
            visit_name=e.text if e.label == "VISIT" else "",
            assessment_name=e.text if e.label == "ASSESSMENT" else "",
            provenance=prov,
        )
        for i, e in enumerate(entities, start=1)
        if e.label in {"VISIT", "ASSESSMENT"}
    ]

    ir = StudyProtocolIR(
        protocol_id=str(uuid.uuid4()),
        protocol_title=data.filename,
        version="1.0",
        requirements=requirements or [],
    )
    save_ir(ir)

    return JobStatus(job_id=str(uuid.uuid4()), state="queued")


@app.get("/health")
def health() -> dict[str, str]:
    """Return service health status."""
    return {"status": "ok"}


__all__ = ["app"]
