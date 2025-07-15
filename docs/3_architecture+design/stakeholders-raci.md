# Stakeholder Register – Protocol to CRF Generator

| Role | Name | Responsibility | RACI (R/A/C/I) | Preferred Channel | Frequency of Updates |
|------|------|---------------|---------------|------------------|----------------------|
| Product Owner / Lead Developer | <Your Name> | Owns project vision, architecture, coding and day‑to‑day delivery | **RA** | GitHub Issues / Slack DM | Daily stand‑ups |
| Regulatory & Compliance SME | Dr. Asha Patel | Advises on 21 CFR Part 11, CDISC compliance and audit readiness | **C** | Email / Slack thread | Bi‑weekly or ad‑hoc |
| Clinical Data Manager Representative | Maria (CRO) | Reviews mapping accuracy, validates CRF usability for data management | **C** | Slack project channel | Weekly review |
| Principal Investigator Representative | Dr. Chen | Confirms clinical requirements are captured in generated CRFs | **C** | Email | Milestone demos |
| DevOps / Infrastructure Lead | David (CRO Tech Lead) | Maintains CI/CD, containerization, and deployment environments | **I** | GitHub PR reviews / Slack | Per sprint |
| QA / Validation Lead | TBD (future hire) | Defines and executes validation & regression test suite | **I** | GitHub Actions reports | On every tagged release |
| Open‑Source Community Contributors | Various | Contribute code, file issues, suggest enhancements | **I** | GitHub Discussions | Continuous |

## Escalation Paths

For day‑to‑day questions, stakeholders post in the dedicated Slack channel or comment on the relevant GitHub issue/PR.  

* **Urgent technical blockers** (e.g., build failures, critical bugs) are escalated directly to the Product Owner via Slack DM and, if unresolved within 4 hours, a short Zoom call is convened with the DevOps Lead.  
* **Regulatory or compliance concerns** are routed to the Regulatory SME; if a decision is needed within 48 hours, the SME and Product Owner jointly decide, documenting the outcome in the project wiki.  
* **Scope or priority conflicts** are surfaced in the weekly review; if consensus isn’t reached, the Product Owner makes the final call, informing all stakeholders via Slack and noting the decision in the next sprint planning notes.

_Last updated: 2025-07-15_
