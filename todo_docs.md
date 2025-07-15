# Documentation To-Do List – Protocol to CRF Generator

This file tracks documentation items that must be produced for the project. Each entry lists the document to write, the relative path where it should live, and any specific coverage notes (domains, services, etc.). All documents live under the `docs/` directory.

- [ ] **Project Charter / Vision Statement**  
  - Path: `docs/1_Vision & Scope/1_Project Charter + Vision Statement/project-charter.md`
  - Already drafted; review for completeness.

- [ ] **Stakeholder Register & RACI List**  
  - Path: `docs/1_Vision & Scope/Stakeholder & RACI list/stakeholders-raci.md`
  - Already drafted; update as new stakeholders join.

- [ ] **Functional Specification / User-Story Backlog**  
  - Path: `docs/2_Requirements/1_Functional Spec or User-Story Backlog/functional-spec-{feature}.md`  
  - Feature-specific docs: start with `functional_spec_protocol_ingestion.md` and create others as features are planned.  
  - Epics to cover include: Document Ingestion, Table & Section Detection, NLP Entity Extraction, Canonical IR Persistence, Operational Logging & Error Handling.

- [ ] **Non-Functional Requirements (NFR) Sheet**  
  - Path: `docs/2_Requirements/2_Non-Functional Requirements (NFR) Sheet/nfr-checklist.md`

- [ ] **High-Level Architecture ADR**  
  - Path: `docs/3_Architecture & Design/1_High-Level Architecture Diagram & ADRs/adr-0001-system-architecture.md`
  - Finalize PlantUML diagram covering services: CLI Tool, FastAPI Gateway, NLP & Extraction Svc, Mapping/Generation Svc, Validation Svc, SPA Web UI, Terminology DB, Audit Log DB, CI/CD Pipeline, external integrations (CDISC repos, EDC/CTMS).

- [ ] **Data Model / ER Diagram**  
  - Path: `docs/3_Architecture & Design/2_Data Model+ERD/er-model-{domain}.md`
  - Domains to document: AE, DM, EX, VS, CM, DS, MH.

- [ ] **API Contract & Versioning Policy**  
  - Path: `docs/3_Architecture & Design/3_API Contract & Versioning Policy/api-contract-{service}.md`
  - Services planned: `fastapi-gateway`, `cli-wrapper`, `nlp-extraction`, `mapping-generation`, `validation`. Each needs an OpenAPI stub and versioning notes.

- [ ] **Roadmap / Milestone Plan**  
  - Path: `docs/4_Planning & Risk/1_Roadmap/roadmap-next-12-months.md`

- [ ] **Risk Register & Mitigation Plan**  
  - Path: `docs/4_Planning & Risk/2_Risk Register & Mitigation Plan/risk-register.md`

- [ ] **Test Strategy & Definition of Done**  
  - Path: `docs/5_Quality & Ops/1_Test Strategy & Definition of Done/test-strategy.md`

- [ ] **Coding Standards & Style Guide**  
  - Path: `docs/5_Quality & Ops/2_Coding Standards + Style Guide/style-guide-python.md`  
  - Use Python as the main language.

- [ ] **CI/CD Pipeline Blueprint**  
  - Path: `docs/5_Quality & Ops/3_CICD Pipeline Blueprint/cicd-blueprint.md`

- [ ] **Deployment & Rollback Runbook**  
  - Path: `docs/5_Quality & Ops/4_Deployment & Rollback Runbook/runbook-deploy-rollback.md`

- [ ] **Repository README & Quick-Start**  
  - Path: `docs/6_Dev Env & Collaboration/1_Repository README & Quick-Start Guide/README.md`  
  - Also update root `README.md` for quick-start instructions.

- [ ] **Branching / Version Control Strategy**  
  - Path: `docs/6_Dev Env & Collaboration/2_Branching + Version Control Strategy/git-strategy.md`

- [ ] **Contribution Guidelines & Code-Review Checklist**  
  - Path: `docs/6_Dev Env & Collaboration/3_Contribution Guidelines & Code-Review Checklist/CONTRIBUTING.md`

- [ ] **Communication & Meeting Cadence Plan**  
  - Path: `docs/6_Dev Env & Collaboration/4_Communication & Meeting Cadence Plan/communication-plan.md`

- [ ] **License & Third-Party Software Inventory**  
  - Path: `docs/7_Governance & Compliance/1_License & Third-Party Software Inventory/third-party-inventory.md`

- [ ] **Security & Privacy Threat Model**  
  - Path: `docs/7_Governance & Compliance/2_Security & Privacy Threat Model/threat-model.md`

Since this is a solo project, you are responsible for drafting, reviewing, and approving every document.
