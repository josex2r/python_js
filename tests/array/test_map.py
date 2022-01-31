from __future__ import annotations
from typing import Callable, List

from lib.array import map

seasons: List[str] = ['Winter', 'Summer', 'Fall', 'Spring']
numbers: List[int] = [1, 2, 3, 4]
seasond_and_numbers: List[int | str] = [*seasons, *numbers]


def test_map():
    format_str: Callable[[str, int],
                         str] = lambda value, index: f"{value} ({index})"

    formatted_seasons = map(seasons, format_str)

    # Then
    assert formatted_seasons == [
        'Winter (0)', 'Summer (1)', 'Fall (2)', 'Spring (3)'
    ]
