from importlib import import_module
from types import ModuleType
from typing import Optional


def try_import(name: str) -> Optional[ModuleType]:
    """
    Return the imported module, or :data:`None` if it was not found.
    """
    try:
        return import_module(name=name)
    except ImportError:
        return None
