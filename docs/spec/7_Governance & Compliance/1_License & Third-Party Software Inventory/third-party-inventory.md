# License & Third-Party Software Inventory

This inventory lists the external dependencies referenced in the project and their associated licenses. The project itself is released under the Apache&nbsp;2.0 license as described in the [technical plan](../technical-plan.md). Keeping an accurate inventory helps ensure compliance with open‑source obligations and simplifies future audits.

| Package | Version | License | URL | Usage | Notes |
| --- | --- | --- | --- | --- | --- |
| **spaCy** | 3.6 | MIT | <https://github.com/explosion/spaCy> | Core NLP pipeline | Required for entity extraction |
| **medspaCy** | 0.5 | MIT | <https://github.com/medspacy/medspacy> | Clinical text modules | Optional models for medical terms |
| **FastAPI** | 0.111 | MIT | <https://github.com/tiangolo/fastapi> | REST API framework | Used by gateway service |
| **Pydantic** | 2.7 | MIT | <https://github.com/pydantic/pydantic> | Data validation | Defines request/response schemas |
| **PlantUML** | 1.2024 | Apache&nbsp;2.0 | <https://plantuml.com> | Architecture diagrams | Downloaded during docs build |
| **pytest** | 8.2 | MIT | <https://github.com/pytest-dev/pytest> | Test runner | Included in dev dependencies |

All licenses must be compatible with Apache&nbsp;2.0 to allow redistribution. If a new dependency is added, record it here with the declared license and verify it against the SPDX database.

## SPDX Compliance

The inventory serves as the basis for generating an SPDX document during releases. SPDX provides a standardized machine‑readable format describing the software bill of materials (SBOM) and license obligations. Maintaining an SPDX file ensures we can demonstrate the provenance of third‑party code and fulfil downstream compliance requirements. The CI pipeline will eventually validate that every package listed in `requirements.txt` has a corresponding entry in this inventory.
