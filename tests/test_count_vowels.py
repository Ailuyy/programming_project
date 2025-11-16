import pytest
from functions.count_vowels import count_vowels

@pytest.mark.parametrize('text, expected', [
    ('Python', 1),
    ('AEIOUY', 6),
    ('bcd', 0),
    ('', 0),
    ('Próba żółwia', 4),
])

def test_count_vowels(text, expected):
    assert count_vowels(text) == expected