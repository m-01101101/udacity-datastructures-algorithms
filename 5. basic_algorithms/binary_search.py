import copy
import math
from typing import List

# iterative solution
def binary_search(array: List, target: int) -> int:
    """binary search algorithm using iteration

    args:
      array: must be ascending sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    """
    attempt = start_index = 0
    end_index = len(array) - 1
    max_attempts = round(math.log(len(array), 2))

    while attempt <= max_attempts:  # alternative, while start_index <= end_index
        attempt += 1
        idx = (start_index + end_index) // 2

        if array[idx] == target:
            return idx

        elif array[idx] < target:
            start_index = idx  # search second half of the list, set mid as lower limit
            # start_index = idx + 1

        elif array[idx] > target:
            end_index = idx  # search first half of the list, set mid as upper limit
            # end_index = idx - 1

    return -1


# recursive solution
def binary_search_recursive(array, target):
    """binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    """
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


def binary_search_recursive_soln(array, target, start_index, end_index):
    idx = (start_index + end_index) // 2

    if array[idx] == target:
        return idx

    elif start_index > end_index or start_index == end_index == 0:
        return -1

    elif array[idx] < target:
        binary_search_recursive_soln(array, target, idx, end_index)

    elif array[idx] > target:
        binary_search_recursive_soln(array, target, start_index, idx)


def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    centre = (len(source) - 1) // 2
    if source[centre] == target:
        return centre
    elif source[centre] < target:
        return recursive_binary_search(target, source[centre + 1 :], left + centre + 1)
    else:
        return recursive_binary_search(target, source[:centre], left)


multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
assert recursive_binary_search(7, multiple) == 5

"""
** variation 1 **
both these functions return the index of an element provided

but it might not be helpful if there are multiple instances of the target

we might want to find the first instance
"""


def find_first(target, source):
    output = []
    temp = copy.deepcopy(source)
    for i in range(len(temp)):
        idx = recursive_binary_search(target, temp)
        if idx:  # equiv is not None
            output.append(idx)  # + i?
            temp.pop(idx)
    return None if len(output) == 0 else min(output)


# better approach
def _find_first(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index - 1] == target:
            index -= 1
        else:
            return index


assert find_first(7, multiple) == 3
assert find_first(9, multiple) == None

"""
** variation 2 **
a function that returns a boolean value indicating whether an element is present, 

but with no information about the location of that element
"""


def contains(target, source):
    return True if recursive_binary_search(target, source) is not None else False


letters = ["a", "c", "d", "f", "g"]
assert contains("a", letters) == True
assert contains("b", letters) == False

"""
** variation 3 **
given a sorted array that may have duplicate values, 
use binary search to find the first and last indexes of a given value

arr = [0, 1, 2, 2, 3, 3, 3, 4, 5, 6]
target = 3
answer = [4, 6]

The expected complexity of the problem is O(log(n))
"""


def _find_first(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return -1
    while source[index] == target:
        if index == 0:
            return 0
        if source[index - 1] == target:
            index -= 1
        else:
            return index


def _find_last(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return -1
    while source[index] == target:
        if index == 0:
            return 0
        if source[index + 1] == target:
            index += 1
        else:
            return index


def first_and_last_index(target, source):
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """
    return [idx for idx in (_find_first(target, source), _find_last(target, source))]


def test_first_list(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(number, input_list)
    return output == solution


input_list = [1]
number = 1
solution = [0, 0]
print(solution, first_and_last_index(number, input_list))
# test_case_1 = [number, input_list, solution]
# assert test_first_list(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
print(solution, first_and_last_index(number, input_list))
# test_case_2 = [number, input_list, solution]
# assert test_first_list(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
print(solution, first_and_last_index(number, input_list))
# test_case_3 = [number, input_list, solution]
# assert test_first_list(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
print(solution, first_and_last_index(number, input_list))
# test_case_4 = [number, input_list, solution]
# assert test_first_list(test_case_4)
