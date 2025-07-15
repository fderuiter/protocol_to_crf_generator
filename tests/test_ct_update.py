from pathlib import Path
from protocol_to_crf_generator import ct_update


def test_build_database(tmp_path: Path) -> None:
    db_file = tmp_path / "ct.sqlite"
    ct_update.build_database(db_file, "2025-01-01")
    assert db_file.exists()
