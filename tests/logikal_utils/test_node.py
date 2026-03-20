from pathlib import Path
from shutil import copy

from pytest import raises

from logikal_utils.node import install_packages


def test_install_packages_error(tmp_path: Path) -> None:
    with raises(RuntimeError, match='Missing Node.js package file'):
        install_packages(prefix=tmp_path)


def test_install_packages(tmp_path: Path) -> None:
    for file in ['package.json', 'package-lock.json']:
        copy(Path(__file__).parent / file, tmp_path)
    install_packages(prefix=tmp_path)
    assert (tmp_path / 'node_modules/stylelint').exists()
