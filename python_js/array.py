# from .array.map import map, CallbackType, ReturnValue
from __future__ import annotations

from typing import List, TypeVar, Callable, Any

from .array_methods.map import map
from .array_methods.filter import filter

T = TypeVar("T")
K = TypeVar("K")


class Array(List[T]):
    def filter(self, func: Callable[[T, int], bool]) -> Array[Any]:
        return Array(filter(self, func))

    def map(self, func: Callable[[T, int], K]) -> Array[K]:
        return Array(map(self, func))
