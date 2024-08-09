import os

from logikal_utils.imports import try_import


def test_import() -> None:
    assert try_import('os') is os
    assert try_import('nonexistent_package') is None
    assert try_import('os.nonexistent_module') is None
