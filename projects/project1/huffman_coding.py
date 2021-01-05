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

you will need to create the sizing schemas to present a summary
"""
import heapq  # python implemention of a min-heap
import sys
from collections import Counter
from typing import List


class Node:
    def __init__(self, char=None, freq=None):
        self.char: str = char
        self.freq: int = freq
        self.left: Node = None
        self.right: Node = None

    def __gt__(self, other):
        if not isinstance(other, Node):
            return -1
        return self.freq > other.freq

    def __repr__(self):
        return f"{self.__class__.__name__}({self.char}, {self.freq})"


def merge_nodes(node1: Node, node2: Node) -> Node:
    """
    Combines the frequency of two nodes and makes them leafs nodes
    """
    output_node = Node(None, node1.freq + node2.freq)

    if node2.freq >= node1.freq:
        output_node.right = node2
        output_node.left = node1
    else:
        output_node.right = node1
        output_node.left = node2

    return output_node



class HuffmanEncoder():
    def __init__(self, data: str):
        enc_data = Counter(data)
        arr = [Node(char=letter, freq=enc_data[letter]) for letter in enc_data]
        arr = sorted(arr, key=lambda x: x.freq)  # might need to change
        self.frequency_list = arr

        if len(arr) == 1:
            node = heapq.heappop(arr)
            huffman_node = Node(None, node.freq)
            huffman_node.left = node
            heapq.heappush(arr, huffman_node)

        while len(arr) > 1:
            node1 = arr.pop(0)
            node2 = arr.pop(0)

            huffman_node = merge_nodes(node1, node2)

            heapq.heappush(arr, huffman_node)

        self.root = arr[0]

    def generate_codes(self):
        if self.root.left is None and self.root.right is None:
            return {self.root.char: "O"}

        return self.code_recursive(self.root, "")

    def code_recursive(self, root, current_code):
        codes = {}

        if root is None:
            return {}

        if root.char is not None:
            codes[root.char] = current_code

        codes.update(self.code_recursive(root.left, current_code + "0"))
        codes.update(self.code_recursive(root.right, current_code + "1"))

        return codes

    def encode(self, data):
        encoded_text = ""
        codes = self.generate_codes()

        for char in data:
            encoded_text += codes[char]
        return encoded_text

    def decode(self, encoded_data: str, tree) -> str:
        decoded_text = ""

        current_node = tree

        for char in encoded_data:
            if char == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.char is not None:
                decoded_text += current_node.char
                current_node = tree
        return decoded_text


def huffman_encoding(data: str) -> (str, HuffmanEncoder):
    encoder = HuffmanEncoder(data)

    return encoder.encode(data), encoder.root


def huffman_decoding(data: str, tree: Node) -> (str):
    encoder = HuffmanEncoder(data)

    return encoder.decode(data, tree)


if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))

    assert a_great_sentence == decoded_data
