"""
Code analyzing

    -> It's a iteractive Algorithm so it is time complexity is O(n)
    -> I used a built-in tool to make a dict of list for each key
    -> Each element was sorted and made a dict key and save in it
    -> Finally it returns a dict of lists with keys for each anagram
"""

from collections import defaultdict


def group_anagrams(words):
    dict_of_anagrams_lists = defaultdict(list)
    for word in words:
        sorted_word = " ".join(sorted(word))
        dict_of_anagrams_lists[sorted_word].append(word)
    return dict_of_anagrams_lists.values()


anagrams = group_anagrams(words=["tea", "eat", "bat", "ate", "arc", "car"])
