"""Mapping service stub for the prototype."""

from __future__ import annotations

import uuid

from fastapi import APIRouter
from pydantic import BaseModel

from protocol_to_crf_generator.ct_cache import CTCache


router = APIRouter()


TERMINOLOGY_DB = {"IR1": "Case Report Form"}


def _fetch_term(code: str) -> str:
    """Simulate a terminology lookup."""

    return TERMINOLOGY_DB.get(code, "")


_cache = CTCache(_fetch_term, maxsize=256)


class MappingRequest(BaseModel):
    """Request model for mapping an IR to CRF."""

    ir_id: str


class MappingResult(BaseModel):
    """Result returned after mapping."""

    crf_id: str


@router.post("/map", response_model=MappingResult)
def map_ir(payload: MappingRequest) -> MappingResult:
    """Return a placeholder CRF identifier for the supplied IR."""

    _cache.lookup(payload.ir_id)
    return MappingResult(crf_id=f"crf-{uuid.uuid4()}")


__all__ = ["router", "MappingRequest", "MappingResult"]
