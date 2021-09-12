from typing import List


def mergesort(arr: List[int]) -> List[int]:
    """implementation of merge sort algorithm"""

    if len(arr) <= 1:
        return arr

    mid_point = len(arr) // 2
    left = arr[:mid_point]
    right = arr[mid_point:]

    left = mergesort(left)
    right = mergesort(right)

    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """takes two sorted lists and merges them"""
    merged = []
    left_idx = right_idx = 0

    # move through the lists until we have exhausted one
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            merged.append(right[right_idx])
            right_idx += 1
        else:
            merged.append(left[left_idx])
            left_idx += 1

    """
    Append any leftovers. Because we've broken from our while loop,
    we know at least one is empty, and the remaining:
    a) are already sorted
    b) all sort past our last element in merged
    """
    merged += left[left_idx:]
    merged += right[right_idx:]

    return merged


test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]

assert mergesort(test_list_1) == [0, 1, 2, 3, 7, 8, 10]
assert mergesort(test_list_2) == [0, 1]
assert mergesort(test_list_3) == [97, 98, 99]
