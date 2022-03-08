"""
1. Build a function that takes two paramenters, the initial word and the
the word you want to check is an anagram of the first word.
2. Output True if an anagram was found and False if not.
"""


def check_for_anagram(word1, word2):
    """
    Checks if word2 is an anagram of word1.
    """
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)


print(check_for_anagram("python", "typhona"))
