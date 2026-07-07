from collections.abc import Iterable
from typing import TypeVar

T = TypeVar('T')


# python 3.12:
# - remove: T = TypeVar('T')
# - update: def unique[T](iterable: Iterable[T]) -> Iterable[T]:
def unique(iterable: Iterable[T]) -> Iterable[T]:
    """
    Yield unique elements from an iterable.
    """
    seen = set()
    for element in iterable:
        if element not in seen:
            seen.add(element)
            yield element
