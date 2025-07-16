# Repository Startup Tasks

This document lists the tasks required to set up the repository and project on GitHub as described in the documentation.

- [x] **Create the repository with basic files**
  - [x] Add a README with prerequisites and a quick 3-step setup including `pre-commit` installation.
  - [x] Include an Apache 2.0 LICENSE file in the root.
  - [x] Maintain a third-party inventory for dependency licenses.

- [x] **Prepare contributor and community files**
  - [x] Add `CONTRIBUTING.md` describing the workflow for forking, branch naming, and the PR template.
  - [x] Include a Contributor Covenant `CODE_OF_CONDUCT.md`.
  - [x] Enable a CLA workflow so external contributors sign before merging PRs.

- [x] **Establish branching and commit rules**
  - [x] Use the documented branch types (`main`, `feat/<desc>`, `docs/<topic>`, `release/vX.Y.Z`, `hotfix/vX.Y.Z`, `chore/ct-update-<date>`).
  - [x] Follow Conventional Commits. Pull requests target `main` and are squash-merged after approval and passing checks.
  - [x] Tag releases with `vMAJOR.MINOR.PATCH` to trigger package and image publishing.

- [x] **Configure pre-commit and code style**
  - [x] Install `pre-commit` and run `pre-commit install` after cloning.
  - [x] `.pre-commit-config.yaml` should run `ruff` and `mypy --strict`.
  - [x] Execute `pre-commit run --all-files` and `pytest` before pushing changes.

- [x] **Set up automated testing and quality gates**
  - [x] Configure GitHub Actions to run sequential jobs: lint-and-format (`ruff` + `mypy --strict`), unit-test (`pytest` with coverage ≥90%), security-scan (Bandit & Semgrep), schema-validate artefacts, package, and deploy on tagged releases.
  - [x] Trigger workflows on pushes/PRs to `main` and schedule a weekly job for controlled terminology updates.

- [x] **Maintain testing standards**
  - [x] Run `pytest -n auto --cov` locally; tests and pre-commit must succeed before pushing.
  - [x] Satisfy the Definition of Done checklist: passing tests with coverage ≥90%, no critical lint/security issues, docs updated, CI success, and peer review.

- [x] **Provide governance and compliance documentation**
  - [x] Maintain a third-party software inventory under `docs/7_Governance & Compliance`.
  - [x] Add a “Standard Version Adoption and Management Policy” in `GOVERNANCE.md`.
  - [x] Document the security & privacy threat model in the repository.

- [x] **Automate controlled terminology updates**
  - [x] Implement a scheduled GitHub Action that checks NCI-EVS weekly, generates `terminology.sqlite`, opens a PR, and requires manual review before merging.

- [x] **Include deployment instructions**
  - [x] Document Docker-based deployment and rollback steps in the repository runbook.
  - [x] Publish static documentation with MkDocs using the Material theme.

- [x] **Use GitHub issues and PRs as the canonical communication channel**
  - [x] Track tasks and decisions in issues and keep discussions in PRs for auditability.
  - [x] Use GitHub Projects for backlog grooming and link meeting notes to issues or PRs.

- [x] **Plan future work**
  - [x] After completing the above tasks, create a new robust, comprehensive, and precise task list outlining the next steps for the project.

## Future Work

- [ ] **Phase 1: Core Engine and Foundational Domains (MVP)**
  - [ ] Implement the CI/CD pipeline foundation (lint, test, package).
  - [ ] Manage CDISC reference data (ODM schemas and CT SQLite database).
  - [ ] Build the DOCX protocol importer.
  - [ ] Develop the NLP pipeline for sentence segmentation and section detection.
  - [ ] Implement rule-based NER and mapping for Demographics (DM), Vital Signs (VS), and Concomitant Medications (CM).
  - [ ] Generate ODM and Markdown artefacts.
  - [ ] Add structural and controlled terminology validation layers.
  - [ ] Provide a CLI entry point for the pipeline.

- [ ] **Phase 2: Expanded Domain Coverage & API**
  - [ ] Extend NER and mapping to Adverse Events (AE), Medical History (MH), Disposition (DS), and Exposure (EX).
  - [ ] Develop and deploy the FastAPI REST API.
  - [ ] Automate CT updates via a GitHub Action.
  - [ ] Publish user documentation, API reference, and a mapping guide.

- [ ] **Phase 3: Advanced Features & Governance**
  - [ ] Build an optional SPA Web UI for file upload and download.
  - [ ] Implement PDF and structured XML importers.
  - [ ] Train a statistical NER model using data bootstrapped from the rule-based system.
  - [ ] Integrate the CDISC CORE validation engine.
  - [ ] Establish the formal governance framework and contribution process.
