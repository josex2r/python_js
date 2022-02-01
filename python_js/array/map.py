from __future__ import annotations

from typing import Iterable, List, Protocol, TypeVar  # Protocol

# P = ParamSpec('P')
T = TypeVar('T', contravariant=True)
K = TypeVar('K')

T_contra = TypeVar('T_contra', contravariant=True)
K_co = TypeVar('K_co', covariant=True)


class Callback(Protocol[T_contra, K_co]):
    """Definition of a callback function protocol."""

    def __call__(
        self,
        value: T_contra,
        index: int,
    ) -> K_co:
        """
        Definition of a callback function.

        Args:
        ----
            value: An element of the iterable.
            index: The index of the element.

        """
        pass


def map(iterable: Iterable[T], func: Callback[T, K]) -> List[K]:
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
