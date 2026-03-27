"""
Utilities for managing imports.
"""
from functools import cache
from importlib import import_module
from importlib.util import find_spec
from types import ModuleType


def try_import(name: str) -> ModuleType | None:
    """
    Return the imported module, or :data:`None` if it was not found.
    """
    try:
        return import_module(name=name)
    except ImportError:
        return None


@cache
def installed(name: str) -> bool:
    """
    Return :data:`True` if a given module has been installed.
    """
    return bool(find_spec(name))
