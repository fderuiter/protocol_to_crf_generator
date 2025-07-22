from protocol_to_crf_generator.nlp.extract import extract_entities
from protocol_to_crf_generator.models.protocol import Provenance


def test_extract_entities_sample() -> None:
    text = "Vital signs will be recorded at Screening and Week 4."
    prov = Provenance(
        source_format="docx",
        source_identifier="prot.docx",
        location_page=1,
        location_table_id="T1",
    )
    entities = extract_entities(text, prov)
    labels = {e.label for e in entities}
    assert "ASSESSMENT" in labels
    assert "VISIT" in labels
    assert any(e.text == "Vital signs" for e in entities)
    assert any(e.text == "Screening" for e in entities)
    assert any(e.text == "Week 4" for e in entities)
    for ent in entities:
        assert ent.confidence >= 0.8
        assert ent.provenance.location_page == 1
        assert ent.provenance.location_table_id == "T1"
