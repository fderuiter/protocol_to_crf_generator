import os
import shutil
import subprocess
from pathlib import Path

import pytest


ROOT_DIR = Path(__file__).resolve().parents[1]


@pytest.mark.skipif(shutil.which("docker") is None, reason="docker not installed")
def test_docker_build() -> None:
    """Ensure Dockerfile builds when Docker daemon is available."""
    if os.environ.get("ENABLE_DOCKER_TESTS") != "1":
        pytest.skip("Docker build test disabled")

    info = subprocess.run(["docker", "info"], capture_output=True)
    if info.returncode != 0:
        pytest.skip("docker daemon not running")

    result = subprocess.run(
        ["docker", "build", "-t", "p2c-test", str(ROOT_DIR)],
        capture_output=True,
    )
    assert result.returncode == 0, result.stderr.decode()
