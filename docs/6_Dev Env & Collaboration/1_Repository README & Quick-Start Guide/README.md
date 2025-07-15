# Repository README & Quick-Start Guide

This document mirrors the top-level `README.md` and provides a concise orientation for new developers. It summarises the essential information from the [CDISC CRF Generation Technical Plan](../../CDISC%20CRF%20Generation%20Technical%20Plan_.md) so the project can be set up in minutes.

## Badges

![CI](https://img.shields.io/badge/ci-github%20actions-blue?logo=github)
![License](https://img.shields.io/badge/license-Apache%202.0-blue)

## Prerequisites

- **Python 3.11+** and `pip`
- **Git** for version control
- **Docker** (optional, for container execution)
- `pre-commit` for automated linting and type checks

## 3-Step Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/protocol-to-crf-generator.git
   cd protocol-to-crf-generator
   ```
2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   pre-commit install
   ```
3. **Run the CLI**
   ```bash
   python -m protocol_to_crf_generator --help
   ```

## Common Commands

- `pre-commit run --all-files` – lint and type-check the entire codebase
- `pytest` – execute the unit and integration tests
- `docker compose up` – launch services defined in `deploy/docker-compose.yml`
- `python -m protocol_to_crf_generator <args>` – invoke the CLI directly

## Testing Instructions

The project follows the strategy outlined in `docs/5_Quality & Ops/1_Test Strategy & Definition of Done/test-strategy.md`.
Run the full suite with:
```bash
pytest -n auto --cov
```
All tests must pass and coverage should remain ≥90% before merging.

## How to Contribute

Please read `docs/6_Dev Env & Collaboration/3_Contribution Guidelines & Code-Review Checklist/CONTRIBUTING.md` for details on the fork → branch → pull request workflow, coding standards and the code review checklist.

## License

This project is licensed under the terms of the [Apache 2.0](../../../LICENSE) license.
