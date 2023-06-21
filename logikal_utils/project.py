from pathlib import Path
from typing import Any

import tomli

PATH = Path('pyproject.toml')
#: The ``pyproject.toml`` configuration of the current project.
PYPROJECT: Any = tomli.loads(PATH.read_text(encoding='utf-8')) if PATH.exists() else {}


def tool_config(name: str) -> Any:
    """
    Return the ``pyproject.toml`` configuration of a given tool.
    """
    return PYPROJECT.get('tool', {}).get(name, {})
