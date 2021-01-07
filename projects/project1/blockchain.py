"""
A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to the other blocks in the chain.
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.
For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.
"""
import hashlib
from typing import List


# Three core elements of the blockchain
# (1) the information hash - we do this for information we want to store
def calc_hash(self):
    sha = hashlib.sha256()
    hash_str = "We are going to encode this string of data!".encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()


# (2) the block
class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next_hash = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.hash})"


# (3) chaining or linking the blocks together
# implement a linked list
class BlockChain:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, block: Block):
        if self.head is None:
            self.head = block
            self.size += 1
        else:
            idx = self.head

            # the following logic does not deal with a clash
            # say two blocks had the same previous hash
            # this would overwrite the existing
            while idx.hash != block.previous_hash:
                idx = idx.next_hash

            idx.next_hash = block.hash
            self.size += 1
