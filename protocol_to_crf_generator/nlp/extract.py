from __future__ import annotations

"""Rule-based NLP extraction using spaCy."""

from dataclasses import dataclass
from typing import List, Optional

import spacy
from spacy.matcher import Matcher

from protocol_to_crf_generator.models.protocol import Provenance


@dataclass
class ExtractedEntity:
    """Simple representation of an extracted entity."""

    text: str
    label: str
    start: int
    end: int
    confidence: float
    provenance: Provenance


_nlp = spacy.blank("en")
_matcher = Matcher(_nlp.vocab)

# Visit patterns: e.g. "Screening", "Week 4", "Day 1"
_matcher.add(
    "VISIT",
    [
        [{"LOWER": "screening"}],
        [{"LOWER": "baseline"}],
        [{"LOWER": "week"}, {"LIKE_NUM": True}],
        [{"LOWER": "day"}, {"LIKE_NUM": True}],
    ],
)

# Assessment patterns: only a few examples for prototype
_matcher.add(
    "ASSESSMENT",
    [
        [{"LOWER": "vital"}, {"LOWER": "signs"}],
        [{"LOWER": "ecg"}],
    ],
)


def extract_entities(text: str, provenance: Optional[Provenance] = None) -> List[ExtractedEntity]:
    """Extract visits and assessments from text.

    Parameters
    ----------
    text:
        Input sentence or paragraph.
    provenance:
        Provenance information to attach to each entity.

    Returns
    -------
    list[ExtractedEntity]
        Recognised entities with character offsets.
    """
    doc = _nlp(text)
    matches = _matcher(doc)
    results: List[ExtractedEntity] = []
    for match_id, start, end in matches:
        span = doc[start:end]
        results.append(
            ExtractedEntity(
                text=span.text,
                label=_nlp.vocab.strings[match_id],
                start=span.start_char,
                end=span.end_char,
                confidence=0.9,
                provenance=provenance or Provenance(source_format="unknown", source_identifier="unknown"),
            )
        )
    return results


__all__ = ["ExtractedEntity", "extract_entities"]
