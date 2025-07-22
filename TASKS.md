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
  - {tag: M4, name: "Continuous Improvement & Scale-Out", target: "TBD"}
-->

<!-- task:start -->
id: 2025-07-16-001
phase: M0
title: "Create GitHub repository and main branch"
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
status: DONE
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
<!-- task:start -->
id: 2025-07-18-001
phase: M3
title: "Execute production blue/green rollout"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-025
  - 2025-07-17-026
path:
  - .github/workflows/release-prod.yml
  - docs/ops/release-checklist.md
  - deploy/docker-compose.yml
  - tests/smoke/test_smoke.py
tests:
  - tests/smoke/test_smoke.py
acceptance:
  - "Production deployment completes without downtime"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The runbook instructs to pull the versioned image, stop existing containers, start new containers,
  run migrations and verify health before switching traffic.
instructions: |
  - Create `release-prod.yml` triggered manually to promote the latest tagged image.
  - Follow runbook steps: `docker pull`, `docker-compose down`, start with `VERSION` env and run `alembic upgrade head`.
  - Invoke smoke tests before flipping the active service.
  - Document the release checklist in `docs/ops/release-checklist.md`.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-18-002
phase: M3
title: "Set up Grafana dashboards and on-call rotation"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-021
path:
  - deploy/grafana-dashboard.json
  - docs/ops/incident-playbook.md
  - docs/ops/oncall-rota.md
  - deploy/prometheus-alerts.yml
tests: []
acceptance:
  - "SLO alert triggers when 99th-latency >3s for >10min"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Observability NFRs require Prometheus metrics with Grafana dashboards and PagerDuty alerts.
  Incident playbooks describe steps for responders.
instructions: |
  - Define dashboards visualising RED metrics and latency SLOs in `grafana-dashboard.json`.
  - Configure alert rules in `prometheus-alerts.yml` and link to PagerDuty.
  - Document the on-call rota and step-by-step incident playbook.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-18-003
phase: M3
title: "Implement cross-region backups and restore drill"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-037
path:
  - scripts/backup.sh
  - docs/ops/disaster-recovery.md
  - tests/test_restore_drill.py
tests:
  - tests/test_restore_drill.py
acceptance:
  - "Restore from cross-region backup within RTO ≤4h and RPO ≤15min"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The technical plan's DRP states daily snapshots and quarterly failover exercises.
  Backups must replicate to another region to guard against outage.
instructions: |
  - Write `backup.sh` performing daily snapshots and copying them to a secondary region.
  - Extend `disaster-recovery.md` with cross-region restore steps.
  - Add `test_restore_drill.py` simulating recovery from the backup location.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-18-004
phase: M3
title: "Generate SPDX SBOM and verify license inventory"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-16-002
path:
  - docs/spec/7_Governance & Compliance/1_License & Third-Party Software Inventory/third-party-inventory.md
  - sbom/spdx_1.0.json
tests: []
acceptance:
  - "SBOM exported with correct licenses for all dependencies"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Inventory lists packages such as spaCy (MIT) and PlantUML (Apache-2.0). GA release requires
  confirming compatibility and publishing an SPDX document.
instructions: |
  - Review `requirements.txt` against `third-party-inventory.md`; add any missing entries.
  - Use `spdx-tools` to generate `sbom/spdx_1.0.json` during release builds.
  - Store the SBOM artefact and link to it in the release notes.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-18-005
phase: M3
title: "Finalize pen-test fixes and compliance attestation"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-016
  - 2025-07-17-017
  - 2025-07-17-018
path:
  - docs/compliance/pen-test-report.md
  - docs/compliance/compliance-attestation.md
  - scripts/rotate_secrets.py
tests: []
acceptance:
  - "All critical pen-test findings resolved and attestation signed"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The threat model mandates TLS, non-root containers and regular secret rotation.
  Final penetration testing must confirm these controls before GA.
instructions: |
  - Address any remaining ZAP or Bandit issues and document fixes in `pen-test-report.md`.
  - Obtain a signed compliance statement in `compliance-attestation.md`.
  - Schedule quarterly execution of `rotate_secrets.py` via CI.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-18-006
phase: M3
title: "Tag v1.0.0 and publish changelog"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-028
path:
  - CHANGELOG.md
  - docs/api/versioning.md
tests: []
acceptance:
  - "Git tag v1.0.0 pushed and changelog announces GA on 2026-12-31"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  API contracts follow Semantic Versioning 2.0 with one minor release grace period for deprecated endpoints.
  The GA tag marks the first stable release.
instructions: |
  - Add a `CHANGELOG.md` entry summarising features and deprecations.
  - Tag the repository as `v1.0.0` and push to GitHub.
  - Publish `docs/api/versioning.md` describing deprecation timelines and support policy.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-18-007
phase: M3
title: "Publish user guide and maintenance plan"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-036
path:
  - docs/user-guide.md
  - docs/maintenance-plan.md
  - README.md
tests: []
acceptance:
  - "User guide explains CLI, API and Docker usage for GA"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  GA release requires comprehensive documentation and a post-release maintenance plan for
  community contributors.
instructions: |
  - Compile step-by-step instructions in `user-guide.md` covering install and troubleshooting.
  - Outline issue triage and release cadence in `maintenance-plan.md`.
  - Update the README to reference these documents.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-18-008
phase: M3
title: "Operational readiness review and rollback rehearsal"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-030
  - 2025-07-17-013
path:
  - docs/ops/release-checklist.md
  - scripts/rollback.sh
  - tests/performance/locustfile.py
tests:
  - tests/performance/locustfile.py
acceptance:
  - "Load-test report signed off and rollback executed successfully"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The runbook's rollback steps use `docker pull`, `docker-compose down` and `alembic downgrade -1`.
  The CI load tests must pass before production traffic is switched.
instructions: |
  - Review Locust results against performance targets and sign off in `release-checklist.md`.
  - Execute `scripts/rollback.sh` as a rehearsal and document the outcome.
  - Capture any gaps in the checklist for future releases.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-18-009
phase: M3
title: "Close risk register and record residual risks"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-18-008
path:
  - docs/spec/4_Planning & Risk/2_Risk Register & Mitigation Plan/risk-register.md
tests: []
acceptance:
  - "High and Medium risks updated with final mitigations and residual ratings"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  The register lists R1–R6 with exposures up to 16. Final mitigation status must be captured before GA.
instructions: |
  - Update the register noting which risks were mitigated or accepted.
  - Document residual severity and link to supporting evidence.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-001
phase: M4
title: "Tune autoscaling thresholds for REST workers"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-18-002
path:
  - deploy/hpa.yaml
  - tests/performance/test_autoscale.py
tests:
  - tests/performance/test_autoscale.py
acceptance:
  - "CPU utilisation ≤70% at 2× peak load"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  NFR checklist targets ≤70 % CPU at 2× load and linear throughput. Post-GA metrics show workers spiking to 85 % during peak.
instructions: |
  - Add HPA configuration in `deploy/hpa.yaml` with tuned thresholds.
  - Implement load test `test_autoscale.py` verifying scaling behaviour.
  - Document autoscaling settings in deployment guide.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-002
phase: M4
title: "Audit SQLite indexes for terminology lookups"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-17-014
path:
  - protocol_to_crf_generator/db/index_audit.py
  - tests/performance/test_index_audit.py
tests:
  - tests/performance/test_index_audit.py
acceptance:
  - "Term lookup latency <50 ms P95 across 75k rows"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  NFR dataset scaling metric requires <50 ms lookups. Profiling identified slow queries lacking indexes.
instructions: |
  - Create script `index_audit.py` to analyze query plans and recommend indexes.
  - Add or adjust indexes in the terminology database.
  - Provide regression test `test_index_audit.py` measuring lookup latency.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-003
phase: M4
title: "Enable spot instances for batch processing workers"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-18-001
path:
  - deploy/spot-instance.tf
tests: []
acceptance:
  - "Monthly compute cost for batch jobs reduced by ≥20%"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Finance reports highlight rising batch-processing spend. Spot instances can cut costs if jobs are retryable.
instructions: |
  - Define Terraform module `spot-instance.tf` provisioning spot-capable nodes.
  - Update batch worker deployment to tolerate interruptions.
  - Document cost impact and rollback strategy.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-004
phase: M4
title: "Expose CRF diff endpoint for version comparisons"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-17-027
path:
  - protocol_to_crf_generator/api/diff.py
  - tests/test_diff_endpoint.py
tests:
  - tests/test_diff_endpoint.py
acceptance:
  - "API returns structured diff of two CRF versions"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  User feedback notes difficulty tracking changes between protocol revisions.
instructions: |
  - Implement FastAPI route in `diff.py` accepting two CRF IDs.
  - Generate a human-readable and JSON diff of form structures.
  - Document usage with examples in API guide.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-005
phase: M4
title: "Add asynchronous batch submission API"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-19-004
path:
  - protocol_to_crf_generator/api/batch.py
  - tests/test_batch_api.py
tests:
  - tests/test_batch_api.py
acceptance:
  - "Batch endpoint accepts up to 100 protocols and returns job IDs"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Feedback summary indicates need for large protocol submissions without waiting for synchronous completion.
instructions: |
  - Create FastAPI router `batch.py` with background task queue integration.
  - Add job status endpoint to poll progress.
  - Provide tests ensuring jobs enqueue and complete successfully.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-006
phase: M4
title: "Support protocol anonymization via CLI flag"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-16-003
path:
  - protocol_to_crf_generator/cli/anonymize.py
  - tests/test_anonymize_cli.py
tests:
  - tests/test_anonymize_cli.py
acceptance:
  - "Sensitive identifiers removed when --anonymize flag is used"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Compliance reviews suggest an anonymization option for sharing sample protocols publicly.
instructions: |
  - Implement `anonymize.py` stripping patient names and IDs from input DOCX.
  - Integrate flag into the existing CLI entry point.
  - Document limitations and verify with tests.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-007
phase: M4
title: "Chaos testing with latency injection"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-18-002
path:
  - tests/performance/test_chaos.py
  - docs/ops/chaos-exercises.md
tests:
  - tests/performance/test_chaos.py
acceptance:
  - "System maintains SLOs with 200ms added latency"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Reliability workstream introduces chaos experiments to validate resilience under network delays.
instructions: |
  - Use Toxiproxy or equivalent to inject latency in `test_chaos.py`.
  - Document scenarios and outcomes in `chaos-exercises.md`.
  - Integrate chaos tests into nightly CI schedule.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-008
phase: M4
title: "Quarterly incident response drill"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-18-002
path:
  - docs/ops/incident-drill-q1.md
tests: []
acceptance:
  - "Drill summary recorded and action items tracked"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Post-GA operations require regular rehearsal of the incident playbook.
instructions: |
  - Schedule a simulated outage and execute the playbook.
  - Capture response times and lessons learned in `incident-drill-q1.md`.
  - Assign follow-up tasks for any gaps found.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-009
phase: M4
title: "Enforce error-budget policy in deployment pipeline"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-19-007
path:
  - .github/workflows/error-budget.yml
tests: []
acceptance:
  - "Deploy job blocks when monthly SLO budget exhausted"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Observability dashboards track SLO burn rates. Automating enforcement prevents pushing risky changes.
instructions: |
  - Implement workflow `error-budget.yml` querying metrics before deployment.
  - Fail the pipeline if the remaining error budget is below threshold.
  - Document policy in the operations handbook.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-010
phase: M4
title: "Patch dependencies for CVE-2025-1234"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-034
path:
  - requirements.txt
  - docs/security/advisory-2025-1234.md
tests: []
acceptance:
  - "No vulnerable package versions remain after patch"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Security advisory CVE-2025-1234 affects a transitive dependency. Immediate patching is required.
instructions: |
  - Upgrade affected libraries in `requirements.txt`.
  - Document remediation steps in `advisory-2025-1234.md`.
  - Schedule a follow-up vulnerability scan.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-011
phase: M4
title: "Renew TLS certificates and rotate keys"
status: TODO
priority: P0
owner: ai
depends_on:
  - 2025-07-17-018
path:
  - deploy/certs/
  - docs/ops/cert-renewal.md
tests: []
acceptance:
  - "New certificates deployed with zero downtime"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Certificates expire annually and must be rotated to maintain A+ TLS grade per NFR security targets.
instructions: |
  - Generate replacement certificates and store in `deploy/certs`.
  - Document renewal process in `cert-renewal.md`.
  - Update deployment pipeline to reload certificates without downtime.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-012
phase: M4
title: "Run threat-model delta review for new features"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-19-010
path:
  - docs/spec/7_Governance & Compliance/2_Security & Privacy Threat Model/threat-model.md
tests: []
acceptance:
  - "Updated threat model reflects batch and diff APIs"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Introducing new endpoints requires reviewing STRIDE impacts and mitigation controls.
instructions: |
  - Reassess threats introduced by batch processing and diff functionality.
  - Update diagrams and mitigation tables in the threat model document.
  - Link evidence of review in compliance records.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-013
phase: M4
title: "Instrument OpenTelemetry metrics and tracing"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-19-001
path:
  - protocol_to_crf_generator/observability/otel.py
  - tests/test_otel.py
tests:
  - tests/test_otel.py
acceptance:
  - "Request traces exported with <1% overhead"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Fine-grained observability will assist anomaly detection and performance tuning.
instructions: |
  - Add instrumentation in `otel.py` exposing traces and custom metrics.
  - Provide tests verifying trace export and metric labels.
  - Document setup instructions for collectors.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-014
phase: M4
title: "Implement anomaly detection on CRF build times"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-19-013
path:
  - observability/anomaly-detection.yaml
tests: []
acceptance:
  - "Alerts fire when build time exceeds 7min P95 for 3 runs"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Post-GA metrics show occasional spikes above the 7 min P95 build target.
instructions: |
  - Create Prometheus rule file `anomaly-detection.yaml`.
  - Configure alertmanager to notify on sustained anomalies.
  - Document runbook steps for investigation.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-015
phase: M4
title: "Quarterly license re-scan with FOSSA"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-18-004
path:
  - .github/workflows/fossa.yml
tests: []
acceptance:
  - "FOSSA report shows no policy violations"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Governance policy mandates quarterly verification of third-party licenses.
instructions: |
  - Set up `fossa.yml` to run on a quarterly schedule.
  - Upload results to compliance storage and update inventory if needed.
  - Note completion in release notes.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-016
phase: M4
title: "Collect SOC2 evidence for Q1"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-19-015
path:
  - docs/compliance/soc2/q1-evidence.md
tests: []
acceptance:
  - "Evidence package uploaded for auditor review"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  SOC2 readiness activities require quarterly evidence capture.
instructions: |
  - Compile logs, policies and scan reports into `q1-evidence.md`.
  - Store the package in the compliance repository.
  - Notify the auditor per checklist.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-017
phase: M4
title: "Generate updated SBOM after dependency upgrades"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-19-010
path:
  - sbom/spdx_1.1.json
tests: []
acceptance:
  - "SBOM reflects all current package versions"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Dependency patches require regenerating the SBOM to maintain accurate provenance records.
instructions: |
  - Use `spdx-tools` to produce `spdx_1.1.json` during the build.
  - Archive the file with release artefacts.
  - Update documentation referencing the new SBOM.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-018
phase: M4
title: "Automate monthly cloud spend reports"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-19-003
path:
  - finance/monthly_spend_report.py
  - docs/finance/README.md
tests: []
acceptance:
  - "Report generated and shared within 2 days of month end"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Cost governance efforts track monthly spending to catch overruns early.
instructions: |
  - Implement `monthly_spend_report.py` pulling cost data via cloud APIs.
  - Document run schedule and recipients in `docs/finance/README.md`.
  - Hook script into CI for automatic execution.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-019
phase: M4
title: "Set budget alert thresholds"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-19-018
path:
  - finance/budget_alerts.yaml
tests: []
acceptance:
  - "Alerts trigger at 80% and 100% of monthly budget"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Finance guidelines require automated budget notifications to prevent overspend.
instructions: |
  - Define thresholds in `budget_alerts.yaml` for the reporting script.
  - Integrate notifications with Slack and email.
  - Review limits quarterly with finance.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-020
phase: M4
title: "Rightsize production resources based on utilisation"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-19-018
path:
  - deploy/rightsizing.md
tests: []
acceptance:
  - "Average CPU utilisation 50‑70% across services"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Usage metrics reveal consistently low utilisation on some nodes. Adjusting resource limits saves costs.
instructions: |
  - Analyse historical Prometheus data to identify over-provisioned services.
  - Record recommendations in `rightsizing.md` and implement via Helm charts.
  - Monitor after change for performance regressions.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-021
phase: M4
title: "Refactor schema validation module"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-17-029
path:
  - protocol_to_crf_generator/validation/schema.py
  - tests/test_schema_validation.py
tests:
  - tests/test_schema_validation.py
acceptance:
  - "Cyclomatic complexity ≤10 per function"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Static analysis flagged `schema.py` as a hotspot with complex logic.
instructions: |
  - Break down large functions into composable helpers.
  - Update tests to cover refactored paths.
  - Ensure behaviour remains backward compatible.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-022
phase: M4
title: "Upgrade FastAPI framework to latest LTS"
status: TODO
priority: P1
owner: ai
depends_on:
  - 2025-07-19-010
path:
  - requirements.txt
  - tests/test_cli.py
tests:
  - tests/test_cli.py
acceptance:
  - "Application runs on FastAPI LTS without regressions"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Upgrading to the LTS release provides long-term support and new features.
instructions: |
  - Update dependency in `requirements.txt` and resolve breaking changes.
  - Run full test suite to confirm compatibility.
  - Document upgrade notes in CHANGELOG.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-023
phase: M4
title: "Publish official Python SDK"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-19-005
path:
  - sdk/README.md
  - sdk/setup.py
  - tests/test_sdk.py
tests:
  - tests/test_sdk.py
acceptance:
  - "SDK available on PyPI with basic examples"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Community adoption is easier with an installable SDK wrapping API calls.
instructions: |
  - Implement SDK package under `sdk/` with convenience classes.
  - Publish to PyPI and document usage in README.
  - Maintain compatibility with REST API endpoints.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-024
phase: M4
title: "Document deprecation schedule for CLI flags"
status: TODO
priority: P3
owner: ai
depends_on:
  - 2025-07-18-006
path:
  - docs/user-guide.md
  - CHANGELOG.md
tests: []
acceptance:
  - "Deprecated flags listed with removal versions"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Support tickets show confusion around old CLI options slated for removal.
instructions: |
  - Update `user-guide.md` and `CHANGELOG.md` with a deprecation timeline.
  - Provide alternative commands and migration tips.
  - Announce schedule in the next release notes.
<!-- task:end -->

<!-- task:start -->
id: 2025-07-19-025
phase: M4
title: "Revise documentation based on support feedback"
status: TODO
priority: P2
owner: ai
depends_on:
  - 2025-07-19-023
path:
  - docs/faq.md
  - docs/troubleshooting.md
tests: []
acceptance:
  - "Common setup issues addressed in FAQ"
  - "All unit and integration tests pass with coverage ≥90%."
  - "Linting, formatting and security scans report no errors of severity \"Critical\" or higher."
  - "Documentation updated for new or changed features."
  - "CI pipeline completes successfully including Docker image build."
  - "Peer review approvals obtained."
context: |
  Support tickets highlight missing guidance for environment setup and error messages.
instructions: |
  - Compile recurring questions into `faq.md`.
  - Expand `troubleshooting.md` with solutions and log snippets.
  - Cross-link from README and SDK docs.
<!-- task:end -->

<!-- End of TASKS.md -->
