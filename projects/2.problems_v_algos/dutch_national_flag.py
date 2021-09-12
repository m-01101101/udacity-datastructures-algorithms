"""Given an input array consisting on only 0, 1, and 2, 
sort the array in a single traversal

You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. 
For e.g. if you traverse the array twice, that would still be an O(n)
    but it will not count as single traversal
"""
from typing import List


def sort_012(input_list: List[int]) -> List[int]:
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    L0 = []
    L1 = []
    L2 = list()

    for e in input_list:
        if e == 0:
            L0.append(e)
        elif e == 1:
            L1.append(e)
        elif e == 2:
            L2.append(e)

    return L0 + L1 + L2


# test cases
test1 = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test2 = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test3 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

# edge cases
test4 = [0, 0, 0, 0, 0]
test5 = []

assert sort_012(test1) == sorted(test1)
assert sort_012(test2) == sorted(test2)
assert sort_012(test3) == sorted(test3)
assert sort_012(test4) == sorted(test4)
assert sort_012(test5) == []


#------------------------------------------------#
# more efficient approach provided with guidance #

# Utility function to swap elements `A[i]` and `A[j]` in the list
def swap(A, i, j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Linear time partition routine to sort a list containing 0, 1, and 2.
# It is similar to 3–way partitioning for the Dutch national flag problem.
def threeWayPartition(A, end):

    start = mid = 0
    pivot = 1

    while mid <= end:
        if A[mid] < pivot:    # current element is 0
            swap(A, start, mid)
            start = start + 1
            mid = mid + 1
        elif A[mid] > pivot: # current element is 2
            swap(A, mid, end)
            end = end - 1
        else:                # current element is 1
            mid = mid + 1
