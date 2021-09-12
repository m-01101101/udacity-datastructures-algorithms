"""Iterative and recursive solutions to perform breadth first search on a tree"""
from collections import deque
from config import Node, Tree, State
from typing import List

# in breadth first search, we walk down the tree one level at a time
# start at the root, visit the left
q = deque()


class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, value):
        self.q.appendleft(value)

    def dequeue(self):
        return self.q.pop() if len(self.q) > 0 else None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) <= 0:
            return "<queue is empty>"

        s = "<enqueue here>\n_________________\n"
        s += "\n_________________\n".join(str(item) for item in self.q)
        s += "\n_________________\n<dequeue here>"
        return s


# BFS algorithm
# TODO - double check this works
def bfs(tree: Tree) -> List[str]:
    """Return items in tree, following pre-order traversal"""
    visit_order = []
    q = Queue()
    node = tree.get_root()

    while node:
        if node.has_left_child():
            q.enqueue(node.get_left_child())
        if node.has_right_child():
            q.enqueue(node.get_right_child())

        visit_order.append(node)
        node = q.dequeue()

    return visit_order


fruit_tree = Tree("apple")
fruit_tree.get_root().set_left_child("banana")
fruit_tree.get_root().set_right_child("cherry")
fruit_tree.get_root().get_left_child().set_left_child("dates")

order_of_fruits = bfs(fruit_tree)
