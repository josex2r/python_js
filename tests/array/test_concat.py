from __future__ import annotations

from typing import List

from python_js.array_methods.concat import concat

seasons: List[str] = ['Winter', 'Summer', 'Fall', 'Spring']
numbers: List[int] = [1, 2]
seasons_and_numbers: List[int | str] = [*seasons, *numbers]


def test_returned_value_instance() -> None:
    formatted_seasons: List[str | int] = concat(seasons, numbers)

    # Then
    assert isinstance(formatted_seasons, List)


def test_input_argument_iterable() -> None:
    result: List[str | int] = concat(seasons, numbers)

    # Then
    assert result == seasons_and_numbers
