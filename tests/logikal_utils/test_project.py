from pytest import raises
from pytest_mock import MockerFixture

from logikal_utils import project


def test_pyproject() -> None:
    assert project.PYPROJECT['project']['name'] == 'logikal-utils'
    assert 'non-existent-section' not in project.PYPROJECT


def test_project_name(mocker: MockerFixture) -> None:
    assert project.project_name() == 'logikal-utils'

    mocker.patch.dict(project.PYPROJECT, {}, clear=True)
    assert not project.project_name(raise_error_on_missing=False)
    with raises(RuntimeError, match='You must specify a project name'):
        project.project_name()


def test_tool_config() -> None:
    assert project.tool_config('setuptools')['packages'] == ['logikal_utils']
    assert not project.tool_config('non-existent-tool')
