# Standard Version Adoption and Management Policy

This policy governs how the project adopts new versions of CDISC standards such as CDASH, SDTM and Controlled Terminology. It implements the governance requirements defined in the [technical plan](docs/CDISC%20CRF%20Generation%20Technical%20Plan_.md).

## Scope

The tool currently supports the CDISC standards listed in the technical plan. As new official versions are released, the steering committee will evaluate them for inclusion.

## Monitoring Process

- **Weekly check**: An automated workflow monitors NCI‑EVS for Controlled Terminology releases.
- **Biannual review**: The committee reviews the CDISC roadmap twice a year to track upcoming major releases of other standards.

## Impact Assessment

For each new major version of a standard the committee will produce an impact assessment covering:

1. Technical changes and their effect on parsing, mapping and validation logic.
2. Estimated effort required to implement support.
3. Backward compatibility considerations.

## Adoption and Support Policy

The project aims to support the **latest final version plus the previous major version** of each standard. Older versions are deprecated and removed in a future major release of the tool.

## Roadmap and Communication

Planned adoption of new standard versions is published on the project roadmap and communicated via GitHub issues and release notes.

## Tool Versioning Alignment

Changes to supported standards correspond to semantic version bumps of the tool:

- **MAJOR** release – adds support for or removes a major standard version.
- **MINOR** release – adds a new backward-compatible standard such as an updated CT package.
