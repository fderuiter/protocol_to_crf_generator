"""Validation service stub for the prototype."""

from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class ValidationRequest(BaseModel):
    """Request model for validation."""

    crf_id: str


class ValidationResult(BaseModel):
    """Validation result returned by the service."""

    status: str


@router.post("/validate", response_model=ValidationResult)
def validate_crf(payload: ValidationRequest) -> ValidationResult:
    """Return a fixed validation status for the supplied CRF."""

    return ValidationResult(status="valid")


__all__ = ["router", "ValidationRequest", "ValidationResult"]
