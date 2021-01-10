"""
fill out the union and intersection functions

The union of two sets A and B is the set of elements which are in A, in B, or in both A and B
    i.e. all elements from both sets, Python pipe operator |
The intersection of two sets A and B, denoted by A ∩ B, 
    is the set of all objects that are members of both the sets A and B
    Python sets uses & operator

take in two linked lists
return a linked list that is composed of either the union or intersection
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """Combines all elements of two Linked Lists"""
    temp_list = llist_1.to_list() + llist_2.to_list()

    ll_union = LinkedList()
    for i in temp_list:
        ll_union.append(i)

    return ll_union


def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """Returns a Linked List with the values present in both Linked Lists"""
    a = llist_1.to_list()
    b = llist_2.to_list()

    temp_set = set(x for x in a if x in b)

    ll_union = LinkedList()
    for i in temp_set:
        ll_union.append(i)

    return ll_union


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
