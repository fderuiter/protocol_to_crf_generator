# Protocol to CRF Generator

[![CI](https://github.com/fderuiter/protocol_to_crf_generator/actions/workflows/main.yml/badge.svg)](https://github.com/fderuiter/protocol_to_crf_generator/actions/workflows/main.yml)
[![Docs](https://github.com/fderuiter/protocol_to_crf_generator/actions/workflows/docs.yml/badge.svg)](https://github.com/fderuiter/protocol_to_crf_generator/actions/workflows/docs.yml)
[![CLA](https://github.com/fderuiter/protocol_to_crf_generator/actions/workflows/cla.yml/badge.svg)](https://github.com/fderuiter/protocol_to_crf_generator/actions/workflows/cla.yml)
[![CT Update](https://github.com/fderuiter/protocol_to_crf_generator/actions/workflows/ct-update.yml/badge.svg)](https://github.com/fderuiter/protocol_to_crf_generator/actions/workflows/ct-update.yml)
![License](https://img.shields.io/badge/license-Apache%202.0-blue)

A toolchain that converts clinical study protocols into CDISC‑compliant Case Report Form artefacts. See the [technical plan](docs/spec/technical-plan.md) for the full architecture and design rationale.

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
   pip install -e .
   pre-commit install
   ```

   Running `pre-commit install` enables automatic formatting, type and
   security checks before each commit.

3. Run the CLI

   ```bash
   python -m protocol_to_crf_generator --help
   ```

## Running via Docker

Build and start the API service:

```bash
docker build -t protocol-to-crf .
docker run -p 8443:8443 -v $(pwd)/deploy/certs:/certs:ro \
  --user 1000:1000 protocol-to-crf \
  uvicorn protocol_to_crf_generator.api.main:app \
  --host 0.0.0.0 --port 8443 \
  --ssl-keyfile /certs/server.key --ssl-certfile /certs/server.crt
```

See [TLS Configuration](docs/ops/tls-setup.md) for generating the certificate bundle.

Alternatively use Docker Compose which starts auxiliary services:

```bash
docker compose -f deploy/docker-compose.yml up --build
```

The API is then available at `https://localhost:8443`.

## Configuration

The rate limiter defaults to `5/minute` per IP address. Override this by setting
the environment variable `RATE_LIMIT` before starting the API:

```bash
export RATE_LIMIT=10/minute
docker compose -f deploy/docker-compose.yml up --build
```

## CLI ingest example

With the API running, upload a protocol document:

```bash
python -m protocol_to_crf_generator ingest sample.docx
```

The command prints the job identifier returned by `/ingest`.

## Common Commands

- `pre-commit run --all-files` – lint, type-check and scan for security issues
- `pytest` – run tests
- `docker compose up` – spin up auxiliary services

## Running Tests

Execute the full suite with coverage:

```bash
pytest -n auto --cov
```

Tests should pass and coverage remain ≥90% as specified in the [test strategy](docs/spec/5_Quality%20&%20Ops/1_Test%20Strategy%20&%20Definition%20of%20Done/test-strategy.md).

## Contributing

Please read the [CONTRIBUTING guide](CONTRIBUTING.md) before submitting issues or pull requests.

## Branching & Commit Rules

This project follows a clear Git strategy:

- Use branch names like `feat/<desc>`, `docs/<topic>`, `release/vX.Y.Z`, `hotfix/vX.Y.Z` and `chore/ct-update-<date>`.
- Commits adhere to the [Conventional Commits](https://www.conventionalcommits.org) style.
- Pull requests must target `main` and are squash merged after approval and passing checks.
- Releases are tagged using `vMAJOR.MINOR.PATCH` to trigger the deployment pipeline.

## Communication

We use GitHub Issues for tracking tasks and decisions, and pull requests for
code review. Meeting notes and important discussions should be summarised in
the relevant issue or PR to maintain a canonical record. See the [Communication
Plan](docs/spec/6_Dev%20Env%20&%20Collaboration/4_Communication%20&%20Meeting%20Cadence%20Plan/communication-plan.md)
for details.

## License

This project is distributed under the [Apache 2.0](LICENSE) license.
