# Documentation To-Do List – Protocol to CRF Generator

This file tracks documentation tasks for the project. Each entry lists the document, location under `docs/`, and key items that must be covered. Because this is a solo project you are responsible for drafting, review and approval.

- [x] **Project Charter / Vision Statement**
  - Path: `docs/1_Vision & Scope/1_Project Charter + Vision Statement/project_charter.md`
  - Include sections: Purpose & Vision, SMART business objectives table, Scope (in/out), Deliverables/Milestones timeline, Success KPIs, Assumptions & Constraints, RACI table, Budget snapshot, Approval & Revision history.
  - Verify document stays under two rendered pages.

- [x] **Stakeholder Register & RACI List**
  - Path: `docs/1_Vision & Scope/Stakeholder & RACI list/stakeholders-raci.md`
  - Table columns: Role, Name, Responsibility, RACI, Preferred Channel, Frequency of Updates.
  - Add "Escalation Paths" paragraph on conflict resolution.
  - Update list whenever new stakeholders are identified.

- [x] **Functional Specification / User-Story Backlog**
  - Path: `docs/2_Requirements/1_Functional Spec or User-Story Backlog/functional-spec-{feature}.md`
  - Draft one spec per feature area (start with `functional_spec_protocol_ingestion.md`).
  - Epics: Document Ingestion, Table & Section Detection, NLP Entity Extraction, Canonical IR Persistence, Operational Logging & Error Handling.
  - For each story include "As a..." wording plus Gherkin acceptance criteria. Link to NFR checklist where applicable.
  - Capture open questions and external dependencies.

- [x] **Non-Functional Requirements (NFR) Sheet**
  - Path: `docs/2_Requirements/2_Non-Functional Requirements (NFR) Sheet/nfr-checklist.md`
  - Cover categories: Performance, Scalability, Availability, Security, Compliance, Accessibility, Observability, Internationalization, Maintainability.
  - Provide measurable targets and note how verification will occur.

- [x] **High-Level Architecture ADR**
  - Path: `docs/3_Architecture & Design/1_High-Level Architecture Diagram & ADRs/adr-0001-system-architecture.md`
  - Follow MADR 2.0 format. Document decision context, considered options, decision outcome and consequences.
  - PlantUML diagram should show services: CLI Tool, FastAPI Gateway, NLP & Extraction svc, Mapping/Generation svc, Validation svc, SPA Web UI, Terminology DB, Audit Log DB, CI/CD pipeline, and integrations with CDISC repos and EDC/CTMS.

- [x] **Data Model / ER Diagram**
  - Path: `docs/3_Architecture & Design/2_Data Model+ERD/er-models/er-model-{domain}.md`
  - Files exist for AE, DM, EX, VS, CM, DS and MH domains.
  - Each includes entity tables with PK/FK attributes and a PlantUML ER diagram block.

- [x] **API Contract & Versioning Policy**
  - Path: `docs/3_Architecture & Design/3_API Contract & Versioning Policy/api-contract-{service}.md`
  - OpenAPI 3.1 stubs exist for services: `fastapi-gateway`, `cli-wrapper`, `nlp-extraction`, `mapping-generation`, `validation`.
  - Each defines one CRUD path, an ErrorObject schema and `x-versioning-policy` with a Mermaid timeline.

- [x] **Roadmap / Milestone Plan**
  - Path: `docs/4_Planning & Risk/1_Roadmap/roadmap-next-12-months.md`
  - Build a table showing epics across the next four quarters with ✅/⚪ indicators and a narrative explaining dependencies.

- [x] **Risk Register & Mitigation Plan**
  - Path: `docs/4_Planning & Risk/2_Risk Register & Mitigation Plan/risk-register.md`
  - List project risks with Impact, Probability, Exposure (auto-computed) and emoji-coded severity. Include mitigation actions and owner.
  - Summarize counts per risk level in a heat-map section.

- [x] **Test Strategy & Definition of Done**
  - Path: `docs/5_Quality & Ops/1_Test Strategy & Definition of Done/test-strategy.md`
  - Cover objectives & scope, test pyramid targets, tooling/environments, non-functional tests, defect severity definitions and a DoD checklist.

- [x] **Coding Standards & Style Guide**
  - Path: `docs/5_Quality & Ops/2_Coding Standards + Style Guide/style-guide-python.md`
  - Focus on Python. Document formatting rules, naming, error handling, docstrings, module layout, snippet examples and pre-commit configuration.

- [x] **CI/CD Pipeline Blueprint**
  - Path: `docs/5_Quality & Ops/3_CICD Pipeline Blueprint/cicd-blueprint.md`
  - Describe trigger flow, build steps, test stages, security/license scans, artifact handling, deployment strategy, rollback hooks and notifications. Include a Mermaid flowchart.

  - [x] **Deployment & Rollback Runbook**
  - Path: `docs/5_Quality & Ops/4_Deployment & Rollback Runbook/runbook-deploy-rollback.md`
  - Detail preconditions, numbered deploy steps, health checks, rollback procedure and contact matrix.

- [x] **Repository README & Quick-Start**
  - Path: `docs/6_Dev Env & Collaboration/1_Repository README & Quick-Start Guide/README.md`
  - Expand root `README.md` with badges, prerequisites, three-step setup, common commands, test instructions, how to contribute and license reference.

- [x] **Branching / Version Control Strategy**
  - Path: `docs/6_Dev Env & Collaboration/2_Branching + Version Control Strategy/git-strategy.md`
  - Describe branch types, naming conventions, PR rules, release tagging, hotfix flow with Mermaid diagram and Conventional Commit table.

- [x] **Contribution Guidelines & Code-Review Checklist**
  - Path: `docs/6_Dev Env & Collaboration/3_Contribution Guidelines & Code-Review Checklist/CONTRIBUTING.md`
  - Explain how to file issues, branch naming pattern, include PR template, 10-question code review checklist and link to Code of Conduct.

- [x] **Communication & Meeting Cadence Plan**
  - Path: `docs/6_Dev Env & Collaboration/4_Communication & Meeting Cadence Plan/communication-plan.md`
  - Provide a ceremonies table (frequency, duration, participants, tool). Add guidelines for async updates and reference decision logging via ADRs.

- [x] **License & Third-Party Software Inventory**
  - Path: `docs/7_Governance & Compliance/1_License & Third-Party Software Inventory/third-party-inventory.md`
  - Create inventory table (package, version, license, URL, usage, notes) and add paragraph on SPDX and compliance obligations.

- [x] **Security & Privacy Threat Model**
  - Path: `docs/7_Governance & Compliance/2_Security & Privacy Threat Model/threat-model.md`
  - Follow STRIDE methodology: system overview, data-flow description, threat enumeration table, mitigation summary and residual risk rating.