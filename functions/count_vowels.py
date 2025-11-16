def count_vowels(text: str) -> int:
    vowels = set('aeiouy')
    return sum(1 for char in text.lower() if char in vowels)