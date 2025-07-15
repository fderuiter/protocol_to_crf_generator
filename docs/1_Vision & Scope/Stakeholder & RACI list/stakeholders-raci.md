# Stakeholder Register – Protocol to CRF Generator

| Role                                 | Name                    | Responsibility                                                                                                    | RACI (R/A/C/I) | Preferred Channel               | Frequency of Updates |
| ------------------------------------ | ----------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------- | -------------------- |
| Product Owner / Lead Developer       | **Frederick de Ruiter** | Owns project vision, end-to-end development, architecture, compliance, deployment, and day-to-day decision-making | **RA** (sole)  | GitHub Issues / Slack (private) | Ad hoc (daily)
| Data Manager (Persona "Maria")       | Maria                   | Provides requirements from CRO data management perspective; validates API and CLI outputs | **C/I**        | Slack / Email                   | Weekly
| Study Designer (Persona "Dr. Chen")  | Dr. Chen                | Supplies clinical protocol content and reviews CRF outputs via optional web UI | **C/I**        | Email                           | At major milestones
| CRO Technical Lead ("David")         | David                   | Oversees deployment in validated environments; ensures CI/CD and container images meet GxP standards | **C/I**        | GitHub PR reviews               | On tagged releases
| Future QA / Validation Lead          | *TBD*                   | Define and execute validation & regression tests once additional resources join | **C/I**        | GitHub PR reviews               | On tagged releases
| Future Regulatory & Compliance SME   | *TBD*                   | Advise on 21 CFR Part 11 and CDISC compliance | **C**          | Email                           | As engaged
| Open-Source Contributors (community) | Various (future)        | Contribute code, file issues, propose enhancements | **I**          | GitHub Discussions              | Continuous

## Escalation Paths

Because this is currently a solo project, **Frederick de Ruiter** resolves all conflicts and urgent technical or compliance decisions directly.

* **Technical blockers** – Investigated immediately; unresolved issues after 4 hours trigger creation of a critical GitHub issue and, if external help is required, a call with a trusted peer or mentor.
* **Regulatory or compliance questions** – Documented in the project wiki; Frederick consults authoritative CDISC/FDA resources or community experts and records the decision.
* **Scope changes or roadmap adjustments** – Logged as GitHub issues and referenced in the next version tag or release notes.

*This register will be updated as new stakeholders join the project.*

