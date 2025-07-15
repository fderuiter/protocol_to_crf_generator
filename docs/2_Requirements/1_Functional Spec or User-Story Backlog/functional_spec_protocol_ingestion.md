# Functional Specification – Protocol Ingestion & Information Extraction

> **Context & Goals**  
> The Protocol Ingestion & Information Extraction (PIIE) feature automates the conversion of heterogeneous study‑protocol documents (DOCX, PDF, XML) into a validated **Study Requirements JSON** that downstream components (mapping, CRF generation, validation) consume.  
> Success is measured by (a) ≥90 % extraction recall for targeted sections (Schedule of Assessments, Eligibility Criteria, etc.), (b) <5 % manual curation rate after first‑pass NLP, and (c) completion within 2 min for a 100‑page protocol.

---

## 📑 Table of Contents

1. [Glossary](#glossary)
2. [User Stories (by Epic)](#user-stories)  
   &nbsp;&nbsp;2.1 [Document Ingestion](#epic-ingest)  
   &nbsp;&nbsp;2.2 [Table & Section Detection](#epic-structure)  
   &nbsp;&nbsp;2.3 [NLP Entity Extraction](#epic-nlp)  
   &nbsp;&nbsp;2.4 [Canonical IR Persistence](#epic-ir)  
   &nbsp;&nbsp;2.5 [Operational Logging & Error Handling](#epic-ops)
3. [Non‑Functional Notes](#nfr)
4. [Open Questions & Dependencies](#open-questions)

---

## Glossary<a name="glossary"></a>

| Term | Definition |
|------|------------|
| **Importer** | Format‑specific module that reads a protocol (DOCX, PDF, XML) and emits raw text + tables. |
| **Section Header** | Human‑readable heading in protocol (e.g., *Schedule of Assessments*). |
| **Canonical IR** | JSON schema (StudyProtocolIR) capturing structured data‑collection requirements with provenance. |
| **Visit** | Planned time‑point in the trial where assessments occur (e.g., *Screening Day –28 to –1*). |
| **Assessment** | Procedure or question to be captured on CRF (e.g., *12‑lead ECG*). |
| **Provenance** | Link (page/line/table) from extracted requirement back to source document for auditability. |
| **Extraction Recall** | % of target requirements correctly identified by NLP pipeline. |

---

## User Stories<a name="user-stories"></a>

### Epic PI‑01 – Document Ingestion<a name="epic-ingest"></a>

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| PI‑01‑01 | As a **Data Manager** I want to upload a *DOCX* protocol so that the system begins extraction automatically. | **Given** a valid DOCX file ≤ 50 MB  
**When** I POST it to */ingest* via API  
**Then** a job is queued and returns 202 with job‑ID. |
| PI‑01‑02 | As a **Study Designer** I want to see an error if the file type is unsupported so that I can fix the input early. | **Given** I upload a *.pptx* file  
**When** validation runs  
**Then** the service responds 400 *“Unsupported format”*. |

### Epic PI‑02 – Table & Section Detection<a name="epic-structure"></a>

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| PI‑02‑01 | As an **NLP Engineer** I want section headers classified so that downstream extractors focus only on relevant portions. | **Given** a parsed protocol  
**When** section detection executes  
**Then** each sentence is tagged with its parent section (*e.g., SOA, Inclusion Criteria*). |
| PI‑02‑02 | As a **Developer** I want tables extracted as CSV so that row/column semantics are preserved. | **Given** a DOCX table with merged headers  
**When** import completes  
**Then** the table is emitted as normalized CSV with header hierarchy flattened. |

### Epic PI‑03 – NLP Entity Extraction<a name="epic-nlp"></a>

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| PI‑03‑01 | As a **Data Scientist** I want visits, assessments, and timing entities recognised so that they map to CDASH later. | **Given** a sentence “Vital signs will be recorded at Screening and Week 4”  
**When** NLP runs  
**Then** entities *(Vital Signs)*‑Assessment, *(Screening, Week 4)*‑Visit are returned with confidence ≥0.8. |
| PI‑03‑02 | As a **Regulatory Lead** I want provenance captured for every extracted entity so that audit requirements are met. | **Given** a table cell in SOA  
**When** the assessment is extracted  
**Then** provenance includes page num, table ID, row/col indices. |

### Epic PI‑04 – Canonical IR Persistence<a name="epic-ir"></a>

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| PI‑04‑01 | As a **Backend Developer** I want validated JSON persisted so that later stages consume consistent schemas. | **Given** extracted entities  
**When** Pydantic validation passes  
**Then** StudyProtocolIR JSON is stored with SHA‑256 hash and status *ready*. |
| PI‑04‑02 | As a **CRO Tech Lead** I want a hash manifest generated so that we can support 21 CFR Part 11 e‑signatures. | **Given** the IR JSON file  
**When** ingestion completes  
**Then** a manifest file lists filename + SHA‑256 hash + timestamp. |

### Epic PI‑05 – Operational Logging & Error Handling<a name="epic-ops"></a>

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| PI‑05‑01 | As a **Site Reliability Engineer** I want structured logs for each ingestion step so that incidents can be triaged quickly. | **Given** ingestion of protocol XYZ  
**When** any sub‑step fails  
**Then** a JSON log entry with level=ERROR, step name, trace ID is written to AuditLog table. |
| PI‑05‑02 | As a **Support Analyst** I want extraction quality metrics emitted so that we can monitor model drift. | **Given** completion of NLP extraction  
**When** metrics computed  
**Then** the job summary includes counts for entities found, confidence distribution, and extraction recall estimate. |

---

## Non‑Functional Notes<a name="nfr"></a>

* **Performance:** Process ≤100‑page DOCX in <2 min (P90).  
* **Scalability:** Async pipeline must allow ≥10 concurrent ingestions (*see NFR‑PERF‑02*).  
* **Compliance:** Audit trail + hash manifest per 21 CFR 11 (*see NFR‑COMP‑01*).  
* **Security:** Only authenticated roles may call */ingest*; files encrypted at rest (NFR‑SEC‑03).  
* **Standards:** Canonical IR schema versioned; backward compatibility guaranteed for MINOR releases.

---

## Open Questions & Dependencies<a name="open-questions"></a>

1. **PDF Table Accuracy** – Do we set minimum recall thresholds or flag PDF imports as *best‑effort* only?
2. **Statistical vs Rule‑based NER** – MVP uses rules; what criteria trigger upgrade to ML model?
3. **Storage Layer** – IR JSON persisted in Postgres JSONB vs object storage? Decision affects query‑ability.
4. **Concurrency Limits** – Alignment with DevOps capacity planning; limits to be defined in Ops playbook.
5. **Internationalization** – Initial protocols assumed English; timeline for multilingual support?

---
*[Return to Top](#functional-spec-protocol-ingestion)
