# Test Strategy & Definition of Done

This strategy outlines how quality will be assured throughout development of the Protocol to CRF Generator. It is based on the approaches described in the [CDISC CRF Generation Technical Plan](../../CDISC%20CRF%20Generation%20Technical%20Plan_.md).

## Objectives & Scope
- Validate that all features work as specified and meet 21 CFR Part 11 compliance requirements.
- Maintain a high level of test automation so regressions are caught before release.
- Cover functional logic, user workflows (CLI and REST API), and non‑functional attributes such as performance and security.

## Testing Pyramid Targets
| Layer | Goal | Tools |
| --- | --- | --- |
| **Unit Tests** | Exercise individual functions and classes in isolation. | `pytest`, `pytest-mock` |
| **Integration Tests** | Verify interactions among modules (e.g., parser → NLP → mapping). | `pytest`, Docker compose services |
| **Regression Suite** | Run end‑to‑end pipelines on the curated protocol corpus. | `pytest`, golden files |
| **Manual / Exploratory** | Sanity checks of the CLI, REST API and optional Web UI. | Developer checklist |

A minimum of **90% code coverage** will be enforced via `pytest-cov`.

## Tooling & Environments
- **Continuous Integration:** GitHub Actions runs the full test suite on every pull request.
- **Static Analysis:** `ruff` for linting and formatting, `bandit` and `semgrep` for security scanning.
- **Coverage Reporting:** `coverage.py` with an enforced threshold. Fail the pipeline if below target.
- **Container Tests:** Docker images are built in CI and integration tests run inside containers to mirror production.

## Non-Functional Testing
- **Performance:** Measure execution time on large protocols during regression tests; flag significant regressions.
- **Security:** SAST tools run in CI, plus dependency vulnerability checks.
- **Compliance:** Validation reports are generated to show audit-log integrity and controlled-terminology consistency.
- **Accessibility (Web UI):** Axe-core checks incorporated if UI is enabled.

## Defect Severity Definitions
| Severity | Description | Example Impact |
| --- | --- | --- |
| **Blocker** | Prevents further testing or use of the system. | CI pipeline fails to run tests. |
| **Critical** | Causes incorrect CRF output or data corruption. | Wrong ODM mappings produced. |
| **Major** | Functional defect with no workaround. | API endpoint returns 500 error. |
| **Minor** | User-facing issue with workaround. | CLI progress messages misaligned. |
| **Trivial** | Cosmetic or documentation issue. | Typos in help text. |

## Definition of Done Checklist
- [ ] All unit and integration tests pass with coverage ≥90%.
- [ ] Linting, formatting and security scans report no errors of severity "Critical" or higher.
- [ ] Documentation updated for new or changed features.
- [ ] CI pipeline completes successfully including Docker image build.
- [ ] Peer review approvals obtained.

