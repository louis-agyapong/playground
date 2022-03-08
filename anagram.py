"""
Quuestion:
1. Build a function that takes two paramenters, the initial word and the
word you want to check is an anagram of the first word.
2. Output True if an anagram was found and False if not.
"""

"""
An anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original
letters exactly once. For example, the word anagram itself can be
rearranged into nag a ram, also the word binary into brainy and the
word adobe into abode. ref: https://en.wikipedia.org/wiki/Anagram
"""


def check_for_anagram(word1, word2):
    """
    Checks if word2 is an anagram of word1.
    """
    return sorted(word1.lower()) == sorted(word2.lower())


if __name__ == "__main__":
    print(check_for_anagram("adobe", "abode"))
