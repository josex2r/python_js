from __future__ import annotations

from typing import Iterable, List, Protocol, TypeVar  # Protocol

# P = ParamSpec('P')
T = TypeVar('T', contravariant=True)
K = TypeVar('K')

T_contra = TypeVar('T_contra', contravariant=True)
K_co = TypeVar('K_co', covariant=True)


class Callback(Protocol[T_contra, K_co]):
    def __call__(
        self,
        value: T_contra,
        index: int,
    ) -> K_co: ...


def map(iterable: Iterable[T], func: Callback[T, K]) -> List[K]:
    """
    Returns a new array with the results of calling func on each element.

    Args:
        iterable: The iterable to map.
        func: The callback which transforms each value.

        Returns:
            A List with each value result.

        Examples:
            >>> map([1, 2, 3], lambda x: x * 2)
            [2, 4, 6]
    """
    return [func(value, index) for index, value in enumerate(iterable)]
