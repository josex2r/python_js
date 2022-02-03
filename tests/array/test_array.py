from __future__ import annotations
from typing import List

from python_js.array import Array

seasons: List[str] = ['Winter', 'Summer', 'Fall', 'Spring']
numbers: List[int] = [1, 2]
seasond_and_numbers: List[int | str] = [*seasons, *numbers]


def test_constructor():
    # Then
    assert Array(seasond_and_numbers) == seasond_and_numbers


def test_map():
    array = Array(seasond_and_numbers)
    result = array.map(lambda x, i: f"{x} ({i})")

    # Then
    assert result == [
        'Winter (0)', 'Summer (1)', 'Fall (2)', 'Spring (3)', '1 (4)', '2 (5)'
    ]


def test_map_chainable():
    array = Array(seasond_and_numbers)
    result = array.map(lambda x, i: f"{x} ({i})").map(lambda x, i: f"({i}) {x}")

    # Then
    assert result == [
        '(0) Winter (0)', '(1) Summer (1)', '(2) Fall (2)', '(3) Spring (3)', '(4) 1 (4)', '(5) 2 (5)'
    ]
