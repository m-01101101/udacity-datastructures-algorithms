"""
A Trie/Prefix Tree is a kind of search tree used to provide quick lookup
of words/patterns in a set of words.

A basic trie such as the one below has a fast look-up and the space complexity in O(n^2)
    # of words * length of words
"""
from typing import List

"""
basic trie is a dictionary and has characters as keys, with nested dictionaries as values

basic_trie.keys()
>>> dict_keys(['a', 'h'])

type(basic_trie["a"])
>>> dict
"""
basic_trie = {
    # a and add word
    "a": {"d": {"d": {"word_end": True}, "word_end": False}, "word_end": True},
    # hi word
    "h": {"i": {"word_end": True}, "word_end": False},
}

# `is_word` starts with the root node, `basic_trie`
# it traverses each character (`char`) in the string provided (`word`)
def is_word(word: str) -> bool:
    """
    Look for the word in `basic_trie`
    """
    current_node = basic_trie

    for char in word:
        if char not in current_node:  # checks in dict keys
            return False

        current_node = current_node[char]  # move to next nested dict

    return current_node["word_end"]


test_words = ["ap", "add"]
assert not is_word(test_words[0])
assert is_word(test_words[1])


class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

    def __repr__(self):
        return str(f"child letters: {self.children.keys()}")


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str):
        """
        Add `word` to trie
        """
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # add character to children
            node = node.children[char]  # reset the working node to new child
        node.is_word = True  # once done, set is_word to True

    def add_many(self, words: List[str]):
        """
        Add multiple words at once to Trie
        """
        for word in words:
            self.add(word)

    def exists(self, word: str) -> bool:
        """
        Check if word exists in trie
        """
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    # def print_words(self, node: TrieNode, word: str) -> str:
    #     word = ""

    #     if node.is_word:
    #         print(word)
    #     for key, value in node.children.items():
    #         print_words(vale, word + key)

    # def __repr__(self) -> str:
    #     return print_words(self.root, "")


word_list = [
    "apple",
    "bear",
    "goo",
    "good",
    "goodbye",
    "goods",
    "goodwill",
    "gooses",
    "zebra",
]
word_trie = Trie()

# Add words
word_trie.add_many(word_list)

"""
apple would look like this:
word_trie.root.children["a"].children["p"].children["p"].children["l"].children["e"].is_word
>>> True
"""

assert word_trie.exists("bear")
assert word_trie.exists("zebra")
assert not word_trie.exists("goos")
assert not word_trie.exists("thisisatest")
