from __future__ import annotations

from typing import Callable, Dict, List

from python_js.array import Array
from python_js.array_methods.reduce import reduce

seasons: List[str] = ['Winter', 'Summer', 'Fall', 'Spring']
numbers: List[int] = [1, 2]
seasons_and_numbers: List[int | str] = [*seasons, *numbers]


def test_returned_value_instance() -> None:
    formatted_seasons: str = reduce(seasons, lambda x, y, i: y)

    # Then
    assert isinstance(formatted_seasons, str)


def test_input_argument_iterable() -> None:
    concat_str: Callable[[str, str | int, int],
                         str] = lambda prev, next, index: f"{prev}, {next}"

    formatted_seasons_and_numbers: str = reduce(
        seasons_and_numbers, concat_str)

    # Then
    assert formatted_seasons_and_numbers == 'None, Winter, Summer, Fall, Spring, 1, 2'


def test_initialValue() -> None:
    accumulator: Dict[str, int] = {}

    def reduce_seasons(acc: Dict[str, int], season: str, index: int) -> Dict[str, int]:
        acc[season] = index
        return acc

    seasons_dict: Dict[str, int] = reduce(
        seasons, reduce_seasons, initialValue=accumulator)

    # Then
    assert seasons_dict == {
        'Winter': 0,
        'Summer': 1,
        'Fall': 2,
        'Spring': 3,
    }
    assert seasons_dict == accumulator
    assert id(seasons_dict) == id(accumulator)
