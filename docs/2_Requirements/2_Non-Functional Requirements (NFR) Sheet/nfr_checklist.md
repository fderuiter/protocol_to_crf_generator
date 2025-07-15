# Non‑Functional Requirements Checklist – CRF Generator

Below is a concise, implementation‑ready checklist of the key non‑functional requirements (NFRs) for the **CRF Generator** project.  Each requirement is mapped to a clear, measurable target so that engineering, QA and compliance teams can objectively verify success.

## Performance
| Requirement | Measurable Target / Metric |
|-------------|---------------------------|
| End‑to‑end CRF build time for a 100‑page DOCX protocol (including NLP, mapping, validation and artefact generation) must remain fast enough for interactive use. | **Median ≤ 5 min; 95th percentile ≤ 7 min** on reference SKU (8 vCPU, 16 GB RAM). |

## Scalability
| Requirement | Measurable Target / Metric |
|-------------|---------------------------|
| The containerised service shall scale horizontally to support multiple concurrent study builds without degradation. | **Linear throughput up to 20 parallel jobs** with < 15 % increase in P95 latency per 5 additional workers when auto‑scaled via Kubernetes HPA. |

## Availability
| Requirement | Measurable Target / Metric |
|-------------|---------------------------|
| Hosted SaaS offering must provide high uptime for regulated customers. | **≥ 99.9 % monthly uptime (three‑nines)** as measured by external synthetic probes hitting the /health endpoint every 60 s. |

## Security
| Requirement | Measurable Target / Metric |
|-------------|---------------------------|
| Protect study data and comply with 21 CFR Part 11 security controls. | • **TLS 1.2+** enforced for all traffic; 100 % A+ SSL Labs score<br>• **RBAC** enforced by OIDC; 100 % of privileged APIs gated<br>• **Zero critical vulnerabilities** in weekly SAST/Dependency scans. |

## Compliance
| Requirement | Measurable Target / Metric |
|-------------|---------------------------|
| System must be validation‑ready for GxP use. | • **Full traceability matrix** linking URS→FRS→Test in Git<br>• **≥ 90 % automated test coverage** (unit + integration)<br>• **Successful execution of IQ/OQ/PQ scripts** in a regulated environment. |

## Accessibility
| Requirement | Measurable Target / Metric |
|-------------|---------------------------|
| Optional web UI shall be usable by all researchers, including those with disabilities. | **WCAG 2.1 AA conformance** verified by axe‑core scan with **0 blocking violations** per release. |

## Observability
| Requirement | Measurable Target / Metric |
|-------------|---------------------------|
| Provide rich telemetry for troubleshooting and SLA evidence. | • **100 % of requests** emit structured JSON logs, traces and RED metrics<br>• **Error budget ≤ 1 %** based on four‑golden‑signals SLO dashboard. |

## Internationalization
| Requirement | Measurable Target / Metric |
|-------------|---------------------------|
| Support multilingual protocols and generated CRFs. | • **UTF‑8 round‑trip fidelity for all inputs/outputs**<br>• Ability to render CRF labels in any CDISC‑supported locale (initially EN/JA); verified via automated Unicode test corpus. |

## Maintainability
| Requirement | Measurable Target / Metric |
|-------------|---------------------------|
| Codebase should remain clean, testable and easy to extend with new CDISC standards. | • **≥ 90 % line coverage**<br>• **≤ 5 % ruff lint violations** (CI must pass) <br>• Median PR lead‑time **≤ 1 day** after review automation. |

---
*Verification:* Targets will be enforced by the CI/CD pipeline: performance & scalability via **k6** load‑tests, uptime by **StatusCake** monitors, security by **OWASP ZAP/Bandit/Semgrep**, accessibility via **axe‑core**, observability metrics via **Prometheus/Grafana SLOs**, and compliance evidence captured in the automated validation pack.

