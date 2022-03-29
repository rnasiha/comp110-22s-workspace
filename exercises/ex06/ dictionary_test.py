"""EX06 - Dictionary tests."""

__author__ = "730330522"

from dictionary import invert, count, favorite_color


""" Count function tests."""


def test_count_edge() -> None:
    """Edge case test for the count function."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_use_1() -> None: 
    """Use case test #1 for the count function."""
    xs: list[str] = ["abc"]
    assert count(xs) == {"abc": 1}


def test_count_use_2() -> None:
    """Use case test #2 for the count function."""
    xs: list[str] = ["abc", "efg", "abc"]
    assert count(xs) == {"abc": 2, "efg": 1}


"""Favorite color function tests."""


def test_favorite_color_edge() -> None:
    """Edge case test for the favorite_color function."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ""


def test_favorite_color_use_1() -> None:
    """Use case test #1 for the favorite_color function."""
    xs: dict[str, str] = {"Ezri": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_use_2() -> None:
    """Use case test #2 for the favorite_color function."""
    xs: dict[str, str] = {"Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == "blue"


"""Invert function tests"""


def test_invert_edge() -> None:
    """Edge case test for the invert function."""
    xs: dict[str, str] = {}
    assert invert(xs) == {} 


def test_invert_use_1() -> None:
    """Use case test #1 for the invert function."""
    xs: dict[str, str] = {"Ezri": "blue"}
    assert invert(xs) == {"blue": "Ezri"}


def test_invert_use_2() -> None:
    """Use case test #2 for the invert function."""
    xs: dict[str, str] = {"Ezri": "blue", "Kris": "pink"}
    assert invert(xs) == {"pink": "Kris", "blue": "Ezri"}
