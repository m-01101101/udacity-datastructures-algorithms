"""
You have been given an array containg numbers.
Find and return the largest sum in a contiguous subarray within the input array.

arr = [1, 2, 3, -4, 6]
The largest sum is `8`, which is the sum of all elements of the array.

arr = [1, 2, -5, -4, 1, 6]
The largest sum is `7`, which is the sum of the last two elements of the array.
"""

from typing import List

def max_sum_subarray(arr: List[int]) -> int:
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    running_total = []
    total = sum(arr)
    for i in arr:
        if sum(arr[:i]):
            running_total.append(i)

