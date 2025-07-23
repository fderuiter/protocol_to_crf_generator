# Secret Rotation Procedure

Regularly rotating credentials reduces the blast radius of leaked secrets. The
`rotate_secrets.py` utility automates generation of new API and database tokens
and updates the deployment environment.

## Usage

```bash
python scripts/rotate_secrets.py --env-file deploy/.env --restart
```

By default the script writes new values for `API_SECRET` and `DB_PASSWORD` to the
specified environment file. When `--restart` is supplied it will restart the
Docker Compose stack so the updated secrets take effect without downtime.

## Scheduling

Secret rotation is triggered automatically via the `rotate_secrets.yml` workflow
in GitHub Actions. This workflow runs weekly but can also be executed manually
from the Actions tab.
