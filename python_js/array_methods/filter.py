from __future__ import annotations
from typing import Iterable, TypeVar, List, Callable, Any

T = TypeVar('T')


def filter(iterable: Iterable[T], func: Callable[[T, int], bool]) -> List[Any]:
    """
    Return a new array with the the elements which passes the callback.

    Args:
        iterable: The iterable to map.
        func: The callback which filters the values.

    Return:
        A filtered List.

    Examples
    --------
        filter([1, 2, 3], lambda x: x > 2) # [3]

    """
    return [value for index, value in enumerate(iterable) if func(value, index)]
