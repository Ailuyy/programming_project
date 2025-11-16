import re
def word_frequencies(sentence: str) -> dict:
    freq = {}
    words = sentence.lower().split()
    for word in words:
        cleaned_word = re.sub('\W+', '', word)
        if cleaned_word:
            freq[word] = freq.get(cleaned_word, 0) + 1
    return freq