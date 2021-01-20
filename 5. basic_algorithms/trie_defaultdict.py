"""
A cleaner way to build a trie is with a Python default dictionary
"""
from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(
            TrieNode
        )  # we're defining children as a dict of nodes
        self.is_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        node = self.root

        for char in word:
            node = node.children[
                char
            ]  # because it remembers the order you can add it as a dictionary
            node.is_word = True

    def add_many(self, words: List[str]):
        """
        Add multiple words at once
        """
        for word in words:
            self.add(word)

    def exists(self, word):  # no change in this implementation
        """
        Check if word exists in trie
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word


valid_words = ["the", "a", "there", "answer", "any", "by", "bye", "their"]
word_trie = Trie()
word_trie.add_many(valid_words)

"""
word_trie.root.children
>>> defaultdict(__main__.TrieNode,
            {'t': <__main__.TrieNode at 0x105d8ba60>,
             'a': <__main__.TrieNode at 0x105d8bdc0>,
             'b': <__main__.TrieNode at 0x1064e7e20>})

same implemention when validating a word:
word_trie.root.children["t"].children["h"].children["e"].is_word
>>> True             
"""

assert word_trie.exists("the")
assert word_trie.exists("any")
assert not word_trie.exists("these")
assert not word_trie.exists("zzz")
