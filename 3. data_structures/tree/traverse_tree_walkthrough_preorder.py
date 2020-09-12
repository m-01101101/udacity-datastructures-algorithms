"""Walking through the process of pre-order traversal of a binary tree"""
from config import Node, Tree

fruit_tree = Tree("apple")
fruit_tree.get_root().set_left_child("banana")
fruit_tree.get_root().set_right_child("cherry")
fruit_tree.get_root().get_left_child().set_left_child("dates")

# define a stack to keep track of the order of nodes we visit
class Stack:
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        return self.list[-1] if len(self.list) > 0 else None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):  # print the values in list in reverse order
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s

        else:
            return "<stack is empty>"


visit_order = list()
stack = Stack()

# start at the root
node = fruit_tree.get_root()
stack.push(node)
visit_order.append(node.get_value())

print(
    f"""
visit order: {visit_order}
stack:
{stack}
"""
)  # we've visited "apple"

# check if "apple" has any left children
if node.has_left_child():
    node = node.get_left_child()  # change the value of the current node
    stack.push(node)
    visit_order.append(node.get_value())

print(
    f"""
visit order: {visit_order}
stack:
{stack}
"""
)  # we've now visited "banana"

# check if "banana" has any left children
if node.has_left_child():
    node = node.get_left_child()  # change the value of the current node
    stack.push(node)
    visit_order.append(node.get_value())

print(
    f"""
visit order: {visit_order}
stack:
{stack}
"""
)  # we've now visited "dates"

# check if "dates" has any left children
if node.has_left_child():
    node = node.get_left_child()  # change the value of the current node
    stack.push(node)
    visit_order.append(node.get_value())
# it doesn't, so check to see if it has any right children
elif node.has_right_child():
    node = node.get_right_child()  # change the value of the current node
    stack.push(node)
    visit_order.append(node.get_value())
# it doesn't so we need to retrace our steps and move back up the tree
# remove "dates" from our stack
else:
    stack.pop()

print(
    f"""
visit order: {visit_order}
stack:
{stack}
"""
)  # we've now removed "dates" from out stack

# set the current node to the head of the stack
# this is the parent of the node we just visited
node = stack.top()
# we've already checked if the node has a left, now check right
if node.has_right_child():
    node = node.get_right_child()
    stack.push(node)
    visit_order.append(node.get_value())
# it doesn't so we pop and reset
else:
    stack.pop()

print(
    f"""
visit order: {visit_order}
stack:
{stack}
"""
)  # we've now removed "banana" from out stack

# we continue checking until the stack is empty
# you can see we could be using a while loop
node = stack.top()

if node.has_right_child():
    node = node.get_right_child()
    stack.push(node)
    visit_order.append(node.get_value())
# now we're back the the root
# this does have a right child

print(
    f"""
visit order: {visit_order}
stack:
{stack}
"""
)  # we've now visited "cherry"

# we've check if cherry has any children
if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)
    visit_order.append(node.get_value())
elif node.has_right_child():
    node = node.get_right_child()
    stack.push(node)
    visit_order.append(node.get_value())
else:
    # it doesn't so we'll remove it from our stack
    stack.pop()

node = stack.top()  # we're now back at the root
stack.pop()
print(
    f"""
visit order: {visit_order}
stack:
{stack}
"""
)
