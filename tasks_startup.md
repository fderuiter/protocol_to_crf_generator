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

- [ ] **Configure pre-commit and code style**
  - [ ] Install `pre-commit` and run `pre-commit install` after cloning.
  - [ ] `.pre-commit-config.yaml` should run `ruff` and `mypy --strict`.
  - [ ] Execute `pre-commit run --all-files` and `pytest` before pushing changes.

- [ ] **Set up automated testing and quality gates**
  - [ ] Configure GitHub Actions to run sequential jobs: lint-and-format (`ruff` + `mypy --strict`), unit-test (`pytest` with coverage ≥90%), security-scan (Bandit & Semgrep), schema-validate artefacts, package, and deploy on tagged releases.
  - [ ] Trigger workflows on pushes/PRs to `main` and schedule a weekly job for controlled terminology updates.

- [ ] **Maintain testing standards**
  - [ ] Run `pytest -n auto --cov` locally; tests and pre-commit must succeed before pushing.
  - [ ] Satisfy the Definition of Done checklist: passing tests with coverage ≥90%, no critical lint/security issues, docs updated, CI success, and peer review.

- [ ] **Provide governance and compliance documentation**
  - [ ] Maintain a third-party software inventory under `docs/7_Governance & Compliance`.
  - [ ] Add a “Standard Version Adoption and Management Policy” in `GOVERNANCE.md`.
  - [ ] Document the security & privacy threat model in the repository.

- [ ] **Automate controlled terminology updates**
  - [ ] Implement a scheduled GitHub Action that checks NCI-EVS weekly, generates `terminology.sqlite`, opens a PR, and requires manual review before merging.

- [ ] **Include deployment instructions**
  - [ ] Document Docker-based deployment and rollback steps in the repository runbook.
  - [ ] Publish static documentation with MkDocs using the Material theme.

- [ ] **Use GitHub issues and PRs as the canonical communication channel**
  - [ ] Track tasks and decisions in issues and keep discussions in PRs for auditability.
  - [ ] Use GitHub Projects for backlog grooming and link meeting notes to issues or PRs.

- [ ] **Plan future work**
  - [ ] After completing the above tasks, create a new robust, comprehensive, and precise task list outlining the next steps for the project.
