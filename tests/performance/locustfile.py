from __future__ import annotations

import base64
from io import BytesIO

from docx import Document
from locust import HttpUser, task, between


def _sample_payload() -> dict[str, str]:
    doc = Document()
    doc.add_paragraph("Protocol Title")
    buffer = BytesIO()
    doc.save(buffer)
    encoded = base64.b64encode(buffer.getvalue()).decode()
    return {"filename": "sample.docx", "content": encoded}


class IngestUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self) -> None:
        self.payload = _sample_payload()

    @task
    def ingest(self) -> None:
        self.client.post("/ingest", json=self.payload, name="/ingest")
