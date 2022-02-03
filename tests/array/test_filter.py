from __future__ import annotations

from typing import Callable, List

from python_js.array import Array
from python_js.array_methods.filter import filter

seasons: List[str] = ['Winter', 'Summer', 'Fall', 'Spring']
numbers: List[int] = [1, 2]
seasons_and_numbers: List[int | str] = [*seasons, *numbers]


def test_returned_value_instance() -> None:
    formatted_seasons: List[str] = filter(seasons, lambda x, i: bool(x))

    # Then
    assert isinstance(formatted_seasons, List)


def test_input_argument_iterable() -> None:
    format_str: Callable[[str | int, int],
                         bool] = lambda value, index: isinstance(value, str)

    formatted_seasons_and_numbers: List[str] = filter(
        seasons_and_numbers, format_str)

    # Then
    assert formatted_seasons_and_numbers == [
        'Winter', 'Summer', 'Fall', 'Spring'
    ]
