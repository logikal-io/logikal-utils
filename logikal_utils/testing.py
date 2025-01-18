"""
Utilities for testing.
"""
from collections.abc import Callable
from operator import methodcaller
from typing import Any


def hide_traceback[Function: Callable[..., Any]](
    function: Function,
    error: type[Exception] = AssertionError,
) -> Function:
    """
    Decorator for hiding pytest failure tracebacks.

    See the :ref:`pytest documentation <pytest:__tracebackhide__>` for more information.
    """
    function.__globals__['__tracebackhide__'] = methodcaller('errisinstance', error)
    return function
