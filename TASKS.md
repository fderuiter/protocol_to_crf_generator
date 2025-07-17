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


<!-- task:start -->
id: 2025-07-17-013
phase: M2
title: "Create Locust load-test suite"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-005
  - 2025-07-17-010
path:
  - tests/performance/locustfile.py
  - tests/performance/README.md
tests: []
acceptance:
  - "Locust script simulates 500 users hitting /ingest"
  - "Median pipeline time ≤5 min; P95 ≤7 min on reference node"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  NFR checklist mandates Locust load tests to validate pipeline throughput and latency targets.
instructions: |
  - Add `tests/performance/locustfile.py` generating POST requests to `/ingest`.
  - Document running `locust -f locustfile.py` in `tests/performance/README.md`.
  - Ensure results capture median and P95 timings for comparison.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-014
phase: M2
title: "Cache controlled terminology lookups"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-005
path:
  - protocol_to_crf_generator/ct_cache.py
  - tests/test_ct_cache.py
tests:
  - tests/test_ct_cache.py
acceptance:
  - "Lookup cache reduces repeated DB queries by ≥90%"
  - "Memory footprint ≤1 GB steady state"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Performance NFRs require efficient terminology access. A local cache will minimise database I/O.
instructions: |
  - Implement an in-memory LRU cache in `ct_cache.py`.
  - Integrate it with terminology lookups in the mapping service.
  - Write tests measuring cache hit rate with repeated queries.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-015
phase: M2
title: "Add API rate limiting middleware"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-005
path:
  - protocol_to_crf_generator/api/rate_limit.py
  - tests/test_rate_limit.py
tests:
  - tests/test_rate_limit.py
acceptance:
  - "Excessive requests return HTTP 429"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The threat model lists denial-of-service as a risk. Rate limiting mitigates abusive traffic.
instructions: |
  - Use `slowapi` or equivalent middleware to enforce per-IP request limits.
  - Configure limits in `api/main.py` and document override variables.
  - Provide tests triggering the limit with repeated calls.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-016
phase: M2
title: "Integrate OWASP ZAP scan in CI"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-16-007
path: .github/workflows/zap_scan.yml
tests: []
acceptance:
  - "ZAP workflow reports 0 high-risk findings"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Weekly OWASP ZAP scans are part of the NFR security checklist.
instructions: |
  - Add `zap_scan.yml` executing ZAP against the staging URL.
  - Fail the job on any high or critical alerts.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-017
phase: M2
title: "Implement secrets rotation utility"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-010
path:
  - scripts/rotate_secrets.py
  - docs/ops/rotate-secrets.md
tests: []
acceptance:
  - "Rotation script replaces API and DB secrets without downtime"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Rotating credentials regularly reduces the impact of secret leaks per the security NFRs.
instructions: |
  - Create `rotate_secrets.py` that generates new tokens and updates the deployment environment.
  - Document the procedure in `docs/ops/rotate-secrets.md`.
  - Schedule rotation via CI or cron as appropriate.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-018
phase: M2
title: "Enforce TLS and non-root containers"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-010
  - 2025-07-17-005
path:
  - Dockerfile
  - deploy/docker-compose.yml
tests: []
acceptance:
  - "Qualys scan grade A+ with no weak ciphers"
  - "Containers run as non-root user"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  NFR security requirements call for TLS1.2+ and container hardening. The threat model notes container escape risks.
instructions: |
  - Update `Dockerfile` to drop privileges and expose the service via HTTPS only.
  - Configure `docker-compose.yml` with mounted certificates and a non-root UID.
  - Document certificate generation and mounting steps.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-019
phase: M2
title: "Add RBAC authentication via external IdP"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-005
path:
  - protocol_to_crf_generator/api/security.py
  - tests/test_rbac.py
tests:
  - tests/test_rbac.py
acceptance:
  - "Privileged endpoints require valid access token"
  - "≥95% unit-test coverage on auth checks"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  RBAC with an external identity provider mitigates data-leakage risk R6 and satisfies the NFR security requirement.
instructions: |
  - Implement OAuth2 bearer authentication in `security.py`.
  - Protect `/ingest`, `/map` and `/validate` with role checks.
  - Provide tests using FastAPI TestClient and mocked token verification.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-020
phase: M2
title: "Ensure structured logging with correlation IDs"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-006
path:
  - protocol_to_crf_generator/audit/logging.py
  - tests/test_logging.py
tests:
  - tests/test_logging.py
acceptance:
  - "100% API calls emit JSON logs with trace_id"
  - "Ingestion→generation trace coverage ≥95%"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Observability NFRs specify structured JSON logging with correlation IDs across all services.
instructions: |
  - Extend `logging.py` to inject a `trace_id` into every log record.
  - Propagate the ID through API requests and background tasks.
  - Add tests verifying presence of `trace_id` fields.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-021
phase: M2
title: "Expose Prometheus metrics and alert rules"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-005
  - 2025-07-16-007
path:
  - protocol_to_crf_generator/metrics.py
  - tests/test_metrics.py
  - deploy/prometheus-alerts.yml
tests:
  - tests/test_metrics.py
acceptance:
  - "Metrics endpoint exports RED and 4 golden signals"
  - "Alert fires when 99th-latency >3s for >10 min"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The NFR checklist requires Prometheus metrics with latency SLO alerts monitored by Grafana/PagerDuty.
instructions: |
  - Implement counters and histograms in `metrics.py` and mount at `/metrics`.
  - Provide `deploy/prometheus-alerts.yml` defining the latency alert rule.
  - Add tests asserting metrics are emitted during sample requests.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-022
phase: M2
title: "Add readiness and liveness probes"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-005
path:
  - protocol_to_crf_generator/api/health.py
  - tests/test_health.py
tests:
  - tests/test_health.py
acceptance:
  - "GET /healthz returns 200 for liveness"
  - "GET /ready returns 200 when dependencies reachable"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Health probes allow Kubernetes to restart unhealthy pods and are part of the availability NFRs.
instructions: |
  - Add `/healthz` and `/ready` routes in `health.py`.
  - Implement dependency checks for the readiness endpoint.
  - Create tests verifying HTTP 200 responses and failure cases.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-023
phase: M2
title: "Generate consolidated validation log"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-008
path:
  - protocol_to_crf_generator/validation/report.py
  - tests/test_validation_report.py
tests:
  - tests/test_validation_report.py
acceptance:
  - "Validation log JSON schema validates for sample jobs"
  - "Human-readable summary generated alongside JSON"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The NFR checklist requires a consolidated validation log for every job.
instructions: |
  - Create `report.py` producing both JSON and Markdown validation summaries.
  - Validate the JSON format against a schema in tests.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-024
phase: M2
title: "Provision staging environment configuration"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-010
path:
  - deploy/docker-compose.staging.yml
  - docs/ops/staging-setup.md
tests: []
acceptance:
  - "Staging stack starts via docker-compose.staging.yml"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  A dedicated staging environment enables blue/green testing before production rollout.
instructions: |
  - Create `docker-compose.staging.yml` mirroring production services.
  - Document setup steps in `docs/ops/staging-setup.md`.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-025
phase: M2
title: "Implement blue/green deployment workflow"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-024
  - 2025-07-16-007
path: .github/workflows/deploy-bluegreen.yml
tests: []
acceptance:
  - "Workflow deploys new container alongside old and switches after health pass"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Staged-release procedures reduce downtime and support quick rollback as described in the runbook.
instructions: |
  - Define `deploy-bluegreen.yml` using two services `blue` and `green`.
  - Switch traffic after `/ready` returns success for the new version.
  - Reuse the runbook steps for pulling images and running migrations.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-026
phase: M2
title: "Run smoke tests after deployment"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-025
path:
  - tests/smoke/test_smoke.py
  - .github/workflows/deploy-bluegreen.yml
  - docs/ops/staging-setup.md
tests:
  - tests/smoke/test_smoke.py
acceptance:
  - "Smoke tests verify /healthz and /validate on deployed build"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The deployment runbook lists health checks to confirm a successful rollout.
instructions: |
  - Add `test_smoke.py` exercising key endpoints against the staging deployment.
  - Invoke the smoke tests in `deploy-bluegreen.yml` before switching traffic.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-027
phase: M2
title: "Add performance and security gates to CI"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-16-007
  - 2025-07-17-013
  - 2025-07-17-016
path: .github/workflows/ci.yml
tests: []
acceptance:
  - "CI fails if load test latency or ZAP scan exceed thresholds"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The CI/CD blueprint calls for perf and security gates before packaging.
instructions: |
  - Update `ci.yml` to run Locust and ZAP jobs after unit tests.
  - Fail the workflow if thresholds are not met.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-028
phase: M2
title: "Implement artifact versioning"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-16-007
path:
  - pyproject.toml
  - .github/workflows/ci.yml
tests: []
acceptance:
  - "Docker images and wheels tagged with semver and git SHA"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Versioned artefacts support reproducible deployments and validation evidence.
instructions: |
  - Update `pyproject.toml` to read the version from git tags.
  - Append the git SHA to Docker image tags in `ci.yml`.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-029
phase: M2
title: "Enable shadow writes for database migrations"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-004
path:
  - protocol_to_crf_generator/persistence/shadow.py
  - tests/test_shadow.py
tests:
  - tests/test_shadow.py
acceptance:
  - "Shadow tables receive writes in parallel during migration"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Data migration safety requires shadow writes before switching schemas.
instructions: |
  - Implement a wrapper in `shadow.py` duplicating writes to new tables.
  - Provide tests ensuring data consistency between live and shadow tables.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-030
phase: M2
title: "Provide automated rollback script"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-029
path:
  - scripts/rollback.sh
  - docs/ops/rollback-guide.md
tests: []
acceptance:
  - "Rollback script restores previous container and DB version"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The runbook specifies commands for pulling prior images and database downgrade.
instructions: |
  - Implement `scripts/rollback.sh` automating the runbook steps:
    `docker pull`, `docker-compose down`, `alembic downgrade -1`.
  - Document usage in `docs/ops/rollback-guide.md`.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-031
phase: M2
title: "Add NLP regression corpus accuracy tests"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-003
path:
  - tests/regression/test_extraction_accuracy.py
  - data/regression_corpus/
tests:
  - tests/regression/test_extraction_accuracy.py
acceptance:
  - "Extraction accuracy ≥90% across regression corpus"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Risk R2 identifies incorrect NLP extraction as a critical issue; automated accuracy tests mitigate drift.
instructions: |
  - Assemble sample protocols under `data/regression_corpus/`.
  - Implement tests comparing extracted entities to golden outputs.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-032
phase: M2
title: "Nightly audit log hash-chain verification"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-006
path:
  - .github/workflows/audit-chain.yml
  - protocol_to_crf_generator/audit/hash_check.py
tests: []
acceptance:
  - "Workflow fails if audit chain verification detects tampering"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Risk R1 requires immutable audit logs validated nightly via SHA-256 chain verification.
instructions: |
  - Implement `hash_check.py` computing and verifying the hash chain of audit entries.
  - Schedule a nightly GitHub Actions workflow `audit-chain.yml` to run the check.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-033
phase: M2
title: "Regression test for CT updates"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-16-007
path:
  - .github/workflows/ct-update-test.yml
  - tests/test_ct_update_regression.py
tests:
  - tests/test_ct_update_regression.py
acceptance:
  - "CT update workflow runs mapping regression tests automatically"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Risk R3 notes terminology updates may break mappings; automated regression protects against this.
instructions: |
  - Create workflow `ct-update-test.yml` triggered weekly and on CT PRs.
  - Add tests ensuring mapping results remain stable after updates.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-034
phase: M2
title: "Schedule weekly Bandit and Semgrep scans"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-16-007
path: .github/workflows/sast.yml
tests: []
acceptance:
  - "Weekly SAST workflow reports zero high severity findings"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Risk R4 highlights vulnerabilities in dependencies; scheduled scans ensure early detection.
instructions: |
  - Configure `sast.yml` to run Bandit and Semgrep on a weekly schedule.
  - Fail the job if any high severity issues are found.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-035
phase: M2
title: "Encrypt protocol documents at rest"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-004
path:
  - protocol_to_crf_generator/persistence/encrypt.py
  - tests/test_encrypt.py
tests:
  - tests/test_encrypt.py
acceptance:
  - "Stored documents encrypted with AES-256"
  - "Decryption yields original bytes"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Risk R6 and the security NFR require encryption at rest to prevent data leakage.
instructions: |
  - Implement helper functions in `encrypt.py` for AES-256 encryption using `cryptography`.
  - Update storage logic to encrypt protocol files before saving.
  - Provide tests confirming round-trip encryption and decryption.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-036
phase: M2
title: "Update documentation for Beta release"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-17-025
path:
  - README.md
  - docs/spec/5_Quality & Ops/4_Deployment & Rollback Runbook/runbook-deploy-rollback.md
  - docs/adr/README.md
tests: []
acceptance:
  - "README reflects staging and blue/green workflows"
  - "Runbook updated with smoke test steps"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Documentation must advertise the Public Beta capabilities and deployment procedures.
instructions: |
  - Revise the README with instructions for staging, blue/green deploy and metrics endpoints.
  - Update the runbook to include smoke test and rollback script references.
  - Add an ADR index entry noting the project has entered Beta.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-17-037
phase: M2
title: "Document disaster recovery plan and failover test"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-024
path:
  - docs/ops/disaster-recovery.md
  - tests/test_failover.py
tests:
  - tests/test_failover.py
acceptance:
  - "Failover exercise restores service within RTO ≤4h and RPO ≤15min"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Availability NFRs specify disaster recovery objectives; a documented DR plan and test confirm readiness.
instructions: |
  - Create `disaster-recovery.md` detailing backup strategy and failover steps.
  - Implement `test_failover.py` simulating a restore from snapshot.
  - Include the exercise results in project records.
<!-- task:end -->
<!-- End of TASKS.md -->
