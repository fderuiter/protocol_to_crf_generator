from protocol_to_crf_generator.models import protocol
from pydantic import ValidationError
import pytest  # type: ignore


def _requirement() -> protocol.DataCollectionRequirement:
    return protocol.DataCollectionRequirement(
        requirement_id="R1",
        visit_name="Screening",
        assessment_name="ECG",
        provenance=protocol.Provenance(
            source_format="docx",
            source_identifier="prot.docx",
            location_page=1,
        ),
    )


def test_study_protocol_ir_valid() -> None:
    ir = protocol.StudyProtocolIR(
        protocol_id="P123",
        protocol_title="Example Study",
        version="1.0",
        requirements=[_requirement()],
    )
    assert ir.protocol_id == "P123"
    assert ir.requirements[0].provenance.location_page == 1


def test_validation_error() -> None:
    with pytest.raises(ValidationError):
        protocol.DataCollectionRequirement(
            visit_name="Screening",
            assessment_name="ECG",
            provenance=protocol.Provenance(source_format="docx", source_identifier="prot.docx"),
        )

    with pytest.raises(ValidationError):
        protocol.StudyProtocolIR(
            protocol_id="P123",
            protocol_title="Example Study",
            version="1.0",
            requirements=[{"not": "a requirement"}],
        )
