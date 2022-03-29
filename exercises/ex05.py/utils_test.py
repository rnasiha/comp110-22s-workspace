
from utils import only_evens, sub, concat 


"""only_evens function tests."""


def test_only_evens_empty() -> None:
    """Testing the only_evens function on an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test__only_evens_single_item() -> None:
    """Testing the only_evens function on a single item."""
    xs: list[int] = [2]
    assert only_evens(xs) == [2]


def test_only_evens_many_items() -> None:
    """Testing the only_evens function on many items."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


"""sub function tests."""


def test_sub_empty() -> None:
    """Testing the sub function on an empty list."""
    xs: list[int] = []
    assert sub(xs, 1, 2) == []


def test__sub_single_item() -> None:
    """Testing the sub function on a single item."""
    xs: list[int] = [0]
    assert sub(xs, 0, 1) == [0]


def test_sub_many_items() -> None:
    """Testing the sub function on many items."""
    xs: list[int] = [1, 2, 3]
    assert sub(xs, 0, 1) == [1]


numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
single_item: list[int] = [1]

"""concat function tests."""


def test_concat_empty() -> None:
    """Testing the concat function on an empty list."""
    xs: list[int] = []
    assert concat(xs, numbers) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_concat_single_item() -> None:
    """Testing the concat function on a single item."""
    xs: list[int] = []
    assert concat(xs, single_item) == [1]


def test_concat_many_items() -> None:
    """Testing the only_evens function on many items."""
    xs: list[int] = [1, 2, 3]
    assert concat(xs, numbers) == [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
