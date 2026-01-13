import pytest

from logikal_utils.string import compact


def test_compact() -> None:
    assert callable(compact)
    assert compact.__name__ == 'compact'
    assert isinstance(compact('hello world'), str)


def test_whitespace() -> None:
    assert compact('hello   world') == 'hello world'
    assert compact('   hello world   ') == 'hello world'
    assert compact('hello' + ' ' * 10 + 'world') == 'hello world'


def test_newlines() -> None:
    assert compact('hello\nworld') == 'hello world'
    assert compact('hello\n\nworld') == 'hello world'
    assert compact('\nhello world') == 'hello world'
    assert compact('\nhello world\n') == 'hello world'
    assert compact("""hello
    world""") == 'hello world'


def test_newlines_whitespace() -> None:
    assert compact('hello\n   \n   world') == 'hello world'


def test_basic() -> None:
    assert compact('hello world') == 'hello world'
    assert compact('hello') == 'hello'


def test_empty() -> None:
    assert not compact('')
    assert not compact('\n')
    assert not compact(' \n ')
    assert not compact('   ')
    assert not compact('\t')


def test_tabs() -> None:
    assert compact('hello\tworld') == 'hello\tworld'


def test_compact_twice() -> None:
    text = """longer text   with
    multiple  whitespaces
    """
    compacted = compact(text)
    assert compact(text) == "longer text with multiple whitespaces"
    assert compact(compacted) == compacted


def test_non_string() -> None:
    with pytest.raises(AttributeError):
        compact(123)  # type: ignore
    with pytest.raises(AttributeError):
        compact([])  # type: ignore
    with pytest.raises(AttributeError):
        compact({'key': 'value'})  # type: ignore
    with pytest.raises(AttributeError):
        compact(True)  # type: ignore


def test_long_string() -> None:
    text = 'hello ' * 10000
    assert compact(text).count(' ') == 9999
    assert len(compact(text)) == 5 * 10000 + 9999
