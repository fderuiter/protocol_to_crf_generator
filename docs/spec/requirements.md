# Project Protocol to CRF Generator – Requirements

## 1. Front-matter

* **Document status:** Draft v0.1 (2025-07-16)
* **Authors & reviewers:** Frederick de Ruiter, Maria, Dr. Chen, David, TBD QA/Validation Lead, TBD Regulatory & Compliance SME, Open-Source Contributors

## 2. Purpose & Scope

The Protocol to CRF Generator converts clinical study protocols into CDISC-compliant Case Report Form artefacts. It provides a CLI, REST API and optional SPA to automate extraction, mapping and validation for Demographics and Vital Signs initially, expanding to additional domains. The system operates as MIT-licensed open-source software with Docker-based deployment and GitHub-driven CI/CD.

## 3. Stakeholders & RACI (summary table)

| Stakeholder | R | A | C | I |
| --- | --- | --- | --- | --- |
| Frederick de Ruiter (Product Owner / Lead Developer) | **R** | **A** | | |
| Maria (Data Manager) | | | **C** | **I** |
| Dr. Chen (Study Designer) | | | **C** | **I** |
| David (CRO Technical Lead) | | | **C** | **I** |
| TBD QA / Validation Lead | | | **C** | **I** |
| TBD Regulatory & Compliance SME | | | **C** | |
| Open-Source Contributors | | | | **I** |

## 4. Functional Requirements

FR-1 The system shall ingest DOCX protocols up to 50 MB via `POST /ingest`, queue a job and return `202` with a job ID. (source: functional_spec_protocol_ingestion.md)
FR-2 The system shall reject unsupported file types with HTTP 400 and message "Unsupported format". (source: functional_spec_protocol_ingestion.md)
FR-3 The ingestion pipeline shall tag each sentence with its parent section. (source: functional_spec_protocol_ingestion.md)
FR-4 The ingestion pipeline shall output tables as normalised CSV with flattened headers. (source: functional_spec_protocol_ingestion.md)
FR-5 The NLP pipeline shall extract visit, assessment and timing entities with confidence ≥0.8. (source: functional_spec_protocol_ingestion.md)
FR-6 The system shall record provenance for every extracted entity including page number, table ID and cell coordinates. (source: functional_spec_protocol_ingestion.md)
FR-7 Validated StudyProtocolIR JSON shall be stored with SHA‑256 hash and status `ready`. (source: functional_spec_protocol_ingestion.md)
FR-8 Upon ingestion completion a manifest shall list each file name, SHA‑256 hash and timestamp. (source: functional_spec_protocol_ingestion.md)
FR-9 The system shall emit structured JSON logs with level and trace ID for all ingestion steps. (source: functional_spec_protocol_ingestion.md)
FR-10 Ingestion jobs shall include metrics counts, confidence distribution and extraction recall estimate. (source: functional_spec_protocol_ingestion.md)
FR-11 The solution shall provide both a command-line interface and REST API. (source: project_charter.md)
FR-12 The system shall output CDASH v2.1 mapped ODM‑XML, ODM‑JSON and Markdown files. (source: project_charter.md)
FR-13 Docker images and CLI packages shall be built and published on tagged releases. (source: cicd-blueprint.md)
FR-14 The system shall maintain an immutable audit log recording who, what, when and why for all changes. (source: technical-plan.md)
FR-15 All generated artefacts shall pass ODM 2.0 schema validation in CI. (source: cicd-blueprint.md)
FR-16 A weekly GitHub Action shall check for new Controlled Terminology releases and open a PR with updates. (source: z_feature_list.md)
FR-17 The system shall provide optional SPA for protocol upload and artifact download. (source: z_feature_list.md)

## 5. Non-Functional Requirements

NFR-1 End-to-end CRF build for a 100-page DOCX must complete with median ≤5 min and P95 ≤7 min on an 8 vCPU, 16 GB RAM node. (source: nfr_checklist.md)
NFR-2 API latency for lightweight operations must be ≤200 ms P95 under 500 concurrent users. (source: nfr_checklist.md)
NFR-3 Memory usage per worker must stay ≤1 GB during processing. (source: nfr_checklist.md)
NFR-4 CLI batch mode shall process ≥20 protocols per hour on a single container. (source: nfr_checklist.md)
NFR-5 REST workers must autoscale to keep CPU utilisation ≤70 % at 2× peak load, demonstrating linear throughput for up to 20 parallel jobs with <15 % P95 latency growth. (source: nfr_checklist.md)
NFR-6 Celery/RabbitMQ queue backlog for 100 job burst must clear within 5 min; queued jobs remain ≤10 for >95 % of test duration. (source: nfr_checklist.md)
NFR-7 Controlled Terminology lookup service shall respond <50 ms P95 for ≈75k rows. (source: nfr_checklist.md)
NFR-8 Service uptime must be ≥99.9 % per calendar month. (source: nfr_checklist.md)
NFR-9 Disaster recovery plan must achieve RTO ≤4 h and RPO ≤15 min. (source: nfr_checklist.md)
NFR-10 Encryption in transit and at rest shall achieve Qualys grade A+ with zero weak ciphers. (source: nfr_checklist.md)
NFR-11 All privileged endpoints must enforce RBAC with ≥95 % unit test coverage on auth checks. (source: nfr_checklist.md)
NFR-12 100 % create/update/delete events must be written to the audit trail within 5 s and validated nightly. (source: nfr_checklist.md)
NFR-13 Zero critical or high CVEs allowed in weekly Bandit and Semgrep scans. (source: nfr_checklist.md)
NFR-14 Hash manifest must exist for all generated files. (source: nfr_checklist.md)
NFR-15 ODM artefacts must pass XSD/JSON schema validation. (source: nfr_checklist.md)
NFR-16 CDISC CORE business-rule checks must report 0 “Error” grade findings. (source: nfr_checklist.md)
NFR-17 Optional SPA must pass axe-core scan with zero critical or serious issues and provide keyboard navigation. (source: nfr_checklist.md)
NFR-18 API and background tasks shall emit JSON logs with correlation IDs; ingestion-to-generation trace coverage ≥95 %. (source: nfr_checklist.md)
NFR-19 Prometheus metrics shall alert when 99th percentile latency exceeds 3 s for over 10 min. (source: nfr_checklist.md)
NFR-20 UTF‑8 corpus tests must show zero encoding errors; PO‑file translations must reach ≥95 % coverage for EN and JA. (source: nfr_checklist.md)
NFR-21 CI must fail if coverage <90 %, ruff violations exist or high-severity SAST issues appear. (source: nfr_checklist.md)
NFR-22 New CT package PR must be merged within 30 days of release. (source: nfr_checklist.md)
NFR-23 Mean Time To Restore for critical defects shall be ≤2 working days. (source: nfr_checklist.md)
NFR-24 New contributor onboarding guide shall yield PR first response within 1 day. (source: nfr_checklist.md)
NFR-25 Pre-commit hooks must run ruff and mypy --strict before each commit. (source: style-guide-python.md)
NFR-26 All code must include Google-style docstrings and pass mypy --strict. (source: style-guide-python.md)
NFR-27 Docker containerisation is mandatory for all deployments. (source: technical-plan.md)
NFR-28 The project license must remain Apache 2.0 and dependencies must use compatible licenses recorded in the inventory. (source: third-party-inventory.md)
NFR-29 The CI/CD pipeline must execute lint, type check, unit tests, security scans, schema validation, package and deploy on tagged releases. (source: cicd-blueprint.md)
NFR-30 Deployment and rollback procedures must follow the runbook with health checks via `/health`, log inspection and worker status. (source: runbook-deploy-rollback.md)

## 6. System Constraints & Dependencies

* Architecture follows a containerised modular service with FastAPI gateway, NLP and mapping workers, validation service and PostgreSQL/SQlite databases. (source: adr-0001-system-architecture.md)
* The project operates on a $0 cash budget and solo developer capacity (~10 h/week). (source: project_charter.md)
* Compliance with 21 CFR Part 11 is “best‑effort” without formal validation hosting. (source: project_charter.md)
* Docker is required across local, CI and production environments. (source: technical-plan.md)
* All third-party libraries must be recorded with license information in the inventory. (source: third-party-inventory.md)
* Development languages and frameworks are limited to Python 3.11, FastAPI, spaCy, Pydantic and related stack. (source: z_feature_list.md)
* Risk mitigations include immutable audit log, regression corpus for NLP accuracy and automated CT updates. (source: risk-register.md)

## 7. Acceptance Criteria / Verification

* Unit, integration and regression tests run via GitHub Actions with ≥90 % coverage. (source: test-strategy.md)
* CI must report no Critical defects from Bandit or Semgrep. (source: test-strategy.md)
* Documentation and changelog updates are required before merging. (source: test-strategy.md)
* Deployment verified by `/health` endpoint, log checks and worker status. (source: runbook-deploy-rollback.md)
* NFR metrics validated with Locust, k6, StatusCake, Prometheus and nightly hash-chain verification. (source: nfr_checklist.md)

## 8. Open Questions & Assumptions

* PDF table accuracy threshold and handling of “best-effort” imports remain undecided. (source: functional_spec_protocol_ingestion.md)
* Criteria for upgrading from rule-based to statistical NER are not finalised. (source: functional_spec_protocol_ingestion.md)
* Storage layer choice between Postgres JSONB and object storage is open. (source: functional_spec_protocol_ingestion.md)
* Concurrency limits depend on future ops capacity planning. (source: functional_spec_protocol_ingestion.md)
* Timeline for multilingual support beyond English is unclear. (source: functional_spec_protocol_ingestion.md)
* Assumes developer has ~10 h/week and free-tier tooling suffices. (source: project_charter.md)

## 9. Appendices (links back to source docs)

* [Project Charter](1_Vision%20&%20Scope/1_Project%20Charter%20+%20Vision%20Statement/project_charter.md)
* [Stakeholder RACI](1_Vision%20&%20Scope/Stakeholder%20&%20RACI%20list/stakeholders-raci.md)
* [Functional Spec](2_Requirements/1_Functional%20Spec%20or%20User-Story%20Backlog/functional_spec_protocol_ingestion.md)
* [Feature List](2_Requirements/1_Functional%20Spec%20or%20User-Story%20Backlog/z_feature_list.md)
* [NFR Checklist](2_Requirements/2_Non-Functional%20Requirements%20(NFR)%20Sheet/nfr_checklist.md)
* [Architecture ADR](3_Architecture%20&%20Design/1_High-Level%20Architecture%20Diagram%20&%20ADRs/adr-0001-system-architecture.md)
* [Roadmap](4_Planning%20&%20Risk/1_Roadmap/roadmap-next-12-months.md)
* [Risk Register](4_Planning%20&%20Risk/2_Risk%20Register%20&%20Mitigation%20Plan/risk-register.md)
* [Test Strategy](5_Quality%20&%20Ops/1_Test%20Strategy%20&%20Definition%20of%20Done/test-strategy.md)
* [Coding Standards](5_Quality%20&%20Ops/2_Coding%20Standards%20+%20Style%20Guide/style-guide-python.md)
* [CI/CD Blueprint](5_Quality%20&%20Ops/3_CICD%20Pipeline%20Blueprint/cicd-blueprint.md)
* [Deployment Runbook](5_Quality%20&%20Ops/4_Deployment%20&%20Rollback%20Runbook/runbook-deploy-rollback.md)
* [Communication Plan](6_Dev%20Env%20&%20Collaboration/4_Communication%20&%20Meeting%20Cadence%20Plan/communication-plan.md)
* [Third-Party Inventory](7_Governance%20&%20Compliance/1_License%20&%20Third-Party%20Software%20Inventory/third-party-inventory.md)
* [Threat Model](7_Governance%20&%20Compliance/2_Security%20&%20Privacy%20Threat%20Model/threat-model.md)
* [Technical Plan](technical-plan.md)
