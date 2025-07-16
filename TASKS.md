<!--
agent:
  project: "Protocol to CRF Generator"
  code_style: "ruff,mypy"
  default_branch: "main"
  commit_template: "[{id}] {title}"
  milestones:
    M1: "Prototype"
    M2: "Beta"
    M3: "GA"
-->

<!-- task:start -->
id: T1
title: "Define StudyProtocolIR Pydantic models"
status: TODO
priority: P0
owner: ai
depends_on: []
path: protocol_to_crf_generator/models/study_ir.py
tests:
  - tests/models/test_study_ir.py
acceptance:
  - "Pydantic schema matches example in technical plan"
  - "ruff and mypy pass"
  - "pytest coverage >=90%"
context: |
  Section 4.3 of the technical plan describes a Canonical Study Requirements JSON with models StudyProtocolIR and DataCollectionRequirement. Lines 256-289 show example fields and rationale.
instructions: |
  - Create `models/study_ir.py` defining `Provenance`, `DataCollectionRequirement`, and `StudyProtocolIR` using Pydantic.
  - Include JSON canonicalization utility per RFC 8785.
  - Add unit tests in `tests/models/test_study_ir.py` verifying model validation and canonicalization.
  - Run ruff, mypy, and pytest ensuring coverage.
<!-- task:end -->

<!-- task:start -->
id: T2
title: "Set up GitHub Actions CI pipeline"
status: TODO
priority: P0
owner: ai
depends_on: []
path: .github/workflows/main.yml
tests: []
acceptance:
  - "Workflow runs ruff, mypy, pytest, security scans and packaging"
  - "Pipeline passes on branch pushes"
context: |
  Section 2.3 and the CI/CD Pipeline Blueprint specify a GitHub Actions workflow with jobs: lint-and-format, unit-test, security-scan, schema-validate-artefacts, package, deploy.
instructions: |
  - Create `.github/workflows/main.yml` implementing the job sequence from `docs/spec/5_Quality & Ops/3_CICD Pipeline Blueprint/cicd-blueprint.md`.
  - Include steps for ruff, mypy --strict, pytest with coverage, bandit and semgrep scans, and packaging Docker image.
  - Configure workflow to trigger on push and pull_request to `main`.
<!-- task:end -->

<!-- task:start -->
id: T3
title: "Implement terminology database builder and service"
status: TODO
priority: P0
owner: ai
depends_on: []
path: protocol_to_crf_generator/terminology
tests:
  - tests/terminology/test_service.py
acceptance:
  - "SQLite terminology.sqlite produced from CT package"
  - "TerminologyService lookups return expected values"
context: |
  Section 3.2 of the technical plan outlines building a normalized SQLite database from CDISC Controlled Terminology and providing a TerminologyService for lookups.
instructions: |
  - Add `terminology/build_db.py` that parses raw CT TSV/CSV and writes `terminology.sqlite` with codelists and terms tables.
  - Add `terminology/service.py` exposing lookup methods `get_terms_for_codelist` and `is_valid_term`.
  - Write unit tests using sample CT files to verify DB generation and service queries.
<!-- task:end -->

<!-- task:start -->
id: T4
title: "Create DOCX importer"
status: TODO
priority: P0
owner: ai
depends_on:
  - T1
path: protocol_to_crf_generator/ingestion/docx.py
tests:
  - tests/ingestion/test_docx.py
acceptance:
  - "Extractor returns text and tables from DOCX"
  - "Unit tests cover parsing of paragraphs and tables"
context: |
  Technical plan Section 4.1 decision 1 mandates a python-docx based importer for DOCX protocols including table extraction with textacy assistance.
instructions: |
  - Implement `DocxImporter` class providing `parse(path: Path) -> StudyProtocolIR` skeleton.
  - Use python-docx to read paragraphs and tables; emit structured content.
  - Include basic sentence segmentation hooks for later NLP stages.
  - Add tests with small sample DOCX files verifying extracted structure.
<!-- task:end -->

<!-- task:start -->
id: T5
title: "Build NLP segmentation pipeline"
status: TODO
priority: P0
owner: ai
depends_on:
  - T4
path: protocol_to_crf_generator/nlp/pipeline.py
tests:
  - tests/nlp/test_pipeline.py
acceptance:
  - "PyRuSH sentence splitter segments text"
  - "Section headers identified via medspaCy"
context: |
  Section 4.2 describes using medspaCy's PyRuSH and section detection components for sentence segmentation and section classification.
instructions: |
  - Implement an NLP pipeline using spaCy and medspaCy with PyRuSH and sectionizer components.
  - Provide functions to process text from importers and return annotated Doc objects.
  - Unit tests supply sample text asserting correct sentence boundaries and section labels.
<!-- task:end -->

<!-- task:start -->
id: T6
title: "Map DM/VS/CM requirements to CDASH"
status: TODO
priority: P0
owner: ai
depends_on:
  - T3
  - T5
path: protocol_to_crf_generator/mapping/cdash_mapper.py
tests:
  - tests/mapping/test_cdash_mapper.py
acceptance:
  - "Extracted requirements map to CDASH variables with confidence score"
  - "Unmapped items flagged"
context: |
  Section 5.1 explains mapping each DataCollectionRequirement to CDASH variable metadata using fuzzy matching; Section 5.2 requires flagging unmapped items.
instructions: |
  - Implement mapping logic using Levenshtein/Jaro-Winkler distance against metadata loaded via TerminologyService.
  - Return mapping results with confidence values and collect unmapped items.
  - Unit tests cover DM, VS, CM examples and verify unmapped flagging below threshold.
<!-- task:end -->

<!-- task:start -->
id: T7
title: "Generate ODM XML/JSON from mappings"
status: TODO
priority: P0
owner: ai
depends_on:
  - T6
  - T1
path: protocol_to_crf_generator/odm/generator.py
tests:
  - tests/odm/test_generator.py
acceptance:
  - "ODM-XML and ODM-JSON files validate against cached schemas"
context: |
  Section 5.3 states the system outputs CDISC ODM 2.0 structures serialized to XML and JSON using typed models from Section 3.1.
instructions: |
  - Generate typed models from cached schemas using xsdata/datamodel-code-generator.
  - Implement functions to build ItemDef, ItemGroupDef, FormDef, and serialize to XML and JSON.
  - Use lxml and jsonschema in tests to validate generated files.
<!-- task:end -->

<!-- task:start -->
id: T8
title: "Render Markdown CRFs with Jinja templates"
status: TODO
priority: P0
owner: ai
depends_on:
  - T7
path: protocol_to_crf_generator/templates
tests:
  - tests/templates/test_render_crf.py
acceptance:
  - "Markdown files include YAML front-matter per spec"
  - "Matching .odm.json saved alongside .md"
context: |
  Section 6 defines YAML front-matter schema and Jinja2 templates for CRF generation. Section 6.3 requires emitting .md and .odm.json pairs.
instructions: |
  - Create Jinja2 templates (crf.md.j2 plus subtemplates) rendering ODM JSON to Markdown with YAML metadata.
  - Implement renderer saving both .md and source .odm.json in output directory.
  - Unit tests render sample ODM and assert output structure.
<!-- task:end -->

<!-- task:start -->
id: T9
title: "Implement CLI using click"
status: TODO
priority: P0
owner: ai
depends_on:
  - T8
path: protocol_to_crf_generator/cli.py
tests:
  - tests/test_cli.py
acceptance:
  - "`crf-gen` command generates CRF artefacts from DOCX input"
context: |
  Technical plan Section 9.1 selects click for a user-friendly CLI exposing core functionality.
instructions: |
  - Replace the simple argparse entrypoint with a click-based CLI named `crf-gen`.
  - Provide options for input file, output directory, and CT version.
  - Hook into importer, NLP, mapping, generation, and validation steps.
  - Update existing tests to invoke the new command.
<!-- task:end -->

<!-- task:start -->
id: T10
title: "Add Dockerfile and container build"
status: TODO
priority: P1
owner: ai
depends_on:
  - T9
  - T2
path: Dockerfile
tests: []
acceptance:
  - "Docker image builds via CI pipeline"
context: |
  Section 9.2 mandates containerisation with Docker and publishing images in CI.
instructions: |
  - Create a multi-stage Dockerfile based on python:3.11-slim installing dependencies and running the FastAPI server by default.
  - Ensure CLI can be executed via `docker run` by overriding entrypoint.
  - Update CI packaging job to build and publish the image.
<!-- task:end -->

<!-- task:start -->
id: T11
title: "Validate generated ODM and CT business rules"
status: TODO
priority: P1
owner: ai
depends_on:
  - T7
  - T3
path: protocol_to_crf_generator/validation/validator.py
tests:
  - tests/validation/test_validator.py
acceptance:
  - "Invalid ODM fails with clear errors"
  - "CT checks verify permissible values"
context: |
  Section 7 describes structural validation against ODM schemas and controlled terminology checks, with future integration to CDISC CORE.
instructions: |
  - Implement validation functions using lxml for XML and jsonschema for JSON.
  - Cross-check codelist values against TerminologyService and flag violations.
  - Produce validation-log.json and HTML report.
  - Unit tests cover valid and invalid examples.
<!-- task:end -->

<!-- task:start -->
id: T12
title: "Expose FastAPI REST API"
status: TODO
priority: P1
owner: ai
depends_on:
  - T9
  - T11
path: protocol_to_crf_generator/api/main.py
tests:
  - tests/api/test_api.py
acceptance:
  - "POST /ingest queues job and returns job_id"
  - "OpenAPI docs auto-generated"
context: |
  Sections 9.1 and API contract docs outline a FastAPI gateway exposing endpoints for ingestion and retrieval.
instructions: |
  - Build FastAPI app with endpoint `/ingest` accepting file uploads and options.
  - Use background tasks to run the full pipeline and store results.
  - Enable automatic OpenAPI docs at `/docs`.
  - Write tests with TestClient verifying endpoint behaviour.
<!-- task:end -->

<!-- task:start -->
id: T13
title: "Automate quarterly CT updates"
status: TODO
priority: P1
owner: ai
depends_on:
  - T3
  - T2
path: .github/workflows/update_ct.yml
tests: []
acceptance:
  - "Workflow opens PR when new CT version detected"
context: |
  Technical plan Section 3.4 specifies a scheduled GitHub Actions workflow that fetches new CT packages and creates a pull request with updated terminology.sqlite.
instructions: |
  - Create workflow triggered weekly on cron.
  - Implement steps to check NCI-EVS FTP for latest version, run build_db.py, commit database, and open PR using gh cli.
  - Ensure PR runs full CI pipeline.
<!-- task:end -->

<!-- task:start -->
id: T14
title: "Extend mapping to AE/MH/DS/EX domains"
status: TODO
priority: P2
owner: ai
depends_on:
  - T6
path: protocol_to_crf_generator/mapping/cdash_mapper.py
tests:
  - tests/mapping/test_additional_domains.py
acceptance:
  - "New domains map correctly using existing framework"
context: |
  The roadmap lists additional domain support (AE, MH, DS, EX) in Q2 after the initial DM/VS/CM mapping.
instructions: |
  - Expand metadata tables to include variables for AE, MH, DS, and EX.
  - Update mapping logic and tests to cover these domains.
<!-- task:end -->

<!-- task:start -->
id: T15
title: "Add PDF and XML importers"
status: TODO
priority: P2
owner: ai
depends_on:
  - T4
path: protocol_to_crf_generator/ingestion
tests:
  - tests/ingestion/test_pdf.py
  - tests/ingestion/test_xml.py
acceptance:
  - "PDF and XML files parsed into StudyProtocolIR"
context: |
  Section 4.1 describes PDF and structured XML importers using pdfminer-six and lxml with XPath extraction.
instructions: |
  - Implement `PdfImporter` leveraging pdfminer-six and optional camelot/tabula for tables.
  - Implement `XmlImporter` using lxml to extract required elements via XPath.
  - Add unit tests with minimal sample documents verifying output.
<!-- task:end -->

<!-- task:start -->
id: T16
title: "Train statistical NER model and integrate CDISC CORE"
status: TODO
priority: P3
owner: ai
depends_on:
  - T5
  - T11
path: protocol_to_crf_generator/nlp/model
tests:
  - tests/nlp/test_ner_model.py
  - tests/validation/test_core_integration.py
acceptance:
  - "NER model achieves recall ≥0.8 on test corpus"
  - "Validation uses CDISC CORE rules when available"
context: |
  The roadmap for Q3 includes statistical NER model training and CDISC CORE integration for advanced validation as per Section 7.2.
instructions: |
  - Prepare training data from labelled protocol snippets and train a spaCy model.
  - Load the model in the NLP pipeline when available.
  - Integrate cdisc-rules-engine to run official rules during validation, gating on model output.
  - Add tests evaluating model performance on sample texts and verifying CORE rule invocation.
<!-- task:end -->

<!-- task:start -->
id: T17
title: "Develop optional React SPA"
status: TODO
priority: P3
owner: ai
depends_on:
  - T12
path: ui
tests: []
acceptance:
  - "Users can upload protocol and download ZIP of artefacts"
context: |
  Section 9.3 and multiple references describe an optional Single-Page Application built with React that interacts with the REST API.
instructions: |
  - Scaffold a React app (e.g., using Vite) under `ui/` providing a file upload form.
  - Call the FastAPI backend to trigger generation and offer a download link.
  - Document build and deployment steps in README.
<!-- task:end -->

