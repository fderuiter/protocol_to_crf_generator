# Protocol to CRF Generator

![CI](https://img.shields.io/badge/ci-github%20actions-blue?logo=github)
![License](https://img.shields.io/badge/license-Apache%202.0-blue)

A toolchain that converts clinical study protocols into CDISC‑compliant Case Report Form artefacts. See the [technical plan](docs/CDISC%20CRF%20Generation%20Technical%20Plan_.md) for the full architecture and design rationale.

## Prerequisites

- Python 3.11+
- Git
- Docker (optional)
- `pre-commit` installed globally or via `pip install pre-commit`

## 3‑Step Setup

1. Clone the repository
   ```bash
   git clone https://github.com/your-org/protocol-to-crf-generator.git
   cd protocol-to-crf-generator
   ```
2. Install dependencies in a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   pre-commit install
   ```
3. Run the CLI
   ```bash
   python -m protocol_to_crf_generator --help
   ```

## Common Commands

- `pre-commit run --all-files` – format and type-check
- `pytest` – run tests
- `docker compose up` – spin up auxiliary services

## Running Tests

Execute the full suite with coverage:
```bash
pytest -n auto --cov
```
Tests should pass and coverage remain ≥90% as specified in the [test strategy](docs/5_Quality%20&%20Ops/1_Test%20Strategy%20&%20Definition%20of%20Done/test-strategy.md).

## Contributing

Please read the [CONTRIBUTING guide](docs/6_Dev%20Env%20&%20Collaboration/3_Contribution%20Guidelines%20&%20Code-Review%20Checklist/CONTRIBUTING.md) before submitting issues or pull requests.

## Branching & Commit Rules

This project follows a clear Git strategy:

- Use branch names like `feat/<desc>`, `docs/<topic>`, `release/vX.Y.Z`, `hotfix/vX.Y.Z` and `chore/ct-update-<date>`.
- Commits adhere to the [Conventional Commits](https://www.conventionalcommits.org) style.
- Pull requests must target `main` and are squash merged after approval and passing checks.
- Releases are tagged using `vMAJOR.MINOR.PATCH` to trigger the deployment pipeline.

## License

This project is distributed under the [Apache 2.0](LICENSE) license.
