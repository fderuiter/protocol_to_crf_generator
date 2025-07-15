from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import sqlite3


def fetch_latest_version() -> str:
    """Return the latest terminology version.

    In a real implementation this would query the NCI-EVS FTP server.
    """
    return date.today().isoformat()


def build_database(db_path: Path, version: str) -> None:
    """Create or update the terminology SQLite database."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS metadata (version TEXT)")
    cur.execute("DELETE FROM metadata")
    cur.execute("INSERT INTO metadata (version) VALUES (?)", (version,))
    conn.commit()
    conn.close()


def main(args: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Update controlled terminology")
    parser.add_argument(
        "--db-path", type=Path, default=Path("terminology.sqlite"), help="Output SQLite file",
    )
    parsed = parser.parse_args(args)
    version = fetch_latest_version()
    build_database(parsed.db_path, version)
    print(f"Generated {parsed.db_path} for version {version}")


if __name__ == "__main__":  # pragma: no cover
    main()
