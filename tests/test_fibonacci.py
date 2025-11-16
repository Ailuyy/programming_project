import pytest
from functions.fibonacci import fibonacci

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (5, 5),
    (10, 55),
    (-1, ValueError),
])

def test_fibonacci(n, expected):
    assert fibonacci(n) == expected