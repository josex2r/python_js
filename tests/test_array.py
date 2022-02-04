from __future__ import annotations

from typing import List

from python_js.array import Array

seasons: List[str] = ['Winter', 'Summer', 'Fall', 'Spring']
numbers: List[int] = [1, 2]
seasons_and_numbers: List[int | str] = [*seasons, *numbers]


def test_constructor() -> None:
    # Then
    assert Array(seasons_and_numbers) == seasons_and_numbers


def test_filter() -> None:
    array = Array(seasons_and_numbers)
    result = array.filter(lambda x, i: isinstance(x, str))

    # Then
    assert result == ["Winter", "Summer", "Fall", "Spring"]


def test_filter_chainable() -> None:
    array = Array(seasons_and_numbers)
    result: List[str] = array.filter(
        lambda x, i: isinstance(x, str)
    ).filter(
        lambda x, i: x.startswith('W')
    )

    # Then
    assert result == ["Winter"]


def test_map() -> None:
    array = Array(seasons_and_numbers)
    result = array.map(lambda x, i: f"{x} ({i})")

    # Then
    assert result == [
        'Winter (0)', 'Summer (1)', 'Fall (2)', 'Spring (3)', '1 (4)', '2 (5)'
    ]


def test_map_chainable() -> None:
    array = Array(seasons_and_numbers)
    result = array.map(lambda x, i: f"{x} ({i})").map(
        lambda x, i: f"({i}) {x}")

    # Then
    assert result == [
        '(0) Winter (0)',
        '(1) Summer (1)',
        '(2) Fall (2)',
        '(3) Spring (3)',
        '(4) 1 (4)',
        '(5) 2 (5)'
    ]


def test_reduce() -> None:
    array = Array(seasons_and_numbers)
    result = array.reduce(lambda prev, next, index: f"{prev}, {next}")

    # Then
    assert result == 'None, Winter, Summer, Fall, Spring, 1, 2'
