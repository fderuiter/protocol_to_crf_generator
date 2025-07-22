"""Mapping service stub for the prototype."""

from __future__ import annotations

import uuid

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class MappingRequest(BaseModel):
    """Request model for mapping an IR to CRF."""

    ir_id: str


class MappingResult(BaseModel):
    """Result returned after mapping."""

    crf_id: str


@router.post("/map", response_model=MappingResult)
def map_ir(payload: MappingRequest) -> MappingResult:
    """Return a placeholder CRF identifier for the supplied IR."""

    return MappingResult(crf_id=f"crf-{uuid.uuid4()}")


__all__ = ["router", "MappingRequest", "MappingResult"]
