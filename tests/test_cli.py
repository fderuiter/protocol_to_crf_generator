from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest  # type: ignore

from protocol_to_crf_generator import __version__
from protocol_to_crf_generator.__main__ import main


def test_cli_runs() -> None:
    main([])


def test_cli_version(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit):
        main(["--version"])
    captured = capsys.readouterr()
    assert __version__ in captured.out

