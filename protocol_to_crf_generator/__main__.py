"""Simple CLI entry point."""

import argparse

from . import __version__


def main(args: list[str] | None = None) -> None:
    """Run the command line interface."""
    parser = argparse.ArgumentParser(description="Protocol to CRF Generator")
    parser.add_argument("--version", action="version", version=__version__)
    parser.parse_args(args)


if __name__ == "__main__":  # pragma: no cover
    main()
