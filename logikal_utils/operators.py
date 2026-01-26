from collections.abc import Iterable
from typing import TypeVar

T = TypeVar('T')


def unique(iterable: Iterable[T]) -> Iterable[T]:
    seen = set()
    for element in iterable:
        if element not in seen:
            seen.add(element)
            yield element
