import pytest
from functions.calculate_discount import calculate_discount

@pytest.mark.parametrize("x, y, expected", [
    (100, 0.2, 80.0),
    (50, 0, 50.0),
    (200, 1, 0.0),
    (100, -0.1, ValueError),
    (100, 1.5, ValueError),
])

def test_calculate_discount(x, y, expected):
    assert calculate_discount(x, y) == expected