def count_vowels(text: str) -> int:
    vowels = set('aąeęiouóy')
    return sum(1 for char in text.lower() if char in vowels)