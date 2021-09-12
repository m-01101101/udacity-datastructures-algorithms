class TrieNode:
    """represents a single node in the Trie"""

    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, char: str):
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix=""):
        """Recursive function that collects the suffix for all complete words below this point"""
        suffixes = []

        for char, node in self.children.items():
            if node.is_word:
                suffixes.append(suffix + char)
            if node.children:
                suffixes.extend(node.suffixes(suffix + char))
        return suffixes


class Trie:
    def __init__(self):
        """initialise Trie with root node"""
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root

        for char in word:
            node.insert(char)
            node = node.children[char]

        node.is_word = True

    def find(self, prefix: str):
        """ Find the Trie node that represents this prefix """
        node = self.root

        for char in prefix:
            if char not in node.children:
                return -1
            return node.children[char]


MyTrie = Trie()
wordList = [
    "ant",
    "anthology",
    "antagonist",
    "antonym",
    "fun",
    "function",
    "factory",
    "trie",
    "trigger",
    "trigonometry",
    "tripod",
]
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact


def f(prefix):
    if prefix != "":
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print("\n".join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print("")


interact(f, prefix="")
