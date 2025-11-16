import pytest
from functions.flatten_list import flatten_list

@pytest.mark.parametrize("input, expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([1, [2, 3], [4, [5]]], [1, 2, 3, 4, 5]),
    ([], []),
    ([[[1]]], [1]),
    ([1, [2, [3, [4]]]], [1, 2, 3, 4]),
])

def test_flatten_list(input, expected):
    assert flatten_list(input) == expected