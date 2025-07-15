# Feature List

## 1. Deliverable & Access Interfaces

* **Git-based source repository** (code, CI/CD, docs)&#x20;
* **Containerised REST API** for programmatic integration&#x20;
* **Command-Line Interface (CLI)** for power users & batch jobs&#x20;
* **Single-Page Web UI (optional)** for drag-and-drop protocol upload&#x20;

## 2. Day-1 CDISC Standards Support

* CDASHIG v2.1 variable mapping
* CDISC Controlled Terminology (CT) – 28 Mar 2025 release, with quarterly update pipeline
* ODM 2.0 generation (XML & JSON serialisations)&#x20;

## 3. Protocol Input Importers

* **DOCX importer** (python-docx + table extraction)
* **Structured XML importer** (lxml + XPath)
* **PDF importer** (pdfminer-six ± Camelot/Tabula heuristics)
* Future-proof hook for **FHIR ResearchStudy importer**&#x20;

## 4. Non-Functional Foundations

* 21 CFR Part 11–ready audit-trail & traceability
* RBAC, TLS 1.2+, encryption-at-rest security controls
* Dual-licensing model (open-source core / enterprise tier)
* Mandatory Docker containerisation for portability&#x20;

## 5. Core Technology Stack

* Python 3.11
* FastAPI (async REST), Pydantic (data models/validation)
* spaCy + medspaCy for clinical NLP
* lxml for XML/XSD, xsdata & datamodel-code-generator for typed models
* Jinja2 templating; MkDocs + Material theme for docs site&#x20;

## 6. Continuous Integration / Continuous Deployment

* GitHub Actions workflow with jobs: **lint / type-check → unit-test → security-scan → schema-validate → package → (tagged) deploy**
* Coverage (pytest-cov), ruff, Bandit + Semgrep SAST&#x20;

## 7. Reference-Data Management

* **ODM schema cache & typed-model generation**
* **TerminologyService** powered by a normalised SQLite CT database
* Curated **eCRF example corpus** for regression tests
* **Automated CT-update GitHub Action** (weekly cron → PR)&#x20;

## 8. Protocol Ingestion & Information Extraction

* Importer framework with common interface
* medspaCy **PyRuSH sentence splitter** & **section-header classifier**
* Table-structure interpreter for Schedules of Assessment
* Custom **NER pipeline** (Visit, Assessment, Biomarker, Timing, Population)
* **Canonical Study Requirements JSON IR** with provenance & RFC 8785 canonicalisation&#x20;

## 9. Semantic Mapping Engine

* Exact + fuzzy (Levenshtein/Jaro-Winkler) mapping to CDASH variables
* Automatic linkage to CT CodeLists & planned SDTM domain
* Confidence-scoring & **human-in-the-loop QA report** for unmapped items&#x20;

## 10. CRF Artefact Generation

* **ODM-XML / ODM-JSON builders** (ItemDef → ItemGroupDef → FormDef hierarchy)
* **Markdown CRF generator** with YAML front-matter & Jinja2 templates
* Dual output: `.md` + matching `.odm.json` for Git-friendly diffs&#x20;

## 11. Validation Layer

* Structural XSD/JSON-Schema validation for every artefact
* CDASH & CT business-rule checks; roadmap to CDISC CORE integration
* Consolidated **validation-log.json + HTML report**&#x20;

## 12. Testing & Quality Control

* Granular **unit tests** (parsers, NLP, mapping, templates)
* **Regression test corpus** with golden ODM outputs
* CI-enforced coverage, lint, and SAST thresholds&#x20;

## 13. Packaging & Deployment Options

* Stand-alone **CLI package** (pip / PyPI)
* **Docker images** pushed on tagged release
* **FastAPI service** container entrypoint
* Optional **React SPA** static bundle served via FastAPI or CDN&#x20;

## 14. Documentation & Onboarding

* Auto-generated **OpenAPI 3 / Swagger & ReDoc** endpoints
* Illustrated “Protocol → CDISC mapping” technical guide
* Public **semantic-versioning policy** (SemVer 2.0)&#x20;

## 15. Governance, Compliance & Community

* **Standards Version-Adoption Steering Document**
* **Requirements Traceability Matrix** & audit-trail spec
* Disaster-Recovery & backup plan
* CONTRIBUTING, Contributor Covenant CoC, CLA automation for open-source ecosystem&#x20;
