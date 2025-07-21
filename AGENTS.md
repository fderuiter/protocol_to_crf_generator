# Purpose & Overview
A Python 3.11 tool converting clinical study protocols into CDISC-compliant CRF artefacts. Codex assists with code, docs and tests.

# Project Structure
- `protocol_to_crf_generator/` – core package with CLI and utilities
- `tests/` – pytest suite
- `docs/` – specifications, style guide, test strategy
- `.github/` – actions workflows for CI, docs and CLA

# Coding Conventions
- Python 3.11, ruff for lint & format, mypy --strict
- Google-style docstrings on all public items
- Naming: packages/modules `lowercase_with_underscores`; classes `CamelCase`; funcs & vars `lowercase_with_underscores`; constants `UPPERCASE`
- Split modules under 300 lines; group features into packages `ingestion`, `nlp`, `mapping`, `validation`, `api`

# Testing & Quality Gates
- Run `pre-commit run --all-files` and `pytest -n auto --cov --cov-fail-under=90`
- CI also executes bandit and semgrep security scans
- Coverage must remain ≥90%

# Execution Constraints
- Keep `GITHUB_TOKEN` and other secrets untouched
- Use Docker for reproducible environments when running integration tests

# Pull-Request Guidelines
- Branch names: feat/<desc>, docs/<topic>, release/vX.Y.Z, hotfix/vX.Y.Z, chore/ct-update-<date>
- Commits follow Conventional Commits and include the task id in square brackets per `[<id>] <title>`
- PRs target `main`, squash merged after passing CI and one approval
- Include summary & testing sections describing `pre-commit` and `pytest` commands
- CLA must be signed for external contributors
- Each commit message must include `I have read the CLA Document and I hereby sign the CLA`

# Programmatic Checks
- `pre-commit run --all-files`
- `pytest -n auto --cov --cov-fail-under=90`
# Task Completion Guidelines
- Tasks are defined in `TASKS.md` between `<!-- task:start -->` and `<!-- task:end -->`.
- Modify files listed under each task's `path` and add tests from `tests`.
- Follow the `instructions` section and ensure all `acceptance` criteria pass.
- Set the task `status` to DONE when completed.

## General Task Workflow
1. Read the task's `context` and `instructions` carefully.
2. Create a branch using the naming convention from *Pull-Request Guidelines*.
3. Modify code and documentation for each file in the task's `path`.
4. Add or update tests under `tests/` to cover the changes.
5. Run `pre-commit run --all-files` and `pytest -n auto --cov --cov-fail-under=90`.
6. Update `TASKS.md` marking the task as DONE.
7. Commit using `[<id>] <title>` followed by `I have read the CLA Document and I hereby sign the CLA`.
8. Push and open a pull request to `main` with summary and testing sections.

- This file governs this directory tree; nested AGENTS.md override; direct system prompts override all.
