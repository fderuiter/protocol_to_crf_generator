<!--
agent:
  project: "Protocol to CRF Generator"
  code_style: "black,pylint"
  default_branch: "main"
  commit_template: "[{id}] {title}"
milestones:
  - {tag: M0, name: "Setup & Scaffolding", target: "2025-07-31"}
  - {tag: M1, name: "Prototype",           target: "2025-12-31"}
  - {tag: M2, name: "Public Beta",         target: "2026-06-30"}
  - {tag: M3, name: "GA",                  target: "2026-12-31"}
-->

<!-- task:start -->
id: 2025-07-16-001
phase: M0
title: "Create GitHub repository and main branch"
status: TODO
priority: P0
owner: Frederick de Ruiter
depends_on: []
path: "."
tests: []
acceptance:
  - "Repository exists on GitHub"
  - "Default branch named 'main'"
context: |
  The communication plan specifies all work targets the `main` branch.
instructions: |
  - Initialize a new GitHub repository named `protocol-to-crf-generator`.
  - Create the default branch `main` and push an initial commit.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-16-002
phase: M0
title: "Seed project documentation and policies"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-16-001
path:
  - README.md
  - LICENSE
  - CODE_OF_CONDUCT.md
  - CONTRIBUTING.md
  - GOVERNANCE.md
tests: []
acceptance:
  - "Files render correctly on GitHub"
context: |
  The project charter and governance sections require a clear README, contribution guidelines, code of conduct and Apache 2.0 license.
instructions: |
  - Add a concise `README.md` describing the project purpose and setup steps.
  - Include `LICENSE` with Apache 2.0 text.
  - Provide `CODE_OF_CONDUCT.md` and `CONTRIBUTING.md` summarising collaboration rules.
  - Create `GOVERNANCE.md` outlining how decisions and releases are managed.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-16-003
phase: M0
title: "Add Python package scaffolding"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-16-002
path:
  - pyproject.toml
  - protocol_to_crf_generator/__init__.py
  - protocol_to_crf_generator/__main__.py
tests:
  - tests/test_cli.py
acceptance:
  - "`python -m protocol_to_crf_generator --version` prints version"
context: |
  The technical plan specifies a CLI tool and a modular Python package.
instructions: |
  - Create `pyproject.toml` configuring `ruff` and `mypy` as described in the coding style guide.
  - Implement a minimal package with `__version__` and CLI entry point that accepts `--version`.
  - Write `tests/test_cli.py` exercising the CLI stub.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-16-004
phase: M0
title: "Create .gitignore for Python artifacts"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-16-003
path: .gitignore
tests: []
acceptance:
  - "Untracked files from virtualenvs and compiled artefacts are ignored"
context: |
  Standard Python projects exclude build outputs and editor files.
instructions: |
  - Add a `.gitignore` covering common Python patterns (`__pycache__`, `.venv`, `*.pyc`, `/dist`).
<!-- task:end -->

<!-- task:start -->
id: 2025-07-16-005
phase: M0
title: "Configure pre-commit with ruff and mypy"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-16-003
path: .pre-commit-config.yaml
tests: []
acceptance:
  - "`pre-commit run --all-files` succeeds"
context: |
  The coding standards document mandates ruff formatting and mypy strict type checks before every commit.
instructions: |
  - Create `.pre-commit-config.yaml` using the snippet from the style guide.
  - Document running `pre-commit install` in the README.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-16-006
phase: M0
title: "Add unit test placeholder"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-16-003
path: tests/test_placeholder.py
tests:
  - tests/test_placeholder.py
acceptance:
  - "`pytest` runs and passes"
context: |
  A minimal test ensures the CI pipeline has something to execute.
instructions: |
  - Create `tests/test_placeholder.py` with a trivial assertion.
  - Ensure the package installs in editable mode for testing.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-16-007
phase: M0
title: "Set up GitHub Actions CI workflow"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-16-005
  - 2025-07-16-006
path: .github/workflows/ci.yml
tests: []
acceptance:
  - "Workflow runs lint, mypy and pytest on pull requests"
  - "All jobs succeed"
context: |
  The CI/CD blueprint defines a job sequence starting with lint-and-format, then unit tests.
instructions: |
  - Create `.github/workflows/ci.yml` implementing `lint-and-format` (ruff & mypy) and `unit-test` jobs.
  - Trigger on `push` and `pull_request` events targeting `main`.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-16-008
phase: M0
title: "Add pull request template"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-16-002
path: .github/pull_request_template.md
tests: []
acceptance:
  - "Template references CONTRIBUTING guidelines"
context: |
  Pull requests are the main communication channel per the communication plan.
instructions: |
  - Create `.github/pull_request_template.md` with summary and testing sections mirroring the CONTRIBUTING instructions.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-16-009
phase: M0
title: "Enable Dependabot for dependencies"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-16-001
path: .github/dependabot.yml
tests: []
acceptance:
  - "Dependabot opens PRs for GitHub Actions and pip updates"
context: |
  The CI/CD blueprint recommends automated dependency monitoring.
instructions: |
  - Add `.github/dependabot.yml` covering `github-actions` and `pip` ecosystems.
  - Schedule weekly checks.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-16-010
phase: M0
title: "Add ADR folder with system architecture record"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-16-002
path: docs/adr/0001-system-architecture.md
tests: []
acceptance:
  - "ADR mirrors content from specification"
context: |
  The architecture decision record from the specification should be versioned under `docs/adr` for future changes.
instructions: |
  - Create `docs/adr/` directory.
  - Copy the initial system architecture ADR from `docs/spec/3_Architecture & Design/1_High-Level Architecture Diagram & ADRs/adr-0001-system-architecture.md`.
  - Include ADR index in `docs/adr/README.md` if helpful.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-001
phase: M1
title: "Implement StudyProtocolIR Pydantic models"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-16-003
path:
  - protocol_to_crf_generator/models/protocol.py
  - tests/test_models.py
tests:
  - tests/test_models.py
acceptance:
  - "Pydantic validation raises errors on invalid input"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The technical plan defines a canonical StudyProtocolIR composed of
  `Provenance`, `DataCollectionRequirement` and a root object holding
  metadata. These models enable validation and decouple ingestion from
  mapping.
instructions: |
  - Add `protocol_to_crf_generator/models/protocol.py` implementing the
    Pydantic models.
  - Reference the field names and example from the technical plan.
  - Write tests in `tests/test_models.py` exercising validation behaviour.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-002
phase: M1
title: "Create DOCX importer with table extraction"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-001
path:
  - protocol_to_crf_generator/ingestion/docx_importer.py
  - tests/test_docx_importer.py
tests:
  - tests/test_docx_importer.py
acceptance:
  - "`load_docx()` returns document text and list of tables as CSV"
  - "Unsupported file types raise `ValueError`"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  User stories PI‑01‑01 and PI‑02‑02 require uploading DOCX protocols and
  emitting tables as normalised CSV. The importer feeds the NLP pipeline.
instructions: |
  - Implement `load_docx(path: Path)` using `python-docx`.
  - Flatten table headers and return a list of CSV strings.
  - Ensure only `.docx` files are accepted.
  - Add unit tests covering a small sample document.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-003
phase: M1
title: "Implement rule-based NLP extraction"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-002
path:
  - protocol_to_crf_generator/nlp/extract.py
  - tests/test_extract.py
tests:
  - tests/test_extract.py
acceptance:
  - "Visits and assessments are returned with confidence ≥0.8"
  - "Provenance includes page and table identifiers when available"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Epic PI‑03 outlines extracting visits, assessments and timing entities
  with provenance. A simple spaCy pipeline is sufficient for the
  prototype.
instructions: |
  - Create `nlp/extract.py` implementing rule-based patterns with spaCy.
  - Return entities with start/end offsets and source provenance.
  - Provide unit tests using example sentences from the spec.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-004
phase: M1
title: "Persist StudyProtocolIR JSON with hash manifest"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-003
path:
  - protocol_to_crf_generator/persistence/storage.py
  - tests/test_storage.py
tests:
  - tests/test_storage.py
acceptance:
  - "JSON output is canonicalised per RFC 8785"
  - "Manifest lists filename, SHA-256 hash and timestamp"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  PI‑04‑01 and PI‑04‑02 require storing validated IR JSON with a
  cryptographic hash manifest for audit purposes.
instructions: |
  - Write `storage.py` providing `save_ir(ir: StudyProtocolIR)` that writes
    canonical JSON and updates `manifest.csv`.
  - Compute SHA-256 hashes and store timestamped entries.
  - Add unit tests verifying reproducible hashes.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-005
phase: M1
title: "Add FastAPI gateway with /ingest and /health endpoints"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-004
path:
  - protocol_to_crf_generator/api/main.py
  - tests/test_api.py
tests:
  - tests/test_api.py
acceptance:
  - "POST /ingest returns 202 and job-id on valid input"
  - "GET /health returns application status"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The FastAPI contract defines an /ingest endpoint accepting ProtocolInput
  and returning JobStatus. A /health route provides a basic liveness check.
instructions: |
  - Implement FastAPI app in `api/main.py` with routes `/ingest` and `/health`.
  - Use Pydantic models from `models/protocol.py` for request/response.
  - Invoke the importer, NLP and storage modules when handling `/ingest`.
  - Write tests using TestClient to validate responses.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-006
phase: M1
title: "Record structured audit logs to SQLite"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-005
path:
  - protocol_to_crf_generator/audit/logging.py
  - tests/test_logging.py
tests:
  - tests/test_logging.py
acceptance:
  - "Errors write JSON entries with level and trace_id to AuditLog table"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Risk R1 mandates an immutable audit log. Logs must capture each
  ingestion step for troubleshooting and compliance.
instructions: |
  - Create `audit/logging.py` configuring the standard logging module to
    write JSON records to `audit_log.sqlite`.
  - Integrate logging into the FastAPI ingestion flow.
  - Provide unit tests checking database rows are inserted.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-007
phase: M1
title: "Add mapping service stub and /map endpoint"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-005
path:
  - protocol_to_crf_generator/api/mapping.py
  - tests/test_mapping.py
tests:
  - tests/test_mapping.py
acceptance:
  - "POST /map returns a placeholder crf_id for a given ir_id"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The API contract specifies a /map endpoint translating StudyProtocolIR
  into CRF artefacts. The prototype returns a dummy ID.
instructions: |
  - Implement `/map` route in `mapping.py` using FastAPI router.
  - Accept a MappingRequest with `ir_id` and return a stub MappingResult.
  - Add unit tests exercising the endpoint.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-008
phase: M1
title: "Add validation service stub and /validate endpoint"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-007
path:
  - protocol_to_crf_generator/api/validation.py
  - tests/test_validation.py
tests:
  - tests/test_validation.py
acceptance:
  - "POST /validate returns status for a supplied crf_id"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The validation microservice checks generated CRFs. For the prototype it
  returns a fixed status value.
instructions: |
  - Create FastAPI router `validation.py` with `/validate` route.
  - Respond with a ValidationResult object containing a stub status.
  - Provide unit tests verifying request and response models.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-009
phase: M1
title: "Extend CLI with ingest command"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-005
path:
  - protocol_to_crf_generator/__main__.py
  - tests/test_cli_ingest.py
tests:
  - tests/test_cli_ingest.py
acceptance:
  - "`python -m protocol_to_crf_generator ingest file.docx` posts to /ingest"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  A CLI wrapper simplifies automated use cases. It should call the REST
  API using the contracts defined in the specification.
instructions: |
  - Add an `ingest` subcommand to `__main__.py` that uploads a DOCX file
    to the running API service.
  - Implement a simple progress message and error handling.
  - Write tests mocking the HTTP call.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-010
phase: M1
title: "Create Dockerfile for FastAPI service"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-005
path: Dockerfile
tests: []
acceptance:
  - "Docker image builds successfully and runs the API"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The technical plan mandates containerised deployment. The Dockerfile
  will be used by the CI pipeline and local testing.
instructions: |
  - Write a multi-stage Dockerfile installing dependencies and copying
    the application source.
  - Expose the FastAPI app using `uvicorn` as entrypoint.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-011
phase: M1
title: "Document canonical IR design in new ADR"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-17-001
path:
  - docs/adr/0002-canonical-ir.md
tests: []
acceptance:
  - "ADR explains rationale for StudyProtocolIR model"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Future architectural changes require a recorded decision on the IR
  structure. An ADR ensures traceability and community discussion.
instructions: |
  - Create `docs/adr/0002-canonical-ir.md` following the ADR template.
  - Summarise trade-offs and the chosen schema approach.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-012
phase: M1
title: "Update README with API and Docker usage"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-17-009
  - 2025-07-17-010
path: README.md
tests: []
acceptance:
  - "README documents running the Docker image and CLI ingest command"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The documentation should guide users through the prototype via Docker
  and CLI. Examples increase adoption and test coverage clarity.
instructions: |
  - Add sections showing how to build and run the Docker container.
  - Provide a usage example for `python -m protocol_to_crf_generator ingest`.
<!-- task:end -->


<!-- End of TASKS.md -->
