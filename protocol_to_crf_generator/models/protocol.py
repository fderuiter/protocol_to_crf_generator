from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class Provenance(BaseModel):
    """Location information for an extracted requirement."""

    source_format: str
    source_identifier: str
    location_page: Optional[int] = None
    location_line: Optional[int] = None
    location_table_id: Optional[str] = None


class DataCollectionRequirement(BaseModel):
    """Structured representation of a single requirement."""

    requirement_id: str
    visit_name: str
    assessment_name: str
    timing_details: Optional[str] = None
    population_subset: Optional[str] = None
    provenance: Provenance


class StudyProtocolIR(BaseModel):
    """Root model holding extracted requirements."""

    protocol_id: str
    protocol_title: str
    version: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    requirements: List[DataCollectionRequirement]


__all__ = [
    "Provenance",
    "DataCollectionRequirement",
    "StudyProtocolIR",
]
