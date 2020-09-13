"""
Suppose you have a linked list where the value of each node is a sorted linked list (i.e., it is a nested list).

Your task is to flatten this nested list—that is, to combine all nested lists into a single (sorted) linked list.
"""

# User defined class
class Node:
    def __init__(
        self, value
    ):  # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({str(self.value)})"


# User defined class
class LinkedList:
    def __init__(
        self, head
    ):  # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    """
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    """

    def append(self, value):
        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return

        # Create a temporary Node object
        node = self.head

        # Iterate till the end of the current LinkedList
        while node.next is not None:
            node = node.next

        # Append the newly created Node at the end of the current LinkedList
        node.next = Node(value)

    """We will need this function to convert a LinkedList object into a Python list of integers"""

    def to_list(self):
        out = []  # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object

        while node:  # <-- Iterate until we have nodes available
            # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            out.append(int(str(node.value)))
            node = node.next

        return out


# my solution - note, doesn't handle none
def merge(list1, list2):
    """
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    """
    holding = list1.to_list()
    [holding.append(i) for i in list2.to_list()]
    # for i in list2.to_list():
    #     holding.append(i)
    holding = sorted(holding)

    output = LinkedList(Node(holding[0]))
    for i in holding[1:]:
        output.append(i)
    return output


# udacity solution, expects both linked lists to be sorted
def udacity_merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged


""" In a NESTED LinkedList object, each node will be a simple LinkedList in itself"""


class NestedLinkedList(LinkedList):
    def flatten(self):
        """
        My solution, first attempted on a simple nested linked list with two known nodes
        However, getting unexpected attribute errors
            >> nested_linked_list.head
            output: <__main__.LinkedList object at 0x7fc8173623d0>
            >> nested_linked_list.head.to_list()
            output: AttributeError: 'Node' object has no attribute 'to_list'

        This is due to when we create the NestedLinkedList class, we pass a linkedlist as a node
        But still confused by error
        """
        return merge(self.head.value, self.head.next.value)


# First Test scenario
""" Create a simple LinkedList"""
linked_list = LinkedList(
    Node(1)
)  # <-- Notice that we are passing a Node made up of an integer
# <-- Notice that we are passing a numerical value as an argument in the append() function here
linked_list.append(3)
linked_list.append(5)

""" Create another simple LinkedList"""
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

expected_list = [1, 2, 3, 4, 5]  # <-- Python list

# Convert the "solution" into a Python list and compare with another Python list
assert merge(linked_list, second_linked_list).to_list() == expected_list

""" Create a NESTED LinkedList, where each node will be a simple LinkedList in itself"""
nested_linked_list = NestedLinkedList(
    Node(linked_list)
)  # <-- Notice that we are passing a Node made up of a simple LinkedList object
nested_linked_list.append(
    second_linked_list
)  # <-- Notice that we are passing a LinkedList object in the append() function here


# --------------------------------------

""" In a NESTED LinkedList object, each node will be a simple LinkedList in itself"""


class udacity_NestedLinkedList(LinkedList):
    def flatten(self):
        # <-- self.head is a node for NestedLinkedList
        return self._flatten(self.head)

    """  A recursive function """

    def _flatten(self, node):

        # A termination condition
        if node.next is None:
            # <-- First argument is a simple LinkedList
            return merge(node.value, None)

        # _flatten() is calling itself untill a termination condition is achieved
        # <-- Both arguments are a simple LinkedList each
        return merge(node.value, self._flatten(node.next))
