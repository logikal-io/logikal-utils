"""
Utilities for viewing project configuration.
"""
import tomllib
from decimal import Decimal
from pathlib import Path
from typing import Any

PATH = Path('pyproject.toml')
#: The ``pyproject.toml`` configuration of the current project.
PYPROJECT: dict[str, Any] = (
    tomllib.loads(PATH.read_text(encoding='utf-8'), parse_float=Decimal)
    if PATH.exists() else {}
)


def project_name(raise_error_on_missing: bool = True) -> str | None:
    """
    Return the project name from ``pyproject.toml``.
    """
    project = PYPROJECT.get('project', {}).get('name')
    if raise_error_on_missing and not project:
        raise RuntimeError('You must specify a project name in pyproject.toml')
    return project  # type: ignore[no-any-return]


def tool_config(name: str) -> Any:
    """
    Return the ``pyproject.toml`` configuration of a given tool.
    """
    return PYPROJECT.get('tool', {}).get(name, {})
