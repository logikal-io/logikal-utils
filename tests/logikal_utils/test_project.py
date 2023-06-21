from logikal_utils import project


def test_pyproject() -> None:
    assert project.PYPROJECT['project']['name'] == 'logikal-utils'
    assert 'non-existent-section' not in project.PYPROJECT


def test_tool_config() -> None:
    assert project.tool_config('setuptools')['packages'] == ['logikal_utils']
    assert not project.tool_config('non-existent-tool')
