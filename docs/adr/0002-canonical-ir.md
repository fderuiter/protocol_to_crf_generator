# ADR 0002: Canonical StudyProtocolIR Design

## Status
Accepted

## Date
2025-07-17

## Context
The ingestion pipeline extracts structured study requirements from diverse input formats such as DOCX or PDF. These requirements need a stable, validated representation that downstream mapping and generation components can rely on. The technical plan mandates a canonical *StudyProtocolIR* composed of Pydantic models providing strict validation and provenance tracking.

## Decision Drivers
1. Decouple ingestion from mapping to allow independent evolution.
2. Provide strong validation and typing using Pydantic.
3. Preserve provenance for auditability and user trust.
4. Enable deterministic JSON output that can be hashed and versioned.

## Considered Options
| ID | Option | Notes |
|----|--------|-------|
|A|Flat dictionaries|Simpler but error‑prone and lacking structure|
|B|Custom classes without validation|Lightweight but no data checks|
|C|**Pydantic‑based models with provenance**|Rich validation and JSON serialisation|

## Decision Outcome
**Chosen option C – Pydantic models with provenance.**

### Rationale
* Models mirror the domain terms in the specification, improving readability.
* Validation prevents malformed data entering the mapping pipeline.
* Provenance fields (page, line, table) satisfy regulatory traceability needs.
* Pydantic's JSON export combined with RFC 8785 canonicalisation ensures reproducible hashes for the persistence layer.

## Consequences
* The `StudyProtocolIR` root object aggregates `DataCollectionRequirement` items.
* Each requirement carries a `Provenance` record specifying its origin in the protocol.
* Downstream modules depend only on this IR, simplifying tests and future refactoring.

## Links
* Technical Plan section 4.3 describing the canonical IR.
* ADR 0001 establishing the overall modular architecture.
