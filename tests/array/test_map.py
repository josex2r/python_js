from __future__ import annotations

from typing import Callable, List

from python_js.array import Array
from python_js.array_methods.map import map

seasons: List[str] = ['Winter', 'Summer', 'Fall', 'Spring']
numbers: List[int] = [1, 2]
seasons_and_numbers: List[int | str] = [*seasons, *numbers]


def test_returned_value_instance() -> None:
    formatted_seasons: List[str] = map(seasons, lambda x, i: x)

    # Then
    assert isinstance(formatted_seasons, List)


def test_input_argument_iterable() -> None:
    format_str: Callable[[str | int, int],
                         str] = lambda value, index: f"{value} ({index})"

    formatted_seasons_and_numbers: List[str] = map(
        seasons_and_numbers, format_str)

    # Then
    assert formatted_seasons_and_numbers == [
        'Winter (0)', 'Summer (1)', 'Fall (2)', 'Spring (3)', '1 (4)', '2 (5)'
    ]
