from __future__ import annotations

from typing import Any, List


def concat(*args: List[Any]) -> List[Any]:
    """
    Merge two or more arrays.
    This method does not change the existing arrays, but instead returns a new array.

    Args:
        *args: The iterables to mergle.

    Return:
        A new element.

    Examples
    --------
        concat(
            ["a", "b", "c"],
            [1, 2, 3]
        ) # ["a", "b", "c", 1, 2, 3]

    """
    result: List[Any] = []

    for x in args:
        result = [*result, *x]

    return result
