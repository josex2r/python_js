# from .array.map import map, CallbackType, ReturnValue
from __future__ import annotations

from .array_methods.map import map, CallbackType, K


class Array(list):
    def map(self, func: CallbackType) -> Array[K]:
        return Array(map(self, func))
