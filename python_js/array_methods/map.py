from __future__ import annotations
from typing import Iterable, TypeVar, List, Callable

T = TypeVar('T')
K = TypeVar('K')


def map(iterable: Iterable[T], func: Callable[[T, int], K]) -> List[K]:
    """
    Return a new array with the results of calling func on each element.

    Args:
        iterable: The iterable to map.
        func: The callback which transforms each value.

    Return:
        A List with each value result.

    Examples
    --------
        map([1, 2, 3], lambda x: x * 2) # [2, 4, 6]

    """
    return [func(value, index) for index, value in enumerate(iterable)]
