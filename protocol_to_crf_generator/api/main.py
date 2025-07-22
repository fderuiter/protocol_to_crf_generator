from __future__ import annotations

import base64
import uuid
from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from protocol_to_crf_generator.ingestion import load_docx
from protocol_to_crf_generator.nlp.extract import extract_entities
from protocol_to_crf_generator.models.protocol import (
    DataCollectionRequirement,
    Provenance,
    StudyProtocolIR,
)
from protocol_to_crf_generator.persistence import save_ir


app = FastAPI(title="Protocol to CRF Generator")


class ProtocolInput(BaseModel):
    """Input document for ingestion."""

    filename: str
    content: str


class JobStatus(BaseModel):
    """Status returned when a job is accepted."""

    job_id: str
    state: str


@app.post("/ingest", status_code=status.HTTP_202_ACCEPTED, response_model=JobStatus)
def ingest(input_data: ProtocolInput) -> JobStatus:
    """Ingest a protocol document synchronously."""

    try:
        binary = base64.b64decode(input_data.content)
    except (base64.binascii.Error, ValueError) as exc:  # pragma: no cover - invalid base64
        raise HTTPException(status_code=400, detail="Invalid content encoding") from exc

    with NamedTemporaryFile(suffix=Path(input_data.filename).suffix) as tmp:
        tmp.write(binary)
        tmp.flush()
        text, _tables = load_docx(Path(tmp.name))

    provenance = Provenance(source_format="docx", source_identifier=input_data.filename)
    entities = extract_entities(text, provenance)

    requirements = [
        DataCollectionRequirement(
            requirement_id=str(i),
            visit_name=e.text if e.label == "VISIT" else "",
            assessment_name=e.text if e.label == "ASSESSMENT" else "",
            provenance=e.provenance,
        )
        for i, e in enumerate(entities)
    ]

    ir = StudyProtocolIR(
        protocol_id=Path(input_data.filename).stem,
        protocol_title=input_data.filename,
        version="1.0",
        requirements=requirements,
    )
    save_ir(ir)

    return JobStatus(job_id=str(uuid.uuid4()), state="accepted")


@app.get("/health")
def health() -> dict[str, str]:
    """Return basic service status."""

    return {"status": "ok"}
