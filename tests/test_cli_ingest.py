from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict

import pytest

from protocol_to_crf_generator.__main__ import main


def test_cmd_ingest_posts(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    file_path = tmp_path / "sample.docx"
    file_path.write_text("dummy")

    captured: Dict[str, Any] = {}

    def fake_post(url: str, json: Dict[str, Any], timeout: int) -> SimpleNamespace:
        captured["url"] = url
        captured["json"] = json

        return SimpleNamespace(
            json=lambda: {"job_id": "42", "state": "accepted"},
            raise_for_status=lambda: None,
        )

    monkeypatch.setattr("httpx.post", fake_post)

    main(["ingest", str(file_path), "--url", "http://test"])
    output = capsys.readouterr().out

    assert captured["url"] == "http://test/ingest"
    assert captured["json"]["filename"] == "sample.docx"
    assert "Job 42 accepted" in output

