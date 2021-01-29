"""
Problem Statement:
    Given an input array and a target value (integer), 
    find two values in the array whose sum is equal to the target value. 
    
    Solve the problem without using extra space. 
    You can assume the array has unique values 
    and will never have more than one solution.
"""
from typing import List


def pair_sum(arr: List[int], target: int) -> List[int]:
    arr.sort()

    # initialize two pointer - one from start of the array and other from the end
    front_index = 0
    back_index = len(arr) - 1

    # shift the pointers
    while front_index < back_index:
        front = arr[front_index]
        back = arr[back_index]

        if front + back == target:
            return [front, back]
        elif front + back < target:  # sum < target ==> shift front pointer forward
            front_index += 1
        else:
            back_index -= 1  # sum > target ==> shift back pointer backward

    return [None, None]


assert pair_sum([2, 7, 11, 15], 9) == [2, 7]
assert pair_sum([0, 8, 5, 7, 9], 9) == [0, 9]
assert pair_sum([110, 9, 89], 9) == [None, None]
