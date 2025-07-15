# 12-Month Roadmap and Milestone Plan

This roadmap spans the first year of development starting from project kickoff. It is derived from the phased implementation described in the Technical Plan.

| Epic / Major Feature | Q1 | Q2 | Q3 | Q4 |
| --- | --- | --- | --- | --- |
| CI/CD pipeline foundation | ✅ | ⚪ | ⚪ | ⚪ |
| Core reference data management | ✅ | ⚪ | ⚪ | ⚪ |
| DOCX importer & basic NLP (segmentation) | ✅ | ⚪ | ⚪ | ⚪ |
| Rule-based NER & mapping for DM/VS/CM | ✅ | ⚪ | ⚪ | ⚪ |
| ODM & Markdown generation engines | ✅ | ⚪ | ⚪ | ⚪ |
| Structural & CT validation | ⚪ | ✅ | ⚪ | ⚪ |
| CLI interface | ✅ | ⚪ | ⚪ | ⚪ |
| Additional domains AE/MH/DS/EX | ⚪ | ✅ | ⚪ | ⚪ |
| FastAPI REST API | ⚪ | ✅ | ⚪ | ⚪ |
| Automated CT updates | ⚪ | ✅ | ⚪ | ⚪ |
| Initial user documentation | ⚪ | ✅ | ⚪ | ⚪ |
| SPA Web UI | ⚪ | ⚪ | ✅ | ⚪ |
| PDF and XML importers | ⚪ | ⚪ | ✅ | ⚪ |
| Statistical NER model training | ⚪ | ⚪ | ✅ | ⚪ |
| CDISC CORE integration | ⚪ | ⚪ | ✅ | ⚪ |
| Governance framework | ⚪ | ⚪ | ✅ | ⚪ |
| Release v1.0 | ⚪ | ⚪ | ⚪ | ✅ |

**Dependencies and Narrative**

The first quarter focuses on establishing the foundation: setting up CI/CD, loading controlled terminology, and implementing the DOCX importer alongside core NLP components. By the end of Q1 the CLI can generate validated CRFs for Demographics, Vital Signs, and Concomitant Medications.

Quarter two expands domain coverage and delivers the first REST API so that the service can be integrated into external systems. Continuous terminology updates and user documentation are also delivered, preparing for broader adoption.

Quarter three emphasizes usability and advanced features. The Web UI lowers the barrier for non-technical users, while PDF/XML importers and a statistical NER model improve extraction accuracy. Integration with CDISC CORE ensures comprehensive validation and a formal governance model is established for future contributions.

Quarter four culminates in the first production-ready release (v1.0) after hardening the system and incorporating feedback from early adopters. Ongoing work items roll into the next planning cycle.

