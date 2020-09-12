from typing import Type


class Node:
    def __init__(self, value=None):
        self.value: str = value  # using strings in this example
        self.left: Node = None
        self.right: Node = None

    def set_value(self, value: str):
        self.value = value

    def get_value(self) -> str:
        return self.value

    def set_left_child(self, value: str):
        self.left = Node(value)

    def set_right_child(self, value: str):
        self.right = Node(value)

    def get_left_child(self):  #  -> Type[Node]
        return self.left

    def get_right_child(self):  #  -> Type[Node]
        return self.right

    def has_left_child(self) -> bool:
        return self.left != None

    def has_right_child(self) -> bool:
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_value()})"


class Tree:
    def __init__(self, root: str = None):
        self.root = Node(root)

    def get_root(self):
        return self.root

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


class State(object):
    def __init__(self, node: Type[Node]):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self) -> Type[Node]:
        return self.node

    def set_visited_left(self):
        """Set visited left child to True"""
        self.visited_left = True

    def set_visited_right(self):
        """Set visited right child to True"""
        self.visited_right = True

    def __repr__(self):
        s = f"""{self.node}
        visited_left = {self.visited_left}
        visited_right = {self.visited_right}
        """
        return s
