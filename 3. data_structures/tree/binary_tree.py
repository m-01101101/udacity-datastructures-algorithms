"""Defining a class for a binary tree

Constraints: a node can only ever have two children at most

Assume that duplicates are overwritten by the new node that is to be inserted.
    - Other options are to keep a counter of duplicate nodes
    - Or to keep a list of duplicates nodes with the same value.
"""

from config import Node


class BinaryTree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    def insert_with_loop(self, new_value):
        node = self.get_root()
        if node == None:
            return self.set_root(new_value)
        elif node.get_value() == new_value:
            # change the value, not the node itself
            # in order to maintain node's relationships
            return node.set_value(new_value)
        else:
            while node:
                if node.left == None:
                    return node.set_left_child(new_value)
                elif node.right == None:
                    return node.set_right_child(new_value)

                node = (
                    node.get_left_child()
                    if node.left != None
                    else node.get_right_child()
                )

    def insert_with_recursion(self, value):
        node = self.root()
        if node == None:
            return self.set_root(value)

        def add_recursively(node):
            if node == None:
                node.set_value(Node(value))
                # add_recursively(node.get_left_child())
                # add_recursively(node.get_right_child())
                # node.set_value(Node(add_recursively(node.get_left_child())))
                # node.set_value(Node(add_recursively(node.get_right_child())))

        node = node.get_left_child() if node.left == None else node.get_right_child()
        add_recursively(node)

    def __repr__(self):
        if self.get_root() == None:
            return "Tree is empty"

        else:
            to_print = []
            level = 0
            node = self.get_root()
            to_print.append((level, node))
            while node:
                level += 1
                if node.has_left_child():
                    to_print.append((level, node.get_left_child()))
                if node.has_right_child():
                    to_print.append((level, node.get_right_child()))

                if node.has_left_child():
                    node = node.get_left_child()
                elif node.has_right_child():
                    node = node.get_right_child()
                else:
                    node = None
        s = "Tree is made up of the following nodes:"  # TODO use rich or pprint
        previous_level = -1
        for i in range(len(to_print)):
            level, node = to_print[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


tree = BinaryTree()
tree.insert_with_loop(5)
tree.insert_with_loop(6)
tree.insert_with_loop(4)
tree.insert_with_loop(2)
tree.insert_with_loop(5)

tree = BinaryTree()
# tree.insert_with_recursion(5)
# tree.insert_with_recursion(6)
# tree.insert_with_recursion(4)
# tree.insert_with_recursion(2)
# tree.insert_with_recursion(5)
