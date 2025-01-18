"""
Utilities for managing imports.
"""
from importlib import import_module
from types import ModuleType


def try_import(name: str) -> ModuleType | None:
    """
    Return the imported module, or :data:`None` if it was not found.
    """
    try:
        return import_module(name=name)
    except ImportError:
        return None
