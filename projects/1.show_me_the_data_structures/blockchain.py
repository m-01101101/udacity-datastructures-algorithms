"""
A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to the other blocks in the chain.
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.
For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.
"""
import hashlib
import time
from typing import List


# (2) the block
class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calc_hash(data)
        # self.next_block = None  # had to implement a direct link between blocks

    # Three core elements of the blockchain
    # (1) the information hash - we do this for information we want to store
    def _calc_hash(self, data) -> str:
        sha = hashlib.sha256()
        sha.update(str(data).encode("utf-8"))
        return sha.hexdigest()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.hash} @ {self.timestamp}\nPrevious Hash: {self.previous_hash}\n)"


# (3) chaining or linking the blocks together
# implement a linked list
class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        block = self.head
        while block:
            yield block.data
            block = block.next_block

    def append(self, data):
        ts = time.gmtime()
        if self.head is None:
            self.head = self.tail = Block(ts, data, None)  # genesis block
        elif self.tail is None:
            self.tail = Block(ts, data, self.head)
        else:
            new_block = Block(ts, data, self.tail)
            self.tail = new_block

        self.size += 1

    def size(self) -> int:
        return self.size

    def to_list(self) -> List[Block]:
        output = set()
        block = self.tail
        while block:
            output.add(block)
            block = block.previous_hash
        return list(output)


blockchain = BlockChain()

blockchain.append(18476)
blockchain.append(759694)
blockchain.append(68794)

print(blockchain.to_list())
