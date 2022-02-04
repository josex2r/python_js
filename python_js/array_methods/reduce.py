from __future__ import annotations
from typing import Iterable, TypeVar, Callable, Any

T = TypeVar('T')
K = TypeVar('K')


def reduce(iterable: Iterable[T], func: Callable[[Any, T, int], Any], initialValue: K | None = None) -> Any:
    """
    Executes a user-supplied “reducer” callback function on each element of
    the array, in order, passing in the return value from the calculation on
    the preceding element. The final result of running the reducer across all
    elements of the array is a single value.

    Args:
        iterable: The iterable to map.
        func: The callback which transforms all the values.

    Return:
        A new element.

    Examples
    --------
        reduce(
            ["a", "b", "c"],
            lambda acc, x, i: (acc[x] = i) and acc,
            {}
        ) # { 'a': 0, 'b': 1, 'c': 2 }

    """
    result = initialValue

    for i, x in enumerate(iterable):
        result = func(result, x, i)

    return result
