"""
Utilities for testing.
"""
from collections.abc import Callable
from operator import methodcaller
from typing import Any, TypeVar

Function = TypeVar('Function', bound=Callable[..., Any])


# python 3.12:
# - remove Function = TypeVar(...)
# - update def hide_traceback[Function: Callable[..., Any]](...)
def hide_traceback(function: Function, error: type[Exception] = AssertionError) -> Function:
    """
    Hide pytest failure tracebacks.

    See the :ref:`pytest documentation <pytest:__tracebackhide__>` for more information.
    """
    function.__globals__['__tracebackhide__'] = methodcaller('errisinstance', error)
    return function
