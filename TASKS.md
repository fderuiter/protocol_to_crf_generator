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

<!-- End of TASKS.md -->
