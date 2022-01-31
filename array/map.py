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


def js_map(array: Iterable[T], func: Callback[T, K]) -> List[K]:
    """
    Returns a new array with the results of calling func on each element.
    """
    return [func(value, index) for index, value in enumerate(array)]
