"""
Given an input string consisting of only `{` and `}`, figure out the minimum number of reversals required to make the brackets balanced.

For example:
* For `input_string = "}}}}`, the number of reversals required is `2`.


* For `input_string = "}{}}`, the number of reversals required is `1`.


If the brackets cannot be balanced, return `-1` to indicate that it is not possible to balance them.
"""

# count appearance of '{' and '}'
# if sum if odd return -1
# calculate number of reversals needed


def _minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of bracket reversals needed
    """
    # this is technically write,
    # however the task is looking for the bracket to follow one another {}
    # not if there are the same amount in each
    a = input_string.count("{")
    b = input_string.count("}")

    if (a + b) % 2 != 0:
        return -1
    else:
        return abs((a - b) / 2)


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def udacity_minimum_bracket_reversals(input_string):
    if len(input_string) % 2 == 1:
        return -1

    stack = Stack()
    count = 0
    for bracket in input_string:
        if not stack.is_empty():
            top = stack.top()
            if top != bracket and top == "{":
                stack.pop()
                continue
        stack.push(bracket)
    ls = []
    while not stack.is_empty():
        first = stack.pop()
        second = stack.pop()
        ls.append(first)
        ls.append(second)
        if first == "}" and second == "}":
            count += 1
        elif first == "{" and second == "}":
            count += 2
        elif first == "{" and second == "{":
            count += 1
    return count
