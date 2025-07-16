# Communication & Meeting Cadence Plan

This plan defines how collaboration occurs on the Protocol to CRF Generator project. It summarises practices referenced in the [CDISC CRF Generation Technical Plan](../../CDISC%20CRF%20Generation%20Technical%20Plan_.md) and complements the stakeholder RACI register.

## Communication Channels

| Channel | Purpose | Notes |
| --- | --- | --- |
| **GitHub Issues** | Track tasks, bugs and discussions | Primary record of decisions, linked to ADRs and pull requests |
| **Pull Requests** | Code review, automated checks and merges | Must pass CI as described in the technical plan; comments remain part of the audit trail |
| **Slack (private)** | Day‑to‑day coordination for the maintainer and close collaborators | Summarised back into GitHub issues to keep a canonical record |
| **Email** | Formal notifications and release announcements | Used for external stakeholders who do not monitor GitHub |

## Ceremonies

| Ceremony | Frequency | Duration | Participants | Tool |
| --- | --- | --- | --- | --- |
| **Weekly Sync** | Every Monday | 30 min | Frederick de Ruiter, invited collaborators | Slack call |
| **Backlog Grooming** | Bi‑weekly | 45 min | Maintainer + contributors | GitHub Projects |
| **Release Review** | On every tagged release | 1 h | Maintainer, CRO Tech Lead, future QA Lead | GitHub PR + email summary |
| **Steering Update** | Biannual | 1 h | Steering committee (future) | Video conference |

These meetings may be cancelled if there are no agenda items. Action items are captured in GitHub Issues for traceability.

Backlog grooming sessions review the GitHub Project board to prioritise work. Notes from these meetings, and from other ceremonies, should be added as comments on the relevant issue or pull request. The Project item should link to those discussions so that the board and issue history provide a complete record.

## Async Updates & Decision Logging

All substantial design or process decisions are documented in Architecture Decision Records (ADRs) stored under `docs/3_Architecture & Design`. When a discussion in Slack or a meeting leads to a new decision, a short note with a link to the relevant ADR or issue is posted in the meeting thread.

GitHub Issues and pull request descriptions serve as the canonical communication log, satisfying the auditability requirements noted in the technical plan. Contributors should prefer asynchronous updates via issues and pull requests so that all discussions remain searchable and linkable.

