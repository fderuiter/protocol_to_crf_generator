"""Command line interface for the package."""

from __future__ import annotations

import argparse
import base64
from pathlib import Path

import httpx

from . import __version__


def _cmd_ingest(file: Path, url: str) -> None:
    """Upload ``file`` to the API ``url``.

    Parameters
    ----------
    file:
        Path to the protocol document.
    url:
        Base URL of the running API service.
    """

    content = base64.b64encode(file.read_bytes()).decode()
    payload = {"filename": file.name, "content": content}

    try:
        response = httpx.post(f"{url.rstrip('/')}/ingest", json=payload, timeout=10)
        response.raise_for_status()
    except httpx.HTTPError as exc:  # pragma: no cover - network failures
        print(f"Error: {exc}")
        raise SystemExit(1) from exc

    data = response.json()
    print(f"Job {data['job_id']} {data['state']}")


def main(args: list[str] | None = None) -> None:
    """Run the command line interface."""
    parser = argparse.ArgumentParser(description="Protocol to CRF Generator")
    parser.add_argument("--version", action="version", version=__version__)

    subparsers = parser.add_subparsers(dest="command")
    ingest_parser = subparsers.add_parser("ingest", help="Upload a protocol")
    ingest_parser.add_argument("file", type=Path)
    ingest_parser.add_argument("--url", default="http://localhost:8000")

    ns = parser.parse_args(args)

    if ns.command == "ingest":
        _cmd_ingest(ns.file, ns.url)


if __name__ == "__main__":  # pragma: no cover
    main()
