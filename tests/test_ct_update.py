from pathlib import Path
import pytest

from protocol_to_crf_generator import ct_update


def test_build_database(tmp_path: Path) -> None:
    db_file = tmp_path / "ct.sqlite"
    ct_update.build_database(db_file, "2025-01-01")
    assert db_file.exists()


def test_fetch_latest_version() -> None:
    version = ct_update.fetch_latest_version()
    assert version.count("-") == 2


def test_main_creates_db(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    db_file = tmp_path / "auto.sqlite"
    ct_update.main(["--db-path", str(db_file)])
    assert db_file.exists()
