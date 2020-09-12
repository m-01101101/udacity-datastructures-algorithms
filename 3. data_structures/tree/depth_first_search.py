"""Iterative and recursive solutions to perform depth first search on a tree"""
from config import Node, Tree, State
from typing import List


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


def pre_order_traversal_with_stack(tree: Tree) -> List[str]:
    """Return items in tree, following pre-order traversal"""
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    state = State(node)

    stack.push(state)  # adding the state class, rather than the node
    visit_order.append(node.get_value())

    while node:  # while node() -> node is not callable, while(node) == while not none
        if node.has_left_child() and not state.visited_left:
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.visited_right:
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)
            # node already in the stack as we check left first
            # so no need to push to stack

        else:
            # retrace steps, remove the last element in the stack
            # reset the state and node to element at the top of the stack
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    return visit_order


fruit_tree = Tree("apple")
fruit_tree.get_root().set_left_child("banana")
fruit_tree.get_root().set_right_child("cherry")
fruit_tree.get_root().get_left_child().set_left_child("dates")

order_of_fruits = pre_order_traversal_with_stack(fruit_tree)


def pre_order_traversal_with_recursion(tree: Tree) -> List[str]:
    """Return items in tree, following pre-order traversal"""
    visit_order = list()

    def recursive_logic(node):  # define the recursive logic, left first

        if node != None:
            visit_order.append(node.value)
            recursive_logic(node.get_left_child())
            recursive_logic(node.get_right_child())

    recursive_logic(tree.get_root())

    return visit_order


# def post_order_traversal_with_stack(tree: Tree) -> List[str]:
#     """Return items in tree, following pre-order traversal"""
# ['dates', 'banana', 'cherry', 'apple']


def post_order_traversal_with_recursion(tree: Tree) -> List[str]:
    """Return items in tree, following pre-order traversal"""
    visit_order = list()

    def recursive_logic(node):  # post order, go to the leaf before appending

        if node != None:
            recursive_logic(node.get_left_child())
            recursive_logic(node.get_right_child())
            visit_order.append(node.value)

    recursive_logic(tree.get_root())

    return visit_order
