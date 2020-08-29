"""
Problem Statement

Given a linked list, swap the two nodes present at position `i` and `j`, 
assuming `0 <= i <= j`.
The positions are based on 0-based indexing.

Note: You have to swap the nodes and not just the values. 

Example:
* `linked_list = 3 4 5 2 6 1 9`
* `positions = 2 5`
* `output = 3 4 1 2 6 5 9`

**Explanation:** 
* The node at position 3 has the value `2`
* The node at position 4 has the value `6`
* Swapping these nodes will result in a final order of nodes of `3 4 5 6 2 1 9`
"""

class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None

"""
Approach
As it's a linked list i need to consider how adjacent nodes handle this
"""

"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped

TODO: complete this function and swap nodes present at position_one and position_two
Do not create a new linked list
"""
def swap_nodes(head, left_index, right_index):
    pass