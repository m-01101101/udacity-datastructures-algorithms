"""
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search.
If found in the array return its index, otherwise return -1.

assume there are no duplicates in the array
your algorithm's runtime complexity must be in the order of O(log n)
"""
from typing import List


def binary_search_recursive(arr: List[int], target: int, left: int, right: int) -> int:
    """Recursively searches sorted array"""
    if left > right:
        return -1

    idx = (left + right) // 2

    if arr[idx] == target:
        return idx

    move_left = binary_search_recursive(arr, target, left, idx - 1)
    move_right = binary_search_recursive(arr, target, idx + 1, right)

    return max(move_left, move_right)  # one side might return -1


def rotated_array_search(arr: List[int], target: int) -> int:
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(array): Input array to search
       number (int): target to search
    Returns:
       int: Index or -1
    """
    return binary_search_recursive(arr=arr, target=target, left=0, right=len(arr) - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


# test cases
t1 = ([6, 7, 8, 9, 10, 1, 2, 3, 4], 6)
t2 = ([6, 7, 8, 9, 10, 1, 2, 3, 4], 1)
t3 = ([6, 7, 8, 1, 2, 3, 4], 8)
t4 = ([6, 7, 8, 1, 2, 3, 4], 1)
t5 = ([6, 7, 8, 1, 2, 3, 4], 10)

# edge cases
t6 = ([1], 0)
t7 = ([], -1)

for test_case in [t1, t2, t3, t4, t5, t6, t7]:
    assert linear_search(test_case[0], test_case[1]) == rotated_array_search(
        test_case[0], test_case[1]
    )
