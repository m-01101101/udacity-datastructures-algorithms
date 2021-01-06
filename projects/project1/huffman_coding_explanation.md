# Explanation for Huffman Coding

- I initalise two versions of the same `HuffmanEncoder` class. This is perhaps inefficient but felt more elegant.
- I use Python's built in min heap implementation `heapq`, it was simplest way to merge nodes successfully. The only other approach I could think of was to have created a separate class specifically for merging the nodes, but this felt unnecessary as Python comes with "batteries included".

## Time complexity

- Linear Big O when creating a frequency dictionary using `Counter`
- Linear Big O converting the dictionary into a list of Nodes
- Recursion
- Time complexity when encoding, and decoding having to work up and down the tree
