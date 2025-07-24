# Protocol to CRF Generator – Project Charter

## Purpose & Vision

The **Protocol to CRF Generator** will let a single developer instantly convert clinical study protocols into CDISC‑compliant eCRF artefacts (ODM‑XML/JSON and review‑ready Markdown) using only open‑source tooling.  By automating extraction, mapping and validation, the project aims to cut study‑startup “CRF build” effort from days to minutes, even for resource‑constrained teams.  A lightweight CLI/API with optional UI will ensure the solution remains portable, reproducible and free to adopt.

## Business Objectives (SMART)

| # | Objective                                                                    | KPI                   | Target      | Owner        | Due        |
| - | ---------------------------------------------------------------------------- | --------------------- | ----------- | ------------ | ---------- |
| 1 | Ship MVP supporting Demographics & Vital Signs via CLI                       | Public Git tag v0.1.0 | 31‑Dec‑2025 | Project Lead | 2025‑12‑31 |
| 2 | Achieve ≥90 % automatic variable‑mapping accuracy on regression corpus       | Accuracy %            | ≥90 %       | Project Lead | 2026‑03‑31 |
| 3 | Reduce manual CRF build effort per protocol from 8 h → ≤1 h (solo benchmark) | Hours/protocol        | ≤1 h        | Project Lead | 2026‑06‑30 |
| 4 | Publish open‑source repo with ≥100 GitHub stars                              | Stars                 | 100         | Project Lead | 2026‑12‑31 |

## Scope

### In‑Scope

* DOCX/PDF ingestion → CDASH v2.1 mapping → ODM‑XML/JSON & Markdown output
* Command‑line interface and REST micro‑service
* GitHub Actions CI with schema validation & unit tests
* MIT‑licensed codebase and docs
* Prompt iteration and model evaluation using **GitHub Models**

### Out‑of‑Scope

* Part 11 validated hosting or paid support
* Direct EDC database build/upload
* Statistical analysis & SDTM conversion
* Multi‑user role‑based access control

## Key Deliverables & High‑Level Milestones

| Milestone                    | Target Date | Description                         |
| ---------------------------- | ----------- | ----------------------------------- |
| Charter approved             | 31‑Jul‑2025 | Self‑sign‑off & repo initialization |
| MVP v0.1.0                   | 31‑Dec‑2025 | CLI pipeline + two domains          |
| API release v0.5.0           | 31‑Mar‑2026 | FastAPI service + CT auto‑update    |
| Core domains complete v0.9.0 | 30‑Jun‑2026 | AE, MH, DS, EX support              |
| GA v1.0.0                    | 31‑Dec‑2026 | Public release & docs               |

## Success Metrics (KPIs)

* **Turn‑around time:** Protocol → validated CRF artefacts ≤15 minutes on laptop
* **Mapping accuracy:** ≥90 % across regression corpus
* **Defect density:** <0.5/blocking issue per release
* **Community engagement:** ≥5 external pull requests merged in 2026

## Assumptions & Constraints

**Assumptions**

* Developer has \~10 non‑billable hrs/week
* Open‑source libraries & free‑tier CI/CD are sufficient

**Constraints**

* Solo capacity may extend timelines
* Must stay within \$0 cash budget
* Compliance limited to “best‑effort” alignment with 21 CFR Part 11 (no formal validation)

## Stakeholders & Roles (RACI)

| Stakeholder           | R     | A     | C     | I     |
| --------------------- | ----- | ----- | ----- | ----- |
| Project Lead (You)    | **R** | **A** |       |       |
| Open‑Source Community |       |       | **C** | **I** |

## Budget / Resourcing Snapshot

| Resource                 | Basis                        | Cash Cost |
| ------------------------ | ---------------------------- | --------- |
| Developer time           | 1 contributor, \~10 h/week   | \$0       |
| Tooling & Infrastructure | GitHub, Docker, free‑tier CI | \$0       |
| **Total**                |                              | **\$0**   |

## Approval & Revision History

| Version | Date        | Author       | Notes                            | Approver     |
| ------- | ----------- | ------------ | -------------------------------- | ------------ |
| 1.0     | 15‑Jul‑2025 | Project Lead | Updated for solo/no‑budget scope | Project Lead |
