"""
Given an array arr and a target element target, 
find the last index of occurrence of target in arr using recursion. 
If target is not present in arr, return -1.

For example:

For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 5, output = 6

For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 7, output = -1
"""
from typing import List

def last_index(arr: List[int], target: int) -> int:
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    """
    if target not in arr:
        return -1
    
    else:
        rev_arr = arr[:][::-1]
        location = len(arr) - 1
        if rev_arr[0] == target:
            return location
        else:
            location -= 1
            # need the return
            return last_index(arr[slice(0, len(arr) - 1)], target)

    return location