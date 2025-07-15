# Contributing

Thank you for your interest in improving Protocol to CRF Generator! This project follows the workflow described in the documentation.

## Workflow

1. **Fork** the repository and create your branch from `main` using our naming conventions (`feat/<desc>`, `docs/<topic>`, `release/vX.Y.Z`, `hotfix/vX.Y.Z`, `chore/ct-update-<date>`).
2. Install the development environment following the quick start in the [README](README.md) and run `pre-commit install`.
3. Ensure `pre-commit run --all-files` and `pytest` succeed before pushing.
4. Push your branch and open a pull request targeting `main`.
5. External contributors must sign the CLA using the automated workflow.
6. At least one maintainer must approve and the CI pipeline must pass before your PR can be squash merged.

Use this template when opening a pull request:

```markdown
## Summary
Explain the change briefly.

## Testing
Describe the commands you ran, e.g. `pre-commit run --all-files` and `pytest`.
```

For more detail see [docs/6_Dev Env & Collaboration/3_Contribution Guidelines & Code-Review Checklist/CONTRIBUTING.md](docs/6_Dev%20Env%20&%20Collaboration/3_Contribution%20Guidelines%20&%20Code-Review%20Checklist/CONTRIBUTING.md).
