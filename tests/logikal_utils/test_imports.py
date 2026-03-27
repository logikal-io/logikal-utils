import os

from logikal_utils.imports import installed, try_import


def test_import() -> None:
    assert try_import('os') is os
    assert try_import('nonexistent_package') is None
    assert try_import('os.nonexistent_module') is None


def test_installed() -> None:
    assert not installed('not_installed_package')
    assert installed('pytest_logikal')
    assert not installed('pytest_logikal.nonexistent_module')
    assert installed('pytest_logikal.core')
