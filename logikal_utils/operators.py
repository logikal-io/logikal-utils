from collections.abc import Iterable


def unique[T](iterable: Iterable[T]) -> Iterable[T]:
    """
    Yield unique elements from an iterable.
    """
    seen = set()
    for element in iterable:
        if element not in seen:
            seen.add(element)
            yield element
