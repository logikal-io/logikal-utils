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


def tool_config(name: str) -> Any:
    """
    Return the ``pyproject.toml`` configuration of a given tool.
    """
    return PYPROJECT.get('tool', {}).get(name, {})
