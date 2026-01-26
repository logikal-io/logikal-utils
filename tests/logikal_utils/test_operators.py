from logikal_utils.operators import unique


def test_unique() -> None:
    assert list(unique([])) == []
    assert list(unique([3, 3, 2, 1])) == [3, 2, 1]
    assert list(unique(['a', 1, 'a', 3, None])) == ['a', 1, 3, None]
