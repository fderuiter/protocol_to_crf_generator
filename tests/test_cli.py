from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from protocol_to_crf_generator.__main__ import main


def test_cli_runs() -> None:
    main([])
