# Python Coding Standards & Style Guide

This guide defines the coding conventions for the Protocol to CRF Generator project. It summarises the practices set forth in the [CDISC CRF Generation Technical Plan](../../CDISC%20CRF%20Generation%20Technical%20Plan_.md) and expands on them with concrete examples.

## Formatting & Linting

- **Ruff** is the single source of truth for formatting and linting. The configuration lives in `pyproject.toml` and enforces a PEP 8 compatible style.
- **Mypy** provides static type checking. All modules must run clean with `mypy --strict`.
- A **pre-commit** hook runs `ruff` and `mypy` automatically before each commit. Install it via `pre-commit install` after cloning.

## Naming Conventions

| Item            | Convention                          | Example              |
| --------------- | ---------------------------------- | -------------------- |
| Packages        | `lowercase_with_underscores`       | `protocol_parser`    |
| Modules         | `lowercase_with_underscores`       | `mapping_rules.py`   |
| Classes         | `CamelCase`                        | `ProtocolLoader`     |
| Functions       | `lowercase_with_underscores`       | `extract_tables()`   |
| Variables       | `lowercase_with_underscores`       | `study_id`           |
| Constants       | `UPPERCASE_WITH_UNDERSCORES`       | `DEFAULT_VERSION`    |

## Error Handling

- Use Python exceptions; never exit the program with `sys.exit` from library code.
- Raise specific exception types (`ValueError`, `RuntimeError`, etc.) and document them in the function docstring.
- Log errors using the standard `logging` module. Do not print directly to stdout/stderr.

## Docstrings

- Every public module, class and function requires a docstring using the **Google** style.
- Include short summaries, argument and return descriptions, and example snippets if helpful.

```python
def load_protocol(path: Path) -> Protocol:
    """Load a protocol document.

    Args:
        path: Location of the protocol file.

    Returns:
        Parsed ``Protocol`` instance ready for NLP extraction.
    """
```

## Module Layout

- Keep files under 300 lines when possible; split into submodules for larger areas.
- Group related code into packages: `ingestion`, `nlp`, `mapping`, `validation`, `api`.
- Place tests in a mirroring `tests/` hierarchy.

## Pre-commit Configuration

Add the following snippet to `.pre-commit-config.yaml` to enforce the style guide:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.6
    hooks:
      - id: ruff
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.10.0
    hooks:
      - id: mypy
        args: ["--strict"]
```

Running `pre-commit run --all-files` should succeed before opening a pull request.

