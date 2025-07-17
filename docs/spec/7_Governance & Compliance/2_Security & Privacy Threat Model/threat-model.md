# Security & Privacy Threat Model

This document outlines potential security and privacy threats to the Protocol to CRF Generator using the **STRIDE** methodology. The analysis draws on controls described in the [technical plan](../../technical-plan.md) such as CI-based static scanning and immutable audit logs.

## System Overview

The system ingests study protocols through a CLI or REST API, processes them with an NLP pipeline and mapping logic, and outputs CDISC-compliant CRF artefacts. Data and logs are stored in version-controlled repositories and audited databases. Deployments run in Docker containers behind a FastAPI gateway.

## Data Flow

1. User submits a protocol document via the CLI or REST API.
2. The document is parsed and processed through the NLP and mapping services.
3. Generated CRFs are stored in Git and optionally pushed to an EDC system.
4. All interactions are logged for compliance and troubleshooting.

## STRIDE Threat Enumeration

| Category | Example Threat | Mitigation |
| --- | --- | --- |
| **Spoofing** | Attacker impersonates a valid user via stolen credentials | Enforce MFA for maintainer accounts and require token-based auth for the API |
| **Tampering** | Modification of CRF templates or mapping rules in transit | Use TLS for all network traffic and sign releases with GPG |
| **Repudiation** | User denies generating a specific CRF version | Maintain immutable Git history and append-only audit logs |
| **Information Disclosure** | Leakage of sensitive protocol details | Store documents in a private repository and restrict access via RBAC |
| **Denial of Service** | Excessive requests overwhelm the NLP service | Rate-limit the API and monitor resource usage via the CI/CD pipeline |
| **Elevation of Privilege** | Exploiting a container escape to gain host access | Run containers with non-root users and apply regular security patches |

## Mitigation Summary

Security scanning with **Bandit** and **Semgrep** is integrated into the CI workflow to catch vulnerabilities early. TLS encryption and strict authentication protect all endpoints. Audit logs support compliance with 21 CFR Part 11. Access to sensitive data is restricted to the maintainer and approved collaborators.

## Residual Risk Rating

Given the controls above, the residual risk is **Low**. Ongoing monitoring and regular dependency updates are required to maintain this posture.
