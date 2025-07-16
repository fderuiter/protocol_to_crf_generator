# Risk Register & Mitigation Plan

The following register tracks key project risks derived from the [CDISC CRF Generation Technical Plan](../../CDISC%20CRF%20Generation%20Technical%20Plan_.md). Impact and Probability are scored from 1 (low) to 5 (high). Exposure is calculated as **Impact × Probability**. Severity icons are coded as:

- 🟥 Critical (16–25)
- 🟧 High (10–15)
- 🟨 Medium (5–9)
- 🟩 Low (1–4)

| ID | Risk Description | Impact | Probability | Exposure | Severity | Mitigation Actions | Owner |
| --- | --------------- | :----: | :---------: | :------: | :-----: | ----------------- | ----- |
| R1 | Non‑compliance with 21 CFR Part 11 audit requirements | 5 | 3 | 15 | 🟧 | Implement immutable audit log and CI/CD validation steps as outlined in the Technical Plan | Project Lead |
| R2 | Inaccurate NLP extraction leading to incorrect CRF mappings | 4 | 4 | 16 | 🟥 | Use rule‑based spaCy pipelines with regression corpus; continuously evaluate accuracy metrics | NLP Engineer |
| R3 | Controlled terminology updates break existing mappings | 3 | 4 | 12 | 🟧 | Automate CT update process and regression tests on mapping logic | Project Lead |
| R4 | Security vulnerability in open‑source dependencies | 4 | 3 | 12 | 🟧 | Integrate Bandit and Semgrep scans in CI; apply dependable tooling for upgrades | Tech Lead |
| R5 | Single‑developer bandwidth delays delivery | 3 | 2 | 6 | 🟨 | Prioritize backlog, automate testing, seek community contributions | Project Lead |
| R6 | Data leakage of proprietary protocol content | 5 | 2 | 10 | 🟧 | Enforce least‑privilege access; containerize and isolate storage; audit API usage | Tech Lead |

## Heat‑Map Summary

The table below summarizes the number of risks per severity level.

| Severity | Count |
| -------- | ----- |
| 🟥 Critical | 1 |
| 🟧 High | 3 |
| 🟨 Medium | 1 |
| 🟩 Low | 0 |

