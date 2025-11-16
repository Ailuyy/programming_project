import pytest
from functions.word_frequencies import word_frequencies

@pytest.mark.parametrize('sentence, expected', [
    ("To be or not to be", {"to": 2, "be": 2, "or": 1, "not": 1}),
    ("Hello, hello!", {"hello": 2}),
    ("", {}),
    ("Python Python python", {"python": 3}),
    ("Ala ma kota, a kot ma Ale.", {"ala": 1, "ma": 2, "a": 1, "kota": 1, "kot": 1, "ale": 1}),
])

def test_word_frequencies(sentence: str, expected: dict) -> None:
    assert word_frequencies(sentence) == expected