"""
In this exercise you are going to apply what you learned about stacks with a real world problem. 

We will be using stacks to make sure the parentheses are balanced in mathematical expressions such as: 
((3^2 + 8)*(5/2))/(2+6)

In real life you can see this extend to many things such as text editor plugins 
    and interactive development environments for all sorts of bracket completion checks. 

Take a string as an input and return `True` if it's parentheses are balanced or `False` if it is not. 
"""
from typing import List


class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """

    opening_parenthesis = Stack()
    closing_parenthesis = Stack()

    for _ in equation:
        if _ == "(":
            opening_parenthesis.push(_)
        elif _ == ")":
            closing_parenthesis.push(_)

    return opening_parenthesis.size() == closing_parenthesis.size()


def _equation_checker(equation):
    """
    Check equation for balanced parentheses
    """

    # not in the the spirit
    return equation.count("(") == equation.count(")")


def udacity_equation_checker(equation):
    stack = Stack()

    for char in equation:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.pop() == None:
                return False

    return stack.size() == 0
