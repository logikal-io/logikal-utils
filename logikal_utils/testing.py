from operator import methodcaller
from typing import Any, Callable


def hide_traceback[Function: Callable[..., Any]](
    function: Function,
    error: type[Exception] = AssertionError,
) -> Function:
    getattr(function, '__globals__')['__tracebackhide__'] = methodcaller('errisinstance', error)
    return function
