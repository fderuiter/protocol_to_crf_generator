# Contribution Guidelines & Code-Review Checklist

This guide explains how to participate in the Protocol to CRF Generator project. It summarises the workflow defined in the [CDISC CRF Generation Technical Plan](../../CDISC%20CRF%20Generation%20Technical%20Plan_.md) and the companion [Git Strategy](../2_Branching%20+%20Version%20Control%20Strategy/git-strategy.md).

## Filing Issues

1. Search the existing issues before creating a new one.
2. Use a clear title and provide steps to reproduce the problem or the motivation for a feature request.
3. Be respectful and follow our [Code of Conduct](../../CODE_OF_CONDUCT.md).

## Getting Started

1. **Fork** the repository and create your branch from `main` using the patterns in the Git Strategy (`feat/`, `fix/`, `docs/`, `chore/` …).
2. Install the development environment using the [README quick‑start](../1_Repository%20README%20%26%20Quick-Start%20Guide/README.md).
3. Run `pre-commit install` and ensure `pre-commit run --all-files` and `pytest` succeed before pushing.

## Pull Requests

- Follow the Conventional Commit style for your commits.
- Push your branch and open a pull request targeting `main`.
- External contributors must sign the CLA via the GitHub workflow before the PR can be merged.
- The CI pipeline must pass and at least one maintainer must approve.

Use this template in the PR description:

```markdown
## Summary
- explain the change briefly

## Testing
- `pre-commit run --all-files`
- `pytest`
```

## Code-Review Checklist

1. Do all tests and pre-commit checks pass?
2. Is new functionality covered by tests with adequate assertions?
3. Are public functions and modules documented with clear docstrings?
4. Is the code easy to read and logically structured?
5. Are errors handled using exceptions and logged appropriately?
6. Have dependencies and licenses been evaluated for compliance?
7. Do names and formatting follow the [style guide](../../5_Quality%20%26%20Ops/2_Coding%20Standards%20+%20Style%20Guide/style-guide-python.md)?
8. Is user-facing documentation updated to reflect the change?
9. Is backward compatibility preserved or explained if not?
10. Have potential security or privacy issues been considered?

Thank you for helping improve the project!
