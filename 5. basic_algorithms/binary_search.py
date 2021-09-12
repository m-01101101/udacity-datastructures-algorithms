import math
from typing import List, Tuple

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

    elif start_index > end_index:
        return -1

    elif array[idx] < target:
        return binary_search_recursive_soln(
            array, target, idx + 1, end_index
        )  # must increment otherwise stuck in recursive loop for values greater than the largest value

    elif array[idx] > target:
        return binary_search_recursive_soln(
            array, target, start_index, idx - 1
        )  # must increment otherwise stuck in recursive loop for small values


test_list = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
assert binary_search_recursive(test_list, 7) == 5
assert binary_search_recursive(test_list, 3) == 1
assert binary_search_recursive(test_list, 2) == -1
assert binary_search_recursive(test_list, 15) == 11
assert binary_search_recursive(test_list, 23) == -1


def recursive_binary_search(array, target, left=0):
    if len(array) == 0:
        return -1

    idx = (len(array) - 1) // 2
    if array[idx] == target:
        return idx + left
    elif array[idx] < target:
        return recursive_binary_search(
            array[idx + 1 :], target, left + idx + 1
        )  # search right side
    elif array[idx] > target:
        return recursive_binary_search(array[:idx], target, left)  # search left side


multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
assert recursive_binary_search(multiple, 7) == 5
assert recursive_binary_search(multiple, 3) == 1
assert recursive_binary_search(multiple, 2) == -1
assert recursive_binary_search(multiple, 15) == 11
assert recursive_binary_search(multiple, 23) == -1

"""
** variation 1 **
both these functions return the index of an element provided

but it might not be helpful if there are multiple instances of the target

we might want to find the first instance
"""


def _find_first(array, target):
    index = recursive_binary_search(array, target)
    if index == -1:
        return -1
    while array[index] == target:
        if index == 0:
            return 0
        if array[index - 1] == target:
            index -= 1
        else:
            return index


assert _find_first(multiple, 7) == 3
assert _find_first(multiple, 9) == -1
assert _find_first(multiple, 2) == -1
test_list1 = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15, 22, 22]
assert _find_first(test_list1, 22) == 12


# replication if _find_last but increments by +1
def _find_last(array, target):
    index = recursive_binary_search(array, target)
    if index == -1:
        return -1
    while array[index] == target:
        if index == 0:
            return 0
        elif index == len(array) - 1 or array[index + 1] != target:  # added to handle IndexError
            return index
        else:
            index += 1


assert _find_last(multiple, 7) == 5
assert _find_last(multiple, 9) == -1
assert _find_last(multiple, 2) == -1
assert _find_last(test_list1, 22) == 13


"""
** variation 2 **
a function that returns a boolean value indicating whether an element is present, 

but with no information about the location of that element
"""


def contains(array, target):
    return recursive_binary_search(array, target) != -1


letters = ["a", "c", "d", "f", "g"]
assert contains(letters, "a") == True
assert contains(letters, "b") == False

"""
** variation 3 **
given a sorted array that may have duplicate values, 
use binary search to find the first and last indexes of a given value

arr = [0, 1, 2, 2, 3, 3, 3, 4, 5, 6]
target = 3
answer = [4, 6]

The expected complexity of the problem is O(log(n))
"""


def first_and_last_index(array, target) -> Tuple[int, int]:
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a tuple containing the first and last indexes of the given value
    """
    return (_find_first(array, target), _find_last(array, target))


def test_first_list(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    return output == solution


input_list = [1]
number = 1
solution = (0, 0)
test_case_1 = [input_list, number, solution]
assert test_first_list(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = (3, 6)
test_case_2 = [input_list, number, solution]
assert test_first_list(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = (5, 5)
test_case_3 = [input_list, number, solution]
assert test_first_list(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = (-1, -1)
test_case_4 = [input_list, number, solution]
assert test_first_list(test_case_4)
