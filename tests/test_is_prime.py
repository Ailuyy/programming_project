import pytest
from functions.is_prime import is_prime

@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (0, False),
    (1, False),
    (5, True),
    (97, True),
])

def test_is_prime(n, expected):
    assert expected == is_prime(n)