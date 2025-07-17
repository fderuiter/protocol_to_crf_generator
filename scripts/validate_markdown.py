from pathlib import Path
import subprocess


def main() -> int:
    roots = [Path("."), Path("docs")]  # scan root markdown and top-level docs
    files = []
    for root in roots:
        if root.exists():
            files.extend(str(p) for p in root.glob("*.md"))
    result = subprocess.run(
        [
            "pymarkdown",
            "-d",
            "MD013,MD022,MD025,MD032,MD033,MD007,MD012,MD041",
            "scan",
            *files,
        ]
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
