"""Defining a class for a binary tree

Constraints: a node can only ever have two children at most

Assume that duplicates are overwritten by the new node that is to be inserted.
    - Other options are to keep a counter of duplicate nodes
    - Or to keep a list of duplicates nodes with the same value.
"""

from config import Node

# TODO compare with
# https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/binary_search_tree.py
# https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/binary_search_tree_recursive.py
class BinaryTree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        The comparison operator is used for traversing the tree.
        Determine the criteria that would make you go left versus right.
        0: new_node == node
        -1: new node < existing node
        1: new node > existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1  # traverse
        else:
            return 1

    def insert_with_loop(self, new_value):
        # logic assumes working with integers
        # change comparison operator if new criteria required
        # adds to the right if larger than existing node, even if left available
        node = self.get_root()
        if node == None:
            self.set_root(new_value)
            return

        else:
            new_node = Node(new_value)
            inserted = False

            while not inserted:
                comparison = self.compare(node, new_node)  # 0 equals match
                if comparison == 0:
                    # change the value, not the node itself
                    # in order to maintain node's relationships
                    node.set_value(new_value)
                    inserted = True
                elif comparison == -1:
                    if node.left != None:
                        node = node.get_left_child()
                    else:
                        node.set_left_child(new_value)
                        inserted = True
                elif comparison == 1:
                    if node.right != None:
                        node = node.get_right_child()
                    else:
                        node.set_right_child(new_value)
                        inserted = True

    def insert_with_recursion(self, value):
        # recursive fills up left first
        # it does not use the comparison operator
        if self.get_root() == None:
            return self.set_root(value)
        elif self.get_root().get_value() == value:
            return self.get_root().set_value(value)
        else:
            node = self.get_root()

        def add_recursively(node):
            if node.left == None:
                node = node.set_left_child(value)
            elif node.get_left_child().get_value() == value:
                node = node.get_left_child().set_value(value)
            elif node.right == None:
                node = node.set_right_child(value)
            elif node.get_right_child().get_value() == value:
                node = node.get_right_child().set_value(value)
            else:
                add_recursively(node.get_left_child())

        add_recursively(node)

    def search(self, value):
        # https://www.geeksforgeeks.org/insert-a-node-in-binary-search-tree-iteratively/
        """takes a value, and returns true if a node containing that value exists in the tree, otherwise false"""
        if value == self.get_root().get_value():
            return True
        else:
            # TODO fix so that logic can handle left being not None and right being None
            # try except? or would that get me in an infinite loop?
            node_left = self.get_root().get_left_child()
            node_right = self.get_root().get_right_child()
            while node_left or node_right:
                if node_left.get_value() == value:
                    return True
                if node_right.get_value() == value:
                    return True
                node_left = node_left.get_left_child()
                node_right = node_right.get_right_child()
            return False

    # TODO - add delete functions
    # https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
    # https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/binary_search_tree.py
    # https://www.youtube.com/watch?time_continue=15&v=fJlWvaqqeZg&feature=emb_logo

    def __repr__(self):
        # TODO print "<empty>" for each node's children
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


tree_loop = BinaryTree()
tree_loop.insert_with_loop(5)
tree_loop.insert_with_loop(6)
tree_loop.insert_with_loop(4)
tree_loop.insert_with_loop(2)
tree_loop.insert_with_loop(5)

tree_recur = BinaryTree()
tree_recur.insert_with_recursion(5)
tree_recur.insert_with_recursion(6)
tree_recur.insert_with_recursion(4)
tree_recur.insert_with_recursion(2)
tree_recur.insert_with_recursion(5)


"""
can't handle duplicates in later nodes

def insert_with_loop(self, new_value):
        node = self.get_root()
        if node == None:
            return self.set_root(new_value)
        elif node.get_value() == new_value:
            # change the value in order to maintain node's relationships
            return node.set_value(new_value)
        else:
            while node:
                if node.left == None:
                    return node.set_left_child(new_value)
                elif node.right == None:
                    return node.set_right_child(new_value)
                
                node = node.get_left_child() if node.get_left_child() != None else node.get_right_child()


depending on the value of the comparison, node could get added right when left is None

def insert_with_loop(self, new_value):
    node = self.get_root()
    if node == None:
        self.set_root(new_value)
        return

    else:
        new_node = Node(new_value)
        inserted = False

        while not inserted:
            comparison = self.compare(node, new_node)  # 0 equals match
            if comparison == 0:
                # change the value, not the node itself
                # in order to maintain node's relationships
                node.set_value(new_value)
                inserted = True
            elif comparison == 1:
                if node.left != None:
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_value)
                    inserted = True

            elif comparison == -1:
                if node.right != None:
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_value)
                    inserted = True
"""
