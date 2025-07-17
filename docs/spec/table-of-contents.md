# Documentation Table of Contents

## Table of Contents

<!--AUTO-TOC-START-->
* [Protocol to CRF Generator – Project Charter](1_Vision & Scope/1_Project Charter + Vision Statement/project_charter.md)
  * Purpose & Vision
  * Business Objectives (SMART)
  * Scope
    * In‑Scope
    * Out‑of‑Scope
  * Key Deliverables & High‑Level Milestones
  * Success Metrics (KPIs)
  * Assumptions & Constraints
  * Stakeholders & Roles (RACI)
  * Budget / Resourcing Snapshot
  * Approval & Revision History
* [Stakeholder Register – Protocol to CRF Generator](1_Vision & Scope/Stakeholder & RACI list/stakeholders-raci.md)
  * Escalation Paths
* [Functional Specification – Protocol Ingestion & Information Extraction](2_Requirements/1_Functional Spec or User-Story Backlog/functional_spec_protocol_ingestion.md)
  * 📑 Table of Contents
  * Glossary<a name="glossary"></a>
  * User Stories<a name="user-stories"></a>
    * Epic PI‑01 – Document Ingestion<a name="epic-ingest"></a>
    * Epic PI‑02 – Table & Section Detection<a name="epic-structure"></a>
    * Epic PI‑03 – NLP Entity Extraction<a name="epic-nlp"></a>
    * Epic PI‑04 – Canonical IR Persistence<a name="epic-ir"></a>
    * Epic PI‑05 – Operational Logging & Error Handling<a name="epic-ops"></a>
  * Non‑Functional Notes<a name="nfr"></a>
  * Open Questions & Dependencies<a name="open-questions"></a>
* [Feature List](2_Requirements/1_Functional Spec or User-Story Backlog/z_feature_list.md)
  * 1. Deliverable & Access Interfaces
  * 2. Day-1 CDISC Standards Support
  * 3. Protocol Input Importers
  * 4. Non-Functional Foundations
  * 5. Core Technology Stack
  * 6. Continuous Integration / Continuous Deployment
  * 7. Reference-Data Management
  * 8. Protocol Ingestion & Information Extraction
  * 9. Semantic Mapping Engine
  * 10. CRF Artefact Generation
  * 11. Validation Layer
  * 12. Testing & Quality Control
  * 13. Packaging & Deployment Options
  * 14. Documentation & Onboarding
  * 15. Governance, Compliance & Community
* [Non‑Functional Requirements Checklist – CRF Generator](2_Requirements/2_Non-Functional Requirements (NFR) Sheet/nfr_checklist.md)
  * Performance
  * Scalability
  * Availability
  * Security
  * Compliance
  * Accessibility
  * Observability
  * Internationalization
  * Maintainability
    * Verification Methods
* [ADR 0001: Choosing System Architecture for **Protocol to CRF Generator**](3_Architecture & Design/1_High-Level Architecture Diagram & ADRs/adr-0001-system-architecture.md)
  * Status
  * Date
  * Context
  * Decision Drivers
  * Considered Options
  * Decision Outcome
    * Rationale
  * Pros & Cons of the Options
  * Consequences
  * Architectural Views
  * Links
* [Adverse Events (AE) ER Model](3_Architecture & Design/2_Data Model+ERD/er-models/er-model-AE.md)
  * Overview
  * Entities
  * PlantUML
* [Concomitant Medications (CM) ER Model](3_Architecture & Design/2_Data Model+ERD/er-models/er-model-CM.md)
  * Overview
  * Entities
  * PlantUML
* [Demographics (DM) ER Model](3_Architecture & Design/2_Data Model+ERD/er-models/er-model-DM.md)
  * Overview
  * Entities
  * PlantUML
* [Disposition (DS) ER Model](3_Architecture & Design/2_Data Model+ERD/er-models/er-model-DS.md)
  * Overview
  * Entities
  * PlantUML
* [Exposure (EX) ER Model](3_Architecture & Design/2_Data Model+ERD/er-models/er-model-EX.md)
  * Overview
  * Entities
  * PlantUML
* [Medical History (MH) ER Model](3_Architecture & Design/2_Data Model+ERD/er-models/er-model-MH.md)
  * Overview
  * Entities
  * PlantUML
* [Vital Signs (VS) ER Model](3_Architecture & Design/2_Data Model+ERD/er-models/er-model-VS.md)
  * Overview
  * Entities
  * PlantUML
* [API Contract – CLI Wrapper](3_Architecture & Design/3_API Contract & Versioning Policy/api-contract-cli-wrapper.md)
  * OpenAPI 3.1 Stub
  * Versioning & Deprecation Timeline
* [API Contract – FastAPI Gateway](3_Architecture & Design/3_API Contract & Versioning Policy/api-contract-fastapi-gateway.md)
  * OpenAPI 3.1 Stub
  * Versioning & Deprecation Timeline
* [API Contract – Mapping Generation Service](3_Architecture & Design/3_API Contract & Versioning Policy/api-contract-mapping-generation.md)
  * OpenAPI 3.1 Stub
  * Versioning & Deprecation Timeline
* [API Contract – NLP Extraction Service](3_Architecture & Design/3_API Contract & Versioning Policy/api-contract-nlp-extraction.md)
  * OpenAPI 3.1 Stub
  * Versioning & Deprecation Timeline
* [API Contract – Validation Service](3_Architecture & Design/3_API Contract & Versioning Policy/api-contract-validation.md)
  * OpenAPI 3.1 Stub
  * Versioning & Deprecation Timeline
* [12-Month Roadmap and Milestone Plan](4_Planning & Risk/1_Roadmap/roadmap-next-12-months.md)
* [Risk Register & Mitigation Plan](4_Planning & Risk/2_Risk Register & Mitigation Plan/risk-register.md)
  * Heat‑Map Summary
* [Test Strategy & Definition of Done](5_Quality & Ops/1_Test Strategy & Definition of Done/test-strategy.md)
  * Objectives & Scope
  * Testing Pyramid Targets
  * Tooling & Environments
  * Non-Functional Testing
  * Defect Severity Definitions
  * Definition of Done Checklist
* [Python Coding Standards & Style Guide](5_Quality & Ops/2_Coding Standards + Style Guide/style-guide-python.md)
  * Formatting & Linting
  * Naming Conventions
  * Error Handling
  * Docstrings
  * Module Layout
  * Pre-commit Configuration
* [CI/CD Pipeline Blueprint](5_Quality & Ops/3_CICD Pipeline Blueprint/cicd-blueprint.md)
  * Workflow Triggers
  * Job Sequence
  * Artefact Handling & Notifications
  * Mermaid Flowchart
* [Deployment & Rollback Runbook](5_Quality & Ops/4_Deployment & Rollback Runbook/runbook-deploy-rollback.md)
  * Preconditions
  * Deployment Steps
  * Health Checks
  * Rollback Procedure
  * Contact Matrix
* [Communication & Meeting Cadence Plan](6_Dev Env & Collaboration/4_Communication & Meeting Cadence Plan/communication-plan.md)
  * Communication Channels
  * Ceremonies
  * Async Updates & Decision Logging
* [License & Third-Party Software Inventory](7_Governance & Compliance/1_License & Third-Party Software Inventory/third-party-inventory.md)
  * SPDX Compliance
* [Security & Privacy Threat Model](7_Governance & Compliance/2_Security & Privacy Threat Model/threat-model.md)
  * System Overview
  * Data Flow
  * STRIDE Threat Enumeration
  * Mitigation Summary
  * Residual Risk Rating
* [Technical Plan](technical-plan.md)
  * **Executive Summary**
  * **Section 1: Foundational Framework and Project Scope**
    * **1.1. Deliverable Format and Target User Personas**
    * **1.2. Define the CDISC Artefacts you must support on Day 1**
    * **1.3. Agree on the study-protocol inputs you will accept**
    * **1.4. List non-functional requirements**
  * **Section 2: System Architecture and Technology Stack**
    * **2.1. Core Programming Language and Library Ecosystem**
    * **2.2. Selection of Templating and Static-Site Generation Tooling**
    * **2.3. CI/CD Pipeline Architecture and Workflow Definition**
  * **Section 3: CDISC Reference Data Acquisition and Management**
    * **3.1. ODM Schema Ingestion and Typed Model Generation**
    * **3.2. Controlled Terminology (CT) Normalization and Lookup Service**
    * **3.3. Acquisition and Use of CDASH eCRF Examples for Test Corpora**
    * **3.4. Automated Ingestion Pipeline for Quarterly CT Updates**
  * **Section 4: Protocol Ingestion & Information Extraction**
    * **4.1. Build Importers**
    * **4.2. NLP Pipeline**
    * **4.3. Persist a canonical Study Requirements JSON (your internal IR)**
  * **Section 5: Mapping to CDISC Metadata**
    * **5.1. For every extracted data item, map to CDISC metadata**
    * **5.2. Flag any unmapped items and surface them in a QA report**
    * **5.3. Generate an ODM block per variable; group into by CRF**
  * **Section 6: Markdown CRF Generator**
    * **6.1. Design a YAML front-matter schema for CRF metadata**
    * **6.2. Create Jinja templates that loop through the ODM JSON and render sections**
    * **6.3. Emit Git-friendly.md files alongside the source ODM JSON**
  * **Section 7: Validation Layer**
    * **7.1. ODM structural validation: run every generated ODM document through the 2.0 XML/JSON schema**
    * **7.2. CDISC rules validation**
    * **7.3. Produce a consolidated validation log**
  * **Section 8: Testing & Quality Control**
    * **8.1. Unit tests for each parser, mapper, and template component**
    * **8.2. Regression test protocols: maintain a small corpus of public protocols and expected CRF outputs**
    * **8.3. Integrate code-coverage, linting, and security scans**
  * **Section 9: Packaging & Deployment**
    * **9.1. Provide both a CLI and a REST API**
    * **9.2. Containerise with Docker; publish images to a registry**
    * **9.3. Optional: Offer a single-page web UI that lets users upload a protocol and download a ZIP**
  * **Section 10: Documentation & Onboarding**
    * **10.1. Auto-generate API docs with OpenAPI / Swagger**
    * **10.2. Write a “How we map protocols to CDISC” guide with examples**
    * **10.3. Publish versioning policy (how often you update CDISC references, semantic-versioning of your tool)**
  * **Section 11: Governance & Future-Proofing**
    * **11.1. Create a steering document for managing future CDISC standard versions**
    * **11.2. Log and track regulated-system requirements**
    * **11.3. Plan community contributions**
  * **Conclusion and Strategic Roadmap**
    * **Works cited**
<!--AUTO-TOC-END-->
