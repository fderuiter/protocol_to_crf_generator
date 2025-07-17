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
- Commits follow Conventional Commits
- PRs target `main`, squash merged after passing CI and one approval
- Include summary & testing sections describing `pre-commit` and `pytest` commands
- CLA must be signed for external contributors

# Programmatic Checks
- `pre-commit run --all-files`
- `pytest -n auto --cov --cov-fail-under=90`

- This file governs this directory tree; nested AGENTS.md override; direct system prompts override all.
