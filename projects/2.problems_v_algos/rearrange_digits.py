"""
Rearrange Array Elements so as to form two numbers that provide the maximum sum
Return these two numbers.
You can assume that all array elements are in the range [0, 9].
The number of digits in both the numbers cannot differ by more than 1. 
You're not allowed to use any sorting function that Python provides
The expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42].
"""
import heapq
import math
from typing import List


def rearrange_digits(input_list: List[int]) -> List[int]:
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 1:
        return input_list

    heapq._heapify_max(input_list)
    out1 = out2 = ""

    for _ in range(len(input_list) // 2):
        out1 += str(heapq._heappop_max(input_list))
        out2 += str(heapq._heappop_max(input_list))

    if input_list:
        out1 += str(heapq._heappop_max(input_list))

    return [int(out1), int(out2)]


# test cases
test1 = [[1, 2, 3, 4, 5], [531, 42]]
test2 = [[4, 6, 2, 5, 9, 8], [964, 852]]

# edge cases
test3 = [[1], [1]]
test4 = [[1, 1], [1, 1]]
test5 = [[6, 6, 6, 6, 6, 6, 6], [6666, 666]]
test6 = [[], []]

assert rearrange_digits(test1[0]) == test1[1]
assert rearrange_digits(test2[0]) == test2[1]
assert rearrange_digits(test3[0]) == test3[1]
assert rearrange_digits(test4[0]) == test4[1]
assert rearrange_digits(test5[0]) == test5[1]
assert rearrange_digits(test6[0]) == test6[1]
