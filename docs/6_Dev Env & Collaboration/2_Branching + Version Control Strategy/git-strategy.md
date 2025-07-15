# Branching & Version Control Strategy

This guide defines how source code is managed in the repository. It expands on the contribution workflow outlined in the [CDISC CRF Generation Technical Plan](../../CDISC%20CRF%20Generation%20Technical%20Plan_.md).

## Branch Types

- **`main`** – the stable trunk. All CI/CD jobs run on every push or pull request targeting this branch. Tagged releases are created from here and trigger the deploy job described in the [CI/CD Blueprint](../3_CICD%20Pipeline%20Blueprint/cicd-blueprint.md).
- **Feature branches** – short‑lived branches for new work. Start from `main` and follow the naming pattern `feat/<description>`.
- **Documentation branches** – for docs‑only changes, use `docs/<topic>`.
- **Release branches** – `release/vX.Y.Z` prepare a new minor or major release when large sets of features are ready.
- **Hotfix branches** – `hotfix/vX.Y.Z` start from the last tag to fix critical issues.
- **Automation branches** – the controlled terminology updater creates `chore/ct-update-<YYYY-MM-DD>` branches automatically as noted in the technical plan.

## Naming Conventions & Commit Messages

All commits follow the **Conventional Commits** specification.

| Type | Purpose |
| --- | --- |
| `feat` | Add a new feature or capability |
| `fix` | Bug fixes and regressions |
| `docs` | Documentation only changes |
| `style` | Formatting, linting, or whitespace changes |
| `refactor` | Code changes that neither fix a bug nor add a feature |
| `test` | Adding or updating tests |
| `chore` | Maintenance tasks such as dependency bumps |

Branches mirror these types. Example: `feat/nlp-pipeline`, `fix/cli-args`, `docs/readme`.

## Pull Request Rules

1. Every change must come through a pull request targeting `main`.
2. Pre‑commit hooks and the full test suite must pass; the CI/CD pipeline enforces this automatically.
3. At least one approval is required. For external contributors a signed CLA and adherence to the [Code of Conduct](../../CDISC%20CRF%20Generation%20Technical%20Plan_.md#113-plan-community-contributions) are mandatory.
4. Squash‑merge is used to keep history linear. The PR title becomes the final commit message following the Conventional Commit style.

## Release Tagging

Releases follow **Semantic Versioning** (`vMAJOR.MINOR.PATCH`). Creating a tag on `main` triggers the deployment job to publish the Python package and Docker image.

```bash
# example
git tag v1.2.0
git push origin v1.2.0
```

Release branches should be merged and tagged once all tests pass and documentation is updated.

## Hotfix Flow

1. Branch from the release tag that requires a patch.
2. Commit the fix on a `hotfix/vX.Y.Z` branch following Conventional Commits.
3. Open a pull request to `main`; once merged, tag the patch release (e.g., `v1.2.1`).

## Visual Overview

```mermaid
gitGraph
   commit tag: "v1.0.0"
   branch feat/my-feature
   commit
   commit
   checkout main
   merge feat/my-feature
   branch release/v1.1.0
   commit
   checkout main
   merge release/v1.1.0
   tag "v1.1.0"
   branch hotfix/v1.1.1
   commit
   checkout main
   merge hotfix/v1.1.1
   tag "v1.1.1"
```

Following this strategy keeps the history clean and ensures that automated workflows described in the technical plan can reliably build, test and deploy the project.
