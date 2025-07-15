# Documentation TODO List – Protocol to CRF Generator

Below is a consolidated checklist of all documentation deliverables referenced in the repository. Each item indicates where the finished file should live under `docs/`.

## Vision & Scope
- [x] **Project Charter / Vision Statement**  
  Path: `docs/1_Vision & Scope/1_Project Charter + Vision Statement/project_charter.md`
- [x] **Stakeholder Register & RACI List**  
  Path: `docs/1_Vision & Scope/Stakeholder & RACI list/stakeholder_list.md`

## Requirements
- [ ] **Functional Specification / User‑Story Backlog**  
  Directory: `docs/2_Requirements/1_Functional Spec or User-Story Backlog/`  
  Existing example: `functional_spec_protocol_ingestion.md` – expand with specs for other modules.
- [x] **Non‑Functional Requirements (NFR) Sheet**  
  Path: `docs/2_Requirements/2_Non-Functional Requirements (NFR) Sheet/nfr_checklist.md`

## Architecture & Design
- [x] **High‑Level Architecture ADR**  
  Path: `docs/3_Architecture & Design/1_High-Level Architecture Diagram & ADRs/adr_0001_system_architecture.md`
- [x] **Data Model / ER Diagrams**  
  Directory: `docs/3_Architecture & Design/2_Data Model+ERD/er-models/`  
  Domains covered: `AE`, `CM`, `DM`, `DS`, `EX`, `MH`, `VS`.
- [ ] **API Contract & Versioning Policy**  
  Directory: `docs/3_Architecture & Design/3_API Contract & Versioning Policy/`  
  Service: `FastAPI` REST service → file `api-contract-fastapi-service.md`.
## Planning & Risk
- [ ] **Roadmap / Milestone Plan**  
  Path: `docs/4_Planning & Risk/1_Roadmap/roadmap-next-12-months.md`
- [ ] **Risk Register & Mitigation Plan**  
  Path: `docs/4_Planning & Risk/2_Risk Register & Mitigation Plan/risk-register.md`

## Quality & Ops
- [ ] **Test Strategy & Definition of Done**  
  Path: `docs/5_Quality & Ops/1_Test Strategy & Definition of Done/test-strategy.md`
- [ ] **Coding Standards & Style Guide**  
  Path: `docs/5_Quality & Ops/2_Coding Standards + Style Guide/style-guide-python.md`  
  Language: Python (FastAPI project).
- [ ] **CI/CD Pipeline Blueprint**  
  Path: `docs/5_Quality & Ops/3_CICD Pipeline Blueprint/cicd-blueprint.md`
- [ ] **Deployment & Rollback Runbook**  
  Path: `docs/5_Quality & Ops/4_Deployment & Rollback Runbook/runbook-deploy-rollback.md`

## Dev Env & Collaboration
- [ ] **Repository README & Quick‑Start Guide**  
  Path: `README.md` (root) and `docs/6_Dev Env & Collaboration/1_Repository README & Quick-Start Guide/README.md`
- [ ] **Branching / Version-Control Strategy**  
  Path: `docs/6_Dev Env & Collaboration/2_Branching + Version Control Strategy/git-strategy.md`
- [ ] **Contribution Guidelines & Code‑Review Checklist**  
  Path: `docs/6_Dev Env & Collaboration/3_Contribution Guidelines & Code-Review Checklist/CONTRIBUTING.md`
- [ ] **Communication & Meeting Cadence Plan**  
  Path: `docs/6_Dev Env & Collaboration/4_Communication & Meeting Cadence Plan/communication-plan.md`

## Governance & Compliance
- [ ] **License & Third‑Party Software Inventory**  
  Path: `docs/7_Governance & Compliance/1_License & Third-Party Software Inventory/third-party-inventory.md`
- [ ] **Security & Privacy Threat Model**  
  Path: `docs/7_Governance & Compliance/2_Security & Privacy Threat Model/threat-model.md`

_All documents are authored and maintained by the solo project lead._
