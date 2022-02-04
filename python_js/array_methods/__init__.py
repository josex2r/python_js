from .filter import filter
from .map import map
from .reduce import reduce

# __all__ = tuple(k for k in locals() if not k.startswith("_"))

__all__ = [
    "filter",
    "map",
    "reduce"
]
