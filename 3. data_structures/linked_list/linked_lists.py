from typing import List


class Node:
    def __init__(self, value):
        self.value = value  # date we want to assign to the node
        self.next = None  # ref to next node in the list


head = Node(2)  # 2 is the value we want to hold

# adding a new element
new_node = Node(1)  # we initialise the new node
head.next = new_node  # we must store the new node as a ref to the previous node

head.next = Node(1)  # really we should do it in one step


def traverse_linkedlist(head: Node) -> Node:
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


def create_linked_list(input_list):
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)
        else:
            # Move to the tail (the last node)
            current_node = head
            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(value)
    return head


# a more efficient solution
def create_linked_list_better(input_list):
    head = None
    tail = None

    for value in input_list:
        if head is None:
            head = Node(value)
            tail = (
                head  # when we only have 1 node, head and tail refer to the same node
            )
        else:
            # attach the new node to the `next` of tail
            tail.next = Node(value)
            tail = tail.next  # update the tail
    return head


class LinkedList:
    def __init__(self, init_list: List = None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    # ----------------------------------------------------#

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        if self.head is None:
            self.head = Node(value)
        else:
            previous_head = self.head
            self.head = Node(value)
            self.head.next = previous_head

    # ----------------------------------------------------#

    def append(self, value):
        """ Append a value to the end of the list. """
        position_tail = self.head

        if position_tail is None:
            self.head = Node(value)

        else:
            while position_tail.next:  # Moving to the end of the list
                position_tail = position_tail.next

            position_tail.next = Node(value)

    # ----------------------------------------------------#

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return None

        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

        raise ValueError("Value not found in the list.")

        return None

    # ----------------------------------------------------#

    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        raise ValueError("Value not found in the list.")

    # ----------------------------------------------------#

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        first_node = self.head
        self.head = self.head.next
        return first_node.value

    # ----------------------------------------------------#

    def insert(self, value, pos):
        """Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list."""
        # If the list is empty
        if self.head is None:
            self.head = Node(value)
            return

        if pos == 0:
            self.prepend(value)
            return

        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return

            index += 1
            node = node.next
        else:
            self.append(value)

    # ----------------------------------------------------#

    def size(self):
        """ Return the size or length of the linked list. """
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    # ----------------------------------------------------#

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


if __name__ == "__main__":
    # Test prepend
    linked_list = LinkedList()
    linked_list.prepend(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    linked_list.prepend(2)
    assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

    # Test append
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

    # Test search
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(3)
    assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
    assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

    # Test remove
    linked_list.remove(1)
    assert linked_list.to_list() == [
        2,
        1,
        3,
        4,
        3,
    ], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [
        2,
        1,
        4,
        3,
    ], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

    # Test pop
    value = linked_list.pop()
    assert value == 2, f"list contents: {linked_list.to_list()}"
    assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

    # Test insert
    linked_list.insert(5, 0)
    assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(2, 1)
    assert linked_list.to_list() == [
        5,
        2,
        1,
        4,
    ], f"list contents: {linked_list.to_list()}"
    linked_list.insert(3, 6)
    assert linked_list.to_list() == [
        5,
        2,
        1,
        4,
        3,
    ], f"list contents: {linked_list.to_list()}"

    # Test size
    assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"
