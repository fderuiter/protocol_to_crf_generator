# Deployment & Rollback Runbook

This runbook outlines the standard procedure for deploying the Protocol to CRF Generator and reverting to a previous release if necessary. It complements the CI/CD workflow described in the [technical plan](../../technical-plan.md) and assumes Docker-based deployments managed via GitHub Actions.

## Preconditions
- A tagged release artifact is available in the container registry and on PyPI.
- Target environment has Docker and `docker-compose` (or compatible orchestrator) installed.
- Necessary environment variables (database URL, CT cache path, secrets) are configured in the deployment host or secret store.
- Appropriate approvals have been recorded in the change management system.

## Deployment Steps
1. **Pull the Versioned Image**
   ```bash
   docker pull ghcr.io/your-org/protocol-to-crf-generator:${VERSION}
   ```
2. **Stop Existing Containers**
   ```bash
   docker-compose -f deploy/docker-compose.yml down
   ```
3. **Start New Containers**
   ```bash
   VERSION=${VERSION} docker-compose -f deploy/docker-compose.yml up -d
   ```
4. **Run Database Migrations** (if applicable)
   ```bash
   docker-compose exec api alembic upgrade head
   ```
5. **Verify Application Health** – see checks below.
6. **Update Change Log** – note deployment time, version and any manual tweaks.

## Health Checks
- **API endpoint test:** `curl -f http://<host>/health` returns `200 OK`.
- **Log inspection:** No errors in the last 5 minutes via `docker-compose logs`.
- **Background workers:** Celery/cron containers are running without restart loops.
- **Database connectivity:** `docker-compose exec api crf-gen db-check` exits with status 0.

## Rollback Procedure
1. Notify stakeholders that rollback is starting.
2. Stop current containers: `docker-compose down`.
3. Pull the previous stable image tag.
   ```bash
   docker pull ghcr.io/your-org/protocol-to-crf-generator:${PREV_VERSION}
   ```
4. Start containers with `PREV_VERSION`.
5. Run database downgrade if required: `alembic downgrade -1`.
6. Confirm health checks pass with the previous version.
7. Update the change log noting the reason for rollback and teams notified.

## Contact Matrix
| Team/Role | Responsibility | Contact |
| --- | --- | --- |
| **DevOps Engineer** | Executes deployment & rollback | devops@example.com |
| **Product Owner** | Approves releases | product@example.com |
| **Clinical SME** | Validates CRF outputs post-deploy | clinical@example.com |
| **Security Officer** | Monitors audit logs & compliance | security@example.com |

Document owners should update this matrix whenever team assignments change.
