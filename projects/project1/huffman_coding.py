"""
A data compression algorithm reduces the amount of memory (bits) required to represent a message (data)

The compressed data, in turn, helps to reduce the transmission time from a sender to receiver

The sender encodes the data, and the receiver decodes the encoded data.

A data compression algorithm could be either lossy or lossless,
    meaning that when compressing the data,
    there is a loss (lossy) or
    no loss (lossless) of information

The Huffman Coding is a lossless data compression algorithm.

We will have two phases in encoding
    1. building the Huffman tree (a binary tree)
    2. generating the encoded data.

Phase 1 - Build the Huffman Tree
A Huffman tree is built in a bottom-up approach.
* determine the frequency of each character in the message
* build and sort a list of nodes in the order lowest to highest frequencies
    each node represents a single character
    build and sort a list of nodes
* need our list to work as a priority queue,
    where a node that has lower frequency should have a higher priority to be popped-out
    tip: use a min-heap instead of a list
* pop-out two nodes with the minimum frequency from the priority queue
* create a new node with a frequency equal to the sum of the two nodes
    This new node would become an internal node in the Huffman tree,
    the two nodes would become the children
    the lower frequency node becomes a left child, 
    and the higher frequency node becomes the right child
* reinsert the newly created node back into the priority queue
    a min-heap will be a better choice due to lower complexity of sort the elements every time there is an insertion
* repeat until there is a single element left in the priority queue

Phase 2 - Generate the Encoded Data
* generate unique binary code for each character of our string message
* for this purpose, you'd have to traverse the path from root to the leaf node
* the binary code is shorter for the more frequent character, and vice-versa
    frequency 2: code 000
    frequency 3: code 001
    frequency 7: code 11

Phase 2 - Decoded the Data
(1) delcare a blank decoded string
(2) pick a bit from the encoded data, traversing from left to right
(3) start traversing the Huffman tree from the root
    if the current bit of encoded data is 0, move to the left child, 
    if the current bit is 1 move to the right child of the tree
    if a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string
(4) repeat (2) and (3) until the encoded data is completely traversed    
"""

"""
use the template provided

you will need to create the sizing schemas to present a summary
"""
# import heapq  # python implemention of a min-heap
import sys
from collections import Counter

# creating a min-heap from scratch

class Node:
    def __init__(self, char=None, freq=None):
        self.char: str = char
        self.freq: int = freq
        self.left: Node = None
        self.right: Node = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.char}, {self.freq})"

    def __lt__(self, other):  # implementation of less than <
        return self.freq < other.freq

    def __gt__(self, other):  # implementation of greater than >
        return self.freq > other.freq


class MinHeap:
    def __init__(self, root: int=None):
        self.root = Node(root)

    def build_heap(self, data):
        encoded_data = Counter(data)
        self.arr = [Node(char=letter, freq=encoded_data[letter]) for letter in encoded_data]


def huffman_encoding(data):
    return encoded_data, tree


def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


message = 'AAAAAAABBBCCCCCCCDDEEEEEE'
