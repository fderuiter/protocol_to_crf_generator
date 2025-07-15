# Non‑Functional Requirements Checklist – CRF Generator (Comprehensive)

This expanded checklist derives directly from the **CDISC CRF Generation Technical Plan** and elaborates each non‑functional requirement (NFR) with concrete, testable targets that align with 21 CFR Part 11, CDISC best‑practice guidance, and modern DevOps principles.

## Performance

| Requirement                                                                                                                                                                         | Measurable Target / Metric                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Pipeline throughput** – end‑to‑end CRF build (ingestion → NLP → mapping → validation → artefact generation) for a 100‑page DOCX protocol must be fast enough for interactive use. | **Median ≤ 5 min; P95 ≤ 7 min** on reference node (8 vCPU, 16 GB RAM). |
| **API latency** for lightweight operations (e.g., `GET /health`)                                                                                                                    | **≤ 200 ms P95** under 500 concurrent users (Locust test).             |
| **Memory footprint** – steady‑state RSS per worker                                                                                                                                  | **≤ 1 GB** while processing the reference workload.                    |
| **Batch throughput** – CLI batch mode                                                                                                                                               | **≥ 20 protocols / hour** on a single container.                       |

## Scalability

| Requirement                                                                                                                                                                                                       | Measurable Target / Metric                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Horizontal scaling** – REST workers are stateless and must autoscale to maintain ≤ 70 % CPU utilisation at 2 × planned peak load, leveraging Kubernetes HPA and containerisation mandates fileciteturn3file2 | Demonstrated linear throughput for up to **20 parallel jobs** with < 15 % P95 latency growth per +5 workers.                             |
| **Task‑queue depth**                                                                                                                                                                                              | During a 100‑job burst the Celery/RabbitMQ queue backlog **empties within 5 min**; maximum queued jobs ≤ 10 for > 95 % of test duration. |
| **Dataset scaling** – Controlled Terminology SQLite                                                                                                                                                               | Lookup service returns **< 50 ms P95** for term queries across full CT set (≈ 75 k rows) fileciteturn3file13                          |

## Availability

| Requirement                                                                        | Measurable Target / Metric                                                                                       |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Service uptime (SaaS)**                                                          | **≥ 99.9 % per calendar month** (three‑nines) measured by external synthetic probes                              |
| **Disaster Recovery** – documented DRP with backup strategy fileciteturn3file16 | **RTO ≤ 4 h; RPO ≤ 15 min** verified in quarterly fail‑over exercise                                             |
| **Zero‑data‑loss restore**                                                         | Full restoration from last snapshot passes schema‑validate‑artefacts CI job with 0 errors fileciteturn3file17 |

## Security

| Requirement                                                                                                             | Measurable Target / Metric                                                           |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Encryption in transit & at rest** (TLS 1.2+, AES‑256) fileciteturn3file0                                           | Qualys scan grade **A+**; 0 weak‑cipher findings                                     |
| **Role‑Based Access Control (RBAC)** integrated with external IdP fileciteturn3file0                                 | 100 % of privileged endpoints gated; ≥ 95 % unit‑test coverage on auth checks        |
| **Immutable audit trail** – who/what/when/why for all create/update/delete operations fileciteturn3file0turn3file19 | 100 % events written within 5 s; tamper‑evident SHA‑256 chain validated nightly      |
| **Vulnerability management**                                                                                            | **Zero critical / high CVEs** in weekly Bandit + Semgrep scans fileciteturn3file7 |
| **Electronic‑signature readiness** – cryptographic hashes for all artefacts fileciteturn3file0                       | Hash manifest present for 100 % generated files                                      |

## Compliance

| Requirement                                                                                   | Measurable Target / Metric                               |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **21 CFR Part 11 traceability** – RTM from URS → FRS → Test fileciteturn3file0turn3file19 | 100 % regulatory clauses mapped; evidence stored in Git  |
| **System validation** – IQ/OQ/PQ ready fileciteturn3file2                                  | Formal scripts execute successfully in validated sandbox |
| **Schema conformance** – ODM‑XML & JSON fileciteturn3file10                                | 100 % artefacts pass XSD/JSON‑Schema validation in CI    |
| **Business‑rule conformance** – CDISC CORE rules fileciteturn3file17                       | 0 “Error” grade findings per run                         |

## Accessibility

| Requirement                                                      | Measurable Target / Metric                                                               |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **WCAG 2.1 AA** adherence for optional SPA fileciteturn3file8 | axe‑core scan: **0 critical / 0 serious issues** per release                             |
| **Keyboard navigation & focus order**                            | All interactive elements reachable; tab‑sequence logical; verified via cypress‑axe tests |

## Observability

| Requirement                                                                      | Measurable Target / Metric                                                                                     |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Structured logging & tracing** fileciteturn3file17                          | 100 % API and background tasks emit JSON logs w/ correlation IDs; ingestion → generation trace coverage ≥ 95 % |
| **Metrics (RED + 4 golden signals)**                                             | Prometheus counters exported; SLO alert when 99th‑latency > 3 s for > 10 min                                   |
| **Consolidated validation log** – machine + human formats fileciteturn3file17 | Delivered for 100 % jobs; JSON schema validated                                                                |

## Internationalization

| Requirement                                     | Measurable Target / Metric                                                     |
| ----------------------------------------------- | ------------------------------------------------------------------------------ |
| **UTF‑8 fidelity** end‑to‑end                   | 0 encoding errors in nightly unicode corpus test                               |
| **Locale coverage** – EN & JA day‑1; extendable | PO‑file translation coverage **≥ 95 %**; date/number formats localised via ICU |

## Maintainability

| Requirement                                                                                | Measurable Target / Metric                                                                 |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **Automated quality gates** – lint, coverage, security fileciteturn3file7turn3file18   | CI fails if **coverage < 90 %**, ruff violations > 0, or high‑severity SAST issues present |
| **Release hygiene** – semantic versioning & quarterly CT update bot fileciteturn3file15 | New CT package PR merged within **30 days** of release                                     |
| **Mean Time To Restore (MTTR)** for critical defects                                       | **≤ 2 working days** (GitHub issue tracking)                                               |
| **Contributor friendliness** – docs & CLA fileciteturn3file16                           | Onboarding guide passes newcomer survey; PR first‑response time ≤ 1 day                    |

---

### Verification Methods

Performance & scalability validated with **Locust** and **k6** load tests run in pre‑prod. Uptime, RTO/RPO, and DR drills monitored via **StatusCake** and quarterly region fail‑over. Security requirements enforced by **Bandit**, **Semgrep**, and weekly **OWASP ZAP** scans; audit‑trail integrity checked by nightly hash‑chain verifier. Compliance evidence (RTM, schema, CORE rules) collected automatically in the **GitHub Actions** CI pipeline; artefacts stored as immutable build attachments. Accessibility tested with **axe‑core** plus manual keyboard audit. Observability SLOs monitored by **Prometheus + Grafana**; alerting via PagerDuty. Internationalization tests use ICU‑based test harness. Maintainability metrics tracked by **Codecov**, ruff, and GitHub Insights.
