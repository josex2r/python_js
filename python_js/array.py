# from .array.map import map, CallbackType, ReturnValue
from __future__ import annotations

from typing import List, TypeVar, Callable, Any

from .array_methods import filter, map, reduce

T = TypeVar("T")
K = TypeVar("K")


class Array(List[T]):
    def filter(self, func: Callable[[T, int], bool]) -> Array[Any]:
        return Array(filter(self, func))

    def map(self, func: Callable[[T, int], K]) -> Array[K]:
        return Array(map(self, func))

    def reduce(self, func: Callable[[Any, T, int], Any], initialValue: K | None = None) -> Any:
        return reduce(self, func, initialValue=initialValue)
