"""Walking through the process of breadth first search of a tree"""
from config import Node, Tree
from collections import deque

fruit_tree = Tree("apple")
fruit_tree.get_root().set_left_child("banana")
fruit_tree.get_root().set_right_child("cherry")
fruit_tree.get_root().get_left_child().set_left_child("dates")

# we need a queue rather than a stack to keep order
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
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


visit_order = list()
q = Queue()

# start at the root
node = fruit_tree.get_root()
visit_order.append(node)

print(
    f"""
visit order: {visit_order}
stack:
{q}
"""
)

# notice, two ifs, not elif as we must check both children
if node.has_left_child():
    q.enqueue(node.get_left_child())
if node.has_right_child():
    q.enqueue(node.get_right_child())

# set the left child as node and add to the list
node = q.dequeue()  # node is now banana
visit_order.append(node)  # visit banana

print(
    f"""
visit order: {visit_order}
stack:
{q}
"""
)

# check if the current node has any children
if node.has_left_child():
    q.enqueue(node.get_left_child())
if node.has_right_child():
    q.enqueue(node.get_right_child())

# we're now dequeueing the element at the same level as the node we just checked
node = q.dequeue()  # node is now cherry
visit_order.append(node)  # visit cherry

print(
    f"""
visit order: {visit_order}
stack:
{q}
"""
)

# we now check if it has children
if node.has_left_child():
    q.enqueue(node.get_left_child())
if node.has_right_child():
    q.enqueue(node.get_right_child())

node = q.dequeue()  # node is now dates
visit_order.append(node)  # visit dates

print(
    f"""
visit order: {visit_order}
stack:
{q}
"""
)

# date is a leaf so these won't execute
if node.has_left_child():
    q.enqueue(node.get_left_child())
if node.has_right_child():
    q.enqueue(node.get_right_child())

print(
    f"""
visit order: {visit_order}
stack:
{q}
"""
)
