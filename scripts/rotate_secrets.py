from __future__ import annotations

import argparse
import os
import secrets
import subprocess
from pathlib import Path


DEFAULT_ENV_FILE = Path("deploy/.env")


def generate_token() -> str:
    """Return a cryptographically secure random token."""

    return secrets.token_urlsafe(32)


def update_env_file(env_path: Path, tokens: dict[str, str]) -> None:
    """Update the given env file with new tokens."""

    env: dict[str, str] = {}
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if "=" in line and not line.strip().startswith("#"):
                key, value = line.split("=", 1)
                env[key] = value
    env.update(tokens)
    env_lines = [f"{k}={v}\n" for k, v in env.items()]
    env_path.write_text("".join(env_lines))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Rotate deployment secrets")
    parser.add_argument(
        "--env-file",
        type=Path,
        default=DEFAULT_ENV_FILE,
        help="Environment file containing secrets",
    )
    parser.add_argument(
        "--restart",
        action="store_true",
        help="Restart services using docker-compose after rotation",
    )
    args = parser.parse_args(argv)

    tokens = {"API_SECRET": generate_token(), "DB_PASSWORD": generate_token()}
    update_env_file(args.env_file, tokens)

    if args.restart:
        try:
            subprocess.run(["docker-compose", "down"], check=True)
            env = os.environ.copy()
            env["VERSION"] = tokens["API_SECRET"][:8]
            subprocess.run(["docker-compose", "up", "-d"], check=True, env=env)
        except (OSError, subprocess.CalledProcessError) as exc:  # pragma: no cover
            print(f"Failed to restart services: {exc}")
            return 1

    print("Secrets rotated successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
