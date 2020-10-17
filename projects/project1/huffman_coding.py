"""
A data compression algorithm reduces the amount of memory (bits) required to represent a message (data)

The sender encodes the data, and the receiver decodes the encoded data.

A data compression algorithm could be either lossy or lossless,
    meaning that when compressing the data,
    there is a loss (lossy) or
    no loss (lossless) of information

The Huffman Coding is a lossless data compression algorithm.

We will have two phases in encoding
    1. building the Huffman tree (a binary tree)
    2. generating the encoded data.

A Huffman tree is built in a bottom-up approach.
* determine the frequency of each character in the message
* build and sort a list of nodes in the order lowest to highest frequencies
* need our list to work as a priority queue, 
    where a node that has lower frequency should have a higher priority to be popped-out
* pop-out two nodes with the minimum frequency from the priority queue
* create a new node with a frequency equal to the sum of the two nodes
    This new node would become an internal node in the Huffman tree, 
    and the two nodes would become the children
    the lower frequency node becomes a left child, 
    and the higher frequency node becomes the right child
* reinsert the newly created node back into the priority queue
* repeat until there is a single element left in the priority queue

"""
